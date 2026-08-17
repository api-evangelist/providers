---
access_model:
  confidence: high
  label: Paid plan required · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - openapi
  trial: false
  try_now: false
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 68.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 112
  human_in_the_loop: 2
  name: Instantly Ai Agentic Access
  operation_count: 186
  slug: instantly-ai-agentic-access
  summary_line: 186 operations · 112 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: 'The full Instantly REST API v2 — 129 paths, 173 operations across 28 resource groups, published as OpenAPI 3.1.0 by Instantly at api.instantly.ai/openapi/api_v2.json. Every operation carries a unique '
  name: Instantly API v2
  slug: instantly-ai-api-v2
- description: The Campaigns API from Instantly — 10 operation(s) for campaigns.
  name: Instantly Campaigns API
  slug: instantly-ai-campaigns-api
artifact_total: 15
asyncapis:
- description: ''
  name: Instantly Ai Webhooks
  slug: instantly-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instantly.ai API v2 Campaigns API
  slug: open-instantly-ai-campaigns-api
- collection_type: open
  name: Instantly.ai API v2
  slug: open-instantly-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instantly-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instantly-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instantly-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://instantly.ai
- group: other
  title: ''
  type: App
  url: https://app.instantly.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.instantly.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developer.instantly.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.instantly.ai/getting-started/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.instantly.ai/getting-started/authorization
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.instantly.ai/openapi/api_v2.json
- group: commercial
  title: ''
  type: Pricing
  url: https://instantly.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://instantly.ai/blog
- group: operate
  title: ''
  type: Help
  url: https://help.instantly.ai
- group: start
  title: ''
  type: Signup
  url: https://app.instantly.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.instantly.ai/auth/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instantly.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instantly.ai/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instantlyai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Instantlydotai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@instantly-ai
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.instantly.ai/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instantly-ai-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.instantly.ai
- group: start
  title: ''
  type: Quickstart
  url: https://developer.instantly.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.instantly.ai
- group: operate
  title: ''
  type: Community
  url: https://developer.instantly.ai/getting-started/slack-channel
- group: start
  title: ''
  type: SignUp
  url: https://app.instantly.ai/auth/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Instantly-ai
- group: build
  title: ''
  type: Packages
  url: packages/instantly-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/instantly-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/instantly-ai-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instantly-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instantly-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/instantly-ai-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/instantly-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instantly-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instantly-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instantly-ai-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instantly-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instantly-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.instantly.ai/guides/api-v1-migration
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instantly-ai-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instantly-ai-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/instantly-ai-api-v2-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/instantly-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instantly-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instantly-ai-finops.yml
created: '2026-05-23'
description: Instantly is a cold email outbound platform that combines mailbox sending infrastructure, email warmup, a B2B lead database, deliverability tools, and a unified inbox for replies. The Instantly v2 REST API at api.instantly.ai/api/v2 publishes a 173-operation OpenAPI 3.1 covering campaigns and subsequences, leads and lead lists, sending accounts and warmup, email verification, inbox placement tests, SuperSearch enrichment, blocklists, custom tags, audit logs, background jobs, webhooks, analytics, API keys, workspaces and workspace groups. Authentication is a scoped Bearer API key backed by a full OAuth 2.0 authorization server with 178 published scopes, PKCE and dynamic client registration. Instantly also runs a hosted remote MCP server, publishes an A2A agent card, an llms.txt and first-party Agent Skills.
finops:
- name: Instantly Ai Finops
  service_category: API
  slug: instantly-ai-finops
graphqls:
- description: '> **Not a provider surface — modelled, not published.** Instantly ships no GraphQL API. On'
  name: Instantly GraphQL Schema
  slug: instantly-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instantly-ai.png
layout: provider
mcp_servers:
- description: ''
  name: instantly-ai-mcp.yml
  slug: instantly-ai-mcpyml
modified: '2026-08-13'
name: Instantly
nav: Providers
network: true
overview: 'Instantly publishes 2 APIs on the [APIs.io](https://apis.io/) network: API v2 and Campaigns API. Tagged areas include Cold Email, Outbound, Sales, Deliverability, and Lead Database.


  The Instantly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Instantly''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 41 more developer resources.'
plans:
- name: Instantly Ai Plans Pricing
  plan_count: 13
  slug: instantly-ai-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 7
  name: Instantly Ai Rate Limits
  slug: instantly-ai-rate-limits
scopes:
- name: Instantly Ai Scopes
  scope_count: 178
  slug: instantly-ai-scopes
  summary_line: 178 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.9
  delta: 20.8
  facets:
    commercial_clarity: 84.2
    contract_quality: 71.9
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/instantly-ai/refs/heads/main/screenshots/instantly-ai-2026-06-20T183518.png
security:
- kind: authentication
  name: Instantly Ai Authentication
  slug: instantly-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Instantly Ai Domain Security
  slug: instantly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instantly-ai
tags:
- Cold Email
- Outbound
- Sales
- Deliverability
- Lead Database
- Email Verification
- Webhooks
website: https://instantly.ai
---
