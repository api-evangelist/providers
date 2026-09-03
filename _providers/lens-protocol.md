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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: The Lens API is a hosted GraphQL endpoint that indexes the Lens Chain contracts and exposes queries and mutations for accounts, posts (publications), feeds, follows, groups, apps, notifications, and s
  name: Lens API (GraphQL)
  slug: lens-api
- description: The Lens SDK is the official TypeScript client for the Lens API. It wraps GraphQL operations behind typed functions, handles auth token lifecycle, encodes content metadata (Lens metadata standards), a
  name: Lens TypeScript SDK
  slug: lens-sdk
- description: The Lens React SDK provides React hooks (useAccount, usePosts, useFollow, useLogin, etc.) layered on top of the Lens client SDK, so frontend developers can wire Lens primitives into UIs without hand-r
  name: Lens React SDK
  slug: lens-react-sdk
- description: The Lens v3 smart contracts implement the onchain social graph on Lens Chain. Core primitives include Accounts (user identity owned by a wallet), Apps (namespaces that publish content), Feeds (ordered
  name: Lens Protocol Smart Contracts
  slug: lens-contracts
- description: 'Lens authentication uses a sign-in-with-Ethereum style challenge: a client requests a signing message from the Lens API, the user signs it with their wallet, and the API returns short-lived access and'
  name: Lens Authentication
  slug: lens-authentication
- description: Lens content (post body, media, profile metadata) is stored as JSON following the Lens Metadata Standards and pinned to decentralized storage (IPFS, Arweave, or Lens-hosted storage). The metadata stan
  name: Lens Storage & Metadata
  slug: lens-storage
artifact_total: 11
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/lens-protocol/lens-sdk/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/lens-protocol/lens-sdk/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lens-protocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lens.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://lens.xyz/docs
- group: other
  title: ''
  type: API
  url: https://lens.xyz/docs/api
- group: build
  title: ''
  type: SDKs
  url: https://lens.xyz/docs/sdk
- group: other
  title: ''
  type: Protocol
  url: https://lens.xyz/docs/protocol
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lens-protocol
- group: other
  title: ''
  type: Explorer
  url: https://explorer.lens.xyz/
- group: company
  title: ''
  type: Blog
  url: https://lens.xyz/news
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LensProtocol
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/lensprotocol
created: '2026-05-23'
description: Lens Protocol is an onchain social graph and a developer platform for building social applications where users own their profile, content, and relationships. Originally launched on Polygon PoS, Lens has since evolved into Lens Chain — an L2 zkEVM rollup purpose-built for social — with the Lens v3 contracts redesigned around primitives like Accounts, Apps, Feeds, Groups, Graphs, and Actions. Developers integrate Lens through the Lens API (a GraphQL gateway over the indexed chain state), the Lens TypeScript SDK and React SDK, the underlying smart contracts, and an authentication layer that issues short-lived auth tokens after a SIWE-style signature. Lens powers social clients (Hey, Orb, Tape, Buttrfly), creator tools, and composable mini-apps that share the same onchain social graph.
finops:
- name: Lens Protocol Finops
  service_category: API
  slug: lens-protocol-finops
graphqls:
- description: The Lens API is a hosted GraphQL endpoint that indexes the Lens
  name: Lens Protocol GraphQL API
  slug: lens-protocol-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lens-protocol.png
layout: provider
modified: '2026-05-23'
name: Lens Protocol
nav: Providers
network: true
overview: 'Lens Protocol publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Lens Protocol, Onchain Social, Web3, Social Graph, and Polygon.


  Lens Protocol''s developer surface includes documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Lens Protocol Plans Pricing
  plan_count: 1
  slug: lens-protocol-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Lens Protocol Rate Limits
  slug: lens-protocol-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 21.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Lens Protocol Domain Security
  slug: lens-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lens-protocol
tags:
- Lens Protocol
- Onchain Social
- Web3
- Social Graph
- Polygon
- Lens Chain
- zkEVM
- GraphQL
- Smart Contracts
- Decentralized Identity
website: https://lens.xyz/
---
