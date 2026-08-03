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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Alloovium's public REST API v2 for document intelligence over construction projects — vault (projects, documents, hybrid search), chat (grounded, cited answers), workflows (automation runs), and templ
  name: Alloovium API
  slug: alloovium-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.alloovium.com/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.alloovium.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.alloovium.com/en/developers/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alloovium.com/en/developers/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alloovium-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alloovium-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alloovium.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alloovium.com/en/docs/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alloovium.com/en/docs/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.alloovium.com/en/contact
- group: auth
  title: ''
  type: Security
  url: https://www.alloovium.com/en/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/alloovium-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alloovium-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alloovium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alloovium-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alloovium-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alloovium-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/alloovium-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alloovium-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alloovium-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alloovium-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alloovium-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alloovium-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/alloovium-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alloovium-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alloovium-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Alloovium is an AI-native document intelligence and compliance platform for the construction industry. It reads construction project documents (contracts, specifications, drawings, submittals, RFIs, and emails), answers questions with page-level citations, extracts and cross-references data, tracks obligations and deadlines, and drafts variations, RFIs, reports, and compliance evidence behind a human review gate. Alloovium exposes a public REST API v2 and a hosted Model Context Protocol (MCP) server so agents and integrations can query the vault, run chat, execute workflows, and fill templates. Founded by Zander Schweitzer and Cielo Nicolosi, Alloovium is a Y Combinator Summer 2026 company based in Brisbane, Australia.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alloovium.png
layout: provider
mcp_servers:
- description: Hosted Streamable-HTTP MCP server at https://api.alloovium.com/api/v1/mcp/ exposing 15 tools over the vault, chat, workflows, and templates; authenticated with an Alloovium API key (Bearer ak_live_).
  name: Alloovium MCP Server
  slug: alloovium-mcp-server
modified: '2026-07-17'
name: Alloovium
nav: Providers
network: true
overview: 'Alloovium publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Document Intelligence, Compliance, and Artificial Intelligence.


  Alloovium''s developer surface includes documentation, API reference, getting-started guide, changelog, pricing, support, authentication, and 20 more developer resources.'
random_paper: 34
rate_limits:
- limit_count: 0
  name: Alloovium Rate Limits
  slug: alloovium-rate-limits
scopes:
- name: Alloovium Scopes
  scope_count: 9
  slug: alloovium-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 43.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 43.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alloovium/refs/heads/main/screenshots/alloovium-2026-07-25T195710.png
security:
- kind: authentication
  name: Alloovium Authentication
  slug: alloovium-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Alloovium Domain Security
  slug: alloovium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alloovium Vulnerability Disclosure
  slug: alloovium-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Alloovium Trust Center
  slug: alloovium-trust-center
  summary_line: SOC 2 Type I, ISO 27001
slug: alloovium
tags:
- Company
- Construction
- Document Intelligence
- Compliance
- Artificial Intelligence
- Construction Technology
- Documents
- MCP
website: https://www.alloovium.com/en/developers
---
