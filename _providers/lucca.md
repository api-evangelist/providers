---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Lucca Agentic Access
  operation_count: 77
  slug: lucca-agentic-access
  summary_line: 77 operations · 33 acting
api_count: 2
apis:
- baseURL: https://{host}
  baseurl_source: declared
  description: Employee-Attributes.
  name: Lucca Employee Attributes API
  slug: lucca-employee-attributes-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Job qualifications & professions.
  name: Lucca Employee Job Qualifications API
  slug: lucca-employee-job-qualifications-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Employee occupations categories.
  name: Lucca Employee Occupation Categories API
  slug: lucca-employee-occupation-categories-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Employees.
  name: Lucca Employees API
  slug: lucca-employees-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Employments & job-positions.
  name: Lucca Employments API
  slug: lucca-employments-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Major resources of the Lucca API are subject to events, which means every time their state changes (creation, update, deletion), an event is fired. These events are stored for a limited time (c.f. doc
  name: Lucca Events API
  slug: lucca-events-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Files.
  name: Lucca Files API
  slug: lucca-files-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Organization.
  name: Lucca Organization API
  slug: lucca-organization-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Taxonomies & taxonomy-labels.
  name: Lucca Taxonomies API
  slug: lucca-taxonomies-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Webhooks.
  name: Lucca Webhooks API
  slug: lucca-webhooks-api
- baseURL: https://{host}
  baseurl_source: declared
  description: working-time-arrangements
  name: Lucca Working Time Arrangements API
  slug: lucca-working-time-arrangements-api
artifact_total: 24
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/agentic-access/lucca-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lucca-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/rules/lucca-rules.yml
  title: ''
  type: Spectral
  url: rules/lucca-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/json-ld/lucca-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lucca-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/vocabulary/lucca-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lucca-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/data-model/lucca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lucca-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/changelog/lucca-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lucca-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/conventions/lucca-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lucca-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/authentication/lucca-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lucca-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/lifecycle/lucca-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/lucca-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/lifecycle/lucca-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lucca-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/errors/lucca-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lucca-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/conformance/lucca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lucca-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/llms/lucca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lucca-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/a2a/lucca-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lucca-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/well-known/lucca-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lucca-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/well-known/lucca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lucca-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/hosts/lucca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lucca-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/vendors/lucca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lucca-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucca.fr/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.lucca.fr/roadmap
- group: start
  title: ''
  type: Login
  url: https://www.lucca.fr/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.luccasoftware.com/documentation/get-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lucca.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.luccasoftware.com/home
- group: docs
  title: ''
  type: APIReference
  url: https://developers.luccasoftware.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/scopes/lucca-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lucca-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucca/refs/heads/main/security/lucca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lucca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lucca.fr
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://status.lucca.fr/mcp
  - status: 200
    url: https://www.lucca.fr
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Lucca provides cloud‑based human resources (HR) and administrative software solutions, offering modules for payroll, talent management, time tracking, expense management, and employee benefits. Their platform integrates with over 300 third‑party tools, supports AI‑driven HR insights, and serves enterprises across Europe and beyond. Lucca’s mission is to simplify HR processes, improve compliance, and enhance employee experience through a unified, user‑friendly SaaS suite.
image: https://www.datocms-assets.com/159754/1752164039-og-default.png
json_schemas:
- name: department
  property_count: 8
  slug: lucca-department-update
- name: employee-attribute-definition
  property_count: 7
  slug: lucca-employee-attribute-definition-create
- name: employee.create
  property_count: 0
  slug: lucca-employee-create
- name: employment
  property_count: 8
  slug: lucca-employment-create
- name: File
  property_count: 8
  slug: lucca-file
- name: job-position
  property_count: 13
  slug: lucca-job-position-create
- name: job-position
  property_count: 12
  slug: lucca-job-position-update
jsonld:
- class_count: 97
  name: Lucca Context
  property_count: 114
  slug: lucca-context
layout: provider
modified: '2026-10-14'
name: Lucca
nav: Providers
network: true
overview: 'Lucca publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Employee Attributes API, Employee Job Qualifications API, Employee Occupation Categories API, and 8 more. Tagged areas include Company, Human Resources, Software-as-a-Service, Payroll, and Talent Management.


  The Lucca catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lucca''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, and 24 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Lucca API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: lucca-rules
scopes:
- name: Lucca Scopes
  scope_count: 36
  slug: lucca-scopes
  summary_line: 36 scopes · clientCredentials
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 67.5
    developer_ergonomics: 51.8
    discoverability: 73.2
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Lucca Authentication
  slug: lucca-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lucca Domain Security
  slug: lucca-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lucca
tags:
- Company
- Human Resources
- Software-as-a-Service
- Payroll
- Talent Management
website: https://www.lucca.fr
---
