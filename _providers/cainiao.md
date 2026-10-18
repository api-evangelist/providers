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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cainiao/refs/heads/main/hosts/cainiao-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cainiao-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cainiao/refs/heads/main/packages/cainiao-packages.yml
  title: ''
  type: SDKs
  url: packages/cainiao-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cainiao/refs/heads/main/packages/cainiao-packages.yml
  title: ''
  type: Packages
  url: packages/cainiao-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cainiao.com/privacypolicy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cainiao/refs/heads/main/security/cainiao-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cainiao-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cainiao.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cainiao.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Cainiao, also known as 菜鸟网络, is a leading global e‑commerce logistics platform under Alibaba Group. It provides end‑to‑end supply chain services, including domestic and international warehousing, parcel delivery, cross‑border logistics, and smart infrastructure. Leveraging AI, IoT, and a massive network of warehouses and sorting centers across over 200 countries, Cainiao enables merchants to ship efficiently worldwide, offering solutions such as same‑day delivery, automated customs clearance, and a digital parcel tracking ecosystem.
layout: provider
modified: '2026-10-06'
name: Cainiao
nav: Providers
network: true
overview: Cainiao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, E-Commerce, Supply Chain, and AlibabaGroup.
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cainiao Domain Security
  slug: cainiao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cainiao
tags:
- Company
- Logistics
- E-Commerce
- Supply Chain
- AlibabaGroup
website: https://www.cainiao.com/
---
