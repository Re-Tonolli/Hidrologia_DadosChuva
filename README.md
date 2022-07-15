# Hidrologia
Este script tem como função receber os dados brutos provenientes do site [HidroWeb](https://www.snirh.gov.br/hidroweb/serieshistoricas), selecionar somente os dados relacionados ao pluviômetro e retornar qual foi o maior índice em acumulados de 1, 2, 3, 4, 5, 10, 20, 30, 40, 50 e 60 dias.
# Dependências
*Disponíveis no arquivo `requirements.txt`*

Utilize Python 3.8 ou maior.

`python -m pip install -r requirements.txt`

# Utilização
É necessário ter acesso aos dados, que devem estar num formato de CSV e com o arquivo em UTF-8. Se necessário consulte o seguinte [tutorial](https://www.criarfazer.net/como-converter-um-arquivo-para-utf-8/).
**Para determinar o formato dos dados, certifique-se que o nome do arquivo contenha `chuva` ou `clima`.** Lembre-se de remover as linhas que não possuem dados, mantendo apenas o cabeçalho da tabela.

Em seguida, execute `python main.py CAMINHO DOS DADOS` onde `CAMINHO DOS DADOS` deve indicar o arquivo csv em questão.

## Exemplos
`python main.py dados/dados_chuva.csv`

`python main.py dados/dados_clima.csv`