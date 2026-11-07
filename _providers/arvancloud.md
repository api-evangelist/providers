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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ArvanCloud provides a developer API documented at https://www.arvancloud.ir/docs. The page redirects and presents a JavaScript loading screen, with no machine‑readable specification discovered.
  name: ArvanCloud API
  slug: arvancloud-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/arvancloud/hosts/arvancloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arvancloud-hosts.yml
- group: auth
  href: https://artifacts.apis.io/arvancloud/security/arvancloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arvancloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arvancloud.ir/
created: '2026-10-27'
description: ArvanCloud provides cloud services including CDN, cloud storage, video streaming, and security solutions. It operates a global network of data centers to deliver high‑performance content delivery and edge computing. The company serves enterprises and developers with APIs for managing resources, configuring services, and monitoring usage, positioning itself as a comprehensive cloud infrastructure provider.
layout: provider
modified: '2026-10-27'
name: ArvanCloud
nav: Providers
network: true
overview: ArvanCloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, CDN, Storage, Video Streaming, and Security.
random_paper: 15
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arvancloud/arvancloud-2026-11-03T121142.png
security:
- kind: domain-security
  name: Arvancloud Domain Security
  slug: arvancloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arvancloud
tags:
- Cloud
- CDN
- Storage
- Video Streaming
- Security
- Company
website: https://arvancloud.ir/
---
