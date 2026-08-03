---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Powerschool Agentic Access
  operation_count: 15
  slug: powerschool-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 8
apis:
- description: OAuth 2.0 token operations
  name: PowerSchool Authentication API
  slug: powerschool-authentication-api
- description: Course catalog information
  name: PowerSchool Courses API
  slug: powerschool-courses-api
- description: District-level resources
  name: PowerSchool District API
  slug: powerschool-district-api
- description: System metadata and configuration
  name: PowerSchool Metadata API
  slug: powerschool-metadata-api
- description: Named PowerQuery endpoints for complex data retrieval
  name: PowerSchool PowerQuery API
  slug: powerschool-powerquery-api
- description: School information and management
  name: PowerSchool Schools API
  slug: powerschool-schools-api
- description: Course sections and scheduling
  name: PowerSchool Sections API
  slug: powerschool-sections-api
- description: Student demographics, enrollment, and records
  name: PowerSchool Students API
  slug: powerschool-students-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/powerschool-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/powerschool-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powerschool-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/powerschool-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.powerschool.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.powerschool.com/developer/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/powerschool
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/powerschool-group-llc/
- group: company
  title: ''
  type: Blog
  url: https://www.powerschool.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.powerschool.com/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powerschool.com/
- group: other
  title: ''
  type: X
  url: https://x.com/mypowerschool
- group: commercial
  title: ''
  type: Plans
  url: plans/powerschool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/powerschool-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/powerschool-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/powerschool-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/powerschool-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/powerschool-student.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/powerschool-school.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/powerschool-section.json
created: 2026-06-13
description: PowerSchool is the leading provider of cloud-based K-12 student information system (SIS) software in North America, serving over 5,300 districts and 17 million students across 56 states and provinces. The PowerSchool REST API enables third-party developers and district integrators to access and manipulate student records, grades, attendance, enrollment, scheduling, and district-level reporting data programmatically. Authentication is handled via OAuth 2.0 client credentials, with client IDs and secrets provisioned through the PowerSchool Plugin Management Dashboard. PowerSchool supports 75+ certified third-party integrations and custom API partnerships aligned with Ed-Fi Alliance and 1EdTech interoperability standards.
examples:
- key_count: 1
  name: Powerschool Get Schools Response
  slug: powerschool-get-schools-response
- key_count: 1
  name: Powerschool Get Students Response
  slug: powerschool-get-students-response
- key_count: 5
  name: Powerschool Oauth Token Request
  slug: powerschool-oauth-token-request
- key_count: 5
  name: Powerschool Powerquery Section Enrollments Request
  slug: powerschool-powerquery-section-enrollments-request
finops:
- name: Powerschool Finops
  service_category: ''
  slug: powerschool-finops
graphqls:
- description: PowerSchool provides K-12 student information systems. The API covers students, enrollments, courses, grades, attendance records, assignments, teachers, sections, parents, and district reporting for S
  name: PowerSchool GraphQL API
  slug: powerschool-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/powerschool.png
json_schemas:
- name: PowerSchool School
  property_count: 11
  slug: powerschool-school
- name: PowerSchool Section
  property_count: 9
  slug: powerschool-section
- name: PowerSchool Student
  property_count: 7
  slug: powerschool-student
jsonld:
- class_count: 0
  name: Powerschool Context
  property_count: 13
  slug: powerschool-context
layout: provider
modified: 2026-06-13
name: PowerSchool
nav: Providers
network: true
overview: 'PowerSchool publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Courses API, District API, and 5 more. Tagged areas include K-12, Education, Student Information System, SIS, and Students.


  The PowerSchool catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PowerSchool''s developer surface includes authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Powerschool Plans Pricing
  plan_count: 3
  slug: powerschool-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Powerschool Rate Limits
  slug: powerschool-rate-limits
rules:
- name: PowerSchool API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: powerschool-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 71.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powerschool/refs/heads/main/screenshots/powerschool-2026-06-20T192035.png
security:
- kind: authentication
  name: Powerschool Authentication
  slug: powerschool-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Powerschool Domain Security
  slug: powerschool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Powerschool Trust Center
  slug: powerschool-trust-center
  summary_line: SOC 2, ISO 27001
slug: powerschool
tags:
- K-12
- Education
- Student Information System
- SIS
- Students
- Grades
- Attendance
- Enrollment
- Scheduling
- EdTech
website: https://www.powerschool.com/
---
