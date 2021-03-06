from datetime import date, datetime
class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco
class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        super().__init__(nome, telefone, cpf, email, endereco)
        self.clt = clt
class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria
class Produto:
    def __init__(self, nome, preco, categoria, fornecedor):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.fornecedor = fornecedor
class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
class Venda:
    def __init__(self, itensVendidos: Produto, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data