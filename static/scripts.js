document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/cars')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('cars-body');
            tbody.innerHTML = '';

            data.forEach(car => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${car.id}</td>
                    <td>${car.make}</td>
                    <td>${car.model}</td>
                    <td>${car.color}</td>
                    <td>${car.year}</td>
                    <td>${car.price}</td>
                    <td>${car.fuel_type}</td>
                    <td>${car.date_created}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

