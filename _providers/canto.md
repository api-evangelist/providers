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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Canto Agentic Access
  operation_count: 75
  slug: canto-agentic-access
  summary_line: 75 operations · 50 acting
api_count: 19
apis:
- description: Perform bulk products operation on a Product Catalog These endpoints allow you to add or remove products that are associated with a specific product catalog in bulk.
  name: Canto bulk_products_catalogs API
  slug: canto-bulk-products-catalogs-api
- description: Perform bulk products operation on a Product Channel Template These endpoints allow you to add or remove products that are associated with a specific channel template in bulk.
  name: Canto bulk_products_channel_templates API
  slug: canto-bulk-products-channel-templates-api
- description: The dimensions API from Canto — 2 operation(s) for dimensions.
  name: Canto dimensions API
  slug: canto-dimensions-api
- description: 'API endpoints for filtering product attributes. Allows filtering and retrieving product attributes based on various criteria including: - Exact value matches - Partial text matches - Multiple value ma'
  name: Canto filter API
  slug: canto-filter-api
- description: 'API endpoints for configuring how CSV imports should be processed. This includes: - Mapping CSV headers to product attributes - Configuring how product variations should be handled - Setting up catego'
  name: Canto import_settings API
  slug: canto-import-settings-api
- description: API endpoint for importing products from a CSV file. Supports multipart form data uploads with import configuration.
  name: Canto imports API
  slug: canto-imports-api
- description: The options API from Canto — 2 operation(s) for options.
  name: Canto options API
  slug: canto-options-api
- description: The product_catalog_products API from Canto — 2 operation(s) for product_catalog_products.
  name: Canto product_catalog_products API
  slug: canto-product-catalog-products-api
- description: The product_catalogs API from Canto — 2 operation(s) for product_catalogs.
  name: Canto product_catalogs API
  slug: canto-product-catalogs-api
- description: The product_categories API from Canto — 2 operation(s) for product_categories.
  name: Canto product_categories API
  slug: canto-product-categories-api
- description: Manage products associated with product channel templates.
  name: Canto product_channel_template_products API
  slug: canto-product-channel-template-products-api
- description: Product Channel Templates define the structure and configuration for importing and exporting product data into and out of Canto PIM.
  name: Canto product_channel_templates API
  slug: canto-product-channel-templates-api
- description: The product_custom_attributes API from Canto — 2 operation(s) for product_custom_attributes.
  name: Canto product_custom_attributes API
  slug: canto-product-custom-attributes-api
- description: Product Share Links allow you to create shareable links for products that can be accessed outside the PIM system. These links can have custom names and optionally expire.
  name: Canto product_share_links API
  slug: canto-product-share-links-api
- description: The product_types API from Canto — 2 operation(s) for product_types.
  name: Canto product_types API
  slug: canto-product-types-api
- description: The products API from Canto — 4 operation(s) for products.
  name: Canto products API
  slug: canto-products-api
- description: The variants API from Canto — 4 operation(s) for variants.
  name: Canto variants API
  slug: canto-variants-api
- description: The webhook_events API from Canto — 2 operation(s) for webhook_events.
  name: Canto webhook_events API
  slug: canto-webhook-events-api
- description: Webhooks are used to notify your application when certain events occur within the system. They can be configured to send a POST request to a specified URL when a specific event happens. Available reso
  name: Canto webhooks API
  slug: canto-webhooks-api
artifact_total: 51
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canto-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/canto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canto-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.canto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.canto.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/canto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canto
- group: company
  title: ''
  type: Blog
  url: https://www.canto.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.canto.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/canto-status
- group: other
  title: ''
  type: X
  url: https://x.com/canto
- group: commercial
  title: ''
  type: Plans
  url: plans/canto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/canto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/canto-finops.yml
created: '2026-06-13'
description: Canto is a digital asset management (DAM) platform offering a fully documented REST API for organizing, tagging, distributing, and sharing brand assets including images, videos, and documents across teams and channels. The API uses OAuth 2.0 for authentication and provides endpoints for asset search, metadata management, folder and album operations, automated workflows, and asset distribution.
examples:
- key_count: 1
  name: Canto Get_Api_V1_Product_Channel_Templates 200 Response
  slug: canto-get_api_v1_product_channel_templates-200-response
