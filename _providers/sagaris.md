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
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: REST API for the SAGARIS Agentic Revenue OS, including the Company Brain context endpoints. Bearer/workspace-key authentication. Formal reference, SDKs, and webhooks are marked 'Soon' (pre-launch).
  name: SAGARIS REST API
  slug: sagaris-rest-api
- description: Read-only MCP server over Streamable HTTP (stateless JSON mode), workspace-key bearer auth, exposing 5 GET-derived tools (list_contacts, list_sequences, brain_claims_current, brain_contact_dossier, br
  name: SAGARIS MCP Server
  slug: sagaris-mcp-server
artifact_total: 4
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sagaris-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.sagaris.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sagaris.ai/docs
- group: agent
  title: ''
  type: MCPServer
  url: https://www.sagaris.ai/mcp
created: '2026-08-24'
description: SAGARIS is an agentic revenue operating system for B2B sales teams — CRM, dialer, inbox, SMS, social, an AI receptionist and an AI coach in one system, where AI agents act on the pipeline under approval gates and an audit trail rather than only reporting on it. Pricing is public at 499 USD per founding seat per month, with a custom Enterprise plan. SAGARIS describes a Model Context Protocol endpoint that lets an AI client read the CRM, sequences and workspace with a workspace API key, read-only and scoped to the workspace.
layout: provider
mcp_servers:
- description: ''
  name: SAGARIS MCP Server
  slug: sagaris-mcp-server
- description: ''
  name: SAGARIS MCP Server
  slug: sagaris-mcp-server-2
modified: '2026-08-24'
name: SAGARIS
nav: Providers
network: true
overview: 'SAGARIS publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Sales, Revenue Operations, MCP, and AI Agents.


  SAGARIS''s developer surface includes documentation and 3 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sagaris/refs/heads/main/screenshots/sagaris-2026-09-02T154255.png
slug: sagaris
tags:
- CRM
- Sales
- Revenue Operations
- MCP
- AI Agents
website: https://www.sagaris.ai/
---
