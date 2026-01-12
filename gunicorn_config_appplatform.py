"""
Gunicorn configuration for DigitalOcean App Platform
"""

import multiprocessing
import os

# Server socket
bind = f"0.0.0.0:{os.getenv('PORT', '8080')}"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 2

# Logging
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = 'info'

# Process naming
proc_name = 'tableau_dashboard_app'

# Server mechanics
daemon = False