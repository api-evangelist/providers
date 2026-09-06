---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  url: security/58com-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.58.com/
- group: company
  title: ''
  type: Website
  url: https://www.58.com/
created: '2026-07-17'
description: 58.com (58同城, "58 Tongcheng") is China's largest online classifieds and local-services marketplace, often called the "Chinese Craigslist." Founded in 2005 and headquartered in Beijing, it operates listings across recruitment and jobs, real estate and housing (Anjuke), used goods (Zhuanzhuan), automobiles, local services, and yellow-pages business directories. Formerly listed on the NYSE (WUBA), it was taken private in 2020 by a Warburg Pincus / General Atlantic consortium. Its 58 Open Platform (open.58.com) exposes payment, recruitment/jobs data, housing, local-service information, security risk-control, marketing, and social capabilities to approved third-party partners via reviewed developer accounts and API keys. Backed historically by DCM Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/58com.png
layout: provider
modified: '2026-07-17'
name: 58.com
nav: Providers
network: true
overview: 58.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Classifieds, Marketplace, and Real-Estate.
random_paper: 8
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 6.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/58com/refs/heads/main/screenshots/58com-2026-07-25T181216.png
security:
- kind: domain-security
  name: 58Com Domain Security
  slug: 58com-domain-security
  summary_line: no transport/DNS hardening detected
slug: 58com
tags:
- Company
- Consumer
- Classifieds
- Marketplace
- Real-Estate
- Recruitment
- Local Services
- China
website: https://www.58.com/
---
