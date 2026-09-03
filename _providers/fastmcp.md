---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: The FastMCP Server is the Python entry point for exposing tools, resources, prompts, and apps to any Model Context Protocol client. Developers instantiate a `FastMCP` server object and register compon
  name: FastMCP Server
  slug: fastmcp-server
- description: The FastMCP Client is a Python client library for talking to any MCP server — local or remote — with full protocol coverage. It supports calling tools, reading resources, getting prompts, declaring ro
  name: FastMCP Client
  slug: fastmcp-client
- description: FastMCP Apps is the framework's runtime for building interactive applications rendered directly inside MCP host conversations. Apps expose UI surfaces — approval flows, choice pickers, form input, and
  name: FastMCP Apps
  slug: fastmcp-apps
- description: FastMCP ships a complete authentication and authorization layer for MCP servers. Servers can verify tokens, terminate OAuth flows directly, or proxy to an external OAuth or OIDC provider, and they can
  name: FastMCP Authentication
  slug: fastmcp-auth
- description: FastMCP can generate an MCP server directly from an existing OpenAPI 3.x description or a FastAPI application, turning every HTTP operation into an MCP tool with auto-generated schemas and validation.
  name: FastMCP OpenAPI and FastAPI Integration
  slug: fastmcp-openapi
- description: The FastMCP CLI is a developer command-line tool for running, inspecting, installing, and debugging MCP servers built with FastMCP. It can launch servers under any transport, inspect their tool/resour
  name: FastMCP CLI
  slug: fastmcp-cli
artifact_total: 45
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PrefectHQ/fastmcp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/PrefectHQ/fastmcp/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/PrefectHQ/fastmcp/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/PrefectHQ/fastmcp/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/PrefectHQ/fastmcp/blob/main/CONTRIBUTING.md
- group: other
  title: ''
  type: AgentCard
  url: a2a/fastmcp-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastmcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gofastmcp.com
- group: start
  title: ''
  type: Portal
  url: https://gofastmcp.com
- group: start
  title: ''
  type: GettingStarted
  url: https://gofastmcp.com/getting-started/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://gofastmcp.com/getting-started/quickstart
- group: other
  title: ''
  type: Installation
  url: https://gofastmcp.com/getting-started/installation
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://gofastmcp.com/changelog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://gofastmcp.com/updates
- group: operate
  title: ''
  type: FAQ
  url: https://gofastmcp.com/more/faq
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PrefectHQ/fastmcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrefectHQ
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/fastmcp
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/uu8dJCgttd
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/deployment/running-server
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/deployment/http
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/deployment/server-configuration
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/deployment/sandboxed-agents
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/deployment/prefect-horizon
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/development/contributing
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/development/releases
- group: docs
  title: ''
  type: Documentation
  url: https://gofastmcp.com/development/tests
- group: commercial
  title: ''
  type: License
  url: https://github.com/PrefectHQ/fastmcp/blob/main/LICENSE
created: '2026-05-25'
description: FastMCP is the fast, Pythonic framework for building Model Context Protocol (MCP) servers, clients, and apps. Originally created by Jeremiah Lowin and maintained by PrefectHQ, FastMCP 1.0 was adopted into the official Anthropic MCP Python SDK in 2024, and the standalone FastMCP project (now at v3) remains the most widely used way to ship MCP servers in Python — the project reports powering roughly 70% of MCP servers across all languages. FastMCP turns ordinary Python functions into MCP tools, resources, prompts, and apps via decorators, auto-generates JSON Schemas from type hints, handles transport negotiation (stdio, Streamable HTTP, SSE), and ships first-class OAuth/OIDC authentication, server composition and proxying, OpenAPI/FastAPI import, a CLI for running and installing servers into Claude Desktop / Claude Code / Cursor / ChatGPT / Gemini CLI / Goose, middleware, lifespan management, elicitation, sampling, progress reporting, OpenTelemetry, and a client library and apps
  runtime for building interactive UIs rendered inside MCP host conversations.
features:
- description: Turn Python functions into MCP tools, resources, and prompts with @mcp.tool / @mcp.resource / @mcp.prompt; schemas are auto-generated from type hints.
  name: Decorator-based tools, resources, and prompts
- description: Three composable surfaces — Server (expose), Client (consume), Apps (interactive UI) — sharing a single runtime, transport, and auth stack.
  name: FastMCP Server, Client, and Apps
- description: Built-in support for stdio, Streamable HTTP, and SSE transports with zero boilerplate.
  name: Transport negotiation
- description: Token verification, OAuth Proxy, OIDC Proxy, remote OAuth, full OAuth server, multi-auth sources, and 15+ provider integrations (Auth0, Cognito, Azure/Entra, GitHub, Google, Discord, Keycloak, OCI, Supabase, WorkOS, AuthKit, Descope, PropelAuth, Scalekit).
  name: First-class authentication
- description: Permit.io and Eunomia integrations for policy-driven authorization.
  name: Authorization providers
- description: Generate an MCP server directly from an OpenAPI spec or FastAPI app so existing REST APIs become agent-callable in one step.
  name: OpenAPI and FastAPI import
