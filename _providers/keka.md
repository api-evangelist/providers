---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Keka Agentic Access
  operation_count: 99
  slug: keka-agentic-access
  summary_line: 99 operations · 27 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: The Assets API from Keka HR — 5 operation(s) for assets.
  name: Keka HR Assets API
  slug: keka-assets-api
- description: The Attendance API from Keka HR — 7 operation(s) for attendance.
  name: Keka HR Attendance API
  slug: keka-attendance-api
- description: The Authentication API from Keka HR — 1 operation(s) for authentication.
  name: Keka HR Authentication API
  slug: keka-authentication-api
- description: The BGV APIs API from Keka HR — 2 operation(s) for bgv apis.
  name: Keka HR BGV APIs API
  slug: keka-bgv-apis-api
- description: The Core HR API from Keka HR — 14 operation(s) for core hr.
  name: Keka HR Core HR API
  slug: keka-core-hr-api
- description: The Documents API from Keka HR — 3 operation(s) for documents.
  name: Keka HR Documents API
  slug: keka-documents-api
- description: The Expense API from Keka HR — 3 operation(s) for expense.
  name: Keka HR Expense API
  slug: keka-expense-api
- description: The Hire API from Keka HR — 12 operation(s) for hire.
  name: Keka HR Hire API
  slug: keka-hire-api
- description: The Leave API from Keka HR — 4 operation(s) for leave.
  name: Keka HR Leave API
  slug: keka-leave-api
- description: The Payroll API from Keka HR — 11 operation(s) for payroll.
  name: Keka HR Payroll API
  slug: keka-payroll-api
- description: The PMS API from Keka HR — 8 operation(s) for pms.
  name: Keka HR PMS API
  slug: keka-pms-api
- description: The PSA API from Keka HR — 15 operation(s) for psa.
  name: Keka HR PSA API
  slug: keka-psa-api
- description: The Requisitions API from Keka HR — 1 operation(s) for requisitions.
  name: Keka HR Requisitions API
  slug: keka-requisitions-api
- description: The Skills API from Keka HR — 2 operation(s) for skills.
  name: Keka HR Skills API
  slug: keka-skills-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Keka HR Assets API
  slug: open-keka-assets-api
- collection_type: open
  name: Keka HR Assets Attendance API
  slug: open-keka-attendance-api
- collection_type: open
  name: Keka HR Assets Authentication API
  slug: open-keka-authentication-api
- collection_type: open
  name: Keka HR Assets BGV APIs API
  slug: open-keka-bgv-apis-api
- collection_type: open
  name: Keka HR Assets Core HR API
  slug: open-keka-core-hr-api
- collection_type: open
  name: Keka HR Assets Documents API
  slug: open-keka-documents-api
- collection_type: open
  name: Keka HR Assets Expense API
  slug: open-keka-expense-api
- collection_type: open
  name: Keka HR Assets Hire API
  slug: open-keka-hire-api
- collection_type: open
  name: Keka HR Assets Leave API
  slug: open-keka-leave-api
- collection_type: open
  name: Keka HR Assets Payroll API
  slug: open-keka-payroll-api
- collection_type: open
  name: Keka HR Assets PMS API
  slug: open-keka-pms-api
- collection_type: open
  name: Keka HR Assets PSA API
  slug: open-keka-psa-api
- collection_type: open
  name: Keka HR Assets Requisitions API
  slug: open-keka-requisitions-api
- collection_type: open
  name: Keka HR Assets Skills API
  slug: open-keka-skills-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keka-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keka-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keka-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.keka.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.keka.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/keka
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keka-hr
- group: company
  title: ''
  type: Blog
  url: https://www.keka.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keka.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keka.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/kekahr_official
- group: commercial
  title: ''
  type: Plans
  url: plans/keka-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keka-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/keka-finops.yml
created: 2026-06-13
description: Keka is an Indian HR and payroll management platform providing a REST API for managing employee data, attendance, leave, payroll processing, expense management, and performance management. The API uses OAuth 2.0 authentication and supports webhooks for event-driven integrations.
examples:
- key_count: 1
  name: Keka Hr Api Examples
  slug: keka-hr-api-examples
finops:
- name: Keka Finops
  service_category: ''
  slug: keka-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keka.png
json_schemas:
- name: Keka HR API
  property_count: 5
  slug: keka-hr-api
layout: provider
modified: 2026-06-13
name: Keka HR
nav: Providers
network: true
overview: 'Keka HR publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Attendance API, Authentication API, and 11 more. Tagged areas include HR, Human Resources, Payroll, Attendance, and Leave Management.


  The Keka HR catalog on APIs.io includes 1 Spectral governance ruleset.


  Keka HR''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Keka Plans Pricing
  plan_count: 3
  slug: keka-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 1
  name: Keka Rate Limits
  slug: keka-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Keka HR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: keka-jsonschema-spectral-rules
scopes:
- name: Keka Scopes
  scope_count: 1
  slug: keka-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 37.1
  delta: -11.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 9.8
    contract_quality: 52.2
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/keka/refs/heads/main/screenshots/keka-2026-06-20T183947.png
security:
- kind: authentication
  name: Keka Authentication
  slug: keka-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Keka Domain Security
  slug: keka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keka
tags:
- HR
- Human Resources
- Payroll
- Attendance
- Leave Management
- Performance Management
- Employee Management
- India
- HRMS
website: https://www.keka.com/
---
