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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Chat Integrations For Workspace Agentic Access
  operation_count: 10
  slug: google-chat-integrations-for-workspace-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 8
apis:
- description: REST API for sending and managing messages, spaces, members, reactions, attachments, custom emoji, user notification settings, and read states in Google Chat. Authentication uses OAuth 2.0 user creden
  name: Google Chat API
  slug: chat-api
- description: The CustomEmojis API from Google Chat Integrations for Workspace — 1 operation(s) for customemojis.
  name: Google Chat Integrations for Workspace CustomEmojis API
  slug: google-chat-integrations-for-workspace-customemojis-api
- description: The Google Chat API API from Google Chat Integrations for Workspace — 1 operation(s) for google chat api.
  name: Google Chat Integrations for Workspace Google Chat API API
  slug: google-chat-integrations-for-workspace-google-chat-api-api
- description: The Members API from Google Chat Integrations for Workspace — 1 operation(s) for members.
  name: Google Chat Integrations for Workspace Members API
  slug: google-chat-integrations-for-workspace-members-api
- description: The Message API from Google Chat Integrations for Workspace — 1 operation(s) for message.
  name: Google Chat Integrations for Workspace Message API
  slug: google-chat-integrations-for-workspace-message-api
- description: The Messages API from Google Chat Integrations for Workspace — 1 operation(s) for messages.
  name: Google Chat Integrations for Workspace Messages API
  slug: google-chat-integrations-for-workspace-messages-api
- description: The Reactions API from Google Chat Integrations for Workspace — 1 operation(s) for reactions.
  name: Google Chat Integrations for Workspace Reactions API
  slug: google-chat-integrations-for-workspace-reactions-api
- description: The Spaces API from Google Chat Integrations for Workspace — 1 operation(s) for spaces.
  name: Google Chat Integrations for Workspace Spaces API
  slug: google-chat-integrations-for-workspace-spaces-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Chat CustomEmojis API
  slug: open-google-chat-integrations-for-workspace-customemojis-api
- collection_type: open
  name: Google Chat CustomEmojis Google Chat API API
  slug: open-google-chat-integrations-for-workspace-google-chat-api-api
- collection_type: open
  name: Google Chat CustomEmojis Members API
  slug: open-google-chat-integrations-for-workspace-members-api
- collection_type: open
  name: Google Chat CustomEmojis Message API
  slug: open-google-chat-integrations-for-workspace-message-api
- collection_type: open
  name: Google Chat CustomEmojis Messages API
  slug: open-google-chat-integrations-for-workspace-messages-api
- collection_type: open
  name: Google Chat CustomEmojis Reactions API
  slug: open-google-chat-integrations-for-workspace-reactions-api
- collection_type: open
  name: Google Chat CustomEmojis Spaces API
  slug: open-google-chat-integrations-for-workspace-spaces-api
- collection_type: open
  name: Google Chat API
  slug: open-google-chat-integrations-for-workspace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-chat-integrations-for-workspace-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-chat-integrations-for-workspace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-chat-integrations-for-workspace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-chat-integrations-for-workspace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-chat-integrations-for-workspace-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: company
  title: ''
  type: Website
  url: https://workspace.google.com/products/chat/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/chat
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/workspace
- group: start
  title: ''
  type: Cloud Console
  url: https://console.cloud.google.com
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://workspace.google.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/chat
- group: company
  title: ''
  type: Blog
  url: https://developers.google.com/feeds/chat-release-notes.xml
created: '2026-05-11'
description: Google Chat is the messaging and collaboration platform built into Google Workspace, allowing teams to chat in direct messages, group conversations, and spaces with threaded discussions, file sharing, tasks, and Chat app integrations. The Google Chat REST API lets developers build Chat apps that send messages, manage spaces and members, post cards, handle slash commands, react to events, and integrate external services into Workspace conversations. Authentication uses OAuth 2.0 (user credentials for user-impersonating calls) or service-account credentials for app-bot calls.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-chat-integrations-for-workspace.png
layout: provider
modified: '2026-05-11'
name: Google Chat Integrations for Workspace
nav: Providers
network: true
overview: 'Google Chat Integrations for Workspace publishes 7 APIs on the [APIs.io](https://apis.io/) network, including CustomEmojis API, Google Chat API API, Members API, and 4 more. Tagged areas include Google Workspace, Team Chat, Messaging, Collaboration, and Chat Apps.


  Google Chat Integrations for Workspace''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 16
scopes:
- name: Google Chat Integrations For Workspace Scopes
  scope_count: 3
  slug: google-chat-integrations-for-workspace-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 32.8
  delta: 1.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-chat-integrations-for-workspace/refs/heads/main/screenshots/google-chat-integrations-for-workspace-2026-06-20T182041.png
security:
- kind: authentication
  name: Google Chat Integrations For Workspace Authentication
  slug: google-chat-integrations-for-workspace-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Chat Integrations For Workspace Domain Security
  slug: google-chat-integrations-for-workspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Chat Integrations For Workspace Vulnerability Disclosure
  slug: google-chat-integrations-for-workspace-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-chat-integrations-for-workspace
tags:
- Google Workspace
- Team Chat
- Messaging
- Collaboration
- Chat Apps
- Spaces
- Slash Commands
- Bots
website: https://workspace.google.com/products/chat/
---
