function formatPrice(event) {
    const input = event.target;
    const price = input.value.replace(/\D/g, '');
    const formattedPrice = '#' + price;
    input.value = formattedPrice;
  }

  // Get the file input element
const fileInput = document.getElementById('profile-pic-input');

// Get the image preview element
const imagePreview = document.getElementById('profile-pic-preview');

// Add an event listener to the file input
fileInput.addEventListener('change', function(event) {
  // Check if a file is selected
  if (event.target.files && event.target.files[0]) {
    // Get the selected file
    const selectedFile = event.target.files[0];

    // Create a FileReader object
    const reader = new FileReader();

    // Set the image source when the FileReader has finished reading the file
    reader.onload = function(event) {
      imagePreview.src = event.target.result;
    };

    // Read the selected file as a data URL
    reader.readAsDataURL(selectedFile);
  }
});




// javascript for product image 

        // Get the file input element
        const productInput = document.getElementById('product-pic-input');
      
        // Get the image preview element
        const productImagePreview = document.getElementById('product-pic-preview');
        
        // Add an event listener to the file input
        productInput.addEventListener('change', function(event) {
          // Check if a file is selected
          if (event.target.files && event.target.files[0]) {
            // Get the selected file
            const selectedFile = event.target.files[0];
        
            // Create a FileReader object
            const reader = new FileReader();
        
            // Set the image source when the FileReader has finished reading the file
            reader.onload = function(event) {
              productImagePreview.src = event.target.result;
            };
        
            // Read the selected file as a data URL
            reader.readAsDataURL(selectedFile);
          }
        });