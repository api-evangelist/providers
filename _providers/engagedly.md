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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Engagedly Agentic Access
  operation_count: 34
  slug: engagedly-agentic-access
  summary_line: 34 operations · 19 acting
api_count: 8
apis:
- description: Access praise and recognition activities
  name: Engagedly Activities API
  slug: engagedly-activities-api
- description: Handle business unit operations
  name: Engagedly Businesses API
  slug: engagedly-businesses-api
- description: Create and manage organizational departments
  name: Engagedly Departments API
  slug: engagedly-departments-api
- description: Define and manage job roles
  name: Engagedly Job Titles API
  slug: engagedly-job-titles-api
- description: Manage office locations and addresses
  name: Engagedly Locations API
  slug: engagedly-locations-api
- description: List available permission roles
  name: Engagedly Permissions API
  slug: engagedly-permissions-api
- description: Retrieve system and custom user attribute definitions
  name: Engagedly User Attributes API
  slug: engagedly-user-attributes-api
- description: Manage user profiles, permissions, and activation status
  name: Engagedly Users API
  slug: engagedly-users-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/engagedly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/engagedly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/engagedly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://engagedly.com
- group: docs
  title: ''
  type: Documentation
  url: https://engagedly.github.io/api-docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/engagedly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/9246522/
- group: company
  title: ''
  type: Blog
  url: https://engagedly.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://engagedly.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.engagedly.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/engagedlyInc
- group: commercial
  title: ''
  type: Plans
  url: plans/engagedly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/engagedly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/engagedly-finops.yml
created: '2026-06-13'
description: Engagedly is a people strategy execution platform with a REST API for managing performance reviews, goal tracking, 360 feedback, learning paths, and employee recognition programs. The API enables programmatic access to users, departments, locations, job titles, activities, and organizational data using header-based authentication with client and secret keys.
examples:
- key_count: 18
  name: Create User Request
  slug: create-user-request
- key_count: 3
  name: List Praises Response
  slug: list-praises-response
- key_count: 3
  name: List Users Response
  slug: list-users-response
finops:
- name: Engagedly Finops
  service_category: ''
  slug: engagedly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/engagedly.png
json_schemas:
- name: Engagedly User
  property_count: 26
  slug: engagedly-user
jsonld:
- class_count: 26
  name: Engagedly Context
  property_count: 42
  slug: engagedly-context
layout: provider
modified: '2026-06-13'
name: Engagedly
nav: Providers
network: true
overview: 'Engagedly publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Businesses API, Departments API, and 5 more. Tagged areas include Performance Management, HR Software, Employee Engagement, Goal Tracking, and 360 Feedback.


  The Engagedly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Engagedly''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Engagedly Plans Pricing
  plan_count: 8
  slug: engagedly-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Engagedly Rate Limits
  slug: engagedly-rate-limits
rules:
- name: Engagedly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: engagedly-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/engagedly/refs/heads/main/screenshots/engagedly-2026-06-20T180715.png
security:
- kind: authentication
  name: Engagedly Authentication
  slug: engagedly-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Engagedly Domain Security
  slug: engagedly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: engagedly
tags:
- Performance Management
- HR Software
- Employee Engagement
- Goal Tracking
- 360 Feedback
- Learning Management
- Employee Recognition
- Talent Management
- OKR
- People Operations
website: https://engagedly.com
---
