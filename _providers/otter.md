---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Otter Agentic Access
  operation_count: 80
  slug: otter-agentic-access
  summary_line: 80 operations · 59 acting
api_count: 19
apis:
- description: Endpoints to manage store onboarding and status
  name: Otter Account Pairing Endpoints API
  slug: otter-account-pairing-endpoints-api
- description: Endpoints to handle token management.
  name: Otter Auth Endpoints API
  slug: otter-auth-endpoints-api
- description: Endpoints for callback management.
  name: Otter Callback Endpoints API
  slug: otter-callback-endpoints-api
- description: Endpoints to manage delivery.
  name: Otter Delivery Endpoints API
  slug: otter-delivery-endpoints-api
- description: Endpoints to get orders directly.
  name: Otter Direct Orders Endpoints API
  slug: otter-direct-orders-endpoints-api
- description: Endpoints to handle financial data.
  name: Otter Finance Endpoints API
  slug: otter-finance-endpoints-api
- description: Endpoints to interact with product inventory.
  name: Otter Inventory Endpoints API
  slug: otter-inventory-endpoints-api
- description: Endpoints to manage loyalty.
  name: Otter Manager Loyalty Endpoints API
  slug: otter-manager-loyalty-endpoints-api
- description: Endpoints for applications managing menus related data and operations.
  name: Otter Manager Menu Endpoints API
  slug: otter-manager-menu-endpoints-api
- description: Endpoints for applications managing order related data and operations.
  name: Otter Manager Order Endpoints API
  slug: otter-manager-order-endpoints-api
- description: Endpoints for applications managing storefront related data and operations.
  name: Otter Manager Storefront Endpoints API
  slug: otter-manager-storefront-endpoints-api
- description: The Market Intel Endpoints API from Otter — 1 operation(s) for market intel endpoints.
  name: Otter Market Intel Endpoints API
  slug: otter-market-intel-endpoints-api
- description: Endpoints to manage menus.
  name: Otter Menus Endpoints API
  slug: otter-menus-endpoints-api
- description: Endpoints to manage orders for a store.
  name: Otter Orders Endpoints API
  slug: otter-orders-endpoints-api
- description: Endpoints to interact with with organizations/brands/stores and with integration connections.
  name: Otter Organization Endpoints API
  slug: otter-organization-endpoints-api
- description: Endpoints to ping and test system authentication.
  name: Otter Ping Endpoints API
  slug: otter-ping-endpoints-api
- description: Endpoints to reports generation operations
  name: Otter Reports Endpoints API
  slug: otter-reports-endpoints-api
- description: Endpoints for review operations
  name: Otter Reviews Endpoints API
  slug: otter-reviews-endpoints-api
- description: Endpoints to manage storefront state
  name: Otter Storefront Endpoints API
  slug: otter-storefront-endpoints-api
artifact_total: 978
collections:
- collection_type: open
  name: Public API
  slug: open-otter-public-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/otter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/otter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/otter-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/otter-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryotter.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer-guides.tryotter.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.tryotter.com/hc/en-us/articles/22694653065107-API-Documentation
- group: company
  title: ''
  type: Blog
  url: https://www.tryotter.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/try-otter
- group: other
  title: ''
  type: X
  url: https://twitter.com/try_otter
- group: design
  title: ''
  type: SpectralRules
  url: rules/otter-public-api-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/otter-public-api-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/otter-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/otter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/otter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/otter-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryotter.com/pricing
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/api-evangelist/otter
created: '2026-06-02'
description: Otter (TryOtter) is a Restaurant Operating System used by hundreds of thousands of restaurants worldwide to aggregate delivery and online orders, consolidate menus, analyze sales, and control third-party delivery services from one place. For developers and integration partners, Otter publishes a Public API (OpenAPI 3.0, OAuth 2.0) and developer guides spanning account pairing, orders, menus, delivery, finance, reports, reviews, storefront, loyalty, organization, and inventory — with HMAC-signed webhooks for event-driven integration. Onboarding begins by registering an application, configuring webhooks, and onboarding stores; authentication and the account-specific base URL are provisioned through an Otter account representative.
examples:
- key_count: 9
  name: Public Api Accept Delivery Callback Request Example
  slug: public-api-accept-delivery-callback-request-example
- key_count: 24
  name: Public Api Accept Delivery Event Example
  slug: public-api-accept-delivery-event-example
- key_count: 4
  name: Public Api Additional Charge Example
  slug: public-api-additional-charge-example
- key_count: 8
  name: Public Api Address Example
  slug: public-api-address-example
- key_count: 2
  name: Public Api Allergen Classification Example
  slug: public-api-allergen-classification-example
- key_count: 5
  name: Public Api Bootstrap Menu Request Example
  slug: public-api-bootstrap-menu-request-example
- key_count: 2
  name: Public Api Brand Example
  slug: public-api-brand-example
- key_count: 3
  name: Public Api Brand Info Example
  slug: public-api-brand-info-example
- key_count: 1
  name: Public Api Bulk Update Item Status Example
  slug: public-api-bulk-update-item-status-example
- key_count: 1
  name: Public Api Cancel Delivery Callback Request Example
  slug: public-api-cancel-delivery-callback-request-example
- key_count: 1
  name: Public Api Cancel Delivery Event Example
  slug: public-api-cancel-delivery-event-example
- key_count: 2
  name: Public Api Card Info Example
  slug: public-api-card-info-example
- key_count: 6
  name: Public Api Category Example
  slug: public-api-category-example
- key_count: 1
  name: Public Api Composite Finance Line Example
  slug: public-api-composite-finance-line-example
- key_count: 2
  name: Public Api Compute Applicable Rewards Request Example
  slug: public-api-compute-applicable-rewards-request-example
- key_count: 1
  name: Public Api Compute Applicable Rewards Response Example
  slug: public-api-compute-applicable-rewards-response-example
- key_count: 1
  name: Public Api Connection Example
  slug: public-api-connection-example
- key_count: 5
  name: Public Api Courier Example
  slug: public-api-courier-example
- key_count: 2
  name: Public Api Courier Service Delivery Info Example
  slug: public-api-courier-service-delivery-info-example
- key_count: 1
  name: Public Api Create Connection Request Example
  slug: public-api-create-connection-request-example
- key_count: 6
  name: Public Api Create Shipment Line Item Example
  slug: public-api-create-shipment-line-item-example
- key_count: 2
  name: Public Api Create Shipment Request Example
  slug: public-api-create-shipment-request-example
- key_count: 1
  name: Public Api Create Shipment Response Example
  slug: public-api-create-shipment-response-example
- key_count: 1
  name: Public Api Create User Request Example
  slug: public-api-create-user-request-example
- key_count: 1
  name: Public Api Create User Response Example
  slug: public-api-create-user-response-example
- key_count: 15
  name: Public Api Custom Bulk Resolution Options Example
  slug: public-api-custom-bulk-resolution-options-example
- key_count: 8
  name: Public Api Customer Payment Example
  slug: public-api-customer-payment-example
- key_count: 4
  name: Public Api Customer Payment V2 Example
  slug: public-api-customer-payment-v2-example
- key_count: 1
  name: Public Api Customer Tip Example
  slug: public-api-customer-tip-example
- key_count: 1
  name: Public Api Default Modifier Selection Data Example
  slug: public-api-default-modifier-selection-data-example
- key_count: 2
  name: Public Api Default Modifier Selection Example
  slug: public-api-default-modifier-selection-example
- key_count: 2
  name: Public Api Delivery Cost Example
  slug: public-api-delivery-cost-example
- key_count: 1
  name: Public Api Delivery Fee Example
  slug: public-api-delivery-fee-example
- key_count: 7
  name: Public Api Delivery Info Example
  slug: public-api-delivery-info-example
- key_count: 2
  name: Public Api Delivery Metadata Example
  slug: public-api-delivery-metadata-example
- key_count: 14
  name: Public Api Delivery Status Update Event Example
  slug: public-api-delivery-status-update-event-example
- key_count: 12
  name: Public Api Delivery Status Update Request Example
  slug: public-api-delivery-status-update-request-example
- key_count: 2
  name: Public Api Delivery Window Example
  slug: public-api-delivery-window-example
- key_count: 1
  name: Public Api Dietary Classification Example
  slug: public-api-dietary-classification-example
- key_count: 2
  name: Public Api Discover Stores Event Result Example
  slug: public-api-discover-stores-event-result-example
- key_count: 2
  name: Public Api Discovered Store Example
  slug: public-api-discovered-store-example
- key_count: 2
  name: Public Api Distance Example
  slug: public-api-distance-example
- key_count: 2
  name: Public Api Dropoff Info Example
  slug: public-api-dropoff-info-example
- key_count: 2
  name: Public Api Dropoff Instructions Example
  slug: public-api-dropoff-instructions-example
- key_count: 9
  name: Public Api Eater Order Example
  slug: public-api-eater-order-example
- key_count: 4
  name: Public Api Eater Order History Request Example
  slug: public-api-eater-order-history-request-example
- key_count: 2
  name: Public Api Eater Order History Response Example
  slug: public-api-eater-order-history-response-example
- key_count: 2
  name: Public Api Energy Kcal Example
  slug: public-api-energy-kcal-example
- key_count: 4
  name: Public Api Enrollment Field Example
  slug: public-api-enrollment-field-example
- key_count: 1
  name: Public Api Entity Path Override Rule Example
  slug: public-api-entity-path-override-rule-example
- key_count: 2
  name: Public Api Error Detail Example
  slug: public-api-error-detail-example
- key_count: 2
  name: Public Api Error Message Example
  slug: public-api-error-message-example
- key_count: 2
  name: Public Api Event Callback Error Example
  slug: public-api-event-callback-error-example
- key_count: 3
  name: Public Api Event Notification Base Example
  slug: public-api-event-notification-base-example
- key_count: 4
  name: Public Api Event Notification Example
  slug: public-api-event-notification-example
- key_count: 3
  name: Public Api Event Result Metadata Example
  slug: public-api-event-result-metadata-example
- key_count: 2
  name: Public Api Existing Credential Example
  slug: public-api-existing-credential-example
- key_count: 2
  name: Public Api Exposed Third Party Info Example
  slug: public-api-exposed-third-party-info-example
- key_count: 1
  name: Public Api Fetch Credentials Event Example
  slug: public-api-fetch-credentials-event-example
- key_count: 19
  name: Public Api Financial Data Example
  slug: public-api-financial-data-example
- key_count: 4
  name: Public Api Financial Invoice Example
  slug: public-api-financial-invoice-example
- key_count: 12
  name: Public Api Financial Transaction Example
  slug: public-api-financial-transaction-example
- key_count: 2
  name: Public Api Fulfilled Credential Example
  slug: public-api-fulfilled-credential-example
- key_count: 7
  name: Public Api Fulfillment Info Example
  slug: public-api-fulfillment-info-example
- key_count: 1
  name: Public Api Fulfillment Mode Override Rule Example
  slug: public-api-fulfillment-mode-override-rule-example
- key_count: 2
  name: Public Api Fulfillment Path Entity Example
  slug: public-api-fulfillment-path-entity-example
- key_count: 6
  name: Public Api Generate Report Multi Request Example
  slug: public-api-generate-report-multi-request-example
- key_count: 1
  name: Public Api Generate Report Response Example
  slug: public-api-generate-report-response-example
- key_count: 1
  name: Public Api Get Enrollment Config Response Example
  slug: public-api-get-enrollment-config-response-example
- key_count: 2
  name: Public Api Get Report Status Response Example
  slug: public-api-get-report-status-response-example
- key_count: 2
  name: Public Api Get Store Details Event Result Example
  slug: public-api-get-store-details-event-result-example
- key_count: 1
  name: Public Api Get User Response Example
  slug: public-api-get-user-response-example
- key_count: 5
  name: Public Api Hour Interval Example
  slug: public-api-hour-interval-example
- key_count: 3
  name: Public Api Hours Data Example
  slug: public-api-hours-data-example
- key_count: 1
  name: Public Api Hours Example
  slug: public-api-hours-example
- key_count: 4
  name: Public Api Hydra Token Example
  slug: public-api-hydra-token-example
- key_count: 2
  name: Public Api Intent To Cancel Event Example
  slug: public-api-intent-to-cancel-event-example
- key_count: 2
  name: Public Api Inventory Summaries Response Example
  slug: public-api-inventory-summaries-response-example
- key_count: 8
  name: Public Api Inventory Summary Example
  slug: public-api-inventory-summary-example
- key_count: 4
  name: Public Api Invoice Payout Info Example
  slug: public-api-invoice-payout-info-example
- key_count: 5
  name: Public Api Item 2 Example
  slug: public-api-item-2-example
- key_count: 3
  name: Public Api Item 3 Example
  slug: public-api-item-3-example
- key_count: 5
  name: Public Api Item 4 Example
  slug: public-api-item-4-example
