# DWG to DXF Tool

## Overview

This project provides a tool for converting DWG files to DXF, extracting data from DXF files, and exporting the data to Excel. The tool has a frontend built with React and a backend using Flask.

## Setup

### Frontend

1. Navigate to the `frontend` directory.
2. Run `npm install` to install dependencies.
3. Start the React app with `npm start`.

### Backend

1. Navigate to the `backend` directory.
2. Create a Python virtual environment with `python -m venv venv`.
3. Activate the environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
4. Install dependencies with `pip install -r requirements.txt`.
5. Run the Flask app with `python app.py`.

## API Endpoints

- `POST /upload`: Uploads a DWG file, converts it to DXF, parses it, and exports data to Excel.
- `GET /download`: Downloads the processed Excel file.

## Configuration

- Set your CloudConvert API key in `backend/app.py`.
