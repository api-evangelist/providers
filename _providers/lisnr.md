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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: The Accounts API from LISNR — 1 operation(s) for accounts.
  name: LISNR Accounts API
  slug: lisnr-accounts-api
- description: The API Tokens API from LISNR — 2 operation(s) for api tokens.
  name: LISNR API Tokens API
  slug: lisnr-api-tokens-api
- description: The Applications API from LISNR — 2 operation(s) for applications.
  name: LISNR Applications API
  slug: lisnr-applications-api
- description: The Authentication API from LISNR — 5 operation(s) for authentication.
  name: LISNR Authentication API
  slug: lisnr-authentication-api
- description: The Billing API from LISNR — 1 operation(s) for billing.
  name: LISNR Billing API
  slug: lisnr-billing-api
- description: The Notifications API from LISNR — 2 operation(s) for notifications.
  name: LISNR Notifications API
  slug: lisnr-notifications-api
- description: The SDK Releases API from LISNR — 1 operation(s) for sdk releases.
  name: LISNR SDK Releases API
  slug: lisnr-sdk-releases-api
- description: The SDK Tokens API from LISNR — 2 operation(s) for sdk tokens.
  name: LISNR SDK Tokens API
  slug: lisnr-sdk-tokens-api
- description: The Tones Service API Reference API from LISNR — 1 operation(s) for tones service api reference.
  name: LISNR Tones Service API Reference API
  slug: lisnr-tones-service-api-reference-api
- description: The Users API from LISNR — 3 operation(s) for users.
  name: LISNR Users API
  slug: lisnr-users-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://lisnr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.lisnr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.lisnr.com/developer-resources/
- group: docs
  title: ''
  type: APIReference
  url: https://portal.lisnr.com/assets/tones-docs/tones-docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.lisnr.com/help-center/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://lisnr1.atlassian.net/servicedesk/customer/portals
- group: operate
  title: ''
  type: HelpCenter
  url: https://portal.lisnr.com/help-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lisnr
- group: start
  title: ''
  type: SignUp
  url: https://portal.lisnr.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lisnr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lisnr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lisnr-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lisnr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lisnr-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/lisnr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lisnr-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lisnr-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lisnr-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lisnr-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/lisnr-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lisnr-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LISNR is a Cincinnati, Ohio company whose ultrasonic data-over-audio technology transmits data between devices using inaudible high-frequency tones instead of radio. Its Radius SDKs (Radius, Radius 3, Point, and the legacy and SDA product lines) embed a transmitter/receiver into iOS, Android, React Native, Linux and Windows applications so that a speaker and a microphone become a proximity data channel for contactless payment, identification, confirmation and device-pairing transactions. Developers work through the LISNR Portal, which issues per-application API tokens and SDK tokens, exposes SDK releases and sample projects, and provides a Tone Creator and a tone-speed calculator. The public Tones Service API generates a downloadable 24-bit audio tone (WAV or MP3) from a hexadecimal payload for a chosen tone profile, with optional AES-256 payload encryption and ToneLock pairing so that only matching receivers can demodulate the tone.
image: https://lh3.googleusercontent.com/v89HEtbE-zGOkBwCmWf7zbG9BBtS22tgXzNSgZG4F3fqv90KqLo0yWO5D1PFUxGG-VSIVNgoxsWEVLLjA-pkHA=w205
layout: provider
mcp_servers:
- description: ''
  name: lisnr-mcp.yml
  slug: lisnr-mcpyml
modified: '2026-07-19'
name: LISNR
nav: Providers
network: true
overview: 'LISNR publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Tokens API, Applications API, and 7 more. Tagged areas include Company, Ultrasonic, Data Over Audio, Proximity, and Contactless Payments.


  LISNR''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 40.4
  delta: -1.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 57.3
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 41.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lisnr/refs/heads/main/screenshots/lisnr-2026-07-25T225338.png
security:
- kind: authentication
  name: Lisnr Authentication
  slug: lisnr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lisnr Domain Security
  slug: lisnr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lisnr
tags:
- Company
- Ultrasonic
- Data Over Audio
- Proximity
- Contactless Payments
- Device Pairing
- Identification
- Audio
- Internet of Things
- SDK
website: https://lisnr.com/
---