- key_count: 1
  name: Public Api Item Added Modification Example
  slug: public-api-item-added-modification-example
- key_count: 14
  name: Public Api Item Example
  slug: public-api-item-example
- key_count: 11
  name: Public Api Item Modifier Example
  slug: public-api-item-modifier-example
- key_count: 3
  name: Public Api Item Price Override Example
  slug: public-api-item-price-override-example
- key_count: 2
  name: Public Api Item Selector Example
  slug: public-api-item-selector-example
- key_count: 2
  name: Public Api Item Status Example
  slug: public-api-item-status-example
- key_count: 2
  name: Public Api Item Tax Example
  slug: public-api-item-tax-example
- key_count: 9
  name: Public Api Item Update Request Example
  slug: public-api-item-update-request-example
- key_count: 2
  name: Public Api Job Reference Example
  slug: public-api-job-reference-example
- key_count: 2
  name: Public Api List Brands Response Example
  slug: public-api-list-brands-response-example
- key_count: 2
  name: Public Api List Shipments Response Example
  slug: public-api-list-shipments-response-example
- key_count: 2
  name: Public Api List Stores Response Example
  slug: public-api-list-stores-response-example
- key_count: 2
  name: Public Api Location Example
  slug: public-api-location-example
- key_count: 1
  name: Public Api Loyalty Info Example
  slug: public-api-loyalty-info-example
- key_count: 2
  name: Public Api Manager Cancel Order Request Example
  slug: public-api-manager-cancel-order-request-example
- key_count: 1
  name: Public Api Manager Confirm Order Request Example
  slug: public-api-manager-confirm-order-request-example
- key_count: 2
  name: Public Api Manager Item Issue Example
  slug: public-api-manager-item-issue-example
- key_count: 2
  name: Public Api Manager Item Issues Example
  slug: public-api-manager-item-issues-example
- key_count: 1
  name: Public Api Manager Order Cancel Details Example
  slug: public-api-manager-order-cancel-details-example
- key_count: 2
  name: Public Api Manager Order Issue Example
  slug: public-api-manager-order-issue-example
- key_count: 2
  name: Public Api Manager Order Issues Example
  slug: public-api-manager-order-issues-example
- key_count: 2
  name: Public Api Marketintel Coordinates Example
  slug: public-api-marketintel-coordinates-example
- key_count: 5
  name: Public Api Marketintel Geo Location Information Example
  slug: public-api-marketintel-geo-location-information-example
- key_count: 3
  name: Public Api Marketintel Hours Data Example
  slug: public-api-marketintel-hours-data-example
- key_count: 2
  name: Public Api Marketintel Location Based Information Example
  slug: public-api-marketintel-location-based-information-example
- key_count: 2
  name: Public Api Marketintel Regular Hours Example
  slug: public-api-marketintel-regular-hours-example
- key_count: 3
  name: Public Api Marketintel Special Hours Example
  slug: public-api-marketintel-special-hours-example
- key_count: 2
  name: Public Api Marketintel Store Chain Example
  slug: public-api-marketintel-store-chain-example
- key_count: 4
  name: Public Api Marketintel Store Delivery Information Example
  slug: public-api-marketintel-store-delivery-information-example
- key_count: 21
  name: Public Api Marketintel Store Details Example
  slug: public-api-marketintel-store-details-example
- key_count: 3
  name: Public Api Marketintel Store Listing Example
  slug: public-api-marketintel-store-listing-example
- key_count: 3
  name: Public Api Marketintel Store Menu Example
  slug: public-api-marketintel-store-menu-example
- key_count: 2
  name: Public Api Marketintel Store Price Level Example
  slug: public-api-marketintel-store-price-level-example
- key_count: 4
  name: Public Api Marketintel Store Promotion Example
  slug: public-api-marketintel-store-promotion-example
- key_count: 3
  name: Public Api Marketintel Store Rating Example
  slug: public-api-marketintel-store-rating-example
- key_count: 3
  name: Public Api Marketintel Store Sales Example
  slug: public-api-marketintel-store-sales-example
- key_count: 2
  name: Public Api Marketintel Time Range Example
  slug: public-api-marketintel-time-range-example
- key_count: 8
  name: Public Api Menu 3 Pd Example
  slug: public-api-menu-3-pd-example
- key_count: 1
  name: Public Api Menu Async Latest Job For Store Response Example
  slug: public-api-menu-async-latest-job-for-store-response-example
- key_count: 3
  name: Public Api Menu Asynchronous Job Example
  slug: public-api-menu-asynchronous-job-example
- key_count: 5
  name: Public Api Menu Data Example
  slug: public-api-menu-data-example
- key_count: 12
  name: Public Api Menu Item 3 Pd Example
  slug: public-api-menu-item-3-pd-example
- key_count: 11
  name: Public Api Menu Item Pos Example
  slug: public-api-menu-item-pos-example
- key_count: 1
  name: Public Api Menu Job Publish State Example
  slug: public-api-menu-job-publish-state-example
- key_count: 7
  name: Public Api Menu Pos Example
  slug: public-api-menu-pos-example
- key_count: 1
  name: Public Api Menu Publish Event Example
  slug: public-api-menu-publish-event-example
- key_count: 2
  name: Public Api Menu Publish Job State Example
  slug: public-api-menu-publish-job-state-example
- key_count: 1
  name: Public Api Menu Publish Request Example
  slug: public-api-menu-publish-request-example
- key_count: 3
  name: Public Api Menu Publish Response Example
  slug: public-api-menu-publish-response-example
- key_count: 1
  name: Public Api Menu Publish Response Menu Publish Targets Example
  slug: public-api-menu-publish-response-menu-publish-targets-example
- key_count: 1
  name: Public Api Menu Publish Target Example
  slug: public-api-menu-publish-target-example
- key_count: 1
  name: Public Api Menu Publish Targets Example
  slug: public-api-menu-publish-targets-example
- key_count: 5
  name: Public Api Menus Example
  slug: public-api-menus-example
- key_count: 3
  name: Public Api Menus Reward Example
  slug: public-api-menus-reward-example
- key_count: 4
  name: Public Api Menus Upsert Request Example
  slug: public-api-menus-upsert-request-example
- key_count: 5
  name: Public Api Metadata Object Example
  slug: public-api-metadata-object-example
- key_count: 10
  name: Public Api Modifier Group Example
  slug: public-api-modifier-group-example
- key_count: 9
  name: Public Api Modifier Group Update Request Example
  slug: public-api-modifier-group-update-request-example
- key_count: 5
  name: Public Api Modifier Item Example
  slug: public-api-modifier-item-example
- key_count: 0
  name: Public Api Null Event Example
  slug: public-api-null-event-example
- key_count: 22
  name: Public Api Nutrition Content Example
  slug: public-api-nutrition-content-example
- key_count: 2
  name: Public Api Nutritional Info Example
  slug: public-api-nutritional-info-example
- key_count: 7
  name: Public Api Oauth Token Generation Request Example
  slug: public-api-oauth-token-generation-request-example
- key_count: 1
  name: Public Api Optional Store Id In Metadata Example
  slug: public-api-optional-store-id-in-metadata-example
- key_count: 4
  name: Public Api Order 2 Example
  slug: public-api-order-2-example
- key_count: 2
  name: Public Api Order Component Id Example
  slug: public-api-order-component-id-example
- key_count: 1
  name: Public Api Order Confirm Event Example
  slug: public-api-order-confirm-event-example
- key_count: 2
  name: Public Api Order Customer Items Update Request Example
  slug: public-api-order-customer-items-update-request-example
- key_count: 4
  name: Public Api Order Customer Payment Update Request Example
  slug: public-api-order-customer-payment-update-request-example
- key_count: 1
  name: Public Api Order Delivery Info Update Request Example
  slug: public-api-order-delivery-info-update-request-example
- key_count: 14
  name: Public Api Order Example
  slug: public-api-order-example
- key_count: 5
  name: Public Api Order External Identifiers Example
  slug: public-api-order-external-identifiers-example
- key_count: 2
  name: Public Api Order Feed Example
  slug: public-api-order-feed-example
- key_count: 1
  name: Public Api Order Fulfilled Event Example
  slug: public-api-order-fulfilled-event-example
- key_count: 4
  name: Public Api Order Handed Off Event Example
  slug: public-api-order-handed-off-event-example
- key_count: 2
  name: Public Api Order Identifier Example
  slug: public-api-order-identifier-example
- key_count: 2
  name: Public Api Order Identifier Finance Example
  slug: public-api-order-identifier-finance-example
- key_count: 1
  name: Public Api Order Issue Example
  slug: public-api-order-issue-example
- key_count: 3
  name: Public Api Order Item Information Example
  slug: public-api-order-item-information-example
- key_count: 1
  name: Public Api Order Prep Time Update Request Example
  slug: public-api-order-prep-time-update-request-example
- key_count: 1
  name: Public Api Order Price Adjusted Modification Example
  slug: public-api-order-price-adjusted-modification-example
- key_count: 1
  name: Public Api Order Ready Event Example
  slug: public-api-order-ready-event-example
- key_count: 2
  name: Public Api Order Reference Example
  slug: public-api-order-reference-example
- key_count: 2
  name: Public Api Order Status Event Example
  slug: public-api-order-status-event-example
- key_count: 2
  name: Public Api Order Status History Example
  slug: public-api-order-status-history-example
- key_count: 1
  name: Public Api Order Status Update Request Example
  slug: public-api-order-status-update-request-example
- key_count: 8
  name: Public Api Order Total Example
  slug: public-api-order-total-example
- key_count: 3
  name: Public Api Order Total V2 Example
  slug: public-api-order-total-v2-example
- key_count: 5
  name: Public Api Order With Manager Info Example
  slug: public-api-order-with-manager-info-example
- key_count: 2
  name: Public Api Org Info Example
  slug: public-api-org-info-example
- key_count: 2
  name: Public Api Organization Example
  slug: public-api-organization-example
- key_count: 1
  name: Public Api Override Rule 3 Pd Example
  slug: public-api-override-rule-3-pd-example
- key_count: 1
  name: Public Api Override Rule Example
  slug: public-api-override-rule-example
- key_count: 2
  name: Public Api Parcel Carrier Delivery Info Example
  slug: public-api-parcel-carrier-delivery-info-example
- key_count: 4
  name: Public Api Pause Request Example
  slug: public-api-pause-request-example
- key_count: 1
  name: Public Api Pause Response Example
  slug: public-api-pause-response-example
- key_count: 2
  name: Public Api Pause Store Event Result Example
  slug: public-api-pause-store-event-result-example
- key_count: 7
  name: Public Api Payment Details Ach Example
  slug: public-api-payment-details-ach-example
- key_count: 9
  name: Public Api Payment Details Acss Example
  slug: public-api-payment-details-acss-example
- key_count: 6
  name: Public Api Payment Details Bacs Example
  slug: public-api-payment-details-bacs-example
- key_count: 5
  name: Public Api Payment Details Becs Example
  slug: public-api-payment-details-becs-example
- key_count: 10
  name: Public Api Payment Details Card Example
  slug: public-api-payment-details-card-example
- key_count: 8
  name: Public Api Payment Details Sepa Example
  slug: public-api-payment-details-sepa-example
- key_count: 7
  name: Public Api Payment Record Example
  slug: public-api-payment-record-example
- key_count: 3
  name: Public Api Payout Example
  slug: public-api-payout-example
- key_count: 2
  name: Public Api Payout Info Example
  slug: public-api-payout-info-example
- key_count: 5
  name: Public Api Person Example
  slug: public-api-person-example
- key_count: 2
  name: Public Api Personal Identifiers Example
  slug: public-api-personal-identifiers-example
- key_count: 4
  name: Public Api Photo Example
  slug: public-api-photo-example
- key_count: 1
  name: Public Api Pick Up Info Example
  slug: public-api-pick-up-info-example
- key_count: 1
  name: Public Api Picture Proof Example
  slug: public-api-picture-proof-example
- key_count: 1
  name: Public Api Picture Requirement Example
  slug: public-api-picture-requirement-example
- key_count: 1
  name: Public Api Ping Event Example
  slug: public-api-ping-event-example
- key_count: 2
  name: Public Api Pong Object Example
  slug: public-api-pong-object-example
- key_count: 4
  name: Public Api Pos Injection State Update Event Example
  slug: public-api-pos-injection-state-update-event-example
- key_count: 3
  name: Public Api Pos Menu Sync Request Example
  slug: public-api-pos-menu-sync-request-example
- key_count: 1
  name: Public Api Pos Menu Sync Response Example
  slug: public-api-pos-menu-sync-response-example
- key_count: 2
  name: Public Api Posorder Status Update Request Example
  slug: public-api-posorder-status-update-request-example
- key_count: 1
  name: Public Api Preparation Time Example
  slug: public-api-preparation-time-example
- key_count: 2
  name: Public Api Price Override Example
  slug: public-api-price-override-example