- key_count: 8
  name: Canto Get_Api_V1_Product_Channel_Templates_Id 200 Response
  slug: canto-get_api_v1_product_channel_templates_id-200-response
- key_count: 2
  name: Canto Get_Api_V1_Products_Product_Id_Variants 200 Response
  slug: canto-get_api_v1_products_product_id_variants-200-response
- key_count: 4
  name: Canto Get_Api_V1_Products_Product_Id_Variants_Id 200 Response
  slug: canto-get_api_v1_products_product_id_variants_id-200-response
- key_count: 4
  name: Canto Patch_Api_V1_Products_Product_Id_Variants_Id 200 Response
  slug: canto-patch_api_v1_products_product_id_variants_id-200-response
- key_count: 3
  name: Canto Post_Api_V1_Bulk_Products_Catalogs Request
  slug: canto-post_api_v1_bulk_products_catalogs-request
- key_count: 3
  name: Canto Post_Api_V1_Bulk_Products_Channel_Templates Request
  slug: canto-post_api_v1_bulk_products_channel_templates-request
- key_count: 1
  name: Canto Post_Api_V1_Product_Catalogs_Product_Catalog_Id_Products Request
  slug: canto-post_api_v1_product_catalogs_product_catalog_id_products-request
- key_count: 8
  name: Canto Post_Api_V1_Product_Channel_Templates 201 Response
  slug: canto-post_api_v1_product_channel_templates-201-response
- key_count: 3
  name: Canto Post_Api_V1_Product_Channel_Templates Request
  slug: canto-post_api_v1_product_channel_templates-request
- key_count: 4
  name: Canto Post_Api_V1_Products_Product_Id_Variants 200 Response
  slug: canto-post_api_v1_products_product_id_variants-200-response
- key_count: 8
  name: Canto Put_Api_V1_Product_Channel_Templates_Id 200 Response
  slug: canto-put_api_v1_product_channel_templates_id-200-response
- key_count: 2
  name: Canto Put_Api_V1_Product_Channel_Templates_Id Request
  slug: canto-put_api_v1_product_channel_templates_id-request
- key_count: 4
  name: Canto Put_Api_V1_Products_Product_Id_Variants_Id 200 Response
  slug: canto-put_api_v1_products_product_id_variants_id-200-response
finops:
- name: Canto Finops
  service_category: ''
  slug: canto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canto.png
json_schemas:
- name: catalog
  property_count: 9
  slug: canto-catalog
- name: category
  property_count: 3
  slug: canto-category
- name: custom_attribute_mapping
  property_count: 3
  slug: canto-custom-attribute-mapping
- name: dimension
  property_count: 3
  slug: canto-dimension
- name: product_channel_template_summary
  property_count: 7
  slug: canto-product-channel-template-summary
- name: product_channel_template
  property_count: 8
  slug: canto-product-channel-template
- name: product_channel_templates_response
  property_count: 1
  slug: canto-product-channel-templates-response
- name: product_share_link_properties
  property_count: 7
  slug: canto-product-share-link-properties
- name: webhook_properties
  property_count: 5
  slug: canto-webhook-properties
jsonld:
- class_count: 27
  name: Canto Context
  property_count: 10
  slug: canto-context
layout: provider
modified: '2026-06-13'
name: Canto
nav: Providers
network: true
overview: 'Canto publishes 19 APIs on the [APIs.io](https://apis.io/) network, including bulk_products_catalogs API, bulk_products_channel_templates API, dimensions API, and 16 more. Tagged areas include Digital Asset Management, DAM, Brand Assets, Images, and Videos.


  The Canto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Canto''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Canto Plans Pricing
  plan_count: 4
  slug: canto-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 0
  name: Canto Rate Limits
  slug: canto-rate-limits
rules:
- name: Canto API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: canto-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: -5.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 61.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/canto/refs/heads/main/screenshots/canto-2026-06-20T173928.png
security:
- kind: authentication
  name: Canto Authentication
  slug: canto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Canto Domain Security
  slug: canto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Canto Trust Center
  slug: canto-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: canto
tags:
- Digital Asset Management
- DAM
- Brand Assets
- Images
- Videos
- Documents
- Media Library
- Asset Distribution
website: https://www.canto.com/
---
