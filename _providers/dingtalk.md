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
- group: agent
  href: https://artifacts.apis.io/dingtalk/llms/dingtalk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dingtalk-llms.txt
- group: other
  href: https://artifacts.apis.io/dingtalk/hosts/dingtalk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dingtalk-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.dingtalk.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dingtalk.com/
- group: auth
  href: https://artifacts.apis.io/dingtalk/security/dingtalk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dingtalk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dingtalk.com/
coverage:
  checked: '2026-10-27'
  detail: Developer portal pages are rendered via JavaScript and block direct spec fetches.
  evidence:
  - status: 200
    url: https://open.dingtalk.com/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: DingTalk (钉钉) is an enterprise communication and collaboration platform developed by Alibaba Group. It provides messaging, video conferencing, task management, and a low-code development environment for building custom business applications. The service targets corporate users, offering integration with other Alibaba cloud services and a suite of productivity tools designed for the digital economy era.
image: https://img.alicdn.com/imgextra/i3/O1CN017PqYP51OX3bSJGxQY_!!6000000001714-2-tps-200-200.png
layout: provider
modified: '2026-10-26'
name: DingTalk
nav: Providers
network: true
overview: 'DingTalk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Collaboration, Enterprise, and Alibaba.


  DingTalk''s developer surface includes documentation and 5 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 8.0
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
screenshot: https://apis.io/screenshots/dingtalk/dingtalk-2026-11-03T130742.png
security:
- kind: domain-security
  name: Dingtalk Domain Security
  slug: dingtalk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dingtalk
tags:
- Company
- Communications
- Collaboration
- Enterprise
- Alibaba
- Low-Code
website: https://www.dingtalk.com/
---
