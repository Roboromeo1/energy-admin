import pandas as pd
import matplotlib.pyplot as plt
import zlib
import bz2
import lzma
import numpy as np  # For generating sample data in the absence of real values

def try_decompress(data):
    """Attempt to decompress data using common compression algorithms."""
    decompressors = [
        ('No compression', lambda x: x),
        ('Zlib', zlib.decompress),
        ('BZ2', bz2.decompress),
        ('LZMA', lzma.decompress),
    ]
    
    for name, decompress in decompressors:
        try:
            decompressed_data = decompress(data)
            return name, decompressed_data
        except:
            continue
    return 'Unknown or unsupported compression', data

def read_file(file_path):
    """Read the entire content of a binary file."""
    with open(file_path, 'rb') as file:
        data = file.read()
        return data

def is_printable_ascii(byte_sequence):
    """Check if a byte sequence is printable ASCII."""
    try:
        return byte_sequence.decode('ascii').strip().isprintable()
    except UnicodeDecodeError:
        return False

def extract_printable_strings(data, min_length=4):
    """Extract sequences of printable ASCII characters from binary data."""
    printable_strings = []
    current_string = bytearray()
    
    for byte in data:
        if 32 <= byte <= 126:  # Range for printable ASCII characters
            current_string.append(byte)
        else:
            if len(current_string) >= min_length and is_printable_ascii(current_string):
                printable_strings.append(current_string.decode('ascii'))
                current_string = bytearray()
            elif len(current_string) > 0:
                current_string = bytearray()
    
    if len(current_string) >= min_length and is_printable_ascii(current_string):
        printable_strings.append(current_string.decode('ascii'))
    
    return printable_strings

def parse_data_to_df(printable_strings):
    """Parse extracted strings into a pandas DataFrame."""
    # Placeholder for actual data parsing logic
    # Assuming each string has a numeric value at the end for this example
    data = []
    for string in printable_strings:
        parts = string.split('_')
        if len(parts) >= 6:
            metric_type = parts[1]
            metric = parts[-3]
            channel = parts[-1]
            # Simulating a value extraction, replace with actual value extraction logic
            value = np.random.rand() * 100  # Placeholder for demonstration
            data.append([metric_type, metric, channel, value])
    df = pd.DataFrame(data, columns=['Type', 'Metric', 'Channel', 'Value'])
    return df

def visualize_data(df):
    """Visualize the DataFrame data with multiple types of plots."""
    # Metric Counts (Bar Chart)
    plt.figure(figsize=(10, 6))
    df['Metric'].value_counts().plot(kind='bar')
    plt.title('Metric Counts')
    plt.xlabel('Metric')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

    # Distribution of Values for a Metric (Histogram)
    plt.figure(figsize=(10, 6))
    # Filtering for QAVG metric as an example
    qavg_values = df[df['Metric'] == 'QAVG']['Value']
    plt.hist(qavg_values, bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of QAVG Values')
    plt.xlabel('QAVG Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # Assuming there are temporal values and channels are numeric for this example
    # Replace 'Channel' and 'Value' with actual time and value columns
    plt.figure(figsize=(10, 6))
    for channel in df['Channel'].unique():
        channel_df = df[df['Channel'] == channel]
        plt.plot(channel_df['Value'], label=f'Channel {channel}')  # Assuming 'Value' is temporal
    plt.title('Metric Value Over Time by Channel')
    plt.xlabel('Time')
    plt.ylabel('Metric Value')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main(file_path):
    data = read_file(file_path)
    compression, data_to_inspect = try_decompress(data)
    print(f"File appears to be using {compression}.")
    printable_strings = extract_printable_strings(data_to_inspect)
    df = parse_data_to_df(printable_strings)
    visualize_data(df)

# Ensure this path is correct
file_path = './INV.pqz'
main(file_path)
