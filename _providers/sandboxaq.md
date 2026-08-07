---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Sandboxaq Agentic Access
  operation_count: 55
  slug: sandboxaq-agentic-access
  summary_line: 55 operations · 9 acting
api_count: 3
apis:
- description: 'The Flint AI Platform API gives programmatic access to everything the Flint AI Platform discovers about an organization''s AI estate: the agents found in code, the models, tools and MCP servers they us'
  name: Flint AI Platform API
  slug: flint-ai-platform-api
- description: AQtive Guard is SandboxAQ's cryptography and non-human-identity management platform, built on the Cryptosense analyzer it acquired. Its API is GraphQL, served at /api/v2 and authenticated with an API-
  name: AQtive Guard API
  slug: aqtive-guard-api
- description: A fully managed, per-tenant Model Context Protocol server that exposes SandboxAQ's proprietary scientific AI models as callable tools inside Claude and other MCP clients. It carries the aqcat tool (de
  name: SandboxAQ MCP Server
  slug: mcp-server
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sandboxaq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sandboxaq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sandboxaq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flintai.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flintai.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flintai.dev/flintai/api-reference/index
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flintai.dev/flintai/cli/guides/scan-quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.sandboxaq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sandbox-quantum
- group: operate
  title: ''
  type: Support
  url: https://docs.aisim.sandboxaq.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.sandboxaq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sandboxaq.com/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sandboxaq.com/legal/privacy-policy
- group: other
  title: ''
  type: Products
  url: https://www.sandboxaq.com/products
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/sandboxaq-stock
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/sandboxaq-flint-ai-platform-openapi.json
- group: docs
  title: ''
  type: GraphQL
  url: graphql/sandboxaq-aqtive-guard.graphql
- group: other
  title: ''
  type: Protobuf
  url: grpc/sandboxaq-sandwich-sandwich.proto
- group: other
  title: ''
  type: AgentCard
  url: a2a/sandboxaq-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sandboxaq-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sandboxaq-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sandboxaq-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/sandboxaq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sandboxaq-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sandboxaq-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sandboxaq-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sandboxaq-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sandboxaq-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sandboxaq-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sandboxaq-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sandboxaq-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sandboxaq-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sandboxaq-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sandboxaq-flint-ai-platform-overlay.yaml
created: '2026-08-02'
description: 'SandboxAQ (SB Technology, Inc.) builds Large Quantitative Models (LQMs) — AI systems that fuse physics, chemistry and proprietary scientific data — and ships them as commercial platforms with public developer surfaces. Three product lines carry callable APIs: AQtive Guard, a cryptography and non-human-identity posture-management platform (built on the Cryptosense analyzer) exposing a GraphQL API at /api/v2 plus a fleet of language and network sensors; Flint AI, an AI-agent security platform whose Platform API is a documented OpenAPI 3.0.3 contract over an inventory graph of agents, models, tools and MCP servers, paired with the flintai CLI and a Python guardrails SDK; and the SandboxAQ MCP Server, a per-tenant OAuth-protected Model Context Protocol endpoint that exposes the AQCat adsorption and AQPotency proteochemometric potency models as tools for LLM clients.'
image: https://cdn.prod.website-files.com/622a3cfaa89636b753810f04/623911fca65004cb868ec3ec_SandboxAQ-social-share.jpg
layout: provider
mcp_servers:
- description: ''
  name: sandboxaq-mcp.yml
  slug: sandboxaq-mcpyml
modified: '2026-08-02'
name: SandboxAQ
nav: Providers
network: true
overview: 'SandboxAQ publishes 1 API on the [APIs.io](https://apis.io/) network: Flint AI Platform API. Tagged areas include Company, Artificial Intelligence, Security, Cryptography, and Post-Quantum Cryptography.


  SandboxAQ''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 28 more developer resources.'
random_paper: 57
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 48.1
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Sandboxaq Authentication
  slug: sandboxaq-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Sandboxaq Domain Security
  slug: sandboxaq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sandboxaq
tags:
- Company
- Artificial Intelligence
- Security
- Cryptography
- Post-Quantum Cryptography
- Agents
- Model Context Protocol
- Simulation
- Drug Discovery
- Materials Science
- AI Security
- Quantum
website: https://www.sandboxaq.com/
---
