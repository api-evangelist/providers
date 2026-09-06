---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://peoplise.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.logo.com.tr/peoplise — a different registrable domain (peoplise.com -> logo.com.tr), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peoplise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peoplise.com
- group: company
  title: ''
  type: Website
  url: https://www.logo.com.tr/peoplise
- group: company
  title: ''
  type: Blog
  url: https://www.logo.com.tr/blog
- group: operate
  title: ''
  type: Support
  url: https://www.logo.com.tr/logo-destek-merkezi
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logo.com.tr/logo-gizlilik-politikalari
created: '2026-07-17'
description: 'Peoplise (now Logo Peoplise) is a Turkish human-resources technology SaaS that digitalizes recruitment and hiring workflows for enterprises. The platform covers the full talent-acquisition funnel: candidate sourcing and application tracking, automated pre-screening and assessments, one-way and live video interviews, reference checking, and digital onboarding. Originally a 500 Global (500 Startups) portfolio company, Peoplise was acquired by Logo (Logo Yazilim), one of Turkey''s largest enterprise-software vendors, and is marketed as "Logo Peoplise" at logo.com.tr. Public probing found a marketing/product site only; no developer portal, OpenAPI/Swagger specification, /.well-known/ discovery surface, or documented public API was found at this time.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peoplise.png
layout: provider
modified: '2026-07-20'
name: Peoplise
nav: Providers
network: true
overview: 'Peoplise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, HR Tech, Recruitment, and Hiring.


  Peoplise''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 8.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peoplise/refs/heads/main/screenshots/peoplise-2026-09-02T151021.png
security:
- kind: domain-security
  name: Peoplise Domain Security
  slug: peoplise-domain-security
  summary_line: TLSv1.3 · DMARC
slug: peoplise
tags:
- Company
- Human Resources
- HR Tech
- Recruitment
- Hiring
- Talent Acquisition
- Video Interview
- Onboarding
- Software-as-a-Service
- Turkey
website: https://peoplise.com
---
