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
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.life360.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/life360-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/life360-security.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/life360-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/life360-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/life360-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/life360-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/life360
- group: design
  title: ''
  type: Conformance
  url: conformance/life360-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/life360-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.life360.com/
- group: operate
  title: ''
  type: Support
  url: https://support.life360.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.life360.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.life360.com/plans-pricing
- group: start
  title: ''
  type: Login
  url: https://www.life360.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.corp.life360.com/hc/en-us/articles/16124856472471-Life360-Terms-of-Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.corp.life360.com/hc/en-us/articles/16038777217175-Life360-Privacy-Policy
- group: company
  title: ''
  type: Press
  url: https://www.life360.com/press
created: '2026-07-17'
description: Life360 is a family safety platform built around a location-sharing mobile app for iOS and Android, offering real-time member location, Place Alerts, location history, driving safety scores and trip history, crash detection, SOS alerts and emergency dispatch, plus digital safety features such as identity theft protection and dark web monitoring. Its hardware line, following the acquisitions of Tile and Jiobit, spans Tile Mate, Pro, Slim and Sticker Bluetooth item trackers and a cellular GPS pet tracker, sold direct and through Amazon, Best Buy, Target and Walmart. The service is sold as Free, Silver, Gold and Platinum membership tiers. Life360 publishes no public developer API, no OpenAPI, no SDKs and no developer portal — its only machine-readable surface is an agent-facing one (llms.txt, an ai-plugin manifest whose advertised OpenAPI does not resolve, and Content-Signal directives in robots.txt). This profile is maintained in the API Evangelist network for company discovery
  and monitoring.
image: https://www.life360.com/svgs/life360-logo-dark.svg
layout: provider
modified: '2026-07-19'
name: Life360
nav: Providers
network: true
overview: 'Life360 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Family Safety, Location, and GPS Tracking.


  Life360''s developer surface includes support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 20.4
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/life360/refs/heads/main/screenshots/life360-2026-07-25T225034.png
security:
- kind: domain-security
  name: Life360 Domain Security
  slug: life360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Life360 Vulnerability Disclosure
  slug: life360-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: life360
tags:
- Company
- Consumer
- Family Safety
- Location
- GPS Tracking
- Bluetooth Trackers
- Mobile Apps
- Driving Safety
- Wearables
- Subscription
website: https://www.life360.com/
---
