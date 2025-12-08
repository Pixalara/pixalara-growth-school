document.addEventListener('DOMContentLoaded', () => {
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