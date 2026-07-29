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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Cloud Farm Management Software for growers and agronomists. Modules cover farm / field / crop data, device management, irrigation scheduling, disease monitoring, nutrition tracking, effluent managemen
  name: CropX Farm Management Software
  slug: fms
- description: In-field IoT hardware - SV soil sensors, ET evapotranspiration sensors, WS weather stations, RG rain gauges, Apex root-zone sensor, and an in-development nitrate sensor - that stream readings to the C
  name: CropX Sensor Hardware
  slug: sensors
- description: TD-series cellular telemetry gateways that connect CropX and third-party sensors to the CropX cloud.
  name: CropX Telemetry Gateways
  slug: telemetry
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cropx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cropx.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cropx.com
- group: company
  title: ''
  type: News
  url: https://cropx.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://cropx.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://cropx.com/blog/
created: '2026-05-23'
description: CropX is an Israeli ag-IoT company that combines in-field soil and weather hardware with a cloud Farm Management Software (FMS) platform. The hardware portfolio includes SV-series soil sensors (moisture, temperature, conductivity, salinity at depth), ET-series evapotranspiration sensors, WS-series weather stations, RG rain gauges, the Apex root-zone sensor, an in-development nitrate sensor, and TD-series cellular telemetry gateways. The FMS covers farm / field / crop data, device management, irrigation scheduling, disease monitoring, nutrition, effluent, and reporting. CropX does not publish a public developer portal; integrations with third-party sensors and machinery are arranged through their team.
finops:
- name: Cropx Finops
  service_category: API
  slug: cropx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cropx.png
layout: provider
modified: '2026-05-23'
name: CropX
nav: Providers
network: true
overview: 'CropX publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, IoT, Soil Sensors, and Irrigation.


  CropX''s developer surface includes product news, engineering blog, and 4 more developer resources.'
plans:
- name: Cropx Plans Pricing
  plan_count: 1
  slug: cropx-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Cropx Rate Limits
  slug: cropx-rate-limits
score:
  band: emerging
  composite: 17.2
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cropx/refs/heads/main/screenshots/cropx-2026-06-20T175242.png
security:
- kind: domain-security
  name: Cropx Domain Security
  slug: cropx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cropx
tags:
- Agriculture
- AgTech
- IoT
- Soil Sensors
- Irrigation
- Farm Management
website: https://cropx.com/
---
