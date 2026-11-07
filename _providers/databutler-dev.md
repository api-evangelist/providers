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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Databutler Dev Agentic Access
  operation_count: 2
  slug: databutler-dev-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Official facts and rates API providing verified data across multiple jurisdictions. No authentication required.
  name: Data Butler API
  slug: data-butler-api
- description: 'databutler-dev API as documented publicly: 58 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: databutler-dev API
  slug: databutler-dev-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/databutler-dev/rules/databutler-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/databutler-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/databutler-dev/json-ld/databutler-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/databutler-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/databutler-dev/vocabulary/databutler-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/databutler-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/databutler-dev/data-model/databutler-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/databutler-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/databutler-dev/conformance/databutler-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/databutler-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/databutler-dev/llms/databutler-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/databutler-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/databutler-dev/mcp/databutler-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/databutler-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/databutler-dev/hosts/databutler-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/databutler-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/databutler-dev/vendors/databutler-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/databutler-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://databutler.dev/terms
- group: start
  title: ''
  type: SignUp
  url: https://databutler.dev/f/uk/gov/register-birth/where
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://databutler.dev/privacy
- group: auth
  href: https://artifacts.apis.io/databutler-dev/security/databutler-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/databutler-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://databutler.dev/
created: '2026-10-29'
description: Data Butler provides official rates, thresholds, and reference data for AI agents across multiple jurisdictions such as the UK, US, Germany, and the EU. The service offers a REST API and an MCP endpoint for querying tax, social‑insurance, vehicle, and other official figures, each with source URLs, verified dates, and digital signatures. No accounts, cookies, or IP logging are used; only anonymous event counts are recorded. The site includes a changelog of verified facts, RSS/Atom feeds, and documentation at /api and llms.txt.
json_schemas:
- name: PostApiStatsRequest
  property_count: 1
  slug: databutler-dev-post-api-stats-request
jsonld:
- class_count: 1
  name: Databutler Dev Context
  property_count: 1
  slug: databutler-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at databutler.dev.
  name: databutler-dev MCP Server
  slug: databutler-dev-mcp-yml
modified: '2026-10-29'
name: databutler-dev
nav: Providers
network: true
overview: 'databutler-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Tax, and Reference.


  The databutler-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  databutler-dev''s developer surface includes signup flow and 13 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: databutler-dev API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: databutler-dev-rules
scopes:
- name: Databutler Dev Scopes
  scope_count: 0
  slug: databutler-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.2
    catalog_earned_first_party: 0.0
    catalog_gap: 73.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 28.3
    developer_ergonomics: 0.0
    discoverability: 55.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 1
      marker_coverage: 50.0
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
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/databutler-dev/databutler-dev-2026-11-03T130133.png
security:
- kind: authentication
  name: Databutler Dev Authentication
  slug: databutler-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Databutler Dev Domain Security
  slug: databutler-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: get-fact
  slug: databutler-dev-getFact
- name: get-facts
  slug: databutler-dev-getFacts
- name: resolve-fact
  slug: databutler-dev-resolveFact
- name: what-changed-since
  slug: databutler-dev-whatChangedSince
slug: databutler-dev
tags:
- Company
- Data
- Tax
- Reference
website: https://databutler.dev/
---
