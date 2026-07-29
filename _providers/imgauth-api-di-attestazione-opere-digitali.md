---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Attestation/proof-of-existence REST API. Client-side SHA-256 hashing, signed PDF certificates, RFC 3161 timestamps, OpenTimestamps/Bitcoin anchoring, verifiable certificate pages, and status telemetry
  name: imgauth REST API
  slug: imgauth-rest-api
- description: 'Hosted, zero-install MCP server (Streamable HTTP) exposing the attestation service to MCP-capable agents. Tools: attest_file, verify_file, verify_certificate, get_certificate_pdf, check_anchor, servic'
  name: imgauth Remote MCP Server
  slug: imgauth-remote-mcp-server
artifact_total: 2
created: '2026-07-19'
description: Digital-work attestation and proof-of-existence service by Spazio Genesi ETS. Clients compute a SHA-256 fingerprint locally (file bytes never leave the device) and receive a signed PDF certificate, an RFC 3161 timestamp, and an OpenTimestamps/Bitcoin anchor. Exposes a public REST API (OpenAPI 3.0.3) and a hosted remote MCP server for agents.
layout: provider
modified: '2026-07-19'
name: imgauth — API di attestazione opere digitali
nav: Providers
network: true
overview: 'imgauth — API di attestazione opere digitali publishes 1 API on the [APIs.io](https://apis.io/) network: imgauth REST API. Tagged areas include digital notarization, timestamping, proof-of-existence, content authenticity, and provenance.'
random_paper: 22
score:
  band: emerging
  composite: 14.0
  delta: -3.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
slug: imgauth-api-di-attestazione-opere-digitali
tags:
- digital notarization
- timestamping
- proof-of-existence
- content authenticity
- provenance
- copyright
- IP protection
- blockchain
- Bitcoin
- OpenTimestamps
- security
- document
- e-signature
- MCP
---
