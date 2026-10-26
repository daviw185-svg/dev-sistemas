const cidade = document.getElementById('cidade');
const btnbuscar = document.getElementById('buscar');
const resultado = document.getElementById('resultado');

btnbuscar.addEventListener("click", () => {
    const [lat, lon] = cidade.value.split(",");
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;
    fetch(url)
        .then((resposta) => resposta.json())    
        .then(data => {
        const temp = data.current_weather.temperature;
        resultado.innerHTML = `
            <h2>${cidade.options[cidade.selectedIndex].text}</h2>
            <p>Temperatura: ${temp} °C</p>
        `;
})
});