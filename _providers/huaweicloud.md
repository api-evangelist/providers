---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/huaweicloud/refs/heads/main/llms/huaweicloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/huaweicloud-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/huaweicloud/refs/heads/main/hosts/huaweicloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/huaweicloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/huaweicloud/refs/heads/main/vendors/huaweicloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/huaweicloud-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: http://www.huaweicloud.com/news/1512571718813.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/huaweicloud/refs/heads/main/security/huaweicloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/huaweicloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.huaweicloud.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.huaweicloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.huaweicloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.huaweicloud.com/intl/en-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.huaweicloud.com/intl/zh-cn/
- group: operate
  title: ''
  type: Support
  url: https://support.huaweicloud.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.huaweicloud.com/pricing/index.html
- group: start
  title: ''
  type: SignUp
  url: https://reg.huaweicloud.com/registerui/public/custom/register.html?locale=zh-cn&service=https%3A%2F%2Fdeveloper.huaweicloud.com%2F
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/huaweicloud/workspace
coverage:
  checked: '2026-10-03'
  detail: Developer portal returns HTML for OpenAPI endpoints, no machine-readable spec found.
  evidence:
  - status: 200
    url: https://developer.huaweicloud.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Huawei Cloud, the public cloud arm of Huawei Technologies, offers a comprehensive suite of cloud services including compute, storage, networking, AI, and big data solutions. It serves enterprises worldwide with flexible pricing, high performance, and strong security compliance, positioning itself as a major global IaaS and PaaS provider.
layout: provider
modified: '2026-10-03'
name: Huawei Cloud
nav: Providers
network: true
overview: 'Huawei Cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Infrastructure-as-a-Service, Platform-as-a-Service, and Artificial Intelligence.


  Huawei Cloud''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Huaweicloud Domain Security
  slug: huaweicloud-domain-security
  summary_line: TLSv1.3 · HSTS
slug: huaweicloud
tags:
- Company
- Cloud
- Infrastructure-as-a-Service
- Platform-as-a-Service
- Artificial Intelligence
website: https://www.huaweicloud.com
---
