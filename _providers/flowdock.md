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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Flowdock Agentic Access
  operation_count: 54
  slug: flowdock-agentic-access
  summary_line: 54 operations · 27 acting
api_count: 15
apis:
- description: 'Long-lived HTTP connection to stream.flowdock.com delivering real-time flow events. Two content types: newline-delimited JSON (`application/json`, `\r` delimited) or HTML5 Server-Sent Events (`text/ev'
  name: Flowdock Streaming API
  slug: streaming-api
- description: Partial SCIM 1.x user provisioning API for CA Flowdock Enterprise customers with Single Sign-On configured. Bearer-token authenticated. Now offline.
  name: Flowdock SCIM Provisioning API
  slug: scim-api
- description: OAuth 2.0 authorization-code grant for user delegation.
  name: Flowdock (Discontinued) Authentication API
  slug: flowdock-authentication-api
- description: Chat-style messages posted as an external user.
  name: Flowdock (Discontinued) Chat API
  slug: flowdock-chat-api
- description: File uploads and downloads attached to messages.
  name: Flowdock (Discontinued) Files API
  slug: flowdock-files-api
- description: Team workspaces combining chat and a shared team inbox.
  name: Flowdock (Discontinued) Flows API
  slug: flowdock-flows-api
- description: Open and accepted invitations to join a flow.
  name: Flowdock (Discontinued) Invitations API
  slug: flowdock-invitations-api
- description: Chat messages, comments, status, activity, discussion, and file events posted to a flow.
  name: Flowdock (Discontinued) Messages API
  slug: flowdock-messages-api
- description: Account-level container that owns flows and bills users.
  name: Flowdock (Discontinued) Organizations API
  slug: flowdock-organizations-api
- description: One-to-one direct message channels between two users.
  name: Flowdock (Discontinued) Private Conversations API
  slug: flowdock-private-conversations-api
- description: Messages within a private conversation.
  name: Flowdock (Discontinued) Private Messages API
  slug: flowdock-private-messages-api
- description: External integrations (GitHub, Jira, Zendesk, etc.) that post into a flow.
  name: Flowdock (Discontinued) Sources API
  slug: flowdock-sources-api
- description: Mail-like messages posted into a flow's team inbox.
  name: Flowdock (Discontinued) Team Inbox API
  slug: flowdock-team-inbox-api
- description: Threaded conversations rooted on a parent message.
  name: Flowdock (Discontinued) Threads API
  slug: flowdock-threads-api
- description: User accounts that may belong to multiple organizations and flows.
  name: Flowdock (Discontinued) Users API
  slug: flowdock-users-api
artifact_total: 59
asyncapis:
- description: 'Historical streaming surface for CA Flowdock. Long-lived HTTP connection that emitted real-time message events from one or more flows. Two content types were supported: a newline-delimited JSON stream'
  name: Flowdock Streaming API
  slug: flowdock-streaming-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flowdock Push Authentication API
  slug: open-flowdock-authentication-api
- collection_type: open
  name: Flowdock Push Authentication Chat API
  slug: open-flowdock-chat-api
- collection_type: open
  name: Flowdock Push Authentication Files API
  slug: open-flowdock-files-api
- collection_type: open
  name: Flowdock Push Authentication Flows API
  slug: open-flowdock-flows-api
- collection_type: open
  name: Flowdock Push Authentication Invitations API
  slug: open-flowdock-invitations-api
- collection_type: open
  name: Flowdock Push Authentication Messages API
  slug: open-flowdock-messages-api
- collection_type: open
  name: Flowdock Push Authentication Organizations API
  slug: open-flowdock-organizations-api
- collection_type: open
  name: Flowdock Push Authentication Private Conversations API
  slug: open-flowdock-private-conversations-api
- collection_type: open
  name: Flowdock Push Authentication Private Messages API
  slug: open-flowdock-private-messages-api
