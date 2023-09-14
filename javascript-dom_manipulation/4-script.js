document.addEventListener("DOMContentLoaded", function () {
    const addItemButton = document.getElementById("add_item");
    const myList = document.querySelector(".my_list");
  
    addItemButton.addEventListener("click", function () {
      // Create a new <li> element
      const newItem = document.createElement("li");
      
      // Set the text content of the new element
      newItem.textContent = "Item";
      
      // Append the new <li> element to the <ul> with class "my_list"
      myList.appendChild(newItem);
    });
  });
  