---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Token-authenticated REST API for managing an Edools school — team and role administration, content (courses, learning paths, lessons, media), student management and engagement triggers, and school pro
  name: Edools Core API
  slug: edools-core-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://edools.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plataforma.edools.com/desenvolvedores
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edools.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.edools.com/file.05_api.html
- group: operate
  title: ''
  type: Support
  url: https://ajuda.herospark.com/
- group: company
  title: ''
  type: Blog
  url: https://herospark.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://herospark.com/calculadora-de-taxas
- group: start
  title: ''
  type: SignUp
  url: https://app.herospark.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.herospark.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://herospark.com/termos-de-uso-herospark/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://herospark.com/politicas-de-privacidade/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Edools
- group: operate
  title: ''
  type: StatusPage
  url: https://status.herospark.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/edools-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edools-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edools-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edools-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/edools-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/edools-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/edools-cli.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edools-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edools-llms.txt
created: '2026-07-17'
description: Edools is a Brazilian e-learning and digital-education platform for creating, hosting, and selling online courses, learning paths, and training programs under a white-label school (LMS) with a Netflix-style members area, video hosting, and student engagement tools. The platform is now delivered as HeroSpark (edools.com redirects to herospark.com), a digital-product sales suite for course creators covering checkout, payments (SparkPay), members areas, and a student mobile app. Edools exposes a token-authenticated REST API (base host per-school on myedools.com) for team, content, and student management, plus first-party Ruby and PHP client libraries and theme development tooling, letting integrators sync courses, students, enrollments, and school products with external systems.
image: https://herospark.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Edools
nav: Providers
network: true
overview: 'Edools publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, E-Learning, LMS, and Online Courses.


  Edools'' developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 15 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 30.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edools/refs/heads/main/screenshots/edools-2026-07-25T212856.png
security:
- kind: authentication
  name: Edools Authentication
  slug: edools-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Edools Domain Security
  slug: edools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edools
tags:
- Company
- Education
- E-Learning
- LMS
- Online Courses
- EdTech
- Content Management
- Digital Products
- Brazil
- REST
website: https://edools.com
---