- key_count: 7
  name: Public Api Process Store Service Provider Status Example
  slug: public-api-process-store-service-provider-status-example
- key_count: 1
  name: Public Api Processing Status Response Example
  slug: public-api-processing-status-response-example
- key_count: 3
  name: Public Api Promotion Details Example
  slug: public-api-promotion-details-example
- key_count: 3
  name: Public Api Quantity Updated Modification Example
  slug: public-api-quantity-updated-modification-example
- key_count: 3
  name: Public Api Redeem And Accumulate Rewards Request Example
  slug: public-api-redeem-and-accumulate-rewards-request-example
- key_count: 3
  name: Public Api Redeem And Accumulate Rewards Response Example
  slug: public-api-redeem-and-accumulate-rewards-response-example
- key_count: 2
  name: Public Api Refund Rewards Request Example
  slug: public-api-refund-rewards-request-example
- key_count: 1
  name: Public Api Refund Rewards Response Example
  slug: public-api-refund-rewards-response-example
- key_count: 2
  name: Public Api Regular Hours Example
  slug: public-api-regular-hours-example
- key_count: 1
  name: Public Api Remove Storelink Event Example
  slug: public-api-remove-storelink-event-example
- key_count: 2
  name: Public Api Report Generated Event Example
  slug: public-api-report-generated-event-example
- key_count: 4
  name: Public Api Request Action Example
  slug: public-api-request-action-example
- key_count: 9
  name: Public Api Request Delivery Quote Callback Request Example
  slug: public-api-request-delivery-quote-callback-request-example
- key_count: 12
  name: Public Api Request Delivery Quote Event Example
  slug: public-api-request-delivery-quote-event-example
- key_count: 6
  name: Public Api Request State Info Example
  slug: public-api-request-state-info-example
- key_count: 8
  name: Public Api Required Address Example
  slug: public-api-required-address-example
- key_count: 7
  name: Public Api Required Delivery Info Example
  slug: public-api-required-delivery-info-example
- key_count: 3
  name: Public Api Required Event Result Metadata Example
  slug: public-api-required-event-result-metadata-example
- key_count: 5
  name: Public Api Required Person Example
  slug: public-api-required-person-example
- key_count: 5
  name: Public Api Review Reply Request Example
  slug: public-api-review-reply-request-example
- key_count: 1
  name: Public Api Review Reply Response Example
  slug: public-api-review-reply-response-example
- key_count: 1
  name: Public Api Reward Effect Example
  slug: public-api-reward-effect-example
- key_count: 7
  name: Public Api Reward Example
  slug: public-api-reward-example
- key_count: 2
  name: Public Api Search Users Response Example
  slug: public-api-search-users-response-example
- key_count: 1
  name: Public Api Selected Menu Reward Example
  slug: public-api-selected-menu-reward-example
- key_count: 3
  name: Public Api Selected Reward Example
  slug: public-api-selected-reward-example
- key_count: 2
  name: Public Api Self Drop Delivery Info Example
  slug: public-api-self-drop-delivery-info-example
- key_count: 1
  name: Public Api Send Menu Event Callback Example
  slug: public-api-send-menu-event-callback-example
- key_count: 1
  name: Public Api Service Override Rule Example
  slug: public-api-service-override-rule-example
- key_count: 2
  name: Public Api Servings Example
  slug: public-api-servings-example
- key_count: 0
  name: Public Api Shipment Delivery Info Example
  slug: public-api-shipment-delivery-info-example
- key_count: 4
  name: Public Api Shipment Example
  slug: public-api-shipment-example
- key_count: 4
  name: Public Api Shipment Line Item Example
  slug: public-api-shipment-line-item-example
- key_count: 2
  name: Public Api Shipment State Change Example
  slug: public-api-shipment-state-change-example
- key_count: 3
  name: Public Api Signature Proof Example
  slug: public-api-signature-proof-example
- key_count: 3
  name: Public Api Signature Requirement Example
  slug: public-api-signature-requirement-example
- key_count: 3
  name: Public Api Simple Finance Line Example
  slug: public-api-simple-finance-line-example
- key_count: 9
  name: Public Api Simple Financial Transaction Example
  slug: public-api-simple-financial-transaction-example
- key_count: 1
  name: Public Api Simple Order Identifier Finance Example
  slug: public-api-simple-order-identifier-finance-example
- key_count: 3
  name: Public Api Simulate Rewards Request Example
  slug: public-api-simulate-rewards-request-example
- key_count: 2
  name: Public Api Simulate Rewards Response Example
  slug: public-api-simulate-rewards-response-example
- key_count: 2
  name: Public Api Sku Barcode Example
  slug: public-api-sku-barcode-example
- key_count: 13
  name: Public Api Sku Details Example
  slug: public-api-sku-details-example
- key_count: 5
  name: Public Api Source External Identifiers Example
  slug: public-api-source-external-identifiers-example
- key_count: 3
  name: Public Api Special Hours Example
  slug: public-api-special-hours-example
- key_count: 1
  name: Public Api Storage Requirement Example
  slug: public-api-storage-requirement-example
- key_count: 6
  name: Public Api Store 2 Example
  slug: public-api-store-2-example
- key_count: 2
  name: Public Api Store 3 Example
  slug: public-api-store-3-example
- key_count: 3
  name: Public Api Store Availability Event Result Example
  slug: public-api-store-availability-event-result-example
- key_count: 3
  name: Public Api Store Example
  slug: public-api-store-example
- key_count: 3
  name: Public Api Store Hours Configuration Event Result Example
  slug: public-api-store-hours-configuration-event-result-example
- key_count: 3
  name: Public Api Store Hours Configuration Example
  slug: public-api-store-hours-configuration-example
- key_count: 2
  name: Public Api Store Hours Example
  slug: public-api-store-hours-example
- key_count: 5
  name: Public Api Store Info 2 Example
  slug: public-api-store-info-2-example
- key_count: 6
  name: Public Api Store Info Example
  slug: public-api-store-info-example
- key_count: 2
  name: Public Api Storefront Error Example
  slug: public-api-storefront-error-example
- key_count: 2
  name: Public Api Storefront Regular Hours Example
  slug: public-api-storefront-regular-hours-example
- key_count: 3
  name: Public Api Storefront Special Hours Example
  slug: public-api-storefront-special-hours-example
- key_count: 2
  name: Public Api Storefront Time Range Example
  slug: public-api-storefront-time-range-example
- key_count: 1
  name: Public Api Subtotal Example
  slug: public-api-subtotal-example
- key_count: 2
  name: Public Api Subtotal Reward Example
  slug: public-api-subtotal-reward-example
- key_count: 3
  name: Public Api Suspend Items Request Example
  slug: public-api-suspend-items-request-example
- key_count: 2
  name: Public Api Suspension Status Example
  slug: public-api-suspension-status-example
- key_count: 2
  name: Public Api Time Range Example
  slug: public-api-time-range-example
- key_count: 4
  name: Public Api Totals Example
  slug: public-api-totals-example
- key_count: 1
  name: Public Api Trigger Example
  slug: public-api-trigger-example
- key_count: 3
  name: Public Api Trigger Menu Example
  slug: public-api-trigger-menu-example
- key_count: 1
  name: Public Api Unpause Request Example
  slug: public-api-unpause-request-example
- key_count: 1
  name: Public Api Unpause Response Example
  slug: public-api-unpause-response-example
- key_count: 1
  name: Public Api Unpause Store Event Result Example
  slug: public-api-unpause-store-event-result-example
- key_count: 2
  name: Public Api Unsuspend Items Request Example
  slug: public-api-unsuspend-items-request-example
- key_count: 2
  name: Public Api Update Delivery Request Callback Request Example
  slug: public-api-update-delivery-request-callback-request-example
- key_count: 6
  name: Public Api Update Delivery Request Event Example
  slug: public-api-update-delivery-request-event-example
- key_count: 2
  name: Public Api Update Item Status Entry Example
  slug: public-api-update-item-status-entry-example
- key_count: 2
  name: Public Api Update Storelink Status Request Example
  slug: public-api-update-storelink-status-request-example
- key_count: 1
  name: Public Api Upload Past Orders Request Example
  slug: public-api-upload-past-orders-request-example
- key_count: 1
  name: Public Api Upload Past Orders Response Example
  slug: public-api-upload-past-orders-response-example
- key_count: 1
  name: Public Api Upsert Full Menu Event Callback Example
  slug: public-api-upsert-full-menu-event-callback-example
- key_count: 1
  name: Public Api Upsert Hours Event Example
  slug: public-api-upsert-hours-event-example
- key_count: 3
  name: Public Api Upsert Storelink Event Example
  slug: public-api-upsert-storelink-event-example
- key_count: 3
  name: Public Api Upsert Storelink Event Result Request Example
  slug: public-api-upsert-storelink-event-result-request-example
- key_count: 3
  name: Public Api User Account Example
  slug: public-api-user-account-example
- key_count: 2
  name: Public Api User Balance Example
  slug: public-api-user-balance-example
- key_count: 2
  name: Public Api User Example
  slug: public-api-user-example
- key_count: 2
  name: Public Api User Field Example
  slug: public-api-user-field-example
- key_count: 3
  name: Public Api Vehicle Information Example
  slug: public-api-vehicle-information-example
- key_count: 2
  name: Public Api Verification Proof Example
  slug: public-api-verification-proof-example
- key_count: 2
  name: Public Api Verification Requirements Example
  slug: public-api-verification-requirements-example
- key_count: 5
  name: Public Api View Credential Example
  slug: public-api-view-credential-example
- key_count: 2
  name: Public Api View Credentials Array Example
  slug: public-api-view-credentials-array-example
features:
- description: Receive, confirm, update, and fulfill orders from multiple delivery and online-ordering channels through a single Public API.
  name: Order Aggregation
- description: Upsert, publish, and synchronize menus, hours, and item availability across connected storefronts and channels.
  name: Menu Management
- description: Request delivery quotes, create and update delivery requests, and track courier status via webhooks.
  name: Delivery Orchestration
- description: Post financial transactions and invoices and retrieve payout and order-total data.
  name: Finance & Payouts
- description: Generate orders, items, payouts, and ratings/reviews reports for stores over a time period.
  name: Reports
- description: Reply to customer reviews and compute, redeem, accumulate, refund, and simulate loyalty rewards.
  name: Reviews & Loyalty
- description: Pause and unpause storefronts and report store availability and hours configuration.
  name: Storefront Control
- description: Onboard stores, manage store links, and read organization, brand, and store data via OAuth authorization-code flow.
  name: Account Pairing & Organization
- description: Subscribe to order, menu, delivery, storefront, reports, and account-pairing events signed with HMAC-SHA256.
  name: Webhooks
finops:
- name: Otter Finops
  service_category: Restaurant Operations & Commerce
  slug: otter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/otter.png
integrations:
- description: Third-party delivery marketplaces and on-demand courier networks.
  name: Delivery Service Providers
- description: Restaurant POS systems exchanging orders and menus with Otter.
  name: Point of Sale Platforms
- description: Branded and third-party online ordering storefronts aggregated by Otter.
  name: Online Ordering Channels
json_schemas:
- name: AcceptDeliveryCallbackRequest
  property_count: 9
  slug: public-api-accept-delivery-callback-request
- name: AcceptDeliveryEvent
  property_count: 24
  slug: public-api-accept-delivery-event
- name: AccountHolderType
  property_count: 0
  slug: public-api-account-holder-type
- name: AccountType
  property_count: 0
  slug: public-api-account-type
- name: AdditionalCharge
  property_count: 4
  slug: public-api-additional-charge
- name: Address
  property_count: 8
  slug: public-api-address
- name: AllergenClassification
  property_count: 2
  slug: public-api-allergen-classification
- name: ApplicationId
  property_count: 0
  slug: public-api-application-id
- name: BootstrapMenuRequest
  property_count: 5
  slug: public-api-bootstrap-menu-request
- name: BrandInfo
  property_count: 3
  slug: public-api-brand-info
- name: Brand
  property_count: 2
  slug: public-api-brand
- name: BulkUpdateItemStatus
  property_count: 1
  slug: public-api-bulk-update-item-status
- name: CancelDeliveryCallbackRequest
  property_count: 1
  slug: public-api-cancel-delivery-callback-request
- name: CancelDeliveryEvent
  property_count: 1
  slug: public-api-cancel-delivery-event
- name: CardBrandType
  property_count: 0
  slug: public-api-card-brand-type
- name: CardFundingType
  property_count: 0
  slug: public-api-card-funding-type
- name: CardInfo
  property_count: 2
  slug: public-api-card-info
- name: CardWalletType
  property_count: 0
  slug: public-api-card-wallet-type
- name: Category
  property_count: 6
  slug: public-api-category
- name: CompositeFinanceLine
  property_count: 1
  slug: public-api-composite-finance-line
