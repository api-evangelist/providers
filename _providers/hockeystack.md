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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 5
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
  type: WellKnown
  url: well-known/hockeystack-well-known.yml
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
created: '2026-07-17'
description: HockeyStack is a B2B revenue and marketing data intelligence platform that unifies marketing, sales, and product data to reveal the full buyer journey from first anonymous (cookieless) touch to closed-won. It applies multiple attribution models, account and intent scoring, lift/incrementality analysis, and no-SQL custom dashboards, and deploys AI "Revenue Agents" (via its ATLAS data foundation and the hosted "Omni" MCP server) to forecast pipeline, brief accounts, and recommend next-best actions. Data flows bidirectionally through prebuilt connectors to CRMs (Salesforce, HubSpot), ad platforms (LinkedIn, Google, Facebook, TikTok), ABM tools, data warehouses (Snowflake, BigQuery), and CDPs (Segment). Its public programmatic surface is the OAuth-secured Omni MCP server rather than a general REST API. Backed by Bessemer Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hockeystack.png
layout: provider
mcp_servers:
- description: ''
  name: hockeystack-mcp.yml
  slug: hockeystack-mcpyml
modified: '2026-07-19'
name: HockeyStack
nav: Providers
network: true
overview: 'HockeyStack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Marketing Analytics, Attribution, and Revenue Intelligence.


  HockeyStack''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, and 13 more developer resources.'
random_paper: 71
scopes:
- name: Hockeystack Scopes
  scope_count: 1
  slug: hockeystack-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 27.6
  delta: 0.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 27.1
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hockeystack/refs/heads/main/screenshots/hockeystack-2026-07-25T221312.png
security:
- kind: authentication
  name: Hockeystack Authentication
  slug: hockeystack-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hockeystack Domain Security
  slug: hockeystack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hockeystack Trust Center
  slug: hockeystack-trust-center
  summary_line: trust center published
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
