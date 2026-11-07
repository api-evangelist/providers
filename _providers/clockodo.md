---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.8
  scored_at: '2026-11-06'
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
  description: Real-time stop-clock control.
  name: Clockodo Clock API
  slug: clockodo-clock-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage absences (holidays, sick days, etc.)
  name: Clockodo Absence API
  slug: clockodo-absence-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage access group rights
  name: Clockodo Access Group Access API
  slug: clockodo-accessgroupaccess-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage customers
  name: Clockodo Customer API
  slug: clockodo-customer-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage time and lump sum entries
  name: Clockodo Entry API
  slug: clockodo-entry-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Query and manage groups of time entries (particularly useful for evaluation and invoicing purposes)
  name: Clockodo Entry Group API
  slug: clockodo-entrygroup-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Query descriptions of time and lump sum entries
  name: Clockodo Entry Text API
  slug: clockodo-entrytext-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage favorites
  name: Clockodo Favorite API
  slug: clockodo-favorite-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage holiday carryovers
  name: Clockodo Holiday Carryover API
  slug: clockodo-holidaycarryover-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage holiday quotas
  name: Clockodo Holiday Quota API
  slug: clockodo-holidayquota-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage individual user rights
  name: Clockodo Individual User Access API
  slug: clockodo-individualuseraccess-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage lump sum services
  name: Clockodo Lump Sum Service API
  slug: clockodo-lumpsumservice-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Query and manage nonbusiness days
  name: Clockodo Nonbusiness Day API
  slug: clockodo-nonbusinessday-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Query and manage nonbusiness groups
  name: Clockodo Nonbusiness Group API
  slug: clockodo-nonbusinessgroup-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage overtime carryovers
  name: Clockodo Overtime Carry API
  slug: clockodo-overtimecarry-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage overtime reductions
  name: Clockodo Overtime Reduction API
  slug: clockodo-overtimereduction-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage projects
  name: Clockodo Project API
  slug: clockodo-project-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Query projects
  name: Clockodo Project Report API
  slug: clockodo-projectreport-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage rates
  name: Clockodo Rate API
  slug: clockodo-rate-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Create Clockodo accounts
  name: Clockodo Register API
  slug: clockodo-register-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage services
  name: Clockodo Service API
  slug: clockodo-service-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage subprojects
  name: Clockodo Subproject API
  slug: clockodo-subproject-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Get subscription info
  name: Clockodo Subscription API
  slug: clockodo-subscription-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage target hours (planned hours)
  name: Clockodo Target Hour API
  slug: clockodo-targethour-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage teams
  name: Clockodo Team API
  slug: clockodo-team-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage co-workers
  name: Clockodo User API
  slug: clockodo-user-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Get non-business days of user
  name: Clockodo User Nonbusiness Day API
  slug: clockodo-usernonbusinessday-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Assign non-business day groups to users and manage time periods
  name: Clockodo User Nonbusiness Group API
  slug: clockodo-usernonbusinessgroup-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Query user reports (e. g. work time evaluation of each day and holiday account of each co-worker)
  name: Clockodo User Report API
  slug: clockodo-userreport-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: The Webhook API from Clockodo — 0 operation(s) for webhook.
  name: Clockodo Webhook API
  slug: clockodo-webhook-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage work times. Work times cannot be edited directly. To edit work times, edit the respective time entries or use requests for change of work time.
  name: Clockodo Work Time API
  slug: clockodo-worktime-api
- baseURL: https://my.clockodo.com/api
  baseurl_source: declared
  description: Manage access groups names and assigned users
  name: Clockodo Access Group API
  slug: clockodo-access-group-api
artifact_total: 53
collections:
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
- group: commercial
  href: https://artifacts.apis.io/clockodo/plans/clockodo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clockodo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/clockodo/rate-limits/clockodo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clockodo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clockodo/finops/clockodo-finops.yml
  title: ''
  type: FinOps
  url: finops/clockodo-finops.yml
- group: other
  href: https://artifacts.apis.io/clockodo/capabilities/clockodo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clockodo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/clockodo/agentic-access/clockodo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clockodo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/clockodo/security/clockodo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clockodo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/clockodo/authentication/clockodo-authentication.yml
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
  href: https://artifacts.apis.io/clockodo/openapi/_original/clockodo-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/clockodo-openapi.yml
- group: docs
  href: https://artifacts.apis.io/clockodo/json-schema/clockodo-entry-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clockodo-entry-schema.json
- group: design
  href: https://artifacts.apis.io/clockodo/json-ld/clockodo-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/clockodo-context.jsonld
- group: design
  href: https://artifacts.apis.io/clockodo/rules/clockodo-rules.yml
  title: ''
  type: Spectral
  url: rules/clockodo-rules.yml
created: '2025-02-17'
description: 'Clockodo is a German-built, cloud-based time-tracking and project- management application used by service firms, agencies, and freelancers. In addition to its web and mobile apps, Clockodo exposes a REST API at my.clockodo.com that mirrors the objects in the UI: time entries, customers, projects, services, users, absences, holiday quotas, lump-sum services, and a real-time stop-clock. Authentication uses a per-user email plus per-user API key delivered as the X-ClockodoApiUser/X-ClockodoApiKey header pair (or HTTP Basic), and every call must include the X-Clockodo-External-Application header identifying the integrating application.'
finops:
- has_sources: false
  method: generated
  name: Clockodo Finops
  primary_unit: request
  service_category: API
  slug: clockodo-finops
  template: true
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
mcp_servers:
- description: Remote MCP server at mcp.clockodo.com over HTTP.
  name: Clockodo MCP Server
  slug: clockodo
modified: '2026-05-19'
name: Clockodo
nav: Providers
network: true
overview: 'Clockodo publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clock API, Absence API, Access Group Access API, and 29 more. Tagged areas include Absence Management, Billing, Project Management, Stopclock, and Time Tracking.


  The Clockodo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clockodo''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
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
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Clockodo — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clockodo-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
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
  composite: 39.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 65.2
    developer_ergonomics: 23.8
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 73.8
      total: 42
    mcp: first-party
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
screenshot: https://apis.io/screenshots/clockodo/clockodo-2026-06-20T174529.png
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
