---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for the CCO.IO Automated Direct platform. Supports search, retrieval and management of displays, networks, markets, products, orders, bookings, campaigns, creatives, photos, customers, accoun
  name: Clear Channel Outdoor Automated Direct API
  slug: clear-channel-outdoor-direct
artifact_total: 37
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clear-channel-outdoor-hldgs-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://clearchanneloutdoor.com/company-news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clear-channel-outdoor
- group: company
  title: ''
  type: Website
  url: https://www.clearchanneloutdoor.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cco.io
- group: other
  title: ''
  type: ProgrammaticAdvertising
  url: https://clearchanneloutdoor.com/programmatic-advertising/
- group: other
  title: ''
  type: DataSolutions
  url: https://clearchanneloutdoor.com/radar-data-solutions/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ClearChannelOutdoor
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clear-channel-outdoor-hldgs-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clear-channel-outdoor-hldgs-vocabulary.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ClearChannelOutdoor/io-sdk-golang
- group: other
  title: ''
  type: Standards
  url: https://github.com/ClearChannelOutdoor/ooh_open_direct
created: '2026-05-04'
description: Clear Channel Outdoor Holdings is one of the largest out-of-home advertising companies in the world and a Fortune 1000 firm, operating billboards, street furniture, transit, airport, and digital out-of-home displays across the United States and select international markets. CCO operates the CCO.IO developer platform with the Automated Direct API at direct.cco.io for programmatic-direct buying of inventory, supports programmatic digital-out-of-home (pDOOH) buying through 21+ DSP partners using OpenRTB 2.6 with the DOOH extension, and offers RADAR, an audience and attribution data suite based on aggregated mobile location data. Open-source SDKs for the Automated Direct API are published under the ClearChannelOutdoor GitHub organization.
examples:
- key_count: 2
  name: Clear Channel Outdoor Direct Create Order Example
  slug: clear-channel-outdoor-direct-create-order-example
- key_count: 2
  name: Clear Channel Outdoor Direct Search Displays Example
  slug: clear-channel-outdoor-direct-search-displays-example
- key_count: 7
  name: Clear Channel Outdoor Hldgs Openrtb Dooh Bid Request Example
  slug: clear-channel-outdoor-hldgs-openrtb-dooh-bid-request-example
finops:
- name: Clear Channel Outdoor Hldgs Finops
  service_category: API
  slug: clear-channel-outdoor-hldgs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clear-channel-outdoor-hldgs.png
integrations:
- description: pDOOH buying via Adelphic DSP integration.
  name: Adelphic
- description: pDOOH buying via Adform DSP integration.
  name: Adform
- description: pDOOH buying via Adomni DSP integration.
  name: Adomni
- description: pDOOH buying via AdQuick DSP integration.
  name: AdQuick
- description: pDOOH buying via Campsite DSP integration.
  name: Campsite
- description: pDOOH buying via Displayce DSP integration.
  name: Displayce
- description: pDOOH buying via Google Display & Video 360 DSP integration.
  name: Google DV360
- description: pDOOH buying via Hivestack DSP/SSP integration.
  name: Hivestack
- description: pDOOH buying via Nexxen DSP integration.
  name: Nexxen
- description: pDOOH buying via OneView (Roku) DSP integration.
  name: OneView
- description: pDOOH buying via OutMoove DSP integration.
  name: OutMoove
- description: pDOOH buying via Pulsepoint DSP integration.
  name: Pulsepoint
- description: pDOOH buying via Quotient DSP integration.
  name: Quotient
- description: pDOOH buying via Simplifi DSP integration.
  name: Simplifi
- description: pDOOH buying via Sito DSP integration.
  name: Sito
- description: pDOOH buying via StackAdapt DSP integration.
  name: StackAdapt
- description: pDOOH buying via The Trade Desk DSP integration.
  name: The Trade Desk
- description: pDOOH buying via Vistar Media DSP/SSP integration.
  name: Vistar Media
- description: pDOOH buying via Xandr DSP integration.
  name: Xandr
- description: pDOOH buying via Yahoo DSP integration.
  name: Yahoo
- description: pDOOH buying via Zeta DSP integration.
  name: Zeta
json_schemas:
- name: DOOH Display
  property_count: 12
  slug: clear-channel-outdoor-hldgs-display
- name: DSP Integration
  property_count: 10
  slug: clear-channel-outdoor-hldgs-dsp-integration
- name: OpenRTB DOOH Bid Request (CCO Profile)
  property_count: 8
  slug: clear-channel-outdoor-hldgs-openrtb-dooh
- name: OOH Order
  property_count: 14
  slug: clear-channel-outdoor-hldgs-order
json_structures:
- name: Clear Channel Outdoor Hldgs Pdooh Supply Chain Structure
  property_count: 0
  slug: clear-channel-outdoor-hldgs-pdooh-supply-chain-structure
jsonld:
- class_count: 31
  name: Clear Channel Outdoor Hldgs Context
  property_count: 23
  slug: clear-channel-outdoor-hldgs-context
layout: provider
modified: '2026-05-05'
name: Clear Channel Outdoor Holdings
nav: Providers
network: true
overview: 'Clear Channel Outdoor Holdings publishes 1 API on the [APIs.io](https://apis.io/) network: Clear Channel Outdoor Automated Direct API. Tagged areas include Advertising, Out Of Home, Programmatic, Digital Out Of Home, and pDOOH.


  The Clear Channel Outdoor Holdings catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clear Channel Outdoor Holdings'' developer surface includes engineering blog, GitHub presence, and 10 more developer resources.'
plans:
- name: Clear Channel Outdoor Hldgs Plans Pricing
  plan_count: 1
  slug: clear-channel-outdoor-hldgs-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 2
  name: Clear Channel Outdoor Hldgs Rate Limits
  slug: clear-channel-outdoor-hldgs-rate-limits
rules:
- name: Clear Channel Outdoor Holdings API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: clear-channel-outdoor-direct-rules
- name: Clear Channel Outdoor Holdings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: clear-channel-outdoor-hldgs-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.5
    developer_ergonomics: 17.4
    discoverability: 85.0
    governance: 39.5
    operational_transparency: 26.3
  previous_composite: 40.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clear-channel-outdoor-hldgs/refs/heads/main/screenshots/clear-channel-outdoor-hldgs-2026-06-20T174457.png
security:
- kind: domain-security
  name: Clear Channel Outdoor Hldgs Domain Security
  slug: clear-channel-outdoor-hldgs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clear-channel-outdoor-hldgs
tags:
- Advertising
- Out Of Home
- Programmatic
- Digital Out Of Home
- pDOOH
- OpenRTB
- OpenDirect
website: https://www.clearchanneloutdoor.com
---
