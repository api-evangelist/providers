---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Public, credential-free JSON behind the mundo.hergertsynthora.com 3D globe: GET /mapstate returns the live state of the mesh map (active layers, objects, sources, timestamps) and GET /api/capa/<slug> '
  name: SYNTHORA Live World Map API
  slug: synthora-live-world-map-api
- baseURL: https://api.hergertsynthora.com
  baseurl_source: declared
  description: Free machine-readable discovery documents
  name: Hergert Synthora Discovery API
  slug: hergertsynthora-com-discovery-api
- baseURL: https://api.hergertsynthora.com
  baseurl_source: declared
  description: The polymarket API from Hergert Synthora — 6 operation(s) for polymarket.
  name: Hergert Synthora Polymarket API
  slug: hergertsynthora-com-polymarket-api
- baseURL: https://api.hergertsynthora.com
  baseurl_source: declared
  description: Pre-trade and pre-payment safety checks
  name: Hergert Synthora Safety API
  slug: hergertsynthora-com-safety-api
- baseURL: https://api.hergertsynthora.com
  baseurl_source: declared
  description: The wallet-enrichment API from Hergert Synthora — 1 operation(s) for wallet-enrichment.
  name: Hergert Synthora Wallet Enrichment API
  slug: hergertsynthora-com-wallet-enrichment-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/hergertsynthora-com/capabilities/hergertsynthora-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hergertsynthora-com-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://hergertsynthora.com/rss.xml
- group: other
  href: https://artifacts.apis.io/hergertsynthora-com/overlays/hergertsynthora-com-mesh-aggregate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hergertsynthora-com-mesh-aggregate-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/skills/hergertsynthora-com-pay-per-call-x402.md
  title: ''
  type: AgentSkill
  url: skills/hergertsynthora-com-pay-per-call-x402.md
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/skills/hergertsynthora-com-polymarket-signal-sweep.md
  title: ''
  type: AgentSkill
  url: skills/hergertsynthora-com-polymarket-signal-sweep.md
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/skills/hergertsynthora-com-wallet-and-tx-screening.md
  title: ''
  type: AgentSkill
  url: skills/hergertsynthora-com-wallet-and-tx-screening.md
- group: other
  href: https://artifacts.apis.io/hergertsynthora-com/overlays/hergertsynthora-com-agent-notary-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hergertsynthora-com-agent-notary-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://notary.hergertsynthora.com/mcp
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/skills/hergertsynthora-com-notarize-and-verify.md
  title: ''
  type: AgentSkill
  url: skills/hergertsynthora-com-notarize-and-verify.md
- group: auth
  href: https://artifacts.apis.io/hergertsynthora-com/security/hergertsynthora-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hergertsynthora-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hergertsynthora-com/authentication/hergertsynthora-com-authentication.yml
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
  href: https://artifacts.apis.io/hergertsynthora-com/llms/hergertsynthora-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hergertsynthora-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://hergertsynthora.com/llms.txt
- group: other
  href: https://artifacts.apis.io/hergertsynthora-com/a2a/hergertsynthora-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hergertsynthora-com-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://hergertsynthora.com/.well-known/agent-card.json
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/mcp/hergertsynthora-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hergertsynthora-com-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.hergertsynthora.com/mcp
- group: build
  href: https://artifacts.apis.io/hergertsynthora-com/mcp/hergertsynthora-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hergertsynthora-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/well-known/hergertsynthora-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hergertsynthora-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hergertsynthora-com/well-known/hergertsynthora-com-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/hergertsynthora-com-x402.json
- group: design
  href: https://artifacts.apis.io/hergertsynthora-com/conformance/hergertsynthora-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hergertsynthora-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/hergertsynthora-com/errors/hergertsynthora-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hergertsynthora-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hergertsynthora-com/lifecycle/hergertsynthora-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hergertsynthora-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/hergertsynthora-com/lifecycle/hergertsynthora-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hergertsynthora-com-lifecycle.yml
