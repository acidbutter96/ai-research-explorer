FROM apache/airflow:slim-3.0.5rc2-python3.11

# Instala dependências de sistema necessárias para compilar libs (ex: psycopg2 se preferir a versão fonte)
USER root
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   build-essential \
	   libpq-dev \
	&& apt-get purge --auto-remove -y \
	&& rm -rf /var/lib/apt/lists/*

# Volta para o usuário airflow conforme imagem base
USER airflow

# Copia e instala apenas dependências extras do projeto (a imagem já contém o Airflow)
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt