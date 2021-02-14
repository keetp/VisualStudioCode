// array to hold the todo list items
let todoItems = [];

// function to render the list items to the webpage for the user
function renderTodo(todo) {
    // selecting first element in the list
    const list = document.querySelector('.todo-list');
    // checking if todo object has checked value of true, assigns done if so.
    const isChecked = todo.checked ? 'done':'';
    // creating a list element to display
    const node = document.createElement('li');
    node.setAttribute('class', `todo-item ${isChecked}`);
    node.setAttribute('class',  todo.id);

    node.innerHTML = ` 
    <input id="${todo.id}" type="checkbox"/>
    <label for="${todo.id}" class="tick js-tick"></label>
    <span>${todo.text}</span>
    <button class="delete-todo js-delete-todo">
    <svg><use href="#delete-icon"></use></svg>
    </button>
    
    `;


    list.append(node);
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
    renderTodo(todo);
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