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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Thought Industries Agentic Access
  operation_count: 15
  slug: thought-industries-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 7
apis:
- description: The Thought Industries GraphQL API provides flexible querying of platform data including courses, users, content, and enrollments. Available at /incoming/api/graphql with schema introspection supporte
  name: Thought Industries GraphQL API
  slug: graphql-api
- description: Learning content and categories
  name: Thought Industries Content API
  slug: thought-industries-content-api
- description: Course management and content
  name: Thought Industries Courses API
  slug: thought-industries-courses-api
- description: Course enrollment management
  name: Thought Industries Enrollments API
  slug: thought-industries-enrollments-api
- description: User group management
  name: Thought Industries Groups API
  slug: thought-industries-groups-api
- description: Analytics and reporting
  name: Thought Industries Reports API
  slug: thought-industries-reports-api
- description: User lifecycle management
  name: Thought Industries Users API
  slug: thought-industries-users-api
artifact_total: 30
collections:
- collection_type: postman
  name: Thought Industries REST Content API
  slug: postman-thought-industries-content-api
- collection_type: postman
  name: Thought Industries REST Content Courses API
  slug: postman-thought-industries-courses-api
- collection_type: postman
  name: Thought Industries REST Content Enrollments API
  slug: postman-thought-industries-enrollments-api
- collection_type: postman
  name: Thought Industries REST Content Groups API
  slug: postman-thought-industries-groups-api
- collection_type: postman
  name: Thought Industries REST Content Reports API
  slug: postman-thought-industries-reports-api
- collection_type: postman
  name: Thought Industries REST Content Users API
  slug: postman-thought-industries-users-api
- collection_type: open
  name: Thought Industries REST API
  slug: open-thought-industries
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thought-industries/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thought-industries-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/thought-industries-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thought-industries-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thought-industries-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.thoughtindustries.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thought-industries
- group: company
  title: ''
  type: Website
  url: https://www.thoughtindustries.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.thoughtindustries.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.thoughtindustries.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.thoughtindustries.com/api-tutorials/
- group: auth
  title: ''
  type: Authentication
  url: https://academy.thoughtindustries.com/courses/api-keys
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thoughtindustries
- group: design
  title: ''
  type: Webhooks
  url: https://developer.thoughtindustries.com/
- group: operate
  title: ''
  type: Support
  url: https://support.thoughtindustries.com/
created: '2025-03-01'
description: Thought Industries is a B2B learning platform (LMS/LXP) providing REST and GraphQL APIs for programmatic access to courses, users, enrollments, content management, and reporting. Their developer portal enables integration of learning experiences into enterprise workflows with webhook support and comprehensive API coverage for user lifecycle, content, and analytics.
examples:
- key_count: 2
  name: Thought Industries Enroll User Example
  slug: thought-industries-enroll-user-example
- key_count: 2
  name: Thought Industries List Users Example
  slug: thought-industries-list-users-example
finops:
- name: Thought Industries Finops
  service_category: API
  slug: thought-industries-finops
graphqls:
- description: The Thought Industries GraphQL API provides flexible querying of platform data including courses, users, content, and enrollments. Available at /incoming/api/graphql with schema introspection supporte
  name: Thought Industries GraphQL API
  slug: thought-industries-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thought-industries.png
json_schemas:
- name: Enrollment
  property_count: 7
  slug: thought-industries-enrollment
- name: User
  property_count: 8
  slug: thought-industries-user
json_structures:
- name: Thought Industries User Structure
  property_count: 0
  slug: thought-industries-user-structure
jsonld:
- class_count: 20
  name: Thought Industries Context
  property_count: 0
  slug: thought-industries-context
layout: provider
modified: '2026-05-19'
name: Thought Industries
nav: Providers
network: true
overview: 'Thought Industries publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Content API, Courses API, Enrollments API, and 3 more. Tagged areas include Education, Learning, LMS, LXP, and E-Learning.


  The Thought Industries catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Thought Industries'' developer surface includes authentication, engineering blog, documentation, getting-started guide, support, and 10 more developer resources.'
plans:
- name: Thought Industries Plans Pricing
  plan_count: 3
  slug: thought-industries-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 5
  name: Thought Industries Rate Limits
  slug: thought-industries-rate-limits
rules:
- name: Thought Industries API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thought-industries-jsonschema-spectral-rules
- name: Thought Industries API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: thought-industries-rules
score:
  band: strong
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 74.2
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thought-industries/refs/heads/main/screenshots/thought-industries-2026-06-20T195312.png
security:
- kind: authentication
  name: Thought Industries Authentication
  slug: thought-industries-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Thought Industries Domain Security
  slug: thought-industries-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thought Industries Trust Center
  slug: thought-industries-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: thought-industries
tags:
- Education
- Learning
- LMS
- LXP
- E-Learning
- Training
website: https://www.thoughtindustries.com/
---
