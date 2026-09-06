---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Sendbird Agentic Access
  operation_count: 13
  slug: sendbird-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- description: The Sendbird Calls API provides voice and video calling capabilities, enabling real-time one-on-one and group calls within applications.
  name: Sendbird Calls API
  slug: sendbird-calls-api
- description: The Sendbird Business Messaging API enables omnichannel customer engagement through SMS, WhatsApp, and other messaging channels, supporting customer support and marketing use cases.
  name: Sendbird Business Messaging API
  slug: sendbird-business-messaging-api
- description: The Sendbird AI Chatbot API enables building and deploying AI-powered chatbots within chat applications, supporting automated customer support and conversational AI experiences.
  name: Sendbird AI Chatbot API
  slug: sendbird-ai-chatbot-api
- baseURL: https://api-{application_id}.sendbird.com/v3
  baseurl_source: declared
  description: Operations for managing group and open channels.
  name: Sendbird Channels API
  slug: sendbird-channels-api
- baseURL: https://api-{application_id}.sendbird.com/v3
  baseurl_source: declared
  description: Operations for sending and managing messages.
  name: Sendbird Messages API
  slug: sendbird-messages-api
- baseURL: https://api-{application_id}.sendbird.com/v3
  baseurl_source: declared
  description: Operations for content moderation and user management.
  name: Sendbird Moderation API
  slug: sendbird-moderation-api
- baseURL: https://api-{application_id}.sendbird.com/v3
  baseurl_source: declared
  description: Operations for managing Sendbird users.
  name: Sendbird Users API
  slug: sendbird-users-api
arazzos:
- description: Confirm a channel, recreate it as distinct with an expanded member set, and notify.
  name: Sendbird Add Members to an Existing Channel
  slug: sendbird-add-members-to-existing-channel-workflow
- description: Read a channel's recent messages for archival, then delete the channel.
  name: Sendbird Archive and Delete a Channel
  slug: sendbird-archive-and-delete-channel-workflow
- description: List channels for a member, then read details and recent messages for one.
  name: Sendbird Audit a Channel and Its Recent Activity
  slug: sendbird-audit-channel-membership-workflow
- description: Confirm a user and channel exist, then ban the user from the channel.
  name: Sendbird Ban a User from a Channel
  slug: sendbird-ban-user-from-channel-workflow
- description: Create a group channel with a member set and immediately broadcast a message.
  name: Sendbird Create a Channel and Broadcast a Message
  slug: sendbird-create-channel-and-broadcast-workflow
- description: Confirm a user exists, then delete the user account from the application.
  name: Sendbird Deactivate and Clean Up a User
  slug: sendbird-deactivate-user-cleanup-workflow
- description: Create a distinct 1:1 channel for two users and send the first message.
  name: Sendbird Open a Direct Message Between Two Users
  slug: sendbird-direct-message-between-users-workflow
- description: Look up a user by ID and create them only if they do not already exist.
  name: Sendbird Find or Create a User
  slug: sendbird-find-or-create-user-workflow
- description: Create a user with an issued access token and send them a private channel greeting.
  name: Sendbird Issue an Access Token and Greet the User
  slug: sendbird-issue-access-token-and-greet-workflow
- description: Read a channel's latest message, identify its author, and mute that user.
  name: Sendbird Moderate the Author of the Latest Channel Message
  slug: sendbird-moderate-channel-message-author-workflow
- description: Mute a user in a channel and post an admin notice explaining the action.
  name: Sendbird Mute a User and Post a Moderation Notice
  slug: sendbird-mute-then-warn-user-workflow
- description: Create a user, open a group channel for them, and post a welcome message.
  name: Sendbird Onboard a User and Start a Group Channel
  slug: sendbird-onboard-user-and-start-channel-workflow
- description: Update a user's nickname and announce the change in a channel.
  name: Sendbird Rename a User and Notify a Channel
  slug: sendbird-rename-user-and-notify-channel-workflow
- description: Read the most recent messages in a channel and post a reply.
  name: Sendbird Reply to the Latest Message in a Channel
  slug: sendbird-reply-to-latest-message-workflow
- description: Fetch a user, then merge nickname, profile, and metadata updates onto them.
  name: Sendbird Update User Metadata
  slug: sendbird-update-user-metadata-workflow
