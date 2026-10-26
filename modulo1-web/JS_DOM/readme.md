# Criando elementos com Javascript

Sintaxe:

```
const novoElemento = document.createElement("tagName");
```

tagName : Uma string que especifica o tipo de elemento a ser criado (ex: "div",
"p", "li", "button").

O método createElement() cria um novo nó de elemento, mas ele não o adiciona
automaticamente à página. Ele apenas o cria na memória. Para que o elemento apareça
na página, ele precisa ser anexado a um elemento existente no DOM.
Exemplo:

```
const novaDiv = document.createElement("div");
console.log(novaDiv); //Saída: <div></div> (elemento na memória)

const novoParagrafo = document.createElement("p");
novoParagrafo.textContent = "Este é um parágrafo criado dinamicamente.";
console.log(novoParagrafo); // Saída: <p>Este é um parágrafo criado
dinamicamente.</p>
```

# Adicionando elementos na página
Depois de criar um elemento, você precisa adicioná-lo como filho de um elemento
existente no DOM para que ele seja exibido na página. Os métodos mais comuns para
isso são appendChild() e insertBefore() .

Exemplo com appendChild() :
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adicionar Elementos</title>
</head>
<body>
<h1>Lista de Compras</h1>
<ul id="lista">
<li>Pão</li>
<li>Leite</li>
</ul>
<button id="adicionarItem">Adicionar Fruta</button>
<script>
const lista = document.querySelector("#lista");
const botaoAdicionar = document.querySelector("#adicionarItem");
botaoAdicionar.addEventListener("click", function() {
const novoItem = document.createElement("li"); // Cria um novo <li>
novoItem.textContent = "Fruta"; // Define o texto do item
lista.appendChild(novoItem); // Adiciona o novo <li> como último filho

da <ul>
});
</script>
</body>
</html>
```

Exemplo com insertBefore() :
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Inserir Antes</title>
</head>

<body>
<h1>Minha Lista</h1>
<ul id="minhaLista">
<li id="item2">Item 2</li>
<li>Item 3</li>
</ul>
<button id="inserirPrimeiro">Inserir Item 1</button>
<script>
const minhaLista = document.querySelector("#minhaLista");
const item2 = document.querySelector("#item2");
const botaoInserir = document.querySelector("#inserirPrimeiro");
botaoInserir.addEventListener("click", function() {
const novoItem1 = document.createElement("li");
novoItem1.textContent = "Item 1";
minhaLista.insertBefore(novoItem1, item2); // Insere novoItem1

antes de item2
});
</script>
</body>
</html>
```
