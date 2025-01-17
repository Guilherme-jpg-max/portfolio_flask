document.addEventListener("DOMContentLoaded", function () {
    function sendContactForm(event) {
        event.preventDefault();

        const form = document.getElementById("contact-form");
        const formData = new FormData(form);
        const flashContainer = document.getElementById("flash-container");
        const submitButton = form.querySelector('button[type="submit"]');

        // Limpa os campos do formulário imediatamente após o clique
        form.reset();

        // Desabilita o botão de envio para evitar múltiplos envios
        submitButton.disabled = true;

        fetch("/contact", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json()) 
            .then((data) => {
                if (data.success) {
                    showFlashMessage(data.message, "success", flashContainer);
                } else {
                    showFlashMessage(data.message, "error", flashContainer);
                }
            })
            .catch(() => {
                showFlashMessage("Erro ao enviar a mensagem. Verifique sua conexão.", "error", flashContainer);
            })
            .finally(() => {
                submitButton.disabled = false;
            });
    }

    function showFlashMessage(message, category, container) {
        const flashMessage = document.createElement("div");
        flashMessage.className = `flash-messages ${category}`; // Sucesso ou erro
        flashMessage.innerHTML = `
            ${message}
            <button class="close-btn">&times;</button>
        `;
        
        container.appendChild(flashMessage);
        
        flashMessage.querySelector(".close-btn").addEventListener("click", function () {
            flashMessage.remove();
        });
        
        // Remove automaticamente após 5 segundos
        setTimeout(() => {
            flashMessage.classList.add("fade-out");
            setTimeout(() => flashMessage.remove(), 300); // Remove após a animação
        }, 3000);
    }

    const form = document.getElementById("contact-form");
    if (form) {
        form.addEventListener("submit", sendContactForm);
    }
});
