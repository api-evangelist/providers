---
access_model:
  confidence: high
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Degenhedge Com Agentic Access
  operation_count: 4
  slug: degenhedge-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://degenhedge.com
  baseurl_source: declared
  description: The fees API from DegenHedge — 1 operation(s) for fees.
  name: DegenHedge Fees API
  slug: degenhedge-com-fees-api
- baseURL: https://degenhedge.com
  baseurl_source: declared
  description: The market data API from DegenHedge — 1 operation(s) for market data.
  name: DegenHedge market data API
  slug: degenhedge-com-market-data-api
- baseURL: https://degenhedge.com
  baseurl_source: declared
  description: The record API from DegenHedge — 2 operation(s) for record.
  name: DegenHedge Record API
  slug: degenhedge-com-record-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/degenhedge-com/agentic-access/degenhedge-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/degenhedge-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/degenhedge-com/rate-limits/degenhedge-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/degenhedge-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/degenhedge-com/plans/degenhedge-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/degenhedge-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/rules/degenhedge-com-rules.yml
  title: ''
  type: Spectral
  url: rules/degenhedge-com-rules.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/json-ld/degenhedge-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/degenhedge-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/degenhedge-com/vocabulary/degenhedge-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/degenhedge-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/degenhedge-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/data-model/degenhedge-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/degenhedge-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/conventions/degenhedge-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/degenhedge-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/degenhedge-com/authentication/degenhedge-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/degenhedge-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/degenhedge-com/lifecycle/degenhedge-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/degenhedge-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/lifecycle/degenhedge-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/degenhedge-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/errors/degenhedge-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/degenhedge-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/degenhedge-com/conformance/degenhedge-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/degenhedge-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/degenhedge-com/overlays/degenhedge-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/degenhedge-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/degenhedge-com/llms/degenhedge-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/degenhedge-com-llms.txt
- group: build
  href: https://artifacts.apis.io/degenhedge-com/mcp/degenhedge-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/degenhedge-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/degenhedge-com/mcp/degenhedge-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/degenhedge-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/degenhedge-com/hosts/degenhedge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/degenhedge-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/degenhedge-com/integrations/degenhedge-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/degenhedge-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/degenhedge-com/vendors/degenhedge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/degenhedge-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/degenhedge-com/security/degenhedge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/degenhedge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://degenhedge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://degenhedge.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://degenhedge.com/kalshi-btc-15-minute-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://degenhedge.com/getting-started/
- group: company
  title: ''
  type: About
  url: https://degenhedge.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://degenhedge.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://degenhedge.com/start/?market=kalshi
- group: company
  title: ''
  type: Blog
  url: https://degenhedge.com/research/
- group: operate
  title: ''
  type: Support
  url: mailto:team@degenhedge.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://degenhedge.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://degenhedge.com/privacy/
- group: other
  title: ''
  type: Telegram
  url: https://t.me/DegenHedgeProof
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/datasets/DegenHedge/kalshi-btc-15m
- group: agent
  title: ''
  type: LLMsTxt
  url: https://degenhedge.com/llms.txt
created: '2026-11-05'
description: 'DegenHedge, a service of EPWH, LLC (a Rhode Island limited liability company), publishes graded Telegram alerts and original data studies for Kalshi prediction markets: the Bitcoin 15-minute up/down markets (series KXBTC15M) and in-game NFL, MLB and NBA markets. Every alert is logged before the outcome is known and graded at settlement, losses included, in a public results log and CSV. It also offers a free read-only public API (/api/btc-window, /api/record, /api/kalshi-fee, /results.csv, described by /openapi.json) and a remote MCP server at https://degenhedge.com/mcp. Feeds cost $4.99 a month after a 30-day trial; for informational and entertainment use only, 18+.'
image: https://degenhedge.com/og-image.png
json_schemas:
- name: BtcWindow
  property_count: 23
  slug: degenhedge-com-btc-window
- name: FeeQuote
  property_count: 16
  slug: degenhedge-com-fee-quote
- name: Record
  property_count: 21
  slug: degenhedge-com-record
jsonld:
- class_count: 4
  name: Degenhedge Com Context
  property_count: 61
  slug: degenhedge-com-context
layout: provider
mcp_servers:
- description: 'Official remote Model Context Protocol server from DegenHedge exposing the same three read-only reads as its public data API (live Kalshi KXBTC15M window, graded alert record, Kalshi fee calculator). '
  name: DegenHedge Kalshi BTC MCP Server
  slug: degenhedge-kalshi-btc-mcp-server
modified: '2026-11-05'
name: DegenHedge
nav: Providers
network: true
overview: 'DegenHedge publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Fees API, market data API, and Record API. Tagged areas include Company, Prediction Markets, Kalshi, Bitcoin, and Trading Signals.


  The DegenHedge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DegenHedge''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 29 more developer resources.'
plans:
- name: Degenhedge Com Plans Pricing
  plan_count: 2
  slug: degenhedge-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Degenhedge Com Rate Limits
  slug: degenhedge-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: DegenHedge API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: degenhedge-com-rules
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 75.8
    catalog_earned_first_party: 16.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 59.5
    developer_ergonomics: 49.4
    discoverability: 71.7
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Degenhedge Com Authentication
  slug: degenhedge-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Degenhedge Com Domain Security
  slug: degenhedge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: check-kalshi-btc-window
  slug: degenhedge-com-check-btc-window
- name: review-degenhedge-graded-record
  slug: degenhedge-com-review-graded-record
slug: degenhedge-com
tags:
- Company
- Prediction Markets
- Kalshi
- Bitcoin
- Trading Signals
- Telegram
- Sports Betting
- MCP
- Market Data
website: https://degenhedge.com/
---
