---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Shippo Agentic Access
  operation_count: 29
  slug: shippo-agentic-access
  summary_line: 29 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Validate and manage shipping addresses
  name: Shippo Addresses API
  slug: shippo-addresses-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Manage carrier account integrations
  name: Shippo Carrier Accounts API
  slug: shippo-carrier-accounts-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Define parcel dimensions and weight
  name: Shippo Parcels API
  slug: shippo-parcels-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Retrieve shipping rates from carriers
  name: Shippo Rates API
  slug: shippo-rates-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Request label refunds
  name: Shippo Refunds API
  slug: shippo-refunds-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Create and manage shipments
  name: Shippo Shipments API
  slug: shippo-shipments-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Track shipments across carriers
  name: Shippo Tracking API
  slug: shippo-tracking-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Purchase shipping labels
  name: Shippo Transactions API
  slug: shippo-transactions-api
- baseURL: https://api.goshippo.com
  baseurl_source: spec
  description: Manage webhook subscriptions
  name: Shippo Webhooks API
  slug: shippo-webhooks-api
artifact_total: 78
asyncapis:
- description: AsyncAPI 2.6 description of the Shippo Webhooks surface. Shippo delivers webhook events over HTTPS as POST requests to a subscriber-registered URL. Each delivery carries a JSON body with an envelope o
  name: Shippo Webhooks
  slug: shippo-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shippo Addresses API
  slug: open-shippo-addresses-api
- collection_type: open
  name: Shippo Addresses Carrier Accounts API
  slug: open-shippo-carrier-accounts-api
- collection_type: open
  name: Shippo Addresses Parcels API
  slug: open-shippo-parcels-api
- collection_type: open
  name: Shippo Addresses Rates API
  slug: open-shippo-rates-api
- collection_type: open
  name: Shippo Addresses Refunds API
  slug: open-shippo-refunds-api
- collection_type: open
  name: Shippo Addresses Shipments API
  slug: open-shippo-shipments-api
- collection_type: open
  name: Shippo Addresses Tracking API
  slug: open-shippo-tracking-api
- collection_type: open
  name: Shippo Addresses Transactions API
  slug: open-shippo-transactions-api
- collection_type: open
  name: Shippo Addresses Webhooks API
  slug: open-shippo-webhooks-api
- collection_type: open
  name: Shippo API
  slug: open-shippo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shippo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shippo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shippo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shippo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shippo
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goshippo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.goshippo.com/shippoapi/public-api
- group: build
  title: ''
  type: SDKs
  url: https://docs.goshippo.com/docs/guides_general/clientlibraries
- group: start
  title: ''
  type: GettingStarted
  url: https://support.goshippo.com/hc/en-us/articles/4404415886491-Shippo-API-Quick-Start-Guide
- group: commercial
  title: ''
  type: Pricing
  url: https://goshippo.com/pricing/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goshippo
- group: start
  title: ''
  type: DeveloperPortal
  url: https://goshippo.com/products/api
- group: company
  title: ''
  type: Website
  url: https://goshippo.com
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/goshippo/shippo-clawhub-skill
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.goshippo.com/llms.txt
created: '2025-03-01'
description: Shippo provides a robust shipping API architecture that helps developers drive efficiency at scale. The Shippo API covers the complete shipping lifecycle from pre-purchase rate shopping across 80+ carriers to label generation, package tracking, and returns management. SDKs are available for Python, JavaScript, PHP, Java, Ruby, and Node.js.
examples:
- key_count: 4
  name: Shippo Create Shipment Example
  slug: shippo-create-shipment-example
- key_count: 4
  name: Shippo Purchase Label Example
  slug: shippo-purchase-label-example
features:
- 'API Starter: 30 free labels/mo + 7¢/label'
- 'API Premier: custom volume discounts, 24/7 monitoring optional'
- 40+ shipping carriers (USPS, FedEx, UPS, DHL, Royal Mail, Canada Post, etc.)
- 'Address validation (US: included; non-US: $0.09 Starter, $0.06 Premier)'
- Tracking webhooks
- Returns labels
- Insurance
- Rating across carriers
- REST API at api.goshippo.com
- Default 250 req/min/token
- Bearer token auth
- Webhooks for shipment, transaction, batch events
- Carrier accounts management API
- Customs documents API
- Batch label creation
- API calls not associated with labels billed at API Starter rates
finops:
- name: Shippo Finops
  service_category: Shipping API
  slug: shippo-finops
