---
access_model:
  confidence: high
  gated: partner
  gated_source:
  - x-api-posture
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Fedex Agentic Access
  operation_count: 7
  slug: fedex-agentic-access
  summary_line: 7 operations · 6 acting · 1 human-in-the-loop
api_count: 29
apis:
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: Leverage the FedEx OAuth 2.0 token authentication method to authorize the application and authenticate API requests.
  name: FedEx API Authorization
  slug: fedex-api-authorization
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: 'Request pre-ship rating information to determine costs. Note: FedEx Integrator Providers who would like to offer rating capabilities are required to select the Comprehensive Rates and Transit Times AP'
  name: FedEx Rates and Transit Times API
  slug: fedex-rates-and-transit-times-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: Process and submit shipping requests to produce a shipping label.
  name: FedEx Ship API
  slug: fedex-ship-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: Manage everything related to courier shipment pickups.
  name: FedEx Pickup Request API
  slug: fedex-pickup-request-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: Use FedEx ® Tracking options to obtain timely and accurate tracking information.
  name: FedEx Basic Integrated Visibility
  slug: fedex-basic-integrated-visibility
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: Submit per-product regulatory compliance data ahead of shipping.
  name: FedEx Regulatory API
  slug: fedex-regulatory-api
- description: FedEx Advanced Integrated Visibility delivers near real-time tracking push notifications directly to your servers via webhook technology, for shipments on registered account numbers or registered trac
  name: FedEx Shipment Visibility Webhook
  slug: fedex-shipment-visibility-webhook
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Address API from FedEx — 1 operation(s) for address.
  name: FedEx Address API
  slug: fedex-address-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Availability API from FedEx — 3 operation(s) for availability.
  name: FedEx Availability API
  slug: fedex-availability-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Commodity API from FedEx — 1 operation(s) for commodity.
  name: FedEx Commodity API
  slug: fedex-commodity-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Country API from FedEx — 1 operation(s) for country.
  name: FedEx Country API
  slug: fedex-country-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Documents API from FedEx — 5 operation(s) for documents.
  name: FedEx Documents API
  slug: fedex-documents-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Dutytax API from FedEx — 1 operation(s) for dutytax.
  name: FedEx Dutytax API
  slug: fedex-dutytax-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Globaltrade API from FedEx — 1 operation(s) for globaltrade.
  name: FedEx Globaltrade API
  slug: fedex-globaltrade-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Irc API from FedEx — 1 operation(s) for irc.
  name: FedEx Irc API
  slug: fedex-irc-api
- baseURL: https://apis.fedex.com
  baseurl_source: declared
  description: The Location API from FedEx — 1 operation(s) for location.
  name: FedEx Location API
  slug: fedex-location-api
- baseURL: https://cvc.site.fedex.com/virts/API-Factory-Dev/NSMCWebhook-Resource/API
  baseurl_source: declared
  description: The Webhook API from FedEx — 5 operation(s) for webhook.
  name: FedEx Webhook API
  slug: fedex-webhook-api
artifact_total: 115
asyncapis:
- description: ''
  name: Fedex Advanced Integrated Visibility Webhooks
  slug: fedex-advanced-integrated-visibility-webhooks
collections:
- collection_type: open
  name: FedEx Track Authorization API
  slug: open-fedex-authorization-api
- collection_type: open
  name: FedEx Authorization Track API
  slug: open-fedex-track-api
- collection_type: open
  name: FedEx Track API
  slug: open-fedex
common:
- group: design
  href: https://artifacts.apis.io/fedex/rules/fedex-rules.yml
  title: ''
  type: Spectral
  url: rules/fedex-rules.yml
- group: design
  href: https://artifacts.apis.io/fedex/json-ld/fedex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fedex-context.jsonld
- group: design
  href: https://artifacts.apis.io/fedex/vocabulary/fedex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fedex-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fedex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fedex/asyncapi/fedex-advanced-integrated-visibility-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fedex-advanced-integrated-visibility-webhooks.yml
