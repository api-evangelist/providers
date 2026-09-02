---
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Current and archived source-linked city observations
  name: SouthendOnSea.city Southend Now API
  slug: southendonsea-southend-now-api
artifact_total: 2
common:
- group: other
  title: ''
  type: APIsJSON
  url: https://southendonsea.city/.well-known/apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/southendonsea-llms.txt
- group: company
  title: ''
  type: Website
  url: https://southendonsea.city
- group: docs
  title: ''
  type: Documentation
  url: https://southendonsea.city/data/reuse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://southendonsea.city/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://southendonsea.city/privacy
created: '2026-08-23'
description: 'SouthendOnSea.city is an independent local information and community-participation platform for Southend-on-Sea, Essex, covering local news, community propositions and public voting, city information and the Southend Science Exhibition. Its public data API — Southend Now — serves unauthenticated, source-linked current and historical observations for the area: weather, designated bathing waters, marine conditions, modelled air quality and flood alerts. Three operations return the current snapshot, a JSON history and a CSV history, refreshed on a 1,800-second interval, with source licensing and attribution preserved in the payload. The platform is independent and unofficial and states plainly that it is not operated by Southend-on-Sea City Council, Essex Police or any election authority.'
examples:
- key_count: 9
  name: Southendonsea Now Example
  slug: southendonsea-now-example
layout: provider
modified: '2026-08-23'
name: SouthendOnSea.city
nav: Providers
network: true
overview: 'SouthendOnSea.city publishes 1 API on the [APIs.io](https://apis.io/) network: Southend Now API. Tagged areas include Open Data, Southend-on-Sea, Weather, Environment, and local data.


  SouthendOnSea.city''s developer surface includes documentation and 5 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: southendonsea
tags:
- Open Data
- Southend-on-Sea
- Weather
- Environment
- local data
website: https://southendonsea.city
---
