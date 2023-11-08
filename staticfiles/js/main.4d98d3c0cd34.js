const initApp = () => {
    const openBtn = document.querySelector('#Openbtn');
    const menu = document.querySelector('#menu');
    const img = document.querySelector('#image');

    const toggleMenu = () => {
        menu.classList.toggle('hidden');
        menu.classList.toggle('block');

        if (menu.classList.contains('block')) {
            img.src = imgCloseMenu;
        } else {
            img.src = imgMenuopen;
        }
    }

    openBtn.addEventListener('click', toggleMenu);
}

document.addEventListener('DOMContentLoaded', initApp);

// Hero Image
// const hero = document.querySelector('#hero');
// hero.style.backgroundImage = `url(${heroImage})`;