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
    agent_skills: derived
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to user's note history.
  name: HackMD History API
  slug: hackmd-history-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations to retrieve user profile information.
  name: HackMD Profile API
  slug: hackmd-profile-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to folders within a team.
  name: HackMD Team Folders API
  slug: hackmd-team-folders-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to notes within a team.
  name: HackMD Team Notes API
  slug: hackmd-team-notes-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to user teams.
  name: HackMD Teams API
  slug: hackmd-teams-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations for listing and restoring trashed notes.
  name: HackMD Trash API
  slug: hackmd-trash-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to a user's personal folders.
  name: HackMD User Folders API
  slug: hackmd-user-folders-api
- baseURL: https://api.hackmd.io/v1
  baseurl_source: declared
  description: Operations related to a user's personal notes.
  name: HackMD User Notes API
  slug: hackmd-user-notes-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HackMD Open History API
  slug: open-hackmd-history-api
- collection_type: open
  name: HackMD Open History Profile API
  slug: open-hackmd-profile-api
- collection_type: open
  name: HackMD Open History Team Folders API
  slug: open-hackmd-team-folders-api
- collection_type: open
  name: HackMD Open History Team Notes API
  slug: open-hackmd-team-notes-api
- collection_type: open
  name: HackMD Open History Teams API
  slug: open-hackmd-teams-api
- collection_type: open
  name: HackMD Open History Trash API
  slug: open-hackmd-trash-api
- collection_type: open
  name: HackMD Open History User Folders API
  slug: open-hackmd-user-folders-api
- collection_type: open
  name: HackMD Open History User Notes API
  slug: open-hackmd-user-notes-api
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
  url: openapi/_original/hackmd-openapi-original.json
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
  name: HackMD MCP Server
  slug: hackmd-mcp-server
modified: '2026-07-19'
name: HackMD
nav: Providers
network: true
overview: 'HackMD publishes 8 APIs on the [APIs.io](https://apis.io/) network, including History API, Profile API, Team Folders API, and 5 more. Tagged areas include Company, Markdown, Collaboration, Documentation, and Note Taking.


  HackMD''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 24 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 2
  name: Hackmd Rate Limits
  slug: hackmd-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 49.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hackmd/refs/heads/main/screenshots/hackmd-2026-07-25T220526.png
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
