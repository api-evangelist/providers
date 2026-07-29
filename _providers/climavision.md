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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/climavision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://climavision.com
- group: company
  title: ''
  type: About
  url: https://climavision.com/about/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.climavision.com/
- group: other
  title: ''
  type: APIAccess
  url: https://docs.climavision.com/docs/access-to-apim-climavision
- group: other
  title: ''
  type: WeatherAPI
  url: https://climavision.com/weather-api/
- group: operate
  title: ''
  type: RadarStatusAPI
  url: https://radardocs.climavision.com/
- group: other
  title: ''
  type: RadarAsAService
  url: https://climavision.com/radar-as-a-service/
- group: other
  title: ''
  type: HorizonPoint
  url: https://climavision.com/horizon-ai-point/
- group: other
  title: ''
  type: HorizonGlobal
  url: https://climavision.com/horizon-ai-global/
- group: other
  title: ''
  type: HorizonHIRES
  url: https://climavision.com/horizon-ai-hires/
- group: other
  title: ''
  type: HorizonS2S
  url: https://climavision.com/horizon-ai-subseasonal-and-seasonal/
- group: other
  title: ''
  type: RenewableEnergy
  url: https://climavision.com/renewable-energy-forecasting/
- group: company
  title: ''
  type: Blog
  url: https://climavision.com/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://climavision.com/resources/case-studies/
- group: company
  title: ''
  type: Careers
  url: https://climavision.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://climavision.com/contact/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Climavision
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/climavision
created: '2026-05-24'
description: Climavision is a Louisville, Kentucky weather intelligence company that combines a proprietary nationwide supplemental network of low-altitude X-band, dual-polarization gap-filling weather radars with AI-driven numerical weather prediction (NWP) to deliver enterprise-grade forecasts and observational data. Its Horizon AI product line includes Horizon Point for site-specific forecasts, Horizon Global for ground-to-high- altitude global models, Horizon HI-RES for custom high-resolution local forecasting, and Horizon S2S for subseasonal-to-seasonal prediction. Climavision exposes a Weather API hosted at point-forecast-api.climavision.com with 1,800+ parameters, 15-day forecasts, and bearer-token authentication, plus a separate Radar Status API and Radar-as-a-Service offering that supplies Level II files, NetCDF, and GeoTIFF radar data products (reflectivity, velocity, dual-pol-derived QPE at 1km, precipitation type, tornado debris detection) for coverage below 4,000 feet where
  NEXRAD cannot see due to Earth curvature. The company integrates its radar feed into MRMS and has provided supplemental data into the National Weather Service's AWIPS software. Climavision processes 1.5+ billion datasets daily, serves customers across agriculture, aviation, commodity trading, drones and Advanced Air Mobility, energy and utilities, government, insurance and reinsurance, media, and transportation and logistics, and raised a $100 million strategic investment from TPG's Rise Fund. API access is gated through a sales-led contact process; no public sandbox or open-source SDKs are published, and the Climavision GitHub organization (github.com/Climavision) currently has only two minor public repositories (an archived Azure Table Storage helper and a GeoServer Helm chart fork).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/climavision.png
layout: provider
modified: '2026-05-24'
name: Climavision
nav: Providers
network: true
overview: 'Climavision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Weather Intelligence, Forecasting, Numerical Weather Prediction, and Weather Radar.


  Climavision''s developer surface includes documentation, engineering blog, GitHub presence, and 16 more developer resources.'
random_paper: 27
score:
  band: minimal
  composite: 8.1
  delta: -2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/climavision/refs/heads/main/screenshots/climavision-2026-06-20T174525.png
security:
- kind: domain-security
  name: Climavision Domain Security
  slug: climavision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: climavision
tags:
- Weather
- Weather Intelligence
- Forecasting
- Numerical Weather Prediction
- Weather Radar
- X-Band Radar
- Dual Polarization
- Gap-Filling Radar
- Radar as a Service
- AI Forecasting
- Horizon AI
- Renewable Energy
- Severe Weather
- Hurricane
- Aviation Weather
- Agriculture
- Energy
- Insurance
website: https://climavision.com
---
