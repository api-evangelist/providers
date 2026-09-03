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
    agent_skills: derived
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Accounts API from LISNR — 1 operation(s) for accounts.
  name: LISNR Accounts API
  slug: lisnr-accounts-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The API Tokens API from LISNR — 2 operation(s) for api tokens.
  name: LISNR API Tokens API
  slug: lisnr-api-tokens-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Applications API from LISNR — 2 operation(s) for applications.
  name: LISNR Applications API
  slug: lisnr-applications-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Authentication API from LISNR — 5 operation(s) for authentication.
  name: LISNR Authentication API
  slug: lisnr-authentication-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Billing API from LISNR — 1 operation(s) for billing.
  name: LISNR Billing API
  slug: lisnr-billing-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Notifications API from LISNR — 2 operation(s) for notifications.
  name: LISNR Notifications API
  slug: lisnr-notifications-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The SDK Releases API from LISNR — 1 operation(s) for sdk releases.
  name: LISNR SDK Releases API
  slug: lisnr-sdk-releases-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The SDK Tokens API from LISNR — 2 operation(s) for sdk tokens.
  name: LISNR SDK Tokens API
  slug: lisnr-sdk-tokens-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Tones Service API Reference API from LISNR — 1 operation(s) for tones service api reference.
  name: LISNR Tones Service API Reference API
  slug: lisnr-tones-service-api-reference-api
- baseURL: https://tones.lisnr.com/
  baseurl_source: declared
  description: The Users API from LISNR — 3 operation(s) for users.
  name: LISNR Users API
  slug: lisnr-users-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LISNR Portal API (observed) Accounts API
  slug: open-lisnr-accounts-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts API Tokens API
  slug: open-lisnr-api-tokens-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts Applications API
  slug: open-lisnr-applications-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts Authentication API
  slug: open-lisnr-authentication-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts Billing API
  slug: open-lisnr-billing-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts Notifications API
  slug: open-lisnr-notifications-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts SDK Releases API
  slug: open-lisnr-sdk-releases-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts SDK Tokens API
  slug: open-lisnr-sdk-tokens-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts Tones Service API Reference API
  slug: open-lisnr-tones-service-api-reference-api
- collection_type: open
  name: LISNR Portal API (observed) Accounts Users API
  slug: open-lisnr-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/lisnr-portal-overlay.yaml
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
  name: LISNR MCP Server
  slug: lisnr-mcp-server
modified: '2026-07-19'
name: LISNR
nav: Providers
network: true
overview: 'LISNR publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Tokens API, Applications API, and 7 more. Tagged areas include Company, Ultrasonic, Data Over Audio, Proximity, and Contactless Payments.


  LISNR''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 15.1
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
