---
access_model:
  confidence: high
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 52
  human_in_the_loop: 1
  name: Audius Agentic Access
  operation_count: 207
  slug: audius-agentic-access
  summary_line: 207 operations · 52 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: Public REST API for the Audius network. Endpoints cover tracks (metadata, stream, trending), users (profile, followers), playlists, search, and resolve (lookup by URL). API hosts are discovered dynami
  name: Audius REST API
  slug: platform
- description: Challenge related operations
  name: Audius challenges API
  slug: audius-challenges-api
- description: The cid_data API from Audius — 1 operation(s) for cid_data.
  name: Audius cid_data API
  slug: audius-cid-data-api
- description: The coins API from Audius — 9 operation(s) for coins.
  name: Audius coins API
  slug: audius-coins-api
- description: Comment related operations
  name: Audius comments API
  slug: audius-comments-api
- description: Protocol dashboard wallet users related operations
  name: Audius dashboard_wallet_users API
  slug: audius-dashboard-wallet-users-api
- description: Developer app related operations
  name: Audius developer_apps API
  slug: audius-developer-apps-api
- description: Events related operations
  name: Audius events API
  slug: audius-events-api
- description: Explore related operations
  name: Audius explore API
  slug: audius-explore-api
- description: The notifications API from Audius — 2 operation(s) for notifications.
  name: Audius notifications API
  slug: audius-notifications-api
- description: Playlist related operations
  name: Audius playlists API
  slug: audius-playlists-api
- description: Prize claiming related operations
  name: Audius prizes API
  slug: audius-prizes-api
- description: The reactions API from Audius — 1 operation(s) for reactions.
  name: Audius reactions API
  slug: audius-reactions-api
- description: Audius Canonical URL resolver
  name: Audius resolve API
  slug: audius-resolve-api
- description: Rewards related operations
  name: Audius rewards API
  slug: audius-rewards-api
- description: The search API from Audius — 3 operation(s) for search.
  name: Audius search API
  slug: audius-search-api
- description: Tip related operations
  name: Audius tips API
  slug: audius-tips-api
- description: Track related operations
  name: Audius tracks API
  slug: audius-tracks-api
- description: The transactions API from Audius — 2 operation(s) for transactions.
  name: Audius transactions API
  slug: audius-transactions-api
- description: User related operations
  name: Audius users API
  slug: audius-users-api
- description: The wallet API from Audius — 1 operation(s) for wallet.
  name: Audius wallet API
  slug: audius-wallet-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Audius challenges API
  slug: open-audius-challenges-api
- collection_type: open
  name: Audius challenges cid_data API
  slug: open-audius-cid-data-api
- collection_type: open
  name: Audius challenges coins API
  slug: open-audius-coins-api
- collection_type: open
  name: Audius challenges comments API
  slug: open-audius-comments-api
- collection_type: open
  name: Audius challenges dashboard_wallet_users API
  slug: open-audius-dashboard-wallet-users-api
- collection_type: open
  name: Audius challenges developer_apps API
  slug: open-audius-developer-apps-api
- collection_type: open
  name: Audius challenges events API
  slug: open-audius-events-api
- collection_type: open
  name: Audius challenges explore API
  slug: open-audius-explore-api
- collection_type: open
  name: Audius challenges notifications API
  slug: open-audius-notifications-api
- collection_type: open
  name: Audius challenges playlists API
  slug: open-audius-playlists-api
- collection_type: open
  name: Audius challenges prizes API
  slug: open-audius-prizes-api
- collection_type: open
  name: Audius challenges reactions API
  slug: open-audius-reactions-api
- collection_type: open
  name: Audius challenges resolve API
  slug: open-audius-resolve-api
- collection_type: open
  name: Audius challenges rewards API
  slug: open-audius-rewards-api
- collection_type: open
  name: Audius challenges search API
  slug: open-audius-search-api
- collection_type: open
  name: Audius challenges tips API
  slug: open-audius-tips-api
- collection_type: open
  name: Audius challenges tracks API
  slug: open-audius-tracks-api
- collection_type: open
  name: Audius challenges transactions API
  slug: open-audius-transactions-api
- collection_type: open
  name: Audius challenges users API
  slug: open-audius-users-api
- collection_type: open
  name: Audius challenges wallet API
  slug: open-audius-wallet-api
- collection_type: open
  name: Audius API
  slug: open-audius
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/audius-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/audius-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/audius-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audius-project
- group: company
  title: ''
  type: Website
  url: https://audius.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.audius.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/audius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/audius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/audius-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://audius.co/llms.txt
created: '2026-05-08'
description: Audius is a decentralized open-source music streaming platform built on the Open Audio Protocol. It exposes a public REST API for tracks, users, playlists, search, and resolve, plus a JavaScript SDK. The protocol layer is open-source on GitHub.
finops:
- name: Audius Finops
  service_category: Music Streaming
  slug: audius-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the [Audius](https://audius.co/) decentralized music streaming platform, derived from the [Audius REST API](https://docs.audius.org/developers/a
  name: Audius GraphQL Schema
  slug: audius-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/audius.png
layout: provider
modified: '2026-05-08'
name: Audius
nav: Providers
network: true
overview: 'Audius publishes 20 APIs on the [APIs.io](https://apis.io/) network, including challenges API, cid_data API, coins API, and 17 more. Tagged areas include Music, Streaming, Decentralized, Web3, and Open Source.


  Audius'' developer surface includes authentication and 10 more developer resources.'
plans:
- name: Audius Plans Pricing
  plan_count: 1
  slug: audius-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 1
  name: Audius Rate Limits
  slug: audius-rate-limits
scopes:
- name: Audius Scopes
  scope_count: 2
  slug: audius-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 28.6
  delta: -1.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 59.1
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audius/refs/heads/main/screenshots/audius-2026-06-20T172554.png
security:
- kind: authentication
  name: Audius Authentication
  slug: audius-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Audius Domain Security
  slug: audius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: audius
tags:
- Music
- Streaming
- Decentralized
- Web3
- Open Source
- Blockchain
website: https://audius.co/
---
