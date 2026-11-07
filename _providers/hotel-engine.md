---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Hotel Engine Agentic Access
  operation_count: 11
  slug: hotel-engine-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- baseURL: https://partner-api.engine.com
  baseurl_source: declared
  description: The CatalogService API from Engine — 1 operation(s) for catalogservice.
  name: Engine Catalog Service API
  slug: hotel-engine-catalogservice-api
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
- baseURL: https://partner-api.engine.com
  baseurl_source: declared
  description: The Content Service API from Engine — 2 operation(s) for content service.
  name: Engine Content Service API
  slug: hotel-engine-content-service-api
artifact_total: 37
collections:
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
- group: commercial
  href: https://artifacts.apis.io/hotel-engine/finops/hotel-engine-finops.yml
  title: ''
  type: FinOps
  url: finops/hotel-engine-finops.yml
- group: design
  href: https://artifacts.apis.io/hotel-engine/rules/hotel-engine-rules.yml
  title: ''
  type: Spectral
  url: rules/hotel-engine-rules.yml
- group: design
  href: https://artifacts.apis.io/hotel-engine/json-ld/hotel-engine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hotel-engine-context.jsonld
- group: design
  href: https://artifacts.apis.io/hotel-engine/vocabulary/hotel-engine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hotel-engine-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/hotel-engine/security/hotel-engine-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hotel-engine-trust-center.yml
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-shop-lodging-v1-room.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-shop-lodging-v1-room.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-shop-lodging-v1-offer.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-shop-lodging-v1-offer.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-shop-lodging-service-v1-service.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-shop-lodging-service-v1-service.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-shop-lodging-service-v1-find_best_offers_streaming.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-shop-lodging-service-v1-find_best_offers_streaming.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-shop-lodging-service-v1-find_best_offers.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-shop-lodging-service-v1-find_best_offers.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-shop-lodging-service-v1-find_availability.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-shop-lodging-service-v1-find_availability.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-service-common-v1-error.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-service-common-v1-error.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-content-v1-lodging-room.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-content-v1-lodging-room.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-content-v1-lodging-property.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-content-v1-lodging-property.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-content-service-v1-service.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-content-service-v1-service.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-content-service-v1-list_property_catalog.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-content-service-v1-list_property_catalog.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-content-service-v1-list_properties.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-content-service-v1-list_properties.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-content-service-v1-get_properties.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-content-service-v1-get_properties.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-traveler.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-traveler.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-sell_type.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-sell_type.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-refund.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-refund.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-price.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-price.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-postal_address.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-postal_address.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-payment_info.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-payment_info.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-payment_card.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-payment_card.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-media.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-media.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-loyalty.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-loyalty.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-image.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-image.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-geo.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-geo.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-engine_direct_bill.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-engine_direct_bill.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-currency.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-currency.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-contact.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-contact.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-conditions.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-conditions.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-common-v1-actions.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-common-v1-actions.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-v1-status.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-v1-status.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-v1-reservation.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-v1-reservation.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-v1-quote.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-v1-quote.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-v1-metadata.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-v1-metadata.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-v1-guests.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-v1-guests.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-v1-booking.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-v1-booking.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-submit_cancellation.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-submit_cancellation.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-service.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-service.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-preview_cancellation.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-preview_cancellation.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-get_bookings_streaming.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-get_bookings_streaming.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-get_bookings.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-get_bookings.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-generate_folio.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-generate_folio.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-confirm_offer.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-confirm_offer.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-lodging-service-v1-book.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-lodging-service-v1-book.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-common-v1-applied_payment_info.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-common-v1-applied_payment_info.proto
- group: other
  href: https://artifacts.apis.io/hotel-engine/grpc/hotel-engine-book-common-service-v1-error.proto
  title: ''
  type: Protobuf
  url: grpc/hotel-engine-book-common-service-v1-error.proto
- group: agent
  href: https://artifacts.apis.io/hotel-engine/well-known/hotel-engine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hotel-engine-well-known.yml
- group: other
  href: https://artifacts.apis.io/hotel-engine/hosts/hotel-engine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hotel-engine-hosts.yml
- group: build
  href: https://artifacts.apis.io/hotel-engine/integrations/hotel-engine-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hotel-engine-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/hotel-engine/vendors/hotel-engine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hotel-engine-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://engine.com/press
- group: commercial
  href: https://artifacts.apis.io/hotel-engine/plans/hotel-engine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hotel-engine-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hotel-engine/rate-limits/hotel-engine-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hotel-engine-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/hotel-engine/overlays/hotel-engine-omni-partner-api-overlay.yaml
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
  href: https://artifacts.apis.io/hotel-engine/changelog/hotel-engine-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hotel-engine-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://engine-public.github.io/engine-partner-api/versioning.html#support-for-deprecated-versions
- group: design
  href: https://artifacts.apis.io/hotel-engine/lifecycle/hotel-engine-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hotel-engine-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.engine.com/responsible-disclosure
- group: auth
  href: https://artifacts.apis.io/hotel-engine/security/hotel-engine-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotel-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.engine.com/
- group: auth
  href: https://artifacts.apis.io/hotel-engine/security/hotel-engine-trust-center.yml
  title: ''
  type: Compliance
  url: security/hotel-engine-trust-center.yml
- group: design
  href: https://artifacts.apis.io/hotel-engine/conformance/hotel-engine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hotel-engine-conformance.yml
