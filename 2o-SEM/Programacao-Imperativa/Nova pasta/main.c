// incluindo bibliotecas
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// cria as constantes necessárias
#define MAX_VENDORES 100
#define MAX_PRODUTOS 100
#define MAX_VENDAS 1000

// struct para representar um produto
typedef struct {
  int codigo;
  float preco;
  char descricao[100];
} Produto;

// struct para representar um vendedor
typedef struct {
  int codigo;
  char nome[100];
} Vendedor;

// struct para representar uma venda
typedef struct {
  int codigoVendedor;
  int codigoProduto;
  int unidadesVendidas;
} Venda;

int main() {
  // lê os vendedores do arquivo vendedores.txt
  FILE *fileVendedores = fopen("vendedores.txt", "r");
  int numVendedores;

  // utiliza a função fscanf para ler um valor inteiro do arquivo
  // "fileVendedores" e armazena na variável numVendedores
  fscanf(fileVendedores, "%d", &numVendedores);
  Vendedor vendedores[MAX_VENDORES];

  // set uma posição no array vendedores com a estrutura de vendedor, utilizando
  // os respectivos codigos e nomes
  for (int i = 0; i < numVendedores; i++) {
    fscanf(fileVendedores, "%d %s", &vendedores[i].codigo, vendedores[i].nome);
  }
  fclose(fileVendedores);

  // lê os produtos do arquivo produtos.txt
  FILE *fileProdutos = fopen("produtos.txt", "r");
  int numProdutos;
  fscanf(fileProdutos, "%d", &numProdutos);
  Produto produtos[MAX_PRODUTOS];
  // faz a mesma lógica do array de vendedores mas com Produto
  for (int i = 0; i < numProdutos; i++) {
    fscanf(fileProdutos, "%d %f %[^\n]", &produtos[i].codigo,
           &produtos[i].preco, produtos[i].descricao);
  }
  fclose(fileProdutos);

  // Lê as vendas do arquivo vendas.txt
  FILE *fileVendas = fopen("vendas.txt", "r");
  int numVendas;
  fscanf(fileVendas, "%d", &numVendas);
  Venda vendas[MAX_VENDAS];

  // faz a mesma lógica do array de vendedores mas com Vendas
  for (int i = 0; i < numVendas; i++) {
    fscanf(fileVendas, "%d %d %d", &vendas[i].codigoVendedor,
           &vendas[i].codigoProduto, &vendas[i].unidadesVendidas);
  }
  fclose(fileVendas);

  // calcula o total de vendas por vendedor e por produto
  float totalGeral = 0.0;
  // seta todos os itens do array com valor 0.0 e tamanho de MAX_PRODUTOS e
  // MAX_VENDORES
  float totalVendasPorProduto[MAX_PRODUTOS] = {0};
  float totalVendasPorVendedor[MAX_VENDORES] = {0};

  // esta criando as variaveis dos codigos dos produtos e dos vendedores e
  // quantidade vendida de cada produto
  for (int i = 0; i < numVendas; i++) {
    int codigoProduto = vendas[i].codigoProduto;
    int codigoVendedor = vendas[i].codigoVendedor;
    int unidadesVendidas = vendas[i].unidadesVendidas;
    float precoProduto = 0.0;

    // Encontra o preço do produto com base no array de struct Produtos
    for (int j = 0; j < numProdutos; j++) {
      if (produtos[j].codigo == codigoProduto) {
        precoProduto = produtos[j].preco;
        break;
      }
    }

    // Calcula o valor da venda
    float valorVenda = precoProduto * unidadesVendidas;

    // Atualiza os totais
    totalGeral += valorVenda;
    totalVendasPorProduto[codigoProduto - 1] += valorVenda;
    totalVendasPorVendedor[codigoVendedor - 1001] += valorVenda;
  }

  // Escreve os resultados no arquivo totais.txt
  FILE *fileTotais = fopen("totais.txt", "w");
  fprintf(fileTotais, "Log de Vendas:\n");
  // escreve o numero de vendas comecando do 0 até numero - 1, igual o template
  // do professor Alcides Calsavara
  for (int i = 0; i < numVendas; i++) {
    fprintf(fileTotais, "[%d] %d %d %d\n", i, vendas[i].codigoVendedor,
            vendas[i].codigoProduto, vendas[i].unidadesVendidas);
  }
  fprintf(fileTotais, "\nCatalogo de Produtos:\n");
  // informa o codigo, nome e preço dos produtos indo de 0 a numero - 1, igual o
  // template do professor Alcides Calsavara
  for (int i = 0; i < numProdutos; i++) {
    fprintf(fileTotais, "[%d] %d %.2f %s\n", i, produtos[i].codigo,
            produtos[i].preco, produtos[i].descricao);
  }
  fprintf(fileTotais, "\nLista de Vendedores:\n");
  // informa o codigo, nome dos vendedores indo de 0 a numero - 1, igual o
  // template do professor Alcides Calsavara
  for (int i = 0; i < numVendedores; i++) {
    fprintf(fileTotais, "[%d] %d %s\n", i, vendedores[i].codigo,
            vendedores[i].nome);
  }

  fprintf(fileTotais, "\nTotal geral vendido: %.2f\n\n", totalGeral);
  // informa o total de vendas utilizando os dados passados no txt coletados
  // pelos devidos array de struct
  fprintf(fileTotais, "Total de vendas de cada produto:\n");
  for (int i = 0; i < numProdutos; i++) {
    fprintf(fileTotais, "Produto %d (%s): R$%.2f\n", produtos[i].codigo,
            produtos[i].descricao, totalVendasPorProduto[i]);
  }
  // informa o total de vendas por vendedor utilizando os dados passados no txt
  // coletados pelos devidos array de struct
  fprintf(fileTotais, "\nTotal de vendas de cada vendedor:\n");
  for (int i = 0; i < numVendedores; i++) {
    fprintf(fileTotais, "Vendedor %d (%s): R$%.2f\n", vendedores[i].codigo,
            vendedores[i].nome, totalVendasPorVendedor[i]);
  }
  fclose(fileTotais);

  printf("Deu certo");

  return 0;
}
