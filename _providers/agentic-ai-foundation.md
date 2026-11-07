---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Agentic Ai Foundation Agentic Access
  operation_count: 32
  slug: agentic-ai-foundation-agentic-access
  summary_line: 32 operations · 20 acting
api_count: 1
apis:
- description: The Model Context Protocol (MCP) is an open JSON-RPC 2.0 standard for connecting AI applications to external systems — tools, resources and reusable prompt templates. Originally developed by Anthropic
  name: Model Context Protocol (MCP)
  slug: model-context-protocol
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
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: Authentication operations for obtaining tokens to publish servers
  name: Agentic AI Foundation Auth API
  slug: agentic-ai-foundation-auth-api
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: Health check endpoint for monitoring service availability
  name: Agentic AI Foundation Health API
  slug: agentic-ai-foundation-health-api
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: Simple ping endpoint for testing connectivity
  name: Agentic AI Foundation Ping API
  slug: agentic-ai-foundation-ping-api
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: Operations for publishing MCP servers to the registry
  name: Agentic AI Foundation Publish API
  slug: agentic-ai-foundation-publish-api
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: Operations for discovering and retrieving MCP servers
  name: Agentic AI Foundation Servers API
  slug: agentic-ai-foundation-servers-api
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: The validate API from Agentic AI Foundation — 2 operation(s) for validate.
  name: Agentic AI Foundation Validate API
  slug: agentic-ai-foundation-validate-api
- baseURL: https://modelcontextprotocol.io/mcp
  baseurl_source: declared
  description: Version information endpoint for retrieving build and version details
  name: Agentic AI Foundation Version API
  slug: agentic-ai-foundation-version-api
artifact_total: 61
common:
- group: agent
  href: https://artifacts.apis.io/agentic-ai-foundation/agentic-access/agentic-ai-foundation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentic-ai-foundation-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/rules/agentic-ai-foundation-rules.yml
  title: ''
  type: Spectral
  url: rules/agentic-ai-foundation-rules.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/rules/agentic-ai-foundation-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/agentic-ai-foundation-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/vocabulary/agentic-ai-foundation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentic-ai-foundation-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/agentic-ai-foundation/lifecycle/agentic-ai-foundation-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/agentic-ai-foundation-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/agentic-ai-foundation/hosts/agentic-ai-foundation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentic-ai-foundation-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentic-ai-foundation/vendors/agentic-ai-foundation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentic-ai-foundation-vendors.yml
- group: other
  href: https://artifacts.apis.io/agentic-ai-foundation/capabilities/agentic-ai-foundation-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agentic-ai-foundation-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/agentic-ai-foundation/finops/agentic-ai-foundation-finops.yml
  title: ''
  type: FinOps
  url: finops/agentic-ai-foundation-finops.yml
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
  href: https://artifacts.apis.io/agentic-ai-foundation/security/agentic-ai-foundation-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentic-ai-foundation-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentic-ai-foundation/security/agentic-ai-foundation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentic-ai-foundation-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/agentic-ai-foundation/well-known/agentic-ai-foundation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentic-ai-foundation-well-known.yml
- group: auth
  href: https://artifacts.apis.io/agentic-ai-foundation/security/agentic-ai-foundation-domain-security.yml
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
  href: https://artifacts.apis.io/agentic-ai-foundation/mcp/agentic-ai-foundation-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentic-ai-foundation-mcp.yml
- group: build
  href: https://artifacts.apis.io/agentic-ai-foundation/mcp/agentic-ai-foundation-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentic-ai-foundation-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/agentic-ai-foundation/a2a/agentic-ai-foundation-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentic-ai-foundation-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentic-ai-foundation/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/agentic-ai-foundation/llms/agentic-ai-foundation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentic-ai-foundation-llms.txt
- group: build
  href: https://artifacts.apis.io/agentic-ai-foundation/packages/agentic-ai-foundation-packages.yml
  title: ''
  type: Packages
  url: packages/agentic-ai-foundation-packages.yml
- group: build
  href: https://artifacts.apis.io/agentic-ai-foundation/packages/agentic-ai-foundation-packages.yml
  title: ''
  type: SDKs
  url: packages/agentic-ai-foundation-packages.yml
- group: build
  href: https://artifacts.apis.io/agentic-ai-foundation/cli/agentic-ai-foundation-cli.yml
  title: ''
  type: CLI
  url: cli/agentic-ai-foundation-cli.yml
- group: auth
  href: https://artifacts.apis.io/agentic-ai-foundation/authentication/agentic-ai-foundation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentic-ai-foundation-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/conventions/agentic-ai-foundation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentic-ai-foundation-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/errors/agentic-ai-foundation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentic-ai-foundation-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/data-model/agentic-ai-foundation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentic-ai-foundation-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/conformance/agentic-ai-foundation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentic-ai-foundation-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/lifecycle/agentic-ai-foundation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentic-ai-foundation-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/agentic-ai-foundation/changelog/agentic-ai-foundation-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentic-ai-foundation-changelog.yml
