document.getElementById("generateEmailBtn").addEventListener("click", function() {
    fetch("/generate")
        .then(response => response.json())
        .then(data => {
            document.getElementById("email").textContent = `Generated Email: ${data.email}`;
            document.getElementById("sendEmailSection").style.display = "block";
        });
});

document.getElementById("sendEmailBtn").addEventListener("click", function() {
    const email = document.getElementById("sendToEmail").value;
    const message = document.getElementById("message").value;

    fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, message: message })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchInbox();
    });
});

function fetchInbox() {
    fetch("/inbox/example@tempmail.com")
        .then(response => response.json())
        .then(data => {
            const inboxMessages = data.inbox;
            const inboxList = document.getElementById("inboxMessages");
            inboxList.innerHTML = "";
            inboxMessages.forEach(message => {
                const li = document.createElement("li");
                li.textContent = message;
                inboxList.appendChild(li);
            });
            document.getElementById("inboxSection").style.display = "block";
        });
}
