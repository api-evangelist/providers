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
api_count: 2
apis:
- description: Tiffany & Co.'s direct-to-consumer e-commerce platform at tiffany.com, enabling online browsing, customization, and purchase of jewelry, watches, accessories, and home items. The platform supports pro
  name: Tiffany & Co. E-Commerce Platform
  slug: tiffany-ecommerce
- description: Tiffany & Co.'s B2B corporate gifting and recognition program platform, providing procurement and delivery of corporate gifts and recognition items. The platform includes order management system integ
  name: Tiffany & Co. Corporate Gifting Platform
  slug: tiffany-corporate-gifting
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiffany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tiffany.com
- group: other
  title: ''
  type: Corporate Gifting
  url: https://www.tiffany.com/en-us/gifts/corporate-gifting/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiffany.com/accessibility/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiffany.com/accessibility/terms-and-conditions/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tiffanyandco
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/tiffanyandco/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/tiffanyandco/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiffany-co/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tiffany-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tiffany-product-schema.json
created: '2024'
description: Tiffany & Co. is a global luxury jeweler and specialty retailer founded in 1837, acquired by LVMH in 2021. The company designs, manufactures, and sells jewelry, watches, fragrances, and accessories under the Tiffany brand across over 300 stores worldwide and a robust e-commerce platform. Tiffany operates a B2B corporate gifting platform and retail e-commerce site with back-end order management integration. The company does not currently offer a public developer API or partner developer program; integration is available through their corporate gifting portal and select enterprise channels.
examples:
- key_count: 14
  name: Tiffany Corporate Order Example
  slug: tiffany-corporate-order-example
- key_count: 18
  name: Tiffany Product Example
  slug: tiffany-product-example
finops:
- name: Tiffany Finops
  service_category: API
  slug: tiffany-finops
image: https://www.tiffany.com/favicon.ico
json_schemas:
- name: Tiffany Corporate Gift Order
  property_count: 13
  slug: tiffany-corporate-order
- name: Tiffany Product
  property_count: 17
  slug: tiffany-product
json_structures:
- name: Tiffany Product Structure
  property_count: 0
  slug: tiffany-product-structure
jsonld:
- class_count: 16
  name: Tiffany Context
  property_count: 19
  slug: tiffany-context
layout: provider
modified: '2026-05-03'
name: Tiffany & Co.
nav: Providers
network: true
overview: 'Tiffany & Co. publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Corporate Gifting, E-Commerce, Jewelry, Luxury Retail, and Watches.


  The Tiffany & Co. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Tiffany Plans Pricing
  plan_count: 3
  slug: tiffany-plans-pricing
press:
- date: '2026-05-25'
  title: Tiffany & Co. boosts sales with AI-powered client advisory ...
  url: https://www.linkedin.com/posts/aimresearch-ai_tiffany-co-the-189-year-old-jewelry-brand-activity-7404905317022498820-A735
- date: '2026-05-25'
  title: Tiffany Demands PSC to Prioritize Baseload Power Sources ...
  url: http://tiffany.house.gov/media/press-releases/tiffany-demands-psc-prioritize-baseload-power-sources-ensure-affordable-energy
- date: '2026-05-25'
  title: Tiffany & Co. achieves sparkling revenue with online ...
  url: https://www.iabuk.com/case-studies/tiffany-co-achieves-sparkling-revenue-online-optimisation
- date: '2026-05-25'
  title: 'Ken Goldberg and Tiffany Shlain: Speculation, Like Nature ...'
  url: https://cclarkgallery.com/exhibitions/73-ken-goldberg-and-tiffany-shlain-speculation-like-nature-media-room/overview/
- date: '2026-05-25'
  title: Disclaimer missing on likely AI-generated Tom Tiffany ...
  url: https://isthmus.com/news/news/disclaimer-missing-on-likely-ai-generated-tom-tiffany-campaign-ad/
random_paper: 24
rate_limits:
- limit_count: 5
  name: Tiffany Rate Limits
  slug: tiffany-rate-limits
rules:
- name: Tiffany & Co. API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tiffany-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.5
  delta: -5.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 39.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tiffany/refs/heads/main/screenshots/tiffany-2026-06-20T195341.png
security:
- kind: domain-security
  name: Tiffany Domain Security
  slug: tiffany-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tiffany
tags:
- Corporate Gifting
- E-Commerce
- Jewelry
- Luxury Retail
- Watches
- Fortune 1000
website: https://www.tiffany.com
---
