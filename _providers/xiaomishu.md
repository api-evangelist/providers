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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xiaomishu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.xiaomishu.com
- group: company
  title: ''
  type: About
  url: http://www.xiaomishu.com/about/aboutus/
- group: other
  title: ''
  type: MobileSite
  url: https://m.xiaomishu.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xiaomishu-llms.txt
created: '2026-07-17'
description: Xiaomishu (订餐小秘书, "Dining Little Secretary") is a Shanghai-based restaurant reservation and dining-marketing technology company operating since 2005 via xiaomishu.com and the 021-57575777 booking hotline. Its platforms — 订餐小秘书, 宴位 (Yanwei, an AI-driven dynamic-pricing product for restaurant private rooms), and 高能店长 — let diners book tables and discounted private-room packages at Shanghai restaurants through web, WAP (m.xiaomishu.com / m.57.cn), phone, and WeChat mini-program channels. The company cites strategic investment from Ctrip and SIG and was surfaced in the API Evangelist network as a Qiming Venture Partners portfolio lead. It publishes no public developer API, portal, or machine-readable surface; api.xiaomishu.com serves a closed (HTTP 403) backend, and the main site is HTTP-only with a mismatched HTTPS certificate.
image: http://www.xiaomishu.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Xiaomishu (订餐小秘书)
nav: Providers
network: true
overview: Xiaomishu (订餐小秘书) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Reservations, Dining, and Food.
random_paper: 17
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xiaomishu/refs/heads/main/screenshots/xiaomishu-2026-09-02T171125.png
security:
- kind: domain-security
  name: Xiaomishu Domain Security
  slug: xiaomishu-domain-security
  summary_line: DMARC
slug: xiaomishu
tags:
- Company
- Restaurant
- Reservations
- Dining
- Food
- Shanghai
- China
website: http://www.xiaomishu.com
---
