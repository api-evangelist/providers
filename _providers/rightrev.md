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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RightRev's REST (and GraphQL) API for revenue recognition — transaction ingestion (orders, invoices, events, bulk uploads), policy-set and company configuration, Revenue Desk 360 contract search and d
  name: RightRev REST API
  slug: rightrev-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://rightrev.com
- group: docs
  title: ''
  type: Documentation
  url: https://apis.rightrev.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.rightrev.com/rightrev-rest-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.rightrev.com/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://www.rightrev.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rightrev.com/terms-of-use/
- group: auth
  title: ''
  type: Authentication
  url: authentication/rightrev-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rightrev-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rightrev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rightrev-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rightrev-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rightrev-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rightrev-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rightrev-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rightrev-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rightrev-domain-security.yml
created: '2026-07-17'
description: RightRev is an AI-powered revenue recognition platform that automates ASC 606 and IFRS 15 compliant accounting for subscription, usage-based, and hybrid revenue models. Its API-first architecture ingests orders, invoices, and usage events, applies configurable Standalone Selling Price (SSP) and revenue policies, and produces revenue contracts, revenue and cost schedules, journal entries, and period-close outputs. RightRev exposes REST and GraphQL APIs secured with OAuth 2.0 / OpenID Connect, alongside a Salesforce-native application and ERP integrations for finance teams.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rightrev.png
layout: provider
modified: '2026-07-21'
name: Rightrev
nav: Providers
network: true
overview: 'Rightrev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Revenue Recognition, Accounting, Finance, and Billing.


  Rightrev''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 11 more developer resources.'
random_paper: 14
scopes:
- name: Rightrev Scopes
  scope_count: 2
  slug: rightrev-scopes
  summary_line: 2 scopes
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rightrev/refs/heads/main/screenshots/rightrev-2026-09-02T153819.png
security:
- kind: authentication
  name: Rightrev Authentication
  slug: rightrev-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Rightrev Domain Security
  slug: rightrev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rightrev
tags:
- Company
- Revenue Recognition
- Accounting
- Finance
- Billing
- ASC 606
- IFRS 15
- Revenue
- SaaS Metrics
website: https://rightrev.com
---