graphqls:
- description: Shippo is a multi-carrier shipping API that provides complete shipping functionality including address validation, rate shopping across 80+ carriers, label generation, package tracking, returns manage
  name: Shippo GraphQL
  slug: shippo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippo.png
json_schemas:
- name: Address
  property_count: 16
  slug: shippo-address
- name: AddressCreateRequest
  property_count: 12
  slug: shippo-addresscreaterequest
- name: AddressPaginatedList
  property_count: 4
  slug: shippo-addresspaginatedlist
- name: CarrierAccount
  property_count: 8
  slug: shippo-carrieraccount
- name: CarrierAccountCreateRequest
  property_count: 4
  slug: shippo-carrieraccountcreaterequest
- name: CarrierAccountPaginatedList
  property_count: 4
  slug: shippo-carrieraccountpaginatedlist
- name: Parcel
  property_count: 10
  slug: shippo-parcel
- name: ParcelCreateRequest
  property_count: 7
  slug: shippo-parcelcreaterequest
- name: ParcelPaginatedList
  property_count: 4
  slug: shippo-parcelpaginatedlist
- name: Rate
  property_count: 14
  slug: shippo-rate
- name: RatePaginatedList
  property_count: 2
  slug: shippo-ratepaginatedlist
- name: Refund
  property_count: 5
  slug: shippo-refund
- name: RefundCreateRequest
  property_count: 2
  slug: shippo-refundcreaterequest
- name: RefundPaginatedList
  property_count: 4
  slug: shippo-refundpaginatedlist
- name: Shippo Shipment
  property_count: 11
  slug: shippo-shipment
- name: ShipmentCreateRequest
  property_count: 7
  slug: shippo-shipmentcreaterequest
- name: ShipmentPaginatedList
  property_count: 4
  slug: shippo-shipmentpaginatedlist
- name: TrackingStatus
  property_count: 10
  slug: shippo-trackingstatus
- name: TrackingWebhookRequest
  property_count: 3
  slug: shippo-trackingwebhookrequest
- name: Shippo Transaction
  property_count: 11
  slug: shippo-transaction
- name: TransactionCreateRequest
  property_count: 4
  slug: shippo-transactioncreaterequest
- name: TransactionPaginatedList
  property_count: 4
  slug: shippo-transactionpaginatedlist
- name: Webhook
  property_count: 7
  slug: shippo-webhook
- name: WebhookCreateRequest
  property_count: 3
  slug: shippo-webhookcreaterequest
json_structures:
- name: Shippo Shipment Structure
  property_count: 0
  slug: shippo-shipment-structure
- name: Shippo Structure
  property_count: 0
  slug: shippo-structure
jsonld:
- class_count: 41
  name: Shippo Context
  property_count: 18
  slug: shippo-context
layout: provider
modified: '2026-05-30'
name: Shippo
nav: Providers
network: true
overview: 'Shippo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Carrier Accounts API, Parcels API, and 6 more. Tagged areas include E-Commerce, Labels, Logistics, Returns, and Shipping.


  The Shippo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Shippo''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 11 more developer resources.'
plans:
- name: Shippo Plans Pricing
  plan_count: 2
  slug: shippo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Shippo Rate Limits
  slug: shippo-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Shippo API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: shippo-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Shippo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: shippo-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Shippo API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 7
  slug: shippo-rules
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 28.8
    contract_quality: 77.7
    developer_ergonomics: 73.8
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shippo/refs/heads/main/screenshots/shippo-2026-06-20T193822.png
security:
- kind: authentication
  name: Shippo Authentication
  slug: shippo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shippo Domain Security
  slug: shippo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Shippo Trust Center
  slug: shippo-trust-center
  summary_line: SOC 2, PCI DSS
skill_count: 1
skills:
- name: shippo-official
  slug: shippo-official
slug: shippo
tags:
- E-Commerce
- Labels
- Logistics
- Returns
- Shipping
- Tracking
website: https://goshippo.com
---
