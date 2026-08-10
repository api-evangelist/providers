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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API providing access to over one million foods including generic, branded, and recipe items, with up to 258 nutrient parameters, allergen information, and regional compliance datasets. JSON respo
  name: Nutritics Food Data API
  slug: food-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutritics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nutritics
- group: company
  title: ''
  type: Website
  url: https://www.nutritics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.nutritics.com/en/product/api/
- group: company
  title: ''
  type: About
  url: https://www.nutritics.com/en/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.nutritics.com/en/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nutritics.com/en/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.nutritics.com/en/blog/
- group: start
  title: ''
  type: Login
  url: https://www.nutritics.com/system2/login.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nutritics.com/en/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nutritics.com/en/privacy-policy/
created: '2025-03-01'
description: Nutritics provides a real-time food and nutrition data API offering access to over one million foods (generic, branded, and recipes), up to 258 nutrient parameters, allergen data, and regional compliance options across the EU, US, Australia, New Zealand, and South Africa.
finops:
- name: Nutritics Finops
  service_category: API
  slug: nutritics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutritics.png
layout: provider
modified: '2026-04-28'
name: Nutritics
nav: Providers
network: true
overview: 'Nutritics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Nutrition, Food Data, Allergens, Calories, and Health.


  Nutritics'' developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Nutritics Plans Pricing
  plan_count: 3
  slug: nutritics-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Nutritics Rate Limits
  slug: nutritics-rate-limits
score:
  band: emerging
  composite: 27.3
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutritics/refs/heads/main/screenshots/nutritics-2026-06-20T190532.png
security:
- kind: domain-security
  name: Nutritics Domain Security
  slug: nutritics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nutritics
tags:
- Nutrition
- Food Data
- Allergens
- Calories
- Health
website: https://www.nutritics.com
---
