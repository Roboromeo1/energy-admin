from flask import Flask, request, jsonify
import os
import tempfile
import pandas as pd
import zlib, bz2, lzma
import numpy as np

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    if file:
        # Save file to a temporary directory
        temp_dir = tempfile.mkdtemp()
        filepath = os.path.join(temp_dir, file.filename)
        file.save(filepath)

        # Process the file
        response_data = process_file(filepath)

        # Clean up the temporary file
        os.remove(filepath)
        os.rmdir(temp_dir)

        return jsonify(response_data), 200

def process_file(file_path):
    data = read_file(file_path)
    compression, data_to_inspect = try_decompress(data)
    printable_strings = extract_printable_strings(data_to_inspect)
    df = parse_data_to_df(printable_strings)
    result = visualize_data_to_json(df)
    return {
        'compression': compression,
        'summary': result
    }

# Placeholder for converting visualization to JSON-compatible format
def visualize_data_to_json(df):
    # Here we'll return a simple JSON with summary data
    return {
        'metric_counts': df['Metric'].value_counts().to_dict(),
        'channel_details': df.groupby('Channel')['Value'].describe().to_dict()
    }

if __name__ == '__main__':
    app.run(debug=True)
