import argparse
import pyshark
import pandas as pd

# Mapping of flag values to their names
TCP_FLAGS = {
    0x20: 'URG',
    0x10: 'ACK',
    0x08: 'PSH',
    0x04: 'RST',
    0x02: 'SYN',
    0x01: 'FIN'
}

def convert_flags_to_list(flags_hex):
    flags = int(flags_hex, 16)
    flag_list = [name for value, name in TCP_FLAGS.items() if flags & value]
    return '; '.join(flag_list) if flag_list else 'None'

def convert_pcap_to_csv(pcap_file, output_csv):
    # Load the pcap/pcapng file
    capture = pyshark.FileCapture(pcap_file)

    # Extract packet information
    packet_data = []

    for packet in capture:
        src_ip = packet.ip.src if hasattr(packet, 'ip') else None
        dst_ip = packet.ip.dst if hasattr(packet, 'ip') else None
        transport_layer = packet.transport_layer
        src_port = None
        dst_port = None
        flags = None

        if transport_layer:
            layer = getattr(packet, transport_layer.lower(), None)
            if layer:
                src_port = getattr(layer, 'srcport', None)
                dst_port = getattr(layer, 'dstport', None)
                if transport_layer == 'TCP' and hasattr(layer, 'flags'):
                    flags_hex = layer.flags
                    flags = convert_flags_to_list(flags_hex)

        packet_info = {
            'time': packet.sniff_time,
            'src': src_ip,
            'dst': dst_ip,
            'srcport': src_port,
            'dstport': dst_port,
            'protocol': transport_layer,
            'flags': flags
        }
        packet_data.append(packet_info)

    # Create a DataFrame and save it to a CSV file
    df = pd.DataFrame(packet_data)
    df.to_csv(output_csv, index=False)
    print(f"PCAP/PCAPNG file converted to CSV and saved as {output_csv}")

def main():
    parser = argparse.ArgumentParser(description="Convert PCAP/PCAPNG file to CSV")
    parser.add_argument("pcap_file", help="Path to the input PCAP/PCAPNG file")
    parser.add_argument("output_csv", help="Path to the output CSV file")

    args = parser.parse_args()

    convert_pcap_to_csv(args.pcap_file, args.output_csv)

if __name__ == "__main__":
    main()
