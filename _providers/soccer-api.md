---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The advertised live football data API — REST plus a WebSocket stream — covering competitions, fixtures, live scores, match events, standings, teams, players, line-ups, statistics, head-to-head, odds, '
  name: Soccer API
  slug: soccer-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://soccer-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://soccer-api.com/api-documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://soccer-api.com/api-pricing/
- group: company
  title: ''
  type: Blog
  url: https://soccer-api.com/api-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://soccer-api.com/feed/
- group: operate
  title: ''
  type: Support
  url: mailto:info@soccer-api.com
- group: commercial
  title: ''
  type: Plans
  url: plans/soccer-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soccer-api-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soccer-api-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soccer-api-domain-security.yml
coverage:
  checked: '2026-08-27'
  detail: 'Soccer API markets a football data API but does not yet operate one: its documentation, pricing and coverage pages each carry a notice declaring their own contents placeholders "until the final production Soccer API specification is supplied", the published base URL is the literal https://api.example.com/v1, and api.soccer-api.com does not resolve.'
  evidence:
  - status: 200
    url: https://soccer-api.com/api-documentation/
  - status: 200
    url: https://soccer-api.com/api-pricing/
  - status: 404
    url: https://soccer-api.com/openapi.json
  - status: 404
    url: https://soccer-api.com/.well-known/api-catalog
  - status: 404
    url: https://soccer-api.com/apis.json
  reason: no-developer-program
  state: none
created: '2026-08-24'
description: 'Soccer API (soccer-api.com) is a Spain-contacted vendor marketing live football data — fixtures, live scores, match events, standings, teams, players, line-ups, statistics, head-to-head, odds, predictions, historical seasons and a real-time WebSocket feed — to developers building sports, fantasy, media and betting applications. The site went live in August 2026 and publishes documentation, coverage and pricing pages plus a small tutorial blog. Re-probed on 2026-08-27, the product is announced but not shipped: every one of those three pages carries the vendor''s own notice declaring its contents placeholders pending a production specification, the documented base URL is the literal example host https://api.example.com/v1, the coverage matrix names no real competition, all paid prices read "$XX", and there is no sign-up, console, key issuance or machine-readable contract of any kind. Access is requested by WhatsApp or email.'
image: https://soccer-api.com/wp-content/uploads/2026/08/cropped-ChatGPT-Image-Aug-6-2026-02_59_14-PM-192x192.png
layout: provider
modified: '2026-08-27'
name: Soccer API
nav: Providers
network: true
overview: 'Soccer API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Soccer, Live Scores, Odds, and Predictions.


  Soccer API''s developer surface includes documentation, pricing, engineering blog, support, and 6 more developer resources.'
plans:
- name: Soccer Api Plans Pricing
  plan_count: 0
  slug: soccer-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Soccer Api Rate Limits
  slug: soccer-api-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
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
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soccer-api/refs/heads/main/screenshots/soccer-api-2026-09-02T160030.png
security:
- kind: domain-security
  name: Soccer Api Domain Security
  slug: soccer-api-domain-security
  summary_line: TLSv1.2 · DMARC
slug: soccer-api
tags:
- Soccer
- Live Scores
- Odds
- Predictions
website: https://soccer-api.com/
---
