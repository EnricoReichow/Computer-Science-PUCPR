function gravar() {

    var form = document.getElementById('formCadastro');
    var dados = new FormData(form)

    fetch("php/gravar.php", {
        method: "POST",
        body: dados
    });
}