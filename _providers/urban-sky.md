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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-19'
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
random_paper: 30
score:
  band: thin
  composite: 34.4
  delta: -4.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 38.9
  provenance:
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
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
