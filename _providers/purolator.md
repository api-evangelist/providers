---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Purolator Agentic Access
  operation_count: 16
  slug: purolator-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 9
apis:
- description: Purolator developer portal provides REST API catalogue for shipping services.
  name: Purolator Shipping API
  slug: purolator-shipping-api
artifact_total: 31
common:
- group: other
  href: https://artifacts.apis.io/purolator/hosts/purolator-hosts.yml
  title: ''
  type: Hosts
  url: hosts/purolator-hosts.yml
- group: other
  href: https://artifacts.apis.io/purolator/vendors/purolator-vendors.yml
  title: ''
  type: Vendors
  url: vendors/purolator-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purolator.com/en/terms-and-conditions-service
- group: operate
  title: ''
  type: Support
  url: https://www.purolator.com/en/support/contact-us/confirm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.purolator.com/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.purolator.com/en/media/23081/edit?destination=/en/node/16/latest
- group: start
  title: ''
  type: Login
  url: https://community.purolator.com/en/user/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ship.purolator.com/developer/restapicatalogue?lang=en
- group: auth
  href: https://artifacts.apis.io/purolator/security/purolator-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/purolator-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.purolator.com
coverage:
  checked: '2026-10-13'
  detail: Developer portal page returns HTML with JavaScript and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://ship.purolator.com/developer/restapicatalogue?lang=en
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Purolator is a leading North American courier and logistics company offering a comprehensive suite of shipping, freight, and supply chain solutions for businesses and consumers. Their services include domestic and international parcel delivery, freight transportation, customs brokerage, and e‑commerce integrations, supported by a robust online platform and developer resources. Purolator emphasizes reliability, tracking visibility, and flexible delivery options across Canada, the United States, and worldwide.
image: https://www.purolator.com/themes/custom/purolator_theme/logo.png
json_schemas:
- name: ApiResponse
  property_count: 1
  slug: purolator-api-response
- name: authentication200
  property_count: 4
  slug: purolator-authentication200
- name: CloseManifestRequest
  property_count: 4
  slug: purolator-close-manifest-request
- name: CloseManifestResponse
  property_count: 5
  slug: purolator-close-manifest-response
- name: CourierEstimateRequest
  property_count: 5
  slug: purolator-courier-estimate-request
- name: CourierEstimateResponse
  property_count: 2
  slug: purolator-courier-estimate-response
- name: CreateShipmentRequest
  property_count: 9
  slug: purolator-create-shipment-request
- name: CreateShipmentResponse
  property_count: 8
  slug: purolator-create-shipment-response
- name: FreightEstimateRequest
  property_count: 4
  slug: purolator-freight-estimate-request
- name: FreightEstimateResponse
  property_count: 1
  slug: purolator-freight-estimate-response
- name: GetDocumentsRequest
  property_count: 3
  slug: purolator-get-documents-request
- name: GetDocumentsResponse
  property_count: 4
  slug: purolator-get-documents-response
- name: GetHistoryRequest
  property_count: 6
  slug: purolator-get-history-request
- name: GetSummaryManifestRequest
  property_count: 3
  slug: purolator-get-summary-manifest-request
- name: GetSummaryManifestResponse
  property_count: 5
  slug: purolator-get-summary-manifest-response
- name: HistoryApiResponse
  property_count: 1
  slug: purolator-history-api-response
- name: Language
  property_count: 0
  slug: purolator-language
- name: ModifyPickup
  property_count: 4
  slug: purolator-modify-pickup
- name: OnlineTrackingResponse
  property_count: 2
  slug: purolator-online-tracking-response
- name: PickupCourier
  property_count: 7
  slug: purolator-pickup-courier
- name: RequestReference
  property_count: 0
  slug: purolator-request-reference
- name: TrackingSearchCriteria
  property_count: 2
  slug: purolator-tracking-search-criteria
- name: voidRequest
  property_count: 2
  slug: purolator-void-request
- name: VoidShipmentRequest
  property_count: 4
  slug: purolator-void-shipment-request
- name: VoidShipmentResponse
  property_count: 4
  slug: purolator-void-shipment-response
jsonld:
- class_count: 120
  name: Purolator Context
  property_count: 261
  slug: purolator-context
layout: provider
modified: '2026-10-13'
name: Purolator
nav: Providers
network: true
overview: 'Purolator publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shipping, Logistics, Couriers, and Freight.


  The Purolator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Purolator''s developer surface includes support and 9 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Purolator API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: purolator-rules
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 20.7
    developer_ergonomics: 7.1
    discoverability: 63.4
    operational_transparency: 0.0
  previous_composite: 23.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/purolator/purolator-2026-11-03T141721.png
security:
- kind: authentication
  name: Purolator Authentication
  slug: purolator-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Purolator Domain Security
  slug: purolator-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: purolator
tags:
- Company
- Shipping
- Logistics
- Couriers
- Freight
website: https://www.purolator.com
---
