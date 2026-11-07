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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/hulft/hosts/hulft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hulft-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.saison-technology.com/company/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saison-technology.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.saison-technology.com/ir/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.saison-technology.com/ir/management/
- group: auth
  href: https://artifacts.apis.io/hulft/security/hulft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hulft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hulft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hulft.com/tech-support
- group: operate
  title: ''
  type: Support
  url: https://www.hulft.com/tech-support
- group: start
  title: ''
  type: Login
  url: https://his.hulft.com/mypage/login/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.saison-technology.com/service/product/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.saison-technology.com/service/product/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.hulft.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: HULFT provides secure, high‑performance data transfer solutions for enterprises, enabling reliable file exchange across heterogeneous environments, cloud services, and on‑premises systems. Their platform supports automation, scheduling, and monitoring, catering to industries such as manufacturing, logistics, and finance. With robust encryption, compliance features, and extensive integration options, HULFT helps organizations streamline data workflows and ensure data integrity and security during transit.
image: https://www.saison-technology.com/ogp_common.jpg
layout: provider
modified: '2026-10-20'
name: HULFT
nav: Providers
network: true
overview: 'HULFT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Transfer, Integration, Enterprise, and Security.


  HULFT''s developer surface includes support, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 50.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hulft/hulft-2026-11-03T133524.png
security:
- kind: domain-security
  name: Hulft Domain Security
  slug: hulft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hulft
tags:
- Company
- Data Transfer
- Integration
- Enterprise
- Security
website: https://www.hulft.com/
---
