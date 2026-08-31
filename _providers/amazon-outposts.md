---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Outposts Agentic Access
  operation_count: 26
  slug: amazon-outposts-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 1
apis:
- description: The Catalog API from Amazon Outposts — 2 operation(s) for catalog.
  name: Amazon Outposts Catalog API
  slug: amazon-outposts-catalog-api
- description: The Connections API from Amazon Outposts — 2 operation(s) for connections.
  name: Amazon Outposts Connections API
  slug: amazon-outposts-connections-api
- description: The List Orders API from Amazon Outposts — 1 operation(s) for list orders.
  name: Amazon Outposts List Orders API
  slug: amazon-outposts-list-orders-api
- description: The Orders API from Amazon Outposts — 3 operation(s) for orders.
  name: Amazon Outposts Orders API
  slug: amazon-outposts-orders-api
- description: The Outposts API from Amazon Outposts — 4 operation(s) for outposts.
  name: Amazon Outposts Outposts API
  slug: amazon-outposts-outposts-api
- description: The Sites API from Amazon Outposts — 5 operation(s) for sites.
  name: Amazon Outposts Sites API
  slug: amazon-outposts-sites-api
- description: The Tags API from Amazon Outposts — 2 operation(s) for tags.
  name: Amazon Outposts Tags API
  slug: amazon-outposts-tags-api
artifact_total: 555
collections:
- collection_type: postman
  name: AWS Outposts Catalog API
  slug: postman-amazon-outposts-catalog-api
- collection_type: postman
  name: AWS Outposts Catalog Connections API
  slug: postman-amazon-outposts-connections-api
- collection_type: postman
  name: AWS Outposts Catalog List Orders API
  slug: postman-amazon-outposts-list-orders-api
- collection_type: postman
  name: AWS Outposts Catalog Orders API
  slug: postman-amazon-outposts-orders-api
- collection_type: postman
  name: AWS Catalog Outposts API
  slug: postman-amazon-outposts-outposts-api
- collection_type: postman
  name: AWS Outposts Catalog Sites API
  slug: postman-amazon-outposts-sites-api
- collection_type: postman
  name: AWS Outposts Catalog Tags API
  slug: postman-amazon-outposts-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Outposts Catalog API
  slug: open-amazon-outposts-catalog-api
- collection_type: open
  name: AWS Outposts Catalog Connections API
  slug: open-amazon-outposts-connections-api
- collection_type: open
  name: AWS Outposts Catalog List Orders API
  slug: open-amazon-outposts-list-orders-api
- collection_type: open
  name: AWS Outposts Catalog Orders API
  slug: open-amazon-outposts-orders-api
- collection_type: open
  name: AWS Catalog Outposts API
  slug: open-amazon-outposts-outposts-api
- collection_type: open
  name: AWS Outposts Catalog Sites API
  slug: open-amazon-outposts-sites-api
- collection_type: open
  name: AWS Outposts Catalog Tags API
  slug: open-amazon-outposts-tags-api
- collection_type: open
  name: AWS Outposts
  slug: open-amazon-outposts
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-outposts/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-outposts-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-outposts-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-outposts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-outposts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-outposts-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/outposts/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/outposts/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/outposts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/tag/aws-outposts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/outposts/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-outposts-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-outposts-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-outposts-openapi-context.jsonld
- group: docs
  title: Openapi Access Denied Exception
  type: JSONSchema
  url: json-schema/openapi-access-denied-exception-schema.json
- group: docs
  title: Openapi Account Id
  type: JSONSchema
  url: json-schema/openapi-account-id-schema.json
- group: docs
  title: Openapi Address Line1
  type: JSONSchema
  url: json-schema/openapi-address-line1-schema.json
- group: docs
  title: Openapi Address Line2
  type: JSONSchema
  url: json-schema/openapi-address-line2-schema.json
- group: docs
  title: Openapi Address Line3
  type: JSONSchema
  url: json-schema/openapi-address-line3-schema.json
created: '2026-03-16'
description: AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience. It allows you to extend AWS infrastructure, AWS services, APIs, and tools to virtually any data center, co-location space, or on-premises facility.
examples:
- key_count: 0
  name: Openapi Access Denied Exception Example
  slug: openapi-access-denied-exception-example
- key_count: 0
  name: Openapi Account Id Example
  slug: openapi-account-id-example
- key_count: 11
  name: Openapi Address Example
  slug: openapi-address-example
- key_count: 0
  name: Openapi Address Line1 Example
  slug: openapi-address-line1-example
- key_count: 0
  name: Openapi Address Line2 Example
  slug: openapi-address-line2-example
- key_count: 0
  name: Openapi Address Line3 Example
  slug: openapi-address-line3-example
- key_count: 0
  name: Openapi Address Type Example
  slug: openapi-address-type-example
- key_count: 0
  name: Openapi Arn Example
  slug: openapi-arn-example
- key_count: 0
  name: Openapi Asset Id Example
  slug: openapi-asset-id-example
- key_count: 5
  name: Openapi Asset Info Example
  slug: openapi-asset-info-example
- key_count: 1
  name: Openapi Asset Location Example
  slug: openapi-asset-location-example
- key_count: 0
  name: Openapi Asset State Example
  slug: openapi-asset-state-example
- key_count: 0
  name: Openapi Asset Type Example
  slug: openapi-asset-type-example
- key_count: 0
  name: Openapi Availability Zone Example
  slug: openapi-availability-zone-example
- key_count: 0
  name: Openapi Availability Zone Id Example
  slug: openapi-availability-zone-id-example
- key_count: 0
  name: Openapi Cancel Order Input Example
  slug: openapi-cancel-order-input-example
- key_count: 0
  name: Openapi Cancel Order Output Example
  slug: openapi-cancel-order-output-example
- key_count: 0
  name: Openapi Catalog Item Class Example
  slug: openapi-catalog-item-class-example
- key_count: 7
  name: Openapi Catalog Item Example
  slug: openapi-catalog-item-example
- key_count: 0
  name: Openapi Catalog Item Power Kva Example
  slug: openapi-catalog-item-power-kva-example
- key_count: 0
  name: Openapi Catalog Item Status Example
  slug: openapi-catalog-item-status-example
- key_count: 0
  name: Openapi Catalog Item Weight Lbs Example
  slug: openapi-catalog-item-weight-lbs-example
- key_count: 0
  name: Openapi Cidr Example
  slug: openapi-cidr-example
- key_count: 0
  name: Openapi City Example
  slug: openapi-city-example
- key_count: 0
  name: Openapi Compute Asset State Example
  slug: openapi-compute-asset-state-example
- key_count: 2
  name: Openapi Compute Attributes Example
  slug: openapi-compute-attributes-example
- key_count: 0
  name: Openapi Conflict Exception Example
  slug: openapi-conflict-exception-example
- key_count: 6
  name: Openapi Connection Details Example
  slug: openapi-connection-details-example
- key_count: 0
  name: Openapi Connection Id Example
  slug: openapi-connection-id-example
- key_count: 0
  name: Openapi Contact Name Example
  slug: openapi-contact-name-example
- key_count: 0
  name: Openapi Contact Phone Number Example
  slug: openapi-contact-phone-number-example
