document.addEventListener('DOMContentLoaded', e => {
    // Helps with the mobile menu 
    const menuBtn = document.getElementById('menuBtn')
    const menu = document.getElementById('menu')
    const secondMenuBtn = document.getElementById('secondMenuBtn')

    menuBtn.addEventListener('click', e => {
        // For fade out effect
        menu.style.opacity = 0
        setTimeout(() => {
            menu.classList.add('hidden')
        }, 100)
    })

    secondMenuBtn.addEventListener('click', e => {
        // For fade in effect
        menu.classList.remove('hidden')
        menu.style.opacity = 0
        setTimeout(() => {
            menu.style.opacity = 1
        }, 100)
    })

})

// To make sure the aside bar isn't hidden after opening the menu
window.addEventListener('resize', () => {
    if (window.innerWidth > 767) {
        menu.style.opacity = 1
    }
})