import React from 'react';
import { Link } from 'react-router-dom';

const ResultsPage = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-800 text-white">
            <h1 className="text-2xl">Processing Complete!</h1>
            <a href="http://localhost:5000/download" className="mt-4 px-4 py-2 bg-green-500 text-white">Download Excel File</a>
            <Link to="/" className="mt-4 text-blue-400 hover:underline">Back to Home</Link>
        </div>
    );
};

export default ResultsPage;
