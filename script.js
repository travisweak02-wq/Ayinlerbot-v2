
// AYINLERBOT V2
// Website interaction system

console.log("AYINLERBOT V2 initialized!");

function showMessage() {
    const message = document.getElementById("message");

    message.textContent =
        "🤖 Welcome, Agent! AYINLERBOT V2 is ready.";

    message.style.color = "#35e88a";
}

function updateStatus() {
    const status = document.querySelector(".status");

    if (status) {
        status.textContent = "● SYSTEM READY";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    updateStatus();

    console.log("Cyber interface loaded successfully.");
});
