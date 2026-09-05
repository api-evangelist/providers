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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Zenzap Agentic Access
  operation_count: 28
  slug: zenzap-agentic-access
  summary_line: 28 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: Endpoints for AI agents to programmatically set up Zenzap organizations. Use `POST /v2/agentic/organization/create` to create an organization, install a bot, and invite a human user in a single reques
  name: ZenZap Agentic API
  slug: zenzap-agentic-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: 'Long polling allows your integration to fetch outbound events instead of receiving webhooks. Use `GET /v2/updates` with: - `offset`: value returned as `nextOffset` from the previous response - `limit`'
  name: ZenZap Long Polling API
  slug: zenzap-long-polling-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: Operations for retrieving organization members
  name: ZenZap Members API
  slug: zenzap-members-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: Operations for sending messages
  name: ZenZap Messages API
  slug: zenzap-messages-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: 'OAuth 2.0 `client_credentials` grant. Used by API-key bots that were created with `credentialType: oauth` to mint short-lived bearer access tokens. **In a nutshell:** 1. Get a `clientId` and `clientSe'
  name: ZenZap OAuth API
  slug: zenzap-oauth-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: Operations for creating polls, recording votes, and retracting votes. Polls are posted as messages in a topic. When you create a poll, each option is assigned a server-generated 6-character ID — use t
  name: ZenZap Polls API
  slug: zenzap-polls-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: Operations for managing tasks
  name: ZenZap Tasks API
  slug: zenzap-tasks-api
- baseURL: https://api.zenzap.co
  baseurl_source: declared
  description: Operations for managing topics (group chats/channels/conversations)
  name: ZenZap Topics (group chats/channels/conversations) API
  slug: zenzap-topics-group-chats-channels-conversations-api
artifact_total: 23
asyncapis:
- description: ''
  name: Zenzap Webhooks
  slug: zenzap-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zenzap External Integration Agentic API
  slug: open-zenzap-agentic-api
- collection_type: open
  name: Zenzap External Integration Agentic Long Polling API
  slug: open-zenzap-long-polling-api
- collection_type: open
  name: Zenzap External Integration Agentic Members API
  slug: open-zenzap-members-api
- collection_type: open
  name: Zenzap External Integration Agentic Messages API
  slug: open-zenzap-messages-api
- collection_type: open
  name: Zenzap External Integration Agentic OAuth API
  slug: open-zenzap-oauth-api
- collection_type: open
  name: Zenzap External Integration Agentic Polls API
  slug: open-zenzap-polls-api
- collection_type: open
  name: Zenzap External Integration Agentic Tasks API
  slug: open-zenzap-tasks-api
- collection_type: open
  name: Zenzap External Integration Agentic Topics (group chats/channels/conversations) API
  slug: open-zenzap-topics-group-chats-channels-conversations-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: ZenZap
nav: Providers
network: true
overview: 'ZenZap publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agentic API, Long Polling API, Members API, and 5 more. Tagged areas include Company, Ai Ml, Messaging, Team Communication, and Collaboration.


  The ZenZap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZenZap''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 13
scopes:
- name: Zenzap Scopes
  scope_count: 12
  slug: zenzap-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 68.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 50.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenzap/refs/heads/main/screenshots/zenzap-2026-08-17T083047.png
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
- Webhook
- Productivity
- Task
website: https://www.zenzap.co/
---
