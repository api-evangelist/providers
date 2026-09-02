---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Sandbox Developers API is the REST surface of The Sandbox Developers HUB. It exposes core ecosystem data behind an OAuth-based identity system - Sandbox user identity, avatars, assets, collections
  name: The Sandbox Developers API
  slug: the-sand-box-developers-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-sand-box-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sandbox.game/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.sandbox.game/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sandbox.game/en
- group: docs
  title: ''
  type: APIReference
  url: https://developers.sandbox.game/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.sandbox.game/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://docs.sandbox.game/en/general/helpcontact
- group: company
  title: ''
  type: Blog
  url: https://www.sandbox.game/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/sandbox-game
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thesandboxgame
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sandbox.game/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sandbox.game/en/privacypolicy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-sand-box-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/the-sand-box-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/the-sand-box-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-sand-box-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-sand-box-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-sand-box-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-sand-box-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/the-sand-box-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-sand-box-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/the-sand-box-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-sand-box-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-sand-box-data-model.yml
created: '2026-08-30'
description: The Sandbox is a user-generated-content metaverse and voxel gaming platform operated by TSB Gaming Ltd (a subsidiary of Animoca Brands), where players and creators build, own and monetise voxel games and assets on Ethereum and Polygon using the SAND token, LAND parcels and ERC-721/ERC-1155 ASSETs. Its creator toolchain is VoxEdit (NFT and avatar designer) and Game Maker (experience designer), with a marketplace for trading assets. For developers The Sandbox runs a Developers HUB publishing a REST API for identity, avatars, assets, collections, libraries and LAND ownership, an OAuth-based identity system, a Swagger playground, and a Developer SDK for Unity distributed as a Unity Package Manager Git dependency. It also publishes its smart-contract source and a set of first-party npm packages under the @sandbox-smart-contracts scope.
image: https://avatars.githubusercontent.com/u/63786662?v=4
layout: provider
modified: '2026-08-30'
name: The Sandbox
nav: Providers
network: true
overview: 'The Sandbox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Metaverse, Gaming, Blockchain, and NFT.


  The Sandbox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 17 more developer resources.'
plans:
- name: The Sand Box Plans Pricing
  plan_count: 0
  slug: the-sand-box-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: The Sand Box Rate Limits
  slug: the-sand-box-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 27.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: The Sand Box Authentication
  slug: the-sand-box-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: The Sand Box Domain Security
  slug: the-sand-box-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: The Sand Box Vulnerability Disclosure
  slug: the-sand-box-vulnerability-disclosure
  summary_line: disclosure policy published
slug: the-sand-box
tags:
- Company
- Metaverse
- Gaming
- Blockchain
- NFT
- Web3
- Virtual Worlds
- User Generated Content
- Ethereum
- Identity
website: https://www.sandbox.game/
---
