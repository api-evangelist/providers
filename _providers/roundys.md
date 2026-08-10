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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: As a Kroger subsidiary, Roundy's stores (Pick 'n Save, Metro Market, Mariano's) are accessible through the Kroger Developer Platform product catalog API. The API enables searching and browsing product
  name: Kroger Product Catalog API
  slug: kroger-product-catalog-api
- description: The Kroger Store Locator API allows developers to find Pick 'n Save, Metro Market, and Mariano's store locations by geographic coordinates, ZIP code, or radius. Returns store details including address
  name: Kroger Store Locator API
  slug: kroger-stores-api
- description: The Kroger Cart API allows authenticated customers to add items directly to their Pick 'n Save, Metro Market, or Mariano's shopping cart for in-store pickup or delivery. Supports product quantity mana
  name: Kroger Cart and Checkout API
  slug: kroger-cart-api
- description: 'The Kroger Identity API provides OAuth 2.0-based authentication for Kroger customers including Roundy''s banner shoppers, enabling access to customer profiles, Plus Card loyalty data, digital coupons, '
  name: Kroger Identity and Loyalty API
  slug: kroger-identity-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roundys-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roundys-inc
- group: company
  title: ''
  type: Website
  url: https://www.roundys.com
- group: other
  title: ''
  type: Pick n Save
  url: https://www.picknsave.com
- group: other
  title: ''
  type: Metro Market
  url: https://www.metromarket.net
- group: other
  title: ''
  type: Marianos
  url: https://www.marianos.com
- group: other
  title: ''
  type: Kroger Developer Platform
  url: https://developer.kroger.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/roundys-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/roundys-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/roundys-store-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/roundys-store-structure.json
created: '2025-01-01'
description: 'Roundy''s, Inc. is a Midwest grocery retailer and wholly-owned subsidiary of The Kroger Co., founded in Milwaukee, Wisconsin in 1872. Roundy''s operates approximately 150 grocery stores under three retail banners: Pick ''n Save (106 locations throughout Wisconsin), Metro Market (premium Wisconsin grocery stores), and Mariano''s (44 Fresh Market locations throughout the Chicago area). As a Kroger subsidiary, Roundy''s leverages the Kroger developer platform and technology infrastructure including the Kroger API for product catalog, digital coupons, store locations, and loyalty program integrations.'
finops:
- name: Roundys Finops
  service_category: API
  slug: roundys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roundys.png
json_schemas:
- name: Roundy's Store Data Schema
  property_count: 2
  slug: roundys-store
json_structures:
- name: Roundys Store Structure
  property_count: 0
  slug: roundys-store-structure
jsonld:
- class_count: 0
  name: Roundys Context
  property_count: 5
  slug: roundys-context
layout: provider
modified: '2026-05-02'
name: Roundy's
nav: Providers
network: true
overview: 'Roundy''s publishes 1 API on the [APIs.io](https://apis.io/) network: Kroger Product Catalog API. Tagged areas include Grocery, Kroger, Midwest, Retail, and Supermarket.


  The Roundy''s catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Roundys Plans Pricing
  plan_count: 3
  slug: roundys-plans-pricing
press:
- date: '2026-05-25'
  title: 'Research Update: Roundy''s Supermarkets Inc. Ratin'
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/8325447
- date: '2026-05-25'
  title: Roundy's Supermarkets (RNDY) CEO Bob Mariano on Q4 ...
  url: https://seekingalpha.com/article/2974396-roundys-supermarkets-rndy-ceo-bob-mariano-on-q4-2014-results-earnings-call-transcript
- date: '2026-05-25'
  title: What's the secret sauce behind Mariano's store experience?
  url: https://www.grocerydive.com/news/whats-the-secret-sauce-behind-marianos-store-experience/541328/
- date: '2026-05-25'
  title: The 375000 square-foot customer fulfillment center uses artificial ...
  url: https://www.facebook.com/dayton247now/posts/the-375000-square-foot-customer-fulfillment-center-uses-artificial-intelligence-/5973614559375807/
- date: '2026-05-25'
  title: Kroger Outlines Plan to Redefine the Way America Eats ...
  url: https://www.prnewswire.com/news-releases/kroger-outlines-plan-to-redefine-the-way-america-eats-and-to-deliver-value-for-customers--shareholders-300534819.html
random_paper: 92
rate_limits:
- limit_count: 5
  name: Roundys Rate Limits
  slug: roundys-rate-limits
rules:
- name: Roundy's API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: roundys-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 40.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 36.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roundys/refs/heads/main/screenshots/roundys-2026-06-20T193225.png
security:
- kind: domain-security
  name: Roundys Domain Security
  slug: roundys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: roundys
tags:
- Grocery
- Kroger
- Midwest
- Retail
- Supermarket
- Wisconsin
website: https://www.roundys.com
---
