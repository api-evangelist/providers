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
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/llms/bancor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bancor-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/well-known/bancor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bancor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/hosts/bancor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bancor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/vendors/bancor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bancor-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/packages/bancor-packages.yml
  title: ''
  type: SDKs
  url: packages/bancor-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/packages/bancor-packages.yml
  title: ''
  type: Packages
  url: packages/bancor-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.bancor.network/
- group: auth
  title: ''
  type: Security
  url: https://support.bancor.network/resources/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bancorprotocol
- group: company
  title: ''
  type: Blog
  url: https://blog.bancor.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bancor.network/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancor/refs/heads/main/security/bancor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bancor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bancor.network/
coverage:
  checked: '2026-09-27'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec could be retrieved.
  evidence:
  - status: 200
    url: https://docs.bancor.network/guides/rest-api/api-reference.md
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Bancor is a decentralized liquidity network that enables users to convert tokens instantly and securely. Founded in 2017, Bancor provides on‑chain liquidity, automated market making, and a suite of tools for token projects and traders across multiple blockchains, including Ethereum, Celo, and others. The platform offers adjustable strategies, liquidity management, and arbitrage infrastructure to maintain price parity across decentralized exchanges.
image: https://framerusercontent.com/assets/Ge6tkw9lQSaRvH2tTNsL5262xQ.png
layout: provider
modified: '2026-09-27'
name: Bancor
nav: Providers
network: true
overview: 'Bancor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Liquidity, Blockchain, and Tokens.


  Bancor''s developer surface includes support, engineering blog, documentation, and 10 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 15.8
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
  name: Bancor Domain Security
  slug: bancor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bancor
tags:
- Company
- DeFi
- Liquidity
- Blockchain
- Tokens
website: https://bancor.network/
---
