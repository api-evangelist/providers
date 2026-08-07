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
- acting_count: 0
  human_in_the_loop: 0
  name: Culture Amp Agentic Access
  operation_count: 19
  slug: culture-amp-agentic-access
  summary_line: 19 operations
api_count: 3
apis:
- description: The Employees API from Culture Amp — 3 operation(s) for employees.
  name: Culture Amp Employees API
  slug: culture-amp-employees-api
- description: The Performance API from Culture Amp — 6 operation(s) for performance.
  name: Culture Amp Performance API
  slug: culture-amp-performance-api
- description: The Surveys API from Culture Amp — 10 operation(s) for surveys.
  name: Culture Amp Surveys API
  slug: culture-amp-surveys-api
artifact_total: 24
collections:
- collection_type: postman
  name: Culture Amp Public Employees API
  slug: postman-culture-amp-employees-api
- collection_type: postman
  name: Culture Amp Public Employees Performance API
  slug: postman-culture-amp-performance-api
- collection_type: postman
  name: Culture Amp Public Employees Surveys API
  slug: postman-culture-amp-surveys-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/culture-amp/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/culture-amp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/culture-amp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/culture-amp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/culture-amp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/culture-amp-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cultureamp.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.cultureamp.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cultureamp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cultureamp
- group: other
  title: ''
  type: X
  url: https://x.com/CultureAmp
- group: company
  title: ''
  type: Blog
  url: https://www.cultureamp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cultureamp.com/platform/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cultureamp.com
- group: commercial
  title: ''
  type: Plans
  url: plans/culture-amp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/culture-amp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/culture-amp-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/culture-amp-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/culture-amp-context.jsonld
created: 2026-06-12
description: Culture Amp is the leading employee experience platform providing tools for employee engagement surveys, performance management, and people analytics. The Culture Amp Public API is a RESTful, read-only interface that enables organizations to programmatically retrieve their people data—including employee records, demographics, performance cycles, manager reviews, and survey results—for use in external systems and custom analytics. The API uses OAuth 2.0 Client Credentials Flow for authentication and is available to all Culture Amp subscribers at no additional cost as part of standard subscription fees. The platform serves thousands of organizations worldwide and integrates with leading HRIS systems, Slack, Microsoft Teams, and compensation tools like Pave.
examples:
- key_count: 1
  name: Culture Amp Employee Example
  slug: culture-amp-employee-example
- key_count: 2
  name: Culture Amp Employees List Example
  slug: culture-amp-employees-list-example
- key_count: 1
  name: Culture Amp Manager Review Example
  slug: culture-amp-manager-review-example
- key_count: 1
  name: Culture Amp Performance Cycle Example
  slug: culture-amp-performance-cycle-example
finops:
- name: Culture Amp Finops
  service_category: ''
  slug: culture-amp-finops
graphqls:
- description: Culture Amp is an employee experience platform. The API covers employee surveys, engagement scores, performance reviews, goal tracking, 1-on-1 meetings, action plans, and workforce analytics for HR te
  name: Culture Amp GraphQL API
  slug: culture-amp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/culture-amp.png
json_schemas:
- name: Employee
  property_count: 10
  slug: culture-amp-employee
- name: ManagerReview
  property_count: 15
  slug: culture-amp-manager-review
- name: PerformanceCycle
  property_count: 6
  slug: culture-amp-performance-cycle
jsonld:
- class_count: 52
  name: Culture Amp Context
  property_count: 24
  slug: culture-amp-context
layout: provider
modified: 2026-06-12
name: Culture Amp
nav: Providers
network: true
overview: 'Culture Amp publishes 3 APIs on the [APIs.io](https://apis.io/) network: Employees API, Performance API, and Surveys API. Tagged areas include HR, Employee Engagement, Performance Management, People Analytics, and Surveys.


  The Culture Amp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Culture Amp''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Culture Amp Plans Pricing
  plan_count: 4
  slug: culture-amp-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Culture Amp Rate Limits
  slug: culture-amp-rate-limits
rules:
- name: Culture Amp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: culture-amp-jsonschema-spectral-rules
scopes:
- name: Culture Amp Scopes
  scope_count: 4
  slug: culture-amp-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: strong
  composite: 59.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 79.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/culture-amp/refs/heads/main/screenshots/culture-amp-2026-06-20T175332.png
security:
- kind: authentication
  name: Culture Amp Authentication
  slug: culture-amp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Culture Amp Domain Security
  slug: culture-amp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Culture Amp Trust Center
  slug: culture-amp-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: culture-amp
tags:
- HR
- Employee Engagement
- Performance Management
- People Analytics
- Surveys
- Human Resources
website: https://www.cultureamp.com
---
