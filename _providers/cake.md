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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cake-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cake-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ridecake.com/en-US
- group: operate
  title: ''
  type: Support
  url: https://ridecake.com/en-US/service-support
- group: company
  title: ''
  type: Blog
  url: https://ridecake.com/en-US/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridecake.com/en-US/terms-for-purchasing-of-cake-products
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridecake.com/en-US/privacy-policy
coverage:
  checked: '2026-08-10'
  detail: CAKE names a "CAKE API" for pulling vehicle data and controls into third-party fleet software on its own :work/food-delivery pages, but ships no developer portal, reference or spec — api.ridecake.com, developer.ridecake.com and docs.ridecake.com are all NXDOMAIN, app.ridecake.com resolves to AWS but refuses connections, and the only stated route to the API is the general contact-us form.
  evidence:
  - status: 200
    url: https://ridecake.com/en-US/food-delivery
  - status: 200
    url: https://ridecake.com/en-US/contact-us
  - status: 500
    url: https://ridecake.com/openapi.json
  - status: 404
    url: https://ridecake.com/.well-known/api-catalog
  - status: 404
    url: https://ridecake.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Cake (stylized CAKE) is a Stockholm, Sweden based maker of premium, lightweight, high-performance electric motorcycles and mopeds, built around a mission to accelerate the shift to a zero-emission society by combining excitement with responsibility. Its clean-mobility lineup spans commuter models (Makka, Osa), off-road bikes (Kalk, Bukk) and work-focused utility variants. Founded by Stefan Ytterborn and backed by Creandum, CAKE filed for bankruptcy in early 2024 and its brand and IP were acquired by Norway's Brages Holding AS, which relaunched the company. Cake sells direct to consumers and through dealers at ridecake.com. Its bikes ship with the CAKE Connect module, and CAKE markets a "CAKE API" on its own :work and delivery pages that lets fleet owners pull vehicle data, telemetry and controls into their own fleet software — but that API has no public developer portal, no reference and no machine-readable specification; access runs through the contact and partner forms.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cake.png
layout: provider
modified: '2026-08-10'
name: Cake
nav: Providers
network: true
overview: 'Cake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Electric Vehicles, Mobility, and Motorcycles.


  Cake''s developer surface includes support, engineering blog, and 5 more developer resources.'
plans:
- name: Cake Plans Pricing
  plan_count: 0
  slug: cake-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 0
  name: Cake Rate Limits
  slug: cake-rate-limits
score:
  band: minimal
  composite: 11.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cake/refs/heads/main/screenshots/cake-2026-07-25T204220.png
security:
- kind: domain-security
  name: Cake Domain Security
  slug: cake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cake
tags:
- Company
- Climate
- Electric Vehicles
- Mobility
- Motorcycles
- Transportation
- Sustainability
- E-commerce
website: https://ridecake.com/en-US
---
