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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 294
  human_in_the_loop: 3
  name: Elastic Path Agentic Access
  operation_count: 541
  slug: elastic-path-agentic-access
  summary_line: 541 operations · 294 acting · 3 human-in-the-loop
api_count: 100
apis:
- description: GraphQL abstraction over a subset of the Elastic Path Commerce Cloud APIs, providing a flexible query interface optimized for shopper-facing experiences including product browsing and catalog queries.
  name: Elastic Path GraphQL API
  slug: graphql-api
- description: The API to organize account addresses.
  name: Elastic Path Account Addresses API
  slug: elastic-path-account-addresses-api
- description: You can use the Account Authentication Settings endpoint to retrieve or modify how settings controlling account and account member authentication.
  name: Elastic Path Account Authentication Settings API
  slug: elastic-path-account-authentication-settings-api
- description: You can create associations between an account and one or more carts. After cart associations exist for an account, those carts are accessible across any device. You can delete associations as require
  name: Elastic Path Account Cart Associations API
  slug: elastic-path-account-cart-associations-api
- description: Commerce provides authentication tokens for an `Account` and an `Account Member`.
  name: Elastic Path Account Management Authentication API
  slug: elastic-path-account-management-authentication-api
- description: An `Account Member` resource is a user that you can add to accounts using account memberships. Account members API is read only, and you cannot add users using this API. There is a 1 to 1 corresponden
  name: Elastic Path Account Members API
  slug: elastic-path-account-members-api
- description: The `Account Membership` resource represents the relationship between an account and an account member. This relationship is many to many. Each account can have multiple account members, and each acco
  name: Elastic Path Account Membership API
  slug: elastic-path-account-membership-api
- description: Account Membership Settings allow Account Members to be associated to, at most, N accounts at a time. You can set this value to any number up to 10,000. The default value is 10,000. This setting is on
  name: Elastic Path Account Membership Settings API
  slug: elastic-path-account-membership-settings-api
- description: Account Tags are custom labels or metadata that can be attached to accounts to help organize and filter them based on specific attributes or criteria.
  name: Elastic Path Account Tags API
  slug: elastic-path-account-tags-api
- description: An Account represents the entity that participates in a Commerce transaction. Accounts can have Carts, Orders, Subscriptions, and Addresses.
  name: Elastic Path Accounts API
  slug: elastic-path-accounts-api
- description: 'Use the Administrator Latest Releases Catalog View API to retrieve product, hierarchy and node information. :::danger The Administrator Latest Releases Catalog View API is for Administrator use only. '
  name: Elastic Path Administrator Latest Releases Catalog API API
  slug: elastic-path-administrator-latest-releases-catalog-api-api
- description: You can use application keys to generate `client_credentials` and `implicit` tokens.
  name: Elastic Path Application Keys API
  slug: elastic-path-application-keys-api
- description: 'An authentication realm is a container that consists of the following: - Users - Represented by [User Authentication Info](/docs/api/single-sign-on/user-authentication-infos) objects - Authentication '
  name: Elastic Path Authentication Realms API
  slug: elastic-path-authentication-realms-api
- description: With Product Experience Manager, you can create and manage bundles. A bundle is a purchasable product, consisting of one or more products that you want to sell together. You can create multiple compon
  name: Elastic Path Bundle Component Products Relationships API
  slug: elastic-path-bundle-component-products-relationships-api
- description: Products added to a cart are referred to as a `cart_item`.
  name: Elastic Path Cart Items API
  slug: elastic-path-cart-items-api
- description: A Cart contains the product and custom cart items that a user intends to purchase. After a Cart is ready for Checkout, you can use the [Checkout endpoint](/docs/api/carts/checkout) to convert the cart
  name: Elastic Path Cart Management API
  slug: elastic-path-cart-management-api
- description: The Cart Payments API from Elastic Path — 1 operation(s) for cart payments.
  name: Elastic Path Cart Payments API
  slug: elastic-path-cart-payments-api
