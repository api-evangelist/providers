---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: TG3D Studio's two RESTful API libraries. ScanAPI (free to partners) controls the Scanatic 360 Body Scanner and registers Cloudzet scan users; APIConnect manipulates data across the Scanatic Body, Nuno
  name: Scanatic APIs (ScanAPI + APIConnect)
  slug: scanatic-apis-scanapi-apiconnect
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tg3d-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tg3ds.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tg3ds.zendesk.com/hc/en-us/categories/900001218663-Business-Integration-with-APIs
- group: docs
  title: ''
  type: Documentation
  url: https://tg3ds.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://tg3ds.zendesk.com/hc/en-us/categories/900001218663-Business-Integration-with-APIs
- group: operate
  title: ''
  type: Support
  url: https://tg3ds.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://strikingly.tg3ds.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tg3ds.com/scanatic-studio-pricing
- group: start
  title: ''
  type: Login
  url: https://api.tg3ds.com/mtm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mtm.tg3ds.com/mtm/activation/legal
- group: auth
  title: ''
  type: Authentication
  url: authentication/tg3d-studio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tg3d-studio-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tg3d-studio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tg3d-studio-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tg3d-studio-plans.yml
created: '2026-07-17'
description: 'TG3D Studio Inc. is a 3D fashion technology company (founded 2016, headquartered in Taiwan) whose Scanatic platform digitizes the body, materials, and clothing for made-to-measure and custom fashion. Its products include the Scanatic 360 Body Scanner (roughly 250 body measurements captured in seconds), Scanatic Studio 3D product-visualization and digital-sampling software, the Cloudzet mobile body-scan app, and the BESPOKE-N virtual try-on app. For developers and partners, TG3D exposes two RESTful API libraries: ScanAPI — offered free to partners for integrating Cloudzet scan-user registration and building custom UI that controls the Scanatic 360 Body Scanner — and APIConnect, which manipulates data across the Scanatic Body, Nuno3D, and StyleBook services. API access is key-based and issued from the Scanatic for Fashion Developer Console; all HTTPS traffic is 256-bit encrypted and each Scanatic Body Service includes up to 1,500 free API requests per month.'
image: https://tg3ds.com/
layout: provider
modified: '2026-07-21'
name: TG3D Studio
nav: Providers
network: true
overview: 'TG3D Studio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Body Scanning, Fashion Technology, Made-to-Measure, and Digital Fashion.


  TG3D Studio''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, and 9 more developer resources.'
plans:
- name: Tg3D Studio Plans
  plan_count: 4
  slug: tg3d-studio-plans
random_paper: 8
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tg3d-studio/refs/heads/main/screenshots/tg3d-studio-2026-09-02T163310.png
security:
- kind: authentication
  name: Tg3D Studio Authentication
  slug: tg3d-studio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tg3D Studio Domain Security
  slug: tg3d-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tg3d-studio
tags:
- Company
- 3D Body Scanning
- Fashion Technology
- Made-to-Measure
- Digital Fashion
- Body Measurement
- Apparel
website: https://tg3ds.com
---
