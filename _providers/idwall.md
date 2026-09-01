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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: RESTful JSON API for identity verification, background checks, public-data consultation, document (CNH) validation, verification reports (relatorios) built from configurable matrices (matrizes), peopl
  name: IDwall API v2
  slug: idwall-api-v2
artifact_total: 4
asyncapis:
- description: ''
  name: Idwall Webhooks
  slug: idwall-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://idwall.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.idwall.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.idwall.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.idwall.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.idwall.co/reference/por-onde-comecar
- group: company
  title: ''
  type: Blog
  url: https://idwall.co/blog
- group: start
  title: ''
  type: Login
  url: https://dashboard.idwall.co
- group: operate
  title: ''
  type: Support
  url: https://idwall.co/contato/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.idwall.co/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/idwall-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/idwall-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/idwall-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/idwall-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/idwall-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/idwall-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/idwall-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idwall-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/idwall-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/idwall-webhooks.yml
created: '2026-07-17'
description: IDwall (idwall.co) is a Brazilian identity verification, KYC, and anti-fraud platform. Its REST API lets companies run background checks and consult public data sources, validate documents such as the CNH (Brazilian driver's license), assemble verification reports (relatorios) from configurable matrices (matrizes), retrieve previously queried people (pessoas), and receive webhook notifications when a report's status changes. Authentication is a per-account API token passed in the Authorization header; the production base URL is https://api-v2.idwall.co and all responses are JSON. There is no sandbox - contracted tokens run against production. IDwall was backed by 500 Global and GGV Capital.
image: https://idwall.co/static/favicon.png
layout: provider
modified: '2026-07-19'
name: IDwall
nav: Providers
network: true
overview: 'IDwall publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity Verification, KYC, Fraud Prevention, and Background Checks.


  The IDwall catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IDwall''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 12 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idwall/refs/heads/main/screenshots/idwall-2026-07-25T222043.png
security:
- kind: authentication
  name: Idwall Authentication
  slug: idwall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Idwall Domain Security
  slug: idwall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: idwall
tags:
- Company
- Identity Verification
- KYC
- Fraud Prevention
- Background Checks
- Document Verification
- Compliance
- Onboarding
- Brazil
website: https://idwall.co
---
