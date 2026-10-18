---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Public REST API for partners and integrations to access Wagepoint Company, Person, Pay Group, and Time data.
  name: Wagepoint Public API
  slug: wagepoint-public-api
- baseURL: https://api.wagepoint.com/api
  baseurl_source: declared
  description: The Companies API from Wagepoint — 2 operation(s) for companies.
  name: Wagepoint Companies API
  slug: wagepoint-companies-api
- baseURL: https://api.wagepoint.com/api
  baseurl_source: declared
  description: The Health API from Wagepoint — 2 operation(s) for health.
  name: Wagepoint Health API
  slug: wagepoint-health-api
- baseURL: https://api.wagepoint.com/api
  baseurl_source: declared
  description: The MCP API from Wagepoint — 1 operation(s) for mcp.
  name: Wagepoint MCP API
  slug: wagepoint-mcp-api
- baseURL: https://api.wagepoint.com/api
  baseurl_source: declared
  description: The Pay Groups API from Wagepoint — 1 operation(s) for pay groups.
  name: Wagepoint Pay Groups API
  slug: wagepoint-pay-groups-api
- baseURL: https://api.wagepoint.com/api
  baseurl_source: declared
  description: The Persons API from Wagepoint — 1 operation(s) for persons.
  name: Wagepoint Persons API
  slug: wagepoint-persons-api
- baseURL: https://api.wagepoint.com/api
  baseurl_source: declared
  description: The Time Entries API from Wagepoint — 2 operation(s) for time entries.
  name: Wagepoint Time Entries API
  slug: wagepoint-time-entries-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/rules/wagepoint-rules.yml
  title: ''
  type: Spectral
  url: rules/wagepoint-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/json-ld/wagepoint-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wagepoint-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/vocabulary/wagepoint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wagepoint-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/conventions/wagepoint-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wagepoint-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/conventions/wagepoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wagepoint-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/conformance/wagepoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wagepoint-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/plans/wagepoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wagepoint-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/data-model/wagepoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wagepoint-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.wagepoint.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/errors/wagepoint-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wagepoint-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/hosts/wagepoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wagepoint-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wagepoint.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wagepoint.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.wagepoint.com/newsroom/
- group: start
  title: ''
  type: Login
  url: https://www.wagepoint.com/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.wagepoint.com/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://www.wagepoint.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WagePoint
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/security/wagepoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wagepoint-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wagepoint/refs/heads/main/security/wagepoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wagepoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wagepoint.com
created: '2026-10-13'
description: Wagepoint provides cloud‑based payroll software for small and medium‑size businesses in Canada. The platform simplifies payroll processing, tax calculations, and compliance for a variety of industries including healthcare, hospitality, construction, retail, and professional services. Users can run payroll, generate T4 slips, manage employee benefits, and integrate with accounting tools such as Xero and QuickBooks. Wagepoint emphasizes ease of use, automated tax filing, and dedicated support, positioning itself as a friendly, modern payroll solution for Canadian employers.
image: https://www.wagepoint.com/wp-content/uploads/2026/04/Homepage-_-General.png
json_schemas:
- name: company_response
  property_count: 9
  slug: wagepoint-company-response
- name: create_time_entries_request
  property_count: 1
  slug: wagepoint-create-time-entries-request
- name: paged_response_company_list_item_response
  property_count: 2
  slug: wagepoint-paged-response-company-list-item-response
- name: paged_response_person_response
  property_count: 2
  slug: wagepoint-paged-response-person-response
- name: update_time_entry_status_request
  property_count: 3
  slug: wagepoint-update-time-entry-status-request
- name: update_time_entry_status_response
  property_count: 2
  slug: wagepoint-update-time-entry-status-response
jsonld:
- class_count: 21
  name: Wagepoint Context
  property_count: 42
  slug: wagepoint-context
layout: provider
modified: '2026-10-13'
name: Wagepoint
nav: Providers
network: true
overview: 'Wagepoint publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Health API, MCP API, and 4 more. Tagged areas include Company, Payroll, Canada, Software-as-a-Service, and Small Business.


  The Wagepoint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wagepoint''s developer surface includes pricing, changelog, engineering blog, and 18 more developer resources.'
plans:
- name: Wagepoint Plans Pricing
  plan_count: 2
  slug: wagepoint-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Wagepoint API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: wagepoint-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 22.0
    contract_quality: 54.5
    developer_ergonomics: 2.4
    discoverability: 67.9
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Wagepoint Domain Security
  slug: wagepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wagepoint Trust Center
  slug: wagepoint-trust-center
  summary_line: SOC 2
slug: wagepoint
tags:
- Company
- Payroll
- Canada
- Software-as-a-Service
- Small Business
website: https://wagepoint.com
---
