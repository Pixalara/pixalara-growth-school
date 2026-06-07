// Immediate Theme initialization to prevent layout flash
(function() {
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', initialTheme);
})();

document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle Functionality
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        const icon = themeToggleBtn.querySelector('i');
        
        // Set correct initial icon
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'dark') {
            icon.classList.replace('fa-moon', 'fa-sun');
        }

        themeToggleBtn.addEventListener('click', () => {
            const activeTheme = document.documentElement.getAttribute('data-theme');
            let newTheme = 'light';
            
            if (activeTheme === 'light') {
                newTheme = 'dark';
                icon.classList.replace('fa-moon', 'fa-sun');
            } else {
                icon.classList.replace('fa-sun', 'fa-moon');
            }
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    // Mobile Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            hamburger.classList.toggle('open');
        });
    }

    // Smooth Scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                navMenu.classList.remove('active');
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Auto-open enrollment popup
    setTimeout(() => {
        const bookingModal = document.getElementById('bookingModal');
        if (bookingModal && !sessionStorage.getItem('enrollmentPopupShown')) {
            bookingModal.classList.add('open');
            sessionStorage.setItem('enrollmentPopupShown', 'true');
        }
    }, 3000);
});

/* --- TAB SWITCHING LOGIC --- */
function openModule(evt, moduleName) {
    // 1. Hide all tab content
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tabcontent[i].classList.remove("active-content");
    }

    // 2. Remove "active" class from all buttons
    tablinks = document.getElementsByClassName("tab-btn");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // 3. Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(moduleName).style.display = "block";
    // Add small delay for animation class
    setTimeout(() => {
        document.getElementById(moduleName).classList.add("active-content");
    }, 10);
    
    evt.currentTarget.className += " active";
}

// Optional: Open the first tab by default when page loads
document.addEventListener('DOMContentLoaded', () => {
    // Find the first tab button in any syllabus container and click it
    const firstTab = document.querySelector('.tab-btn');
    if(firstTab) {
        firstTab.click();
    }
});

/* --- INTERACTIVE SYLLABUS ACCORDION --- */
function toggleModule(element) {
    // 1. Close all other modules
    const allModules = document.querySelectorAll('.module-card');
    
    allModules.forEach(card => {
        if (card !== element && card.classList.contains('active')) {
            card.classList.remove('active');
            card.querySelector('.module-body').style.maxHeight = null;
        }
    });

    // 2. Toggle the clicked module
    element.classList.toggle('active');
    
    // 3. Handle Smooth Height Animation
    const body = element.querySelector('.module-body');
    if (body.style.maxHeight) {
        body.style.maxHeight = null; // Close
    } else {
        body.style.maxHeight = body.scrollHeight + "px"; // Open to full height
    }
}

/* --- MODAL LOGIC --- */
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('open');
        document.body.style.overflow = 'hidden'; // Stop background scrolling
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = 'auto'; // Restore scrolling
    }
}

// Close modal if Esc key is pressed
document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
        const openModals = document.querySelectorAll('.modal-overlay.open');
        openModals.forEach(modal => {
            modal.classList.remove('open');
            document.body.style.overflow = 'auto';
        });
    }
});

/* --- MODAL LOGIC --- */
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('open');
        document.body.style.overflow = 'hidden'; // Stop background scrolling
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = 'auto'; // Restore scrolling
    }
}

// Close modal if Esc key is pressed
document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
        const openModals = document.querySelectorAll('.modal-overlay.open');
        openModals.forEach(modal => {
            modal.classList.remove('open');
            document.body.style.overflow = 'auto';
        });
    }
});

/* --- SCROLL REVEAL ANIMATION --- */
window.addEventListener('scroll', reveal);

function reveal() {
    var reveals = document.querySelectorAll('.reveal');

    for (var i = 0; i < reveals.length; i++) {
        var windowheight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealpoint = 100; // Trigger point

        if (revealtop < windowheight - revealpoint) {
            reveals[i].classList.add('active');
        }
    }
}

// Trigger once on load
reveal();