- name: ComputeApplicableRewardsRequest
  property_count: 2
  slug: public-api-compute-applicable-rewards-request
- name: ComputeApplicableRewardsResponse
  property_count: 1
  slug: public-api-compute-applicable-rewards-response
- name: Connection
  property_count: 1
  slug: public-api-connection
- name: Courier
  property_count: 5
  slug: public-api-courier
- name: CourierServiceDeliveryInfo
  property_count: 0
  slug: public-api-courier-service-delivery-info
- name: CreateConnectionRequest
  property_count: 1
  slug: public-api-create-connection-request
- name: CreateShipmentLineItem
  property_count: 6
  slug: public-api-create-shipment-line-item
- name: CreateShipmentRequest
  property_count: 2
  slug: public-api-create-shipment-request
- name: CreateShipmentResponse
  property_count: 1
  slug: public-api-create-shipment-response
- name: CreateUserRequest
  property_count: 1
  slug: public-api-create-user-request
- name: CreateUserResponse
  property_count: 1
  slug: public-api-create-user-response
- name: CredentialsSchemaVersion
  property_count: 0
  slug: public-api-credentials-schema-version
- name: CustomBulkResolutionOptions
  property_count: 15
  slug: public-api-custom-bulk-resolution-options
- name: CustomerItemModification
  property_count: 3
  slug: public-api-customer-item-modification
- name: CustomerPayment
  property_count: 8
  slug: public-api-customer-payment
- name: CustomerPaymentV2
  property_count: 4
  slug: public-api-customer-payment-v2
- name: CustomerTip
  property_count: 1
  slug: public-api-customer-tip
- name: DefaultModifierSelectionData
  property_count: 1
  slug: public-api-default-modifier-selection-data
- name: DefaultModifierSelection
  property_count: 2
  slug: public-api-default-modifier-selection
- name: DeliveryCost
  property_count: 2
  slug: public-api-delivery-cost
- name: DeliveryFee
  property_count: 1
  slug: public-api-delivery-fee
- name: DeliveryInfo
  property_count: 7
  slug: public-api-delivery-info
- name: DeliveryMetadata
  property_count: 2
  slug: public-api-delivery-metadata
- name: DeliveryStatus
  property_count: 0
  slug: public-api-delivery-status
- name: DeliveryStatusUpdateEvent
  property_count: 14
  slug: public-api-delivery-status-update-event
- name: DeliveryStatusUpdateRequest
  property_count: 12
  slug: public-api-delivery-status-update-request
- name: DeliveryWindow
  property_count: 2
  slug: public-api-delivery-window
- name: DietaryClassification
  property_count: 1
  slug: public-api-dietary-classification
- name: DiscoverStoresEventResult
  property_count: 2
  slug: public-api-discover-stores-event-result
- name: DiscoveredStore
  property_count: 2
  slug: public-api-discovered-store
- name: Distance
  property_count: 2
  slug: public-api-distance
- name: DropoffInfo
  property_count: 2
  slug: public-api-dropoff-info
- name: DropoffInstructions
  property_count: 2
  slug: public-api-dropoff-instructions
- name: EaterOrderHistoryRequest
  property_count: 4
  slug: public-api-eater-order-history-request
- name: EaterOrderHistoryResponse
  property_count: 2
  slug: public-api-eater-order-history-response
- name: EaterOrder
  property_count: 9
  slug: public-api-eater-order
- name: EnergyKcal
  property_count: 2
  slug: public-api-energy-kcal
- name: EnrollmentField
  property_count: 4
  slug: public-api-enrollment-field
- name: EntityPathOverrideRule
  property_count: 0
  slug: public-api-entity-path-override-rule
- name: ErrorDetail
  property_count: 2
  slug: public-api-error-detail
- name: ErrorMessage
  property_count: 2
  slug: public-api-error-message
- name: EventCallbackError
  property_count: 2
  slug: public-api-event-callback-error
- name: EventNotificationBase
  property_count: 3
  slug: public-api-event-notification-base
- name: EventNotification
  property_count: 4
  slug: public-api-event-notification
- name: EventResultMetadata
  property_count: 3
  slug: public-api-event-result-metadata
- name: ExistingCredential
  property_count: 2
  slug: public-api-existing-credential
- name: ExposedThirdPartyInfo
  property_count: 2
  slug: public-api-exposed-third-party-info
- name: FetchCredentialsEvent
  property_count: 1
  slug: public-api-fetch-credentials-event
- name: FinancialData
  property_count: 19
  slug: public-api-financial-data
- name: FinancialInvoice
  property_count: 4
  slug: public-api-financial-invoice
- name: FinancialTransaction
  property_count: 12
  slug: public-api-financial-transaction
- name: FulfilledCredential
  property_count: 2
  slug: public-api-fulfilled-credential
- name: FulfillmentInfo
  property_count: 7
  slug: public-api-fulfillment-info
- name: FulfillmentModeOverrideRule
  property_count: 0
  slug: public-api-fulfillment-mode-override-rule
- name: FulfillmentPathEntity
  property_count: 2
  slug: public-api-fulfillment-path-entity
- name: GenerateReportMultiRequest
  property_count: 6
  slug: public-api-generate-report-multi-request
- name: GenerateReportResponse
  property_count: 1
  slug: public-api-generate-report-response
- name: GetEnrollmentConfigResponse
  property_count: 1
  slug: public-api-get-enrollment-config-response
- name: GetReportStatusResponse
  property_count: 2
  slug: public-api-get-report-status-response
- name: GetStoreDetailsEventResult
  property_count: 2
  slug: public-api-get-store-details-event-result
- name: GetUserResponse
  property_count: 1
  slug: public-api-get-user-response
- name: Gtin
  property_count: 0
  slug: public-api-gtin
- name: HourInterval
  property_count: 5
  slug: public-api-hour-interval
- name: HoursData
  property_count: 3
  slug: public-api-hours-data
- name: Hours
  property_count: 1
  slug: public-api-hours
- name: HydraToken
  property_count: 4
  slug: public-api-hydra-token
- name: IntentToCancelEvent
  property_count: 2
  slug: public-api-intent-to-cancel-event
- name: InventorySummariesResponse
  property_count: 2
  slug: public-api-inventory-summaries-response
- name: InventorySummary
  property_count: 8
  slug: public-api-inventory-summary
- name: InvoicePayoutInfo
  property_count: 4
  slug: public-api-invoice-payout-info
- name: Item-2
  property_count: 5
  slug: public-api-item-2
- name: Item-3
  property_count: 3
  slug: public-api-item-3
- name: Item-4
  property_count: 5
  slug: public-api-item-4
- name: ItemAddedModification
  property_count: 1
  slug: public-api-item-added-modification
- name: ItemModifier
  property_count: 11
  slug: public-api-item-modifier
- name: ItemPriceOverride
  property_count: 3
  slug: public-api-item-price-override
- name: Item
  property_count: 14
  slug: public-api-item
- name: ItemSelector
  property_count: 2
  slug: public-api-item-selector
- name: ItemStatus
  property_count: 2
  slug: public-api-item-status
- name: ItemTax
  property_count: 2
  slug: public-api-item-tax
- name: ItemUpdateRequest
  property_count: 9
  slug: public-api-item-update-request
- name: JobId
  property_count: 0
  slug: public-api-job-id
- name: JobReference
  property_count: 2
  slug: public-api-job-reference
- name: ListBrandsResponse
  property_count: 2
  slug: public-api-list-brands-response
- name: ListShipmentsResponse
  property_count: 2
  slug: public-api-list-shipments-response
- name: ListStoresResponse
  property_count: 2
  slug: public-api-list-stores-response
- name: Location
  property_count: 2
  slug: public-api-location
- name: LoyaltyInfo
  property_count: 1
  slug: public-api-loyalty-info
- name: ManagerCancelOrderRequest
  property_count: 2
  slug: public-api-manager-cancel-order-request
- name: ManagerConfirmOrderRequest
  property_count: 1
  slug: public-api-manager-confirm-order-request
- name: ManagerItemIssue
  property_count: 2
  slug: public-api-manager-item-issue
- name: ManagerItemIssues
  property_count: 2
  slug: public-api-manager-item-issues
- name: ManagerOrderCancelDetails
  property_count: 1
  slug: public-api-manager-order-cancel-details
- name: ManagerOrderIssue
  property_count: 2
  slug: public-api-manager-order-issue
- name: ManagerOrderIssues
  property_count: 2
  slug: public-api-manager-order-issues
- name: MandateStatus
  property_count: 0
  slug: public-api-mandate-status
- name: Marketintel_Coordinates
  property_count: 2
  slug: public-api-marketintel-coordinates
- name: Marketintel_GeoLocationInformation
  property_count: 5
  slug: public-api-marketintel-geo-location-information
- name: Marketintel_HoursData
  property_count: 3
  slug: public-api-marketintel-hours-data
- name: Marketintel_LocationBasedInformation
  property_count: 2
  slug: public-api-marketintel-location-based-information
- name: Marketintel_RegularHours
  property_count: 2
  slug: public-api-marketintel-regular-hours
- name: Marketintel_SpecialHours
  property_count: 3
  slug: public-api-marketintel-special-hours
- name: Marketintel_StoreChain
  property_count: 2
  slug: public-api-marketintel-store-chain
- name: Marketintel_StoreDeliveryInformation
  property_count: 4
  slug: public-api-marketintel-store-delivery-information
- name: Marketintel_StoreDetails
  property_count: 21
  slug: public-api-marketintel-store-details
- name: Marketintel_StoreListing
  property_count: 3
  slug: public-api-marketintel-store-listing
- name: Marketintel_StoreMenu
  property_count: 3
  slug: public-api-marketintel-store-menu
- name: Marketintel_StorePriceLevel
  property_count: 2
  slug: public-api-marketintel-store-price-level
- name: Marketintel_StorePromotion
  property_count: 4
  slug: public-api-marketintel-store-promotion
- name: Marketintel_StoreRating
  property_count: 3
  slug: public-api-marketintel-store-rating
- name: Marketintel_StoreSales
  property_count: 3
  slug: public-api-marketintel-store-sales
- name: Marketintel_TimeRange
  property_count: 2
  slug: public-api-marketintel-time-range
- name: Menu_3PD
  property_count: 8
  slug: public-api-menu-3-pd
- name: MenuAsyncJobType
  property_count: 0
  slug: public-api-menu-async-job-type
- name: MenuAsyncLatestJobForStoreResponse
  property_count: 1
  slug: public-api-menu-async-latest-job-for-store-response
- name: MenuAsynchronousJob
  property_count: 3
  slug: public-api-menu-asynchronous-job
- name: MenuData
  property_count: 5
  slug: public-api-menu-data
- name: MenuItem_3PD
  property_count: 12
  slug: public-api-menu-item-3-pd
- name: MenuItem_POS
  property_count: 11
  slug: public-api-menu-item-pos
- name: MenuJobPublishState
  property_count: 0
  slug: public-api-menu-job-publish-state
- name: MenuJobType
  property_count: 0
  slug: public-api-menu-job-type
- name: Menu_POS
  property_count: 7
  slug: public-api-menu-pos
- name: MenuPublishEvent
  property_count: 1
  slug: public-api-menu-publish-event
- name: MenuPublishJobState
  property_count: 2
  slug: public-api-menu-publish-job-state
- name: MenuPublishRequest
  property_count: 1
  slug: public-api-menu-publish-request
- name: MenuPublishResponseMenuPublishTargets
  property_count: 1
  slug: public-api-menu-publish-response-menu-publish-targets
- name: MenuPublishResponse
  property_count: 3
  slug: public-api-menu-publish-response
- name: MenuPublishTarget
  property_count: 1
  slug: public-api-menu-publish-target
- name: MenuPublishTargets
  property_count: 1
  slug: public-api-menu-publish-targets
- name: MenusReward
  property_count: 3
  slug: public-api-menus-reward
- name: Menus
  property_count: 5
  slug: public-api-menus
- name: MenusUpsertRequest
  property_count: 4
  slug: public-api-menus-upsert-request
- name: MetadataObject
  property_count: 5
  slug: public-api-metadata-object
- name: ModifierGroup
  property_count: 10
  slug: public-api-modifier-group
- name: ModifierGroupUpdateRequest
  property_count: 9
  slug: public-api-modifier-group-update-request
- name: ModifierItem
  property_count: 5
  slug: public-api-modifier-item
- name: Money
  property_count: 2
  slug: public-api-money
- name: NullEvent
  property_count: 0
  slug: public-api-null-event
- name: NutritionContent
  property_count: 22
  slug: public-api-nutrition-content
- name: NutritionalInfo
  property_count: 2
  slug: public-api-nutritional-info
- name: OAuthTokenGenerationRequest
  property_count: 7
  slug: public-api-oauth-token-generation-request
- name: OperationType
  property_count: 0
  slug: public-api-operation-type
