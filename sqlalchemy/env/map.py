from unicodedata import name
import sqlalchemy
#Permite a construção do objeto relacionado ao banco de dados
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, delete
#Criar uma sessão do banco de dados
from sqlalchemy.orm import sessionmaker

#Conectando ao banco de dados
engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo=False) #Echo = True Retorna as operações em formato SQL | Motivo de aprendizagem

#Declarando o mapeamento
Base = declarative_base()

class User(Base):
    #Nome da tabela
    __tablename__ = 'users' #obrigatório

    #chave primária no banco
    id = Column(Integer, primary_key=True)
    #Novas colunas na tabela
    name = Column(String(50))
    full_name = Column(String(50))
    age = Column(Integer)

    #Visualização do objeto
    def __repr__(self):
        return "<User(name= {}, full_name= {}, age= {})>".format(self.name, self.full_name, self.age) 

#Criar a tabela no banco de dados
Base.metadata.create_all(engine)

#Criar instâncias da classe
user = User(name="Keven", full_name="Keven Coutinho Crisostomo", age="20")

#Criar uma sessão do banco de dados
Session = sessionmaker(bind=engine) #criando o objeto
session =  Session() #instanciando o objeto

#Adicionando objetos a tabela
session.add(user) #OBS : Precisamos commitar os dados. Ao alterarmos  a sessão ela fica salva apenas em memória
session.commit() 

#Aicionar várias informações ao banco
session.add_all([
    #Criar novas instâncias da classe
    User(name="Valencio", full_name="Valencio Amarildo Amarok", age="43"),
    User(name="Pedro", full_name="Peter Pedro Parker", age="24")
])

#Consultando objetos e selecionando dados
query_user = session.query(User).filter_by(name="Keven").first()

# for instance in session.query(User.name, User.age).filter_by(name="Keven"):
#     print(instance)

#Modificando objetos
user.full_name = "Keven De Oliveira"
print(user)
#Ver as informações em memória, modificadas pelo session
print(session.dirty)
session.commit()

#Deletando objetos
user = session.query(User).filter_by(name="Valencio").count()

session.delete(user)
session.commit()
print(user)