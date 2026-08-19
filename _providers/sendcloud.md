---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Sendcloud Agentic Access
  operation_count: 94
  slug: sendcloud-agentic-access
  summary_line: 94 operations · 42 acting
api_count: 24
apis:
- description: The Address API from Sendcloud — 1 operation(s) for address.
  name: Sendcloud Address API
  slug: sendcloud-address-api
- description: The Analytics API from Sendcloud — 2 operation(s) for analytics.
  name: Sendcloud Analytics API
  slug: sendcloud-analytics-api
- description: The Broadcast API from Sendcloud — 1 operation(s) for broadcast.
  name: Sendcloud Broadcast API
  slug: sendcloud-broadcast-api
- description: The Connections API from Sendcloud — 2 operation(s) for connections.
  name: Sendcloud Connections API
  slug: sendcloud-connections-api
- description: The Customs Documents Download API from Sendcloud — 2 operation(s) for customs documents download.
  name: Sendcloud Customs Documents Download API
  slug: sendcloud-customs-documents-download-api
- description: Integration exception logs API
  name: Sendcloud Exception logs API
  slug: sendcloud-exception-logs-api
- description: The Integrations API from Sendcloud — 6 operation(s) for integrations.
  name: Sendcloud Integrations API
  slug: sendcloud-integrations-api
- description: The Label Download API from Sendcloud — 4 operation(s) for label download.
  name: Sendcloud Label Download API
  slug: sendcloud-label-download-api
- description: The Labels API from Sendcloud — 2 operation(s) for labels.
  name: Sendcloud Labels API
  slug: sendcloud-labels-api
- description: The OAuth2 API from Sendcloud — 1 operation(s) for oauth2.
  name: Sendcloud OAuth2 API
  slug: sendcloud-oauth2-api
- description: OrderAPI
  name: Sendcloud Orders API
  slug: sendcloud-orders-api
- description: The Parcel Documents API from Sendcloud — 2 operation(s) for parcel documents.
  name: Sendcloud Parcel Documents API
  slug: sendcloud-parcel-documents-api
- description: The Parcel Tracking API from Sendcloud — 2 operation(s) for parcel tracking.
  name: Sendcloud Parcel Tracking API
  slug: sendcloud-parcel-tracking-api
- description: Get insights about parcels
  name: Sendcloud Parcels API
  slug: sendcloud-parcels-api
- description: Get insights about products
  name: Sendcloud Products API
  slug: sendcloud-products-api
- description: Generate data exports and reports.
  name: Sendcloud Reporting API
  slug: sendcloud-reporting-api
- description: The Returns API from Sendcloud — 6 operation(s) for returns.
  name: Sendcloud Returns API
  slug: sendcloud-returns-api
- description: Service Points API
  name: Sendcloud Service Points API
  slug: sendcloud-service-points-api
- description: OrderLabelAPI
  name: Sendcloud Ship an Order API
  slug: sendcloud-ship-an-order-api
- description: Shipments API
  name: Sendcloud Shipments API
  slug: sendcloud-shipments-api
- description: The Subscriptions API from Sendcloud — 2 operation(s) for subscriptions.
  name: Sendcloud Subscriptions API
  slug: sendcloud-subscriptions-api
- description: The Tracking API from Sendcloud — 1 operation(s) for tracking.
  name: Sendcloud Tracking API
  slug: sendcloud-tracking-api
- description: Get insights about average transit times per carriers and shipping methods
  name: Sendcloud Transit times API
  slug: sendcloud-transit-times-api
- description: Get list of carriers and shipping methods a user ever used
  name: Sendcloud User Carriers and Shipping Methods API
  slug: sendcloud-user-carriers-and-shipping-methods-api
arazzos:
- description: Announce a shipment synchronously, then retrieve the return portal URL customers use to create a return.
  name: Sendcloud Announce a Shipment and Get its Return Portal URL
  slug: sendcloud-announce-shipment-return-portal-workflow
- description: Announce a shipment synchronously, then verify it and read its label document link.
  name: Sendcloud Announce a Shipment with Label
  slug: sendcloud-announce-shipment-with-label-workflow
- description: List parcels filtered by status, then request a single bulk PDF of their labels.
  name: Sendcloud Bulk Print Labels for Recent Parcels
  slug: sendcloud-bulk-print-labels-workflow
