export async function getPresquisa() {
    const endpoint = `/api/buscar_produto/${document.getElementById("pesquisa").value}`;
    
    const response = await fetch(endpoint);
    if (!response.ok) {
      throw new Error("query error");
    }
    
    return await response.json();
  }
  