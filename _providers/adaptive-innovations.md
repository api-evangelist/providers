---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-innovations-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaptive.co/
- group: company
  title: ''
  type: Blog
  url: https://adaptive.co/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://adaptive.co/rss.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptive.co/app/privacy
- group: company
  title: ''
  type: Careers
  url: https://adaptive.co/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adaptiveinnovations/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/joinadaptive
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptive-innovations-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/adaptive-innovations-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adaptive-innovations-rate-limits.yml
coverage:
  checked: '2026-09-07'
  detail: 'Adaptive Innovations is a care-delivery company whose software ships only as its own iOS/Android app: adaptive.co is a three-page site (home, blog, careers) with no developer portal, and the one API host that exists, api.adaptive.co, is an unadvertised FastAPI backend for that app whose /openapi.json, /docs and /redoc all answer HTTP 401 "Not authorized".'
  evidence:
  - status: 401
    url: https://api.adaptive.co/openapi.json
  - status: 200
    url: https://api.adaptive.co/health
  - status: 200
    url: https://adaptive.co/sitemap-0.xml
  - status: 404
    url: https://adaptive.co/llms.txt
  - status: 404
    url: https://adaptive.co/.well-known/api-catalog
  - status: 404
    url: https://adaptivehh.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: Adaptive Innovations Co. is an AI-native home health provider headquartered in New York, NY, with operations centered in Texas. Founded in 2025 by Alex Wendland and Logan Stinson (co-CEOs), Hunter Stinson (COO) and Ryan Tolsma (CTO), the company pairs clinicians in the home with an internally built "AI operating system" that automates medical intake, scheduling, charting, and compliance billing. It delivers care under the Adaptive Home Health brand (adaptivehh.com), a Medicare-certified agency that reports 100,000+ patient visits, 500+ referring healthcare organizations and roughly 500 clinical staff. Adaptive raised $60M across a Seed and a $50M Series A (June 2026) led by Felicis and Bain Capital Ventures, with Optum Ventures, BoxGroup, Conviction, SV Angel, Sunflower Capital, Constellation and Dorm Room Fund participating. Its software is operated internally and shipped to patients and clinicians as an iOS/Android app; as of this profile Adaptive publishes no public developer
  program, API reference, or machine-readable contract.
image: https://adaptive.co/og-image.png
layout: provider
modified: '2026-09-07'
name: Adaptive Innovations
nav: Providers
network: true
overview: 'Adaptive Innovations is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Home Health, Health Care Services, and Artificial Intelligence.


  Adaptive Innovations'' developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Adaptive Innovations Plans Pricing
  plan_count: 0
  slug: adaptive-innovations-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Adaptive Innovations Rate Limits
  slug: adaptive-innovations-rate-limits
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adaptive Innovations Domain Security
  slug: adaptive-innovations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptive-innovations
tags:
- Company
- Healthcare
- Home Health
- Health Care Services
- Artificial Intelligence
- Clinical Operations
- Medicare
- Care Delivery
website: https://adaptive.co/
---