- key_count: 0
  name: Openapi Country Code Example
  slug: openapi-country-code-example
- key_count: 4
  name: Openapi Create Order Input Example
  slug: openapi-create-order-input-example
- key_count: 1
  name: Openapi Create Order Output Example
  slug: openapi-create-order-output-example
- key_count: 7
  name: Openapi Create Outpost Input Example
  slug: openapi-create-outpost-input-example
- key_count: 1
  name: Openapi Create Outpost Output Example
  slug: openapi-create-outpost-output-example
- key_count: 7
  name: Openapi Create Site Input Example
  slug: openapi-create-site-input-example
- key_count: 1
  name: Openapi Create Site Output Example
  slug: openapi-create-site-output-example
- key_count: 0
  name: Openapi Delete Outpost Input Example
  slug: openapi-delete-outpost-input-example
- key_count: 0
  name: Openapi Delete Outpost Output Example
  slug: openapi-delete-outpost-output-example
- key_count: 0
  name: Openapi Delete Site Input Example
  slug: openapi-delete-site-input-example
- key_count: 0
  name: Openapi Delete Site Output Example
  slug: openapi-delete-site-output-example
- key_count: 0
  name: Openapi Device Serial Number Example
  slug: openapi-device-serial-number-example
- key_count: 0
  name: Openapi District Or County Example
  slug: openapi-district-or-county-example
- key_count: 3
  name: Openapi Ec2 Capacity Example
  slug: openapi-ec2-capacity-example
- key_count: 0
  name: Openapi Family Example
  slug: openapi-family-example
- key_count: 0
  name: Openapi Fiber Optic Cable Type Example
  slug: openapi-fiber-optic-cable-type-example
- key_count: 0
  name: Openapi Get Catalog Item Input Example
  slug: openapi-get-catalog-item-input-example
- key_count: 1
  name: Openapi Get Catalog Item Output Example
  slug: openapi-get-catalog-item-output-example
- key_count: 0
  name: Openapi Get Connection Request Example
  slug: openapi-get-connection-request-example
- key_count: 2
  name: Openapi Get Connection Response Example
  slug: openapi-get-connection-response-example
- key_count: 0
  name: Openapi Get Order Input Example
  slug: openapi-get-order-input-example
- key_count: 1
  name: Openapi Get Order Output Example
  slug: openapi-get-order-output-example
- key_count: 0
  name: Openapi Get Outpost Input Example
  slug: openapi-get-outpost-input-example
- key_count: 0
  name: Openapi Get Outpost Instance Types Input Example
  slug: openapi-get-outpost-instance-types-input-example
- key_count: 4
  name: Openapi Get Outpost Instance Types Output Example
  slug: openapi-get-outpost-instance-types-output-example
- key_count: 1
  name: Openapi Get Outpost Output Example
  slug: openapi-get-outpost-output-example
- key_count: 0
  name: Openapi Get Site Address Input Example
  slug: openapi-get-site-address-input-example
- key_count: 3
  name: Openapi Get Site Address Output Example
  slug: openapi-get-site-address-output-example
- key_count: 0
  name: Openapi Get Site Input Example
  slug: openapi-get-site-input-example
- key_count: 1
  name: Openapi Get Site Output Example
  slug: openapi-get-site-output-example
- key_count: 0
  name: Openapi Host Id Example
  slug: openapi-host-id-example
- key_count: 0
  name: Openapi Instance Type Example
  slug: openapi-instance-type-example
- key_count: 1
  name: Openapi Instance Type Item Example
  slug: openapi-instance-type-item-example
- key_count: 0
  name: Openapi Internal Server Exception Example
  slug: openapi-internal-server-exception-example
- key_count: 0
  name: Openapi Iso8601 Timestamp Example
  slug: openapi-iso8601-timestamp-example
- key_count: 0
  name: Openapi Life Cycle Status Example
  slug: openapi-life-cycle-status-example
- key_count: 2
  name: Openapi Line Item Asset Information Example
  slug: openapi-line-item-asset-information-example
- key_count: 8
  name: Openapi Line Item Example
  slug: openapi-line-item-example
- key_count: 0
  name: Openapi Line Item Id Example
  slug: openapi-line-item-id-example
- key_count: 0
  name: Openapi Line Item Quantity Example
  slug: openapi-line-item-quantity-example
- key_count: 2
  name: Openapi Line Item Request Example
  slug: openapi-line-item-request-example
- key_count: 0
  name: Openapi Line Item Status Counts Example
  slug: openapi-line-item-status-counts-example
- key_count: 0
  name: Openapi Line Item Status Example
  slug: openapi-line-item-status-example
- key_count: 0
  name: Openapi List Assets Input Example
  slug: openapi-list-assets-input-example
- key_count: 2
  name: Openapi List Assets Output Example
  slug: openapi-list-assets-output-example
- key_count: 0
  name: Openapi List Catalog Items Input Example
  slug: openapi-list-catalog-items-input-example
- key_count: 2
  name: Openapi List Catalog Items Output Example
  slug: openapi-list-catalog-items-output-example
- key_count: 0
  name: Openapi List Orders Input Example
  slug: openapi-list-orders-input-example
- key_count: 2
  name: Openapi List Orders Output Example
  slug: openapi-list-orders-output-example
- key_count: 0
  name: Openapi List Outposts Input Example
  slug: openapi-list-outposts-input-example
- key_count: 2
  name: Openapi List Outposts Output Example
  slug: openapi-list-outposts-output-example
- key_count: 0
  name: Openapi List Sites Input Example
  slug: openapi-list-sites-input-example
- key_count: 2
  name: Openapi List Sites Output Example
  slug: openapi-list-sites-output-example
- key_count: 0
  name: Openapi List Tags For Resource Request Example
  slug: openapi-list-tags-for-resource-request-example
- key_count: 1
  name: Openapi List Tags For Resource Response Example
  slug: openapi-list-tags-for-resource-response-example
- key_count: 0
  name: Openapi Mac Address Example
  slug: openapi-mac-address-example
- key_count: 0
  name: Openapi Max Results1000 Example
  slug: openapi-max-results1000-example
- key_count: 0
  name: Openapi Max Size Example
  slug: openapi-max-size-example
- key_count: 0
  name: Openapi Maximum Supported Weight Lbs Example
  slug: openapi-maximum-supported-weight-lbs-example
- key_count: 0
  name: Openapi Municipality Example
  slug: openapi-municipality-example
- key_count: 0
  name: Openapi Network Interface Device Index Example
  slug: openapi-network-interface-device-index-example
- key_count: 0
  name: Openapi Not Found Exception Example
  slug: openapi-not-found-exception-example
- key_count: 0
  name: Openapi Optical Standard Example
  slug: openapi-optical-standard-example
- key_count: 9
  name: Openapi Order Example
  slug: openapi-order-example
- key_count: 0
  name: Openapi Order Id Example
  slug: openapi-order-id-example
- key_count: 0
  name: Openapi Order Status Example
  slug: openapi-order-status-example
- key_count: 7
  name: Openapi Order Summary Example
  slug: openapi-order-summary-example
