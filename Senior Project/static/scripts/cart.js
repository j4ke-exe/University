document.addEventListener('DOMContentLoaded', () => {
   const quantityInputs = document.querySelectorAll('.quantity-input');
   
   quantityInputs.forEach(input => {
     input.addEventListener('change', (e) => {
       const itemId = e.target.getAttribute('data-id');
       updateCartItemQuantity(itemId, e.target.value);
     });
   });
   
   const removeButtons = document.querySelectorAll('.remove-item-btn');
   
   removeButtons.forEach(button => {
     button.addEventListener('click', (e) => {
       const itemId = e.target.getAttribute('data-id');
       removeItemFromCart(itemId);
     });
   });
   
   function updateCartItemQuantity(itemId, quantity) {
     // AJAX call to server to update quantity
     console.log(`Update item ${itemId} to quantity ${quantity}`);
     // Implement actual update logic here
   }
   
   function removeItemFromCart(itemId) {
     // AJAX call to server to remove item
     console.log(`Remove item ${itemId}`);
     // Implement actual removal logic here
   }
 }); 