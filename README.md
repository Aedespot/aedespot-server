AedeSpot
========
[![Build Status](https://travis-ci.org/henriquenogueira/aedes.svg?branch=master)](https://travis-ci.org/henriquenogueira/aedes)
[![Code Health](https://landscape.io/github/henriquenogueira/aedes/master/landscape.svg?style=flat)](https://landscape.io/github/henriquenogueira/aedes/master)
[![codecov.io](https://codecov.io/github/henriquenogueira/aedes/coverage.svg?branch=master)](https://codecov.io/github/henriquenogueira/aedes?branch=master)

Monitoramento da Dengue.

* O site pode ser acessado [aqui](http://aedespot-server.herokuapp.com/).
* Os endpoints da API REST estão [aqui](http://aedespot-server.herokuapp.com/api/).
* A interface de administração está [aqui](http://aedespot.herokuapp.com/admin/).

Ambiente
========

Este projeto foi testado e desenvolvido com:
* Python 3.5.1
* Django 1.9.4

Instalação
==========

Pegue o código do repositório da seguinte maneira:

    git clone git@github.com:Aedespot/aedespot-server.git

Copie o arquivo contrib/env-sample para o root do projeto com o nome .env:

    cp contrib/env-sample .env

Gere uma SECRET_KEY e a coloque no .env:

    SECRET=$(python contrib/gen_secret.py)

Instale as dependências necessárias:

    pip install -r requirements/dev.txt
    pip install -r conda_requirements.txt

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