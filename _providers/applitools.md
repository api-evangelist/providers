---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Applitools Agentic Access
  operation_count: 7
  slug: applitools-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- description: REST API for the Applitools Eyes cloud server. Endpoint groups include Batch Management (results, statistics, properties, deletion), Discussions (list and manage comments), and SCM Integrations (statu
  name: Applitools Eyes Server REST API
  slug: eyes-server-api
- description: 'Visual testing SDKs that integrate with existing test frameworks (Selenium, Cypress, Playwright, WebdriverIO, Puppeteer, Appium, Espresso, XCUI, Robot Framework, Images) across JavaScript/TypeScript, '
  name: Applitools Eyes SDKs
  slug: eyes-sdks
- description: AI-powered no-code platform for end-to-end functional, visual, and API testing. Handles test authoring, result analysis, and provides REST API access for programmatic integration into CI/CD.
  name: Applitools Autonomous
  slug: autonomous
- description: Cloud test execution infrastructure with self-healing capabilities - tests remain functional even when UI elements change. Drop-in remote WebDriver replacement for Selenium, Playwright, and WebdriverI
  name: Applitools Execution Cloud
  slug: execution-cloud
- description: Cross-browser and device visual rendering grid. Renders DOM snapshots captured by Eyes SDKs across many browser/viewport combinations in parallel and applies Visual AI comparison.
  name: Applitools Ultrafast Grid
  slug: ultrafast-grid
- description: Batch management endpoints
  name: Applitools Batches API
  slug: applitools-batches-api
- description: Discussion and comment endpoints
  name: Applitools Discussions API
  slug: applitools-discussions-api
- description: Source-control management integrations
  name: Applitools SCM API
  slug: applitools-scm-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Applitools Eyes Server REST Batches API
  slug: open-applitools-batches-api
- collection_type: open
  name: Applitools Eyes Server REST Batches Discussions API
  slug: open-applitools-discussions-api
- collection_type: open
  name: Applitools Eyes Server REST Batches SCM API
  slug: open-applitools-scm-api
- collection_type: open
  name: Applitools Eyes Server REST API
  slug: open-applitools
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/applitools-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/applitools-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/applitools-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/applitools-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://applitools.com/
- group: docs
  title: ''
  type: Documentation
  url: https://applitools.com/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/applitools
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/applitools
- group: commercial
  title: ''
  type: Plans
  url: plans/applitools-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/applitools-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/applitools-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://applitools.com/blog/feed/
created: '2026-05-23'
description: Applitools is a Visual AI testing platform for end-to-end functional, visual, and API testing. The product line covers Eyes (Visual AI inside existing test frameworks), Autonomous (no-code AI-powered E2E platform), Execution Cloud (self-healing cloud test runner), and Ultrafast Grid (cross-browser/device visual rendering). Applitools exposes a REST server API at eyesapi.applitools.com and ships SDKs for Selenium, Cypress, Playwright, WebdriverIO, Puppeteer, Appium, Espresso, XCUI, Robot Framework, and more across JavaScript, TypeScript, Java, Python, C#, and Ruby.
finops:
- name: Applitools Finops
  service_category: API
  slug: applitools-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/applitools.png
layout: provider
modified: '2026-05-23'
name: Applitools
nav: Providers
network: true
overview: 'Applitools publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batches API, Discussions API, and SCM API. Tagged areas include Testing, Visual AI, Visual Testing, Autonomous Testing, and REST.


  Applitools'' developer surface includes authentication, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Applitools Plans Pricing
  plan_count: 1
  slug: applitools-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Applitools Rate Limits
  slug: applitools-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/applitools/refs/heads/main/screenshots/applitools-2026-06-20T172326.png
security:
- kind: authentication
  name: Applitools Authentication
  slug: applitools-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Applitools Domain Security
  slug: applitools-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Applitools Trust Center
  slug: applitools-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: applitools
tags:
- Testing
- Visual AI
- Visual Testing
- Autonomous Testing
- REST
- SDK
- Cross-Browser
- Execution Cloud
website: https://applitools.com/
---
