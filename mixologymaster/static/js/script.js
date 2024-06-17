document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search");
    const filterForm = document.getElementById("filterForm");
    const categoryFilter = document.getElementById("categoryFilter");
    const cocktails = document.querySelectorAll(".cocktail-item");
    const notFound = document.getElementById("not-found");

    // Filter cocktails based on search input
    searchInput.addEventListener("input", function() {
        filterCocktails();
    });

    // Filter cocktails based on selected category
    filterForm.addEventListener("submit", function(e) {
        e.preventDefault();
        filterCocktails();
    });

    function filterBySearch(cocktail, searchValue) {
        const cocktailName = cocktail.querySelector(".cocktail-name").textContent.trim().toLowerCase();
        return cocktailName.includes(searchValue);
    }

    function filterByCategory(cocktail, selectedCategory) {
        const cocktailCategory = cocktail.getAttribute("data-category").toLowerCase();
        return selectedCategory === "" || cocktailCategory === selectedCategory;
    }

    function filterCocktails() {
        const searchValue = searchInput.value.trim().toLowerCase();
        const selectedCategory = categoryFilter.value.toLowerCase();
        let hasResults = false;

        cocktails.forEach(function(card) {
            const matchesSearch = filterBySearch(card, searchValue);
            const matchesCategory = filterByCategory(card, selectedCategory);

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