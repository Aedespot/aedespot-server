AedeSpot
========
[![Build Status](https://travis-ci.org/Aedespot/aedespot-server.svg?branch=master)](https://travis-ci.org/Aedespot/aedespot-server)
[![Code Health](https://landscape.io/github/Aedespot/aedespot-server/master/landscape.svg?style=flat)](https://landscape.io/github/Aedespot/aedespot-server/master)
[![codecov.io](https://codecov.io/github/Aedespot/aedespot-server/coverage.svg?branch=master)](https://codecov.io/github/Aedespot/aedespot-server?branch=master)

Monitoramento da Dengue.

* O site pode ser acessado [aqui](http://aedespot.com.br/). (Ainda não está no ar)
* Os endpoints da API REST estão [aqui](http://aedespot.com.br/api/).
* A interface de administração está [aqui](http://aedespot.com.br/admin/).

Ambiente
========

Este projeto foi testado e desenvolvido com:
* Python 3.5.1
* Django 1.9.6

Instalação
==========

Pegue o código do repositório da seguinte maneira:

    git clone https://github.com/Aedespot/aedespot-server.git

Copie o arquivo contrib/env-sample para o root do projeto com o nome .env:

    cp contrib/env-sample .env

Gere uma SECRET_KEY e a coloque no .env:

    python contrib/gen_secret.py

Instale as dependências necessárias:

    pip install -r requirements/dev.txt

Lance o servidor Django:

    python manage.py runserver

Testes
======

Os testes do CardDig foram implementados usando o
[framework de testes do Django](https://docs.djangoproject.com/en/1.9/topics/testing/overview/).

Para a execução dos testes:

    python manage.py test

Problemas conhecidos
====================

Nenhum problema reportado até então.