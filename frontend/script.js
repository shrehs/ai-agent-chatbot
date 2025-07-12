const chatBox = document.getElementById("chat");
const input = document.getElementById("message");

async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  chatBox.innerHTML += `🧑‍💻 You: ${message}\n`;

  try {
    const response = await fetch("http://localhost:8000/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  });

    const data = await response.json();

    if (data.response) {
      chatBox.innerHTML += `🤖 AI: ${data.response}\n\n`;
    } else {
      chatBox.innerHTML += `⚠️ Error: ${data.error || "Unknown error"}\n\n`;
    }

  } catch (error) {
    chatBox.innerHTML += `❌ Network Error: ${error.message}\n\n`;
  }

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function resetChat() {
  try {
    await fetch("http://localhost:8000/api/reset", { method: "POST" });
    chatBox.innerHTML += `🧹 Chat history cleared.\n\n`;
  } catch (error) {
    chatBox.innerHTML += `❌ Reset failed: ${error.message}\n\n`;
  }
}
