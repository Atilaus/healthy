const stateMsg = document.querySelector('.pre-state-msg'),
  buttonz = document.querySelectorAll('.submit-button');

const updateButtonMsg = function(e) {
  this.classList.add('state-1', 'animated');
  setTimeout(() => finalButtonMsg(this), 1300);
};

const finalButtonMsg = function(e) {
  e.classList.add('state-2');
  setTimeout(() => setInitialButtonState(e), 1250);
};

const setInitialButtonState = function(e) {
  e.classList.remove('state-1', 'state-2', 'animated');
};

buttonz.forEach(el => {
  el.addEventListener('click', updateButtonMsg);
});