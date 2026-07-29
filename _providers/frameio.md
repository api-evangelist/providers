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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Frameio Agentic Access
  operation_count: 90
  slug: frameio-agentic-access
  summary_line: 90 operations · 53 acting
api_count: 20
apis:
- description: Manage Account Permissions and related operations.
  name: Frame.io Account Permissions API
  slug: frameio-account-permissions-api
- description: Manage Accounts and related operations.
  name: Frame.io Accounts API
  slug: frameio-accounts-api
- description: Manage Collections and related operations.
  name: Frame.io Collections API
  slug: frameio-collections-api
- description: Manage Comments and related operations.
  name: Frame.io Comments API
  slug: frameio-comments-api
- description: Manage Custom Actions and related operations.
  name: Frame.io Custom Actions API
  slug: frameio-custom-actions-api
- description: Manage Files and related operations.
  name: Frame.io Files API
  slug: frameio-files-api
- description: Manage Folder Permissions and related operations.
  name: Frame.io Folder Permissions API
  slug: frameio-folder-permissions-api
- description: Manage Folders and related operations.
  name: Frame.io Folders API
  slug: frameio-folders-api
- description: Manage Groups and related operations.
  name: Frame.io Groups API
  slug: frameio-groups-api
- description: Manage Metadata and related operations.
  name: Frame.io Metadata API
  slug: frameio-metadata-api
- description: Manage Metadata Fields and related operations.
  name: Frame.io Metadata Fields API
  slug: frameio-metadata-fields-api
- description: Manage Project Permissions and related operations.
  name: Frame.io Project Permissions API
  slug: frameio-project-permissions-api
- description: Manage Projects and related operations.
  name: Frame.io Projects API
  slug: frameio-projects-api
- description: Manage Search and related operations.
  name: Frame.io Search API
  slug: frameio-search-api
- description: Manage Shares and related operations.
  name: Frame.io Shares API
  slug: frameio-shares-api
- description: Manage Users and related operations.
  name: Frame.io Users API
  slug: frameio-users-api
- description: Manage Version Stacks and related operations.
  name: Frame.io Version Stacks API
  slug: frameio-version-stacks-api
- description: Manage Webhooks and related operations.
  name: Frame.io Webhooks API
  slug: frameio-webhooks-api
- description: Manage Workspace Permissions and related operations.
  name: Frame.io Workspace Permissions API
  slug: frameio-workspace-permissions-api
- description: Manage Workspaces and related operations.
  name: Frame.io Workspaces API
  slug: frameio-workspaces-api
artifact_total: 27
asyncapis:
- description: ''
  name: Frameio Webhooks
  slug: frameio-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.frame.io
- group: docs
  title: ''
  type: Documentation
  url: https://next.developer.frame.io/platform/v4/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://next.developer.frame.io/platform/v4/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://next.developer.frame.io/platform/v4/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.frame.io
- group: company
  title: ''
  type: Blog
  url: https://blog.frame.io
- group: commercial
  title: ''
  type: Pricing
  url: https://frame.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.frame.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Frameio
- group: operate
  title: ''
  type: StatusPage
  url: https://status.frame.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/frameio-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/frameio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/frameio-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/frameio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/frameio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/frameio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/frameio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://frame.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/frameio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frameio-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frameio-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/frameio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/frameio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/frameio-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/frameio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/frameio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/frameio-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: http://www.frame.io
created: '2026-07-17'
description: Frame.io is a cloud-based video review and collaboration platform, now part of Adobe, used by video and media production teams to upload media, leave frame-accurate comments, manage versions, and route work through review and approval. Its V4 developer platform exposes a REST API (base https://api.frame.io/v4) covering accounts, workspaces, projects, folders, files and uploads, comments, version stacks, shares and reviewers, collections, groups, custom actions, metadata fields, and webhooks. Authentication is OAuth2 via Adobe IMS (authorization-code for user apps and client-credentials for server-to-server), plus a Camera to Cloud (C2C) device-integration surface, an official Python SDK, the fioctl CLI, and a hosted MCP server.
image: https://github.com/Frameio.png
layout: provider
mcp_servers:
- description: ''
  name: frameio-mcp.yml
  slug: frameio-mcpyml
modified: '2026-07-19'
name: Frame.io
nav: Providers
network: true
overview: 'Frame.io publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Account Permissions API, Accounts API, Collections API, and 17 more. Tagged areas include Company, Media, Video, Collaboration, and Review and Approval.


  The Frame.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Frame.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 10
scopes:
- name: Frameio Scopes
  scope_count: 6
  slug: frameio-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.3
  delta: 1.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.9
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frameio/refs/heads/main/screenshots/frameio-2026-07-25T215109.png
security:
- kind: authentication
  name: Frameio Authentication
  slug: frameio-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Frameio Domain Security
  slug: frameio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Frameio Trust Center
  slug: frameio-trust-center
  summary_line: SOC 2, ISO 27001
slug: frameio
tags:
- Company
- Media
- Video
- Collaboration
- Review and Approval
- Media Production
- Adobe
- Content
website: http://www.frame.io
---
