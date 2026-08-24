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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Workday Advanced Compensation Agentic Access
  operation_count: 11
  slug: workday-advanced-compensation-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 8
apis:
- description: Manage bonus and incentive plans
  name: Workday Advanced Compensation Bonus Plans API
  slug: workday-advanced-compensation-bonus-plans-api
- description: Manage compensation budgets and allocations
  name: Workday Advanced Compensation Compensation Budgets API
  slug: workday-advanced-compensation-compensation-budgets-api
- description: Manage compensation grade profiles and pay ranges
  name: Workday Advanced Compensation Compensation Grades API
  slug: workday-advanced-compensation-compensation-grades-api
- description: Manage compensation plans and eligibility rules
  name: Workday Advanced Compensation Compensation Plans API
  slug: workday-advanced-compensation-compensation-plans-api
- description: Manage compensation review processes and cycles
  name: Workday Advanced Compensation Compensation Reviews API
  slug: workday-advanced-compensation-compensation-reviews-api
- description: Manage individual employee compensation packages
  name: Workday Advanced Compensation Employee Compensation API
  slug: workday-advanced-compensation-employee-compensation-api
- description: Manage merit increase plans and cycles
  name: Workday Advanced Compensation Merit Plans API
  slug: workday-advanced-compensation-merit-plans-api
- description: Manage equity and stock compensation plans
  name: Workday Advanced Compensation Stock Plans API
  slug: workday-advanced-compensation-stock-plans-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans API
  slug: open-workday-advanced-compensation-bonus-plans-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Compensation Budgets API
  slug: open-workday-advanced-compensation-compensation-budgets-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Compensation Grades API
  slug: open-workday-advanced-compensation-compensation-grades-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Compensation Plans API
  slug: open-workday-advanced-compensation-compensation-plans-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Employee Compensation API
  slug: open-workday-advanced-compensation-employee-compensation-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Merit Plans API
  slug: open-workday-advanced-compensation-merit-plans-api
- collection_type: open
  name: Workday Advanced Compensation Bonus Plans Stock Plans API
  slug: open-workday-advanced-compensation-stock-plans-api
- collection_type: open
  name: Workday Advanced Compensation API
  slug: open-workday-advanced-compensation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-advanced-compensation-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-advanced-compensation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-advanced-compensation-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workday.com/
- group: operate
  title: ''
  type: API Status
  url: https://status.workday.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: auth
  title: ''
  type: Security
  url: https://www.workday.com/en-us/why-workday/security-trust.html
- group: operate
  title: ''
  type: RateLimits
  url: https://doc.workday.com/r/Workday_Web_Services/Workday_Web_Services_Directory/Web_Service_Rate_Limiting
- group: start
  title: ''
  type: Sandbox
  url: https://doc.workday.com/r/en-us/workday-studio/workday-studio-user-guide/sandboxes
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Workday
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workday-advanced-compensation-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-advanced-compensation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-advanced-compensation-vocabulary.yml
created: '2024-01-15'
description: API for managing compensation plans, budgets, allocations, and related processes in Workday.
examples:
- key_count: 8
  name: Workday Advanced Compensation Bonus Plan Example
  slug: workday-advanced-compensation-bonus-plan-example
- key_count: 9
  name: Workday Advanced Compensation Compensation Budget Example
  slug: workday-advanced-compensation-compensation-budget-example
- key_count: 8
  name: Workday Advanced Compensation Compensation Change Request Example
  slug: workday-advanced-compensation-compensation-change-request-example
- key_count: 9
  name: Workday Advanced Compensation Compensation Grade Example
  slug: workday-advanced-compensation-compensation-grade-example
- key_count: 8
  name: Workday Advanced Compensation Compensation Plan Example
  slug: workday-advanced-compensation-compensation-plan-example
- key_count: 8
  name: Workday Advanced Compensation Compensation Review Example
  slug: workday-advanced-compensation-compensation-review-example
- key_count: 9
  name: Workday Advanced Compensation Employee Compensation Example
  slug: workday-advanced-compensation-employee-compensation-example
