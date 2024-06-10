document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search');
    const cocktails = document.querySelectorAll('.cocktail-card');
    const notFound = document.getElementById('not-found');

    searchInput.addEventListener('input', function() {
        const searchValue = this.value.trim().toLowerCase();
        let hasResults = false;

        cocktails.forEach(function(card) {
            const cocktailName = card.querySelector('.cocktail-name').textContent.trim().toLowerCase();
            const cocktailCategory = card.querySelector('.cocktail-category').textContent.trim().toLowerCase();

            const matchesSearch = cocktailName.includes(searchValue) || cocktailCategory.includes(searchValue);

            if (matchesSearch) {
                card.style.display = 'block';
                hasResults = true;
            } else {
                card.style.display = 'none';
            }
        });

        notFound.style.display = hasResults ? 'none' : 'block';
    });
});