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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://fig-1.co
- group: start
  title: ''
  type: SignUp
  url: https://fig-1.co/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fig-1.co/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fig-1.co/policies/terms-of-service
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fig-1-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fig-1-domain-security.yml
created: '2026-07-17'
description: Fig.1 (Figure 1 Beauty) is a direct-to-consumer skincare brand created through 8VC's Build program, co-founded with Harvard-trained dermatologist Dr. Courtney Rubin, focused on demystifying and democratizing skincare through transparent, efficacy-driven, in-house formulations sold across a small launch line of cleansers, treatments, and moisturizers. Its public surface is a Shopify-hosted ecommerce storefront at fig-1.co; Fig.1 publishes no first-party developer API, OpenAPI, SDKs, or documentation. This API Evangelist profile records the brand's identity, storefront policy pages, and domain-security posture. The /.well-known/openid-configuration served on the host is Shopify's shared Customer-Account platform OIDC, not a Fig.1 API.
image: https://fig-1.co/cdn/shop/files/logo-orange.svg
layout: provider
modified: '2026-07-19'
name: Fig 1
nav: Providers
network: true
overview: 'Fig 1 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Skincare, Beauty, E-Commerce, and Direct to Consumer.


  Fig 1''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fig-1/refs/heads/main/screenshots/fig-1-2026-08-07T165251.png
security:
- kind: domain-security
  name: Fig 1 Domain Security
  slug: fig-1-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fig-1
tags:
- Company
- Skincare
- Beauty
- E-Commerce
- Direct to Consumer
- Consumer
- Shopify
website: https://fig-1.co
---
