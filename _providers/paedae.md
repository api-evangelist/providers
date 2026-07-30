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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The Applications API from Paedae — 2 operation(s) for applications.
  name: Paedae Applications API
  slug: paedae-applications-api
- description: The Beacon Configurations API from Paedae — 2 operation(s) for beacon configurations.
  name: Paedae Beacon Configurations API
  slug: paedae-beacon-configurations-api
- description: The Beacons API from Paedae — 4 operation(s) for beacons.
  name: Paedae Beacons API
  slug: paedae-beacons-api
- description: The Communications API from Paedae — 7 operation(s) for communications.
  name: Paedae Communications API
  slug: paedae-communications-api
- description: The Places API from Paedae — 2 operation(s) for places.
  name: Paedae Places API
  slug: paedae-places-api
artifact_total: 9
asyncapis:
- description: ''
  name: Paedae Webhooks
  slug: paedae-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paedae-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paedae-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.gimbal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gimbal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gimbal.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gimbal.com/rest.html
- group: start
  title: ''
  type: Portal
  url: https://manager.gimbal.com
- group: start
  title: ''
  type: SignUp
  url: https://manager.gimbal.com
- group: operate
  title: ''
  type: Support
  url: https://support.gimbal.com/hc/en-us/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.gimbal.com
- group: build
  title: ''
  type: Packages
  url: packages/paedae-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paedae-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paedae-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paedae-well-known.yml
created: '2026-07-17'
description: Paedae is the company behind the Gimbal proximity and location platform (a 500 Global portfolio company; paedae.com now redirects to gimbal.com, operated under Infillion). Gimbal provides beacons, geofencing, and a proximity SDK for iOS and Android, plus a Gimbal Manager REST API to manage applications, places, beacons, beacon configurations, and location-triggered communications. Beacon sighting events (Arrived/Departed/Sighted) are delivered via HTTP callbacks. This profile was enriched from the live Gimbal developer surface at docs.gimbal.com and manager.gimbal.com.
image: https://raw.githubusercontent.com/api-evangelist/paedae/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-20'
name: Paedae
nav: Providers
network: true
overview: 'Paedae publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Beacon Configurations API, Beacons API, and 2 more. Tagged areas include Company, Proximity, Location, Beacons, and Geofencing.


  The Paedae catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paedae''s developer surface includes documentation, API reference, developer portal, signup flow, support, and 10 more developer resources.'
random_paper: 34
scopes:
- name: Paedae Scopes
  scope_count: 0
  slug: paedae-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  delta: -1.8
  facets:
    commercial_clarity: 13.2
    contract_quality: 66.3
    developer_ergonomics: 36.4
    discoverability: 85.2
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 39.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Paedae Authentication
  slug: paedae-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Paedae Domain Security
  slug: paedae-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paedae
tags:
- Company
- Proximity
- Location
- Beacons
- Geofencing
- Mobile SDK
- Advertising
- Marketing
website: https://www.gimbal.com
---
