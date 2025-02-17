function callPython() {
    const userInput = document.getElementById("user-input").value;
    const chatDiv = document.getElementById("chat");

    // Display user's message
    chatDiv.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    // Send user input to the backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then((response) => response.json())
    .then((data) => {
        // Display chatbot's response
        chatDiv.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        // Scroll to the bottom of the chat
        chatDiv.scrollTop = chatDiv.scrollHeight;
    })
    .catch((error) => {
        console.error("Error:", error);
    });

    // Clear the input field
    document.getElementById("user-input").value = "";
}