- name: OptionalStoreIdInMetadata
  property_count: 1
  slug: public-api-optional-store-id-in-metadata
- name: Order-2
  property_count: 4
  slug: public-api-order-2
- name: OrderComponentId
  property_count: 2
  slug: public-api-order-component-id
- name: OrderConfirmEvent
  property_count: 1
  slug: public-api-order-confirm-event
- name: OrderCustomerItemsUpdateRequest
  property_count: 2
  slug: public-api-order-customer-items-update-request
- name: OrderCustomerPaymentUpdateRequest
  property_count: 4
  slug: public-api-order-customer-payment-update-request
- name: OrderDeliveryInfoUpdateRequest
  property_count: 1
  slug: public-api-order-delivery-info-update-request
- name: OrderExternalIdentifiers
  property_count: 5
  slug: public-api-order-external-identifiers
- name: OrderFeed
  property_count: 2
  slug: public-api-order-feed
- name: OrderFulfilledEvent
  property_count: 1
  slug: public-api-order-fulfilled-event
- name: OrderHandedOffEvent
  property_count: 4
  slug: public-api-order-handed-off-event
- name: OrderIdentifierFinance
  property_count: 2
  slug: public-api-order-identifier-finance
- name: OrderIdentifier
  property_count: 2
  slug: public-api-order-identifier
- name: OrderIssue
  property_count: 1
  slug: public-api-order-issue
- name: OrderItemInformation
  property_count: 3
  slug: public-api-order-item-information
- name: OrderPrepTimeUpdateRequest
  property_count: 1
  slug: public-api-order-prep-time-update-request
- name: OrderPriceAdjustedModification
  property_count: 1
  slug: public-api-order-price-adjusted-modification
- name: OrderReadyEvent
  property_count: 1
  slug: public-api-order-ready-event
- name: OrderReference
  property_count: 2
  slug: public-api-order-reference
- name: Order
  property_count: 14
  slug: public-api-order
- name: OrderStatusEvent
  property_count: 2
  slug: public-api-order-status-event
- name: OrderStatusHistory
  property_count: 2
  slug: public-api-order-status-history
- name: OrderStatusUpdateRequest
  property_count: 1
  slug: public-api-order-status-update-request
- name: OrderTotal
  property_count: 8
  slug: public-api-order-total
- name: OrderTotalV2
  property_count: 3
  slug: public-api-order-total-v2
- name: OrderWithManagerInfo
  property_count: 5
  slug: public-api-order-with-manager-info
- name: OrgInfo
  property_count: 2
  slug: public-api-org-info
- name: Organization
  property_count: 2
  slug: public-api-organization
- name: OverrideRule_3PD
  property_count: 1
  slug: public-api-override-rule-3-pd
- name: OverrideRule
  property_count: 1
  slug: public-api-override-rule
- name: ParcelCarrierDeliveryInfo
  property_count: 0
  slug: public-api-parcel-carrier-delivery-info
- name: PauseReason
  property_count: 0
  slug: public-api-pause-reason
- name: PauseRequest
  property_count: 4
  slug: public-api-pause-request
- name: PauseResponse
  property_count: 1
  slug: public-api-pause-response
- name: PauseStoreEventResult
  property_count: 2
  slug: public-api-pause-store-event-result
- name: PaymentDetailsAch
  property_count: 7
  slug: public-api-payment-details-ach
- name: PaymentDetailsAcss
  property_count: 9
  slug: public-api-payment-details-acss
- name: PaymentDetailsBacs
  property_count: 6
  slug: public-api-payment-details-bacs
- name: PaymentDetailsBecs
  property_count: 5
  slug: public-api-payment-details-becs
- name: PaymentDetailsCard
  property_count: 10
  slug: public-api-payment-details-card
- name: PaymentDetailsSepa
  property_count: 8
  slug: public-api-payment-details-sepa
- name: PaymentRecord
  property_count: 7
  slug: public-api-payment-record
- name: PayoutInfo
  property_count: 2
  slug: public-api-payout-info
- name: Payout
  property_count: 3
  slug: public-api-payout
- name: PercentageValue
  property_count: 1
  slug: public-api-percentage-value
- name: Person
  property_count: 5
  slug: public-api-person
- name: PersonalIdentifiers
  property_count: 2
  slug: public-api-personal-identifiers
- name: Photo
  property_count: 4
  slug: public-api-photo
- name: PickUpInfo
  property_count: 1
  slug: public-api-pick-up-info
- name: PictureProof
  property_count: 1
  slug: public-api-picture-proof
- name: PictureRequirement
  property_count: 1
  slug: public-api-picture-requirement
- name: PingEvent
  property_count: 1
  slug: public-api-ping-event
- name: PongObject
  property_count: 2
  slug: public-api-pong-object
- name: PosInjectionStateUpdateEvent
  property_count: 4
  slug: public-api-pos-injection-state-update-event
- name: PosMenuSyncRequest
  property_count: 3
  slug: public-api-pos-menu-sync-request
- name: PosMenuSyncResponse
  property_count: 1
  slug: public-api-pos-menu-sync-response
- name: POSOrderStatusUpdateRequest
  property_count: 2
  slug: public-api-posorder-status-update-request
- name: PreparationTime
  property_count: 1
  slug: public-api-preparation-time
- name: PriceOverride
  property_count: 2
  slug: public-api-price-override
- name: ProcessStoreServiceProviderStatus
  property_count: 7
  slug: public-api-process-store-service-provider-status
- name: ProcessingStatusResponse
  property_count: 1
  slug: public-api-processing-status-response
- name: PromotionDetails
  property_count: 3
  slug: public-api-promotion-details
- name: QuantityUpdatedModification
  property_count: 3
  slug: public-api-quantity-updated-modification
- name: RecordPaymentType
  property_count: 0
  slug: public-api-record-payment-type
- name: RecordProviderType
  property_count: 0
  slug: public-api-record-provider-type
- name: RedeemAndAccumulateRewardsRequest
  property_count: 3
  slug: public-api-redeem-and-accumulate-rewards-request
- name: RedeemAndAccumulateRewardsResponse
  property_count: 3
  slug: public-api-redeem-and-accumulate-rewards-response
- name: RefundRewardsRequest
  property_count: 2
  slug: public-api-refund-rewards-request
- name: RefundRewardsResponse
  property_count: 1
  slug: public-api-refund-rewards-response
- name: RegularHours
  property_count: 2
  slug: public-api-regular-hours
- name: RemoveStorelinkEvent
  property_count: 1
  slug: public-api-remove-storelink-event
- name: ReportGeneratedEvent
  property_count: 2
  slug: public-api-report-generated-event
- name: RequestAction
  property_count: 4
  slug: public-api-request-action
- name: RequestDeliveryQuoteCallbackRequest
  property_count: 9
  slug: public-api-request-delivery-quote-callback-request
- name: RequestDeliveryQuoteEvent
  property_count: 12
  slug: public-api-request-delivery-quote-event
- name: RequestStateInfo
  property_count: 6
  slug: public-api-request-state-info
- name: RequestState
  property_count: 0
  slug: public-api-request-state
- name: RequiredAddress
  property_count: 8
  slug: public-api-required-address
- name: RequiredDeliveryInfo
  property_count: 7
  slug: public-api-required-delivery-info
- name: RequiredEventResultMetadata
  property_count: 3
  slug: public-api-required-event-result-metadata
- name: RequiredPerson
  property_count: 5
  slug: public-api-required-person
- name: ReviewReplyRequest
  property_count: 5
  slug: public-api-review-reply-request
- name: ReviewReplyResponse
  property_count: 1
  slug: public-api-review-reply-response
- name: RewardEffect
  property_count: 1
  slug: public-api-reward-effect
- name: Reward
  property_count: 7
  slug: public-api-reward
- name: SearchUsersResponse
  property_count: 2
  slug: public-api-search-users-response
- name: SelectedMenuReward
  property_count: 1
  slug: public-api-selected-menu-reward
- name: SelectedReward
  property_count: 3
  slug: public-api-selected-reward
- name: SelfDropDeliveryInfo
  property_count: 0
  slug: public-api-self-drop-delivery-info
- name: SendMenuEventCallback
  property_count: 1
  slug: public-api-send-menu-event-callback
- name: ServiceOverrideRule
  property_count: 0
  slug: public-api-service-override-rule
- name: Servings
  property_count: 2
  slug: public-api-servings
- name: ShipmentDeliveryInfo
  property_count: 0
  slug: public-api-shipment-delivery-info
- name: ShipmentLineItem
  property_count: 4
  slug: public-api-shipment-line-item
- name: Shipment
  property_count: 4
  slug: public-api-shipment
- name: ShipmentStateChange
  property_count: 2
  slug: public-api-shipment-state-change
- name: ShipmentState
  property_count: 0
  slug: public-api-shipment-state
- name: SignatureProof
  property_count: 3
  slug: public-api-signature-proof
- name: SignatureRequirement
  property_count: 3
  slug: public-api-signature-requirement
- name: SimpleFinanceLine
  property_count: 3
  slug: public-api-simple-finance-line
- name: SimpleFinancialTransaction
  property_count: 9
  slug: public-api-simple-financial-transaction
- name: SimpleOrderIdentifierFinance
  property_count: 1
  slug: public-api-simple-order-identifier-finance
- name: SimulateRewardsRequest
  property_count: 3
  slug: public-api-simulate-rewards-request
- name: SimulateRewardsResponse
  property_count: 2
  slug: public-api-simulate-rewards-response
- name: SkuBarcode
  property_count: 2
  slug: public-api-sku-barcode
- name: SkuDetails
  property_count: 13
  slug: public-api-sku-details
- name: SourceExternalIdentifiers
  property_count: 5
  slug: public-api-source-external-identifiers
- name: SpecialHours
  property_count: 3
  slug: public-api-special-hours
- name: Status
  property_count: 0
  slug: public-api-status
- name: StorageRequirement
  property_count: 1
  slug: public-api-storage-requirement
- name: Store-2
  property_count: 6
  slug: public-api-store-2
- name: Store-3
  property_count: 2
  slug: public-api-store-3
- name: StoreAvailabilityEventResult
  property_count: 3
  slug: public-api-store-availability-event-result
- name: StoreHoursConfigurationEventResult
  property_count: 3
  slug: public-api-store-hours-configuration-event-result
- name: StoreHoursConfiguration
  property_count: 3
  slug: public-api-store-hours-configuration
- name: StoreHours
  property_count: 2
  slug: public-api-store-hours
- name: StoreId
  property_count: 0
  slug: public-api-store-id
- name: StoreInfo-2
  property_count: 5
  slug: public-api-store-info-2
- name: StoreInfo
  property_count: 6
  slug: public-api-store-info
- name: Store
  property_count: 3
  slug: public-api-store
- name: StorefrontError
  property_count: 2
  slug: public-api-storefront-error
- name: Storefront_RegularHours
  property_count: 2
  slug: public-api-storefront-regular-hours
- name: Storefront_SpecialHours
  property_count: 3
  slug: public-api-storefront-special-hours
- name: Storefront_TimeRange
  property_count: 2
  slug: public-api-storefront-time-range
- name: SubtotalReward
  property_count: 2
  slug: public-api-subtotal-reward
- name: Subtotal
  property_count: 1
  slug: public-api-subtotal
- name: SuspendItemsRequest
  property_count: 3
  slug: public-api-suspend-items-request
- name: SuspensionStatus
  property_count: 2
  slug: public-api-suspension-status
- name: TimeRange
  property_count: 2
  slug: public-api-time-range
- name: Totals
  property_count: 4
  slug: public-api-totals
- name: TriggerMenu
  property_count: 3
  slug: public-api-trigger-menu
- name: Trigger
  property_count: 1
  slug: public-api-trigger
- name: UnitPriceAndCount
  property_count: 2
  slug: public-api-unit-price-and-count
- name: UnpauseRequest
  property_count: 1
  slug: public-api-unpause-request
- name: UnpauseResponse
  property_count: 1
  slug: public-api-unpause-response
- name: UnpauseStoreEventResult
  property_count: 1
  slug: public-api-unpause-store-event-result
- name: UnpauseStoreEvent
  property_count: 0
  slug: public-api-unpause-store-event
- name: UnsuspendItemsRequest
  property_count: 2
  slug: public-api-unsuspend-items-request
- name: UpdateDeliveryRequestCallbackRequest
  property_count: 2
  slug: public-api-update-delivery-request-callback-request
- name: UpdateDeliveryRequestEvent
  property_count: 6
  slug: public-api-update-delivery-request-event
- name: UpdateItemStatusEntry
  property_count: 2
  slug: public-api-update-item-status-entry
- name: UpdateStorelinkStatusRequest
  property_count: 2
  slug: public-api-update-storelink-status-request
- name: UploadPastOrdersRequest
  property_count: 1
  slug: public-api-upload-past-orders-request
