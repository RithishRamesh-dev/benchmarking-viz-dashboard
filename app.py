#!/usr/bin/env python3
"""
Tableau Dashboard Website
A Flask application to display Tableau Public dashboards
"""

from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'

# Tableau Public Dashboard URLs
# These are the embed URLs (not the viewing URLs)
DASHBOARDS = {
    'inference': {
        'title': 'MLCommons - Inference Datacenter',
        'embed_url': 'https://public.tableau.com/views/MLCommons-InferenceDatacenter/MLCommons-Inference',
        'description': 'Performance metrics and analysis for ML inference workloads in datacenter environments.'
    },
    'training': {
        'title': 'MLCommons - Training',
        'embed_url': 'https://public.tableau.com/views/MLCommons-Training_16993769118290/MLCommons-Training',
        'description': 'Training performance benchmarks and insights for machine learning models.'
    }
}


@app.route('/')
def index():
    """
    Home page - Landing page with links to all dashboards
    """
    return render_template('index.html', dashboards=DASHBOARDS)


@app.route('/inference')
def inference():
    """
    Inference Dashboard Page
    """
    dashboard = DASHBOARDS['inference']
    return render_template(
        'dashboard.html',
        title=dashboard['title'],
        embed_url=dashboard['embed_url'],
        description=dashboard['description']
    )


@app.route('/training')
def training():
    """
    Training Dashboard Page
    """
    dashboard = DASHBOARDS['training']
    return render_template(
        'dashboard.html',
        title=dashboard['title'],
        embed_url=dashboard['embed_url'],
        description=dashboard['description']
    )


@app.route('/about')
def about():
    """
    About page - Information about the dashboards and site
    """
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    """
    Custom 500 error handler
    """
    return render_template('500.html'), 500


# Context processor to make dashboards available in all templates
@app.context_processor
def inject_dashboards():
    """
    Make dashboard info available to all templates for navigation
    """
    return dict(dashboards=DASHBOARDS)


if __name__ == '__main__':
    # This is used for development only
    # In production (App Platform), Gunicorn is used automatically
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)