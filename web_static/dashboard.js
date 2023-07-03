const menuItems = document.querySelectorAll('.menu a');

menuItems.forEach(item => {
  item.addEventListener('click', function() {
    menuItems.forEach(item => item.classList.remove('active'));
    this.classList.add('active');
  });
});
  

$(document).ready(function() {
  $(".user-profile img").click(function() {
    $(".dropdown").fadeToggle(1000);
  });

  $(document).click(function(event) {
    if (!$(event.target).closest(".user-profile").length) {
      $(".dropdown").fadeOut(1000);
    }
  });
});