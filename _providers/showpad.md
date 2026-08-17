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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: Manage assets, query content with ShowQL, get content recommendations, and handle buyer engagement through shares, sharing themes, and digital shared spaces.
  name: Showpad Content API
  slug: showpad-content-api
- description: The actively developed Showpad REST API. Covers assets and asset files, tags and tag categories, divisions, users, shares, Shared Spaces with templates, themes and quick actions, CRM recommendation ru
  name: Showpad API v4
  slug: showpad-api-v4
- description: Access analytics and insights for coaching and training programs, including learning paths, skill assessments, roleplay AI analysis, and coach analytics data.
  name: Showpad Coach API
  slug: showpad-coach-api
- description: Create and manage users, groups, divisions, and permissions with full SCIM 2.0 support for automated identity provisioning and deprovisioning.
  name: Showpad User Management API
  slug: showpad-user-management-api
- description: Create and manage webhook subscriptions and read their delivery logs. Notifications carry a CloudEvents-shaped envelope and are signed with HMAC-SHA256 over the raw body plus a timestamp, with a five-
  name: Showpad Webhooks API
  slug: showpad-webhooks-api
- description: Hosted remote Model Context Protocol server that lets AI assistants such as Claude and Cursor search Showpad assets, fetch their content, run ShowQL filters, ask questions with cited sources, and read
  name: Showpad MCP Server
  slug: showpad-mcp-server
artifact_total: 16
asyncapis:
- description: ''
  name: Showpad Webhooks
  slug: showpad-webhooks
common:
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
  name: showpad-mcp.yml
  slug: showpad-mcpyml
modified: '2026-08-14'
name: Showpad
nav: Providers
network: true
overview: 'Showpad publishes 3 APIs on the [APIs.io](https://apis.io/) network: Content API, API v4, and User Management API. Tagged areas include Sales Enablement, Sales Coaching, Content Management, Buyer Engagement, and Sales Analytics.


  The Showpad catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Showpad''s developer surface includes authentication, CLI, sandbox, developer portal, documentation, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Showpad Plans Pricing
  plan_count: 3
  slug: showpad-plans-pricing
random_paper: 13
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
  band: exemplar
  composite: 71.2
  delta: 37.8
  facets:
    commercial_clarity: 100.0
    contract_quality: 59.5
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 33.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
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
- Model Context Protocol
- SCIM
website: https://developer.showpad.com/
---
