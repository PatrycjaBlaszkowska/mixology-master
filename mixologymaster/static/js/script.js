document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search");
    const filterForm = document.getElementById("filterForm");
    const categoryFilter = document.getElementById("categoryFilter");
    const cocktails = document.querySelectorAll(".cocktail-item");
    const notFound = document.getElementById("not-found");

    // Filter cocktails based on search input
    searchInput.addEventListener("input", function() {
        const searchValue = this.value.trim().toLowerCase();
        filterCocktails(searchValue, categoryFilter.value.toLowerCase());
    });

    // Filter cocktails based on selected category
    filterForm.addEventListener("submit", function(e) {
        e.preventDefault();
        filterCocktails(searchInput.value.trim().toLowerCase(), categoryFilter.value.toLowerCase());
    });

    function filterCocktails(searchValue, selectedCategory) {
        let hasResults = false;

        cocktails.forEach(function(card) {
            const cocktailName = card.querySelector(".cocktail-name").textContent.trim().toLowerCase();
            const cocktailCategory = card.getAttribute("data-category").toLowerCase();

            const matchesSearch = cocktailName.includes(searchValue);
            const matchesCategory = selectedCategory === "" || cocktailCategory === selectedCategory;

            if (matchesSearch && matchesCategory) {
                card.style.display = "block";
                hasResults = true;
            } else {
                card.style.display = "none";
            }
        });

        notFound.style.display = hasResults ? "none" : "block";
    }
});