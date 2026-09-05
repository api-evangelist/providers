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
- description: The central API hub for Developers, Consumers, Application Managers, and Architects to discover and use P&G APIs.
  name: P&G Developer API Marketplace
  slug: p-g
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/p-g-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/p-g-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/procter-gamble
- group: start
  title: ''
  type: Portal
  url: https://developer.pg.com/
- group: company
  title: ''
  type: Website
  url: https://www.pg.com/
created: '2025-02-08'
description: Procter & Gamble provides an API Marketplace - the central API hub for Developers, Consumers, Application Managers, and Architects to discover and use P&G APIs.
finops:
- name: P G Finops
  service_category: API
  slug: p-g-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/p-g.png
layout: provider
modified: '2026-04-28'
name: P&G
nav: Providers
network: true
overview: 'P&G publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Marketplace and Consumer Goods.


  P&G''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: P G Plans Pricing
  plan_count: 3
  slug: p-g-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: P G Rate Limits
  slug: p-g-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/p-g/refs/heads/main/screenshots/p-g-2026-06-20T191300.png
security:
- kind: domain-security
  name: P G Domain Security
  slug: p-g-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: P G Vulnerability Disclosure
  slug: p-g-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: p-g
tags:
- API Marketplace
- Consumer Goods
website: https://www.pg.com/
---
