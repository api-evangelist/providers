---
aid: ebay
name: eBay
description: eBay is a multinational e-commerce corporation that operates a website facilitating consumer-to-consumer and business-to-consumer sales through its online platform. Users can buy and sell a wide range of products, including electronics, fashion, collectibles, and more, in an auction-style or buy-it-now format. eBay provides a secure and user-friendly platform for sellers to reach a global audience and for buyers to access a vast selection of items.
url: https://raw.githubusercontent.com/api-evangelist/ebay/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Auctions
  - Commerce
  - Products
  - Marketplace
created: '2023-11-09'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: ebay:account-api
    name: eBay Account API
    description: The eBay Account API allows sellers to programmatically configure their seller accounts on eBay, including payment policies, return policies, fulfillment policies, sales tax tables, and program opt-ins.
    humanURL: https://developer.ebay.com/api-docs/sell/account/static/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Account
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/account/static/overview.html
      - type: OpenAPI
        url: openapi/ebay-account-openapi-original.yml
  - aid: ebay:analytics-api
    name: eBay Analytics API
    description: The eBay Analytics API provides sellers with key performance metrics, traffic reports, customer service metrics, and seller standards information so they can measure and improve their performance on eBay.
    humanURL: https://developer.ebay.com/api-docs/sell/analytics/static/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Analytics
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/analytics/static/overview.html
      - type: OpenAPI
        url: openapi/ebay-analytics-openapi-original.yml
  - aid: ebay:compliance-api
    name: eBay Compliance API
    description: The eBay Compliance API surfaces listing-violation and policy-compliance issues so sellers can identify and resolve listings that conflict with eBay marketplace policies.
    humanURL: https://developer.ebay.com/api-docs/sell/compliance/resources/methods
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Compliance
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/compliance/resources/methods
      - type: OpenAPI
        url: openapi/ebay-compliance-openapi-original.yml
  - aid: ebay:feed-api
    name: eBay Feed API
    description: The eBay Feed API lets developers download large bulk feed files of eBay item, product, and order data for offline analysis and synchronization.
    humanURL: https://developer.ebay.com/api-docs/sell/feed/resources/methods
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Feed
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/feed/resources/methods
      - type: OpenAPI
        url: openapi/ebay-feed-openapi-original.yml
  - aid: ebay:browse-api
    name: eBay Browse API
    description: The eBay Browse API enables buyers to search and browse the eBay catalog, retrieve item details, and discover items by aspect or category.
    humanURL: https://developer.ebay.com/api-docs/buy/browse/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Buy
      - Browse
      - Search
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/buy/browse/overview.html
      - type: OpenAPI
        url: openapi/ebay-browse-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/buy/browse/release-notes.html
  - aid: ebay:deal-api
    name: eBay Deal API
    description: The eBay Deal API exposes the deals and promotions surfaced on eBay's deal pages so applications can present discounted offers to shoppers.
    humanURL: https://developer.ebay.com/api-docs/buy/deal/resources/methods
    baseURL: https://api.ebay.com
    tags:
      - Buy
      - Deals
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/buy/deal/resources/methods
      - type: OpenAPI
        url: openapi/ebay-deal-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/buy/deal/release-notes.html
  - aid: ebay:marketing-api
    name: eBay Marketing API
    description: The eBay Marketing API (also referred to as the Market API) provides merchandising placements, "also viewed" recommendations, and similar item suggestions to drive buyer engagement.
    humanURL: https://developer.ebay.com/api-docs/buy/marketing/resources/methods
    baseURL: https://api.ebay.com
    tags:
      - Buy
      - Marketing
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/buy/marketing/resources/methods
      - type: OpenAPI
        url: openapi/ebay-market-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/buy/marketing/release-notes.html
  - aid: ebay:marketplace-insights-api
    name: eBay Marketplace Insights API
    description: The eBay Marketplace Insights API gives access to historical sold-item data across the eBay marketplace so applications can analyze pricing trends and sell-through rates.
    humanURL: https://developer.ebay.com/api-docs/buy/marketplace-insights/resources/methods
    baseURL: https://api.ebay.com
    tags:
      - Buy
      - Insights
      - Analytics
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/buy/marketplace-insights/resources/methods
      - type: OpenAPI
        url: openapi/ebay-marketplace-insights-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/buy/marketplace-insights/release-notes.html
  - aid: ebay:offer-api
    name: eBay Offer API
    description: The eBay Offer API supports the offers experience for buyers, allowing applications to discover and act on offers across eligible listings.
    humanURL: https://developer.ebay.com/api-docs/buy/offer/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Buy
      - Offers
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/buy/offer/overview.html
      - type: OpenAPI
        url: openapi/ebay-offer-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/buy/offer/release-notes.html
  - aid: ebay:order-api
    name: eBay Order API
    description: The eBay Order API enables buyer-side checkout and order management workflows, including guest checkout sessions and order retrieval.
    humanURL: https://developer.ebay.com/api-docs/buy/order/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Buy
      - Orders
      - Checkout
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/buy/order/overview.html
      - type: OpenAPI
        url: openapi/ebay-order-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/buy/order/release-notes.html
  - aid: ebay:finances-api
    name: eBay Finances API
    description: The eBay Finances API gives sellers programmatic access to payouts, transactions, transfers, and seller funds tied to managed payments.
    humanURL: https://developer.ebay.com/api-docs/sell/finances/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Finances
      - Payments
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/finances/overview.html
      - type: OpenAPI
        url: openapi/ebay-finances-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/finances/release-notes.html
  - aid: ebay:fulfillment-api
    name: eBay Fulfillment API
    description: The eBay Fulfillment API helps sellers manage post-purchase order fulfillment, shipments, tracking, and refunds.
    humanURL: https://developer.ebay.com/api-docs/sell/fulfillment/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Fulfillment
      - Orders
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/fulfillment/overview.html
      - type: OpenAPI
        url: openapi/ebay-fulfillment-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/fulfillment/release-notes.html
  - aid: ebay:inventory-api
    name: eBay Inventory API
    description: The eBay Inventory API allows sellers to manage inventory items, offers, and listing publication on the eBay marketplace.
    humanURL: https://developer.ebay.com/api-docs/sell/inventory/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Inventory
      - Listings
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/inventory/overview.html
      - type: OpenAPI
        url: openapi/ebay-inventory-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/inventory/release-notes.html
  - aid: ebay:logistics-api
    name: eBay Logistics API
    description: The eBay Logistics API provides shipping rate quotes and label purchasing for sellers fulfilling orders inside or outside the eBay platform.
    humanURL: https://developer.ebay.com/api-docs/sell/logistics/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Logistics
      - Shipping
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/logistics/overview.html
      - type: OpenAPI
        url: openapi/ebay-logistics-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/logistics/release-notes.html
  - aid: ebay:metadata-api
    name: eBay Metadata API
    description: The eBay Metadata API exposes marketplace policies and configuration metadata that govern selling activity across countries and categories.
    humanURL: https://developer.ebay.com/api-docs/sell/metadata/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Metadata
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/metadata/overview.html
      - type: OpenAPI
        url: openapi/ebay-metadata-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/metadata/release-notes.html
  - aid: ebay:negotiation-api
    name: eBay Negotiation API
    description: The eBay Negotiation API lets sellers send targeted offers to interested buyers with discounted pricing on eligible listings.
    humanURL: https://developer.ebay.com/api-docs/sell/negotiation/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Negotiation
      - Offers
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/negotiation/overview.html
      - type: OpenAPI
        url: openapi/ebay-negotiation-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/negotiation/release-notes.html
  - aid: ebay:recommendation-api
    name: eBay Recommendation API
    description: The eBay Recommendation API surfaces actionable recommendations sellers can apply to improve listing performance, such as enabling Promoted Listings.
    humanURL: https://developer.ebay.com/api-docs/sell/recommendation/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Recommendations
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/recommendation/overview.html
      - type: OpenAPI
        url: openapi/ebay-recommendation-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/recommendation/release-notes.html
  - aid: ebay:stores-api
    name: eBay Stores API
    description: The eBay Stores API lets sellers manage the categories that organize listings within their eBay Store storefront.
    humanURL: https://developer.ebay.com/api-docs/sell/stores/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Sell
      - Stores
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/sell/stores/overview.html
      - type: OpenAPI
        url: openapi/ebay-stores-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/sell/stores/release-notes.html
  - aid: ebay:catalog-api
    name: eBay Catalog API
    description: The eBay Catalog API gives access to the eBay product catalog so sellers can attach items to canonical product entries when listing.
    humanURL: https://developer.ebay.com/api-docs/commerce/catalog/resources/methods
    baseURL: https://api.ebay.com
    tags:
      - Commerce
      - Catalog
      - Products
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/catalog/resources/methods
      - type: OpenAPI
        url: openapi/ebay-catalog-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/catalog/release-notes.html
  - aid: ebay:charity-api
    name: eBay Charity API
    description: The eBay Charity API exposes the registered charitable organizations supported by eBay for Charity so applications can search and reference them.
    humanURL: https://developer.ebay.com/api-docs/commerce/charity/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Commerce
      - Charity
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/charity/overview.html
      - type: OpenAPI
        url: openapi/ebay-charity-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/charity/release-notes.html
  - aid: ebay:identity-api
    name: eBay Identity API
    description: The eBay Identity API returns information about the authenticated eBay user so applications can personalize the buying or selling experience.
    humanURL: https://developer.ebay.com/api-docs/commerce/identity/overview.html
    baseURL: https://apiz.ebay.com
    tags:
      - Commerce
      - Identity
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/identity/overview.html
      - type: OpenAPI
        url: openapi/ebay-identity-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/identity/release-notes.html
  - aid: ebay:media-api
    name: eBay Media API
    description: The eBay Media API allows sellers to upload and manage video assets that can be associated with their listings.
    humanURL: https://developer.ebay.com/api-docs/commerce/media/overview.html
    baseURL: https://apim.ebay.com
    tags:
      - Commerce
      - Media
      - Video
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/media/overview.html
      - type: OpenAPI
        url: openapi/ebay-media-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/media/release-notes.html
  - aid: ebay:notification-api
    name: eBay Notification API
    description: The eBay Notification API manages destinations and subscriptions for the event-driven notifications eBay publishes to integrators, including marketplace account deletion, item availability, item price, campaign budget status, and authorization revocation events.
    humanURL: https://developer.ebay.com/api-docs/commerce/notification/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Commerce
      - Notifications
      - Events
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/notification/overview.html
      - type: OpenAPI
        url: openapi/ebay-notification-openapi-original.yml
      - type: AsyncAPI
        url: openapi/ebay-priority-listing-revisions-asyncapi-original.yml
      - type: AsyncAPI
        url: openapi/ebay-market-account-deletion-asyncapi-original.yml
      - type: AsyncAPI
        url: openapi/ebay-item-price-asyncapi-original.yml
      - type: AsyncAPI
        url: openapi/ebay-item-availability-asyncapi-original.yml
      - type: AsyncAPI
        url: openapi/ebay-campaign-budget-status-asyncapi-original.yml
      - type: AsyncAPI
        url: openapi/ebay-authorization-revocation-asyncapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/notification/release-notes.html
  - aid: ebay:taxonomy-api
    name: eBay Taxonomy API
    description: The eBay Taxonomy API exposes the category trees and item-aspect metadata that govern how items are classified across eBay marketplaces.
    humanURL: https://developer.ebay.com/api-docs/commerce/taxonomy/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Commerce
      - Taxonomy
      - Categories
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/taxonomy/overview.html
      - type: OpenAPI
        url: openapi/ebay-taxonomy-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/taxonomy/release-notes.html
  - aid: ebay:translation-api
    name: eBay Translation API
    description: The eBay Translation API provides machine translation of seller-supplied content such as listing titles and descriptions into supported eBay marketplace languages.
    humanURL: https://developer.ebay.com/api-docs/commerce/translation/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Commerce
      - Translation
      - Localization
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/commerce/translation/overview.html
      - type: OpenAPI
        url: openapi/ebay-translation-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/commerce/translation/release-notes.html
  - aid: ebay:client-registration-api
    name: eBay Client Registration API
    description: The eBay Client Registration API enables developers to create the application keys (App ID, Cert ID, Dev ID) used to authenticate calls to eBay APIs.
    humanURL: https://developer.ebay.com/api-docs/developer/client-registration/overview.html
    baseURL: https://api.ebay.com
    tags:
      - Developer
      - Registration
      - Authentication
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/developer/client-registration/overview.html
      - type: OpenAPI
        url: openapi/ebay-client-registration-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/developer/client-registration/release-notes.html
  - aid: ebay:key-management-api
    name: eBay Key Management API
    description: The eBay Key Management API manages the public/private key pairs developers use to sign requests for sensitive operations on the eBay platform.
    humanURL: https://developer.ebay.com/api-docs/developer/key-management/overview.html
    baseURL: https://apiz.ebay.com
    tags:
      - Developer
      - Keys
      - Security
    properties:
      - type: Documentation
        url: https://developer.ebay.com/api-docs/developer/key-management/overview.html
      - type: OpenAPI
        url: openapi/ebay-key-management-openapi-original.yml
      - type: Release Notes
        url: https://developer.ebay.com/api-docs/developer/key-management/release-notes.html
common:
  - type: Developer Portal
    url: https://developer.ebay.com/
  - type: Getting Started
    url: https://developer.ebay.com/develop/get-started
  - type: Guides
    url: https://developer.ebay.com/develop/guides
  - type: Tools
    url: https://developer.ebay.com/develop/tools
  - type: SDKs
    url: https://developer.ebay.com/develop/ebay-sdks
  - type: Widgets
    url: https://developer.ebay.com/develop/widgets
  - type: Support
    url: https://developer.ebay.com/my/support/tickets
  - type: Rate Limits
    url: https://developer.ebay.com/develop/apis/api-call-limits
  - type: Status
    url: https://developer.ebay.com/support/api-status
  - type: Forum
    url: https://community.ebay.com/t5/Developer-Groups/ct-p/developergroup
  - type: License
    url: https://developer.ebay.com/join/api-license-agreement
  - type: FAQ
    url: https://developer.ebay.com/support/faq
  - type: Blog
    url: https://developer.ebay.com/updates/blog
  - type: Newsletter
    url: https://developer.ebay.com/updates/newsletter
  - type: Events
    url: https://developer.ebay.com/grow/events
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
---
