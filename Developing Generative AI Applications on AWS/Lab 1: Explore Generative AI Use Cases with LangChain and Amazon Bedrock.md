In this lab, you learn about the architecture patterns to build applications for key generative AI use cases and work through examples of generating and summarizing text, question answering, and a chatbot.

# 🧪 Resumo do Funcionamento do Laboratório 1 (IA Generativa com LangChain e Amazon Bedrock)

## 🎯 Objetivo Principal
Explorar o uso de **modelos de IA generativa hospedados no Amazon Bedrock** para resolver problemas empresariais reais, como geração e resumo de texto, chatbot, perguntas e respostas e geração de código, integrando com o **LangChain**.

---

## ✅ Etapas e Funcionamento

### 🔹 0. Configuração do Ambiente
- Solicita acesso aos modelos base no **Amazon Bedrock**:
  - **Titan Embeddings G1 - Text**
  - **Nova Lite**
- Abre o **SageMaker Studio** via URL fornecida.
- Clona o repositório Git com os notebooks do laboratório.

> ✅ **Tarefa concluída:** Ambiente configurado e modelos prontos para uso no Bedrock.

---

### 🔹 1. Geração de Texto
Executa dois notebooks:
- **Task1a.ipynb**: Faz geração de texto com **zero-shot prompt** usando Bedrock.
- **Task1b.ipynb**: Utiliza o **LangChain** para criar prompts personalizados com contexto.

> ✅ **Resultado esperado:** Textos gerados de forma personalizada com e sem contexto.

---

### 🔹 2. Resumo de Texto
Executa dois notebooks:
- **Task2a.ipynb**: Resume arquivos pequenos de texto.
- **Task2b.ipynb**: Usa chunking para resumir textos longos.

> ✅ **Resultado esperado:** Resumos otimizados de diferentes tamanhos de texto.

---

### 🔹 3. Perguntas e Respostas com Bedrock
- **Task3.ipynb**: Utiliza o modelo **Nova Lite** para responder perguntas com base em contexto fornecido.

> ✅ **Resultado esperado:** Respostas relevantes e contextuais geradas por IA.

---

### 🔹 4. Criação de Chatbot com IA Generativa
- **Task4.ipynb**: Constrói um chatbot usando os modelos **Nova Lite** e **Titan Embeddings** como base.

> ✅ **Resultado esperado:** Chatbot funcional com compreensão de contexto.

---

### 🔹 5. Geração de Código com Bedrock
- **Task5.ipynb**: Usa prompts em linguagem natural para gerar código automaticamente via LLM.

> ✅ **Resultado esperado:** Blocos de código gerados de acordo com solicitações descritivas.

---

### 🔹 6. Integração com LangChain Agents
- **Task6.ipynb**: Utiliza o modelo "plan-and-execute" com agentes do LangChain, que tomam decisões e executam ações automaticamente.

> ✅ **Resultado esperado:** Execução estruturada de tarefas pela IA com uso de ferramentas externas.

---

## 🧠 Como tudo funciona junto

| Componente                       | Função no sistema                                                            |
|----------------------------------|------------------------------------------------------------------------------|
| **Amazon Bedrock**              | Plataforma de modelos base para IA generativa.                              |
| **SageMaker Studio**            | Ambiente de desenvolvimento com Jupyter para executar notebooks.            |
| **LangChain**                   | Framework para integração de LLMs com agentes e ferramentas externas.       |
| **Modelos Titan / Nova**        | Modelos usados para geração, resumo, Q&A, chatbot e geração de código.      |
| **Notebooks Jupyter**          | Executam as tarefas de IA passo a passo com visualização de resultados.     |

---

## 🚀 Resultado Final

- ✅ Você realizou geração e resumo de textos com IA generativa.
- ✅ Utilizou o Bedrock para responder perguntas com base em contexto.
- ✅ Construiu um chatbot inteligente com modelos base.
- ✅ Gerou código automaticamente a partir de prompts.
- ✅ Integrando tudo com **LangChain Agents** para tomada de decisão e execução.

> 🌟 **Ambiente pronto para aplicação empresarial de IA generativa com Amazon Bedrock.**
