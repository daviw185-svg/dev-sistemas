document.getElementById('buscar').addEventListener('click', () => {
    let nome = document.getElementById('usuario').value; //Guardar a variável
    fetch(`https://api.github.com/users/${nome}`)
    .then((r) => r.json())
    .then((user) => { //Juntar script com HTML
        document.getElementById('perfil').innerHTML = `
        <img src="${user.avatar_url}" width="120"
        <h3>${user.name || "Sem nome"}</h3>
        <p>${user.bio || "Bio indisponível"}</p>`;
    });
});    
    