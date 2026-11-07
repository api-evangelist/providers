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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Aspern Org Agentic Access
  operation_count: 108
  slug: aspern-org-agentic-access
  summary_line: 108 operations · 16 acting
api_count: 1
apis:
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: Your balance, quota, plans and this document.
  name: ASPERN Account API
  slug: aspern-org-account-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: The Agents API from ASPERN — 8 operation(s) for agents.
  name: ASPERN Agents API
  slug: aspern-org-agents-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: Watches you arm, and the webhooks they fire.
  name: ASPERN Alerts API
  slug: aspern-org-alerts-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: Whether a sequence is intact, checkable without trusting us.
  name: ASPERN Attestation API
  slug: aspern-org-attestation-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: The Capital API from ASPERN — 3 operation(s) for capital.
  name: ASPERN Capital API
  slug: aspern-org-capital-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: The Commerce API from ASPERN — 3 operation(s) for commerce.
  name: ASPERN Commerce API
  slug: aspern-org-commerce-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: The Crowding API from ASPERN — 1 operation(s) for crowding.
  name: ASPERN Crowding API
  slug: aspern-org-crowding-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: Series over time. Every point is a measurement taken then, never a backfill of what we believe now.
  name: ASPERN History API
  slug: aspern-org-history-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: Commit to a decision before executing, reveal it afterwards, and let anyone check the two match.
  name: ASPERN Judgement API
  slug: aspern-org-judgement-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: The market around a position, crowding, correlation, who leads and who follows.
  name: ASPERN Market API
  slug: aspern-org-market-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: What we think of a strategy. Free, the argument is worth more to us published than sold.
  name: ASPERN Ratings API
  slug: aspern-org-ratings-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: What each vault and operator actually did, read from the chain rather than reported to us.
  name: ASPERN Record API
  slug: aspern-org-record-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: The Reference API from ASPERN — 3 operation(s) for reference.
  name: ASPERN Reference API
  slug: aspern-org-reference-api
- baseURL: https://aspern.org/api
  baseurl_source: declared
  description: 'What a shock costs you: look-through exposure, liquidation distance, forced selling.'
  name: ASPERN Risk API
  slug: aspern-org-risk-api
artifact_total: 29
asyncapis:
- description: ''
  name: Aspern Org Webhooks
  slug: aspern-org-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/aspern-org/agentic-access/aspern-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aspern-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aspern-org/rules/aspern-org-rules.yml
  title: ''
  type: Spectral
  url: rules/aspern-org-rules.yml
- group: design
  href: https://artifacts.apis.io/aspern-org/json-ld/aspern-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aspern-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/aspern-org/vocabulary/aspern-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aspern-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aspern-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aspern-org/asyncapi/aspern-org-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aspern-org-webhooks.yml
- group: design
  href: https://artifacts.apis.io/aspern-org/data-model/aspern-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aspern-org-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aspern-org/security/aspern-org-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aspern-org-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/aspern-org/errors/aspern-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aspern-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aspern-org/conformance/aspern-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aspern-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aspern-org/llms/aspern-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aspern-org-llms.txt
- group: other
  href: https://artifacts.apis.io/aspern-org/a2a/aspern-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aspern-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aspern-org/mcp/aspern-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aspern-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aspern-org/well-known/aspern-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aspern-org-security.txt
- group: agent
  href: https://artifacts.apis.io/aspern-org/well-known/aspern-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aspern-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/aspern-org/hosts/aspern-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspern-org-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aspern.org/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://aspern.org/changelog
- group: auth
  href: https://artifacts.apis.io/aspern-org/authentication/aspern-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aspern-org-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aspern-org/security/aspern-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aspern-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aspern-org/security/aspern-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspern-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aspern.org/
- group: docs
  title: ''
  type: APIReference
  url: https://aspern.org/api/v1/openapi.json
- group: docs
  title: ''
  type: Documentation
  url: https://aspern.org/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://aspern.org/overview
- group: operate
  title: ''
  type: Support
  url: https://aspern.org/support
- group: commercial
  title: ''
  type: Pricing
  url: https://aspern.org/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aspern.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aspern.org/privacy
- group: start
  title: ''
  type: SignUp
  url: https://aspern.org/signup
- group: start
  title: ''
  type: Login
  url: https://aspern.org/login
created: '2026-11-01'
description: ASPERN provides independent financial intelligence for autonomous capital, aggregating evidence about agent‑managed vaults, capital flows, crowding, liquidation stress, and survivorship across blockchain networks. The platform offers real‑time data on vault holdings, transaction volumes, and risk metrics, enabling agents and investors to assess exposure and make informed decisions.
image: https://aspern.org/opengraph-image?bb467bc75b05ae90
json_schemas:
- name: AgentProfile
  property_count: 3
  slug: aspern-org-agent-profile
- name: CounterpartyCheck
  property_count: 3
  slug: aspern-org-counterparty-check
- name: RevenueData
  property_count: 3
  slug: aspern-org-revenue-data
- name: RwaData
  property_count: 3
  slug: aspern-org-rwa-data
- name: ServiceData
  property_count: 3
  slug: aspern-org-service-data
- name: TradingData
  property_count: 3
  slug: aspern-org-trading-data
jsonld:
- class_count: 120
  name: Aspern Org Context
  property_count: 193
  slug: aspern-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at aspern.org.
  name: ASPERN MCP Server
  slug: aspern-org-mcp-yml
modified: '2026-11-01'
name: ASPERN
nav: Providers
network: true
overview: 'ASPERN publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Alerts API, and 11 more. Tagged areas include Finance, Blockchain, Artificial Intelligence, Data, and Intelligence.


  The ASPERN catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ASPERN''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, support, pricing, and 24 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: ASPERN API Rules
  rule_count: 62
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 12
  slug: aspern-org-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 71.8
    developer_ergonomics: 35.0
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aspern Org Authentication
  slug: aspern-org-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Aspern Org Domain Security
  slug: aspern-org-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aspern Org Vulnerability Disclosure
  slug: aspern-org-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: vaults
  slug: aspern-org-vaults
slug: aspern-org
tags:
- Finance
- Blockchain
- Artificial Intelligence
- Data
- Intelligence
website: https://aspern.org/
---
