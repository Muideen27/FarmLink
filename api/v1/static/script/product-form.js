function formatPrice(event) {
    const input = event.target;
    const price = input.value.replace(/\D/g, '');
    const formattedPrice = '#' + price;
    input.value = formattedPrice;
}

// document.getElementById('product-form').addEventListener('submit', function(event) {
//   event.preventDefault(); // Prevent the default form submission

//   // Get the form data
//   var formData = new FormData(this);

//   // Get the image file
//   var imageFile = document.getElementById('image').files[0];

//   // Create a new FormData instance for the image upload
//   var imageFormData = new FormData();
//   imageFormData.append('image', imageFile);

//   // Perform the image upload request
//   fetch(uploadURL, {
//       method: 'POST',
//       body: imageFormData
//   })
//   .then(function(response) {
//       if (response.ok) {
//           // Image upload successful, continue with product creation
//           fetch(postProductURL, {
//               method: 'POST',
//               body: formData
//           })
//           .then(function(response) {
//               if (response.ok) {
//                   // Product creation successful
//                   alert('Product created successfully');
//                   // Perform any additional actions or redirects
//               } else {
//                   // Product creation failed
//                   alert('Failed to create product');
//               }
//           })
//           .catch(function(error) {
//               // Handle error from product creation request
//               alert('An error occurred while creating the product');
//           });
//       } else {
//           // Image upload failed
//           alert('Failed to upload image');
//       }
//   })
//   .catch(function(error) {
//       // Handle error from image upload request
//       alert('An error occurred while uploading the image');
//   });
// });

// document.getElementById('product-form-submit').addEventListener('click', function(event) {
//     event.preventDefault(); // Prevent the default form submission
  
//     // Get the form data
//     var formData = new FormData(document.getElementById('product-form'));
  
//     // Get the image file
//     var imageFile = document.getElementById('image').files[0];
  
//     // Create a new FormData instance for the image upload
//     var imageFormData = new FormData();
//     imageFormData.append('image', imageFile);
  
//     // Get the farmer_id from the data attribute
//     var farmerId = document.getElementById('product-form-submit').getAttribute('data-farmer-id');
  
//     // Define the URLs
//     var uploadURL = '/upload-product-image/' + farmerId;
//     var postProductURL = '/post-product/' + farmerId;
  
//     // Perform the image upload request
//     fetch(uploadURL, {
//         method: 'POST',
//         body: imageFormData
//     })
//     .then(function(response) {
//         if (response.ok) {
//             // Image upload successful, continue with product creation
//             fetch(postProductURL, {
//                 method: 'POST',
//                 body: formData
//             })
//             .then(function(response) {
//                 if (response.ok) {
//                     // Product creation successful
//                     alert('Product created successfully');
//                     // Perform any additional actions or redirects
//                 } else {
//                     // Product creation failed
//                     alert('Failed to create product');
//                 }
//             })
//             .catch(function(error) {
//                 // Handle error from product creation request
//                 alert('An error occurred while creating the product');
//             });
//         } else {
//             // Image upload failed
//             alert('Failed to upload image');
//         }
//     })
//     .catch(function(error) {
//         // Handle error from image upload request
//         alert('An error occurred while uploading the image');
//     });
// });

// document.getElementById('product-form-submit').addEventListener('click', function(event) {
//     event.preventDefault(); // Prevent the default form submission

//     // Get the form data
//     var formData = new FormData(document.getElementById('product-form'));

//     // Get the image file
//     var imageFile = document.getElementById('image').files[0];

//     // Create a new FormData instance for the image upload
//     var imageFormData = new FormData();
//     imageFormData.append('image', imageFile);

//     // Get the farmer_id from the data attribute
//     var farmerId = document.getElementById('product-form-submit').getAttribute('data-farmer-id');

//     // Perform the image upload request
//     fetch(uploadURL, {
//         method: 'POST',
//         body: imageFormData
//     })
//     .then(function(response) {
//         if (response.ok) {
//             // Image upload successful, continue with product creation
//             fetch(postProductURL, {
//                 method: 'POST',
//                 body: formData
//             })
//             .then(function(response) {
//                 if (response.ok) {
//                     // Product creation successful
//                     alert('Product created successfully');
//                     // Perform any additional actions or redirects
//                 } else {
//                     // Product creation failed
//                     alert('Failed to create product');
//                 }
//             })
//             .catch(function(error) {
//                 // Handle error from product creation request
//                 alert('An error occurred while creating the product');
//             });
//         } else {
//             // Image upload failed
//             alert('Failed to upload image');
//         }
//     })
//     .catch(function(error) {
//         // Handle error from image upload request
//         alert('An error occurred while uploading the image');
//     });
// });
var farmerId = "{{ farmer_id }}"; 
var uploadURL = '/upload-product-image/' + farmerId;
var postProductURL = '/post-product/' + farmerId;

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