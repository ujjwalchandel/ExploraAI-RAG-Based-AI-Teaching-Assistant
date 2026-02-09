function toggleChat() {
    const bot = document.getElementById("chatbot");
    bot.style.display = bot.style.display === "block" ? "none" : "block";
}

function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value.trim();
    if (text === "") return;

    addMessage(text, "user-msg");
    input.value = "";
 
    try {
        const response = await getBotReply(text); // This "unwraps" the promise
        
        // Assuming Flask returns: jsonify({"message": "Hello!"})
        const reply = response.message; 
        
        addMessage(reply, "bot-msg");
    } catch (error) {
        console.error("Error fetching reply:", error);
        addMessage("Server error. Please try again.", "bot-msg");
    }
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
async function getBotReply(message) {
    message = message.toLowerCase();
    if(message === "")
        return;

    const response = await fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ "query": message })
    })
    return await response.json();

}