- description: Look up a shipment by id, then cancel it and branch on whether cancellation was immediate or queued.
  name: Sendcloud Cancel a Shipment with Confirmation
  slug: sendcloud-cancel-shipment-workflow
- description: Create a parcel with a label request, then retrieve its PDF label download URLs.
  name: Sendcloud Create a Parcel and Fetch its Label
  slug: sendcloud-create-parcel-fetch-label-workflow
- description: Create a labelled parcel, then retrieve the return portal URL a customer can use to start a return.
  name: Sendcloud Create a Parcel and Get its Return Portal URL
  slug: sendcloud-create-parcel-return-portal-workflow
- description: Create a labelled parcel, then poll its tracking until it is en route.
  name: Sendcloud Create a Parcel and Track its Shipment
  slug: sendcloud-create-parcel-track-shipment-workflow
- description: Create a standalone return, inspect it, and request cancellation only when it is still cancellable.
  name: Sendcloud Create a Return and Cancel It If Cancellable
  slug: sendcloud-create-return-cancel-if-cancellable-workflow
- description: Register a parcel labelled outside Sendcloud for tracking, then retrieve its tracking record.
  name: Sendcloud Register an External Parcel and Track It
  slug: sendcloud-register-external-parcel-track-workflow
- description: Request a label for an order asynchronously, then poll the created parcel until it has a label.
  name: Sendcloud Ship an Order Asynchronously and Poll the Parcel
  slug: sendcloud-ship-order-async-poll-parcel-workflow
- description: Request a label for an order synchronously, then pull its v3 tracking detail.
  name: Sendcloud Ship an Order Synchronously and Track It
  slug: sendcloud-ship-order-sync-track-workflow
- description: Validate a return payload, create the return, then retrieve its full detail.
  name: Sendcloud Validate and Create a Return
  slug: sendcloud-validate-create-return-workflow
artifact_total: 152
collections:
- collection_type: postman
  name: Shipments
  slug: postman-sendcloud-shipments
- collection_type: postman
  name: Analytics
  slug: postman-sendcloud-v2-analytics
- collection_type: postman
  name: Integrations
  slug: postman-sendcloud-v2-integrations
- collection_type: postman
  name: Labels
  slug: postman-sendcloud-v2-labels
- collection_type: postman
  name: Parcel Documents
  slug: postman-sendcloud-v2-parcel-documents
- collection_type: postman
  name: Parcels
  slug: postman-sendcloud-v2-parcels
- collection_type: postman
  name: Reporting
  slug: postman-sendcloud-v2-reporting
- collection_type: postman
  name: Tracking parcels
  slug: postman-sendcloud-v2-tracking
- collection_type: postman
  name: Webhooks
  slug: postman-sendcloud-v2-webhooks
- collection_type: postman
  name: Analytics
  slug: postman-sendcloud-v3-analytics
- collection_type: postman
  name: Event Subscriptions API
  slug: postman-sendcloud-v3-event-subscriptions
- collection_type: postman
  name: Integrations
  slug: postman-sendcloud-v3-integrations
- collection_type: postman
  name: Orders
  slug: postman-sendcloud-v3-orders
- collection_type: postman
  name: Parcel documents API
  slug: postman-sendcloud-v3-parcel-documents
- collection_type: postman
  name: Parcel Tracking API
  slug: postman-sendcloud-v3-parcel-tracking
- collection_type: postman
  name: Reporting
  slug: postman-sendcloud-v3-reporting
- collection_type: postman
  name: Returns
  slug: postman-sendcloud-v3-returns
- collection_type: postman
  name: Service Points API [BETA]
  slug: postman-sendcloud-v3-service-points
- collection_type: postman
  name: Ship an Order
  slug: postman-sendcloud-v3-ship-an-order
- collection_type: postman
  name: Webhooks
  slug: postman-sendcloud-v3-webhooks
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shipments Address API
  slug: open-sendcloud-address-api
- collection_type: open
  name: Shipments Address Analytics API
  slug: open-sendcloud-analytics-api
- collection_type: open
  name: Shipments Address Broadcast API
  slug: open-sendcloud-broadcast-api
- collection_type: open
  name: Shipments Address Connections API
  slug: open-sendcloud-connections-api
