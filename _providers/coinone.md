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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/security/coinone-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/coinone-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/llms/coinone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinone-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/hosts/coinone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinone-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/vendors/coinone-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinone-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/packages/coinone-packages.yml
  title: ''
  type: SDKs
  url: packages/coinone-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/packages/coinone-packages.yml
  title: ''
  type: Packages
  url: packages/coinone-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/security/coinone-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinone-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinone/refs/heads/main/security/coinone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinone.co.kr/
created: '2026-10-09'
description: Coinone (코인원) is a South Korean cryptocurrency exchange offering trading of Bitcoin, Ethereum, and other digital assets. It provides a user-friendly platform with features such as staking, smart trading, and a public Open API for developers. The exchange emphasizes security, fast transaction processing, and a range of services including fiat deposits, withdrawals, and market insights.
layout: provider
modified: '2026-10-09'
name: Coinone
nav: Providers
network: true
overview: Coinone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 6.6
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
    developer_ergonomics: 7.1
    discoverability: 42.9
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinone Domain Security
  slug: coinone-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coinone Vulnerability Disclosure
  slug: coinone-vulnerability-disclosure
  summary_line: no policy recorded
slug: coinone
tags:
- Company
website: https://coinone.co.kr/
---
