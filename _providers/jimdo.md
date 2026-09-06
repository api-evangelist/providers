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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for managing Jimdo website content, blog posts, online store products, orders, and customer data for small business websites built on the Jimdo platform.
  name: Jimdo API
  slug: jimdo-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jimdo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jimdo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jimdo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.jimdoweb.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Jimdo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jimdo/
- group: company
  title: ''
  type: Blog
  url: https://dev.jimdoweb.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jimdo.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jimdo.com/
- group: other
  title: ''
  type: X
  url: https://x.com/jimdo
- group: commercial
  title: ''
  type: Plans
  url: plans/jimdo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jimdo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jimdo-finops.yml
created: '2026-06-13'
description: Jimdo is a website builder platform that provides REST APIs for managing website content, blog posts, online store products, and customer data for small business websites. The platform offers AI-powered website creation tools, ecommerce capabilities, and developer integrations enabling businesses to build and manage their online presence programmatically.
finops:
- name: Jimdo Finops
  service_category: ''
  slug: jimdo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jimdo.png
layout: provider
modified: '2026-06-13'
name: Jimdo
nav: Providers
network: true
overview: 'Jimdo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Website Builder, E-Commerce, CMS, Small Business, and Online Store.


  Jimdo''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Jimdo Plans Pricing
  plan_count: 12
  slug: jimdo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Jimdo Rate Limits
  slug: jimdo-rate-limits
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 27.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jimdo/refs/heads/main/screenshots/jimdo-2026-06-20T183734.png
security:
- kind: domain-security
  name: Jimdo Domain Security
  slug: jimdo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jimdo Vulnerability Disclosure
  slug: jimdo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jimdo
tags:
- Website Builder
- E-Commerce
- CMS
- Small Business
- Online Store
- Blog
website: https://www.jimdo.com/
---
