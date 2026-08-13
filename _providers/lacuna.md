---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Lacuna Agentic Access
  operation_count: 2
  slug: lacuna-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 4
apis:
- description: Hosted Model Context Protocol server (Streamable HTTP) at https://www.lacuna.fm/mcp, protocol 2025-06-18. initialize and tools/list answer anonymously and return real input schemas; tools/call require
  name: Lacuna MCP Server
  slug: lacuna-mcp-server
- description: Agent-to-Agent JSON-RPC endpoint at https://www.lacuna.fm/a2a advertising the "Lacuna Music" agent card at /.well-known/agent-card.json (protocolVersion 0.3.0). One skill, generate_music, which accept
  name: Lacuna A2A Agent
  slug: lacuna-a2a-agent
- description: The Lacuna Music API API from Lacuna — 0 operation(s) for lacuna music api.
  name: Lacuna Lacuna Music API API
  slug: lacuna-lacuna-music-api-api
- description: Music generation endpoints.
  name: Lacuna Music API
  slug: lacuna-music-api
arazzos:
- description: Submits a music generation task to the Lacuna Music API, polls it to a terminal state, and returns the hosted audio URL of the first rendered track. Both operationIds are verified against the provider
  name: Generate a Lacuna track and collect the audio
  slug: lacuna-generate-and-collect
artifact_total: 14
asyncapis:
- description: ''
  name: Lacuna Webhooks
  slug: lacuna-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lacuna-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lacuna.fm/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.lacuna.fm/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.lacuna.fm/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lacuna.fm/docs
- group: operate
  title: ''
  type: Support
  url: https://www.lacuna.fm/contact
- group: company
  title: ''
  type: Blog
  url: https://www.lacuna.fm/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JOYLINK-LTD
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lacuna.fm/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.lacuna.fm/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lacuna.fm/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lacuna.fm/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.lacuna.fm/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lacuna-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/lacuna-music-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lacuna-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lacuna-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lacuna-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/lacuna-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lacuna-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lacuna-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/lacuna-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/lacuna-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lacuna-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lacuna-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lacuna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lacuna-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lacuna-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lacuna-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lacuna-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lacuna-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lacuna-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lacuna-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lacuna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lacuna.fm/.well-known/security.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lacuna-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lacuna-plans.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lacuna-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lacuna-music-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lacuna-generate-and-collect.yml
created: '2026-08-02'
description: 'Lacuna (lacuna.fm), operated by JOYLINK LTD, is an AI music creation platform that turns lyrics or a plain-text style description into complete songs with vocals, alongside lyrics writing, word-level timed lyrics (LRC/SRT/VTT), lyric video export, AI mastering, mashups, stem separation, album-cover art, MIDI tooling and sheet-music conversion, plus long-form AI radio for focus, sleep and ambience. Developers get a documented REST music-generation API (OpenAPI 3.1 published at /api/openapi.json), an official TypeScript SDK, a `lacuna` CLI, and an unusually complete agent surface: a hosted Streamable-HTTP MCP server at /mcp with an anonymous tools/list, an A2A JSON-RPC agent endpoint at /a2a with a published agent card, an RFC 9727 api-catalog, RFC 8414 / RFC 9728 OAuth discovery, an agent-oriented auth.md, an llms.txt, and a packaged Agent Skill. API access requires a Pro plan or above and is billed in credits per generation.'
image: https://www.lacuna.fm/favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: lacuna-mcp.yml
  slug: lacuna-mcpyml
modified: '2026-08-09'
name: Lacuna
nav: Providers
network: true
overview: 'Lacuna publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lacuna Music API API and Music API. Tagged areas include AI Music, Music Generation, AI Song Generator, AI Lyrics Generator, and Audio.


  The Lacuna catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lacuna''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Lacuna Plans
  plan_count: 4
  slug: lacuna-plans
random_paper: 28
rate_limits:
- limit_count: 3
  name: Lacuna Rate Limits
  slug: lacuna-rate-limits
scopes:
- name: Lacuna Scopes
  scope_count: 5
  slug: lacuna-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 65.5
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 57.1
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 71.1
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Lacuna Authentication
  slug: lacuna-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lacuna Domain Security
  slug: lacuna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lacuna Vulnerability Disclosure
  slug: lacuna-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lacuna
tags:
- AI Music
- Music Generation
- AI Song Generator
- AI Lyrics Generator
- Audio
- MIDI
- Songwriting
- Generative AI
- MCP Server
- Agent Skill
- A2A
- Developer Tools
website: https://www.lacuna.fm/docs
---
