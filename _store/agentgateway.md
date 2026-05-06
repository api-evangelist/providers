---
aid: agentgateway
name: AgentGateway
description: AgentGateway is an open-source, AI-native proxy and gateway for routing, observing, and governing traffic to and from AI agents, LLM providers, and MCP servers. Built on the A2A and MCP protocols, it provides a unified gateway for LLM consumption, MCP tool federation, agent-to-agent communication, security, and observability. AgentGateway supports multi-provider LLM routing across OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Azure OpenAI with built-in RBAC, JWT authentication, rate limiting, and OpenTelemetry integration.
url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/apis.yml
humanURL: https://agentgateway.dev/
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Gateway
  - API Gateway
  - MCP
  - LLM
  - Agent-to-Agent
  - Open Source
  - CNCF
  - Observability
  - Security
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agentgateway:agentgateway
    name: AgentGateway
    description: AgentGateway provides AI-native gateway capabilities for routing LLM traffic, federating MCP tools, enabling agent-to-agent communication, and applying security and observability controls across AI agent infrastructure.
    humanURL: https://agentgateway.dev/
    baseURL: https://agentgateway.dev
    tags:
      - AI Gateway
      - LLM Routing
      - MCP
      - Agent-to-Agent
      - Security
      - Observability
    properties:
      - type: Documentation
        url: https://agentgateway.dev/docs/
      - type: GettingStarted
        url: https://agentgateway.dev/docs/quickstart/
      - type: GitHubRepository
        url: https://github.com/agentgateway/agentgateway
common:
  - type: GitHubOrganization
    url: https://github.com/agentgateway
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-llm-backend-schema.json
    title: LLM Backend Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-mcp-target-schema.json
    title: MCP Target Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-schema/agentgateway-route-schema.json
    title: Route Schema
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/json-ld/agentgateway-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/agentgateway/refs/heads/main/vocabulary/agentgateway-vocabulary.yaml
  - type: Portal
    url: https://agentgateway.dev/
  - type: Documentation
    url: https://agentgateway.dev/docs/
  - type: GettingStarted
    url: https://agentgateway.dev/docs/quickstart/
  - type: Support
    url: https://discord.gg/y9efgEmppm
  - type: Features
    data:
      - name: LLM Gateway
        description: Routes traffic to OpenAI, Anthropic, Google Gemini, AWS Bedrock, and Azure OpenAI through a unified API with model aliasing, failover, and load balancing.
      - name: MCP Gateway
        description: Connects LLMs to tools via Model Context Protocol with static and dynamic routing, tool federation, and stateful MCP sessions.
      - name: Agent-to-Agent (A2A) Gateway
        description: Enables secure, governed communication between AI agents using the A2A protocol for multi-agent orchestration.
      - name: Inference Routing
        description: Intelligently routes requests to self-hosted models based on GPU utilization and request priority.
      - name: Security and Authentication
        description: Provides JWT, OAuth2, API key management, CORS, CSRF protection, MCP authentication, and external authorization support.
      - name: Traffic Management
        description: Supports request routing and matching, header manipulation, rate limiting, retries, gRPC routing, traffic splitting, and direct responses.
      - name: Observability
        description: Integrates with OpenTelemetry for metrics, traces, and access logging with a built-in Admin UI and debugging tools.
      - name: Guardrails
        description: Applies prompt guards, content filtering, regex filters, moderation policies, and custom webhooks for AI safety.
      - name: Cost Controls
        description: Tracks budget and spend limits per user, team, or application with RBAC-based controls on LLM consumption.
      - name: Prompt Enrichment
        description: Supports prompt templates and enrichment for standardizing and augmenting requests before routing to LLM providers.
  - type: UseCases
    data:
      - name: Unified LLM Routing
        description: Route requests across multiple LLM providers with a single API, enabling failover, load balancing, and cost optimization without changing client code.
      - name: MCP Tool Federation
        description: Aggregate tools from multiple MCP servers behind a single gateway endpoint, enabling agents to discover and invoke tools from any connected MCP server.
      - name: Enterprise AI Governance
        description: Apply organization-wide security policies, rate limits, budget controls, and content filters to all AI agent traffic through a centralized gateway.
      - name: REST API to MCP Conversion
        description: Convert existing REST APIs into MCP-native tool endpoints that AI agents can discover and invoke through the Model Context Protocol.
      - name: Multi-Agent Orchestration
        description: Enable secure agent-to-agent communication using the A2A protocol, allowing specialized agents to delegate tasks to each other through the gateway.
      - name: Observability and Debugging
        description: Collect unified telemetry across all AI agent and LLM interactions to monitor cost, latency, and behavior at scale.
  - type: Integrations
    data:
      - name: OpenAI
        description: Route to OpenAI GPT models through the AgentGateway LLM backend with model aliasing and budget controls.
      - name: Anthropic
        description: Connect to Anthropic Claude models via the unified LLM gateway with failover and load balancing.
      - name: Google Gemini
        description: Route traffic to Google Gemini models through the AgentGateway multi-provider backend.
      - name: AWS Bedrock
        description: Integrate with AWS Bedrock for managed LLM access via the AgentGateway routing layer.
      - name: Azure OpenAI
        description: Route requests to Azure-hosted OpenAI models through the unified gateway API.
      - name: Ollama
        description: Connect to locally hosted Ollama models for self-hosted inference routing.
      - name: vLLM
        description: Route to vLLM inference servers with GPU utilization-aware routing for optimal performance.
      - name: OpenTelemetry
        description: Export metrics, traces, and logs to any OpenTelemetry-compatible observability backend.
      - name: Kubernetes Gateway API
        description: Deploy and configure AgentGateway on Kubernetes using the standard Gateway API for dynamic configuration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
