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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The Compliance Report API from CareAcademy — 1 operation(s) for compliance report.
  name: CareAcademy Compliance Report API
  slug: careacademy-compliance-report-api
- description: The Locations API from CareAcademy — 1 operation(s) for locations.
  name: CareAcademy Locations API
  slug: careacademy-locations-api
- description: The Organizations API from CareAcademy — 1 operation(s) for organizations.
  name: CareAcademy Organizations API
  slug: careacademy-organizations-api
- description: The Practitioners API from CareAcademy — 2 operation(s) for practitioners.
  name: CareAcademy Practitioners API
  slug: careacademy-practitioners-api
- description: The Sign In Url API from CareAcademy — 1 operation(s) for sign in url.
  name: CareAcademy Sign In Url API
  slug: careacademy-sign-in-url-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://careacademy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://activatedinsights.com/training/api/
- group: docs
  title: ''
  type: Documentation
  url: https://app.swaggerhub.com/apis-docs/CareAcademy/CareAcademy/1.0.10
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis-docs/CareAcademy/CareAcademy/1.0.10
- group: start
  title: ''
  type: GettingStarted
  url: https://activatedinsights.com/training/api/
- group: operate
  title: ''
  type: Support
  url: https://help.careacademy.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://careacademy.com/resources/?_sorting_by_category=blog
- group: commercial
  title: ''
  type: Pricing
  url: https://careacademy.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://go.careacademy.com/signup
- group: start
  title: ''
  type: Login
  url: https://go.careacademy.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careacademy.com/?page_id=603
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://activatedinsights.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.careacademy.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/careacademy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/careacademy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/careacademy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/careacademy-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/careacademy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/careacademy-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/careacademy-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/careacademy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/careacademy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/careacademy-domain-security.yml
created: '2026-07-17'
description: CareAcademy (part of Activated Insights) is an online training, compliance, and workforce-management platform for post-acute care — home care, home health, hospice, and senior living organizations. It automates regulatory training assignment, caregiver onboarding, and audit-ready compliance reporting for 2,500+ organizations and 800K+ caregivers. The CareAcademy API lets integration partners (home-care software platforms) create agency organizations and caregivers, provide Single Sign-On into CareAcademy from their own product, and query course-completion and compliance data in real time. The partner API is an OpenAPI 3.0 REST interface using HTTP Basic authentication, published on SwaggerHub, with named integrations for WellSky, AxisCare, AlayaCare, eRSP, Aaniie, and Spectrum TeleTrack Services.
image: https://careacademy.com/wp-content/uploads/2022/09/CA-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: careacademy-mcp.yml
  slug: careacademy-mcpyml
modified: '2026-07-18'
name: CareAcademy
nav: Providers
network: true
overview: 'CareAcademy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Compliance Report API, Locations API, Organizations API, and 2 more. Tagged areas include Company, Training, Education, Compliance, and Home Care.


  CareAcademy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 69
score:
  band: developing
  composite: 44.3
  delta: -4.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 49.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 48.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Careacademy Authentication
  slug: careacademy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Careacademy Domain Security
  slug: careacademy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: careacademy
tags:
- Company
- Training
- Education
- Compliance
- Home Care
- Home Health
- Hospice
- Senior Living
- Healthcare
- Workforce Management
- Single Sign-On
- Caregivers
website: https://careacademy.com/
---
