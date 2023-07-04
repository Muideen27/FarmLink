  $(document).ready(function() {
    $(".user-profile img").click(function() {
      $(".dropdown").fadeToggle(1000);
    });

    $(document).click(function(event) {
      if (!$(event.target).closest(".user-profile").length) {
        $(".dropdown").fadeOut(1000);
      }
    });

    $(".sign-in-btn").click(function() {
      $(".sign-in-form").fadeIn(1000);
    });

    $(".close-form").click(function() {
      $(".sign-in-form").fadeOut(1000);
    });
  });