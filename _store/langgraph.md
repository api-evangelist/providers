---
aid: langgraph
name: LangGraph
description: LangGraph is an open-source framework from LangChain for building stateful, multi-actor agent workflows with low-level primitives for greater control over agent behavior. LangGraph Platform (LangSmith Deployment) provides managed infrastructure for running agents in production with assistants, threads, and runs.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agents
  - Artificial Intelligence
  - Large Language Models
  - Workflows
  - Orchestration
created: '2026-01-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/langgraph/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: langgraph:control-plane
    name: LangSmith Deployment Control Plane API
    description: The LangSmith Deployment Control Plane API is used to programmatically create and manage Agent Server deployments for LangGraph Platform. The API can be orchestrated to create custom CI/CD workflows for deployments, revisions, integrations (GitHub, Forge), authentication providers, and agent connections. Authentication uses the X-Api-Key header.
    humanURL: https://docs.langchain.com/langgraph-platform
    baseURL: https://api.host.langchain.com
    tags:
      - Agents
      - Deployment
      - Control Plane
      - CI/CD
      - Authentication
      - Integrations
    properties:
      - type: Documentation
        url: https://docs.langchain.com/langgraph-platform
      - type: OpenAPI
        url: openapi/langgraph-openapi.json
      - type: Repository
        url: https://github.com/langchain-ai/langgraph
      - type: Authentication
        url: https://docs.langchain.com/langsmith/create-account-api-key
common:
  - name: LangGraph
    url: https://www.langchain.com/langgraph
    type: Website
  - name: LangGraph Documentation
    url: https://docs.langchain.com/langgraph-platform
    type: Documentation
  - name: LangGraph GitHub
    url: https://github.com/langchain-ai/langgraph
    type: GitHub
  - name: LangChain
    url: https://www.langchain.com/
    type: ParentCompany
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
