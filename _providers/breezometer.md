---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Real-time and forecast air quality data with street-level accuracy, including pollutant levels (CO, NO2, O3, PM10, PM2.5, SO2), AQI scores, and health recommendations for any location worldwide.
  name: BreezoMeter Air Quality API
  slug: breezometer-air-quality-api
- description: Daily forecast pollen data for a specific location, providing pollen index for various plant types for up to 5 days, helping allergy sufferers plan their outdoor activities.
  name: BreezoMeter Pollen API
  slug: breezometer-pollen-api
- description: Real-time wildfire monitoring API providing area monitoring and precision tracking of active fires worldwide, including fire perimeters, intensity, and spread patterns for predefined areas of interest
  name: BreezoMeter Wildfire Tracker+ API
  slug: breezometer-wildfire-tracker-api
- description: Advanced weather forecast API providing current conditions, hourly forecasts for up to 5 days, and daily forecasts for up to 5 days, powered by high-resolution environmental data models.
  name: BreezoMeter Weather API
  slug: breezometer-weather-api
- description: Personalized environmental alerting platform that sends proactive notifications about air quality, pollen, wildfire, and weather events via a single POST endpoint driving the Insights Engine with cust
  name: BreezoMeter Environmental Alerts API
  slug: breezometer-environmental-alerts-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/breezometer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breezometer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mapsplatform.google.com/maps-products/#environment-section
- group: docs
  title: ''
  type: Documentation
  url: https://docs.breezometer.com/api-documentation/introduction/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/breezometer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/breezometer
- group: company
  title: ''
  type: Blog
  url: https://blog.breezometer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://breezometer.com/air-quality-features/pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/breezometer
- group: commercial
  title: ''
  type: Plans
  url: plans/breezometer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/breezometer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/breezometer-finops.yml
created: '2026-06-13'
description: Environmental intelligence REST API providing real-time and forecast air quality, pollen counts, wildfire data, and weather information with street-level accuracy. BreezoMeter was acquired by Google in September 2022 and its technology is now integrated into Google Maps Platform.
finops:
- name: Breezometer Finops
  service_category: ''
  slug: breezometer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/breezometer.png
layout: provider
modified: '2026-06-13'
name: BreezoMeter
nav: Providers
network: true
overview: 'BreezoMeter publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Air Quality, Environment, Pollen, Wildfire, and Weather.


  BreezoMeter''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Breezometer Plans Pricing
  plan_count: 3
  slug: breezometer-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Breezometer Rate Limits
  slug: breezometer-rate-limits
score:
  band: emerging
  composite: 16.0
  delta: -4.3
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breezometer/refs/heads/main/screenshots/breezometer-2026-06-20T173650.png
security:
- kind: domain-security
  name: Breezometer Domain Security
  slug: breezometer-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Breezometer Vulnerability Disclosure
  slug: breezometer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: breezometer
tags:
- Air Quality
- Environment
- Pollen
- Wildfire
- Weather
- Environmental Intelligence
website: https://mapsplatform.google.com/maps-products/#environment-section
---