- name: UploadPastOrdersResponse
  property_count: 1
  slug: public-api-upload-past-orders-response
- name: UpsertFullMenuEventCallback
  property_count: 1
  slug: public-api-upsert-full-menu-event-callback
- name: UpsertHoursEvent
  property_count: 1
  slug: public-api-upsert-hours-event
- name: UpsertStorelinkEventResultRequest
  property_count: 3
  slug: public-api-upsert-storelink-event-result-request
- name: UpsertStorelinkEvent
  property_count: 3
  slug: public-api-upsert-storelink-event
- name: UserAccount
  property_count: 3
  slug: public-api-user-account
- name: UserBalance
  property_count: 2
  slug: public-api-user-balance
- name: UserField
  property_count: 2
  slug: public-api-user-field
- name: User
  property_count: 2
  slug: public-api-user
- name: VehicleInformation
  property_count: 3
  slug: public-api-vehicle-information
- name: VerificationProof
  property_count: 2
  slug: public-api-verification-proof
- name: VerificationRequirements
  property_count: 2
  slug: public-api-verification-requirements
- name: ViewCredential
  property_count: 5
  slug: public-api-view-credential
- name: ViewCredentialsArray
  property_count: 2
  slug: public-api-view-credentials-array
json_structures:
- name: Public Api Accept Delivery Callback Request Structure
  property_count: 9
  slug: public-api-accept-delivery-callback-request-structure
- name: Public Api Accept Delivery Event Structure
  property_count: 24
  slug: public-api-accept-delivery-event-structure
- name: Public Api Account Holder Type Structure
  property_count: 0
  slug: public-api-account-holder-type-structure
- name: Public Api Account Type Structure
  property_count: 0
  slug: public-api-account-type-structure
- name: Public Api Additional Charge Structure
  property_count: 4
  slug: public-api-additional-charge-structure
- name: Public Api Address Structure
  property_count: 8
  slug: public-api-address-structure
- name: Public Api Allergen Classification Structure
  property_count: 2
  slug: public-api-allergen-classification-structure
- name: Public Api Application Id Structure
  property_count: 0
  slug: public-api-application-id-structure
- name: Public Api Bootstrap Menu Request Structure
  property_count: 5
  slug: public-api-bootstrap-menu-request-structure
- name: Public Api Brand Info Structure
  property_count: 3
  slug: public-api-brand-info-structure
- name: Public Api Brand Structure
  property_count: 2
  slug: public-api-brand-structure
- name: Public Api Bulk Update Item Status Structure
  property_count: 1
  slug: public-api-bulk-update-item-status-structure
- name: Public Api Cancel Delivery Callback Request Structure
  property_count: 1
  slug: public-api-cancel-delivery-callback-request-structure
- name: Public Api Cancel Delivery Event Structure
  property_count: 1
  slug: public-api-cancel-delivery-event-structure
- name: Public Api Card Brand Type Structure
  property_count: 0
  slug: public-api-card-brand-type-structure
- name: Public Api Card Funding Type Structure
  property_count: 0
  slug: public-api-card-funding-type-structure
- name: Public Api Card Info Structure
  property_count: 2
  slug: public-api-card-info-structure
- name: Public Api Card Wallet Type Structure
  property_count: 0
  slug: public-api-card-wallet-type-structure
- name: Public Api Category Structure
  property_count: 6
  slug: public-api-category-structure
- name: Public Api Composite Finance Line Structure
  property_count: 1
  slug: public-api-composite-finance-line-structure
- name: Public Api Compute Applicable Rewards Request Structure
  property_count: 2
  slug: public-api-compute-applicable-rewards-request-structure
- name: Public Api Compute Applicable Rewards Response Structure
  property_count: 1
  slug: public-api-compute-applicable-rewards-response-structure
- name: Public Api Connection Structure
  property_count: 1
  slug: public-api-connection-structure
- name: Public Api Courier Service Delivery Info Structure
  property_count: 0
  slug: public-api-courier-service-delivery-info-structure
- name: Public Api Courier Structure
  property_count: 5
  slug: public-api-courier-structure
- name: Public Api Create Connection Request Structure
  property_count: 1
  slug: public-api-create-connection-request-structure
- name: Public Api Create Shipment Line Item Structure
  property_count: 6
  slug: public-api-create-shipment-line-item-structure
- name: Public Api Create Shipment Request Structure
  property_count: 2
  slug: public-api-create-shipment-request-structure
- name: Public Api Create Shipment Response Structure
  property_count: 1
  slug: public-api-create-shipment-response-structure
- name: Public Api Create User Request Structure
  property_count: 1
  slug: public-api-create-user-request-structure
- name: Public Api Create User Response Structure
  property_count: 1
  slug: public-api-create-user-response-structure
- name: Public Api Credentials Schema Version Structure
  property_count: 0
  slug: public-api-credentials-schema-version-structure
- name: Public Api Custom Bulk Resolution Options Structure
  property_count: 15
  slug: public-api-custom-bulk-resolution-options-structure
- name: Public Api Customer Item Modification Structure
  property_count: 3
  slug: public-api-customer-item-modification-structure
- name: Public Api Customer Payment Structure
  property_count: 8
  slug: public-api-customer-payment-structure
- name: Public Api Customer Payment V2 Structure
  property_count: 4
  slug: public-api-customer-payment-v2-structure
- name: Public Api Customer Tip Structure
  property_count: 1
  slug: public-api-customer-tip-structure
- name: Public Api Default Modifier Selection Data Structure
  property_count: 1
  slug: public-api-default-modifier-selection-data-structure
- name: Public Api Default Modifier Selection Structure
  property_count: 2
  slug: public-api-default-modifier-selection-structure
- name: Public Api Delivery Cost Structure
  property_count: 2
  slug: public-api-delivery-cost-structure
- name: Public Api Delivery Fee Structure
  property_count: 1
  slug: public-api-delivery-fee-structure
- name: Public Api Delivery Info Structure
  property_count: 7
  slug: public-api-delivery-info-structure
- name: Public Api Delivery Metadata Structure
  property_count: 2
  slug: public-api-delivery-metadata-structure
- name: Public Api Delivery Status Structure
  property_count: 0
  slug: public-api-delivery-status-structure
- name: Public Api Delivery Status Update Event Structure
  property_count: 14
  slug: public-api-delivery-status-update-event-structure
- name: Public Api Delivery Status Update Request Structure
  property_count: 12
  slug: public-api-delivery-status-update-request-structure
- name: Public Api Delivery Window Structure
  property_count: 2
  slug: public-api-delivery-window-structure
- name: Public Api Dietary Classification Structure
  property_count: 1
  slug: public-api-dietary-classification-structure
- name: Public Api Discover Stores Event Result Structure
  property_count: 2
  slug: public-api-discover-stores-event-result-structure
- name: Public Api Discovered Store Structure
  property_count: 2
  slug: public-api-discovered-store-structure
- name: Public Api Distance Structure
  property_count: 2
  slug: public-api-distance-structure
- name: Public Api Dropoff Info Structure
  property_count: 2
  slug: public-api-dropoff-info-structure
- name: Public Api Dropoff Instructions Structure
  property_count: 2
  slug: public-api-dropoff-instructions-structure
- name: Public Api Eater Order History Request Structure
  property_count: 4
  slug: public-api-eater-order-history-request-structure
- name: Public Api Eater Order History Response Structure
  property_count: 2
  slug: public-api-eater-order-history-response-structure
- name: Public Api Eater Order Structure
  property_count: 9
  slug: public-api-eater-order-structure
- name: Public Api Energy Kcal Structure
  property_count: 2
  slug: public-api-energy-kcal-structure
- name: Public Api Enrollment Field Structure
  property_count: 4
  slug: public-api-enrollment-field-structure
- name: Public Api Entity Path Override Rule Structure
  property_count: 0
  slug: public-api-entity-path-override-rule-structure
- name: Public Api Error Detail Structure
  property_count: 2
  slug: public-api-error-detail-structure
- name: Public Api Error Message Structure
  property_count: 2
  slug: public-api-error-message-structure
- name: Public Api Event Callback Error Structure
  property_count: 2
  slug: public-api-event-callback-error-structure
- name: Public Api Event Notification Base Structure
  property_count: 3
  slug: public-api-event-notification-base-structure
- name: Public Api Event Notification Structure
  property_count: 4
  slug: public-api-event-notification-structure
- name: Public Api Event Result Metadata Structure
  property_count: 3
  slug: public-api-event-result-metadata-structure
- name: Public Api Existing Credential Structure
  property_count: 2
  slug: public-api-existing-credential-structure
- name: Public Api Exposed Third Party Info Structure
  property_count: 2
  slug: public-api-exposed-third-party-info-structure
- name: Public Api Fetch Credentials Event Structure
  property_count: 1
  slug: public-api-fetch-credentials-event-structure
- name: Public Api Financial Data Structure
  property_count: 19
  slug: public-api-financial-data-structure
- name: Public Api Financial Invoice Structure
  property_count: 4
  slug: public-api-financial-invoice-structure
- name: Public Api Financial Transaction Structure
  property_count: 12
  slug: public-api-financial-transaction-structure
- name: Public Api Fulfilled Credential Structure
  property_count: 2
  slug: public-api-fulfilled-credential-structure
- name: Public Api Fulfillment Info Structure
  property_count: 7
  slug: public-api-fulfillment-info-structure
- name: Public Api Fulfillment Mode Override Rule Structure
  property_count: 0
  slug: public-api-fulfillment-mode-override-rule-structure
- name: Public Api Fulfillment Path Entity Structure
  property_count: 2
  slug: public-api-fulfillment-path-entity-structure
- name: Public Api Generate Report Multi Request Structure
  property_count: 6
  slug: public-api-generate-report-multi-request-structure
- name: Public Api Generate Report Response Structure
  property_count: 1
  slug: public-api-generate-report-response-structure
- name: Public Api Get Enrollment Config Response Structure
  property_count: 1
  slug: public-api-get-enrollment-config-response-structure
- name: Public Api Get Report Status Response Structure
  property_count: 2
  slug: public-api-get-report-status-response-structure
- name: Public Api Get Store Details Event Result Structure
  property_count: 2
  slug: public-api-get-store-details-event-result-structure
- name: Public Api Get User Response Structure
  property_count: 1
  slug: public-api-get-user-response-structure
- name: Public Api Gtin Structure
  property_count: 0
  slug: public-api-gtin-structure
- name: Public Api Hour Interval Structure
  property_count: 5
  slug: public-api-hour-interval-structure
- name: Public Api Hours Data Structure
  property_count: 3
  slug: public-api-hours-data-structure
- name: Public Api Hours Structure
  property_count: 1
  slug: public-api-hours-structure
- name: Public Api Hydra Token Structure
  property_count: 4
  slug: public-api-hydra-token-structure
- name: Public Api Intent To Cancel Event Structure
  property_count: 2
  slug: public-api-intent-to-cancel-event-structure
- name: Public Api Inventory Summaries Response Structure
  property_count: 2
  slug: public-api-inventory-summaries-response-structure
- name: Public Api Inventory Summary Structure
  property_count: 8
  slug: public-api-inventory-summary-structure
- name: Public Api Invoice Payout Info Structure
  property_count: 4
  slug: public-api-invoice-payout-info-structure
- name: Public Api Item 2 Structure
  property_count: 5
  slug: public-api-item-2-structure
- name: Public Api Item 3 Structure
  property_count: 3
  slug: public-api-item-3-structure
- name: Public Api Item 4 Structure
  property_count: 5
  slug: public-api-item-4-structure
- name: Public Api Item Added Modification Structure
  property_count: 1
  slug: public-api-item-added-modification-structure
- name: Public Api Item Modifier Structure
  property_count: 11
  slug: public-api-item-modifier-structure
- name: Public Api Item Price Override Structure
  property_count: 3
  slug: public-api-item-price-override-structure
- name: Public Api Item Selector Structure
  property_count: 2
  slug: public-api-item-selector-structure
- name: Public Api Item Status Structure
  property_count: 2
  slug: public-api-item-status-structure
- name: Public Api Item Structure
  property_count: 14
  slug: public-api-item-structure
- name: Public Api Item Tax Structure
  property_count: 2
  slug: public-api-item-tax-structure
- name: Public Api Item Update Request Structure
  property_count: 9
  slug: public-api-item-update-request-structure
- name: Public Api Job Id Structure
  property_count: 0
  slug: public-api-job-id-structure
- name: Public Api Job Reference Structure
  property_count: 2
  slug: public-api-job-reference-structure
- name: Public Api List Brands Response Structure
  property_count: 2
  slug: public-api-list-brands-response-structure
- name: Public Api List Shipments Response Structure
  property_count: 2
  slug: public-api-list-shipments-response-structure
- name: Public Api List Stores Response Structure
  property_count: 2
  slug: public-api-list-stores-response-structure
- name: Public Api Location Structure
  property_count: 2
  slug: public-api-location-structure
