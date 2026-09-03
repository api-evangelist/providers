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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 143
  human_in_the_loop: 122
  name: Postiz Agentic Access
  operation_count: 248
  slug: postiz-agentic-access
  summary_line: 248 operations · 143 acting · 122 human-in-the-loop
api_count: 3
apis:
- description: Configure a webhook URL in Postiz to receive an HTTP POST notifying your own systems when a post is published, so you can sync downstream tools such as spreadsheets, Slack, or a CRM. Webhooks are conf
  name: Postiz Webhooks
  slug: webhooks
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: Platform- and post-level analytics.
  name: Postiz Analytics API
  slug: postiz-analytics-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: Connected social media channels and scheduling slots.
  name: Postiz Integrations API
  slug: postiz-integrations-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: Account notifications.
  name: Postiz Notifications API
  slug: postiz-notifications-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: Create, schedule, list, and delete posts.
  name: Postiz Posts API
  slug: postiz-posts-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: Upload media files referenced by posts.
  name: Postiz Uploads API
  slug: postiz-uploads-api
- description: Hosted, remote Model Context Protocol server run as part of the Postiz backend, exposing 11 tools for listing channels, reading platform settings schemas, scheduling and re-settings posts, and generat
  name: Postiz MCP Server
  slug: postiz-mcp-server
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Admin API from Postiz — 3 operation(s) for admin.
  name: Postiz Admin API
  slug: postiz-admin-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Announcements API from Postiz — 2 operation(s) for announcements.
  name: Postiz Announcements API
  slug: postiz-announcements-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Approved Apps API from Postiz — 2 operation(s) for approved apps.
  name: Postiz Approved Apps API
  slug: postiz-approved-apps-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Auth API from Postiz — 10 operation(s) for auth.
  name: Postiz Auth API
  slug: postiz-auth-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Autopost API from Postiz — 4 operation(s) for autopost.
  name: Postiz Autopost API
  slug: postiz-autopost-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Billing API from Postiz — 20 operation(s) for billing.
  name: Postiz Billing API
  slug: postiz-billing-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Copilot API from Postiz — 5 operation(s) for copilot.
  name: Postiz Copilot API
  slug: postiz-copilot-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Enterprise API from Postiz — 3 operation(s) for enterprise.
  name: Postiz Enterprise API
  slug: postiz-enterprise-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Media API from Postiz — 13 operation(s) for media.
  name: Postiz Media API
  slug: postiz-media-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Monitor API from Postiz — 1 operation(s) for monitor.
  name: Postiz Monitor API
  slug: postiz-monitor-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The OAuth API from Postiz — 2 operation(s) for oauth.
  name: Postiz O Auth API
  slug: postiz-oauth-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The OAuth App API from Postiz — 2 operation(s) for oauth app.
  name: Postiz OAuth App API
  slug: postiz-oauth-app-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Public API API from Postiz — 22 operation(s) for public api.
  name: Postiz Public API
  slug: postiz-public-api-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Public API from Postiz — 6 operation(s) for public.
  name: Postiz Public API
  slug: postiz-public-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Root API from Postiz — 1 operation(s) for root.
  name: Postiz Root API
  slug: postiz-root-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Sets API from Postiz — 2 operation(s) for sets.
  name: Postiz Sets API
  slug: postiz-sets-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Settings API from Postiz — 4 operation(s) for settings.
  name: Postiz Settings API
  slug: postiz-settings-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Signatures API from Postiz — 3 operation(s) for signatures.
  name: Postiz Signatures API
  slug: postiz-signatures-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Stripe API from Postiz — 1 operation(s) for stripe.
  name: Postiz Stripe API
  slug: postiz-stripe-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Third Party API from Postiz — 7 operation(s) for third party.
  name: Postiz Third Party API
  slug: postiz-third-party-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The User API from Postiz — 15 operation(s) for user.
  name: Postiz User API
  slug: postiz-user-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: Generate videos with AI
  name: Postiz Video Generation API
  slug: postiz-video-generation-api
- baseURL: https://api.postiz.com/public/v1
  baseurl_source: declared
  description: The Webhooks API from Postiz — 3 operation(s) for webhooks.
  name: Postiz Webhooks API
  slug: postiz-webhooks-api
artifact_total: 47
asyncapis:
- description: ''
  name: Postiz Webhooks
  slug: postiz-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Postiz Public Analytics API
  slug: open-postiz-analytics-api
- collection_type: open
  name: Postiz Public Analytics Integrations API
  slug: open-postiz-integrations-api
- collection_type: open
  name: Postiz Public Analytics Notifications API
  slug: open-postiz-notifications-api
- collection_type: open
  name: Postiz Public Analytics Posts API
  slug: open-postiz-posts-api
- collection_type: open
  name: Postiz Public Analytics Uploads API
  slug: open-postiz-uploads-api
- collection_type: open
  name: Postiz Public API
  slug: open-postiz
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/gitroomhq/postiz-app/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/postiz-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/postiz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postiz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postiz-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitroomhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postiz
- group: company
  title: ''
  type: Website
  url: https://postiz.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postiz.com
- group: company
  title: ''
  type: Blog
  url: https://postiz.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/postiz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postiz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/postiz-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/postiz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/postiz-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/postiz-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/postiz-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/postiz-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/postiz-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postiz-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/postiz-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/postiz-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/postiz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/postiz-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/postiz-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/postiz-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/postiz-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postiz.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/postiz-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/postiz-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/postiz-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/postiz-public-api-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/postiz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/gitroomhq/postiz-app/blob/main/SECURITY.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.postiz.com/public-api/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.postiz.com/public-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.postiz.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.postiz.com/support
- group: operate
  title: ''
  type: Community
  url: https://discord.postiz.com
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.postiz.com
- group: commercial
  title: ''
  type: Pricing
  url: https://postiz.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.postiz.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postiz.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postiz.com/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/gitroomhq/postiz-app
created: '2026-06-25'
description: Postiz is an open-source social media scheduling and management platform for posting across 30+ social, video, community, and blogging channels from a single calendar. It ships as a free AGPL-licensed self-hosted app and as a paid managed Cloud. The Postiz Public API uses simple API-key auth to list connected channels, upload media, and create, schedule, list, and delete posts.
finops:
- name: Postiz Finops
  service_category: Social Media Management
  slug: postiz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postiz.png
layout: provider
mcp_servers:
- description: ''
  name: Postiz MCP Server
  slug: postiz-mcp-server
modified: '2026-08-13'
name: Postiz
nav: Providers
network: true
overview: 'Postiz publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Integrations API, Notifications API, and 25 more. Tagged areas include Social-Media, Scheduling, Open-Source, Content, and Marketing.


  The Postiz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Postiz''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, sandbox, API reference, and 39 more developer resources.'
plans:
- name: Postiz Plans Pricing
  plan_count: 5
  slug: postiz-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Postiz Rate Limits
  slug: postiz-rate-limits
scopes:
- name: Postiz Scopes
  scope_count: 2
  slug: postiz-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 28
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 48.5
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 89.5
  previous_composite: 63.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 22.2
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postiz/refs/heads/main/screenshots/postiz-2026-08-17T080412.png
security:
- kind: authentication
  name: Postiz Authentication
  slug: postiz-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Postiz Domain Security
  slug: postiz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Postiz Vulnerability Disclosure
  slug: postiz-vulnerability-disclosure
  summary_line: contact published
slug: postiz
tags:
- Social-Media
- Scheduling
- Open-Source
- Content
- Marketing
- Agents
- MCP
- Automation
- Publishing
- Analytics
website: https://postiz.com
---
