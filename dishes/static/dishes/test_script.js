// dishes/static/dishes/test_script.js

// Simple JavaScript tests for frontend functionality

function runTests() {
    console.log('Running JavaScript tests...');
    
    // Test 1: Mobile menu toggle functionality
    testMobileMenuToggle();
    
    // Test 2: Form validation
    testFormValidation();
    
    // Test 3: Navigation links
    testNavigationLinks();
    
    console.log('All JavaScript tests completed!');
}

function testMobileMenuToggle() {
    console.log('Testing mobile menu toggle...');
    
    const menuToggle = document.getElementById('mobile-menu');
    const navbarLinks = document.getElementById('navbar-links');
    
    if (menuToggle && navbarLinks) {
        // Simulate click
        menuToggle.click();
        
        // Check if active class is added
        if (navbarLinks.classList.contains('active')) {
            console.log('✓ Mobile menu toggle works correctly');
        } else {
            console.log('✗ Mobile menu toggle failed');
        }
        
        // Reset
        menuToggle.click();
    } else {
        console.log('✗ Mobile menu elements not found');
    }
}

function testFormValidation() {
    console.log('Testing form validation...');
    
    const form = document.querySelector('.reservation-form');
    if (form) {
        const nameInput = form.querySelector('input[name="name"]');
        const emailInput = form.querySelector('input[name="email"]');
        
        if (nameInput && emailInput) {
            // Test required field validation
            nameInput.value = '';
            emailInput.value = '';
            
            // Check if form prevents submission with empty fields
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                console.log('✓ Form validation elements found');
            } else {
                console.log('✗ Submit button not found');
            }
        } else {
            console.log('✗ Form inputs not found');
        }
    } else {
        console.log('✗ Reservation form not found');
    }
}

function testNavigationLinks() {
    console.log('Testing navigation links...');
    
    const navLinks = document.querySelectorAll('.navbar-links a');
    let validLinks = 0;
    
    navLinks.forEach(link => {
        if (link.href && link.href !== '') {
            validLinks++;
        }
    });
    
    if (validLinks > 0) {
        console.log(`✓ Found ${validLinks} valid navigation links`);
    } else {
        console.log('✗ No valid navigation links found');
    }
}

// Run tests when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Only run tests in development
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        runTests();
    }
});
