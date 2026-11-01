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
api_count: 1
apis:
- description: Machine Control Protocol (MCP) API providing tool list and other operations for Twelve Permissions.
  name: Twelve Permissions MCP API
  slug: twelve-permissions-mcp-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/twelvepermissions-com/llms/twelvepermissions-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twelvepermissions-com-llms.txt
- group: other
  href: https://artifacts.apis.io/twelvepermissions-com/hosts/twelvepermissions-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/twelvepermissions-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/twelvepermissions-com/vendors/twelvepermissions-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/twelvepermissions-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/twelvepermissions-com/security/twelvepermissions-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twelvepermissions-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://twelvepermissions.com/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered despite MCP being harvestable.
  evidence:
  - status: 200
    url: https://twelvepermissions.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Twelve Permissions is a blockchain‑based project on the XRP Ledger that issues a series of twelve unique digital permissions. Each permission is minted as an NFT, with the final one contingent on delivering a robot dog to Anchorage. The platform showcases tokenized access rights, integrates with XRPL accounts, and demonstrates novel use‑cases for NFTs and decentralized finance.
layout: provider
modified: '2026-10-30'
name: twelvepermissions-com
nav: Providers
network: true
overview: twelvepermissions-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, NFT, XRP Ledger, and Digital Permissions.
random_paper: 7
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
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
  name: Twelvepermissions Com Domain Security
  slug: twelvepermissions-com-domain-security
  summary_line: TLSv1.3
slug: twelvepermissions-com
tags:
- Company
- Blockchain
- NFT
- XRP Ledger
- Digital Permissions
website: https://twelvepermissions.com/
---
