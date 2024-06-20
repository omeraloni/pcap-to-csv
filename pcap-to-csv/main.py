import argparse
import scapy.all as scapy
import pandas as pd

def convert_pcap_to_csv(pcap_file, output_csv):
    # Load the pcap file
    packets = scapy.rdpcap(pcap_file)

    # Extract packet information
    packet_data = []

    for packet in packets:
        packet_info = {
            'time': packet.time,
            'src': packet[scapy.IP].src if scapy.IP in packet else None,
            'dst': packet[scapy.IP].dst if scapy.IP in packet else None,
            'srcport': packet[scapy.TCP].sport if scapy.TCP in packet else (packet[scapy.UDP].sport if scapy.UDP in packet else None),
            'dstport': packet[scapy.TCP].dport if scapy.TCP in packet else (packet[scapy.UDP].dport if scapy.UDP in packet else None),
            'protocol': packet[scapy.IP].proto if scapy.IP in packet else None
        }
        packet_data.append(packet_info)

    # Create a DataFrame and save it to a CSV file
    df = pd.DataFrame(packet_data)
    df.to_csv(output_csv, index=False)
    print(f"PCAP file converted to CSV and saved as {output_csv}")

def main():
    parser = argparse.ArgumentParser(description="Convert PCAP file to CSV")
    parser.add_argument("pcap_file", help="Path to the input PCAP file")
    parser.add_argument("output_csv", help="Path to the output CSV file")

    args = parser.parse_args()

    convert_pcap_to_csv(args.pcap_file, args.output_csv)

if __name__ == "__main__":
    main()
