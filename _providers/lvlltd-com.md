---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Lvlltd Com Agentic Access
  operation_count: 32
  slug: lvlltd-com-agentic-access
  summary_line: 32 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://lvlltd.com
  baseurl_source: declared
  description: 'REST contract for the x402 skill marketplace: health and readiness probes, the ESP (Evaluate -> Settle -> Prove) protocol root, catalog search and the full catalog.json, free per-skill outline.json an'
  name: LVL LTD Agent Skill Market API
  slug: lvl-ltd-agent-skill-market-api
- description: Remote Model Context Protocol server at https://lvlltd.com/api/mcp (alias /mcp; HTTP JSON-RPC, protocol version 2025-06-18, serverInfo lvlltd-skill-market 1.1.0). initialize and tools/list answer anon
  name: LVL LTD MCP Server
  slug: lvl-ltd-mcp-server
- description: 'Agent2Agent surface: an Ed25519-JWS-signed agent card (protocolVersion 1.0.0, JSONRPC transport, version 1.5.0, JWKS at /.well-known/jwks.json) served from both /.well-known/agent-card.json and the le'
  name: LVL LTD Skill Market A2A Agent
  slug: lvl-ltd-a2a-agent
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/agentic-access/lvlltd-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lvlltd-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/security/lvlltd-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lvlltd-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/security/lvlltd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lvlltd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lvlltd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lvlltd.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://lvlltd.com/docs/REFERENCE.md
- group: start
  title: ''
  type: GettingStarted
  url: https://lvlltd.com/how-to/agent-setup/
- group: operate
  title: ''
  type: Support
  url: https://lvlltd.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omgawdmadeit1
- group: commercial
  title: ''
  type: Pricing
  url: https://lvlltd.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lvlltd.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lvlltd.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://lvlltd.com/security/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/a2a/lvlltd-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lvlltd-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/mcp/lvlltd-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lvlltd-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/well-known/lvlltd-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lvlltd-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/well-known/lvlltd-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lvlltd-com-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/llms/lvlltd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lvlltd-com-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/packages/lvlltd-com-packages.yml
  title: ''
  type: Packages
  url: packages/lvlltd-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/packages/lvlltd-com-packages.yml
  title: ''
  type: SDKs
  url: packages/lvlltd-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/conventions/lvlltd-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lvlltd-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/conventions/lvlltd-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lvlltd-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/errors/lvlltd-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lvlltd-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/lifecycle/lvlltd-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lvlltd-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/conformance/lvlltd-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lvlltd-com-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/rate-limits/lvlltd-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lvlltd-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/plans/lvlltd-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lvlltd-com-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/data-model/lvlltd-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lvlltd-com-data-model.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://lvlltd.com/docs/AGENT-RAILS-2026.md
- group: operate
  title: ''
  type: StatusPage
  url: https://lvlltd.com/monitors/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/authentication/lvlltd-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lvlltd-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/scopes/lvlltd-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lvlltd-com-scopes.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://lvlltd.com/privacy/
- group: other
  title: ''
  type: Subprocessors
  url: https://lvlltd.com/privacy/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lvlltd-com/refs/heads/main/well-known/lvlltd-com-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/lvlltd-com-robots.txt
created: '2026-09-19'
description: 'LVL LTD CO is a sole-operator product lab in Cleveland, Georgia (operator Joseph Lamar Taylor; trade name, LLC registration stated as pending) that runs lvlltd.com, an agent-native marketplace of 250 sealed AI-agent skill packs priced in USDC on Base (chain 8453) and settled over the x402 HTTP 402 protocol. Every skill has a free outline and sample; payment is proven by posting a Base transaction hash (or an EIP-3009 PAYMENT-SIGNATURE) back to /api/pay, and the public /api/proof ledger is the only success signal the operator will stand behind. The same catalog is exposed four ways: a 32-operation OpenAPI 3.1.0 REST contract at /openapi.json, a remote MCP server at /api/mcp that answers an anonymous tools/list with 59 tools, an Ed25519-JWS-signed A2A 1.0.0 agent card at /.well-known/agent-card.json with a JSON-RPC endpoint at /api/a2a, and a full agent map in /llms.txt. Optional AP2 spend mandates, ERC-8004 identity lookups, recurring catalog-access plans and a Coinbase CDP
  facilitator path sit on top of the one-time unlock model.'
image: https://lvlltd.com/og-imagine.jpg
layout: provider
mcp_servers:
- description: ''
  name: LVL LTD CO MCP Server
  slug: lvl-ltd-co-mcp-server
- description: ''
  name: LVL LTD MCP endpoint (HTTP JSON-RPC)
  slug: lvl-ltd-mcp-endpoint-http-json-rpc
modified: '2026-09-19'
name: LVL LTD CO
nav: Providers
network: true
overview: 'LVL LTD CO publishes 1 API on the [APIs.io](https://apis.io/) network: LVL LTD Agent Skill Market API. Tagged areas include Agents, Agentic Commerce, Agent Skills, A2A, and MCP.


  LVL LTD CO''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, and 30 more developer resources.'
plans:
- name: Lvlltd Com Plans Pricing
  plan_count: 9
  slug: lvlltd-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Lvlltd Com Rate Limits
  slug: lvlltd-com-rate-limits
scopes:
- name: Lvlltd Com Scopes
  scope_count: 4
  slug: lvlltd-com-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 50.3
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
    contract_quality: 36.7
    developer_ergonomics: 59.5
    discoverability: 75.9
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Lvlltd Com Authentication
  slug: lvlltd-com-authentication
  summary_line: none/x402-payment-proof · 5 schemes
- kind: domain-security
  name: Lvlltd Com Domain Security
  slug: lvlltd-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lvlltd Com Vulnerability Disclosure
  slug: lvlltd-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lvlltd-com
tags:
- Agents
- Agentic Commerce
- Agent Skills
- A2A
- MCP
- x402
- Micropayments
- Stablecoins
- Marketplace
- Agent-Native
- United States
website: https://lvlltd.com/
---
