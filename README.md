# PCAP to CSV Converter

This project provides a script to convert PCAP/PCAPNG files to CSV format.

## Features

- Convert PCAP/PCAPNG files to CSV format.
- Extract and store packet information such as time, source, destination, source port, destination port, and protocol.
- For TCP packets, extract and store TCP flags in a formatted list.

## Requirements

- Python 3.11 or higher
- Poetry
- tshark (part of Wireshark)

## Installation

1. **Install Poetry**:

    Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry.

2. **Install Wireshark and Tshark**:

    - **Ubuntu/Debian**:
      ```bash
      sudo apt-get update
      sudo apt-get install tshark
      ```

    - **macOS**:
      ```bash
      brew install wireshark
      ```

    - **Windows**:
      Download and install Wireshark from the [official website](https://www.wireshark.org/download.html). During the installation process, make sure to select the option to install `tshark`.

## Usage

1. **Install dependencies using Poetry**:

    ```bash
    poetry install
    ```

2. **Run the script**:

    You can run the script to convert the PCAP/PCAPNG file to CSV:

    ```bash
    poetry run pcap-to-csv path_to_your_pcap_file.pcapng output.csv
    ```

3. **Example**:

    ```bash
    poetry run pcap-to-csv example.pcapng output.csv
    ```

## CSV Output Example

After running the script, the CSV file will contain headers and data similar to the following:

| time                | src         | dst         | srcport | dstport | protocol | flags      |
|---------------------|-------------|-------------|---------|---------|----------|------------|
| 2023-07-12 14:30:01 | 192.168.1.2 | 192.168.1.1 | 12345   | 1502    | TCP      | SYN        |
| 2023-07-12 14:30:02 | 192.168.1.3 | 192.168.1.1 | 12346   | 1502    | TCP      | SYN; ACK   |
| 2023-07-12 14:30:03 | 192.168.1.4 | 192.168.1.1 | 12347   | 1502    | UDP      | None       |

## Development

To set up the project for development using Poetry:

1. **Install Poetry**:

    Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry.

2. **Install dependencies**:

    ```bash
    poetry install
    ```

3. **Run the script using Poetry**:

    ```bash
    poetry run pcap-to-csv path_to_your_pcap_file.pcapng output.csv
    ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License.
