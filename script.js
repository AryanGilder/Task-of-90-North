// Function to toggle the visibility of the left menu
function toggleMenu() {
    const menu = document.getElementById("menu-items");
    menu.classList.toggle("hidden");
}

// Function to adjust page width based on screen size
function adjustPageWidth() {
    const width = window.innerWidth;
    const scale =
        width <= 600 ? 0.5 :
        width <= 700 ? 0.75 :
        width <= 767 ? 0.8 :
        width <= 1600 ? 0.9 : 1;

    document.body.style.transform = `scale(${scale})`;
}

// Add event listener for screen resizing
window.addEventListener("resize", adjustPageWidth);
adjustPageWidth();
