---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Assetfare Agentic Access
  operation_count: 66
  slug: assetfare-agentic-access
  summary_line: 66 operations · 15 acting
api_count: 6
apis:
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: 'Reads the live v2 capability document: chains, asset endpoints, active and inactive directed routes, fee policy, amount policy and execution availability.'
  name: AssetFare Capabilities API
  slug: assetfare-capabilities-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: Returns a validated, bounded unsigned action bundle for a quote the caller has explicitly approved; the caller signs and submits.
  name: AssetFare Prepare API
  slug: assetfare-prepare-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: Quotes a live route with expected and minimum receive, total token-path cost, provider fees, ETA and the ordered direct-protocol provider path.
  name: AssetFare Quote API
  slug: assetfare-quote-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: 'Quote-bound, idempotent, receipt-driven sessions for multistep routes: create, read, observe source and output receipts, and refresh an expired unsubmitted action.'
  name: AssetFare Session API
  slug: assetfare-session-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: Reads route and provider health without creating a quote.
  name: AssetFare Status API
  slug: assetfare-status-api
- description: The earlier v1 route API (wallet auth, quote, session and status), still served for compatibility and listed in the provider's API catalog as a legacy anchor beside v2.
  name: AssetFare Legacy v1 Compatibility API
  slug: assetfare-legacy-v1-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The App Store API from AssetFare — 16 operation(s) for app store.
  name: AssetFare App Store API
  slug: assetfare-app-store-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: The Auth API from AssetFare — 2 operation(s) for auth.
  name: AssetFare Auth API
  slug: assetfare-auth-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Events API from AssetFare — 1 operation(s) for events.
  name: AssetFare Events API
  slug: assetfare-events-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Google Play API from AssetFare — 19 operation(s) for google play.
  name: AssetFare Google Play API
  slug: assetfare-google-play-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Jobs API from AssetFare — 1 operation(s) for jobs.
  name: AssetFare Jobs API
  slug: assetfare-jobs-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: The Route Selection API from AssetFare — 2 operation(s) for route selection.
  name: AssetFare Route Selection API
  slug: assetfare-route-selection-api
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: The .well Known API from AssetFare — 1 operation(s) for .well known.
  name: AssetFare .well Known API
  slug: assetfare-well-known-api
arazzos:
- description: Verify AssetFare and obtain a fresh Solana SOL to Base or Arbitrum ETH quote.
  name: AssetFare read-only route evaluation
  slug: assetfare-route-evaluation-arazzo
artifact_total: 29
common:
- group: other
  href: https://artifacts.apis.io/assetfare/capabilities/assetfare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/assetfare-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/assetfare/plans/assetfare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assetfare-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/assetfare/rate-limits/assetfare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/assetfare-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.assetfare.dev/mcp
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/assetfare/assetfare-mcp/blob/main/skills/assetfare-route/SKILL.md
- group: other
  href: https://artifacts.apis.io/assetfare/overlays/assetfare-agent-native-route-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/assetfare-agent-native-route-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/assetfare/security/assetfare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetfare-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/assetfare/security/assetfare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/assetfare-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/assetfare/authentication/assetfare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/assetfare-authentication.yml
- group: agent
  href: https://artifacts.apis.io/assetfare/well-known/assetfare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assetfare-well-known.yml
- group: auth
  href: https://artifacts.apis.io/assetfare/well-known/assetfare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/assetfare-security.txt
- group: auth
  href: https://artifacts.apis.io/assetfare/well-known/assetfare-security.txt
  title: ''
  type: Security
  url: well-known/assetfare-security.txt
- group: agent
  href: https://artifacts.apis.io/assetfare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/assetfare/mcp/assetfare-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/assetfare-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://assetfare.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://assetfare.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assetfare.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assetfare.dev/privacy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/assetfare/assetfare-mcp
- group: company
  title: ''
  type: Website
  url: https://assetfare.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://assetfare.dev/pilot/
- group: docs
  title: ''
  type: Documentation
  url: https://assetfare.dev/llms-full.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://assetfare.dev/llms.txt
- group: agent
  title: ''
  type: LLMsFullTxt
  url: https://assetfare.dev/llms-full.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://assetfare.dev/pricing.json
