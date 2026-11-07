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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-11-06'
api_count: 1
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
- baseURL: https://atlas.hellosafe.com/api/v1/travel
  baseurl_source: declared
  description: Coverage gaps and ranked sell arguments from a traveller profile and a bank card.
  name: HelloSafe Coach API
  slug: hellosafe-coach-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/hellosafe/capabilities/hellosafe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hellosafe-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/hellosafe/well-known/hellosafe-provider-apis.json
  title: ''
  type: APIsJSON
  url: well-known/hellosafe-provider-apis.json
- group: start
  href: https://artifacts.apis.io/hellosafe/well-known/hellosafe-api-onboarding.json
  title: ''
  type: Onboarding
  url: well-known/hellosafe-api-onboarding.json
- group: agent
  href: https://artifacts.apis.io/hellosafe/llms/hellosafe-llms.txt
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
mcp_servers:
- description: Remote MCP server at hellosafe.com over HTTP.
  name: HelloSafe MCP Server
  slug: hellosafe
modified: '2026-08-25'
name: HelloSafe
nav: Providers
network: true
overview: 'HelloSafe publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversion API, Links API, Quotes API, and 1 more. Tagged areas include Travel Insurance, Insurance Distribution, Pricing, and Travel.


  The HelloSafe catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: HelloSafe API Rules
  rule_count: 68
  severity_counts:
    error: 66
    hint: 0
    info: 1
    warn: 1
  slug: hellosafe-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 56.7
    developer_ergonomics: 26.2
    discoverability: 63.3
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 44.4
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hellosafe/hellosafe-2026-09-02T145720.png
slug: hellosafe
tags:
- Travel Insurance
- Insurance Distribution
- Pricing
- Travel
website: https://hellosafe.com
---