- collection_type: open
  name: Shipments Address Customs Documents Download API
  slug: open-sendcloud-customs-documents-download-api
- collection_type: open
  name: Shipments Address Exception logs API
  slug: open-sendcloud-exception-logs-api
- collection_type: open
  name: Shipments Address Integrations API
  slug: open-sendcloud-integrations-api
- collection_type: open
  name: Shipments Address Label Download API
  slug: open-sendcloud-label-download-api
- collection_type: open
  name: Shipments Address Labels API
  slug: open-sendcloud-labels-api
- collection_type: open
  name: Shipments Address OAuth2 API
  slug: open-sendcloud-oauth2-api
- collection_type: open
  name: Shipments Address Orders API
  slug: open-sendcloud-orders-api
- collection_type: open
  name: Shipments Address Parcel Documents API
  slug: open-sendcloud-parcel-documents-api
- collection_type: open
  name: Shipments Address Parcel Tracking API
  slug: open-sendcloud-parcel-tracking-api
- collection_type: open
  name: Shipments Address Parcels API
  slug: open-sendcloud-parcels-api
- collection_type: open
  name: Shipments Address Products API
  slug: open-sendcloud-products-api
- collection_type: open
  name: Shipments Address Reporting API
  slug: open-sendcloud-reporting-api
- collection_type: open
  name: Shipments Address Returns API
  slug: open-sendcloud-returns-api
- collection_type: open
  name: Shipments Address Service Points API
  slug: open-sendcloud-service-points-api
- collection_type: open
  name: Shipments Address Ship an Order API
  slug: open-sendcloud-ship-an-order-api
- collection_type: open
  name: Address Shipments API
  slug: open-sendcloud-shipments-api
- collection_type: open
  name: Shipments
  slug: open-sendcloud-shipments
- collection_type: open
  name: Shipments Address Subscriptions API
  slug: open-sendcloud-subscriptions-api
- collection_type: open
  name: Shipments Address Tracking API
  slug: open-sendcloud-tracking-api
- collection_type: open
  name: Shipments Address Transit times API
  slug: open-sendcloud-transit-times-api
- collection_type: open
  name: Shipments Address User Carriers and Shipping Methods API
  slug: open-sendcloud-user-carriers-and-shipping-methods-api
- collection_type: open
  name: Analytics
  slug: open-sendcloud-v2-analytics
- collection_type: open
  name: Integrations
  slug: open-sendcloud-v2-integrations
- collection_type: open
  name: Labels
  slug: open-sendcloud-v2-labels
- collection_type: open
  name: Parcel Documents
  slug: open-sendcloud-v2-parcel-documents
- collection_type: open
  name: Parcels
  slug: open-sendcloud-v2-parcels
- collection_type: open
  name: Reporting
  slug: open-sendcloud-v2-reporting
- collection_type: open
  name: Tracking parcels
  slug: open-sendcloud-v2-tracking
- collection_type: open
  name: Webhooks
  slug: open-sendcloud-v2-webhooks
- collection_type: open
  name: Analytics
  slug: open-sendcloud-v3-analytics
- collection_type: open
  name: Event Subscriptions API
  slug: open-sendcloud-v3-event-subscriptions
- collection_type: open
  name: Integrations
  slug: open-sendcloud-v3-integrations
- collection_type: open
  name: Orders
  slug: open-sendcloud-v3-orders
- collection_type: open
  name: Parcel documents API
  slug: open-sendcloud-v3-parcel-documents
- collection_type: open
  name: Parcel Tracking API
  slug: open-sendcloud-v3-parcel-tracking
- collection_type: open
  name: Reporting
  slug: open-sendcloud-v3-reporting
- collection_type: open
  name: Returns
  slug: open-sendcloud-v3-returns
- collection_type: open
  name: Service Points API [BETA]
  slug: open-sendcloud-v3-service-points
- collection_type: open
  name: Ship an Order
  slug: open-sendcloud-v3-ship-an-order