- key_count: 8
  name: Workday Advanced Compensation Merit Plan Example
  slug: workday-advanced-compensation-merit-plan-example
- key_count: 8
  name: Workday Advanced Compensation Stock Plan Example
  slug: workday-advanced-compensation-stock-plan-example
finops:
- name: Workday Advanced Compensation Finops
  service_category: API
  slug: workday-advanced-compensation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-advanced-compensation.png
json_schemas:
- name: Bonus Plan
  property_count: 8
  slug: workday-advanced-compensation-bonus-plan
- name: Compensation Budget
  property_count: 9
  slug: workday-advanced-compensation-compensation-budget
- name: Compensation Change Request
  property_count: 8
  slug: workday-advanced-compensation-compensation-change-request
- name: Compensation Grade
  property_count: 9
  slug: workday-advanced-compensation-compensation-grade
- name: Compensation Plan
  property_count: 8
  slug: workday-advanced-compensation-compensation-plan
- name: Compensation Review
  property_count: 8
  slug: workday-advanced-compensation-compensation-review
- name: Employee Compensation
  property_count: 9
  slug: workday-advanced-compensation-employee-compensation
- name: Merit Plan
  property_count: 8
  slug: workday-advanced-compensation-merit-plan
- name: Stock Plan
  property_count: 8
  slug: workday-advanced-compensation-stock-plan
json_structures:
- name: Workday Advanced Compensation Bonus Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-bonus-plan-structure
- name: Workday Advanced Compensation Compensation Budget Structure
  property_count: 9
  slug: workday-advanced-compensation-compensation-budget-structure
- name: Workday Advanced Compensation Compensation Change Request Structure
  property_count: 8
  slug: workday-advanced-compensation-compensation-change-request-structure
- name: Workday Advanced Compensation Compensation Grade Structure
  property_count: 9
  slug: workday-advanced-compensation-compensation-grade-structure
- name: Workday Advanced Compensation Compensation Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-compensation-plan-structure
- name: Workday Advanced Compensation Compensation Review Structure
  property_count: 8
  slug: workday-advanced-compensation-compensation-review-structure
- name: Workday Advanced Compensation Employee Compensation Structure
  property_count: 9
  slug: workday-advanced-compensation-employee-compensation-structure
- name: Workday Advanced Compensation Merit Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-merit-plan-structure
- name: Workday Advanced Compensation Stock Plan Structure
  property_count: 8
  slug: workday-advanced-compensation-stock-plan-structure
jsonld:
- class_count: 31
  name: Workday Advanced Compensation Context
  property_count: 17
  slug: workday-advanced-compensation-context
layout: provider
modified: '2026-05-19'
name: Workday Advanced Compensation
nav: Providers
network: true
overview: 'Workday Advanced Compensation publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bonus Plans API, Compensation Budgets API, Compensation Grades API, and 5 more.


  The Workday Advanced Compensation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Advanced Compensation''s developer surface includes authentication, sandbox, and 12 more developer resources.'
plans:
- name: Workday Advanced Compensation Plans Pricing
  plan_count: 3
  slug: workday-advanced-compensation-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Workday Advanced Compensation Rate Limits
  slug: workday-advanced-compensation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Workday Advanced Compensation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-advanced-compensation-jsonschema-spectral-rules
- effective_rule_count: 84
  extends:
  - spectral:oas
  name: Workday Advanced Compensation API Rules
  rule_count: 43
  severity_counts:
    error: 7
    hint: 0
    info: 11
    warn: 25
  slug: workday-advanced-compensation-spectral-rules
scopes:
- name: Workday Advanced Compensation Scopes
  scope_count: 2
  slug: workday-advanced-compensation-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 28.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 29.8
    developer_ergonomics: 19.0
    discoverability: 37.0
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/screenshots/workday-advanced-compensation-2026-06-20T201555.png
security:
- kind: authentication
  name: Workday Advanced Compensation Authentication
  slug: workday-advanced-compensation-authentication
  summary_line: oauth2 · 1 scheme
slug: workday-advanced-compensation
website: https://developer.workday.com/
---
