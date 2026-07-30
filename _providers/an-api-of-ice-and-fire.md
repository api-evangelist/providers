---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: An Api Of Ice And Fire Agentic Access
  operation_count: 7
  slug: an-api-of-ice-and-fire-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: Books in the A Song of Ice and Fire series.
  name: An API of Ice And Fire Books API
  slug: an-api-of-ice-and-fire-books-api
- description: Characters from the A Song of Ice and Fire universe.
  name: An API of Ice And Fire Characters API
  slug: an-api-of-ice-and-fire-characters-api
- description: Noble houses of Westeros and Essos.
  name: An API of Ice And Fire Houses API
  slug: an-api-of-ice-and-fire-houses-api
- description: API entry-point listing the top-level resource URLs.
  name: An API of Ice And Fire Root API
  slug: an-api-of-ice-and-fire-root-api
artifact_total: 9
collections:
- collection_type: open
  name: An API of Ice And Fire
  slug: open-an-api-of-ice-and-fire
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/an-api-of-ice-and-fire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/an-api-of-ice-and-fire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anapioficeandfire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anapioficeandfire.com/Documentation
- group: docs
  title: Project Wiki
  type: Documentation
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/wiki
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/joakimskoog/AnApiOfIceAndFire
- group: commercial
  title: BSD 3-Clause-like (see LICENSE.md)
  type: License
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/blob/master/LICENSE.md
- group: docs
  title: ''
  type: ContributingGuide
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/blob/master/CONTRIBUTING.md
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/joakimskoog/AnApiOfIceAndFire
- group: build
  title: Maintainer
  type: GitHubOrganization
  url: https://github.com/joakimskoog
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/an-api-of-ice-and-fire-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/an-api-of-ice-and-fire-vocabulary.yml
created: '2026-05-28'
description: An API of Ice And Fire is the world's greatest source for quantified and structured data from the universe of A Song of Ice and Fire (and the HBO series Game of Thrones). The open, read-only REST API exposes Books, Characters, and Houses as hypermedia resources with HAL-style URL references, RFC 5988 Link-header pagination, conditional caching, and version selection via custom media types. It is free, unauthenticated, and rate-limited at 20,000 requests per IP per day.
graphqls:
- description: ''
  name: An API of Ice And Fire GraphQL API
  slug: an-api-of-ice-and-fire-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/an-api-of-ice-and-fire.png
layout: provider
modified: '2026-05-30'
name: An API of Ice And Fire
nav: Providers
network: true
overview: 'An API of Ice And Fire publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Books API, Characters API, Houses API, and 1 more. Tagged areas include Video, Public APIs, Open Source, Game of Thrones, and A Song of Ice and Fire.


  The An API of Ice And Fire catalog on APIs.io includes 1 Spectral governance ruleset.


  An API of Ice And Fire''s developer surface includes documentation and 12 more developer resources.'
random_paper: 25
rules:
- name: An API of Ice And Fire API Rules
  rule_count: 53
  severity_counts:
    error: 16
    hint: 0
    info: 11
    warn: 26
  slug: an-api-of-ice-and-fire-spectral-rules
score:
  band: emerging
  composite: 26.3
  delta: -5.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 44.1
    developer_ergonomics: 8.7
    discoverability: 81.5
    governance: 47.9
    operational_transparency: 5.3
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/an-api-of-ice-and-fire/refs/heads/main/screenshots/an-api-of-ice-and-fire-2026-06-20T171942.png
security:
- kind: domain-security
  name: An Api Of Ice And Fire Domain Security
  slug: an-api-of-ice-and-fire-domain-security
  summary_line: TLSv1.3 · HSTS
slug: an-api-of-ice-and-fire
tags:
- Video
- Public APIs
- Open Source
- Game of Thrones
- A Song of Ice and Fire
- Fan API
- Hypermedia
- HAL
- REST
- Open Data
- Entertainment
website: https://anapioficeandfire.com/
---