- description: Mount servers under namespaces, proxy to other MCP servers (including local, filesystem, and skills providers), and transform tools/prompts/resources between surfaces.
  name: Server composition and proxying
- description: Wrap requests with middleware and inject runtime dependencies into tool handlers.
  name: Middleware and dependency injection
- description: Full MCP protocol coverage including lifespan management, request context, structured logging, progress reporting, and user elicitation.
  name: Lifespan, context, logging, progress, elicitation
- description: Client APIs for LLM sampling against the host model and for spawning background tasks.
  name: LLM sampling and background tasks
- description: Built-in OpenTelemetry tracing for servers.
  name: OpenTelemetry instrumentation
- description: Tool Transformation, Tool Search, Prompts-as-Tools, Resources-as-Tools, Namespace, Component Visibility, and Code Mode transforms.
  name: Tool transforms
- description: Production-grade primitives for paginated responses, server versioning, pluggable storage backends, and component icons.
  name: Pagination, versioning, storage backends, icons
- description: Run, inspect, install, and generate FastMCP servers and clients; one-line install into Claude Desktop, Claude Code, Cursor, ChatGPT, and Gemini CLI.
  name: CLI for running and installing servers
- description: Approval, Choice, Form Input, and File Upload providers plus prefab, generative, and low-level HTML apps rendered inside MCP host conversations.
  name: Apps runtime
- description: FastMCP 1.0 was incorporated into the official Anthropic MCP Python SDK; the standalone FastMCP project (now v3) continues as the leading Python framework, reportedly powering ~70% of MCP servers across all languages.
  name: Anthropic-adopted lineage
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: First-party integration with the Anthropic Messages API; FastMCP 1.0 was adopted into the official Anthropic MCP Python SDK.
  name: Anthropic API
- description: Reference implementation of the Anthropic-stewarded Model Context Protocol specification.
  name: Model Context Protocol
- description: Connect FastMCP servers to OpenAI models and the OpenAI API.
  name: OpenAI API
- description: Integration with Google Gemini SDK and Gemini CLI.
  name: Google Gemini
- description: Drop FastMCP servers into Pydantic AI agents.
  name: Pydantic AI
- description: One-line install for FastMCP servers into Claude Desktop.
  name: Claude Desktop
- description: Install FastMCP servers into Claude Code as MCP tools.
  name: Claude Code
- description: Install FastMCP servers into the Cursor editor.
  name: Cursor
- description: Install FastMCP servers into ChatGPT.
  name: ChatGPT
- description: Integration with Block's Goose agent runtime.
  name: Goose
- description: Import any OpenAPI 3.x spec and serve it as an MCP server.
  name: OpenAPI
- description: Wrap a FastAPI app as an MCP server with one line.
  name: FastAPI
- description: First-class OAuth provider integrations for authenticating MCP servers.
  name: Auth0, AWS Cognito, Azure/Entra ID, GitHub, Google, Discord, Keycloak, OCI IAM, Supabase, WorkOS, AuthKit, Descope, PropelAuth, Scalekit
- description: Policy-driven authorization integrations.
  name: Permit.io and Eunomia
- description: Managed deployment platform for MCP servers from the FastMCP maintainers at PrefectHQ.
  name: Prefect Horizon
layout: provider
modified: '2026-05-25'
name: FastMCP
nav: Providers
network: true
overview: 'FastMCP publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, Python, Framework, Open-Source, and AI Agents.


  FastMCP''s developer surface includes developer portal, getting-started guide, documentation, changelog, release notes, FAQ, and 25 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -8.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 27.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fastmcp/refs/heads/main/screenshots/fastmcp-2026-06-20T181055.png
security:
- kind: domain-security
  name: Fastmcp Domain Security
  slug: fastmcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fastmcp
tags:
- MCP
- Python
- Framework
- Open-Source
- AI Agents
- Tools
- Resources
- Prompts
- LLMs
- Anthropic
use_cases:
- description: Point FastMCP at an OpenAPI spec or FastAPI app to expose every operation as an MCP tool without rewriting handlers.
  name: Wrap an existing REST API as an MCP server
- description: Expose internal utilities (databases, search, ticketing, CI/CD, infra) to Claude, ChatGPT, Cursor, or any MCP host as governed tools.
  name: Build agent-callable internal tools
- description: Use FastMCP Apps to render approval prompts, choice pickers, forms, and file uploads inside agent conversations.
  name: Ship interactive MCP apps
- description: Aggregate multiple MCP servers behind a single namespaced surface with the proxy and namespace transforms.
  name: Proxy and compose third-party MCP servers
- description: Drop in one of 15+ identity providers to authenticate real users into an MCP server without writing OAuth plumbing.
  name: Add OAuth/OIDC to an MCP deployment
- description: Deploy MCP servers over HTTP with structured config, sandboxed agents, OpenTelemetry, and optional Prefect Horizon for managed runtime.
  name: Production deployment of MCP servers
- description: Install FastMCP servers into Claude Desktop, Claude Code, Cursor, ChatGPT, or Gemini CLI via the FastMCP CLI for stdio-based local agent workflows.
  name: Local agent tooling
website: https://gofastmcp.com
---