- key_count: 0
  name: Openapi Order Type Example
  slug: openapi-order-type-example
- key_count: 0
  name: Openapi Outpost Arn Example
  slug: openapi-outpost-arn-example
- key_count: 0
  name: Openapi Outpost Description Example
  slug: openapi-outpost-description-example
- key_count: 12
  name: Openapi Outpost Example
  slug: openapi-outpost-example
- key_count: 0
  name: Openapi Outpost Id Example
  slug: openapi-outpost-id-example
- key_count: 0
  name: Openapi Outpost Id Only Example
  slug: openapi-outpost-id-only-example
- key_count: 0
  name: Openapi Outpost Identifier Example
  slug: openapi-outpost-identifier-example
- key_count: 0
  name: Openapi Outpost Name Example
  slug: openapi-outpost-name-example
- key_count: 0
  name: Openapi Owner Id Example
  slug: openapi-owner-id-example
- key_count: 0
  name: Openapi Payment Option Example
  slug: openapi-payment-option-example
- key_count: 0
  name: Openapi Payment Term Example
  slug: openapi-payment-term-example
- key_count: 0
  name: Openapi Postal Code Example
  slug: openapi-postal-code-example
- key_count: 0
  name: Openapi Power Connector Example
  slug: openapi-power-connector-example
- key_count: 0
  name: Openapi Power Draw Kva Example
  slug: openapi-power-draw-kva-example
- key_count: 0
  name: Openapi Power Feed Drop Example
  slug: openapi-power-feed-drop-example
- key_count: 0
  name: Openapi Power Phase Example
  slug: openapi-power-phase-example
- key_count: 0
  name: Openapi Quantity Example
  slug: openapi-quantity-example
- key_count: 0
  name: Openapi Rack Elevation Example
  slug: openapi-rack-elevation-example
- key_count: 0
  name: Openapi Rack Id Example
  slug: openapi-rack-id-example
- key_count: 9
  name: Openapi Rack Physical Properties Example
  slug: openapi-rack-physical-properties-example
- key_count: 0
  name: Openapi Server Endpoint Example
  slug: openapi-server-endpoint-example
- key_count: 0
  name: Openapi Service Quota Exceeded Exception Example
  slug: openapi-service-quota-exceeded-exception-example
- key_count: 0
  name: Openapi Shipment Carrier Example
  slug: openapi-shipment-carrier-example
- key_count: 2
  name: Openapi Shipment Information Example
  slug: openapi-shipment-information-example
- key_count: 0
  name: Openapi Site Arn Example
  slug: openapi-site-arn-example
- key_count: 0
  name: Openapi Site Description Example
  slug: openapi-site-description-example
- key_count: 11
  name: Openapi Site Example
  slug: openapi-site-example
- key_count: 0
  name: Openapi Site Id Example
  slug: openapi-site-id-example
- key_count: 0
  name: Openapi Site Name Example
  slug: openapi-site-name-example
- key_count: 0
  name: Openapi Site Notes Example
  slug: openapi-site-notes-example
- key_count: 0
  name: Openapi Sku Code Example
  slug: openapi-sku-code-example
- key_count: 4
  name: Openapi Start Connection Request Example
  slug: openapi-start-connection-request-example
- key_count: 2
  name: Openapi Start Connection Response Example
  slug: openapi-start-connection-response-example
- key_count: 0
  name: Openapi State Or Region Example
  slug: openapi-state-or-region-example
- key_count: 0
  name: Openapi Supported Hardware Type Example
  slug: openapi-supported-hardware-type-example
- key_count: 0
  name: Openapi Supported Storage Enum Example
  slug: openapi-supported-storage-enum-example
- key_count: 0
  name: Openapi Supported Uplink Gbps Example
  slug: openapi-supported-uplink-gbps-example
- key_count: 0
  name: Openapi Tag Key Example
  slug: openapi-tag-key-example
- key_count: 0
  name: Openapi Tag Map Example
  slug: openapi-tag-map-example
- key_count: 1
  name: Openapi Tag Resource Request Example
  slug: openapi-tag-resource-request-example
- key_count: 0
  name: Openapi Tag Resource Response Example
  slug: openapi-tag-resource-response-example
- key_count: 0
  name: Openapi Tag Value Example
  slug: openapi-tag-value-example
- key_count: 0
  name: Openapi Token Example
  slug: openapi-token-example
- key_count: 0
  name: Openapi Tracking Id Example
  slug: openapi-tracking-id-example
- key_count: 0
  name: Openapi Underlay Ip Address Example
  slug: openapi-underlay-ip-address-example
- key_count: 0
  name: Openapi Untag Resource Request Example
  slug: openapi-untag-resource-request-example
- key_count: 0
  name: Openapi Untag Resource Response Example
  slug: openapi-untag-resource-response-example
- key_count: 3
  name: Openapi Update Outpost Input Example
  slug: openapi-update-outpost-input-example
- key_count: 1
  name: Openapi Update Outpost Output Example
  slug: openapi-update-outpost-output-example
- key_count: 2
  name: Openapi Update Site Address Input Example
  slug: openapi-update-site-address-input-example
- key_count: 2
  name: Openapi Update Site Address Output Example
  slug: openapi-update-site-address-output-example
- key_count: 3
  name: Openapi Update Site Input Example
  slug: openapi-update-site-input-example
- key_count: 1
  name: Openapi Update Site Output Example
  slug: openapi-update-site-output-example
- key_count: 9
  name: Openapi Update Site Rack Physical Properties Input Example
  slug: openapi-update-site-rack-physical-properties-input-example
- key_count: 1
  name: Openapi Update Site Rack Physical Properties Output Example
  slug: openapi-update-site-rack-physical-properties-output-example
- key_count: 0
  name: Openapi Uplink Count Example
  slug: openapi-uplink-count-example
- key_count: 0
  name: Openapi Uplink Gbps Example
  slug: openapi-uplink-gbps-example
- key_count: 0
  name: Openapi Validation Exception Example
  slug: openapi-validation-exception-example
- key_count: 0
  name: Openapi Wire Guard Public Key Example
  slug: openapi-wire-guard-public-key-example
finops:
- name: Amazon Outposts Finops
  service_category: API
  slug: amazon-outposts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-outposts.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: openapi-access-denied-exception
- name: AccountId
  property_count: 0
  slug: openapi-account-id
- name: AddressLine1
  property_count: 0
  slug: openapi-address-line1
- name: AddressLine2
  property_count: 0
  slug: openapi-address-line2
- name: AddressLine3
  property_count: 0
  slug: openapi-address-line3
- name: Address
  property_count: 11
  slug: openapi-address
- name: AddressType
  property_count: 0
  slug: openapi-address-type
- name: Arn
  property_count: 0
  slug: openapi-arn
- name: AssetId
  property_count: 0
  slug: openapi-asset-id
- name: AssetInfo
  property_count: 5
  slug: openapi-asset-info
- name: AssetListDefinition
  property_count: 0
  slug: openapi-asset-list-definition
- name: AssetLocation
  property_count: 1
  slug: openapi-asset-location
- name: AssetState
  property_count: 0
  slug: openapi-asset-state
- name: AssetType
  property_count: 0
  slug: openapi-asset-type
