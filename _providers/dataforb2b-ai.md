---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dataforb2B Ai Agentic Access
  operation_count: 6
  slug: dataforb2b-ai-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.dataforb2b.ai
  baseurl_source: declared
  description: The DataForB2B API API from dataforb2b-ai — 1 operation(s) for dataforb2b api.
  name: dataforb2b-ai DataForB2B API
  slug: dataforb2b-ai-dataforb2b-api-api
- baseURL: https://api.dataforb2b.ai
  baseurl_source: declared
  description: The Health API from dataforb2b-ai — 1 operation(s) for health.
  name: dataforb2b-ai Health API
  slug: dataforb2b-ai-health-api
- baseURL: https://api.dataforb2b.ai
  baseurl_source: declared
  description: The search API from dataforb2b-ai — 3 operation(s) for search.
  name: dataforb2b-ai Search API
  slug: dataforb2b-ai-search-api
- baseURL: https://api.dataforb2b.ai
  baseurl_source: declared
  description: The Stats API from dataforb2b-ai — 1 operation(s) for stats.
  name: dataforb2b-ai Stats API
  slug: dataforb2b-ai-stats-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/dataforb2b-ai/data-model/dataforb2b-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dataforb2b-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/dataforb2b-ai/agentic-access/dataforb2b-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dataforb2b-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dataforb2b-ai/rules/dataforb2b-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dataforb2b-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dataforb2b-ai/vocabulary/dataforb2b-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataforb2b-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dataforb2b-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dataforb2b-ai/errors/dataforb2b-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataforb2b-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataforb2b-ai/conformance/dataforb2b-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataforb2b-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataforb2b-ai/llms/dataforb2b-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataforb2b-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/dataforb2b-ai/a2a/dataforb2b-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dataforb2b-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/dataforb2b-ai/mcp/dataforb2b-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dataforb2b-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dataforb2b-ai/mcp/dataforb2b-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dataforb2b-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dataforb2b-ai/well-known/dataforb2b-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataforb2b-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataforb2b-ai/hosts/dataforb2b-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataforb2b-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataforb2b-ai/vendors/dataforb2b-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataforb2b-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dataforb2b-ai/security/dataforb2b-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataforb2b-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataforb2b.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dataforb2b.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dataforb2b.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dataforb2b.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dataforb2b.ai/get-started/introduction
- group: company
  title: ''
  type: Blog
  url: https://dataforb2b.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dataforb2b.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataforb2b.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataforb2b.ai/privacy
created: '2026-10-30'
description: DataForB2B provides a B2B data API for AI agents, offering over 850 million verified profiles and 75 million companies, including buying signals. The service supports REST and MCP endpoints for use cases in sales, recruiting, and investment, delivering enriched people, company, and intent data.
image: https://mintcdn.com/dataforb2b/GIq82P9n090DmLuZ/logo/light.png?fit=max&auto=format&n=GIq82P9n090DmLuZ&q=85&s=91b2e53546d923607d4aad865ea8e172
json_schemas:
- name: AdvancedCompanySearchRequest
  property_count: 0
  slug: dataforb2b-ai-advanced-company-search-request
- name: AdvancedPeopleSearchRequest
  property_count: 0
  slug: dataforb2b-ai-advanced-people-search-request
- name: AdvancedPostSearchRequest
  property_count: 0
  slug: dataforb2b-ai-advanced-post-search-request
- name: CompanySearchResponse
  property_count: 0
  slug: dataforb2b-ai-company-search-response
- name: PostSearchResponse
  property_count: 0
  slug: dataforb2b-ai-post-search-response
- name: StatsResponse
  property_count: 0
  slug: dataforb2b-ai-stats-response
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.dataforb2b.ai requiring OAuth.
  name: dataforb2b-ai MCP Server
  slug: dataforb2b-ai-mcp-yml
modified: '2026-10-30'
name: dataforb2b-ai
nav: Providers
network: true
overview: 'dataforb2b-ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including DataForB2B API, Health API, Search API, and 1 more. Tagged areas include Company, Data, B2B, Artificial Intelligence, and Analytics.


  The dataforb2b-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  dataforb2b-ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: dataforb2b-ai API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: dataforb2b-ai-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 44.5
    developer_ergonomics: 22.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 36.2
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dataforb2b-ai/dataforb2b-ai-2026-11-03T130153.png
security:
- kind: domain-security
  name: Dataforb2B Ai Domain Security
  slug: dataforb2b-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: search
  slug: dataforb2b-ai-search
slug: dataforb2b-ai
tags:
- Company
- Data
- B2B
- Artificial Intelligence
- Analytics
website: https://dataforb2b.ai/
---
