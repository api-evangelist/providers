---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rainbow Agentic Access
  operation_count: 16
  slug: rainbow-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 7
apis:
- description: Register and manage developer applications
  name: Rainbow Applications API
  slug: rainbow-applications-api
- description: OAuth2 token management
  name: Rainbow Authentication API
  slug: rainbow-authentication-api
- description: Manage group chat rooms (bubbles)
  name: Rainbow Bubbles API
  slug: rainbow-bubbles-api
- description: Manage and search contacts
  name: Rainbow Contacts API
  slug: rainbow-contacts-api
- description: Manage one-to-one and group conversations
  name: Rainbow Conversations API
  slug: rainbow-conversations-api
- description: Send and receive chat messages
  name: Rainbow Messages API
  slug: rainbow-messages-api
- description: User profile and presence operations
  name: Rainbow Users API
  slug: rainbow-users-api
artifact_total: 26
collections:
- collection_type: open
  name: Rainbow Application Portal API
  slug: open-rainbow-application
- collection_type: open
  name: Rainbow Contacts API
  slug: open-rainbow-contacts
- collection_type: open
  name: Rainbow Messaging API
  slug: open-rainbow-messaging
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rainbow-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rainbow-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rainbow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rainbow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openrainbow
- group: company
  title: ''
  type: Website
  url: https://www.openrainbow.com
- group: other
  title: ''
  type: Developer
  url: https://developers.openrainbow.com/
- group: start
  title: ''
  type: Signup
  url: https://hub.openrainbow.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Rainbow-CPaaS
- group: build
  title: ''
  type: SDKNode
  url: https://github.com/Rainbow-CPaaS/Rainbow-Node-SDK
- group: build
  title: ''
  type: SDKIOS
  url: https://github.com/Rainbow-CPaaS/Rainbow-iOS-SDK
- group: build
  title: ''
  type: SDKCS
  url: https://github.com/Rainbow-CPaaS/Rainbow-CSharp-SDK-Samples
- group: build
  title: ''
  type: CLI
  url: https://github.com/Rainbow-CPaaS/Rainbow-CLI-SDK
- group: design
  title: ''
  type: SpectralRules
  url: rules/rainbow-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rainbow-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rainbow-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.openrainbow.com/llms.txt
created: '2025-02-06'
description: Rainbow is a CPaaS platform from Alcatel-Lucent Enterprise (ALE) that lets developers enrich applications with chat, group chat, voice, video, file sharing, and telephony PBX features through more than 200 APIs, REST interfaces, and multi-language SDKs including Node.js, C#, iOS, and Android.
examples:
- key_count: 2
  name: Rainbow Get Oauth Token Example
  slug: rainbow-get-oauth-token-example
- key_count: 2
  name: Rainbow Search Contacts Example
  slug: rainbow-search-contacts-example
- key_count: 2
  name: Rainbow Send Message Example
  slug: rainbow-send-message-example
finops:
- name: Rainbow Finops
  service_category: Communications
  slug: rainbow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rainbow.png
json_schemas:
- name: Rainbow Contact
  property_count: 9
  slug: rainbow-contact
- name: Rainbow Message
  property_count: 7
  slug: rainbow-message
json_structures:
- name: Rainbow Message Structure
  property_count: 0
  slug: rainbow-message-structure
jsonld:
- class_count: 18
  name: Rainbow Context
  property_count: 10
  slug: rainbow-context
layout: provider
modified: '2026-05-19'
name: Rainbow
nav: Providers
network: true
overview: 'Rainbow publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Bubbles API, and 4 more. Tagged areas include Communications, CPaaS, Chat, Voice, and Video.


  The Rainbow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rainbow''s developer surface includes authentication, signup flow, GitHub presence, CLI, and 13 more developer resources.'
plans:
- name: Rainbow Plans Pricing
  plan_count: 1
  slug: rainbow-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 1
  name: Rainbow Rate Limits
  slug: rainbow-rate-limits
rules:
- name: Rainbow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rainbow-jsonschema-spectral-rules
- name: Rainbow API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: rainbow-rules
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 72.1
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rainbow/refs/heads/main/screenshots/rainbow-2026-06-20T192535.png
security:
- kind: authentication
  name: Rainbow Authentication
  slug: rainbow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rainbow Domain Security
  slug: rainbow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rainbow Trust Center
  slug: rainbow-trust-center
  summary_line: ISO 27001, HIPAA
slug: rainbow
tags:
- Communications
- CPaaS
- Chat
- Voice
- Video
- Telephony
- Messaging
- Collaboration
- Unified Communications
website: https://www.openrainbow.com
---
