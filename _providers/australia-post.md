---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Australia Post Agentic Access
  operation_count: 9
  slug: australia-post-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 12
apis:
- description: Enables eParcel and StarTrack contract customers to lodge orders, create and print shipping labels (including dangerous goods forms), generate order summaries, despatch parcels, estimate prices and in
  name: Australia Post Shipping and Tracking API
  slug: shipping-and-tracking
- description: Lets businesses and developers embed a postage calculator into websites or applications to retrieve standard retail postage rates for domestic and international parcels and letters. Accepts weight, di
  name: Australia Post Postage Assessment Calculator API
  slug: postage-assessment-calculator
- description: Allows customers to select preferred delivery options at checkout, including delivery speed, delivery or collection location, and specific day, date, and time of delivery. Supports parcel locker deliv
  name: Australia Post Delivery Choices API
  slug: delivery-choices
- baseURL: https://digitalapi.auspost.com.au
  baseurl_source: declared
  description: The Endpoints API from Australia Post — 9 operation(s) for endpoints.
  name: Australia Post Endpoints API
  slug: australia-post-endpoints-api
artifact_total: 75
collections:
- collection_type: open
  name: Delivery Partner Endpoints API
  slug: open-australia-post-endpoints-api
common:
- group: design
  href: https://artifacts.apis.io/australia-post/rules/australia-post-rules.yml
  title: ''
  type: Spectral
  url: rules/australia-post-rules.yml
- group: design
  href: https://artifacts.apis.io/australia-post/rules/australia-post-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/australia-post-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/australia-post/json-ld/australia-post-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/australia-post-context.jsonld
- group: design
  href: https://artifacts.apis.io/australia-post/vocabulary/australia-post-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/australia-post-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/australia-post/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/australia-post/data-model/australia-post-data-model.yml
  title: ''
  type: DataModel
  url: data-model/australia-post-data-model.yml
- group: design
  href: https://artifacts.apis.io/australia-post/components/australia-post-components.yml
  title: ''
  type: Components
  url: components/australia-post-components.yml
- group: operate
  href: https://artifacts.apis.io/australia-post/changelog/australia-post-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/australia-post-changelog.yml
- group: design
  href: https://artifacts.apis.io/australia-post/conventions/australia-post-conventions.yml
  title: ''
  type: Conventions
  url: conventions/australia-post-conventions.yml
- group: start
  href: https://artifacts.apis.io/australia-post/sandbox/australia-post-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/australia-post-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://auspost.com.au/about-us/about-our-site/responsible-disclosure
- group: operate
  href: https://artifacts.apis.io/australia-post/lifecycle/australia-post-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/australia-post-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/australia-post/lifecycle/australia-post-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/australia-post-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/australia-post/errors/australia-post-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/australia-post-error-codes.yml
- group: design
  href: https://artifacts.apis.io/australia-post/errors/australia-post-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/australia-post-problem-types.yml
- group: design
  href: https://artifacts.apis.io/australia-post/conformance/australia-post-conformance.yml
  title: ''
  type: Conformance
  url: conformance/australia-post-conformance.yml
- group: other
  href: https://artifacts.apis.io/australia-post/overlays/australia-post-agency-data-delivery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/australia-post-agency-data-delivery-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/australia-post/well-known/australia-post-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australia-post-status-security.txt
- group: auth
  href: https://artifacts.apis.io/australia-post/well-known/australia-post-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australia-post-security.txt
- group: agent
  href: https://artifacts.apis.io/australia-post/well-known/australia-post-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/australia-post-well-known.yml
- group: other
  href: https://artifacts.apis.io/australia-post/hosts/australia-post-hosts.yml
  title: ''
  type: Hosts
  url: hosts/australia-post-hosts.yml
- group: build
  href: https://artifacts.apis.io/australia-post/integrations/australia-post-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/australia-post-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/australia-post/vendors/australia-post-vendors.yml
  title: ''
  type: Vendors
  url: vendors/australia-post-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://auspost.com.au/disruptions-and-updates/pricing-updates
- group: auth
  href: https://artifacts.apis.io/australia-post/scopes/australia-post-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/australia-post-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/australia-post/plans/australia-post-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/australia-post-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/australia-post/rate-limits/australia-post-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/australia-post-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/australia-post/finops/australia-post-finops.yml
  title: ''
  type: FinOps
  url: finops/australia-post-finops.yml
