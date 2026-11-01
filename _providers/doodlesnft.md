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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/doodlesnft/hosts/doodlesnft-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doodlesnft-hosts.yml
- group: other
  href: https://artifacts.apis.io/doodlesnft/vendors/doodlesnft-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doodlesnft-vendors.yml
- group: auth
  href: https://artifacts.apis.io/doodlesnft/security/doodlesnft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doodlesnft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/doodlesnft
coverage:
  checked: '2026-10-24'
  detail: The provider's homepage returns a JavaScript shell and rendering fails, preventing access to machine-readable docs.
  evidence:
  - status: 200
    url: https://doodlesnft.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Doodlesnft is a digital art and NFT platform that enables creators to mint, showcase, and trade unique collectible tokens on the blockchain. The company provides an API for developers to integrate NFT creation, ownership verification, and marketplace functionalities into their applications. It supports standard NFT metadata standards, offers webhooks for transaction events, and includes rate‑limit information for API usage. Doodlesnft aims to foster a vibrant community of artists, collectors, and developers by providing robust tooling and documentation for building NFT experiences.
layout: provider
modified: '2026-10-24'
name: Doodlesnft
nav: Providers
network: true
overview: Doodlesnft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, NFT, DigitalArt, Blockchain, and Marketplace.
random_paper: 18
score:
  band: minimal
  composite: 3.1
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doodlesnft Domain Security
  slug: doodlesnft-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doodlesnft
tags:
- Company
- NFT
- DigitalArt
- Blockchain
- Marketplace
- API
website: https://equityzen.com/company/doodlesnft
---
