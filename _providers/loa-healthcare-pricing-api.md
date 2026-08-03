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
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Versioned REST API for searching hospital/provider entities, retrieving source-labeled price rows, comparing prices by CPT code, and submitting reviewed corrections. Public reads require no key; optio
  name: Loa Healthcare Pricing REST API
  slug: loa-healthcare-pricing-rest-api
- description: Hosted/remote MCP server 'LOA Healthcare Pricing' v1.0.0 over Streamable HTTP with 12 tools for CPT search, procedure suggestions, provider/hospital search, pricing estimates, market pricing, entity p
  name: Loa Healthcare Pricing MCP Server
  slug: loa-healthcare-pricing-mcp-server
artifact_total: 2
created: '2026-07-28'
description: Source-labeled U.S. healthcare price transparency API and MCP server. Provides hospital and provider entity search, source-labeled price rows, cross-entity price comparison by CPT/HCPCS, and a reviewed update-submission workflow. Data comes from 6,000+ hospital Machine Readable Files under the federal Hospital Price Transparency Rule plus CMS NPI Registry and Loa-reviewed provider submissions.
layout: provider
modified: '2026-08-02'
name: Loa Healthcare Pricing API
nav: Providers
network: true
overview: 'Loa Healthcare Pricing API publishes 1 API on the [APIs.io](https://apis.io/) network: Loa Healthcare Pricing REST API. Tagged areas include healthcare, price transparency, medical pricing, hospitals, and providers.'
random_paper: 84
score:
  band: emerging
  composite: 16.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.5
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.9
  scored_at: '2026-08-03'
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
