---
access_model:
  confidence: medium
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 164
  human_in_the_loop: 4
  name: Ordoro Agentic Access
  operation_count: 243
  slug: ordoro-agentic-access
  summary_line: 243 operations · 164 acting · 4 human-in-the-loop
api_count: 27
apis:
- description: Address objects are used and referenced in Orders shipping and billing addresses, Warehouses, and Suppliers.
  name: Ordoro Address API
  slug: ordoro-address-api
- description: The Api Key API from Ordoro — 2 operation(s) for api key.
  name: Ordoro Api Key API
  slug: ordoro-api-key-api
- description: The Authenticated API from Ordoro — 1 operation(s) for authenticated.
  name: Ordoro Authenticated API
  slug: ordoro-authenticated-api
- description: Current routes for `/cart/` are sometimes interchangeably referenced as `sales_channel`
  name: Ordoro Cart API
  slug: ordoro-cart-api
- description: The Company API from Ordoro — 5 operation(s) for company.
  name: Ordoro Company API
  slug: ordoro-company-api
- description: 'Goods Receipts are used for receiving items on a Purchase Order. You may have multiple Goods Receipts per Purchase Order and can have multiple lines and quantities of products related to the Purchase '
  name: Ordoro Goods Receipt API
  slug: ordoro-goods-receipt-api
- description: Currently Ordoro offers one type of integration to QuickBooks Online. Orders can be exported from Ordoro to QuickBooks using the integration.
  name: Ordoro Integration API
  slug: ordoro-integration-api
- description: Labels can be retrieved in a raw image format using the Label endpoints. For order specific labels refer to the Orders section.
  name: Ordoro Label API
  slug: ordoro-label-api
- description: Manufacturing Orders are used for creating and tracking Bill of Material orders. A Manufacturing Order is assigned to a warehouse and may have multiple lines and tags.
  name: Ordoro Manufacturing Order API
  slug: ordoro-manufacturing-order-api
- description: Orders are the main level of management in Ordoro. Orders have lines, warehouse associations and can be dropshipped or have labels created for them.
  name: Ordoro Order API
  slug: ordoro-order-api
- description: A company or account may have multple packing list formats to be saved, retrieved and used for printing Order information.
  name: Ordoro Packing List API
  slug: ordoro-packing-list-api
- description: Methods for retrieving postage account information to be used with USPS carriers.
  name: Ordoro Postage Account API
  slug: ordoro-postage-account-api
- description: The Product API from Ordoro — 21 operation(s) for product.
  name: Ordoro Product API
  slug: ordoro-product-api
- description: The Purchase Order API from Ordoro — 12 operation(s) for purchase order.
  name: Ordoro Purchase Order API
  slug: ordoro-purchase-order-api
- description: Rates are cost estimates or quotes provided by a shipping carrier or shipper. These can be retrieved per Order based on the order's package and address details.
  name: Ordoro Rate API
  slug: ordoro-rate-api
- description: The Return Label API from Ordoro — 3 operation(s) for return label.
  name: Ordoro Return Label API
  slug: ordoro-return-label-api
- description: The Return Order API from Ordoro — 3 operation(s) for return order.
  name: Ordoro Return Order API
  slug: ordoro-return-order-api
- description: The Return Order Label API from Ordoro — 8 operation(s) for return order label.
  name: Ordoro Return Order Label API
  slug: ordoro-return-order-label-api
- description: The Return Order Rate API from Ordoro — 7 operation(s) for return order rate.
  name: Ordoro Return Order Rate API
  slug: ordoro-return-order-rate-api
- description: The Return Tracking API from Ordoro — 2 operation(s) for return tracking.
  name: Ordoro Return Tracking API
  slug: ordoro-return-tracking-api
- description: The Rule API from Ordoro — 3 operation(s) for rule.
  name: Ordoro Rule API
  slug: ordoro-rule-api
- description: A shipper or carrier account can be created and used to get quotes and generate labels for orders.
  name: Ordoro Shipper API
  slug: ordoro-shipper-api
- description: The Supplier API from Ordoro — 5 operation(s) for supplier.
  name: Ordoro Supplier API
  slug: ordoro-supplier-api
- description: The Tag API from Ordoro — 3 operation(s) for tag.
  name: Ordoro Tag API
  slug: ordoro-tag-api
