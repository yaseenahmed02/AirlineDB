const chooseBtn = document.getElementById("choose-btn");
const tablesDropdown = document.getElementById("tables-dropdown");

chooseBtn.addEventListener("click", function () {
  const selectedTable = tablesDropdown.value;
  window.location.href = `/${selectedTable}.html`;
});