- description: Use Cart Settings to configure cart behavior for your store, including cart expiry, custom discounts, rule promotions, deferred inventory checks, and cart visibility for admins.
  name: Elastic Path Cart Settings API
  slug: elastic-path-cart-settings-api
- description: The Cart Shipping Groups API from Elastic Path — 2 operation(s) for cart shipping groups.
  name: Elastic Path Cart Shipping Groups API
  slug: elastic-path-cart-shipping-groups-api
- description: A catalog contains the products available for sale either in your organization or store. A catalog also contains information about how to organize those products for navigation menus and search facets
  name: Elastic Path Catalogs API
  slug: elastic-path-catalogs-api
- description: The checkout workflow ties together many of the key concepts covered in this section. When a customer initiates the checkout process, an order is created from the cart. The order is incomplete until a
  name: Elastic Path Checkout API
  slug: elastic-path-checkout-api
- description: ':::caution - There is a hard limit of 10 currencies per store. :::'
  name: Elastic Path Currencies API
  slug: elastic-path-currencies-api
- description: A **Custom API Entry** is a specific instance of a resource, such as a single wishlist in a Custom API for wishlists. Custom API Entries can be accessed in two different ways, via the **extension** en
  name: Elastic Path Custom API Entries API
  slug: elastic-path-custom-api-entries-api
- description: A Custom API Role Policy defines the level of access a role has to a Custom API. By default, administrative roles like **Store Admin** or **Org Admin** have full access to all Custom APIs. To grant ac
  name: Elastic Path Custom API Role Policies API
  slug: elastic-path-custom-api-role-policies-api
- description: Custom APIs allow you to extend the capabilities of Commerce. With Custom APIs, you can efficiently manage large data sets while benefiting from both simple and complex multidimensional filtering opti
  name: Elastic Path Custom APIs API
  slug: elastic-path-custom-apis-api
- description: With custom discounts, you can allow your shoppers to apply discounts from external services to their purchases. To apply custom discounts to carts and cart items, you need to set `custom_discounts_en
  name: Elastic Path Custom Discounts API
  slug: elastic-path-custom-discounts-api
- description: A Custom Field represents a single field of data (for example a Product Rating). A Custom API is composed of one or more Custom Fields. Here is a comparison of different types and validation available
  name: Elastic Path Custom Fields API
  slug: elastic-path-custom-fields-api
- description: The Custom Relationships API from Elastic Path — 2 operation(s) for custom relationships.
  name: Elastic Path Custom Relationships API
  slug: elastic-path-custom-relationships-api
- description: The API to organize customer addresses.
  name: Elastic Path Customer Addresses API
  slug: elastic-path-customer-addresses-api
- description: You can create associations between a customer and one or more carts. After cart associations exist for a customer, those carts are accessible across any device. You can delete associations as require
  name: Elastic Path Customer Cart Associations API
  slug: elastic-path-customer-cart-associations-api
- description: Dunning is the process of handling failed payment attempts. This is important for recovering revenue from failed payments, reduces customer churn and maintains cashflow. By implementing efficient dunn
  name: Elastic Path Dunning Rules API
  slug: elastic-path-dunning-rules-api
- description: '### Entries in Commerce Entries hold the pieces of data collected within the fields. If your flow has more than one field related to it, you see multiple field slugs. ### Entries in Product Experience'
  name: Elastic Path Entries API
  slug: elastic-path-entries-api
- description: '### Entry Relationships in Commerce When you create a field that uses `relationship` as a `field_type`, you update your entry values using the `Entry Relationship` endpoints. ### Entry Relationships i'
  name: Elastic Path Entry Relationships API
  slug: elastic-path-entry-relationships-api
- description: '```mdx-code-block import TemplatesOverview from ''/docs/partials/pxm/templates/extendingproducts.mdx''; <TemplatesOverview /> ```'
  name: Elastic Path Extending Products with Templates API
  slug: elastic-path-extending-products-with-templates-api
- description: A feature indicates some benefit that is received as a result of having an active subscription. This translates to tags being applied to the subscriber's account allowing access to some resource to be
  name: Elastic Path Features API
  slug: elastic-path-features-api
- description: 'With fields, you can: - in Commerce, use a field in your flows to represent single field of data (for example a `Product Rating`) to be applied to an entity - in Product Experience Manager, use an att'
  name: Elastic Path Fields API
  slug: elastic-path-fields-api
- description: 'You can upload image files or URLs by using `multipart/form-data` as the content type header. For example, `"Content-Type: multipart/form-data" \`. Commerce supports the following file types. | File E'
  name: Elastic Path Files API
  slug: elastic-path-files-api
- description: '### Flows in Commerce There are two scenarios for using flows: - Extend an existing resource, such as customers and orders. - Create a new resource, such as a blog, wishlist, or customer review. #### '
  name: Elastic Path Flows API
  slug: elastic-path-flows-api
- description: The Gateways API from Elastic Path — 12 operation(s) for gateways.
  name: Elastic Path Gateways API
  slug: elastic-path-gateways-api
- description: The Generate an Access Token API from Elastic Path — 1 operation(s) for generate an access token.
  name: Elastic Path Generate an Access Token API
  slug: elastic-path-generate-an-access-token-api
- description: '```mdx-code-block import HierarchyOverview from ''/docs/partials/pxm/hierarchies/hierarchies.mdx''; import HierarchyCatalog from ''/docs/partials/pxm/hierarchies/hierarchycatalogs.mdx''; <HierarchyOvervie'
  name: Elastic Path Hierarchies API
  slug: elastic-path-hierarchies-api