- group: other
  href: https://artifacts.apis.io/agentic-ai-foundation/overlays/agentic-ai-foundation-mcp-registry-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentic-ai-foundation-mcp-registry-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/agentic-ai-foundation/plans/agentic-ai-foundation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentic-ai-foundation-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/agentic-ai-foundation/rate-limits/agentic-ai-foundation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentic-ai-foundation-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/vocabulary/agentic-ai-foundation-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/agentic-ai-foundation-vocabulary.yaml
- group: docs
  href: https://artifacts.apis.io/agentic-ai-foundation/json-schema/agentic-ai-foundation-mcp-protocol-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/agentic-ai-foundation-mcp-protocol-schema.json
- group: build
  href: https://artifacts.apis.io/agentic-ai-foundation/examples/agentic-ai-foundation-mcp-tool-example.json
  title: ''
  type: Examples
  url: examples/agentic-ai-foundation-mcp-tool-example.json
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/rules/agentic-ai-foundation-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/agentic-ai-foundation-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/agentic-ai-foundation/json-ld/agentic-ai-foundation-context.jsonld
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
- has_sources: true
  method: derived
  name: Agentic Ai Foundation Finops
  primary_unit: ''
  service_category: ''
  slug: agentic-ai-foundation-finops
  template: true
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
- name: GitHubOIDCTokenExchangeInputBody
  property_count: 1
  slug: agentic-ai-foundation-git-hub-oidctoken-exchange-input-body
- name: GitHubTokenExchangeInputBody
  property_count: 1
  slug: agentic-ai-foundation-git-hub-token-exchange-input-body
- name: HealthBody
  property_count: 2
  slug: agentic-ai-foundation-health-body
- name: Agentic Ai Foundation Mcp Protocol
  property_count: 0
  slug: agentic-ai-foundation-mcp-protocol
- name: MCPResource
  property_count: 5
  slug: agentic-ai-foundation-mcp-resource
- name: MCPTool
  property_count: 4
  slug: agentic-ai-foundation-mcp-tool
- name: OIDCTokenExchangeInputBody
  property_count: 1
  slug: agentic-ai-foundation-oidctoken-exchange-input-body
- name: PingBody
  property_count: 1
  slug: agentic-ai-foundation-ping-body
- name: ServerJSON
  property_count: 11
  slug: agentic-ai-foundation-server-json
- name: ServerListResponse
  property_count: 2
  slug: agentic-ai-foundation-server-list-response
- name: ServerResponse
  property_count: 2
  slug: agentic-ai-foundation-server-response
- name: SignatureTokenExchangeInput
  property_count: 3
  slug: agentic-ai-foundation-signature-token-exchange-input
- name: TokenResponse
  property_count: 2
  slug: agentic-ai-foundation-token-response
- name: UpdateAllVersionsStatusResponse
  property_count: 2
  slug: agentic-ai-foundation-update-all-versions-status-response
- name: UpdateServerStatusBody
  property_count: 2
  slug: agentic-ai-foundation-update-server-status-body
- name: ValidationResult
  property_count: 2
  slug: agentic-ai-foundation-validation-result
- name: VersionBody
  property_count: 3
  slug: agentic-ai-foundation-version-body
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
  slug: agentic-ai-foundation-mcp-yml
modified: '2026-08-30'
name: Agentic AI Foundation
nav: Providers
network: true
overview: 'Agentic AI Foundation publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Health API, Ping API, and 9 more. Tagged areas include AI Agents, Linux Foundation, Open Source, Standards, and MCP.


  The Agentic AI Foundation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agentic AI Foundation''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, product news, support, and 49 more developer resources.'
plans:
- name: Agentic Ai Foundation Plans Pricing
  plan_count: 0
  slug: agentic-ai-foundation-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Agentic Ai Foundation Rate Limits
  slug: agentic-ai-foundation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Agentic AI Foundation — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agentic-ai-foundation-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Agentic AI Foundation API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 1
  slug: agentic-ai-foundation-rules
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 37
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.2
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 58.2
    developer_ergonomics: 78.6
    discoverability: 67.5
    operational_transparency: 42.1
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agentic-ai-foundation/agentic-ai-foundation-2026-06-20T170026.png
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
skill_count: 2
skills:
- name: draft-sep
  slug: agentic-ai-foundation-draft-sep
- name: search-mcp-github
  slug: agentic-ai-foundation-search-mcp-github
slug: agentic-ai-foundation
tags:
- AI Agents
- Linux Foundation
- Open Source
- Standards
- MCP
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
