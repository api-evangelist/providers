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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Library API for defining server-side logic for a "party" - a backend object backed by a Cloudflare Durable Object. Provides lifecycle hooks for connections, messages, requests, alarms, and state persi
  name: PartyKit Party.Server (Server API)
  slug: party-server
- description: Browser and runtime client library for connecting to a PartyKit server over WebSockets. Wraps the standard WebSocket API with reconnection, buffering, and resilience. Runs in Web, ServiceWorker, Node.
  name: PartyKit PartySocket (Client API)
  slug: partysocket
- description: Yjs provider for PartyKit that turns a party into a Yjs collaboration backend, enabling shared text, rich text, and structured CRDT documents across many clients.
  name: Y-PartyKit (Yjs Integration)
  slug: y-partykit
- description: Public HTTP and WebSocket interface for a deployed PartyKit project at project.user.partykit.dev. Each party is reachable at /parties/{party}/{room} and accepts WebSocket upgrades or HTTP requests.
  name: PartyKit Deployed Party (HTTP / WebSocket)
  slug: deployed-party-http
artifact_total: 10
asyncapis:
- description: AsyncAPI description of the PartyKit realtime protocol. PartyKit is a realtime backend framework (acquired by Cloudflare) that wraps Cloudflare Durable Objects with an opinionated developer experience
  name: PartyKit Realtime Protocol
  slug: partykit-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/partykit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.partykit.io
- group: start
  title: ''
  type: Portal
  url: https://docs.partykit.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partykit.io
- group: company
  title: ''
  type: Blog
  url: https://blog.partykit.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudflare/partykit
- group: build
  title: ''
  type: CLI
  url: https://docs.partykit.io/reference/partykit-cli/
- group: build
  title: ''
  type: Examples
  url: https://docs.partykit.io/examples/
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.partykit.io/guides/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudflare.com/website-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudflare.com/privacypolicy/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/g5uqHQJc3z
created: '2026-05-23'
description: PartyKit is a real-time backend framework, now part of Cloudflare, that wraps Cloudflare Durable Objects with an opinionated developer experience for building multiplayer applications. It exposes a Party.Server library API for backend logic, a PartySocket client API for WebSockets, a Y-PartyKit Yjs integration, an HTTP/WebSocket interface at *.partykit.dev URLs, a CLI for local dev and deployment, and integrations with React, Next.js, and Remix.
finops:
- name: Partykit Finops
  service_category: API
  slug: partykit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/partykit.png
layout: provider
modified: '2026-05-29'
name: PartyKit
nav: Providers
network: true
overview: 'PartyKit publishes 1 API on the [APIs.io](https://apis.io/) network: Deployed Party (HTTP / WebSocket). Tagged areas include Real-Time, Multiplayer, WebSockets, Cloudflare, and Durable Objects.


  The PartyKit catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PartyKit''s developer surface includes developer portal, documentation, engineering blog, GitHub presence, CLI, code examples, and 6 more developer resources.'
plans:
- name: Partykit Plans Pricing
  plan_count: 1
  slug: partykit-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Partykit Rate Limits
  slug: partykit-rate-limits
rules:
- name: PartyKit API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 4
  slug: partykit-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: 3.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 26.3
  previous_composite: 43.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/partykit/refs/heads/main/screenshots/partykit-2026-06-20T191429.png
security:
- kind: domain-security
  name: Partykit Domain Security
  slug: partykit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: partykit
tags:
- Real-Time
- Multiplayer
- WebSockets
- Cloudflare
- Durable Objects
- Edge
- CRDT
- Yjs
- Serverless
website: https://www.partykit.io
---
