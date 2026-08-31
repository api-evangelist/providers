---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Avora Agent Forge Agentic Access
  operation_count: 8
  slug: avora-agent-forge-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 2
apis:
- description: Hosted streamable-HTTP MCP server exposing eleven tools across scanning, offers, Solana Pay ordering, settlement verification, and aggregate commerce telemetry. tools/list responds 200 anonymously wit
  name: AVORA Agent Forge MCP Server
  slug: avora-agent-forge-mcp-server
- description: The Agent API from AVORA Agent Forge — 5 operation(s) for agent.
  name: AVORA Agent Forge Agent API
  slug: avora-agent-forge-agent-api
- description: Public-data token evidence with mandatory human-review controls.
  name: AVORA Agent Forge Public Evidence API
  slug: avora-agent-forge-public-evidence-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AVORA Forge Commerce Agent API
  slug: open-avora-agent-forge-agent-api
- collection_type: open
  name: AVORA Public AI Interoperability Public Evidence API
  slug: open-avora-agent-forge-public-evidence-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avora-agent-forge.netlify.app/agent-forge/
- group: docs
  title: ''
  type: Documentation
  url: https://avora-agent-forge.netlify.app/agent-forge/
- group: docs
  title: ''
  type: APIReference
  url: https://avora-agent-forge.netlify.app/agent-forge/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://avora-agent-forge.netlify.app/ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://avora-agent-forge.netlify.app/agent-forge/pricing.json
- group: commercial
  title: ''
  type: Plans
  url: plans/avora-agent-forge-plans.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/avora-agent-forge-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/avora-agent-forge-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/avora-agent-forge-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/avora-agent-forge-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avora-agent-forge-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avora-agent-forge-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/avora-agent-forge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avora-agent-forge-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/avora-agent-forge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avora-agent-forge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avora-agent-forge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avora-agent-forge-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/avora-agent-forge-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avora-agent-forge-domain-security.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/avora-agent-forge-catalog.jsonld
- group: other
  title: ''
  type: Overlay
  url: overlays/avora-agent-forge-commerce-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/avora-agent-forge-public-sector-overlay.yaml
created: '2026-07-30'
description: 'AVORA Agent Forge is an evidence-first Solana SPL token risk scanner and public AI interoperability service built for humans, wallets, and autonomous agents. It publishes two OpenAPI 3.1 REST APIs, a hosted streamable-HTTP MCP server whose tools/list responds anonymously with eleven fully-schemad tools, and an A2A agent card with three published skills. Every operation is unauthenticated: there are no accounts, no API keys, and no OAuth. Paid tiers are gated instead by non-custodial, user-signed Solana Pay (USDC) settlement verified on-chain, where the payment reference doubles as the idempotency key. Public-sector assessments return Ed25519 JWS receipts that any third party can verify offline against a published JWKS, and the service ships a voluntary NIST AI RMF alignment profile that explicitly disclaims certification and government approval and requires human review.'
image: https://avora-agent-forge.netlify.app/AVORA.png
jsonld:
- class_count: 0
  name: Avora Agent Forge Catalog Context
  property_count: 0
  slug: avora-agent-forge-catalog
layout: provider
mcp_servers:
- description: Solana token scans, signed assessments, user-approved evidence orders, and verified commerce status.
  name: AVORA Agent Forge MCP Server
  slug: avora-agent-forge-mcp-server
modified: '2026-08-09'
name: AVORA Agent Forge
nav: Providers
network: true
overview: 'AVORA Agent Forge publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agent API and Public Evidence API. Tagged areas include Blockchain, Crypto, Solana, Token Risk, and Due Diligence.


  The AVORA Agent Forge catalog on APIs.io includes 1 JSON-LD context.


  AVORA Agent Forge''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, and 19 more developer resources.'
plans:
- name: Avora Agent Forge Plans
  plan_count: 4
  slug: avora-agent-forge-plans
random_paper: 5
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 50.7
    developer_ergonomics: 51.8
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Avora Agent Forge Authentication
  slug: avora-agent-forge-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Avora Agent Forge Domain Security
  slug: avora-agent-forge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avora-agent-forge
tags:
- Blockchain
- Crypto
- Solana
- Token Risk
- Due Diligence
- On-chain Evidence
- Fraud Intelligence
- AI Agents
- MCP
- A2A
- Signed Receipts
- Provenance
- Non-custodial Payments
- USDC
- Solana Pay
- Public-sector AI Interoperability
website: https://avora-agent-forge.netlify.app/agent-forge/
---
