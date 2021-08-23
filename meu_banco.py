# Programação Orientada a Objetos
# AC02 ADS-EaD - Criando classes
#
# Email Impacta: paulo.mello@aluno.faculdadeimpacta.com.br

class Cliente():
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self.telefone = telefone
        self.email = email

    def _valida_digitos_telefone(self, numero):
        import re
        # Essa linha limpa o número dos símbolos permitidos
        numero_limpo = re.sub(r'[ \(\)\-]', '', numero)

        # Essa linha verifica se o número contém apenas números e retorna um booleano
        return numero_limpo.isdigit()

    def _valida_email(self, email):
        arrobas = 0
        for digito in email:
            if digito == "@":
                arrobas += 1

        if arrobas != 1:
            return False
        else:
            return True

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_numero):

        if not isinstance(novo_numero, str):
            raise TypeError

        if not self._valida_digitos_telefone(novo_numero):
            raise ValueError

        self._telefone = novo_numero

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):

        if not isinstance(email, str):
            raise TypeError

        if not self._valida_email(email):
            raise ValueError

        self._email = email


class Conta():

    def __init__(self, clientes, numero, saldo):
        self._clientes = clientes
        self._numero = numero
        self._saldo = saldo
        self._operacoes = [("saldo inicial", saldo)]

    @property
    def clientes(self):
        return self._clientes

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    # métodos

    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError

        self._saldo -= valor
        self._operacoes.append(("saque", valor))

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(("deposito", valor))

    def tirar_extrato(self):
        # lista de todas as operações feitas na conta, incluindo abertura
        # saldo inicial, saque, deposito
        # uma lista com tuplas
        return self._operacoes


class Banco():

    def __init__(self, nome):
        self._nome = nome
        self._contas = []

    @property
    def nome(self):
        return self._nome

    @property
    def contas(self):
        return self._contas

    def abrir_conta(self, clientes, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError

        numero = len(self._contas)

        nova_conta = Conta(clientes, numero + 1, saldo_inicial)
        print(vars(nova_conta))

        self._contas.append(nova_conta)