- group: design
  href: https://artifacts.apis.io/fedex/data-model/fedex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fedex-data-model.yml
- group: operate
  href: https://artifacts.apis.io/fedex/changelog/fedex-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fedex-changelog.yml
- group: design
  href: https://artifacts.apis.io/fedex/conventions/fedex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fedex-conventions.yml
- group: start
  href: https://artifacts.apis.io/fedex/sandbox/fedex-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fedex-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/fedex/security/fedex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fedex-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.fedex.com/api/en-us/guides/versioning.html
- group: design
  href: https://artifacts.apis.io/fedex/lifecycle/fedex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fedex-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fedex/errors/fedex-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/fedex-error-codes.yml
- group: design
  href: https://artifacts.apis.io/fedex/errors/fedex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fedex-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fedex/conformance/fedex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fedex-conformance.yml
- group: other
  href: https://artifacts.apis.io/fedex/overlays/fedex-account-number-subscription-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fedex-account-number-subscription-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fedex/hosts/fedex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fedex-hosts.yml
- group: build
  href: https://artifacts.apis.io/fedex/integrations/fedex-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/fedex-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/fedex/vendors/fedex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fedex-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/fedex/plans/fedex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fedex-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fedex/rate-limits/fedex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fedex-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fedex/finops/fedex-finops.yml
  title: ''
  type: FinOps
  url: finops/fedex-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://digital-blog.fedex.com/index.rss
- group: other
  href: https://artifacts.apis.io/fedex/capabilities/fedex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fedex-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/fedex/agentic-access/fedex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fedex-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fedex/security/fedex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fedex-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fedex/authentication/fedex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fedex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fedex
- group: company
  title: ''
  type: Website
  url: https://www.fedex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fedex.com/api/en-us/home.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fedex.com/api/en-us/get-started.html
- group: other
  title: ''
  type: Catalog
  url: https://developer.fedex.com/api/en-us/catalog.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fedex.com/api/en-us/home.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fedex.com/api/en-us/catalog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.fedex.com/api/en-us/guides/pricing-guide.html
- group: operate
  title: ''
  type: Support
  url: https://developer.fedex.com/api/en-us/support.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.fedex.com/api/en-us/announcements.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fedex.com/en-us/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fedex.com/en-us/trust-center/global-privacy-policy.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.fedex.com/en-us/trust-center.html
- group: auth
  title: ''
  type: Security
  url: https://www.fedex.com/en-us/trust-center/vulnerability-disclosure-program.html
- group: commercial
  title: ''
  type: License
  url: https://developer.fedex.com/api/en-us/legal/fdpla.html
created: '2025-03-01'
description: FedEx is a logistics company that provides shipping and delivery services worldwide. They offer a range of solutions for individuals and businesses, including express shipping, freight services, and e-commerce fulfillment. FedEx publishes a suite of REST APIs covering tracking, shipping, rating, address validation, pickup, locator, trade documents, and post-shipment visibility through their developer portal.
finops:
- has_sources: true
  method: generated
  name: Fedex Finops
  primary_unit: ''
  service_category: Logistics / Shipping
  slug: fedex-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fedex.png
json_schemas:
- name: AdvcResponseVO
  property_count: 3
  slug: fedex-advc-response-vo
- name: AvailabilitycxsResponseVO
  property_count: 3
  slug: fedex-availabilitycxs-response-vo
- name: body_1
  property_count: 0
  slug: fedex-body-1
- name: body_2
  property_count: 0
  slug: fedex-body-2
- name: body
  property_count: 0
  slug: fedex-body
- name: body_specialserviceoptions
  property_count: 0
  slug: fedex-body-specialserviceoptions
- name: CmdcResponseVO
  property_count: 3
  slug: fedex-cmdc-response-vo
- name: ConfirmConsolidationResultsResponse
  property_count: 3
  slug: fedex-confirm-consolidation-results-response
