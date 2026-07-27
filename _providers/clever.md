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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Clever Agentic Access
  operation_count: 51
  slug: clever-agentic-access
  summary_line: 51 operations · 4 acting
api_count: 11
apis:
- description: OAuth 2.0, OIDC, and SAML-based single sign-on integration that enables application partners to authenticate students, teachers, and staff through the Clever portal. Issues bearer access tokens scoped
  name: Clever Single Sign-On API
  slug: clever-single-sign-on-api
- description: Delta-sync event stream API that notifies application partners of changes to roster data (creates, updates, deletes) within a district. Must be enabled via the application dashboard and uses a distric
  name: Clever Events API
  slug: clever-events-api
- description: The Assignments API from Clever — 3 operation(s) for assignments.
  name: Clever Assignments API
  slug: clever-assignments-api
- description: The Courses API from Clever — 6 operation(s) for courses.
  name: Clever Courses API
  slug: clever-courses-api
- description: The Districts API from Clever — 2 operation(s) for districts.
  name: Clever Districts API
  slug: clever-districts-api
- description: The Resources API from Clever — 5 operation(s) for resources.
  name: Clever Resources API
  slug: clever-resources-api
- description: The Schools API from Clever — 7 operation(s) for schools.
  name: Clever Schools API
  slug: clever-schools-api
- description: The Sections API from Clever — 8 operation(s) for sections.
  name: Clever Sections API
  slug: clever-sections-api
- description: The Submissions API from Clever — 1 operation(s) for submissions.
  name: Clever Submissions API
  slug: clever-submissions-api
- description: The Terms API from Clever — 5 operation(s) for terms.
  name: Clever Terms API
  slug: clever-terms-api
- description: The Users API from Clever — 9 operation(s) for users.
  name: Clever Users API
  slug: clever-users-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clever-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clever-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clever-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clever-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clever-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clever-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://clever.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.clever.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/clever-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clever-inc-/
- group: company
  title: ''
  type: Blog
  url: https://www.clever.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clever.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clever.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/clever
- group: commercial
  title: ''
  type: Plans
  url: plans/clever-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clever-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clever-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clever-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/clever-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clever-user.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clever-student.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clever-school.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clever-section.json
- group: build
  title: ''
  type: Examples
  url: examples/clever-user-example.json
- group: build
  title: ''
  type: Examples
  url: examples/clever-student-example.json
- group: build
  title: ''
  type: Examples
  url: examples/clever-district-example.json
- group: build
  title: ''
  type: Examples
  url: examples/clever-section-example.json
created: 2026-06-13
description: Clever is a K-12 EdTech identity platform that provides a unified single sign-on portal and roster synchronization service used by over 111,000 US schools, including 95 of the largest 100 districts. The Clever REST API enables application partners to securely access real-time student roster data, school and district information, class and section data, and user identity records through a single integration. Clever Complete offers Secure Sync for district-managed rostering, LMS Connect for gradebook syncing, and Single Sign-On via OAuth 2.0, OIDC, and SAML, eliminating the need for per-SIS integrations. Approximately 60 percent of US students log in monthly through Clever, making it the de facto identity layer for K-12 EdTech applications across the United States.
examples:
- key_count: 2
  name: Clever District Example
  slug: clever-district-example
- key_count: 2
  name: Clever Section Example
  slug: clever-section-example
- key_count: 2
  name: Clever Student Example
  slug: clever-student-example
- key_count: 2
  name: Clever User Example
  slug: clever-user-example
finops:
- name: Clever Finops
  service_category: ''
  slug: clever-finops
graphqls:
- description: Clever provides a native GraphQL API endpoint alongside its REST API, offering a flexible query interface for K-12 education roster data. The GraphQL API allows application partners to request precise
  name: Clever GraphQL API
  slug: clever-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clever.png
json_schemas:
- name: School
  property_count: 16
  slug: clever-school
- name: Section
  property_count: 18
  slug: clever-section
- name: Student
  property_count: 28
  slug: clever-student
- name: User
  property_count: 8
  slug: clever-user
jsonld:
- class_count: 68
  name: Clever Context
  property_count: 17
  slug: clever-context
layout: provider
modified: 2026-06-13
name: Clever
nav: Providers
network: true
overview: 'Clever publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Events API, Assignments API, Courses API, and 7 more. Tagged areas include Education, K-12, EdTech, Single Sign-On, and Rostering.


  The Clever catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clever''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, and 22 more developer resources.'
plans:
- name: Clever Plans Pricing
  plan_count: 3
  slug: clever-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 0
  name: Clever Rate Limits
  slug: clever-rate-limits
rules:
- name: Clever API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clever-jsonschema-spectral-rules
scopes:
- name: Clever Scopes
  scope_count: 5
  slug: clever-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 59.3
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 53.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clever/refs/heads/main/screenshots/clever-2026-06-20T174509.png
security:
- kind: authentication
  name: Clever Authentication
  slug: clever-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Clever Domain Security
  slug: clever-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clever Vulnerability Disclosure
  slug: clever-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clever Trust Center
  slug: clever-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: clever
tags:
- Education
- K-12
- EdTech
- Single Sign-On
- Rostering
- Identity
- SSO
- Student Data
- LMS
- SIS
website: https://clever.com
---
