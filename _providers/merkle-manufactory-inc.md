---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The read/write REST interface a Snapchain node serves on port 3381 under the /v1 path. Read endpoints (casts, reactions, links, user data, verifications, fids, username proofs, storage limits, on-chai
  name: Snapchain HTTP API
  slug: snapchain-http-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merkle-manufactory-inc-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.farcaster.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.farcaster.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://snapchain.farcaster.xyz/reference/httpapi/httpapi
- group: start
  title: ''
  type: GettingStarted
  url: https://snapchain.farcaster.xyz/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/farcasterxyz
- group: start
  title: ''
  type: SignUp
  url: https://farcaster.xyz/
- group: operate
  title: ''
  type: Support
  url: https://farcaster.xyz/~/channel/fc-devs
- group: auth
  title: ''
  type: Authentication
  url: authentication/merkle-manufactory-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/merkle-manufactory-inc-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/merkle-manufactory-inc-conventions.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/merkle-manufactory-inc-rpc.proto
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/merkle-manufactory-inc-llms.txt
created: '2026-07-17'
description: 'Merkle Manufactory Inc. is the company that builds Farcaster, a sufficiently decentralized social network, and Snapchain, the blockchain-like peer-to-peer network that stores and syncs Farcaster''s social data. Its developer surface is open and protocol-based rather than a single hosted product API: Snapchain nodes serve an HTTP API (port 3381, /v1) and a gRPC API (port 3383) for reading casts, reactions, links, user data, verifications and on-chain events and for submitting signed messages; Mini Apps (formerly Frames v2) run inside the Farcaster feed; and Sign In with Farcaster (SIWF) plus AuthKit provide identity for third-party apps. The stack is fully open source under the farcasterxyz GitHub organization. Backed by a16z.'
image: https://docs.farcaster.xyz/og-image.png
layout: provider
modified: '2026-07-20'
name: Merkle Manufactory Inc.
nav: Providers
network: true
overview: 'Merkle Manufactory Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Decentralized Social, Protocol, and Blockchain.


  Merkle Manufactory Inc.''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 7 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/merkle-manufactory-inc/refs/heads/main/screenshots/merkle-manufactory-inc-2026-08-07T172606.png
security:
- kind: authentication
  name: Merkle Manufactory Inc Authentication
  slug: merkle-manufactory-inc-authentication
  summary_line: none/signed-message · 2 schemes
- kind: domain-security
  name: Merkle Manufactory Inc Domain Security
  slug: merkle-manufactory-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: merkle-manufactory-inc
tags:
- Company
- Social
- Decentralized Social
- Protocol
- Blockchain
- Web3
- Developer Platform
- Farcaster
website: https://docs.farcaster.xyz/
---