- name: Public Api Loyalty Info Structure
  property_count: 1
  slug: public-api-loyalty-info-structure
- name: Public Api Manager Cancel Order Request Structure
  property_count: 2
  slug: public-api-manager-cancel-order-request-structure
- name: Public Api Manager Confirm Order Request Structure
  property_count: 1
  slug: public-api-manager-confirm-order-request-structure
- name: Public Api Manager Item Issue Structure
  property_count: 2
  slug: public-api-manager-item-issue-structure
- name: Public Api Manager Item Issues Structure
  property_count: 2
  slug: public-api-manager-item-issues-structure
- name: Public Api Manager Order Cancel Details Structure
  property_count: 1
  slug: public-api-manager-order-cancel-details-structure
- name: Public Api Manager Order Issue Structure
  property_count: 2
  slug: public-api-manager-order-issue-structure
- name: Public Api Manager Order Issues Structure
  property_count: 2
  slug: public-api-manager-order-issues-structure
- name: Public Api Mandate Status Structure
  property_count: 0
  slug: public-api-mandate-status-structure
- name: Public Api Marketintel Coordinates Structure
  property_count: 2
  slug: public-api-marketintel-coordinates-structure
- name: Public Api Marketintel Geo Location Information Structure
  property_count: 5
  slug: public-api-marketintel-geo-location-information-structure
- name: Public Api Marketintel Hours Data Structure
  property_count: 3
  slug: public-api-marketintel-hours-data-structure
- name: Public Api Marketintel Location Based Information Structure
  property_count: 2
  slug: public-api-marketintel-location-based-information-structure
- name: Public Api Marketintel Regular Hours Structure
  property_count: 2
  slug: public-api-marketintel-regular-hours-structure
- name: Public Api Marketintel Special Hours Structure
  property_count: 3
  slug: public-api-marketintel-special-hours-structure
- name: Public Api Marketintel Store Chain Structure
  property_count: 2
  slug: public-api-marketintel-store-chain-structure
- name: Public Api Marketintel Store Delivery Information Structure
  property_count: 4
  slug: public-api-marketintel-store-delivery-information-structure
- name: Public Api Marketintel Store Details Structure
  property_count: 21
  slug: public-api-marketintel-store-details-structure
- name: Public Api Marketintel Store Listing Structure
  property_count: 3
  slug: public-api-marketintel-store-listing-structure
- name: Public Api Marketintel Store Menu Structure
  property_count: 3
  slug: public-api-marketintel-store-menu-structure
- name: Public Api Marketintel Store Price Level Structure
  property_count: 2
  slug: public-api-marketintel-store-price-level-structure
- name: Public Api Marketintel Store Promotion Structure
  property_count: 4
  slug: public-api-marketintel-store-promotion-structure
- name: Public Api Marketintel Store Rating Structure
  property_count: 3
  slug: public-api-marketintel-store-rating-structure
- name: Public Api Marketintel Store Sales Structure
  property_count: 3
  slug: public-api-marketintel-store-sales-structure
- name: Public Api Marketintel Time Range Structure
  property_count: 2
  slug: public-api-marketintel-time-range-structure
- name: Public Api Menu 3 Pd Structure
  property_count: 8
  slug: public-api-menu-3-pd-structure
- name: Public Api Menu Async Job Type Structure
  property_count: 0
  slug: public-api-menu-async-job-type-structure
- name: Public Api Menu Async Latest Job For Store Response Structure
  property_count: 1
  slug: public-api-menu-async-latest-job-for-store-response-structure
- name: Public Api Menu Asynchronous Job Structure
  property_count: 3
  slug: public-api-menu-asynchronous-job-structure
- name: Public Api Menu Data Structure
  property_count: 5
  slug: public-api-menu-data-structure
- name: Public Api Menu Item 3 Pd Structure
  property_count: 12
  slug: public-api-menu-item-3-pd-structure
- name: Public Api Menu Item Pos Structure
  property_count: 11
  slug: public-api-menu-item-pos-structure
- name: Public Api Menu Job Publish State Structure
  property_count: 0
  slug: public-api-menu-job-publish-state-structure
- name: Public Api Menu Job Type Structure
  property_count: 0
  slug: public-api-menu-job-type-structure
- name: Public Api Menu Pos Structure
  property_count: 7
  slug: public-api-menu-pos-structure
- name: Public Api Menu Publish Event Structure
  property_count: 1
  slug: public-api-menu-publish-event-structure
- name: Public Api Menu Publish Job State Structure
  property_count: 2
  slug: public-api-menu-publish-job-state-structure
- name: Public Api Menu Publish Request Structure
  property_count: 1
  slug: public-api-menu-publish-request-structure
- name: Public Api Menu Publish Response Menu Publish Targets Structure
  property_count: 1
  slug: public-api-menu-publish-response-menu-publish-targets-structure
- name: Public Api Menu Publish Response Structure
  property_count: 3
  slug: public-api-menu-publish-response-structure
- name: Public Api Menu Publish Target Structure
  property_count: 1
  slug: public-api-menu-publish-target-structure
- name: Public Api Menu Publish Targets Structure
  property_count: 1
  slug: public-api-menu-publish-targets-structure
- name: Public Api Menus Reward Structure
  property_count: 3
  slug: public-api-menus-reward-structure
- name: Public Api Menus Structure
  property_count: 5
  slug: public-api-menus-structure
- name: Public Api Menus Upsert Request Structure
  property_count: 4
  slug: public-api-menus-upsert-request-structure
- name: Public Api Metadata Object Structure
  property_count: 5
  slug: public-api-metadata-object-structure
- name: Public Api Modifier Group Structure
  property_count: 10
  slug: public-api-modifier-group-structure
- name: Public Api Modifier Group Update Request Structure
  property_count: 9
  slug: public-api-modifier-group-update-request-structure
- name: Public Api Modifier Item Structure
  property_count: 5
  slug: public-api-modifier-item-structure
- name: Public Api Money Structure
  property_count: 2
  slug: public-api-money-structure
- name: Public Api Null Event Structure
  property_count: 0
  slug: public-api-null-event-structure
- name: Public Api Nutrition Content Structure
  property_count: 22
  slug: public-api-nutrition-content-structure
- name: Public Api Nutritional Info Structure
  property_count: 2
  slug: public-api-nutritional-info-structure
- name: Public Api Oauth Token Generation Request Structure
  property_count: 7
  slug: public-api-oauth-token-generation-request-structure
- name: Public Api Operation Type Structure
  property_count: 0
  slug: public-api-operation-type-structure
- name: Public Api Optional Store Id In Metadata Structure
  property_count: 1
  slug: public-api-optional-store-id-in-metadata-structure
- name: Public Api Order 2 Structure
  property_count: 4
  slug: public-api-order-2-structure
- name: Public Api Order Component Id Structure
  property_count: 2
  slug: public-api-order-component-id-structure
- name: Public Api Order Confirm Event Structure
  property_count: 1
  slug: public-api-order-confirm-event-structure
- name: Public Api Order Customer Items Update Request Structure
  property_count: 2
  slug: public-api-order-customer-items-update-request-structure
- name: Public Api Order Customer Payment Update Request Structure
  property_count: 4
  slug: public-api-order-customer-payment-update-request-structure
- name: Public Api Order Delivery Info Update Request Structure
  property_count: 1
  slug: public-api-order-delivery-info-update-request-structure
- name: Public Api Order External Identifiers Structure
  property_count: 5
  slug: public-api-order-external-identifiers-structure
- name: Public Api Order Feed Structure
  property_count: 2
  slug: public-api-order-feed-structure
- name: Public Api Order Fulfilled Event Structure
  property_count: 1
  slug: public-api-order-fulfilled-event-structure
- name: Public Api Order Handed Off Event Structure
  property_count: 4
  slug: public-api-order-handed-off-event-structure
- name: Public Api Order Identifier Finance Structure
  property_count: 2
  slug: public-api-order-identifier-finance-structure
- name: Public Api Order Identifier Structure
  property_count: 2
  slug: public-api-order-identifier-structure
- name: Public Api Order Issue Structure
  property_count: 1
  slug: public-api-order-issue-structure
- name: Public Api Order Item Information Structure
  property_count: 3
  slug: public-api-order-item-information-structure
- name: Public Api Order Prep Time Update Request Structure
  property_count: 1
  slug: public-api-order-prep-time-update-request-structure
- name: Public Api Order Price Adjusted Modification Structure
  property_count: 1
  slug: public-api-order-price-adjusted-modification-structure
- name: Public Api Order Ready Event Structure
  property_count: 1
  slug: public-api-order-ready-event-structure
- name: Public Api Order Reference Structure
  property_count: 2
  slug: public-api-order-reference-structure
- name: Public Api Order Status Event Structure
  property_count: 2
  slug: public-api-order-status-event-structure
- name: Public Api Order Status History Structure
  property_count: 2
  slug: public-api-order-status-history-structure
- name: Public Api Order Status Update Request Structure
  property_count: 1
  slug: public-api-order-status-update-request-structure
- name: Public Api Order Structure
  property_count: 14
  slug: public-api-order-structure
- name: Public Api Order Total Structure
  property_count: 8
  slug: public-api-order-total-structure
- name: Public Api Order Total V2 Structure
  property_count: 3
  slug: public-api-order-total-v2-structure
- name: Public Api Order With Manager Info Structure
  property_count: 5
  slug: public-api-order-with-manager-info-structure
- name: Public Api Org Info Structure
  property_count: 2
  slug: public-api-org-info-structure
- name: Public Api Organization Structure
  property_count: 2
  slug: public-api-organization-structure
- name: Public Api Override Rule 3 Pd Structure
  property_count: 1
  slug: public-api-override-rule-3-pd-structure
- name: Public Api Override Rule Structure
  property_count: 1
  slug: public-api-override-rule-structure
- name: Public Api Parcel Carrier Delivery Info Structure
  property_count: 0
  slug: public-api-parcel-carrier-delivery-info-structure
- name: Public Api Pause Reason Structure
  property_count: 0
  slug: public-api-pause-reason-structure
- name: Public Api Pause Request Structure
  property_count: 4
  slug: public-api-pause-request-structure
- name: Public Api Pause Response Structure
  property_count: 1
  slug: public-api-pause-response-structure
- name: Public Api Pause Store Event Result Structure
  property_count: 2
  slug: public-api-pause-store-event-result-structure
- name: Public Api Payment Details Ach Structure
  property_count: 7
  slug: public-api-payment-details-ach-structure
- name: Public Api Payment Details Acss Structure
  property_count: 9
  slug: public-api-payment-details-acss-structure
- name: Public Api Payment Details Bacs Structure
  property_count: 6
  slug: public-api-payment-details-bacs-structure
- name: Public Api Payment Details Becs Structure
  property_count: 5
  slug: public-api-payment-details-becs-structure
- name: Public Api Payment Details Card Structure
  property_count: 10
  slug: public-api-payment-details-card-structure
- name: Public Api Payment Details Sepa Structure
  property_count: 8
  slug: public-api-payment-details-sepa-structure
- name: Public Api Payment Record Structure
  property_count: 7
  slug: public-api-payment-record-structure
- name: Public Api Payout Info Structure
  property_count: 2
  slug: public-api-payout-info-structure
- name: Public Api Payout Structure
  property_count: 3
  slug: public-api-payout-structure
- name: Public Api Percentage Value Structure
  property_count: 1
  slug: public-api-percentage-value-structure
- name: Public Api Person Structure
  property_count: 5
  slug: public-api-person-structure
- name: Public Api Personal Identifiers Structure
  property_count: 2
  slug: public-api-personal-identifiers-structure
- name: Public Api Photo Structure
  property_count: 4
  slug: public-api-photo-structure
- name: Public Api Pick Up Info Structure
  property_count: 1
  slug: public-api-pick-up-info-structure
- name: Public Api Picture Proof Structure
  property_count: 1
  slug: public-api-picture-proof-structure
- name: Public Api Picture Requirement Structure
  property_count: 1
  slug: public-api-picture-requirement-structure
- name: Public Api Ping Event Structure
  property_count: 1
  slug: public-api-ping-event-structure
- name: Public Api Pong Object Structure
  property_count: 2
  slug: public-api-pong-object-structure
- name: Public Api Pos Injection State Update Event Structure
  property_count: 4
  slug: public-api-pos-injection-state-update-event-structure
- name: Public Api Pos Menu Sync Request Structure
  property_count: 3
  slug: public-api-pos-menu-sync-request-structure
- name: Public Api Pos Menu Sync Response Structure
  property_count: 1
  slug: public-api-pos-menu-sync-response-structure
- name: Public Api Posorder Status Update Request Structure
  property_count: 2
  slug: public-api-posorder-status-update-request-structure
- name: Public Api Preparation Time Structure
  property_count: 1
  slug: public-api-preparation-time-structure
