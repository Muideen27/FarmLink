const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});

// Submit the form if validation passes
const loginForm = document.forms['form'];
loginForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form submission
  if (validated()) {
    this.submit();
}
});

const sliderContainer = document.querySelector('.slider-container');
        const slides = sliderContainer.querySelectorAll('div');

        let currentSlide = 0;

        function showSlide() {
            slides.forEach((slide, index) => {
                slide.style.transform = `translateX(${index - currentSlide}00%)`;
            });
        }

        function nextSlide() {
            currentSlide++;
            if (currentSlide >= slides.length) {
                currentSlide = 0;
            }
            showSlide();
        }

        setInterval(nextSlide, 6000);