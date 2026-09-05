---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Server-to-server conversion postback.
  name: HelloSafe Conversion API
  slug: hellosafe-conversion-api
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Turn a chosen offer into a tracked, attributed subscription link.
  name: HelloSafe Links API
  slug: hellosafe-links-api
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Price a trip and read the catalogue vocabulary.
  name: HelloSafe Quotes API
  slug: hellosafe-quotes-api
artifact_total: 3
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hellosafe-capability-edges.yml
- group: other
  title: ''
  type: APIsJSON
  url: well-known/hellosafe-provider-apis.json
- group: start
  title: ''
  type: Onboarding
  url: well-known/hellosafe-api-onboarding.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hellosafe-llms.txt
- group: company
  title: ''
  type: Website
  url: https://hellosafe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atlas.hellosafe.com/platform/api
created: '2026-08-25'
description: HelloSafe distributes travel insurance through APIs, under the Atlas platform at atlas.hellosafe.com. The Travel Insurance API returns multi-insurer pricing, tracked attributed links and a pre-sale coverage assessment, aimed at travel agencies, tour operators, OTAs, booking engines and travel apps. A second surface, the Coach API, sits alongside it. The contract is an OpenAPI 3.1 document of 4 operations and 8 schemas, and requests are HMAC-SIGNED rather than bearing a plain API key — three headers, AtlasKeyId, AtlasTimestamp and AtlasSignature, which is materially stronger than what most providers this size ship.
layout: provider
modified: '2026-08-25'
name: HelloSafe
nav: Providers
network: true
overview: 'HelloSafe publishes 3 APIs on the [APIs.io](https://apis.io/) network: Conversion API, Links API, and Quotes API. Tagged areas include Travel Insurance, Insurance Distribution, Pricing, and Travel.'
random_paper: 2
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 58.3
    developer_ergonomics: 26.2
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hellosafe/refs/heads/main/screenshots/hellosafe-2026-09-02T145720.png
slug: hellosafe
tags:
- Travel Insurance
- Insurance Distribution
- Pricing
- Travel
website: https://hellosafe.com
---
