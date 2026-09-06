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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Resource-oriented JSON REST API for treasury and payment operations. Paths follow /{namespace}/v#/{resource} across financial-data, payments, iam, connectivity, analytics and accounting namespaces. OA
  name: Atlar API
  slug: atlar-api
artifact_total: 6
asyncapis:
- description: ''
  name: Atlar Webhooks
  slug: atlar-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/atlar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atlar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atlar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.atlar.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlar.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atlar.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atlar.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.atlar.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.atlar.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.atlar.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlar.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.atlar.com/docs/migrate-from-v1-to-v2
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlar.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.atlar.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlar.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.atlar.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/atlar-authentication.yml
- group: auth
  title: ''
  type: OAuthAuthorizationServer
  url: well-known/atlar-oauth-authorization-server.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atlar-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atlar-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atlar-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/atlar-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/atlar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atlar-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/atlar-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atlar-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/atlar-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/atlar-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atlar-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atlar-data-model.yml
created: '2026-07-17'
description: Atlar is a treasury and payment operations platform that centralizes cash management, payments, forecasting, bank reconciliation, and debt and investment management for finance teams. It connects to banks and ERPs (NetSuite, SAP, Dynamics 365, Workday) across 100+ countries and exposes a resource-oriented JSON REST API grouped into product namespaces — financial-data (accounts, balances, transactions), payments (credit transfers, direct debits, counterparties, mandates), connectivity, IAM, analytics/forecasting and accounting. The platform is AI-native, offering a hosted MCP server, signed webhooks, OAuth 2.0 client-credentials auth, idempotency keys, cursor pagination and ETag optimistic concurrency. Atlar is SOC 2 and ISO 27001 certified. It is headquartered in Stockholm and backed by Index Ventures and General Catalyst.
image: https://cdn.prod.website-files.com/656f3c6489ea21aff4dfcf78/692571712cc755c88534f173_atlar-treasury-meta-comp.png
layout: provider
mcp_servers:
- description: ''
  name: Atlar MCP Server
  slug: atlar-mcp-server
modified: '2026-07-18'
name: Atlar
nav: Providers
network: true
overview: 'Atlar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Treasury, Payments, and Banking.


  The Atlar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Atlar''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 24 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 43.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 45.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/screenshots/atlar-2026-07-25T201542.png
security:
- kind: authentication
  name: Atlar Authentication
  slug: atlar-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Atlar Domain Security
  slug: atlar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Atlar Trust Center
  slug: atlar-trust-center
  summary_line: SOC 2, ISO 27001
slug: atlar
tags:
- Company
- Fintech
- Treasury
- Payments
- Banking
- Cash Management
- Financial Operations
- ERP Integration
website: https://www.atlar.com/
---
