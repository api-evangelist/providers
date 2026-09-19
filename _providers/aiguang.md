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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.guang.com/
- group: operate
  title: ''
  type: Support
  url: https://bbs.guang.com/d/32
- group: operate
  title: ''
  type: Community
  url: https://bbs.guang.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiguang/refs/heads/main/changelog/aiguang-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aiguang-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiguang/refs/heads/main/lifecycle/aiguang-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aiguang-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bbs.guang.com/d/875
- group: start
  title: ''
  type: Login
  url: https://www.guang.com/v4/guang/liveshopping/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bbs.guang.com/d/964
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bbs.guang.com/d/965
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiguang/refs/heads/main/plans/aiguang-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiguang-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiguang/refs/heads/main/llms/aiguang-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiguang-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiguang/refs/heads/main/security/aiguang-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiguang-domain-security.yml
coverage:
  checked: '2026-09-14'
  detail: Aiguang ships a consumer WeChat live-commerce app and an account-gated merchant/supplier console and publishes no developer program at all — its merchant forum bbs.guang.com is the only public technical surface, and both guang.com and www.guang.com answer HTTP 200 on every unknown path (an applinks catch-all and a single-page-app shell respectively), so the 200s on /openapi.json and /.well-known/agent-card.json are soft-404s, not documents.
  evidence:
  - status: 200
    url: https://www.guang.com/openapi.json
  - status: 200
    url: https://guang.com/.well-known/agent-card.json
  - status: 404
    url: https://api.guang.com/openapi.json
  - status: 404
    url: https://bbs.guang.com/.well-known/api-catalog
  - status: 200
    url: https://www.guang.com/
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: Aiguang (爱逛) is a Hangzhou, China live-streaming and short-video commerce platform built on the WeChat ecosystem. Consumers enter live rooms through the Aiguang WeChat mini-program and the Aiguang mobile app to take part in limited-time discounts, group buys and live-stream giveaways, while merchants and MCN hosts run their broadcasts from the Aiguang seller app and a PC live-broadcast console carrying interaction, marketing, promotion and analytics tooling. The platform is wired into the Youzan (有赞) CPS product pool so viewers can resell what they watch. Per its own user agreement and privacy statement (effective 2025-01-17) the platform is operated by 杭州杨杨得翼文化有限公司 (Hangzhou Yangyang Deyi Culture Co., Ltd.). Aiguang publishes no public developer program, API reference or machine-readable contract; its merchant, supplier and MCN surfaces are reached through account logins and a merchant community forum.
image: https://img.yzcdn.cn/guang/intro/20200410/logo@3x.png
layout: provider
modified: '2026-09-14'
name: Aiguang
nav: Providers
network: true
overview: 'Aiguang is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Live Commerce, Live Streaming, and Social Commerce.


  Aiguang''s developer surface includes support, changelog, pricing, and 9 more developer resources.'
plans:
- name: Aiguang Plans Pricing
  plan_count: 0
  slug: aiguang-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Aiguang Rate Limits
  slug: aiguang-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 17.7
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiguang Domain Security
  slug: aiguang-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: aiguang
tags:
- Company
- E-Commerce
- Live Commerce
- Live Streaming
- Social Commerce
- Retail
- Video
- WeChat
- China
- Marketplace
website: https://www.guang.com/
---
