---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Akeneo Agentic Access
  operation_count: 54
  slug: akeneo-agentic-access
  summary_line: 54 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Authentication API from Akeneo — 1 operation(s) for authentication.
  name: Akeneo Authentication API
  slug: akeneo-authentication-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Catalogs API from Akeneo — 2 operation(s) for catalogs.
  name: Akeneo Catalogs API
  slug: akeneo-catalogs-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The System API from Akeneo — 2 operation(s) for system.
  name: Akeneo System API
  slug: akeneo-system-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Workflows API from Akeneo — 2 operation(s) for workflows.
  name: Akeneo Workflows API
  slug: akeneo-workflows-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An asset is a flexible object that makes it possible to enrich products with images, videos, documents… An asset must be part of an asset family. That way, it will have its own attributes and lifecycl
  name: Akeneo Asset API
  slug: akeneo-asset-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An asset attribute is a piece of information that can be associated with an asset. Asset attributes can be used to store various types of data, such as text, numbers, dates, or media files. They are u
  name: Akeneo Asset attribute API
  slug: akeneo-asset-attribute-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: 'An asset attribute option is a value that can be associated with an asset attribute. For example, if you have an asset attribute called "Type", the options could be "Image", "Video", "Document", etc. '
  name: Akeneo Asset attribute option API
  slug: akeneo-asset-attribute-option-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An asset family is a set of attributes that are shared by assets belonging to this family. In other words, an asset family can be considered as a template for assets.
  name: Akeneo Asset family API
  slug: akeneo-asset-family-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An asset media file is a file that can be attached to an asset family or an asset. It can be an image, a video, a PDF, or any other type of file. Asset media files are used to enrich the asset informa
  name: Akeneo Asset media file API
  slug: akeneo-asset-media-file-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An association type is a way to define the relationship between products or product models. It allows you to create links between products, such as "related products", "up-sell products", or "cross-se
  name: Akeneo Association type API
  slug: akeneo-association-type-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An attribute is a piece of information that can be associated with a product or product model. Attributes can be used to store various types of data, such as text, numbers, dates, or media files. They
  name: Akeneo Attribute API
  slug: akeneo-attribute-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: 'An attribute group is a way to organize attributes in the PIM. It allows you to group related attributes together, making it easier to manage and maintain product data. For example, you could have an '
  name: Akeneo Attribute group API
  slug: akeneo-attribute-group-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: An attribute option is a value that can be associated with an attribute. For example, if you have an attribute called "Color", the options could be "Red", "Blue", "Green", etc. Options are used to pro
  name: Akeneo Attribute option API
  slug: akeneo-attribute-option-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A catalog contains a selection of products from the PIM, intended to be synchronized with a third-party application via the API. The Catalog products endpoint allows you to retrieve the list of produc
  name: Akeneo Catalog products API
  slug: akeneo-catalog-products-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A category is a way of classifying products. Categories constitute category trees and in Akeneo, you can have multiple category trees with an unlimited number of levels (categories, subcategories, sub
  name: Akeneo Category API
  slug: akeneo-category-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A channel is a way to define how products are presented in different contexts, such as online stores, mobile applications, or print catalogs. Channels can have different configurations, such as curren
  name: Akeneo Channel API
  slug: akeneo-channel-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A currency is a unit of exchange that is used to price products. Currencies are used in the PIM to define the prices of products in different markets.
  name: Akeneo Currency API
  slug: akeneo-currency-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Data Architect Agent endpoints allow you to create modelization suggestions for the data model designer. These suggestions can be used to improve the catalog structure and data quality.
  name: Akeneo Data Architect Agent API
  slug: akeneo-data-architect-agent-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: Extensions allow you to extend the Akeneo PIM user interface with custom components. They can be used to add new features or to modify the existing ones. Extensions are useful for integrating with ext
  name: Akeneo Extensions API
  slug: akeneo-extensions-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A family is a set of attributes that are shared by products belonging to this family. In other words, a family can be considered as a template for products. A product family can use all of the attribu
  name: Akeneo Family API
  slug: akeneo-family-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A family variant is a specific type of family that allows you to create variants of a product model. It allows you to define the attributes and values that are specific to the variants of a product mo
  name: Akeneo Family variant API
  slug: akeneo-family-variant-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A job is a process that can be executed in the PIM to perform various tasks, such as importing or exporting data. Jobs can be used to synchronize data between the PIM and external systems, or to perfo
  name: Akeneo Jobs API
  slug: akeneo-jobs-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: 'A locale is a combination of a language (English, German, French...) and a country (United States, United Kingdom, France...). Examples: English UK (en_GB), English US (en_US), English AU (en_AU). You'
  name: Akeneo Locale API
  slug: akeneo-locale-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The mapping schema for products defines the expected structure of product data when synchronizing via the API. It describes the fields, their types, constraints, and transformation rules applied durin
  name: Akeneo Mapping schema for products API
  slug: akeneo-mapping-schema-for-products-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A measurement family is a set of comparable units used to measure a specific physical quantity, such as Area, Weight, or Power. For example, the "Weight" measurement family can group units like "Kilog
  name: Akeneo Measurement family API
  slug: akeneo-measurement-family-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: This API reference provides comprehensive documentation for the Akeneo PIM REST API. It describes all available endpoints, request and response formats, authentication methods, and error codes. The Ak
  name: Akeneo Overview API
  slug: akeneo-overview-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Permissions endpoints allow you to retrieve the permissions for a given user. You can use these endpoints to get information about which channels and locales a user can view or edit.
  name: Akeneo Permissions API
  slug: akeneo-permissions-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A product is a single item that can be managed in the PIM. It can have various attributes and values, and can be associated with product models, categories, and other entities. Products are the core e
  name: Akeneo Product [identifier] API
  slug: akeneo-product-identifier-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A media file is a file that can be attached to a product, product model, category, or asset. It can be an image, a video, a PDF, or any other type of file. Media files are used to enrich the product i
  name: Akeneo Product media file API
  slug: akeneo-product-media-file-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: 'A product model is a template for products that share the same attributes and values. It allows you to create a hierarchy of products, where a product model can have several variants. A product model '
  name: Akeneo Product model API
  slug: akeneo-product-model-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A product is a single item that can be managed in the PIM. It can have various attributes and values, and can be associated with product models, categories, and other entities. Products are the core e
  name: Akeneo Product [uuid] API
  slug: akeneo-product-uuid-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A readiness configuration defines custom "ready" criteria for products and/or product models, distinct from completeness. It computes a 0-100 score for each channel/locale combination, based on a conf
  name: Akeneo Readiness API
  slug: akeneo-readiness-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A reference entity is a custom entity that can be used to store additional information about products or product models. It allows you to create your own entities with their own attributes and values,
  name: Akeneo Reference entity API
  slug: akeneo-reference-entity-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A reference entity attribute is a piece of information that can be associated with a reference entity. Reference entity attributes can be used to store various types of data, such as text, numbers, da
  name: Akeneo Reference entity attribute API
  slug: akeneo-reference-entity-attribute-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A reference entity attribute option is a value that can be associated with a reference entity attribute. For example, if you have a reference entity attribute called "Category", the options could be "
  name: Akeneo Reference entity attribute option API
  slug: akeneo-reference-entity-attribute-option-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A reference entity media file is a file that can be attached to a reference entity record. It can be an image, a video, a PDF, or any other type of file. Reference entity media files are used to enric
  name: Akeneo Reference entity media file API
  slug: akeneo-reference-entity-media-file-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A reference entity record is a specific instance of a reference entity. It contains the values for the attributes defined in the reference entity. Reference entity records can be linked to products or
  name: Akeneo Reference entity record API
  slug: akeneo-reference-entity-record-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: Rule definitions automate product data enrichment by applying actions when conditions are met. These endpoints allow you to list, read, and create or update rule definitions.
  name: Akeneo Rule definition API
  slug: akeneo-rule-definition-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: 'A supplier is an external organization that contributes product data to the PIM through the supplier portal. A supplier holds its own users, who sign in to the portal to submit and enrich products on '
  name: Akeneo Supplier API
  slug: akeneo-supplier-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: A user is a person who signs in to the PIM. Their roles define what they are allowed to do, and their user groups define which data they can access.
  name: Akeneo User API
  slug: akeneo-user-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Workflow executions endpoints allow you to start workflows on products and product models.
  name: Akeneo Workflow executions API
  slug: akeneo-workflow-executions-api
- baseURL: https://api.akeneo.com
  baseurl_source: declared
  description: The Tasks endpoints allow you to retrieve the tasks for each workflow steps, products and product models. It also allows you to manage the tasks by approving, rejecting or completing them.
  name: Akeneo Workflow tasks API
  slug: akeneo-workflow-tasks-api
artifact_total: 65
collections:
- collection_type: open
  name: Akeneo PIM REST Asset Manager API
  slug: open-akeneo-asset-manager-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Attributes API
  slug: open-akeneo-attributes-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Authentication API
  slug: open-akeneo-authentication-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Catalogs API
  slug: open-akeneo-catalogs-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Categories API
  slug: open-akeneo-categories-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Channels API
  slug: open-akeneo-channels-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Currencies API
  slug: open-akeneo-currencies-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Families API
  slug: open-akeneo-families-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Locales API
  slug: open-akeneo-locales-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Media Files API
  slug: open-akeneo-media-files-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Product Models API
  slug: open-akeneo-product-models-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Products API
  slug: open-akeneo-products-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Reference Entities API
  slug: open-akeneo-reference-entities-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager System API
  slug: open-akeneo-system-api
- collection_type: open
  name: Akeneo PIM REST Asset Manager Workflows API
  slug: open-akeneo-workflows-api
- collection_type: open
  name: Akeneo PIM REST API
  slug: open-akeneo
common:
- group: other
  href: https://artifacts.apis.io/akeneo/capabilities/akeneo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/akeneo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/akeneo/agentic-access/akeneo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/akeneo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/akeneo/security/akeneo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/akeneo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/akeneo/security/akeneo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/akeneo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/akeneo/security/akeneo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akeneo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/akeneo/authentication/akeneo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/akeneo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/akeneo/scopes/akeneo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/akeneo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akeneo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akeneo
- group: company
  title: ''
  type: Website
  url: https://www.akeneo.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.akeneo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.akeneo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.akeneo.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.akeneo.com/request-a-demo/
- group: company
  title: ''
  type: Blog
  url: https://www.akeneo.com/feed/
created: '2026-05-11'
description: Akeneo is a Product Information Management (PIM) platform that centralizes, enriches, and distributes product data across digital commerce channels, enabling brands, retailers, and manufacturers to deliver consistent product experiences. The Akeneo PIM SaaS exposes a REST API, GraphQL API, an Event Platform with webhooks, a Supplier Data Manager API, and an Activation API for retail use cases. Authentication uses OAuth 2.0 client credentials with per-tenant base URLs in the cloud edition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akeneo.png
layout: provider
modified: '2026-05-11'
name: Akeneo
nav: Providers
network: true
overview: 'Akeneo publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Catalogs API, System API, and 39 more. Tagged areas include Product Information Management, Product Data, Catalog Management, Commerce, and Retail.


  The Akeneo catalog on APIs.io includes 1 Spectral governance ruleset.


  Akeneo''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 10 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Akeneo API Rules
  rule_count: 69
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 15
  slug: akeneo-rules
scopes:
- name: Akeneo Scopes
  scope_count: 36
  slug: akeneo-scopes
  summary_line: 36 scopes · clientCredentials
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 61.3
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 72.4
      total: 58
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/akeneo/akeneo-2026-06-20T171448.png
security:
- kind: authentication
  name: Akeneo Authentication
  slug: akeneo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Akeneo Domain Security
  slug: akeneo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Akeneo Vulnerability Disclosure
  slug: akeneo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Akeneo Trust Center
  slug: akeneo-trust-center
  summary_line: SOC 2, ISO 27001
slug: akeneo
tags:
- Product Information Management
- Product Data
- Catalog Management
- Commerce
- Retail
website: https://www.akeneo.com
---
