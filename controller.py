from dao import *
from datetime import datetime
class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        categoriaLer = DaoCategoria.ler()
        for categorias in categoriaLer:
            if categorias.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria já existe!')
    def removeCategoria(self, categoriaRemover):
        categoriaLer = DaoCategoria.ler()
        cat = list(filter(lambda categoriaLer: categoriaLer.categoria == categoriaRemover, categoriaLer))
        if len(cat) == 0:
            print('A categoria que deseja remover não existe')
        else:
            for categorias in range(len(categoriaLer)):
                if categoriaLer[categorias].categoria == categoriaRemover:
                    del categoriaLer[categorias]
                    break
            print('Categoria removida com sucesso!')
            #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w') as arq:
                for categorias in categoriaLer:
                    arq.writelines(categorias.categoria)
                    arq.writelines('\n')
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        categoriaLer = DaoCategoria.ler()
        cat = list(filter(lambda categoriaLer: categoriaLer.categoria == categoriaAlterar, categoriaLer))
        if len(cat) > 0:
            catAlt = list(filter(lambda categoriaLer: categoriaLer.categoria == categoriaAlterada, categoriaLer))
            if len(catAlt) == 0:
                categoriaLer = list(map(lambda categoriaLer: Categoria(categoriaAlterada) if(categoriaLer.categoria == categoriaAlterar) else(categoriaLer), categoriaLer))
                print('A categoria foi alterada!')
                #TODO: ALTERAR A CATEGORIA TAMBEM DO ESTOQUE
            else:
                print('A categoria já existe!')
        else:
            print('A categoria que deseja alterar não existe!')
        with open('categoria.txt', 'w') as arq:
            for categorias in categoriaLer:
                arq.writelines(categorias.categoria)
                arq.writelines('\n')      
    def mostrarCategoria(self):
        categorialer = DaoCategoria.ler()
        if len(categorialer) == 0:
            print('Categoria Vazia!')
        else:
            for categorias in categorialer:
                print(f'Categoria: {categorias.categoria}')
class ControllerEstroque:
    def cadastrarProduto(self, nome, preco, categoria, fornecedor, quantidade):
        estoqueLer = DaoEstoque.ler()
        categoriaLer = DaoCategoria.ler()
        categorias = list(filter(lambda categoriaLer: categoriaLer.categoria == categoria, categoriaLer))
        estoques = list(filter(lambda estoqueLer: estoqueLer.produto.nome == nome, estoqueLer))
        if len(categorias) > 0:
            if len(estoques) == 0:
                produto = Produto(nome, preco, categoria, fornecedor)
                DaoEstoque.salvar(produto, quantidade)
                print('produto cadastrado com sucesso!')
            else:
                print('produto já existe em estoque!')
        else:
            print('Categoria inexistente!')
    def removerProduto(self, nome):
        estoqueLer = DaoEstoque.ler()
        estoques = list(filter(lambda x: x.produto.nome == nome, estoqueLer))
        if len(estoques) > 0:
            for produto in range(len(estoqueLer)):
                if estoqueLer[produto].produto.nome == nome:
                    del estoqueLer[produto]
                    print('produto removido com sucesso!')
                    break
        else:
            print('produto que deseja remover não existe no estoque!')
        with open('estoque.txt', 'w') as arq:
            for produto in estoqueLer:
                arq.writelines(produto.produto.nome + "|" + produto.produto.preco + "|" + produto.produto.categoria + "|" + produto.produto.fornecedor + "|" + str(produto.quantidade))
                arq.writelines('\n')
    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novoFornecedor, novaQuantidade):
        estoqueLer = DaoEstoque.ler()
        categoriaLer = DaoCategoria.ler()
        categorias = list(filter(lambda x: x.categoria == novaCategoria, categoriaLer))
        if len(categorias) > 0:
            estoques = list(filter(lambda x: x.produto.nome == nomeAlterar, estoqueLer))
            if len(estoques) > 0:
                estoques = list(filter(lambda x: x.produto.nome == novoNome, estoqueLer))
                if len(estoques) == 0:
                    estoqueLer = list(map(lambda estoqueLer: Estoque(Produto(novoNome, novoPreco, novaCategoria, novoFornecedor), novaQuantidade) if(estoqueLer.produto.nome == nomeAlterar) else(estoqueLer), estoqueLer))
                    print('Produto alterado com sucesso!!')
                else:
                    print('Produto já cadastrado!!')
            else:
                print('O produto que deseja alterar não existe')
            with open('estoque.txt', 'w') as arq:
                for produto in estoqueLer:
                      arq.writelines(produto.produto.nome + "|" + produto.produto.preco + "|" + produto.produto.categoria + "|" + produto.produto.fornecedor + "|" + str(produto.quantidade))
                      arq.writelines('\n')
        else:
            print('a categoria informada não existe')
    def mostrarEstoque(self):
        estoqueler = DaoEstoque.ler()
        if len(estoqueler) == 0:
            print('Estoque vazio!')
        else:
            print('========== Produtos ==========')
            for produto in estoqueler:
                print(f'nome: {produto.produto.nome}\n'
                 f'Preço: {produto.produto.preco}\n' 
                 f'Categoria: {produto.produto.categoria}\n' 
                 f'Fornecedor: {produto.produto.fornecedor}\n' 
                 f'Quantidade: {produto.quantidade}')
                print('=========================')
