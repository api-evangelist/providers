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
  url: security/ruhnn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ruhnn-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ruhnn.com
coverage:
  checked: '2026-08-13'
  detail: 'Ruhnn runs two client-rendered SPAs — the ruhnn.com corporate site and the www.kol18.com (爱推广) KOL/merchant platform — and neither exposes a developer surface: api., open., developer., dev., docs. and openapi.ruhnn.com all return NXDOMAIN, and every spec and /.well-known path on both hosts answers 200 with the identical HTML app shell rather than a document.'
  evidence:
  - status: 200
    url: https://ruhnn.com/openapi.json
  - status: 200
    url: https://ruhnn.com/.well-known/agent-card.json
  - status: 200
    url: https://www.kol18.com/v2/api-docs
  - status: 404
    url: https://api.github.com/orgs/ruhnn
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Ruhnn Holding Limited (如涵控股) is a Hangzhou-based Chinese influencer (KOL) incubation, marketing, and e-commerce company. It pioneered the "internet celebrity" (wanghong) commercialization model, signing and developing influencers and monetizing their audiences through self-operated online stores on marketplaces such as Taobao and Tmall, as well as through a platform/advertising business that connects its network of KOLs with third-party brands for social-marketing campaigns. The company listed on NASDAQ under the ticker RUHN in 2019 and was subsequently taken private. It is surfaced here as a portfolio company of Qiming Venture Partners. Ruhnn is a consumer-facing influencer marketing and commerce operator and does not publish a public developer platform, API, or SDK surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ruhnn.png
layout: provider
modified: '2026-08-13'
name: ruhnn
nav: Providers
network: true
overview: ruhnn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, E-Commerce, KOL, and Social Commerce.
random_paper: 9
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 0.0
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ruhnn/refs/heads/main/screenshots/ruhnn-2026-09-02T154213.png
security:
- kind: domain-security
  name: Ruhnn Domain Security
  slug: ruhnn-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ruhnn
tags:
- Company
- Influencer Marketing
- E-Commerce
- KOL
- Social Commerce
- Marketing
- China
- Consumer
website: https://ruhnn.com
---
