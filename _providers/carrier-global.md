---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: REST API surface exposing Lynx Fleet telematics and control data for diesel and electric transport refrigeration units (TRUs). Enables systems integrators to pull asset inventory, setpoints, temperatu
  name: Carrier Lynx Fleet API
  slug: lynx-fleet-api
- description: i-Vu is Carrier's web-based commercial building automation system for monitoring and controlling HVAC, lighting, and related building systems. It integrates with BACnet and other standard building pro
  name: Carrier i-Vu Building Automation
  slug: i-vu-building-automation
- description: Carrier Comfort Network (CCN) is Carrier's proprietary control and communication network for tying together chillers, air handlers, and related HVAC equipment, typically integrated into BMS/BAS deploy
  name: Carrier Comfort Network
  slug: carrier-comfort-network
- description: Abound is Carrier's cloud-based building intelligence platform that aggregates data from HVAC, IAQ sensors, and occupancy systems to provide indoor-environmental-quality analytics, energy insights, an
  name: Carrier Abound
  slug: abound-building-platform
- description: The Carrier SmartHome app lets homeowners remotely control Carrier connected smart thermostats and residential HVAC equipment. No public developer API is currently published; integration is via the co
  name: Carrier SmartHome App
  slug: carrier-smarthome
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carrier-global-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carrier
- group: company
  title: ''
  type: Website
  url: https://www.corporate.carrier.com
- group: other
  title: ''
  type: ConsumerSite
  url: https://www.carrier.com/us/en/
- group: docs
  title: ''
  type: Documentation
  url: https://doc-api.fleet.lynx.carrier.io/
- group: start
  title: ''
  type: Portal
  url: https://api.tta.lynxfleet.carrier.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc-api.fleet.lynx.carrier.io/api-documentation
- group: other
  title: ''
  type: Abound
  url: https://www.carrier.com/commercial/en/us/software/abound/
- group: other
  title: ''
  type: BuildingAutomation
  url: https://www.carrier.com/commercial/en/us/software/building-automation/i-vu-building-automation/
- group: other
  title: ''
  type: SmartHome
  url: https://www.carrier.com/residential/en/us/smart-thermostats/smarthome-app/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.carrier.com
- group: company
  title: ''
  type: Careers
  url: https://careers.corporate.carrier.com
- group: operate
  title: ''
  type: Contact
  url: https://www.corporate.carrier.com/contact-us/
- group: agent
  title: ''
  type: LlmsText
  url: https://doc-api.fleet.lynx.carrier.io/llms.txt
created: '2026-03-21'
description: Carrier Global Corporation is a global provider of healthy, safe, sustainable, and intelligent building and cold-chain solutions, spanning HVAC, refrigeration, fire, security, and building automation technologies. Its digital ecosystem includes the Lynx Fleet telematics platform (Lynx APIs for transport refrigeration units), the Abound building management platform, i-Vu and Carrier Comfort Network for commercial building automation, and the Carrier SmartHome app for residential smart thermostats.
finops:
- name: Carrier Global Finops
  service_category: HVAC / IoT Platform
  slug: carrier-global-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carrier-global.png
jsonld:
- class_count: 0
  name: Carrier Global Context
  property_count: 10
  slug: carrier-global-context
layout: provider
modified: '2026-04-23'
name: Carrier Global
nav: Providers
network: true
overview: 'Carrier Global publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Cold Chain, Telematics, Building Automation, and IoT.


  The Carrier Global catalog on APIs.io includes 1 JSON-LD context.


  Carrier Global''s developer surface includes documentation, developer portal, getting-started guide, and 11 more developer resources.'
plans:
- name: Carrier Global Plans Pricing
  plan_count: 3
  slug: carrier-global-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Carrier Global Rate Limits
  slug: carrier-global-rate-limits
score:
  band: emerging
  composite: 15.4
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carrier-global/refs/heads/main/screenshots/carrier-global-2026-06-20T174016.png
security:
- kind: domain-security
  name: Carrier Global Domain Security
  slug: carrier-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carrier-global
tags:
- HVAC
- Cold Chain
- Telematics
- Building Automation
- IoT
- Refrigeration
- Fortune 500
website: https://www.corporate.carrier.com
---