- name: AvailabilityZoneIdList
  property_count: 0
  slug: openapi-availability-zone-id-list
- name: AvailabilityZoneId
  property_count: 0
  slug: openapi-availability-zone-id
- name: AvailabilityZoneList
  property_count: 0
  slug: openapi-availability-zone-list
- name: AvailabilityZone
  property_count: 0
  slug: openapi-availability-zone
- name: CancelOrderInput
  property_count: 0
  slug: openapi-cancel-order-input
- name: CancelOrderOutput
  property_count: 0
  slug: openapi-cancel-order-output
- name: CatalogItemClassList
  property_count: 0
  slug: openapi-catalog-item-class-list
- name: CatalogItemClass
  property_count: 0
  slug: openapi-catalog-item-class
- name: CatalogItemListDefinition
  property_count: 0
  slug: openapi-catalog-item-list-definition
- name: CatalogItemPowerKva
  property_count: 0
  slug: openapi-catalog-item-power-kva
- name: CatalogItem
  property_count: 7
  slug: openapi-catalog-item
- name: CatalogItemStatus
  property_count: 0
  slug: openapi-catalog-item-status
- name: CatalogItemWeightLbs
  property_count: 0
  slug: openapi-catalog-item-weight-lbs
- name: CIDRList
  property_count: 0
  slug: openapi-cidr-list
- name: CIDR
  property_count: 0
  slug: openapi-cidr
- name: CityList
  property_count: 0
  slug: openapi-city-list
- name: City
  property_count: 0
  slug: openapi-city
- name: ComputeAssetState
  property_count: 0
  slug: openapi-compute-asset-state
- name: ComputeAttributes
  property_count: 2
  slug: openapi-compute-attributes
- name: ConflictException
  property_count: 0
  slug: openapi-conflict-exception
- name: ConnectionDetails
  property_count: 6
  slug: openapi-connection-details
- name: ConnectionId
  property_count: 0
  slug: openapi-connection-id
- name: ContactName
  property_count: 0
  slug: openapi-contact-name
- name: ContactPhoneNumber
  property_count: 0
  slug: openapi-contact-phone-number
- name: CountryCodeList
  property_count: 0
  slug: openapi-country-code-list
- name: CountryCode
  property_count: 0
  slug: openapi-country-code
- name: CreateOrderInput
  property_count: 4
  slug: openapi-create-order-input
- name: CreateOrderOutput
  property_count: 1
  slug: openapi-create-order-output
- name: CreateOutpostInput
  property_count: 7
  slug: openapi-create-outpost-input
- name: CreateOutpostOutput
  property_count: 1
  slug: openapi-create-outpost-output
- name: CreateSiteInput
  property_count: 7
  slug: openapi-create-site-input
- name: CreateSiteOutput
  property_count: 1
  slug: openapi-create-site-output
- name: DeleteOutpostInput
  property_count: 0
  slug: openapi-delete-outpost-input
- name: DeleteOutpostOutput
  property_count: 0
  slug: openapi-delete-outpost-output
- name: DeleteSiteInput
  property_count: 0
  slug: openapi-delete-site-input
- name: DeleteSiteOutput
  property_count: 0
  slug: openapi-delete-site-output
- name: DeviceSerialNumber
  property_count: 0
  slug: openapi-device-serial-number
- name: DistrictOrCounty
  property_count: 0
  slug: openapi-district-or-county
- name: EC2CapacityListDefinition
  property_count: 0
  slug: openapi-ec2-capacity-list-definition
- name: EC2Capacity
  property_count: 3
  slug: openapi-ec2-capacity
- name: EC2FamilyList
  property_count: 0
  slug: openapi-ec2-family-list
- name: Family
  property_count: 0
  slug: openapi-family
- name: FiberOpticCableType
  property_count: 0
  slug: openapi-fiber-optic-cable-type
- name: GetCatalogItemInput
  property_count: 0
  slug: openapi-get-catalog-item-input
- name: GetCatalogItemOutput
  property_count: 1
  slug: openapi-get-catalog-item-output
- name: GetConnectionRequest
  property_count: 0
  slug: openapi-get-connection-request
- name: GetConnectionResponse
  property_count: 2
  slug: openapi-get-connection-response
- name: GetOrderInput
  property_count: 0
  slug: openapi-get-order-input
- name: GetOrderOutput
  property_count: 1
  slug: openapi-get-order-output
- name: GetOutpostInput
  property_count: 0
  slug: openapi-get-outpost-input
- name: GetOutpostInstanceTypesInput
  property_count: 0
  slug: openapi-get-outpost-instance-types-input
- name: GetOutpostInstanceTypesOutput
  property_count: 4
  slug: openapi-get-outpost-instance-types-output
- name: GetOutpostOutput
  property_count: 1
  slug: openapi-get-outpost-output
- name: GetSiteAddressInput
  property_count: 0
  slug: openapi-get-site-address-input
- name: GetSiteAddressOutput
  property_count: 3
  slug: openapi-get-site-address-output
- name: GetSiteInput
  property_count: 0
  slug: openapi-get-site-input
- name: GetSiteOutput
  property_count: 1
  slug: openapi-get-site-output
- name: HostIdList
  property_count: 0
  slug: openapi-host-id-list
- name: HostId
  property_count: 0
  slug: openapi-host-id
- name: InstanceTypeItem
  property_count: 1
  slug: openapi-instance-type-item
- name: InstanceTypeListDefinition
  property_count: 0
  slug: openapi-instance-type-list-definition
- name: InstanceType
  property_count: 0
  slug: openapi-instance-type
- name: InternalServerException
  property_count: 0
  slug: openapi-internal-server-exception
- name: ISO8601Timestamp
  property_count: 0
  slug: openapi-iso8601-timestamp
- name: LifeCycleStatusList
  property_count: 0
  slug: openapi-life-cycle-status-list
- name: LifeCycleStatus
  property_count: 0
  slug: openapi-life-cycle-status
- name: LineItemAssetInformationList
  property_count: 0
  slug: openapi-line-item-asset-information-list
- name: LineItemAssetInformation
  property_count: 2
  slug: openapi-line-item-asset-information
- name: LineItemId
  property_count: 0
  slug: openapi-line-item-id
- name: LineItemListDefinition
  property_count: 0
  slug: openapi-line-item-list-definition
- name: LineItemQuantity
  property_count: 0
  slug: openapi-line-item-quantity
- name: LineItemRequestListDefinition
  property_count: 0
  slug: openapi-line-item-request-list-definition
- name: LineItemRequest
  property_count: 2
  slug: openapi-line-item-request
- name: LineItem
  property_count: 8
  slug: openapi-line-item
- name: LineItemStatusCounts
  property_count: 0
  slug: openapi-line-item-status-counts
- name: LineItemStatus
  property_count: 0
  slug: openapi-line-item-status
- name: ListAssetsInput
  property_count: 0
  slug: openapi-list-assets-input
- name: ListAssetsOutput
  property_count: 2
  slug: openapi-list-assets-output
- name: ListCatalogItemsInput
  property_count: 0
  slug: openapi-list-catalog-items-input
