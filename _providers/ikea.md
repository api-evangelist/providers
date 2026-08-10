---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ikea Agentic Access
  operation_count: 9
  slug: ikea-agentic-access
  summary_line: 9 operations
api_count: 6
apis:
- description: The DIRIGERA hub is IKEA's next-generation smart home gateway (replacing TRADFRI). It exposes a private, locally-served REST API on the LAN with bearer-token authentication (token obtained by pressing
  name: IKEA DIRIGERA Smart Home Hub API (Unofficial, Local)
  slug: dirigera-hub
- description: Everything about Availability
  name: IKEA Availability API
  slug: ikea-availability-api
- description: Everything about Categories
  name: IKEA Categories API
  slug: ikea-categories-api
- description: Everything about Parts
  name: IKEA Parts API
  slug: ikea-parts-api
- description: Everything about Products
  name: IKEA Products API
  slug: ikea-products-api
- description: Everything about Stores
  name: IKEA Stores API
  slug: ikea-stores-api
artifact_total: 67
collections:
- collection_type: open
  name: IKEA After Purchase Ordering API
  slug: open-ikea-after-purchase-ordering
- collection_type: open
  name: IKEA Product Catalog API
  slug: open-ikea-product-catalog
- collection_type: open
  name: IKEA Sales Item API
  slug: open-ikea-sales-item
- collection_type: open
  name: IKEA Search API
  slug: open-ikea-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ikea-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ikea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ikea-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ikea-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ikea.com/global/en/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IKEA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ikea
- group: company
  title: ''
  type: Website
  url: https://www.ikea.com/
- group: other
  title: ''
  type: CorporateSite
  url: https://www.inter.ikea.com/
- group: build
  title: Python ikea_api (vrslev/ikea-api-client, archived)
  type: SDKs
  url: https://pypi.org/project/ikea_api/
- group: build
  title: Community OpenAPI Specs (idelsink/ikea-openapi)
  type: SourceCode
  url: https://github.com/idelsink/ikea-openapi
- group: build
  title: IKEA 3D Assembly Dataset
  type: SourceCode
  url: https://github.com/IKEA/IKEA3DAssemblyDataset
- group: build
  title: ikea-availability-checker (Ephigenia)
  type: CodeExamples
  url: https://github.com/Ephigenia/ikea-availability-checker
- group: build
  title: ikeaStockChecker (DavisChappins)
  type: CodeExamples
  url: https://github.com/DavisChappins/ikeaStockChecker
- group: build
  title: ikeaScraper (Mirzaei81)
  type: CodeExamples
  url: https://github.com/Mirzaei81/ikeaScraper
created: '2026-05-05'
description: A Swedish multinational furniture and home goods retailer known for its affordable, ready-to-assemble products. Operates hundreds of stores worldwide and is the world's largest furniture retailer with a distinctive showroom-based shopping experience. IKEA does not publish an official public developer API or developer portal; the surfaces profiled here are community reverse-engineered specs of the IKEA storefront (Product Catalog, Search, Sales Item availability, After Purchase Ordering / spare parts) plus the local-network API of the DIRIGERA smart home hub. All artifacts are community-built and unofficial — they may change at any time and are not affiliated with, endorsed by, or supported by IKEA.
examples:
- key_count: 8
  name: Ikea After Purchase Ordering Get Part By Id Example
  slug: ikea-after-purchase-ordering-get-part-by-id-example
- key_count: 8
  name: Ikea Product Catalog Get Product By Id Example
  slug: ikea-product-catalog-get-product-by-id-example
- key_count: 5
  name: Ikea Sales Item Get Product Availability Example
  slug: ikea-sales-item-get-product-availability-example
- key_count: 3
  name: Ikea Search Find Products Example
  slug: ikea-search-find-products-example
- key_count: 3
  name: Ikea Search Find Products Paginated Example
  slug: ikea-search-find-products-paginated-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ikea.png
json_schemas:
- name: Part
  property_count: 8
  slug: ikea-after-purchase-ordering-part
- name: ProductParts
  property_count: 5
  slug: ikea-after-purchase-ordering-product-parts
- name: SearchPart
  property_count: 9
  slug: ikea-after-purchase-ordering-search-part
- name: status
  property_count: 0
  slug: ikea-after-purchase-ordering-status
- name: Category
  property_count: 5
  slug: ikea-product-catalog-category
- name: ProductDetails
  property_count: 15
  slug: ikea-product-catalog-product-details
- name: Store
  property_count: 18
  slug: ikea-product-catalog-store
- name: AvailabilityEnvelope
  property_count: 5
  slug: ikea-sales-item-availability-envelope
- name: AvailabilityError
  property_count: 3
  slug: ikea-sales-item-availability-error
- name: Availability
  property_count: 6
  slug: ikea-sales-item-availability
- name: ClassUnitKey
  property_count: 2
  slug: ikea-sales-item-class-unit-key
