---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The CyberConnect GraphQL Indexer API provides precise and flexible queries for social graph data. Developers can query address identities, follower and following lists, social connections between addr
  name: CyberConnect GraphQL API
  slug: cyberconnect-graphql-api
- description: The CyberConnect JavaScript SDK provides connect and disconnect (follow and unfollow) functions for writing social graph connection data. It encapsulates complex authentication logic with Ceramic Netw
  name: CyberConnect JavaScript SDK
  slug: cyberconnect-javascript-sdk
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyberconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyber.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cyber.co/
- group: docs
  title: ''
  type: LegacyDocumentation
  url: https://cyberconnect-docs-v2.vercel.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyberconnecthq
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/cyberconnect
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/CyberConnectHQ
- group: company
  title: ''
  type: Blog
  url: https://cyber.co/blog
- group: other
  title: ''
  type: StarterRepository
  url: https://github.com/cyberconnecthq/cyberconnect-starter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cyber.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cyber.co/privacy
- group: operate
  title: ''
  type: Forums
  url: https://forum.cyberconnect.me
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cyberconnect/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cyberconnect/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cyberconnect/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: CyberConnect is a Web3 social graph protocol that enables developers to build decentralized social applications. It provides GraphQL and SDK-based APIs for accessing social graphs, profiles, followers, connections, and recommendation data across Ethereum and Solana networks. The protocol stores user-generated social data in a decentralized manner, allowing users to truly own their identities, content, and connections.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: The CyberConnect GraphQL API is the primary interface for the CyberConnect Web3 social graph protocol. It exposes a comprehensive set of queries and mutations for interacting with decentralized social
  name: CyberConnect GraphQL API
  slug: cyberconnect-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cyberconnect.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: CyberConnect
nav: Providers
network: true
overview: 'CyberConnect publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Web3, Social Graph, Decentralized, GraphQL, and Blockchain.


  The CyberConnect catalog on APIs.io includes 1 JSON-LD context.


  CyberConnect''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.4
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyberconnect/refs/heads/main/screenshots/cyberconnect-2026-06-20T175407.png
security:
- kind: domain-security
  name: Cyberconnect Domain Security
  slug: cyberconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cyberconnect
tags:
- Web3
- Social Graph
- Decentralized
- GraphQL
- Blockchain
- Social Network
- Identity
website: https://cyber.co/
---