- name: ConsolidationShipmentResultsResponse
  property_count: 3
  slug: fedex-consolidation-shipment-results-response
- name: CountryCXSResponseVO
  property_count: 3
  slug: fedex-country-cxsresponse-vo
- name: CreateConsolidationResponse
  property_count: 3
  slug: fedex-create-consolidation-response
- name: CreateConsolidationShipmentResponse
  property_count: 3
  slug: fedex-create-consolidation-shipment-response
- name: CustomerKeyInputVO
  property_count: 3
  slug: fedex-customer-key-input-vo
- name: deleteConsolidationResponse
  property_count: 3
  slug: fedex-delete-consolidation-response
- name: DocumentResponseOutputVO
  property_count: 2
  slug: fedex-document-response-output-vo
- name: Domestic_Ground_Shipment
  property_count: 0
  slug: fedex-domestic-ground-shipment
- name: EdtDetailsRequestVO
  property_count: 7
  slug: fedex-edt-details-request-vo
- name: EdtDetailsResponseVO
  property_count: 3
  slug: fedex-edt-details-response-vo
- name: Electronic_Trade_Documents_Requested_Document_Copies
  property_count: 0
  slug: fedex-electronic-trade-documents-requested-document-copies
- name: Express_OneLabelATATime_Child_Shipment
  property_count: 0
  slug: fedex-express-one-label-atatime-child-shipment
- name: FreightShipment_BillTo_Freight_Account
  property_count: 0
  slug: fedex-freight-shipment-bill-to-freight-account
- name: FreightShipment_International_SingleShot_MPS_ShipTo_Freight_Account
  property_count: 0
  slug: fedex-freight-shipment-international-single-shot-mps-ship-to-freight-account
- name: FreightShipment_OneLabelAtATime_MPS_Child_ShipTo_Freight_Account
  property_count: 0
  slug: fedex-freight-shipment-one-label-at-atime-mps-child-ship-to-freight-account
- name: FreightShipment_OneLabelAtATime_MPS_Master_ShipTo_Freight_Account
  property_count: 0
  slug: fedex-freight-shipment-one-label-at-atime-mps-master-ship-to-freight-account
- name: FreightShipment_ShipTo_Freight_Account
  property_count: 0
  slug: fedex-freight-shipment-ship-to-freight-account
- name: FullSchema-confirmOpenShipment
  property_count: 8
  slug: fedex-full-schema-confirm-open-shipment
- name: FullSchema-CreatePickup
  property_count: 11
  slug: fedex-full-schema-create-pickup
- name: Full_Schema_Find_Location
  property_count: 24
  slug: fedex-full-schema-find-location
- name: FullSchema-getOpenShipmentResults
  property_count: 4
  slug: fedex-full-schema-get-open-shipment-results
- name: FullSchema-ImageUploadServiceInputVO
  property_count: 3
  slug: fedex-full-schema-image-upload-service-input-vo
- name: FullSchema-modifyPackageInOpenShipment
  property_count: 6
  slug: fedex-full-schema-modify-package-in-open-shipment
- name: Full_Schema_Multiple_Piece_Shipment
  property_count: 4
  slug: fedex-full-schema-multiple-piece-shipment
- name: Full_Schema_Notification
  property_count: 6
  slug: fedex-full-schema-notification
- name: FullSchema
  property_count: 5
  slug: fedex-full-schema
- name: Full_Schema_SPOD
  property_count: 2
  slug: fedex-full-schema-spod
- name: Full_Schema_Tracking_References
  property_count: 2
  slug: fedex-full-schema-tracking-references
- name: FullSchema-ValidatePostal
  property_count: 9
  slug: fedex-full-schema-validate-postal
- name: Ground_OneLabelATATime_Child_Shipment
  property_count: 0
  slug: fedex-ground-one-label-atatime-child-shipment
