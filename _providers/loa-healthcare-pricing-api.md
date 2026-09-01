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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Loa Healthcare Pricing Entities API
  slug: open-loa-healthcare-pricing-api-entities-api
- collection_type: open
  name: Loa Healthcare Pricing Entity Analytics API
  slug: open-loa-healthcare-pricing-api-entity-analytics-api
- collection_type: open
  name: Loa Healthcare Pricing Entity Updates API
  slug: open-loa-healthcare-pricing-api-entity-updates-api
- collection_type: open
  name: Loa Healthcare Pricing Prices API
  slug: open-loa-healthcare-pricing-api-prices-api
created: '2026-07-28'
description: Source-labeled U.S. healthcare price transparency API and MCP server. Provides hospital and provider entity search, source-labeled price rows, cross-entity price comparison by CPT/HCPCS, and a reviewed update-submission workflow. Data comes from 6,000+ hospital Machine Readable Files under the federal Hospital Price Transparency Rule plus CMS NPI Registry and Loa-reviewed provider submissions.
layout: provider
mcp_servers:
- description: ''
  name: Loa Healthcare Pricing API MCP Server
  slug: loa-healthcare-pricing-api-mcp-server
modified: '2026-08-02'
name: Loa Healthcare Pricing API
nav: Providers
network: true
overview: Loa Healthcare Pricing API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Entity Analytics API, Entity Updates API, and 1 more. Tagged areas include Healthcare, Price Transparency, medical pricing, Hospitals, and Providers.
random_paper: 13
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.1
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loa-healthcare-pricing-api/refs/heads/main/screenshots/loa-healthcare-pricing-api-2026-08-07T171743.png
slug: loa-healthcare-pricing-api
tags:
- Healthcare
- Price Transparency
- medical pricing
- Hospitals
- Providers
- Provider Directory
- hospital prices
- CPT
- HCPCS
- MCP
- agent-native
- OpenAPI
- llms-txt
---
