// static/js/main.js

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize any components that need JavaScript
    initAOS();
    initSmoothScrolling();
    initHeaderScroll();
    initBackToTop();
    initParallaxEffect();
    initMobileMenu();
    initContactForm();
    initCounters();
    initCursorEffect();
    initImageLoading();
});

// Initialize AOS (Animate On Scroll)
function initAOS() {
    // Check if AOS is available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,           // Duration in milliseconds
            easing: 'ease-out-cubic', // Easing function
            once: true,              // Animation will execute only once
            offset: 50,              // Offset (in pixels) from the trigger point
            delay: 50,               // Values from 0 to 3000, in 50ms steps
            mirror: false            // Whether animations should mirror on scroll up
        });
    }
}

// Initialize header with scroll effect
function initHeaderScroll() {
    const header = document.querySelector('.site-header');
    
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
        
        // Check initial scroll position
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        }
    }
}

// Initialize back to top button
function initBackToTop() {
    const backToTopBtn = document.getElementById('back-to-top');
    
    if (backToTopBtn) {
        // Show button when user scrolls down
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });
        
        // Click action to return to the top of the page
        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
}

// Parallax effect for images and background elements
function initParallaxEffect() {
    const parallaxElements = document.querySelectorAll('.parallax-element');
    
    if (parallaxElements.length > 0) {
        window.addEventListener('scroll', function() {
            const scrollY = window.scrollY;
            
            parallaxElements.forEach(element => {
                const speed = element.getAttribute('data-speed') || 0.2;
                const yPos = -(scrollY * speed);
                element.style.transform = `translateY(${yPos}px)`;
            });
        });
    }
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Get target element adjusted for sticky header
                const headerHeight = document.querySelector('.site-header')?.offsetHeight || 0;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL hash without triggering scroll
                history.pushState(null, null, targetId);
            }
        });
    });
}

// Initialize animate counters for statistics
function initCounters() {
    const counters = document.querySelectorAll('.counter');
    
    if (counters.length > 0) {
        const countUp = (counter, target) => {
            const count = +counter.innerText;
            const increment = target / 100;
            
            if (count < target) {
                counter.innerText = Math.ceil(count + increment);
                setTimeout(() => countUp(counter, target), 20);
            } else {
                counter.innerText = target;
            }
        };
        
        const handleCounterVisibility = () => {
            counters.forEach(counter => {
                const rect = counter.getBoundingClientRect();
                const isInViewport = (
                    rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 &&
                    rect.bottom >= 0
                );
                
                if (isInViewport && !counter.classList.contains('counted')) {
                    const target = +counter.getAttribute('data-target');
                    counter.classList.add('counted');
                    countUp(counter, target);
                }
            });
        };
        
        // Check initial visibility and add scroll listener
        handleCounterVisibility();
        window.addEventListener('scroll', handleCounterVisibility);
    }
}

// Special effect for cursor on certain elements
function initCursorEffect() {
    const cursorElements = document.querySelectorAll('.cursor-effect');
    
    cursorElements.forEach(element => {
        element.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            this.style.setProperty('--cursor-x', `${x}px`);
            this.style.setProperty('--cursor-y', `${y}px`);
        });
    });
}

// Image loading effect (lazy loading)
function initImageLoading() {
    // Add class for lazy loading effect to all images that are not loaded
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    images.forEach(img => {
        const parent = img.parentElement;
        if (!parent.classList.contains('img-loading')) {
            parent.classList.add('img-loading');
        }
        
        img.addEventListener('load', function() {
            parent.classList.remove('img-loading');
        });
    });
}

// Mobile menu functionality
function initMobileMenu() {
    const mobileMenuToggle = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (mobileMenuToggle && navbarCollapse) {
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInside = navbarCollapse.contains(event.target) || mobileMenuToggle.contains(event.target);
            
            if (!isClickInside && navbarCollapse.classList.contains('show')) {
                mobileMenuToggle.click();
            }
        });
        
        // Close menu when clicking on a nav link
        const navLinks = navbarCollapse.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (navbarCollapse.classList.contains('show')) {
                    mobileMenuToggle.click();
                }
            });
        });
        
        // Add animation effect to mobile menu opening
        mobileMenuToggle.addEventListener('click', function() {
            if (!navbarCollapse.classList.contains('show')) {
                setTimeout(() => {
                    const navItems = navbarCollapse.querySelectorAll('.nav-item');
                    navItems.forEach((item, index) => {
                        item.style.animationDelay = `${index * 0.1}s`;
                        item.classList.add('fade-in-right');
                    });
                }, 50);
            } else {
                const navItems = navbarCollapse.querySelectorAll('.nav-item');
                navItems.forEach(item => {
                    item.classList.remove('fade-in-right');
                });
            }
        });
    }
}

// Contact form validation and submission
function initContactForm() {
    const contactForm = document.getElementById('contact-form');
    
    if (contactForm) {
        // Add animation to inputs
        const formInputs = contactForm.querySelectorAll('input, textarea');
        formInputs.forEach(input => {
            // Animation when input gets focus
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('input-focused');
            });
            
            // Animation when input loses focus
            input.addEventListener('blur', function() {
                if (!this.value.trim()) {
                    this.parentElement.classList.remove('input-focused');
                }
            });
            
            // Check if input already has value (e.g., after page reload)
            if (input.value.trim()) {
                input.parentElement.classList.add('input-focused');
            }
        });
        
        // Form validation
        contactForm.addEventListener('submit', function(e) {
            let isValid = true;
            
            // Simple validation
            const requiredFields = contactForm.querySelectorAll('[required]');
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('is-invalid');
                    field.parentElement.classList.add('input-error');
                } else {
                    field.classList.remove('is-invalid');
                    field.parentElement.classList.remove('input-error');
                }
            });
            
            // Email validation
            const emailField = contactForm.querySelector('input[type="email"]');
            if (emailField && emailField.value) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(emailField.value)) {
                    isValid = false;
                    emailField.classList.add('is-invalid');
                    emailField.parentElement.classList.add('input-error');
                }
            }
            
            // Prevent form submission if validation fails
            if (!isValid) {
                e.preventDefault();
                
                // Animate scroll to first invalid field
                const firstInvalidField = contactForm.querySelector('.is-invalid');
                if (firstInvalidField) {
                    firstInvalidField.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                
                // Add shake effect to form
                contactForm.classList.add('form-error-shake');
                setTimeout(() => {
                    contactForm.classList.remove('form-error-shake');
                }, 500);
            } else {
                // Show loading animation during submission
                const submitButton = contactForm.querySelector('button[type="submit"]');
                if (submitButton) {
                    submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Submitting...';
                    submitButton.disabled = true;
                }
            }
        });
        
        // Clear validation styles on input
        formInputs.forEach(input => {
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    this.classList.remove('is-invalid');
                    this.parentElement.classList.remove('input-error');
                }
            });
        });
    }
}