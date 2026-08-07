---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Leapsome Agentic Access
  operation_count: 36
  slug: leapsome-agentic-access
  summary_line: 36 operations · 12 acting
api_count: 14
apis:
- description: The absences API from Leapsome — 1 operation(s) for absences.
  name: Leapsome absences API
  slug: leapsome-absences-api
- description: The accessRoles API from Leapsome — 1 operation(s) for accessroles.
  name: Leapsome accessRoles API
  slug: leapsome-accessroles-api
- description: The auth API from Leapsome — 1 operation(s) for auth.
  name: Leapsome auth API
  slug: leapsome-auth-api
- description: The documents API from Leapsome — 2 operation(s) for documents.
  name: Leapsome documents API
  slug: leapsome-documents-api
- description: The feedback API from Leapsome — 4 operation(s) for feedback.
  name: Leapsome feedback API
  slug: leapsome-feedback-api
- description: The goals API from Leapsome — 6 operation(s) for goals.
  name: Leapsome goals API
  slug: leapsome-goals-api
- description: Operations on groups belonging to an organization
  name: Leapsome Groups API
  slug: leapsome-groups-api
- description: The Leapsome API API from Leapsome — 1 operation(s) for leapsome api.
  name: Leapsome Leapsome API API
  slug: leapsome-leapsome-api-api
- description: The payroll API from Leapsome — 2 operation(s) for payroll.
  name: Leapsome payroll API
  slug: leapsome-payroll-api
- description: The reviews API from Leapsome — 4 operation(s) for reviews.
  name: Leapsome reviews API
  slug: leapsome-reviews-api
- description: Operations on schemas
  name: Leapsome Schemas API
  slug: leapsome-schemas-api
- description: The timeTracking API from Leapsome — 1 operation(s) for timetracking.
  name: Leapsome timeTracking API
  slug: leapsome-timetracking-api
- description: The users API from Leapsome — 4 operation(s) for users.
  name: Leapsome users API
  slug: leapsome-users-api
- description: The workLocations API from Leapsome — 1 operation(s) for worklocations.
  name: Leapsome workLocations API
  slug: leapsome-worklocations-api
artifact_total: 36
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leapsome-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/leapsome-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leapsome-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leapsome-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.leapsome.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.leapsome.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Leapsome
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leapsome
- group: company
  title: ''
  type: Blog
  url: https://www.leapsome.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leapsome.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leapsome.tech/
- group: other
  title: ''
  type: X
  url: https://x.com/leapsome
- group: commercial
  title: ''
  type: Plans
  url: plans/leapsome-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leapsome-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leapsome-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/leapsome-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/leapsome-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/leapsome-api-examples.json
created: '2026-06-13'
description: Leapsome is an AI-powered people enablement platform that combines HRIS, talent management, and HR automation into a single modular solution used by more than 2,000 organizations worldwide. The platform covers the full employee lifecycle including performance reviews, OKRs and goal management, engagement surveys, 1:1 meetings, instant feedback, learning pathways, and compensation management. Leapsome exposes a REST Content API for extracting reviews, goals, employee attributes, payroll, and time-tracking data, plus a SCIM 2.0 API for automated user provisioning and lifecycle management with enterprise identity providers. Both APIs authenticate via bearer tokens generated inside the platform settings and are documented through Swagger UI at api.leapsome.com.
examples:
- key_count: 2
  name: Leapsome Api Examples
  slug: leapsome-api-examples
finops:
- name: Leapsome Finops
  service_category: ''
  slug: leapsome-finops
graphqls:
- description: Leapsome is a people enablement platform for performance management. The API covers performance reviews, OKRs and goals, learning paths, employee surveys, compensation cycles, and engagement analytics
  name: Leapsome GraphQL API
  slug: leapsome-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leapsome.png
json_schemas:
- name: Absence
  property_count: 16
  slug: leapsome-absence
- name: Employee
  property_count: 27
  slug: leapsome-employee
- name: FeedbackItem
  property_count: 10
  slug: leapsome-feedbackitem
- name: Goal
  property_count: 17
  slug: leapsome-goal
- name: PayrollCycle
  property_count: 15
  slug: leapsome-payrollcycle
- name: SCIM Group
  property_count: 6
  slug: leapsome-scim-group
- name: SCIM GroupDefinition
  property_count: 2
  slug: leapsome-scim-groupdefinition
- name: SCIM User
  property_count: 14
  slug: leapsome-scim-user
- name: SCIM UserDefinition
  property_count: 10
  slug: leapsome-scim-userdefinition
- name: Timesheet
  property_count: 10
  slug: leapsome-timesheet
- name: WorkLocation
  property_count: 14
  slug: leapsome-worklocation
jsonld:
- class_count: 5
  name: Leapsome Context
  property_count: 10
  slug: leapsome-context
layout: provider
modified: '2026-06-13'
name: Leapsome
nav: Providers
network: true
overview: 'Leapsome publishes 14 APIs on the [APIs.io](https://apis.io/) network, including absences API, accessRoles API, auth API, and 11 more. Tagged areas include People Enablement, Performance Management, OKRs, Goals, and Engagement Surveys.


  The Leapsome catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Leapsome''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, and 14 more developer resources.'
plans:
- name: Leapsome Plans Pricing
  plan_count: 2
  slug: leapsome-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Leapsome Rate Limits
  slug: leapsome-rate-limits
rules:
- name: Leapsome API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: leapsome-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.6
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 74.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leapsome/refs/heads/main/screenshots/leapsome-2026-06-20T184400.png
security:
- kind: authentication
  name: Leapsome Authentication
  slug: leapsome-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leapsome Domain Security
  slug: leapsome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Leapsome Trust Center
  slug: leapsome-trust-center
  summary_line: trust center published
slug: leapsome
tags:
- People Enablement
- Performance Management
- OKRs
- Goals
- Engagement Surveys
- HRIS
- SCIM
- Employee Development
- 1:1 Meetings
- Learning
website: https://www.leapsome.com/
---
