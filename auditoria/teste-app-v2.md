# Teste funcional da aplicação V2

## Comando

```bash
printf '1\nadmin\nadmin123\n9\n' | docker run --rm -i biblioteca-grupo6:v2
```

## Resultado

- Container iniciou corretamente.
- Login administrativo com `admin` / `admin123`: aprovado.
- Mensagem de boas-vindas exibida: aprovada.
- Menu de bibliotecário exibido: aprovado.
- Encerramento pela opção 9: aprovado.

O arquivo `teste-app-v2-login.txt` contém a saída completa do teste.
