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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 11.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adidas-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adidas
- group: company
  title: ''
  type: Website
  url: https://www.adidas.com/
- group: start
  title: ''
  type: Login
  url: https://www.adidas.com/us/login
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.adidas-group.com/en/about/our-network/our-partners
- group: build
  title: ''
  type: GitHub
  url: https://github.com/adidas
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: A German multinational corporation designing and manufacturing athletic shoes, apparel, and accessories. One of the world's largest sportswear brands competing across performance and lifestyle markets.
features:
- description: Adidas loyalty program rewarding members with points, exclusive products, and personalized experiences.
  name: adiClub Loyalty
- description: Mobile app providing access to limited-edition sneaker drops and reservation-based releases.
  name: Confirmed App
- description: Online storefront for footwear, apparel, and accessories across consumer and performance lines.
  name: E-commerce Storefront
- description: Locate Adidas branded retail stores and authorized retailers worldwide.
  name: Store Locator
- description: Adidas-owned running and fitness app (formerly Runtastic) tracking activity and integrating with adiClub.
  name: Runtastic / adidas Running
finops:
- name: Adidas Finops
  service_category: Retail / Sportswear
  slug: adidas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adidas.png
integrations:
- description: Awin affiliate network manages Adidas' affiliate program in most regions.
  name: Awin
- description: Rakuten Advertising affiliate distribution in select markets.
  name: Rakuten Advertising
- description: Mobile Confirmed app for reservation-based sneaker releases.
  name: Confirmed App
- description: Activity sharing from adidas Running to Strava for joint athlete experience.
  name: Strava
- description: Adidas runs portions of its e-commerce stack on Salesforce Commerce Cloud.
  name: Salesforce Commerce Cloud
layout: provider
modified: '2026-05-16'
name: Adidas
nav: Providers
network: true
overview: 'Adidas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Athletic Apparel, Footwear, and Sportswear.


  Adidas'' developer surface includes GitHub presence, authentication, and 4 more developer resources.'
plans:
- name: Adidas Plans Pricing
  plan_count: 1
  slug: adidas-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Adidas Rate Limits
  slug: adidas-rate-limits
score:
  band: emerging
  composite: 18.5
  delta: -1.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Adidas Domain Security
  slug: adidas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adidas
tags:
- Athletic Apparel
- Footwear
- Sportswear
use_cases:
- description: Direct-to-consumer e-commerce for performance footwear and apparel.
  name: Sportswear E-commerce
- description: Allocated release of limited-edition footwear through the Confirmed app and adidas.com.
  name: Sneaker Drop Distribution
- description: Member engagement and retention through adiClub points, tiers, and personalized offers.
  name: Loyalty Engagement
- description: Activity tracking and training plans delivered through adidas Running and Training apps.
  name: Fitness Tracking
website: https://www.adidas.com/
---
