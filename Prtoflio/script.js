// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 800,
    easing: 'slide',
    once: true,
    offset: 50
});

// Mobile Navigation
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener('click', () => {
    // Toggle Nav
    navLinks.classList.toggle("active");
    
    // Animate Links
    links.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = '';
        } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
        }
    });
    
    // Burger Animation
    hamburger.classList.toggle("toggle");
});

// Close mobile menu when link is clicked
links.forEach(link => {
    link.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            hamburger.classList.remove('toggle');
            links.forEach(l => l.style.animation = '');
        }
    });
});

// Navbar background change on scroll
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(22, 27, 34, 0.9)';
        navbar.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.5)';
        navbar.style.borderBottom = '1px solid rgba(88, 166, 255, 0.2)';
    } else {
        navbar.style.background = 'rgba(22, 27, 34, 0.6)';
        navbar.style.boxShadow = 'none';
        navbar.style.borderBottom = '1px solid rgba(255, 255, 255, 0.1)';
    }
});

// Typing Text Effect for Hero Section
const typingText = document.querySelector('.typing-text');
const phrases = [
    "Mechatronics Engineering Student",
    "Robotics Enthusiast",
    "Software Developer",
    "Tech Visionary"
];
let phraseIndex = 0;
let letterIndex = 0;
let currentPhrase = [];
let isDeleting = false;
let isEnd = false;

function loop() {
    isEnd = false;
    typingText.innerHTML = currentPhrase.join('') + '<span class="highlight">|</span>';

    if (phraseIndex < phrases.length) {

        if (!isDeleting && letterIndex <= phrases[phraseIndex].length) {
            currentPhrase.push(phrases[phraseIndex][letterIndex]);
            letterIndex++;
            typingText.innerHTML = currentPhrase.join('') + '<span class="highlight">|</span>';
        }

        if (isDeleting && letterIndex <= phrases[phraseIndex].length) {
            currentPhrase.pop();
            letterIndex--;
            typingText.innerHTML = currentPhrase.join('') + '<span class="highlight">|</span>';
        }

        if (letterIndex == phrases[phraseIndex].length) {
            isEnd = true;
            isDeleting = true;
        }

        if (isDeleting && letterIndex === 0) {
            currentPhrase = [];
            isDeleting = false;
            phraseIndex++;
            if (phraseIndex === phrases.length) {
                phraseIndex = 0;
            }
        }
    }
    
    // Timing logic
    const spedUp = Math.random() * (80 - 50) + 50;
    const normalSpeed = Math.random() * (200 - 100) + 100;
    const time = isEnd ? 2000 : isDeleting ? spedUp : normalSpeed;
    
    setTimeout(loop, time);
}

// Start typing effect when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // We already have HTML hardcoded so clear it and start typing
    typingText.innerHTML = '';
    setTimeout(loop, 1000); // 1s delay
});