- collection_type: open
  name: Flowdock Push API
  slug: open-flowdock-push-api
- collection_type: open
  name: Flowdock REST API
  slug: open-flowdock-rest-api
- collection_type: open
  name: Flowdock Push Authentication SCIM API
  slug: open-flowdock-scim-api
- collection_type: open
  name: Flowdock Push Authentication Sources API
  slug: open-flowdock-sources-api
- collection_type: open
  name: Flowdock Push Authentication Team Inbox API
  slug: open-flowdock-team-inbox-api
- collection_type: open
  name: Flowdock Push Authentication Threads API
  slug: open-flowdock-threads-api
- collection_type: open
  name: Flowdock Push Authentication Users API
  slug: open-flowdock-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flowdock-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flowdock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flowdock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flowdock-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flowdock-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://web.archive.org/web/2022/https://www.flowdock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/flowdock/api-docs
- group: company
  title: ''
  type: Blog
  url: https://web.archive.org/web/2022/https://blog.flowdock.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/flowdock
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/flowdock
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/flowdock
- group: other
  title: Broadcom (via CA Technologies acquisition)
  type: ParentCompany
  url: https://www.broadcom.com
- group: other
  title: Flowdock end-of-life 2023-08-15
  type: SunsetNotice
  url: https://www.broadcom.com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/flowdock-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/flowdock-context.jsonld
- group: build
  title: Ruby gem (flowdock-api)
  type: SDKs
  url: https://github.com/flowdock/flowdock-api
- group: build
  title: Node.js client (node-flowdock)
  type: SDKs
  url: https://github.com/flowdock/node-flowdock
- group: build
  title: JavaScript text/tag parser (flowdock-text)
  type: SDKs
  url: https://github.com/flowdock/flowdock-text
- group: build
  title: Ruby text/tag parser (flowdock-text-rb)
  type: SDKs
  url: https://github.com/flowdock/flowdock-text-rb
- group: build
  title: markdown-it Flowdock
  type: SDKs
  url: https://github.com/flowdock/markdown-it-flowdock
- group: build
  title: Ruby OmniAuth strategy (omniauth-flowdock)
  type: SDKs
  url: https://github.com/flowdock/omniauth-flowdock
- group: build
  title: Hubot adapter for Flowdock
  type: SDKs
  url: https://github.com/flowdock/hubot-flowdock
- group: build
  title: Clojure (clj-flowdock)
  type: SDKs
  url: https://github.com/RallySoftware/clj-flowdock
- group: build
  title: Erlang (eflowdock)
  type: SDKs
  url: https://github.com/0xAX/eflowdock
- group: build
  title: Go (wm/go-flowdock)
  type: SDKs
  url: https://github.com/wm/go-flowdock
- group: build
  title: Go (njern/flowdock)
  type: SDKs
  url: https://github.com/njern/flowdock
- group: build
  title: Haskell (flowdock)
  type: SDKs
  url: https://hackage.haskell.org/package/flowdock
- group: build
  title: Haskell (flowdock-api)
  type: SDKs
  url: https://hackage.haskell.org/package/flowdock-api
- group: build
  title: PHP (mremi/Flowdock)
  type: SDKs
  url: https://github.com/mremi/Flowdock
- group: build
  title: PHP (flim/PHPFlow)
  type: SDKs
  url: https://github.com/flim/PHPFlow
- group: build
  title: Python (python-flowdock)
  type: SDKs
  url: https://bitbucket.org/j00bar/python-flowdock
- group: build
  title: Python (PyFlowdock)
  type: SDKs
  url: https://github.com/Aeron/PyFlowdock
- group: build
  title: R (flowdockr)
  type: SDKs
  url: https://github.com/hrbrmstr/flowdockr
- group: build
  title: Perl (Net::Flowdock)
  type: SDKs
  url: https://github.com/gphat/net-flowdock
