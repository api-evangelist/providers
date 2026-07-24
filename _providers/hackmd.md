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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-23'
api_count: 8
apis:
- description: Operations related to user's note history.
  name: HackMD History API
  slug: hackmd-history-api
- description: Operations to retrieve user profile information.
  name: HackMD Profile API
  slug: hackmd-profile-api
- description: Operations related to folders within a team.
  name: HackMD Team Folders API
  slug: hackmd-team-folders-api
- description: Operations related to notes within a team.
  name: HackMD Team Notes API
  slug: hackmd-team-notes-api
- description: Operations related to user teams.
  name: HackMD Teams API
  slug: hackmd-teams-api
- description: Operations for listing and restoring trashed notes.
  name: HackMD Trash API
  slug: hackmd-trash-api
- description: Operations related to a user's personal folders.
  name: HackMD User Folders API
  slug: hackmd-user-folders-api
- description: Operations related to a user's personal notes.
  name: HackMD User Notes API
  slug: hackmd-user-notes-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://hackmd.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hackmd.io/@docs/developer-portal
- group: docs
  title: ''
  type: Documentation
  url: https://hackmd.io/@docs/developer-portal
- group: docs
  title: ''
  type: APIReference
  url: https://api.hackmd.io/v1/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://hackmd.io/@docs/how-to-issue-an-api-token
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hackmdio
- group: company
  title: ''
  type: Blog
  url: https://hackmd.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hackmd.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hackmd.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hackmd.io/s/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hackmd.io/s/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hackmd.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hackmd-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hackmd-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hackmd-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/hackmd-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/hackmd-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hackmd-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hackmd-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hackmd-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hackmd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hackmd-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/hackmd-api-catalog.json
- group: design
  title: ''
  type: Conventions
  url: conventions/hackmd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hackmd-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hackmd-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hackmd-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hackmd-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hackmd-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hackmd-domain-security.yml
created: '2026-07-17'
description: HackMD is a real-time collaborative Markdown editor and knowledge base for individuals and teams. Multiple people can co-edit a Markdown document live, organize notes into folders and team workspaces, and publish them as web pages, slide decks or books. HackMD exposes a v1 REST API at api.hackmd.io that lets developers programmatically create, read, update and delete personal and team notes, manage folders and folder ordering, upload image attachments, restore notes from trash, and read the current user profile and view history. The API authenticates with a personal access token sent as an HTTP bearer credential, is described by a published OpenAPI 3.0 specification and Swagger UI, ships an official Node.js/TypeScript client (@hackmd/api) and command-line interface, and advertises its full developer surface through an RFC 9727 api-catalog. HackMD is a Techstars-backed company.
image: https://hackmd.io/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: hackmd-mcp.yml
  slug: hackmd-mcpyml
modified: '2026-07-19'
name: HackMD
nav: Providers
network: true
overview: 'HackMD publishes 8 APIs on the [APIs.io](https://apis.io/) network, including History API, Profile API, Team Folders API, and 5 more. Tagged areas include Company, Markdown, Collaboration, Documentation, and Note Taking.


  HackMD''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 24 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Hackmd Rate Limits
  slug: hackmd-rate-limits
score:
  band: developing
  composite: 50.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 46.0
    developer_ergonomics: 76.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 50.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Hackmd Authentication
  slug: hackmd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hackmd Domain Security
  slug: hackmd-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: hackmd
tags:
- Company
- Markdown
- Collaboration
- Documentation
- Note Taking
- Knowledge Base
- Productivity
- Content
website: https://hackmd.io/
---
