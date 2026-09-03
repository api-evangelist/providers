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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: 'Asynchronous bulk data API for downloading chlorophyll-fluorescence (ChF) and Gardin-indices data. Submit a query, poll its status, then download the result set as CSV. Supports control-area, device, '
  name: Gardin Query API
  slug: gardin-query-api
- description: Device registry and control API to list and find sensors, group devices, run and stop measurement / pick-poses jobs, enable or disable schedules, and check command job status.
  name: Gardin Sensor Management API
  slug: gardin-sensor-management-api
- description: Real-time plant-health alert delivery over webhooks and websockets. Emits PLANT_CRITICAL_ALERT, PLANT_STRESS_ALERT, PLANT_LIGHT_ALERT and PLANT_RECOVERY_ALERT events (RAISED / CLOSED) with an HMAC-SHA
  name: Gardin Notification API
  slug: gardin-notification-api
artifact_total: 7
asyncapis:
- description: ''
  name: Gardin Notification Webhooks
  slug: gardin-notification-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://gardin.ag/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gardin.ag/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gardin.ag/docs/dev-guide/getting-started/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gardin.ag/docs/gardin-api/gardin-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gardin.ag/docs/dev-guide/getting-started/welcome
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.gardin.ag/docs/dev-guide/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gardin.ag/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gardinltd
- group: company
  title: ''
  type: Blog
  url: https://gardin.ag/news
- group: operate
  title: ''
  type: Support
  url: https://gardin.ag/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gardin.ag/documents/GardinPrivacyNotice.pdf
- group: auth
  title: ''
  type: Authentication
  url: authentication/gardin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gardin-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gardin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gardin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gardin-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gardin-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gardin-notification-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/gardin-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gardin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gardin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gardin-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gardin-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gardin-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gardin-data-model.yml
created: '2026-07-17'
description: Gardin is a UK-based agritech company (Abingdon, Oxfordshire) whose product, Gardin Pulse, is a real-time plant-level crop intelligence platform built on an optical sensor that measures chlorophyll fluorescence to assess photosynthetic efficiency. The sensors detect crop stress weeks before visible symptoms appear, letting growers optimise lighting, irrigation and climate control across glasshouses, polytunnels and indoor farms. Gardin exposes this plant-health data to growers and developers through the Gardin API — a set of OAuth2 client-credentials-secured HTTP services covering sensor/device management, an asynchronous bulk Query API for chlorophyll-fluorescence and Gardin-indices data, and a Notification API that delivers real-time plant alerts over webhooks and websockets. Gardin also integrates plant feedback into leading climate-control systems including Priva, Ridder and LetsGrow.
image: https://gardin.ag/_astro/get-started.BY5JeD8x.png
layout: provider
modified: '2026-07-19'
name: Gardin
nav: Providers
network: true
overview: 'Gardin publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgriTech, Precision Agriculture, and Plant Health.


  The Gardin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gardin''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 20
scopes:
- name: Gardin Scopes
  scope_count: 11
  slug: gardin-scopes
  summary_line: 11 scopes
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 42.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gardin/refs/heads/main/screenshots/gardin-2026-07-25T215444.png
security:
- kind: authentication
  name: Gardin Authentication
  slug: gardin-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Gardin Domain Security
  slug: gardin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gardin
tags:
- Company
- Agriculture
- AgriTech
- Precision Agriculture
- Plant Health
- Photosynthesis
- IoT
- Sensors
- Greenhouse
- Crop Intelligence
- Sustainability
- Data
website: https://gardin.ag/
---
