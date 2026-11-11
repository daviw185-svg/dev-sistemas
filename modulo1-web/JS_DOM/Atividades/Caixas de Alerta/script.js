document.addEventListener("DOMContentLoaded", function() {
const caixas = [
    document.getElementById("caixa1"), 
    document.getElementById("caixa2"),
    document.getElementById("caixa3")];
const colors = ["red", "purple", "blue", "orange"];

// Função Auxiliar: pega índice da cor atual e retornar para a próxima
 function proximaCorAtual(element) { 
    const estilo = getComputedStyle(element); 
    const bg = estilo.backgroundColor; // retorna rgb(...) 
   
    // tenta mapear rgb para nome aproximado por comparação simples com colors definidas 
    for (let c of colors) { 
      const temp = document.createElement("div"); 
      temp.style.background = c; 
      document.body.appendChild(temp); 
      const comp = getComputedStyle(temp).backgroundColor; 
      document.body.removeChild(temp); 
      if (comp === bg) { 
        
        // encontrou; retorna próxima cor do array 
        const idx = colors.indexOf(c); 
        return colors[(idx + 1) % colors.length]; 
      } 
    } 
    
    // se não identificou, retorna primeira cor 
    return colors[0]; 
  } 
 
  caixas.forEach((caixa, index) => { 
    if (!caixa) return; 
 
    // dblclick: trocar cor e alert com o nome 
    caixa.addEventListener("dblclick", function() { 
      const nova = proximaCorAtual(this); 
      this.style.background = nova; 
      alert(`Cor alterada para: ${nova}`); 
      console.log("this (elemento que disparou dblclick):", this); 
    }); 
 
    // clique simples via arrow function para demonstrar this herdado 
    caixa.addEventListener("click", () => { 
      console.log("Arrow function this (não é o elemento):", this); 
    }); 
  });

});