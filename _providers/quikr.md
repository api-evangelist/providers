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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.quikr.com
  baseurl_source: declared
  description: The App API from Quikr — 1 operation(s) for app.
  name: Quikr App API
  slug: quikr-app-api
- baseURL: https://api.quikr.com
  baseurl_source: declared
  description: The Platform API from Quikr — 1 operation(s) for platform.
  name: Quikr Platform API
  slug: quikr-platform-api
- baseURL: https://api.quikr.com
  baseurl_source: declared
  description: The Public API from Quikr — 7 operation(s) for public.
  name: Quikr Public API
  slug: quikr-public-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quikr Developer Platform (QDP) App API
  slug: open-quikr-app-api
- collection_type: open
  name: Quikr Developer (QDP) App Platform API
  slug: open-quikr-platform-api
- collection_type: open
  name: Quikr Developer Platform (QDP) App Public API
  slug: open-quikr-public-api
common:
- group: company
  title: ''
  type: Website
  url: https://quikr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.quikr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.quikr.com/index.php/documentation
- group: company
  title: ''
  type: Blog
  url: https://blog.quikr.com
- group: build
  title: ''
  type: SDKs
  url: packages/quikr-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quikr-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quikr-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quikr-llms.txt
created: '2026-07-17'
description: Quikr is India's leading online classifieds platform, describing itself as "India's no. 1 online classifieds platform" for buying, selling, and renting across vehicles, real estate, jobs, mobiles, electronics, furniture, and 300+ service categories, plus education, events, pets, and matrimonial listings. Quikr operates a portfolio of brands including CommonFloor, Hiree, IndiaProperty, and Zefo. The Quikr Developer Platform (QDP) exposes classifieds data and actions to approved partner apps through an invitation-only beta API at api.quikr.com, using custom HMAC-SHA1 signed request headers rather than OAuth. Quikr is backed by Norwest Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quikr.png
layout: provider
modified: '2026-07-20'
name: Quikr
nav: Providers
network: true
overview: 'Quikr publishes 3 APIs on the [APIs.io](https://apis.io/) network: App API, Platform API, and Public API. Tagged areas include Company, Classifieds, Marketplace, Real-Estate, and Automotive.


  Quikr''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 10
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
    contract_quality: 50.3
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 28.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quikr/refs/heads/main/screenshots/quikr-2026-09-02T152654.png
security:
- kind: authentication
  name: Quikr Authentication
  slug: quikr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Quikr Domain Security
  slug: quikr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quikr
tags:
- Company
- Classifieds
- Marketplace
- Real-Estate
- Automotive
- Job
- E-Commerce
- India
- Developer Platform
website: https://quikr.com
---
