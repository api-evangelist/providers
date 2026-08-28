---
agent_readiness:
  band: human-only
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: REST API for the SAGARIS Agentic Revenue OS, including the Company Brain context endpoints. Bearer/workspace-key authentication. Formal reference, SDKs, and webhooks are marked 'Soon' (pre-launch).
  name: SAGARIS REST API
  slug: sagaris-rest-api
- description: Read-only MCP server over Streamable HTTP (stateless JSON mode), workspace-key bearer auth, exposing 5 GET-derived tools (list_contacts, list_sequences, brain_claims_current, brain_contact_dossier, br
  name: SAGARIS MCP Server
  slug: sagaris-mcp-server
artifact_total: 3
created: '2026-08-24'
description: Agentic Revenue OS / AI Sales Operator for B2B sales teams, offering CRM, dialer, email/SMS sequences, and a shared 'Company Brain' memory. Exposes a read-only MCP server, a documented REST API, and advertised OpenAPI and llms.txt contracts. Access is gated behind a paid workspace and the company is pre-launch.
layout: provider
mcp_servers:
- description: ''
  name: SAGARIS API MCP Server
  slug: sagaris-api-mcp-server
modified: '2026-08-24'
name: SAGARIS API
nav: Providers
network: true
overview: SAGARIS API publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include sales, crm, sales-engagement, dialer, and ai-agents.
random_paper: 13
score:
  band: minimal
  composite: 3.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 0.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
slug: sagaris-api
tags:
- sales
- crm
- sales-engagement
- dialer
- ai-agents
- mcp
- revenue
- conversation-intelligence
- sms
- email
- ai-receptionist
---
