---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Responses-compatible inference REST API fronting many model families through opaque routing, with unauthenticated public catalog/status endpoints and authenticated model-list and Responses endpoints. '
  name: Infer Responses API
  slug: infer-responses-api
artifact_total: 10
collections:
- collection_type: open
  name: Infer by Flow7 Public API
  slug: open-infer-by-flow7-public-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infer-by-flow7-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infer-by-flow7-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://infer.flow7.org/
- group: docs
  title: ''
  type: Documentation
  url: https://infer.flow7.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://infer.flow7.org/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://infer.flow7.org/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://infer.flow7.org/support
- group: company
  title: ''
  type: BlogRSS
  url: https://infer.flow7.org/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://infer.flow7.org/models
- group: start
  title: ''
  type: SignUp
  url: https://infer.flow7.org/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infer.flow7.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infer.flow7.org/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://infer.flow7.org/status
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/infer-by-flow7-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infer-by-flow7-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://infer.flow7.org/.well-known/api-catalog
- group: other
  title: ''
  type: APIsJSON
  url: https://infer.flow7.org/.well-known/apis.json
- group: auth
  title: ''
  type: Security
  url: security/infer-by-flow7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infer-by-flow7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/infer-by-flow7-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/infer-by-flow7-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infer-by-flow7-changelog.yml
created: '2026-08-11'
description: 'A single Responses-compatible inference API that fronts multiple model families through a private, opaque supplier pool. Public paid beta offering a prepaid-wallet billing model, locked prices, spending limits, and per-call receipts for accountable coding-agent inference. Four operations — two of them unauthenticated — cover a machine-readable price catalog, per-model route status with p95 latency, an authenticated selector list, and the Responses endpoint itself. Distinguished by an unusually legible commercial surface: the full rate card, including per-tier margin floors and dated market-reference discounts, is served as JSON without a key, and every completed request returns a receipt with the locked price version and the exact charge.'
image: https://infer.flow7.org/assets/og-infer.png?v=20260811
layout: provider
mcp_servers:
- description: ''
  name: infer-by-flow7-mcp.yml
  slug: infer-by-flow7-mcpyml
modified: '2026-08-11'
name: Infer by Flow7
nav: Providers
network: true
overview: 'Infer by Flow7 publishes 1 API on the [APIs.io](https://apis.io/) network: Infer Responses API. Tagged areas include AI/ML inference, LLM API gateway, Responses-compatible API, Coding-agent tooling, and Developer tools.


  Infer by Flow7''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 15 more developer resources.'
plans:
- name: Infer By Flow7 Plans Pricing
  plan_count: 4
  slug: infer-by-flow7-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Infer By Flow7 Rate Limits
  slug: infer-by-flow7-rate-limits
scopes:
- name: Infer By Flow7 Scopes
  scope_count: 0
  slug: infer-by-flow7-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.4
  delta: 0.9
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 35.2
    developer_ergonomics: 42.9
    discoverability: 70.4
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 49.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infer-by-flow7/refs/heads/main/screenshots/infer-by-flow7-2026-08-17T080956.png
security:
- kind: authentication
  name: Infer By Flow7 Authentication
  slug: infer-by-flow7-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Infer By Flow7 Domain Security
  slug: infer-by-flow7-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Infer By Flow7 Vulnerability Disclosure
  slug: infer-by-flow7-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Infer By Flow7 Trust Center
  slug: infer-by-flow7-trust-center
  summary_line: trust center published
slug: infer-by-flow7
tags:
- AI/ML inference
- LLM API gateway
- Responses-compatible API
- Coding-agent tooling
- Developer tools
- Usage-based billing
- Prepaid billing
- Agent-native
- Agent Skills
- Model routing
website: https://infer.flow7.org/
---
