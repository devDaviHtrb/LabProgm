import { getProdutoos } from "../api/GetProdutos.js";
import { renderProdutos } from "../ui/renderProdutos.js";
import { paginacao_interface_render } from "../ui/Paginacao.js";

export async function loadProducts(page = 1) {
  try {
    const data = await getProdutoos(page);
    renderProdutos(data);
    paginacao_interface_render(data, data.current_page);
    return data.currentPage;
  } catch (err) {
    console.error(err);
    return page;
  }
}