- group: other
  href: https://artifacts.apis.io/australia-post/capabilities/australia-post-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/australia-post-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/australia-post/agentic-access/australia-post-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/australia-post-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/australia-post/security/australia-post-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/australia-post-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/australia-post/security/australia-post-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/australia-post-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/australia-post/authentication/australia-post-authentication.yml
  title: ''
  type: Authentication
  url: authentication/australia-post-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://auspost.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://auspost.com.au/developers/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.auspost.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://auspost.com.au/developers/help-support/about-our-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://auspost.com.au/developers/help-support/how-to-get-credentials/
- group: other
  title: ''
  type: Catalog
  url: https://auspost.com.au/developers/api-documentations/
- group: start
  title: ''
  type: Signup
  url: https://developers.auspost.com.au/apis/pacpcs-registration
- group: start
  title: ''
  type: Login
  url: https://developers.auspost.com.au/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developers.auspost.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auspost.com.au/content/dam/auspost_corp/media/documents/api-licence-terms-of-use.pdf
- group: operate
  title: ''
  type: FAQ
  url: https://auspost.com.au/developers/help-support/
- group: operate
  title: ''
  type: FAQ
  url: https://developers.auspost.com.au/faq
- group: docs
  title: ''
  type: APIReference
  url: https://developers.auspost.com.au/docs/reference
- group: build
  title: ''
  type: Plugins
  url: https://developers.auspost.com.au/plugins
- group: operate
  title: ''
  type: Support
  url: https://auspost.com.au/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auspost.com.au/privacy
- group: company
  title: ''
  type: Blog
  url: https://auspost.com.au/business/grow-your-business/business-ideas-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auspost
- group: company
  title: ''
  type: Twitter
  url: https://x.com/auspost
- group: operate
  title: ''
  type: Contact
  url: mailto:customer_connectivity@auspost.com.au
- group: other
  title: ''
  type: IntegratePage
  url: https://auspost.com.au/integrate-shipping-and-tracking-apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/australia-post
created: '2026-06-13'
description: Australia Post is Australia's primary postal operator, offering a developer platform with REST APIs for e-commerce merchants, logistics providers, and delivery partners. APIs cover shipping label creation, parcel tracking, postage calculation, parcel locker and post office location lookup, delivery choice and scheduling, and delivery partner event reporting for an integrated end-to-end fulfilment ecosystem.
examples:
- key_count: 4
  name: Locations Multiple Points Returned Of Different Types
  slug: locations-multiple-points-returned-of-different-types
- key_count: 7
  name: Locations Services Get 200 Example1
  slug: locations-services-get-200-example1
- key_count: 7
  name: Locations Services_{Service_Codes} Get 200 Example1
  slug: locations-services_{service_codes}-get-200-example1
- key_count: 4
  name: Locations Single Po Returned
  slug: locations-single-po-returned
features:
- RESTful APIs using JSON payloads; GET, POST, PUT, PATCH, and DELETE methods supported
- Authentication via API Key (AUTH-KEY header), Basic Auth, OAuth 2.0 Client Credentials, or OAuth 2.0 Authorization Code
- Base URL for all production APIs is https://digitalapi.auspost.com.au
- Sandbox (test-bed) environment available for Shipping and Tracking API; requires account credentials
- Locations API and Postage Assessment Calculator API keys obtainable via self-serve registration; no contract required
- Shipping and Tracking API and Delivery Choices API require an active eParcel or StarTrack parcels contract
- Delivery Partner API requires authorised delivery network partner status
- Rate limits enforced per second, minute, hour, and day; HTTP 429 returned on breach
- Rate-limit status surfaced via X-RateLimit-Limit-* and X-RateLimit-Remaining-* response headers
- OpenAPI definitions available for Locations and Delivery Partner APIs; Swagger code generation supported
- API status monitoring at status.developers.auspost.com.au
finops:
- has_sources: true
  method: generated
  name: Australia Post Finops
  primary_unit: ''
  service_category: Logistics / Shipping
  slug: australia-post-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/australia-post.png
json_schemas:
- name: ApiPostageResult
  property_count: 4
  slug: australia-post-api-postage-result
- name: ClassificationV3Item
  property_count: 3
  slug: australia-post-classification-v3-item
- name: CountryMetadataRequest
  property_count: 1
  slug: australia-post-country-metadata-request
- name: CountryMetadataResponse
  property_count: 1
  slug: australia-post-country-metadata-response
- name: DrcResponse
  property_count: 3
  slug: australia-post-drc-response
- name: EventVO
  property_count: 9
  slug: australia-post-event-vo
- name: LandedCostV3Request
  property_count: 3
  slug: australia-post-landed-cost-v3-request
- name: LandedCostV3Response
  property_count: 7
  slug: australia-post-landed-cost-v3-response
