# Processo Integrado de XP, Scrum e Kanban

**Aluno:** Rafael Oliveira Molina

## 1. Quadro Kanban proposto

**Link do GitHub Projects:** `INSERIR_AQUI_O_LINK_DO_QUADRO_APOS_CRIÁ-LO`

O quadro deve ser configurado com as seguintes colunas:

| Coluna | Regra de movimentação |
|---|---|
| **Product Backlog** | Histórias conhecidas, ordenadas pelo Product Owner, ainda sem compromisso para a Sprint. |
| **Pronto para desenvolver** | Item refinado, pequeno e com critérios de aceite compreendidos; corresponde ao Sprint Backlog disponível. |
| **Em desenvolvimento — WIP 2** | Trabalho ativo. Cada card deve ter responsável e, quando necessário, dupla definida. |
| **Revisão e testes — WIP 2** | Código integrado, em revisão e com testes automatizados passando. |
| **Concluído** | Critérios de aceite e Definition of Done atendidos; incremento demonstrável. |

Os limites de WIP evitam que a equipe comece muitas tarefas sem terminar as anteriores. Quando uma coluna alcança o limite, os desenvolvedores colaboram para desbloquear ou concluir itens existentes.

### Cards iniciais

| ID | User story/tarefa | Critérios de aceite principais | Prioridade inicial |
|---|---|---|---|
| US-01 | Como usuário, quero criar uma conta para acessar o sistema. | Nome, e-mail e senha obrigatórios; e-mail não pode se repetir; confirmação de sucesso. | Alta |
| US-02 | Como usuário, quero entrar com e-mail e senha para acessar meus projetos. | Credenciais válidas permitem acesso; credenciais inválidas exibem resposta segura; senha não aparece em texto puro. | Alta |
| US-03 | Como usuário, quero criar um projeto para organizar o trabalho da equipe. | Título obrigatório; descrição opcional; criador é associado ao projeto. | Alta |
| US-04 | Como membro, quero criar tarefas em um projeto para registrar o trabalho. | Título e status obrigatórios; tarefa vinculada a um projeto; status inicial “A fazer”. | Média |
| US-05 | Como membro, quero mover uma tarefa entre status para acompanhar seu andamento. | Movimentação entre “A fazer”, “Em andamento” e “Concluído”; mudança persistida; quadro atualizado. | Média |
| TS-06 | Configurar pipeline de integração contínua. | A cada push, executar análise estática e testes; impedir merge quando a verificação falhar. | Alta |

Para reproduzir o quadro no GitHub Projects, crie os seis cards acima, adicione campos de prioridade e responsável, configure as cinco colunas e aplique os limites de WIP como política visível na descrição das colunas.

## 2. Práticas de XP adotadas

1. **Design Simples:** implementar a solução mais simples que atenda aos requisitos atuais. Evita antecipações e facilita mudanças.
2. **Desenvolvimento Orientado a Testes (TDD):** escrever um teste que falha, implementar o mínimo para fazê-lo passar e então refatorar. O ciclo fornece feedback técnico rápido.
3. **Programação em Pares:** utilizar driver e navigator em histórias complexas, defeitos críticos e partes centrais do domínio, alternando papéis regularmente.
4. **Integração Contínua:** integrar alterações pequenas frequentemente. O pipeline executa testes e verificações a cada atualização.
5. **Refatoração Contínua:** melhorar estrutura, nomes e duplicações sem alterar o comportamento, apoiado pela suíte de testes.
6. **Propriedade Coletiva do Código:** qualquer integrante pode melhorar qualquer parte do sistema, respeitando testes e revisão. Isso reduz gargalos de conhecimento.
7. **Pequenas Entregas:** dividir histórias para que possam ser concluídas e demonstradas dentro da Sprint, oferecendo retorno rápido ao negócio.
8. **Cliente Presente de forma adaptada:** o Product Owner representa as decisões diárias e concentra as dúvidas para reuniões curtas com o cliente, respeitando sua disponibilidade limitada.

## 3. Integração das práticas de XP com Scrum

Scrum organiza o trabalho e cria ciclos de inspeção e adaptação; XP orienta como o software é construído com qualidade dentro desses ciclos. Na Sprint Planning, histórias refinadas e pequenas são selecionadas. Durante a execução, a equipe aplica TDD, programação em pares, Design Simples, refatoração e integração contínua. A Daily Scrum permite identificar bloqueios, mas não substitui a colaboração técnica.

O incremento só é aceito na Sprint Review se cumprir a Definition of Done: código revisado, testes passando, integração concluída, critérios de aceite atendidos e documentação essencial atualizada. Na Retrospectiva, a equipe avalia tanto o processo Scrum quanto a eficácia das práticas de XP e define uma melhoria concreta para a próxima Sprint.

## 4. Fluxo semanal

### Semana 1

