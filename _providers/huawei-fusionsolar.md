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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/huawei-fusionsolar/refs/heads/main/security/huawei-fusionsolar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/huawei-fusionsolar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://solar.huawei.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/huawei-fusionsolar/refs/heads/main/vendors/huawei-fusionsolar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/huawei-fusionsolar-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.huawei.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.huaweicloud.com/?utm_source=hdhome&amp;utm_adplace=AdPlace070853
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/huawei-fusionsolar/refs/heads/main/hosts/huawei-fusionsolar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/huawei-fusionsolar-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.huawei.com/cn/trust-center
- group: company
  title: ''
  type: Newsroom
  url: https://solar.huawei.com/news
- group: company
  title: ''
  type: Blog
  url: https://blog.huawei.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.huawei.com/consumer/cn/llms/docs-getting-started.txt
- group: operate
  title: ''
  type: Support
  url: https://solar.huawei.com/cn/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solar.huawei.com/cn/privacy
- group: operate
  title: ''
  type: ContactUs
  url: https://solar.huawei.com/cn/contact-us/
coverage:
  checked: 2026-09-23
  detail: Developer portal pages render only via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.huawei.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Huawei FusionSolar provides intelligent solar energy solutions, including photovoltaic inverters, energy storage systems, and management platforms for residential, commercial, and utility-scale solar projects. The platform offers monitoring, design tools, and a developer portal for integrating solar data and services.
image: https://solar.huawei.com/admin/asset/v1/pro/view/83edde1a92a94a33ab98eb70fe8eb7aa.png
layout: provider
modified: '2026-09-23'
name: Huawei FusionSolar
nav: Providers
network: true
overview: 'Huawei FusionSolar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Energy, IoT, and Inverters.


  Huawei FusionSolar''s developer surface includes documentation, engineering blog, getting-started guide, support, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Huawei Fusionsolar Domain Security
  slug: huawei-fusionsolar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: huawei-fusionsolar
tags:
- Company
- Solar
- Energy
- IoT
- Inverters
website: https://solar.huawei.com/
---
