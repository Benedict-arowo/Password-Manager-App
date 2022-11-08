const registerBtn = document.getElementById('registerBtn')
const loginBtn = document.getElementById('loginBtn')
const form = document.getElementsByTagName('form')[0]
const formContent = document.getElementById('form')
const desc = document.getElementById('desc')

let currentMode;
const formSelector = ({ e, mode, descMessage }) => {
    if (currentMode == mode) {
        return
    }
    e.preventDefault()
    currentMode = mode
    form.setAttribute('action', mode == 'login' ? loginUrl : registerUrl) // Deciding on which url to send the form to depending on the mode login or register
    formContent.innerHTML = mode == 'login' ? login : register
    // Changes the form content to an html prebuilt form defined in the auth.html page.
    desc.textContent = descMessage
    // Chaging the button colors to show the user which page is active
    if (mode == 'login') {
        loginBtn.style.backgroundColor = 'rgb(37 99 235 /  var(--tw-bg-opacity))'
        registerBtn.style.backgroundColor = 'rgb(147 197 253 /  var(--tw-bg-opacity))'
    }
    else {
        loginBtn.style.backgroundColor = 'rgb(147 197 253 /  var(--tw-bg-opacity))'
        registerBtn.style.backgroundColor = 'rgb(37 99 235 /  var(--tw-bg-opacity))'
    }
}

window.addEventListener('DOMContentLoaded', e => {
    formSelector({
        e,
        mode: 'login',
        descMessage: 'Log in to access your secure vault.'
    })
})

registerBtn.addEventListener('click', e => {
    formSelector({
        e,
        mode: 'register',
        descMessage: 'Register a new account'
    })
})


loginBtn.addEventListener('click', e => {
    formSelector({
        e,
        mode: 'login',
        descMessage: 'Log in to access your secure vault.'
    })

})