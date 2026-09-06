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
- description: 'Sunyur''s enterprise procurement open integration platform ("聚贤阁"). Exposes an accessToken-authenticated API base at https://open.sunyur.com/api that connects buyers to mainstream e-commerce platforms '
  name: Sunyur Open Platform
  slug: sunyur-open-platform
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.sunyur.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.sunyur.com
- group: docs
  title: ''
  type: Documentation
  url: https://open.sunyur.com/front/#/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/sunyur-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sunyur-error-codes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunyur-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sunyur-well-known.yml
created: '2026-07-17'
description: Sunyur (商越科技 / Beijing Sunyur Network Technology Co., Ltd, 北京商越网络科技有限公司) is a Chinese enterprise procurement digitalization company providing AI-driven procurement solutions for large and medium enterprises. Its products include an intelligent procurement middle-platform (采购中台), an SRM supplier relationship management system, an e-procurement SaaS platform, and a procurement mall (采购商城), helping each customer build a dedicated online, digital, and intelligent enterprise procurement platform to raise efficiency and lower cost. Sunyur operates an open integration platform ("聚贤阁", open.sunyur.com) that connects enterprises to 30+ mainstream e-commerce platforms and 10+ third-party applications through a single accessToken-authenticated API surface. Sunyur is backed by Qiming Venture Partners.
image: https://img.sunyur.com/158313907762748503.png
layout: provider
modified: '2026-07-21'
name: Sunyur
nav: Providers
network: true
overview: 'Sunyur publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, SRM, eProcurement, and Supplier Management.


  Sunyur''s developer surface includes documentation, authentication, and 5 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 13.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunyur/refs/heads/main/screenshots/sunyur-2026-09-02T161156.png
security:
- kind: authentication
  name: Sunyur Authentication
  slug: sunyur-authentication
  summary_line: accessToken · 1 scheme
- kind: domain-security
  name: Sunyur Domain Security
  slug: sunyur-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sunyur
tags:
- Company
- Procurement
- SRM
- eProcurement
- Supplier Management
- Digital Procurement
- Enterprise Software
- Software-as-a-Service
- B2B
- China
- Artificial Intelligence
website: https://www.sunyur.com
---