- name: Ground_OneLabelATATime_Master_Shipment
  property_count: 0
  slug: fedex-ground-one-label-atatime-master-shipment
- name: GticResponseVO
  property_count: 3
  slug: fedex-gtic-response-vo
- name: HarmonizedCodeSearchRequestVO
  property_count: 1
  slug: fedex-harmonized-code-search-request-vo
- name: HarmonizedCodeSearchResponseVO
  property_count: 3
  slug: fedex-harmonized-code-search-response-vo
- name: ImageUploadServiceOutputVO_1
  property_count: 3
  slug: fedex-image-upload-service-output-vo-1
- name: ImageUploadServiceOutputVO
  property_count: 2
  slug: fedex-image-upload-service-output-vo
- name: IrcpResponseVO
  property_count: 2
  slug: fedex-ircp-response-vo
- name: LoccResponseVO
  property_count: 3
  slug: fedex-locc-response-vo
- name: MinimumSamplePayload-CreateOpenshipmentAsynchronous
  property_count: 0
  slug: fedex-minimum-sample-payload-create-openshipment-asynchronous
- name: MinimumSamplePayload-CreateOpenshipment
  property_count: 0
  slug: fedex-minimum-sample-payload-create-openshipment
- name: MinimumSamplePayload-modifyOpenShipment
  property_count: 0
  slug: fedex-minimum-sample-payload-modify-open-shipment
- name: MinimumSamplePayload
  property_count: 0
  slug: fedex-minimum-sample-payload
- name: ModifyConsolidationResponse
  property_count: 3
  slug: fedex-modify-consolidation-response
- name: MultiBasePreResponse_1
  property_count: 3
  slug: fedex-multi-base-pre-response-1
- name: MultiBasePreResponse
  property_count: 3
  slug: fedex-multi-base-pre-response
- name: NSMCWebhookResponseVO_1
  property_count: 3
  slug: fedex-nsmcwebhook-response-vo-1
- name: NSMCWebhookResponseVO_2
  property_count: 3
  slug: fedex-nsmcwebhook-response-vo-2
- name: NSMCWebhookResponseVO_3
  property_count: 4
  slug: fedex-nsmcwebhook-response-vo-3
- name: NSMCWebhookResponseVO_4
  property_count: 2
  slug: fedex-nsmcwebhook-response-vo-4
- name: PudcResponseVO_CancelPickup
  property_count: 3
  slug: fedex-pudc-response-vo-cancel-pickup
- name: PudcResponseVO_CreatePickup
  property_count: 3
  slug: fedex-pudc-response-vo-create-pickup
- name: PudcResponseVO_PickupAvailability
  property_count: 3
  slug: fedex-pudc-response-vo-pickup-availability
- name: RatcResponseVO
  property_count: 3
  slug: fedex-ratc-response-vo
- name: RegulatoryProfileRequest
  property_count: 0
  slug: fedex-regulatory-profile-request
- name: RegulatoryProfileResponse
  property_count: 3
  slug: fedex-regulatory-profile-response
- name: regulatorydetails_retrieve_body
  property_count: 0
  slug: fedex-regulatorydetails-retrieve-body
- name: Response
  property_count: 4
  slug: fedex-response
- name: RetrieveSubscriptionOutputVO
  property_count: 3
  slug: fedex-retrieve-subscription-output-vo
- name: SamplePayload-InternationalShipmentMPS
  property_count: 0
  slug: fedex-sample-payload-international-shipment-mps
- name: Search_Location_by_Geographic_Coordinates
  property_count: 0
  slug: fedex-search-location-by-geographic-coordinates
- name: Search_Location_by_RETURNS_SERVICES
  property_count: 0
  slug: fedex-search-location-by-returns-services
- name: Search_Location_HOLD_AT_LOCATION
  property_count: 0
  slug: fedex-search-location-hold-at-location
- name: Search_Location_OFFICE_AND_ONSITE
  property_count: 0
  slug: fedex-search-location-office-and-onsite
