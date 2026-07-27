---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Trakstar Agentic Access
  operation_count: 34
  slug: trakstar-agentic-access
  summary_line: 34 operations · 12 acting
api_count: 12
apis:
- description: Authentication and SSO operations
  name: Trakstar Auth API
  slug: trakstar-auth-api
- description: Manage messages sent to candidates
  name: Trakstar Candidate Messages API
  slug: trakstar-candidate-messages-api
- description: Manage job candidates
  name: Trakstar Candidates API
  slug: trakstar-candidates-api
- description: Manage course enrollment and information
  name: Trakstar Courses API
  slug: trakstar-courses-api
- description: Manage candidate evaluations
  name: Trakstar Evaluations API
  slug: trakstar-evaluations-api
- description: Manage user groups
  name: Trakstar Groups API
  slug: trakstar-groups-api
- description: Manage internal notes on candidates
  name: Trakstar Internal Notes API
  slug: trakstar-internal-notes-api
- description: Manage candidate interviews
  name: Trakstar Interviews API
  slug: trakstar-interviews-api
- description: Manage job openings / positions
  name: Trakstar Openings API
  slug: trakstar-openings-api
- description: Manage candidate reviews
  name: Trakstar Reviews API
  slug: trakstar-reviews-api
- description: Manage to-do items
  name: Trakstar To-Dos API
  slug: trakstar-to-dos-api
- description: Manage user accounts
  name: Trakstar Users API
  slug: trakstar-users-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trakstar-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trakstar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trakstar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trakstar-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trakstar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.recruiterbox.com/reference/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/promantek
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trakstar
- group: company
  title: ''
  type: Blog
  url: https://www.trakstar.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trakstar.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hire.trakstar.com/
- group: other
  title: ''
  type: X
  url: https://x.com/trakstar_hr
- group: commercial
  title: ''
  type: Plans
  url: plans/trakstar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trakstar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trakstar-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/trakstar/refs/heads/main/vocabulary/trakstar-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/trakstar/refs/heads/main/json-ld/trakstar-context.jsonld
created: '2026-06-13'
description: Trakstar is an HR performance and talent management platform serving over 3,000 companies with integrated tools for performance appraisals, goal alignment, 360-degree feedback, and employee development tracking. The platform comprises four core products — Hire (applicant tracking), Learn (learning management), Perform (performance management), and Insights (workforce analytics) — each exposing its own REST API. Trakstar Hire offers a v2 REST API for managing openings, candidates, interviews, evaluations, and reviews using API key authentication. Trakstar Learn provides a REST API for user account management, group assignments, course enrollment, and reporting. Acquired by Mitratech in April 2023, Trakstar is SOC 2, GDPR, and CCPA compliant and supports seamless integrations with HRIS, SSO, and communications applications.
examples:
- key_count: 10
  name: Trakstar Hire Candidate Example
  slug: trakstar-hire-candidate-example
- key_count: 8
  name: Trakstar Hire Opening Example
  slug: trakstar-hire-opening-example
- key_count: 6
  name: Trakstar Learn Add Users Example
  slug: trakstar-learn-add-users-example
- key_count: 13
  name: Trakstar Learn User Example
  slug: trakstar-learn-user-example
finops:
- name: Trakstar Finops
  service_category: ''
  slug: trakstar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trakstar.png
json_schemas:
- name: Trakstar Hire Candidate
  property_count: 10
  slug: trakstar-candidate
- name: Trakstar Learn Group
  property_count: 4
  slug: trakstar-group
- name: Trakstar Hire Opening
  property_count: 8
  slug: trakstar-opening
- name: Trakstar Learn User
  property_count: 22
  slug: trakstar-user
jsonld:
- class_count: 2
  name: Trakstar Context
  property_count: 55
  slug: trakstar-context
layout: provider
modified: '2026-06-13'
name: Trakstar
nav: Providers
network: true
overview: 'Trakstar publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Candidate Messages API, Candidates API, and 9 more. Tagged areas include HR, Human Resources, Performance Management, Talent Management, and Applicant Tracking.


  The Trakstar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Trakstar''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Trakstar Plans Pricing
  plan_count: 4
  slug: trakstar-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 0
  name: Trakstar Rate Limits
  slug: trakstar-rate-limits
rules:
- name: Trakstar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trakstar-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.8
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 55.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trakstar/refs/heads/main/screenshots/trakstar-2026-06-20T195534.png
security:
- kind: authentication
  name: Trakstar Authentication
  slug: trakstar-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Trakstar Domain Security
  slug: trakstar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trakstar Trust Center
  slug: trakstar-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: trakstar
tags:
- HR
- Human Resources
- Performance Management
- Talent Management
- Applicant Tracking
- Learning Management
- 360 Feedback
- Goal Management
- Employee Development
- Performance Appraisal
website: https://www.trakstar.com/
---
