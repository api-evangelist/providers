---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 67.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Arena Predictions Com Agentic Access
  operation_count: 37
  slug: arena-predictions-com-agentic-access
  summary_line: 37 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: 'Create, list, rotate and revoke keys, at the same path Kalshi uses. A person''s session only (the website, or a signed-in CLI''s session token): a key can never mint, rotate or revoke a key.'
  name: Arena API keys API
  slug: arena-predictions-com-api-keys-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: Whose account a key acts for, which organizations it belongs to, and what it may do.
  name: Arena Identity API
  slug: arena-predictions-com-identity-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: Arena's instruments and games, venue quotes, POST /backtest (a paper game-winner replay), and GET /history* (Fly price history). Scope markets:read. Venue references, prices and history only while the
  name: Arena Markets API
  slug: arena-predictions-com-markets-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: The key owner's own paper account, positions, orders and trades. Scope portfolio:read. Send X-Arena-Org to read an organization sandbox instead. Arena-owned data only while the venue-data switch is of
  name: Arena Portfolio API
  slug: arena-predictions-com-portfolio-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: 'Arena''s public records: the leaderboards, trader records with their resets, and settled picks. Scope records:read. Arena-owned data only: no exchange tickers, market titles, entry prices or live price'
  name: Arena Records API
  slug: arena-predictions-com-records-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: Is the API up.
  name: Arena Status API
  slug: arena-predictions-com-status-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: Place and cancel paper orders for the key owner. Scope trade:write, which a key carries only when its creator asked for it. Send X-Arena-Org to trade that organization's paper sandbox. Paper is the de
  name: Arena Trading API
  slug: arena-predictions-com-trading-api
- baseURL: https://arena-predictions.com/api/v1
  baseurl_source: declared
  description: Where the key's account stands against its plan. Any valid key; never counted.
  name: Arena Usage API
  slug: arena-predictions-com-usage-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/arena-predictions-com/agentic-access/arena-predictions-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arena-predictions-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/arena-predictions-com/rules/arena-predictions-com-rules.yml
  title: ''
  type: Spectral
  url: rules/arena-predictions-com-rules.yml
- group: design
  href: https://artifacts.apis.io/arena-predictions-com/json-ld/arena-predictions-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arena-predictions-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/arena-predictions-com/vocabulary/arena-predictions-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arena-predictions-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arena-predictions-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arena-predictions-com/data-model/arena-predictions-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arena-predictions-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/arena-predictions-com/cli/arena-predictions-com-cli.yml
  title: ''
  type: CLI
  url: cli/arena-predictions-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/arena-predictions-com/authentication/arena-predictions-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arena-predictions-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/arena-predictions-com/errors/arena-predictions-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arena-predictions-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arena-predictions-com/conformance/arena-predictions-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arena-predictions-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arena-predictions-com/llms/arena-predictions-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arena-predictions-com-llms.txt
- group: other
  href: https://artifacts.apis.io/arena-predictions-com/a2a/arena-predictions-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/arena-predictions-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/arena-predictions-com/mcp/arena-predictions-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arena-predictions-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/arena-predictions-com/mcp/arena-predictions-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arena-predictions-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arena-predictions-com/well-known/arena-predictions-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arena-predictions-com-security.txt
- group: agent
  href: https://artifacts.apis.io/arena-predictions-com/well-known/arena-predictions-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arena-predictions-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arena-predictions-com/hosts/arena-predictions-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arena-predictions-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arena-predictions-com/vendors/arena-predictions-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arena-predictions-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/arena-predictions-com/packages/arena-predictions-com-packages.yml
  title: ''
  type: SDKs
  url: packages/arena-predictions-com-packages.yml
- group: build
  href: https://artifacts.apis.io/arena-predictions-com/packages/arena-predictions-com-packages.yml
  title: ''
  type: Packages
  url: packages/arena-predictions-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://arena-predictions.com/status
- group: auth
  title: ''
  type: Security
  url: https://arena-predictions.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://arena-predictions.com/business/sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: https://arena-predictions.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arena-predictions.com\
- group: auth
  href: https://artifacts.apis.io/arena-predictions-com/security/arena-predictions-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arena-predictions-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arena-predictions-com/security/arena-predictions-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arena-predictions-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arena-predictions.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arena-predictions.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arena-predictions.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arena-predictions.com/getting-started/first-request
- group: operate
  title: ''
  type: Support
  url: https://arena-predictions.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arena-predictions.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arena-predictions.com/privacy
created: '2026-11-01'
description: 'Test prediction-market strategies in Arena''s sandbox: live prices, paper fills and a graded track record, from the website, a CLI or an MCP server. Private accounts by default, public AI model records, a public leaderboard and large-order signals.'
image: https://arena-predictions.com/api/og/site?v=2
json_schemas:
- name: InstrumentBook
  property_count: 13
  slug: arena-predictions-com-instrument-book
- name: Me
  property_count: 5
  slug: arena-predictions-com-me
- name: OrderRequest
  property_count: 27
  slug: arena-predictions-com-order-request
- name: OrderResult
  property_count: 14
  slug: arena-predictions-com-order-result
- name: OwnerScoreboardResponse
  property_count: 16
  slug: arena-predictions-com-owner-scoreboard-response
- name: TrackRecordResponse
  property_count: 9
  slug: arena-predictions-com-track-record-response
jsonld:
- class_count: 59
  name: Arena Predictions Com Context
  property_count: 284
  slug: arena-predictions-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at arena-predictions.com.
  name: Arena MCP Server
  slug: arena-predictions-com-mcp-yml
modified: '2026-11-01'
name: Arena
nav: Providers
network: true
overview: 'Arena publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including API keys API, Identity API, Markets API, and 5 more. Tagged areas include Prediction Markets, Paper Trading, Sandbox, and CLI.


  The Arena catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arena''s developer surface includes CLI, authentication, sandbox, changelog, documentation, API reference, getting-started guide, and 27 more developer resources.'
plans:
- name: Arena Predictions Com Plans Pricing
  plan_count: 0
  slug: arena-predictions-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Arena Predictions Com Rate Limits
  slug: arena-predictions-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 119
  extends:
  - spectral:oas
  name: Arena API Rules
  rule_count: 78
  severity_counts:
    error: 62
    hint: 0
    info: 5
    warn: 11
  slug: arena-predictions-com-rules
scopes:
- name: Arena Predictions Com Scopes
  scope_count: 0
  slug: arena-predictions-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 66.3
    developer_ergonomics: 57.6
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arena Predictions Com Authentication
  slug: arena-predictions-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Arena Predictions Com Domain Security
  slug: arena-predictions-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Arena Predictions Com Vulnerability Disclosure
  slug: arena-predictions-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: get-balance
  slug: arena-predictions-com-get-balance
- name: get-leaderboard
  slug: arena-predictions-com-get-leaderboard
- name: get-trader
  slug: arena-predictions-com-get-trader
- name: place-trade
  slug: arena-predictions-com-place-trade
slug: arena-predictions-com
tags:
- Prediction Markets
- Paper Trading
- Sandbox
- CLI
website: https://arena-predictions.com/
---
