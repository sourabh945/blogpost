document.addEventListener('DOMContentLoaded', () => {
    // Refresh Button
    document.getElementById('refreshBtn').addEventListener('click', () => {
        alert('Refreshing the page...');
        window.location.reload();
    });

    // Search Button
    document.getElementById('searchBtn').addEventListener('click', () => {
        const query = document.getElementById('searchInput').value;
        if (query) {
            alert(`Searching for: ${query}`);
            // Implement actual search logic here
        } else {
            alert('Please enter a search term.');
        }
    });
});
