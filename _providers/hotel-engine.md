---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Hotel Engine Agentic Access
  operation_count: 11
  slug: hotel-engine-agentic-access
  summary_line: 11 operations · 10 acting
api_count: 2
apis:
- baseURL: https://partner-api.engine.com
  baseurl_source: declared
  description: The CatalogService API from Engine — 1 operation(s) for catalogservice.
  name: Engine Catalog Service API
  slug: hotel-engine-catalogservice-api
- baseURL: https://partner-api.engine.com
  baseurl_source: declared
  description: The ContentService API from Engine — 2 operation(s) for contentservice.
  name: Engine Content Service API
  slug: hotel-engine-contentservice-api
- baseURL: https://partner-api.engine.com
  baseurl_source: declared
  description: The LodgingBookingService API from Engine — 5 operation(s) for lodgingbookingservice.
  name: Engine Lodging Booking Service API
  slug: hotel-engine-lodgingbookingservice-api
- baseURL: https://partner-api.engine.com
  baseurl_source: declared
  description: The LodgingShoppingService API from Engine — 2 operation(s) for lodgingshoppingservice.
  name: Engine Lodging Shopping Service API
  slug: hotel-engine-lodgingshoppingservice-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Omni, Powered by Engine Catalog Service API
  slug: open-hotel-engine-catalogservice-api
- collection_type: open
  name: Omni, Powered by Engine Content Service API
  slug: open-hotel-engine-contentservice-api
- collection_type: open
  name: Omni, Powered by Engine Lodging Booking Service API
  slug: open-hotel-engine-lodgingbookingservice-api
- collection_type: open
  name: Omni, Powered by Engine Lodging Shopping Service API
  slug: open-hotel-engine-lodgingshoppingservice-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hotel-engine-omni-partner-api-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/engine-public/engine-partner-api/blob/main/LICENSE
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


  Engine''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 16
  name: Hotel Engine Rate Limits
  slug: hotel-engine-rate-limits
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
