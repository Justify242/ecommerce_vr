document.addEventListener('DOMContentLoaded', () => {
  const burger = document.querySelector('.burger');
  const navCenter = document.querySelector('.nav-center');

  if (burger && navCenter) {
    burger.addEventListener('click', () => {
      navCenter.classList.toggle('active');
      burger.classList.toggle('open'); // для анимации бургер → крестик
    });
  }
});

document.querySelectorAll(".card").forEach(card => {
  card.addEventListener("click", () => {
    const targetId = card.getAttribute("data-target");

    // скрыть весь контент
    document.querySelectorAll(".tab-content").forEach(tab => {
      tab.classList.remove("active");
    });

    // показать нужный
    document.getElementById(targetId).classList.add("active");

    // показать row-extra
    document.querySelector(".row-extra").classList.add("active");
  });
});
