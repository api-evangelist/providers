---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for managing Infogram projects programmatically — list and copy projects, read and update project entities, upload image assets, publish and unpublish, delete, and export projects as image/PD
  name: Infogram API
  slug: infogram-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://infogram.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.infogram.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.infogram.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.infogram.com/
- group: operate
  title: ''
  type: Support
  url: https://support.infogram.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://infogram.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://infogram.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://infogram.com/signup
- group: start
  title: ''
  type: Login
  url: https://infogram.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infogram.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infogram.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infogram
- group: operate
  title: ''
  type: StatusPage
  url: https://infogram.statuspage.io/
- group: build
  title: ''
  type: Packages
  url: packages/infogram-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infogram-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infogram-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infogram-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/infogram-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infogram-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infogram-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/infogram-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infogram-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infogram-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infogram-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infogram-data-model.yml
created: '2026-07-17'
description: Infogram is a data visualization platform (based in Riga, Latvia, part of the Prezi family) that lets writers, marketers, journalists, researchers, and analysts turn raw data into interactive infographics, charts, maps, reports, and dashboards that can be embedded or shared anywhere. Its REST API at api.infogram.com uses bearer-token authentication and lets developers list and copy projects, read and update project entities (text, charts, images), upload image assets, publish and unpublish projects, delete projects, and export a project as PNG/JPG/PDF or zipped HTML. Long-running export/download tasks are monitored over Server-Sent Events via a task-status stream. First-party client libraries are published for PHP, Java, Node.js, and Ruby.
image: https://cdn.jifo.co/js/dist/f248da3747f83ee2a1a6a8768140ce82.png
layout: provider
modified: '2026-07-19'
name: Infogram
nav: Providers
network: true
overview: 'Infogram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Visualization, Infographics, Charts, and Dashboards.


  Infogram''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 29.4
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infogram/refs/heads/main/screenshots/infogram-2026-07-25T222416.png
security:
- kind: authentication
  name: Infogram Authentication
  slug: infogram-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Infogram Domain Security
  slug: infogram-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: infogram
tags:
- Company
- Data Visualization
- Infographics
- Charts
- Dashboards
- Reporting
- Business Intelligence
- Content
- Embeds
website: https://infogram.com
---
