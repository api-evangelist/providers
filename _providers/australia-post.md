---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Australia Post Agentic Access
  operation_count: 9
  slug: australia-post-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 2
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
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Delivery Partner Endpoints API
  slug: open-australia-post-endpoints-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/australia-post-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/australia-post-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/australia-post-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/australia-post-domain-security.yml
- group: auth
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
  url: https://auspost.com.au/developers/help-support/
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
- name: Australia Post Finops
  service_category: Logistics / Shipping
  slug: australia-post-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/australia-post.png
json_schemas:
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
layout: provider
modified: '2026-06-13'
name: Australia Post
nav: Providers
network: true
overview: 'Australia Post publishes 1 API on the [APIs.io](https://apis.io/) network: Endpoints API. Tagged areas include Address Validation, Click and Collect, Delivery, E-Commerce, and Labels.


  The Australia Post catalog on APIs.io includes 1 Spectral governance ruleset.


  Australia Post''s developer surface includes authentication, documentation, getting-started guide, signup flow, and 14 more developer resources.'
plans:
- name: Australia Post Plans Pricing
  plan_count: 4
  slug: australia-post-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Australia Post Rate Limits
  slug: australia-post-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Australia Post API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: australia-post-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 54.8
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 47.4
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/australia-post/refs/heads/main/screenshots/australia-post-2026-06-20T172603.png
security:
- kind: authentication
  name: Australia Post Authentication
  slug: australia-post-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Australia Post Domain Security
  slug: australia-post-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Australia Post Vulnerability Disclosure
  slug: australia-post-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: australia-post
tags:
- Address Validation
- Click and Collect
- Delivery
- E-Commerce
- Labels
- Locations
- Logistics
- Parcel Locker
- Postal
- Postage
- Shipping
- Tracking
website: https://auspost.com.au/
---
