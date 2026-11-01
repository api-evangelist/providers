---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Startup Jobs Agentic Access
  operation_count: 7
  slug: startup-jobs-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.startup.jobs
  baseurl_source: declared
  description: The Companies API from startup-jobs — 2 operation(s) for companies.
  name: startup-jobs Companies API
  slug: startup-jobs-companies-api
- baseURL: https://api.startup.jobs
  baseurl_source: declared
  description: The Jobs API from startup-jobs — 2 operation(s) for jobs.
  name: startup-jobs Jobs API
  slug: startup-jobs-jobs-api
- baseURL: https://api.startup.jobs
  baseurl_source: declared
  description: The Locations API from startup-jobs — 1 operation(s) for locations.
  name: startup-jobs Locations API
  slug: startup-jobs-locations-api
- baseURL: https://api.startup.jobs
  baseurl_source: declared
  description: The Openapi.json API from startup-jobs — 1 operation(s) for openapi.json.
  name: startup-jobs Openapi.json API
  slug: startup-jobs-openapi-json-api
- baseURL: https://api.startup.jobs
  baseurl_source: declared
  description: The Roles API from startup-jobs — 1 operation(s) for roles.
  name: startup-jobs Roles API
  slug: startup-jobs-roles-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/startup-jobs/agentic-access/startup-jobs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/startup-jobs-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/startup-jobs/rate-limits/startup-jobs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/startup-jobs-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/startup-jobs/rules/startup-jobs-rules.yml
  title: ''
  type: Spectral
  url: rules/startup-jobs-rules.yml
- group: design
  href: https://artifacts.apis.io/startup-jobs/json-ld/startup-jobs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/startup-jobs-context.jsonld
- group: design
  href: https://artifacts.apis.io/startup-jobs/vocabulary/startup-jobs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/startup-jobs-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/startup-jobs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/startup-jobs/data-model/startup-jobs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/startup-jobs-data-model.yml
- group: design
  href: https://artifacts.apis.io/startup-jobs/conventions/startup-jobs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/startup-jobs-conventions.yml
- group: auth
  href: https://artifacts.apis.io/startup-jobs/authentication/startup-jobs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/startup-jobs-authentication.yml
- group: design
  href: https://artifacts.apis.io/startup-jobs/errors/startup-jobs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/startup-jobs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/startup-jobs/conformance/startup-jobs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/startup-jobs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/startup-jobs/llms/startup-jobs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/startup-jobs-llms.txt
- group: other
  href: https://artifacts.apis.io/startup-jobs/hosts/startup-jobs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/startup-jobs-hosts.yml
- group: other
  href: https://artifacts.apis.io/startup-jobs/vendors/startup-jobs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/startup-jobs-vendors.yml
- group: auth
  href: https://artifacts.apis.io/startup-jobs/security/startup-jobs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/startup-jobs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://startup.jobs/
created: '2026-10-31'
description: 'startup-jobs is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: Company
  property_count: 6
  slug: startup-jobs-company
- name: Job
  property_count: 12
  slug: startup-jobs-job
- name: JobsPage
  property_count: 5
  slug: startup-jobs-jobs-page
- name: Location
  property_count: 3
  slug: startup-jobs-location
- name: Startup Jobs Mcp
  property_count: 0
  slug: startup-jobs-mcp
- name: Role
  property_count: 4
  slug: startup-jobs-role
jsonld:
- class_count: 6
  name: Startup Jobs Context
  property_count: 25
  slug: startup-jobs-context
layout: provider
modified: '2026-10-31'
name: startup-jobs
nav: Providers
network: true
overview: 'startup-jobs publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Jobs API, Locations API, and 2 more. Tagged areas include Company.


  The startup-jobs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  startup-jobs'' developer surface includes authentication and 15 more developer resources.'
plans:
- name: Startup Jobs Plans Pricing
  plan_count: 0
  slug: startup-jobs-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Startup Jobs Rate Limits
  slug: startup-jobs-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: startup-jobs API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 1
  slug: startup-jobs-rules
scopes:
- name: Startup Jobs Scopes
  scope_count: 0
  slug: startup-jobs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 72.9
    catalog_earned_first_party: 0.0
    catalog_gap: 42.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 79.1
    contract_quality: 60.0
    developer_ergonomics: 18.3
    discoverability: 44.6
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Startup Jobs Authentication
  slug: startup-jobs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Startup Jobs Domain Security
  slug: startup-jobs-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 7
skills:
- name: get-lcompany
  slug: startup-jobs-get-lcompany
- name: get-ljob
  slug: startup-jobs-get-ljob
- name: get-lopen-lapi-lspec
  slug: startup-jobs-get-lopen-lapi-lspec
- name: list-lcompany-ljobs
  slug: startup-jobs-list-lcompany-ljobs
- name: list-ljobs
  slug: startup-jobs-list-ljobs
- name: list-llocations
  slug: startup-jobs-list-llocations
- name: list-lroles
  slug: startup-jobs-list-lroles
slug: startup-jobs
tags:
- Company
website: https://startup.jobs/
---
