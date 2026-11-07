---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Frameio Agentic Access
  operation_count: 90
  slug: frameio-agentic-access
  summary_line: 90 operations · 52 acting
api_count: 1
apis:
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Accounts and related operations.
  name: Frame.io Accounts API
  slug: frameio-accounts-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Collections and related operations.
  name: Frame.io Collections API
  slug: frameio-collections-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Comments and related operations.
  name: Frame.io Comments API
  slug: frameio-comments-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Custom Actions and related operations.
  name: Frame.io Custom Actions API
  slug: frameio-custom-actions-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Files and related operations.
  name: Frame.io Files API
  slug: frameio-files-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Folder Permissions and related operations.
  name: Frame.io Folder Permissions API
  slug: frameio-folder-permissions-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Folders and related operations.
  name: Frame.io Folders API
  slug: frameio-folders-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Groups and related operations.
  name: Frame.io Groups API
  slug: frameio-groups-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Metadata and related operations.
  name: Frame.io Metadata API
  slug: frameio-metadata-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Metadata Fields and related operations.
  name: Frame.io Metadata Fields API
  slug: frameio-metadata-fields-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Project Permissions and related operations.
  name: Frame.io Project Permissions API
  slug: frameio-project-permissions-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Projects and related operations.
  name: Frame.io Projects API
  slug: frameio-projects-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Search and related operations.
  name: Frame.io Search API
  slug: frameio-search-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Shares and related operations.
  name: Frame.io Shares API
  slug: frameio-shares-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Users and related operations.
  name: Frame.io Users API
  slug: frameio-users-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Version Stacks and related operations.
  name: Frame.io Version Stacks API
  slug: frameio-version-stacks-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Webhooks and related operations.
  name: Frame.io Webhooks API
  slug: frameio-webhooks-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Workspace Permissions and related operations.
  name: Frame.io Workspace Permissions API
  slug: frameio-workspace-permissions-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Workspaces and related operations.
  name: Frame.io Workspaces API
  slug: frameio-workspaces-api
- baseURL: https://api.frame.io
  baseurl_source: declared
  description: Manage Account Permissions and related operations.
  name: Frame.io Accountpermissions API
  slug: frameio-accountpermissions-api
artifact_total: 55
asyncapis:
- description: ''
  name: Frameio Webhooks
  slug: frameio-webhooks
collections:
- collection_type: open
  name: Frame.io Account Permissions API
  slug: open-frameio-account-permissions-api
- collection_type: open
  name: Frame.io Account Permissions Accounts API
  slug: open-frameio-accounts-api
- collection_type: open
  name: Frame.io Account Permissions Collections API
  slug: open-frameio-collections-api
- collection_type: open
  name: Frame.io Account Permissions Comments API
  slug: open-frameio-comments-api
- collection_type: open
  name: Frame.io Account Permissions Custom Actions API
  slug: open-frameio-custom-actions-api
- collection_type: open
  name: Frame.io Account Permissions Files API
  slug: open-frameio-files-api
- collection_type: open
  name: Frame.io Account Permissions Folder Permissions API
  slug: open-frameio-folder-permissions-api
- collection_type: open
  name: Frame.io Account Permissions Folders API
  slug: open-frameio-folders-api
- collection_type: open
  name: Frame.io Account Permissions Groups API
  slug: open-frameio-groups-api
- collection_type: open
  name: Frame.io Account Permissions Metadata API
  slug: open-frameio-metadata-api
- collection_type: open
  name: Frame.io Account Permissions Metadata Fields API
  slug: open-frameio-metadata-fields-api
- collection_type: open
  name: Frame.io Account Permissions Project Permissions API
  slug: open-frameio-project-permissions-api
- collection_type: open
  name: Frame.io Account Permissions Projects API
  slug: open-frameio-projects-api
- collection_type: open
  name: Frame.io Account Permissions Search API
  slug: open-frameio-search-api
- collection_type: open
  name: Frame.io Account Permissions Shares API
  slug: open-frameio-shares-api
- collection_type: open
  name: Frame.io Account Permissions Users API
  slug: open-frameio-users-api
- collection_type: open
  name: Frame.io Account Permissions Version Stacks API
  slug: open-frameio-version-stacks-api
- collection_type: open
  name: Frame.io Account Permissions Webhooks API
  slug: open-frameio-webhooks-api
- collection_type: open
  name: Frame.io Account Permissions Workspace Permissions API
  slug: open-frameio-workspace-permissions-api
