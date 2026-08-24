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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Farcaster Agentic Access
  operation_count: 27
  slug: farcaster-agentic-access
  summary_line: 27 operations · 3 acting
api_count: 15
apis:
- description: Query interface for Farcaster's Snapchain network - read casts, reactions, follows, user data, and verifications by FID; submit signed messages; and run a Snapchain node for full replication. Public r
  name: Snapchain / Hub API
  slug: snapchain
- description: JavaScript SDK for building Mini Apps (the evolution of Frames) that run inside Farcaster feeds and clients. Provides host bridge, context, wallet actions, notifications, and analytics for permissionl
  name: Farcaster Mini Apps SDK
  slug: mini-apps-sdk
- description: Authentication flow that lets users sign in to third-party apps with their Farcaster identity, returning a verified FID and optional profile data. Backed by EIP-4361-style signed messages.
  name: Sign In with Farcaster (SIWF)
  slug: siwf
- description: React toolkit wrapping Sign In with Farcaster - provides hooks and components for the QR-code / deep-link handoff to a Farcaster client and returns the verified user context to the host app.
  name: Farcaster AuthKit (React)
  slug: auth-kit
- description: 'Third-party indexer providing hosted Hub access, indexed read APIs (users, casts, channels, feeds), write APIs (publish casts, reactions, follows), webhooks for real-time events, a Node.js SDK, and a '
  name: Neynar Hosted Farcaster API
  slug: neynar
- description: Client-side API exposed by the Warpcast / Farcaster app for client-specific surfaces (channels, mentions, direct casts, mini-app contexts) layered above the Snapchain protocol APIs.
  name: Warpcast / Farcaster Client API
  slug: warpcast-api
- description: The Casts API from Farcaster — 4 operation(s) for casts.
  name: Farcaster Casts API
  slug: farcaster-casts-api
- description: The Events API from Farcaster — 2 operation(s) for events.
  name: Farcaster Events API
  slug: farcaster-events-api
- description: The Info API from Farcaster — 2 operation(s) for info.
  name: Farcaster Info API
  slug: farcaster-info-api
- description: The Links API from Farcaster — 3 operation(s) for links.
  name: Farcaster Links API
  slug: farcaster-links-api
- description: The OnChain API from Farcaster — 4 operation(s) for onchain.
  name: Farcaster OnChain API
  slug: farcaster-onchain-api
- description: The Reactions API from Farcaster — 4 operation(s) for reactions.
  name: Farcaster Reactions API
  slug: farcaster-reactions-api
- description: The Submit API from Farcaster — 3 operation(s) for submit.
  name: Farcaster Submit API
  slug: farcaster-submit-api
- description: The UserData API from Farcaster — 4 operation(s) for userdata.
  name: Farcaster UserData API
  slug: farcaster-userdata-api
- description: The Verifications API from Farcaster — 1 operation(s) for verifications.
  name: Farcaster Verifications API
  slug: farcaster-verifications-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts API
  slug: open-farcaster-casts-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts Events API
  slug: open-farcaster-events-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts Info API
  slug: open-farcaster-info-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts Links API
  slug: open-farcaster-links-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts OnChain API
  slug: open-farcaster-onchain-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts Reactions API
  slug: open-farcaster-reactions-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts Submit API
  slug: open-farcaster-submit-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts UserData API
  slug: open-farcaster-userdata-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP Casts Verifications API
  slug: open-farcaster-verifications-api
- collection_type: open
  name: Farcaster Snapchain Hub HTTP API
  slug: open-farcaster
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/farcaster-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farcaster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.farcaster.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.farcaster.xyz/
- group: other
  title: ''
  type: Mini Apps
  url: https://miniapps.farcaster.xyz/
- group: other
  title: ''
  type: Snapchain
  url: https://snapchain.farcaster.xyz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/farcasterxyz
- group: other
  title: ''
  type: Neynar
  url: https://neynar.com/
created: '2026-05-23'
description: Farcaster is a decentralised social protocol built on Snapchain, an append-only state machine that stores casts, reactions, follows, and user profile data. The protocol publishes a Hub / Snapchain reference implementation, the Mini Apps SDK (formerly Frames) for distributing interactive apps inside Farcaster feeds, Sign In with Farcaster (SIWF) for authentication, and AuthKit for React-based sign-in. The Warpcast client (now rebranded Farcaster app at farcaster.xyz) is the primary consumer surface. Indexer providers such as Neynar host scaled Hub APIs and value-added read / write / webhook APIs at api.neynar.com.
finops:
- name: Farcaster Finops
  service_category: API
  slug: farcaster-finops
graphqls:
- description: 'title: Farcaster GraphQL Schema'
  name: Farcaster GraphQL Schema
  slug: farcaster-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farcaster.png
layout: provider
modified: '2026-05-23'
name: Farcaster
nav: Providers
network: true
overview: 'Farcaster publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Casts API, Events API, Info API, and 6 more. Tagged areas include Social, Decentralized, Protocol, Mini Apps, and Frames.


  Farcaster''s developer surface includes documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Farcaster Plans Pricing
  plan_count: 1
  slug: farcaster-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Farcaster Rate Limits
  slug: farcaster-rate-limits
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.6
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/farcaster/refs/heads/main/screenshots/farcaster-2026-06-20T181039.png
security:
- kind: domain-security
  name: Farcaster Domain Security
  slug: farcaster-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: farcaster
tags:
- Social
- Decentralized
- Protocol
- Mini Apps
- Frames
- Authentication
- Web3
- SDK
website: https://www.farcaster.xyz/
---
