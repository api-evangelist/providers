---
aid: context-engineering
url: https://raw.githubusercontent.com/api-evangelist/context-engineering/refs/heads/main/apis.yml
name: Context Engineering
x-type: topic
description: Context engineering is the practice of curating the information that large language models receive at inference time so that the model can perform a task reliably and cost-effectively. It treats the context window as a finite attention budget and looks for the smallest set of high-signal tokens that maximize the likelihood of the desired outcome. Context engineering subsumes and extends prompt engineering, system prompts, tool design, retrieval, agent loops, structured note taking, compaction, and multi-agent decomposition. It is a foundational discipline for building production AI agents and assistants.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agents
  - AI
  - Anthropic
  - Compaction
  - Context Window
  - LLM
  - Memory
  - Prompt Engineering
  - RAG
  - Tools
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: context-engineering:anthropic-guide
    name: Effective Context Engineering for AI Agents
    description: Anthropic's engineering guide to context engineering, framing context as a finite attention budget and walking through system prompts, tool design, few-shot examples, just-in-time retrieval, compaction, structured note taking, and multi-agent architectures.
    humanURL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    baseURL: https://www.anthropic.com
    tags:
      - Anthropic
      - Best Practices
      - Engineering
    properties:
      - type: Documentation
        url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
      - type: Reference
        url: https://docs.anthropic.com/en/docs/agents-and-tools/agent-best-practices
    x-features:
      - Frames context as a finite attention budget
      - Distinguishes context engineering from prompt engineering
      - Covers system prompts, tools, few-shot, and retrieval
      - Long-horizon strategies (compaction, notes, sub-agents)
    x-useCases:
      - Building production AI agents and assistants
      - Tuning system prompts and toolsets for reliability
      - Designing memory and compaction for long-running agents
  - aid: context-engineering:retrieval-augmented-generation
    name: Retrieval-Augmented Generation (RAG)
    description: RAG is a context engineering pattern that augments LLM prompts with passages retrieved at inference time from a vector store, search index, or knowledge base. RAG keeps facts outside the model and is one of the most widely used context engineering techniques.
    humanURL: https://arxiv.org/abs/2005.11401
    baseURL: https://arxiv.org
    tags:
      - Embeddings
      - Knowledge Base
      - RAG
      - Retrieval
    properties:
      - type: Specification
        url: https://arxiv.org/abs/2005.11401
      - type: Reference
        url: https://docs.llamaindex.ai/
      - type: Reference
        url: https://python.langchain.com/docs/concepts/rag/
    x-features:
      - Pluggable retrievers over vector and keyword indexes
      - Pre-retrieval rewriting and post-retrieval re-ranking
      - Hybrid retrieval combining BM25 and dense vectors
      - Citations and grounding for answer auditing
    x-useCases:
      - Domain-specific question answering over private documents
      - Customer support agents with up-to-date knowledge
      - Long-tail factual recall outside model training
  - aid: context-engineering:prompt-engineering
    name: Prompt Engineering
    description: Prompt engineering is the discipline of crafting model instructions and examples to guide model behavior. Prompt engineering remains a sub-discipline of context engineering and includes techniques like role prompting, chain-of-thought, few-shot examples, and structured output formats.
    humanURL: https://www.promptingguide.ai/
    baseURL: https://www.promptingguide.ai
    tags:
      - Few-Shot
      - Instructions
      - Prompting
    properties:
      - type: Documentation
        url: https://www.promptingguide.ai/
      - type: Reference
        url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
      - type: Reference
        url: https://platform.openai.com/docs/guides/prompt-engineering
    x-features:
      - Chain-of-thought and reasoning prompts
      - Few-shot, zero-shot, and self-consistency prompts
      - Structured output formatting (JSON, XML)
      - Role and persona instructions
    x-useCases:
      - Steering model behavior in zero-shot tasks
      - Eliciting structured responses suitable for downstream tools
      - Mitigating undesired outputs through guardrails
  - aid: context-engineering:agent-loops
    name: Agentic Loops and Tool Use
    description: 'Agentic loops are iterative reasoning patterns in which an LLM plans, calls tools, observes results, and refines its plan. Tool design is a central context engineering concern: tools must be token-efficient, have minimal overlap, and include clear, motivating descriptions.'
    humanURL: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
    baseURL: https://docs.anthropic.com
    tags:
      - Agents
      - Function Calling
      - ReAct
      - Tool Use
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
      - type: Reference
        url: https://platform.openai.com/docs/guides/function-calling
      - type: Reference
        url: https://arxiv.org/abs/2210.03629
    x-features:
      - Tool definitions with JSON Schema arguments
      - Iterative plan-act-observe loops
      - Parallel tool invocation
      - Server- and client-side tool execution
    x-useCases:
      - Building task-completing AI agents
      - Wiring LLMs to internal APIs and databases
      - Decomposing complex problems with sub-tools
  - aid: context-engineering:long-horizon-strategies
    name: Long-Horizon Context Strategies
    description: Long-horizon strategies handle conversations and tasks that exceed the context window. Techniques include compaction (summarizing history into a smaller representation), structured note taking (persistent external memory), and multi-agent decomposition where sub-agents handle bounded subtasks and return condensed summaries.
    humanURL: https://www.anthropic.com/news/contextual-retrieval
    baseURL: https://www.anthropic.com
    tags:
      - Compaction
      - Long Context
      - Memory
      - Multi-Agent
    properties:
      - type: Documentation
        url: https://www.anthropic.com/news/contextual-retrieval
      - type: Reference
        url: https://www.anthropic.com/research/swe-bench-sonnet
      - type: Reference
        url: https://github.com/microsoft/autogen
    x-features:
      - Conversation summarization for compaction
      - Persistent memory files for cross-session knowledge
      - Multi-agent decomposition with bounded sub-agents
      - Hierarchical planning over long-running tasks
    x-useCases:
      - Long-running coding agents and SWE assistants
      - Multi-day customer engagements requiring memory
      - Complex research tasks decomposed across sub-agents
common:
  - type: Reference
    url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - type: Reference
    url: https://www.promptingguide.ai/
  - type: Reference
    url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
  - type: Reference
    url: https://docs.llamaindex.ai/
  - type: Reference
    url: https://python.langchain.com/docs/concepts/rag/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
