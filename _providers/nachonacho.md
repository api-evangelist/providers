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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: NachoNacho is a SaaS procurement and subscription management marketplace helping businesses discover, buy, and manage software subscriptions.
  name: NachoNacho
  slug: nachonacho
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nachonacho/refs/heads/main/security/nachonacho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nachonacho-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nachonacho-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nachonacho
- group: company
  title: ''
  type: Website
  url: https://www.nachonacho.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.nachonacho.com/resources
created: '2026-03-27'
description: NachoNacho is a SaaS procurement and subscription management marketplace helping businesses discover, buy, and manage software subscriptions.
finops:
- name: Nachonacho Finops
  service_category: API
  slug: nachonacho-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nachonacho.png
layout: provider
modified: '2026-04-28'
name: NachoNacho
nav: Providers
network: true
overview: 'NachoNacho publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS Procurement and Subscription Management.


  NachoNacho''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Nachonacho Plans Pricing
  plan_count: 3
  slug: nachonacho-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Nachonacho Rate Limits
  slug: nachonacho-rate-limits
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 43.3
    operational_transparency: 10.5
  previous_composite: 8.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/nachonacho/refs/heads/main/screenshots/nachonacho-2026-06-20T185926.png
security:
- kind: domain-security
  name: Nachonacho Domain Security
  slug: nachonacho-domain-security
  summary_line: TLSv1.2 · DMARC
slug: nachonacho
tags:
- SaaS Procurement
- Subscription Management
website: https://www.nachonacho.com
---
