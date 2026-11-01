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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/theblockcrypto-com/llms/theblockcrypto-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/theblockcrypto-com-llms.txt
- group: other
  href: https://artifacts.apis.io/theblockcrypto-com/hosts/theblockcrypto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theblockcrypto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/theblockcrypto-com/vendors/theblockcrypto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/theblockcrypto-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/theblockcrypto-com/security/theblockcrypto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theblockcrypto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.theblock.co
created: '2026-10-21'
description: The Block is a leading media and research platform covering the digital asset and cryptocurrency industry. It provides news, analysis, data, and research reports to professionals, investors, and enthusiasts. The company offers a subscription-based service with in‑depth market insights, price indexes, and industry events, positioning itself as a primary source of information in the crypto ecosystem.
layout: provider
modified: '2026-10-21'
name: The Block
nav: Providers
network: true
overview: The Block is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Cryptocurrency, Research, and News.
random_paper: 9
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Theblockcrypto Com Domain Security
  slug: theblockcrypto-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: theblockcrypto-com
tags:
- Company
- Media
- Cryptocurrency
- Research
- News
website: https://www.theblock.co
---