- description: The Tracking API from Ordoro — 2 operation(s) for tracking.
  name: Ordoro Tracking API
  slug: ordoro-tracking-api
- description: The User API from Ordoro — 3 operation(s) for user.
  name: Ordoro User API
  slug: ordoro-user-api
- description: The Warehouse API from Ordoro — 3 operation(s) for warehouse.
  name: Ordoro Warehouse API
  slug: ordoro-warehouse-api
artifact_total: 216
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ordoro API Documentation Address API
  slug: open-ordoro-address-api
- collection_type: open
  name: Ordoro API Documentation Address Api Key API
  slug: open-ordoro-api-key-api
- collection_type: open
  name: Ordoro API Documentation Address Authenticated API
  slug: open-ordoro-authenticated-api
- collection_type: open
  name: Ordoro API Documentation Address Cart API
  slug: open-ordoro-cart-api
- collection_type: open
  name: Ordoro API Documentation Address Company API
  slug: open-ordoro-company-api
- collection_type: open
  name: Ordoro API Documentation Address Goods Receipt API
  slug: open-ordoro-goods-receipt-api
- collection_type: open
  name: Ordoro API Documentation Address Integration API
  slug: open-ordoro-integration-api
- collection_type: open
  name: Ordoro API Documentation Address Label API
  slug: open-ordoro-label-api
- collection_type: open
  name: Ordoro API Documentation Address Manufacturing Order API
  slug: open-ordoro-manufacturing-order-api
- collection_type: open
  name: Ordoro API Documentation Address Order API
  slug: open-ordoro-order-api
- collection_type: open
  name: Ordoro API Documentation Address Packing List API
  slug: open-ordoro-packing-list-api
- collection_type: open
  name: Ordoro API Documentation Address Postage Account API
  slug: open-ordoro-postage-account-api
- collection_type: open
  name: Ordoro API Documentation Address Product API
  slug: open-ordoro-product-api
- collection_type: open
  name: Ordoro API Documentation Address Purchase Order API
  slug: open-ordoro-purchase-order-api
- collection_type: open
  name: Ordoro API Documentation Address Rate API
  slug: open-ordoro-rate-api
- collection_type: open
  name: Ordoro API Documentation Address Return Label API
  slug: open-ordoro-return-label-api
- collection_type: open
  name: Ordoro API Documentation Address Return Order API
  slug: open-ordoro-return-order-api
- collection_type: open
  name: Ordoro API Documentation Address Return Order Label API
  slug: open-ordoro-return-order-label-api
- collection_type: open
  name: Ordoro API Documentation Address Return Order Rate API
  slug: open-ordoro-return-order-rate-api
- collection_type: open
  name: Ordoro API Documentation Address Return Tracking API
  slug: open-ordoro-return-tracking-api
- collection_type: open
  name: Ordoro API Documentation Address Rule API
  slug: open-ordoro-rule-api
- collection_type: open
  name: Ordoro API Documentation Address Shipper API
  slug: open-ordoro-shipper-api
- collection_type: open
  name: Ordoro API Documentation Address Supplier API
  slug: open-ordoro-supplier-api
- collection_type: open
  name: Ordoro API Documentation Address Tag API
  slug: open-ordoro-tag-api
- collection_type: open
  name: Ordoro API Documentation Address Tracking API
  slug: open-ordoro-tracking-api
- collection_type: open
  name: Ordoro API Documentation Address User API
  slug: open-ordoro-user-api
- collection_type: open
  name: Ordoro API Documentation Address Warehouse API
  slug: open-ordoro-warehouse-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ordoro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ordoro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ordoro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ordoro.com/
- group: other
  title: ''
  type: Developer
  url: https://www.ordoro.com/developer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ordoro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ordoro-inc
- group: other
  title: ''
  type: X
  url: https://twitter.com/ordoro
- group: company
  title: ''
  type: Blog
  url: https://blog.ordoro.com/
- group: operate
  title: ''
  type: Forums
  url: https://forums.ordoro.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ordoro.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://ordoro.statuspage.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/ordoro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ordoro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ordoro-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ordoro-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ordoro-context.jsonld