- group: operate
  title: ''
  type: SLA
  url: https://api.hergertsynthora.com/sla/
- group: start
  href: https://artifacts.apis.io/hergertsynthora-com/sandbox/hergertsynthora-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hergertsynthora-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hergertsynthora-com/conventions/hergertsynthora-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hergertsynthora-com-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/hergertsynthora-com/plans/hergertsynthora-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hergertsynthora-com-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://hergertsynthora.com/muestras/
- group: operate
  href: https://artifacts.apis.io/hergertsynthora-com/rate-limits/hergertsynthora-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hergertsynthora-com-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/hergertsynthora-com/packages/hergertsynthora-com-packages.yml
  title: ''
  type: Packages
  url: packages/hergertsynthora-com-packages.yml
- group: design
  href: https://artifacts.apis.io/hergertsynthora-com/components/hergertsynthora-com-components.yml
  title: ''
  type: Components
  url: components/hergertsynthora-com-components.yml
- group: design
  href: https://artifacts.apis.io/hergertsynthora-com/data-model/hergertsynthora-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hergertsynthora-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/hergertsynthora-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/hergertsynthora-com/regulatory/hergertsynthora-com-regulatory-posture.yml
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
finops:
- has_sources: true
  method: derived
  name: Hergertsynthora Com Finops
  primary_unit: ''
  service_category: ''
  slug: hergertsynthora-com-finops
  template: true
image: https://hergertsynthora.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Hergert Synthora MCP Server
  slug: mcp
- description: Hergert Synthora runs a hosted, anonymous-to-list MCP server for its SYNTHORA intelligence mesh, plus a one-tool MCP endpoint on the Agent Notary host. Every tool is a read-only, x402-paid verdict; to
  name: Hergert Synthora MCP Server
  slug: synthora-mcp
modified: '2026-10-06'
name: Hergert Synthora
nav: Providers
network: true
overview: 'Hergert Synthora publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Polymarket API, Safety API, and 2 more. Tagged areas include Company, Agents, A2A, MCP, and x402.


  The Hergert Synthora catalog on APIs.io includes 1 Spectral governance ruleset.


  Hergert Synthora''s developer surface includes authentication, documentation, API reference, sandbox, pricing, and 42 more developer resources.'
plans:
- name: Hergertsynthora Com Plans Pricing
  plan_count: 6
  slug: hergertsynthora-com-plans-pricing
- name: Hergertsynthora Com Price Estimates
  plan_count: 0
  slug: hergertsynthora-com-price-estimates
random_paper: 13
rate_limits:
- limit_count: 2
  name: Hergertsynthora Com Rate Limits
  slug: hergertsynthora-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Hergert Synthora API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 1
  slug: hergertsynthora-com-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 47.4
    contract_governance: 31.8
    contract_quality: 52.7
    developer_ergonomics: 25.6
    discoverability: 75.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 49.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hergertsynthora-com/hergertsynthora-com-2026-10-11T105417.png
security:
- kind: authentication
  name: Hergertsynthora Com Authentication
  slug: hergertsynthora-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hergertsynthora Com Domain Security
  slug: hergertsynthora-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: hergertsynthora-com-notarize-and-verify
  slug: hergertsynthora-com-notarize-and-verify
- name: hergertsynthora-com-pay-per-call-x402
  slug: hergertsynthora-com-pay-per-call-x402
- name: hergertsynthora-com-polymarket-signal-sweep
  slug: hergertsynthora-com-polymarket-signal-sweep
- name: hergertsynthora-com-wallet-and-tx-screening
  slug: hergertsynthora-com-wallet-and-tx-screening
slug: hergertsynthora-com
tags:
- Company
- Agents
- A2A
- MCP
- x402
- Web3
- Sanctions Screening
- Prediction Markets
- OSINT
- Blockchain
- Spain
website: https://hergertsynthora.com/
---
