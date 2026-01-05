---
aid: langchain
url: >-
  https://raw.githubusercontent.com/api-evangelist/langchain/refs/heads/main/apis.yml
apis:
  - aid: langchain:langchain
    name: LangChain
    tags:
      - Agents
      - Artificial Intelligence
      - Large Language Models
    humanURL: ' https://www.langchain.com/'
    properties:
      - url: ' https://www.langchain.com/'
        type: Documentation
    description: >-
      LangChain is an open-source framework (Python and JavaScript) for building
      production-grade applications with large language models by composing
      prompts, models, tools, and data into reliable chains and agentic
      workflows. It provides standard interfaces for chat/LLM/embedding models;
      utilities for prompt templating, output parsing, function/tool calling,
      and streaming; and integrations with many model providers, vector stores,
      retrievers, document loaders, and APIs. Its LangChain Expression Language
      (LCEL) and runnables let you declaratively build, test, and deploy
      pipelines; LangGraph supports stateful, multi-actor agents; LangServe
      exposes chains as web APIs; and LangSmith adds tracing, evaluation, and
      observability. Common use cases include retrieval-augmented generation
      over private data, chat and Q&A, structured extraction, coding or data
      agents, and multi-step tool use. In short, LangChain connects LLMs to your
      data and tools and manages the flow between them so you can ship
      maintainable, production-ready AI features.
name: LangChain
tags:
  - Agents
  - Artificial Intelligence
  - Large Language Models
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.langchain.com/
    name: LangChain
    type: Website
    description: 'null'
  - url: https://blog.langchain.com/
    name: LangChain Blog
    type: Blog
    description: 'null'
  - url: https://blog.langchain.com/tag/case-studies/
    name: Case Studies - LangChain Blog
    type: CaseStudies
    description: 'null'
  - url: https://docs.langchain.com/
    name: Home - Docs by LangChain
    type: Documentation
    description: 'null'
  - url: https://www.langchain.com/resources
    name: Resources
    type: Guide
    description: 'null'
  - url: https://changelog.langchain.com/
    name: LangChain - Changelog
    type: ChangeLog
    description: 'null'
  - url: https://www.langchain.com/pricing
    name: Plans and Pricing - LangChain
    type: Pricing
    description: 'null'
  - url: https://support.langchain.com
    name: LangChain Support Portal
    type: Support
    description: 'null'
created: '2026-01-02'
modified: '2026-01-04'
position: Consuming
description: >-
  LangChain is a comprehensive ecosystem for building and deploying AI agents,
  consisting of open-source frameworks and an agent engineering platform called
  LangSmith. The company offers two main frameworks: LangChain, which enables
  rapid development with pre-built agent architectures and model integrations,
  and LangGraph, which provides low-level primitives for building custom agent
  workflows with greater control. LangSmith, their agent engineering platform,
  provides end-to-end capabilities for observability (tracing each step of agent
  execution for debugging), evaluation (building test sets from production data
  and scoring performance), and deployment (infrastructure designed for
  long-running agent workloads with memory, auto-scaling, and enterprise
  security). The platform is framework-neutral and works with any open-source
  framework or custom code, serving use cases like copilots, enterprise GPT,
  customer support automation, research synthesis, code generation, and AI
  search. With over 90 million monthly downloads, 100,000+ GitHub stars, and
  1,000 integrations, LangChain powers top engineering teams from AI startups to
  global enterprises like Klarna, Elastic, and Rakuten, helping them ship
  reliable agents faster while maintaining visibility, control, and durable
  performance at scale.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---