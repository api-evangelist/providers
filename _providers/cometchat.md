---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Cometchat Agentic Access
  operation_count: 52
  slug: cometchat-agentic-access
  summary_line: 52 operations · 33 acting
api_count: 13
apis:
- description: Client SDKs (JavaScript, React, React Native, Android, iOS, Flutter, Ionic) connect over a managed WebSocket layer for realtime message delivery, typing indicators, presence, and read receipts. The so
  name: CometChat Realtime & Client SDK
  slug: cometchat-realtime-sdk
- description: Per-user authentication tokens for SDK login
  name: CometChat Auth Tokens API
  slug: cometchat-auth-tokens-api
- description: Ban and unban users from groups
  name: CometChat Banned Users API
  slug: cometchat-banned-users-api
- description: Block and unblock users
  name: CometChat Blocked Users API
  slug: cometchat-blocked-users-api
- description: List conversations and manage read/delivered state
  name: CometChat Conversations API
  slug: cometchat-conversations-api
- description: User-to-user friend relationships
  name: CometChat Friends API
  slug: cometchat-friends-api
- description: Add, list, kick, and scope group members
  name: CometChat Group Members API
  slug: cometchat-group-members-api
- description: Create and manage groups
  name: CometChat Groups API
  slug: cometchat-groups-api
- description: Send, list, edit, and delete messages
  name: CometChat Messages API
  slug: cometchat-messages-api
- description: Add and remove message reactions
  name: CometChat Reactions API
  slug: cometchat-reactions-api
- description: Custom roles and permissions
  name: CometChat Roles API
  slug: cometchat-roles-api
- description: Create and manage app users
  name: CometChat Users API
  slug: cometchat-users-api
- description: Register webhooks and manage event triggers
  name: CometChat Webhooks API
  slug: cometchat-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: CometChat REST Management API
  slug: open-cometchat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cometchat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cometchat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cometchat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cometchat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cometchat
- group: company
  title: ''
  type: Website
  url: https://www.cometchat.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cometchat.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/cometchat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cometchat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cometchat-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cometchat.com/blog
created: '2026-06-20'
description: CometChat is an in-app messaging platform offering chat, voice, and video SDKs plus a server-side REST Management API. The REST API (v3) manages users, auth tokens, groups, group members, messages, conversations, reactions, roles, and webhooks for an app, while client SDKs and a managed realtime WebSocket layer deliver one-to-one and group conversations, presence, and calling.
finops:
- name: Cometchat Finops
  service_category: Communication and Messaging
  slug: cometchat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cometchat.png
layout: provider
modified: '2026-06-20'
name: CometChat
nav: Providers
network: true
overview: 'CometChat publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth Tokens API, Banned Users API, Blocked Users API, and 9 more. Tagged areas include Chat, Messaging, Voice, Video, and SDK.


  CometChat''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cometchat Plans Pricing
  plan_count: 4
  slug: cometchat-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 4
  name: Cometchat Rate Limits
  slug: cometchat-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cometchat/refs/heads/main/screenshots/cometchat-2026-06-20T174808.png
security:
- kind: authentication
  name: Cometchat Authentication
  slug: cometchat-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cometchat Domain Security
  slug: cometchat-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cometchat
tags:
- Chat
- Messaging
- Voice
- Video
- SDK
- Realtime
website: https://www.cometchat.com
---
