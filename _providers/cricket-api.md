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
  scored_at: '2026-09-04'
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
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.6
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
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
