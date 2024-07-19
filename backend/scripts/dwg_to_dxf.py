import os
import requests

def convert_dwg_to_dxf(dwg_path, api_key):
    file_url = f'file:///{os.path.abspath(dwg_path)}'  # Adjust if necessary
    response = requests.post(
        'https://sync.api.cloudconvert.com/v2/jobs',
        json={
            "tasks": {
                "import-my-file": {
                    "operation": "import/url",
                    "url": file_url
                },
                "convert-my-file": {
                    "operation": "convert",
                    "input": "import-my-file",
                    "input_format": "dwg",
                    "output_format": "dxf"
                },
                "export-my-file": {
                    "operation": "export/url",
                    "input": "convert-my-file"
                }
            },
            "redirect": False
        },
        headers={
            "Authorization": f"Bearer {api_key}"
        }
    )
    response.raise_for_status()
    return response.json()
