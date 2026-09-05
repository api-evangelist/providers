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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: ANDPAD's external REST API for integrating partner services with the ANDPAD construction management platform via the ANDPAD App Market. Served from api.andpad.jp with a versioned /v1 base path, JSON r
  name: ANDPAD API
  slug: andpad-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.andpad.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.andpad.jp/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.andpad.jp/reference
- group: company
  title: ''
  type: Website
  url: https://andpad.jp/
- group: company
  title: ''
  type: CompanyWebsite
  url: https://andpad.co.jp/
- group: company
  title: ''
  type: Blog
  url: https://andpad.co.jp/news/
- group: operate
  title: ''
  type: Support
  url: https://andpad.jp/contacts/new
- group: operate
  title: ''
  type: StatusPage
  url: https://status.andpad.jp/
- group: company
  title: ''
  type: Careers
  url: https://hrmos.co/pages/andpad/jobs/140
- group: auth
  title: ''
  type: SecurityTxt
  url: https://andpad.jp/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/andpad-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andpad-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/andpad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/andpad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/andpad-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/andpad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/andpad-problem-types.yml
created: '2026-07-17'
description: ANDPAD (株式会社アンドパッド / ANDPAD Inc.) is Japan's leading cloud construction-management and construction-DX platform, used by more than 260,000 companies and hundreds of thousands of field and office users across new-build housing, renovation, specialty trades, general contracting, and facilities management. The platform spans scheduling, photo and document management, drawings, inspection checklists, chat, billing, and procurement, and exposes an external REST API (api.andpad.jp) plus an app marketplace (ANDPAD App Market) so partners can integrate their own services with ANDPAD. ANDPAD is backed by Hongshan (HongShan / Sequoia China) and operates a public developer site, a system status page, and a published security.txt disclosure channel.
image: https://andpad.jp/wp-content/uploads/OGP_top.jpg
layout: provider
modified: '2026-07-18'
name: ANDPAD
nav: Providers
network: true
overview: 'ANDPAD publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Construction, Construction Management, and Construction DX.


  ANDPAD''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 79.6
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/andpad/refs/heads/main/screenshots/andpad-2026-07-25T200226.png
security:
- kind: authentication
  name: Andpad Authentication
  slug: andpad-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Andpad Domain Security
  slug: andpad-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Andpad Vulnerability Disclosure
  slug: andpad-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: andpad
tags:
- Company
- Technology
- Construction
- Construction Management
- Construction DX
- Software-as-a-Service
- Project Management
- Japan
website: https://andpad.jp/
---
