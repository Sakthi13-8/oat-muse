// ==========================
// Smooth scrolling
// ==========================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});


// ==========================
// Navbar sticky (SAFE)
// ==========================

const navbar = document.querySelector(".navbar");

if (navbar) {
    window.addEventListener("scroll", () => {
        if (window.scrollY > 80) {
            navbar.classList.add("sticky");
        } else {
            navbar.classList.remove("sticky");
        }
    });
}


// ==========================
// Section animation
// ==========================

document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll("section");

    if (sections.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                }
            });
        }, { threshold: 0.1 });

        sections.forEach(section => {
            section.classList.add("show"); 
            observer.observe(section);
        });
    }
});


// ==========================
// Form validation (SAFE)
// ==========================

const form = document.querySelector(".vertical-form");

if (form) {
    form.addEventListener("submit", (e) => {
        const inputs = form.querySelectorAll("input, textarea");
        let valid = true;

        inputs.forEach(input => {
            if (input.value.trim() === "") {
                valid = false;
            }
        });

        if (!valid) {
            e.preventDefault();
            alert("Please fill all the fields.");
        }
    });
}


// ==========================
// POPUP MODAL (SAFE)
// ==========================

const popup = document.getElementById("popup");
const popupTitle = document.getElementById("popupTitle");
const popupText = document.getElementById("popupText");
const popupClose = document.getElementById("popupClose");
const closeBtn = document.querySelector(".close-btn");

function openPopup(title, text) {
    if (!popup || !popupTitle || !popupText) return;

    popupTitle.innerText = title;
    popupText.innerText = text;
    popup.classList.add("show");
}

if (popupClose) {
    popupClose.onclick = () => popup.classList.remove("show");
}

if (closeBtn) {
    closeBtn.onclick = () => popup.classList.remove("show");
}

window.onclick = function (e) {
    if (popup && e.target == popup) {
        popup.classList.remove("show");
    }
};


// ==========================
// ABOUT BUTTONS (SAFE)
// ==========================

const ingredientsBtn = document.getElementById("ingredientsBtn");
if (ingredientsBtn) {
    ingredientsBtn.onclick = (e) => {
        e.preventDefault();
        openPopup(
            "Clean Ingredients",
            "Our skincare uses oat extracts, botanical oils and gentle actives..."
        );
    };
}

const formulaBtn = document.getElementById("formulaBtn");
if (formulaBtn) {
    formulaBtn.onclick = (e) => {
        e.preventDefault();
        openPopup(
            "Expert Formulas",
            "We combine nature and dermatological science..."
        );
    };
}

const educationBtn = document.getElementById("educationBtn");
if (educationBtn) {
    educationBtn.onclick = (e) => {
        e.preventDefault();
        openPopup(
            "Skin Education",
            "Learn how to build a simple skincare routine..."
        );
    };
}

const sustainableBtn = document.getElementById("sustainableBtn");
if (sustainableBtn) {
    sustainableBtn.onclick = (e) => {
        e.preventDefault();
        openPopup(
            "Sustainable Care",
            "Eco-friendly packaging and cruelty-free practices..."
        );
    };
}


// ==========================
// LOAD PRODUCTS (SAFE - SINGLE VERSION)
// ==========================

const container =
    document.querySelector(".products-container") ||
    document.getElementById("products-container");

if (container) {
    fetch("/api/products")
        .then(res => res.json())
        .then(products => {

            container.innerHTML = "";

            products.forEach(p => {
                container.innerHTML += `
                    <div class="product-card">
                        <img src="/static/images/${p.image}" alt="${p.name}">
                        <h3>${p.name}</h3>
                        <p>₹${p.price}</p>
                        <button onclick='addToCart(${JSON.stringify(p)})'>
                            Add to Cart
                        </button>
                    </div>
                `;
            });

        })
        .catch(err => console.log("Error loading products:", err));
}


// ==========================
// ADD TO CART
// ==========================

function addToCart(product) {
    fetch("/add-to-cart", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(product)
    })
    .then(res => res.json())
    .then(data => {
        alert(product.name + " added to cart!");
    })
    .catch(err => console.error(err));
}


// ==========================
// ABOUT TOGGLE
// ==========================

function toggleAbout() {
    const about = document.getElementById("aboutMore");
    if (!about) return;

    about.style.display =
        about.style.display === "block" ? "none" : "block";
}