---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 36
  human_in_the_loop: 4
  name: Merchant 0 Com Agentic Access
  operation_count: 95
  slug: merchant-0-com-agentic-access
  summary_line: 95 operations · 36 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.merchant-0.com
  baseurl_source: declared
  description: The REST contract behind Merchant-0's agent-commerce surface, served by a FastAPI application at https://api.merchant-0.com and described by a 95-operation OpenAPI 3.1.0 document at /openapi.json. Pub
  name: Merchant-0 A2A Protocol Server API
  slug: merchant-0-a2a-protocol-server-api
- description: 'Agent2Agent (A2A) surface: an agent card served from https://merchant-0.com/.well-known/agent-card.json (with a pre-0.3 agent.json at the legacy path) naming did:web:merchant-0.com, four skills (SEA i'
  name: Merchant-0 A2A Agent
  slug: merchant-0-a2a-agent
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/security/merchant-0-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merchant-0-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/agentic-access/merchant-0-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/merchant-0-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://merchant-0.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.merchant-0.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://api.merchant-0.com/api/catalog
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/a2a/merchant-0-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/merchant-0-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/well-known/merchant-0-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/merchant-0-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/mcp/merchant-0-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/merchant-0-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/mcp/merchant-0-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/merchant-0-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/llms/merchant-0-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/merchant-0-com-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/conformance/merchant-0-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/merchant-0-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/errors/merchant-0-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/merchant-0-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/lifecycle/merchant-0-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/merchant-0-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/authentication/merchant-0-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/merchant-0-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/conventions/merchant-0-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/merchant-0-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/data-model/merchant-0-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/merchant-0-com-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/plans/merchant-0-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/merchant-0-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/rate-limits/merchant-0-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/merchant-0-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/sandbox/merchant-0-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/merchant-0-com-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/merchant-0-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'Merchant-0 is a self-described "sovereign autonomous enterprise" that sells machine-to-machine trade-intelligence products to other AI agents rather than to people: Grok-generated intelligence queries and market reports for Southeast Asian and BRICS+ trade corridors, freight-rate and HS-tariff monitoring, regulatory-risk briefs, origin attestations, agent DID verification and signed subscription-status proofs, priced per call or per monthly plan in USD and settled through a Wise business account. It identifies itself as did:web:merchant-0.com and publishes an A2A agent card at merchant-0.com/.well-known/agent-card.json (with a pre-0.3 agent.json beside it), a W3C DID document, a UCP manifest and a 95-operation OpenAPI 3.1 contract at api.merchant-0.com/openapi.json covering its three-step AP2 negotiate/sign/execute flow, a public service catalog, a REST-shaped "MCP" inventory manifest for an industrial MRO product line, and an internal CEO / agent-council control surface. The
  human-facing site is a Next.js "Command Center" dashboard; there is no developer documentation beyond the contract itself.'
image: https://merchant-0.com/icons/icon-512.png
layout: provider
mcp_servers:
- description: Industrial B2B product catalog with GEO-optimized metadata. Search fasteners, sensors, pneumatics, safety equipment, and more.
  name: Merchant-0 Inventory Server
  slug: merchant-0-inventory-server
modified: '2026-09-19'
name: Merchant-0
nav: Providers
network: true
overview: 'Merchant-0 publishes 1 API on the [APIs.io](https://apis.io/) network: A2A Protocol Server API. Tagged areas include Agents, Agentic Commerce, A2A, AP2, and Universal Commerce Protocol.


  Merchant-0''s developer surface includes API reference, pricing, authentication, sandbox, and 16 more developer resources.'
plans:
- name: Merchant 0 Com Plans Pricing
  plan_count: 4
  slug: merchant-0-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Merchant 0 Com Rate Limits
  slug: merchant-0-com-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 28.0
    discoverability: 68.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Merchant 0 Com Authentication
  slug: merchant-0-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Merchant 0 Com Domain Security
  slug: merchant-0-com-domain-security
  summary_line: TLSv1.3
slug: merchant-0-com
tags:
- Agents
- Agentic Commerce
- A2A
- AP2
- Universal Commerce Protocol
- Trade Intelligence
- Market Intelligence
- Supply Chain
- Southeast Asia
- Decentralized Identity
- agent-native
website: https://merchant-0.com/
---
