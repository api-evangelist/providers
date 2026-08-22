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
api_count: 1
apis:
- description: The first-party HTTP API behind the Vidjet embed and the Vidjet platform plugins, served from https://app-api.vidjet.io (Express). Vidjet publishes no developer documentation, reference, or machine-re
  name: Vidjet App API
  slug: app-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.vidjet.io
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.vidjet.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.vidjet.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vidjet.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.vidjet.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.vidjet.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vidjet.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vidjet.io/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.vidjet.io/en/articles/11392786-onboarding-the-3-steps-you-need-to-do
- group: operate
  title: ''
  type: Support
  url: https://help.vidjet.io/
- group: start
  title: ''
  type: Login
  url: https://app.vidjet.io/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vidjet-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vidjet-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/vidjet-packages.yml
- group: design
  title: ''
  type: Components
  url: components/vidjet-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vidjet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vidjet-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vidjet-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vidjet-conformance.yml
created: '2026-07-17'
description: Vidjet is a shoppable video platform for e-commerce that lets merchants embed on-site video without impacting page speed. Merchants build video feeds, tag products inside videos, and display formats such as Stories, Carousel, Bubble, Embed, Popup, and a Sticky Play Button across thousands of product pages. It is a no-code product installed via a JavaScript embed, Google Tag Manager, or platform plugins for Shopify, WooCommerce/WordPress, Magento, Wix, Webflow, PrestaShop, and Salesforce Commerce Cloud, with analytics, multilingual support, and email collection integrations to Klaviyo and Google Sheets. The company behind it is VIDJET TECHNOLOGIES, S.L. of Barcelona, Spain, a Seedcamp portfolio company. Vidjet runs no developer program and publishes no API reference, OpenAPI, SDK, OAuth surface, or webhook catalog. It does operate a first-party HTTP API at app-api.vidjet.io, whose base URL and several endpoints are published by Vidjet itself in the GPL-licensed WordPress plugin
  source and in the public embed script — a real but undocumented API surface, not a product an integrator can build against from published documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vidjet.png
layout: provider
modified: '2026-08-13'
name: Vidjet
nav: Providers
network: true
overview: 'Vidjet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Video, Shoppable Video, and Shopify.


  Vidjet''s developer surface includes documentation, pricing, engineering blog, signup flow, getting-started guide, support, and 13 more developer resources.'
plans:
- name: Vidjet Plans Pricing
  plan_count: 4
  slug: vidjet-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Vidjet Rate Limits
  slug: vidjet-rate-limits
score:
  band: thin
  composite: 28.9
  delta: -1.8
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Vidjet Authentication
  slug: vidjet-authentication
  summary_line: none/apiKey · 4 schemes
- kind: domain-security
  name: Vidjet Domain Security
  slug: vidjet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vidjet
tags:
- Company
- E-commerce
- Video
- Shoppable Video
- Shopify
- Conversion
- Marketing
- No-code
- Widgets
- Embed
website: https://www.vidjet.io
---
