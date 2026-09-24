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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gonna Bond Agentic Access
  operation_count: 24
  slug: gonna-bond-agentic-access
  summary_line: 24 operations · 3 acting
api_count: 1
apis:
- baseURL: https://legit.gonna.bond
  baseurl_source: declared
  description: 'REST API for the LEGIT trust oracle: trust-check one x402 merchant address (score, grade, uptime, latency, explanation), pull a deep report with 30-day history and percentile, batch-check up to 20 add'
  name: LEGIT Trust API
  slug: legit-trust-api
- description: Remote Model Context Protocol server at https://legit.gonna.bond/mcp (stateless JSON-RPC 2.0 over HTTP POST; initialize reports protocolVersion 2024-11-05, serverInfo legit 1.0.0, capabilities tools o
  name: LEGIT MCP Server
  slug: legit-mcp-server
- description: 'Agent card served from https://legit.gonna.bond/.well-known/agent.json and, byte-identical, from the canonical /.well-known/agent-card.json: name LEGIT, version 0.1.0, provider organization GONNA, cap'
  name: LEGIT A2A Agent Card
  slug: legit-a2a-agent
artifact_total: 12
asyncapis:
- description: ''
  name: Gonna Bond Watch Webhooks
  slug: gonna-bond-watch-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/agentic-access/gonna-bond-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gonna-bond-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/security/gonna-bond-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gonna-bond-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/well-known/gonna-bond-security.txt
  title: ''
  type: Security
  url: well-known/gonna-bond-security.txt
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/sandbox/gonna-bond-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gonna-bond-sandbox.yml
- group: company
  title: ''
  type: Website
  url: https://gonna.bond/
- group: docs
  title: ''
  type: Documentation
  url: https://legit.gonna.bond/docs
- group: docs
  title: ''
  type: APIReference
  url: https://legit.gonna.bond/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://legit.gonna.bond/.well-known/legit
- group: operate
  title: ''
  type: Community
  url: https://t.me/GONNAFI
- group: company
  title: ''
  type: Twitter
  url: https://x.com/gonnalgo
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/a2a/gonna-bond-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gonna-bond-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/mcp/gonna-bond-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gonna-bond-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/mcp/gonna-bond-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gonna-bond-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/llms/gonna-bond-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gonna-bond-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/well-known/gonna-bond-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gonna-bond-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/well-known/gonna-bond-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gonna-bond-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/well-known/gonna-bond-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/gonna-bond-x402.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/asyncapi/gonna-bond-watch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gonna-bond-watch-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/authentication/gonna-bond-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gonna-bond-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/conventions/gonna-bond-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gonna-bond-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/errors/gonna-bond-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gonna-bond-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/data-model/gonna-bond-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gonna-bond-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/components/gonna-bond-components.yml
  title: ''
  type: Components
  url: components/gonna-bond-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/rate-limits/gonna-bond-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gonna-bond-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/plans/gonna-bond-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gonna-bond-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/conformance/gonna-bond-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gonna-bond-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/lifecycle/gonna-bond-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gonna-bond-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/packages/gonna-bond-packages.yml
  title: ''
  type: Packages
  url: packages/gonna-bond-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/security/gonna-bond-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gonna-bond-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gonna-bond/refs/heads/main/regulatory/gonna-bond-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/gonna-bond-regulatory-posture.yml
created: '2026-09-19'
description: 'GONNA is an Algorand-native meme-coin and games community ($GONNA, Algorand ASA 2582294183; the "GONNAVERSE" at gonna.bond) that builds and operates LEGIT, a trust oracle for the x402 agentic economy at legit.gonna.bond. LEGIT trust-checks any x402 merchant or agent address across Algorand, Base, Solana and 17 other chains before a payment is routed: grades (A+ to F) and scores (0-100) are built from live uptime, latency and payment-coherence probes rather than self-reported data. The surface is exposed three ways from one host: a 24-operation OpenAPI 3.1.0 REST contract at https://legit.gonna.bond/openapi.json (free reads; five verdict endpoints paid per call in USDC over x402, $0.004 on Algorand / $0.005 on Base, no accounts or API keys), a remote MCP server at https://legit.gonna.bond/mcp answering an anonymous tools/list with four tools, and an A2A-style agent card at /.well-known/agent.json and /.well-known/agent-card.json. The apex site gonna.bond is a JavaScript-rendered
  community page with no API surface of its own.'
image: https://legit.gonna.bond/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: GONNA MCP Server
  slug: gonna-mcp-server
- description: ''
  name: LEGIT MCP endpoint (JSON-RPC 2.0 over HTTP POST)
  slug: legit-mcp-endpoint-json-rpc-20-over-http-post
modified: '2026-09-19'
name: GONNA
nav: Providers
network: true
overview: 'GONNA publishes 1 API on the [APIs.io](https://apis.io/) network: LEGIT Trust API. Tagged areas include Company, Agents, Agentic Commerce, x402, and Trust.


  The GONNA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GONNA''s developer surface includes sandbox, documentation, API reference, pricing, authentication, and 26 more developer resources.'
plans:
- name: Gonna Bond Plans Pricing
  plan_count: 2
  slug: gonna-bond-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Gonna Bond Rate Limits
  slug: gonna-bond-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 54.5
    developer_ergonomics: 42.3
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Gonna Bond Authentication
  slug: gonna-bond-authentication
  summary_line: none/x402 · 3 schemes
- kind: domain-security
  name: Gonna Bond Domain Security
  slug: gonna-bond-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gonna Bond Vulnerability Disclosure
  slug: gonna-bond-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gonna-bond
tags:
- Company
- Agents
- Agentic Commerce
- x402
- Trust
- Merchant Trust
- MCP
- A2A
- Algorand
- Blockchain
- Payments
- Agent-Native
website: https://gonna.bond/
---