- name: expandOption
  property_count: 0
  slug: ikea-sales-item-expand-option
- name: ItemKey
  property_count: 2
  slug: ikea-sales-item-item-key
- name: itemType
  property_count: 0
  slug: ikea-sales-item-item-type
- name: SalesLocation
  property_count: 3
  slug: ikea-sales-item-sales-location
- name: Category
  property_count: 4
  slug: ikea-search-category
- name: CommonProperties
  property_count: 2
  slug: ikea-search-common-properties
- name: itemType
  property_count: 0
  slug: ikea-search-item-type
- name: MoreProductsEnvelope
  property_count: 1
  slug: ikea-search-more-products-envelope
- name: ProductListPageEnvelope
  property_count: 9
  slug: ikea-search-product-list-page-envelope
- name: Product
  property_count: 31
  slug: ikea-search-product
json_structures:
- name: Ikea After Purchase Ordering Part Structure
  property_count: 8
  slug: ikea-after-purchase-ordering-part-structure
- name: Ikea After Purchase Ordering Product Parts Structure
  property_count: 5
  slug: ikea-after-purchase-ordering-product-parts-structure
- name: Ikea After Purchase Ordering Search Part Structure
  property_count: 9
  slug: ikea-after-purchase-ordering-search-part-structure
- name: Ikea After Purchase Ordering Status Structure
  property_count: 0
  slug: ikea-after-purchase-ordering-status-structure
- name: Ikea Product Catalog Category Structure
  property_count: 5
  slug: ikea-product-catalog-category-structure
- name: Ikea Product Catalog Product Details Structure
  property_count: 15
  slug: ikea-product-catalog-product-details-structure
- name: Ikea Product Catalog Store Structure
  property_count: 18
  slug: ikea-product-catalog-store-structure
- name: Ikea Sales Item Availability Envelope Structure
  property_count: 5
  slug: ikea-sales-item-availability-envelope-structure
- name: Ikea Sales Item Availability Error Structure
  property_count: 3
  slug: ikea-sales-item-availability-error-structure
- name: Ikea Sales Item Availability Structure
  property_count: 6
  slug: ikea-sales-item-availability-structure
- name: Ikea Sales Item Class Unit Key Structure
  property_count: 2
  slug: ikea-sales-item-class-unit-key-structure
- name: Ikea Sales Item Expand Option Structure
  property_count: 0
  slug: ikea-sales-item-expand-option-structure
- name: Ikea Sales Item Item Key Structure
  property_count: 2
  slug: ikea-sales-item-item-key-structure
- name: Ikea Sales Item Item Type Structure
  property_count: 0
  slug: ikea-sales-item-item-type-structure
- name: Ikea Sales Item Sales Location Structure
  property_count: 3
  slug: ikea-sales-item-sales-location-structure
- name: Ikea Search Category Structure
  property_count: 4
  slug: ikea-search-category-structure
- name: Ikea Search Common Properties Structure
  property_count: 2
  slug: ikea-search-common-properties-structure
- name: Ikea Search Item Type Structure
  property_count: 0
  slug: ikea-search-item-type-structure
- name: Ikea Search More Products Envelope Structure
  property_count: 1
  slug: ikea-search-more-products-envelope-structure
- name: Ikea Search Product List Page Envelope Structure
  property_count: 9
  slug: ikea-search-product-list-page-envelope-structure
- name: Ikea Search Product Structure
  property_count: 31
  slug: ikea-search-product-structure
jsonld:
- class_count: 4
  name: Ikea After Purchase Ordering Context
  property_count: 14
  slug: ikea-after-purchase-ordering-context
- class_count: 3
  name: Ikea Product Catalog Context
  property_count: 34
  slug: ikea-product-catalog-context
- class_count: 8
  name: Ikea Sales Item Context
  property_count: 18
  slug: ikea-sales-item-context
- class_count: 5
  name: Ikea Search Context
  property_count: 45
  slug: ikea-search-context
layout: provider
modified: '2026-05-30'
name: IKEA
nav: Providers
network: true
overview: 'IKEA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Categories API, Parts API, and 2 more. Tagged areas include Retail, Home Furnishings, Consumer Products, Opensource, and Community.


  The IKEA catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  IKEA''s developer surface includes authentication, engineering blog, code examples, and 12 more developer resources.'
random_paper: 62
rules:
- name: IKEA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ikea-jsonschema-spectral-rules
- name: IKEA API Rules
  rule_count: 34
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 19
  slug: ikea-rules
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 71.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Ikea Authentication
  slug: ikea-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ikea Domain Security
  slug: ikea-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ikea Vulnerability Disclosure
  slug: ikea-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ikea
tags:
- Retail
- Home Furnishings
- Consumer Products
- Opensource
- Community
- Unofficial API
- Smart Home
website: https://www.ikea.com/
---
