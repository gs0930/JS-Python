let playerScore = 0;
let computerScore = 0;
let computerChoiceElement = document.getElementById("computer-choice");

function rpsJudge(choice1, choice2) {
  if (choice1 === choice2) {
    return 0;
  } else if ((choice1 === "rock" && choice2 === "scissors") || 
             (choice1 === "scissors" && choice2 === "paper") || 
             (choice1 === "paper" && choice2 === "rock")) {
    return 1;
  } else {
    return -1;
  }
}

function highlightPlayerChoice(choice) {
  var choiceElements = document.querySelectorAll(".choice");
  for (var i = 0; i < choiceElements.length; i++) {
    choiceElements[i].style.borderColor = "white";
  }
  document.getElementById(choice).style.borderColor = "green";
}

function showComputerChoice(choice) {
  //var computerChoiceElement = document.getElementById("computer-choice");
  computerChoiceElement.style.display='block';
  computerChoiceElement.src = "/"+ choice + ".png";
  computerChoiceElement.alt = "Computer chose " + choice;
  computerChoiceElement.setAttribute("aria-live", "polite");
}

function resetRPS() {
  var choiceElements = document.querySelectorAll(".choice");
  for (var i = 0; i < choiceElements.length; i++) {
    choiceElements[i].style.borderColor = "white";
  }
  var messageElement = document.getElementById("message");
  messageElement.innerHTML = "";
}

function startOver() {
  playerScore = 0;
  computerScore = 0;
  resetRPS();
  updateScores();
  computerChoiceElement.src = "/question-mark.png";
}

function updateScores() {
  document.getElementById("player-score").innerHTML = playerScore;
  if(playerScore==3){
    document.getElementById("winner").innerHTML = "You won!"
    startOver();
  }
  document.getElementById("computer-score").innerHTML = computerScore;
  if(computerScore==3){
    document.getElementById("winner").innerHTML = "You lost :("
    startOver();
  }
}

function playerTurn(choice) {
  resetRPS();
  highlightPlayerChoice(choice);
  var choices = Array("rock", "paper", "scissors");
  var computerChoice = choices[Math.floor(Math.random()*choices.length)];

  showComputerChoice(computerChoice);
  var result = rpsJudge(choice, computerChoice);
  if (result === 1) {
    playerScore++;
    updateScores();
    document.getElementById("message").innerHTML = "You won this round!";
  } else if (result === -1) {
    computerScore++;
    document.getElementById("message").innerHTML = "The computer won this round.";
  } else {
    document.getElementById("message").innerHTML = "It's a tie!";
  }
  updateScores();
}


var rockButton = document.getElementById("rock");
rockButton.addEventListener("click", function() {
  playerTurn("rock");
});

var paperButton = document.getElementById("paper");
paperButton.addEventListener("click", function() {
  playerTurn("paper");
});

var scissorsButton = document.getElementById("scissors");
scissorsButton.addEventListener("click", function() {
  playerTurn("scissors");
});

var startover = document.getElementById("start-over");
startover.addEventListener("click", function(){
  startOver();
})

