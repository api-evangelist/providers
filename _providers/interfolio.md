---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: RESTful API for the Faculty180 (Faculty Activity Reporting) system, exposing faculty listings, courses taught, scholarly contribution and professional (SCP) activity attachments, faculty vita, and pub
  name: Faculty180 Faculty Activity Reporting API
  slug: faculty180-faculty-activity-reporting-api
- description: REST and GraphQL APIs for the Interfolio Faculty Information System covering core Units, Faculty Search (Positions, Position Types/Status, Applications, Application Documents, Reports), and Review, Pr
  name: Interfolio Core, Search & RPT API
  slug: interfolio-core-search-rpt-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.interfolio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.faculty180.com/api_docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.faculty180.com/api_docs
- group: docs
  title: ''
  type: APIReference
  url: https://faculty180.interfolio.com/swagger/ui/
- group: operate
  title: ''
  type: Support
  url: https://product-help.interfolio.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.interfolio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.interfolio.com/resources/
- group: start
  title: ''
  type: SignUp
  url: https://account.interfolio.com/login
- group: start
  title: ''
  type: Login
  url: https://account.interfolio.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elsevier.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elsevier.com/legal/elsevier-website-terms-and-conditions
- group: auth
  title: ''
  type: Authentication
  url: authentication/interfolio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interfolio-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/interfolio-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/interfolio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interfolio-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interfolio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interfolio-llms.txt
created: '2026-07-17'
description: 'Interfolio is a Faculty Information System (now an Elsevier product) that helps colleges and universities manage the full faculty lifecycle: recruiting and hiring (Faculty Search), activity reporting and reviews (Faculty180 / Faculty Activity Reporting), review, promotion and tenure (RPT), lifecycle management, faculty web profiles, and the Dossier application service for individual academics. Interfolio exposes REST and GraphQL APIs for integrating faculty, activity, position, and review data with campus systems, secured with an HMAC public/private key mechanism scoped by tenant. Surfaced as a portfolio company of Insight Partners and enriched with real developer-surface artifacts.'
image: https://assets.interfolio.com/public/images/favicons/apple-touch-icon.png
layout: provider
modified: '2026-07-19'
name: Interfolio
nav: Providers
network: true
overview: 'Interfolio publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Higher Education, Faculty Information System, and Faculty Activity Reporting.


  Interfolio''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interfolio/refs/heads/main/screenshots/interfolio-2026-07-25T222701.png
security:
- kind: authentication
  name: Interfolio Authentication
  slug: interfolio-authentication
  summary_line: hmac · 2 schemes
- kind: domain-security
  name: Interfolio Domain Security
  slug: interfolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: interfolio
tags:
- Company
- Education
- Higher Education
- Faculty Information System
- Faculty Activity Reporting
- Review Promotion Tenure
- Academic
- Research
website: https://www.interfolio.com/
---