- description: You can create and update product price books and prices in bulk, at both organization and store level, using the Price Book Import API. This is useful, for example, if you have a promotion and want t
  name: Elastic Path Import a Price Book and Prices API
  slug: elastic-path-import-a-price-book-and-prices-api
- description: You can import stock positions for up to 50,000 products in a single operation via an import. This is useful for synchronosing external systems with Elastic Path. The API uses a [**JSONL**](https://js
  name: Elastic Path Imports API
  slug: elastic-path-imports-api
- description: 'Indexable Fields allow you to extend and fine-tune the search schema. By default, the search index includes all the core product fields like name, description, SKU, slug etc. Indexable Fields let you:'
  name: Elastic Path Indexable Fields API
  slug: elastic-path-indexable-fields-api
- description: Setting up and managing integrations.
  name: Elastic Path Integrations API
  slug: elastic-path-integrations-api
- description: The Inventory API allows you to manage stock for products at both organization and store levels. Each product keeps a history of inventory transactions, enabling easier stock auditing. You can specify
  name: Elastic Path Inventory API
  slug: elastic-path-inventory-api
- description: 'Invoices represent the amount a customer owes for a subscription. Elastic Path Subscriptions generates an invoice for every period in a subscription billing cycle. Invoices provide: - an itemized list'
  name: Elastic Path Invoices API
  slug: elastic-path-invoices-api
- description: 'Jobs manage the indexing operations for catalog search. When catalogs are published or when reindexing is required, jobs process the product data and build search indexes. ### Job Types | Type | Descr'
  name: Elastic Path Jobs API
  slug: elastic-path-jobs-api
- description: The Locations API from Elastic Path — 2 operation(s) for locations.
  name: Elastic Path Locations API
  slug: elastic-path-locations-api
- description: You can use the Logs TTL Settings endpoint to retrieve and update settings controlling logs time-to-live (TTL).
  name: Elastic Path Logs Time to Live Settings API
  slug: elastic-path-logs-time-to-live-settings-api
- description: The Merchant Realm Mappings API from Elastic Path — 2 operation(s) for merchant realm mappings.
  name: Elastic Path Merchant Realm Mappings API
  slug: elastic-path-merchant-realm-mappings-api
- description: An offering is a combination of plans and pricing options; plans are combined with one or more pricing options to form an offering. For example, your company provides online streaming of movies, web-s
  name: Elastic Path Offerings API
  slug: elastic-path-offerings-api
- description: The OIDC IDP Login endpoints handle the initiation of OpenID Connect authentication flows. When a user needs to authenticate via OIDC, they are redirected to these endpoints which then redirect them t
  name: Elastic Path OIDC Authentication API
  slug: elastic-path-oidc-authentication-api
- description: An OpenID Connect Profile resource represents a specific configuration of an OpenID Connect Provider. An authentication realm can have multiple OpenID Connect Profiles. This allows shoppers to authent
  name: Elastic Path OIDC Profiles API
  slug: elastic-path-oidc-profiles-api
- description: The Order Shipping Groups API from Elastic Path — 2 operation(s) for order shipping groups.
  name: Elastic Path Order Shipping Groups API
  slug: elastic-path-order-shipping-groups-api
- description: An Order is created through the [checkout](/docs/api/carts/checkout) endpoint within the Carts API. An order is created after a customer checks out their cart. On creation, the order is marked unpaid.
  name: Elastic Path Orders API
  slug: elastic-path-orders-api
- description: A `password_profile` resource represents a specific configuration that allows users to authenticate through username and password. Password Profiles support One-Time Password Tokens, which can be used
  name: Elastic Path Password Profiles API
  slug: elastic-path-password-profiles-api
- description: When you [checkout](/docs/api/carts/checkout) a [cart](/docs/api/carts/cart-management), an unpaid [order](/docs/api/carts/orders) is returned. You can process the payment for the order though a payme
  name: Elastic Path Payments API
  slug: elastic-path-payments-api
- description: Erasure requests enable you to exercise the right, referred to in regulations such as GDPR, as the right to be forgotten or right to erase. Erasure requests allow you to wipe out personal data from Co
  name: Elastic Path Personal Data Erasure Requests API
  slug: elastic-path-personal-data-erasure-requests-api
- description: When a user’s personal data is changed, an event is logged by Commerce. You can use the Personal Data Logs endpoint to access these logs. This API is read only, and you cannot add, update, or delete l
  name: Elastic Path Personal Data Logs API
  slug: elastic-path-personal-data-logs-api
- description: This is a supplementary endpoint for the [logs](/docs/api/personal-data/logs-time-to-live-settings) endpoint. It allows you to view all data entries that are related to the resource specified in the f
  name: Elastic Path Personal Data Related Data Entries API
  slug: elastic-path-personal-data-related-data-entries-api
- description: You can use price modifiers to change the price property of child products. By default, child products inherit the same price as their base products. Using price modifiers, you can enable child produc
  name: Elastic Path Price Book Modifiers API
  slug: elastic-path-price-book-modifiers-api
- description: Price books contain prices for the products in your catalog. Each catalog must have one price book. In your storefront, the product prices are displayed in the currency for the selected locale. If a p
  name: Elastic Path Price Books API
  slug: elastic-path-price-books-api
- description: 'Price books contain prices for the products in your catalog. Use the Price Books API to create price books and add product prices to the price book. ### Volume (tiers) Pricing Using volume (tiers) pri'
  name: Elastic Path Prices API
  slug: elastic-path-prices-api
- description: '```mdx-code-block import ProductExport from ''/docs/partials/pxm/import/export.mdx''; <ProductExport /> ``` ### Characteristics of Exporting Products - Product exports are an asynchronous operation. Whe'
  name: Elastic Path Product Export API
  slug: elastic-path-product-export-api
- description: Products are the items or services that you might want to sell in your store. In Product Experience Manager, products can also have associated rich media assets, such as product images or a file conta
  name: Elastic Path Product File Relationships API
  slug: elastic-path-product-file-relationships-api
- description: Products are the items or services that you might want to sell in your store. In Product Experience Manager, products can also have associated rich media assets, such as product images or a file conta
  name: Elastic Path Product Image Relationships API
  slug: elastic-path-product-image-relationships-api
- description: '```mdx-code-block import ProductImport from ''/docs/partials/pxm/import/import.mdx''; <ProductImport /> ``` #### Using Imported Main Image Files You can use the main images that you have previously uplo'
  name: Elastic Path Product Import/Bulk Update API
  slug: elastic-path-product-import-bulk-update-api
- description: The Product Relationships API from Elastic Path — 3 operation(s) for product relationships.
  name: Elastic Path Product Relationships API
  slug: elastic-path-product-relationships-api
- description: '```mdx-code-block import ProductTags from ''/docs/partials/pxm/products/tags.mdx''; <ProductTags /> ```'
  name: Elastic Path Product Tags API
  slug: elastic-path-product-tags-api
- description: '```mdx-code-block import ProductsOverview from ''/docs/partials/pxm/products/productsoverview.mdx''; import ProductTypes from ''/docs/partials/pxm/products/types.mdx''; import ProductTags from ''/docs/part'
  name: Elastic Path Products API
  slug: elastic-path-products-api
- description: 'You can apply promotions automatically to all customer carts, or you can create promotion codes that customers must enter to receive the discount. You can enable this feature by setting the automatic '
  name: Elastic Path Promotion Codes API
  slug: elastic-path-promotion-codes-api
- description: 'Use Jobs API to initiate a job within a promotion. Jobs operate asynchronously and have a different status based on their progress. The following are the job statuses: - `pending`: Commerce has receiv'
  name: Elastic Path Promotion Jobs API
  slug: elastic-path-promotion-jobs-api
- description: The Promotions Standard API from Elastic Path — 3 operation(s) for promotions standard.
  name: Elastic Path Promotions Standard API
  slug: elastic-path-promotions-standard-api
- description: 'Proration is the adjustment of charges or credits on a subscriber''s account based on the amount of time a service is used. Proration ensures that subscribers are only charged for the actual time they '
  name: Elastic Path Proration Policies API
  slug: elastic-path-proration-policies-api
- description: 'When a catalog is published, a catalog release is created. A catalog release provides a snapshot of the product information taken at the time of publication. You can have one or more catalog releases '
  name: Elastic Path Releases API
  slug: elastic-path-releases-api
- description: The Rule Promotion Codes API from Elastic Path — 2 operation(s) for rule promotion codes.
  name: Elastic Path Rule Promotion Codes API
  slug: elastic-path-rule-promotion-codes-api
- description: The Rule Promotion Jobs API from Elastic Path — 3 operation(s) for rule promotion jobs.
  name: Elastic Path Rule Promotion Jobs API
  slug: elastic-path-rule-promotion-jobs-api
- description: The Rule Promotion Usages API from Elastic Path — 3 operation(s) for rule promotion usages.
  name: Elastic Path Rule Promotion Usages API
  slug: elastic-path-rule-promotion-usages-api
- description: The Rule Promotions API from Elastic Path — 2 operation(s) for rule promotions.
  name: Elastic Path Rule Promotions API
  slug: elastic-path-rule-promotions-api
- description: If your store requires multiple catalogs, add catalog rules to control when a catalog is displayed. A catalog rule contains a catalog plus the criteria under which to display the catalog. :::caution Y
  name: Elastic Path Rules API
  slug: elastic-path-rules-api
- description: You can schedule your billing, tax, and payment runs. By scheduling billing, tax, and payment runs, you automate the process, reducing manual intervention and ensuring the jobs are run in a timely man
  name: Elastic Path Schedules API
  slug: elastic-path-schedules-api
- description: The Search API enables you to search for products in your published catalogs. Search provides powerful capabilities including full-text search, filtering, faceting, and sorting to help shoppers find p
  name: Elastic Path Search API
  slug: elastic-path-search-api
- description: Search Indexes represent the indexed data for your catalog releases. Each time a catalog is published with search enabled, a search index is created containing the product data optimized for fast quer
  name: Elastic Path Search Indexes API
  slug: elastic-path-search-indexes-api
- description: Search Profiles are configuration objects that control how search queries are executed. They provide a powerful way to customize search relevance, filtering, and ranking without requiring code changes
  name: Elastic Path Search Profiles API
  slug: elastic-path-search-profiles-api
- description: The Searchable Fields API returns a list of all fields available for searching, filtering, faceting, and sorting in your search queries. This includes both the standard product fields that are indexed
  name: Elastic Path Searchable Fields API
  slug: elastic-path-searchable-fields-api
- description: The Settings API allow you to configure global settings for your project.
  name: Elastic Path Settings API
  slug: elastic-path-settings-api
- description: Use the Shopper Catalog View API to retrieve hierarchy, node and product information for a catalog release. When you publish a catalog for a store, you can define catalog rules so that you can show ca
  name: Elastic Path Shopper Catalog API API
  slug: elastic-path-shopper-catalog-api-api
- description: Standard Shopper Roles represent the roles of customers.
  name: Elastic Path Standard Shopper Roles API
  slug: elastic-path-standard-shopper-roles-api
- description: Standard User Roles represent the roles that can be assigned to users through Commerce Manager. These roles define the level of access a user has to Commerce Manager.
  name: Elastic Path Standard User Roles API
  slug: elastic-path-standard-user-roles-api
- description: 'Stopword Sets allow you to define sets of common words (such as "the", "a", "an", "is") that should be ignored during search queries. By removing these low-value terms from search processing, you can '
  name: Elastic Path Stopword Sets API
  slug: elastic-path-stopword-sets-api
- description: A subscriber is someone who subscribes to your plan or service.
  name: Elastic Path Subscribers API
  slug: elastic-path-subscribers-api
- description: Elastic Path Subscriptions enables you to manage your subscriptions plans and pricing options, using offerings. Offerings can contain any combination of pricing options and a plan. When a customer cho
  name: Elastic Path Subscriptions API
  slug: elastic-path-subscriptions-api
- description: 'Synonym Sets allow you to define groups of equivalent or related terms so that searches for one term also return results for its synonyms. This helps shoppers find products regardless of the specific '
  name: Elastic Path Synonym Sets API
  slug: elastic-path-synonym-sets-api
- description: Taxes differ by country and can differ within the country by region, state, or province. Each jurisdiction has a unique tax code and rate. If your store serves many jurisdictions, integrate a third-pa
  name: Elastic Path Tax Items API
  slug: elastic-path-tax-items-api
- description: Methods to allow you to modify and view a products stock via transactions.
  name: Elastic Path Transactions API
  slug: elastic-path-transactions-api
- description: A `user-authentication-info` represents a user. This object contains information, such as the name and email address, and has sub-resources for each mechanism that the user can use to log in./single-s
  name: Elastic Path User Authentication Infos API
  slug: elastic-path-user-authentication-infos-api
- description: The `user-authentication-oidc-profile-info` object is the information object about the relationship between a [User Authentication Info](/docs/api/single-sign-on/user-authentication-infos) and an [Ope
  name: Elastic Path User Authentication OIDC Profile Infos API
  slug: elastic-path-user-authentication-oidc-profile-infos-api
- description: The `user-authentication-password-profile-info` object is the information object about the relationship between a [User Authentication Info](/docs/api/single-sign-on/user-authentication-infos) and a [
  name: Elastic Path User Authentication Password Profile Infos API
  slug: elastic-path-user-authentication-password-profile-infos-api
- description: '```mdx-code-block import VariationsOverview from ''/docs/partials/pxm/variations/variationsoverview.mdx''; import VariationsReusability from ''/docs/partials/pxm/variations/variationsreusability.mdx''; im'
  name: Elastic Path Variations API
  slug: elastic-path-variations-api
artifact_total: 122
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-path-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elastic-path-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elastic-path-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elastic-path-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elasticpath.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.elasticpath.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/elasticpath
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-path
- group: company
  title: ''
  type: Blog
  url: https://www.elasticpath.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elasticpath.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elasticpath.com
- group: other
  title: ''
  type: X
  url: https://x.com/elasticpath
- group: commercial
  title: ''
  type: Plans
  url: plans/elastic-path-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elastic-path-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elastic-path-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.elasticpath.com
- group: build
  title: ''
  type: PostmanCollection
  url: https://developer.elasticpath.com/docs/developer-tools/index
created: 2026-06-13
description: Elastic Path is a headless commerce platform providing REST and GraphQL APIs for managing catalogs, products, price books, promotions, carts, orders, subscriptions, payments, and customer accounts in composable commerce architectures. It is designed for B2B, D2C, and multi-brand enterprise retailers building API-first, microservices-based shopping experiences.
examples:
- key_count: 4
  name: Elastic Path Examples
  slug: elastic-path-examples
finops:
- name: Elastic Path Finops
  service_category: ''
  slug: elastic-path-finops
graphqls:
- description: GraphQL abstraction over the Elastic Path Commerce Cloud platform, providing a flexible query interface optimized for shopper-facing and headless commerce experiences. The GraphQL server wraps the und
  name: Elastic Path GraphQL API
  slug: elastic-path-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic-path.png
json_schemas:
- name: Account Management Introduction
  property_count: 0
  slug: accounts
- name: Carts, Checkout, Orders Introduction
  property_count: 0
  slug: carts
- name: Catalogs Introduction
  property_count: 0
  slug: catalog
- name: Currencies Introduction
  property_count: 0
  slug: currencies
- name: Files Introduction
  property_count: 0
  slug: files
- name: Integrations Introduction
  property_count: 0
  slug: integrations
- name: Inventories Introduction
  property_count: 0
  slug: inventory
- name: Payment Gateways Introduction
  property_count: 0
  slug: payments
- name: Product Experience Manager Introduction
  property_count: 0
  slug: pim
- name: Price Books Introduction
  property_count: 0
  slug: pricebooks
- name: Promotions Standard Introduction
  property_count: 0
  slug: promotions
- name: Subscriptions Introduction
  property_count: 0
  slug: subscriptions
layout: provider
modified: 2026-06-13
name: Elastic Path
nav: Providers
network: true
overview: 'Elastic Path publishes 99 APIs on the [APIs.io](https://apis.io/) network, including Account Addresses API, Account Authentication Settings API, Account Cart Associations API, and 96 more. Tagged areas include Commerce, Headless Commerce, Composable Commerce, eCommerce, and B2B.


  The Elastic Path catalog on APIs.io includes 1 Spectral governance ruleset.


  Elastic Path''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Elastic Path Plans Pricing
  plan_count: 0
  slug: elastic-path-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Elastic Path Rate Limits
  slug: elastic-path-rate-limits
rules:
- name: Elastic Path API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: elastic-path-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.0
  delta: -3.2
  facets:
    commercial_clarity: 18.4
    contract_quality: 63.5
    developer_ergonomics: 30.4
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 99
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elastic-path/refs/heads/main/screenshots/elastic-path-2026-06-20T180529.png
security:
- kind: authentication
  name: Elastic Path Authentication
  slug: elastic-path-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Elastic Path Domain Security
  slug: elastic-path-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Elastic Path Vulnerability Disclosure
  slug: elastic-path-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: elastic-path
tags:
- Commerce
- Headless Commerce
- Composable Commerce
- eCommerce
- B2B
- Products
- Catalogs
- Orders
- Promotions
- Subscriptions
- Payments
website: https://www.elasticpath.com
---
