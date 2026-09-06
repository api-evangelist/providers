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
- group: company
  title: ''
  type: Website
  url: https://www.lemonbox.com/
- group: company
  title: ''
  type: Website
  url: https://www.lemonbox.com.cn/
- group: company
  title: ''
  type: About
  url: https://www.lemonbox.com/en/about
- group: company
  title: ''
  type: Blog
  url: https://www.lemonbox.com/zh/insights
- group: company
  title: ''
  type: BlogRSS
  url: https://www.lemonbox.com/feed.xml
- group: operate
  title: ''
  type: FAQ
  url: https://www.lemonbox.com/zh/faq
- group: other
  title: ''
  type: Products
  url: https://www.lemonbox.com/zh/products
- group: company
  title: ''
  type: Press
  url: https://www.lemonbox.com/zh/media
- group: other
  title: ''
  type: Sitemap
  url: https://www.lemonbox.com/sitemap.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lemonbox-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemonbox-domain-security.yml
created: '2026-07-17'
description: LemonBox (来檬) is a health-technology brand working in AI-generative personalized nutrition. Founded in 2016 in Silicon Valley, incubated at the University of Chicago Polsky Center in 2017, and accepted into Y Combinator in 2018, it entered the Chinese market that year and is now headquartered in Shanghai. LemonBox builds individualized daily vitamin and supplement packs from a three-minute FFQ (food frequency questionnaire) nutrition assessment scored by its LemonAlgo adaptive engine, then fulfills them one pack at a time (MOQ=1) through its Personalization Fulfillment Center in Hong Kong. The company reports serving more than 10 million cumulative users as of 2026 and sells both direct-to-consumer and B2B. Investors include Y Combinator and Partech. LemonBox operates a consumer web and WeChat mini-program experience and publishes no public developer API, SDK, or developer portal; its agent-facing surface is limited to a published /llms.txt and a robots.txt that explicitly allow-lists
  generative-AI crawlers.
image: https://www.lemonbox.com/images/lemon.png
layout: provider
modified: '2026-07-19'
name: LemonBox
nav: Providers
network: true
overview: 'LemonBox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Health, Nutrition, and Supplements.


  LemonBox''s developer surface includes engineering blog, FAQ, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 4.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonbox/refs/heads/main/screenshots/lemonbox-2026-07-25T224911.png
security:
- kind: domain-security
  name: Lemonbox Domain Security
  slug: lemonbox-domain-security
  summary_line: TLSv1.2
slug: lemonbox
tags:
- Company
- Consumer
- Health
- Nutrition
- Supplements
- Personalization
- Artificial Intelligence
- Direct to Consumer
- E-Commerce
- China
website: https://www.lemonbox.com/
---
