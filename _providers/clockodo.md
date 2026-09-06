---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Clockodo Agentic Access
  operation_count: 33
  slug: clockodo-agentic-access
  summary_line: 33 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Absence records (vacation, sickness, etc.).
  name: Clockodo Absences API
  slug: clockodo-absences-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Real-time stop-clock control.
  name: Clockodo Clock API
  slug: clockodo-clock-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Customer records.
  name: Clockodo Customers API
  slug: clockodo-customers-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Time-tracking entries.
  name: Clockodo Entries API
  slug: clockodo-entries-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Per-user holiday quotas.
  name: Clockodo HolidaysQuota API
  slug: clockodo-holidaysquota-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Lump-sum services for fixed-price billing.
  name: Clockodo LumpSumServices API
  slug: clockodo-lumpsumservices-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Projects under customers.
  name: Clockodo Projects API
  slug: clockodo-projects-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Service catalog used for entries.
  name: Clockodo Services API
  slug: clockodo-services-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Co-workers/users in the account.
  name: Clockodo Users API
  slug: clockodo-users-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clockodo Absences API
  slug: open-clockodo-absences-api
- collection_type: open
  name: Clockodo Absences Clock API
  slug: open-clockodo-clock-api
- collection_type: open
  name: Clockodo Absences Customers API
  slug: open-clockodo-customers-api
- collection_type: open
  name: Clockodo Absences Entries API
  slug: open-clockodo-entries-api
- collection_type: open
  name: Clockodo Absences HolidaysQuota API
  slug: open-clockodo-holidaysquota-api
- collection_type: open
  name: Clockodo Absences LumpSumServices API
  slug: open-clockodo-lumpsumservices-api
- collection_type: open
  name: Clockodo Absences Projects API
  slug: open-clockodo-projects-api
- collection_type: open
  name: Clockodo Absences Services API
  slug: open-clockodo-services-api
- collection_type: open
  name: Clockodo Absences Users API
  slug: open-clockodo-users-api
- collection_type: open
  name: Clockodo API
  slug: open-clockodo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clockodo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clockodo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clockodo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clockodo
- group: company
  title: ''
  type: Website
  url: https://www.clockodo.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clockodo.com/en/api/
- group: company
  title: ''
  type: Blog
  url: https://www.clockodo.com/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clockodo.com/en/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clockodo.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clockodo.com/en/data-privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/clockodo-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clockodo-entry-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/clockodo-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clockodo-rules.yml
created: '2025-02-17'
description: 'Clockodo is a German-built, cloud-based time-tracking and project- management application used by service firms, agencies, and freelancers. In addition to its web and mobile apps, Clockodo exposes a REST API at my.clockodo.com that mirrors the objects in the UI: time entries, customers, projects, services, users, absences, holiday quotas, lump-sum services, and a real-time stop-clock. Authentication uses a per-user email plus per-user API key delivered as the X-ClockodoApiUser/X-ClockodoApiKey header pair (or HTTP Basic), and every call must include the X-Clockodo-External-Application header identifying the integrating application.'
finops:
- name: Clockodo Finops
  service_category: API
  slug: clockodo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clockodo.png
json_schemas:
- name: Clockodo Time Entry
  property_count: 12
  slug: clockodo-entry
jsonld:
- class_count: 7
  name: Clockodo Context
  property_count: 10
  slug: clockodo-context
layout: provider
modified: '2026-05-19'
name: Clockodo
nav: Providers
network: true
overview: 'Clockodo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Clock API, Customers API, and 6 more. Tagged areas include Absence Management, Billing, Project Management, Stopclock, and Time Tracking.


  The Clockodo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clockodo''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Clockodo Plans Pricing
  plan_count: 3
  slug: clockodo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Clockodo Rate Limits
  slug: clockodo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Clockodo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clockodo-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Clockodo API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: clockodo-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 61.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clockodo/refs/heads/main/screenshots/clockodo-2026-06-20T174529.png
security:
- kind: authentication
  name: Clockodo Authentication
  slug: clockodo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clockodo Domain Security
  slug: clockodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clockodo
tags:
- Absence Management
- Billing
- Project Management
- Stopclock
- Time Tracking
- Timesheets
website: https://www.clockodo.com/en/
---
