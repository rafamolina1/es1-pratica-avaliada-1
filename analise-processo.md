# Análise de Processo da AgileTech Solutions

**Aluno:** Rafael Oliveira Molina

## 1. Aplicação dos valores do Manifesto Ágil

### Indivíduos e interações mais que processos e ferramentas

Como a equipe possui apenas cinco desenvolvedores e um Product Owner, a comunicação direta deve ser privilegiada. Reuniões curtas, conversas objetivas e colaboração na resolução de problemas evitam que informações importantes fiquem presas em documentos ou ferramentas. O processo continua existindo, mas serve à equipe, em vez de impor burocracia. Isso também permite aproveitar melhor o pouco tempo disponível do cliente.

### Software em funcionamento mais que documentação abrangente

O histórico da empresa mostra que documentos extensos se tornavam desatualizados rapidamente. A AgileTech deve produzir somente a documentação que tenha utilidade real, como critérios de aceite, decisões arquiteturais relevantes e instruções de uso. O principal indicador de progresso será um incremento executável e testado ao fim de cada Sprint. Assim, a startup consegue demonstrar valor ao mercado desde cedo e aprender com o uso do produto.

### Colaboração com o cliente mais que negociação de contratos

Os requisitos são vagos e mudam com frequência, portanto não é produtivo tratá-los como um contrato fechado no início do projeto. O Product Owner deve organizar as necessidades em um Product Backlog e combinar com o cliente momentos curtos e previsíveis de validação. Como a disponibilidade dele é limitada, dúvidas podem ser reunidas e priorizadas antes de cada conversa. A colaboração frequente reduz o risco de a equipe construir algo tecnicamente correto, mas sem valor para o usuário.

### Responder a mudanças mais que seguir um plano

O planejamento continua importante, porém deve ser revisável. A cada Sprint, novas informações podem alterar a prioridade do backlog sem interromper o trabalho que já está em andamento. Entregas pequenas permitem testar hipóteses e incorporar mudanças com custo menor. Isso é especialmente adequado para uma startup que ainda está descobrindo seu produto e precisa reagir ao mercado.

Os termos “mais que” não significam eliminar processos, ferramentas, documentos, contratos ou planos. Eles indicam que os elementos da esquerda devem orientar as decisões quando houver conflito.

## 2. Por que adotar uma abordagem ágil

O processo em cascata pressupõe que seja possível compreender e estabilizar os requisitos antes da implementação. Neste caso, essa premissa não se sustenta: as necessidades iniciais são vagas, o cliente pode mudar de opinião e existe pressão por resultados rápidos. Em cascata, uma validação tardia poderia revelar que meses de análise, documentação e desenvolvimento produziram uma solução inadequada. A correção seria cara porque atravessaria fases consideradas encerradas.

Uma abordagem ágil diminui esse risco ao trabalhar em ciclos curtos. A equipe entrega uma parte utilizável, recebe feedback e reorganiza as próximas prioridades. A visibilidade aumenta, mudanças são tratadas como parte normal do desenvolvimento e o investimento é direcionado primeiro às funcionalidades de maior valor. Para a AgileTech, isso significa aprender rapidamente sem abandonar planejamento, qualidade ou disciplina técnica.

## 3. Práticas a adotar imediatamente

1. **Product Backlog priorizado e refinamento contínuo:** registrar necessidades como histórias pequenas, com valor e critérios de aceite. O Product Owner deve ordenar o backlog por valor, risco e urgência, refinando os próximos itens com a equipe.
2. **Sprints curtas com incrementos demonstráveis:** utilizar ciclos de duas semanas e concluir poucas histórias de ponta a ponta. Cada Sprint deve resultar em software integrado, testado e potencialmente entregável.
3. **Sprint Review com feedback do cliente:** reservar antecipadamente um horário curto com o cliente para demonstrar o incremento e validar as decisões. Se ele não puder participar, pode enviar feedback assíncrono por vídeo ou comentários nos critérios de aceite.
4. **Integração contínua e testes automatizados:** integrar alterações pequenas várias vezes por semana e executar testes automaticamente. Isso reduz conflitos e revela defeitos cedo.
5. **Daily Scrum objetiva:** sincronizar o trabalho em até 15 minutos, destacando progresso, plano imediato e impedimentos, sem transformar a reunião em prestação de contas individual.

## 4. Programação em pares

Na programação em pares, duas pessoas trabalham juntas sobre o mesmo problema. O **driver** escreve o código e mantém o foco no próximo passo; o **navigator** revisa continuamente, pensa no desenho da solução, identifica riscos e sugere alternativas. Os papéis são trocados com frequência. A prática favorece revisão imediata, compartilhamento de conhecimento, redução de defeitos, decisões de design mais conscientes e menor dependência de uma única pessoa.

Em um curso a distância, os principais desafios são conciliar horários, lidar com diferenças de conexão e equipamento, evitar fadiga causada por longas chamadas e manter a participação equilibrada. Também pode ser mais difícil perceber dúvidas do colega, e o compartilhamento de tela pode introduzir atraso. A dupla precisa combinar regras para que o navigator não se torne apenas um observador e para que o trabalho continue sendo realmente colaborativo.

Duas adaptações viáveis são:

1. **Sessões remotas curtas e síncronas:** encontros de 45 a 60 minutos com compartilhamento de tela ou edição colaborativa, troca de papéis a cada 15 ou 20 minutos e um objetivo pequeno definido no início.
2. **Pair programming assíncrono:** uma pessoa implementa um incremento pequeno e registra contexto, decisões e dúvidas; a outra revisa, testa e propõe o próximo passo em seguida. A autoria se alterna a cada ciclo, com uma conversa curta quando surgir uma decisão importante.

## 5. Dificuldades essenciais de Brooks

As quatro dificuldades aparecem no cenário, embora mutabilidade e complexidade sejam as mais evidentes.

| Dificuldade | Manifestação na AgileTech | Mitigação por métodos ágeis |
|---|---|---|
| **Complexidade** | Um sistema de gestão de projetos possui regras, estados, permissões e relações que interagem entre si. Mesmo uma equipe pequena precisa compreender esse domínio. | Histórias pequenas, Design Simples, programação em pares, testes automatizados e refatoração contínua limitam a complexidade acidental e tornam as regras verificáveis. |
| **Conformidade** | O sistema precisa se adaptar a regras do negócio, integrações, padrões web e restrições externas que não foram criados pela equipe. | Refinamentos frequentes, critérios de aceite e entregas integradas revelam cedo incompatibilidades e permitem ajustar a solução antes que elas se espalhem. |
| **Mutabilidade** | Requisitos vagos e mudanças frequentes alteram prioridades e detalhes da solução. É a dificuldade mais diretamente percebida no caso. | Backlog reordenável, Sprints curtas, arquitetura evolutiva e feedback constante acomodam mudanças de modo controlado, sem tentar prever todas as necessidades. |
| **Invisibilidade** | Software não pode ser observado fisicamente; sem uma representação comum, cliente e equipe podem imaginar produtos diferentes. | Quadro Kanban, incremento funcionando, demonstrações, protótipos e critérios de aceite tornam o estado do trabalho e o comportamento esperado mais visíveis. |

Os métodos ágeis não eliminam essas dificuldades essenciais. Eles criam ciclos de inspeção, aprendizado e adaptação que impedem que incertezas se acumulem por muito tempo. A combinação de feedback de negócio com práticas técnicas de XP ajuda a preservar a capacidade de mudança do produto.

