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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mobcrush
- group: build
  title: ''
  type: Packages
  url: packages/mobcrush-packages.yml
coverage:
  checked: '2026-08-25'
  detail: Mobcrush was acquired by Super League Gaming on 2 June 2021 and the brand retired; its domain mobcrush.com is still registered and still delegated to four Route 53 name servers, but the hosted zone behind them was deleted, so every public resolver returns SERVFAIL for mobcrush.com and every subdomain and no HTTP request to any Mobcrush host can even open a connection — and Wayback shows the company never published a developer portal, reference or spec while it was alive, only an internal /api/ used by its own site and apps.
  evidence:
  - status: 0
    url: https://mobcrush.com/
  - status: 0
    url: https://api.mobcrush.com/openapi.json
  - status: 0
    url: https://mobcrush.com/.well-known/agent-card.json
  - status: 0
    url: https://mobcrush.com/.well-known/agent.json
  - status: 0
    url: https://mobcrush.com/llms.txt
  - status: 404
    url: https://www.mobcrush.com/api/
  - status: 404
    url: https://www.superleague.com/mobcrush
  - status: 200
    url: https://api.github.com/orgs/Mobcrush
  - status: 200
    url: https://www.superleague.com/
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Mobcrush Streaming, Inc. was a Santa Monica, California live-streaming technology company, founded in 2013 by Royce Disini with James Hurley, Travis Rogers and Stephen Dao, that made it possible for mobile gamers to broadcast gameplay straight from an iOS or Android device with no capture card, no desktop encoder and no third-party software. Its differentiator was simulcast: a creator went live once and Mobcrush relayed the same broadcast simultaneously to Twitch, YouTube, Facebook, Twitter and Periscope at no extra charge, which turned the product from a competing destination into distribution infrastructure for creators who already had audiences elsewhere. The company added an advertising and sponsorship layer in 2018 ("Go Live, Get Paid") and operated Mineville, one of six official Minecraft server partners under agreement with Microsoft, reaching more than twenty million players a year. It raised roughly $35.9M across its rounds, including an $11M Series A in September
  2015 led by Kleiner Perkins Caufield & Byers and a $20M round in 2016, with First Round Capital and Lowercase Capital also participating. Super League Gaming announced its acquisition of Mobcrush on 11 March 2021 and closed it on 2 June 2021 for approximately 12.6 million shares of common stock; the acquirer now trades as Super League Enterprise, Inc. and does not carry the Mobcrush brand forward as a product. Mobcrush ran a JSON web API at www.mobcrush.com/api/ that backed its own site and mobile apps, but it never published a developer portal, an API reference, a first-party SDK or any machine-readable specification, so there is no public API surface to catalog — and the mobcrush.com domain, while still registered, no longer resolves at all. This profile is retained as a historical record.'
image: https://avatars.githubusercontent.com/u/14281215?v=4
layout: provider
modified: '2026-08-25'
name: Mobcrush
nav: Providers
network: true
overview: Mobcrush is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, Gaming, and Live Streaming.
random_paper: 6
score:
  band: minimal
  composite: 5.3
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
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
slug: mobcrush
tags:
- Company
- Defunct
- Acquired
- Gaming
- Live Streaming
- Video
- Mobile
- Creator Economy
- Media
- Advertising
---
