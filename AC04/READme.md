# Atividade Contínua 4

## Funcionamento
>O código em questão é uma aplicação em Flask que utiliza três rotas de API, sendo estas dos métodos GET, POST e DELETE, para se comunicar com o serviço externo jsonplaceholder.typicode.com. Também são presentes outras três rotas que têm por finalidade chamar o primeiro serviço para cada respectivo método, e estão disponíveis no localhost:5000. A seguir, são descritas cada uma das chamadas e suas respectivas funções:

## jsonplaceholder.typicode.com
`/todos` *(GET)*
- Criamos apenas uma função GET para que quando chamada verifica todos os registros dentro da API citada.

`/todos/<id>` *(POST)*
- Ainda parecida com a função citada acima, apenas registramos uma nova choice com base no userid.

`/todos/<id>` *(DELETE)*
- E agora sim, totalmente ao contrário das anteriores, de acordo com o ID a função que chama esta URL, exclui a choice, de acordo com o number(id) passado na URL.

## localhost:5000
`/todos` *(GET)*
- Esta rota tem como função exibir os registros cadastrados atráves do metodo GET. Ao ser requisitada, deve-se retornar o status code 200, indicando que a requisição foi bem-sucedida. 

`/todos/<id>` *(POST)*
- Esta rota utiliza o metodo POST para adicionar novos registros através de um ID. Ao ser requisitada, deve-se retornar o status code 200, indicando que a requisição foi bem-sucedida.

`/todos/<id>` *(DELETE)*
- Esta rota utiliza o metodo DELETE para deletar registros existentes através de seu ID. Ao ser requisitada, deve-se retornar o status code 200, indicando que a requisição foi bem-sucedida.

