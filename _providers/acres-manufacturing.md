---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-07'
api_count: 2
apis:
- description: 'WebSocket streaming API onto the Foundation event bus. Two channels are documented: a real-time event streamer that pushes every event as it is collected from the floor (backed by a rolling cache of u'
  name: Foundation Event Replay API
  slug: foundation-event-replay-api
- description: First-party Bluetooth Low Energy SDK, published for iOS (Swift package) and Android (Kotlin), that lets a technology partner's mobile app talk directly to Acres BLE hardware on the casino floor. Two c
  name: AcresBLE SDK (Bluetooth Low Energy)
  slug: acresble-sdk-bluetooth-low-energy
artifact_total: 7
asyncapis:
- description: ''
  name: Acres Manufacturing Foundation Events
  slug: acres-manufacturing-foundation-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acres-manufacturing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acresmanufacturing.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/acres4/foundation-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/acres4/foundation-documentation/blob/master/apis/event/1.4/usage.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acres4
- group: company
  title: ''
  type: Blog
  url: https://acresmanufacturing.com/blog/
- group: operate
  title: ''
  type: FAQ
  url: https://acresmanufacturing.com/faq/
- group: operate
  title: ''
  type: Contact
  url: https://acresmanufacturing.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acresmanufacturing.com/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/acres-manufacturing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/acres-manufacturing-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acres-manufacturing-foundation-events.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acres-manufacturing-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acres-manufacturing-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acres-manufacturing-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acres-manufacturing-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acres-manufacturing-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acres-manufacturing-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acres-manufacturing-llms.txt
created: '2026-09-06'
description: 'Acres Manufacturing Company (also trading as Acres 4.0), of Las Vegas, Nevada, builds Foundation — a casino management system that connects directly to a slot machine''s SAS port and streams every gaming-floor event in real time. Foundation carries the operator''s cashless, bonusing, ticketing, loyalty and analytics products (FoundationHQ, Cashless Casino, Player Budget, Achievement Bonusing, Ticket In Bonus Out, Video Poker Analyzer, Guardian and Kai), and it is sold as an open platform: Acres publishes a Foundation App Store and gives third-party developers an event API onto the same floor data its own applications consume. The public developer surface is the Foundation Event Replay API — real-time and historical WebSocket streams of SAS 6.02 exception events, meter movements, machine info and player-card events, documented per version in the company''s own acres4 GitHub organization — plus the AcresBLE iOS and Android SDKs, which let a partner mobile app card a player in
  and fund or cash out a slot or table over Bluetooth Low Energy. Foundation communication is TLS 1.3 and Acres states its APIs require mTLS for authentication.'
image: https://acresmanufacturing.com/wp-content/uploads/2022/02/cropped-Acres_Submark_Gradient-192x192.png
layout: provider
modified: '2026-09-06'
name: Acres Manufacturing
nav: Providers
network: true
overview: 'Acres Manufacturing publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Casino Gaming, Casino Management System, Gaming Technology, Slot Machines, and Cashless Payments.


  The Acres Manufacturing catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acres Manufacturing''s developer surface includes documentation, API reference, engineering blog, FAQ, authentication, and 14 more developer resources.'
plans:
- name: Acres Manufacturing Plans Pricing
  plan_count: 0
  slug: acres-manufacturing-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Acres Manufacturing Rate Limits
  slug: acres-manufacturing-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 37.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acres Manufacturing Authentication
  slug: acres-manufacturing-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Acres Manufacturing Domain Security
  slug: acres-manufacturing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acres-manufacturing
tags:
- Casino Gaming
- Casino Management System
- Gaming Technology
- Slot Machines
- Cashless Payments
- Real-Time Data
- Event Streaming
- WebSocket
- Bluetooth Low Energy
- Loyalty and Bonusing
- Hospitality
website: https://acresmanufacturing.com
---
