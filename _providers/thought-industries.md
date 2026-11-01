---
access_model:
  confidence: medium
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Thought Industries Agentic Access
  operation_count: 15
  slug: thought-industries-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
apis:
- description: The Thought Industries GraphQL API provides flexible querying of platform data including courses, users, content, and enrollments. Available at /incoming/api/graphql with schema introspection supporte
  name: Thought Industries GraphQL API
  slug: graphql-api
- baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
  baseurl_source: declared
  description: Learning content and categories
  name: Thought Industries Content API
  slug: thought-industries-content-api
- baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
  baseurl_source: declared
  description: Course management and content
  name: Thought Industries Courses API
  slug: thought-industries-courses-api
- baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
  baseurl_source: declared
  description: Course enrollment management
  name: Thought Industries Enrollments API
  slug: thought-industries-enrollments-api
- baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
  baseurl_source: declared
  description: User group management
  name: Thought Industries Groups API
  slug: thought-industries-groups-api
- baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
  baseurl_source: declared
  description: Analytics and reporting
  name: Thought Industries Reports API
  slug: thought-industries-reports-api
- baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
  baseurl_source: declared
  description: User lifecycle management
  name: Thought Industries Users API
  slug: thought-industries-users-api
artifact_total: 36
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
  name: Thought Industries REST Content API
  slug: open-thought-industries-content-api
- collection_type: open
  name: Thought Industries REST Content Courses API
  slug: open-thought-industries-courses-api
- collection_type: open
  name: Thought Industries REST Content Enrollments API
  slug: open-thought-industries-enrollments-api
- collection_type: open
  name: Thought Industries REST Content Groups API
  slug: open-thought-industries-groups-api
- collection_type: open
  name: Thought Industries REST Content Reports API
  slug: open-thought-industries-reports-api
- collection_type: open
  name: Thought Industries REST Content Users API
  slug: open-thought-industries-users-api
- collection_type: open
  name: Thought Industries REST API
  slug: open-thought-industries
common:
- group: commercial
  href: https://artifacts.apis.io/thought-industries/plans/thought-industries-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thought-industries-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/thought-industries/rate-limits/thought-industries-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thought-industries-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/thought-industries/finops/thought-industries-finops.yml
  title: ''
  type: FinOps
  url: finops/thought-industries-finops.yml
- group: other
  href: https://artifacts.apis.io/thought-industries/capabilities/thought-industries-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thought-industries-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thought-industries/overview
- group: agent
  href: https://artifacts.apis.io/thought-industries/agentic-access/thought-industries-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thought-industries-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/thought-industries/security/thought-industries-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thought-industries-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/thought-industries/security/thought-industries-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thought-industries-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/thought-industries/authentication/thought-industries-authentication.yml
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
- has_sources: false
  method: generated
  name: Thought Industries Finops
  primary_unit: request
  service_category: API
  slug: thought-industries-finops
  template: true
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
overview: 'Thought Industries publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Content API, Courses API, Enrollments API, and 4 more. Tagged areas include Education, Learning, LMS, LXP, and E-Learning.


  The Thought Industries catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Thought Industries'' developer surface includes authentication, engineering blog, documentation, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Thought Industries Plans Pricing
  plan_count: 3
  slug: thought-industries-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Thought Industries Rate Limits
  slug: thought-industries-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Thought Industries — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thought-industries-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Thought Industries API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: thought-industries-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 59.5
    developer_ergonomics: 51.2
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thought-industries/thought-industries-2026-06-20T195312.png
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
