let options = {
    strings: ['Welcome to Ict Site'],
    typeSpeed: 40,
    startDelay: 500,
};

let typed = new Typed('.element', options);

let nav = document.querySelector('nav')

window.addEventListener('scroll', ()=> {
    nav.classList.toggle('nav-active', window.scrollY > 0)
});

// scroll top
let scrollTop = document.querySelector('.nav-list__link')

window.addEventListener('scroll', ()=> {
    scrollTop.classList.toggle('nav-list__link-active', window.scrollY >= 400)
});


