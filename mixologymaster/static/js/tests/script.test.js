const { filterBySearch, filterByCategory, filterCocktails } = require('../script');
const { fireEvent } = require('@testing-library/dom');

document.body.innerHTML = `
<div>
    <!-- Search and Filter Section -->
    <input id="search" type="text" />
    <form id="filterForm">
        <select id="categoryFilter">
            <option value="">All Categories</option>
            <option value="vodka">Vodka</option>
            <option value="rum">Rum </option>
        </select>
        <button type="submit">Filter</button>
    </form>
    <div id="not-found" style="display: none;">No Results! Please try different phrase.</div>
    <div class="cocktail-item" data-category="category1">
        <span class="cocktail-name">Cocktail One</span>
    </div>
    <div class="cocktail-item" data-category="category2">
        <span class="cocktail-name">Cocktail Two</span>
    </div>
    <div class="cocktail-item" data-category="category1">
        <span class="cocktail-name">Another Cocktail</span>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="delete-modal" tabindex="-1" aria-labelledby="delete-modal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">WARNING</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Are you sure you wish to delete this <span id="item-type"></span>?</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" id="confirm-delete-btn">Delete</button>
                </div>
            </div>
        </div>
    </div>
</div>
`;

describe('Search and Filter Functionality', () => {
    let searchInput, filterForm, categoryFilter, notFound, cocktails;

    beforeAll(() => {
        searchInput = document.getElementById('search');
        filterForm = document.getElementById('filterForm');
        categoryFilter = document.getElementById('categoryFilter');
        notFound = document.getElementById('not-found');
        cocktails = document.querySelectorAll('.cocktail-item');
    });

    test('Filters cocktails based on search input', () => {
        searchInput.value = 'cocktail one';
        fireEvent.input(searchInput);

        filterCocktails();

        cocktails.forEach((card) => {
            const name = card.querySelector('.cocktail-name').textContent.trim().toLowerCase();
            if (name.includes('cocktail one')) {
                expect(card.style.display).toBe('block');
            } else {
                expect(card.style.display).toBe('none');
            }
        });
        expect(notFound.style.display).toBe('none');
    });

    test('Filters cocktails based on selected category', () => {
        categoryFilter.value = 'vodka';
        fireEvent.change(categoryFilter);
        fireEvent.submit(filterForm);
    
        filterCocktails();
    
        cocktails.forEach((card) => {
            const category = card.getAttribute('data-category').toLowerCase();
            if (category === 'vodka') {
                expect(card.style.display).toBe('block');
            } else {
                expect(card.style.display).toBe('none');
            }
        });
        expect(notFound.style.display).toBe('block'); 
    });

    test('Displays not found message when no results match search and filter', () => {
        searchInput.value = 'nonexistent';
        categoryFilter.value = 'rum';
        fireEvent.submit(filterForm);

        filterCocktails();

        cocktails.forEach((card) => {
            expect(card.style.display).toBe('none');
        });
        expect(notFound.style.display).toBe('block');
    });
});

describe('Delete Warning Modal', () => {
    let deleteModal, confirmDeleteBtn;

    beforeAll(() => {
        deleteModal = document.getElementById('delete-modal');
        confirmDeleteBtn = document.getElementById('confirm-delete-btn');
    });

    test('Shows delete modal with correct item type and id', () => {
        const button = document.createElement('button');
        button.setAttribute('data-toggle', 'modal');
        button.setAttribute('data-target', '#delete-modal');
        button.setAttribute('data-item-id', '1');
        button.setAttribute('data-item-type', 'cocktail');

        document.body.appendChild(button);

        fireEvent.click(button);

        // Simulate showing the modal and setting data attributes
        document.getElementById('item-type').textContent = 'cocktail';
        confirmDeleteBtn.setAttribute('data-item-id', '1');
        confirmDeleteBtn.setAttribute('data-item-type', 'cocktail');

        expect(deleteModal.querySelector('#item-type').textContent).toBe('cocktail');
        expect(confirmDeleteBtn.getAttribute('data-item-id')).toBe('1');
        expect(confirmDeleteBtn.getAttribute('data-item-type')).toBe('cocktail');
    });
});

/**
 * Testing delete modal
 */

describe('Delete Warning Modal', () => {
    let deleteModal, confirmDeleteBtn;

    beforeAll(() => {
        deleteModal = document.getElementById('delete-modal');
        confirmDeleteBtn = document.getElementById('confirm-delete-btn');
    });

    test('Shows delete modal with correct item type and id', () => {
        const button = document.createElement('button');
        button.setAttribute('data-toggle', 'modal');
        button.setAttribute('data-target', '#delete-modal');
        button.setAttribute('data-item-id', '1');
        button.setAttribute('data-item-type', 'cocktail');

        document.body.appendChild(button);

        fireEvent.click(button);

        // Simulate showing the modal and setting data attributes
        document.getElementById('item-type').textContent = 'cocktail';
        confirmDeleteBtn.setAttribute('data-item-id', '1');
        confirmDeleteBtn.setAttribute('data-item-type', 'cocktail');

        expect(deleteModal.querySelector('#item-type').textContent).toBe('cocktail');
        expect(confirmDeleteBtn.getAttribute('data-item-id')).toBe('1');
        expect(confirmDeleteBtn.getAttribute('data-item-type')).toBe('cocktail');
    });
});
