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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/softbank/refs/heads/main/llms/softbank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/softbank-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/softbank/refs/heads/main/hosts/softbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/softbank-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/softbank/refs/heads/main/vendors/softbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/softbank-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.softbank.jp/en/support/
- group: auth
  title: ''
  type: Security
  url: https://www.softbank.jp/en/corp/aboutus/governance/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.softbank.jp/en/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.softbank.jp/en/corp/news/press/sbkk/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/softbank/refs/heads/main/security/softbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/softbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.softbank.jp/en/
coverage:
  checked: '2026-10-13'
  detail: SoftBank's developer pages are absent and no machine‑readable API specifications were discovered.
  evidence:
  - status: 0
    url: https://api.softbank.jp/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: SoftBank Corp. is a multinational conglomerate headquartered in Tokyo, Japan, operating across telecommunications, internet services, AI, robotics, and investment. The company provides a wide range of consumer and enterprise services, including mobile communications, broadband, energy solutions, and a portfolio of technology investments. Its public website offers information on corporate philosophy, sustainability initiatives, news, and support resources, reflecting its role as a major player in the global technology and finance sectors.
image: https://www.softbank.jp/site/set/common/shared/img/icon_softbank.gif
layout: provider
modified: '2026-10-13'
name: SoftBank
nav: Providers
network: true
overview: 'SoftBank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Technology, Investment, and Artificial Intelligence.


  SoftBank''s developer surface includes support and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Softbank Domain Security
  slug: softbank-domain-security
  summary_line: TLSv1.3
slug: softbank
tags:
- Company
- Telecommunications
- Technology
- Investment
- Artificial Intelligence
- Robotics
website: https://www.softbank.jp/en/
---
