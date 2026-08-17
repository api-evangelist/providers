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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: 'NIP-01 defines the core Nostr protocol: event format (id, pubkey, created_at, kind, tags, content, sig), client-to-relay messages (EVENT, REQ, CLOSE), and relay-to-client messages (EVENT, OK, EOSE, CL'
  name: Nostr Protocol (NIP-01)
  slug: nostr-protocol
- description: NIPs are the standards documents that extend Nostr beyond the core protocol. They define event kinds (text notes, reactions, zaps, long-form articles, DMs, calendar events, marketplaces), client behav
  name: Nostr Implementation Possibilities (NIPs)
  slug: nostr-nips
- description: 'A Nostr relay is a WebSocket server that accepts signed events, stores them subject to its own policy, and responds to subscription filters from clients. The relay surface is intentionally minimal: no'
  name: Nostr Relay WebSocket Interface
  slug: relay-interface
- description: 'nostr-tools is the de-facto JavaScript/TypeScript library for Nostr clients and bots. It implements event creation, signing, relay connections, subscription filters, and many common NIPs, and is used '
  name: nostr-tools JavaScript Library
  slug: nostr-tools
artifact_total: 10
asyncapis:
- description: AsyncAPI definition of the canonical Nostr relay-client protocol as specified by NIP-01 (basic protocol) and NIP-42 (authentication). Nostr relays expose a single WebSocket endpoint that exchanges JSO
  name: Nostr Relay Protocol
  slug: nostr-asyncapi
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nbd-wtf/nostr-tools/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/nbd-wtf/nostr-tools/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/nbd-wtf/nostr-tools/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nostr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nostr.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nostr-protocol
- group: docs
  title: ''
  type: Specification
  url: https://github.com/nostr-protocol/nips
- group: docs
  title: ''
  type: ProtocolReference
  url: https://github.com/nostr-protocol/nostr
- group: other
  title: ''
  type: AppDirectory
  url: https://nostrapps.com/
- group: other
  title: ''
  type: SoftwareDirectory
  url: https://nostr.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://start.njump.me/
- group: other
  title: ''
  type: NetworkExplorer
  url: https://nostr.band/
- group: other
  title: ''
  type: OriginalEssay
  url: https://fiatjaf.com/nostr.html
- group: agent
  title: ''
  type: LlmsText
  url: https://nostr.com/llms.txt
created: '2026-05-23'
description: Nostr (Notes and Other Stuff Transmitted by Relays) is an open, permissionless protocol for censorship-resistant social and messaging applications. Identity is a public/private keypair; content is a signed JSON event; transport is a WebSocket connection to one or more relays. There is no central server, no canonical API, and no organization that owns the protocol — only a set of community-defined NIPs (Nostr Implementation Possibilities) describing event kinds, relay behavior, and client conventions. A large ecosystem of clients (Damus, Amethyst, Coracle, Yakihonne, Nostur, Iris), relay implementations (strfry, nostream, khatru), and language libraries (nostr-tools for JS, python-nostr, go-nostr, rust-nostr, NDK) has formed around the protocol. Nostr is profiled here through its specifications and reference implementations rather than a vendor API.
finops:
- name: Nostr Finops
  service_category: API
  slug: nostr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nostr.png
layout: provider
modified: '2026-05-29'
name: Nostr
nav: Providers
network: true
overview: 'Nostr publishes 2 APIs on the [APIs.io](https://apis.io/) network: Protocol (NIP-01) and Relay WebSocket Interface. Tagged areas include Nostr, Decentralized Social, Open Protocol, Relays, and WebSocket.


  The Nostr catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nostr''s developer surface includes getting-started guide and 13 more developer resources.'
plans:
- name: Nostr Plans Pricing
  plan_count: 1
  slug: nostr-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 2
  name: Nostr Rate Limits
  slug: nostr-rate-limits
rules:
- name: Nostr API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: nostr-asyncapi-spectral-rules
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.6
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 42.1
  previous_composite: 39.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nostr/refs/heads/main/screenshots/nostr-2026-06-20T190421.png
security:
- kind: domain-security
  name: Nostr Domain Security
  slug: nostr-domain-security
  summary_line: TLSv1.3
slug: nostr
tags:
- Nostr
- Decentralized Social
- Open Protocol
- Relays
- WebSocket
- Signed Events
- NIP
- Censorship Resistant
- Self-Sovereign Identity
website: https://nostr.com/
---
