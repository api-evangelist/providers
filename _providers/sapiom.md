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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for transaction management, payment authorization, agents, spending rules, analytics, and phone verification. Bearer-token authenticated; JSON envelope with cursor pagination.
  name: Sapiom REST API
  slug: sapiom-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.sapiom.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sapiom.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sapiom.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sapiom.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sapiom.ai/agents/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.sapiom.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sapiom
- group: start
  title: ''
  type: SignUp
  url: https://app.sapiom.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.sapiom.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.sapiom.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.sapiom.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.sapiom.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sapiom-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sapiom-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/sapiom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sapiom-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sapiom-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sapiom-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sapiom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sapiom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sapiom-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sapiom-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sapiom-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sapiom-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapiom-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sapiom-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sapiom-data-model.yml
created: '2026-07-17'
description: 'Sapiom is an execution engine for AI agents that gives agents and code instant, pay-per-use access to a catalog of paid capabilities through a single API key and wallet — no per-vendor accounts. Capabilities include web search and scraping, access to 400+ AI models, image/video generation, audio/text-to-speech, browser automation, compute sandboxes, databases (Postgres/Redis/vector/search), messaging and queues, file storage, private git repositories, GitHub export, email enrichment, domains/DNS, and phone verification. It is reachable three ways: a typed SDK client (@sapiom/tools / ctx.sapiom.*), a hosted remote MCP server (~130 tools), and a REST API (https://api.sapiom.ai/v1) for transaction, agent, spending-rule, and analytics management. Metered access is authorized via an x402 (HTTP 402) payment flow with per-agent spend rules. Sapiom is backed by Accel.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sapiom.png
layout: provider
mcp_servers:
- description: ''
  name: Sapiom MCP Server
  slug: sapiom-mcp-server
modified: '2026-07-21'
name: Sapiom
nav: Providers
network: true
overview: 'Sapiom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Infrastructure, and MCP.


  Sapiom''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, CLI, and 21 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: Sapiom Rate Limits
  slug: sapiom-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 82.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 37.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sapiom Authentication
  slug: sapiom-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sapiom Domain Security
  slug: sapiom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sapiom
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Infrastructure
- MCP
- API Gateway
- Payments
- Agentic Commerce
- Developer Tools
- SDK
website: https://www.sapiom.ai/
---
