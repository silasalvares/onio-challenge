# onio-challenge

Estrutura:
  - 2 microserviços: Vendas e Fidelidade
  - RabbitMQ: Utilizado para comunicação entre os microseviços
  - Banco: MongoDB (Cada microserviço possui o seu próprio banco)
  - RabbitMQ-Credit-Worger: Script responsável por tratar a fila de crédito do RabbitMQ
  - Interface Web
  
Para executar com o docker:
  - docker-compose up (na raiz)
  
Para executar os testes:
  - pytest (dentro do diretório do serviço)
  
Para executar um serviço isoladamente:
  - python run.py (dentro do diretório do serviço)
