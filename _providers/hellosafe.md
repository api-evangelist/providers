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
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Multi-insurer travel-insurance pricing, tracked attributed links and a pre-sale coverage assessment. 4 operations, 8 schemas, HMAC-signed requests.
  name: HelloSafe Travel Insurance API
  slug: hellosafe-travel-insurance-api
- description: Second Atlas surface, declared by the provider alongside the travel API and sharing the same OpenAPI document.
  name: HelloSafe Coach API
  slug: hellosafe-coach-api
artifact_total: 2
common:
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
overview: 'HelloSafe publishes 2 APIs on the [APIs.io](https://apis.io/) network: Travel Insurance API and Coach API. Tagged areas include Insurance, Travel, Insurtech, Pricing, and Affiliate.'
random_paper: 2
score:
  band: thin
  composite: 32.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 59.9
    developer_ergonomics: 26.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
slug: hellosafe
tags:
- Insurance
- Travel
- Insurtech
- Pricing
- Affiliate
- Distribution
website: https://hellosafe.com
---
