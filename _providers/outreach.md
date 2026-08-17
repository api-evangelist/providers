---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.outreach.ai/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 160
  human_in_the_loop: 0
  name: Outreach Agentic Access
  operation_count: 253
  slug: outreach-agentic-access
  summary_line: 253 operations · 160 acting
api_count: 5
apis:
- description: JSON API 1.0 REST API covering accounts, prospects, opportunities, sequences, sequence states, mailings, calls, tasks, teams, users, notes, imports, batch actions and webhooks — 147 paths and 253 oper
  name: Outreach REST API
  slug: outreach-rest-api
- description: Remote Model Context Protocol server exposing Outreach as 41 agent tools (27 read, 11 write, 3 schema introspection) over streamable HTTP, authorized by OAuth 2.1 with PKCE and RFC 7591 Dynamic Client
  name: Outreach MCP Server
  slug: outreach-mcp-server
- description: Client extensibility surface for embedding a web application inside the Outreach client — shell, tab and tile web-widget extensions, a text-editor extension, activity-feed custom events and a mailing-
  name: Outreach Client Extensions API
  slug: outreach-client-extensions-api
- description: Read-only access to an organization's Outreach data through Snowflake secure data sharing and Delta Sharing, in a ready-to-query format with no data copy or custom pipeline. Roughly 60 documented tabl
  name: Outreach Data Sharing
  slug: outreach-data-sharing
- description: Event-driven webhook deliveries for accounts, calls, contacts, email addresses, imports, Kaia recordings, mailings, opportunities, opportunity prospect roles, prospects, sequences, sequence states, ta
  name: Outreach Webhooks
  slug: outreach-webhooks
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/outreach-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/outreach-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/outreach-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/outreach-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.outreach.ai/platform/trust
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/outreach-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.outreach.ai/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outreach-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outreach-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/outreach-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outreach-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.outreach.io
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.outreach.io/api/deprecated-features
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/outreach-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/outreach-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/outreach-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getoutreach
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/outreach-saas
- group: company
  title: ''
  type: Website
  url: https://www.outreach.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.outreach.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.outreach.io/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.outreach.io/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.outreach.io/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.outreach.io/support/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.outreach.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.outreach.ai/request-demo
- group: start
  title: ''
  type: Login
  url: https://accounts.outreach.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outreach.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outreach.ai/privacy-statement
- group: commercial
  title: ''
  type: Plans
  url: plans/outreach-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outreach-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/outreach-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outreach-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.outreach.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.outreach.ai/resources/blog
created: '2026-05-08'
description: Outreach is a sales execution and revenue platform for go-to-market teams, unifying email, calling, social and meetings into sequenced outbound motions with AI agents layered on top. Its public developer surface is a JSON API 1.0 REST API at api.outreach.io/api/v2 covering accounts, prospects, opportunities, sequences, sequence states, mailings, calls, tasks, teams, users, imports and webhooks across 51 tagged resources and 253 operations, authorized by OAuth 2.0 with a scope-per-resource permission model and a separate server-to-server JWT token for unattended integrations. Outreach also runs a remote Model Context Protocol server at api.outreach.io/mcp with 41 tools, authorized by OAuth 2.1 with PKCE and Dynamic Client Registration, plus a client extensibility SDK for embedding web widgets inside the Outreach app, an event-driven webhook surface with HMAC-signed deliveries, and Outreach Data Sharing over Snowflake and Delta Sharing.
finops:
- name: Outreach Finops
  service_category: Sales
  slug: outreach-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outreach.png
json_schemas:
- name: Outreach Hyper
  property_count: 50
  slug: outreach-hyper
layout: provider
mcp_servers:
- description: ''
  name: outreach-mcp.yml
  slug: outreach-mcpyml
modified: '2026-08-13'
name: Outreach
nav: Providers
network: true
overview: 'Outreach publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API and Webhooks. Tagged areas include Sales, Sales Engagement, Sequences, CRM, and Email.


  Outreach''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 29 more developer resources.'
plans:
- name: Outreach Plans Pricing
  plan_count: 4
  slug: outreach-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 4
  name: Outreach Rate Limits
  slug: outreach-rate-limits
scopes:
- name: Outreach Scopes
  scope_count: 46
  slug: outreach-scopes
  summary_line: 46 scopes · authorizationCode
score:
  band: strong
  composite: 63.0
  delta: 37.1
  facets:
    commercial_clarity: 76.3
    contract_quality: 58.8
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 25.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/outreach/refs/heads/main/screenshots/outreach-2026-06-20T191233.png
security:
- kind: authentication
  name: Outreach Authentication
  slug: outreach-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Outreach Domain Security
  slug: outreach-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Outreach Vulnerability Disclosure
  slug: outreach-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Outreach Trust Center
  slug: outreach-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: outreach
tags:
- Sales
- Sales Engagement
- Sequences
- CRM
- Email
- Revenue Operations
- Sales Execution
- Prospecting
- Agents
- MCP
website: https://www.outreach.ai/
---
