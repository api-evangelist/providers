---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rainbow Agentic Access
  operation_count: 16
  slug: rainbow-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 3
apis:
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: Register and manage developer applications
  name: Rainbow Applications API
  slug: rainbow-applications-api
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: OAuth2 token management
  name: Rainbow Authentication API
  slug: rainbow-authentication-api
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: Manage group chat rooms (bubbles)
  name: Rainbow Bubbles API
  slug: rainbow-bubbles-api
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: Manage and search contacts
  name: Rainbow Contacts API
  slug: rainbow-contacts-api
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: Manage one-to-one and group conversations
  name: Rainbow Conversations API
  slug: rainbow-conversations-api
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: Send and receive chat messages
  name: Rainbow Messages API
  slug: rainbow-messages-api
- baseURL: https://openrainbow.com/api/rainbow
  baseurl_source: declared
  description: User profile and presence operations
  name: Rainbow Users API
  slug: rainbow-users-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rainbow Application Portal API
  slug: open-rainbow-application
- collection_type: open
  name: Rainbow Application Portal Applications API
  slug: open-rainbow-applications-api
- collection_type: open
  name: Rainbow Application Portal Applications Authentication API
  slug: open-rainbow-authentication-api
- collection_type: open
  name: Rainbow Application Portal Applications Bubbles API
  slug: open-rainbow-bubbles-api
- collection_type: open
  name: Rainbow Application Portal Applications Contacts API
  slug: open-rainbow-contacts-api
- collection_type: open
  name: Rainbow Contacts API
  slug: open-rainbow-contacts
- collection_type: open
  name: Rainbow Application Portal Applications Conversations API
  slug: open-rainbow-conversations-api
- collection_type: open
  name: Rainbow Application Portal Applications Messages API
  slug: open-rainbow-messages-api
- collection_type: open
  name: Rainbow Messaging API
  slug: open-rainbow-messaging
- collection_type: open
  name: Rainbow Application Portal Applications Users API
  slug: open-rainbow-users-api
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
random_paper: 19
rate_limits:
- limit_count: 1
  name: Rainbow Rate Limits
  slug: rainbow-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rainbow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rainbow-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Rainbow API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: rainbow-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 67.5
    catalog_earned_first_party: 0.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 64.4
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 39.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
