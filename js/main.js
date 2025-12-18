document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const errorMessage = document.getElementById('error-message');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault(); 
            
            const password = document.getElementById('password').value;

          
            if (password.length > 10) {
                errorMessage.textContent = "La contraseña no puede superar los 10 caracteres.";
                errorMessage.style.display = "block";
            } else if (password.length === 0) {
                errorMessage.textContent = "Por favor, ingrese su contraseña.";
                errorMessage.style.display = "block";
            } else {
                errorMessage.style.display = "none";
              
                window.location.href = "cursos.html";
            }
        });
    }
});