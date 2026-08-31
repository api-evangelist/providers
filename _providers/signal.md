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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Signal Agentic Access
  operation_count: 18
  slug: signal-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 1
apis:
- description: 'The Signal Protocol Specifications define the core cryptographic protocols that underpin Signal''s end-to-end encrypted messaging. These include the X3DH (Extended Triple Diffie-Hellman) key agreement '
  name: Signal Protocol Specifications
  slug: signal-protocol-specifications
- description: The libsignal SDK provides platform-agnostic APIs used by the official Signal clients and server. It implements the Signal Protocol including the Double Ratchet algorithm, as well as other cryptograph
  name: Signal libsignal SDK
  slug: signal-libsignal-sdk
- description: Signal-Android is the open-source Android client for the Signal encrypted messaging platform. It provides the full messaging experience including end-to-end encrypted text messages, voice calls, video
  name: Signal Android SDK
  slug: signal-android-sdk
- description: 'Signal-iOS is the open-source iOS client for the Signal encrypted messaging platform. It delivers end-to-end encrypted messaging, voice calls, video calls, and group communications on iPhone and iPad '
  name: Signal iOS SDK
  slug: signal-ios-sdk
- description: 'Signal-Desktop is the open-source desktop client for the Signal encrypted messaging platform, built with Electron and TypeScript. It provides end-to-end encrypted messaging, voice calls, video calls, '
  name: Signal Desktop SDK
  slug: signal-desktop-sdk
- description: Account management endpoints for configuring account settings, managing capabilities, and account lifecycle operations.
  name: Signal Accounts API
  slug: signal-accounts-api
- description: Attachment handling endpoints for uploading and downloading media files associated with messages.
  name: Signal Attachments API
  slug: signal-attachments-api
- description: Certificate endpoints for retrieving delivery certificates used in sealed sender message delivery.
  name: Signal Certificates API
  slug: signal-certificates-api
- description: Device management endpoints for linking, unlinking, and managing devices associated with a Signal account.
  name: Signal Devices API
  slug: signal-devices-api
- description: Pre-key bundle management endpoints for uploading and retrieving public key material used in the Signal Protocol key exchange.
  name: Signal Keys API
  slug: signal-keys-api
- description: Message sending and receiving endpoints for delivering encrypted messages between Signal users.
  name: Signal Messages API
  slug: signal-messages-api
- description: Profile management endpoints for setting and retrieving user profile information including names, avatars, and capabilities.
  name: Signal Profiles API
  slug: signal-profiles-api
- description: Account registration endpoints for creating new Signal accounts via phone number verification.
  name: Signal Registration API
  slug: signal-registration-api
- description: Sticker pack management endpoints for uploading and retrieving sticker packs.
  name: Signal Stickers API
  slug: signal-stickers-api
artifact_total: 41
asyncapis:
- description: 'The Signal Server real-time messaging interface provides WebSocket connections for persistent, bidirectional communication between Signal clients and the server. When a client has an active WebSocket '
  name: Signal Server Real-Time Events
  slug: signal-server-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Signal Server Accounts API
  slug: open-signal-accounts-api
- collection_type: open
  name: Signal Server Accounts Attachments API
  slug: open-signal-attachments-api
- collection_type: open
  name: Signal Server Accounts Certificates API
  slug: open-signal-certificates-api
- collection_type: open
  name: Signal Server Accounts Devices API
  slug: open-signal-devices-api
- collection_type: open
  name: Signal Server Accounts Keys API
  slug: open-signal-keys-api
- collection_type: open
  name: Signal Server Accounts Messages API
  slug: open-signal-messages-api
- collection_type: open
  name: Signal Server Accounts Profiles API
  slug: open-signal-profiles-api
- collection_type: open
  name: Signal Server Accounts Registration API
  slug: open-signal-registration-api
- collection_type: open
  name: Signal Server API
  slug: open-signal-server
- collection_type: open
  name: Signal Server Accounts Stickers API
  slug: open-signal-stickers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signal-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signal-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signal-messenger
- group: company
  title: ''
  type: Website
  url: https://signal.org/
- group: docs
  title: ''
  type: Documentation
  url: https://signal.org/docs/
- group: company
  title: ''
  type: Blog
  url: https://signal.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.signal.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signal.org/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signal.org/legal/#privacy-policy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/signalapp
created: '2026-03-20'
description: Signal is a privacy-focused messaging platform that provides end-to-end encrypted communication through open-source applications on mobile and desktop. Their developer ecosystem centers around the open-source Signal Protocol, client SDKs, and server infrastructure, enabling developers to study, audit, and integrate secure messaging capabilities. The Signal Protocol is the most widely deployed end-to-end encryption protocol in the world, used by Signal, WhatsApp, Google Messages, and other platforms.
examples:
- key_count: 2
  name: Signal Get Account Identity Example
  slug: signal-get-account-identity-example
- key_count: 2
  name: Signal List Devices Example
  slug: signal-list-devices-example
finops:
- name: Signal Finops
  service_category: Messaging (Non-Commercial)
  slug: signal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signal.png
json_schemas:
- name: Signal Protocol Entities
  property_count: 0
  slug: signal-protocol-entities
json_structures:
- name: Signal Server Structure
  property_count: 0
  slug: signal-server-structure
jsonld:
- class_count: 0
  name: Signal Context
  property_count: 10
  slug: signal-context
layout: provider
modified: '2026-05-19'
name: Signal
nav: Providers
network: true
overview: 'Signal publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Certificates API, and 6 more. Tagged areas include Encryption, Messaging, Security, Cryptography, and Open-Source.


  The Signal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Signal''s developer surface includes authentication, documentation, engineering blog, support, GitHub presence, and 7 more developer resources.'
plans:
- name: Signal Plans Pricing
  plan_count: 1
  slug: signal-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Signal Rate Limits
  slug: signal-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Signal API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: signal-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Signal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: signal-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Signal API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 4
  slug: signal-rules
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 52.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 75.7
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signal/refs/heads/main/screenshots/signal-2026-06-20T193905.png
security:
- kind: authentication
  name: Signal Authentication
  slug: signal-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Signal Domain Security
  slug: signal-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Signal Vulnerability Disclosure
  slug: signal-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: signal
tags:
- Encryption
- Messaging
- Security
- Cryptography
- Open-Source
- Privacy
website: https://signal.org/
---
