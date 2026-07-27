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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The EVgo Inside partner integration API allows third-party apps — including automaker head units, fleet management platforms, and mobile apps — to embed EVgo's full charging workflow. Capabilities inc
  name: EVgo Inside API
  slug: evgo-inside-api
- description: The PlugShare Charging Stations API, operated by EVgo (which acquired Recargo/PlugShare in 2021), provides deep and comprehensive public charging location data drawn from charge point operators, indus
  name: PlugShare Station Data API
  slug: plugshare-station-data-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evgo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.evgo.com/blog/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.evgo.com/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evgo.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.evgo.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evgo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evgo.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.evgo.com/company/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.evgo.com/support/faq/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.evgo.com/hc/en-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evgo/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/evgonetwork
- group: build
  title: ''
  type: GitHub
  url: https://github.com/evgo
created: '2026-06-13'
description: EVgo is one of the largest public DC fast charging networks in the United States, operating over 1,100 fast charging locations across 47 states. EVgo provides REST APIs through its EVgo Inside partner integration platform, enabling automakers, fleet operators, and app developers to embed charging station discovery, real-time availability, session initiation, account creation, and payment processing directly into their own branded experiences. Charging station data is also served via the PlugShare API, which EVgo owns and operates.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evgo.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: EVgo
nav: Providers
network: true
overview: 'EVgo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Vehicles, EV Charging, Charging Stations, Energy, and Transportation.


  The EVgo catalog on APIs.io includes 1 JSON-LD context.


  EVgo''s developer surface includes engineering blog, pricing, support, GitHub presence, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 6
  slug: plans
random_paper: 25
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 29.9
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 9.4
    developer_ergonomics: 6.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Evgo Domain Security
  slug: evgo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: evgo
tags:
- Electric Vehicles
- EV Charging
- Charging Stations
- Energy
- Transportation
- Mobility
website: https://www.evgo.com/
---
