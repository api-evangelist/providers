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
  url: security/chatail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chatail.com
created: '2026-07-17'
description: Chatail is a Shanghai-based SaaS company (founded 2016) that provides private-domain livestream and video sales software for high-end and luxury retail brands across fashion, jewelry, beauty, automotive, and home-goods verticals, pairing intelligent customer acquisition with conversion tooling ("智能获客与高效转化双轮驱动"). The product is delivered as a hosted web application at chatail.com; no public developer API, documentation portal, or OpenAPI surface is published at this time (api.chatail.com serves a default nginx placeholder). Chatail raised a Series B round led by Qiming Venture Partners and is tracked in the API Evangelist network as a Qiming portfolio company.
image: https://www.chatail.com/static/chatail-logo2.png
layout: provider
modified: '2026-07-18'
name: chatail
nav: Providers
network: true
overview: chatail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Live Commerce, Video, and Retail.
random_paper: 12
score:
  band: minimal
  composite: 5.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/chatail/refs/heads/main/screenshots/chatail-2026-07-25T205127.png
security:
- kind: domain-security
  name: Chatail Domain Security
  slug: chatail-domain-security
  summary_line: no transport/DNS hardening detected
slug: chatail
tags:
- Company
- Software-as-a-Service
- Live Commerce
- Video
- Retail
- Customer Engagement
- China
website: https://www.chatail.com
---
