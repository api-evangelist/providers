---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Swytchcode''s publicly consumable surfaces: developer documentation and a published llms.txt. The primary interface is an npm-installable CLI plus a local MCP server (localhost-only, not a hosted endpo'
  name: Swytchcode Documentation & Agent Surfaces
  slug: swytchcode-documentation-agent-surfaces
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swytchcode-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.swytchcode.com/feed/
- group: build
  title: ''
  type: Packages
  url: packages/swytchcode-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/swytchcode-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swytchcode-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swytchcode-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swytchcode-llms-full.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/swytchcode-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swytchcode-lifecycle.yml
created: '2026-07-02'
description: Deterministic API-execution layer for AI agents and developers that sits between an agent and production APIs, handling auth, retries, idempotency, and policy control across 2,000+ APIs. Consumable via a public npm-installable CLI and a local MCP server, with a published llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swytchcode.png
layout: provider
mcp_servers:
- description: Local MCP server shipped inside the Swytchcode CLI (npm package `swytchcode`). Runs on the developer's machine, not a hosted/remote endpoint.
  name: Swytchcode MCP Server
  slug: swytchcode-mcp-server
modified: '2026-06-20'
name: Swytchcode
nav: Providers
network: true
overview: 'Swytchcode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI / Agent Tooling, agentic middleware, API Integration, API Orchestration, and API execution layer.


  Swytchcode''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Swytchcode Domain Security
  slug: swytchcode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swytchcode
tags:
- AI / Agent Tooling
- agentic middleware
- API Integration
- API Orchestration
- API execution layer
- LLM tool execution
- MCP Server
- Developer Tools
- API Documentation
- API playground
---
