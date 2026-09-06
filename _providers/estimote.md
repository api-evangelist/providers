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
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'REST API for managing Estimote devices (beacons): list and configure devices, associate cloud Attachments (custom key/value data) with a device, and read events reported by LTE beacons. Authenticated '
  name: Estimote Cloud API
  slug: estimote-cloud-api
artifact_total: 4
asyncapis:
- description: ''
  name: Estimote Lte Events Webhooks
  slug: estimote-lte-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://estimote.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.estimote.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.estimote.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.estimote.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.estimote.com/lte-beacon/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://forums.estimote.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.estimote.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Estimote
- group: start
  title: ''
  type: SignUp
  url: https://cloud.estimote.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://estimote.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: authentication/estimote-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/estimote-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/estimote-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/estimote-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/estimote-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/estimote-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/estimote-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/estimote-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/estimote-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/estimote-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estimote-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/estimote-lte-events-webhooks.yml
- group: operate
  title: ''
  type: Community
  url: https://forums.estimote.com/
- group: start
  title: ''
  type: Login
  url: https://cloud.estimote.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://estimote.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://estimote.com/privacy/
created: '2026-07-17'
description: Estimote is a proximity and indoor-location company founded in 2012 that designs Bluetooth Low Energy, Ultra-Wideband (UWB) and LTE-M/NB-IoT beacons together with the Estimote Cloud platform for managing them at fleet scale. The Estimote Cloud REST API lets developers list and configure registered devices, attach contextual key/value data (Attachments) to individual beacons, and consume events reported by LTE beacons, authenticated with an App ID and App Token over HTTP Basic or, in private beta, OAuth 2.0. Native SDKs for iOS, Android, React Native and UWB deliver on-device proximity, indoor positioning, secure iBeacon/Eddystone broadcasting and beacon fleet management. Estimote is backed by a16z and Homebrew.
image: https://estimote.com/favicon.ico
layout: provider
modified: '2026-08-08'
name: Estimote
nav: Providers
network: true
overview: 'Estimote publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location, Proximity, Beacons, and Bluetooth.


  The Estimote catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Estimote''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 19 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 34.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/estimote/refs/heads/main/screenshots/estimote-2026-07-25T213641.png
security:
- kind: authentication
  name: Estimote Authentication
  slug: estimote-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Estimote Domain Security
  slug: estimote-domain-security
  summary_line: TLSv1.3 · DMARC
slug: estimote
tags:
- Company
- Location
- Proximity
- Beacons
- Bluetooth
- IoT
- Indoor Location
- UWB
- Asset Tracking
- Developer Tools
website: https://estimote.com
---
