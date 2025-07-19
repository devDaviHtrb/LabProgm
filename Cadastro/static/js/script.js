function validarEmail(email) {
  const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  return regex.test(email);
}
function validacao(event) {
  let dados = [
    document.getElementById("username").value,
    document.getElementById("password").value,
    document.getElementById("email").value,
  ];
  var status = true;
  for (dado of dados) {
    if (dado.length < 1) {
      status = false;
      break;
    }
  }
  if (validarEmail(dados[2]) == false) {
    status = false;
  }
  if (status == true) {
    console.log("foi");
  } else {
    event.preventDefault();
    document.getElementById("status").innerText =
      "Erro de validação, verifique o formato de seus dados";
  }
}

let form = document.querySelector("form");
form.addEventListener("submit", validacao);
