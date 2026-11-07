---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Alphabotpro Cloud Agentic Access
  operation_count: 16
  slug: alphabotpro-cloud-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 1
apis:
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Checkout API from AlphaBotPro — 2 operation(s) for checkout.
  name: AlphaBotPro Checkout API
  slug: alphabotpro-cloud-checkout-api
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Ea API from AlphaBotPro — 1 operation(s) for ea.
  name: AlphaBotPro Ea API
  slug: alphabotpro-cloud-ea-api
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Expert Advisors API from AlphaBotPro — 1 operation(s) for expert advisors.
  name: AlphaBotPro Expert Advisors API
  slug: alphabotpro-cloud-expert-advisors-api
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Mcp API from AlphaBotPro — 1 operation(s) for mcp.
  name: AlphaBotPro MCP API
  slug: alphabotpro-cloud-mcp-api
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Signals API from AlphaBotPro — 1 operation(s) for signals.
  name: AlphaBotPro Signals API
  slug: alphabotpro-cloud-signals-api
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Stocks API from AlphaBotPro — 1 operation(s) for stocks.
  name: AlphaBotPro Stocks API
  slug: alphabotpro-cloud-stocks-api
- baseURL: https://mcp.alphabotpro.cloud
  baseurl_source: declared
  description: The Warroom API from AlphaBotPro — 1 operation(s) for warroom.
  name: AlphaBotPro Warroom API
  slug: alphabotpro-cloud-warroom-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/alphabotpro-cloud/agentic-access/alphabotpro-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alphabotpro-cloud-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/alphabotpro-cloud/plans/alphabotpro-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphabotpro-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alphabotpro-cloud/rules/alphabotpro-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/alphabotpro-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/alphabotpro-cloud/errors/alphabotpro-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alphabotpro-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alphabotpro-cloud/conformance/alphabotpro-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alphabotpro-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alphabotpro-cloud/llms/alphabotpro-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphabotpro-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/alphabotpro-cloud/mcp/alphabotpro-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alphabotpro-cloud-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alphabotpro-cloud/well-known/alphabotpro-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphabotpro-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/alphabotpro-cloud/hosts/alphabotpro-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphabotpro-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphabotpro-cloud/vendors/alphabotpro-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphabotpro-cloud-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://alphabotpro.cloud/src/signup.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alphabotpro.cloud/
- group: auth
  href: https://artifacts.apis.io/alphabotpro-cloud/authentication/alphabotpro-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alphabotpro-cloud-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alphabotpro-cloud/security/alphabotpro-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphabotpro-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphabotpro.cloud/
- group: company
  title: ''
  type: Blog
  url: https://alphabotpro.cloud/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://alphabotpro.cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphabotpro.cloud/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphabotpro.cloud/pages/privacy
created: '2026-11-01'
description: AlphaBotPro provides automated MT5 trading robots, VIP signal services, and risk‑control tools for prop‑firm traders. The platform offers free trials, AI‑driven market analysis, and a suite of bots that integrate with MetaTrader 5, helping users automate strategies, manage risk, and access premium trading signals across forex and commodities.
image: https://alphabotpro.cloud/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.alphabotpro.cloud requiring an API key.
  name: AlphaBotPro MCP Server
  slug: alphabotpro-cloud-mcp-yml
modified: '2026-11-01'
name: AlphaBotPro
nav: Providers
network: true
overview: 'AlphaBotPro publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkout API, Ea API, Expert Advisors API, and 4 more. Tagged areas include Company, Trading, Automation, Signals, and MT5.


  The AlphaBotPro catalog on APIs.io includes 1 Spectral governance ruleset.


  AlphaBotPro''s developer surface includes signup flow, documentation, authentication, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Alphabotpro Cloud Plans Pricing
  plan_count: 7
  slug: alphabotpro-cloud-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AlphaBotPro API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: alphabotpro-cloud-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 53.9
    contract_governance: 15.9
    contract_quality: 50.4
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alphabotpro Cloud Authentication
  slug: alphabotpro-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alphabotpro Cloud Domain Security
  slug: alphabotpro-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: alphabotpro-cloud
tags:
- Company
- Trading
- Automation
- Signals
- MT5
- PropFirm
website: https://alphabotpro.cloud/
---
