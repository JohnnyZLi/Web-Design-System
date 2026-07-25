const menuButton = document.querySelector('.menu-button');
const menu = document.querySelector('#site-menu');

function closeMenu({ restoreFocus = false } = {}) {
  menu.hidden = true;
  menuButton.setAttribute('aria-expanded', 'false');
  if (restoreFocus) menuButton.focus();
}

menuButton.addEventListener('click', () => {
  const opening = menu.hidden;
  menu.hidden = !opening;
  menuButton.setAttribute('aria-expanded', String(opening));
  if (opening) menu.querySelector('a').focus();
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !menu.hidden) closeMenu({ restoreFocus: true });
});

document.addEventListener('click', (event) => {
  if (!menu.hidden && !menu.contains(event.target) && event.target !== menuButton) {
    closeMenu();
  }
});

menu.addEventListener('click', () => closeMenu());

const dialog = document.querySelector('#delete-dialog');
const openDialog = document.querySelector('[data-open-dialog]');
openDialog.addEventListener('click', () => dialog.showModal());
dialog.addEventListener('close', () => openDialog.focus());
