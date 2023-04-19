// Get the search input element and the list element
const searchInput = document.getElementById("myInput");
const listElement = document.getElementById("myList");

// Define the values array (in this case, we're just using an example array)
const values = ['Hemingway', 'Fitzgerald', 'Johnny'];

// Function to filter the list of values based on user input
function filterValues() {
  // Get the user's search input
  const filterValue = searchInput.value.toLowerCase();
  
  // Remove any existing list items from the list element
  while (listElement.firstChild) {
    listElement.removeChild(listElement.firstChild);
  }

  // Loop through each value in the values array
  for (let i = 0; i < values.length; i++) {
    // Convert the current value to lowercase for case-insensitive matching
    const currentValue = values[i].toLowerCase();

    // If the current value contains the user's search input, add it to the list
    if (currentValue.includes(filterValue)) {
      const item = document.createElement("li");
      const text = document.createTextNode(values[i]);
      item.appendChild(text);
      listElement.appendChild(item);
    }
  }
}

// Call the filterValues function to populate the list with all values initially
filterValues();

  