created: '2026-06-12'
description: Ordoro is a multi-channel order management and ecommerce logistics platform designed for small and medium-sized businesses. It provides a REST API for syncing orders across sales channels, managing inventory in multiple warehouses, creating shipping labels from major carriers, and handling dropshipping workflows with suppliers. The API supports operations including order retrieval and creation, product and inventory management, purchase orders, manufacturing orders, and shipment tracking. API access is available on Premium-level plans and above, using Basic HTTP Authentication with API keys.
examples:
- key_count: 5
  name: Ordoro Post V3 Account Add_Funds
  slug: ordoro-post-v3-account-add_funds
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Label Australia_Post
  slug: ordoro-post-v3-order-order_number-label-australia_post
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Label Fedex
  slug: ordoro-post-v3-order-order_number-label-fedex
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Label Pitney
  slug: ordoro-post-v3-order-order_number-label-pitney
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Line
  slug: ordoro-post-v3-order-order_number-line
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Mark_As_Dropshipped
  slug: ordoro-post-v3-order-order_number-mark_as_dropshipped
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Shipping_Info
  slug: ordoro-post-v3-order-order_number-shipping_info
- key_count: 5
  name: Ordoro Post V3 Order Order_Number Split
  slug: ordoro-post-v3-order-order_number-split
- key_count: 5
  name: Ordoro Post V3 Order
  slug: ordoro-post-v3-order
- key_count: 5
  name: Ordoro Put V3 Order Order_Number Billing_Address
  slug: ordoro-put-v3-order-order_number-billing_address
- key_count: 5
  name: Ordoro Put V3 Order Order_Number Financial
  slug: ordoro-put-v3-order-order_number-financial
- key_count: 5
  name: Ordoro Put V3 Order Order_Number Line Order_Line_Id
  slug: ordoro-put-v3-order-order_number-line-order_line_id
- key_count: 5
  name: Ordoro Put V3 Order Order_Number Shipping_Address
  slug: ordoro-put-v3-order-order_number-shipping_address
- key_count: 5
  name: Ordoro Put V3 Order Order_Number Shipping_Info
  slug: ordoro-put-v3-order-order_number-shipping_info
- key_count: 5
  name: Ordoro Put V3 Order Order_Number Warehouse
  slug: ordoro-put-v3-order-order_number-warehouse
- key_count: 5
  name: Ordoro Put V3 Order Order_Number
  slug: ordoro-put-v3-order-order_number
finops:
- name: Ordoro Finops
  service_category: ''
  slug: ordoro-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Ordoro multi-channel order management and ecommerce logistics platform. Ordoro provides a REST API for syncing orders across sales channels,
  name: Ordoro GraphQL Schema
  slug: ordoro-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ordoro.png
json_schemas:
- name: Address Schema
  property_count: 15
  slug: ordoro-address
- name: Address List Schema
  property_count: 4
  slug: ordoro-address_list
- name: Address Schema
  property_count: 14
  slug: ordoro-address_lite
- name: API Key Schema
  property_count: 9
  slug: ordoro-api_key
- name: API Key List Schema
  property_count: 4
  slug: ordoro-api_key_list
- name: Account Balance Response Schema
  property_count: 6
  slug: ordoro-balance
- name: Shipper Carrier Response
  property_count: 13
  slug: ordoro-carrier
- name: Cart Schema
  property_count: 18
  slug: ordoro-cart_base
- name: cart_bigcommerce_vendor_config
  property_count: 6
  slug: ordoro-cart_bigcommerce_vendor_config
- name: cart_etsy_vendor_config
  property_count: 4
  slug: ordoro-cart_etsy_vendor_config
- name: cart_list
  property_count: 4
  slug: ordoro-cart_list
- name: cart_magento_v2_vendor_config
  property_count: 4
  slug: ordoro-cart_magento_v2_vendor_config
- name: cart_magento_vendor_config
  property_count: 5
  slug: ordoro-cart_magento_vendor_config
- name: cart_miva_vendor_config
  property_count: 4
  slug: ordoro-cart_miva_vendor_config
- name: cart_shopify_vendor_config
  property_count: 8
  slug: ordoro-cart_shopify_vendor_config
- name: cart_shopsite_vendor_config
  property_count: 7
  slug: ordoro-cart_shopsite_vendor_config
- name: cart_sps_commerce_vendor_config
  property_count: 4
  slug: ordoro-cart_sps_commerce_vendor_config
