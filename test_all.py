#!/usr/bin/env python3
"""
Comprehensive testing script for the application
Tests all routes, response codes, and content
"""

import sys
from app import app, DASHBOARDS

def test_all_routes():
    """Test all application routes"""
    print("=" * 70)
    print("COMPREHENSIVE APPLICATION TEST")
    print("=" * 70)
    
    test_results = {
        'passed': 0,
        'failed': 0,
        'total': 0
    }
    
    with app.test_client() as client:
        
        # Test 1: Home page
        print("\n[TEST 1] Home Page (/)...")
        test_results['total'] += 1
        response = client.get('/')
        if response.status_code == 200 and b'MLCommons' in response.data:
            print("   ✓ PASSED: Home page loads correctly")
            test_results['passed'] += 1
        else:
            print(f"   ✗ FAILED: Status {response.status_code}")
            test_results['failed'] += 1
        
        # Test 2: Inference dashboard
        print("\n[TEST 2] Inference Dashboard (/inference)...")
        test_results['total'] += 1
        response = client.get('/inference')
        if response.status_code == 200 and b'iframe' in response.data:
            print("   ✓ PASSED: Inference dashboard loads with iframe")
            test_results['passed'] += 1
        else:
            print(f"   ✗ FAILED: Status {response.status_code}")
            test_results['failed'] += 1
        
        # Test 3: Training dashboard
        print("\n[TEST 3] Training Dashboard (/training)...")
        test_results['total'] += 1
        response = client.get('/training')
        if response.status_code == 200 and b'iframe' in response.data:
            print("   ✓ PASSED: Training dashboard loads with iframe")
            test_results['passed'] += 1
        else:
            print(f"   ✗ FAILED: Status {response.status_code}")
            test_results['failed'] += 1
        
        # Test 4: About page
        print("\n[TEST 4] About Page (/about)...")
        test_results['total'] += 1
        response = client.get('/about')
        if response.status_code == 200 and b'MLCommons' in response.data:
            print("   ✓ PASSED: About page loads correctly")
            test_results['passed'] += 1
        else:
            print(f"   ✗ FAILED: Status {response.status_code}")
            test_results['failed'] += 1
        
        # Test 5: 404 Error
        print("\n[TEST 5] 404 Error Page...")
        test_results['total'] += 1
        response = client.get('/nonexistent')
        if response.status_code == 404:
            print("   ✓ PASSED: 404 page returns correct status")
            test_results['passed'] += 1
        else:
            print(f"   ✗ FAILED: Expected 404, got {response.status_code}")
            test_results['failed'] += 1
        
        # Test 6: CSS loads
        print("\n[TEST 6] Static CSS File...")
        test_results['total'] += 1
        response = client.get('/static/css/style.css')
        if response.status_code == 200:
            print("   ✓ PASSED: CSS file accessible")
            test_results['passed'] += 1
        else:
            print(f"   ✗ FAILED: CSS not found ({response.status_code})")
            test_results['failed'] += 1
        
        # Test 7: Dashboard URLs configured
        print("\n[TEST 7] Dashboard Configuration...")
        test_results['total'] += 1
        if ('inference' in DASHBOARDS and 
            'training' in DASHBOARDS and
            'embed_url' in DASHBOARDS['inference']):
            print("   ✓ PASSED: Dashboard configuration is complete")
            test_results['passed'] += 1
        else:
            print("   ✗ FAILED: Dashboard configuration incomplete")
            test_results['failed'] += 1
        
        # Test 8: Tableau URLs are valid format
        print("\n[TEST 8] Tableau Embed URLs...")
        test_results['total'] += 1
        inference_url = DASHBOARDS['inference']['embed_url']
        training_url = DASHBOARDS['training']['embed_url']
        
        if ('public.tableau.com/views/' in inference_url and
            'public.tableau.com/views/' in training_url):
            print("   ✓ PASSED: Tableau URLs are properly formatted")
            print(f"      - Inference: {inference_url[:60]}...")
            print(f"      - Training: {training_url[:60]}...")
            test_results['passed'] += 1
        else:
            print("   ✗ FAILED: Tableau URLs not properly formatted")
            test_results['failed'] += 1
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total Tests: {test_results['total']}")
    print(f"Passed: {test_results['passed']} ✓")
    print(f"Failed: {test_results['failed']} ✗")
    
    if test_results['failed'] == 0:
        print("\n🎉 ALL TESTS PASSED! Application is ready for deployment.")
        print("=" * 70)
        return 0
    else:
        print(f"\n⚠️  {test_results['failed']} test(s) failed. Please review errors above.")
        print("=" * 70)
        return 1

if __name__ == '__main__':
    sys.exit(test_all_routes())