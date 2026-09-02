---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: The Model Context Protocol (MCP) is an open JSON-RPC 2.0 standard for connecting AI applications to external systems — tools, resources and reusable prompt templates. Originally developed by Anthropic
  name: Model Context Protocol (MCP)
  slug: model-context-protocol
- description: The Official MCP Registry is the community registry service for Model Context Protocol servers, run by the MCP project. Its REST API publishes a full OpenAPI 3.1.0 contract with 32 operations across t
  name: Official MCP Registry API
  slug: mcp-registry
- description: goose is a general-purpose, open-source AI agent that runs locally. Originally from Block and now governed by AAIF, it is written in Rust, ships a desktop app and a CLI for macOS, Linux and Windows, c
  name: Goose AI Agent
  slug: goose
- description: 'AGENTS.md is a simple, universal convention that gives AI coding agents a consistent, predictable source of project-specific guidance — build commands, test commands, conventions and constraints — in '
  name: AGENTS.md
  slug: agents-md
- description: 'Agent2Agent (A2A) is an open protocol that lets AI agents built by different organisations, on different frameworks, discover each other''s capabilities, communicate, delegate tasks and collaborate on '
  name: Agent2Agent (A2A)
  slug: agent2agent
- description: agentgateway is an open-source data plane for agentic AI — it secures, observes and governs the connections between AI agents, models, MCP tools and APIs across ecosystems. Hosted by AAIF; current rel
  name: agentgateway
  slug: agentgateway
artifact_total: 37
common:
- group: company
  title: ''
  type: Website
  url: https://aaif.io/
- group: start
  title: ''
  type: Portal
  url: https://aaif.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aaif.io/projects
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- group: docs
  title: ''
  type: APIReference
  url: https://registry.modelcontextprotocol.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
- group: company
  title: ''
  type: Blog
  url: https://aaif.io/blog
- group: company
  title: ''
  type: News
  url: https://aaif.io/news
- group: operate
  title: ''
  type: Support
  url: https://aaif.io/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/n8R5VaWDAn
- group: operate
  title: ''
  type: Roadmap
  url: https://modelcontextprotocol.io/development/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aaif
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md
- group: auth
  title: ''
  type: Security
  url: security/agentic-ai-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentic-ai-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/agentic-ai-foundation-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agentic-ai-foundation-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentic-ai-foundation-domain-security.yml
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentic-ai-foundation
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agentic-ai-foundation-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/agentic-ai-foundation-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/agentic-ai-foundation-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentic-ai-foundation-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/agentic-ai-foundation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agentic-ai-foundation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/agentic-ai-foundation-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentic-ai-foundation-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentic-ai-foundation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agentic-ai-foundation-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agentic-ai-foundation-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentic-ai-foundation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentic-ai-foundation-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agentic-ai-foundation-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/agentic-ai-foundation-mcp-registry-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/agentic-ai-foundation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agentic-ai-foundation-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agentic-ai-foundation-vocabulary.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/agentic-ai-foundation-mcp-protocol-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/agentic-ai-foundation-mcp-tool-example.json
- group: design
  title: ''
  type: Rules
  url: rules/agentic-ai-foundation-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/agentic-ai-foundation-context.jsonld
created: '2026-03-16'
description: 'The Agentic AI Foundation (AAIF) is a Linux Foundation project, announced 9 December 2025, that gives the core open standards and projects of the AI agent ecosystem a neutral home. It hosts five projects: Anthropic''s Model Context Protocol (MCP), Block''s goose agent, OpenAI''s AGENTS.md, the Agent2Agent (A2A) protocol, and agentgateway. Platinum members include Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft and OpenAI. AAIF publishes no commercial API of its own; the callable surface in this profile belongs to its hosted projects — the Official MCP Registry REST API, a live anonymous MCP server on the MCP documentation host, and an A2A agent card served from the same host. Eight working groups cover reliability, agentic commerce, governance and regulatory alignment, identity and trust, observability, security and privacy, workflow integration, and taxonomy.'
examples:
- key_count: 5
  name: Agentic Ai Foundation Mcp Resource Example
  slug: agentic-ai-foundation-mcp-resource-example
- key_count: 4
  name: Agentic Ai Foundation Mcp Tool Example
  slug: agentic-ai-foundation-mcp-tool-example
features:
- description: All AAIF projects operate under Linux Foundation neutral governance, ensuring no single vendor controls the direction of AI agent standards.
  name: Neutral Open Governance
- description: MCP is a universal adapter standard enabling AI agents to connect to any external tool, data source, or workflow through a consistent protocol.
  name: Model Context Protocol (MCP)
