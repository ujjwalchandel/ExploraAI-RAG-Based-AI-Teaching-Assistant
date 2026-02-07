function toggleChat() {
    const bot = document.getElementById("chatbot");
    bot.style.display = bot.style.display === "block" ? "none" : "block";
}

function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value.trim();
    if (text === "") return;

    addMessage(text, "user-msg");
    input.value = "";

    setTimeout(() => {
        const reply = getBotReply(text);
        addMessage(reply, "bot-msg");
    }, 800);
}

function addMessage(text, className) {
    const chatBody = document.getElementById("chatBody");
    const msg = document.createElement("div");
    msg.className = className;
    msg.innerText = text;
    chatBody.appendChild(msg);
    chatBody.scrollTop = chatBody.scrollHeight;
}

/* Smart Reply System */
function getBotReply(message) {
    message = message.toLowerCase();
    if(message === "")
        return;

    fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "query": message })
    })
    .then(response => response.json())
    .then(data => alert("Server says: " + data.message));

}