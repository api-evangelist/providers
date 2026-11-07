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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Salesjobs Now Agentic Access
  operation_count: 4
  slug: salesjobs-now-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://salesjobs.now
  baseurl_source: declared
  description: The Jobs API from SalesJobs.Now — 1 operation(s) for jobs.
  name: SalesJobs.Now Jobs API
  slug: salesjobs-now-jobs-api
- baseURL: https://salesjobs.now
  baseurl_source: declared
  description: The Pay.csv API from SalesJobs.Now — 1 operation(s) for pay.csv.
  name: SalesJobs.Now Pay.csv API
  slug: salesjobs-now-pay-csv-api
- baseURL: https://salesjobs.now
  baseurl_source: declared
  description: The Pay.json API from SalesJobs.Now — 1 operation(s) for pay.json.
  name: SalesJobs.Now Pay.json API
  slug: salesjobs-now-pay-json-api
- baseURL: https://salesjobs.now
  baseurl_source: declared
  description: The Roles.json API from SalesJobs.Now — 1 operation(s) for roles.json.
  name: SalesJobs.Now Roles.json API
  slug: salesjobs-now-roles-json-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/salesjobs-now/agentic-access/salesjobs-now-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/salesjobs-now-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/salesjobs-now/rules/salesjobs-now-rules.yml
  title: ''
  type: Spectral
  url: rules/salesjobs-now-rules.yml
- group: design
  href: https://artifacts.apis.io/salesjobs-now/json-ld/salesjobs-now-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/salesjobs-now-context.jsonld
- group: design
  href: https://artifacts.apis.io/salesjobs-now/vocabulary/salesjobs-now-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/salesjobs-now-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/salesjobs-now/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/salesjobs-now/data-model/salesjobs-now-data-model.yml
  title: ''
  type: DataModel
  url: data-model/salesjobs-now-data-model.yml
- group: design
  href: https://artifacts.apis.io/salesjobs-now/errors/salesjobs-now-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/salesjobs-now-problem-types.yml
- group: design
  href: https://artifacts.apis.io/salesjobs-now/conformance/salesjobs-now-conformance.yml
  title: ''
  type: Conformance
  url: conformance/salesjobs-now-conformance.yml
- group: agent
  href: https://artifacts.apis.io/salesjobs-now/llms/salesjobs-now-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/salesjobs-now-llms.txt
- group: build
  href: https://artifacts.apis.io/salesjobs-now/mcp/salesjobs-now-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/salesjobs-now-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/salesjobs-now/mcp/salesjobs-now-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/salesjobs-now-mcp.yml
- group: agent
  href: https://artifacts.apis.io/salesjobs-now/well-known/salesjobs-now-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/salesjobs-now-well-known.yml
- group: other
  href: https://artifacts.apis.io/salesjobs-now/hosts/salesjobs-now-hosts.yml
  title: ''
  type: Hosts
  url: hosts/salesjobs-now-hosts.yml
- group: other
  href: https://artifacts.apis.io/salesjobs-now/vendors/salesjobs-now-vendors.yml
  title: ''
  type: Vendors
  url: vendors/salesjobs-now-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://salesjobs.now/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://salesjobs.now/legal/privacy
- group: auth
  href: https://artifacts.apis.io/salesjobs-now/security/salesjobs-now-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/salesjobs-now-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://salesjobs.now
- group: docs
  title: ''
  type: Documentation
  url: https://salesjobs.now/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://salesjobs.now/how-it-works
- group: docs
  title: ''
  type: APIReference
  url: https://salesjobs.now/pay.json
created: '2026-11-02'
description: SalesJobs.Now aggregates real-time sales job listings from 1,481 hiring companies, providing a searchable database of SDR, BDR, account executive, account manager, customer success, and sales engineering roles with salary ranges and filters by role, company, location, and remote work. The platform updates hourly, ensuring current data for job seekers and analysts.
image: https://salesjobs.now/opengraph-image
json_schemas:
- name: JobsResult
  property_count: 3
  slug: salesjobs-now-jobs-result
- name: PayDocument
  property_count: 8
  slug: salesjobs-now-pay-document
- name: RolesDocument
  property_count: 11
  slug: salesjobs-now-roles-document
jsonld:
- class_count: 5
  name: Salesjobs Now Context
  property_count: 30
  slug: salesjobs-now-context
layout: provider
mcp_servers:
- description: Remote MCP server at salesjobs.now.
  name: SalesJobs.Now MCP Server
  slug: salesjobs-now-mcp-yml
modified: '2026-11-02'
name: SalesJobs.Now
nav: Providers
network: true
overview: 'SalesJobs.Now publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Jobs API, Pay.csv API, Pay.json API, and 1 more. Tagged areas include Sales, Job, Recruiting, and Data.


  The SalesJobs.Now catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SalesJobs.Now''s developer surface includes documentation, getting-started guide, API reference, and 18 more developer resources.'
plans:
- name: Salesjobs Now Plans Pricing
  plan_count: 0
  slug: salesjobs-now-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Salesjobs Now Rate Limits
  slug: salesjobs-now-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: SalesJobs.Now API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: salesjobs-now-rules
scopes:
- name: Salesjobs Now Scopes
  scope_count: 0
  slug: salesjobs-now-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 20.7
    discoverability: 56.7
    operational_transparency: 0.0
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
  name: Salesjobs Now Authentication
  slug: salesjobs-now-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Salesjobs Now Domain Security
  slug: salesjobs-now-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-sales-jobs
  slug: search-sales-jobs
slug: salesjobs-now
tags:
- Sales
- Job
- Recruiting
- Data
website: https://salesjobs.now
---
