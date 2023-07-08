/* clicking on about shows up or disappears about-menu */
// let about_link = document.querySelector(".about-link");
// let about_menu = document.querySelector(".about-menu");

// function showMenu() {
//   if (about_menu.style.display === "none") {
//     about_menu.style.display = "block";
//   } else {
//     about_menu.style.display = "none";
//   }
// }

function burgerFunction() {
  let x = document.getElementById("sm");
  let y = document.getElementById("burger");
  if (x.style.display === "flex") {
    x.style.display = "none";
  } else {
    x.style.display = "flex";
  }
}

window.addEventListener("resize", function () {
  let x = document.getElementById("sm");
  x.style.display = "none";
});

/* code block for carousel for testimonials */

let testimonialIndex = 1;
showSlides(testimonialIndex);

// next/previous controls
function plusSlides(n) {
  showSlides((testimonialIndex += n));
}

// control from dot
function currentSlide(n) {
  showSlides((testimonialIndex = n));
}

function showSlides(n) {
  let i = 0;
  let testimonials = document.getElementsByClassName("testimonial");
  let dots = document.getElementsByClassName("dot");

  if (n > testimonials.length) {
    testimonialIndex = 1;
  }

  if (n < 1) {
    testimonialIndex = testimonials.length;
  }

  for (i = 0; i < testimonials.length; i++) {
    testimonials[i].style.display = "none";
  }

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace("active", "");
  }

  testimonials[testimonialIndex - 1].style.display = "block";
  dots[testimonialIndex - 1].className += " active";

  /* automate the carousel */
  // if (testimonialIndex < 3) {
  //   testimonialIndex++;
  // } else if (testimonialIndex === 3) {
  //   testimonialIndex = 1;
  // }
  // setTimeout(showSlides, 20000);
}
