---
aid: composio
name: Composio
description: Composio is a unified API and tooling platform for AI agents with 1000+ pre-built connectors, managed OAuth, tool search, context management, and a sandboxed workbench to help you build AI agents that turn intent into action.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - Authentication
  - Integrations
  - OAuth
  - Tools
  - Unified_API
created: '2026-03-03'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/apis.yml
specificationVersion: '0.19'
x-type: company
apis:
  - aid: composio:tool-router-api
    name: Composio Tool Router API
    description: Session-based API for AI agents to discover and execute tools. The Tool Router provides the primary interface for AI agents to find relevant tools and execute actions through Composio's unified platform.
    humanURL: https://docs.composio.dev/reference
    baseURL: https://backend.composio.dev/api/v3
    tags:
      - AI Agents
      - Sessions
      - Tools
    properties:
      - type: Documentation
        url: https://docs.composio.dev/reference
      - type: OpenAPI
        url: openapi/composio-openapi-original.yml
      - type: OpenAPI
        url: https://backend.composio.dev/api/v3/openapi.json
      - type: Spectral Rules
        url: rules/composio-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/composio-tool-router.yml
    features:
      - title: Session Lifecycle
        description: Create sessions that scope an AI agent's tool discovery and execution.
      - title: Connected Account Binding
        description: Sessions are scoped to a single connected account for authenticated calls.
    useCases:
      - title: Agent Runtime
        description: Power AI agents that discover and execute tools at runtime within an isolated session.
  - aid: composio:tools-api
    name: Composio Tools API
    description: Enables listing, searching, and executing individual actions within toolkits. The Tools API allows developers to discover available tools, filter by toolkit or capability, and execute specific actions on behalf of connected users.
    humanURL: https://docs.composio.dev/reference/api-reference/tools
    baseURL: https://backend.composio.dev/api/v3
    tags:
      - Actions
      - Execution
      - Tools
    properties:
      - type: Documentation
        url: https://docs.composio.dev/reference/api-reference/tools
      - type: OpenAPI
        url: openapi/composio-openapi-original.yml
      - type: OpenAPI
        url: https://backend.composio.dev/api/v3/openapi.json
      - type: Spectral Rules
        url: rules/composio-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/composio-tool-router.yml
    features:
      - title: Tool Discovery
        description: List and search tools across toolkits with filtering on toolkit and capability.
      - title: Action Execution
        description: Execute a specific tool with structured arguments on behalf of a connected user.
    useCases:
      - title: Tool Calling
        description: Surface a curated set of tools to an LLM for tool calling use cases.
      - title: Agent Action Execution
        description: Execute the tool selected by an agent to take real-world action.
  - aid: composio:connected-accounts-api
    name: Composio Connected Accounts API
    description: Handles management of user OAuth connections to applications. The Connected Accounts API enables creating, listing, and managing authenticated connections between end users and third-party applications through Composio's managed OAuth flow.
    humanURL: https://docs.composio.dev/reference/api-reference/connected-accounts
    baseURL: https://backend.composio.dev/api/v3
    tags:
      - Accounts
      - Authentication
      - Connections
      - OAuth
    properties:
      - type: Documentation
        url: https://docs.composio.dev/reference/api-reference/connected-accounts
      - type: OpenAPI
        url: openapi/composio-openapi-original.yml
      - type: OpenAPI
        url: https://backend.composio.dev/api/v3/openapi.json
      - type: Spectral Rules
        url: rules/composio-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/composio-tool-router.yml
    features:
      - title: Managed OAuth
        description: Initiate and manage OAuth flows that connect users to third-party apps.
      - title: Account Lifecycle
        description: List, retrieve, and disconnect connected accounts.
    useCases:
      - title: User Onboarding
        description: Walk a user through connecting their third-party accounts to an AI agent.
      - title: Account Management UI
        description: Power "connections" management screens in agent applications.
  - aid: composio:auth-configs-api
    name: Composio Auth Configs API
    description: Allows configuration of authentication methods for toolkit access. Auth configs contain developer credentials and app-level settings such as scopes and authentication methods, and can be reused across all users.
    humanURL: https://docs.composio.dev/reference/api-reference/auth-configs
    baseURL: https://backend.composio.dev/api/v3
    tags:
      - Authentication
      - Configuration
      - OAuth
    properties:
      - type: Documentation
        url: https://docs.composio.dev/reference/api-reference/auth-configs
      - type: OpenAPI
        url: openapi/composio-openapi-original.yml
      - type: OpenAPI
        url: https://backend.composio.dev/api/v3/openapi.json
      - type: Spectral Rules
        url: rules/composio-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/composio-tool-router.yml
    features:
      - title: Reusable Auth Profiles
        description: Centralize OAuth client IDs, secrets, and scopes for reuse across users.
      - title: Per-Toolkit Configuration
        description: Define auth methods (OAuth2, API key, basic) per toolkit.
    useCases:
      - title: White-Label OAuth
        description: Expose your own branded OAuth experience to end users for each integrated toolkit.
  - aid: composio:triggers-api
    name: Composio Triggers API
    description: Manages webhook subscriptions from connected applications. The Triggers API enables developers to set up and manage event-driven notifications from third-party applications, allowing AI agents to respond to real-time events.
    humanURL: https://docs.composio.dev/reference/api-reference/triggers
    baseURL: https://backend.composio.dev/api/v3
    tags:
      - Events
      - Triggers
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.composio.dev/reference/api-reference/triggers
      - type: OpenAPI
        url: openapi/composio-openapi-original.yml
      - type: OpenAPI
        url: https://backend.composio.dev/api/v3/openapi.json
      - type: Spectral Rules
        url: rules/composio-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/composio-tool-router.yml
    features:
      - title: Webhook Subscriptions
        description: Subscribe to event-driven notifications from connected applications.
      - title: Trigger Inventory
        description: List active trigger subscriptions per user, project, or toolkit.
    useCases:
      - title: Event-Driven Agents
        description: Wake AI agents in response to real-world events from connected applications.
  - aid: composio:toolkits-api
    name: Composio Toolkits API
    description: Provides browsing capabilities for available applications and their associated tools. The Toolkits API allows developers to discover and explore the 1000+ available integrations across services like GitHub, Gmail, Slack, Notion, and more.
    humanURL: https://docs.composio.dev/reference/api-reference/toolkits
    baseURL: https://backend.composio.dev/api/v3
    tags:
      - Applications
      - Integrations
      - Toolkits
    properties:
      - type: Documentation
        url: https://docs.composio.dev/reference/api-reference/toolkits
      - type: OpenAPI
        url: openapi/composio-openapi-original.yml
      - type: OpenAPI
        url: https://backend.composio.dev/api/v3/openapi.json
      - type: Spectral Rules
        url: rules/composio-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/composio-tool-router.yml
    features:
      - title: Toolkit Catalog
        description: Browse over 1000 toolkits across categories such as productivity, dev tools, and CRM.
      - title: Toolkit Detail
        description: Retrieve a single toolkit with its associated tools and metadata.
    useCases:
      - title: Integration Selection
        description: Allow agent builders to pick the right integrations for their use case.
      - title: App Marketplace UI
        description: Power an in-product app marketplace inside agentic applications.
