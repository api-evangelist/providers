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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 50.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for accessing Fellow meeting data — recordings, transcripts, structured notes, and action items — plus recording uploads and webhook management. Uses X-API-KEY authentication, cursor-based pa
  name: Fellow Developer API
  slug: fellow-developer-api
artifact_total: 7
asyncapis:
- description: Real-time webhook events delivered by Fellow when meeting AI notes and action items change. Fellow POSTs JSON to a registered HTTPS endpoint. Deliveries are svix-signed (HMAC-SHA256 over `{svix-id}.{s
  name: Fellow Webhooks
  slug: fellow-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fellow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fellow.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fellow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fellow.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.fellow.ai/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.fellow.ai/reference/authentication-1
- group: operate
  title: ''
  type: Support
  url: https://help.fellow.ai/
- group: company
  title: ''
  type: Blog
  url: https://fellow.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fellowapp
- group: commercial
  title: ''
  type: Pricing
  url: https://fellow.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://fellow.app/auth/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fellow.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fellow.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fellow.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fellow.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://help.fellow.ai/en/articles/4302231-security-and-compliance
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fellow-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fellow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fellow-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fellow-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/fellow-webhooks-asyncapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fellow-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fellow-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fellow-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fellow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fellow-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fellow-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fellow-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fellow-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/fellow-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fellow-well-known.yml
created: '2026-07-17'
description: 'Fellow is an AI meeting assistant and meeting-management platform that records, transcribes, and summarizes meetings, then captures structured notes, action items, and decisions across a team''s calendar. Fellow''s Developer API opens that meeting data through a REST interface: authenticated workspace users generate personal API keys and retrieve recordings, transcripts, notes, and action items, upload recordings, and manage webhook subscriptions for real-time events. Fellow also publishes a hosted, OAuth-secured Model Context Protocol (MCP) server so AI assistants like Claude and ChatGPT can query meeting context in natural language. Backed by Craft Ventures and Felicis. The API requires a paid workspace plan and is governed by workspace admins under Security settings, with a 90-day audit log, SOC 2 Type II, HIPAA BAA availability, and GDPR/CCPA support.'
image: https://framerusercontent.com/assets/J0X2qL3rwf819TDwjCc8iG9UjUk.png
layout: provider
mcp_servers:
- description: ''
  name: fellow-mcp.yml
  slug: fellow-mcpyml
modified: '2026-07-19'
name: Fellow
nav: Providers
network: true
overview: 'Fellow publishes 1 API on the [APIs.io](https://apis.io/) network: Developer API. Tagged areas include Company, Saas, Meetings, AI, and Meeting Notes.


  The Fellow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fellow''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 37
rate_limits:
- limit_count: 0
  name: Fellow Rate Limits
  slug: fellow-rate-limits
scopes:
- name: Fellow Scopes
  scope_count: 5
  slug: fellow-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 27.8
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 47.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Fellow Authentication
  slug: fellow-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Fellow Domain Security
  slug: fellow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fellow
tags:
- Company
- Saas
- Meetings
- AI
- Meeting Notes
- Transcription
- Productivity
- Action Items
- Webhooks
- MCP
website: https://fellow.ai
---
