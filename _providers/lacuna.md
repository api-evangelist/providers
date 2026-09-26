---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.2
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Lacuna Agentic Access
  operation_count: 3
  slug: lacuna-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: Hosted Model Context Protocol server (Streamable HTTP) at https://www.lacuna.fm/mcp, protocol 2025-06-18. initialize and tools/list answer anonymously and return real input schemas; tools/call require
  name: Lacuna MCP Server
  slug: lacuna-mcp-server
- description: Agent-to-Agent JSON-RPC endpoint at https://www.lacuna.fm/a2a advertising the "Lacuna Music" agent card at /.well-known/agent-card.json (protocolVersion 0.3.0). One skill, generate_music, which accept
  name: Lacuna A2A Agent
  slug: lacuna-a2a-agent
- baseURL: https://www.lacuna.fm/api
  baseurl_source: declared
  description: The outbound event surface of the Lacuna Music API. Lacuna publishes no AsyncAPI document; it describes its events natively in the OpenAPI 3.1 `webhooks` block — four events (job.completed, job.failed
  name: Lacuna Music API Events
  slug: lacuna-lacuna-music-api-api
- baseURL: https://www.lacuna.fm/api
  baseurl_source: declared
  description: Music generation endpoints.
  name: Lacuna Music API
  slug: lacuna-music-api
- baseURL: https://www.lacuna.fm/mcp
  baseurl_source: declared
  description: Account, plan and credential introspection.
  name: Lacuna Account API
  slug: lacuna-account-api
arazzos:
- description: Submits a music generation task to the Lacuna Music API, polls it to a terminal state, and returns the hosted audio URL of the first rendered track. Both operationIds are verified against the provider
  name: Generate a Lacuna track and collect the audio
  slug: lacuna-generate-and-collect
artifact_total: 18
asyncapis:
- description: ''
  name: Lacuna Webhooks
  slug: lacuna-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lacuna Music Lacuna Music API API
  slug: open-lacuna-lacuna-music-api-api
- collection_type: open
  name: Lacuna Music API
  slug: open-lacuna-music-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/skills/lacuna-preflight-and-budget.md
  title: ''
  type: AgentSkill
  url: skills/lacuna-preflight-and-budget.md
- group: company
  title: ''
  type: Website
  url: https://www.lacuna.fm/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/agentic-access/lacuna-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lacuna-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lacuna.fm/docs
- group: start
  title: ''
  type: Portal
  url: https://www.lacuna.fm/ai-music-api
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
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/changelog/lacuna-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lacuna-changelog.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/openapi/_original/lacuna-music-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/lacuna-music-openapi-original.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/llms/lacuna-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lacuna-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/well-known/lacuna-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lacuna-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/well-known/lacuna-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lacuna-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/well-known/lacuna-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/lacuna-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/mcp/lacuna-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lacuna-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/mcp/lacuna-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lacuna-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/a2a/lacuna-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/lacuna-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/packages/lacuna-packages.yml
  title: ''
  type: Packages
  url: packages/lacuna-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/packages/lacuna-packages.yml
  title: ''
  type: SDKs
  url: packages/lacuna-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/cli/lacuna-cli.yml
  title: ''
  type: CLI
  url: cli/lacuna-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/authentication/lacuna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lacuna-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/scopes/lacuna-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lacuna-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/conventions/lacuna-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lacuna-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/errors/lacuna-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lacuna-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/asyncapi/lacuna-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lacuna-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/lifecycle/lacuna-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lacuna-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/conformance/lacuna-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lacuna-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/security/lacuna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lacuna-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/security/lacuna-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lacuna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lacuna.fm/.well-known/security.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/rate-limits/lacuna-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lacuna-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/plans/lacuna-plans.yml
  title: ''
  type: Plans
  url: plans/lacuna-plans.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/data-model/lacuna-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lacuna-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/overlays/lacuna-music-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lacuna-music-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/arazzo/lacuna-generate-and-collect.yml
  title: ''
  type: Arazzo
  url: arazzo/lacuna-generate-and-collect.yml
created: '2026-08-02'
description: 'Lacuna (lacuna.fm), operated by JOYLINK LTD, is an AI music creation platform that turns lyrics or a plain-text style description into complete songs with vocals, alongside lyrics writing, word-level timed lyrics (LRC/SRT/VTT), lyric video export, AI mastering, mashups, stem separation, album-cover art, MIDI tooling and sheet-music conversion, plus long-form AI radio for focus, sleep and ambience. Developers get a documented REST music-generation API (OpenAPI 3.1 published at /api/openapi.json), an official TypeScript SDK, a `lacuna` CLI, and an unusually complete agent surface: a hosted Streamable-HTTP MCP server at /mcp with an anonymous tools/list, an A2A JSON-RPC agent endpoint at /a2a with a published agent card, an RFC 9727 api-catalog, RFC 8414 / RFC 9728 / RFC 7009 OAuth discovery and revocation, an agent-oriented auth.md, an llms.txt, and packaged Agent Skills. The REST contract carries three operations: submit a generation, poll it, and — added since August — a free
  GET /v1/me that returns the calling credential''s plan, credit balance, scopes, key expiry and effective rate limits, which is the only precondition check available on an API that offers no idempotency key, no dry run and no way to cancel or refund a generation once submitted. API access requires a Pro plan or above and is billed in credits per generation.'
image: https://www.lacuna.fm/favicon-192x192.png
layout: provider
mcp_servers:
- description: Generate AI music from a style description and optional lyrics. Submit a task, poll it, collect the rendered audio.
  name: Lacuna MCP Server
  slug: lacuna-mcp-server
modified: '2026-09-11'
name: Lacuna
nav: Providers
network: true
overview: 'Lacuna publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Music API Events, Music API, Account API, and 2 more. Tagged areas include AI Music, Music Generation, AI Song Generator, AI Lyrics Generator, and Audio.


  The Lacuna catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lacuna''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Lacuna Plans
  plan_count: 4
  slug: lacuna-plans
random_paper: 12
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
  composite: 64.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 53.8
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 63.2
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/lacuna/refs/heads/main/screenshots/lacuna-2026-08-17T081024.png
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
  summary_line: Hackerone · contact published
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
- Agent Skills
- A2A
- Developer Tools
- Account
- Authentication
website: https://www.lacuna.fm/
---