- name: ListCatalogItemsOutput
  property_count: 2
  slug: openapi-list-catalog-items-output
- name: ListOrdersInput
  property_count: 0
  slug: openapi-list-orders-input
- name: ListOrdersOutput
  property_count: 2
  slug: openapi-list-orders-output
- name: ListOutpostsInput
  property_count: 0
  slug: openapi-list-outposts-input
- name: ListOutpostsOutput
  property_count: 2
  slug: openapi-list-outposts-output
- name: ListSitesInput
  property_count: 0
  slug: openapi-list-sites-input
- name: ListSitesOutput
  property_count: 2
  slug: openapi-list-sites-output
- name: ListTagsForResourceRequest
  property_count: 0
  slug: openapi-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: openapi-list-tags-for-resource-response
- name: MacAddressList
  property_count: 0
  slug: openapi-mac-address-list
- name: MacAddress
  property_count: 0
  slug: openapi-mac-address
- name: MaxResults1000
  property_count: 0
  slug: openapi-max-results1000
- name: MaxSize
  property_count: 0
  slug: openapi-max-size
- name: MaximumSupportedWeightLbs
  property_count: 0
  slug: openapi-maximum-supported-weight-lbs
- name: Municipality
  property_count: 0
  slug: openapi-municipality
- name: NetworkInterfaceDeviceIndex
  property_count: 0
  slug: openapi-network-interface-device-index
- name: NotFoundException
  property_count: 0
  slug: openapi-not-found-exception
- name: OpticalStandard
  property_count: 0
  slug: openapi-optical-standard
- name: OrderId
  property_count: 0
  slug: openapi-order-id
- name: Order
  property_count: 9
  slug: openapi-order
- name: OrderStatus
  property_count: 0
  slug: openapi-order-status
- name: OrderSummaryListDefinition
  property_count: 0
  slug: openapi-order-summary-list-definition
- name: OrderSummary
  property_count: 7
  slug: openapi-order-summary
- name: OrderType
  property_count: 0
  slug: openapi-order-type
- name: OutpostArn
  property_count: 0
  slug: openapi-outpost-arn
- name: OutpostDescription
  property_count: 0
  slug: openapi-outpost-description
- name: OutpostIdOnly
  property_count: 0
  slug: openapi-outpost-id-only
- name: OutpostId
  property_count: 0
  slug: openapi-outpost-id
- name: OutpostIdentifier
  property_count: 0
  slug: openapi-outpost-identifier
- name: outpostListDefinition
  property_count: 0
  slug: openapi-outpost-list-definition
- name: OutpostName
  property_count: 0
  slug: openapi-outpost-name
- name: Outpost
  property_count: 12
  slug: openapi-outpost
- name: OwnerId
  property_count: 0
  slug: openapi-owner-id
- name: PaymentOption
  property_count: 0
  slug: openapi-payment-option
- name: PaymentTerm
  property_count: 0
  slug: openapi-payment-term
- name: PostalCode
  property_count: 0
  slug: openapi-postal-code
- name: PowerConnector
  property_count: 0
  slug: openapi-power-connector
- name: PowerDrawKva
  property_count: 0
  slug: openapi-power-draw-kva
- name: PowerFeedDrop
  property_count: 0
  slug: openapi-power-feed-drop
- name: PowerPhase
  property_count: 0
  slug: openapi-power-phase
- name: Quantity
  property_count: 0
  slug: openapi-quantity
- name: RackElevation
  property_count: 0
  slug: openapi-rack-elevation
- name: RackId
  property_count: 0
  slug: openapi-rack-id
- name: RackPhysicalProperties
  property_count: 9
  slug: openapi-rack-physical-properties
- name: ServerEndpoint
  property_count: 0
  slug: openapi-server-endpoint
- name: ServiceQuotaExceededException
  property_count: 0
  slug: openapi-service-quota-exceeded-exception
- name: ShipmentCarrier
  property_count: 0
  slug: openapi-shipment-carrier
- name: ShipmentInformation
  property_count: 2
  slug: openapi-shipment-information
- name: SiteArn
  property_count: 0
  slug: openapi-site-arn
- name: SiteDescription
  property_count: 0
  slug: openapi-site-description
- name: SiteId
  property_count: 0
  slug: openapi-site-id
- name: siteListDefinition
  property_count: 0
  slug: openapi-site-list-definition
- name: SiteName
  property_count: 0
  slug: openapi-site-name
- name: SiteNotes
  property_count: 0
  slug: openapi-site-notes
- name: Site
  property_count: 11
  slug: openapi-site
- name: SkuCode
  property_count: 0
  slug: openapi-sku-code
- name: StartConnectionRequest
  property_count: 4
  slug: openapi-start-connection-request
- name: StartConnectionResponse
  property_count: 2
  slug: openapi-start-connection-response
- name: StateOrRegionList
  property_count: 0
  slug: openapi-state-or-region-list
- name: StateOrRegion
  property_count: 0
  slug: openapi-state-or-region
- name: StatusList
  property_count: 0
  slug: openapi-status-list
- name: SupportedHardwareType
  property_count: 0
  slug: openapi-supported-hardware-type
- name: SupportedStorageEnum
  property_count: 0
  slug: openapi-supported-storage-enum
- name: SupportedStorageList
  property_count: 0
  slug: openapi-supported-storage-list
- name: SupportedUplinkGbpsListDefinition
  property_count: 0
  slug: openapi-supported-uplink-gbps-list-definition
- name: SupportedUplinkGbps
  property_count: 0
  slug: openapi-supported-uplink-gbps
- name: TagKeyList
  property_count: 0
  slug: openapi-tag-key-list
- name: TagKey
  property_count: 0
  slug: openapi-tag-key
- name: TagMap
  property_count: 0
  slug: openapi-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: openapi-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: openapi-tag-resource-response
- name: TagValue
  property_count: 0
  slug: openapi-tag-value
- name: Token
  property_count: 0
  slug: openapi-token
- name: TrackingId
  property_count: 0
  slug: openapi-tracking-id
- name: UnderlayIpAddress
  property_count: 0
  slug: openapi-underlay-ip-address
- name: UntagResourceRequest
  property_count: 0
  slug: openapi-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: openapi-untag-resource-response
- name: UpdateOutpostInput
  property_count: 3
  slug: openapi-update-outpost-input
- name: UpdateOutpostOutput
  property_count: 1
  slug: openapi-update-outpost-output
- name: UpdateSiteAddressInput
  property_count: 2
  slug: openapi-update-site-address-input
- name: UpdateSiteAddressOutput
  property_count: 2
  slug: openapi-update-site-address-output
- name: UpdateSiteInput
  property_count: 3
  slug: openapi-update-site-input
- name: UpdateSiteOutput
  property_count: 1
  slug: openapi-update-site-output
- name: UpdateSiteRackPhysicalPropertiesInput
  property_count: 9
  slug: openapi-update-site-rack-physical-properties-input
- name: UpdateSiteRackPhysicalPropertiesOutput
  property_count: 1
  slug: openapi-update-site-rack-physical-properties-output
- name: UplinkCount
  property_count: 0
  slug: openapi-uplink-count
- name: UplinkGbps
  property_count: 0
  slug: openapi-uplink-gbps
