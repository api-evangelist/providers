---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Create end users, capture consent, run data collections (including PSD2 banking data), and retrieve structured wealth data. Dual auth (backend API key + per-user JWT), date-based versioning, and colle
  name: Insurely Open Finance API
  slug: insurely-open-finance-api
artifact_total: 5
asyncapis:
- description: ''
  name: Insurely Collection Webhooks
  slug: insurely-collection-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.insurely.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.insurely.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.insurely.com/integration
- group: docs
  title: ''
  type: APIReference
  url: https://docs.insurely.com/integration/api/collecting-psd2-data/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.insurely.com/integration/api/quick-start/
- group: start
  title: ''
  type: SignUp
  url: https://hub.insurely.com/login/register
- group: operate
  title: ''
  type: Support
  url: https://www.insurely.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.insurely.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.insurely.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/insurely-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insurely-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/insurely-collection-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/insurely-collection-states.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insurely-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/insurely-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/insurely-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insurely-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/insurely-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.insurely.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/insurely-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insurely-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.insurely.com/security
created: '2026-07-17'
description: Insurely is a European open finance platform that provides real-time access to consented, structured financial data across investments, pensions, insurance, savings, and credit. Its Open Finance API lets financial institutions, fintechs, and AI companies create end users, capture user consent, run data collections (including PSD2 banking data), and retrieve normalized wealth data through a signal-and-fetch webhook model. The API pairs a static backend API key with short-lived per-user JWT session tokens, pins versions via a date-based Insurely-Version header, and runs on EU-only AWS infrastructure under ISO/IEC 27001 certification and GDPR compliance. Insurely is backed by Insight Partners.
image: https://assets.insurely.com/images/favicon.png
layout: provider
modified: '2026-07-19'
name: Insurely
nav: Providers
network: true
overview: 'Insurely publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Finance, Insurance, Fintech, and PSD2.


  The Insurely catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Insurely''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 33.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insurely/refs/heads/main/screenshots/insurely-2026-07-25T222626.png
security:
- kind: authentication
  name: Insurely Authentication
  slug: insurely-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Insurely Domain Security
  slug: insurely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Insurely Trust Center
  slug: insurely-trust-center
  summary_line: ISO 27001, GDPR
slug: insurely
tags:
- Company
- Open Finance
- Insurance
- Fintech
- PSD2
- Financial Data
- Data Aggregation
- Pensions
- Wealth
- Europe
website: https://www.insurely.com/
---
