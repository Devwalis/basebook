# Atividade prática — Ansible, Molecule e Testinfra

**Repositório e arquivos da atividade:**<br>
<https://github.com/Devwalis/basebook/tree/feat/testes-infra>

## Respostas

### Ansible

1. **O que é uma Role?**<br>
   É uma forma de agrupar tarefas e configurações para reaproveitar a automação.

2. **Para que serve o diretório `tasks`?**<br>
   Guarda as tarefas que o Ansible executa ao aplicar a Role.

3. **Para que serve `defaults/main.yml`?**<br>
   Define os valores padrão das variáveis da Role, que podem ser substituídos quando necessário.

4. **Por que separar a automação em arquivos e diretórios?**<br>
   Para deixar cada parte mais fácil de encontrar, alterar e reaproveitar.

5. **Para que serve um inventário? Pode ter vários servidores no mesmo grupo?**<br>
   O inventário lista e agrupa as máquinas usadas pelo Ansible. Sim, um grupo pode ter vários servidores.

6. **Qual é a diferença entre conexão SSH e local?**<br>
   SSH conecta a uma máquina remota. A conexão local executa as tarefas na própria máquina.

7. **O que significam `name`, `hosts`, `connection` e `roles` no playbook?**<br>
   `name` descreve a execução; `hosts` escolhe os alvos; `connection` define como conectar; `roles` indica quais Roles aplicar.

8. **Por que o playbook principal chama uma Role?**<br>
   Para manter o playbook simples e deixar as tarefas organizadas e reaproveitáveis na Role.

9. **O que são variáveis no Ansible? Por que usar `app_dir` e `venv_dir`?**<br>
   São valores reutilizados nas tarefas. Usar variáveis evita repetir caminhos e facilita alterá-los em um só lugar.

10. **Qual é a diferença entre `defaults` e um valor escrito diretamente na tarefa?**<br>
    Em `defaults`, o valor fica centralizado e pode ser substituído. Um valor fixo na tarefa precisa ser alterado diretamente em cada lugar onde aparece.

11. **Para que serve o módulo `copy`?**<br>
    Copia arquivos do controlador Ansible para a máquina configurada.

12. **Qual é a vantagem de automatizar a preparação do ambiente?**<br>
    Evita repetir etapas manualmente e ajuda a obter o mesmo resultado em novas execuções.

### Molecule e Testinfra

13. **Para que serve o Molecule?**<br>
    Para executar e organizar os testes de uma Role do Ansible.

14. **O que fazem o driver, o provisionador e o verificador?**<br>
    O driver define onde o cenário roda; o provisionador aplica a Role com Ansible; o verificador testa o resultado com Testinfra. Neste exercício, tudo roda localmente.

15. **O que é a etapa Converge?**<br>
    É quando o Molecule executa o playbook do cenário e aplica a Role ao ambiente de teste.

16. **Por que existem `Ansible/playbook.yml` e `molecule/default/converge.yml`?**<br>
    O primeiro é usado para executar a automação normalmente. O segundo é usado pelo Molecule durante os testes. Os dois aplicam a mesma Role em fluxos diferentes.

17. **Como o Testinfra verifica arquivos e diretórios?**<br>
    `host.file(caminho)` representa o recurso que será verificado. Propriedades como `exists`, `is_directory` e `is_file` são usadas com `assert` para conferir o estado esperado.

18. **Qual é a diferença entre testar a aplicação e testar a infraestrutura?**<br>
    `unittest` verifica o comportamento do código da aplicação. Testinfra verifica se o ambiente, os arquivos e os executáveis foram preparados corretamente.

19. **O que significa idempotência?**<br>
    Significa que, se o estado desejado já foi alcançado, executar a automação novamente não provoca mudanças desnecessárias.