- name: LetterThicknessResult
  property_count: 1
  slug: australia-post-letter-thickness-result
- name: OperationalCapabilitiesResponse
  property_count: 2
  slug: australia-post-operational-capabilities-response
- name: PointsResponse
  property_count: 1
  slug: australia-post-points-response
- name: PresentationCatalogue
  property_count: 2
  slug: australia-post-presentation-catalogue
- name: PresentationData
  property_count: 2
  slug: australia-post-presentation-data
- name: ProhibitionsV3Response
  property_count: 6
  slug: australia-post-prohibitions-v3-response
- name: Services
  property_count: 4
  slug: australia-post-services
- name: SettlementReport
  property_count: 1
  slug: australia-post-settlement-report
- name: Transactions
  property_count: 2
  slug: australia-post-transactions
- name: WorkCentreByIdResponse
  property_count: 1
  slug: australia-post-work-centre-by-id-response
- name: WorkCentresResponse
  property_count: 2
  slug: australia-post-work-centres-response
- name: ArticleVO
  property_count: 3
  slug: delivery-partner-articlevo
- name: AttachmentVO
  property_count: 2
  slug: delivery-partner-attachmentvo
- name: AuditVO
  property_count: 2
  slug: delivery-partner-auditvo
- name: DeliveryVO
  property_count: 2
  slug: delivery-partner-deliveryvo
- name: EventOriginatorVO
  property_count: 2
  slug: delivery-partner-eventoriginatorvo
- name: EventVO
  property_count: 9
  slug: delivery-partner-eventvo
- name: FacilityVO
  property_count: 1
  slug: delivery-partner-facilityvo
- name: LocationVO
  property_count: 2
  slug: delivery-partner-locationvo
- name: PersonVO
  property_count: 1
  slug: delivery-partner-personvo
- name: ProofOfDeliveryVO
  property_count: 5
  slug: delivery-partner-proofofdeliveryvo
- name: ServiceActionsVO
  property_count: 4
  slug: delivery-partner-serviceactionsvo
- name: SystemVO
  property_count: 2
  slug: delivery-partner-systemvo
- name: Address
  property_count: 12
  slug: locations-address
- name: Category
  property_count: 2
  slug: locations-category
- name: Hour
  property_count: 6
  slug: locations-hour
- name: Location
  property_count: 3
  slug: locations-location
- name: Point
  property_count: 17
  slug: locations-point
- name: PointsResponse
  property_count: 1
  slug: locations-pointsresponse
- name: Service
  property_count: 8
  slug: locations-service
- name: ServicesResponse
  property_count: 1
  slug: locations-servicesresponse
jsonld:
- class_count: 104
  name: Australia Post Context
  property_count: 252
  slug: australia-post-context
layout: provider
modified: '2026-10-21'
name: Australia Post
nav: Providers
network: true
overview: 'Australia Post publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Endpoints API, and 3 more. Tagged areas include Address Validation, Click and Collect, Delivery, E-Commerce, and Labels.


  The Australia Post catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Australia Post''s developer surface includes changelog, sandbox, pricing, authentication, documentation, getting-started guide, signup flow, and 48 more developer resources.'
plans:
- name: Australia Post Plans Pricing
  plan_count: 1
  slug: australia-post-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Australia Post Rate Limits
  slug: australia-post-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Australia Post — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: australia-post-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Australia Post API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 1
  slug: australia-post-rules
scopes:
- name: Australia Post Scopes
  scope_count: 1
  slug: australia-post-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 37
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 60.1
    developer_ergonomics: 58.9
    discoverability: 71.4
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/australia-post/australia-post-2026-06-20T172603.png
security:
- kind: authentication
  name: Australia Post Authentication
  slug: australia-post-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Australia Post Domain Security
  slug: australia-post-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Australia Post Vulnerability Disclosure
  slug: australia-post-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: calculate-domestic-parcel-postage
  slug: australia-post-calculate-domestic-parcel-postage
- name: calculate-international-parcel-postage
  slug: australia-post-calculate-international-parcel-postage
- name: check-international-export-compliance
  slug: australia-post-check-international-export-compliance
- name: find-post-office-locations
  slug: australia-post-find-post-office-locations
- name: reconcile-agency-transactions
  slug: australia-post-reconcile-agency-transactions
slug: australia-post
tags:
- Address Validation
- Click and Collect
- Delivery
- E-Commerce
- Labels
- Location
- Logistics
- Parcel Locker
- Postal
- Postage
- Shipping
- Tracking
- Australia
website: https://auspost.com.au/
---
