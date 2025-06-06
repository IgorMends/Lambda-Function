# Lambda-Function - Calculadora de IMC

Esta função AWS Lambda recebe um JSON com informações de uma pessoa e retorna outro json com o calculo imc feito e a classificação da pessoa


# ⚠️ Validações
Peso e altura devem ser maiores que zero.<br>
Se algum valor for inválido ou ausente, será retornado erro 400.


# 📦 Dependências
Nenhuma. A função utiliza apenas bibliotecas nativas do Python.


# ▶️ Como testar com Postman

1 - Enviando a Requisição<br>
Use o Postman (ou qualquer outro cliente HTTP) para fazer um POST para a URL da função Lambda:

** URL da função Lambda:**<br>
https://35265bbqrmtqjhphwqxrw4heuu0xzjzu.lambda-url.us-east-2.on.aws/


** Exemplo de configuração no Postman:**<br>

Método: POST<br>
Aba Body:<br>
Selecione a opção raw<br>
Escolha o tipo JSON (ícone à direita)<br>
Cole e edite o seguinte JSON conforme necessário:<br>

  {<br>
  "peso": 70,<br>
  "altura": 1.75<br>
  }