- name: SHPCResponseVO
  property_count: 2
  slug: fedex-shpcresponse-vo
- name: trackingnumbers_association_body
  property_count: 0
  slug: fedex-trackingnumbers-association-body
- name: TransitTimeOutputVO
  property_count: 3
  slug: fedex-transit-time-output-vo
- name: TrkcResponseVO_ReferenceNumber
  property_count: 3
  slug: fedex-trkc-response-vo-reference-number
- name: TrkcResponseVO_TrackingNumber
  property_count: 3
  slug: fedex-trkc-response-vo-tracking-number
- name: UpdateSubscriptionOutputVO
  property_count: 3
  slug: fedex-update-subscription-output-vo
- name: v1_endofday_body_1
  property_count: 0
  slug: fedex-v1-endofday-body-1
- name: v1_endofday_body
  property_count: 0
  slug: fedex-v1-endofday-body
- name: v3_subscriptions_body
  property_count: 0
  slug: fedex-v3-subscriptions-body
jsonld:
- class_count: 120
  name: Fedex Context
  property_count: 263
  slug: fedex-context
layout: provider
modified: '2026-11-05'
name: FedEx
nav: Providers
network: true
overview: 'FedEx publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Authorization, Rates and Transit Times API, Ship API, and 14 more. Tagged areas include Address Validation, Freight, Logistics, Pickup, and Ratings.


  The FedEx catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  FedEx''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, API reference, pricing, and 35 more developer resources.'
plans:
- name: Fedex Plans Pricing
  plan_count: 6
  slug: fedex-plans-pricing
press:
- date: ''
  title: FedEx to Offer Access to AI-Powered Post-Purchase ...
  url: https://newsroom.fedex.com/newsroom/global-english/fedex-to-offer-access-to-ai-powered-post-purchase-solutions-for-enterprises
- date: ''
  title: FedEx and Cisco Transform Business Through AI Workflows
  url: https://www.virtasant.com/ai-today/unlocking-potential-ai-workflows-at-fedex-cisco
- date: ''
  title: FedEx Freight Adds AI Tools to Boost Win Percentage - TT
  url: https://www.ttnews.com/articles/fedex-freight-ai-tools-2026
- date: ''
  title: Technology and Innovation Policy Perspectives
  url: https://www.fedex.com/en-us/about/policy/technology-innovation.html
- date: ''
  title: FedEx Announces Expansion of FedEx Fulfillment With ...
  url: https://newsroom.fedex.com/newsroom/global-english/fedex-announces-expansion-of-fedex-fulfillment-with-nimble-alliance
random_paper: 20
rate_limits:
- limit_count: 5
  name: Fedex Rate Limits
  slug: fedex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: FedEx API Rules
  rule_count: 62
  severity_counts:
    error: 43
    hint: 0
    info: 6
    warn: 13
  slug: fedex-rules
scopes:
- name: Fedex Scopes
  scope_count: 0
  slug: fedex-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 40
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 38.4
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 69.8
    developer_ergonomics: 64.9
    discoverability: 71.4
    operational_transparency: 73.7
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 29.4
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fedex/fedex-2026-06-20T181131.png
security:
- kind: authentication
  name: Fedex Authentication
  slug: fedex-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fedex Domain Security
  slug: fedex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fedex Vulnerability Disclosure
  slug: fedex-vulnerability-disclosure
  summary_line: contact published
skill_count: 4
skills:
- name: fedex-find-locations
  slug: fedex-find-locations
- name: fedex-rate-and-ship
  slug: fedex-rate-and-ship
- name: fedex-schedule-pickup
  slug: fedex-schedule-pickup
- name: fedex-track-shipment
  slug: fedex-track-shipment
slug: fedex
tags:
- Address Validation
- Freight
- Logistics
- Pickup
- Ratings
- Shipping
- Tracking
- Webhook
- Fortune 100
website: https://www.fedex.com/
---