- name: ValidationException
  property_count: 0
  slug: openapi-validation-exception
- name: WireGuardPublicKey
  property_count: 0
  slug: openapi-wire-guard-public-key
json_structures:
- name: Openapi Access Denied Exception Structure
  property_count: 0
  slug: openapi-access-denied-exception-structure
- name: Openapi Account Id Structure
  property_count: 0
  slug: openapi-account-id-structure
- name: Openapi Address Line1 Structure
  property_count: 0
  slug: openapi-address-line1-structure
- name: Openapi Address Line2 Structure
  property_count: 0
  slug: openapi-address-line2-structure
- name: Openapi Address Line3 Structure
  property_count: 0
  slug: openapi-address-line3-structure
- name: Openapi Address Structure
  property_count: 11
  slug: openapi-address-structure
- name: Openapi Address Type Structure
  property_count: 0
  slug: openapi-address-type-structure
- name: Openapi Arn Structure
  property_count: 0
  slug: openapi-arn-structure
- name: Openapi Asset Id Structure
  property_count: 0
  slug: openapi-asset-id-structure
- name: Openapi Asset Info Structure
  property_count: 5
  slug: openapi-asset-info-structure
- name: Openapi Asset List Definition Structure
  property_count: 0
  slug: openapi-asset-list-definition-structure
- name: Openapi Asset Location Structure
  property_count: 1
  slug: openapi-asset-location-structure
- name: Openapi Asset State Structure
  property_count: 0
  slug: openapi-asset-state-structure
- name: Openapi Asset Type Structure
  property_count: 0
  slug: openapi-asset-type-structure
- name: Openapi Availability Zone Id List Structure
  property_count: 0
  slug: openapi-availability-zone-id-list-structure
- name: Openapi Availability Zone Id Structure
  property_count: 0
  slug: openapi-availability-zone-id-structure
- name: Openapi Availability Zone List Structure
  property_count: 0
  slug: openapi-availability-zone-list-structure
- name: Openapi Availability Zone Structure
  property_count: 0
  slug: openapi-availability-zone-structure
- name: Openapi Cancel Order Input Structure
  property_count: 0
  slug: openapi-cancel-order-input-structure
- name: Openapi Cancel Order Output Structure
  property_count: 0
  slug: openapi-cancel-order-output-structure
- name: Openapi Catalog Item Class List Structure
  property_count: 0
  slug: openapi-catalog-item-class-list-structure
- name: Openapi Catalog Item Class Structure
  property_count: 0
  slug: openapi-catalog-item-class-structure
- name: Openapi Catalog Item List Definition Structure
  property_count: 0
  slug: openapi-catalog-item-list-definition-structure
- name: Openapi Catalog Item Power Kva Structure
  property_count: 0
  slug: openapi-catalog-item-power-kva-structure
- name: Openapi Catalog Item Status Structure
  property_count: 0
  slug: openapi-catalog-item-status-structure
- name: Openapi Catalog Item Structure
  property_count: 7
  slug: openapi-catalog-item-structure
- name: Openapi Catalog Item Weight Lbs Structure
  property_count: 0
  slug: openapi-catalog-item-weight-lbs-structure
- name: Openapi Cidr List Structure
  property_count: 0
  slug: openapi-cidr-list-structure
- name: Openapi Cidr Structure
  property_count: 0
  slug: openapi-cidr-structure
- name: Openapi City List Structure
  property_count: 0
  slug: openapi-city-list-structure
- name: Openapi City Structure
  property_count: 0
  slug: openapi-city-structure
- name: Openapi Compute Asset State Structure
  property_count: 0
  slug: openapi-compute-asset-state-structure
- name: Openapi Compute Attributes Structure
  property_count: 2
  slug: openapi-compute-attributes-structure
- name: Openapi Conflict Exception Structure
  property_count: 0
  slug: openapi-conflict-exception-structure
- name: Openapi Connection Details Structure
  property_count: 6
  slug: openapi-connection-details-structure
- name: Openapi Connection Id Structure
  property_count: 0
  slug: openapi-connection-id-structure
- name: Openapi Contact Name Structure
  property_count: 0
  slug: openapi-contact-name-structure
- name: Openapi Contact Phone Number Structure
  property_count: 0
  slug: openapi-contact-phone-number-structure
- name: Openapi Country Code List Structure
  property_count: 0
  slug: openapi-country-code-list-structure
- name: Openapi Country Code Structure
  property_count: 0
  slug: openapi-country-code-structure
- name: Openapi Create Order Input Structure
  property_count: 4
  slug: openapi-create-order-input-structure
- name: Openapi Create Order Output Structure
  property_count: 1
  slug: openapi-create-order-output-structure
- name: Openapi Create Outpost Input Structure
  property_count: 7
  slug: openapi-create-outpost-input-structure
- name: Openapi Create Outpost Output Structure
  property_count: 1
  slug: openapi-create-outpost-output-structure
- name: Openapi Create Site Input Structure
  property_count: 7
  slug: openapi-create-site-input-structure
- name: Openapi Create Site Output Structure
  property_count: 1
  slug: openapi-create-site-output-structure
- name: Openapi Delete Outpost Input Structure
  property_count: 0
  slug: openapi-delete-outpost-input-structure
- name: Openapi Delete Outpost Output Structure
  property_count: 0
  slug: openapi-delete-outpost-output-structure
- name: Openapi Delete Site Input Structure
  property_count: 0
  slug: openapi-delete-site-input-structure
- name: Openapi Delete Site Output Structure
  property_count: 0
  slug: openapi-delete-site-output-structure
- name: Openapi Device Serial Number Structure
  property_count: 0
  slug: openapi-device-serial-number-structure
- name: Openapi District Or County Structure
  property_count: 0
  slug: openapi-district-or-county-structure
- name: Openapi Ec2 Capacity List Definition Structure
  property_count: 0
  slug: openapi-ec2-capacity-list-definition-structure
- name: Openapi Ec2 Capacity Structure
  property_count: 3
  slug: openapi-ec2-capacity-structure
- name: Openapi Ec2 Family List Structure
  property_count: 0
  slug: openapi-ec2-family-list-structure
- name: Openapi Family Structure
  property_count: 0
  slug: openapi-family-structure
- name: Openapi Fiber Optic Cable Type Structure
  property_count: 0
  slug: openapi-fiber-optic-cable-type-structure
- name: Openapi Get Catalog Item Input Structure
  property_count: 0
  slug: openapi-get-catalog-item-input-structure
- name: Openapi Get Catalog Item Output Structure
  property_count: 1
  slug: openapi-get-catalog-item-output-structure
- name: Openapi Get Connection Request Structure
  property_count: 0
  slug: openapi-get-connection-request-structure
- name: Openapi Get Connection Response Structure
  property_count: 2
  slug: openapi-get-connection-response-structure
- name: Openapi Get Order Input Structure
  property_count: 0
  slug: openapi-get-order-input-structure
- name: Openapi Get Order Output Structure
  property_count: 1
  slug: openapi-get-order-output-structure
- name: Openapi Get Outpost Input Structure
  property_count: 0
  slug: openapi-get-outpost-input-structure
