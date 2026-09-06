---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: In-page JavaScript API exposed by the embedded Sayduck 3D viewer/configurator Web Component. Accessed via DOM CustomEvents (sayduck.api-ready) once the viewer loads, with namespaces for variants, conf
  name: Sayduck 3D Viewer API
  slug: sayduck-3d-viewer-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: http://sayduck.com
- group: start
  title: ''
  type: Portal
  url: https://help.sayduck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sayduck.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.sayduck.com/en/article/3d-viewer-api-documentation-1ftbxnx/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sayduck.com/en/article/getting-started-d0bngy/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.sayduck.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sayduck.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sayduck.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.sayduck.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sayduck.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sayduck.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sayduck
- group: design
  title: ''
  type: Components
  url: components/sayduck-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sayduck-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sayduck-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Sayduck/sayduck-platform-release/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sayduck-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sayduck-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sayduck-domain-security.yml
created: '2026-07-17'
description: Sayduck is a 3D product visualization platform for ecommerce that turns static product pages into interactive shopping experiences. Brands upload 3D assets to a self-service platform and embed them as interactive 3D configurators, WebAR (view-in-your-space) experiences, and virtual product photography. The public integration surface is a browser-native Web Component (`<sayduck-viewer>`) with an in-page JavaScript API driven by DOM CustomEvents; the platform is backed by a GraphQL API internally. Founded in 2012 by Niklas Slotte, part of Goodbye Kansas Group 2019-2023, and independent since 2024 via The Optical Foundry.
image: https://static.wixstatic.com/media/f4f00a_7c822c9db9194c5793d6d732ab9250f7~mv2.png
layout: provider
modified: '2026-07-21'
name: SayDuck
nav: Providers
network: true
overview: 'SayDuck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D, Augmented Reality, E-Commerce, and Product Visualization.


  SayDuck''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 25.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sayduck/refs/heads/main/screenshots/sayduck-2026-09-02T154455.png
security:
- kind: domain-security
  name: Sayduck Domain Security
  slug: sayduck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sayduck
tags:
- Company
- 3D
- Augmented Reality
- E-Commerce
- Product Visualization
- WebAR
- 3D Configurator
- Web Components
website: http://sayduck.com
---
