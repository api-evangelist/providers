---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The private product API behind the Linzumi web workspace and the local Commander runner, served from serve.linzumi.com under a /api/v2 URI-versioned path. It is not a published developer API — there i
  name: Linzumi Runner API
  slug: runner-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://linzumi.com/
- group: start
  title: ''
  type: Login
  url: https://serve.linzumi.com/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@linzumi.com
- group: other
  title: ''
  type: Download
  url: https://downloads.linzumi.com/macos-beta/linzumi_macos_latest.dmg
- group: other
  title: ''
  type: Profile
  url: https://www.ycombinator.com/companies/linzumi
- group: build
  title: ''
  type: Packages
  url: packages/linzumi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/linzumi-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linzumi-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linzumi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linzumi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linzumi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linzumi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linzumi-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linzumi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linzumi-llms.txt
created: '2026-07-17'
description: Linzumi is a Y Combinator (Spring 2026) company in San Francisco building a Slack-shaped team chat that runs a fleet of AI coding agents inside every channel. Engineering teams kick off work, watch agent activity in real time, review output, and ship code without leaving the thread. Unlike sandboxed cloud agent products, Linzumi runs agents on the developer's own machine through a local "Commander" runner installed from the @linzumi/cli npm package, so agents work against real environment variables, dotfiles, and branches inside explicitly trusted folders. The product adds a decision inbox that surfaces only the choices needing a human, continuously compiled team context, git safety snapshots taken before each agent turn, and a bundled local MCP server that lets coding agents read scoped Linzumi message, thread, and channel context. It supports OpenAI Codex today with Claude Code announced as coming soon. The service is in beta via a macOS desktop app and a web workspace; there
  is no public developer API program, documentation portal, or published OpenAPI at this time.
image: https://storage.googleapis.com/ployai/d195dfe3-6a0f-4051-8d67-1a4376685f60/user/3e1aeaf5-og-home-en.jpg
layout: provider
mcp_servers:
- description: ''
  name: Linzumi MCP Server
  slug: linzumi-mcp-server
modified: '2026-07-19'
name: Linzumi
nav: Providers
network: true
overview: 'Linzumi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Developer Tools, Coding Agents, and Team Chat.


  Linzumi''s developer surface includes support, CLI, authentication, changelog, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 15.7
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linzumi/refs/heads/main/screenshots/linzumi-2026-07-25T225305.png
security:
- kind: authentication
  name: Linzumi Authentication
  slug: linzumi-authentication
  summary_line: oauth2-device-code/oauth2-authorization-code · 3 schemes
- kind: domain-security
  name: Linzumi Domain Security
  slug: linzumi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: linzumi
tags:
- Company
- Artificial Intelligence
- Developer Tools
- Coding Agents
- Team Chat
- Collaboration
- MCP
- Command Line Interface
- Y Combinator
website: https://linzumi.com/
---
