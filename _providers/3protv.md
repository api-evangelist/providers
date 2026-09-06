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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://3protv.com
- group: company
  title: ''
  type: About
  url: https://apps.3protv.com/company
- group: operate
  title: ''
  type: Support
  url: https://apps.3protv.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apps.3protv.com/policy/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apps.3protv.com/policy/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://apps.3protv.com/membership/intro
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@3protv
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3protv-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3protv-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/3protv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/3protv-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: 3ProTV is a Korean consumer financial-media subscription business whose only machine surface is the private backend for its own apps at api.3protv.com — it answers `{}` at the root and serves a /health document, but returns 404 on /openapi.json, /swagger.json, /api-docs, /graphql and every /.well-known/ path, and the company publishes no developer portal, reference, SDK, package or webhook catalog anywhere.
  evidence:
  - status: 404
    url: https://api.3protv.com/openapi.json
  - status: 404
    url: https://api.3protv.com/api-docs
  - status: 404
    url: https://api.3protv.com/graphql
  - status: 404
    url: https://apps.3protv.com/openapi.json
  - status: 404
    url: https://apps.3protv.com/.well-known/agent-card.json
  - status: 200
    url: https://api.3protv.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '3ProTV (삼프로TV), operated by E-Broadcasting Co. of Seoul, South Korea, is the country''s largest economic and financial media platform — a YouTube-native economics broadcaster founded in 2018 that has grown into a subscription content business spanning live market programming, original news and research (PDS) archives, premium lectures and seminars, paid membership clubs, and a publishing arm. Its content is distributed through the 3ProTV web application at apps.3protv.com and native iOS and Android apps backed by a private application API at api.3protv.com. 3ProTV is an end-user media and education product: as of this profile it publishes no public developer program, API reference, machine-readable contract, SDK or webhook surface.'
image: https://apps.3protv.com/assets/images/opengraph-800x400.png
layout: provider
modified: '2026-09-05'
name: 3ProTV
nav: Providers
network: true
overview: '3ProTV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Financial Media, Video, and Streaming.


  3ProTV''s developer surface includes support, pricing, YouTube channel, and 8 more developer resources.'
plans:
- name: 3Protv Plans Pricing
  plan_count: 0
  slug: 3protv-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: 3Protv Rate Limits
  slug: 3protv-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 3Protv Domain Security
  slug: 3protv-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 3protv
tags:
- Company
- Media
- Financial Media
- Video
- Streaming
- Subscription
- Education
- South Korea
- Content
website: https://3protv.com
---
