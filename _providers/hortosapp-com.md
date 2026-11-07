---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hortosapp Com Agentic Access
  operation_count: 2
  slug: hortosapp-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://au.hortosapp.com
  baseurl_source: declared
  description: The Quote API from hortosapp-com — 1 operation(s) for quote.
  name: hortosapp-com Quote API
  slug: hortosapp-com-quote-api
- baseURL: https://au.hortosapp.com
  baseurl_source: declared
  description: The Search API from hortosapp-com — 1 operation(s) for search.
  name: hortosapp-com Search API
  slug: hortosapp-com-search-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/hortosapp-com/agentic-access/hortosapp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hortosapp-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hortosapp-com/rules/hortosapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hortosapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hortosapp-com/json-ld/hortosapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hortosapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/hortosapp-com/vocabulary/hortosapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hortosapp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hortosapp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hortosapp-com/data-model/hortosapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hortosapp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/hortosapp-com/errors/hortosapp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hortosapp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hortosapp-com/conformance/hortosapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hortosapp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hortosapp-com/llms/hortosapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hortosapp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/hortosapp-com/mcp/hortosapp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hortosapp-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/hortosapp-com/hosts/hortosapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hortosapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hortosapp-com/vendors/hortosapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hortosapp-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://au.hortosapp.com/login
- group: auth
  href: https://artifacts.apis.io/hortosapp-com/security/hortosapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hortosapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hortosapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hortosapp.com/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://hortosapp.com/api/v1/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hortosapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hortosapp.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://hortosapp.com/for-growers
- group: start
  title: ''
  type: GettingStarted
  url: https://hortosapp.com/search?q=plant
created: '2026-10-29'
description: 'HortOS is the open trade directory and live availability market for nursery stock in Australia (au.hortosapp.com), the United States (us.hortosapp.com), New Zealand (nz.hortosapp.com), Canada (ca.hortosapp.com) and the United Kingdom (uk.hortosapp.com): growers, wholesale nurseries and trade yards, with the plants, sizes and trade prices they publish, and the HortOS Plant Price Index, the monthly statistical picture of what the trade charges.'
image: https://hortosapp.com/favicon.ico
json_schemas:
- name: Quote
  property_count: 7
  slug: hortosapp-com-quote
- name: SearchResult
  property_count: 5
  slug: hortosapp-com-search-result
jsonld:
- class_count: 3
  name: Hortosapp Com Context
  property_count: 11
  slug: hortosapp-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at au.hortosapp.com.
  name: hortosapp-com MCP Server
  slug: hortosapp-com-mcp-yml
modified: '2026-10-29'
name: hortosapp-com
nav: Providers
network: true
overview: 'hortosapp-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Quote API and Search API. Tagged areas include Agriculture, Horticulture, Marketplace, Wholesale, and PlantData.


  The hortosapp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  hortosapp-com''s developer surface includes documentation, API reference, support, getting-started guide, and 17 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Hortosapp Com Rate Limits
  slug: hortosapp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: hortosapp-com API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: hortosapp-com-rules
scopes:
- name: Hortosapp Com Scopes
  scope_count: 0
  slug: hortosapp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 17.1
    contract_governance: 19.7
    contract_quality: 59.3
    developer_ergonomics: 23.1
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hortosapp-com/hortosapp-com-2026-11-03T133453.png
security:
- kind: authentication
  name: Hortosapp Com Authentication
  slug: hortosapp-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hortosapp Com Domain Security
  slug: hortosapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: price-plant-list
  slug: hortosapp-com-price-plant-list
- name: search-plants
  slug: hortosapp-com-search-plants
slug: hortosapp-com
tags:
- Agriculture
- Horticulture
- Marketplace
- Wholesale
- PlantData
website: https://hortosapp.com/
---