- name: cart_square_vendor_config
  property_count: 4
  slug: ordoro-cart_square_vendor_config
- name: cart_volusion_v1_vendor_config
  property_count: 3
  slug: ordoro-cart_volusion_v1_vendor_config
- name: cart_walmart_vendor_config
  property_count: 4
  slug: ordoro-cart_walmart_vendor_config
- name: cart_wayfair_vendor_config
  property_count: 4
  slug: ordoro-cart_wayfair_vendor_config
- name: cart_woocommerce_vendor_config
  property_count: 3
  slug: ordoro-cart_woocommerce_vendor_config
- name: Comment Schema
  property_count: 3
  slug: ordoro-comment
- name: Company Schema
  property_count: 28
  slug: ordoro-company
- name: Company Logo Response Schema
  property_count: 7
  slug: ordoro-company_logo
- name: Customs Line Schema
  property_count: 10
  slug: ordoro-customs_line
- name: Dropshipping Info Schema
  property_count: 8
  slug: ordoro-dropshipping_info
- name: Amazon Extra Info Schema
  property_count: 9
  slug: ordoro-extra_info_amazon
- name: Ebay Extra Info Schema
  property_count: 3
  slug: ordoro-extra_info_ebay
- name: Etsy Extra Info Schema
  property_count: 3
  slug: ordoro-extra_info_etsy
- name: GET Tag List Schema
  property_count: 3
  slug: ordoro-get_v3_tag_list
- name: Goods Receipt Schema
  property_count: 10
  slug: ordoro-goods_receipt
- name: goods_receipt_list
  property_count: 4
  slug: ordoro-goods_receipt_list
- name: Hazmat Item Schema
  property_count: 21
  slug: ordoro-hazmat_item
- name: Integration Base Schema
  property_count: 7
  slug: ordoro-integration_base
- name: Integration list schema
  property_count: 4
  slug: ordoro-integration_list
- name: integration_quickbooks_vendor_config
  property_count: 5
  slug: ordoro-integration_quickbooks_vendor_config
- name: Inventory as Warehouse Schema
  property_count: 18
  slug: ordoro-inventory_as_warehouse
- name: Manufacturing Order Schema
  property_count: 10
  slug: ordoro-manufacturing_order
- name: manufacturing_order_list
  property_count: 4
  slug: ordoro-manufacturing_order_list
- name: Order Schema
  property_count: 42
  slug: ordoro-order
- name: Get Order Counts Response Schema
  property_count: 6
  slug: ordoro-order_counts
- name: Order Financial Schema
  property_count: 6
  slug: ordoro-order_financial
- name: order_list
  property_count: 4
  slug: ordoro-order_list
- name: Packing List Schema
  property_count: 19
  slug: ordoro-packing_list
- name: packing_list_list
  property_count: 4
  slug: ordoro-packing_list_list
- name: Parent Order Schema
  property_count: 20
  slug: ordoro-parent_order
- name: Pickup Response
  property_count: 9
  slug: ordoro-pickup
- name: Amazon Label Request Schema
  property_count: 19
  slug: ordoro-post_amazon_label
- name: Amazon Rate POST Request schema
  property_count: 16
  slug: ordoro-post_amazon_rate
- name: Buy More Products Request Schema
  property_count: 5
  slug: ordoro-post_buy_more
- name: Canada Post Label Request Schema
  property_count: 21
  slug: ordoro-post_canada_post_label
- name: Canada Post POST Rate Request Schema
  property_count: 14
  slug: ordoro-post_canada_post_rate
- name: post_cart_base
  property_count: 3
  slug: ordoro-post_cart_base
- name: DHL eCommerce Label Request schema
  property_count: 21
  slug: ordoro-post_dhl_ecommerce_label
- name: DHL eCommerce Label Request schema
  property_count: 17
  slug: ordoro-post_dhl_ecommerce_rate
- name: DHL Label Request schema
  property_count: 39
  slug: ordoro-post_dhl_label
- name: DHL Rate POST Request schema
  property_count: 17
  slug: ordoro-post_dhl_rate
- name: Easypost POST Label Request Schema
  property_count: 20
  slug: ordoro-post_easypost_label
- name: Easypost POST Rate Request Schema
  property_count: 16
  slug: ordoro-post_easypost_rate
