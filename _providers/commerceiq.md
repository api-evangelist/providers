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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commerceiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.commerceiq.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commerceiq-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.commerceiq.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commerceiq.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.commerceiq.ai/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.commerceiq.ai/faqs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commerceiq/
- group: build
  title: ''
  type: Packages
  url: packages/commerceiq-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/commerceiq-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.commerceiq.ai/faqs
coverage:
  checked: '2026-08-12'
  detail: CommerceIQ ships only a login-gated enterprise application — *.commerceiq.ai is a wildcard that 302s api., docs. and developer. to the marketing site, so there is no developer host at all, and the company's own FAQ describes consuming the Instacart and Amazon APIs rather than publishing one.
  evidence:
  - status: 302
    url: https://developer.commerceiq.ai/
  - status: 302
    url: https://api.commerceiq.ai/openapi.json
  - status: 404
    url: https://my.commerceiq.ai/openapi.json
  - status: 404
    url: https://www.commerceiq.ai/.well-known/agent-card.json
  - status: 200
    url: https://www.commerceiq.ai/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: CommerceIQ is an AI-powered ecommerce platform that helps consumer brands win in algorithmic retail across sales, digital shelf, retail media, and content execution. Its unified platform, Ally AI, packages four AI agents (Content, Shelf, Media, and Sales) that optimize product content and SEO, monitor digital-shelf availability and search rankings across 1,450+ retailers globally, manage and automate retail media bidding and spend, and forecast and execute sales strategy from Amazon and Walmart to Instacart and Criteo. Founded in 2019, CommerceIQ serves enterprise brands including PepsiCo, P&G, Coca-Cola, and Colgate-Palmolive, and is backed by Insight Partners, SoftBank Vision Fund, and Trinity Ventures. The company operates as a managed enterprise platform and does not publish a public self-service API or developer portal.
image: https://djijnrz4nj20x.cloudfront.net/2026/07/opengraph-v2-a81c0ced.png
layout: provider
modified: '2026-08-12'
name: CommerceIQ
nav: Providers
network: true
overview: 'CommerceIQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail Media, Digital Shelf, and Artificial Intelligence.


  CommerceIQ''s developer surface includes engineering blog, support, FAQ, and 8 more developer resources.'
plans:
- name: Commerceiq Plans Pricing
  plan_count: 0
  slug: commerceiq-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Commerceiq Rate Limits
  slug: commerceiq-rate-limits
score:
  band: emerging
  composite: 13.0
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 13.0
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commerceiq/refs/heads/main/screenshots/commerceiq-2026-07-25T210126.png
security:
- kind: domain-security
  name: Commerceiq Domain Security
  slug: commerceiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commerceiq
tags:
- Company
- E-Commerce
- Retail Media
- Digital Shelf
- Artificial Intelligence
- Retail
- Analytics
- Marketing
website: https://www.commerceiq.ai/
---
