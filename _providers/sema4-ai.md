---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The v2 REST API drives the Sema4.ai platform programmatically — list and talk to agents, stream responses, queue and manage Work Items, read data connections, manage MCP servers, and read audits. Each
  name: Sema4.ai REST API
  slug: sema4ai-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://sema4.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sema4.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://sema4.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sema4.ai/docs/v2/api
- group: start
  title: ''
  type: GettingStarted
  url: https://sema4.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://sema4.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sema4.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://sema4.ai/try-team-edition/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sema4.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sema4.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://sema4.ai/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sema4AI
- group: build
  title: ''
  type: Packages
  url: packages/sema4-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sema4-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sema4-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sema4-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sema4-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sema4-ai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sema4-ai-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sema4-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sema4-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sema4-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sema4-ai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sema4-ai-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sema4-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sema4-ai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sema4-ai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sema4-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://sema4.ai/.well-known/responsible-disclosure-policy.html
created: '2026-07-17'
description: Sema4.ai is an enterprise AI agent company building a platform that lets organizations design, run, and manage AI agents that combine actions, intelligence, and enterprise context to transform knowledge work. Its developer surface centers on AI Actions — Python functions exposed to agents via the open-source Sema4.ai Action Server, which serves both an OpenAPI-compatible REST API and a Model Context Protocol (MCP) server. The platform adds a versioned REST API (v2) for driving agents, conversations, Work Items, data connections, MCP servers, and audits programmatically, plus Enterprise and Snowflake-native Team editions. Founded by the team behind Robocorp, Sema4.ai is backed by Mayfield.
image: https://sema4.ai/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Sema4 Ai MCP Server
  slug: sema4-ai-mcp-server
modified: '2026-07-21'
name: Sema4 Ai
nav: Providers
network: true
overview: 'Sema4 Ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Automation, and MCP.


  Sema4 Ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 35.1
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sema4 Ai Authentication
  slug: sema4-ai-authentication
  summary_line: http/openIdConnect · 3 schemes
- kind: domain-security
  name: Sema4 Ai Domain Security
  slug: sema4-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sema4 Ai Vulnerability Disclosure
  slug: sema4-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sema4-ai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Automation
- MCP
- Enterprise AI
- Actions
- Python
- Developer Tools
website: https://sema4.ai
---
