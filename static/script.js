const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const customerSignUpBtn = document.getElementById("customer-sign-up");
const adminLoginBtn = document.getElementById("admin-login");


adminLoginBtn.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "./admin_login.html";
});

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


employeeSignUpBtn.addEventListener("click", function() {
  window.location.href = "employee_signup.html";
});

customerSignUpBtn.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "./customer.html";
});

adminLoginBtn.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "./admin_login.html";
});


