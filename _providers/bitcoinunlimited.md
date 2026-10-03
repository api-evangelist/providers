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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinunlimited/refs/heads/main/hosts/bitcoinunlimited-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcoinunlimited-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitcoinunlimited/refs/heads/main/security/bitcoinunlimited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcoinunlimited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitcoinunlimited.org
coverage:
  checked: '2026-09-28'
  detail: Main site returns a JavaScript shell with no machine‑readable API spec
  evidence:
  - status: 200
    url: https://bitcoinunlimited.org
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bitcoin Unlimited is a community-driven organization focused on the development and promotion of Bitcoin as a peer‑to‑peer electronic cash system. It advocates for larger block sizes to increase transaction throughput, supports the Bitcoin Unlimited client software, and provides educational resources, forums, and tools for developers and users to engage with the Bitcoin ecosystem.
layout: provider
modified: '2026-09-28'
name: Bitcoinunlimited
nav: Providers
network: true
overview: Bitcoinunlimited is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bitcoin, Cryptocurrency, Open Source, and Community.
random_paper: 21
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitcoinunlimited Domain Security
  slug: bitcoinunlimited-domain-security
  summary_line: TLSv1.3
slug: bitcoinunlimited
tags:
- Company
- Bitcoin
- Cryptocurrency
- Open Source
- Community
website: https://bitcoinunlimited.org
---
