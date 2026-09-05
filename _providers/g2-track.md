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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: G2 Track / Cleanshelf SaaS management product, now part of BetterCloud Spend Optimization, providing spend monitoring, contract tracking, and usage insights.
  name: G2 Track
  slug: g2-track
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/g2-track-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bettercloud.com/platform/spend-management/
- group: other
  title: ''
  type: Developer
  url: https://developer.bettercloud.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bettercloud.com/monitor/feed/
created: '2026-03-27'
description: G2 Track (formerly Cleanshelf) was a SaaS management platform providing SaaS spend monitoring, contract tracking, and usage insights. The product has since been acquired and is now offered as BetterCloud Spend Optimization.
finops:
- name: G2 Track Finops
  service_category: API
  slug: g2-track-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/g2-track.png
layout: provider
modified: '2026-04-28'
name: G2 Track
nav: Providers
network: true
overview: 'G2 Track publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Management, SaaS Management, and Spend Optimization.


  G2 Track''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: G2 Track Plans Pricing
  plan_count: 3
  slug: g2-track-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: G2 Track Rate Limits
  slug: g2-track-rate-limits
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/g2-track/refs/heads/main/screenshots/g2-track-2026-06-20T181631.png
security:
- kind: domain-security
  name: G2 Track Domain Security
  slug: g2-track-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: g2-track
tags:
- Contract Management
- SaaS Management
- Spend Optimization
website: https://www.bettercloud.com/platform/spend-management/
---
