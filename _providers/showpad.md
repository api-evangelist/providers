---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Access analytics and insights for coaching and training programs, including learning paths, skill assessments, roleplay AI analysis, and coach analytics data.
  name: Showpad Coach API
  slug: showpad-coach-api
- description: Create and manage webhook subscriptions and read their delivery logs. Notifications carry a CloudEvents-shaped envelope and are signed with HMAC-SHA256 over the raw body plus a timestamp, with a five-
  name: Showpad Webhooks API
  slug: showpad-webhooks-api
- description: Hosted remote Model Context Protocol server that lets AI assistants such as Claude and Cursor search Showpad assets, fetch their content, run ShowQL filters, ask questions with cited sources, and read
  name: Showpad MCP Server
  slug: showpad-mcp-server
- description: The assets API from Showpad — 16 operation(s) for assets.
  name: Showpad Assets API
  slug: showpad-assets-api
- description: The channels API from Showpad — 22 operation(s) for channels.
  name: Showpad Channels API
  slug: showpad-channels-api
- description: The comments API from Showpad — 4 operation(s) for comments.
  name: Showpad Comments API
  slug: showpad-comments-api
- description: These are endpoints for managing crm recommendation rules and fetching shares and shared spaces cmr records
  name: Showpad CRM API
  slug: showpad-crm-api
- description: The divisionpermissions API from Showpad — 6 operation(s) for divisionpermissions.
  name: Showpad Divisionpermissions API
  slug: showpad-divisionpermissions-api
- description: The divisions API from Showpad — 17 operation(s) for divisions.
  name: Showpad Divisions API
  slug: showpad-divisions-api
- description: The exports API from Showpad — 25 operation(s) for exports.
  name: Showpad Exports API
  slug: showpad-exports-api
- description: The generic API from Showpad — 1 operation(s) for generic.
  name: Showpad Generic API
  slug: showpad-generic-api
- description: These are endpoints for fetching available Languages and Countries information.
  name: Showpad Locale API
  slug: showpad-locale-api
- description: These are endpoints for managing Mutual Action Plans
  name: Showpad Mutual Action Plan API
  slug: showpad-mutual-action-plan-api
- description: The recommendations API from Showpad — 6 operation(s) for recommendations.
  name: Showpad Recommendations API
  slug: showpad-recommendations-api
- description: These are endpoints for managing Shared Space Templates
  name: Showpad Shared Space Templates API
  slug: showpad-shared-space-templates-api
- description: These are endpoints for managing Shared Spaces
  name: Showpad Shared Spaces API
  slug: showpad-shared-spaces-api
- description: These are endpoints for managing Shared Spaces Quick Actions
  name: Showpad Shared Spaces Quick Actions API
  slug: showpad-shared-spaces-quick-actions-api
- description: These are endpoints for managing Shares
  name: Showpad Shares API
  slug: showpad-shares-api
- description: These are endpoints for managing Tag Categories.
  name: Showpad Tag Categories API
  slug: showpad-tag-categories-api
- description: The tags API from Showpad — 12 operation(s) for tags.
  name: Showpad Tags API
  slug: showpad-tags-api
- description: These are endpoints for managing Themes
  name: Showpad Themes API
  slug: showpad-themes-api
- description: The tickets API from Showpad — 9 operation(s) for tickets.
  name: Showpad Tickets API
  slug: showpad-tickets-api
- description: The usergroups API from Showpad — 14 operation(s) for usergroups.
  name: Showpad Usergroups API
  slug: showpad-usergroups-api
- description: The userpermissions API from Showpad — 6 operation(s) for userpermissions.
  name: Showpad Userpermissions API
  slug: showpad-userpermissions-api
- description: The users API from Showpad — 22 operation(s) for users.
  name: Showpad Users API
  slug: showpad-users-api
artifact_total: 35
asyncapis:
- description: ''
  name: Showpad Webhooks
  slug: showpad-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/showpad-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/showpad-v3-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/showpad-v4-overlay.yaml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/showpad-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/showpad-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/showpad-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/showpad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.showpad.com/responsible-disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: security/showpad-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bigtincan.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/showpad-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/showpad-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/showpad-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/showpad-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/showpad-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/showpad-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/showpad-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/showpad-cli.yml
- group: design
  title: ''
  type: Components
  url: components/showpad-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/showpad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/showpad-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/showpad-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/showpad-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.showpad.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/showpad-sandbox.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.showpad.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.showpad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.showpad.com/docs/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.showpad.com/docs/apis/references
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.showpad.com/docs/apis/concepts/fundamentals
- group: other
  title: ''
  type: Fundamentals
  url: https://developer.showpad.com/docs/apis/concepts/fundamentals
- group: design
  title: ''
  type: Versioning
  url: https://developer.showpad.com/docs/apis/concepts/versions
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/showpad-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/showpad-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.showpad.com/news
- group: operate
  title: ''
  type: Status
  url: https://status.showpad.com
- group: company
  title: ''
  type: Blog
  url: https://www.showpad.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.showpad.com/hc/en-us/requests/new
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.showpad.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/showpad
- group: commercial
  title: ''
  type: Pricing
  url: https://www.showpad.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.showpad.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.showpad.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.showpad.com/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/showpad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/showpad-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/showpad-finops.yml
created: '2026-06-13'
description: Showpad is a sales enablement and coaching platform offering a REST API for managing sales content, training programs, meeting analytics, and buyer engagement. The API supports content management with ShowQL query language, buyer engagement through shares and digital sales rooms, seller effectiveness via CRM recommendation rules, user management with SCIM 2.0, and analytics covering content reporting and coaching insights across the sales cycle. Showpad publishes machine-readable OpenAPI 3.0.3 definitions for both API v3 (200 operations) and API v4 (65 operations), a signed webhook surface, and a hosted OAuth-protected MCP server for AI assistants.
finops:
- name: Showpad Finops
  service_category: ''
  slug: showpad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/showpad.png
layout: provider
mcp_servers:
- description: ''
  name: Showpad MCP Server
  slug: showpad-mcp-server
modified: '2026-08-14'
name: Showpad
nav: Providers
network: true
overview: 'Showpad publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Channels API, Comments API, and 19 more. Tagged areas include Sales Enablement, Sales Coaching, Content Management, Buyer Engagement, and Sales Analytics.


  The Showpad catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Showpad''s developer surface includes authentication, CLI, sandbox, developer portal, documentation, API reference, getting-started guide, and 41 more developer resources.'
plans:
- name: Showpad Plans Pricing
  plan_count: 3
  slug: showpad-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Showpad Rate Limits
  slug: showpad-rate-limits
scopes:
- name: Showpad Scopes
  scope_count: 8
  slug: showpad-scopes
  summary_line: 8 scopes · password/authorizationCode
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 27
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 62.5
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 63.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/showpad/refs/heads/main/screenshots/showpad-2026-06-20T193845.png
security:
- kind: authentication
  name: Showpad Authentication
  slug: showpad-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Showpad Domain Security
  slug: showpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Showpad Vulnerability Disclosure
  slug: showpad-vulnerability-disclosure
  summary_line: Intigriti · contact published
- kind: trust-center
  name: Showpad Trust Center
  slug: showpad-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701
slug: showpad
tags:
- Sales Enablement
- Sales Coaching
- Content Management
- Buyer Engagement
- Sales Analytics
- Training
- CRM Integration
- Digital Sales Rooms
- MCP
- SCIM
website: https://developer.showpad.com/
---
