// Selecionar todos os cards
const skills = document.querySelectorAll('.skill');

skills.forEach(skill => {
  skill.addEventListener('click', () => {
    // Verifica se o card já está expandido
    const isExpanded = skill.classList.contains('expanded');
    
    // Remove a classe expanded de todos os cards
    skills.forEach(s => s.classList.remove('expanded'));
    
    // Esconde todas as descrições
    skills.forEach(s => {
      const description = s.querySelector('.skill-description');
      if (description) description.classList.remove('active');
    });

    // Se o card não estava expandido, expanda e mostre a descrição
    if (!isExpanded) {
      skill.classList.add('expanded');
      const description = skill.querySelector('.skill-description');
      if (description) description.classList.add('active');
    }
  });
});
