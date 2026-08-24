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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: 'REST API for the CCO.IO Automated Direct platform at direct.cco.io. Supports search, retrieval and management of displays, networks, markets, products, orders, bookings, campaigns, creatives, photos, '
  name: Clear Channel Outdoor Automated Direct API
  slug: clear-channel-outdoor-direct
- description: Programmatic digital out-of-home (pDOOH) supply made available through 20+ DSP partners that transact CCO inventory via OpenRTB 2.6 with the DOOH object extension (with imp.qty support and the OpenOOH
  name: Clear Channel Outdoor pDOOH RTB Supply
  slug: pdooh-rtb-supply
- description: 'RADAR is CCO''s first-party audience-planning, attribution and measurement suite built on aggregated and/or anonymous mobile location data licensed from business partners. The suite includes RADARView '
  name: Clear Channel Outdoor RADAR Data Suite
  slug: radar
artifact_total: 39
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clear-channel-outdoor-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://clearchanneloutdoor.com/company-news/
- group: company
  title: ''
  type: Website
  url: https://clearchanneloutdoor.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cco.io
- group: start
  title: ''
  type: Portal
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClearChannelOutdoor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clear-channel-outdoor
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.clearchannel.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearchanneloutdoor.com/privacy-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clear-channel-outdoor-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clear-channel-outdoor-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clear-channel-outdoor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clear-channel-outdoor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clear-channel-outdoor-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ClearChannelOutdoor/io-sdk-golang
- group: other
  title: ''
  type: Standards
  url: https://github.com/ClearChannelOutdoor/ooh_open_direct
- group: other
  title: ''
  type: Products
  url: https://clearchanneloutdoor.com
created: '2026-05-22'
description: 'Clear Channel Outdoor (NYSE: CCO) is one of the largest out-of-home (OOH) advertising companies in the world, operating billboards, street furniture, transit, airport, and digital out-of-home (DOOH) displays across 65+ U.S. markets and 55+ commercial airports, reaching "130 million Americans weekly." The CCO developer surface spans three layers: the CCO.IO Automated Direct REST API at direct.cco.io for programmatic-direct buying of inventory (OAuth 2.0 client credentials, open-source Go SDK at github.com/ClearChannelOutdoor/io-sdk-golang), programmatic digital out-of-home (pDOOH) buying through 20+ DSP partners using OpenRTB 2.6 with the DOOH object extension, and RADAR — CCO''s first-party audience and attribution data suite (RADARView, RADARProof, RADARConnect, RADARSync, Inflight Insights) built on aggregated and anonymous mobile location data. CCO maintains a public fork of the IAB Tech Lab OpenDirect-OOH specification at github.com/ClearChannelOutdoor/ooh_open_direct.'
examples:
- key_count: 2
  name: Clear Channel Outdoor Direct Create Order Example
  slug: clear-channel-outdoor-direct-create-order-example
- key_count: 2
  name: Clear Channel Outdoor Direct Search Displays Example
  slug: clear-channel-outdoor-direct-search-displays-example
- key_count: 7
  name: Clear Channel Outdoor Openrtb Dooh Bid Request Example
  slug: clear-channel-outdoor-openrtb-dooh-bid-request-example
finops:
- name: Clear Channel Outdoor Finops
  service_category: API
  slug: clear-channel-outdoor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clear-channel-outdoor.png
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
  slug: clear-channel-outdoor-display
- name: DSP Integration
  property_count: 10
  slug: clear-channel-outdoor-dsp-integration
- name: OpenRTB DOOH Bid Request (CCO Profile)
  property_count: 8
  slug: clear-channel-outdoor-openrtb-dooh
- name: OOH Order
  property_count: 14
  slug: clear-channel-outdoor-order
json_structures:
- name: Clear Channel Outdoor Pdooh Supply Chain Structure
  property_count: 0
  slug: clear-channel-outdoor-pdooh-supply-chain-structure
jsonld:
- class_count: 31
  name: Clear Channel Outdoor Context
  property_count: 23
  slug: clear-channel-outdoor-context
layout: provider
modified: '2026-05-23'
name: Clear Channel Outdoor
nav: Providers
network: true
overview: 'Clear Channel Outdoor publishes 1 API on the [APIs.io](https://apis.io/) network: Automated Direct API. Tagged areas include Advertising, Out-of-Home, OOH, Programmatic, and Digital Out Of Home.


  The Clear Channel Outdoor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clear Channel Outdoor''s developer surface includes engineering blog, developer portal, GitHub presence, and 17 more developer resources.'
plans:
- name: Clear Channel Outdoor Plans Pricing
  plan_count: 1
  slug: clear-channel-outdoor-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Clear Channel Outdoor Rate Limits
  slug: clear-channel-outdoor-rate-limits
rules:
- effective_rule_count: 7
  extends:
  - '@stoplight/spectral-rulesets/oas'
  name: Clear Channel Outdoor API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: clear-channel-outdoor-direct-rules
- effective_rule_count: 5
  extends: []
  name: Clear Channel Outdoor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: clear-channel-outdoor-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 54.5
    contract_quality: 64.8
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 54.5
    operational_transparency: 23.7
  previous_composite: 41.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clear-channel-outdoor/refs/heads/main/screenshots/clear-channel-outdoor-2026-06-20T174453.png
security:
- kind: domain-security
  name: Clear Channel Outdoor Domain Security
  slug: clear-channel-outdoor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clear-channel-outdoor
tags:
- Advertising
- Out-of-Home
- OOH
- Programmatic
- Digital Out Of Home
- DOOH
- pDOOH
- OpenRTB
- OpenDirect
- Billboards
- Transit Advertising
- Airport Advertising
- Audience Measurement
- Location Data
website: https://clearchanneloutdoor.com
---
