data = [
  {
    "id": 3,
    "sourceAccount": "A",
    "targetAccount": "B",
    "amount": 100,
    "category": "eating_out",
    "time": "2018-03-02T10:34:30.000Z"
  },
  {
    "id": 1,
    "sourceAccount": "A",
    "targetAccount": "B",
    "amount": 100,
    "category": "eating_out",
    "time": "2018-03-02T10:33:00.000Z"
  },
  {
    "id": 6,
    "sourceAccount": "A",
    "targetAccount": "C",
    "amount": 250,
    "category": "other",
    "time": "2018-03-02T10:33:05.000Z"
  },
  {
    "id": 4,
    "sourceAccount": "A",
    "targetAccount": "B",
    "amount": 100,
    "category": "eating_out",
    "time": "2018-03-02T10:36:00.000Z"
  },
  {
    "id": 2,
    "sourceAccount": "A",
    "targetAccount": "B",
    "amount": 100,
    "category": "eating_out",
    "time": "2018-03-02T10:33:50.000Z"
  },
  {
    "id": 5,
    "sourceAccount": "A",
    "targetAccount": "C",
    "amount": 250,
    "category": "other",
    "time": "2018-03-02T10:33:00.000Z"
  }
]

# Desafio: retornar lista de listas com transações duplicadas
# mesma targetAccount, mesma sourceAccount e amount e category 

def find_duplicates(data_list):

  # Vamos inicializar um dicionário para encontrar as duplicatas
  # e a lista que retornará os dados duplicados
  dup_dict = {}
  ret_list = []

  # Percorre a lista recebida criando um hash e adicionando-o ao dicionário caso ainda não exista
  # caso já exista, adiciona a transação na lista da chave encontrada
  for transaction in data_list:
    k = '{targetAccount}:{sourceAccount}:{amount}:{category}'.format(**transaction)
    
    if k not in dup_dict:
      dup_dict[k] = [transaction]
      continue
    
    dup_dict[k].append(transaction)
  
  # Percorre o dicionário para encontrar as listas que possuem duplicatas.
  # Caso existirem duplicatas (len > 1) adiciona na lista de retorno.
  for v in dup_dict.values():
    if len(v) > 1:
      ret_list.append(v)

  return ret_list

if __name__ == "__main__":
  print(find_duplicates(data))