---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sense-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sense.com
- group: other
  title: ''
  type: Homes
  url: https://sense.com/homes/
- group: other
  title: ''
  type: Utilities
  url: https://sense.com/utilities/
- group: company
  title: ''
  type: Partners
  url: https://sense.com/partners/
- group: company
  title: ''
  type: MeterPartners
  url: https://sense.com/resources/sense-enabled-meter-partners/
- group: other
  title: ''
  type: WebApp
  url: https://home.sense.com/
- group: other
  title: ''
  type: DownloadApp
  url: https://sense.com/homes/download-app/
- group: other
  title: ''
  type: Resources
  url: https://sense.com/resources/
- group: operate
  title: ''
  type: Community
  url: https://community.sense.com
- group: operate
  title: ''
  type: Support
  url: https://help.sense.com/hc/en-us
- group: operate
  title: ''
  type: ContactPartners
  url: https://sense.com/partners/get-in-touch/
- group: company
  title: ''
  type: Careers
  url: https://sense.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sense-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sense
created: '2026-05-25'
description: Sense is a Cambridge, Massachusetts energy-intelligence company that builds a residential energy monitor and machine-learning platform for real-time whole-home electricity disaggregation. The Sense Monitor installs in a home electrical panel, samples voltage and current at one million times per second, and uses signature-based machine-learning models to identify individual appliances and loads behind a single point of measurement. The Sense iOS, Android, and web apps surface device-level usage, always-on load, solar production, time-of-use cost, and goal tracking to homeowners. For utilities and grid operators, Sense embeds its disaggregation software into next-generation AMI 2.0 smart meters through partnerships with meter manufacturers such as Landis+Gyr, providing grid-edge visibility, fault detection, load-management, demand-response, and virtual-power-plant enablement. Sense also runs a partner program for smart-device integration with thermostats, EV chargers, heat pumps,
  and home-service providers. Sense has not released an official public developer API; community developers maintain reverse-engineered, unofficial clients in Python, Node.js, and Home Assistant against an undocumented and unsupported endpoint. Sense's revenue model is hardware sales of the consumer monitor and licensing of its disaggregation software to utilities and meter OEMs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sense-energy.png
layout: provider
modified: '2026-05-25'
name: Sense
nav: Providers
network: true
overview: 'Sense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Home Energy, Energy Monitoring, Electricity, and Smart Meters.


  Sense''s developer surface includes support and 14 more developer resources.'
random_paper: 45
score:
  band: minimal
  composite: 4.3
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sense-energy/refs/heads/main/screenshots/sense-energy-2026-06-20T193703.png
security:
- kind: domain-security
  name: Sense Energy Domain Security
  slug: sense-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sense-energy
tags:
- Energy
- Home Energy
- Energy Monitoring
- Electricity
- Smart Meters
- AMI
- Grid Edge
- Utilities
- Demand Response
- Virtual Power Plant
- Disaggregation
- Machine Learning
- Smart Home
- IoT
- Solar
- Sustainability
website: https://sense.com
---
