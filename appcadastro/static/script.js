function adicionarProduto() {
    const numeroEncomenda = document.getElementById("numeroEncomenda").value;
    const dataRecebimento = document.getElementById("dataRecebimento").value;
    const horaRecebimento = document.getElementById("horaRecebimento").value;
    const observacoes = document.getElementById("observacoes").value;

    const tabela = document.getElementById("produtoTableBody");
    const novaLinha = tabela.insertRow();

    novaLinha.innerHTML = `
        <td>${numeroEncomenda}</td>
        <td>${dataRecebimento} ${horaRecebimento}</td>
        <td>${observacoes}</td>
        <td><input type="checkbox" name="entregue" id="entregue"></td>
        <td><input type="button" onclick="removerProduto()">Remover Produto</buttonRemove></td>
    `;

    document.getElementById("produtoForm").reset();
}

function removerProduto() {
    const tabela = document.getElementById("produtoTableBody");
    if (tabela.rows.length > 0) {
        tabela.deleteRow(tabela.rows.length - 1); 
    } else {
        alert("Nenhum produto para remover.");
    }
}