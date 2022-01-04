var actionBtn = document.querySelector(".ChangerButtonEffect");
var changingTxt = document.querySelector(".MainBackgroundColor span");

actionBtn.addEventListener("click", myFunction);

function myFunction() {
    let RandomColor = "#" + Math.random().toString(15).substr(2, 6);
    changingTxt.textContent = RandomColor;
    document.body.style.backgroundColor = RandomColor;
}