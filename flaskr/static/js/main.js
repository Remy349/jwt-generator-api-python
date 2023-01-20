document.addEventListener('DOMContentLoaded', () => {
  // Nav toggle
  const navMenu = document.getElementById('navMenu')
  const navToggle = document.getElementById('navToggle')
  const navClose = document.getElementById('navClose')

  navToggle.addEventListener('click', () => {
    navMenu.classList.add('show-menu')
  })

  navClose.addEventListener('click', () => {
    navMenu.classList.remove('show-menu')
  })

  // Messages
  const messages = document.getElementById('messages')

  if (messages) {
    const TIME_DURATION = 6000

    setTimeout(() => {
      messages.classList.add('hide-message')
    }, TIME_DURATION)

    setTimeout(() => {
      messages.style.display = 'none'
    }, TIME_DURATION + 1000)
  }
})
