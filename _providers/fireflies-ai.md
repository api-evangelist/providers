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
- description: Public GraphQL API for Fireflies.ai — query transcripts, users, channels, bites, analytics, and AskFred threads; upload audio; control the live-meeting bot; and subscribe to webhooks. Single endpoint,
  name: Fireflies.ai GraphQL API
  slug: fireflies-ai-graphql
artifact_total: 7
asyncapis:
- description: ''
  name: Fireflies Ai Webhooks
  slug: fireflies-ai-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fireflies-ai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fireflies.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fireflies.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fireflies.ai/graphql-api/query/transcripts
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fireflies.ai/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://fireflies.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://guide.fireflies.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firefliesai
- group: commercial
  title: ''
  type: Pricing
  url: https://fireflies.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fireflies.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fireflies.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fireflies.ai/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fireflies.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fireflies-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fireflies-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fireflies-ai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fireflies-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fireflies-ai-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fireflies-ai-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fireflies-ai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fireflies-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.fireflies.ai/additional-info/deprecated
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fireflies-ai-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fireflies-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fireflies-ai-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fireflies-ai-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fireflies-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/fireflies-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fireflies-ai-packages.yml
created: '2026-07-17'
description: Fireflies.ai is an AI meeting assistant that records, transcribes, summarizes, searches, and analyzes voice conversations across Zoom, Google Meet, Microsoft Teams, Webex, and dialed calls. It offers 95%+ transcription accuracy in 100+ languages, AI-generated summaries with action items, conversation analytics, soundbites, and the AskFred assistant. Developers integrate via a public GraphQL API (bearer-token auth, with OAuth 2.0 for apps and the hosted MCP server) that exposes transcripts, users, channels, analytics, audio upload, live-meeting bot control, webhooks, and a WebSocket Realtime transcription stream.
image: https://fireflies.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: fireflies-ai-mcp.yml
  slug: fireflies-ai-mcpyml
modified: '2026-07-19'
name: Fireflies.ai
nav: Providers
network: true
overview: 'Fireflies.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Meetings, Transcription, Speech to Text, and Conversation Intelligence.


  The Fireflies.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fireflies.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 27
rate_limits:
- limit_count: 0
  name: Fireflies Ai Rate Limits
  slug: fireflies-ai-rate-limits
scopes:
- name: Fireflies Ai Scopes
  scope_count: 2
  slug: fireflies-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Fireflies Ai Authentication
  slug: fireflies-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fireflies Ai Domain Security
  slug: fireflies-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fireflies-ai
tags:
- Company
- Meetings
- Transcription
- Speech to Text
- Conversation Intelligence
- Artificial Intelligence
- GraphQL
- MCP
- Productivity
website: https://fireflies.ai/api
---
