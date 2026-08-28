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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Version 1 of the HockeyStack Revenue Agents API. Attaches AI agents to companies and deals from the connected CRM, holds conversations with those agents, manages the tasks they generate, and reads the
  name: HockeyStack Revenue Agents API
  slug: hockeystack-revenue-agents-api
artifact_total: 9
asyncapis:
- description: ''
  name: Hockeystack Webhooks
  slug: hockeystack-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.hockeystack.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hockeystack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hockeystack.com/
- group: company
  title: ''
  type: Blog
  url: https://hockeystack.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://hockeystack.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.hockeystack.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hockeystack.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hockeystack.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.hockeystack.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hockeystack-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hockeystack-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hockeystack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hockeystack-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hockeystack-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hockeystack-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hockeystack-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hockeystack-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/hockeystack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hockeystack-packages.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hockeystack-tool-crosswalk.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hockeystack-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hockeystack-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hockeystack-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hockeystack-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hockeystack-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hockeystack-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/hockeystack-components.yml
- group: auth
  title: ''
  type: Compliance
  url: security/hockeystack-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hockeystack-agents-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HockeyStack
- group: operate
  title: ''
  type: Support
  url: mailto:support@hockeystack.com
- group: start
  title: ''
  type: SignUp
  url: https://www.hockeystack.com/pricing
created: '2026-07-17'
description: 'HockeyStack is a B2B revenue and marketing data intelligence platform that unifies marketing, sales, and product data to reveal the full buyer journey from first anonymous (cookieless) touch to closed-won. It applies multiple attribution models, account and intent scoring, lift/incrementality analysis, and no-SQL custom dashboards, and deploys AI "Revenue Agents" (via its ATLAS data foundation and the hosted "Omni" MCP server) to forecast pipeline, brief accounts, and recommend next-best actions. Data flows bidirectionally through prebuilt connectors to CRMs (Salesforce, HubSpot), ad platforms (LinkedIn, Google, Facebook, TikTok), ABM tools, data warehouses (Snowflake, BigQuery), and CDPs (Segment). Its programmatic surface is two-part: the OAuth-secured hosted "Omni" MCP server, and the Revenue Agents REST API v1 (bearer token, 30 operations across agents, conversations, tasks and credits), which is wrapped by a first-party npm MCP server but has no published OpenAPI. Backed
  by Bessemer Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hockeystack.png
layout: provider
mcp_servers:
- description: ''
  name: HockeyStack MCP Server
  slug: hockeystack-mcp-server
modified: '2026-08-13'
name: HockeyStack
nav: Providers
network: true
overview: 'HockeyStack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Marketing Analytics, Attribution, and Revenue Intelligence.


  The HockeyStack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HockeyStack''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, support, signup flow, and 25 more developer resources.'
plans:
- name: Hockeystack Plans Pricing
  plan_count: 0
  slug: hockeystack-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Hockeystack Rate Limits
  slug: hockeystack-rate-limits
scopes:
- name: Hockeystack Scopes
  scope_count: 1
  slug: hockeystack-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 41.8
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.8
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hockeystack/refs/heads/main/screenshots/hockeystack-2026-07-25T221312.png
security:
- kind: authentication
  name: Hockeystack Authentication
  slug: hockeystack-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hockeystack Domain Security
  slug: hockeystack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hockeystack Trust Center
  slug: hockeystack-trust-center
  summary_line: SOC 2 Type 2
slug: hockeystack
tags:
- Company
- Data
- Marketing Analytics
- Attribution
- Revenue Intelligence
- B2B
- Account Intelligence
- MCP
- AI Agents
website: https://www.hockeystack.com/
---
