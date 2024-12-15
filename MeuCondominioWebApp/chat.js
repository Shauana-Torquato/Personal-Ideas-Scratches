const socket = io();

// Função para enviar uma mensagem
function sendMessage() {
    const messageInput = document.querySelector('.chat-input input');
    const message = messageInput.value;
    socket.emit('chat message', message);
    messageInput.value = '';
}

// Função para adicionar uma nova mensagem à conversa
socket.on('chat message', (msg) => {
    const messagesDiv = document.querySelector('.chat-messages');
    const newMessage = document.createElement('div');
    newMessage.textContent = msg;
    messagesDiv.appendChild(newMessage);
});