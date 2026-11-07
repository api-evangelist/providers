---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Datascoop Io Agentic Access
  operation_count: 24
  slug: datascoop-io-agentic-access
  summary_line: 24 operations · 5 acting
api_count: 1
apis:
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The Australia API from DataScoop — 1 operation(s) for australia.
  name: DataScoop Australia API
  slug: datascoop-io-australia-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The Datasets API from DataScoop — 4 operation(s) for datasets.
  name: DataScoop Datasets API
  slug: datascoop-io-datasets-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The Me API from DataScoop — 1 operation(s) for me.
  name: DataScoop Me API
  slug: datascoop-io-me-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The Pricing API from DataScoop — 1 operation(s) for pricing.
  name: DataScoop Pricing API
  slug: datascoop-io-pricing-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The Saved care territories API from DataScoop — 4 operation(s) for saved care territories.
  name: DataScoop Saved care territories API
  slug: datascoop-io-saved-care-territories-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The Signup API from DataScoop — 1 operation(s) for signup.
  name: DataScoop Signup API
  slug: datascoop-io-signup-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The United Kingdom API from DataScoop — 5 operation(s) for united kingdom.
  name: DataScoop United Kingdom API
  slug: datascoop-io-united-kingdom-api
- baseURL: https://datascoop.io
  baseurl_source: declared
  description: The United States API from DataScoop — 5 operation(s) for united states.
  name: DataScoop United States API
  slug: datascoop-io-united-states-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/datascoop-io/agentic-access/datascoop-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datascoop-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/datascoop-io/rate-limits/datascoop-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datascoop-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/datascoop-io/plans/datascoop-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datascoop-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datascoop-io/rules/datascoop-io-rules.yml
  title: ''
  type: Spectral
  url: rules/datascoop-io-rules.yml
- group: design
  href: https://artifacts.apis.io/datascoop-io/json-ld/datascoop-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datascoop-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/datascoop-io/vocabulary/datascoop-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datascoop-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/datascoop-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/datascoop-io/data-model/datascoop-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datascoop-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datascoop-io/authentication/datascoop-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datascoop-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/datascoop-io/errors/datascoop-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datascoop-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datascoop-io/conformance/datascoop-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datascoop-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datascoop-io/llms/datascoop-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datascoop-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/datascoop-io/mcp/datascoop-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datascoop-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/datascoop-io/hosts/datascoop-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datascoop-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datascoop.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datascoop.io/privacy
- group: start
  title: ''
  type: Login
  url: https://datascoop.io/login
- group: auth
  href: https://artifacts.apis.io/datascoop-io/security/datascoop-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datascoop-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datascoop.io/
- group: docs
  title: ''
  type: Documentation
  url: https://datascoop.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://datascoop.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://datascoop.io/about
created: '2026-11-05'
description: DataScoop provides public records as downloadable spreadsheets, APIs, and AI‑agent tools. It aggregates official datasets, offers open licences, attribution, and visible import dates, enabling developers and AI agents to access structured public data easily. The platform includes a catalog of datasets across various sectors, pricing plans, and documentation for integration.
image: https://datascoop.io/assets/og-image.png
json_schemas:
- name: Dataset
  property_count: 8
  slug: datascoop-io-dataset
- name: QueryResult
  property_count: 15
  slug: datascoop-io-query-result
jsonld:
- class_count: 3
  name: Datascoop Io Context
  property_count: 24
  slug: datascoop-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at datascoop.io.
  name: DataScoop MCP Server
  slug: datascoop-io-mcp-yml
modified: '2026-11-05'
name: DataScoop
nav: Providers
network: true
overview: 'DataScoop publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Australia API, Datasets API, Me API, and 5 more. Tagged areas include Data, Public Records, AI Agents, and Datasets.


  The DataScoop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DataScoop''s developer surface includes authentication, documentation, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Datascoop Io Plans Pricing
  plan_count: 3
  slug: datascoop-io-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Datascoop Io Rate Limits
  slug: datascoop-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: DataScoop API Rules
  rule_count: 59
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 10
  slug: datascoop-io-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 20.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 60.5
    developer_ergonomics: 35.1
    discoverability: 56.7
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datascoop Io Authentication
  slug: datascoop-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datascoop Io Domain Security
  slug: datascoop-io-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: datascoop-io-fetch-dataset
  slug: datascoop-io-fetch-dataset
- name: datascoop-io-manage-care-territories
  slug: datascoop-io-manage-care-territories
slug: datascoop-io
tags:
- Data
- Public Records
- AI Agents
- Datasets
website: https://datascoop.io/
---
