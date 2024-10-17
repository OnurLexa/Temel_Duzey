document.getElementById("ekleButton").addEventListener("click", function() {
    const notInput = document.getElementById("notInput");
    const notText = notInput.value.trim();

    if (notText) {
        const li = document.createElement("li");
        li.textContent = notText;

        const silButton = document.createElement("button");
        silButton.textContent = "Sil";
        silButton.addEventListener("click", function() {
            li.remove();
        });

        li.appendChild(silButton);
        document.getElementById("notlarListesi").appendChild(li);
        notInput.value = "";
    }
});
