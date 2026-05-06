---
aid: bifrost
name: Bifrost
description: Bifrost is a high-performance open-source AI gateway that unifies access to 20+ AI providers through a single OpenAI-compatible API. It supports 1,000+ models with adaptive load balancing, automatic failover, semantic caching, and enterprise observability features. Bifrost is open-source under Apache 2.0.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Gateway
  - LLM
  - Load Balancing
  - Open Source
  - OpenAI Compatible
  - MCP
url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: bifrost:bifrost-http-gateway-api
    name: Bifrost HTTP Gateway API
    description: The Bifrost HTTP Gateway API provides an OpenAI-compatible RESTful interface that routes requests to any of 20+ supported AI providers. Requests specify the provider and model using provider/model-name in the model field, enabling seamless provider switching without client code changes.
    humanURL: https://docs.getbifrost.ai/quickstart/gateway/setting-up
    baseURL: http://localhost:8080
    tags:
      - AI Gateway
      - LLM
      - OpenAI Compatible
      - REST
    properties:
      - type: Documentation
        url: https://docs.getbifrost.ai/quickstart/gateway/setting-up
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/openapi/bifrost-http-gateway-api.yaml
  - aid: bifrost:bifrost-go-sdk
    name: Bifrost Go SDK
    description: The Bifrost Go SDK provides a native Go client for embedding the Bifrost AI gateway directly into Go applications using the github.com/maximhq/bifrost/core package.
    humanURL: https://docs.getbifrost.ai/quickstart/go-sdk/setting-up
    baseURL: https://pkg.go.dev/github.com/maximhq/bifrost/core
    tags:
      - AI Gateway
      - Go
      - LLM
      - SDK
    properties:
      - type: Documentation
        url: https://docs.getbifrost.ai/quickstart/go-sdk/setting-up
      - type: GettingStarted
        url: https://docs.getbifrost.ai/quickstart/go-sdk/setting-up
      - type: GitHubRepository
        url: https://github.com/maximhq/bifrost
  - aid: bifrost:bifrost-mcp-gateway
    name: Bifrost MCP Gateway
    description: The Bifrost Model Context Protocol (MCP) Gateway enables AI agents to discover and execute external tools through a standardized protocol, with OAuth 2.0 authentication and tool approval controls.
    humanURL: https://docs.getbifrost.ai/features/mcp
    tags:
      - AI Agents
      - MCP
      - OAuth
      - Tool Execution
    properties:
      - type: Documentation
        url: https://docs.getbifrost.ai/features/mcp
      - type: GitHubRepository
        url: https://github.com/maximhq/bifrost
common:
  - type: Portal
    url: https://www.getmaxim.ai/bifrost/enterprise
  - type: Documentation
    url: https://docs.getbifrost.ai
  - type: GettingStarted
    url: https://docs.getbifrost.ai/quickstart/gateway/setting-up
  - type: GitHubRepository
    url: https://github.com/maximhq/bifrost
  - type: GitHubOrganization
    url: https://github.com/maximhq
  - type: ChangeLog
    url: https://github.com/maximhq/bifrost/releases
  - type: Community
    url: https://discord.gg/exN5KAydbU
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/rules/bifrost-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/vocabulary/bifrost-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/capabilities/ai-chat-routing.yaml
  - type: Features
    data:
      - name: OpenAI-Compatible API
        description: Single API interface compatible with OpenAI SDK for all 20+ providers.
      - name: Adaptive Load Balancing
        description: Distribute requests across providers and models based on availability and performance.
      - name: Automatic Failover
        description: Automatically retry failed requests on alternative providers without client changes.
      - name: Semantic Caching
        description: Cache semantically similar prompts to reduce latency and API costs.
      - name: MCP Gateway
        description: Model Context Protocol gateway for AI agent tool discovery and execution.
      - name: Go SDK
        description: Native Go library for embedding Bifrost gateway directly into applications.
      - name: Enterprise Observability
        description: Built-in metrics, tracing, and logging for production AI gateway deployments.
      - name: Provider Key Management
        description: Centralized API key management for all connected AI providers.
  - type: UseCases
    data:
      - name: Multi-Provider AI Applications
        description: Build applications that can seamlessly switch between OpenAI, Anthropic, and other providers.
      - name: Cost Optimization
        description: Route requests to cheaper providers during peak costs or use caching to reduce API spend.
      - name: High Availability AI
        description: Ensure AI features remain available by failing over across multiple provider accounts.
      - name: AI Agent Tooling
        description: Enable AI agents to discover and execute tools through the MCP gateway protocol.
      - name: LLM Provider Evaluation
        description: A/B test different models and providers without changing application code.
  - type: Integrations
    data:
      - name: OpenAI
        description: Route to OpenAI GPT-4o, GPT-4, and other OpenAI models.
      - name: Anthropic
        description: Route to Claude 3.5 Sonnet, Claude 3 Opus, and other Anthropic models.
      - name: Cohere
        description: Route to Cohere Command and other Cohere models.
      - name: AWS Bedrock
        description: Route to models hosted on AWS Bedrock including Titan and Claude.
      - name: Azure OpenAI
        description: Route to Azure-hosted OpenAI deployments.
      - name: Google Vertex AI
        description: Route to Gemini and other models on Google Vertex AI.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
