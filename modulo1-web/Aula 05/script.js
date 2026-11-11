document.getElementById('buscar').addEventListener('click', () => {
    const resultado = document.getElementById('resultado')
    const cep = document.getElementById('cep').value; //Guardar a variável
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then((resposta) => {
        return (resposta).json();    
    })
    .then((dados) => { //Juntar script com HTML
            document.getElementById('lodoro').innerHTML = 
            dados.logradouro
            document.getElementById('bairro').innerHTML = 
            dados.bairro
            document.getElementById('cidade').innerHTML = 
            dados.localidade
            document.getElementById('uf').innerHTML = 
            dados.uf
    })
    .catch(resultado => {
            resultado.innerHTML= `<p>CEP inválido. O CEP precisa conter 8 números</p>`;
            console.error(resultado);
    })
        
});    
     