- collection_type: open
  name: Frame.io Account Permissions Workspaces API
  slug: open-frameio-workspaces-api
common:
- group: operate
  href: https://artifacts.apis.io/frameio/rate-limits/frameio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/frameio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/frameio/plans/frameio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/frameio-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/frameio/capabilities/frameio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/frameio-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/frameio/overlays/frameio-v4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/frameio-v4-overlay.yaml
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
  href: https://artifacts.apis.io/frameio/lifecycle/frameio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/frameio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/frameio/lifecycle/frameio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/frameio-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/frameio/changelog/frameio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/frameio-changelog.yml
- group: auth
  href: https://artifacts.apis.io/frameio/authentication/frameio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/frameio-authentication.yml
- group: auth
  href: https://artifacts.apis.io/frameio/scopes/frameio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/frameio-scopes.yml
- group: design
  href: https://artifacts.apis.io/frameio/conventions/frameio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/frameio-conventions.yml
- group: design
  href: https://artifacts.apis.io/frameio/conformance/frameio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/frameio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://frame.io/security
- group: auth
  href: https://artifacts.apis.io/frameio/security/frameio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/frameio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/frameio/security/frameio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frameio-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/frameio/agentic-access/frameio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/frameio-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/frameio/packages/frameio-packages.yml
  title: ''
  type: Packages
  url: packages/frameio-packages.yml
- group: build
  href: https://artifacts.apis.io/frameio/packages/frameio-packages.yml
  title: ''
  type: SDKs
  url: packages/frameio-packages.yml
- group: build
  href: https://artifacts.apis.io/frameio/cli/frameio-cli.yml
  title: ''
  type: CLI
  url: cli/frameio-cli.yml
- group: agent
  href: https://artifacts.apis.io/frameio/mcp/frameio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/frameio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/frameio/llms/frameio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/frameio-llms.txt
- group: agent
  href: https://artifacts.apis.io/frameio/well-known/frameio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/frameio-well-known.yml
- group: agent
  href: https://artifacts.apis.io/frameio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: http://www.frame.io
created: '2026-07-17'
description: Frame.io is a cloud-based video review and collaboration platform, now part of Adobe, used by video and media production teams to upload media, leave frame-accurate comments, manage versions, and route work through review and approval. Its V4 developer platform exposes a REST API (base https://api.frame.io/v4) covering accounts, workspaces, projects, folders, files and uploads, comments, version stacks, shares and reviewers, collections, groups, custom actions, metadata fields, and webhooks. Authentication is OAuth2 via Adobe IMS (authorization-code for user apps and client-credentials for server-to-server), plus a Camera to Cloud (C2C) device-integration surface, an official Python SDK, the fioctl CLI, and a hosted MCP server.
finops:
- has_sources: true
  method: derived
  name: Frameio Finops
  primary_unit: member + tax
  service_category: ''
  slug: frameio-finops
  template: false
image: https://github.com/Frameio.png
layout: provider
mcp_servers:
- description: Official Frame.io documentation/platform MCP server, advertised in the provider's llms.txt for AI client integration (Claude Code, Cursor, etc.). Responds 200 to GET at the endpoint above.
  name: Frame.io MCP Server
  slug: frameio
modified: '2026-07-19'
name: Frame.io
nav: Providers
network: true
overview: 'Frame.io publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Collections API, Comments API, and 17 more. Tagged areas include Company, Media, Video, Collaboration, and Review and Approval.


  The Frame.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Frame.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Frameio Plans Pricing
  plan_count: 4
  slug: frameio-plans-pricing
- name: Frameio Price Estimates
  plan_count: 0
  slug: frameio-price-estimates
random_paper: 19
rate_limits:
- limit_count: 5
  name: Frameio Rate Limits
  slug: frameio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 121
  extends:
  - spectral:oas
  name: Frame.io API Rules
  rule_count: 80
  severity_counts:
    error: 70
    hint: 0
    info: 1
    warn: 9
  slug: frameio-rules
scopes:
- name: Frameio Scopes
  scope_count: 6
  slug: frameio-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 60.6
    developer_ergonomics: 69.6
    discoverability: 75.0
    operational_transparency: 81.6
  previous_composite: 65.9
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/frameio/frameio-2026-07-25T215109.png
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
skill_count: 3
skills:
- name: Share assets with external reviewers
  slug: frameio-share-for-review
- name: Upload media and collect review comments
  slug: frameio-upload-and-review
- name: Automate workflows with webhooks
  slug: frameio-webhook-automation
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
