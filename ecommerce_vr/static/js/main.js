window.addEventListener('load', () => {
  window.scrollTo(0, 0);
});

document.addEventListener('DOMContentLoaded', () => {

  /*
  -------------------
  Управление бургером
  -------------------
  */

  const burger = document.querySelector('.burger');
  const navCenter = document.querySelector('.nav-center');
  const navLinks = document.querySelectorAll('.nav-center a');

  if (burger && navCenter) {
    burger.addEventListener('click', () => {
      navCenter.classList.toggle('active');
      burger.classList.toggle('open'); // для анимации бургер → крестик
    });
  }

  /* Скрытие меню и прокрутка до выбранной секции */
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault(); // предотвращаем стандартный переход

      const targetId = link.getAttribute('href'); // получаем якорь
      const targetElement = document.querySelector(targetId);
      const header = document.querySelector('.site-header');
      const headerHeight = header ? header.offsetHeight + 40 : 0;

      if (targetElement) {
        const elementPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
        const offsetPosition = elementPosition - headerHeight;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }

      // скрываем меню
      navCenter.classList.remove('active');
      burger.classList.remove('open');
    });
  });

  /*
  -------------------
  Управление появлением текста и кнопки на хиро
  -------------------
  */

  const heroText = document.querySelector(".hero-text");
  const heroBtn = document.querySelector(".hero-btn");

  // можно добавить небольшую задержку для кнопки
  setTimeout(() => heroText.classList.add("show"), 300);
  setTimeout(() => heroBtn.classList.add("show"), 300);

  /*
  -------------------
  Управление появлением секций и элементов
  при прокрутке
  -------------------
  */

  const sections = document.querySelectorAll("section");
  const aboutUsCards = document.querySelectorAll(".about-us .card");
  const casesCards = document.querySelectorAll(".cases .case-card")
  const technologiesCards = document.querySelectorAll(".technologies .card")
  const faqCards = document.querySelectorAll(".faq .card-collapse")
  const timelinePoints = document.querySelectorAll(".timeline .container")

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
        observer.unobserve(entry.target); // если нужно один раз
      }
    });
  }, {
    threshold: 0.2
  });

  /* Секции */
  sections.forEach(section => {
    observer.observe(section);
  });

  /* Карточки в секции о нас */
  aboutUsCards.forEach((card, index) => {
    observer.observe(card);
    // Задержка для каскадного эффекта
    card.style.transitionDelay = `${index * 0.2}s`;
  });

  casesCards.forEach((card, index) => {
    observer.observe(card);
    card.style.transitionDelay = `${index * 0.2}s`;
  });

  /* Карточки в секции технологии */
  technologiesCards.forEach((card, index) => {
    observer.observe(card);
    card.style.transitionDelay = `${index * 0.2}s`;
  });

  /* Карточки в секции часто задаваемые вопросы */
  faqCards.forEach((card, index) => {
    observer.observe(card);
    card.style.transitionDelay = `${index * 0.2}s`;
  });

  /* Пункты таймлайна */
  timelinePoints.forEach((card, index) => {
    observer.observe(card);
    card.style.transitionDelay = `${index * 0.2}s`;
  });
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

    // переключаем класс expanded на кнопке
    btn.classList.toggle('expanded');

    // можно переключать класс на самой карточке, если нужно
    card.classList.toggle('expanded');
  });
});

 /*
 -------------------
 Отправка формы
 -------------------
 */

const form = document.getElementById('formOrder');
const submitBtn = document.getElementById('submitBtn');
const alertBox = document.getElementById('formAlert');

form.addEventListener('submit', async (e) => {
  e.preventDefault(); // отменяем стандартную отправку

  // блокируем кнопку
  submitBtn.disabled = true;

  // показываем статус "Отправка..."
  alertBox.style.display = 'block';
  alertBox.textContent = 'Отправка...';
  alertBox.className = 'sending';

  // собираем данные формы
  const formData = new FormData(form);

  try {
    const response = await fetch(form.action, {
      method: 'POST',
      body: formData,
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    });

    if (response.ok) {
      alertBox.textContent = 'Ваша заявка успешно отправлена. В ближайшее время с Вами свяжется наш оператор.';
      alertBox.className = 'success';
      form.reset();
    } else {
      alertBox.textContent = 'Ошибка отправки формы.';
      alertBox.className = 'error';
    }
  } catch (error) {
    alertBox.textContent = 'Ошибка сети, попробуйте позже.';
    alertBox.className = 'error';
  }

  // разблокируем кнопку через 3 секунды
  setTimeout(() => {
    submitBtn.disabled = false;
  }, 3000);
});

const modal = document.getElementById('caseModal');
const modalImg = modal.querySelector('.carousel-image');
const closeBtn = modal.querySelector('.close');
const prevBtn = modal.querySelector('.prev');
const nextBtn = modal.querySelector('.next');
const dotsContainer = modal.querySelector('.carousel-dots');

let currentImages = [];
let currentIndex = 0;

// Открытие модалки
document.querySelectorAll('.case-card').forEach(card => {
  card.addEventListener('click', () => {
    currentImages = JSON.parse(card.dataset.images);
    currentIndex = 0;
    modalImg.src = currentImages[currentIndex];
    modal.classList.add('show');

    // Создаём точки
    dotsContainer.innerHTML = '';
    currentImages.forEach((_, i) => {
      const dot = document.createElement('span');
      dot.classList.add('dot');
      if (i === 0) dot.classList.add('active');
      dot.addEventListener('click', () => showImage(i));
      dotsContainer.appendChild(dot);
    });
  });
});

// Показ изображения и обновление точек
function showImage(index) {
  currentIndex = index;
  modalImg.src = currentImages[currentIndex];
  const dots = dotsContainer.querySelectorAll('.dot');
  dots.forEach((dot, i) => dot.classList.toggle('active', i === currentIndex));
}

// Навигация
prevBtn.addEventListener('click', () => {
  showImage((currentIndex - 1 + currentImages.length) % currentImages.length);
});

nextBtn.addEventListener('click', () => {
  showImage((currentIndex + 1) % currentImages.length);
});

// Закрытие модалки
closeBtn.addEventListener('click', () => modal.classList.remove('show'));
window.addEventListener('click', e => { if (e.target === modal) modal.classList.remove('show'); });