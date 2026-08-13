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
- group: company
  title: ''
  type: Website
  url: https://targetspot.com
- group: start
  title: ''
  type: Portal
  url: https://passport.targetspot.com/
- group: start
  title: ''
  type: Login
  url: https://passport.targetspot.com/
- group: company
  title: ''
  type: Blog
  url: https://www.targetspot.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.targetspot.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.targetspot.com/privacy-policy/
- group: other
  title: ''
  type: Products
  url: https://www.targetspot.com/products/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.targetspot.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/targetspot
- group: auth
  title: ''
  type: DomainSecurity
  url: security/targetspot-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/targetspot-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/targetspot-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/targetspot-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Targetspot markets a Passport reporting API on its product page but publishes no reference for it anywhere — the only route to the contract is a tenant login at passport.targetspot.com, whose server answers 200 with the same JavaScript app shell for every path including ones that cannot exist, while the API host api.targetspot.com resolves in DNS and then refuses TCP on 80 and 443.
  evidence:
  - status: 200
    url: https://www.targetspot.com/passport/
  - status: 200
    url: https://passport.targetspot.com/openapi.json
  - status: 404
    url: https://www.targetspot.com/.well-known/api-catalog
  - status: 0
    url: https://api.targetspot.com/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Targetspot is a global digital-audio advertising (AdTech) company founded in 2007 and headquartered in New York, connecting brands with audiences across podcasts, online radio, streaming, in-video audio, mobile gaming, and in-home/out-of-home audio. Its Passport product is a self-serve ad-serving platform for publishers and advertisers, with granular reporting data made available via a partner API, and Targetplay extends audio advertising into gaming and in-app inventory. Targetspot is now part of the Azerion platform. This profile originated as a Union Square Ventures portfolio lead and has been enriched from public web probes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/targetspot.png
layout: provider
modified: '2026-08-12'
name: Targetspot
nav: Providers
network: true
overview: 'Targetspot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Digital Audio, and Ad Serving.


  Targetspot''s developer surface includes developer portal, engineering blog, support, and 10 more developer resources.'
plans:
- name: Targetspot Plans Pricing
  plan_count: 0
  slug: targetspot-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Targetspot Rate Limits
  slug: targetspot-rate-limits
score:
  band: emerging
  composite: 14.2
  delta: 1.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Targetspot Domain Security
  slug: targetspot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: targetspot
tags:
- Company
- Advertising
- AdTech
- Digital Audio
- Ad Serving
- Podcast Advertising
- Publishers
- Advertisers
website: https://targetspot.com
---
