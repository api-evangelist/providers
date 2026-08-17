---
access_model:
  confidence: medium
  label: Self-serve signup, API gated to paid tiers
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - authentication
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Manychat Agentic Access
  operation_count: 35
  slug: manychat-agentic-access
  summary_line: 35 operations · 22 acting
api_count: 5
apis:
- description: REST API for managing subscribers, custom fields, tags, bot fields, flows, and sending messages in ManyChat across Instagram, Messenger, WhatsApp and SMS. 35 operations across four tags. Authenticatio
  name: ManyChat REST API
  slug: rest-api
- description: 'Page-level configuration for a connected ManyChat page: connected page info, tags, typed custom user field definitions, global bot fields, automations (flows) and folders, growth tools and One-Time No'
  name: ManyChat Page API
  slug: manychat-page-api
- description: White-label profile and template management. A single operation that generates a single-use install link for a ManyChat template, served from its own Swagger document at api.manychat.com/swagger/compi
  name: ManyChat Profile API
  slug: manychat-profile-api
- description: 'Send Dynamic Block content and trigger automations for a subscriber across Messenger, Instagram and WhatsApp. 3 operations. This is the surface governed by Meta policy rather than by ManyChat: outside'
  name: ManyChat Sending API
  slug: manychat-sending-api
- description: Look up, search, create, update, tag and set custom field values on subscribers. 15 operations. A subscriber carries per-channel identity fields for Messenger, Instagram, WhatsApp, email and SMS on on
  name: ManyChat Subscriber API
  slug: manychat-subscriber-api
artifact_total: 18
asyncapis:
- description: ''
  name: Manychat Dynamic Block Webhooks
  slug: manychat-dynamic-block-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ManyChat Page API
  slug: open-manychat-page-api
- collection_type: open
  name: ManyChat Profile API
  slug: open-manychat-profile-api
- collection_type: open
  name: ManyChat Sending API
  slug: open-manychat-sending-api
- collection_type: open
  name: ManyChat Subscriber API
  slug: open-manychat-subscriber-api
- collection_type: open
  name: ManyChat API
  slug: open-manychat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/manychat-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/manychat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://manychat.com/security/vulnerability
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manychat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/manychat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/manychat-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/manychat-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/manychat-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/manychat-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/manychat-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/manychat-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/manychat-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.manychat.com
- group: build
  title: ''
  type: Packages
  url: packages/manychat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/manychat-packages.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/manychat-dynamic-block-vocabulary.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/manychat-dynamic-block-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/manychat-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/manychat-well-known.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/manychat-mcp.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manychat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manychat
- group: company
  title: ''
  type: Website
  url: https://manychat.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.manychat.com/swagger
- group: docs
  title: ''
  type: APIReference
  url: https://api.manychat.com/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://help.manychat.com/hc/en-us/articles/14281252007580-Dev-Tools-Basics
- group: operate
  title: ''
  type: Support
  url: https://help.manychat.com
- group: operate
  title: ''
  type: Help Center
  url: https://help.manychat.com
- group: operate
  title: ''
  type: Community
  url: https://community.manychat.com
- group: commercial
  title: ''
  type: Pricing
  url: https://manychat.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://manychat.com/signup
created: '2026-05-11'
description: 'ManyChat is a chat-marketing platform that lets businesses build automated conversations and marketing flows across Instagram Direct Messages, Facebook Messenger, WhatsApp, Telegram, TikTok and SMS. It provides a visual flow builder, audience segmentation, broadcasts, growth tools and integrations with ecommerce and CRM systems to drive engagement, lead capture and sales. The public ManyChat REST API is a page-scoped surface of 35 operations covering subscribers, tags, typed custom fields, page-level bot fields, automations and sending, published as OpenAPI 3.0 and served through an interactive Swagger console at api.manychat.com/swagger. Authentication is a per-page API key sent as an Authorization Bearer token in the form page-id:api-key; there is no OAuth, no scopes and no account-wide credential. ManyChat''s only asynchronous surface runs outbound: the External Request flow step calls a partner endpoint and expects a Dynamic Block v2 JSON response back, so the integrator
  is the webhook receiver rather than ManyChat pushing events.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manychat.png
layout: provider
modified: '2026-08-13'
name: ManyChat
nav: Providers
network: true
overview: 'ManyChat publishes 5 APIs on the [APIs.io](https://apis.io/) network, including REST API, Page API, Profile API, and 2 more. Tagged areas include Chat Marketing, Messenger Marketing, Conversational Commerce, Marketing Automation, and Instagram.


  The ManyChat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ManyChat''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Manychat Plans Pricing
  plan_count: 0
  slug: manychat-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 35
  name: Manychat Rate Limits
  slug: manychat-rate-limits
score:
  band: developing
  composite: 51.2
  delta: 19.8
  facets:
    commercial_clarity: 23.7
    contract_quality: 71.3
    developer_ergonomics: 54.3
    discoverability: 81.5
    governance: 31.3
    operational_transparency: 71.1
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/manychat/refs/heads/main/screenshots/manychat-2026-06-20T184935.png
security:
- kind: authentication
  name: Manychat Authentication
  slug: manychat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Manychat Domain Security
  slug: manychat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Manychat Vulnerability Disclosure
  slug: manychat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: manychat
tags:
- Chat Marketing
- Messenger Marketing
- Conversational Commerce
- Marketing Automation
- Instagram
- WhatsApp
- Facebook Messenger
- SMS
- Chatbots
- Customer Engagement
- Automation
website: https://manychat.com
---
