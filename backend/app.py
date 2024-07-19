from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
import requests
import traceback
from scripts.dwg_to_dxf import convert_dwg_to_dxf
from scripts.parse_dxf import parse_dxf
from scripts.excel_export import export_to_excel

app = Flask(__name__)
CORS(app)  # Enable CORS

# Environment Variables
CLOUDCONVERT_API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOGIzMDIxYzlhNTZmM2UwNGEwY2M1MjNjYWEzYWU1YjM2OTMwYmE5MmYwM2Q5YTExNTBiMDk5YWZhM2VmZGM2OGExZTE0NDkzOWI0MzczZDQiLCJpYXQiOjE3MjEzNTAzNDYuOTUzNTY0LCJuYmYiOjE3MjEzNTAzNDYuOTUzNTY1LCJleHAiOjQ4NzcwMjM5NDYuOTQ5NDM4LCJzdWIiOiI2OTAzNjkzNyIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsInByZXNldC5yZWFkIiwid2ViaG9vay5yZWFkIl19.ntmlKKqbPHklIw4x_8hiHnJU_vwE5pztmVOpgs64-MUxjd6hqdqQYhyoQ0U5KbiIPTa5z2Huv31FbLB8gROTr1Fe2if94cxqvhFiTBGVfPNy4H8-1NoqE94vwMpY5EmM9A2Eb46eD4KWONaJFdDpYmTkp6CXouaYpB6KN2JYnQiG3_WPxjeAjQEwy1z_NPgfXSjyy9D6izekrWb4y70yOFZO0iQLpnVQ4PSxDV3PioonineXFb8krST8agGItjLbmwkcTkIkyj6NGIrtnqYEu61KaH7JKEwszaSRX41HhK2YmIW9x3yRtemjIdOEfo39cA4dddfMZZghk4QUek__XqbffgCTIehbDUZPeWpJH-kowQz04fdFlv2fET7T28ZUJPI6PuvfSLllBEG3JsLB5zg1aVXvlcDHnbLFyvDnt-52RJQqH8YkgIQY4IAHlmXdhYeZRG3hmrhje7CvIi9NZT6vF4Kt5aYpPMf359tS6ZgIT7LY855ADhg6eabwwg_eAXho32Vh3R4-ZMDW0pyDzj4maCOAcqlRWGHJbIiQJ0nX1TOS_jIIA4ua-XenEXJ6pWvfVeQcsKMepDAwtTBRmlMjUNlN8A15wMtk57bJBgZKU2zdmp_v8Pc1fCEzgxYq5U00Fdyge77LPG5xCo-YJTQCez-_Za_zy1E9YtWUFbg'
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        # Convert DWG to DXF
        conversion_result = convert_dwg_to_dxf(file_path, CLOUDCONVERT_API_KEY)
        
        if 'data' not in conversion_result:
            return jsonify({'error': 'Invalid response from CloudConvert API', 'response': conversion_result}), 500
        
        dxf_url = conversion_result['data']['tasks']['export-my-file']['result']['files'][0]['url']

        # Download the DXF file
        dxf_response = requests.get(dxf_url)
        if dxf_response.status_code != 200:
            return jsonify({'error': 'Failed to download DXF file'}), 500
        
        dxf_file_path = os.path.join(UPLOAD_FOLDER, 'converted.dxf')
        with open(dxf_file_path, 'wb') as f:
            f.write(dxf_response.content)

        # Parse DXF file
        points = parse_dxf(dxf_file_path)

        # Export to Excel
        excel_path = os.path.join(RESULT_FOLDER, 'output.xlsx')
        export_to_excel(points, excel_path)

        return jsonify({'message': 'File processed successfully'}), 200
    except Exception as e:
        traceback.print_exc()  # Print the full traceback to the console
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['GET'])
def download_file():
    return send_file(os.path.join(RESULT_FOLDER, 'output.xlsx'), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