- name: Public Api Price Override Structure
  property_count: 2
  slug: public-api-price-override-structure
- name: Public Api Process Store Service Provider Status Structure
  property_count: 7
  slug: public-api-process-store-service-provider-status-structure
- name: Public Api Processing Status Response Structure
  property_count: 1
  slug: public-api-processing-status-response-structure
- name: Public Api Promotion Details Structure
  property_count: 3
  slug: public-api-promotion-details-structure
- name: Public Api Quantity Updated Modification Structure
  property_count: 3
  slug: public-api-quantity-updated-modification-structure
- name: Public Api Record Payment Type Structure
  property_count: 0
  slug: public-api-record-payment-type-structure
- name: Public Api Record Provider Type Structure
  property_count: 0
  slug: public-api-record-provider-type-structure
- name: Public Api Redeem And Accumulate Rewards Request Structure
  property_count: 3
  slug: public-api-redeem-and-accumulate-rewards-request-structure
- name: Public Api Redeem And Accumulate Rewards Response Structure
  property_count: 3
  slug: public-api-redeem-and-accumulate-rewards-response-structure
- name: Public Api Refund Rewards Request Structure
  property_count: 2
  slug: public-api-refund-rewards-request-structure
- name: Public Api Refund Rewards Response Structure
  property_count: 1
  slug: public-api-refund-rewards-response-structure
- name: Public Api Regular Hours Structure
  property_count: 2
  slug: public-api-regular-hours-structure
- name: Public Api Remove Storelink Event Structure
  property_count: 1
  slug: public-api-remove-storelink-event-structure
- name: Public Api Report Generated Event Structure
  property_count: 2
  slug: public-api-report-generated-event-structure
- name: Public Api Request Action Structure
  property_count: 4
  slug: public-api-request-action-structure
- name: Public Api Request Delivery Quote Callback Request Structure
  property_count: 9
  slug: public-api-request-delivery-quote-callback-request-structure
- name: Public Api Request Delivery Quote Event Structure
  property_count: 12
  slug: public-api-request-delivery-quote-event-structure
- name: Public Api Request State Info Structure
  property_count: 6
  slug: public-api-request-state-info-structure
- name: Public Api Request State Structure
  property_count: 0
  slug: public-api-request-state-structure
- name: Public Api Required Address Structure
  property_count: 8
  slug: public-api-required-address-structure
- name: Public Api Required Delivery Info Structure
  property_count: 7
  slug: public-api-required-delivery-info-structure
- name: Public Api Required Event Result Metadata Structure
  property_count: 3
  slug: public-api-required-event-result-metadata-structure
- name: Public Api Required Person Structure
  property_count: 5
  slug: public-api-required-person-structure
- name: Public Api Review Reply Request Structure
  property_count: 5
  slug: public-api-review-reply-request-structure
- name: Public Api Review Reply Response Structure
  property_count: 1
  slug: public-api-review-reply-response-structure
- name: Public Api Reward Effect Structure
  property_count: 1
  slug: public-api-reward-effect-structure
- name: Public Api Reward Structure
  property_count: 7
  slug: public-api-reward-structure
- name: Public Api Search Users Response Structure
  property_count: 2
  slug: public-api-search-users-response-structure
- name: Public Api Selected Menu Reward Structure
  property_count: 1
  slug: public-api-selected-menu-reward-structure
- name: Public Api Selected Reward Structure
  property_count: 3
  slug: public-api-selected-reward-structure
- name: Public Api Self Drop Delivery Info Structure
  property_count: 0
  slug: public-api-self-drop-delivery-info-structure
- name: Public Api Send Menu Event Callback Structure
  property_count: 1
  slug: public-api-send-menu-event-callback-structure
- name: Public Api Service Override Rule Structure
  property_count: 0
  slug: public-api-service-override-rule-structure
- name: Public Api Servings Structure
  property_count: 2
  slug: public-api-servings-structure
- name: Public Api Shipment Delivery Info Structure
  property_count: 0
  slug: public-api-shipment-delivery-info-structure
- name: Public Api Shipment Line Item Structure
  property_count: 4
  slug: public-api-shipment-line-item-structure
- name: Public Api Shipment State Change Structure
  property_count: 2
  slug: public-api-shipment-state-change-structure
- name: Public Api Shipment State Structure
  property_count: 0
  slug: public-api-shipment-state-structure
- name: Public Api Shipment Structure
  property_count: 4
  slug: public-api-shipment-structure
- name: Public Api Signature Proof Structure
  property_count: 3
  slug: public-api-signature-proof-structure
- name: Public Api Signature Requirement Structure
  property_count: 3
  slug: public-api-signature-requirement-structure
- name: Public Api Simple Finance Line Structure
  property_count: 3
  slug: public-api-simple-finance-line-structure
- name: Public Api Simple Financial Transaction Structure
  property_count: 9
  slug: public-api-simple-financial-transaction-structure
- name: Public Api Simple Order Identifier Finance Structure
  property_count: 1
  slug: public-api-simple-order-identifier-finance-structure
- name: Public Api Simulate Rewards Request Structure
  property_count: 3
  slug: public-api-simulate-rewards-request-structure
- name: Public Api Simulate Rewards Response Structure
  property_count: 2
  slug: public-api-simulate-rewards-response-structure
- name: Public Api Sku Barcode Structure
  property_count: 2
  slug: public-api-sku-barcode-structure
- name: Public Api Sku Details Structure
  property_count: 13
  slug: public-api-sku-details-structure
- name: Public Api Source External Identifiers Structure
  property_count: 5
  slug: public-api-source-external-identifiers-structure
- name: Public Api Special Hours Structure
  property_count: 3
  slug: public-api-special-hours-structure
- name: Public Api Status Structure
  property_count: 0
  slug: public-api-status-structure
- name: Public Api Storage Requirement Structure
  property_count: 1
  slug: public-api-storage-requirement-structure
- name: Public Api Store 2 Structure
  property_count: 6
  slug: public-api-store-2-structure
- name: Public Api Store 3 Structure
  property_count: 2
  slug: public-api-store-3-structure
- name: Public Api Store Availability Event Result Structure
  property_count: 3
  slug: public-api-store-availability-event-result-structure
- name: Public Api Store Hours Configuration Event Result Structure
  property_count: 3
  slug: public-api-store-hours-configuration-event-result-structure
- name: Public Api Store Hours Configuration Structure
  property_count: 3
  slug: public-api-store-hours-configuration-structure
- name: Public Api Store Hours Structure
  property_count: 2
  slug: public-api-store-hours-structure
- name: Public Api Store Id Structure
  property_count: 0
  slug: public-api-store-id-structure
- name: Public Api Store Info 2 Structure
  property_count: 5
  slug: public-api-store-info-2-structure
- name: Public Api Store Info Structure
  property_count: 6
  slug: public-api-store-info-structure
- name: Public Api Store Structure
  property_count: 3
  slug: public-api-store-structure
- name: Public Api Storefront Error Structure
  property_count: 2
  slug: public-api-storefront-error-structure
- name: Public Api Storefront Regular Hours Structure
  property_count: 2
  slug: public-api-storefront-regular-hours-structure
- name: Public Api Storefront Special Hours Structure
  property_count: 3
  slug: public-api-storefront-special-hours-structure
- name: Public Api Storefront Time Range Structure
  property_count: 2
  slug: public-api-storefront-time-range-structure
- name: Public Api Subtotal Reward Structure
  property_count: 2
  slug: public-api-subtotal-reward-structure
- name: Public Api Subtotal Structure
  property_count: 1
  slug: public-api-subtotal-structure
- name: Public Api Suspend Items Request Structure
  property_count: 3
  slug: public-api-suspend-items-request-structure
- name: Public Api Suspension Status Structure
  property_count: 2
  slug: public-api-suspension-status-structure
- name: Public Api Time Range Structure
  property_count: 2
  slug: public-api-time-range-structure
- name: Public Api Totals Structure
  property_count: 4
  slug: public-api-totals-structure
- name: Public Api Trigger Menu Structure
  property_count: 3
  slug: public-api-trigger-menu-structure
- name: Public Api Trigger Structure
  property_count: 1
  slug: public-api-trigger-structure
- name: Public Api Unit Price And Count Structure
  property_count: 2
  slug: public-api-unit-price-and-count-structure
- name: Public Api Unpause Request Structure
  property_count: 1
  slug: public-api-unpause-request-structure
- name: Public Api Unpause Response Structure
  property_count: 1
  slug: public-api-unpause-response-structure
- name: Public Api Unpause Store Event Result Structure
  property_count: 1
  slug: public-api-unpause-store-event-result-structure
- name: Public Api Unpause Store Event Structure
  property_count: 0
  slug: public-api-unpause-store-event-structure
- name: Public Api Unsuspend Items Request Structure
  property_count: 2
  slug: public-api-unsuspend-items-request-structure
- name: Public Api Update Delivery Request Callback Request Structure
  property_count: 2
  slug: public-api-update-delivery-request-callback-request-structure
- name: Public Api Update Delivery Request Event Structure
  property_count: 6
  slug: public-api-update-delivery-request-event-structure
- name: Public Api Update Item Status Entry Structure
  property_count: 2
  slug: public-api-update-item-status-entry-structure
- name: Public Api Update Storelink Status Request Structure
  property_count: 2
  slug: public-api-update-storelink-status-request-structure
- name: Public Api Upload Past Orders Request Structure
  property_count: 1
  slug: public-api-upload-past-orders-request-structure
- name: Public Api Upload Past Orders Response Structure
  property_count: 1
  slug: public-api-upload-past-orders-response-structure
- name: Public Api Upsert Full Menu Event Callback Structure
  property_count: 1
  slug: public-api-upsert-full-menu-event-callback-structure
- name: Public Api Upsert Hours Event Structure
  property_count: 1
  slug: public-api-upsert-hours-event-structure
- name: Public Api Upsert Storelink Event Result Request Structure
  property_count: 3
  slug: public-api-upsert-storelink-event-result-request-structure
- name: Public Api Upsert Storelink Event Structure
  property_count: 3
  slug: public-api-upsert-storelink-event-structure
- name: Public Api User Account Structure
  property_count: 3
  slug: public-api-user-account-structure
- name: Public Api User Balance Structure
  property_count: 2
  slug: public-api-user-balance-structure
- name: Public Api User Field Structure
  property_count: 2
  slug: public-api-user-field-structure
- name: Public Api User Structure
  property_count: 2
  slug: public-api-user-structure
- name: Public Api Vehicle Information Structure
  property_count: 3
  slug: public-api-vehicle-information-structure
- name: Public Api Verification Proof Structure
  property_count: 2
  slug: public-api-verification-proof-structure
- name: Public Api Verification Requirements Structure
  property_count: 2
  slug: public-api-verification-requirements-structure
- name: Public Api View Credential Structure
  property_count: 5
  slug: public-api-view-credential-structure
- name: Public Api View Credentials Array Structure
  property_count: 2
  slug: public-api-view-credentials-array-structure
jsonld:
- class_count: 294
  name: Otter Public Api Context
  property_count: 557
  slug: otter-public-api-context
layout: provider
modified: '2026-06-03'
name: Otter
nav: Providers
network: true
overview: 'Otter publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account Pairing Endpoints API, Auth Endpoints API, Callback Endpoints API, and 16 more. Tagged areas include Restaurant, Order Management, Delivery, Online Ordering, and Menu Management.


  The Otter catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Otter''s developer surface includes authentication, documentation, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Otter Plans Pricing
  plan_count: 4
  slug: otter-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 6
  name: Otter Rate Limits
  slug: otter-rate-limits
rules:
- name: Otter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: otter-jsonschema-spectral-rules
- name: Otter API Rules
  rule_count: 29
  severity_counts:
    error: 6
    hint: 0
    info: 10
    warn: 13
  slug: otter-public-api-rules
scopes:
- name: Otter Scopes
  scope_count: 31
  slug: otter-scopes
  summary_line: 31 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 28.5
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 19
      marker_coverage: 100.0
      total: 19
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/otter/refs/heads/main/screenshots/otter-2026-06-20T191236.png
security:
- kind: authentication
  name: Otter Authentication
  slug: otter-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Otter Domain Security
  slug: otter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: otter
tags:
- Restaurant
- Order Management
- Delivery
- Online Ordering
- Menu Management
- Analytics
use_cases:
- description: Sync orders and menus between a third-party point-of-sale system and Otter-connected channels.
  name: POS Integration
- description: Provide delivery services by responding to quote and delivery-request webhooks and posting status updates.
  name: Delivery Provider Integration
- description: Centrally manage and publish menus and availability across many stores and storefronts.
  name: Menu Aggregator
- description: Pull payout, order-total, and transaction data to reconcile restaurant finances.
  name: Financial Reconciliation
- description: Power a loyalty program by computing and redeeming rewards against Otter orders.
  name: Loyalty Program
website: https://www.tryotter.com
---
