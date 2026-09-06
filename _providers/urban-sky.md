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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Real-time balloon telemetry feed delivered over WebSocket via the Urban Sky SDK (JavaScript and Python, distributed by CDN loader from sdk.atmosys.com), with balloon and unassigned-device location upd
  name: Urban Sky SDK (Real-time Balloon Telemetry)
  slug: urban-sky-sdk-real-time-balloon-telemetry
artifact_total: 4
asyncapis:
- description: 'Real-time balloon telemetry feed delivered over WebSocket by the Urban Sky SDK (JavaScript and Python). Clients authenticate with an organization-scoped API token and receive push updates for balloon '
  name: Urban Sky Real-time Balloon Telemetry
  slug: urban-sky-telemetry-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://urbansky.com/
- group: company
  title: ''
  type: About
  url: https://urbansky.com/company/about
- group: company
  title: ''
  type: Blog
  url: https://urbansky.com/news
- group: company
  title: ''
  type: Careers
  url: https://urbansky.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://urbansky.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbansky.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbansky.com/terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/urban-sky-strato
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urban-sky
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.urbansky.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urbansky.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.urbansky.com/api/javascript.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.urbansky.com/guide/getting-started.html
- group: build
  title: ''
  type: Packages
  url: packages/urban-sky-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/urban-sky-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urban-sky-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/urban-sky-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/urban-sky-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/urban-sky-conventions.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/urban-sky-telemetry-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urban-sky-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urban-sky-domain-security.yml
created: '2026-07-17'
description: Urban Sky is a Denver-based aerospace company, founded in 2016, that designs and operates reusable stratospheric microballoons for high-altitude remote sensing, persistent aerial surveillance, communications relay, and atmospheric data collection. Its balloons launch in under five minutes, float at 61,000-75,000 feet for multi-day missions, and carry the modular Wallabee payload platform with RGB, VNIR, and LWIR thermal sensors delivering 10cm-resolution imagery with real-time downlink. Through its Atmosys software platform, Urban Sky publishes an SDK for developers (JavaScript and Python, delivered via CDN loader) that streams real-time balloon telemetry over WebSocket and provides mission imagery access, serving defense and intelligence, commercial monitoring, and science and weather markets. Urban Sky is a Techstars portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urban-sky.png
layout: provider
modified: '2026-07-21'
name: Urban Sky
nav: Providers
network: true
overview: 'Urban Sky publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Stratospheric Balloons, Remote Sensing, and Earth Observation.


  The Urban Sky catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Urban Sky''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, sandbox, and 17 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.5
  provenance:
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urban-sky/refs/heads/main/screenshots/urban-sky-2026-09-02T165154.png
security:
- kind: authentication
  name: Urban Sky Authentication
  slug: urban-sky-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Urban Sky Domain Security
  slug: urban-sky-domain-security
  summary_line: TLSv1.3 · DMARC
slug: urban-sky
tags:
- Company
- Aerospace
- Stratospheric Balloons
- Remote Sensing
- Earth Observation
- Aerial Imagery
- Telemetry
- Defense
- Weather
website: https://urbansky.com/
---
