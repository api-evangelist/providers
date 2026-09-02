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
- description: REST API for provisioning and managing Class virtual classrooms — Classes, Enrollments, Schedules, Templates, Users, launch links, and attendance / metrics reporting. 27 endpoints across 7 resource gr
  name: Class API
  slug: class-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.class.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.class.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.class.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.class.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.class.com
- group: operate
  title: ''
  type: Support
  url: https://support.class.com
- group: company
  title: ''
  type: Blog
  url: https://www.class.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.class.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.class.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.class.com/terms-of-service
- group: auth
  title: ''
  type: TrustCenter
  url: security/class-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.class.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/class-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/class-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/class-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/class-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/class-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/class-llms.txt
created: '2026-07-17'
description: Class (Class Technologies Inc.) is an edtech company providing a next-generation virtual classroom platform for instructor-led live learning. Built on Zoom and Microsoft Teams and delivered on the web as Class Collaborate, it adds teaching and engagement tools — interactive breakout rooms, engagement analytics, course templates, and automated attendance — and integrates with major learning management systems (Canvas, D2L Brightspace, Blackboard Learn, Docebo, Cornerstone OnDemand, Open LMS). Class serves K-12 schools, higher education, government, healthcare, financial services, and corporate training. Class publishes a REST API for managing classes, enrollments, schedules, templates, users, launch links, and reporting, authenticated with scoped API keys.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/class.png
layout: provider
modified: '2026-07-18'
name: Class
nav: Providers
network: true
overview: 'Class publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EdTech, Education, Virtual Classroom, and Learning.


  Class'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 30.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/class/refs/heads/main/screenshots/class-2026-07-25T205513.png
security:
- kind: authentication
  name: Class Authentication
  slug: class-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Class Domain Security
  slug: class-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Class Trust Center
  slug: class-trust-center
  summary_line: SOC 2, ISO 27001
slug: class
tags:
- Company
- EdTech
- Education
- Virtual Classroom
- Learning
- LMS
- Video Conferencing
- Live Learning
website: https://www.class.com
---
