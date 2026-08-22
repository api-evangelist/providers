---
access_model:
  confidence: high
  label: Enterprise sales only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.epsilon.com/us/products-and-services/accelerate
  - plans/yieldify-plans-pricing.yml
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yieldify-domain-security.yml
- group: design
  title: ''
  type: Components
  url: components/yieldify-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yieldify-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yieldify-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/yieldify-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yieldify-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.yieldify.com/
- group: operate
  title: ''
  type: Support
  url: https://support.yieldify.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.yieldify.com/en/
- group: start
  title: ''
  type: Login
  url: https://convert.yieldify.com/
- group: company
  title: ''
  type: Blog
  url: https://www.yieldify.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.yieldify.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yieldify.com/website-privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yieldify.com/terms-and-conditions-home/
coverage:
  checked: '2026-08-13'
  detail: Yieldify ships as a client-side JavaScript tag only — its 137-article Epsilon Accelerate help center covers campaign components, targeting and CSP allowlisting but contains no API, webhook or developer reference, and no OpenAPI/GraphQL/MCP/agent-card exists on any of its four hosts.
  evidence:
  - status: 200
    url: https://support.yieldify.com/en/
  - status: 404
    url: https://www.yieldify.com/openapi.json
  - status: 404
    url: https://yieldify.com/.well-known/agent-card.json
  - status: 200
    url: https://convert.yieldify.com/openapi.json
  - status: 200
    url: https://status.yieldify.com
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Yieldify is a website personalization and conversion rate optimization (CRO) platform for ecommerce brands, founded in 2013 in London by Jay Radia and backed by investors including GV (Google Ventures). Its SaaS platform delivers targeted on-site messaging, customer-journey personalization, and A/B testing to lift conversion and revenue. Yieldify was acquired by Publicis Groupe in January 2023 and folded into Epsilon, where it is now sold as Epsilon Accelerate; yieldify.com redirects to the Epsilon Accelerate product page and the legal entity behind the platform is Zeus Enterprise Ltd, trading as Yieldify. Delivery is entirely client-side: a customer-specific JavaScript tag placed before the closing head tag (directly, or via Google Tag Manager, Tealium, Shopify theme.liquid or Recharge checkout) renders a documented library of on-site experience components — overlays, notifications, banners, sticky and embedded experiences, toasters, carousels, countdown timers, lead-capture
  forms — configured from the Yieldify Conversion Platform at convert.yieldify.com, with a typed dynamic-expression language for personalized copy and client-side yieldify_impression/click/close/form_submit events pushed into the customer''s own GA4 property. There is no public developer API: probing every Yieldify host on 2026-08-13 found no OpenAPI, GraphQL, MCP, A2A card, webhooks, SDK, CLI or developer portal, the status page at status.yieldify.com has been deactivated, and no pricing is published anywhere.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yieldify.png
layout: provider
modified: '2026-08-13'
name: Yieldify *
nav: Providers
network: true
overview: 'Yieldify * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Personalization, Conversion Rate Optimization, and Ecommerce.


  Yieldify *''s developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Yieldify Plans Pricing
  plan_count: 0
  slug: yieldify-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 16.0
  delta: -0.5
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.5
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Yieldify Domain Security
  slug: yieldify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yieldify
tags:
- Company
- Enterprise
- Personalization
- Conversion Rate Optimization
- Ecommerce
- Marketing Technology
- Customer Experience
- A/B Testing
- Tag Management
- Lead Capture
- Website Optimization
website: https://www.yieldify.com/
---
