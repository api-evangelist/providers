---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tickdb Ai Agentic Access
  operation_count: 46
  slug: tickdb-ai-agentic-access
  summary_line: 46 operations
api_count: 1
apis:
- description: Real-time market data API for stocks, forex, metals, indices, China/HK futures, and crypto.
  name: TickDB Market Data API
  slug: tickdb-market-data-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The account API from tickdb-ai — 1 operation(s) for account.
  name: tickdb-ai Account API
  slug: tickdb-ai-account-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The fundamentals-capital-actions API from tickdb-ai — 4 operation(s) for fundamentals-capital-actions.
  name: tickdb-ai Fundamentals Capital Actions API
  slug: tickdb-ai-fundamentals-capital-actions-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The fundamentals-company API from tickdb-ai — 2 operation(s) for fundamentals-company.
  name: tickdb-ai Fundamentals Company API
  slug: tickdb-ai-fundamentals-company-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The fundamentals-events API from tickdb-ai — 8 operation(s) for fundamentals-events.
  name: tickdb-ai Fundamentals Events API
  slug: tickdb-ai-fundamentals-events-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The fundamentals-financials API from tickdb-ai — 5 operation(s) for fundamentals-financials.
  name: tickdb-ai Fundamentals Financials API
  slug: tickdb-ai-fundamentals-financials-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The fundamentals-holders API from tickdb-ai — 4 operation(s) for fundamentals-holders.
  name: tickdb-ai Fundamentals Holders API
  slug: tickdb-ai-fundamentals-holders-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The fundamentals-valuation-industry API from tickdb-ai — 6 operation(s) for fundamentals-valuation-industry.
  name: tickdb-ai Fundamentals Valuation Industry API
  slug: tickdb-ai-fundamentals-valuation-industry-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The Market API from tickdb-ai — 15 operation(s) for market.
  name: tickdb-ai Market API
  slug: tickdb-ai-market-api
- baseURL: https://api.tickdb.ai
  baseurl_source: declared
  description: The Symbols API from tickdb-ai — 1 operation(s) for symbols.
  name: tickdb-ai Symbols API
  slug: tickdb-ai-symbols-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/tickdb-ai/agentic-access/tickdb-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tickdb-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tickdb-ai/rate-limits/tickdb-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tickdb-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tickdb-ai/rules/tickdb-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/tickdb-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/tickdb-ai/json-ld/tickdb-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tickdb-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/tickdb-ai/vocabulary/tickdb-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tickdb-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tickdb-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tickdb-ai/data-model/tickdb-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tickdb-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/tickdb-ai/cli/tickdb-ai-cli.yml
  title: ''
  type: CLI
  url: cli/tickdb-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/tickdb-ai/changelog/tickdb-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tickdb-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/tickdb-ai/conventions/tickdb-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tickdb-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tickdb.ai/security
- group: auth
  href: https://artifacts.apis.io/tickdb-ai/authentication/tickdb-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tickdb-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/tickdb-ai/errors/tickdb-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tickdb-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tickdb-ai/conformance/tickdb-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tickdb-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tickdb-ai/llms/tickdb-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tickdb-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/tickdb-ai/a2a/tickdb-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tickdb-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/tickdb-ai/mcp/tickdb-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tickdb-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tickdb-ai/mcp/tickdb-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tickdb-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tickdb-ai/well-known/tickdb-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tickdb-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/tickdb-ai/hosts/tickdb-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tickdb-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tickdb-ai/vendors/tickdb-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tickdb-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/tickdb-ai/packages/tickdb-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/tickdb-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/tickdb-ai/packages/tickdb-ai-packages.yml
  title: ''
  type: Packages
  url: packages/tickdb-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/tickdb-ai/security/tickdb-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tickdb-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tickdb-ai/security/tickdb-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tickdb-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tickdb.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tickdb.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tickdb.ai/zh-Hans/index
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tickdb.ai/zh-Hans/quick-start
- group: company
  title: ''
  type: Blog
  url: https://blog.tickdb.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TickDB/tickdb-unified-realtime-marketdata-api
- group: start
  title: ''
  type: Login
  url: https://tickdb.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://tickdb.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tickdb.ai/privacy
- group: auth
  title: ''
  type: Security
  url: https://tickdb.ai/security
- group: operate
  title: ''
  type: Support
  url: https://tickdb.ai/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tickdb.ai/terms
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tickdb.ai/zh-Hans/release-notes
created: '2026-10-31'
description: TickDB provides real-time market data via REST and WebSocket APIs for stocks, forex, metals, indices, China and Hong Kong futures, and crypto. The platform offers comprehensive documentation, pricing plans, and developer resources, including a quick‑start guide, API reference, changelog, and support channels. Users can access data through the production API at https://api.tickdb.ai and explore detailed specs in OpenAPI and AsyncAPI formats. TickDB emphasizes security with a dedicated security page and privacy policy, and maintains an active blog and GitHub repository for community engagement.
image: https://tickdb.ai/logo.svg
json_schemas:
- name: FullMarketTickerResponse
  property_count: 3
  slug: tickdb-ai-full-market-ticker-response
- name: SuccessEnvelope
  property_count: 1
  slug: tickdb-ai-success-envelope
jsonld:
- class_count: 58
  name: Tickdb Ai Context
  property_count: 200
  slug: tickdb-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.tickdb.ai.
  name: tickdb-ai MCP Server
  slug: tickdb-ai-mcp-yml
modified: '2026-10-31'
name: tickdb-ai
nav: Providers
network: true
overview: 'tickdb-ai publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Fundamentals Capital Actions API, Fundamentals Company API, and 7 more. Tagged areas include Company, Finance, Market Data, and Real-Time.


  The tickdb-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tickdb-ai''s developer surface includes CLI, changelog, authentication, API reference, documentation, getting-started guide, engineering blog, and 31 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 4
  name: Tickdb Ai Rate Limits
  slug: tickdb-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: tickdb-ai API Rules
  rule_count: 52
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 3
  slug: tickdb-ai-rules
scopes:
- name: Tickdb Ai Scopes
  scope_count: 0
  slug: tickdb-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 35
    catalog_earned: 66.2
    catalog_earned_first_party: 12.0
    catalog_gap: 48.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 58.8
    developer_ergonomics: 50.5
    discoverability: 56.7
    operational_transparency: 47.4
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 31.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tickdb-ai/tickdb-ai-2026-11-03T144718.png
security:
- kind: authentication
  name: Tickdb Ai Authentication
  slug: tickdb-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tickdb Ai Domain Security
  slug: tickdb-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tickdb Ai Trust Center
  slug: tickdb-ai-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 1
skills:
- name: get-api-key-status
  slug: tickdb-ai-get-api-key-status
slug: tickdb-ai
tags:
- Company
- Finance
- Market Data
- Real-Time
website: https://tickdb.ai/
---