- **Segunda-feira:** Sprint Planning, definição da Sprint Goal e seleção das histórias; início do trabalho em pares e do ciclo TDD.
- **Terça a quinta-feira:** Daily Scrum, desenvolvimento, integração contínua, revisão, testes e movimentação dos cards conforme o fluxo real.
- **Sexta-feira:** Daily Scrum, integração do incremento parcial, verificação de métricas do pipeline e refinamento breve das histórias seguintes.

### Semana 2

- **Segunda a quarta-feira:** Daily Scrum e conclusão das histórias, mantendo TDD, refatoração e integração frequente.
- **Quinta-feira:** estabilização do incremento sem abrir novas tarefas; validação dos critérios de aceite e preparação da demonstração.
- **Sexta-feira:** Daily Scrum, Sprint Review, Sprint Retrospective e atualização do backlog pelo Product Owner.

## 5. Cronograma da Sprint de duas semanas

| Momento | Evento/atividade | Duração | Participantes | Resultado esperado |
|---|---|---:|---|---|
| Dia 1, 9h | Sprint Planning | 2 horas | Product Owner e desenvolvedores | Sprint Goal, Sprint Backlog e plano inicial. |
| Dias 1 a 10, 9h | Daily Scrum | 15 minutos por dia | Desenvolvedores; PO opcional | Plano das próximas 24 horas e impedimentos visíveis. |
| Dias 1 a 8 | TDD e Design Simples | Contínuo | Desenvolvedores | Funcionalidades pequenas cobertas por testes. |
| Dias 1 a 8 | Programação em pares | Blocos de 45–60 min | Duplas rotativas | Decisões revisadas e conhecimento distribuído. |
| Dias 1 a 9 | Integração contínua | A cada alteração pequena | Desenvolvedores | Branch principal estável e falhas detectadas cedo. |
| Dias 2 a 9 | Refatoração e revisão | Contínuo | Desenvolvedores | Código limpo sem mudança de comportamento. |
| Dia 5, 15h | Refinamento do Product Backlog | 1 hora | PO e desenvolvedores | Próximas histórias compreendidas e estimáveis. |
| Dia 9, tarde | Validação final da Sprint | Até 2 horas | Desenvolvedores e PO | Definition of Done verificada e demonstração preparada. |
| Dia 10, 14h | Sprint Review | 1 hora | PO, desenvolvedores e cliente/stakeholders | Incremento demonstrado, feedback coletado e backlog adaptado. |
| Dia 10, 15h15 | Sprint Retrospective | 1 hora | Time Scrum | Uma ação de melhoria com responsável definido. |

### Entregas esperadas

- Cadastro e autenticação de usuário concluídos.
- Criação básica de projeto concluída.
- Pipeline de integração contínua executando testes automaticamente.
- Código revisado, integrado e de acordo com a Definition of Done.
- Product Backlog atualizado com o feedback da Sprint Review.

## 6. Scrum versus Kanban

| Aspecto | Scrum | Kanban | Combinação na AgileTech |
|---|---|---|---|
| **Quando usar** | Produto complexo que se beneficia de metas e ciclos regulares de planejamento e feedback. | Fluxo contínuo, manutenção ou demanda com prioridades que mudam a qualquer momento. | Scrum define a cadência; Kanban torna o trabalho da Sprint visível. |
| **Cadência** | Sprints de duração fixa. | Fluxo contínuo, sem iteração obrigatória. | Sprint de duas semanas com acompanhamento diário do fluxo. |
| **Compromisso** | A equipe seleciona trabalho em torno de uma Sprint Goal. | Novos itens são puxados quando existe capacidade. | O escopo vem do Sprint Backlog e cada item só é puxado respeitando WIP. |
| **Papéis** | Product Owner, Scrum Master e Developers. | Não prescreve papéis. | Mantêm-se as responsabilidades do Scrum e usa-se o quadro como ferramenta de gestão do fluxo. |
| **Limites de WIP** | Não são obrigatórios. | São um mecanismo central. | Limites em “Em desenvolvimento” e “Revisão e testes” reduzem multitarefa. |
| **Mudanças** | Evitam-se alterações que coloquem a Sprint Goal em risco durante a Sprint. | Prioridades podem mudar continuamente antes de o item ser puxado. | O PO reordena o backlog; urgências são avaliadas sem desorganizar o trabalho iniciado. |
| **Métricas** | Velocidade, alcance da Sprint Goal e previsibilidade. | Lead time, cycle time, throughput e itens bloqueados. | A equipe observa a meta da Sprint e também os gargalos do fluxo. |

Essa combinação é frequentemente chamada de Scrumban quando práticas de gestão de fluxo do Kanban complementam a cadência e os eventos do Scrum. O objetivo não é misturar cerimônias sem critério, mas preservar transparência, foco e melhoria contínua.

