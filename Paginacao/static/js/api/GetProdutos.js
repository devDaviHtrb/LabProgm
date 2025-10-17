export async function getProdutoos(page = 1) {
    const endpoint = `/produtos_paginados/${page}`;
    
    const response = await fetch(endpoint);
    if (!response.ok) {
      throw new Error("query error");
    }
    
    return await response.json();
  }
  