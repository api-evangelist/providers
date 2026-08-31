---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API (OpenAPI 3.1) exposing POST /v2/extract (x402 V2 paid), legacy POST /extract, GET /health, and GET /metrics. Converts text/HTML into schema-valid JSON. Includes llms.txt integration guide and
  name: SchemaSure Structured Extraction API
  slug: schemasure-structured-extraction-api
artifact_total: 1
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/schemasure-a2a.yml
created: '2026-07-19'
description: Structured data extraction API that converts unstructured text or HTML into JSON guaranteed to validate against a caller-supplied JSON Schema, or returns a typed error at no charge. Access is gated by x402 pay-per-call micropayments (USDC on Base), with no accounts or API keys.
layout: provider
modified: '2026-07-19'
name: SchemaSure
nav: Providers
network: true
overview: 'SchemaSure publishes 1 API on the [APIs.io](https://apis.io/) network: Structured Extraction API. Tagged areas include structured-data-extraction, text-to-JSON, JSON-Schema, document-parsing, and data-cleaning.'
random_paper: 1
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 1
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 15.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: schemasure
tags:
- structured-data-extraction
- text-to-JSON
- JSON-Schema
- document-parsing
- data-cleaning
- LLM-tooling
- AI-agents
- x402-micropayments
- agent-native
- A2A
- MCP
---
