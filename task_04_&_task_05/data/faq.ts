export const FAQ_DB = {
  "What is LangChain?":
    "LangChain is a framework for developing applications powered by language models. It provides tools and abstractions for working with AI models, managing prompts, and creating chains of operations.",
  "How do I install LangChain?":
    "You can install LangChain using npm: 'npm install @langchain/core @langchain/openai'",
  "What are the core components of LangChain?":
    "The core components of LangChain include: Chains (for combining multiple operations), Agents (for dynamic tool usage), and LLMs (Language Model interfaces)",
  "What is a Chain in LangChain?":
    "A Chain in LangChain is a sequence of operations that can be executed in order. It allows you to combine multiple steps like prompting an LLM, processing the output, and using it in another step.",
  "What is an Agent in LangChain?":
    "An Agent in LangChain is an AI that can use tools to accomplish tasks. It decides which actions to take based on user input and can use multiple tools to achieve its goals.",
  "What are LLMs in LangChain?":
    "LLMs (Large Language Models) in LangChain are the AI models that power the framework. LangChain supports various LLM providers like OpenAI, Anthropic, and local models.",
  "How do I create a simple chain?":
    "To create a simple chain in LangChain, you can use LLMChain. First, create a prompt template, initialize an LLM, then combine them: 'const chain = new LLMChain({ llm, prompt })'.",
  "What are prompt templates?":
    "Prompt templates in LangChain are reusable structures for creating prompts. They allow you to define a template with variables that can be filled in later: 'new PromptTemplate({ template: \"Answer: {question}\", inputVariables: [\"question\"] })'.",
  "How do I handle errors in LangChain?":
    "In LangChain, you can handle errors using try-catch blocks. Common errors include API rate limits, token limits, and network issues. Always implement proper error handling in production.",
  "What are memory systems in LangChain?":
    "Memory systems in LangChain allow you to maintain conversation history or state between interactions. Common types include BufferMemory for simple history and VectorDBMemory for more complex storage.",
  "How do I use different LLM providers?":
    "LangChain supports multiple LLM providers. To switch providers, import the appropriate class (e.g., OpenAI, Anthropic) and initialize it with your API key. The rest of your code remains largely unchanged.",
  "What are output parsers?":
    "Output parsers in LangChain help structure LLM outputs into specific formats. They can convert raw text into JSON, lists, or custom objects, making it easier to work with LLM responses.",
  "How do I integrate LangChain with a database?":
    "LangChain can integrate with various databases through VectorStores. Popular options include Pinecone, Supabase, and Chroma. These are useful for semantic search and storing embeddings.",
  "What are embeddings in LangChain?":
    "Embeddings in LangChain are numerical representations of text that capture semantic meaning. They're useful for similarity search, clustering, and other NLP tasks. LangChain supports various embedding models.",
  "How do I implement chat functionality?":
    "LangChain provides ChatModels and MessagePromptTemplates for chat functionality. You can use BufferMemory to maintain conversation history and create interactive chat applications."
} as const;

export type FAQKey = keyof typeof FAQ_DB;