common:
  - type: Portal
    url: https://app.composio.dev/dashboard
  - type: Documentation
    url: https://docs.composio.dev/docs
  - type: Getting Started
    url: https://docs.composio.dev/docs/quickstart
  - type: API Reference
    url: https://docs.composio.dev/reference
  - type: OpenAPI
    url: https://backend.composio.dev/api/v3/openapi.json
  - type: Authentication
    url: https://docs.composio.dev/faq/api_key/api_key
  - type: Blog
    url: https://composio.dev/blog
  - type: Status
    url: https://status.composio.dev
  - type: Pricing
    url: https://composio.dev/pricing
  - type: Change Log
    url: https://docs.composio.dev/docs/changelog
  - type: Privacy Policy
    url: https://composio.dev/privacy
  - type: Terms of Service
    url: https://composio.dev/terms
  - type: GitHub Organization
    url: https://github.com/ComposioHQ
  - type: GitHub Repo
    url: https://github.com/ComposioHQ/composio
  - type: Python SDK
    url: https://github.com/ComposioHQ/composio
  - type: Node.js SDK
    url: https://www.npmjs.com/package/@composio/client
  - type: Sign Up
    url: https://app.composio.dev/dashboard
  - type: JSON-LD
    url: json-ld/composio-context.jsonld
  - type: JSONSchema
    url: json-schema/composio-tool-schema.json
  - type: JSONSchema
    url: json-schema/composio-toolkit-schema.json
  - type: JSONSchema
    url: json-schema/composio-connected-account-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
