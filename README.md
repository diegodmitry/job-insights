# Boas-vindas ao Job Insights!  💼

O objetivo do projeto é implementar análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask. Além de escrever testes para a implementação de uma análise de dados. Por fim, o desenvolvimento de rotas e views para a aplicação web! 💻

# Habilidades Necessárias

* Utilizar o terminal interativo do Python;
* Utilizar esturturas condicionais e laços de repetição;
* Utilizar funções incorporadas do Python;
* Utilizar tratamento de exceções;
* Realizar a manipulação de arqquivos;
* Utilizar funções em Python;
* Escrever testes;

# Instalando o projeto
1. Download do projeto:
``` git clone git@github.com:diegodmitry/job-insights.git ```
2. Dentro do diretório, execute o comando:
``` python3 -m venv .venv && source .venv/bin/activate ```
3. Instale as dependências:
``` python3 -m pip install -r dev-requirements.txt ```


# Estrutura do projeto

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── src
  │   ├──🔸app.py
  │   ├──🔸brazilian_jobs.py
  │   ├──🔸counter.py
  │   ├──🔹insights.py
  │   ├──🔸jobs.csv
  │   ├──🔹jobs.py
  │   ├──🔸more_insights.py
  │   ├──🔹routes_and_views.py
  │   ├──🔸sorting.py
  │   └── templates
  │       ├──🔸base.jinja2
  │       ├── includes
  │       │   └──🔸nav.jinja2
  │       ├──🔸index.jinja2
  │       ├──🔸job.jinja2
  │       └──🔸list_jobs.jinja2
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔹test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_insights.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
  ```

</details>
