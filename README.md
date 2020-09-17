# Calculadora

## Calculadora construída na linguagem Python. Os testes foram criados com a biblioteca pytest.
O projeto faz parte de uma atividade prática sobre Testes de software da matéria de Engenharia de Software, lecionada por Prof. Ruy Nishimura na faculdade Anhembi Morumbi.

Para executar o projeto no seu ambiente, instale as dependencias utilizando o comando:
`pip install -r requirements.txt`

Após isso, execute o projeto utizando o comando: <br />
`python3 main/main.py`

Para executar os testes utilize o comando na raiz do projeto: <br />
`py.test tests/tests_main.py`

Para executar os tested BDD, dentro do diretório tests/, utilize o comando: <br />
`behave calc.feature`

Se tiver qualquer problema com imports de módulos e pacotes, configure a variável de ambiente `PYTHONPATH` apontando para o path do projeto:<br />
`export PYTHONPATH="$PYTHONPATH:path/do/projeto/"`
