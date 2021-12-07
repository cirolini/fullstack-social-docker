# Containers

Primeiro de tudo é importante entender o que são containers. Containers são formas de isolar um conjunto de processos dentro do sistema operacional Linux, ou seja é uma forma de fazer com que um conjunto de processos não tenha acesso ao restante do sistema, a outros processos ou pastas e também poder limitar esses processos em relação a recursos de sistema. É quase como rodar um segundo sistema operacional dentro do mesmo sistema.

Container são muito utilizados para resolver problemas de ambiente, com eles podemos "empacotar" todo o necessário para a nossa aplicação executar e depois distribuir ele para os sistemas de produção, basicamente da mesma forma que programamos ele na nossa estação de trabalho.

O Docker foi o modelo de container que mais se popularizou, é um conjunto de ferramentas com diversas facilidades para criar containers, existem outros, alguns se tornando muito populares como o containerd ou o cri-o.

Com orquestradores de containers como o Kubernetes diversas outras funcionalidades e facilidades surgiram, como facilidades para aumentar a capacidade de entrega de aplicações (scaling), configurações de aplicação como código (IaC), Capacidades de autocura, rollouts e rollbacks automatizados. Basicamente possibilitou o desenvolver se preocupar somente com o código e não mais com a infraestrutura.

## Meu primeiro container

Indo para a pasta `docker` deste projeto, temos um esqueleto de um primeiro container de uma aplicação web em python muito simples. Nessa aplicação vamos fazer funcionar um servidor web que vai escrever "Hello, Cirolini" na tela. Para isso 3 arquivos são necessários.

- Dockerfile, é o arquivo onde vamos instruir ao docker como criar o nosso container
- app.py, é o código da nossa aplicação Python
- requirementes.txt, é um metodo do Python para instalação de dependencias ja que vamos precisar instalar o Flask, que é um framework Python para criar pequenos servidores web

Indo para a lista de comandos:

### Build

O primeiro passo é criar a imagem docker, e podemos fazer assim:

```
cd docker
docker build -t hello-cirolini .
```

### Executar

Para executar o container basta:

```
docker run --publish 5000:5000 hello-cirolini
```

Depois podemos acessar o navegador local com `localhost:5000` e vamos ver o Hello, Cirolini escrito na tela.

### Modificar

```
sed -i '' s/Cirolini/teste/g app.py
docker build -t hello-cirolini .
docker run --publish 5000:5000 hello-cirolini
```

### Tag Image

```
docker tag hello-cirolini cirolini/hello-cirolini:1.0
```

### Enviando para o docker hub

```
docker push cirolini/hello-cirolini:1.0
```

## Docker Compose

Geralmente um ambiente de um software envolve mais de um componente, usando containers podemos querer usar mais de um containers e fazer com que eles se comuniquem, para o desenvolvolvimento local podemos usar o docker compose, uma ferramenta que ajuda a usar varios containers ao mesmo tempo e fazer com que eles se comuniquem:

```
docker-compose build
docker-compose up
```

## Kubernetes

Explicar a arquitetura do Kubernetes

Vamos instalar o kind.


```
kubectl apply -f deployment.yml
sudo kubectl port-forward service/hello-cirolini-service 80:80
```
