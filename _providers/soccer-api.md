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
