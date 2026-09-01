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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The embedded credit-card API that powers hi.health. Partners issue and manage cards, cardholders, transactions, receipts, payments, statements and external transfers, with OAuth2 client-credentials au
  name: Pliant Cards-as-a-Service (CaaS) API
  slug: pliant-cards-as-a-service-caas-api
- description: The customer-facing Pro API for programmatic access to Pliant credit-card data and features (cards, cardholders, transactions, receipts, accounting, payments).
  name: Pliant Pro API
  slug: pliant-pro-api
artifact_total: 9
asyncapis:
- description: ''
  name: Hihealth Webhooks
  slug: hihealth-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.getpliant.com/en/industry/insurance-payments/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partner.getpliant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner.getpliant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://partner.getpliant.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.getpliant.com/docs/introduction.md
- group: operate
  title: ''
  type: Support
  url: https://help.getpliant.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://help.getpliant.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://partner.getpliant.com/docs/versioning.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/hihealth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hihealth-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hihealth-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hihealth-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hihealth-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hihealth-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hihealth-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hihealth-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hihealth-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hihealth-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hihealth-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hihealth-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hihealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getpliant.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hihealth-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hihealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/hihealth-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hihealth-changelog.yml
created: '2026-07-17'
description: 'hi.health is a cashless, real-time claims and payments platform for the insurance industry, now operated as "hi.health by Pliant" after joining Pliant. It replaces legacy reimbursement models with instantly issued virtual and physical cards whose spend is programmatically controlled per policy, merchant, currency and country. Members pay nothing upfront: eligible claims are settled in real time at the point of care across health, home, travel, corporate and auto insurance lines, and structured transaction data is streamed back to insurers for dashboards, reconciliation and fraud prevention. The developer surface is Pliant''s PCI-DSS-certified Cards-as-a-Service (CaaS) and Pro API: OAuth2 client-credentials access, asynchronous callback/webhook events, and a full sandbox, which partners embed to issue and manage cards, cardholders, transactions, receipts, payments and external transfers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hihealth.png
layout: provider
mcp_servers:
- description: ''
  name: hi.health MCP Server
  slug: hihealth-mcp-server
modified: '2026-07-19'
name: hi.health
nav: Providers
network: true
overview: 'hi.health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Payments, Cards, and Fintech.


  The hi.health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  hi.health''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 19 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Hihealth Rate Limits
  slug: hihealth-rate-limits
scopes:
- name: Hihealth Scopes
  scope_count: 3
  slug: hihealth-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 36.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 69.7
  previous_composite: 44.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 68.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hihealth/refs/heads/main/screenshots/hihealth-2026-07-25T221215.png
security:
- kind: authentication
  name: Hihealth Authentication
  slug: hihealth-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hihealth Domain Security
  slug: hihealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hihealth Vulnerability Disclosure
  slug: hihealth-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hihealth
tags:
- Company
- Insurance
- Payments
- Cards
- Fintech
- Health
- Cards-as-a-Service
- Embedded Finance
- Reimbursement
- Claims
website: https://www.getpliant.com/en/industry/insurance-payments/
---
