---
api_count: 1
apis:
- description: 'Documented cricket endpoints (fixtures, live scores, ball-by-ball, statistics, odds, predictions, WebSocket) behind a sales-gated, undisclosed base URL. No machine-readable contract is published, and '
  name: Cricket API
  slug: cricket-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://cricket-api.net
- group: commercial
  title: ''
  type: Pricing
  url: https://cricket-api.net/api-pricing/
- group: company
  title: ''
  type: Blog
  url: https://cricket-api.net/api-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://cricket-api.net/feed/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cricket-api-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cricket-api-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/cricket-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cricket-api-rate-limits.yml
coverage:
  checked: '2026-09-04'
  detail: The public developer documentation is fully readable but describes every endpoint against the placeholder host api.example.com and prints its own implementation notice telling the reader to replace the base URL, paths, auth header, field names and quotas with the confirmed production specification, so there is nothing machine-readable and nothing callable to capture.
  evidence:
  - status: 200
    url: https://cricket-api.net/api-documentation/
  - status: 404
    url: https://cricket-api.net/openapi.json
  - status: 404
    url: https://cricket-api.net/.well-known/agent-card.json
  - status: 404
    url: https://cricket-api.net/this-does-not-exist-xyz
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-03'
description: 'A cricket data API advertised at cricket-api.net -- live scores, fixtures, ball-by-ball events, player and team statistics, betting odds and win-probability predictions, over REST and a documented WebSocket stream. ACCESS REALITY, stated plainly: the production base URL is not published; the docs describe every endpoint against the placeholder api.example.com and carry their own implementation notice that the base URL, paths, headers, quotas and responses are documentation examples to be replaced after signup. Four plan tiers are named but no price or quota is published for any of them. Listed on the surfaces that are actually served; the rating reflects what is published.'
image: https://cricket-api.net/wp-content/uploads/2026/08/cropped-cricket_-api-removebg-preview-1-192x192.png
layout: provider
modified: '2026-09-04'
name: Cricket API
nav: Providers
network: true
overview: 'Cricket API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cricket, Sports, Sports Data, Live Scores, and Cricket Statistics.


  Cricket API''s developer surface includes pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Cricket Api Plans Pricing
  plan_count: 1
  slug: cricket-api-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Cricket Api Rate Limits
  slug: cricket-api-rate-limits
security:
- kind: domain-security
  name: Cricket Api Domain Security
  slug: cricket-api-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cricket-api
tags:
- Cricket
- Sports
- Sports Data
- Live Scores
- Cricket Statistics
- Cricket Odds
- Cricket Predictions
website: https://cricket-api.net
---