- description: AAIF standards enable AI agents to run consistently across different platforms, environments, and LLM providers without vendor lock-in.
  name: Cross-Platform Agent Portability
- description: The MCP standard enables a rich ecosystem of 70+ tools and extensions that any compliant agent can discover and invoke.
  name: Tool and Extension Ecosystem
- description: AAIF projects support 15+ LLM providers including Anthropic, OpenAI, Google, Azure, and Ollama through standardized provider interfaces.
  name: Multi-LLM Provider Support
- description: The Agent Communication Protocol (ACP) enables agents to authenticate and communicate with each other and LLM providers through open standards.
  name: Open Agent Communication
finops:
- name: Agentic Ai Foundation Finops
  service_category: API
  slug: agentic-ai-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agentic-ai-foundation.png
integrations:
- description: Native MCP support via the Anthropic Messages API, the originating implementation of the MCP standard.
  name: Claude (Anthropic)
- description: MCP tool integration via the OpenAI Responses API, enabling ChatGPT to invoke MCP-compatible tools.
  name: ChatGPT (OpenAI)
- description: GitHub Copilot in VS Code supports MCP servers for AI-assisted development through the AAIF MCP standard.
  name: VS Code
- description: Cursor IDE integrates MCP tool support for AI-assisted coding agents.
  name: Cursor
- description: AAIF operates under Linux Foundation governance alongside related projects in the LF AI & Data portfolio.
  name: Linux Foundation
json_schemas:
- name: Agentic Ai Foundation Mcp Protocol
  property_count: 0
  slug: agentic-ai-foundation-mcp-protocol
- name: MCPResource
  property_count: 5
  slug: agentic-ai-foundation-mcp-resource
- name: MCPTool
  property_count: 4
  slug: agentic-ai-foundation-mcp-tool
json_structures:
- name: Agentic Ai Foundation Mcp Resource Structure
  property_count: 5
  slug: agentic-ai-foundation-mcp-resource-structure
- name: Agentic Ai Foundation Mcp Tool Structure
  property_count: 4
  slug: agentic-ai-foundation-mcp-tool-structure
jsonld:
- class_count: 5
  name: Agentic Ai Foundation Context
  property_count: 7
  slug: agentic-ai-foundation-context
layout: provider
mcp_servers:
- description: The Model Context Protocol project — the standard AAIF governs — operates a live, anonymous remote MCP server on its own documentation host. tools/list returned HTTP 200 with three tools and full inpu
  name: Agentic AI Foundation MCP Server
  slug: agentic-ai-foundation-mcp-server
modified: '2026-08-30'
name: Agentic AI Foundation
nav: Providers
network: true
overview: 'Agentic AI Foundation publishes 1 API on the [APIs.io](https://apis.io/) network: Official MCP Registry API. Tagged areas include AI Agents, Linux Foundation, Open-Source, Standards, and MCP.


  The Agentic AI Foundation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentic AI Foundation''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, product news, support, and 41 more developer resources.'
plans:
- name: Agentic Ai Foundation Plans Pricing
  plan_count: 0
  slug: agentic-ai-foundation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Agentic Ai Foundation Rate Limits
  slug: agentic-ai-foundation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agentic AI Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agentic-ai-foundation-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 28
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 29.5
    contract_quality: 58.5
    developer_ergonomics: 78.6
    discoverability: 72.2
    governance: 29.5
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 57.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentic-ai-foundation/refs/heads/main/screenshots/agentic-ai-foundation-2026-06-20T170026.png
security:
- kind: authentication
  name: Agentic Ai Foundation Authentication
  slug: agentic-ai-foundation-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentic Ai Foundation Domain Security
  slug: agentic-ai-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Agentic Ai Foundation Vulnerability Disclosure
  slug: agentic-ai-foundation-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: agentic-ai-foundation
tags:
- AI Agents
- Linux Foundation
- Open-Source
- Standards
- MCP
- Agentic AI
- Interoperability
- Agent Protocols
- A2A
- AGENTS.md
- Open Governance
use_cases:
- description: Build MCP-compatible tools once and make them available to any AI agent or client that supports the MCP standard, eliminating integration silos.
  name: Interoperable AI Tool Development
- description: Organizations adopt AAIF standards to ensure their AI agent infrastructure is portable, auditable, and not locked to a single AI vendor.
  name: Enterprise Agent Standardization
- description: Use AAIF protocols to connect specialized AI agents that collaborate on complex tasks, each contributing domain-specific capabilities.
  name: Multi-Agent Workflow Orchestration
- description: Developers build and extend open-source AI agents like goose using the AAIF ecosystem of standards and extensions.
  name: Open-Source Agent Development
website: https://aaif.io/
---