class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        estoqueLer = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        for produto in estoqueLer:
            if existe == False:
                if produto.produto.nome == nomeProduto:
                    existe = True
                    if produto.quantidade >= int(quantidadeVendida):
                        quantidade = True
                        produto.quantidade = int(produto.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produto(produto.produto.nome, produto.produto.preco, produto.produto.categoria, produto.produto.fornecedor), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * float(produto.produto.preco)
                        DaoVenda.salvar(vendido)
            temp.append(Estoque(Produto(produto.produto.nome, produto.produto.preco, produto.produto.categoria, produto.produto.fornecedor), produto.quantidade))
        arq = open('estoque.txt', 'w')
        arq.write('')
        for produto in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(produto.produto.nome + "|" + produto.produto.preco + "|" + produto.produto.categoria + "|" + produto.produto.fornecedor + "|" + str(produto.quantidade))
                arq.writelines('\n')
            if existe == False:
                print('O produto não existe')
                return None
            elif not quantidade:
                print(f'O estoque só contem {produto.quantidade} unidades')
            else:
                return valorCompra
    def relatorioVendas(self):
        vendasLer = DaoVenda.ler()
        produtos = []
        for produto in vendasLer:
            nome = produto.itensVendidos.nome
            quantidade = produto.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
        print(produtos)
        ordenar = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        print('Esses são os produtos mais vendidos')
        a = 1
        for produto in ordenar:
            print(f'========== Produto [{a}] ==========')
            print(f"Produto: {produto['produto']}\n"
            f"Quantidade: {produto['quantidade']}\n")
            a += 1
    def mostrarVendas(self, dataInicial, dataFinal):
        vendasLer = DaoVenda.ler()
        dataInicial = datetime.strptime(dataInicial, '%d/%m/%Y')
        dataFinal = datetime.strptime(dataFinal, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicial and datetime.strptime(x.data, '%d/%m/%Y') <= dataFinal, vendasLer))

        cont = 1
        total = 0

        for produtos in vendasSelecionadas:
            print(f'========== Vendas [{cont}] ==========')
            print(f"Nome: {produtos.itensVendidos.nome}\n"
            f"Categoria: {produtos.itensVendidos.categoria}\n"
            f"Data: {produtos.data}\n"
            f"Quantidade: {produtos.quantidadeVendida}\n"
            f"Preço unitario: {produtos.itensVendidos.preco}\n"
            f"Cliente: {produtos.comprador}\n"
            f"Vendedor: {produtos.vendedor}\n")
            total += float(produtos.itensVendidos.preco) * int(produtos.quantidadeVendida)
            cont += 1
        print(f"Total Vendido: {total}")
class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        fornecedorLer = DaoFornecedor.ler()
        listCnpj = list(filter(lambda x: x.cnpj == cnpj, fornecedorLer))
        listTel = list(filter(lambda x: x.telefone == telefone, fornecedorLer))
        if len(listCnpj) > 0:
            print('O cnpj já existe!')
        elif len(listTel) > 0:
            print('O telefone já existe!')
        else:
            if len(cnpj) == 14 and len(telefone) == 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso!')
            else:
                print('Digite um cnpj ou telefone válido!')
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        fornecedorLer = DaoFornecedor.ler()
        fornecedor = list(filter(lambda x: x.nome == nomeAlterar, fornecedorLer))
        if len(fornecedor) > 0:
            fornecedor = list(filter(lambda x: x.cnpj == novoCnpj, fornecedorLer))
            if len(fornecedor) == 0:
                fornecedorLer = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar)else(x), fornecedorLer))
                print('Fornecedor alterado com sucesso!')
            else:
                print('Cnpj já existe!')
            with open('fornecedor.txt', 'w') as arq:
                for fornecedor in fornecedorLer:
                    arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + str(fornecedor.categoria))
                    arq.writelines("\n")
        else:
            print('O Fornecedor que deseja alterar não existe')
    def removerFornecedor(self, nome):
        fornecedorLer = DaoFornecedor.ler()
        fornecedor = list(filter(lambda x: x.nome == nome, fornecedorLer))
        if len(fornecedor) > 0:
            for fornecedor in range(len(fornecedorLer)):
                if fornecedorLer[fornecedor].fornecedor.nome == nome:
                    del fornecedorLer[fornecedor]
                    print('Fornecedor removido com sucesso!')
                    break
        else:
            print('O fornecedor que deseja remover não existe!')
        with open('fornecedor.txt', 'w') as arq:
            for fornecedor in fornecedorLer:
               arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + str(fornecedor.categoria))
               arq.writelines("\n")

        
        
      
f = ControllerFornecedor()
f.alterarFornecedor('Pague Menos', 'Drogasil', '07204404000285', '85988685545', 'Remedios')
f.removerFornecedor('Drogasil')