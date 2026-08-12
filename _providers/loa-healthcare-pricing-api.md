---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-11'
api_count: 5
apis:
- description: Hosted/remote MCP server 'LOA Healthcare Pricing' v1.0.0 over Streamable HTTP with 12 tools for CPT search, procedure suggestions, provider/hospital search, pricing estimates, market pricing, entity p
  name: Loa Healthcare Pricing MCP Server
  slug: loa-healthcare-pricing-mcp-server
- description: The Entities API from Loa Healthcare Pricing API — 3 operation(s) for entities.
  name: Loa Healthcare Pricing API Entities API
  slug: loa-healthcare-pricing-api-entities-api
- description: The Entity Analytics API from Loa Healthcare Pricing API — 1 operation(s) for entity analytics.
  name: Loa Healthcare Pricing API Entity Analytics API
  slug: loa-healthcare-pricing-api-entity-analytics-api
- description: The Entity Updates API from Loa Healthcare Pricing API — 1 operation(s) for entity updates.
  name: Loa Healthcare Pricing API Entity Updates API
  slug: loa-healthcare-pricing-api-entity-updates-api
- description: The Prices API from Loa Healthcare Pricing API — 1 operation(s) for prices.
  name: Loa Healthcare Pricing API Prices API
  slug: loa-healthcare-pricing-api-prices-api
artifact_total: 6
created: '2026-07-28'
description: Source-labeled U.S. healthcare price transparency API and MCP server. Provides hospital and provider entity search, source-labeled price rows, cross-entity price comparison by CPT/HCPCS, and a reviewed update-submission workflow. Data comes from 6,000+ hospital Machine Readable Files under the federal Hospital Price Transparency Rule plus CMS NPI Registry and Loa-reviewed provider submissions.
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-02'
name: Loa Healthcare Pricing API
nav: Providers
network: true
overview: Loa Healthcare Pricing API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Entity Analytics API, Entity Updates API, and 1 more. Tagged areas include healthcare, price transparency, medical pricing, hospitals, and providers.
random_paper: 2
score:
  band: emerging
  composite: 17.5
  delta: 0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 56.2
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.1
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loa-healthcare-pricing-api/refs/heads/main/screenshots/loa-healthcare-pricing-api-2026-08-07T171743.png
slug: loa-healthcare-pricing-api
tags:
- healthcare
- price transparency
- medical pricing
- hospitals
- providers
- provider directory
- hospital prices
- CPT
- HCPCS
- MCP
- agent-native
- OpenAPI
- llms.txt
---
