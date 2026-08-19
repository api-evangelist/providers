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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Chatwork Agentic Access
  operation_count: 32
  slug: chatwork-agentic-access
  summary_line: 32 operations · 17 acting
api_count: 9
apis:
- description: The Contacts API from Chatwork — 1 operation(s) for contacts.
  name: Chatwork Contacts API
  slug: chatwork-contacts-api
- description: The Files API from Chatwork — 2 operation(s) for files.
  name: Chatwork Files API
  slug: chatwork-files-api
- description: The Incoming Requests API from Chatwork — 2 operation(s) for incoming requests.
  name: Chatwork Incoming Requests API
  slug: chatwork-incoming-requests-api
- description: The Link API from Chatwork — 1 operation(s) for link.
  name: Chatwork Link API
  slug: chatwork-link-api
- description: The Me API from Chatwork — 3 operation(s) for me.
  name: Chatwork Me API
  slug: chatwork-me-api
- description: The Members API from Chatwork — 1 operation(s) for members.
  name: Chatwork Members API
  slug: chatwork-members-api
- description: The Messages API from Chatwork — 4 operation(s) for messages.
  name: Chatwork Messages API
  slug: chatwork-messages-api
- description: The Rooms API from Chatwork — 2 operation(s) for rooms.
  name: Chatwork Rooms API
  slug: chatwork-rooms-api
- description: The Tasks API from Chatwork — 3 operation(s) for tasks.
  name: Chatwork Tasks API
  slug: chatwork-tasks-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chatwork API v2 Contacts API
  slug: open-chatwork-contacts-api
- collection_type: open
  name: Chatwork API v2 Contacts Files API
  slug: open-chatwork-files-api
- collection_type: open
  name: Chatwork API v2 Contacts Incoming Requests API
  slug: open-chatwork-incoming-requests-api
- collection_type: open
  name: Chatwork API v2 Contacts Link API
  slug: open-chatwork-link-api
- collection_type: open
  name: Chatwork API v2 Contacts Me API
  slug: open-chatwork-me-api
- collection_type: open
  name: Chatwork API v2 Contacts Members API
  slug: open-chatwork-members-api
- collection_type: open
  name: Chatwork API v2 Contacts Messages API
  slug: open-chatwork-messages-api
- collection_type: open
  name: Chatwork API v2 Contacts Rooms API
  slug: open-chatwork-rooms-api
- collection_type: open
  name: Chatwork API v2 Contacts Tasks API
  slug: open-chatwork-tasks-api
- collection_type: open
  name: Chatwork API v2
  slug: open-chatwork
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chatwork-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chatwork-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatwork-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatwork-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatwork
- group: company
  title: ''
  type: Website
  url: https://go.chatwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.chatwork.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.chatwork.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://go.chatwork.com/en/price/
- group: start
  title: ''
  type: Signup
  url: https://www.chatwork.com/login/
- group: start
  title: ''
  type: Login
  url: https://www.chatwork.com/login/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.chatwork.com/docs/oauth
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatwork
- group: other
  title: ''
  type: API Source
  url: https://github.com/chatwork/api
- group: operate
  title: ''
  type: Support
  url: https://help.chatwork.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chatwork.com
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/chatwork/chatwork-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.chatwork.com/llms.txt
created: '2026-05-11'
description: Chatwork is a Japanese business messaging and collaboration platform similar to Slack, providing group chat rooms, task management, file sharing, and video calls for teams and organizations. The Chatwork REST API v2 enables programmatic access to user info, contacts, chat rooms, messages, tasks, and files, authenticated via an API token sent in the X-ChatWorkToken HTTP header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatwork.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Chatwork
nav: Providers
network: true
overview: 'Chatwork publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Files API, Incoming Requests API, and 6 more. Tagged areas include Messaging, Chat, Collaboration, Productivity, and Tasks.


  Chatwork''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, and 12 more developer resources.'
random_paper: 122
score:
  band: thin
  composite: 28.3
  delta: -9.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 25.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/chatwork/refs/heads/main/screenshots/chatwork-2026-06-20T174238.png
security:
- kind: authentication
  name: Chatwork Authentication
  slug: chatwork-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chatwork Domain Security
  slug: chatwork-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chatwork Vulnerability Disclosure
  slug: chatwork-vulnerability-disclosure
  summary_line: disclosure policy published
slug: chatwork
tags:
- Messaging
- Chat
- Collaboration
- Productivity
- Tasks
website: https://go.chatwork.com
---
