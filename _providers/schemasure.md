---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
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
random_paper: 27
score:
  band: emerging
  composite: 14.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.0
  schema_version: 0.9
  scored_at: '2026-08-03'
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
