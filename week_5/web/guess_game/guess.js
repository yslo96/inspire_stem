const randomNumber = Math.floor(Math.random() * 100)
console.log(randomNumber)
let attempt = 1;

function checkGuess(){
    const guess = parseInt(document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess) || guess < 1 || guess > 100){
        setMessage("Please a valid number between 1 and 100")
        return;
    }
    if(guess === randomNumber){
        setMessage("NIGGA umeomoka")
        document.getElementById("guessField").disable = true;
    }else if(guess < randomNumber){
        setMessage("Changamka bana")
    }else(
        setMessage("Punguza pace")
    )
}
function setMessage(message){
    document.getElementById("message").textContent = message
}