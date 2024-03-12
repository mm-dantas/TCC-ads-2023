const chatbotToggler = document.querySelector(".chatbot-toggler");
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));


function checkEnter(event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  }

function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    var chatbox = document.getElementById('chatbox');
    
    // Verificar se o usuário digitou "1"
    if (userInput.trim() === "menu") {
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            
            chatbox.scrollTop = chatbox.scrollHeight;
        });
        
        var initialMessage = "Olá! Eu sou o chatbot Rafael.</br><br>Digite: <br><b>1. </b> Caso você já seja um estudante da Etec de Guarulhos<br><b>2. </b> Caso você seja um vestibulando.";
        chatbox.innerHTML += '<p class="user-message">' + userInput + '</p>';
        chatbox.innerHTML += '<p class="bot-message">' + initialMessage + '</p>';
        
        
        
    } else {
        // Caso contrário, enviar a entrada do usuário para o servidor
        chatbox.innerHTML += '<p class="user-message">' + userInput + '</p>';
        
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            chatbox.innerHTML += '<p class="bot-message">' + data.message + '</p>';
            chatbox.scrollTop = chatbox.scrollHeight;
        });
    }
    
    document.getElementById('user-input').value = '';
}

