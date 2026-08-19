---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energy Charts Api Agentic Access
  operation_count: 17
  slug: energy-charts-api-agentic-access
  summary_line: 17 operations
api_count: 4
apis:
- description: Import/export values
  name: Energy Charts API import_export API
  slug: energy-charts-api-import-export-api
- description: Query power values
  name: Energy Charts API power API
  slug: energy-charts-api-power-api
- description: Query price values
  name: Energy Charts API prices API
  slug: energy-charts-api-prices-api
- description: Renewable shares
  name: Energy Charts API ren_share API
  slug: energy-charts-api-ren-share-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Energy-Charts import_export API
  slug: open-energy-charts-api-import-export-api
- collection_type: open
  name: Energy-Charts import_export power API
  slug: open-energy-charts-api-power-api
- collection_type: open
  name: Energy-Charts import_export prices API
  slug: open-energy-charts-api-prices-api
- collection_type: open
  name: Energy-Charts import_export ren_share API
  slug: open-energy-charts-api-ren-share-api
- collection_type: open
  name: Energy-Charts API
  slug: open-energy-charts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-charts-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-charts-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.energy-charts.info/
- group: other
  title: ''
  type: Provider
  url: https://www.ise.fraunhofer.de/
created: '2025-05-02'
description: The Energy-Charts API, provided by Fraunhofer ISE, delivers European energy data including electricity production by source, day-ahead spot market prices, cross-border electricity trading and physical flows, grid frequency, installed capacity, and renewable energy share forecasts. It covers more than 40 European countries and bidding zones, supports ISO 8601, daily, and UNIX timestamp formats, and is largely licensed under CC BY 4.0.
finops:
- name: Energy Charts Api Finops
  service_category: API
  slug: energy-charts-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-charts-api.png
layout: provider
modified: '2026-05-19'
name: Energy Charts API
nav: Providers
network: true
overview: Energy Charts API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including import_export API, power API, prices API, and 1 more. Tagged areas include Energy, Electricity, Renewables, Grid, and Europe.
plans:
- name: Energy Charts Api Plans Pricing
  plan_count: 3
  slug: energy-charts-api-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Energy Charts Api Rate Limits
  slug: energy-charts-api-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: -2.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.3
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-charts-api/refs/heads/main/screenshots/energy-charts-api-2026-06-20T180710.png
security:
- kind: domain-security
  name: Energy Charts Api Domain Security
  slug: energy-charts-api-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: energy-charts-api
tags:
- Energy
- Electricity
- Renewables
- Grid
- Europe
- Power
- Pricing
- Forecasts
website: https://www.energy-charts.info/
---
