#!/usr/bin/env python3
"""
Development server runner
Use this for testing locally, NOT for production
"""

from app import app
import os

if __name__ == '__main__':
    print("=" * 60)
    print("Starting Flask Development Server")
    print("=" * 60)
    print("Access the application at: http://YOUR_DROPLET_IP:5000")
    print("Press CTRL+C to stop the server")
    print("=" * 60)
    
    app.run(
        host='0.0.0.0',  # Listen on all interfaces
        port=5000,
        debug=True  # Enable debug mode for development
    )