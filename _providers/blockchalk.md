---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Location-pinned neighborhood messages.
  name: BlockChalk chalks API
  slug: blockchalk-chalks-api
artifact_total: 3
common:
- group: docs
  title: ''
  type: Documentation
  url: http://web.archive.org/web/20090810213933/http://blockchalk.com/developers
- group: docs
  title: ''
  type: APIReference
  url: http://web.archive.org/web/20090810213933/http://blockchalk.com/developers
- group: build
  title: ''
  type: Packages
  url: packages/blockchalk-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blockchalk-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockchalk-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blockchalk-llms.txt
created: '2026-07-17'
description: 'BlockChalk was a location-based neighborhood messaging service founded in 2009 by Stephen Hood, the former product lead for Delicious, and Dave Baggeroer of the Stanford Institute of Design. Users with GPS-enabled smartphones left short public messages called "chalks" pinned to a specific geographic point, and read the chalks other people had left on their block, so neighbors could ask, answer, praise, gripe, report potholes and lost pets, announce garage sales and organize locally. The company raised $1M in seed financing in May 2010 from Joshua Schachter, Battery Ventures, Founder Collective, Harrison Metal, Mitch Kapor, Josh Stylman, Tom McInerney and David Liu. BlockChalk published a small read-only public API on its developer page, offering XML, JSON and RSS interfaces that returned nearby chalks for a supplied latitude and longitude, later joined by a versioned GeoRSS endpoint. The product and the company are retired: blockchalk.com holds an active domain registration
  but its delegated nameservers no longer resolve, and no BlockChalk host answers on the public internet. This profile preserves the historical API surface as documentation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockchalk.png
layout: provider
modified: '2026-07-20'
name: BlockChalk
nav: Providers
network: true
overview: 'BlockChalk publishes 1 API on the [APIs.io](https://apis.io/) network: chalks API. Tagged areas include Company, Location, Geolocation, Social, and Messaging.


  BlockChalk''s developer surface includes documentation, API reference, and 4 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 15.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 14.0
    developer_ergonomics: 15.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 15.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockchalk/refs/heads/main/screenshots/blockchalk-2026-07-25T203346.png
security:
- kind: authentication
  name: Blockchalk Authentication
  slug: blockchalk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Blockchalk Domain Security
  slug: blockchalk-domain-security
  summary_line: HSTS
slug: blockchalk
tags:
- Company
- Location
- Geolocation
- Social
- Messaging
- Local
- Neighborhood
- Mobile
- Retired
---
