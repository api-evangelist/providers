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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Talkjs Agentic Access
  operation_count: 23
  slug: talkjs-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- description: 'Server-to-server event delivery for message.sent, message.read, message.updated, message.deleted, user.created/updated, conversation.deleted, and notification lifecycle events, posted as JSON with an '
  name: TalkJS Webhooks API
  slug: talkjs-webhooks-api
- description: Create, update, list, and delete conversations.
  name: TalkJS Conversations API
  slug: talkjs-conversations-api
- description: Import messages with original timestamps.
  name: TalkJS Import API
  slug: talkjs-import-api
- description: Send, list, fetch, edit, delete messages, and manage reactions.
  name: TalkJS Messages API
  slug: talkjs-messages-api
- description: Add, update, and remove conversation participants.
  name: TalkJS Participants API
  slug: talkjs-participants-api
- description: Create, update, retrieve, and list users; manage presence.
  name: TalkJS Users API
  slug: talkjs-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TalkJS REST Conversations API
  slug: open-talkjs-conversations-api
- collection_type: open
  name: TalkJS REST Conversations Import API
  slug: open-talkjs-import-api
- collection_type: open
  name: TalkJS REST Conversations Messages API
  slug: open-talkjs-messages-api
- collection_type: open
  name: TalkJS REST Conversations Participants API
  slug: open-talkjs-participants-api
- collection_type: open
  name: TalkJS REST Conversations Users API
  slug: open-talkjs-users-api
- collection_type: open
  name: TalkJS REST API
  slug: open-talkjs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talkjs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/talkjs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/talkjs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talkjs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/talkjs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/talkjs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talkjs
- group: company
  title: ''
  type: Website
  url: https://talkjs.com
- group: docs
  title: ''
  type: Documentation
  url: https://talkjs.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/talkjs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talkjs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talkjs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://talkjs.com/resources/rss/
created: '2026-06-20'
description: TalkJS is a chat API and SDK for adding messaging to web and mobile apps. It pairs a customizable pre-built chat UI (the TalkJS JavaScript SDK and Chat UI) with a server-side REST API at https://api.talkjs.com/v1/{appId} for managing users, conversations, participants, and messages, importing existing chat history, and receiving events via webhooks.
finops:
- name: Talkjs Finops
  service_category: Developer Tools and Communication
  slug: talkjs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talkjs.png
layout: provider
modified: '2026-06-20'
name: TalkJS
nav: Providers
network: true
overview: 'TalkJS publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Import API, Messages API, and 2 more. Tagged areas include Chat, Messaging, Communications, SDK, and Webhook.


  TalkJS''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Talkjs Plans Pricing
  plan_count: 3
  slug: talkjs-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Talkjs Rate Limits
  slug: talkjs-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talkjs/refs/heads/main/screenshots/talkjs-2026-06-20T194905.png
security:
- kind: authentication
  name: Talkjs Authentication
  slug: talkjs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Talkjs Domain Security
  slug: talkjs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Talkjs Vulnerability Disclosure
  slug: talkjs-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Talkjs Trust Center
  slug: talkjs-trust-center
  summary_line: ISO 27001, GDPR
slug: talkjs
tags:
- Chat
- Messaging
- Communications
- SDK
- Webhook
website: https://talkjs.com
---
