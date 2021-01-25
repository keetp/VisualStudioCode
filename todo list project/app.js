// array to hold the todo list items
let todoItems = [];

// function to render the list items to the webpage for the user
function displayTodo(todo) {
    // selecting first element in the list
    const list = document.querySelector('.todo-list');
    // need to figure out how to implement this, in over my head
}



// function to create a new todo object based on the 
// text that was entered in the text input, and push it
// onto the 'todoItems' array
function addTodo(text){
    const todo ={
        text,
        checked:false,
        id: Date.now(),
    };

    todoItems.push(todo);
    console.log(todoItems)
    //    displayTodo(todo);
}


// selecting the form element
const form = document.querySelector('.todo-form');
// adding a submit event listener
form.addEventListener('submit', event => {
    // stops page refresh
    event.preventDefault();
    // selecting the text input
    const input = document.querySelector('.todo-input');

    const text = input.value.trim();
    if (text !== ''){
        addTodo(text);
        input.value='';
        input.focus();
    }
});