---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://webapi.timedoctor.com
  baseurl_source: declared
  description: 'Time Doctor API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Time Doctor API
  slug: time-doctor-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/time-doctor/rules/time-doctor-rules.yml
  title: ''
  type: Spectral
  url: rules/time-doctor-rules.yml
- group: design
  href: https://artifacts.apis.io/time-doctor/json-ld/time-doctor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/time-doctor-context.jsonld
- group: design
  href: https://artifacts.apis.io/time-doctor/vocabulary/time-doctor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/time-doctor-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/time-doctor/data-model/time-doctor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/time-doctor-data-model.yml
- group: design
  href: https://artifacts.apis.io/time-doctor/conformance/time-doctor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/time-doctor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/time-doctor/llms/time-doctor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/time-doctor-llms.txt
- group: agent
  href: https://artifacts.apis.io/time-doctor/mcp/time-doctor-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/time-doctor-mcp.yml
- group: agent
  href: https://artifacts.apis.io/time-doctor/well-known/time-doctor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/time-doctor-well-known.yml
- group: other
  href: https://artifacts.apis.io/time-doctor/hosts/time-doctor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/time-doctor-hosts.yml
- group: other
  href: https://artifacts.apis.io/time-doctor/vendors/time-doctor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/time-doctor-vendors.yml
- group: build
  href: https://artifacts.apis.io/time-doctor/packages/time-doctor-packages.yml
  title: ''
  type: SDKs
  url: packages/time-doctor-packages.yml
- group: build
  href: https://artifacts.apis.io/time-doctor/packages/time-doctor-packages.yml
  title: ''
  type: Packages
  url: packages/time-doctor-packages.yml
- group: auth
  href: https://artifacts.apis.io/time-doctor/security/time-doctor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/time-doctor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.timedoctor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.timedoctor.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.timedoctor.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.timedoctor.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.timedoctor.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.timedoctor.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: The Time Doctor website provides no machine‑readable API specification and developer pages return 404.
  evidence:
  - status: 200
    url: https://www.timedoctor.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Time Doctor provides workforce visibility and productivity tracking solutions for distributed teams, offering time‑tracking, activity monitoring, payroll integration, AI‑driven insights, and capacity planning tools to help managers optimize performance and resource allocation across projects.
image: https://www.timedoctor.com/AppIcon.png
json_schemas:
- name: PostV11CompaniesCompanyidUsersUseridWebHooksRequest
  property_count: 5
  slug: time-doctor-post-v11-companies-companyid-users-userid-web-hooks-request
- name: PostV11CompaniesInvitesRequest
  property_count: 5
  slug: time-doctor-post-v11-companies-invites-request
- name: PostV11CompaniesRequest
  property_count: 6
  slug: time-doctor-post-v11-companies-request
- name: PostV11CompaniesResponse
  property_count: 4
  slug: time-doctor-post-v11-companies-response
- name: PutV11CompaniesCompanyidUsersUseridProjectsProjectidRequest
  property_count: 3
  slug: time-doctor-put-v11-companies-companyid-users-userid-projects-projectid-request
- name: PutV11CompaniesCompanyidUsersUseridTasksTaskidRequest
  property_count: 6
  slug: time-doctor-put-v11-companies-companyid-users-userid-tasks-taskid-request
jsonld:
- class_count: 24
  name: Time Doctor Context
  property_count: 25
  slug: time-doctor-context
layout: provider
mcp_servers:
- description: Remote MCP server at api2.timedoctor.com.
  name: Time Doctor MCP Server
  slug: time-doctor-mcp-yml
modified: '2026-10-26'
name: Time Doctor
nav: Providers
network: true
overview: 'Time Doctor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, TimeTracking, WorkforceManagement, Productivity, and AI.


  The Time Doctor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Time Doctor''s developer surface includes documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Time Doctor Plans Pricing
  plan_count: 0
  slug: time-doctor-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Time Doctor API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: time-doctor-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Time Doctor Domain Security
  slug: time-doctor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: time-doctor
tags:
- Company
- TimeTracking
- WorkforceManagement
- Productivity
- AI
website: https://www.timedoctor.com/
---
