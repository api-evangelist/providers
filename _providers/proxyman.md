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
- description: Proxyman is a modern, native macOS app for HTTP/HTTPS debugging proxy with advanced features for API development and testing.
  name: Proxyman
  slug: proxyman
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proxyman-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proxyman
- group: company
  title: ''
  type: Website
  url: https://proxyman.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.proxyman.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nicklama
- group: company
  title: ''
  type: Blog
  url: https://proxyman.com/rss.xml
created: '2026-03-27'
description: Proxyman is a modern, native macOS app for HTTP/HTTPS debugging proxy with advanced features for API development and testing.
finops:
- name: Proxyman Finops
  service_category: API
  slug: proxyman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proxyman.png
layout: provider
modified: '2026-04-28'
name: Proxyman
nav: Providers
network: true
overview: 'Proxyman publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Debugging Proxy and Proxy.


  Proxyman''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Proxyman Plans Pricing
  plan_count: 3
  slug: proxyman-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Proxyman Rate Limits
  slug: proxyman-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proxyman/refs/heads/main/screenshots/proxyman-2026-06-20T192227.png
security:
- kind: domain-security
  name: Proxyman Domain Security
  slug: proxyman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: proxyman
tags:
- Debugging Proxy
- Proxy
website: https://proxyman.io/
---
