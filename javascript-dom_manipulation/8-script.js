document.addEventListener("DOMContentLoaded", function () {
    const helloElement = document.getElementById("hello");
  
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then(data => {
        // Get the translation of "hello" from the fetched data
        const translation = data.hello;
        
        // Update the content of the "hello" element with the translation
        helloElement.textContent = translation;
      })
      .catch(error => {
        console.error("Fetch error:", error);
      });
  });
  