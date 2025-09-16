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

    // показать нужный контент
    document.getElementById(targetId).classList.add("active");

    // показать row-extra
    document.querySelector(".row-extra").classList.add("active");

    // убрать класс active со всех карточек
    document.querySelectorAll(".card").forEach(c => c.classList.remove("active"));

    // добавить класс active к текущей карточке
    card.classList.add("active");
  });
});

document.querySelectorAll('.card-collapse').forEach(card => {
  const btn = card.querySelector('.collapse-btn');
  const icon = btn.querySelector('.icon');

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    card.classList.toggle('expanded');
    icon.src = card.classList.contains('expanded') ? '/static/assets/cross.png' : '/static/assets/cross.png';
  });
});