let currentPage = 1;

import { loadProducts } from "../interactivity/Paginar.js";
import { getPresquisa } from "../api/GetPesquisa.js";
document.addEventListener("DOMContentLoaded", async () => {
    await loadProducts(currentPage);
});

document.getElementById("prev-btn").addEventListener("click", async () => {
        currentPage--;
        await loadProducts(currentPage);
    
});

document.getElementById("next-btn").addEventListener("click", async () => {
        currentPage++;
        await loadProducts(currentPage);
    
});

document.getElementById("btn_pesquisa").addEventListener("click", async (e)=>{
    e.preventDefault()
    let data = await getPresquisa()
   
    document.getElementById("resultado").innerHTML = "<h1>Resultados:</h1>"
    if (data.produtos.length == 0){
     document.getElementById("resultado").innerHTML = "<h1>Nenhum produto correspondente</h1>"}
    data.produtos.forEach((produto) => {
        document.getElementById("resultado").innerHTML += `
          <li>
            <h3>${produto.nome}</h3>
            <a href="/detalhe_produto/${produto.id}"> pagina </a> 
      
          </li>`;
      });

})


