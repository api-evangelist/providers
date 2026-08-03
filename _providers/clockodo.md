---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Clockodo Agentic Access
  operation_count: 33
  slug: clockodo-agentic-access
  summary_line: 33 operations · 19 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Absence records (vacation, sickness, etc.).
  name: Clockodo Absences API
  slug: clockodo-absences-api
- description: Real-time stop-clock control.
  name: Clockodo Clock API
  slug: clockodo-clock-api
- description: Customer records.
  name: Clockodo Customers API
  slug: clockodo-customers-api
- description: Time-tracking entries.
  name: Clockodo Entries API
  slug: clockodo-entries-api
- description: Per-user holiday quotas.
  name: Clockodo HolidaysQuota API
  slug: clockodo-holidaysquota-api
- description: Lump-sum services for fixed-price billing.
  name: Clockodo LumpSumServices API
  slug: clockodo-lumpsumservices-api
- description: Projects under customers.
  name: Clockodo Projects API
  slug: clockodo-projects-api
- description: Service catalog used for entries.
  name: Clockodo Services API
  slug: clockodo-services-api
- description: Co-workers/users in the account.
  name: Clockodo Users API
  slug: clockodo-users-api
artifact_total: 20
collections:
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
  url: openapi/clockodo-openapi.yml
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
overview: 'Clockodo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Clock API, Customers API, and 6 more. Tagged areas include Absence Management, Billing, Project Management, Stop Clock, and Time Tracking.


  The Clockodo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clockodo''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Clockodo Plans Pricing
  plan_count: 3
  slug: clockodo-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 5
  name: Clockodo Rate Limits
  slug: clockodo-rate-limits
rules:
- name: Clockodo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clockodo-jsonschema-spectral-rules
- name: Clockodo API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: clockodo-rules
score:
  band: developing
  composite: 53.5
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 65.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Stop Clock
- Time Tracking
- Timesheets
website: https://www.clockodo.com/en/
---
