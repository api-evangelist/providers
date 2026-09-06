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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Internal REST API for managing Strikingly website content, sections, blog posts, store products, form submissions, and membership settings. Access is provided through the Strikingly platform using OAu
  name: Strikingly Site Management API
  slug: strikingly-site-management-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strikingly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.strikingly.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.strikingly.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/strikingly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/striking-ly
- group: company
  title: ''
  type: Blog
  url: https://www.strikingly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.strikingly.com/s/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://x.com/strikinglystat
- group: other
  title: ''
  type: X
  url: https://x.com/strikingly
- group: commercial
  title: ''
  type: Plans
  url: plans/strikingly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/strikingly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/strikingly-finops.yml
created: '2026-06-13'
description: Strikingly is a mobile-first website builder platform that enables users to create gorgeous, mobile-optimized websites without coding. The platform provides tools for managing site content, sections, blog posts, store products, form submissions, and membership settings through its web interface and internal REST APIs.
finops:
- name: Strikingly Finops
  service_category: ''
  slug: strikingly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/strikingly.png
layout: provider
modified: '2026-06-13'
name: Strikingly
nav: Providers
network: true
overview: 'Strikingly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Website Builder, CMS, Blogging, E-Commerce, and Membership.


  Strikingly''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Strikingly Plans Pricing
  plan_count: 4
  slug: strikingly-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 15
  name: Strikingly Rate Limits
  slug: strikingly-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 26.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/strikingly/refs/heads/main/screenshots/strikingly-2026-06-20T194620.png
security:
- kind: domain-security
  name: Strikingly Domain Security
  slug: strikingly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: strikingly
tags:
- Website Builder
- CMS
- Blogging
- E-Commerce
- Membership
- No-Code
website: https://www.strikingly.com
---