- name: Endicia Label Request
  property_count: 25
  slug: ordoro-post_endicia_label
- name: Endicia Rate POST Request Schema
  property_count: 22
  slug: ordoro-post_endicia_rate
- name: FBA Recieved Info Schema
  property_count: 6
  slug: ordoro-post_fba_received
- name: Fedex Label Request Schema
  property_count: 52
  slug: ordoro-post_fedex_label
- name: Fedex Rate POST Request Schema
  property_count: 42
  slug: ordoro-post_fedex_rate
- name: Fedex Pickup Request Schema
  property_count: 15
  slug: ordoro-post_fedex_schedule_pickup
- name: Post Goods Receipt Schema
  property_count: 3
  slug: ordoro-post_goods_receipt
- name: Create a Manufacturing Order
  property_count: 5
  slug: ordoro-post_manufacturing_order
- name: Add a Manufacturing Order Line
  property_count: 4
  slug: ordoro-post_manufacturing_order_line
- name: Order dropship request schema
  property_count: 11
  slug: ordoro-post_order_dropship
- name: POST Order Line Request Schema
  property_count: 12
  slug: ordoro-post_order_line
- name: Core API Order Schema
  property_count: 24
  slug: ordoro-post_order_v1
- name: Put Packing List Schema
  property_count: 14
  slug: ordoro-post_packing_list
- name: Pitney Label Request Schema
  property_count: 28
  slug: ordoro-post_pitney_label
- name: Pitney Rate POST Request Schema
  property_count: 19
  slug: ordoro-post_pitney_rate
- name: Product Post Schema
  property_count: 30
  slug: ordoro-post_product
- name: Buy More Products Request Schema
  property_count: 11
  slug: ordoro-post_purchase_order
- name: Create a Purchase Order Item
  property_count: 4
  slug: ordoro-post_purchase_order_item
- name: Create a Return Order
  property_count: 8
  slug: ordoro-post_return_order
- name: post_shipper_base
  property_count: 3
  slug: ordoro-post_shipper_base
- name: POST Supplier Schema
  property_count: 13
  slug: ordoro-post_supplier
- name: Add a shipping method to a mapped supplier method
  property_count: 5
  slug: ordoro-post_supplier_shipping_method
- name: UPS Label Request Schema
  property_count: 48
  slug: ordoro-post_ups_label
- name: UPS Rate POST Request Schema
  property_count: 44
  slug: ordoro-post_ups_rate
- name: UPS Pickup Request Schema
  property_count: 8
  slug: ordoro-post_ups_schedule_pickup
- name: Create User Schema
  property_count: 4
  slug: ordoro-post_user
- name: Preset Object Schema
  property_count: 8
  slug: ordoro-preset
- name: preset_list
  property_count: 4
  slug: ordoro-preset_list
- name: Product Schema
  property_count: 35
  slug: ordoro-product_base
- name: Product List Response schema
  property_count: 4
  slug: ordoro-product_list
- name: Purchase Order Schema
  property_count: 20
  slug: ordoro-purchase_order
- name: Purchase Order Counts Response Schema
  property_count: 6
  slug: ordoro-purchase_order_counts
- name: Purchase Order Item Schema
  property_count: 4
  slug: ordoro-purchase_order_item
- name: Purchase Order List Response schema
  property_count: 4
  slug: ordoro-purchase_order_list
- name: put_cart_base
  property_count: 4
  slug: ordoro-put_cart_base
- name: Address Schema
  property_count: 12
  slug: ordoro-put_company
- name: PUT Company Logo Schema
  property_count: 3
  slug: ordoro-put_company_logo
- name: Update a Manufacturing Order
  property_count: 4
  slug: ordoro-put_manufacturing_order
- name: Update a Manufacturing Order Line
  property_count: 4
  slug: ordoro-put_manufacturing_order_line
- name: Order Update Schema
  property_count: 5
  slug: ordoro-put_order
- name: Update Order Line Schema
  property_count: 6
  slug: ordoro-put_order_line
- name: Shipping Info Request Schema
  property_count: 14
  slug: ordoro-put_order_shipping_info
- name: Put Packing List Schema
  property_count: 14
  slug: ordoro-put_packing_list
- name: Product Post Schema
  property_count: 25
  slug: ordoro-put_product
