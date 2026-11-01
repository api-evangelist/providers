---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Tencent Open Platform provides APIs for QQ services and integration.
  name: QQ Open Platform
  slug: qq-open-platform
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/tencent-qq/llms/tencent-qq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tencent-qq-llms.txt
- group: agent
  href: https://artifacts.apis.io/tencent-qq/well-known/tencent-qq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tencent-qq-well-known.yml
- group: other
  href: https://artifacts.apis.io/tencent-qq/hosts/tencent-qq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tencent-qq-hosts.yml
- group: build
  href: https://artifacts.apis.io/tencent-qq/packages/tencent-qq-packages.yml
  title: ''
  type: SDKs
  url: packages/tencent-qq-packages.yml
- group: build
  href: https://artifacts.apis.io/tencent-qq/packages/tencent-qq-packages.yml
  title: ''
  type: Packages
  url: packages/tencent-qq-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.qq.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sj.qq.com/tag/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qq.com/
- group: auth
  href: https://artifacts.apis.io/tencent-qq/security/tencent-qq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tencent-qq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connect.qq.com/
coverage:
  checked: '2026-10-26'
  detail: Developer portal renders content via JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://open.qq.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: 'Tencent QQ is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-26'
name: Tencent QQ
nav: Providers
network: true
overview: 'Tencent QQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Tencent QQ''s developer surface includes support, sandbox, documentation, and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tencent Qq Domain Security
  slug: tencent-qq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tencent-qq
tags:
- Company
website: https://connect.qq.com/
---
