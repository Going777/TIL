// 코드를 작성해 주세요
const player1 = document.querySelector('#player1-img')
const player2 = document.querySelector('#player2-img')

const rockBtn = document.querySelector('#rock-button')
const scissorsBtn = document.querySelector('#scissors-button')
const paperBtn = document.querySelector('#paper-button')

let idx = 0
const player2Img = function() {
  images = ['rock','scissors','paper']
  player2.src = `./img/${images[idx]}.png`
  idx++
  if (idx==images.length) {
    idx = 0
  }
}


function player1Choice(choice) {
  player1.src = `./img/${choice}.png`
  rockBtn.disabled = true
  scissorsBtn.disabled = true
  paperBtn.disabled = true
  
  // 0.1초 간격으로 호출
  const intervalId = setInterval(player2Img, 100)
  /// 3초 후 종료
  setTimeout(function() {
    clearInterval(intervalId)
  }, 3000)

  rockBtn.disabled = false
  scissorsBtn.disabled = false
  paperBtn.disabled = false
}

rockBtn.addEventListener('click', function(event) {
  player1Choice('rock')
})
scissorsBtn.addEventListener('click', function(event) {
  player1Choice('scissors')
})
paperBtn.addEventListener('click', function(event) {
  player1Choice('paper')
})
