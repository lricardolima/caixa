from model import *
class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        cat = []
        for categorias in cls.categoria:
            cat.append(Categoria(categorias))
        return cat
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|" + venda.itensVendidos.preco + "|" + venda.itensVendidos.categoria + "|" + venda.itensVendidos.fornecedor + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')  
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
            cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
            cls.venda = list(map(lambda x: x.split('|'), cls.venda))
            vend = []
            for i in cls.venda:
                vend.append(Venda(Produto(i[0], i[1], i[2], i[3]), i[4], i[5], i[6], i[7]))
            return vend
class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria + "|" + produto.fornecedor + "|" + str(quantidade))
            arq.writelines('\n')  
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
            cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
            est = []
            if len(cls.estoque) > 0:
                for i in cls.estoque:
                     est.append(Estoque(Produto(i[0], i[1], i[2], i[3]), int(i[4])))
            return est            
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + fornecedor.categoria)
            arq.writelines("\n")
    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
            cls.fornecedor = list(map(lambda x: x.replace("\n", ""), cls.fornecedor))
            cls.fornecedor = list(map(lambda x: x.split("|"), cls.fornecedor))
            forn = []
            for i in cls.fornecedor:
                forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
            return forn
class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Pessoa):
        with open('cliente.txt', 'a') as arq:
            arq.writelines(cliente.nome + "|" + cliente.idade + "|" + cliente.cpf + "|" + cliente.sexo)
            arq.writelines("\n")
    @classmethod
    def ler(cls):
        with open('cliente.txt', 'r') as arq:
            cls.cliente = arq.readlines()
            cls.cliente = list(map(lambda x: x.replace("\n", ""), cls.cliente))
            cls.cliente = list(map(lambda x: x.split("|"), cls.cliente))
        cli = []
        for i in cls.cliente:
            cli.append(Pessoa(i[0], i[1], i[2], i[3]))
        return cli
class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.idade + "|" + funcionario.cpf + "|" + funcionario.sexo)
            arq.writelines("\n")  
    @classmethod
    def ler(cls):
        with open('funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()
            cls.funcionario = list(map(lambda x: x.replace("\n", ""), cls.funcionario))
            cls.funcionario = list(map(lambda x: x.split("|"), cls.funcionario))
        funci = []
        for i in cls.funcionario:
            funci.append(Funcionario(i[0], i[1], i[2], i[3], i[4]))
        return funci

'''categorias = Categoria('Verduras')
DaoCategoria.salvar(categorias)
categorias1 = DaoCategoria.ler()
print(categorias1[0].nome)
x = Produto('Amoxilina', '2,65', 'Remedios', 'Pague Menos')
y = Estoque(x, '500')
DaoEstoque.salvar(x, y.quantidade)
z = DaoEstoque.ler()
print(z[0].quantidade)'''

