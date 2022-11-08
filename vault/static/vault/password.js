const passwordField = document.getElementById('id_password')
const passwordBtn = document.getElementById('showPass')
const copyPswdBtn = document.getElementById('copyPswd')
const copyMsg = document.getElementById('copyMsg')
const genPswdMsg = document.getElementById('genPswdMsg')
const pwsdGenBtn = document.getElementById('pwsdGenBtn')

// For showing and hiding password, whilist updating the icon.
passwordBtn.addEventListener('click', e => {
    if (passwordField.type == 'text') {
        passwordField.type = 'password'
        passwordBtn.classList = 'fa-solid fa-eye'
    }
    else {
        passwordField.type = 'text'
        passwordBtn.classList = 'fa-solid fa-eye-slash'
    }
})

const password = {
    'char': "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    'length': 16,
}

// An hidden input element that helps hold the generated password.
let passwordHolder = document.createElement('input')
passwordHolder.style.cssText = 'display: none;'
pwsdGenBtn.appendChild(passwordHolder)

pwsdGenBtn.addEventListener('click', e => {
    e.preventDefault()
    let generatedPswd = ''
    for (let i = 0; i < password.length; i++) {
        let char = password.char[Math.floor(Math.random() * password.char.length)]
        generatedPswd += char
    }

    passwordHolder.value = generatedPswd
    passwordHolder.style.cssText = 'display: block;' // Changes the password display to block, since trying to copy the input element's value while it's hidden does not work.
    copyPswd(passwordHolder)
    passwordHolder.style.cssText = 'display: none;' // Hides the input element

    // Displays the 'Password Copied' message.
    genPswdMsg.classList.remove('hidden')
    setTimeout(() => {
        genPswdMsg.classList.add('hidden')
    }, 1000)
})

const copyPswd = (field) => {
    // Stores the field type, changes it's type to text so the text inside the element can be copied, copies it, then changes it back to its original fieldType
    fieldType = field.type
    field.type = 'text'
    let text = field.select()
    document.execCommand('copy')
    field.type = fieldType
}

copyPswdBtn.addEventListener('click', e => {
    copyPswd(passwordField)

    // Displays the 'Password Copied' message.
    copyPswdBtn.classList.add('text-blue-600')
    copyMsg.classList.remove('hidden')
    setTimeout(() => {
        copyMsg.classList.add('hidden')
        copyPswdBtn.classList.remove('text-blue-600')
    }, 1000)
})
