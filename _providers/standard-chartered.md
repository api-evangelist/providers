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
  url: security/standard-chartered-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/standardchartered
- group: company
  title: ''
  type: Website
  url: https://www.sc.com/
- group: company
  title: ''
  type: About
  url: https://www.sc.com/en/about/
- group: company
  title: ''
  type: Investors
  url: https://www.sc.com/en/investors/
- group: company
  title: ''
  type: News
  url: https://www.sc.com/en/press-releases/
- group: company
  title: ''
  type: Careers
  url: https://www.sc.com/en/careers/
- group: company
  title: ''
  type: Blog
  url: https://www.sc.com/en/feed/
created: '2026-05-05'
description: A British multinational banking and financial services company headquartered in London with a strong focus on Asia, Africa, and the Middle East. Provides corporate, institutional, and consumer banking across more than 50 markets globally.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/standard-chartered.png
layout: provider
modified: '2026-05-16'
name: Standard Chartered
nav: Providers
network: true
overview: 'Standard Chartered is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Banks, and Global Banking.


  Standard Chartered''s developer surface includes product news, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 1.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 1.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/standard-chartered/refs/heads/main/screenshots/standard-chartered-2026-06-20T194500.png
security:
- kind: domain-security
  name: Standard Chartered Domain Security
  slug: standard-chartered-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: standard-chartered
tags:
- Financial
- Banks
- Global Banking
website: https://www.sc.com/
---
