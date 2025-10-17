export function renderProdutos(data) {
    const produtos = document.getElementById("produtos");
    produtos.innerHTML = "";
    console.log(data.Error);
  
    if (data.Error) {
      console.log("odf");
      produtos.innerHTML = `<p>${data.Error}</p>`;
    }
  
    data.produtos.forEach((produto) => {
      produtos.innerHTML += `
        <li>
          <h3>${produto.nome}</h3>
          <a href="/detalhe_produto/${produto.id}"> pagina </a> 
    
        </li>`;
    });
  
    document.querySelectorAll(".join-auction").forEach((btn) => {
      btn.addEventListener("click", (e) => joinRoom(e));
    });
  }