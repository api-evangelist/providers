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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Algoum De Agentic Access
  operation_count: 54
  slug: algoum-de-agentic-access
  summary_line: 54 operations
api_count: 1
apis:
- baseURL: https://api.algoum.de/v1
  baseurl_source: declared
  description: Ticker/CIK resolution and company search, the raw SEC filing behind every record, and the freshness of each data source.
  name: algoum-de Common API
  slug: algoum-de-common-api
- baseURL: https://api.algoum.de/v1
  baseurl_source: declared
  description: Material events a company has to disclose – leadership changes, mergers, bankruptcies, cyber incidents and more. Available as searchable history, as a cross-market feed and as a push stream.
  name: algoum-de Events API
  slug: algoum-de-events-api
- baseURL: https://api.algoum.de/v1
  baseurl_source: declared
  description: Buys and sells reported by officers, directors and 10% owners, plus the signals derived from them (cluster buys, buy/sell ratio). Source are the SEC forms 4 and 5, which reach the API within minutes o
  name: algoum-de Insider API
  slug: algoum-de-insider-api
- baseURL: https://api.algoum.de/v1
  baseurl_source: declared
  description: Quarterly portfolios of institutional investors and the aggregated picture per stock. 13F filings are due 45 days after quarter end, so the most recent quarter fills up over several weeks.
  name: algoum-de Institutional API
  slug: algoum-de-institutional-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/algoum-de/agentic-access/algoum-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/algoum-de-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/algoum-de/rate-limits/algoum-de-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/algoum-de-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/algoum-de/rules/algoum-de-rules.yml
  title: ''
  type: Spectral
  url: rules/algoum-de-rules.yml
- group: design
  href: https://artifacts.apis.io/algoum-de/json-ld/algoum-de-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/algoum-de-context.jsonld
- group: design
  href: https://artifacts.apis.io/algoum-de/vocabulary/algoum-de-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/algoum-de-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/algoum-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/algoum-de/data-model/algoum-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algoum-de-data-model.yml
- group: design
  href: https://artifacts.apis.io/algoum-de/conventions/algoum-de-conventions.yml
  title: ''
  type: Conventions
  url: conventions/algoum-de-conventions.yml
- group: auth
  href: https://artifacts.apis.io/algoum-de/authentication/algoum-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algoum-de-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.algoum.de/v1/status
- group: design
  href: https://artifacts.apis.io/algoum-de/lifecycle/algoum-de-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/algoum-de-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/algoum-de/errors/algoum-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algoum-de-problem-types.yml
- group: design
  href: https://artifacts.apis.io/algoum-de/conformance/algoum-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algoum-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/algoum-de/mcp/algoum-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algoum-de-mcp.yml
- group: other
  href: https://artifacts.apis.io/algoum-de/hosts/algoum-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algoum-de-hosts.yml
- group: auth
  href: https://artifacts.apis.io/algoum-de/security/algoum-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algoum-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algoum.de/
- group: docs
  title: ''
  type: APIReference
  url: https://algoum.de/docs
- group: docs
  title: ''
  type: Documentation
  url: https://algoum.de/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://algoum.de/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://algoum.de/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algoum.de/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algoum.de/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://algoum.de/signup
- group: start
  title: ''
  type: Login
  url: https://algoum.de/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fi4all
created: '2026-10-30'
description: algoum provides a SEC EDGAR API delivering insider trades, 8‑K filings and 13F data in clear, plain‑language JSON. It transforms official company disclosures into easy‑to‑read updates for investors and algorithmic traders, offering free access, no ads, and optional API keys for higher‑volume use. The service includes real‑time streaming, MCP integration, and comprehensive documentation, aiming to make financial filings transparent and actionable.
image: https://algoum.de/favicon.svg
json_schemas:
- name: ClusterBuy
  property_count: 15
  slug: algoum-de-cluster-buy
- name: Disclosure
  property_count: 7
  slug: algoum-de-disclosure
- name: Event
  property_count: 9
  slug: algoum-de-event
- name: Holding
  property_count: 11
  slug: algoum-de-holding
- name: InsiderTransaction
  property_count: 20
  slug: algoum-de-insider-transaction
- name: InstitutionalSentiment
  property_count: 11
  slug: algoum-de-institutional-sentiment
jsonld:
- class_count: 19
  name: Algoum De Context
  property_count: 71
  slug: algoum-de-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.algoum.de requiring an API key.
  name: algoum-de MCP Server
  slug: algoum-de-mcp-yml
modified: '2026-10-30'
name: algoum-de
nav: Providers
network: true
overview: 'algoum-de publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Common API, Events API, Insider API, and 1 more. Tagged areas include Company, Finance, SEC, and Insider Trading.


  The algoum-de catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  algoum-de''s developer surface includes authentication, API reference, documentation, getting-started guide, support, signup flow, and 20 more developer resources.'
plans:
- name: Algoum De Plans Pricing
  plan_count: 0
  slug: algoum-de-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Algoum De Rate Limits
  slug: algoum-de-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: algoum-de API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: algoum-de-rules
scopes:
- name: Algoum De Scopes
  scope_count: 0
  slug: algoum-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 66.7
    developer_ergonomics: 35.0
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/algoum-de/algoum-de-2026-11-03T120620.png
security:
- kind: authentication
  name: Algoum De Authentication
  slug: algoum-de-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Algoum De Domain Security
  slug: algoum-de-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-recent-insider-transactions
  slug: algoum-de-get-recent-insider-transactions
slug: algoum-de
tags:
- Company
- Finance
- SEC
- Insider Trading
website: https://algoum.de/
---
