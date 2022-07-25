from re import U
from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Juarez', idade=34)
    pessoa.save()

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Mauricio').first()
    pessoa.nome = 'azulão'
    pessoa.save()


def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Mauricio').first()
    # print(pessoa.idade)
    
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='azulão').first()
    pessoa.delete()
    
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuario():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    insere_usuario('Saulo','2345')
    insere_usuario('Felipe','8762')
    consulta_usuario()
    # insere_pessoas()
    # # altera_pessoa()
    # excluir_pessoa()
    # consulta_pessoa()