- name: Update Product Cart Bridge Schema
  property_count: 8
  slug: ordoro-put_product_cart_bridge
- name: Update a Product Supplier Schema
  property_count: 4
  slug: ordoro-put_product_supplier
- name: Update a Product Warehouse Schema
  property_count: 3
  slug: ordoro-put_product_warehouse
- name: Update a Purchase Order
  property_count: 11
  slug: ordoro-put_purchase_order
- name: Update a Purchase Order Item
  property_count: 3
  slug: ordoro-put_purchase_order_item
- name: Update a shipping method mapped to a supplier method
  property_count: 5
  slug: ordoro-put_supplier_shipping_method
- name: User Update Schema
  property_count: 8
  slug: ordoro-put_user
- name: Return Order Schema
  property_count: 16
  slug: ordoro-return_order
- name: return_order_list
  property_count: 4
  slug: ordoro-return_order_list
- name: shipper_australia_post_vendor_config
  property_count: 5
  slug: ordoro-shipper_australia_post_vendor_config
- name: Shipper Base Schema
  property_count: 7
  slug: ordoro-shipper_base
- name: shipper_canada_post_vendor_config
  property_count: 5
  slug: ordoro-shipper_canada_post_vendor_config
- name: shipper_endicia_vendor_config
  property_count: 7
  slug: ordoro-shipper_endicia_vendor_config
- name: shipper_fedex_vendor_config
  property_count: 6
  slug: ordoro-shipper_fedex_vendor_config
- name: shipper_list
  property_count: 4
  slug: ordoro-shipper_list
- name: shipper_newgistics_vendor_config
  property_count: 4
  slug: ordoro-shipper_newgistics_vendor_config
- name: shipper_ups_vendor_config
  property_count: 11
  slug: ordoro-shipper_ups_vendor_config
- name: Shipping Info Schema
  property_count: 36
  slug: ordoro-shipping_info
- name: Supplier Schema
  property_count: 20
  slug: ordoro-supplier
- name: Supplier List Schema
  property_count: 4
  slug: ordoro-supplier_list
- name: Supplier shipping method map
  property_count: 9
  slug: ordoro-supplier_shipping_method_map
- name: Tag Schema
  property_count: 5
  slug: ordoro-tag
- name: Tag List Schema
  property_count: 4
  slug: ordoro-tag_list
- name: Tax Info Schema
  property_count: 3
  slug: ordoro-tax_info
- name: Update Address Schema
  property_count: 13
  slug: ordoro-update_address
- name: User Schema
  property_count: 12
  slug: ordoro-user
- name: v1_address
  property_count: 17
  slug: ordoro-v1_address
- name: Core API Order Line Product Schema
  property_count: 15
  slug: ordoro-v1_order_line_product
- name: V3 Tag Schema
  property_count: 3
  slug: ordoro-v3_tag
- name: Tag List Schema
  property_count: 4
  slug: ordoro-v3_tag_list
- name: Warehouse Schema
  property_count: 6
  slug: ordoro-warehouse
- name: Warehouse Address Schema
  property_count: 9
  slug: ordoro-warehouse_address
- name: warehouse_list
  property_count: 4
  slug: ordoro-warehouse_list
jsonld:
- class_count: 85
  name: Ordoro Context
  property_count: 0
  slug: ordoro-context
layout: provider
modified: '2026-06-12'
name: Ordoro
nav: Providers
network: true
overview: 'Ordoro publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Address API, Api Key API, Authenticated API, and 24 more. Tagged areas include Order Management, Inventory Management, Shipping, Dropshipping, and Ecommerce.


  The Ordoro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ordoro''s developer surface includes documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Ordoro Plans Pricing
  plan_count: 7
  slug: ordoro-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Ordoro Rate Limits
  slug: ordoro-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Ordoro API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ordoro-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.5
  delta: -5.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 58.4
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ordoro/refs/heads/main/screenshots/ordoro-2026-06-20T191205.png
security:
- kind: domain-security
  name: Ordoro Domain Security
  slug: ordoro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ordoro
tags:
- Order Management
- Inventory Management
- Shipping
- Dropshipping
- Ecommerce
- Multi-Channel
- Fulfillment
- Logistics
website: https://www.ordoro.com/
---