artifact_total: 47
collections:
- collection_type: postman
  name: Sendbird Platform API
  slug: postman-sendbird-platform
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sendbird Platform Channels API
  slug: open-sendbird-channels-api
- collection_type: open
  name: Sendbird Platform Channels Messages API
  slug: open-sendbird-messages-api
- collection_type: open
  name: Sendbird Platform Channels Moderation API
  slug: open-sendbird-moderation-api
- collection_type: open
  name: Sendbird Platform API
  slug: open-sendbird-platform
- collection_type: open
  name: Sendbird Platform Channels Users API
  slug: open-sendbird-users-api
common:
- group: build
  title: ''
  type: Packages
  url: packages/sendbird-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sendbird-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sendbird-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendbird-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sendbird-platform-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/sendbird-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendbird-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendbird-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendbird-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sendbird-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/sendbird-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendbird-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendbird-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sendbird-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sendbird-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendbird-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendbird-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendbird/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-add-members-to-existing-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-archive-and-delete-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-audit-channel-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-ban-user-from-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-create-channel-and-broadcast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-deactivate-user-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-direct-message-between-users-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-find-or-create-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-issue-access-token-and-greet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-moderate-channel-message-author-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-mute-then-warn-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-onboard-user-and-start-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-rename-user-and-notify-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-reply-to-latest-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendbird-update-user-metadata-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendbird
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendbird
- group: start
  title: ''
  type: Portal
  url: https://sendbird.com/docs/
- group: auth
  title: ''
  type: Authentication
  url: https://sendbird.com/docs/chat/platform-api/v3/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://sendbird.com/docs/chat/platform-api/v3/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://sendbird.com/docs/chat/platform-api/v3/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendbird.com/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendbird.com/
- group: operate
  title: ''
  type: Support
  url: https://sendbird.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://sendbird.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://sendbird.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendbird.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendbird.com/terms-of-service/
- group: company
  title: ''
  type: Website
  url: https://sendbird.com
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.sendbird.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/sendbird-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sendbird-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sendbird-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://sendbird.com/llms.txt
created: '2025-01-14'
description: Sendbird provides APIs and SDKs for in-app chat, voice, video, AI chatbots, and omnichannel business messaging. Used by over 4,000 companies to build real-time communication experiences for customer support, communities, and marketplace platforms.
examples:
- key_count: 6
  name: Sendbird Create User Example
  slug: sendbird-create-user-example
- key_count: 6
  name: Sendbird Send Message Example
  slug: sendbird-send-message-example
finops:
- name: Sendbird Finops
  service_category: Communications PaaS
  slug: sendbird-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Sendbird in-app messaging and chat platform. The schema is derived from the [Sendbird Platform API](https://sendbird.com/docs/chat/platform-
  name: Sendbird GraphQL Schema
  slug: sendbird-graphql
image: https://sendbird.com/favicon.ico
json_schemas:
- name: Sendbird Group Channel
  property_count: 10
  slug: sendbird-group-channel
- name: Sendbird Message
  property_count: 10
  slug: sendbird-message
- name: Sendbird User
  property_count: 9
  slug: sendbird-user
json_structures:
- name: Sendbird User Structure
  property_count: 0
  slug: sendbird-user-structure
jsonld:
- class_count: 11
  name: Sendbird Context
  property_count: 11
  slug: sendbird-context
layout: provider
modified: '2026-06-20'
name: Sendbird
nav: Providers
network: true
overview: 'Sendbird publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Messages API, Moderation API, and 1 more.


  The Sendbird catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sendbird''s developer surface includes authentication, developer portal, changelog, support, pricing, engineering blog, and 46 more developer resources.'
plans:
- name: Sendbird Plans Pricing
  plan_count: 4
  slug: sendbird-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 13
  name: Sendbird Rate Limits
  slug: sendbird-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sendbird API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sendbird-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Sendbird API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: sendbird-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 33.3
    contract_quality: 70.8
    developer_ergonomics: 27.4
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 26.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendbird/refs/heads/main/screenshots/sendbird-2026-06-20T193652.png
security:
- kind: authentication
  name: Sendbird Authentication
  slug: sendbird-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sendbird Domain Security
  slug: sendbird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sendbird Vulnerability Disclosure
  slug: sendbird-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Sendbird Trust Center
  slug: sendbird-trust-center
  summary_line: SOC 2, ISO 27001
slug: sendbird
website: https://sendbird.com
---
