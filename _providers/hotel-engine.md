---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Hotel Engine Agentic Access
  operation_count: 11
  slug: hotel-engine-agentic-access
  summary_line: 11 operations · 10 acting
api_count: 4
apis:
- description: The CatalogService API from Engine — 1 operation(s) for catalogservice.
  name: Engine Catalog Service API
  slug: hotel-engine-catalogservice-api
- description: The ContentService API from Engine — 2 operation(s) for contentservice.
  name: Engine Content Service API
  slug: hotel-engine-contentservice-api
- description: The LodgingBookingService API from Engine — 5 operation(s) for lodgingbookingservice.
  name: Engine Lodging Booking Service API
  slug: hotel-engine-lodgingbookingservice-api
- description: The LodgingShoppingService API from Engine — 2 operation(s) for lodgingshoppingservice.
  name: Engine Lodging Shopping Service API
  slug: hotel-engine-lodgingshoppingservice-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.engine.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://omni.engine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://engine-public.github.io/engine-partner-api/
- group: docs
  title: ''
  type: APIReference
  url: https://engine-public.github.io/engine-partner-api/swagger-ui/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://engine-public.github.io/engine-partner-api/api/grpc/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://engine-public.github.io/engine-partner-api/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://engine-public.github.io/engine-partner-api/support.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.engine.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.engine.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/engine-public
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/engine-public/engine-partner-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.engine.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.engine.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engine.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engine.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/engine-public/engine-partner-api/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hotel-engine-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://engine-public.github.io/engine-partner-api/versioning.html#support-for-deprecated-versions
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hotel-engine-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.engine.com/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotel-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.engine.com/
- group: auth
  title: ''
  type: Compliance
  url: security/hotel-engine-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hotel-engine-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/hotel-engine-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hotel-engine-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hotel-engine-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hotel-engine-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hotel-engine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotel-engine-domain-security.yml
created: '2026-08-04'
description: 'Engine (formerly Hotel Engine, rebranded in 2024) is a Denver, Colorado business travel and spend platform for booking and managing lodging, flights, rental cars, group travel, and meeting and event spaces, with travel policy enforcement, trip approvals, consolidated DirectBill invoicing, and the Engine X charge card. Engine says it serves 25,000+ businesses and 1.2 million travelers with negotiated rates across 1,000,000+ hotel properties. Its API product is Omni — a partner-facing lodging inventory API offered over gRPC and HTTP/JSON, authenticated with mutual TLS, that covers property content, real-time rate shopping, booking, folio generation, and cancellation. Omni is protobuf-first: the proto contracts are published under Apache 2.0 on GitHub and the Swagger document, descriptor set, and JVM client bindings are generated from them and released per version.'
image: https://engine.com/_astro/engine-og-default.BAjJjAAC.png
layout: provider
modified: '2026-08-04'
name: Engine
nav: Providers
network: true
overview: 'Engine publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog Service API, Content Service API, Lodging Booking Service API, and 1 more. Tagged areas include Company, Travel, Business Travel, Lodging, and Hotels.


  Engine''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 55
rate_limits:
- limit_count: 16
  name: Hotel Engine Rate Limits
  slug: hotel-engine-rate-limits
score:
  band: developing
  composite: 54.6
  delta: 0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.2
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 71.1
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotel-engine/refs/heads/main/screenshots/hotel-engine-2026-08-07T170318.png
security:
- kind: authentication
  name: Hotel Engine Authentication
  slug: hotel-engine-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Hotel Engine Domain Security
  slug: hotel-engine-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hotel Engine Vulnerability Disclosure
  slug: hotel-engine-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Hotel Engine Trust Center
  slug: hotel-engine-trust-center
  summary_line: SOC 2 Type II
slug: hotel-engine
tags:
- Company
- Travel
- Business Travel
- Lodging
- Hotels
- Booking
- Travel Management
- Expense Management
- Payments
- gRPC
- Protobuf
- Partner API
website: https://www.engine.com/
---
