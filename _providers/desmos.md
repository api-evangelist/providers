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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Client-side JavaScript API for embedding interactive Desmos calculators (Graphing, 3D, Geometry, Scientific, Four-Function) into web pages and apps, controlled through a browser object model.
  name: Desmos API
  slug: desmos-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.desmos.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.desmos.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.desmos.com/api/v1.12/docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.desmos.com/api/v1.12/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.desmos.com/api/v1.12/docs/index.html
- group: start
  title: ''
  type: SignUp
  url: https://www.desmos.com/my-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.desmos.com/api/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.desmos.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/desmos-lifecycle.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.desmos.com/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.desmos.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.desmos.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/desmosinc
- group: design
  title: ''
  type: Components
  url: components/desmos-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/desmos-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/desmos-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/desmos-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/desmos-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/desmos-llms.txt
created: '2026-07-17'
description: Desmos (Desmos Studio PBC) is the dead-simple way to embed rich, interactive math into a web page or web app. Its developer product is not a REST API but a client-side JavaScript library that mounts embeddable calculators — a full-featured Graphing Calculator, a 3D Calculator, and Geometry, Scientific, and Four-Function calculators — controlled through a browser object model (expressions, graph state, screenshots, and events). The API loads via a single versioned script include and authenticates with an API key passed as a URL parameter. Founded in 2011 by Eli Luberoff and originally backed by GV, the world-renowned Desmos calculators now operate as an independent public benefit corporation and remain free to all, while the Desmos curriculum business was acquired by Amplify in 2022.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/desmos.png
layout: provider
modified: '2026-07-18'
name: Desmos
nav: Providers
network: true
overview: 'Desmos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Education, Mathematics, and Graphing Calculator.


  Desmos'' developer surface includes documentation, API reference, getting-started guide, signup flow, changelog, engineering blog, authentication, and 12 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 32.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 32.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/desmos/refs/heads/main/screenshots/desmos-2026-07-25T211755.png
security:
- kind: authentication
  name: Desmos Authentication
  slug: desmos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Desmos Domain Security
  slug: desmos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: desmos
tags:
- Company
- Consumer
- Education
- Mathematics
- Graphing Calculator
- Embeddable
- JavaScript
- EdTech
- Data Visualization
website: https://www.desmos.com
---
