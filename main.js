function changeText() {
    const textElement = document.getElementById("text-element")
    textElement.textContent = "Текст был изменен!"
}

function addText() {
    const textElement = document.getElementById("text-element")
    textElement.textContent += " (дополнено)"
}

function resetText() {
    const textElement = document.getElementById("text-element")
    textElement.textContent = "Исходный текст этого параграфа"
}

function safeOutput() {
    const userInput = document.getElementById("user-input")
    const output =  document.getElementById("safe-output")
    output.textContent = userInput.value
}

function unsafeOutput() {
    const userInput = document.getElementById("user-input")
     const output =  document.getElementById("safe-output")
    output.innerHTML = userInput.value
}


function addSimpleContent() {
    const dynamicContent = document.getElementById('dynamic-content');
    const newParagraph = document.createElement('p');
    newParagraph.textContent = 'Новый текстовый блок';
    dynamicContent.appendChild(newParagraph);
}

function addHTMLContent() {
    const dynamicContent = document.getElementById('dynamic-content');
    
    const newDiv = document.createElement('div');
    newDiv.innerHTML = `
        <h1>Новый заголовок</h1>
        <p>Это параграф в новом блоке.</p>
        <ul>
            <li>Элемент списка 1</li>
            <li>Элемент списка 2</li>
            <li>Элемент списка 3</li>
        </ul>
    `;
    
    dynamicContent.appendChild(newDiv);
}

function clearContent() {
    const dynamicContent = document.getElementById('dynamic-content');
    dynamicContent.innerHTML = '';
}


function changeColor() {
    const styleDemo = document.getElementById('style-demo');
    styleDemo.style.backgroundColor = 'lightblue';
}

function changeSize() {
    const styleDemo = document.getElementById('style-demo');
    styleDemo.style.width = '300px';
    styleDemo.style.height = '100px';
}

function addBorder() {
    const styleDemo = document.getElementById('style-demo');
    styleDemo.style.borderRadius = '10px';
    styleDemo.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
}

function resetStyles() {
    const styleDemo = document.getElementById('style-demo');
    styleDemo.style.cssText = 'padding: 20px; border: 1px solid black;';
}

function updateName() {
    const nameInput = document.getElementById('name-input').value;
    const userName = document.getElementById('user-name');
    if (nameInput) {
        userName.textContent = nameInput;
    }
}

function updateTitle() {
    const titleInput = document.getElementById('title-input').value;
    const userTitle = document.getElementById('user-title');
    if (titleInput) {
        userTitle.textContent = titleInput;
    }
}

function updateBio() {
    const bioInput = document.getElementById('bio-input').value;
    const userBio = document.getElementById('user-bio');
    if (bioInput) {
        userBio.textContent = bioInput;
    }
}

function highlightProfile() {
    const userProfile = document.getElementById('user-profile');
    userProfile.style.cssText = "padding: 20px; border: 1px solid red;";
}

function resetProfile() {
    document.getElementById('user-name').textContent = 'Иван Иванов';
    document.getElementById('user-title').textContent = 'Студент';
    document.getElementById('user-bio').textContent = 'Люблю изучать JavaScript';

    document.getElementById('name-input').value = '';
    document.getElementById('title-input').value = '';
    document.getElementById('bio-input').value = '';
    
    const userProfile = document.getElementById('user-profile');
    userProfile.style.cssText = ""
}



