// get the dropdown menus
const tablesDropdown = document.getElementById("tables-dropdown");

const chooseBtn = document.querySelector('#choose-btn');

// add click event listener to choose button
chooseBtn.addEventListener('click', chooseOption);

function chooseOption() {
    var dropdown = document.getElementById("tables-dropdown");
    var selectedTable = dropdown.options[dropdown.selectedIndex].value;
    console.log("Selected table:", selectedTable);
    // Do something with the selected table value
    alert(`You clicked the "Choose" button! You selected table: ${selectedTable}`);
}

// fetch the list of tables from the server
fetch("/tables")
  .then(response => response.json())
  .then(tables => {
    // create an option for each table and add it to the dropdown
    tables.forEach(table => {
      const option = document.createElement("option");
      option.value = table;
      option.text = table;
      tablesDropdown.appendChild(option);
    });
  })
  .catch(error => console.error(error));
