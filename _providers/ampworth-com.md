---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Ampworth Com Agentic Access
  operation_count: 31
  slug: ampworth-com-agentic-access
  summary_line: 31 operations · 11 acting
api_count: 1
apis:
- baseURL: https://ampworth.com
  baseurl_source: declared
  description: The MCS and ENA methods, run over a request.
  name: ampworth-com Calculators API
  slug: ampworth-com-calculators-api
- baseURL: https://ampworth.com
  baseurl_source: declared
  description: Where everything else is.
  name: ampworth-com Discovery API
  slug: ampworth-com-discovery-api
- baseURL: https://ampworth.com
  baseurl_source: declared
  description: The guides, articles and question sets.
  name: ampworth-com Documents API
  slug: ampworth-com-documents-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/ampworth-com/agentic-access/ampworth-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ampworth-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ampworth-com/rules/ampworth-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ampworth-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ampworth-com/json-ld/ampworth-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ampworth-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ampworth-com/vocabulary/ampworth-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ampworth-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ampworth-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ampworth-com/data-model/ampworth-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ampworth-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/ampworth-com/cli/ampworth-com-cli.yml
  title: ''
  type: CLI
  url: cli/ampworth-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/ampworth-com/changelog/ampworth-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ampworth-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/ampworth-com/errors/ampworth-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ampworth-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ampworth-com/conformance/ampworth-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ampworth-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ampworth-com/llms/ampworth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ampworth-com-llms.txt
- group: build
  href: https://artifacts.apis.io/ampworth-com/mcp/ampworth-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ampworth-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ampworth-com/mcp/ampworth-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ampworth-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ampworth-com/hosts/ampworth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ampworth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ampworth-com/vendors/ampworth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ampworth-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://ampworth.com/support
- group: operate
  title: ''
  type: ChangeLog
  url: https://ampworth.com/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ampworth
- group: auth
  href: https://artifacts.apis.io/ampworth-com/security/ampworth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ampworth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ampworth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ampworth.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://ampworth.com/api/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://ampworth.com/calculators
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ampworth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ampworth.com/privacy
created: '2026-10-29'
description: Ampworth provides UK homeowners with clean energy solutions, offering heat pumps, solar panels, and battery storage systems. Their platform includes calculators, guides, and open data APIs that deliver real-time information on energy consumption, savings, and system performance. All data is accessible without authentication, supporting developers and researchers in building tools for sustainable home energy management.
image: https://ampworth.com/favicon.ico
json_schemas:
- name: CategoryList
  property_count: 3
  slug: ampworth-com-category-list
- name: Discovery
  property_count: 10
  slug: ampworth-com-discovery
- name: DocumentDetail
  property_count: 3
  slug: ampworth-com-document-detail
- name: DocumentList
  property_count: 3
  slug: ampworth-com-document-list
- name: PerspectiveList
  property_count: 3
  slug: ampworth-com-perspective-list
- name: SearchResults
  property_count: 4
  slug: ampworth-com-search-results
jsonld:
- class_count: 9
  name: Ampworth Com Context
  property_count: 24
  slug: ampworth-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ampworth.com.
  name: ampworth-com MCP Server
  slug: ampworth-com-mcp-yml
modified: '2026-10-29'
name: ampworth-com
nav: Providers
network: true
overview: 'ampworth-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calculators API, Discovery API, and Documents API. Tagged areas include Company, Energy, Heat Pumps, Solar, and Batteries.


  The ampworth-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ampworth-com''s developer surface includes CLI, changelog, support, documentation, API reference, getting-started guide, and 19 more developer resources.'
plans:
- name: Ampworth Com Plans Pricing
  plan_count: 0
  slug: ampworth-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Ampworth Com Rate Limits
  slug: ampworth-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: ampworth-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: ampworth-com-rules
scopes:
- name: Ampworth Com Scopes
  scope_count: 0
  slug: ampworth-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 59.7
    developer_ergonomics: 42.3
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ampworth Com Authentication
  slug: ampworth-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ampworth Com Domain Security
  slug: ampworth-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: connection-route
  slug: ampworth-com-connection_route
slug: ampworth-com
tags:
- Company
- Energy
- Heat Pumps
- Solar
- Batteries
- UK
website: https://ampworth.com/
---
