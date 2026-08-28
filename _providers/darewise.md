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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/darewise-domain-security.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/darewise-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/darewise-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/darewise-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.lifebeyondstudios.com/
- group: company
  title: ''
  type: About
  url: https://www.lifebeyondstudios.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.lifebeyondstudios.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.lifebeyondstudios.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Darewise
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Darewise/asyncapi-template-cpp-ue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lifebeyondstudios
- group: other
  title: ''
  type: ParentCompany
  url: https://www.animocabrands.com/
coverage:
  checked: '2026-08-17'
  detail: Darewise ships a consumer game and nothing else — the legacy brand host www.darewise.com now refuses TCP on both 443 and 80 (its last Internet Archive capture serving HTTP 200 is 2025-04-21), the live successor host www.lifebeyondstudios.com returns a real origin 404 for /llms.txt and for every /.well-known/* path while answering all HTML and API-shaped paths with a Cloudflare "Just a moment..." 403 interstitial, no api./docs./developer. subdomain resolves in DNS on either domain, and the studio's only first-party developer artifact anywhere is an unmaintained Apache-2.0 AsyncAPI generator template for Unreal Engine on npm (v0.1.3, 2023-12-11) — a code generator, not an API.
  evidence:
  - status: 0
    url: https://www.darewise.com/
  - status: 404
    url: https://www.lifebeyondstudios.com/.well-known/agent-card.json
  - status: 404
    url: https://www.lifebeyondstudios.com/.well-known/security.txt
  - status: 404
    url: https://www.lifebeyondstudios.com/.well-known/api-catalog
  - status: 404
    url: https://www.lifebeyondstudios.com/llms.txt
  - status: 403
    url: https://www.lifebeyondstudios.com/openapi.json
  - status: 403
    url: https://www.lifebeyondstudios.com/graphql
  - status: 200
    url: https://www.lifebeyondstudios.com/robots.txt
  - status: 200
    url: https://registry.npmjs.org/@darewise%2Fasyncapi-template-cpp-ue
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Darewise Entertainment is a European game studio founded by AAA industry veterans — game director Benjamin Charbit (Assassin''s Creed IV: Black Flag) and engine tech lead Samuel Kahn (Ubisoft Snowdrop, Crytek CryEngine) — with offices in Paris, London and Barcelona. It builds Life Beyond, a free-to-play sci-fi MMO on Unreal Engine 5 set on the alien world Dolos, combining Web3 asset ownership (NFTs and ERC-20 tokens) with player-driven settlement and governance. Animoca Brands announced the acquisition of a majority stake in April 2022, and the studio now trades as Life Beyond Studios. The original darewise.com website last served content in April 2025 and the host now refuses TCP connections on 80 and 443. Darewise publishes no API, developer portal, or API documentation of any kind; the only machine-readable developer artifact it has ever released publicly is an open-source AsyncAPI generator template that emits Unreal Engine C++ from an AsyncAPI 3.x document, published to
  npm under its own scope.'
image: https://avatars.githubusercontent.com/u/35532823?v=4
layout: provider
modified: '2026-08-17'
name: Darewise
nav: Providers
network: true
overview: Darewise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Games, Game Development, and Web3.
random_paper: 12
score:
  band: minimal
  composite: 6.1
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Darewise Domain Security
  slug: darewise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: darewise
tags:
- Company
- Blockchain
- Games
- Game Development
- Web3
- NFT
- Metaverse
- Unreal Engine
- Entertainment
- Open-Source
website: https://www.lifebeyondstudios.com/
---
