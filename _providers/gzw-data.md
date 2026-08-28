---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Read-only JSON REST API for Gray Zone Warfare game data, backed by an OpenAPI 3.0 contract. Datasets are auto-discovered; supports filtering, full-text search, sorting and pagination. No API key requi
  name: GZW Data API
  slug: gzw-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gzw-data-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gzw-data.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://gzw-data.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://gzw-data.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://gzw-data.dev/docs/#quickstart
- group: start
  title: ''
  type: Console
  url: https://gzw-data.dev/#explorer
- group: operate
  title: ''
  type: Support
  url: https://github.com/ZoniBoy00/gzw-data/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZoniBoy00
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ZoniBoy00/gzw-data
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/ZoniBoy00/gzw-data-js/blob/main/ROADMAP.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gzw-data.dev/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gzw-data.dev/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/gzw-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gzw-data-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gzw-data-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gzw-data-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gzw-data-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gzw-data-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gzw-data-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gzw-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gzw-data-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gzw-data-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gzw-data-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: GZW Data is a free, fan-made, read-only REST API for Gray Zone Warfare game data, published by independent maintainer ZoniBoy00 and hosted on Vercel at gzw-data.dev. It exposes 85+ datasets auto-discovered from a wiki-scraped data directory - weapons, ammo, armor, magazines, attachments, tasks and missions, keys and keycards, loot containers, medical, provisions, gear and vendors - behind one uniform JSON envelope with equality filters, full-text search, sorting and page-number pagination. Three smart routes union related datasets (armor, weapon_parts, helmet_mods). There is no authentication, no account and no API key; access is governed by a best-effort limit of 100 requests per minute per IP with X-RateLimit-* headers. An OpenAPI 3.0.3 contract, an llms.txt and a zero-dependency TypeScript client on npm are published. Data is scraped weekly from the community GZW Fandom Wiki; the project is unofficial and not affiliated with the game's publisher.
image: https://gzw-data.dev/assets/gzw-data-logo.png
layout: provider
modified: '2026-08-26'
name: GZW Data API
nav: Providers
network: true
overview: 'GZW Data API publishes 1 API on the [APIs.io](https://apis.io/) network: GZW Data API. Tagged areas include gaming, video-games, gray-zone-warfare, game-data, and developer-tools.


  GZW Data API''s developer surface includes documentation, API reference, getting-started guide, developer console, support, authentication, and 18 more developer resources.'
plans:
- name: Gzw Data Plans Pricing
  plan_count: 1
  slug: gzw-data-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Gzw Data Rate Limits
  slug: gzw-data-rate-limits
score:
  band: developing
  composite: 45.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 16.7
    contract_quality: 26.7
    developer_ergonomics: 70.8
    discoverability: 70.4
    governance: 16.7
    operational_transparency: 28.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Gzw Data Authentication
  slug: gzw-data-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gzw Data Domain Security
  slug: gzw-data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: gzw-data
tags:
- gaming
- video-games
- gray-zone-warfare
- game-data
- developer-tools
- open-data
- openapi
- weapons
- missions
- loot
- rest-api
- public-api
- no-auth
- read-only
- free-api
- community
website: https://gzw-data.dev/
---
