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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 82
  human_in_the_loop: 10
  name: Adhdevaluations Fyi Agentic Access
  operation_count: 129
  slug: adhdevaluations-fyi-agentic-access
  summary_line: 129 operations · 82 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://adhdevaluations.fyi/api/v1
  baseurl_source: declared
  description: The Admin API from ADHDEvaluations — 89 operation(s) for admin.
  name: ADHDEvaluations Admin API
  slug: adhdevaluations-fyi-admin-api
- baseURL: https://adhdevaluations.fyi/api/v1
  baseurl_source: declared
  description: The Categories API from ADHDEvaluations — 1 operation(s) for categories.
  name: ADHDEvaluations Categories API
  slug: adhdevaluations-fyi-categories-api
- baseURL: https://adhdevaluations.fyi/api/v1
  baseurl_source: declared
  description: The Listings API from ADHDEvaluations — 2 operation(s) for listings.
  name: ADHDEvaluations Listings API
  slug: adhdevaluations-fyi-listings-api
- baseURL: https://adhdevaluations.fyi/api/v1
  baseurl_source: declared
  description: The Places API from ADHDEvaluations — 1 operation(s) for places.
  name: ADHDEvaluations Places API
  slug: adhdevaluations-fyi-places-api
- baseURL: https://adhdevaluations.fyi/api/v1
  baseurl_source: declared
  description: The Sources API from ADHDEvaluations — 1 operation(s) for sources.
  name: ADHDEvaluations Sources API
  slug: adhdevaluations-fyi-sources-api
- baseURL: https://adhdevaluations.fyi/api/v1
  baseurl_source: declared
  description: The Stats API from ADHDEvaluations — 1 operation(s) for stats.
  name: ADHDEvaluations Stats API
  slug: adhdevaluations-fyi-stats-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/adhdevaluations-fyi/agentic-access/adhdevaluations-fyi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adhdevaluations-fyi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adhdevaluations-fyi/rules/adhdevaluations-fyi-rules.yml
  title: ''
  type: Spectral
  url: rules/adhdevaluations-fyi-rules.yml
- group: design
  href: https://artifacts.apis.io/adhdevaluations-fyi/json-ld/adhdevaluations-fyi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adhdevaluations-fyi-context.jsonld
- group: design
  href: https://artifacts.apis.io/adhdevaluations-fyi/vocabulary/adhdevaluations-fyi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adhdevaluations-fyi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adhdevaluations-fyi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adhdevaluations-fyi/data-model/adhdevaluations-fyi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adhdevaluations-fyi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/adhdevaluations-fyi/security/adhdevaluations-fyi-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adhdevaluations-fyi-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/adhdevaluations-fyi/errors/adhdevaluations-fyi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adhdevaluations-fyi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adhdevaluations-fyi/conformance/adhdevaluations-fyi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adhdevaluations-fyi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adhdevaluations-fyi/llms/adhdevaluations-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adhdevaluations-fyi-llms.txt
- group: other
  href: https://artifacts.apis.io/adhdevaluations-fyi/a2a/adhdevaluations-fyi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adhdevaluations-fyi-a2a.yml
- group: build
  href: https://artifacts.apis.io/adhdevaluations-fyi/mcp/adhdevaluations-fyi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adhdevaluations-fyi-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/adhdevaluations-fyi/mcp/adhdevaluations-fyi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adhdevaluations-fyi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adhdevaluations-fyi/well-known/adhdevaluations-fyi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adhdevaluations-fyi-security.txt
- group: agent
  href: https://artifacts.apis.io/adhdevaluations-fyi/well-known/adhdevaluations-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adhdevaluations-fyi-well-known.yml
- group: other
  href: https://artifacts.apis.io/adhdevaluations-fyi/hosts/adhdevaluations-fyi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adhdevaluations-fyi-hosts.yml
- group: other
  href: https://artifacts.apis.io/adhdevaluations-fyi/vendors/adhdevaluations-fyi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adhdevaluations-fyi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adhdevaluations.fyi/terms
- group: operate
  title: ''
  type: Support
  url: https://adhdevaluations.fyi/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adhdevaluations.fyi/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://adhdevaluations.fyi/pa/media
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adhdevaluations.fyi/developers
- group: auth
  href: https://artifacts.apis.io/adhdevaluations-fyi/security/adhdevaluations-fyi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adhdevaluations-fyi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adhdevaluations-fyi/security/adhdevaluations-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adhdevaluations-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adhdevaluations.fyi/
- group: docs
  title: ''
  type: Documentation
  url: https://adhdevaluations.fyi/guides
- group: docs
  title: ''
  type: APIReference
  url: https://adhdevaluations.fyi/api/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://adhdevaluations.fyi/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://adhdevaluations.fyi/pricing
- group: start
  title: ''
  type: SignUp
  url: https://adhdevaluations.fyi/submit
created: '2026-10-31'
description: ADHDEvaluations is a public directory that aggregates over 9,800 ADHD evaluation providers across all 55 U.S. states, districts and territories. The data is sourced from the CMS NPI Registry and includes practice addresses and contact details. The service helps users find qualified clinicians for ADHD assessments, offering tools, guides, and pricing information while emphasizing that listings do not guarantee service availability.
image: https://adhdevaluations.fyi/brand/home/scene.svg
json_schemas:
- name: CategoryNode
  property_count: 5
  slug: adhdevaluations-fyi-category-node
- name: ListingItem
  property_count: 15
  slug: adhdevaluations-fyi-listing-item
- name: Listing
  property_count: 27
  slug: adhdevaluations-fyi-listing
- name: Page
  property_count: 5
  slug: adhdevaluations-fyi-page
- name: PlaceNode
  property_count: 7
  slug: adhdevaluations-fyi-place-node
- name: Stats
  property_count: 7
  slug: adhdevaluations-fyi-stats
jsonld:
- class_count: 9
  name: Adhdevaluations Fyi Context
  property_count: 49
  slug: adhdevaluations-fyi-context
layout: provider
mcp_servers:
- description: Remote MCP server at adhdevaluations.fyi.
  name: ADHDEvaluations MCP Server
  slug: adhdevaluations-fyi-mcp-yml
modified: '2026-10-31'
name: ADHDEvaluations
nav: Providers
network: true
overview: 'ADHDEvaluations publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Categories API, Listings API, and 3 more. Tagged areas include ADHD, Healthcare, Directory, Evaluation, and Providers.


  The ADHDEvaluations catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ADHDEvaluations'' developer surface includes support, documentation, API reference, getting-started guide, pricing, signup flow, and 24 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ADHDEvaluations API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: adhdevaluations-fyi-rules
scopes:
- name: Adhdevaluations Fyi Scopes
  scope_count: 0
  slug: adhdevaluations-fyi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 54.9
    developer_ergonomics: 23.2
    discoverability: 65.8
    operational_transparency: 10.5
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 29.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adhdevaluations Fyi Authentication
  slug: adhdevaluations-fyi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adhdevaluations Fyi Domain Security
  slug: adhdevaluations-fyi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adhdevaluations Fyi Vulnerability Disclosure
  slug: adhdevaluations-fyi-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: get-listing
  slug: get-listing
- name: get-stats
  slug: get-stats
- name: list-categories
  slug: list-categories
- name: list-places
  slug: list-places
- name: list-sources
  slug: list-sources
- name: search-listings
  slug: search-listings
slug: adhdevaluations-fyi
tags:
- ADHD
- Healthcare
- Directory
- Evaluation
- Providers
website: https://adhdevaluations.fyi/
---
