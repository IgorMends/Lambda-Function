# Lambda-Function - Calculadora de IMC

Esta função AWS Lambda recebe um JSON com informações de uma pessoa e retorna outro json com o calculo imc feito e a classificação da pessoa


# ⚠️ Validações
&nbsp;&nbsp;Peso e altura devem ser maiores que zero.<br>
&nbsp;&nbsp;Se algum valor for inválido ou ausente, será retornado erro 400.


# 📦 Dependências
&nbsp;&nbsp;Nenhuma. A função utiliza apenas bibliotecas nativas do Python.


# ▶️ Como testar com Postman

1 - Enviando a Requisição<br>
&nbsp;&nbsp;Use o Postman (ou qualquer outro cliente HTTP) para fazer um POST para a URL da função Lambda:

** URL da função Lambda:**<br>
&nbsp;&nbsp;https://35265bbqrmtqjhphwqxrw4heuu0xzjzu.lambda-url.us-east-2.on.aws/


** Exemplo de configuração no Postman:**<br>

&nbsp;&nbsp;Método: POST<br>
&nbsp;&nbsp;Aba Body:<br>
&nbsp;&nbsp;Selecione a opção raw<br>
&nbsp;&nbsp;Escolha o tipo JSON (ícone à direita)<br>
&nbsp;&nbsp;Cole e edite o seguinte JSON conforme necessário:<br>

  {<br>
  "peso": 70,<br>
  "altura": 1.75<br>
  }
