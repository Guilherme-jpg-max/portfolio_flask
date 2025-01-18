document.addEventListener("DOMContentLoaded", function() {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll("nav ul li a");

    // Função para atualizar a classe "active"
    function setActiveLink() {
        let currentSection = "";

        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 0 && rect.bottom >= 0) {
                currentSection = section.id;
            }
        });

        navLinks.forEach(link => {
            if (link.getAttribute("href").includes(currentSection)) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        });
    }

    // Chama a função inicialmente
    setActiveLink();

    // Adiciona o evento de rolagem para atualizar a seção ativa
    window.addEventListener("scroll", setActiveLink);

    // Função para alternar o menu hambúrguer
    function toggleMenu() {
        const menu = document.querySelector('nav ul');
        menu.classList.toggle('active');
    }

    // Adiciona o evento de clique no menu hambúrguer
    const menuHamburguer = document.querySelector('.menu-hamburguer');
    if (menuHamburguer) {
        menuHamburguer.addEventListener('click', toggleMenu);
    }
});
