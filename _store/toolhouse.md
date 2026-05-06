---
aid: toolhouse
url: https://raw.githubusercontent.com/api-evangelist/toolhouse/refs/heads/main/apis.yml
apis:
  - aid: toolhouse:platform-api
    name: Toolhouse Platform API
    tags:
      - Agent Runs
      - AI Agents
      - API Keys
      - Billing
      - Bundles
      - Management
      - Schedules
      - Tools
    humanURL: https://docs.toolhouse.ai/toolhouse
    properties:
      - url: https://docs.toolhouse.ai/toolhouse
        type: Documentation
      - url: openapi/toolhouse-openapi-original.yml
        type: OpenAPI
      - url: rules/toolhouse-rules.yml
        type: SpectralRules
      - url: capabilities/shared/toolhouse-platform.yaml
        type: NaftikoCapability
    description: The Toolhouse Platform API provides management and orchestration capabilities for AI agents and tools. It includes endpoints for user profile management, billing, API key administration, tool discovery and execution, agent run management with pagination, Agent Studio chat sessions, agent file management, agent subscriptions, bundle management, scheduled agent execution via cron expressions, and MCP server configuration. Authentication uses HTTPBearer JWT tokens.
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
  - MCP
  - Tools
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://toolhouse.ai/
    name: Toolhouse Website
    type: Website
    description: 'null'
  - url: https://docs.toolhouse.ai/toolhouse
    name: Toolhouse Documentation
    type: Documentation
    description: 'null'
  - url: https://toolhouse.ai/blog
    name: Toolhouse Blog
    type: Blog
    description: 'null'
  - url: https://toolhouse.ai/pricing
    name: Toolhouse Pricing
    type: Pricing
    description: 'null'
  - url: https://app.toolhouse.ai
    name: Toolhouse Login
    type: Login
    description: 'null'
  - url: https://toolhouse.ai/about
    name: Toolhouse About
    type: About
    description: 'null'
  - url: https://github.com/toolhouseai
    name: Toolhouse GitHub
    type: GitHubOrganization
    description: 'null'
  - url: https://toolhouse.ai/privacy
    name: Toolhouse Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://toolhouse.ai/tos
    name: Toolhouse Terms of Service
    type: TermsOfService
    description: 'null'
  - url: https://x.com/toolhouseai
    name: Toolhouse Twitter
    type: Twitter
    description: 'null'
  - url: https://www.linkedin.com/company/toolhouseai
    name: Toolhouse LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://discord.com/invite/xPvyBxhHtu
    name: Toolhouse Discord
    type: Discord
    description: 'null'
  - url: https://youtube.com/@toolhouseai
    name: Toolhouse YouTube
    type: YouTube
    description: 'null'
  - url: https://help.toolhouse.ai/
    name: Toolhouse Support
    type: Support
    description: 'null'
  - url: https://toolhouse.betteruptime.com/
    name: Toolhouse Status
    type: Status
    description: 'null'
  - url: https://github.com/toolhouseai/toolhouse-sdk-python
    name: Toolhouse Python SDK
    type: SDK
    description: Official Python SDK for integrating Toolhouse into Python applications.
  - url: https://github.com/toolhouseai/toolhouse-sdk-typescript
    name: Toolhouse TypeScript SDK
    type: SDK
    description: Official TypeScript/JavaScript SDK for Toolhouse integration.
  - url: https://github.com/toolhouseai/toolhouse-mcp
    name: Toolhouse MCP Server
    type: Integration
    description: Connect Toolhouse tools to any MCP-compatible client or agent.
  - url: https://github.com/toolhouseai/n8n-nodes-toolhouse
    name: Toolhouse n8n Integration
    type: Integration
    description: n8n workflow automation nodes for Toolhouse.
  - url: json-ld/toolhouse-context.jsonld
    name: Toolhouse JSON-LD Context
    type: JSON-LD
    description: JSON-LD context defining Toolhouse domain vocabulary and linked data mappings.
  - url: json-schema/toolhouse-agent-schema.json
    name: Toolhouse Agent Schema
    type: JSON-Schema
    description: JSON Schema describing the Toolhouse agent entity model and related types.
  - url: json-structure/toolhouse-agent-structure.json
    name: Toolhouse Agent Structure
    type: JSONStructure
    description: Structured documentation of the Toolhouse Agent object model.
  - url: rules/toolhouse-rules.yml
    name: Toolhouse Spectral Rules
    type: SpectralRules
    description: Spectral ruleset enforcing Toolhouse API conventions and standards.
  - url: capabilities/agent-management.yaml
    name: Toolhouse Agent Management Capability
    type: NaftikoCapability
    description: Naftiko workflow capability for full Toolhouse agent lifecycle management.
  - url: vocabulary/toolhouse-vocabulary.yml
    name: Toolhouse Vocabulary
    type: Vocabulary
    description: Vocabulary and taxonomy for the Toolhouse AI agent platform domain.
  - name: Features
    type: Features
    data:
      - name: AI Agent Deployment
      - name: Agent Studio
      - name: Tool Library (40+ tools)
      - name: MCP Server Integration
      - name: RAG Memory
      - name: Code Execution
      - name: Browser Automation
      - name: Web Scraping
      - name: Scheduled Agent Runs
      - name: Agent Observability
      - name: API Key Management
      - name: Agent Subscriptions
      - name: Streaming Responses
      - name: Bundle Management
  - name: Use Cases
    type: UseCases
    data:
      - name: AI Agent Backend-as-a-Service
      - name: Automated Agent Scheduling
      - name: Tool-Augmented LLM Pipelines
      - name: Agent Studio Chat
      - name: MCP Client Integration
      - name: Production Agent Deployment
  - name: Integrations
    type: Integrations
    data:
      - name: OpenAI
      - name: Anthropic Claude
      - name: Vercel AI SDK
      - name: LlamaIndex
      - name: n8n
      - name: MCP Clients
created: '2026-03-26'
modified: '2026-05-03'
position: Consumer
segments:
  - AI Agents
  - Tools
  - Agent Infrastructure
description: Toolhouse is a Backend-as-a-Service platform for building, deploying, and managing AI agents. Developers define agents as code and deploy them as APIs with a single command. Agents are automatically connected to over 40 pre-built tools including RAG, memory, code execution, browser automation, web scraping, and database connections. Toolhouse also provides an MCP server so any MCP-compatible client can access the full tool library. The platform includes Agent Studio for visual agent development, cron-based scheduling, and comprehensive observability through execution logs.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
