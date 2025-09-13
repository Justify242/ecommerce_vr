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