- name: Openapi Get Outpost Instance Types Input Structure
  property_count: 0
  slug: openapi-get-outpost-instance-types-input-structure
- name: Openapi Get Outpost Instance Types Output Structure
  property_count: 4
  slug: openapi-get-outpost-instance-types-output-structure
- name: Openapi Get Outpost Output Structure
  property_count: 1
  slug: openapi-get-outpost-output-structure
- name: Openapi Get Site Address Input Structure
  property_count: 0
  slug: openapi-get-site-address-input-structure
- name: Openapi Get Site Address Output Structure
  property_count: 3
  slug: openapi-get-site-address-output-structure
- name: Openapi Get Site Input Structure
  property_count: 0
  slug: openapi-get-site-input-structure
- name: Openapi Get Site Output Structure
  property_count: 1
  slug: openapi-get-site-output-structure
- name: Openapi Host Id List Structure
  property_count: 0
  slug: openapi-host-id-list-structure
- name: Openapi Host Id Structure
  property_count: 0
  slug: openapi-host-id-structure
- name: Openapi Instance Type Item Structure
  property_count: 1
  slug: openapi-instance-type-item-structure
- name: Openapi Instance Type List Definition Structure
  property_count: 0
  slug: openapi-instance-type-list-definition-structure
- name: Openapi Instance Type Structure
  property_count: 0
  slug: openapi-instance-type-structure
- name: Openapi Internal Server Exception Structure
  property_count: 0
  slug: openapi-internal-server-exception-structure
- name: Openapi Iso8601 Timestamp Structure
  property_count: 0
  slug: openapi-iso8601-timestamp-structure
- name: Openapi Life Cycle Status List Structure
  property_count: 0
  slug: openapi-life-cycle-status-list-structure
- name: Openapi Life Cycle Status Structure
  property_count: 0
  slug: openapi-life-cycle-status-structure
- name: Openapi Line Item Asset Information List Structure
  property_count: 0
  slug: openapi-line-item-asset-information-list-structure
- name: Openapi Line Item Asset Information Structure
  property_count: 2
  slug: openapi-line-item-asset-information-structure
- name: Openapi Line Item Id Structure
  property_count: 0
  slug: openapi-line-item-id-structure
- name: Openapi Line Item List Definition Structure
  property_count: 0
  slug: openapi-line-item-list-definition-structure
- name: Openapi Line Item Quantity Structure
  property_count: 0
  slug: openapi-line-item-quantity-structure
- name: Openapi Line Item Request List Definition Structure
  property_count: 0
  slug: openapi-line-item-request-list-definition-structure
- name: Openapi Line Item Request Structure
  property_count: 2
  slug: openapi-line-item-request-structure
- name: Openapi Line Item Status Counts Structure
  property_count: 0
  slug: openapi-line-item-status-counts-structure
- name: Openapi Line Item Status Structure
  property_count: 0
  slug: openapi-line-item-status-structure
- name: Openapi Line Item Structure
  property_count: 8
  slug: openapi-line-item-structure
- name: Openapi List Assets Input Structure
  property_count: 0
  slug: openapi-list-assets-input-structure
- name: Openapi List Assets Output Structure
  property_count: 2
  slug: openapi-list-assets-output-structure
- name: Openapi List Catalog Items Input Structure
  property_count: 0
  slug: openapi-list-catalog-items-input-structure
- name: Openapi List Catalog Items Output Structure
  property_count: 2
  slug: openapi-list-catalog-items-output-structure
- name: Openapi List Orders Input Structure
  property_count: 0
  slug: openapi-list-orders-input-structure
- name: Openapi List Orders Output Structure
  property_count: 2
  slug: openapi-list-orders-output-structure
- name: Openapi List Outposts Input Structure
  property_count: 0
  slug: openapi-list-outposts-input-structure
- name: Openapi List Outposts Output Structure
  property_count: 2
  slug: openapi-list-outposts-output-structure
- name: Openapi List Sites Input Structure
  property_count: 0
  slug: openapi-list-sites-input-structure
- name: Openapi List Sites Output Structure
  property_count: 2
  slug: openapi-list-sites-output-structure
- name: Openapi List Tags For Resource Request Structure
  property_count: 0
  slug: openapi-list-tags-for-resource-request-structure
- name: Openapi List Tags For Resource Response Structure
  property_count: 1
  slug: openapi-list-tags-for-resource-response-structure
- name: Openapi Mac Address List Structure
  property_count: 0
  slug: openapi-mac-address-list-structure
- name: Openapi Mac Address Structure
  property_count: 0
  slug: openapi-mac-address-structure
- name: Openapi Max Results1000 Structure
  property_count: 0
  slug: openapi-max-results1000-structure
- name: Openapi Max Size Structure
  property_count: 0
  slug: openapi-max-size-structure
- name: Openapi Maximum Supported Weight Lbs Structure
  property_count: 0
  slug: openapi-maximum-supported-weight-lbs-structure
- name: Openapi Municipality Structure
  property_count: 0
  slug: openapi-municipality-structure
- name: Openapi Network Interface Device Index Structure
  property_count: 0
  slug: openapi-network-interface-device-index-structure
- name: Openapi Not Found Exception Structure
  property_count: 0
  slug: openapi-not-found-exception-structure
- name: Openapi Optical Standard Structure
  property_count: 0
  slug: openapi-optical-standard-structure
- name: Openapi Order Id Structure
  property_count: 0
  slug: openapi-order-id-structure
- name: Openapi Order Status Structure
  property_count: 0
  slug: openapi-order-status-structure
- name: Openapi Order Structure
  property_count: 9
  slug: openapi-order-structure
- name: Openapi Order Summary List Definition Structure
  property_count: 0
  slug: openapi-order-summary-list-definition-structure
- name: Openapi Order Summary Structure
  property_count: 7
  slug: openapi-order-summary-structure
- name: Openapi Order Type Structure
  property_count: 0
  slug: openapi-order-type-structure
- name: Openapi Outpost Arn Structure
  property_count: 0
  slug: openapi-outpost-arn-structure
- name: Openapi Outpost Description Structure
  property_count: 0
  slug: openapi-outpost-description-structure
- name: Openapi Outpost Id Only Structure
  property_count: 0
  slug: openapi-outpost-id-only-structure
- name: Openapi Outpost Id Structure
  property_count: 0
  slug: openapi-outpost-id-structure
- name: Openapi Outpost Identifier Structure
  property_count: 0
  slug: openapi-outpost-identifier-structure
- name: Openapi Outpost List Definition Structure
  property_count: 0
  slug: openapi-outpost-list-definition-structure
- name: Openapi Outpost Name Structure
  property_count: 0
  slug: openapi-outpost-name-structure
- name: Openapi Outpost Structure
  property_count: 12
  slug: openapi-outpost-structure
- name: Openapi Owner Id Structure
  property_count: 0
  slug: openapi-owner-id-structure
- name: Openapi Payment Option Structure
  property_count: 0
  slug: openapi-payment-option-structure
- name: Openapi Payment Term Structure
  property_count: 0
  slug: openapi-payment-term-structure
- name: Openapi Postal Code Structure
  property_count: 0
  slug: openapi-postal-code-structure