- collection_type: open
  name: Webhooks
  slug: open-sendcloud-v3-webhooks
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/sendcloud-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendcloud-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sendcloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendcloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendcloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sendcloud-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendcloud/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-announce-shipment-return-portal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-announce-shipment-with-label-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-bulk-print-labels-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-cancel-shipment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-parcel-fetch-label-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-parcel-return-portal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-parcel-track-shipment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-return-cancel-if-cancellable-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-register-external-parcel-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-ship-order-async-poll-parcel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-ship-order-sync-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-validate-create-return-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendcloud.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendcloud.dev
- group: docs
  title: ''
  type: Documentation
  url: https://sendcloud.dev/docs/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://sendcloud.dev/api/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://sendcloud.dev/docs/getting-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://sendcloud.dev/docs/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://sendcloud.dev/docs/getting-started/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://sendcloud.dev/docs/getting-started/rate-limits/
- group: design
  title: ''
  type: Pagination
  url: https://sendcloud.dev/api/v3/pagination/
- group: docs
  title: ''
  type: APIVersionGuide
  url: https://sendcloud.dev/docs/getting-started/api-version-guide/
- group: docs
  title: ''
  type: MigrationGuide
  url: https://sendcloud.dev/docs/getting-started/migration-guidelines-for-api-v3/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendcloud.dev/api/v3/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendcloud.dev/api/v2/changelog/
- group: other
  title: ''
  type: Glossary
  url: https://sendcloud.dev/docs/getting-started/glossary/
- group: build
  title: ''
  type: Postman
  url: https://sendcloud.dev/docs/getting-started/postman/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendcloud.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sendcloud.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.sendcloud.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://releaselog.sendcloud.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sendcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendcloud/
- group: agent
  title: ''
  type: LlmsText
  url: https://sendcloud.dev/llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: rules/sendcloud-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sendcloud-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sendcloud-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/sendcloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendcloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sendcloud-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Sendcloud/SendCloud-API-PHP-Wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Sendcloud/api-integration-example
created: '2026-05-25'
description: Sendcloud is Europe's leading shipping platform for e-commerce, headquartered in Eindhoven, Netherlands. The platform connects 30,000+ merchants to 160+ carriers (DHL, DPD, UPS, GLS, FedEx, PostNL, bpost, La Poste, Royal Mail, Hermes, and many more) and 100+ commerce / WMS / marketplace integrations across the UK, Netherlands, Belgium, France, Germany, Austria, Italy, and Spain. The Sendcloud APIs cover the full fulfillment lifecycle — Orders, Ship an Order, Shipments, Service Points, Parcel Tracking, Parcel Documents, Returns, Event Subscriptions, Webhooks, Integrations, Analytics, and Reporting — over a versioned v2 / v3 REST surface on https://panel.sendcloud.sc, authenticated with HTTP Basic (public + private key) or OAuth 2.0 client credentials.
examples:
- key_count: 6
  name: Sendcloud Announce Shipment Example
  slug: sendcloud-announce-shipment-example
- key_count: 7
  name: Sendcloud Create Return Example
  slug: sendcloud-create-return-example
- key_count: 2
  name: Sendcloud List Service Points Example
  slug: sendcloud-list-service-points-example
features:
- description: DHL, DPD, UPS, GLS, FedEx, PostNL, bpost, La Poste, Royal Mail, Hermes, Colissimo, Chronopost, Mondial Relay, and many more.
  name: 160+ European carriers
- description: Shopify, WooCommerce, Magento, PrestaShop, BigCommerce, Amazon, eBay, Etsy, Bol.com, Lightspeed.
  name: 100+ commerce / WMS / marketplace integrations
- description: Aggregated parcel-shop, locker, and post-office network exposed through one Service Points API.
  name: Service points across Europe
- description: Merchant-branded tracking pages, email / SMS / WhatsApp delivery notifications.
  name: Branded tracking
- description: Self-service consumer return portal with drop-off, pickup, postbox, and in-store options.
  name: Returns portal
- description: Multiple physical parcels announced under a single shipment.
  name: Multicollo (multi-parcel) shipments
- description: Warehouse-floor pick-and-pack workflow.
  name: Pack & Go
- description: Versioned v2 and v3 REST surface.
  name: REST API at panel.sendcloud.sc
- description: Public/private key Basic auth or token exchange at https://account.sendcloud.com/oauth2/token (scope api).
  name: HTTP Basic + OAuth 2.0 client credentials
- description: v3 list endpoints return next/previous cursors.
  name: Cursor-based pagination
- description: parcel-status-changed, return-created and other typed events delivered to merchant endpoints.
  name: Typed event subscriptions and webhooks
