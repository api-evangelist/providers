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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.domesystems.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.domesystems.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.domesystems.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.domesystems.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://domesystems.ai/get-started
- group: operate
  title: ''
  type: Support
  url: https://domesystems.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://domesystems.ai/perspectives
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dome-systems
- group: start
  title: ''
  type: SignUp
  url: https://domesystems.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://login.domesystems.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domesystems.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domesystems.ai/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/dome-systems-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/dome-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dome-systems-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dome-systems-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dome-systems-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dome-systems-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dome-systems-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dome-systems-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dome-systems-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dome-systems-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dome-systems-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dome-systems-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dome-systems-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.domesystems.ai/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dome-systems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dome-systems-domain-security.yml
created: '2026-07-17'
description: Dome Systems is the enterprise agentic operations platform — the system of control for the agent era. Founded in 2024 by Dave McJannet (former HashiCorp CEO) and Marc Holmes, and backed by Redpoint Ventures, Bessemer Venture Partners, and Mango Capital, Dome registers every AI agent, governs every tool and model call against policy, and produces an immutable audit trail across the estate — regardless of runtime, cloud, or who built the agent. The Dome Platform is three control points — Registry (code), Gateway (tools), and Broker (models) — on a control plane of Cedar-based Authorization and Audit, administered through Go and Python SDKs, a REST API, a CLI, and a built-in MCP surface that exposes Dome itself to AI assistants.
image: https://www.domesystems.ai/favicon.ico
layout: provider
mcp_servers:
- description: The Dome Platform CLI ships a built-in MCP server that exposes Dome itself to Claude and other MCP clients for triage and review of the agentic estate (agents, tools, models, policy, and audit). Launc
  name: Dome Systems MCP Server
  slug: dome-systems-mcp-server
modified: '2026-07-18'
name: Dome Systems
nav: Providers
network: true
overview: 'Dome Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Governance, AI Operations, and Authorization.


  Dome Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dome-systems/refs/heads/main/screenshots/dome-systems-2026-07-25T212250.png
security:
- kind: authentication
  name: Dome Systems Authentication
  slug: dome-systems-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Dome Systems Domain Security
  slug: dome-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dome Systems Vulnerability Disclosure
  slug: dome-systems-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dome-systems
tags:
- Company
- AI Agents
- Agent Governance
- AI Operations
- Authorization
- Audit
- MCP
- Enterprise
- Cedar Policy
- LLM
website: https://www.domesystems.ai/
---