- name: Openapi Power Connector Structure
  property_count: 0
  slug: openapi-power-connector-structure
- name: Openapi Power Draw Kva Structure
  property_count: 0
  slug: openapi-power-draw-kva-structure
- name: Openapi Power Feed Drop Structure
  property_count: 0
  slug: openapi-power-feed-drop-structure
- name: Openapi Power Phase Structure
  property_count: 0
  slug: openapi-power-phase-structure
- name: Openapi Quantity Structure
  property_count: 0
  slug: openapi-quantity-structure
- name: Openapi Rack Elevation Structure
  property_count: 0
  slug: openapi-rack-elevation-structure
- name: Openapi Rack Id Structure
  property_count: 0
  slug: openapi-rack-id-structure
- name: Openapi Rack Physical Properties Structure
  property_count: 9
  slug: openapi-rack-physical-properties-structure
- name: Openapi Server Endpoint Structure
  property_count: 0
  slug: openapi-server-endpoint-structure
- name: Openapi Service Quota Exceeded Exception Structure
  property_count: 0
  slug: openapi-service-quota-exceeded-exception-structure
- name: Openapi Shipment Carrier Structure
  property_count: 0
  slug: openapi-shipment-carrier-structure
- name: Openapi Shipment Information Structure
  property_count: 2
  slug: openapi-shipment-information-structure
- name: Openapi Site Arn Structure
  property_count: 0
  slug: openapi-site-arn-structure
- name: Openapi Site Description Structure
  property_count: 0
  slug: openapi-site-description-structure
- name: Openapi Site Id Structure
  property_count: 0
  slug: openapi-site-id-structure
- name: Openapi Site List Definition Structure
  property_count: 0
  slug: openapi-site-list-definition-structure
- name: Openapi Site Name Structure
  property_count: 0
  slug: openapi-site-name-structure
- name: Openapi Site Notes Structure
  property_count: 0
  slug: openapi-site-notes-structure
- name: Openapi Site Structure
  property_count: 11
  slug: openapi-site-structure
- name: Openapi Sku Code Structure
  property_count: 0
  slug: openapi-sku-code-structure
- name: Openapi Start Connection Request Structure
  property_count: 4
  slug: openapi-start-connection-request-structure
- name: Openapi Start Connection Response Structure
  property_count: 2
  slug: openapi-start-connection-response-structure
- name: Openapi State Or Region List Structure
  property_count: 0
  slug: openapi-state-or-region-list-structure
- name: Openapi State Or Region Structure
  property_count: 0
  slug: openapi-state-or-region-structure
- name: Openapi Status List Structure
  property_count: 0
  slug: openapi-status-list-structure
- name: Openapi Supported Hardware Type Structure
  property_count: 0
  slug: openapi-supported-hardware-type-structure
- name: Openapi Supported Storage Enum Structure
  property_count: 0
  slug: openapi-supported-storage-enum-structure
- name: Openapi Supported Storage List Structure
  property_count: 0
  slug: openapi-supported-storage-list-structure
- name: Openapi Supported Uplink Gbps List Definition Structure
  property_count: 0
  slug: openapi-supported-uplink-gbps-list-definition-structure
- name: Openapi Supported Uplink Gbps Structure
  property_count: 0
  slug: openapi-supported-uplink-gbps-structure
- name: Openapi Tag Key List Structure
  property_count: 0
  slug: openapi-tag-key-list-structure
- name: Openapi Tag Key Structure
  property_count: 0
  slug: openapi-tag-key-structure
- name: Openapi Tag Map Structure
  property_count: 0
  slug: openapi-tag-map-structure
- name: Openapi Tag Resource Request Structure
  property_count: 1
  slug: openapi-tag-resource-request-structure
- name: Openapi Tag Resource Response Structure
  property_count: 0
  slug: openapi-tag-resource-response-structure
- name: Openapi Tag Value Structure
  property_count: 0
  slug: openapi-tag-value-structure
- name: Openapi Token Structure
  property_count: 0
  slug: openapi-token-structure
- name: Openapi Tracking Id Structure
  property_count: 0
  slug: openapi-tracking-id-structure
- name: Openapi Underlay Ip Address Structure
  property_count: 0
  slug: openapi-underlay-ip-address-structure
- name: Openapi Untag Resource Request Structure
  property_count: 0
  slug: openapi-untag-resource-request-structure
- name: Openapi Untag Resource Response Structure
  property_count: 0
  slug: openapi-untag-resource-response-structure
- name: Openapi Update Outpost Input Structure
  property_count: 3
  slug: openapi-update-outpost-input-structure
- name: Openapi Update Outpost Output Structure
  property_count: 1
  slug: openapi-update-outpost-output-structure
- name: Openapi Update Site Address Input Structure
  property_count: 2
  slug: openapi-update-site-address-input-structure
- name: Openapi Update Site Address Output Structure
  property_count: 2
  slug: openapi-update-site-address-output-structure
- name: Openapi Update Site Input Structure
  property_count: 3
  slug: openapi-update-site-input-structure
- name: Openapi Update Site Output Structure
  property_count: 1
  slug: openapi-update-site-output-structure
- name: Openapi Update Site Rack Physical Properties Input Structure
  property_count: 9
  slug: openapi-update-site-rack-physical-properties-input-structure
- name: Openapi Update Site Rack Physical Properties Output Structure
  property_count: 1
  slug: openapi-update-site-rack-physical-properties-output-structure
- name: Openapi Uplink Count Structure
  property_count: 0
  slug: openapi-uplink-count-structure
- name: Openapi Uplink Gbps Structure
  property_count: 0
  slug: openapi-uplink-gbps-structure
- name: Openapi Validation Exception Structure
  property_count: 0
  slug: openapi-validation-exception-structure
- name: Openapi Wire Guard Public Key Structure
  property_count: 0
  slug: openapi-wire-guard-public-key-structure
jsonld:
- class_count: 118
  name: Amazon Outposts Openapi Context
  property_count: 101
  slug: amazon-outposts-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon Outposts
nav: Providers
network: true
overview: 'Amazon Outposts publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Connections API, List Orders API, and 4 more. Tagged areas include Edge Computing, Hybrid Cloud, Infrastructure, and On-Premises.


  The Amazon Outposts catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Outposts'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 20 more developer resources.'
plans:
- name: Amazon Outposts Plans Pricing
  plan_count: 3
  slug: amazon-outposts-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Amazon Outposts Rate Limits
  slug: amazon-outposts-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Outposts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-outposts-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon Outposts API Rules
  rule_count: 26
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 15
  slug: amazon-outposts-spectral-rules
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 70.9
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-outposts/refs/heads/main/screenshots/amazon-outposts-2026-06-20T171754.png
security:
- kind: authentication
  name: Amazon Outposts Authentication
  slug: amazon-outposts-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Outposts Domain Security
  slug: amazon-outposts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Outposts Vulnerability Disclosure
  slug: amazon-outposts-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Outposts Trust Center
  slug: amazon-outposts-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-outposts
tags:
- Edge Computing
- Hybrid Cloud
- Infrastructure
- On-Premises
website: https://aws.amazon.com/outposts/
---
