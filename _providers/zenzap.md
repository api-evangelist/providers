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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Zenzap Agentic Access
  operation_count: 28
  slug: zenzap-agentic-access
  summary_line: 28 operations · 19 acting
api_count: 8
apis:
- description: Endpoints for AI agents to programmatically set up Zenzap organizations. Use `POST /v2/agentic/organization/create` to create an organization, install a bot, and invite a human user in a single reques
  name: ZenZap Agentic API
  slug: zenzap-agentic-api
- description: 'Long polling allows your integration to fetch outbound events instead of receiving webhooks. Use `GET /v2/updates` with: - `offset`: value returned as `nextOffset` from the previous response - `limit`'
  name: ZenZap Long Polling API
  slug: zenzap-long-polling-api
- description: Operations for retrieving organization members
  name: ZenZap Members API
  slug: zenzap-members-api
- description: Operations for sending messages
  name: ZenZap Messages API
  slug: zenzap-messages-api
- description: 'OAuth 2.0 `client_credentials` grant. Used by API-key bots that were created with `credentialType: oauth` to mint short-lived bearer access tokens. **In a nutshell:** 1. Get a `clientId` and `clientSe'
  name: ZenZap OAuth API
  slug: zenzap-oauth-api
- description: Operations for creating polls, recording votes, and retracting votes. Polls are posted as messages in a topic. When you create a poll, each option is assigned a server-generated 6-character ID — use t
  name: ZenZap Polls API
  slug: zenzap-polls-api
- description: Operations for managing tasks
  name: ZenZap Tasks API
  slug: zenzap-tasks-api
- description: Operations for managing topics (group chats/channels/conversations)
  name: ZenZap Topics (group chats/channels/conversations) API
  slug: zenzap-topics-group-chats-channels-conversations-api
artifact_total: 15
asyncapis:
- description: ''
  name: Zenzap Webhooks
  slug: zenzap-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenzap.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenzap.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenzap.co/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenzap.co/api-reference/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.zenzap.co/quickstart
- group: operate
  title: ''
  type: Support
  url: https://knowledge.zenzap.co/
- group: company
  title: ''
  type: Blog
  url: https://www.zenzap.co/blog-posts
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenzap.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://onelink-invites.zenzap.co/7Aqe/7f0o4ql4
- group: start
  title: ''
  type: Login
  url: https://app.zenzap.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zenzap.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zenzap.co/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenzap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zenzap-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenzap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenzap-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zenzap-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zenzap.co/trust-center
- group: design
  title: ''
  type: Conformance
  url: conformance/zenzap-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zenzap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zenzap-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenzap-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zenzap-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zenzap-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zenzap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenzap-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zenzap-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zenzap-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.zenzap.co/
created: '2026-07-17'
description: 'Zenzap is an AI-native work communication platform — "Work Chat Built for the AI Era" — used by teams in healthcare, hospitality, construction, food service, retail, franchise, manufacturing, and non-profit operations. It organizes work into topics (group chats / channels / conversations) carrying messages, tasks, polls, reactions, and file attachments, with HIPAA and SOC 2 compliance, SAML SSO, and SCIM provisioning for enterprises. The Zenzap External Integration API (v2) lets external applications and AI agents act as bots: create topics, send and manage messages, run tasks and polls, manage members, and receive events by webhook or long polling. Backed by Bessemer Venture Partners.'
image: https://cdn.prod.website-files.com/6559c53afcb17d5a5995bfc0/683d76d5c705aada2bab4c9e_Open%20graph%20visual.png
layout: provider
mcp_servers:
- description: ''
  name: zenzap-mcp.yml
  slug: zenzap-mcpyml
modified: '2026-07-21'
name: ZenZap
nav: Providers
network: true
overview: 'ZenZap publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agentic API, Long Polling API, Members API, and 5 more. Tagged areas include Company, Ai Ml, Messaging, Team Communication, and Collaboration.


  The ZenZap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZenZap''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 99
scopes:
- name: Zenzap Scopes
  scope_count: 12
  slug: zenzap-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 76.0
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Zenzap Authentication
  slug: zenzap-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Zenzap Domain Security
  slug: zenzap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zenzap Trust Center
  slug: zenzap-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: zenzap
tags:
- Company
- Ai Ml
- Messaging
- Team Communication
- Collaboration
- Chat
- Bots
- Webhooks
- Productivity
- Tasks
website: https://www.zenzap.co/
---
