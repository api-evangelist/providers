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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://revie.lat
- group: commercial
  title: ''
  type: Pricing
  url: https://revie.lat/planes
- group: company
  title: ''
  type: Blog
  url: https://revie.lat/blog/ecommerce
- group: operate
  title: ''
  type: HelpCenter
  url: https://revie.lat/centro-de-ayuda
- group: docs
  title: ''
  type: Documentation
  url: https://help.revie.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revie.lat/aviso-de-privacidad
- group: start
  title: ''
  type: SignUp
  url: https://apps.shopify.com/revie
- group: start
  title: ''
  type: Login
  url: https://app.revie.lat/
- group: commercial
  title: ''
  type: Plans
  url: plans/revie-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/revie-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revie-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revieio
coverage:
  checked: '2026-08-13'
  detail: Revie ships only end-user storefront apps for Shopify, Tiendanube and VTEX — there is no developer portal, no API reference, no SDK and no GitHub organisation, and the one API host that exists (api.revie.lat) is the private AWS API Gateway backend for the app.revie.lat dashboard, named in the SPA's own config.js and answering every path with 403 "Missing Authentication Token".
  evidence:
  - status: 403
    url: https://api.revie.lat/openapi.json
  - status: 404
    url: https://www.revie.lat/openapi.json
  - status: 404
    url: https://help.revie.ai/openapi.json
  - status: 404
    url: https://www.revie.lat/llms.txt
  - status: 404
    url: https://www.revie.lat/.well-known/agent-card.json
  - status: 200
    url: https://app.revie.lat/config/config.js
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Revie is an AI-powered customer review collection and WhatsApp marketing automation platform for e-commerce businesses, with a focus on the Latin American market. It requests and collects product reviews over WhatsApp (in text, photo, video, and voice-note formats) after a purchase, then applies AI sentiment analysis and keyword grouping to surface customer feedback in a dashboard. Revie also powers WhatsApp marketing campaigns, customer segmentation, and discount incentives, and integrates with Shopify, Tienda Nube, and VTEX storefronts. The company exposes no public developer API or SDK; its product is delivered as installable storefront apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revie.png
layout: provider
modified: '2026-08-13'
name: Revie
nav: Providers
network: true
overview: 'Revie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reviews, WhatsApp, Marketing, and E-Commerce.


  Revie''s developer surface includes pricing, engineering blog, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Revie Plans Pricing
  plan_count: 7
  slug: revie-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revie/refs/heads/main/screenshots/revie-2026-09-02T153715.png
security:
- kind: domain-security
  name: Revie Domain Security
  slug: revie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: revie
tags:
- Company
- Reviews
- WhatsApp
- Marketing
- E-Commerce
- Customer Experience
- Messaging
- Artificial Intelligence
- Shopify
- Latin America
website: https://revie.lat
---
