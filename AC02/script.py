# Nome: Matheus Cardoso Morais RA: 2200764

from flask import Flask, jsonify

produtos = [
    {
        'categoria': 'calçados',
        'marca': 'nike',
        'nome': 'air force 1'
    },
    {
        'categoria': 'calçados',
        'marca': 'adidas',
        'nome': 'forum low'
    },
    {
        'categoria': 'calçados',
        'marca': 'puma',
        'nome': 'puma suede'
    },
    {
        'categoria': 'calças',
        'marca': 'nike',
        'nome': 'calça de moletom'
    },
    {
        'categoria': 'calças',
        'marca': 'nike',
        'nome': 'calça de jeans'
    },
    {
        'categoria': 'calças',
        'marca': 'nike',
        'nome': 'calça cargo'
    },
    {
        'categoria': 'camisetas',
        'marca': 'nike',
        'nome': 'Camiseta nike branca'
    },
    {
        'categoria': 'camisetas',
        'marca': 'adidas',
        'nome': 'Camiseta lisa adidas'
    },
    {
        'categoria': 'camisetas',
        'marca': 'puma',
        'nome': 'Camiseta cinza puma'
    }
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Olá, você pode acessar a URI de /produtos/ para ter acesso a lista de produtos ou /produtos/categoria para filtra-lás por categoria.', 200

@app.route('/produtos', methods=['GET'])
def listProducts():
    return jsonify(produtos), 200

@app.route('/produtos/<string:categoria>', methods=['GET'])
def filterProducts(categoria):
    list = []

    for produto in produtos:
        if produto.get('categoria') == categoria:
            list.append(produto)

    return jsonify(list), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)