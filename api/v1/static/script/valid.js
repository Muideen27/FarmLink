var email = document.forms['form']['email'];
var password = document.forms['form']['password'];

var email_error = document.querySelector('.email_error');
var pass_error = document.querySelector('.pass_error');

email.addEventListener('input', email_verify);
password.addEventListener('input', pass_verify);

function validated() {
    var emailValid = email.value.length >= 9;
    var passwordValid = password.value.length >= 9;

    if (!emailValid) {
        email_error.style.display = "block";
        /*email.style.input-box; "2px solid red";*/
        email.focus();
    } else {
        email_error.style.display = "none";
    }

    if (!passwordValid) {
        pass_error.style.display = "block";
        password.focus();
    } else {
        pass_error.style.display = "none";
    }

    return emailValid && passwordValid;
}

function email_verify() {
    if (email.value.length >= 9) {
        email_error.style.display = "none";
    }
}

function pass_verify() {
    if (password.value.length >= 9) {
        pass_error.style.display = "none";
    }
}
