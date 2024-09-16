// Frontend validation for registration form
document.getElementById('registerForm').onsubmit = function() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;
    
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return false;
    }
    return true;
};

// Captcha Verification for Login
function verifyCaptcha() {
    // Add your CAPTCHA verification logic here
    return true;
}