- description: 1,000 GET / minute and 100 unsafe / minute (15 burst / second) per integration.
  name: Rate limits by HTTP safety class
- description: Subscription priced in EUR; carrier postage in local currency.
  name: Multi-currency billing
- description: Official Postman and downloadable OpenAPI for v3 surfaces.
  name: Postman collection + OpenAPI v3
- description: Sendcloud-Partner-Id header for third-party platforms calling on behalf of merchants.
  name: Marketplace integration guidelines
finops:
- name: Sendcloud Finops
  service_category: Shipping API
  slug: sendcloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: DeliveryOption
  property_count: 0
  slug: sendcloud-deliveryoption
- name: Sendcloud Order
  property_count: 0
  slug: sendcloud-order
- name: Sendcloud ParcelTrackingCreateRequest
  property_count: 0
  slug: sendcloud-parceltrackingcreaterequest
- name: Sendcloud ParcelTrackingResponse
  property_count: 0
  slug: sendcloud-parceltrackingresponse
- name: Price Object
  property_count: 2
  slug: sendcloud-price
- name: Return Object
  property_count: 33
  slug: sendcloud-return
- name: Service Point Search Result
  property_count: 0
  slug: sendcloud-servicepoint
- name: Service Point Address
  property_count: 5
  slug: sendcloud-servicepointaddress
- name: Service Point
  property_count: 13
  slug: sendcloud-servicepointdetail
json_structures:
- name: Sendcloud Return Structure
  property_count: 7
  slug: sendcloud-return-structure
- name: Sendcloud Shipment Structure
  property_count: 9
  slug: sendcloud-shipment-structure
jsonld:
- class_count: 40
  name: Sendcloud Context
  property_count: 17
  slug: sendcloud-context
layout: provider
modified: '2026-05-25'
name: Sendcloud
nav: Providers
network: true
overview: 'Sendcloud publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Address API, Analytics API, Broadcast API, and 21 more. Tagged areas include Shipping, Logistics, Ecommerce, Carriers, and Labels.


  The Sendcloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sendcloud''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 42 more developer resources.'
plans:
- name: Sendcloud Plans Pricing
  plan_count: 6
  slug: sendcloud-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 3
  name: Sendcloud Rate Limits
  slug: sendcloud-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sendcloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sendcloud-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Sendcloud API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 8
  slug: sendcloud-rules
scopes:
- name: Sendcloud Scopes
  scope_count: 1
  slug: sendcloud-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 65.8
  delta: 0.7
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 78.3
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 54.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/screenshots/sendcloud-2026-06-20T193651.png
security:
- kind: authentication
  name: Sendcloud Authentication
  slug: sendcloud-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Sendcloud Domain Security
  slug: sendcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sendcloud Trust Center
  slug: sendcloud-trust-center
  summary_line: ISO 27001, GDPR
slug: sendcloud
solutions:
- description: EUR 33/month - 400 labels/month, 3 integrations, branded tracking.
  name: Lite
- description: EUR 99/month - 1,000 labels/month, Pack & Go, WhatsApp notifications.
  name: Growth
- description: EUR 195/month - 10,000 labels/month, return management module, analytics.
  name: Premium
- description: EUR 799/month - 30,000 labels/month, dedicated CSM, marketplace solutions.
  name: Pro
- description: Custom volumes, SLAs, custom development.
  name: Enterprise
tags:
- Shipping
- Logistics
- Ecommerce
- Carriers
- Labels
- Returns
- Tracking
- Europe
use_cases:
- description: Direct-to-consumer brands shipping across the EU from a central warehouse.
  name: European D2C fulfillment
- description: UK / EU cross-border shipping with customs documents and carrier routing.
  name: Cross-border ecommerce
- description: Brands selling on Amazon, eBay, Etsy, and Bol.com aggregating fulfillment in one platform.
  name: Marketplace shipping
- description: Warehouse providers calling Sendcloud on behalf of multiple merchants via the Integrations API and Sendcloud-Partner-Id header.
  name: 3PL / WMS integration
- description: Merchant-branded tracking, return portal, and notifications.
  name: Branded post-purchase experience
- description: Self-service returns with multi-method drop-off / pickup.
  name: Returns automation
website: https://www.sendcloud.com
---
