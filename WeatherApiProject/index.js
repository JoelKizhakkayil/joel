const apiKey = '812aed369640cd1acccbb5853aaddf2b';

function getWeather() {
    const city = document.getElementById('city').value;

    if (!city) {
        alert('Please enter a city');
        return;
    }

    const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}`;

    // then is used when the func runs successfully and catch is used when an error is faced  

    // to catch error faced in fetching weather=>

    fetch(currentWeatherUrl)
        .then(response => response.json())
        .then(data => {
            if (data.cod !== 200) {
                alert(`Error: ${data.message}`);
                throw new Error(`API Error: ${data.message}`);
            }
            displayWeather(data);
        })
        .catch(error => {
            console.error('Error fetching current weather data:', error);
            alert('Error fetching current weather data. Please try again.');
        });

    // to catch error in forecast =>
    fetch(forecastUrl)
        .then(response => response.json())
        .then(data => {
            if (data.cod !== '200') {
                alert(`Error: ${data.message}`);
                throw new Error(`API Error: ${data.message}`);
            }
            displayHourlyForecast(data.list);
        })
        .catch(error => {
            console.error('Error fetching hourly forecast data:', error);
            alert('Error fetching hourly forecast data. Please try again.');
        });
}

function displayWeather(data) {
    const tempDivInfo = document.getElementById('temp-div');
    const weatherInfoDiv = document.getElementById('weather-info');
    const weatherIcon = document.getElementById('weather-icon');
    const hourlyForecastDiv = document.getElementById('hourly-forecast');

    // Clear previous content
    weatherInfoDiv.innerHTML = '';
    hourlyForecastDiv.innerHTML = '';
    tempDivInfo.innerHTML = '';

    if (!data || !data.main || !data.weather) {
        weatherInfoDiv.innerHTML = `<p>Error: Invalid data received</p>`;
        return;
    }

    const cityName = data.name;
    const temperature = Math.round(data.main.temp - 273.15); // Convert to Celsius
    let description = data.weather[0].description; // Get weather description
    const iconCode = data.weather[0].icon;
    const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@4x.png`;

    // Capitalize the first letter of each word in the weather description
    description = description.replace(/\b\w/g, char => char.toUpperCase());

    const temperatureHTML = `<p>${temperature}°C</p>`;
    const weatherHtml = `<p>${cityName}</p><p>${description}</p>`;

    tempDivInfo.innerHTML = temperatureHTML;
    weatherInfoDiv.innerHTML = weatherHtml;
    weatherIcon.src = iconUrl;
    weatherIcon.alt = description;

    showImage();
}

function displayHourlyForecast(hourlyData) {
    const hourlyForecastDiv = document.getElementById('hourly-forecast');

    if (!hourlyData || hourlyData.length === 0) {
        hourlyForecastDiv.innerHTML = '<p>No forecast data available</p>';
        return;
    }

    const next24Hours = hourlyData.slice(0, 8); // Display the next 24 hours (3-hour intervals)

    next24Hours.forEach(item => {
        const dateTime = new Date(item.dt * 1000); // Convert timestamp to milliseconds
        const hour = dateTime.getHours();
        const temperature = Math.round(item.main.temp - 273.15); // Convert to Celsius
        const iconCode = item.weather[0].icon;
        const iconUrl = `https://openweathermap.org/img/wn/${iconCode}.png`;

        const hourlyItemHtml = `
            <div class="hourly-item">
                <span>${hour}:00</span>
                <img src="${iconUrl}" alt="Hourly Weather Icon">
                <span>${temperature}°C</span>
            </div>
        `;

        hourlyForecastDiv.innerHTML += hourlyItemHtml;
    });
}

function showImage() {
    const weatherIcon = document.getElementById('weather-icon');
    weatherIcon.style.display = 'block'; // Make the image visible once it's loaded
}




//