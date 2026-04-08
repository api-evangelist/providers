---
aid: toolhouse
url: https://raw.githubusercontent.com/api-evangelist/toolhouse/refs/heads/main/apis.yml
apis:
- aid: toolhouse:platform-api
  name: Toolhouse Platform API
  tags:
  - Agent Runs
  - AI Agents
  - Management
  - Tools
  humanURL: https://docs.toolhouse.ai/toolhouse
  properties:
  - url: https://docs.toolhouse.ai/toolhouse
    type: Documentation
  - url: openapi/toolhouse-openapi-original.yml
    type: OpenAPI
  description: The Toolhouse Platform API provides management and orchestration capabilities for AI agents and tools. It includes endpoints for user profile management, billing, API key administration, tool discovery and execution, agent run management with pagination, Agent Studio chat sessions, and scheduled agent execution via cron expressions. Authentication uses HTTPBearer JWT tokens.
- aid: toolhouse:agents-api
  name: Toolhouse Agents API
  tags:
  - AI Agents
  - Conversations
  - Execution
  - Streaming
  humanURL: https://docs.toolhouse.ai/toolhouse/advanced-concepts/publish-and-run-your-agents
  properties:
  - url: https://docs.toolhouse.ai/toolhouse/advanced-concepts/publish-and-run-your-agents
    type: Documentation
  description: The Toolhouse Agents API enables execution of deployed AI agents via simple HTTP endpoints. Agents defined as code can be deployed and accessed through REST calls that support streaming responses, conversation continuation via run IDs, and full conversation history retrieval. Public agents require no authentication while private agents use Bearer token authorization.
name: Toolhouse
tags:
- Agent Infrastructure
- AI Agents
- Backend as a Service
- Tools
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Toolhouse is a Backend-as-a-Service platform for building, deploying, and managing AI agents. Developers define agents as code and deploy them as APIs with a single command. Agents are automatically connected to over 40 pre-built tools including RAG, memory, code execution, browser automation, web scraping, and database connections.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

