---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Hostdefi Agentic Access
  operation_count: 32
  slug: hostdefi-agentic-access
  summary_line: 32 operations · 10 acting
api_count: 1
apis:
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: Token risk scanning for Solana mints — authority state, liquidity, holder concentration, Token-2022 extension flags and sell simulation. 26 operations, API-key authentication.
  name: HostDeFi Token Risk API
  slug: hostdefi-token-risk-api
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: The Analyze Token API from HostDeFi — 1 operation(s) for analyze token.
  name: HostDeFi Analyze Token API
  slug: hostdefi-analyze-token-api
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: The Health API from HostDeFi — 1 operation(s) for health.
  name: HostDeFi Health API
  slug: hostdefi-health-api
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: The Keys API from HostDeFi — 1 operation(s) for keys.
  name: HostDeFi Keys API
  slug: hostdefi-keys-api
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: The Scan API from HostDeFi — 1 operation(s) for scan.
  name: HostDeFi Scan API
  slug: hostdefi-scan-api
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: The Usage API from HostDeFi — 1 operation(s) for usage.
  name: HostDeFi Usage API
  slug: hostdefi-usage-api
- baseURL: https://hostdefi.com/api
  baseurl_source: declared
  description: 'Pay-per-call lane for AI agents (x402 protocol): no key, no account - pay USDC per request and get the same A+-F Safety Read. Free tier and API-key plans are unchanged and remain the better per-call p'
  name: HostDeFi x402 (machine-payable) API
  slug: hostdefi-x402-machine-payable-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/hostdefi/capabilities/hostdefi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hostdefi-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://hostdefi.com/feed.xml
- group: agent
  href: https://artifacts.apis.io/hostdefi/agentic-access/hostdefi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hostdefi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hostdefi/security/hostdefi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hostdefi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hostdefi/security/hostdefi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hostdefi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hostdefi/authentication/hostdefi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hostdefi-authentication.yml
- group: agent
  href: https://artifacts.apis.io/hostdefi/mcp/hostdefi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hostdefi-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/hostdefi/finops/hostdefi-x402-manifest.json
  title: ''
  type: FinOps
  url: finops/hostdefi-x402-manifest.json
- group: agent
  href: https://artifacts.apis.io/hostdefi/llms/hostdefi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hostdefi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://hostdefi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hostdefi.com/docs/api/
- group: other
  href: https://artifacts.apis.io/hostdefi/a2a/hostdefi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hostdefi-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hostdefi/well-known/hostdefi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hostdefi-well-known.yml
- group: auth
  href: https://artifacts.apis.io/hostdefi/well-known/hostdefi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hostdefi-security.txt
- group: auth
  title: ''
  type: Security
  url: https://hostdefi.com/why
- group: design
  href: https://artifacts.apis.io/hostdefi/errors/hostdefi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hostdefi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hostdefi/lifecycle/hostdefi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hostdefi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hostdefi/conformance/hostdefi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hostdefi-conformance.yml
- group: design
  href: https://artifacts.apis.io/hostdefi/conventions/hostdefi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hostdefi-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/hostdefi/plans/hostdefi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hostdefi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hostdefi/rate-limits/hostdefi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hostdefi-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/hostdefi/packages/hostdefi-packages.yml
  title: ''
  type: Packages
  url: packages/hostdefi-packages.yml
- group: design
  href: https://artifacts.apis.io/hostdefi/data-model/hostdefi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hostdefi-data-model.yml
- group: agent
  href: https://artifacts.apis.io/hostdefi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/hostdefi/overlays/hostdefi-token-risk-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hostdefi-token-risk-api-overlay.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://hostdefi.com/docs/api/
- group: operate
  title: ''
  type: Support
  url: https://t.me/hostdefiapps
created: '2026-08-21'
description: 'HostDeFi is a non-custodial Solana token-risk service that scans a mint before a purchase — mint and freeze authority state, liquidity depth and lock status, holder concentration, dangerous Token-2022 extensions, sell simulation and contract flags. The public contract is an OpenAPI 3.1 document of 32 operations served from hostdefi.com/api with API-key authentication. HostDeFi also exposes an x402 machine-payment surface: an authority quick-check endpoint that returns HTTP 402 with a signed payment challenge, priced in USDC and payable on either Solana or Base, so an agent can buy a single check without an account.'
finops:
- has_sources: true
  method: derived
  name: Hostdefi Finops
  primary_unit: call
  service_category: ''
  slug: hostdefi-finops
  template: false
image: https://hostdefi.com/logo512.png
layout: provider
mcp_servers:
- description: Remote MCP server at hostdefi.com over HTTP; 15 tools listed.
  name: HostDeFi MCP Server
  slug: hostdefi
modified: '2026-10-06'
name: HostDeFi
nav: Providers
network: true
overview: 'HostDeFi publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Token Risk API, Analyze Token API, Health API, and 4 more. Tagged areas include Solana, Token Risk, DeFi, rug pull, and x402.


  The HostDeFi catalog on APIs.io includes 1 Spectral governance ruleset.


  HostDeFi''s developer surface includes authentication, pricing, support, and 24 more developer resources.'
plans:
- name: Hostdefi Plans Pricing
  plan_count: 15
  slug: hostdefi-plans-pricing
- name: Hostdefi Price Estimates
  plan_count: 0
  slug: hostdefi-price-estimates
random_paper: 14
rate_limits:
- limit_count: 3
  name: Hostdefi Rate Limits
  slug: hostdefi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: HostDeFi API Rules
  rule_count: 67
  severity_counts:
    error: 57
    hint: 0
    info: 4
    warn: 6
  slug: hostdefi-rules
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 56.9
    developer_ergonomics: 44.6
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hostdefi/hostdefi-2026-09-02T145742.png
security:
- kind: authentication
  name: Hostdefi Authentication
  slug: hostdefi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hostdefi Domain Security
  slug: hostdefi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hostdefi Vulnerability Disclosure
  slug: hostdefi-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Buy an API key with SOL and track quota
  slug: hostdefi-buy-key-with-sol
- name: Scan a token for safety, free
  slug: hostdefi-free-token-safety-scan
- name: Pay per call with x402
  slug: hostdefi-x402-pay-per-call
slug: hostdefi
tags:
- Solana
- Token Risk
- DeFi
- rug pull
- x402
- A2A
website: https://hostdefi.com
---
