export function paginacao_interface_render(data) {
    console.log(data.currentPage)
    document.getElementById("prev-btn").disabled = data.currentPage == 1;
    document.getElementById("next-btn").disabled = !data.has_next;
    document.getElementById(
      "page-info"
    ).textContent = `Page ${data.currentPage} of ${data.total_pages}`;
  }