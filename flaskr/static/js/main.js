document.addEventListener('DOMContentLoaded', () => {
  const navMenu = document.getElementById('navMenu')
  const navToggle = document.getElementById('navToggle')
  const navClose = document.getElementById('navClose')

  navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu')
  })

  navClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu')
  })
})
