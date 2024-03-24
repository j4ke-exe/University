document.addEventListener('DOMContentLoaded', function () {
   const cardNumberInput = document.getElementById('cardNumber');
   const cardExpiryInput = document.getElementById('cardExpiry');
   const cardCVVInput = document.getElementById('cardCVV');
   const phoneInput = document.getElementById('phone');

   cardNumberInput.addEventListener('input', function () {
       let cardType = null;
       if (this.value.startsWith('4')) {
           cardType = 'VISA';
       } else if (this.value.startsWith('5')) {
           cardType = 'MasterCard';
       } else if (this.value.startsWith('34') || this.value.startsWith('37')) {
           cardType = 'AMEX';
       }

       cardCVVInput.setAttribute('maxlength', cardType === 'AMEX' ? '4' : '3');
       
       this.value = this.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '').substring(0, 16);

       let matches = this.value.match(/\d{4,}/g);
       let match = matches && matches[0] || '';
       let parts = [];
       for (let i = 0, len = match.length; i < len; i += 4) {
           parts.push(match.substring(i, i + 4));
       }
       this.value = parts.length ? parts.join(' ') : this.value;
   });

   cardExpiryInput.addEventListener('input', function () {
       var v = this.value.replace(/\D/g, '').slice(0, 4);
       if (v.length >= 3) {
           v = v.slice(0, 2) + '/' + v.slice(2);
       }
       this.value = v;
   });

   cardCVVInput.addEventListener('input', function () {
       // Enforce the maxlength attribute for CVV input
       let maxLength = this.getAttribute('maxlength');
       this.value = this.value.replace(/[^\d]/g, '').substring(0, maxLength);
   });

   phoneInput.addEventListener('input', function (e) {
       e.target.value = formatPhoneNumber(e.target.value);
   });

   function formatPhoneNumber(value) {
       value = value.replace(/\D/g, '').substring(0, 10);

       let formattedValue;
       if (value.length < 4) {
           formattedValue = '(' + value;
       } else if (value.length < 7) {
           formattedValue = '(' + value.substring(0, 3) + ') ' + value.substring(3);
       } else {
           formattedValue = '(' + value.substring(0, 3) + ') ' + value.substring(3, 6) + '-' + value.substring(6);
       }
       return formattedValue;
   }

   function enforceNumeric(event) {
       if (event.which < 48 || event.which > 57) {
           event.preventDefault();
       }
   }

   // Apply enforceNumeric for the phone field as well as card number, expiry, and CVV fields
   phoneInput.addEventListener('keypress', enforceNumeric);
   cardNumberInput.addEventListener('keypress', enforceNumeric);
   cardExpiryInput.addEventListener('keypress', enforceNumeric);
   cardCVVInput.addEventListener('keypress', enforceNumeric);
});