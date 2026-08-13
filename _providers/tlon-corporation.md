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
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.9
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Urbit ship HTTP API (Eyre channels) that powers Tlon Messenger. Clients authenticate to a ship with its +code access code, then poke and subscribe over a channel to send/read messages, manage grou
  name: Urbit HTTP API (Tlon)
  slug: urbit-http-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tlon-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tlon.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.urbit.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urbit.org
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/tloncorp/api-beta
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.urbit.org/get-on-urbit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tloncorp
- group: company
  title: ''
  type: Blog
  url: https://tlon.io/posts
- group: operate
  title: ''
  type: ChangeLog
  url: https://tlon.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tlon-corporation-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://tlon.io/posts/faq
- group: start
  title: ''
  type: SignUp
  url: https://tlon.network/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tlon.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tlon.io/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tloncorporation
- group: build
  title: ''
  type: Packages
  url: packages/tlon-corporation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tlon-corporation-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tlon-corporation-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tlon-corporation-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/tlon-corporation-conventions.yml
created: '2026-07-17'
description: Tlon Corporation builds Tlon Messenger, a self-owned, self-hosted social messaging app that runs on the user's own Urbit ship, and Tlon Hosting, which runs managed ships under tlon.network. Every account ships with Tlonbot, an OpenClaw-powered AI agent. Developers integrate through the Urbit ship HTTP API (Eyre channels) using the @tloncorp/api and @urbit/http-api TypeScript clients, and through the first-party Tlon MCP Server that exposes messaging, groups, channels, and profile tools to agents. Backed by a16z.
image: https://tlon.io/apple-touch-icon.png
layout: provider
mcp_servers:
- description: First-party open-source MCP server (tloncorp/tlon-mcp-server) exposing ~30 tools for Tlon Messenger over a running Urbit ship; stdio or http transport.
  name: Tlon MCP Server
  slug: tlon-mcp-server
modified: '2026-07-21'
name: Tlon Corporation
nav: Providers
network: true
overview: 'Tlon Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, Social, Urbit, and Self-Hosting.


  Tlon Corporation''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, support, signup flow, and 14 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 58.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.8
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Tlon Corporation Domain Security
  slug: tlon-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tlon-corporation
tags:
- Company
- Messaging
- Social
- Urbit
- Self-Hosting
- Decentralization
- Agents
- MCP
- Chat
- Hosting
website: https://tlon.io
---
