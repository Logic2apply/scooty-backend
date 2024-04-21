
// -----------------------script1.js-------------------------------
const wraper = document.querySelector('.wraper');
const loginlink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
//             SHOW HIDDEN -PASSWORD----------------
const loginEyeIcon = document.getElementById('login-eye-icon');
const loginPasswordInput = document.getElementById('login-pass');
const registerEyeIcon = document.getElementById('register-eye-icon');
const registerPasswordInput = document.getElementById('register-pass');



registerLink.addEventListener('click', () => {
    wraper.classList.add('active');
});

loginlink.addEventListener('click', () => {
    wraper.classList.remove('active');
});



loginEyeIcon.addEventListener('click', function () {
    togglePasswordVisibility(loginPasswordInput, loginEyeIcon);
});

registerEyeIcon.addEventListener('click', function () {
    togglePasswordVisibility(registerPasswordInput, registerEyeIcon);
});

function togglePasswordVisibility(inputElement, eyeIconElement) {
    const currentType = inputElement.getAttribute('type');
    if (currentType === 'password') {
        inputElement.setAttribute('type', 'text');
        eyeIconElement.innerHTML = '<ion-icon name="eye-outline"></ion-icon>';
    } else {
        inputElement.setAttribute('type', 'password');
        eyeIconElement.innerHTML = '<ion-icon name="eye-off-outline"></ion-icon>';
    }
}