/**
 * Function handles search bar and filter functionality.
 */
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search");
    const filterForm = document.getElementById("filterForm");
    const categoryFilter = document.getElementById("categoryFilter");
    const cocktails = document.querySelectorAll(".cocktail-item");
    const notFound = document.getElementById("not-found");


    // Filter cocktails based on search input
    if (searchInput) {
        searchInput.addEventListener("input", function() {
            filterCocktails();
    });
    } 
    
    // Filter cocktails based on selected category
    if (filterForm) {
        filterForm.addEventListener("submit", function(e) {
            e.preventDefault();
            filterCocktails();
        });
    }

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

/**
 * Function handles delete "warning" modal 
 */
$(document).ready(function() {
    $('#delete-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget); // Button that triggered the modal
        const itemId = button.data('item-id'); // Extract info from data-* attributes
        const itemType = button.data('item-type');
        const modal = $(this);
        
        // Update the modal's content
        modal.find('#item-type').text(itemType);
        
        // Set the delete button's data attributes
        $('#confirm-delete-btn').data('item-id', itemId);
        $('#confirm-delete-btn').data('item-type', itemType);
    });

    $('#confirm-delete-btn').click(function() {
        const itemId = $(this).data('item-id');
        const itemType = $(this).data('item-type');
        let deleteUrl;

        if (itemType === 'cocktail') {
            deleteUrl = '/delete_cocktail/' + itemId;
        } else if (itemType === 'account') {
            deleteUrl = '/delete_account/' + itemId;
        }

        window.location.href = deleteUrl;
    });
});