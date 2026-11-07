---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.peoplehr.net
  baseurl_source: declared
  description: 'PeopleHR API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: PeopleHR API
  slug: peoplehr-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/peoplehr/plans/peoplehr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peoplehr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/peoplehr/rules/peoplehr-rules.yml
  title: ''
  type: Spectral
  url: rules/peoplehr-rules.yml
- group: design
  href: https://artifacts.apis.io/peoplehr/json-ld/peoplehr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/peoplehr-context.jsonld
- group: design
  href: https://artifacts.apis.io/peoplehr/vocabulary/peoplehr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/peoplehr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/peoplehr/data-model/peoplehr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/peoplehr-data-model.yml
- group: design
  href: https://artifacts.apis.io/peoplehr/conformance/peoplehr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peoplehr-conformance.yml
- group: other
  href: https://artifacts.apis.io/peoplehr/hosts/peoplehr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peoplehr-hosts.yml
- group: other
  href: https://artifacts.apis.io/peoplehr/vendors/peoplehr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peoplehr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/peoplehr/security/peoplehr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peoplehr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peoplehr.com/en-gb/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.peoplehr.com/en-gb/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.peoplehr.com/en-gb/
- group: docs
  title: ''
  type: APIReference
  url: https://www.peoplehr.com/en-gb/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.peoplehr.com/en-gb/
- group: operate
  title: ''
  type: Support
  url: https://www.peoplehr.com/en-gb/forms/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.peoplehr.com/en-gb/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.peoplehr.com/en-gb/pricing/
coverage:
  checked: '2026-10-26'
  detail: The developer portal page returns HTML with no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.peoplehr.com/en-gb/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: PeopleHR provides a cloud‑based HR software platform for small and medium businesses, offering modules for core HR, recruitment, performance management, payroll, time‑and‑attendance, and employee self‑service. The solution helps organisations automate HR processes, stay compliant with employment law, and improve employee experience through an AI‑driven HR assistant.
image: https://www.theaccessgroup.com/images/accessgroup.png
json_schemas:
- name: PostAbsenceRequest
  property_count: 13
  slug: peoplehr-post-absence-request
- name: PostEmployeedocumentRequest
  property_count: 13
  slug: peoplehr-post-employeedocument-request
- name: PostHolidayentitlementsRequest
  property_count: 8
  slug: peoplehr-post-holidayentitlements-request
- name: PostMaternitypaternityRequest
  property_count: 9
  slug: peoplehr-post-maternitypaternity-request
- name: PostSalaryRequest
  property_count: 13
  slug: peoplehr-post-salary-request
- name: PostTimesheetRequest
  property_count: 37
  slug: peoplehr-post-timesheet-request
jsonld:
- class_count: 23
  name: Peoplehr Context
  property_count: 108
  slug: peoplehr-context
layout: provider
modified: '2026-10-26'
name: PeopleHR
nav: Providers
network: true
overview: 'PeopleHR is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Software-as-a-Service, Payroll, and Recruiting.


  The PeopleHR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PeopleHR''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Peoplehr Plans Pricing
  plan_count: 4
  slug: peoplehr-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: PeopleHR API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: peoplehr-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 36.8
    contract_governance: 33.3
    contract_quality: 24.8
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/peoplehr/peoplehr-2026-11-03T141113.png
security:
- kind: domain-security
  name: Peoplehr Domain Security
  slug: peoplehr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peoplehr
tags:
- Company
- Human Resources
- Software-as-a-Service
- Payroll
- Recruiting
- Employee Management
website: https://www.peoplehr.com/en-gb/
---
