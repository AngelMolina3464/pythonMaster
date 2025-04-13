document.addEventListener("DOMContentLoaded", function () {
  const selectLinks = document.querySelectorAll(".nav__Container__Select > a");

  selectLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();

      const parentLi = link.parentElement;
      const optionsContainer = parentLi.querySelector(
        ".nav__Container__Option"
      );

      if (optionsContainer.classList.contains("visible")) {
        optionsContainer.classList.remove("visible");
      } else {
        document
          .querySelectorAll(".nav__Container__Option")
          .forEach((option) => {
            option.classList.remove("visible");
          });

        optionsContainer.classList.add("visible");
      }
    });
  });
});

window.addEventListener("scroll", () => {
  let scrollY = window.scrollY;
  // console.log("Desplazamiento vertical: " + scrollY);
});

console.log("Con js y abe")