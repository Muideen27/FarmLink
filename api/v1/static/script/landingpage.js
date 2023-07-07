$(document).ready(function() {
  $(".user-profile img").click(function() {
    $(".dropdown").fadeToggle(500);
  });

  $(document).click(function(event) {
    if (!$(event.target).closest(".user-profile").length) {
      $(".dropdown").fadeOut(500);
    }
  });

  $(".sign-in-btn").click(function() {
    $(".sign-in-form").fadeIn(500);
  });

  $('.form-submit').click(function(event) {
    // Prevent form submission
    event.preventDefault();

    // Hide any previous error messages
    $('.sign-in-form .error').hide();

    // Submit the form
    $('.sign-in-form form').submit();
  });

  $(".close-form").click(function() {
    $(".sign-in-form").fadeOut(500);
  });

});

// $(document).ready(function() {
//   $(".user-icon").click(function() {
//     $(".dropdown-container").fadeToggle(200);
//   });

//   $(document).click(function(event) {
//     if (!$(event.target).closest(".user-icon-container").length) {
//       $(".dropdown-container").fadeOut(200);
//     }
//   });
// });