- group: build
  href: https://artifacts.apis.io/hotel-engine/packages/hotel-engine-packages.yml
  title: ''
  type: Packages
  url: packages/hotel-engine-packages.yml
- group: build
  href: https://artifacts.apis.io/hotel-engine/packages/hotel-engine-packages.yml
  title: ''
  type: SDKs
  url: packages/hotel-engine-packages.yml
- group: start
  href: https://artifacts.apis.io/hotel-engine/sandbox/hotel-engine-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hotel-engine-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/hotel-engine/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hotel-engine/llms/hotel-engine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hotel-engine-llms.txt
- group: agent
  href: https://artifacts.apis.io/hotel-engine/agentic-access/hotel-engine-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hotel-engine-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hotel-engine/security/hotel-engine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hotel-engine-domain-security.yml
created: '2026-08-04'
description: 'Engine (formerly Hotel Engine, rebranded in 2024) is a Denver, Colorado business travel and spend platform for booking and managing lodging, flights, rental cars, group travel, and meeting and event spaces, with travel policy enforcement, trip approvals, consolidated DirectBill invoicing, and the Engine X charge card. Engine says it serves 25,000+ businesses and 1.2 million travelers with negotiated rates across 1,000,000+ hotel properties. Its API product is Omni — a partner-facing lodging inventory API offered over gRPC and HTTP/JSON, authenticated with mutual TLS, that covers property content, real-time rate shopping, booking, folio generation, and cancellation. Omni is protobuf-first: the proto contracts are published under Apache 2.0 on GitHub and the Swagger document, descriptor set, and JVM client bindings are generated from them and released per version.'
finops:
- has_sources: true
  method: derived
  name: Hotel Engine Finops
  primary_unit: ''
  service_category: ''
  slug: hotel-engine-finops
  template: true
image: https://engine.com/_astro/engine-og-default.BAjJjAAC.png
json_schemas:
- name: apiHttpBody
  property_count: 3
  slug: hotel-engine-api-http-body
- name: Book_Lodging_Service_BookRequest_v1
  property_count: 4
  slug: hotel-engine-v1-book-request
- name: Book_Lodging_Service_ConfirmOfferRequest_v1
  property_count: 2
  slug: hotel-engine-v1-confirm-offer-request
- name: Book_Lodging_Service_ConfirmOfferRequest_v1
  property_count: 2
  slug: hotel-engine-v1-confirm-offer-response
- name: Shop_Lodging_Service_FindAvailabilityRequest_v1
  property_count: 2
  slug: hotel-engine-v1-find-availability-request
- name: Shop_Lodging_Service_FindAvailabilityResponse_v1
  property_count: 1
  slug: hotel-engine-v1-find-availability-response
- name: Shop_Lodging_Service_FindBestOffersRequest_v1
  property_count: 3
  slug: hotel-engine-v1-find-best-offers-request
- name: Shop_Lodging_Service_FindBestOffersResponse_v1
  property_count: 1
  slug: hotel-engine-v1-find-best-offers-response
- name: Book_Lodging_Service_GetBookingsRequest_v1
  property_count: 1
  slug: hotel-engine-v1-get-bookings-request
- name: GetPropertiesRequest_v1
  property_count: 1
  slug: hotel-engine-v1-get-properties-request
- name: GetPropertiesResponse_v1
  property_count: 2
  slug: hotel-engine-v1-get-properties-response
- name: ListPropertiesResponse_v1
  property_count: 2
  slug: hotel-engine-v1-list-properties-response
- name: ListPropertyCatalogRequest_v1
  property_count: 2
  slug: hotel-engine-v1-list-property-catalog-request
- name: ListPropertyCatalogResponse_v1
  property_count: 2
  slug: hotel-engine-v1-list-property-catalog-response
- name: Book_Lodging_Service_PreviewCancellationResponse_v1
  property_count: 2
  slug: hotel-engine-v1-preview-cancellation-response
jsonld:
- class_count: 100
  name: Hotel Engine Context
  property_count: 176
  slug: hotel-engine-context
layout: provider
modified: '2026-08-04'
name: Engine
nav: Providers
network: true
overview: 'Engine publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog Service API, Lodging Booking Service API, Lodging Shopping Service API, and 1 more. Tagged areas include Company, Travel, Business Travel, Lodging, and Hotels.


  The Engine catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Engine''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 83 more developer resources.'
plans:
- name: Hotel Engine Plans Pricing
  plan_count: 1
  slug: hotel-engine-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 16
  name: Hotel Engine Rate Limits
  slug: hotel-engine-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Engine API Rules
  rule_count: 60
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 7
  slug: hotel-engine-rules
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.0
  facets:
    access_clarity: 73.7
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 68.4
  previous_composite: 58.9
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
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hotel-engine/hotel-engine-2026-08-07T170318.png
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
skill_count: 4
skills:
- name: Deep link travelers into Engine checkout (Omni Swift)
  slug: hotel-engine-deep-link-to-engine-checkout
- name: Manage and cancel Engine lodging bookings
  slug: hotel-engine-manage-and-cancel-bookings
- name: Shop and book lodging with the Engine Omni API
  slug: hotel-engine-shop-and-book-lodging
- name: Sync the Engine lodging property catalog
  slug: hotel-engine-sync-property-catalog
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
