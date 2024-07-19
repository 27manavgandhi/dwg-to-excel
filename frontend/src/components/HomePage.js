import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-800 text-white">
            <h1 className="text-4xl">DWG to DXF Converter</h1>
            <Link to="/upload" className="mt-4 text-blue-400 hover:underline">Go to Upload Page</Link>
        </div>
    );
};

export default HomePage;
