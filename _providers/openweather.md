---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openweather Agentic Access
  operation_count: 5
  slug: openweather-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Air Pollution API provides current, forecast, and historical air pollution data for any coordinates on the globe. It returns the basic Air Quality Index along with concentrations of CO, NO, NO2, O
  name: OpenWeather Air Pollution API
  slug: openweather-air-pollution-api
- description: Current, forecast, and historical air pollution data.
  name: OpenWeather Air Pollution API
  slug: openweather-air-pollution-api
- description: Combined current weather, forecast, and historical weather data.
  name: OpenWeather One Call API
  slug: openweather-one-call-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenWeather One Call and Air Pollution API
  slug: open-openweather-air-pollution-api
- collection_type: open
  name: OpenWeather and Air Pollution One Call API
  slug: open-openweather-one-call-api
- collection_type: open
  name: OpenWeather One Call and Air Pollution API
  slug: open-openweather
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openweather-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openweather-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openweather-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openweathermap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openweathermap
- group: company
  title: ''
  type: Website
  url: https://openweathermap.org/
- group: start
  title: ''
  type: API Portal
  url: https://openweathermap.org/api
- group: docs
  title: ''
  type: Documentation
  url: https://openweathermap.org/technology
- group: commercial
  title: ''
  type: Pricing
  url: https://openweathermap.org/price
- group: start
  title: ''
  type: Signup
  url: https://home.openweathermap.org/users/sign_up
- group: company
  title: ''
  type: Blog
  url: https://openweather.co.uk/blog
- group: operate
  title: ''
  type: FAQ
  url: https://openweathermap.org/faq
- group: operate
  title: ''
  type: Support
  url: https://openweathermap.org/contact-us
- group: commercial
  title: ''
  type: Privacy
  url: https://openweather.co.uk/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openweather.co.uk/terms
created: '2024-11-07'
description: OpenWeather is a data platform that provides accurate and reliable weather information to individuals, businesses, and organizations around the world. They gather real-time data from a network of sensors, satellites, and weather stations to deliver comprehensive weather forecasts, historical weather data, and climate information.
finops:
- name: Openweather Finops
  service_category: API
  slug: openweather-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openweather.png
layout: provider
modified: '2026-05-19'
name: OpenWeather
nav: Providers
network: true
overview: 'OpenWeather publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Air Pollution API, One Call API, and 1 more. Tagged areas include Air Pollution, Air Quality, Climate, Forecasting, and Weather.


  OpenWeather''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, FAQ, support, and 8 more developer resources.'
plans:
- name: Openweather Plans Pricing
  plan_count: 3
  slug: openweather-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 5
  name: Openweather Rate Limits
  slug: openweather-rate-limits
score:
  band: developing
  composite: 39.8
  delta: -0.8
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 56.6
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openweather/refs/heads/main/screenshots/openweather-2026-06-20T191054.png
security:
- kind: authentication
  name: Openweather Authentication
  slug: openweather-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openweather Domain Security
  slug: openweather-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openweather
tags:
- Air Pollution
- Air Quality
- Climate
- Forecasting
- Weather
website: https://openweathermap.org/
---
