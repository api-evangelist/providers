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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Workday Benefits Agentic Access
  operation_count: 10
  slug: workday-benefits-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 6
apis:
- description: Manage employee benefit enrollments and elections
  name: Workday Benefits Benefit Enrollments API
  slug: workday-benefits-benefit-enrollments-api
- description: Manage benefit qualifying events and open enrollment
  name: Workday Benefits Benefit Events API
  slug: workday-benefits-benefit-events-api
- description: Manage benefit plan definitions and configurations
  name: Workday Benefits Benefit Plans API
  slug: workday-benefits-benefit-plans-api
- description: Manage employee dependents and beneficiaries
  name: Workday Benefits Dependents API
  slug: workday-benefits-dependents-api
- description: Manage individual employee benefit summaries and balances
  name: Workday Benefits Employee Benefits API
  slug: workday-benefits-employee-benefits-api
- description: Manage time off and leave benefit plans
  name: Workday Benefits Time Off Plans API
  slug: workday-benefits-time-off-plans-api
artifact_total: 45
collections:
- collection_type: postman
  name: Workday Benefits Benefit Enrollments API
  slug: postman-workday-benefits-benefit-enrollments-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Benefit Events API
  slug: postman-workday-benefits-benefit-events-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Benefit Plans API
  slug: postman-workday-benefits-benefit-plans-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Dependents API
  slug: postman-workday-benefits-dependents-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Employee Benefits API
  slug: postman-workday-benefits-employee-benefits-api
- collection_type: postman
  name: Workday Benefits Benefit Enrollments Time Off Plans API
  slug: postman-workday-benefits-time-off-plans-api
- collection_type: open
  name: Workday Benefits API
  slug: open-workday-benefits
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-benefits/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-benefits-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-benefits-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-benefits-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-benefits-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-benefits-scopes.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/_wTPrHlQFO6kuhPPQvXUdg
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workday.com
- group: docs
  title: ''
  type: Authentication Guide
  url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/bRN0dJVT1fKqLxCRjJCx6w
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Workday
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/technology.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workday-benefits-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-benefits-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-benefits-vocabulary.yml
created: '2024-01-01'
description: APIs for managing employee benefits, enrollments, and benefits administration in Workday.
examples:
- key_count: 10
  name: Workday Benefits Benefit Enrollment Example
  slug: workday-benefits-benefit-enrollment-example
- key_count: 5
  name: Workday Benefits Benefit Enrollment Request Example
  slug: workday-benefits-benefit-enrollment-request-example
- key_count: 6
  name: Workday Benefits Benefit Event Example
  slug: workday-benefits-benefit-event-example
- key_count: 11
  name: Workday Benefits Benefit Plan Example
  slug: workday-benefits-benefit-plan-example
- key_count: 7
  name: Workday Benefits Dependent Example
  slug: workday-benefits-dependent-example
- key_count: 5
  name: Workday Benefits Employee Benefits Example
  slug: workday-benefits-employee-benefits-example
- key_count: 7
  name: Workday Benefits Time Off Plan Example
  slug: workday-benefits-time-off-plan-example
finops:
- name: Workday Benefits Finops
  service_category: API
  slug: workday-benefits-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-benefits.png
json_schemas:
- name: Benefit Enrollment Request
  property_count: 6
  slug: workday-benefits-benefit-enrollment-request
- name: Benefit Enrollment
  property_count: 10
  slug: workday-benefits-benefit-enrollment
- name: Benefit Event
  property_count: 7
  slug: workday-benefits-benefit-event
- name: Benefit Plan
  property_count: 11
  slug: workday-benefits-benefit-plan
- name: Dependent
  property_count: 7
  slug: workday-benefits-dependent
- name: Employee Benefits
  property_count: 5
  slug: workday-benefits-employee-benefits
- name: Time Off Plan
  property_count: 7
  slug: workday-benefits-time-off-plan
json_structures:
- name: Workday Benefits Benefit Enrollment Request Structure
  property_count: 6
  slug: workday-benefits-benefit-enrollment-request-structure
- name: Workday Benefits Benefit Enrollment Structure
  property_count: 10
  slug: workday-benefits-benefit-enrollment-structure
- name: Workday Benefits Benefit Event Structure
  property_count: 7
  slug: workday-benefits-benefit-event-structure
- name: Workday Benefits Benefit Plan Structure
  property_count: 11
  slug: workday-benefits-benefit-plan-structure
- name: Workday Benefits Dependent Structure
  property_count: 7
  slug: workday-benefits-dependent-structure
- name: Workday Benefits Employee Benefits Structure
  property_count: 5
  slug: workday-benefits-employee-benefits-structure
- name: Workday Benefits Time Off Plan Structure
  property_count: 7
  slug: workday-benefits-time-off-plan-structure
jsonld:
- class_count: 25
  name: Workday Benefits Context
  property_count: 14
  slug: workday-benefits-context
layout: provider
modified: '2026-05-19'
name: Workday Benefits
nav: Providers
network: true
overview: 'Workday Benefits publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Benefit Enrollments API, Benefit Events API, Benefit Plans API, and 3 more.


  The Workday Benefits catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Benefits'' developer surface includes authentication, getting-started guide, engineering blog, and 12 more developer resources.'
plans:
- name: Workday Benefits Plans Pricing
  plan_count: 3
  slug: workday-benefits-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Workday Benefits Rate Limits
  slug: workday-benefits-rate-limits
rules:
- name: Workday Benefits API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-benefits-jsonschema-spectral-rules
- name: Workday Benefits API Rules
  rule_count: 44
  severity_counts:
    error: 7
    hint: 0
    info: 12
    warn: 25
  slug: workday-benefits-spectral-rules
scopes:
- name: Workday Benefits Scopes
  scope_count: 1
  slug: workday-benefits-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 55.4
  delta: -6.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.6
    developer_ergonomics: 43.5
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-benefits/refs/heads/main/screenshots/workday-benefits-2026-06-20T201559.png
security:
- kind: authentication
  name: Workday Benefits Authentication
  slug: workday-benefits-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Workday Benefits Domain Security
  slug: workday-benefits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Benefits Trust Center
  slug: workday-benefits-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-benefits
website: https://developer.workday.com
---
