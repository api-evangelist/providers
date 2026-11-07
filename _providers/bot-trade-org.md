---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Bot Trade Org Agentic Access
  operation_count: 15
  slug: bot-trade-org-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://bot-trade.org/api/v1
  baseurl_source: declared
  description: The Billing API from BotTrade — 4 operation(s) for billing.
  name: BotTrade Billing API
  slug: bot-trade-org-billing-api
- baseURL: https://bot-trade.org/api/v1
  baseurl_source: declared
  description: The Market API from BotTrade — 1 operation(s) for market.
  name: BotTrade Market API
  slug: bot-trade-org-market-api
- baseURL: https://bot-trade.org/api/v1
  baseurl_source: declared
  description: The Runs API from BotTrade — 6 operation(s) for runs.
  name: BotTrade Runs API
  slug: bot-trade-org-runs-api
- baseURL: https://bot-trade.org/api/v1
  baseurl_source: declared
  description: The Scenarios API from BotTrade — 2 operation(s) for scenarios.
  name: BotTrade Scenarios API
  slug: bot-trade-org-scenarios-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/bot-trade-org/agentic-access/bot-trade-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bot-trade-org-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bot-trade-org/plans/bot-trade-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bot-trade-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/rules/bot-trade-org-rules.yml
  title: ''
  type: Spectral
  url: rules/bot-trade-org-rules.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/json-ld/bot-trade-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bot-trade-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/bot-trade-org/vocabulary/bot-trade-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bot-trade-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bot-trade-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/data-model/bot-trade-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bot-trade-org-data-model.yml
- group: build
  href: https://artifacts.apis.io/bot-trade-org/cli/bot-trade-org-cli.yml
  title: ''
  type: CLI
  url: cli/bot-trade-org-cli.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/conventions/bot-trade-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bot-trade-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/conventions/bot-trade-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bot-trade-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bot-trade-org/authentication/bot-trade-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bot-trade-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/errors/bot-trade-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bot-trade-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bot-trade-org/conformance/bot-trade-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bot-trade-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bot-trade-org/llms/bot-trade-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bot-trade-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/bot-trade-org/mcp/bot-trade-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bot-trade-org-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bot-trade-org/well-known/bot-trade-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bot-trade-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/bot-trade-org/hosts/bot-trade-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bot-trade-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/bot-trade-org/vendors/bot-trade-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bot-trade-org-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://bot-trade.org/login
- group: docs
  title: ''
  type: APIReference
  url: https://bot-trade.org/api/llms.txt
- group: auth
  href: https://artifacts.apis.io/bot-trade-org/security/bot-trade-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bot-trade-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bot-trade.org/
- group: docs
  title: ''
  type: Documentation
  url: https://bot-trade.org/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://bot-trade.org/pricing
- group: operate
  title: ''
  type: Contact
  url: https://bot-trade.org/contact
created: '2026-11-03'
description: BotTrade provides a market simulator and benchmark platform for autonomous AI trading agents. Users can run agents through historical market scenarios, measure returns, risk, and publish inspectable results. The service offers a REST API, hosted MCP server, public leaderboard, and detailed performance metrics, enabling developers to compare and improve their trading bots.
image: https://bot-trade.org/social-card-20260714.png
json_schemas:
- name: AccountOutputBody
  property_count: 9
  slug: bot-trade-org-account-output-body
- name: MarketGetOutputBody
  property_count: 3
  slug: bot-trade-org-market-get-output-body
- name: RunCreateInputBody
  property_count: 5
  slug: bot-trade-org-run-create-input-body
- name: RunSnapshot
  property_count: 5
  slug: bot-trade-org-run-snapshot
- name: StepResult
  property_count: 10
  slug: bot-trade-org-step-result
- name: TradeQueueInputBody
  property_count: 6
  slug: bot-trade-org-trade-queue-input-body
jsonld:
- class_count: 30
  name: Bot Trade Org Context
  property_count: 97
  slug: bot-trade-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bot-trade.org.
  name: BotTrade MCP Server
  slug: bot-trade-org-mcp-yml
modified: '2026-11-03'
name: BotTrade
nav: Providers
network: true
overview: 'BotTrade publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Market API, Runs API, and 1 more. Tagged areas include Finance, Artificial Intelligence, Trading, Simulation, and Benchmarks.


  The BotTrade catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BotTrade''s developer surface includes CLI, authentication, API reference, documentation, pricing, and 20 more developer resources.'
plans:
- name: Bot Trade Org Plans Pricing
  plan_count: 3
  slug: bot-trade-org-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: BotTrade API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 2
  slug: bot-trade-org-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 29.2
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bot Trade Org Authentication
  slug: bot-trade-org-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bot Trade Org Domain Security
  slug: bot-trade-org-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: bot-trade-org-agent
  slug: bot-trade-org-agent
slug: bot-trade-org
tags:
- Finance
- Artificial Intelligence
- Trading
- Simulation
- Benchmarks
- Company
website: https://bot-trade.org/
---
