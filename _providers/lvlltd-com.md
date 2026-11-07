---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Lvlltd Com Agentic Access
  operation_count: 32
  slug: lvlltd-com-agentic-access
  summary_line: 32 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://lvlltd.com/api/mcp (alias /mcp; HTTP JSON-RPC, protocol version 2025-06-18, serverInfo lvlltd-skill-market 1.1.0). initialize and tools/list answer anon
  name: LVL LTD MCP Server
  slug: lvl-ltd-mcp-server
- description: 'Agent2Agent surface: an Ed25519-JWS-signed agent card (protocolVersion 1.0.0, JSONRPC transport, version 1.5.0, JWKS at /.well-known/jwks.json) served from both /.well-known/agent-card.json and the le'
  name: LVL LTD Skill Market A2A Agent
  slug: lvl-ltd-a2a-agent
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The A2a API from LVL LTD CO — 1 operation(s) for a2a.
  name: LVL LTD CO A2a API
  slug: lvlltd-com-a2a-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Access API from LVL LTD CO — 1 operation(s) for access.
  name: LVL LTD CO Access API
  slug: lvlltd-com-access-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Agent Identity API from LVL LTD CO — 1 operation(s) for agent identity.
  name: LVL LTD CO Agent Identity API
  slug: lvlltd-com-agent-identity-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Bundles API from LVL LTD CO — 1 operation(s) for bundles.
  name: LVL LTD CO Bundles API
  slug: lvlltd-com-bundles-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Catalog API from LVL LTD CO — 1 operation(s) for catalog.
  name: LVL LTD CO Catalog API
  slug: lvlltd-com-catalog-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Catalog.json API from LVL LTD CO — 1 operation(s) for catalog.json.
  name: LVL LTD CO Catalog.json API
  slug: lvlltd-com-catalog-json-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Esp API from LVL LTD CO — 1 operation(s) for esp.
  name: LVL LTD CO Esp API
  slug: lvlltd-com-esp-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Eval API from LVL LTD CO — 1 operation(s) for eval.
  name: LVL LTD CO Eval API
  slug: lvlltd-com-eval-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Health API from LVL LTD CO — 1 operation(s) for health.
  name: LVL LTD CO Health API
  slug: lvlltd-com-health-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Intent API from LVL LTD CO — 1 operation(s) for intent.
  name: LVL LTD CO Intent API
  slug: lvlltd-com-intent-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Judges API from LVL LTD CO — 1 operation(s) for judges.
  name: LVL LTD CO Judges API
  slug: lvlltd-com-judges-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Mandates API from LVL LTD CO — 1 operation(s) for mandates.
  name: LVL LTD CO Mandates API
  slug: lvlltd-com-mandates-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Mcp API from LVL LTD CO — 1 operation(s) for mcp.
  name: LVL LTD CO MCP API
  slug: lvlltd-com-mcp-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Meter API from LVL LTD CO — 1 operation(s) for meter.
  name: LVL LTD CO Meter API
  slug: lvlltd-com-meter-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Pay API from LVL LTD CO — 1 operation(s) for pay.
  name: LVL LTD CO Pay API
  slug: lvlltd-com-pay-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Proof API from LVL LTD CO — 1 operation(s) for proof.
  name: LVL LTD CO Proof API
  slug: lvlltd-com-proof-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Ready API from LVL LTD CO — 1 operation(s) for ready.
  name: LVL LTD CO Ready API
  slug: lvlltd-com-ready-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Revenue API from LVL LTD CO — 1 operation(s) for revenue.
  name: LVL LTD CO Revenue API
  slug: lvlltd-com-revenue-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Security API from LVL LTD CO — 1 operation(s) for security.
  name: LVL LTD CO Security API
  slug: lvlltd-com-security-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Shop API from LVL LTD CO — 1 operation(s) for shop.
  name: LVL LTD CO Shop API
  slug: lvlltd-com-shop-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Signals API from LVL LTD CO — 1 operation(s) for signals.
  name: LVL LTD CO Signals API
  slug: lvlltd-com-signals-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Skills API from LVL LTD CO — 2 operation(s) for skills.
  name: LVL LTD CO Skills API
  slug: lvlltd-com-skills-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Subscribe API from LVL LTD CO — 1 operation(s) for subscribe.
  name: LVL LTD CO Subscribe API
  slug: lvlltd-com-subscribe-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The Trust API from LVL LTD CO — 1 operation(s) for trust.
  name: LVL LTD CO Trust API
  slug: lvlltd-com-trust-api
- baseURL: https://lvlltd.com/api/mcp
  baseurl_source: declared
  description: The .well Known API from LVL LTD CO — 1 operation(s) for .well known.
  name: LVL LTD CO .well Known API
  slug: lvlltd-com-well-known-api
