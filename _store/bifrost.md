---
aid: bifrost
url: https://raw.githubusercontent.com/api-evangelist/bifrost/refs/heads/main/apis.yml
apis:
- aid: bifrost:bifrost-http-gateway-api
  name: Bifrost HTTP Gateway API
  description: The Bifrost HTTP Gateway API provides an OpenAI-compatible RESTful interface that routes requests to any of 20+ supported AI providers. Requests specify the provider and model in the model field using the format provider/model-name, enabling unified access to chat completions and other AI endpoints without changing client code.
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
  - type: Getting Started
    url: https://docs.getbifrost.ai/quickstart/gateway/setting-up
  - type: Reference
    url: https://docs.getbifrost.ai/features/unified-interface
  - type: Authentication
    url: https://docs.getbifrost.ai/quickstart/gateway/provider-configuration
  - type: GitHubRepository
    url: https://github.com/maximhq/bifrost
- aid: bifrost:bifrost-go-sdk
  name: Bifrost Go SDK
  description: The Bifrost Go SDK provides a native Go client for embedding the Bifrost AI gateway directly into Go applications. It implements the same unified provider interface as the HTTP gateway, allowing applications to switch between AI providers without code changes using the github.com/maximhq/bifrost/core package.
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
  - type: Getting Started
    url: https://docs.getbifrost.ai/quickstart/go-sdk/setting-up
  - type: GitHubRepository
    url: https://github.com/maximhq/bifrost
- aid: bifrost:bifrost-mcp-gateway
  name: Bifrost MCP Gateway
  description: The Bifrost Model Context Protocol (MCP) Gateway enables AI agents to discover and execute external tools through a standardized protocol. It supports OAuth 2.0 authentication, tool approval controls, agent mode for autonomous operations, and code mode for AI-orchestrated workflows.
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
name: Bifrost
tags:
- AI Gateway
- LLM
- Load Balancing
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bifrost is a high-performance open-source AI gateway that unifies access to 20+ AI providers through a single OpenAI-compatible API. It supports 1,000+ models with adaptive load balancing, automatic failover, semantic caching, and enterprise observability features.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

