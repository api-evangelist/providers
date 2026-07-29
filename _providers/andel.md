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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Andel Agentic Access
  operation_count: 5
  slug: andel-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 2
apis:
- description: The purchases API from Andel — 2 operation(s) for purchases.
  name: Andel purchases API
  slug: andel-purchases-api
- description: The webhooks API from Andel — 2 operation(s) for webhooks.
  name: Andel webhooks API
  slug: andel-webhooks-api
artifact_total: 8
asyncapis:
- description: ''
  name: Andel Data Exchange Webhooks
  slug: andel-data-exchange-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://build.andel.org
- group: docs
  title: ''
  type: Documentation
  url: https://build.andel.org/home/welcome/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://build.andel.org/dataexchange
- group: start
  title: ''
  type: GettingStarted
  url: https://build.andel.org/dataexchange/overview/overview
- group: company
  title: ''
  type: Blog
  url: https://www.andel.org/blog
- group: operate
  title: ''
  type: Support
  url: https://www.andel.org/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.andel.org/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.andel.org/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.andel.org/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.andel.org
- group: agent
  title: ''
  type: MCPServer
  url: mcp/andel-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/andel-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/andel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/andel-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/andel-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/andel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/andel-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/andel-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/andel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/andel-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/andel-data-exchange-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/andel-data-exchange-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andel-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/andel-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.andel.org
created: '2026-07-17'
description: Andel is a cooperative marketplace for drug affordability that unlocks direct manufacturer pricing on high-spend specialty medications, connecting health plans, PBMs, and members without rebates, spreads, or intermediaries across neurology, immunology, dermatology, oncology, fertility, cardiometabolic, and rare/orphan therapeutic areas. Its Data Exchange API provides real-time, RFC 9457-compliant interchange of member purchase events between Andel and counterparty plans or PBMs, with OAuth 2.0 machine-to-machine authentication via Descope, per-plan authorization, cursor pagination, purchase.created webhooks, and Express Scripts (ESI) CDH accumulator-format compatibility.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/andel.png
layout: provider
mcp_servers:
- description: ''
  name: andel-mcp.yml
  slug: andel-mcpyml
modified: '2026-07-17'
name: Andel
nav: Providers
network: true
overview: 'Andel publishes 2 APIs on the [APIs.io](https://apis.io/) network: purchases API and webhooks API. Tagged areas include Company, Healthcare, Pharmacy, Pharmacy Benefits, and Drug Pricing.


  The Andel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Andel''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 42
scopes:
- name: Andel Scopes
  scope_count: 1
  slug: andel-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 49.6
  delta: -3.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.0
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/andel/refs/heads/main/screenshots/andel-2026-07-25T200224.png
security:
- kind: authentication
  name: Andel Authentication
  slug: andel-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Andel Domain Security
  slug: andel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andel
tags:
- Company
- Healthcare
- Pharmacy
- Pharmacy Benefits
- Drug Pricing
- Specialty Medications
- Data Exchange
- Webhooks
website: https://www.andel.org
---