artifact_total: 40
common:
- group: other
  href: https://artifacts.apis.io/lvlltd-com/capabilities/lvlltd-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lvlltd-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lvlltd-com/overlays/lvlltd-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lvlltd-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lvlltd-com/agentic-access/lvlltd-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lvlltd-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lvlltd-com/security/lvlltd-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lvlltd-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lvlltd-com/security/lvlltd-com-domain-security.yml
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
  href: https://artifacts.apis.io/lvlltd-com/a2a/lvlltd-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lvlltd-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/lvlltd-com/mcp/lvlltd-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lvlltd-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lvlltd-com/well-known/lvlltd-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lvlltd-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/lvlltd-com/well-known/lvlltd-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lvlltd-com-security.txt
- group: agent
  href: https://artifacts.apis.io/lvlltd-com/llms/lvlltd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lvlltd-com-llms.txt
- group: build
  href: https://artifacts.apis.io/lvlltd-com/packages/lvlltd-com-packages.yml
  title: ''
  type: Packages
  url: packages/lvlltd-com-packages.yml
- group: build
  href: https://artifacts.apis.io/lvlltd-com/packages/lvlltd-com-packages.yml
  title: ''
  type: SDKs
  url: packages/lvlltd-com-packages.yml
- group: design
  href: https://artifacts.apis.io/lvlltd-com/conventions/lvlltd-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lvlltd-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/lvlltd-com/conventions/lvlltd-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lvlltd-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/lvlltd-com/errors/lvlltd-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lvlltd-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lvlltd-com/lifecycle/lvlltd-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lvlltd-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lvlltd-com/conformance/lvlltd-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lvlltd-com-conformance.yml
- group: operate
  href: https://artifacts.apis.io/lvlltd-com/rate-limits/lvlltd-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lvlltd-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lvlltd-com/plans/lvlltd-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lvlltd-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/lvlltd-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lvlltd-com/data-model/lvlltd-com-data-model.yml
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
  href: https://artifacts.apis.io/lvlltd-com/authentication/lvlltd-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lvlltd-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lvlltd-com/scopes/lvlltd-com-scopes.yml
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
  href: https://artifacts.apis.io/lvlltd-com/well-known/lvlltd-com-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/lvlltd-com-robots.txt
created: '2026-09-19'
description: 'LVL LTD CO is a sole-operator product lab in Cleveland, Georgia (operator Joseph Lamar Taylor; trade name, LLC registration stated as pending) that runs lvlltd.com, an agent-native marketplace of 250 sealed AI-agent skill packs priced in USDC on Base (chain 8453) and settled over the x402 HTTP 402 protocol. Every skill has a free outline and sample; payment is proven by posting a Base transaction hash (or an EIP-3009 PAYMENT-SIGNATURE) back to /api/pay, and the public /api/proof ledger is the only success signal the operator will stand behind. The same catalog is exposed four ways: a 32-operation OpenAPI 3.1.0 REST contract at /openapi.json, a remote MCP server at /api/mcp that answers an anonymous tools/list with 59 tools, an Ed25519-JWS-signed A2A 1.0.0 agent card at /.well-known/agent-card.json with a JSON-RPC endpoint at /api/a2a, and a full agent map in /llms.txt. Optional AP2 spend mandates, ERC-8004 identity lookups, recurring catalog-access plans and a Coinbase CDP
  facilitator path sit on top of the one-time unlock model.'
finops:
- has_sources: true
  method: derived
  name: Lvlltd Com Finops
  primary_unit: 90 replies
  service_category: ''
  slug: lvlltd-com-finops
  template: false
image: https://lvlltd.com/og-imagine.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at lvlltd.com over HTTP; 59 tools listed.
  name: LVL LTD CO MCP Server
  slug: lvlltd-skill-market
modified: '2026-09-19'
name: LVL LTD CO
nav: Providers
network: true
overview: 'LVL LTD CO publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Access API, Agent Identity API, and 24 more. Tagged areas include Agents, Agentic Commerce, Agent Skills, A2A, and MCP.


  The LVL LTD CO catalog on APIs.io includes 1 Spectral governance ruleset.


  LVL LTD CO''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, and 32 more developer resources.'
plans:
- name: Lvlltd Com Plans Pricing
  plan_count: 4
  slug: lvlltd-com-plans-pricing
- name: Lvlltd Com Price Estimates
  plan_count: 0
  slug: lvlltd-com-price-estimates
random_paper: 14
rate_limits:
- limit_count: 1
  name: Lvlltd Com Rate Limits
  slug: lvlltd-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: LVL LTD CO API Rules
  rule_count: 38
  severity_counts:
    error: 33
    hint: 0
    info: 2
    warn: 3
  slug: lvlltd-com-rules
scopes:
- name: Lvlltd Com Scopes
  scope_count: 4
  slug: lvlltd-com-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 46.1
    developer_ergonomics: 42.9
    discoverability: 75.0
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 25
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 44.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lvlltd-com/lvlltd-com-2026-10-11T110618.png
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
skill_count: 2
skills:
- name: ESP evaluate, settle and prove a skill purchase
  slug: lvlltd-com-esp-evaluate-settle-prove
- name: lvlltd-x402-shop
  slug: lvlltd-com-x402-shop
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
