---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 75.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: 0Xinsider Com Agentic Access
  operation_count: 94
  slug: 0xinsider-com-agentic-access
  summary_line: 94 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Identify the account and credential authenticated for a paid API request.
  name: 0xinsider Account API
  slug: 0xinsider-com-account-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Polymarket multi-leg combo fills, details, and live counts.
  name: 0xinsider Combos API
  slug: 0xinsider-com-combos-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Search across 0xinsider editorial content.
  name: 0xinsider Content API
  slug: 0xinsider-com-content-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Durable public event replay streams.
  name: 0xinsider Events API
  slug: 0xinsider-com-events-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: 'Sports and esports games: both sides, schedules, provider status and the Polymarket markets linked to each game.'
  name: 0xinsider Games API
  slug: 0xinsider-com-games-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Deprecated spelling of Suspicious trades; both operations stay live as aliases until their 2027-02-01 sunset (#29351).
  name: 0xinsider Insider Radar API
  slug: 0xinsider-com-insider-radar-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Largest current open positions from graded traders (Polymarket-only).
  name: 0xinsider Large Positions API
  slug: 0xinsider-com-large-positions-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Recent and historical large trades.
  name: 0xinsider Large trades API
  slug: 0xinsider-com-large-trades-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Ranked trader discovery and category/strategy leaderboards.
  name: 0xinsider Leaderboard API
  slug: 0xinsider-com-leaderboard-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Market search, discovery, snapshots, and sharp-money flow.
  name: 0xinsider Markets API
  slug: 0xinsider-com-markets-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Remote Model Context Protocol transport.
  name: 0xinsider MCP API
  slug: 0xinsider-com-mcp-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: 'Self-serve agent registration: a sandbox key with no account, and the path to live access.'
  name: 0xinsider Onboarding API
  slug: 0xinsider-com-onboarding-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: 'One sourced sharp-money call a day: the side profitable wallets are backing, with pre-game odds, the holders, and the track record.'
  name: 0xinsider Pick of the Day API
  slug: 0xinsider-com-pick-of-the-day-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Current prediction-market position snapshots from backend-owned mirrors.
  name: 0xinsider Positions API
  slug: 0xinsider-com-positions-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Daily, weekly, monthly, and trader export report snapshots.
  name: 0xinsider Reports API
  slug: 0xinsider-com-reports-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Resumable real-time Server-Sent Events stream of live feed envelopes.
  name: 0xinsider Streaming API
  slug: 0xinsider-com-streaming-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Trades whose recorded suspicion score meets the live flag threshold.
  name: 0xinsider Suspicious trades API
  slug: 0xinsider-com-suspicious-trades-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Health and operational status checks.
  name: 0xinsider System API
  slug: 0xinsider-com-system-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Traders, batch lookups, timelines, and export readiness.
  name: 0xinsider Traders API
  slug: 0xinsider-com-traders-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Developer API budget and usage introspection.
  name: 0xinsider Usage API
  slug: 0xinsider-com-usage-api
- baseURL: https://api.0xinsider.com
  baseurl_source: declared
  description: Signed builder webhook destinations and delivery controls.
  name: 0xinsider Webhooks API
  slug: 0xinsider-com-webhooks-api
artifact_total: 39
asyncapis:
- description: ''
  name: 0Xinsider Com Webhooks
  slug: 0xinsider-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/0xinsider-com/agentic-access/0xinsider-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/0xinsider-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/0xinsider-com/rate-limits/0xinsider-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/0xinsider-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/0xinsider-com/plans/0xinsider-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/0xinsider-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/rules/0xinsider-com-rules.yml
  title: ''
  type: Spectral
  url: rules/0xinsider-com-rules.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/json-ld/0xinsider-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/0xinsider-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/0xinsider-com/vocabulary/0xinsider-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0xinsider-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/0xinsider-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/asyncapi/0xinsider-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/0xinsider-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/data-model/0xinsider-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/0xinsider-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/0xinsider-com/cli/0xinsider-com-cli.yml
  title: ''
  type: CLI
  url: cli/0xinsider-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/0xinsider-com/changelog/0xinsider-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/0xinsider-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/conventions/0xinsider-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/0xinsider-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/conventions/0xinsider-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/0xinsider-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/0xinsider-com/sandbox/0xinsider-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/0xinsider-com-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://0xinsider.com/security
- group: auth
  href: https://artifacts.apis.io/0xinsider-com/authentication/0xinsider-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/0xinsider-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/0xinsider-com/scopes/0xinsider-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/0xinsider-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/errors/0xinsider-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/0xinsider-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/0xinsider-com/conformance/0xinsider-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0xinsider-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/0xinsider-com/llms/0xinsider-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0xinsider-com-llms.txt
- group: other
  href: https://artifacts.apis.io/0xinsider-com/a2a/0xinsider-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/0xinsider-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/0xinsider-com/mcp/0xinsider-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/0xinsider-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/0xinsider-com/mcp/0xinsider-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/0xinsider-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/0xinsider-com/well-known/0xinsider-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/0xinsider-com-security.txt
- group: agent
  href: https://artifacts.apis.io/0xinsider-com/well-known/0xinsider-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/0xinsider-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/0xinsider-com/hosts/0xinsider-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0xinsider-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/0xinsider-com/vendors/0xinsider-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0xinsider-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/0xinsider-com/packages/0xinsider-com-packages.yml
  title: ''
  type: SDKs
  url: packages/0xinsider-com-packages.yml
- group: build
  href: https://artifacts.apis.io/0xinsider-com/packages/0xinsider-com-packages.yml
  title: ''
  type: Packages
  url: packages/0xinsider-com-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://0xinsider.com/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0xinsider.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xinsider
- group: start
  title: ''
  type: SignUp
  url: https://api.0xinsider.com/api/v1/agents/register
- group: commercial
  title: ''
  type: Pricing
  url: https://0xinsider.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.yourapp.com/webhooks/0xinsider
- group: auth
  href: https://artifacts.apis.io/0xinsider-com/security/0xinsider-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/0xinsider-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/0xinsider-com/security/0xinsider-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0xinsider-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0xinsider.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.0xinsider.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.0xinsider.com/api-reference/introduction.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.0xinsider.com/quickstart.md
created: '2026-10-31'
description: 0xinsider provides Polymarket sports and esports analytics via a public API. It offers wallet grades, market activity, daily picks, large trade data, and statistical insights across major US leagues and esports. The platform delivers real‑time data, performance metrics, and a sandbox for developers to explore without an API key.
image: https://0xinsider.com/opengraph-image
json_schemas:
- name: MarketSnapshot
  property_count: 6
  slug: 0xinsider-com-market-snapshot
- name: PickOfTheDay
  property_count: 64
  slug: 0xinsider-com-pick-of-the-day
- name: TraderContext
  property_count: 4
  slug: 0xinsider-com-trader-context
- name: TraderExportJob
  property_count: 3
  slug: 0xinsider-com-trader-export-job
- name: TraderPnl
  property_count: 10
  slug: 0xinsider-com-trader-pnl
- name: Trader
  property_count: 21
  slug: 0xinsider-com-trader
jsonld:
- class_count: 120
  name: 0Xinsider Com Context
  property_count: 533
  slug: 0xinsider-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.0xinsider.com requiring an API key.
  name: 0xinsider MCP Server
  slug: 0xinsider-com-mcp-yml
modified: '2026-10-31'
name: 0xinsider
nav: Providers
network: true
overview: '0xinsider publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Combos API, Content API, and 18 more. Tagged areas include Sports, Esports, Analytics, and Finance.


  The 0xinsider catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  0xinsider''s developer surface includes CLI, changelog, sandbox, authentication, signup flow, pricing, documentation, and 34 more developer resources.'
plans:
- name: 0Xinsider Com Plans Pricing
  plan_count: 3
  slug: 0xinsider-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: 0Xinsider Com Rate Limits
  slug: 0xinsider-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: 0xinsider API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: 0xinsider-com-rules
scopes:
- name: 0Xinsider Com Scopes
  scope_count: 4
  slug: 0xinsider-com-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 75.0
    developer_ergonomics: 55.2
    discoverability: 56.7
    operational_transparency: 63.2
  previous_composite: 70.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 0Xinsider Com Authentication
  slug: 0xinsider-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 0Xinsider Com Domain Security
  slug: 0xinsider-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 0Xinsider Com Vulnerability Disclosure
  slug: 0xinsider-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: 0xinsider-com-api-access
  slug: 0xinsider-com-api-access
slug: 0xinsider-com
tags:
- Sports
- Esports
- Analytics
- Finance
website: https://0xinsider.com/
---
