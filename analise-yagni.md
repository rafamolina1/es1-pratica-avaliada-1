# Análise do Princípio YAGNI

**Aluno:** Rafael Oliveira Molina

## 1. Conceito

YAGNI significa *You Aren't Gonna Need It* (“você não vai precisar disso”). O princípio recomenda não implementar uma funcionalidade apenas porque ela talvez seja útil no futuro. Na situação atual, o sistema precisa somente cadastrar usuários com nome, e-mail e senha, validar o login e listar os usuários. Todo elemento que não apoia diretamente esses requisitos aumenta o código a compreender, testar e manter sem entregar valor presente.

O hash da senha foi mantido porque é uma proteção básica explicitamente permitida pelo enunciado. A validação de e-mail duplicado também foi preservada por ser um requisito essencial.

## 2. Atributos desnecessários da classe `Usuario`

| Atributo removido | Motivo da violação de YAGNI |
|---|---|
| `id` | Nenhum requisito atual busca ou relaciona usuários por identificador. Ele existia apenas para funcionalidades futuras. |
| `data_cadastro` | Não há requisito de auditoria, ordenação por data ou relatório de cadastro. |
| `ultimo_login` | O login precisa somente validar credenciais; não precisa registrar quando ocorreu. |
| `perfil` | Não existem tipos de perfil ou regras de autorização no escopo atual. |
| `permissoes` | O sistema não precisa conceder, remover ou consultar permissões. |
| `configuracoes` | Não existe requisito de preferências personalizadas. |
| `historico_logins` | Não há auditoria de acessos, e manter esse histórico acrescenta estado e regras desnecessárias. |
| `foto_perfil_url` | O cadastro atual aceita somente nome, e-mail e senha. |
| `telefone` | Não faz parte dos dados solicitados para cadastro. |
| `endereco` | Não faz parte dos dados solicitados para cadastro. |
| `empresa` | Não há informação profissional no requisito atual. |
| `cargo` | Não há informação profissional no requisito atual. |
| `departamento` | Não há informação profissional no requisito atual. |

Os atributos `nome`, `email` e `senha` permanecem porque representam exatamente os dados necessários ao cadastro e à autenticação.

## 3. Métodos desnecessários da classe `Usuario`

| Método removido | Motivo da violação de YAGNI |
|---|---|
| `_gerar_id()` | Serve exclusivamente ao atributo `id`, que não é necessário neste momento. |
| `adicionar_permissao()` | Antecipa um sistema de autorização ainda não solicitado. |
| `remover_permissao()` | Antecipa o gerenciamento de permissões. |
| `tem_permissao()` | Não existe operação atual condicionada a permissões. |
| `atualizar_configuracao()` | Não existe requisito de configurações pessoais. |
| `registrar_login()` | O requisito exige validar o login, não armazenar data, IP ou histórico de acesso. |
| `exportar_json()` | Nenhum formato de exportação foi solicitado. |
| `exportar_xml()` | Adiciona outra representação e uma dependência sem necessidade presente. |
| `atualizar_foto_perfil()` | Foto de perfil está fora do cadastro mínimo. |
| `atualizar_dados_profissionais()` | Empresa, cargo e departamento estão fora do escopo atual. |

Os métodos `_hash_senha()` e `validar_senha()` foram mantidos porque sustentam a validação segura de credenciais.

## 4. Elementos desnecessários de `GerenciadorUsuarios`

Além dos métodos, o gerenciador possuía os atributos `cache` e `indice_email`. O `cache` existia apenas para a busca por ID e foi removido. O `indice_email` poderia acelerar consultas em um volume elevado, mas esse requisito de desempenho não existe; para uma solução pequena, percorrer a lista mantém o desenho mais simples e suficiente.

| Método removido | Motivo da violação de YAGNI |
|---|---|
| `_atualizar_cache()` | Mantinha uma estrutura duplicada apenas para funcionalidades não solicitadas. |
| `buscar_por_id()` | Busca por identificador não está nos requisitos atuais. |
| `buscar_por_perfil()` | Perfis não fazem parte do escopo. |
| `buscar_por_permissao()` | Permissões não fazem parte do escopo. |
| `exportar_todos_json()` | Exportação de usuários não foi solicitada. |
| `importar_usuarios_json()` | Importação não foi solicitada e o método sequer possuía implementação. |
| `gerar_relatorio_atividade()` | Relatórios e métricas de atividade são necessidades apenas hipotéticas. |

Os métodos `cadastrar()`, `fazer_login()` e `listar_todos()` permanecem por corresponderem diretamente às três funcionalidades atuais. O resultado é uma implementação menor, com menos estados para sincronizar, menos dependências e menor custo de mudança.

