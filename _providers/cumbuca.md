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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cumbuca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cumbuca.com/
- group: docs
  title: ''
  type: Documentation
  url: https://juspay-2.gitbook.io/open-finance/pt
- group: start
  title: ''
  type: GettingStarted
  url: https://juspay.io/open-finance
- group: company
  title: ''
  type: Blog
  url: https://www.cumbuca.com/en/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://cumbuca.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cumbuca.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://via.cumbuca.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cumbuca-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cumbuca-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cumbuca-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cumbuca-security.txt
- group: auth
  title: ''
  type: Security
  url: https://cumbuca.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cumbuca-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cumbuca-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cumbuca-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cumbuca-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cumbuca.com/politica-de-seguranca-cibernetica/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cumbuca-llms.txt
created: '2026-07-17'
description: Cumbuca is a Banco Central do Brasil-licensed Payment Institution that provides regulated "proxy" access to Brazil's Pix and Open Finance networks. Acting as a thin, transparent layer with a 1:1 mapping to the official Open Finance Brasil and Central Bank API specifications, it forwards cryptographically signed requests between client infrastructure and the regulated ecosystem so fintechs can build directly on the rails without holding their own license (zero lock-in via certificate swap when they obtain one). Capabilities span Pix payment initiation, Open Finance account and credit-data access, recurring payments, and SCR credit-information queries, with a 0ms median latency overhead and a 99.99% availability SLA. Founded in 2021 in Sao Paulo and backed by Lightspeed Venture Partners and Y Combinator, Cumbuca also ships an Open Finance Data MCP server, the Regulus regulatory AI assistant, public status pages, and the open-source Open Finance Playground developer guide built
  with Juspay.
image: https://cumbuca.com/assets/og-home.png
layout: provider
mcp_servers:
- description: ''
  name: Open Finance Data MCP
  slug: open-finance-data-mcp
modified: '2026-07-18'
name: Cumbuca
nav: Providers
network: true
overview: 'Cumbuca is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Open Finance, Pix, and Payments.


  Cumbuca''s developer surface includes documentation, getting-started guide, engineering blog, support, authentication, and 14 more developer resources.'
random_paper: 40
scopes:
- name: Cumbuca Scopes
  scope_count: 4
  slug: cumbuca-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 79.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cumbuca/refs/heads/main/screenshots/cumbuca-2026-07-25T210921.png
security:
- kind: authentication
  name: Cumbuca Authentication
  slug: cumbuca-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Cumbuca Domain Security
  slug: cumbuca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cumbuca Vulnerability Disclosure
  slug: cumbuca-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cumbuca
tags:
- Company
- Fintech
- Open Finance
- Pix
- Payments
- Banking
- Brazil
- Open Banking
- Financial Data
- MCP
website: https://cumbuca.com/
---
