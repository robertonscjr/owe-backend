# ÒWE BACK-END

ÒWE, é um provérbio Iorubá que significa ajuda mútua. Pensando nisso, desenvolvemos uma plataforma para auxiliar o jovem que evadiu da escola a encontrar sua jornada em busca da formação profissionalizante. Através de trilhas básicas de aprendizagens, alinhadas à BNCC e aos Intinerários Formativos, é possível gerar relatórios e dados capazes de orientar o jovem em sua trilha de desenvolvimento profissional.

Olá, seja bem vind ao repositório da implementação back-end do ÒWE. Aqui você encontrará informações sobre como fazer o 'deployment' e como chamar este serviço.

Vídeo Pitch do [ÒWÉ aqui](https://www.youtube.com/watch?v=TDzSth-01GE)!

## Chamada de API

Esta API foi pensada para receber dados genéricos, isto será útil neste processo de entendimento da lógica de negócio.

1. Registrar dado de usuário
    - Action: **POST**
    - URI: https://OWE_HOST:OWE_PORT/registerUserData
    - Request payload:
      - ```bash
              { "data_sample": string }
           ```


### Exemplo com CURL
```bash
curl -H "Content-Type: application/json" -X POST -d '{"idade": "20 < x < 30"}' https://OWE_HOST:OWE_PORT/registerUserData
```

## Deployment

Você pode utilizar Docker para fazer o build e o deployment do app.

```bash
sudo docker build -t owe-monolithic:0.1 .
```

Obs: Este repositório tem suporte para o deployment no Heroku. Deployment público: https://owe-monolithic.herokuapp.com
