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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bittrexllc/refs/heads/main/hosts/bittrexllc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bittrexllc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bittrexllc/refs/heads/main/vendors/bittrexllc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bittrexllc-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bittrex
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bittrexllc/refs/heads/main/security/bittrexllc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bittrexllc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bittrex.com
coverage:
  checked: '2026-09-28'
  detail: Main website loads API information via JavaScript without providing a static OpenAPI spec.
  evidence:
  - status: 200
    url: https://bittrex.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bittrex LLC is a leading cryptocurrency exchange founded in 2014, offering a secure platform for buying, selling, and trading a wide variety of digital assets. The exchange provides advanced trading features, robust security measures, and a comprehensive API suite that enables developers to integrate market data, order execution, and account management into their applications. Bittrex serves retail and institutional clients worldwide, emphasizing compliance, liquidity, and a user-friendly experience across web, mobile, and API interfaces.
layout: provider
modified: '2026-09-28'
name: Bittrexllc
nav: Providers
network: true
overview: Bittrexllc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 7
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 0
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bittrexllc Domain Security
  slug: bittrexllc-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: bittrexllc
tags:
- Company
website: https://bittrex.com
---
