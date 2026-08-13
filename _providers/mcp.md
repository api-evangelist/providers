---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.3
  scored_at: '2026-08-12'
api_count: 17
apis:
- description: The authoritative protocol definition for the Model Context Protocol, maintained at modelcontextprotocol.io and in the modelcontextprotocol/ specification GitHub repository. The TypeScript schema (sch
  name: MCP Specification
  slug: mcp-specification
- description: Official TypeScript SDK published as @modelcontextprotocol/sdk on npm. Dual-purpose library for building MCP servers and clients on Node.js, Bun, and Deno. Supports Standard Schema (Zod, Valibot, ArkT
  name: MCP TypeScript SDK
  slug: mcp-typescript-sdk
- description: Official Python SDK published as `mcp` on PyPI. Includes the FastMCP high-level framework with decorators for tools, resources, and prompts; low-level server primitives for production; client SDK; OAu
  name: MCP Python SDK
  slug: mcp-python-sdk
- description: Official Java SDK for building MCP servers and clients on the JVM. Maintained in the modelcontextprotocol/java-sdk repository.
  name: MCP Java SDK
  slug: mcp-java-sdk
- description: Official Kotlin SDK for MCP servers and clients targeting Kotlin and Android runtimes.
  name: MCP Kotlin SDK
  slug: mcp-kotlin-sdk
- description: Official C# SDK for .NET, maintained in collaboration with Microsoft.
  name: MCP C# SDK
  slug: mcp-c-sdk
- description: Official Swift SDK for MCP servers and clients on Apple platforms.
  name: MCP Swift SDK
  slug: mcp-swift-sdk
- description: Official Rust SDK for MCP servers and clients.
  name: MCP Rust SDK
  slug: mcp-rust-sdk
- description: Canonical collection of reference MCP server implementations maintained by the project. The active servers (Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time) demonstrate every ser
  name: MCP Reference Servers
  slug: mcp-reference-servers
- description: Developer tool for testing and debugging MCP servers. React-based web UI plus Node.js proxy, launched with `npx @modelcontextprotocol/inspector` and accessible at http://localhost:6274. Provides inter
  name: MCP Inspector
  slug: mcp-inspector
- description: Community-driven, Anthropic-maintained registry that functions as an app store for MCP servers. Allows developers to publish server definitions and clients to discover them. Currently in API freeze at
  name: Official MCP Registry
  slug: official-mcp-registry
- description: Third-party MCP server registry and hosted runtime. Catalogs community-built MCP servers, generates installation snippets for clients like Claude Desktop and Cursor, and can host servers on Smithery's
  name: Smithery
  slug: smithery
- description: Third-party MCP directory and news site. Maintains a sub-registry API that implements the Generic MCP Registry API specification with PulseMCP-specific extensions for enriched metadata.
  name: Pulse MCP
  slug: pulse-mcp
- description: Anthropic's Claude Desktop application was the first MCP host. Connects to local MCP servers via stdio transport defined in claude_desktop_config .json and to remote servers via Streamable HTTP with O
  name: Claude Desktop (MCP Host)
  slug: claude-desktop-mcp-host
- description: Cursor IDE supports MCP servers as a first-class extension mechanism, configured via mcp.json. Cursor is one of the most widely used MCP hosts for code-related workflows.
  name: Cursor (MCP Host)
  slug: cursor-mcp-host
- description: VS Code's GitHub Copilot Chat integrates MCP servers as agents and tools. Microsoft has standardized on MCP for Copilot's agent-mode extensibility.
  name: Visual Studio Code (MCP Host)
  slug: visual-studio-code-mcp-host
- description: OpenAI's ChatGPT supports MCP through the Apps SDK and developer tooling documented at developers.openai.com, making MCP a cross-vendor surface for connecting tools and data to ChatGPT.
  name: ChatGPT (MCP Host)
  slug: chatgpt-mcp-host
artifact_total: 66
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/modelcontextprotocol/specification/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/modelcontextprotocol/specification/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md
- group: other
  title: ''
  type: AgentCard
  url: a2a/mcp-a2a.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mcp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcp-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.modelcontextprotocol.io/index.xml
- group: start
  title: ''
  type: Portal
  url: https://modelcontextprotocol.io
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modelcontextprotocol
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/modelcontextprotocol/specification
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mcp-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mcp-context.jsonld
created: '2026-05-22'
description: Model Context Protocol is an open, JSON-RPC 2.0 protocol from Anthropic that standardizes how AI applications (hosts) connect to external systems via servers that expose tools, resources, and prompts. MCP is positioned as "a USB-C port for AI applications" and has become the de-facto integration layer for Claude, ChatGPT, Cursor, Visual Studio Code, and a growing ecosystem of agent runtimes. This topic repo catalogs the canonical specification, the official multi-language SDKs, the reference server collection, community registries (Smithery, Pulse MCP, Naftiko Sandbox), and major MCP-aware clients, plus the vocabulary, JSON Schema, JSON-LD, and example payloads needed to reason about the protocol.
examples:
- key_count: 3
  name: Mcp Error Response Example
  slug: mcp-error-response-example
- key_count: 4
  name: Mcp Initialize Request Example
  slug: mcp-initialize-request-example
- key_count: 3
  name: Mcp Initialize Result Example
  slug: mcp-initialize-result-example
- key_count: 3
  name: Mcp Progress Notification Example
  slug: mcp-progress-notification-example
- key_count: 2
  name: Mcp Prompts Get Example
  slug: mcp-prompts-get-example
- key_count: 2
  name: Mcp Resources List Example
  slug: mcp-resources-list-example
- key_count: 2
  name: Mcp Resources Read Example
  slug: mcp-resources-read-example
- key_count: 2
  name: Mcp Roots List Example
  slug: mcp-roots-list-example
- key_count: 2
  name: Mcp Sampling Create Message Example
  slug: mcp-sampling-create-message-example
- key_count: 2
  name: Mcp Tools Call Example
  slug: mcp-tools-call-example
- key_count: 2
  name: Mcp Tools List Example
  slug: mcp-tools-list-example
features:
- description: MCP defines request, response, and notification message shapes on top of JSON-RPC 2.0 with strict rules on IDs and structure.
  name: JSON-RPC 2.0 Base Protocol
- description: Clients and servers negotiate capabilities during the initialize handshake and maintain stateful connections for the lifetime of the session.
  name: Stateful Sessions
- description: Servers expose callable tools with JSON Schema 2020-12 input schemas; clients invoke them via tools/call.
  name: Tools
- description: Servers expose URI-addressable context (files, database rows, API responses) via resources/list, resources/read, and subscription notifications.
  name: Resources
- description: Servers expose templated prompts and workflows via prompts/list and prompts/get for users to invoke.
  name: Prompts
- description: Clients can offer sampling/createMessage so servers can ask the host LLM to run agentic, recursive inference under user consent.
  name: Sampling
- description: Clients can advertise filesystem roots that bound a server's operating scope via roots/list.
  name: Roots
- description: Servers can request additional information from users mid-session via elicitation/create.
  name: Elicitation
- description: MCP defines stdio for local processes and Streamable HTTP (with an optional SSE legacy mode) for networked deployments.
  name: Multiple Transports
- description: HTTP-based transports follow an MCP-defined OAuth 2.1 authorization framework; stdio transports retrieve credentials from the environment.
  name: OAuth 2.1 Authorization
- description: Implementations, tools, prompts, and resources can publish icon metadata for richer UIs, with strict security constraints on icon URIs.
  name: Icons and Branding
- description: MCP reserves the _meta property with a structured prefix/name format for attaching additional metadata to interactions.
  name: Reserved _meta Namespace
integrations:
- description: Claude Desktop, Claude Code, and the Claude API are first-class MCP hosts and are the protocol's reference consumers.
  name: Anthropic Claude
- description: ChatGPT supports MCP through the Apps SDK and OpenAI's developer docs.
  name: OpenAI ChatGPT
- description: Cursor IDE consumes MCP servers via mcp.json configuration.
  name: Cursor
- description: VS Code's Copilot Chat treats MCP servers as agents and tools.
  name: Visual Studio Code
- description: MCPJam is a community client implementation for testing MCP servers interactively.
  name: MCPJam
json_schemas:
- name: MCP tools/call Request and Result
  property_count: 0
  slug: mcp-call-tool
- name: MCP Initialize Request and Result
  property_count: 0
  slug: mcp-initialize
- name: MCP JSON-RPC Message
  property_count: 0
  slug: mcp-jsonrpc-message
- name: MCP Prompt
  property_count: 6
  slug: mcp-prompt
- name: MCP Resource
  property_count: 9
  slug: mcp-resource
- name: MCP Root
  property_count: 3
  slug: mcp-root
- name: MCP sampling/createMessage Request and Result
  property_count: 0
  slug: mcp-sampling
- name: MCP Tool
  property_count: 8
  slug: mcp-tool
jsonld:
- class_count: 34
  name: Mcp Context
  property_count: 12
  slug: mcp-context
layout: provider
modified: '2026-05-22'
name: Model Context Protocol (MCP)
nav: Providers
network: true
overview: 'Model Context Protocol (MCP) publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Model Context Protocol, MCP, AI Agents, Tools, and Resources.


  The Model Context Protocol (MCP) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Model Context Protocol (MCP)''s developer surface includes engineering blog, developer portal, documentation, and 12 more developer resources.'
random_paper: 80
rules:
- name: Model Context Protocol (MCP) API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: mcp-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 27.4
    developer_ergonomics: 19.6
    discoverability: 61.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 29.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mcp/refs/heads/main/screenshots/mcp-2026-06-20T185104.png
security:
- kind: domain-security
  name: Mcp Domain Security
  slug: mcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mcp Vulnerability Disclosure
  slug: mcp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mcp
solutions:
- description: modelcontextprotocol.io publishes the spec, schema, official SDKs for TypeScript, Python, Java, Kotlin, C#, Swift, and Rust, plus a set of reference servers and an Inspector debugging tool.
  name: Spec, SDKs, and Reference Servers
- description: The official MCP Registry is a central index of MCP servers with GitHub OAuth/OIDC and DNS-based ownership verification.
  name: Official Registry
- description: Smithery and Pulse MCP provide alternative discovery surfaces and, in Smithery's case, hosted execution of community servers.
  name: Third-Party Registries
- description: Claude, ChatGPT, Cursor, VS Code Copilot, Continue, Cline, Zed, Windsurf, and many other assistants act as MCP hosts.
  name: Vendor Hosts
tags:
- Model Context Protocol
- MCP
- AI Agents
- Tools
- Resources
- Prompts
- JSON-RPC
- Anthropic
- Standards
- Topic
use_cases:
- description: MCP servers extend coding assistants like Cursor, VS Code Copilot, and Claude Code with project-aware tools, repository search, and terminal/build access.
  name: IDE Augmentation
- description: MCP resources surface documentation, wikis, and structured data stores to AI hosts under user consent.
  name: Knowledge Base Access
- description: MCP tools let agents trigger build pipelines, send notifications, create tickets, and orchestrate multi-step business workflows.
  name: Workflow Automation
- description: Vendors expose enterprise systems (CRMs, ITSM, data warehouses) as MCP servers so that any MCP-aware host can connect without bespoke integration code.
  name: Enterprise Connectors
- description: Local MCP servers expose filesystem, git, shell, browser, and desktop automation tools to assistants running on the same machine.
  name: Local Computer Use
website: https://modelcontextprotocol.io
---
