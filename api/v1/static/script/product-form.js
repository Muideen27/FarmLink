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

// document.getElementById('product-form').addEventListener('submit', function(event) {
//   event.preventDefault(); // Prevent the default form submission

//   // Get the form data
//   var formData = new FormData(this);

//   // Get the farmer_id from the data attribute
//   var farmerId = document.querySelector('script[data-farmer-id]').getAttribute('data-farmer-id');

//   // Define the URLs
//   var uploadURL = '/upload-product-image/' + farmerId;
//   var postProductURL = '/post-product/' + farmerId;

//   // Get the selected value from the availability field
//   var availabilitySelect = document.getElementById('availability');
//   var availabilityValue = availabilitySelect.options[availabilitySelect.selectedIndex].value;

//   // Set the availability_status value in the form data
//   formData.set('availability_status', availabilityValue);

//   // Perform the image upload request
//   fetch(uploadURL, {
//     method: 'POST',
//     body: new FormData(document.getElementById('product-form'))
//   })
//     .then(function(response) {
//       if (response.ok) {
//         // Image upload successful, continue with product creation
//         return fetch(postProductURL, {
//           method: 'POST',
//           body: formData
//         });
//       } else {
//         // Image upload failed
//         throw new Error('Failed to upload image');
//       }
//     })
//     .then(function(response) {
//       if (response.ok) {
//         // Product creation successful
//         alert('Product created successfully');
//         // Perform any additional actions or redirects
//       } else {
//         // Product creation failed
//         throw new Error('Failed to create product');
//       }
//     })
//     .catch(function(error) {
//       // Handle error from image upload or product creation request
//       alert('An error occurred: ' + error.message);
//     });
// });

// const fileInput = document.getElementById('profile-pic-input');
// const imagePreview = document.getElementById('profile-pic-preview');

// const productInput = document.getElementById('product-pic-input');
// const productImagePreview = document.getElementById('product-pic-preview');

// fileInput.addEventListener('change', handleFileInputChange);
// productInput.addEventListener('change', handleFileInputChange);

// function handleFileInputChange(event) {
//   const input = event.target;
//   const previewElement = input.nextElementSibling; // Assuming the preview element is the next sibling

//   if (input.files && input.files[0]) {
//     const reader = new FileReader();
//     reader.onload = function(event) {
//       previewElement.src = event.target.result;
//     };
//     reader.readAsDataURL(input.files[0]);
//   }
// }

document.getElementById('product-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const formData = new FormData(this);
  const farmerId = document.querySelector('script[data-farmer-id]').getAttribute('data-farmer-id');
  const postProductURL = `/farmers/${farmerId}/products/`;

  const availabilitySelect = document.getElementById('availability');
  const availabilityValue = availabilitySelect.value;
  formData.set('availability', availabilityValue);

  fetch(postProductURL, {
    method: 'POST',
    body: formData
  })
    .then(function(response) {
      if (response.ok) {
        alert('Product created successfully');
      } else {
        throw new Error('Failed to create product');
      }
    })
    .catch(function(error) {
      alert('An error occurred: ' + error.message);
    });
});
