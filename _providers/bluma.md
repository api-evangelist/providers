---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://docs.getbluma.com/concepts/credits
  - https://docs.getbluma.com/guides/test-vs-production
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 29.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Asynchronous short-form video generation REST API. Submit a template id and a prompt to POST /v1/videos, receive a job id, and collect the finished render either by polling GET /v1/videos/{id} or by s
  name: Bluma API
  slug: bluma-api
- description: Hosted Model Context Protocol server on the Bluma API host. Discovered via RFC 9728 OAuth Protected Resource Metadata rather than from the documentation, which never mentions it. Requires an OAuth 2.1
  name: Bluma MCP Server
  slug: bluma-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Bluma Webhooks
  slug: bluma-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getbluma.com
- group: start
  title: ''
  type: SignUp
  url: https://www.getbluma.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbluma.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbluma.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getbluma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getbluma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getbluma.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getbluma.com/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluma-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bluma-scopes.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.getbluma.com/concepts/credits
- group: commercial
  title: ''
  type: Plans
  url: plans/bluma-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bluma-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bluma-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bluma-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bluma-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bluma-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bluma-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bluma-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bluma-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/bluma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bluma-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bluma-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bluma-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bluma-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bluma-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/cZGXY4nrFZ
- group: start
  title: ''
  type: Login
  url: https://app.getbluma.com/settings?tab=api
created: '2026-07-17'
description: 'Bluma is a San Francisco-based AI company (Y Combinator Fall 2025) building a short-form AI content engine that lets creators, agencies, and brands produce social media video ads at scale. The platform "de-edits" existing reference videos into their individual scenes, captions, and overlays, then uses AI asset generation and a node-based canvas editor to recreate and remix shots into new ads, UGC, and template-based videos optimized for TikTok, Reels, and Shorts. Bluma ships a public developer program: a REST API at api.getbluma.com/api/v1 for asynchronous video generation, templates, credits, API keys, webhooks and usage analytics; Mintlify-hosted documentation at docs.getbluma.com; first-party TypeScript and Python SDKs; a seven-event HMAC-signed webhook surface; published per-tier rate limits; and an undocumented but live hosted MCP server at api.getbluma.com/api/mcp gated by Clerk OAuth 2.1 with dynamic client registration. Founded by Alisa Wu (formerly Zoox/Amazon) and
  Stephen Ni.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluma.png
layout: provider
mcp_servers:
- description: ''
  name: Bluma MCP Server
  slug: bluma-mcp-server
modified: '2026-08-12'
name: Bluma
nav: Providers
network: true
overview: 'Bluma publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Video Generation, and Advertising.


  The Bluma catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bluma''s developer surface includes signup flow, documentation, API reference, getting-started guide, authentication, pricing, changelog, and 23 more developer resources.'
plans:
- name: Bluma Plans Pricing
  plan_count: 6
  slug: bluma-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Bluma Rate Limits
  slug: bluma-rate-limits
scopes:
- name: Bluma Scopes
  scope_count: 0
  slug: bluma-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 56.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluma/refs/heads/main/screenshots/bluma-2026-07-25T203511.png
security:
- kind: authentication
  name: Bluma Authentication
  slug: bluma-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Bluma Domain Security
  slug: bluma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluma
tags:
- Company
- Artificial Intelligence
- Video
- Video Generation
- Advertising
- Marketing
- Content Creation
- Short-Form Video
- Social-Media
- Generative AI
- Creative Tools
- Text-to-Speech
- Media
- Automation
- Webhook
website: https://www.getbluma.com
---
