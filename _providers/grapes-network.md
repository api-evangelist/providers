---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Grape DAO products providing on‑chain identity, reputation, access and governance primitives.
  name: Grape DAO API
  slug: grape-dao-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/grapes-network/llms/grapes-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grapes-network-llms.txt
- group: agent
  href: https://artifacts.apis.io/grapes-network/well-known/grapes-network-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grapes-network-well-known.yml
- group: other
  href: https://artifacts.apis.io/grapes-network/hosts/grapes-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grapes-network-hosts.yml
- group: other
  href: https://artifacts.apis.io/grapes-network/vendors/grapes-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grapes-network-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Grape-Labs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.grapes.network/grape-network/quick-start-and-faq
- group: docs
  title: ''
  type: Documentation
  url: https://docs.grapes.network/
- group: auth
  href: https://artifacts.apis.io/grapes-network/security/grapes-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grapes-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grapes.network
coverage:
  checked: '2026-10-26'
  detail: Docs are served as a JavaScript‑rendered GitBook site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://grapedao.gitbook.io/products/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Grapes (operating as Grape DAO) is a Solana‑based platform that provides on‑chain identity, reputation, access control, and governance primitives for decentralized communities. It enables developers to integrate verifiable reputation scores, permissioned access, and community voting mechanisms into their dApps, leveraging the security and composability of the Solana blockchain.
image: https://grapedao.org/opengraph-image?162c47b55c3b726f
layout: provider
modified: '2026-10-25'
name: Grapes
nav: Providers
network: true
overview: 'Grapes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Reputation, Access Control, Governance, and DAO Infrastructure.


  Grapes'' developer surface includes getting-started guide, documentation, and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 5.3
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
  name: Grapes Network Domain Security
  slug: grapes-network-domain-security
  summary_line: TLSv1.3 · HSTS
slug: grapes-network
tags:
- Identity
- Reputation
- Access Control
- Governance
- DAO Infrastructure
- Discord Bots
- Solana
website: https://grapes.network
---
