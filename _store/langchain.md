---
aid: langchain
name: LangChain
description: 'LangChain is a comprehensive ecosystem for building and deploying AI agents, consisting of open-source frameworks and an agent engineering platform called LangSmith. The company offers two main frameworks: LangChain, which enables rapid development with pre-built agent architectures and model integrations, and LangGraph, which provides low-level primitives for building custom agent workflows with greater control.'
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agents
  - Artificial Intelligence
  - Large Language Models
  - LLM Observability
  - Tracing
  - Evaluation
created: '2026-01-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/langchain/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: langchain:langsmith
    name: LangSmith API
    description: The LangSmith API is used to programmatically create and manage LangSmith resources including tracer sessions, datasets, examples, workspaces, audit logs, filter views, insights jobs, tags, and prompts. LangSmith is the agent engineering platform maintained by LangChain that provides observability, evaluation, and deployment tooling for LLM and agent applications. The API is OpenAPI 3.1 with 345+ endpoints and uses an X-Api-Key header for authentication.
    humanURL: https://docs.langchain.com/langsmith
    baseURL: https://api.smith.langchain.com
    tags:
      - Agents
      - Artificial Intelligence
      - Large Language Models
      - Observability
      - Tracing
      - Evaluation
      - Datasets
      - Prompts
    properties:
      - type: Documentation
        url: https://docs.langchain.com/langsmith
      - type: OpenAPI
        url: openapi/langchain-openapi.json
      - type: SignUp
        url: https://smith.langchain.com/
      - type: Authentication
        url: https://docs.langchain.com/langsmith/create-account-api-key
common:
  - name: LangChain
    url: https://www.langchain.com/
    type: Website
  - name: LangChain Blog
    url: https://blog.langchain.com/
    type: Blog
  - name: Case Studies
    url: https://blog.langchain.com/tag/case-studies/
    type: CaseStudies
  - name: Documentation
    url: https://docs.langchain.com/
    type: Documentation
  - name: Resources
    url: https://www.langchain.com/resources
    type: Guide
  - name: Changelog
    url: https://changelog.langchain.com/
    type: ChangeLog
  - name: Pricing
    url: https://www.langchain.com/pricing
    type: Pricing
  - name: Support
    url: https://support.langchain.com
    type: Support
  - name: GitHub
    url: https://github.com/langchain-ai
    type: GitHub
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
