#!/usr/bin/env python3
"""
Test script to verify Flask application is properly configured
"""

import sys
from app import app, DASHBOARDS

def test_app():
    print("=" * 60)
    print("Flask Application Configuration Test")
    print("=" * 60)
    
    # Test 1: App exists
    print("\n1. Testing Flask app initialization...")
    if app:
        print("   ✓ Flask app initialized successfully")
    else:
        print("   ✗ Flask app initialization failed")
        sys.exit(1)
    
    # Test 2: Routes exist
    print("\n2. Testing routes...")
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    expected_routes = ['/', '/inference', '/training', '/about']
    
    for route in expected_routes:
        if route in routes:
            print(f"   ✓ Route '{route}' found")
        else:
            print(f"   ✗ Route '{route}' missing")
    
    # Test 3: Dashboard configuration
    print("\n3. Testing dashboard configuration...")
    if 'inference' in DASHBOARDS and 'training' in DASHBOARDS:
        print("   ✓ Both dashboards configured")
        print(f"   - Inference: {DASHBOARDS['inference']['title']}")
        print(f"   - Training: {DASHBOARDS['training']['title']}")
    else:
        print("   ✗ Dashboard configuration incomplete")
    
    # Test 4: Configuration
    print("\n4. Testing app configuration...")
    if app.config.get('SECRET_KEY'):
        print("   ✓ SECRET_KEY is set")
    else:
        print("   ⚠ SECRET_KEY is not set (using default)")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

if __name__ == '__main__':
    test_app()