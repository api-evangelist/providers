---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-09-21'
api_count: 2
apis:
- baseURL: https://api.hergertsynthora.com
  baseurl_source: declared
  description: 'Aggregate contract for the SYNTHORA x402 mesh: pay-per-call intelligence verdicts (contract safety, wallet enrichment, Polymarket whale/odds/resolution/dispute/insider signals) served as POST JSON on '
  name: SYNTHORA Machine-Payable API Mesh
  slug: synthora-machine-payable-api-mesh
- baseURL: https://notary.hergertsynthora.com
  baseurl_source: declared
  description: 'Proof-of-existence, proof-of-execution and proof-of-agreement for machine-to-machine deals: notarize a SHA-256 (content never stored) and receive an Ed25519-signed receipt anyone can verify later. 0.0'
  name: SYNTHORA Agent Notary
  slug: synthora-agent-notary
- baseURL: https://api.hergertsynthora.com/v1
  baseurl_source: declared
  description: The individual OpenAPI contracts published by the SYNTHORA product hosts under *.hergertsynthora.com - one POST /service operation each (sanctions and AML screening, vessel and chokepoint risk, DeFi T
  name: SYNTHORA x402 Per-Service Contracts
  slug: synthora-x402-per-service-contracts
- description: 'Public, credential-free JSON behind the mundo.hergertsynthora.com 3D globe: GET /mapstate returns the live state of the mesh map (active layers, objects, sources, timestamps) and GET /api/capa/<slug> '
  name: SYNTHORA Live World Map API
  slug: synthora-live-world-map-api
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/security/hergertsynthora-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hergertsynthora-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/authentication/hergertsynthora-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hergertsynthora-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hergertsynthora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hergertsynthora.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://api.hergertsynthora.com/openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/llms/hergertsynthora-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hergertsynthora-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://hergertsynthora.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/a2a/hergertsynthora-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hergertsynthora-com-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://hergertsynthora.com/.well-known/agent-card.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/mcp/hergertsynthora-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hergertsynthora-com-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.hergertsynthora.com/mcp
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/mcp/hergertsynthora-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hergertsynthora-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/well-known/hergertsynthora-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hergertsynthora-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/well-known/hergertsynthora-com-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/hergertsynthora-com-x402.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/conformance/hergertsynthora-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hergertsynthora-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/errors/hergertsynthora-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hergertsynthora-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/lifecycle/hergertsynthora-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hergertsynthora-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/lifecycle/hergertsynthora-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hergertsynthora-com-lifecycle.yml
- group: operate
  title: ''
  type: SLA
  url: https://api.hergertsynthora.com/sla/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/sandbox/hergertsynthora-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hergertsynthora-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/conventions/hergertsynthora-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hergertsynthora-com-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/plans/hergertsynthora-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hergertsynthora-com-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://hergertsynthora.com/muestras/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/rate-limits/hergertsynthora-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hergertsynthora-com-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/packages/hergertsynthora-com-packages.yml
  title: ''
  type: Packages
  url: packages/hergertsynthora-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/components/hergertsynthora-com-components.yml
  title: ''
  type: Components
  url: components/hergertsynthora-com-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/data-model/hergertsynthora-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hergertsynthora-com-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hergertsynthora-com/refs/heads/main/regulatory/hergertsynthora-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/hergertsynthora-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://hergertsynthora.com/legal/privacidad/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hergertsynthora.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hergertsynthora.com/legal/privacidad/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://hergertsynthora.com/legal/aviso-legal/
- group: other
  title: ''
  type: CookiePolicy
  url: https://hergertsynthora.com/legal/cookies/
- group: other
  title: ''
  type: Sitemap
  url: https://hergertsynthora.com/sitemap-index.xml
- group: other
  title: ''
  type: Robots
  url: https://hergertsynthora.com/robots.txt
- group: company
  title: ''
  type: About
  url: https://hergertsynthora.com/grupo/
- group: operate
  title: ''
  type: Contact
  url: https://hergertsynthora.com/contacto/
created: '2026-09-19'
description: 'HERGERT SYNTHORA S.L. is a Las Palmas de Gran Canaria (Spain) company that operates SYNTHORA, an autonomous agent mesh selling machine-payable intelligence: 121 pay-per-call verdict products (sanctions and AML screening, wallet and transaction risk, Polymarket and prediction-market signals, maritime AIS, DeFi, macro and OSINT data), an Agent Notary, a 30-tool hosted MCP server and a signed A2A agent card, all settled per call in USDC on Base over the x402 protocol with Ed25519-signed receipts, an ERC-8004 on-chain identity and no accounts or API keys.'
image: https://hergertsynthora.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: synthora-notario MCP endpoint (1 tool)
  slug: synthora-notario-mcp-endpoint-1-tool
- description: Hergert Synthora runs a hosted, anonymous-to-list MCP server for its SYNTHORA intelligence mesh, plus a one-tool MCP endpoint on the Agent Notary host. Every tool is a read-only, x402-paid verdict; to
  name: Hergert Synthora MCP Server
  slug: hergert-synthora-mcp-server
- description: ''
  name: 'synthora-mcp remote endpoint (30 tools). POST-only JSON-RPC: a GET answers 404 {"error": "MCP endpoint: POST JSON-RPC"} by design; verified live 2026-09-19 with initialize + tools/list.'
  slug: synthora-mcp-remote-endpoint-30-tools-post-only-json-rpc-a-get-answers-404-error-mcp-endpoint-post-json-rpc-by-design-verified-live-2026-09-19-with-initialize-toolslist
modified: '2026-09-19'
name: Hergert Synthora
nav: Providers
network: true
overview: 'Hergert Synthora publishes 3 APIs on the [APIs.io](https://apis.io/) network: SYNTHORA Machine-Payable API Mesh, SYNTHORA Agent Notary, and SYNTHORA x402 Per-Service Contracts. Tagged areas include Company, Agents, A2A, MCP, and x402.


  Hergert Synthora''s developer surface includes authentication, documentation, API reference, sandbox, pricing, and 33 more developer resources.'
plans:
- name: Hergertsynthora Com Plans Pricing
  plan_count: 6
  slug: hergertsynthora-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Hergertsynthora Com Rate Limits
  slug: hergertsynthora-com-rate-limits
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 52.9
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 46.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hergertsynthora Com Authentication
  slug: hergertsynthora-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hergertsynthora Com Domain Security
  slug: hergertsynthora-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hergertsynthora-com
tags:
- Company
- Agents
- A2A
- MCP
- x402
- Web3
- Intelligence
- Sanctions Screening
- Prediction Markets
- OSINT
- Blockchain
- Spain
website: https://hergertsynthora.com/
---
