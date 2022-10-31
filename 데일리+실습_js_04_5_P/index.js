// 코드를 작성해 주세요
const player1 = document.querySelector('#player1-img')
const player2 = document.querySelector('#player2-img')

const rockBtn = document.querySelector('#rock-button')
const scissorsBtn = document.querySelector('#scissors-button')
const paperBtn = document.querySelector('#paper-button')

let idx = _.random(0,2)   // 첫 시작 랜덤하게
const player2Img = function() {
  images = ['rock','scissors','paper']
  player2.src = `./img/${images[idx%3]}.png`
  idx++
  
  rockBtn.disabled = true
  scissorsBtn.disabled = true
  paperBtn.disabled = true
}

// const winnerFind(plqyer1, player2) {

// }

function player1Choice(choice) {
  player1.src = `./img/${choice}.png`
  
  
  // 0.1초 간격으로 호출
  const intervalId = setInterval(player2Img, 100)
  /// 3초 후 종료
  setTimeout(function() {
    idx = _.random(0,2)   // 첫 시작 랜덤하게
    clearInterval(intervalId)

    console.log(player2.src)
    console.log(player2)
    console.log(player1.src)
    console.log(player1)

    rockBtn.disabled = false
    scissorsBtn.disabled = false
    paperBtn.disabled = false
  }, 3000)

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

