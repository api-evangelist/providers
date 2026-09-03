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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Canvas Agentic Access
  operation_count: 30
  slug: canvas-agentic-access
  summary_line: 30 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Canvas LMS REST API provides programmatic access to courses, assignments, quizzes, grades, users, enrollments, accounts, discussions, files, modules, rubrics, submissions, SIS imports, and account
  name: Canvas LMS REST API
  slug: canvas-lms-rest-api
- description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and ag
  name: Canvas LMS GraphQL API
  slug: canvas-lms-graphql-api
- description: Canvas supports Learning Tools Interoperability (LTI 1.1 and LTI 1.3 / Advantage) for embedding external tools, assignments, and content into courses with deep linking, grade passback, and names-and-r
  name: Canvas LTI Integrations
  slug: canvas-lti-integrations
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: spec
  description: The Courses API from Canvas — 25 operation(s) for courses.
  name: Canvas Courses API
  slug: canvas-courses-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canvas LMS REST API ( subset) Courses API
  slug: open-canvas-courses-api
- collection_type: open
  name: Canvas LMS REST API (Courses subset)
  slug: open-canvas
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/instructure/canvas-lms/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/instructure/canvas-lms/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/instructure/canvas-lms/blob/master/code_of_conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/instructure/canvas-lms/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/instructure/canvas-lms/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/canvas-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canvas-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canvas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canvas-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/canvaslms
- group: company
  title: ''
  type: Website
  url: https://www.instructure.com/canvas
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instructure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/instructure/canvas-lms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instructure.com/
- group: operate
  title: ''
  type: Community
  url: https://community.canvaslms.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instructure.com/policies/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instructure.com/policies/product-acceptable-use
- group: company
  title: ''
  type: Blog
  url: https://www.instructure.com/resources/blog
created: '2025-01-14'
description: Canvas is Instructure's open-source learning management system (LMS) used by K-12, higher education, and corporate training organizations to deliver courses, assessments, and learner communication. Canvas exposes a comprehensive REST API and a GraphQL endpoint for reading and modifying courses, assignments, quizzes, grades, users, enrollments, content, and account administration, and it integrates with external tools through LTI, Caliper, and live event streams.
finops:
- name: Canvas Finops
  service_category: API
  slug: canvas-finops
graphqls:
- description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and ag
  name: Canvas GraphQL API
  slug: canvas-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canvas.png
layout: provider
modified: '2026-04-23'
name: Canvas
nav: Providers
network: true
overview: 'Canvas publishes 1 API on the [APIs.io](https://apis.io/) network: Courses API. Tagged areas include Education, EdTech, GraphQL, Learning Management System, and LMS.


  Canvas'' developer surface includes authentication, documentation, engineering blog, and 17 more developer resources.'
plans:
- name: Canvas Plans Pricing
  plan_count: 3
  slug: canvas-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Canvas Rate Limits
  slug: canvas-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 12.4
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/screenshots/canvas-2026-06-20T173929.png
security:
- kind: authentication
  name: Canvas Authentication
  slug: canvas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Canvas Domain Security
  slug: canvas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canvas Vulnerability Disclosure
  slug: canvas-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Canvas Trust Center
  slug: canvas-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: canvas
tags:
- Education
- EdTech
- GraphQL
- Learning Management System
- LMS
- LTI
- Open-Source
- REST
website: https://www.instructure.com/canvas
---