- group: other
  title: ''
  type: APICatalog
  url: https://api.assetfare.dev/.well-known/api-catalog
- group: other
  title: ''
  type: APICatalog
  url: https://assetfare.dev/.well-known/api-catalog
- group: other
  title: ''
  type: APIsJSON
  url: https://assetfare.dev/apis.json
- group: other
  title: ''
  type: AgentCard
  url: https://api.assetfare.dev/.well-known/agent-card.json
- group: other
  title: ''
  type: ARD
  url: https://assetfare.dev/.well-known/ard.json
- group: build
  title: ''
  type: PluginManifest
  url: https://assetfare.dev/.well-known/ai-plugin.json
- group: other
  title: ''
  type: X-ProviderManifest
  url: https://api.assetfare.dev/.well-known/assetfare-manifest.json
- group: operate
  title: ''
  type: StatusPage
  url: https://api.assetfare.dev/v2/status
- group: design
  title: ''
  type: Arazzo
  url: https://assetfare.dev/arazzo.yaml
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/assetfare-mcp
created: '2026-09-14'
description: A non-custodial routing API for AI agents that returns fee-inclusive cross-chain and same-chain quotes and bounded unsigned actions; the caller's own wallet verifies, signs and submits every transaction, and AssetFare never holds keys, signs or submits. Its live v2 capabilities document (checked 2026-10-03) lists 16 chains, 20 asset endpoints and 54 active directed routes (a further 44 measured routes are inactive), with a USD 1 minimum, no business maximum and an exact 1 bp service fee on top of provider and network fees. The v2 REST contract covers capabilities, quote, prepare, a receipt-driven session lifecycle and status; the same surface is offered over MCP and A2A, and a legacy v1 compatibility API remains live.
finops:
- has_sources: true
  method: derived
  name: Assetfare Finops
  primary_unit: eligible successful atomic action, on fee basis
  service_category: ''
  slug: assetfare-finops
  template: false
json_schemas:
- name: SessionResponse
  property_count: 9
  slug: assetfare-session-response
- name: UnsignedActionBundle
  property_count: 10
  slug: assetfare-unsigned-action-bundle
jsonld:
- class_count: 7
  name: Assetfare Context
  property_count: 74
  slug: assetfare-context
layout: provider
mcp_servers:
- description: ''
  name: AssetFare MCP Server
  slug: mcp
modified: '2026-10-03'
name: AssetFare
nav: Providers
network: true
overview: 'AssetFare publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Prepare API, Quote API, and 10 more. Tagged areas include AI Agents, Asset Transfer, Bridge, Cross-Chain, and Non-Custodial.


  The AssetFare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AssetFare''s developer surface includes authentication, pricing, getting-started guide, documentation, and 31 more developer resources.'
plans:
- name: Assetfare Plans Pricing
  plan_count: 2
  slug: assetfare-plans-pricing
- name: Assetfare Price Estimates
  plan_count: 0
  slug: assetfare-price-estimates
random_paper: 22
rate_limits:
- limit_count: 6
  name: Assetfare Rate Limits
  slug: assetfare-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AssetFare API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 1
  slug: assetfare-rules
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 34
    catalog_earned: 85.5
    catalog_earned_first_party: 20.0
    catalog_gap: 29.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 62.8
    developer_ergonomics: 35.7
    discoverability: 86.7
    operational_transparency: 63.2
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 21.1
      total: 19
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/assetfare/assetfare-2026-10-11T100552.png
security:
- kind: authentication
  name: Assetfare Authentication
  slug: assetfare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Assetfare Domain Security
  slug: assetfare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Assetfare Vulnerability Disclosure
  slug: assetfare-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: assetfare-route
  slug: assetfare-route
- name: quote-cross-chain-route
  slug: quote-cross-chain-route
slug: assetfare
tags:
- AI Agents
- Asset Transfer
- Bridge
- Cross-Chain
- Non-Custodial
- Cryptocurrency
- Solana
- Base
- Arbitrum
- Robinhood Chain
- Optimism
- Ethereum
- OpenAPI
- MCP
- Agent Skills
website: https://assetfare.dev/
---
