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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST + JSON API for GroupMe groups, memberships, messages, chats, likes, blocks, users, and bots, plus a Bayeux push service and bot webhook callbacks.
  name: GroupMe API v3
  slug: groupme-api-v3
artifact_total: 5
asyncapis:
- description: ''
  name: Groupme Push Webhooks
  slug: groupme-push-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://groupme.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.groupme.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.groupme.com/docs/v3
- group: docs
  title: ''
  type: APIReference
  url: https://dev.groupme.com/docs/v3
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.groupme.com/tutorials/oauth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://groupme.com/en-US/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groupme.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://web.groupme.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/groupme-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groupme-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/groupme-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groupme-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/groupme-push-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/groupme-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groupme-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groupme-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/groupme-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groupme-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/groupme-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groupme-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groupme-domain-security.yml
created: '2026-07-17'
description: GroupMe is a group messaging application, owned by Microsoft, that lets people chat in named groups and direct conversations across iOS, Android, and the web, including over SMS. For developers, GroupMe publishes the GroupMe API v3 — a REST + JSON API at https://api.groupme.com/v3 authenticated with a per-user access token in the X-Access-Token header. The API covers groups and former groups, memberships and nicknames, group and direct messages with attachments, likes, blocks, user profiles, and bots. A Bayeux/Faye push service delivers realtime message and typing events, and bots receive HTTP webhook callbacks for every group message. GroupMe was surfaced as a portfolio company of Thrive Capital and enriched here from its public developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groupme.png
layout: provider
mcp_servers:
- description: ''
  name: groupme-mcp.yml
  slug: groupme-mcpyml
modified: '2026-07-19'
name: GroupMe
nav: Providers
network: true
overview: 'GroupMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Messaging, Chat, and Bots.


  The GroupMe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GroupMe''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 16 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 38.3
  delta: -0.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 38.7
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groupme/refs/heads/main/screenshots/groupme-2026-07-25T220348.png
security:
- kind: authentication
  name: Groupme Authentication
  slug: groupme-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Groupme Domain Security
  slug: groupme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groupme
tags:
- Company
- Consumer
- Messaging
- Chat
- Bots
- Group Messaging
- Communication
- Social
website: https://groupme.com
---
