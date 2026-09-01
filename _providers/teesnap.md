---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teesnap-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teesnap
- group: company
  title: ''
  type: Website
  url: https://www.teesnap.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.teesnap.com
- group: commercial
  title: ''
  type: Plans
  url: plans/teesnap-plans-pricing.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.teesnap.com/our-platform/
- group: other
  title: ''
  type: ProductPage
  url: https://www.teesnap.com/point-of-sale/
created: '2026-07-11'
description: Teesnap is an all-in-one golf course management platform and point-of-sale system for golf operators, founded in 2013 and based in Las Vegas, Nevada. Its cloud software suite covers a tee sheet and tee-time booking engine, golf and food-and-beverage point of sale, customer and membership management, an online store, websites, payments, and a marketing and reporting system. Teesnap connects to the wider golf ecosystem through partner integrations - GolfNow (its official online tee-time distribution partner via NBC Sports Next), Priswing dynamic pricing, Golf Genius tournament management, QuickBooks Online accounting, Gallus mobile apps, Heartland payment processing, and range hardware from eRange and Select Pi. As of this catalog's review date Teesnap does not publish a public, self-service developer API or developer portal; integrations are delivered through partner-gated, business-development relationships. The APIs listed here are honestly modeled from Teesnap's public product
  surface and are not sourced from published API documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teesnap.png
layout: provider
modified: '2026-07-25'
name: Teesnap
nav: Providers
network: true
overview: 'Teesnap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Golf, Point-of-Sale, Tee Times, Golf Course Management, and Booking.


  Teesnap''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Teesnap Plans Pricing
  plan_count: 1
  slug: teesnap-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Teesnap Domain Security
  slug: teesnap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teesnap
tags:
- Golf
- Point-of-Sale
- Tee Times
- Golf Course Management
- Booking
- Partner Gated
website: https://www.teesnap.com
---
