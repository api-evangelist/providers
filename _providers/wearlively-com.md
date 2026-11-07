---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/wearlively-com/llms/wearlively-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wearlively-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/wearlively-com/well-known/wearlively-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wearlively-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wearlively-com/hosts/wearlively-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wearlively-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shopbtemptd.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shopbtemptd.com/pages/privacy-policy
- group: auth
  href: https://artifacts.apis.io/wearlively-com/security/wearlively-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wearlively-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wearlively.com/
created: '2026-10-25'
description: Lively provides a platform that connects wearable device manufacturers with consumers, offering tools for device management, data analytics, and user engagement. Backed by GGV Capital, the company focuses on simplifying the integration of wearables into everyday life, enabling developers to build richer experiences through robust APIs and SDKs. Their services include device provisioning, firmware updates, health data aggregation, and personalized insights, aiming to accelerate innovation in the wearable technology market.
layout: provider
modified: '2026-10-25'
name: Lively
nav: Providers
network: true
overview: Lively is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Platform, and Data Analytics.
random_paper: 16
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wearlively-com/wearlively-com-2026-11-03T150033.png
security:
- kind: domain-security
  name: Wearlively Com Domain Security
  slug: wearlively-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wearlively-com
tags:
- Company
- Wearables
- Platform
- Data Analytics
website: https://www.wearlively.com/
---
