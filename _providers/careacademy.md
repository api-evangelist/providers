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
    agent_skills: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://go.careacademy.com/api/v1
  baseurl_source: declared
  description: The Compliance Report API from CareAcademy — 1 operation(s) for compliance report.
  name: CareAcademy Compliance Report API
  slug: careacademy-compliance-report-api
- baseURL: https://go.careacademy.com/api/v1
  baseurl_source: declared
  description: The Locations API from CareAcademy — 1 operation(s) for locations.
  name: CareAcademy Locations API
  slug: careacademy-locations-api
- baseURL: https://go.careacademy.com/api/v1
  baseurl_source: declared
  description: The Organizations API from CareAcademy — 1 operation(s) for organizations.
  name: CareAcademy Organizations API
  slug: careacademy-organizations-api
- baseURL: https://go.careacademy.com/api/v1
  baseurl_source: declared
  description: The Practitioners API from CareAcademy — 2 operation(s) for practitioners.
  name: CareAcademy Practitioners API
  slug: careacademy-practitioners-api
- baseURL: https://go.careacademy.com/api/v1
  baseurl_source: declared
  description: The Sign In Url API from CareAcademy — 1 operation(s) for sign in url.
  name: CareAcademy Sign In Url API
  slug: careacademy-sign-in-url-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CareAcademy Compliance Report API
  slug: open-careacademy-compliance-report-api
- collection_type: open
  name: CareAcademy Compliance Report Locations API
  slug: open-careacademy-locations-api
- collection_type: open
  name: CareAcademy Compliance Report Organizations API
  slug: open-careacademy-organizations-api
- collection_type: open
  name: CareAcademy Compliance Report Practitioners API
  slug: open-careacademy-practitioners-api
- collection_type: open
  name: CareAcademy Compliance Report Sign In Url API
  slug: open-careacademy-sign-in-url-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/careacademy-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/careacademy-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: CareAcademy
nav: Providers
network: true
overview: 'CareAcademy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Compliance Report API, Locations API, Organizations API, and 2 more. Tagged areas include Company, Training, Education, Compliance, and Home Care.


  CareAcademy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 47.8
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 39.4
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
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/careacademy/refs/heads/main/screenshots/careacademy-2026-08-07T175428.png
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
