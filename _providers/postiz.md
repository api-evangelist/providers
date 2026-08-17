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
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 65.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 143
  human_in_the_loop: 122
  name: Postiz Agentic Access
  operation_count: 248
  slug: postiz-agentic-access
  summary_line: 248 operations · 143 acting · 122 human-in-the-loop
api_count: 9
apis:
- description: Configure a webhook URL in Postiz to receive an HTTP POST notifying your own systems when a post is published, so you can sync downstream tools such as spreadsheets, Slack, or a CRM. Webhooks are conf
  name: Postiz Webhooks
  slug: webhooks
- description: Platform- and post-level analytics.
  name: Postiz Analytics API
  slug: postiz-analytics-api
- description: Connected social media channels and scheduling slots.
  name: Postiz Integrations API
  slug: postiz-integrations-api
- description: Account notifications.
  name: Postiz Notifications API
  slug: postiz-notifications-api
- description: Create, schedule, list, and delete posts.
  name: Postiz Posts API
  slug: postiz-posts-api
- description: Upload media files referenced by posts.
  name: Postiz Uploads API
  slug: postiz-uploads-api
- description: The complete, provider-published Postiz Public API — 23 operations across integrations (channels), groups, posts, uploads, analytics, notifications and AI video generation, served at https://api.posti
  name: Postiz Public API
  slug: postiz-public-api
- description: Hosted, remote Model Context Protocol server run as part of the Postiz backend, exposing 11 tools for listing channels, reading platform settings schemas, scheduling and re-settings posts, and generat
  name: Postiz MCP Server
  slug: postiz-mcp-server
- description: The full Postiz backend surface as published by the provider's own Swagger UI at https://api.postiz.com/docs, machine-readable at /docs-json — 205 operations across auth, integrations, posts, media, b
  name: Postiz Platform API
  slug: postiz-platform-api
artifact_total: 26
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
  name: postiz-mcp.yml
  slug: postiz-mcpyml
modified: '2026-08-13'
name: Postiz
nav: Providers
network: true
overview: 'Postiz publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Integrations API, Notifications API, and 4 more. Tagged areas include Social Media, Scheduling, Open Source, Content, and Marketing.


  The Postiz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Postiz''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, sandbox, API reference, and 37 more developer resources.'
plans:
- name: Postiz Plans Pricing
  plan_count: 5
  slug: postiz-plans-pricing
random_paper: 85
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
  band: exemplar
  composite: 74.2
  delta: 35.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 64.8
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 92.1
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
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
- Social Media
- Scheduling
- Open Source
- Content
- Marketing
- Agents
- MCP
- Automation
- Publishing
- Analytics
website: https://postiz.com
---
