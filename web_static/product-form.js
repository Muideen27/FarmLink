function formatPrice(event) {
    const input = event.target;
    const price = input.value.replace(/\D/g, '');
    const formattedPrice = '#' + price;
    input.value = formattedPrice;
  }