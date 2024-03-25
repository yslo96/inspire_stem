// Data Types:
/* //Multiline Comment In Javascript
1. String
2. Integers/numbers
3. Booleans
4. Array

*/
let name = "Lawrence"
let height = 50

//Onclick Events
//Element Selector In JS
function submit(){
    var input = document.getElementById("inputField").value;
    var input = parseInt(input);
    var input = input + 1;
    console.log(input)
}

//Boolean data type
let adult = true;
let fruits = ['kiwi', 'pineapple', 'apple', 30, false]//Array or a list
let person = {
    Firstname: 'Ada',
    Secondname: 'Lovelace',
    Age: 18,
    Address: {
        country: 'Sudan',
        city: 'Khartoum',
        street: 'Bani bani',
    },
    children: ['Kelly' ,'Mary']
}

function saveItem(){
    var input = document.getElementById("inputField").value;
    localStorage.setItem('inputField', item)
    showWelcomeMessage(input)
}    

function showWelcomeMessage(input){
    var messageElement = document.getElementById("show message")
    messageElement.textContent = "We have save your input as"+ input
}

var storedItem = localStorage.getItem('inputItem');
if(storedItem){
    showWelcomeMessage(storedItem)
}