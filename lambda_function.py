import json

def lambda_handler(event, context):
    try:
        body = event.get("body")

        if body is None:
            return {
                "statusCode": 400,
                "body": json.dumps({ "erro": "Corpo da requisição ausente." })
            }

        data = json.loads(body)

        peso = float(data.get("peso", 0))
        altura = float(data.get("altura", 0))

        if peso <= 0 or altura <= 0:
            return {
                "statusCode": 400,
                "body": json.dumps({ "erro": "Peso e altura devem ser maiores que zero." })
            }

        imc = round(peso / (altura ** 2), 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 24.9:
            classificacao = "Peso normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        elif imc < 34.9:
            classificacao = "Obesidade grau I"
        elif imc < 39.9:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        return {
            "statusCode": 200,
            "body": json.dumps({
                "imc": imc,
                "classificacao": classificacao
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({ "erro": f"Erro ao processar dados: {str(e)}" })
        }