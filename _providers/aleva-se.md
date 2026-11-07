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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aleva Se Agentic Access
  operation_count: 50
  slug: aleva-se-agentic-access
  summary_line: 50 operations
api_count: 2
apis:
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Aviation API from Aleva — 2 operation(s) for aviation.
  name: Aleva Aviation API
  slug: aleva-se-aviation-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Courts API from Aleva — 2 operation(s) for courts.
  name: Aleva Courts API
  slug: aleva-se-courts-api
- baseURL: https://dev-api.aleva.se
  baseurl_source: declared
  description: The Domains API from Aleva — 5 operation(s) for domains.
  name: Aleva Domains API
  slug: aleva-se-domains-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Economy API from Aleva — 2 operation(s) for economy.
  name: Aleva Economy API
  slug: aleva-se-economy-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Energy API from Aleva — 2 operation(s) for energy.
  name: Aleva Energy API
  slug: aleva-se-energy-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Foods API from Aleva — 1 operation(s) for foods.
  name: Aleva Foods API
  slug: aleva-se-foods-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Jobs API from Aleva — 2 operation(s) for jobs.
  name: Aleva Jobs API
  slug: aleva-se-jobs-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Medicines API from Aleva — 3 operation(s) for medicines.
  name: Aleva Medicines API
  slug: aleva-se-medicines-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Municipalities API from Aleva — 2 operation(s) for municipalities.
  name: Aleva Municipalities API
  slug: aleva-se-municipalities-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Rates API from Aleva — 2 operation(s) for rates.
  name: Aleva Rates API
  slug: aleva-se-rates-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Riksdag API from Aleva — 2 operation(s) for riksdag.
  name: Aleva Riksdag API
  slug: aleva-se-riksdag-api
- baseURL: https://dev-api.aleva.se
  baseurl_source: declared
  description: The Stats API from Aleva — 2 operation(s) for stats.
  name: Aleva Stats API
  slug: aleva-se-stats-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Sweden API from Aleva — 4 operation(s) for sweden.
  name: Aleva Sweden API
  slug: aleva-se-sweden-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Tourism API from Aleva — 3 operation(s) for tourism.
  name: Aleva Tourism API
  slug: aleva-se-tourism-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Trains API from Aleva — 2 operation(s) for trains.
  name: Aleva Trains API
  slug: aleva-se-trains-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Weather API from Aleva — 2 operation(s) for weather.
  name: Aleva Weather API
  slug: aleva-se-weather-api
- baseURL: https://api.aleva.se
  baseurl_source: declared
  description: The Web API from Aleva — 7 operation(s) for web.
  name: Aleva Web API
  slug: aleva-se-web-api
artifact_total: 28
common:
- group: docs
  title: ''
  type: APIReference
  url: https://api.aleva.se/v1/web/apis
- group: agent
  href: https://artifacts.apis.io/aleva-se/agentic-access/aleva-se-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aleva-se-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/aleva-se/rate-limits/aleva-se-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aleva-se-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/aleva-se/rules/aleva-se-rules.yml
  title: ''
  type: Spectral
  url: rules/aleva-se-rules.yml
- group: design
  href: https://artifacts.apis.io/aleva-se/json-ld/aleva-se-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aleva-se-context.jsonld
- group: design
  href: https://artifacts.apis.io/aleva-se/vocabulary/aleva-se-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aleva-se-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aleva-se/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aleva-se/data-model/aleva-se-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aleva-se-data-model.yml
- group: design
  href: https://artifacts.apis.io/aleva-se/conventions/aleva-se-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aleva-se-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aleva-se/authentication/aleva-se-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aleva-se-authentication.yml
- group: design
  href: https://artifacts.apis.io/aleva-se/errors/aleva-se-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aleva-se-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aleva-se/conformance/aleva-se-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aleva-se-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aleva-se/llms/aleva-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aleva-se-llms.txt
- group: build
  href: https://artifacts.apis.io/aleva-se/mcp/aleva-se-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aleva-se-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aleva-se/mcp/aleva-se-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aleva-se-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aleva-se/well-known/aleva-se-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aleva-se-security.txt
- group: auth
  href: https://artifacts.apis.io/aleva-se/well-known/aleva-se-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aleva-se-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/aleva-se/well-known/aleva-se-dev-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aleva-se-dev-api-security.txt
- group: auth
  href: https://artifacts.apis.io/aleva-se/well-known/aleva-se-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aleva-se-api-security.txt
- group: agent
  href: https://artifacts.apis.io/aleva-se/well-known/aleva-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aleva-se-well-known.yml
- group: other
  href: https://artifacts.apis.io/aleva-se/hosts/aleva-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aleva-se-hosts.yml
- group: other
  href: https://artifacts.apis.io/aleva-se/vendors/aleva-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aleva-se-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://aleva.se/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aleva.se/en/privacy
- group: auth
  href: https://artifacts.apis.io/aleva-se/security/aleva-se-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aleva-se-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aleva-se/security/aleva-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aleva-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aleva.se/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aleva.se/docs
- group: docs
  title: ''
  type: Documentation
  url: https://aleva.se/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://aleva.se/docs#start
- group: operate
  title: ''
  type: Support
  url: https://aleva.se/#form
created: '2026-11-01'
description: Aleva provides Swedish data infrastructure for AI agents, offering open data APIs that connect APIs, files and other data sources, making them available as API and MCP servers. Their platform serves datasets from .se and .nu domains, weather from SMHI, statistics from SCB and Kolada, discontinued medicines, interest rates from the Riksbank, parliamentary votes, and more. All infrastructure runs in Sweden, ensuring data residency. They plan to open limited access to companies after 2027, with interest registration via email or SMS.
image: https://aleva.se/favicon.svg
json_schemas:
- name: Meta
  property_count: 9
  slug: aleva-se-meta
jsonld:
- class_count: 2
  name: Aleva Se Context
  property_count: 10
  slug: aleva-se-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aleva.se.
  name: Aleva MCP Server
  slug: aleva-se-mcp-yml
modified: '2026-11-01'
name: Aleva
nav: Providers
network: true
overview: 'Aleva publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aviation API, Courts API, Domains API, and 14 more. Tagged areas include Swedish, Data Infrastructure, Artificial Intelligence, Open Data, and Government Data.


  The Aleva catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aleva''s developer surface includes API reference, authentication, documentation, getting-started guide, support, and 26 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 2
  name: Aleva Se Rate Limits
  slug: aleva-se-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Aleva API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: aleva-se-rules
scopes:
- name: Aleva Se Scopes
  scope_count: 0
  slug: aleva-se-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.2
    catalog_earned_first_party: 8.0
    catalog_gap: 50.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 56.9
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 26.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aleva Se Authentication
  slug: aleva-se-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aleva Se Domain Security
  slug: aleva-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aleva Se Vulnerability Disclosure
  slug: aleva-se-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-data
  slug: aleva-se-get-data
slug: aleva-se
tags:
- Swedish
- Data Infrastructure
- Artificial Intelligence
- Open Data
- Government Data
website: https://aleva.se/
---
