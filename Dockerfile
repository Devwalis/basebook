FROM python:3.12-slim

WORKDIR /app

COPY . .

# A aplicacao usa somente a biblioteca padrao; ferramentas de auditoria ficam fora da imagem final.
RUN python -m pip uninstall --yes pip setuptools

CMD ["python", "main.py"]
