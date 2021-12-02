//header-navbar-start
window.addEventListener("scroll", function () {
    var nav = document.querySelector("nav");
    nav.classList.toggle("sticky", window.scrollY > 5);
})
//header-navbar-end

//main-about-pro-skills-start
const numb = document.querySelector(".numb");
let counter = 0;
setInterval(() => {
    if (counter == 100) {
        clearInterval();
    } else {
        counter += 1;
        numb.textContent = counter + "%";
    }
}, 80);
//main-about-pro-skills-end