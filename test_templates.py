#!/usr/bin/env python3
"""
Test Flask templates to ensure they render without errors
"""

from app import app

def test_templates():
    print("=" * 60)
    print("Testing Flask Templates")
    print("=" * 60)
    
    with app.test_client() as client:
        # Test home page
        print("\n1. Testing home page (/)...")
        response = client.get('/')
        if response.status_code == 200:
            print("   ✓ Home page renders successfully")
        else:
            print(f"   ✗ Home page failed: {response.status_code}")
        
        # Test inference page
        print("\n2. Testing inference page (/inference)...")
        response = client.get('/inference')
        if response.status_code == 200:
            print("   ✓ Inference page renders successfully")
        else:
            print(f"   ✗ Inference page failed: {response.status_code}")
        
        # Test training page
        print("\n3. Testing training page (/training)...")
        response = client.get('/training')
        if response.status_code == 200:
            print("   ✓ Training page renders successfully")
        else:
            print(f"   ✗ Training page failed: {response.status_code}")
        
        # Test about page
        print("\n4. Testing about page (/about)...")
        response = client.get('/about')
        if response.status_code == 200:
            print("   ✓ About page renders successfully")
        else:
            print(f"   ✗ About page failed: {response.status_code}")
        
        # Test 404 error
        print("\n5. Testing 404 error page...")
        response = client.get('/nonexistent-page')
        if response.status_code == 404:
            print("   ✓ 404 page works correctly")
        else:
            print(f"   ✗ 404 page failed: {response.status_code}")
    
    print("\n" + "=" * 60)
    print("Template testing completed!")
    print("=" * 60)

if __name__ == '__main__':
    test_templates()