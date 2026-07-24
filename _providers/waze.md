---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: URL-invocation API to open the Waze app from an external link to locate an address, drop a pin, or start navigation. Query params include ll (lat,lon), q (search), navigate, z (zoom), favorite, and av
  name: Waze Deep Links
  slug: waze-deep-links
- description: Embeddable client-side component that renders the interactive Waze Live Map inside a web page via an <iframe>, with zoom, lat, lon, pin, and desc parameters. No authentication required.
  name: Waze iFrame (Live Map)
  slug: waze-iframe-live-map
- description: 'Partner data-exchange for road closures, incidents, and working vehicles using CIFS (preferred), WZDx, DATEX II, or ESRI formats; Waze returns a partner-specific JSON alerts feed. Provisioned through '
  name: Waze for Cities Data Feeds
  slug: waze-for-cities-data-feeds
- description: Partner-gated SDK for transportation apps to add ETA and routing points and trip-data collection using Waze real-time traffic and location data.
  name: Waze Transport SDK
  slug: waze-transport-sdk
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://waze.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/waze
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/waze
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/waze/deeplinks
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/waze/partners
- group: operate
  title: ''
  type: Community
  url: https://www.waze.com/discuss/
- group: company
  title: ''
  type: Blog
  url: https://blog.waze.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.waze.com/en/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waze.com/en/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/waze-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/waze-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/waze-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waze-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/waze-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/waze-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/waze-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/waze-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/waze-llms.txt
created: '2026-07-17'
description: Waze is a Google-owned, community-driven navigation and real-time traffic application. Its developer surface is not a self-service JSON REST API but a set of public URL-invocation and embed contracts plus partner-gated data and SDK programs. Waze Deep Links open the Waze app from a URL to locate an address, drop a pin, or start turn-by-turn navigation; the Waze iFrame embeds the interactive Live Map in any web page; Waze for Cities Data Feeds let agencies exchange road-closure, incident, and working-vehicle data (CIFS, WZDx, DATEX II, ESRI) and receive a partner-specific JSON alerts feed; the Waze Transport SDK gives transportation apps ETA/routing and trip-data collection; and the Waze Audio Kit surfaces audio content in-drive. Developer documentation is hosted on Google for Developers at developers.google.com/waze and partner programs are provisioned through the Waze Partner Hub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waze.png
layout: provider
modified: '2026-07-21'
name: Waze
nav: Providers
network: true
overview: 'Waze publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Navigation, Maps, and Traffic.


  Waze''s developer surface includes documentation, getting-started guide, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Waze Authentication
  slug: waze-authentication
  summary_line: none/partner-provisioned · 2 schemes
- kind: domain-security
  name: Waze Domain Security
  slug: waze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Waze Vulnerability Disclosure
  slug: waze-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: waze
tags:
- Company
- Mobility
- Navigation
- Maps
- Traffic
- Location
- Transportation
- Smart Cities
website: https://waze.com
---
