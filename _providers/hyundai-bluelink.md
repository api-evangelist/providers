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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyundai-bluelink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://owners.hyundaiusa.com/us/en/bluelink.html
- group: other
  title: ''
  type: Overview
  url: https://www.hyundaiusa.com/us/en/owners/connected-services
- group: other
  title: ''
  type: BluelinkPlus
  url: https://owners.hyundaiusa.com/us/en/page/blue-link-plus-sign-up.html
- group: commercial
  title: ''
  type: TermsAndConditions
  url: https://owners.hyundaiusa.com/us/en/page/bluelink-terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyundaiusa.com/us/en/privacy-policy
- group: commercial
  title: ''
  type: ConnectedCarPrivacy
  url: https://www.hyundaiusa.com/us/en/connected-car-privacy
- group: other
  title: ''
  type: MobileAppIOS
  url: https://apps.apple.com/us/app/myhyundai-with-bluelink/id850284574
- group: other
  title: ''
  type: MobileAppAndroid
  url: https://play.google.com/store/apps/details?id=com.hyundai.bluelink
- group: start
  title: ''
  type: OwnerPortal
  url: https://owners.hyundaiusa.com/
- group: operate
  title: ''
  type: OwnerSupport
  url: https://owners.hyundaiusa.com/us/en/contact-us
- group: operate
  title: ''
  type: BluelinkSupport
  url: https://owners.hyundaiusa.com/us/en/bluelink-support.html
- group: other
  title: ''
  type: EVCharging
  url: https://www.hyundaiusa.com/us/en/electric/charging
- group: agent
  title: ''
  type: AlexaSkill
  url: https://www.amazon.com/Hyundai-Motor-America-Bluelink/dp/B073XB5XYL
- group: company
  title: ''
  type: Newsroom
  url: https://www.hyundainews.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.hyundai.com/
- group: other
  title: ''
  type: USCompany
  url: https://www.hyundaiusa.com/
- group: build
  title: ''
  type: CommunityClientPython
  url: https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api
- group: build
  title: ''
  type: CommunityClientHomeAssistant
  url: https://github.com/Hyundai-Kia-Connect/kia_uvo
- group: build
  title: ''
  type: CommunityClientNode
  url: https://github.com/Hacksore/bluelinky
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Hyundai
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Hyundai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/HyundaiUSA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyundai-motor-company
- group: other
  title: ''
  type: RelatedProvider
  url: https://github.com/api-evangelist/hyundai
created: '2026-05-25'
description: Hyundai Bluelink is Hyundai Motor America's connected vehicle service for Hyundai owners, providing remote vehicle control, vehicle status and diagnostics, navigation and route services, safety and security features, and EV-specific charging and climate management. Bluelink is delivered to owners through the MyHyundai with Bluelink mobile app (iOS and Android), the in-vehicle infotainment head unit, the owner web portal at owners.hyundaiusa.com, and connected smart-home and voice integrations (Amazon Alexa, Google Assistant, smartwatch apps). Feature sets vary by model year and subscription tier — typically Bluelink, Bluelink+, and Bluelink Connected Care / Remote / Guidance bundles — and include remote start with climate, remote door lock/unlock, remote horn and lights, vehicle finder, stolen vehicle recovery and SVI, automatic collision notification, SOS emergency assistance, monthly vehicle health reports, destination search (powered by Google), in-vehicle Wi-Fi hotspot (via
  AT&T on supported models), and EV-specific remote charge start/stop, charge schedule, charge-level monitoring, and pre-conditioning. Bluelink is a consumer-facing, owner-authenticated service. Hyundai does not publish a public developer portal, public OpenAPI specification, or self-serve API keys for third-party integration with Bluelink vehicle endpoints; access is limited to authenticated owners through Hyundai's first-party apps and to enterprise partners under contract (fleet, insurance telematics, charging networks, smart-home platforms). A community ecosystem of reverse-engineered, unofficial Python and Node.js clients (Hyundai-Kia-Connect/hyundai_kia_connect_api, Home Assistant integrations, Bluelinky) is used by enthusiasts and home automation users, but these are not endorsed, supported, or governed by Hyundai and may break at any time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyundai-bluelink.png
layout: provider
modified: '2026-05-25'
name: Hyundai Bluelink
nav: Providers
network: true
overview: 'Hyundai Bluelink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Connected Vehicles, Telematics, Automotive, Remote Vehicle Control, and Vehicle Diagnostics.


  Hyundai Bluelink''s developer surface includes YouTube channel and 24 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyundai-bluelink/refs/heads/main/screenshots/hyundai-bluelink-2026-06-20T183107.png
security:
- kind: domain-security
  name: Hyundai Bluelink Domain Security
  slug: hyundai-bluelink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyundai-bluelink
tags:
- Connected Vehicles
- Telematics
- Automotive
- Remote Vehicle Control
- Vehicle Diagnostics
- Electric Vehicles
- EV Charging
- Stolen Vehicle Recovery
- Automatic Collision Notification
- Roadside Assistance
- In-Vehicle Wi-Fi
- Navigation
- Smart Home Integration
- Voice Assistant
- Hyundai
- Bluelink
website: https://owners.hyundaiusa.com/us/en/bluelink.html
---
