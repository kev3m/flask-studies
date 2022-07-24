from models import Pessoas

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
    

if __name__ == '__main__':
    insere_pessoas()
    # # altera_pessoa()
    # excluir_pessoa()
    consulta_pessoa()