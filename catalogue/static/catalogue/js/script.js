document.getElementById('search-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const searchParams = new URLSearchParams(formData);

    const resultsArea = document.getElementById('results-area');
    const noResults = document.getElementById('no-results');
    const resultsTable = document.getElementById('results-table');
    const loadingSpinner = document.getElementById('loading-spinner');

    // Show loading, hide others
    loadingSpinner.classList.remove('hidden');
    resultsTable.classList.add('hidden');
    noResults.classList.add('hidden');
    resultsArea.innerHTML = '';

    fetch(`/api/search/?${searchParams.toString()}`)
        .then(response => response.json())
        .then(data => {
            loadingSpinner.classList.add('hidden'); // Hide loading

            resultsArea.innerHTML = ''; // Clear again just in case

            if (data.results.length === 0) {
                noResults.classList.remove('hidden');
                resultsTable.classList.add('hidden');
            } else {
                noResults.classList.add('hidden');
                resultsTable.classList.remove('hidden');

                data.results.forEach(plant => {
                    const row = document.createElement('tr');

                    const imageUrl = plant.image_url || 'https://placehold.co/100x100/e8f5e9/2e7d32?text=No+Img';

                    row.innerHTML = `
                        <td>
                            <img src="${imageUrl}" alt="Plant" class="table-thumb">
                        </td>
                        <td><strong>${plant.barcode}</strong></td>
                        <td>${plant.family}</td>
                        <td><i>${plant.genus}</i></td>
                        <td><i>${plant.species}</i></td>
                        <td>
                            <a href="/herbarium/${plant.barcode}/" class="view-btn">View ➡</a>
                        </td>
                    `;

                    resultsArea.appendChild(row);
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("Something went wrong with the search! 🥀");
        });
});
