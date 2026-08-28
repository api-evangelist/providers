---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Partner-only API access for shipping, payment, and integration partners. Not self-serve; access granted under partnership agreements.
  name: Mercari Partner API
  slug: partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercari-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mercari
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercari-inc-
- group: company
  title: ''
  type: Website
  url: https://www.mercari.com/
- group: other
  title: ''
  type: Developer
  url: https://about.mercari.com/en/business/
- group: commercial
  title: ''
  type: Plans
  url: plans/mercari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mercari-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mercari-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://about.mercari.com/en/press/news/
created: '2026-05-08'
description: Mercari is a peer-to-peer marketplace for new and used goods, operating in Japan and the United States. Mercari does not maintain a public developer API; integration is restricted to approved partners (e.g., shipping carriers, payment partners) under direct agreements.
finops:
- name: Mercari Finops
  service_category: Marketplace
  slug: mercari-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercari.png
layout: provider
modified: '2026-05-08'
name: Mercari
nav: Providers
network: true
overview: 'Mercari publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Resale, P2P, and E-Commerce.


  Mercari''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Mercari Plans Pricing
  plan_count: 1
  slug: mercari-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Mercari Rate Limits
  slug: mercari-rate-limits
score:
  band: minimal
  composite: 9.1
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercari/refs/heads/main/screenshots/mercari-2026-06-20T185213.png
security:
- kind: domain-security
  name: Mercari Domain Security
  slug: mercari-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mercari
tags:
- Marketplace
- Resale
- P2P
- E-Commerce
website: https://www.mercari.com/
---
