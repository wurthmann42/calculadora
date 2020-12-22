# Calculadora

O projeto faz parte de uma atividade prática sobre Testes de software da matéria de Engenharia de Software, lecionada por Prof. Ruy Nishimura e tem como principal intuito praticar o uso da linguagem e exercitar diferentes conceitos sobre testes de softwares.

Para executar o projeto no seu ambiente, instale as dependencias utilizando o comando: <br />
`pip install -r requirements.txt`

Após isso, execute o projeto utilizando o comando: <br />
`python3 src/app.py`

Para executar os testes utilize o comando na raiz do projeto: <br />
`py.test tests/tests_main.py`

Para executar os tested BDD, dentro do diretório tests/, utilize o comando: <br />
`behave calc.feature`

Se tiver qualquer problema com imports de módulos e pacotes, configure a variável de ambiente `PYTHONPATH` apontando para o path do projeto:<br />
`export PYTHONPATH="$PYTHONPATH:local/project/root/path"`
