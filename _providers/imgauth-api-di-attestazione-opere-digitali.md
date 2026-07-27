---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-27'
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
random_paper: 32
score:
  band: emerging
  composite: 17.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