- group: build
  title: Perl (p5-Flowdock)
  type: SDKs
  url: https://github.com/samvtran/p5-Flowdock
created: '2026-05-22'
description: CA Flowdock was a team chat and shared team-inbox product originally founded as Flowdock in Helsinki / Tampere, Finland (Nodeta Oy spin-off, ~2010), acquired by CA Technologies in 2013, and operated under Broadcom after Broadcom's 2018 acquisition of CA. The hosted service and all public APIs (REST, Push, Streaming, SCIM) were discontinued on August 15, 2023. Broadcom's sunset notice directed customers to Microsoft Teams or Slack as successor products. This profile is an archival record assembled from the public api-docs repository and archived snapshots of the developer portal.
examples:
- key_count: 3
  name: Flowdock Chat Push Request
  slug: flowdock-chat-push-request
- key_count: 5
  name: Flowdock Invitation Response
  slug: flowdock-invitation-response
- key_count: 11
  name: Flowdock Message Event Stream
  slug: flowdock-message-event-stream
- key_count: 6
  name: Flowdock Private Conversation Response
  slug: flowdock-private-conversation-response
- key_count: 1
  name: Flowdock Scim User Response
  slug: flowdock-scim-user-response
- key_count: 3
  name: Flowdock Send Message Request
  slug: flowdock-send-message-request
- key_count: 5
  name: Flowdock Team Inbox Push Request
  slug: flowdock-team-inbox-push-request
image: https://raw.githubusercontent.com/api-evangelist/flowdock/main/icon.png
json_schemas:
- name: Flowdock Flow
  property_count: 11
  slug: flowdock-flow
- name: Flowdock Invitation
  property_count: 5
  slug: flowdock-invitation
- name: Flowdock Message
  property_count: 14
  slug: flowdock-message
- name: Flowdock Organization
  property_count: 9
  slug: flowdock-organization
- name: Flowdock Source
  property_count: 8
  slug: flowdock-source
- name: Flowdock Thread
  property_count: 8
  slug: flowdock-thread
- name: Flowdock User
  property_count: 7
  slug: flowdock-user
json_structures:
- name: Flowdock Flow Structure
  property_count: 0
  slug: flowdock-flow-structure
- name: Flowdock Message Structure
  property_count: 0
  slug: flowdock-message-structure
- name: Flowdock Organization Structure
  property_count: 0
  slug: flowdock-organization-structure
jsonld:
- class_count: 34
  name: Flowdock Context
  property_count: 0
  slug: flowdock-context
layout: provider
modified: '2026-08-21'
name: Flowdock (Discontinued)
nav: Providers
network: true
overview: 'Flowdock (Discontinued) publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Flowdock Streaming API, Flowdock SCIM Provisioning API, Authentication API, and 12 more. Tagged areas include Team Chat, Team Inbox, Collaboration, Real-Time Messaging, and Integration.


  The Flowdock (Discontinued) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Flowdock (Discontinued)''s developer surface includes authentication, developer portal, documentation, engineering blog, GitHub presence, and 30 more developer resources.'
random_paper: 17
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Flowdock (Discontinued) API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: flowdock-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Flowdock (Discontinued) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: flowdock-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Flowdock (Discontinued) API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 5
  slug: flowdock-rules
scopes:
- name: Flowdock Scopes
  scope_count: 3
  slug: flowdock-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 30.5
  delta: 2.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 37.1
    developer_ergonomics: 51.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flowdock/refs/heads/main/screenshots/flowdock-2026-06-20T181333.png
security:
- kind: authentication
  name: Flowdock Authentication
  slug: flowdock-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Flowdock Domain Security
  slug: flowdock-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Flowdock Vulnerability Disclosure
  slug: flowdock-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flowdock
tags:
- Team Chat
- Team Inbox
- Collaboration
- Real-Time Messaging
- Integration
- Discontinued
website: https://web.archive.org/web/2022/https://www.flowdock.com/
---
