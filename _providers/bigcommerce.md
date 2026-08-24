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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 341
  human_in_the_loop: 2
  name: Bigcommerce Agentic Access
  operation_count: 547
  slug: bigcommerce-agentic-access
  summary_line: 547 operations · 341 acting · 2 human-in-the-loop
api_count: 161
apis:
- description: BigCommerce Inventory API exposes location-aware, item-level inventory data to API consumers. You can get inventory levels at all locations or specific locations and update inventory levels at a speci
  name: Big Commerce Inventory
  slug: bigcommerce-inventory
- description: 'BigCommerce Locations API allows merchants to create, read, update, and delete inventory locations for their store. All BigCommerce stores have at least one default location, and additional locations '
  name: Big Commerce Locations
  slug: bigcommerce-locations
- description: BigCommerce Customer Segmentation API enables the creation of externally defined customer segments that can be targeted within promotions and other customized shopping experiences. The API allows merc
  name: Big Commerce Customer Segmentation
  slug: bigcommerce-customer-segmentation
- description: BigCommerce Promotions API allows merchants to create, manage, and delete promotional campaigns and discount codes for their online store. A promotion is composed of a condition that a customer can sa
  name: Big Commerce Promotions
  slug: bigcommerce-promotions
- description: 'BigCommerce Promotion Settings API enables merchants to configure and manage global promotion settings for their online store. This API provides control over how promotions are applied and displayed, '
  name: Big Commerce Promotion Settings
  slug: bigcommerce-promotion-settings
- description: BigCommerce Pickup Methods API allows merchants to manage pickup methods for their buy online, pick up in store (BOPIS) fulfillment strategy. This REST Management API enables the creation and configur
  name: Big Commerce Pickup Methods
  slug: bigcommerce-pickup-methods
- description: BigCommerce Storefront Pickup Options API returns up to 10 available pickup options for requested items around a radius of provided search coordinates. The pickup options returned only include options
  name: Big Commerce Storefront Pickup Options
  slug: bigcommerce-storefront-pickup-options
- description: 'BigCommerce Transactions API provides access to order transaction data and payment actions. The API returns transaction details for orders, including payment method information and fraud details when '
  name: Big Commerce Transactions
  slug: bigcommerce-transactions
- description: The Abandoned Cart Emails API from BigCommerce — 3 operation(s) for abandoned cart emails.
  name: BigCommerce Abandoned Cart Emails API
  slug: bigcommerce-abandoned-cart-emails-api
- description: The Abandoned Cart Settings API from BigCommerce — 1 operation(s) for abandoned cart settings.
  name: BigCommerce Abandoned Cart Settings API
  slug: bigcommerce-abandoned-cart-settings-api
- description: The Abandoned Carts API from BigCommerce — 1 operation(s) for abandoned carts.
  name: BigCommerce Abandoned Carts API
  slug: bigcommerce-abandoned-carts-api
- description: The Abandoned Carts Settings API from BigCommerce — 2 operation(s) for abandoned carts settings.
  name: BigCommerce Abandoned Carts Settings API
  slug: bigcommerce-abandoned-carts-settings-api
- description: The Access API from BigCommerce — 1 operation(s) for access.
  name: BigCommerce Access API
  slug: bigcommerce-access-api
- description: The Active Theme API from BigCommerce — 1 operation(s) for active theme.
  name: BigCommerce Active Theme API
  slug: bigcommerce-active-theme-api
- description: The Addresses API from BigCommerce — 1 operation(s) for addresses.
  name: BigCommerce Addresses API
  slug: bigcommerce-addresses-api
- description: The Analytics API from BigCommerce — 2 operation(s) for analytics.
  name: BigCommerce Analytics API
  slug: bigcommerce-analytics-api
- description: The API Token API from BigCommerce — 1 operation(s) for api token.
  name: BigCommerce API Token API
  slug: bigcommerce-api-token-api
- description: The Attribute Values API from BigCommerce — 1 operation(s) for attribute values.
  name: BigCommerce Attribute Values API
  slug: bigcommerce-attribute-values-api
- description: The Attributes API from BigCommerce — 1 operation(s) for attributes.
  name: BigCommerce Attributes API
  slug: bigcommerce-attributes-api
- description: The Banners API from BigCommerce — 3 operation(s) for banners.
  name: BigCommerce Banners API
  slug: bigcommerce-banners-api
- description: The Batch Metafields API from BigCommerce — 7 operation(s) for batch metafields.
  name: BigCommerce Batch Metafields API
  slug: bigcommerce-batch-metafields-api
- description: The Blog Posts API from BigCommerce — 3 operation(s) for blog posts.
  name: BigCommerce Blog Posts API
  slug: bigcommerce-blog-posts-api
- description: The Blog Tags API from BigCommerce — 1 operation(s) for blog tags.
  name: BigCommerce Blog Tags API
  slug: bigcommerce-blog-tags-api
- description: The Brands API from BigCommerce — 2 operation(s) for brands.
  name: BigCommerce Brands API
  slug: bigcommerce-brands-api
- description: The Bulk Pricing Rules API from BigCommerce — 1 operation(s) for bulk pricing rules.
  name: BigCommerce Bulk Pricing Rules API
  slug: bigcommerce-bulk-pricing-rules-api
- description: The Cart API from BigCommerce — 2 operation(s) for cart.
  name: BigCommerce Cart API
  slug: bigcommerce-cart-api
- description: The Cart Currency API from BigCommerce — 1 operation(s) for cart currency.
  name: BigCommerce Cart Currency API
  slug: bigcommerce-cart-currency-api
- description: The Cart Items API from BigCommerce — 2 operation(s) for cart items.
  name: BigCommerce Cart Items API
  slug: bigcommerce-cart-items-api
- description: The Carts (Single) API from BigCommerce — 2 operation(s) for carts (single).
  name: BigCommerce Carts (Single) API
  slug: bigcommerce-carts-single-api
- description: The Catalog API from BigCommerce — 1 operation(s) for catalog.
  name: BigCommerce Catalog API
  slug: bigcommerce-catalog-api
- description: The Categories API from BigCommerce — 1 operation(s) for categories.
  name: BigCommerce Categories API
  slug: bigcommerce-categories-api
- description: The Categories (Deprecated) API from BigCommerce — 2 operation(s) for categories (deprecated).
  name: BigCommerce Categories (Deprecated) API
  slug: bigcommerce-categories-deprecated-api
- description: The Category Assignments API from BigCommerce — 1 operation(s) for category assignments.
  name: BigCommerce Category Assignments API
  slug: bigcommerce-category-assignments-api
- description: The Category Trees API from BigCommerce — 2 operation(s) for category trees.
  name: BigCommerce Category Trees API
  slug: bigcommerce-category-trees-api
- description: The Channel Assignments API from BigCommerce — 1 operation(s) for channel assignments.
  name: BigCommerce Channel Assignments API
  slug: bigcommerce-channel-assignments-api
- description: The Channel Settings API from BigCommerce — 1 operation(s) for channel settings.
  name: BigCommerce Channel Settings API
  slug: bigcommerce-channel-settings-api
- description: The Channels API from BigCommerce — 2 operation(s) for channels.
  name: BigCommerce Channels API
  slug: bigcommerce-channels-api
- description: The Checkout API from BigCommerce — 1 operation(s) for checkout.
  name: BigCommerce Checkout API
  slug: bigcommerce-checkout-api
- description: The Checkout Billing Address API from BigCommerce — 2 operation(s) for checkout billing address.
  name: BigCommerce Checkout Billing Address API
  slug: bigcommerce-checkout-billing-address-api
- description: The Checkout Cart Items API from BigCommerce — 1 operation(s) for checkout cart items.
  name: BigCommerce Checkout Cart Items API
  slug: bigcommerce-checkout-cart-items-api
- description: The Checkout Consignments API from BigCommerce — 2 operation(s) for checkout consignments.
  name: BigCommerce Checkout Consignments API
  slug: bigcommerce-checkout-consignments-api
- description: The Checkout Coupons API from BigCommerce — 2 operation(s) for checkout coupons.
  name: BigCommerce Checkout Coupons API
  slug: bigcommerce-checkout-coupons-api
- description: The Checkout Discounts API from BigCommerce — 1 operation(s) for checkout discounts.
  name: BigCommerce Checkout Discounts API
  slug: bigcommerce-checkout-discounts-api
- description: The Checkout Gift Certificates API from BigCommerce — 2 operation(s) for checkout gift certificates.
  name: BigCommerce Checkout Gift Certificates API
  slug: bigcommerce-checkout-gift-certificates-api
- description: The Checkout Orders API from BigCommerce — 1 operation(s) for checkout orders.
  name: BigCommerce Checkout Orders API
  slug: bigcommerce-checkout-orders-api
- description: The Checkout Settings API from BigCommerce — 1 operation(s) for checkout settings.
  name: BigCommerce Checkout Settings API
  slug: bigcommerce-checkout-settings-api
- description: The Checkout Spam Protection API from BigCommerce — 1 operation(s) for checkout spam protection.
  name: BigCommerce Checkout Spam Protection API
  slug: bigcommerce-checkout-spam-protection-api
- description: The Checkout Store Credit API from BigCommerce — 1 operation(s) for checkout store credit.
  name: BigCommerce Checkout Store Credit API
  slug: bigcommerce-checkout-store-credit-api
- description: The Checkout Token API from BigCommerce — 1 operation(s) for checkout token.
  name: BigCommerce Checkout Token API
  slug: bigcommerce-checkout-token-api
- description: The Complex Rules API from BigCommerce — 2 operation(s) for complex rules.
  name: BigCommerce Complex Rules API
  slug: bigcommerce-complex-rules-api
- description: The Consent API from BigCommerce — 2 operation(s) for consent.
  name: BigCommerce Consent API
  slug: bigcommerce-consent-api
- description: The Countries API from BigCommerce — 3 operation(s) for countries.
  name: BigCommerce Countries API
  slug: bigcommerce-countries-api
- description: The Coupons API from BigCommerce — 3 operation(s) for coupons.
  name: BigCommerce Coupons API
  slug: bigcommerce-coupons-api
- description: The Currencies (Bulk) API from BigCommerce — 1 operation(s) for currencies (bulk).
  name: BigCommerce Currencies (Bulk) API
  slug: bigcommerce-currencies-bulk-api
- description: The Currencies (Single) API from BigCommerce — 1 operation(s) for currencies (single).
  name: BigCommerce Currencies (Single) API
  slug: bigcommerce-currencies-single-api
- description: The Currency Assignments API from BigCommerce — 2 operation(s) for currency assignments.
  name: BigCommerce Currency Assignments API
  slug: bigcommerce-currency-assignments-api
- description: The Current Customers API from BigCommerce — 1 operation(s) for current customers.
  name: BigCommerce Current Customers API
  slug: bigcommerce-current-customers-api
- description: The Custom Fields API from BigCommerce — 2 operation(s) for custom fields.
  name: BigCommerce Custom Fields API
  slug: bigcommerce-custom-fields-api
- description: The Custom Template Associations API from BigCommerce — 1 operation(s) for custom template associations.
  name: BigCommerce Custom Template Associations API
  slug: bigcommerce-custom-template-associations-api
- description: The Customer Batch Metafields API from BigCommerce — 1 operation(s) for customer batch metafields.
  name: BigCommerce Customer Batch Metafields API
  slug: bigcommerce-customer-batch-metafields-api
- description: The Customer Impersonation Token API from BigCommerce — 1 operation(s) for customer impersonation token.
  name: BigCommerce Customer Impersonation Token API
  slug: bigcommerce-customer-impersonation-token-api
- description: The Customer Metafields API from BigCommerce — 2 operation(s) for customer metafields.
  name: BigCommerce Customer Metafields API
  slug: bigcommerce-customer-metafields-api
- description: The Customers API from BigCommerce — 1 operation(s) for customers.
  name: BigCommerce Customers API
  slug: bigcommerce-customers-api
- description: The Customs Information API from BigCommerce — 1 operation(s) for customs information.
  name: BigCommerce Customs Information API
  slug: bigcommerce-customs-information-api
- description: The Email Statuses API from BigCommerce — 1 operation(s) for email statuses.
  name: BigCommerce Email Statuses API
  slug: bigcommerce-email-statuses-api
- description: The Email Templates API from BigCommerce — 2 operation(s) for email templates.
  name: BigCommerce Email Templates API
  slug: bigcommerce-email-templates-api
- description: The Favicon Image API from BigCommerce — 1 operation(s) for favicon image.
  name: BigCommerce Favicon Image API
  slug: bigcommerce-favicon-image-api
- description: The Form Field Values API from BigCommerce — 1 operation(s) for form field values.
  name: BigCommerce Form Field Values API
  slug: bigcommerce-form-field-values-api
- description: The Form Fields API from BigCommerce — 1 operation(s) for form fields.
  name: BigCommerce Form Fields API
  slug: bigcommerce-form-fields-api
- description: The Gift Certificates API from BigCommerce — 2 operation(s) for gift certificates.
  name: BigCommerce Gift Certificates API
  slug: bigcommerce-gift-certificates-api
- description: The Global Settings API from BigCommerce — 1 operation(s) for global settings.
  name: BigCommerce Global Settings API
  slug: bigcommerce-global-settings-api
- description: The Images API from BigCommerce — 6 operation(s) for images.
  name: BigCommerce Images API
  slug: bigcommerce-images-api
- description: The Import-Export API from BigCommerce — 6 operation(s) for import-export.
  name: BigCommerce Import-Export API
  slug: bigcommerce-import-export-api
- description: The Inventory API from BigCommerce — 1 operation(s) for inventory.
  name: BigCommerce Inventory API
  slug: bigcommerce-inventory-api
- description: The Inventory Notifications API from BigCommerce — 1 operation(s) for inventory notifications.
  name: BigCommerce Inventory Notifications API
  slug: bigcommerce-inventory-notifications-api
- description: The Items API from BigCommerce — 2 operation(s) for items.
  name: BigCommerce Items API
  slug: bigcommerce-items-api
- description: The Listings API from BigCommerce — 2 operation(s) for listings.
  name: BigCommerce Listings API
  slug: bigcommerce-listings-api
- description: The Login Token API from BigCommerce — 1 operation(s) for login token.
  name: BigCommerce Login Token API
  slug: bigcommerce-login-token-api
- description: The Logo API from BigCommerce — 1 operation(s) for logo.
  name: BigCommerce Logo API
  slug: bigcommerce-logo-api
- description: The Logo Image API from BigCommerce — 1 operation(s) for logo image.
  name: BigCommerce Logo Image API
  slug: bigcommerce-logo-image-api
- description: The Manage Webhooks (Bulk) API from BigCommerce — 1 operation(s) for manage webhooks (bulk).
  name: BigCommerce Manage Webhooks (Bulk) API
  slug: bigcommerce-manage-webhooks-bulk-api
- description: The Manage Webhooks (Single) API from BigCommerce — 1 operation(s) for manage webhooks (single).
  name: BigCommerce Manage Webhooks (Single) API
  slug: bigcommerce-manage-webhooks-single-api
- description: The Menus API from BigCommerce — 1 operation(s) for menus.
  name: BigCommerce Menus API
  slug: bigcommerce-menus-api
- description: The Metafields API from BigCommerce — 14 operation(s) for metafields.
  name: BigCommerce Metafields API
  slug: bigcommerce-metafields-api
- description: The Methods API from BigCommerce — 1 operation(s) for methods.
  name: BigCommerce Methods API
  slug: bigcommerce-methods-api
- description: The Methods (Deprecated) API from BigCommerce — 1 operation(s) for methods (deprecated).
  name: BigCommerce Methods (Deprecated) API
  slug: bigcommerce-methods-deprecated-api
- description: The Order API from BigCommerce — 1 operation(s) for order.
  name: BigCommerce Order API
  slug: bigcommerce-order-api
- description: The Order Settings API from BigCommerce — 2 operation(s) for order settings.
  name: BigCommerce Order Settings API
  slug: bigcommerce-order-settings-api
- description: The Pages API from BigCommerce — 2 operation(s) for pages.
  name: BigCommerce Pages API
  slug: bigcommerce-pages-api
- description: The Pages (Bulk) API from BigCommerce — 1 operation(s) for pages (bulk).
  name: BigCommerce Pages (Bulk) API
  slug: bigcommerce-pages-bulk-api
- description: The Pages (Single) API from BigCommerce — 1 operation(s) for pages (single).
  name: BigCommerce Pages (Single) API
  slug: bigcommerce-pages-single-api
- description: The Payment Actions API from BigCommerce — 7 operation(s) for payment actions.
  name: BigCommerce Payment Actions API
  slug: bigcommerce-payment-actions-api
- description: The Payments API from BigCommerce — 2 operation(s) for payments.
  name: BigCommerce Payments API
  slug: bigcommerce-payments-api
- description: BigCommerce Placements API Definition.
  name: BigCommerce Placement API
  slug: bigcommerce-placement-api
- description: The Price Lists API from BigCommerce — 2 operation(s) for price lists.
  name: BigCommerce Price Lists API
  slug: bigcommerce-price-lists-api
- description: The Price Lists Assignments API from BigCommerce — 2 operation(s) for price lists assignments.
  name: BigCommerce Price Lists Assignments API
  slug: bigcommerce-price-lists-assignments-api
- description: The Price Lists Records API from BigCommerce — 4 operation(s) for price lists records.
  name: BigCommerce Price Lists Records API
  slug: bigcommerce-price-lists-records-api
- description: The Processing API from BigCommerce — 1 operation(s) for processing.
  name: BigCommerce Processing API
  slug: bigcommerce-processing-api
- description: The Product Modifiers API from BigCommerce — 2 operation(s) for product modifiers.
  name: BigCommerce Product Modifiers API
  slug: bigcommerce-product-modifiers-api
- description: The Product Tax Properties API from BigCommerce — 1 operation(s) for product tax properties.
  name: BigCommerce Product Tax Properties API
  slug: bigcommerce-product-tax-properties-api
- description: The Product Variant Options API from BigCommerce — 2 operation(s) for product variant options.
  name: BigCommerce Product Variant Options API
  slug: bigcommerce-product-variant-options-api
- description: The Product Variants API from BigCommerce — 2 operation(s) for product variants.
  name: BigCommerce Product Variants API
  slug: bigcommerce-product-variants-api
- description: The Products API from BigCommerce — 3 operation(s) for products.
  name: BigCommerce Products API
  slug: bigcommerce-products-api
- description: The Redirects API from BigCommerce — 4 operation(s) for redirects.
  name: BigCommerce Redirects API
  slug: bigcommerce-redirects-api
- description: The Redirects - Cart Redirect URLs API from BigCommerce — 1 operation(s) for redirects - cart redirect urls.
  name: BigCommerce Redirects - Cart Redirect URLs API
  slug: bigcommerce-redirects-cart-redirect-urls-api
- description: The Regions API from BigCommerce — 1 operation(s) for regions.
  name: BigCommerce Regions API
  slug: bigcommerce-regions-api
- description: The Reviews API from BigCommerce — 2 operation(s) for reviews.
  name: BigCommerce Reviews API
  slug: bigcommerce-reviews-api
- description: The Scripts API from BigCommerce — 2 operation(s) for scripts.
  name: BigCommerce Scripts API
  slug: bigcommerce-scripts-api
- description: The Search Filters API from BigCommerce — 3 operation(s) for search filters.
  name: BigCommerce Search Filters API
  slug: bigcommerce-search-filters-api
- description: The Settings API from BigCommerce — 2 operation(s) for settings.
  name: BigCommerce Settings API
  slug: bigcommerce-settings-api
- description: The Shipping Provider API from BigCommerce — 2 operation(s) for shipping provider.
  name: BigCommerce Shipping Provider API
  slug: bigcommerce-shipping-provider-api
- description: The Site API from BigCommerce — 1 operation(s) for site.
  name: BigCommerce Site API
  slug: bigcommerce-site-api
- description: The Site Certificate API from BigCommerce — 2 operation(s) for site certificate.
  name: BigCommerce Site Certificate API
  slug: bigcommerce-site-certificate-api
- description: The Site Checkout URL API from BigCommerce — 1 operation(s) for site checkout url.
  name: BigCommerce Site Checkout URL API
  slug: bigcommerce-site-checkout-url-api
- description: The Site Routes API from BigCommerce — 2 operation(s) for site routes.
  name: BigCommerce Site Routes API
  slug: bigcommerce-site-routes-api
- description: Enables creation and management of external sites (domains) where shoppers shop. Allows for the correct shopping experience to be delivered and maintained (i.e. redirect URLs, email links) when a shop
  name: BigCommerce Sites API
  slug: bigcommerce-sites-api
- description: The Sort Order API from BigCommerce — 1 operation(s) for sort order.
  name: BigCommerce Sort Order API
  slug: bigcommerce-sort-order-api
- description: The States API from BigCommerce — 5 operation(s) for states.
  name: BigCommerce States API
  slug: bigcommerce-states-api
- description: The Store Information API from BigCommerce — 1 operation(s) for store information.
  name: BigCommerce Store Information API
  slug: bigcommerce-store-information-api
- description: The Store Locale API from BigCommerce — 1 operation(s) for store locale.
  name: BigCommerce Store Locale API
  slug: bigcommerce-store-locale-api
- description: The Store Profile API from BigCommerce — 1 operation(s) for store profile.
  name: BigCommerce Store Profile API
  slug: bigcommerce-store-profile-api
- description: The Stored Instruments API from BigCommerce — 1 operation(s) for stored instruments.
  name: BigCommerce Stored Instruments API
  slug: bigcommerce-stored-instruments-api
- description: The Storefront Category API from BigCommerce — 1 operation(s) for storefront category.
  name: BigCommerce Storefront Category API
  slug: bigcommerce-storefront-category-api
- description: The Storefront Product API from BigCommerce — 1 operation(s) for storefront product.
  name: BigCommerce Storefront Product API
  slug: bigcommerce-storefront-product-api
- description: The Storefront Robotstxt API from BigCommerce — 1 operation(s) for storefront robotstxt.
  name: BigCommerce Storefront Robotstxt API
  slug: bigcommerce-storefront-robotstxt-api
- description: The Storefront Search API from BigCommerce — 1 operation(s) for storefront search.
  name: BigCommerce Storefront Search API
  slug: bigcommerce-storefront-search-api
- description: The Storefront Security API from BigCommerce — 1 operation(s) for storefront security.
  name: BigCommerce Storefront Security API
  slug: bigcommerce-storefront-security-api
- description: The Storefront SEO API from BigCommerce — 1 operation(s) for storefront seo.
  name: BigCommerce Storefront SEO API
  slug: bigcommerce-storefront-seo-api
- description: The Storefront Status API from BigCommerce — 1 operation(s) for storefront status.
  name: BigCommerce Storefront Status API
  slug: bigcommerce-storefront-status-api
- description: BigCommerce Customers API Definition.
  name: BigCommerce Subscribers API
  slug: bigcommerce-subscribers-api
- description: The Subscription API from BigCommerce — 1 operation(s) for subscription.
  name: BigCommerce Subscription API
  slug: bigcommerce-subscription-api
- description: The Summary API from BigCommerce — 1 operation(s) for summary.
  name: BigCommerce Summary API
  slug: bigcommerce-summary-api
- description: The System Logs API from BigCommerce — 1 operation(s) for system logs.
  name: BigCommerce System Logs API
  slug: bigcommerce-system-logs-api
- description: The Tax Properties API from BigCommerce — 1 operation(s) for tax properties.
  name: BigCommerce Tax Properties API
  slug: bigcommerce-tax-properties-api
- description: The Tax Provider API from BigCommerce — 4 operation(s) for tax provider.
  name: BigCommerce Tax Provider API
  slug: bigcommerce-tax-provider-api
- description: The Tax Provider Connection API from BigCommerce — 1 operation(s) for tax provider connection.
  name: BigCommerce Tax Provider Connection API
  slug: bigcommerce-tax-provider-connection-api
- description: The Tax Rates API from BigCommerce — 1 operation(s) for tax rates.
  name: BigCommerce Tax Rates API
  slug: bigcommerce-tax-rates-api
- description: The Tax Settings API from BigCommerce — 1 operation(s) for tax settings.
  name: BigCommerce Tax Settings API
  slug: bigcommerce-tax-settings-api
- description: The Tax Zone Check API from BigCommerce — 1 operation(s) for tax zone check.
  name: BigCommerce Tax Zone Check API
  slug: bigcommerce-tax-zone-check-api
- description: The Tax Zones API from BigCommerce — 1 operation(s) for tax zones.
  name: BigCommerce Tax Zones API
  slug: bigcommerce-tax-zones-api
- description: The Taxes API from BigCommerce — 2 operation(s) for taxes.
  name: BigCommerce Taxes API
  slug: bigcommerce-taxes-api
- description: The Template Settings API from BigCommerce — 1 operation(s) for template settings.
  name: BigCommerce Template Settings API
  slug: bigcommerce-template-settings-api
- description: The Theme Actions API from BigCommerce — 2 operation(s) for theme actions.
  name: BigCommerce Theme Actions API
  slug: bigcommerce-theme-actions-api
- description: The Theme Configurations API from BigCommerce — 2 operation(s) for theme configurations.
  name: BigCommerce Theme Configurations API
  slug: bigcommerce-theme-configurations-api
- description: The Theme Custom Templates API from BigCommerce — 1 operation(s) for theme custom templates.
  name: BigCommerce Theme Custom Templates API
  slug: bigcommerce-theme-custom-templates-api
- description: The Theme Jobs API from BigCommerce — 1 operation(s) for theme jobs.
  name: BigCommerce Theme Jobs API
  slug: bigcommerce-theme-jobs-api
- description: The Themes API from BigCommerce — 2 operation(s) for themes.
  name: BigCommerce Themes API
  slug: bigcommerce-themes-api
- description: The Time Zone API from BigCommerce — 1 operation(s) for time zone.
  name: BigCommerce Time Zone API
  slug: bigcommerce-time-zone-api
- description: The Tokens API from BigCommerce — 1 operation(s) for tokens.
  name: BigCommerce Tokens API
  slug: bigcommerce-tokens-api
- description: The Transactions API from BigCommerce — 1 operation(s) for transactions.
  name: BigCommerce Transactions API
  slug: bigcommerce-transactions-api
- description: The Units of Measurement API from BigCommerce — 1 operation(s) for units of measurement.
  name: BigCommerce Units of Measurement API
  slug: bigcommerce-units-of-measurement-api
- description: The Validate Credentials API from BigCommerce — 1 operation(s) for validate credentials.
  name: BigCommerce Validate Credentials API
  slug: bigcommerce-validate-credentials-api
- description: The Values API from BigCommerce — 4 operation(s) for values.
  name: BigCommerce Values API
  slug: bigcommerce-values-api
- description: The Variants (Batch) API from BigCommerce — 1 operation(s) for variants (batch).
  name: BigCommerce Variants (Batch) API
  slug: bigcommerce-variants-batch-api
- description: The Videos API from BigCommerce — 2 operation(s) for videos.
  name: BigCommerce Videos API
  slug: bigcommerce-videos-api
- description: The Webhook Events API from BigCommerce — 1 operation(s) for webhook events.
  name: BigCommerce Webhook Events API
  slug: bigcommerce-webhook-events-api
- description: The Webhooks Admin API from BigCommerce — 1 operation(s) for webhooks admin.
  name: BigCommerce Webhooks Admin API
  slug: bigcommerce-webhooks-admin-api
- description: The Widget API from BigCommerce — 2 operation(s) for widget.
  name: BigCommerce Widget API
  slug: bigcommerce-widget-api
- description: BigCommerce Widget Templates API Definition.
  name: BigCommerce Widget Template API
  slug: bigcommerce-widget-template-api
- description: The Wishlists API from BigCommerce — 2 operation(s) for wishlists.
  name: BigCommerce Wishlists API
  slug: bigcommerce-wishlists-api
- description: The Wishlists Items API from BigCommerce — 2 operation(s) for wishlists items.
  name: BigCommerce Wishlists Items API
  slug: bigcommerce-wishlists-items-api
artifact_total: 1333
asyncapis:
- description: AsyncAPI description of BigCommerce's outbound webhook surface. BigCommerce delivers near real-time event notifications by issuing HTTP POST requests with a JSON body to a customer-configured destinat
  name: BigCommerce Webhooks
  slug: bigcommerce-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BigCommerce Accepted Payment Methods
  slug: open-accepted-payment-methods
- collection_type: open
  name: BigCommerce Abandoned Cart Emails API
  slug: open-bigcommerce-abandoned-cart-emails-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Abandoned Cart Settings API
  slug: open-bigcommerce-abandoned-cart-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Abandoned Carts API
  slug: open-bigcommerce-abandoned-carts-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Abandoned Carts Settings API
  slug: open-bigcommerce-abandoned-carts-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Access API
  slug: open-bigcommerce-access-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Active Theme API
  slug: open-bigcommerce-active-theme-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Addresses API
  slug: open-bigcommerce-addresses-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Analytics API
  slug: open-bigcommerce-analytics-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails API Token API
  slug: open-bigcommerce-api-token-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Attribute Values API
  slug: open-bigcommerce-attribute-values-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Attributes API
  slug: open-bigcommerce-attributes-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Banners API
  slug: open-bigcommerce-banners-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Batch Metafields API
  slug: open-bigcommerce-batch-metafields-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Blog Posts API
  slug: open-bigcommerce-blog-posts-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Blog Tags API
  slug: open-bigcommerce-blog-tags-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Brands API
  slug: open-bigcommerce-brands-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Bulk Pricing Rules API
  slug: open-bigcommerce-bulk-pricing-rules-api
- collection_type: open
  name: BigCommerce Abandoned Emails Cart API
  slug: open-bigcommerce-cart-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Cart Currency API
  slug: open-bigcommerce-cart-currency-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Cart Items API
  slug: open-bigcommerce-cart-items-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Carts (Single) API
  slug: open-bigcommerce-carts-single-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Catalog API
  slug: open-bigcommerce-catalog-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Categories API
  slug: open-bigcommerce-categories-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Categories (Deprecated) API
  slug: open-bigcommerce-categories-deprecated-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Category Assignments API
  slug: open-bigcommerce-category-assignments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Category Trees API
  slug: open-bigcommerce-category-trees-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Channel Assignments API
  slug: open-bigcommerce-channel-assignments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Channel Settings API
  slug: open-bigcommerce-channel-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Channels API
  slug: open-bigcommerce-channels-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout API
  slug: open-bigcommerce-checkout-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Billing Address API
  slug: open-bigcommerce-checkout-billing-address-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Cart Items API
  slug: open-bigcommerce-checkout-cart-items-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Consignments API
  slug: open-bigcommerce-checkout-consignments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Coupons API
  slug: open-bigcommerce-checkout-coupons-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Discounts API
  slug: open-bigcommerce-checkout-discounts-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Gift Certificates API
  slug: open-bigcommerce-checkout-gift-certificates-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Orders API
  slug: open-bigcommerce-checkout-orders-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Settings API
  slug: open-bigcommerce-checkout-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Spam Protection API
  slug: open-bigcommerce-checkout-spam-protection-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Store Credit API
  slug: open-bigcommerce-checkout-store-credit-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Checkout Token API
  slug: open-bigcommerce-checkout-token-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Complex Rules API
  slug: open-bigcommerce-complex-rules-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Consent API
  slug: open-bigcommerce-consent-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Countries API
  slug: open-bigcommerce-countries-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Coupons API
  slug: open-bigcommerce-coupons-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Currencies (Bulk) API
  slug: open-bigcommerce-currencies-bulk-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Currencies (Single) API
  slug: open-bigcommerce-currencies-single-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Currency Assignments API
  slug: open-bigcommerce-currency-assignments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Current Customers API
  slug: open-bigcommerce-current-customers-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Custom Fields API
  slug: open-bigcommerce-custom-fields-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Custom Template Associations API
  slug: open-bigcommerce-custom-template-associations-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Customer Batch Metafields API
  slug: open-bigcommerce-customer-batch-metafields-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Customer Impersonation Token API
  slug: open-bigcommerce-customer-impersonation-token-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Customer Metafields API
  slug: open-bigcommerce-customer-metafields-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Customers API
  slug: open-bigcommerce-customers-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Customs Information API
  slug: open-bigcommerce-customs-information-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Email Statuses API
  slug: open-bigcommerce-email-statuses-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Email Templates API
  slug: open-bigcommerce-email-templates-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Favicon Image API
  slug: open-bigcommerce-favicon-image-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Form Field Values API
  slug: open-bigcommerce-form-field-values-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Form Fields API
  slug: open-bigcommerce-form-fields-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Gift Certificates API
  slug: open-bigcommerce-gift-certificates-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Global Settings API
  slug: open-bigcommerce-global-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Images API
  slug: open-bigcommerce-images-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Import-Export API
  slug: open-bigcommerce-import-export-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Inventory API
  slug: open-bigcommerce-inventory-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Inventory Notifications API
  slug: open-bigcommerce-inventory-notifications-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Items API
  slug: open-bigcommerce-items-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Listings API
  slug: open-bigcommerce-listings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Login Token API
  slug: open-bigcommerce-login-token-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Logo API
  slug: open-bigcommerce-logo-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Logo Image API
  slug: open-bigcommerce-logo-image-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Manage Webhooks (Bulk) API
  slug: open-bigcommerce-manage-webhooks-bulk-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Manage Webhooks (Single) API
  slug: open-bigcommerce-manage-webhooks-single-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Menus API
  slug: open-bigcommerce-menus-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Metafields API
  slug: open-bigcommerce-metafields-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Methods API
  slug: open-bigcommerce-methods-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Methods (Deprecated) API
  slug: open-bigcommerce-methods-deprecated-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Order API
  slug: open-bigcommerce-order-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Order Settings API
  slug: open-bigcommerce-order-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Pages API
  slug: open-bigcommerce-pages-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Pages (Bulk) API
  slug: open-bigcommerce-pages-bulk-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Pages (Single) API
  slug: open-bigcommerce-pages-single-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Payment Actions API
  slug: open-bigcommerce-payment-actions-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Payments API
  slug: open-bigcommerce-payments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Placement API
  slug: open-bigcommerce-placement-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Price Lists API
  slug: open-bigcommerce-price-lists-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Price Lists Assignments API
  slug: open-bigcommerce-price-lists-assignments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Price Lists Records API
  slug: open-bigcommerce-price-lists-records-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Processing API
  slug: open-bigcommerce-processing-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Product Modifiers API
  slug: open-bigcommerce-product-modifiers-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Product Tax Properties API
  slug: open-bigcommerce-product-tax-properties-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Product Variant Options API
  slug: open-bigcommerce-product-variant-options-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Product Variants API
  slug: open-bigcommerce-product-variants-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Products API
  slug: open-bigcommerce-products-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Redirects API
  slug: open-bigcommerce-redirects-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Redirects - Cart Redirect URLs API
  slug: open-bigcommerce-redirects-cart-redirect-urls-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Regions API
  slug: open-bigcommerce-regions-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Scripts API
  slug: open-bigcommerce-scripts-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Search Filters API
  slug: open-bigcommerce-search-filters-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Settings API
  slug: open-bigcommerce-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Shipping Provider API
  slug: open-bigcommerce-shipping-provider-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Site API
  slug: open-bigcommerce-site-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Site Certificate API
  slug: open-bigcommerce-site-certificate-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Site Checkout URL API
  slug: open-bigcommerce-site-checkout-url-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Site Routes API
  slug: open-bigcommerce-site-routes-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Sites API
  slug: open-bigcommerce-sites-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Sort Order API
  slug: open-bigcommerce-sort-order-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails States API
  slug: open-bigcommerce-states-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Store Information API
  slug: open-bigcommerce-store-information-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Store Locale API
  slug: open-bigcommerce-store-locale-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Store Profile API
  slug: open-bigcommerce-store-profile-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Stored Instruments API
  slug: open-bigcommerce-stored-instruments-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront Category API
  slug: open-bigcommerce-storefront-category-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront Product API
  slug: open-bigcommerce-storefront-product-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront Robotstxt API
  slug: open-bigcommerce-storefront-robotstxt-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront Search API
  slug: open-bigcommerce-storefront-search-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront Security API
  slug: open-bigcommerce-storefront-security-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront SEO API
  slug: open-bigcommerce-storefront-seo-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Storefront Status API
  slug: open-bigcommerce-storefront-status-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Subscribers API
  slug: open-bigcommerce-subscribers-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Subscription API
  slug: open-bigcommerce-subscription-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Summary API
  slug: open-bigcommerce-summary-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails System Logs API
  slug: open-bigcommerce-system-logs-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Properties API
  slug: open-bigcommerce-tax-properties-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Provider API
  slug: open-bigcommerce-tax-provider-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Provider Connection API
  slug: open-bigcommerce-tax-provider-connection-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Rates API
  slug: open-bigcommerce-tax-rates-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Settings API
  slug: open-bigcommerce-tax-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Zone Check API
  slug: open-bigcommerce-tax-zone-check-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tax Zones API
  slug: open-bigcommerce-tax-zones-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Taxes API
  slug: open-bigcommerce-taxes-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Template Settings API
  slug: open-bigcommerce-template-settings-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Theme Actions API
  slug: open-bigcommerce-theme-actions-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Theme Configurations API
  slug: open-bigcommerce-theme-configurations-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Theme Custom Templates API
  slug: open-bigcommerce-theme-custom-templates-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Theme Jobs API
  slug: open-bigcommerce-theme-jobs-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Themes API
  slug: open-bigcommerce-themes-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Time Zone API
  slug: open-bigcommerce-time-zone-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Tokens API
  slug: open-bigcommerce-tokens-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Transactions API
  slug: open-bigcommerce-transactions-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Units of Measurement API
  slug: open-bigcommerce-units-of-measurement-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Validate Credentials API
  slug: open-bigcommerce-validate-credentials-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Values API
  slug: open-bigcommerce-values-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Variants (Batch) API
  slug: open-bigcommerce-variants-batch-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Videos API
  slug: open-bigcommerce-videos-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Webhook Events API
  slug: open-bigcommerce-webhook-events-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Webhooks Admin API
  slug: open-bigcommerce-webhooks-admin-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Widget API
  slug: open-bigcommerce-widget-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Widget Template API
  slug: open-bigcommerce-widget-template-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Wishlists API
  slug: open-bigcommerce-wishlists-api
- collection_type: open
  name: BigCommerce Abandoned Cart Emails Wishlists Items API
  slug: open-bigcommerce-wishlists-items-api
- collection_type: open
  name: BigCommerce Payment Access Token
  slug: open-payment-access-token
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigcommerce-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bigcommerce-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigcommerce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigcommerce-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigcommerce
- group: start
  title: ''
  type: Portal
  url: https://developer.bigcommerce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bigcommerce.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bigcommerce.com/docs/start
- group: auth
  title: ''
  type: Authentication
  url: https://developer.bigcommerce.com/docs/start/authentication/api-accounts
- group: design
  title: ''
  type: Webhooks
  url: https://developer.bigcommerce.com/docs/integrations/webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigcommerce
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bigcommerce/refs/heads/main/rules/bigcommerce-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bigcommerce/refs/heads/main/vocabulary/bigcommerce-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.bigcommerce.com/rss.xml
created: '2023-11-21'
description: BigCommerce is a leading e-commerce platform providing APIs for building and managing online stores, products, catalogs, orders, customers, checkouts, payments, and shipping. BigCommerce powers tens of thousands of online stores with its open SaaS architecture.
examples:
- key_count: 6
  name: Bigcommerce Addcartlineitem Example
  slug: bigcommerce-addcartlineitem-example
- key_count: 6
  name: Bigcommerce Addcartlineitems Example
  slug: bigcommerce-addcartlineitems-example
- key_count: 6
  name: Bigcommerce Addcheckoutbillingaddress Example
  slug: bigcommerce-addcheckoutbillingaddress-example
- key_count: 6
  name: Bigcommerce Addcheckoutconsignment Example
  slug: bigcommerce-addcheckoutconsignment-example
- key_count: 6
  name: Bigcommerce Addcheckoutcoupon Example
  slug: bigcommerce-addcheckoutcoupon-example
- key_count: 6
  name: Bigcommerce Addcheckoutdiscount Example
  slug: bigcommerce-addcheckoutdiscount-example
- key_count: 6
  name: Bigcommerce Addcheckoutgiftcertificate Example
  slug: bigcommerce-addcheckoutgiftcertificate-example
- key_count: 6
  name: Bigcommerce Addwishlistitem Example
  slug: bigcommerce-addwishlistitem-example
- key_count: 6
  name: Bigcommerce Adjusttaxquote Example
  slug: bigcommerce-adjusttaxquote-example
- key_count: 6
  name: Bigcommerce Committaxquote Example
  slug: bigcommerce-committaxquote-example
- key_count: 6
  name: Bigcommerce Createabandonedcartemailtemplate Example
  slug: bigcommerce-createabandonedcartemailtemplate-example
- key_count: 6
  name: Bigcommerce Createbanner Example
  slug: bigcommerce-createbanner-example
- key_count: 6
  name: Bigcommerce Createblogposts Example
  slug: bigcommerce-createblogposts-example
- key_count: 6
  name: Bigcommerce Createbrand Example
  slug: bigcommerce-createbrand-example
- key_count: 6
  name: Bigcommerce Createbrandimage Example
  slug: bigcommerce-createbrandimage-example
- key_count: 6
  name: Bigcommerce Createbrandmetafield Example
  slug: bigcommerce-createbrandmetafield-example
- key_count: 6
  name: Bigcommerce Createcart Example
  slug: bigcommerce-createcart-example
- key_count: 6
  name: Bigcommerce Createcartmetafield Example
  slug: bigcommerce-createcartmetafield-example
- key_count: 6
  name: Bigcommerce Createcategories Example
  slug: bigcommerce-createcategories-example
- key_count: 6
  name: Bigcommerce Createcategoryimage Example
  slug: bigcommerce-createcategoryimage-example
- key_count: 6
  name: Bigcommerce Createcategorymetafield Example
  slug: bigcommerce-createcategorymetafield-example
- key_count: 6
  name: Bigcommerce Createcheckoutconsignment Example
  slug: bigcommerce-createcheckoutconsignment-example
- key_count: 6
  name: Bigcommerce Createcheckouttoken Example
  slug: bigcommerce-createcheckouttoken-example
- key_count: 6
  name: Bigcommerce Createcoupon Example
  slug: bigcommerce-createcoupon-example
- key_count: 6
  name: Bigcommerce Createcustomer Example
  slug: bigcommerce-createcustomer-example
- key_count: 6
  name: Bigcommerce Createcustomers Example
  slug: bigcommerce-createcustomers-example
- key_count: 6
  name: Bigcommerce Createcustomersaddresses Example
  slug: bigcommerce-createcustomersaddresses-example
- key_count: 6
  name: Bigcommerce Creategiftcertificate Example
  slug: bigcommerce-creategiftcertificate-example
- key_count: 6
  name: Bigcommerce Createorder Example
  slug: bigcommerce-createorder-example
- key_count: 6
  name: Bigcommerce Createorderrefund Example
  slug: bigcommerce-createorderrefund-example
- key_count: 6
  name: Bigcommerce Createordersrefundquotes Example
  slug: bigcommerce-createordersrefundquotes-example
- key_count: 6
  name: Bigcommerce Createpage Example
  slug: bigcommerce-createpage-example
- key_count: 6
  name: Bigcommerce Createpages Example
  slug: bigcommerce-createpages-example
- key_count: 6
  name: Bigcommerce Createpaymentaccesstoken Example
  slug: bigcommerce-createpaymentaccesstoken-example
- key_count: 6
  name: Bigcommerce Createpricelist Example
  slug: bigcommerce-createpricelist-example
- key_count: 6
  name: Bigcommerce Createproduct Example
  slug: bigcommerce-createproduct-example
- key_count: 6
  name: Bigcommerce Createproductimage Example
  slug: bigcommerce-createproductimage-example
- key_count: 6
  name: Bigcommerce Createproductmetafield Example
  slug: bigcommerce-createproductmetafield-example
- key_count: 6
  name: Bigcommerce Createproductmodifierimage Example
  slug: bigcommerce-createproductmodifierimage-example
- key_count: 6
  name: Bigcommerce Createproductmodifiervalue Example
  slug: bigcommerce-createproductmodifiervalue-example
- key_count: 6
  name: Bigcommerce Createproductreview Example
  slug: bigcommerce-createproductreview-example
- key_count: 6
  name: Bigcommerce Createproductvariant Example
  slug: bigcommerce-createproductvariant-example
- key_count: 6
  name: Bigcommerce Createproductvariantimage Example
  slug: bigcommerce-createproductvariantimage-example
- key_count: 6
  name: Bigcommerce Createproductvariantmetafield Example
  slug: bigcommerce-createproductvariantmetafield-example
- key_count: 6
  name: Bigcommerce Createproductvariantoption Example
  slug: bigcommerce-createproductvariantoption-example
- key_count: 6
  name: Bigcommerce Createproductvariantoptionvalue Example
  slug: bigcommerce-createproductvariantoptionvalue-example
- key_count: 6
  name: Bigcommerce Createproductvideo Example
  slug: bigcommerce-createproductvideo-example
- key_count: 6
  name: Bigcommerce Createredirect Example
  slug: bigcommerce-createredirect-example
- key_count: 6
  name: Bigcommerce Createscript Example
  slug: bigcommerce-createscript-example
- key_count: 6
  name: Bigcommerce Createtaxrates Example
  slug: bigcommerce-createtaxrates-example
- key_count: 6
  name: Bigcommerce Createtaxzones Example
  slug: bigcommerce-createtaxzones-example
- key_count: 6
  name: Bigcommerce Createwebhooks Example
  slug: bigcommerce-createwebhooks-example
- key_count: 6
  name: Bigcommerce Createwishlist Example
  slug: bigcommerce-createwishlist-example
- key_count: 6
  name: Bigcommerce Deletecartlineitem Example
  slug: bigcommerce-deletecartlineitem-example
- key_count: 6
  name: Bigcommerce Deletecheckoutconsignment Example
  slug: bigcommerce-deletecheckoutconsignment-example
- key_count: 6
  name: Bigcommerce Deletecheckoutcoupon Example
  slug: bigcommerce-deletecheckoutcoupon-example
- key_count: 6
  name: Bigcommerce Deletecheckoutlineitem Example
  slug: bigcommerce-deletecheckoutlineitem-example
- key_count: 6
  name: Bigcommerce Deletepage Example
  slug: bigcommerce-deletepage-example
- key_count: 6
  name: Bigcommerce Deletepages Example
  slug: bigcommerce-deletepages-example
- key_count: 6
  name: Bigcommerce Deletetaxproviderconnection Example
  slug: bigcommerce-deletetaxproviderconnection-example
- key_count: 6
  name: Bigcommerce Deletewishlistitem Example
  slug: bigcommerce-deletewishlistitem-example
- key_count: 6
  name: Bigcommerce Downloadstoretheme Example
  slug: bigcommerce-downloadstoretheme-example
- key_count: 6
  name: Bigcommerce Estimatetaxes Example
  slug: bigcommerce-estimatetaxes-example
- key_count: 6
  name: Bigcommerce Getabandonedcartemailtemplates Example
  slug: bigcommerce-getabandonedcartemailtemplates-example
- key_count: 6
  name: Bigcommerce Getallcategories Example
  slug: bigcommerce-getallcategories-example
- key_count: 6
  name: Bigcommerce Getbanner Example
  slug: bigcommerce-getbanner-example
- key_count: 6
  name: Bigcommerce Getbanners Example
  slug: bigcommerce-getbanners-example
- key_count: 6
  name: Bigcommerce Getbannerscount Example
  slug: bigcommerce-getbannerscount-example
- key_count: 6
  name: Bigcommerce Getblogpost Example
  slug: bigcommerce-getblogpost-example
- key_count: 6
  name: Bigcommerce Getblogposts Example
  slug: bigcommerce-getblogposts-example
- key_count: 6
  name: Bigcommerce Getblogpostscount Example
  slug: bigcommerce-getblogpostscount-example
- key_count: 6
  name: Bigcommerce Getbrand Example
  slug: bigcommerce-getbrand-example
- key_count: 6
  name: Bigcommerce Getbrandmetafield Example
  slug: bigcommerce-getbrandmetafield-example
- key_count: 6
  name: Bigcommerce Getbrandmetafields Example
  slug: bigcommerce-getbrandmetafields-example
- key_count: 6
  name: Bigcommerce Getbrands Example
  slug: bigcommerce-getbrands-example
- key_count: 6
  name: Bigcommerce Getbulkpricingrule Example
  slug: bigcommerce-getbulkpricingrule-example
- key_count: 6
  name: Bigcommerce Getcategories Example
  slug: bigcommerce-getcategories-example
- key_count: 6
  name: Bigcommerce Getcategorymetafield Example
  slug: bigcommerce-getcategorymetafield-example
- key_count: 6
  name: Bigcommerce Getcategorymetafields Example
  slug: bigcommerce-getcategorymetafields-example
- key_count: 6
  name: Bigcommerce Getcategorytree Example
  slug: bigcommerce-getcategorytree-example
- key_count: 6
  name: Bigcommerce Getcategorytrees Example
  slug: bigcommerce-getcategorytrees-example
- key_count: 6
  name: Bigcommerce Getcheckout Example
  slug: bigcommerce-getcheckout-example
- key_count: 6
  name: Bigcommerce Getcheckoutsettings Example
  slug: bigcommerce-getcheckoutsettings-example
- key_count: 6
  name: Bigcommerce Getcoupons Example
  slug: bigcommerce-getcoupons-example
- key_count: 6
  name: Bigcommerce Getcouponscount Example
  slug: bigcommerce-getcouponscount-example
- key_count: 6
  name: Bigcommerce Getcurrentcustomer Example
  slug: bigcommerce-getcurrentcustomer-example
- key_count: 6
  name: Bigcommerce Getcustomerssettings Example
  slug: bigcommerce-getcustomerssettings-example
- key_count: 6
  name: Bigcommerce Getcustomerssettingschannel Example
  slug: bigcommerce-getcustomerssettingschannel-example
- key_count: 6
  name: Bigcommerce Getcustomerstoredinstruments Example
  slug: bigcommerce-getcustomerstoredinstruments-example
- key_count: 6
  name: Bigcommerce Getcustomtemplateassociations Example
  slug: bigcommerce-getcustomtemplateassociations-example
- key_count: 6
  name: Bigcommerce Getdefaultabandonedcartemailtemplate Example
  slug: bigcommerce-getdefaultabandonedcartemailtemplate-example
- key_count: 6
  name: Bigcommerce Getemailtemplate Example
  slug: bigcommerce-getemailtemplate-example
- key_count: 6
  name: Bigcommerce Getemailtemplates Example
  slug: bigcommerce-getemailtemplates-example
- key_count: 6
  name: Bigcommerce Getgiftcertificate Example
  slug: bigcommerce-getgiftcertificate-example
- key_count: 6
  name: Bigcommerce Getgiftcertificates Example
  slug: bigcommerce-getgiftcertificates-example
- key_count: 6
  name: Bigcommerce Getordermetafields Example
  slug: bigcommerce-getordermetafields-example
- key_count: 6
  name: Bigcommerce Getpage Example
  slug: bigcommerce-getpage-example
- key_count: 6
  name: Bigcommerce Getpages Example
  slug: bigcommerce-getpages-example
- key_count: 6
  name: Bigcommerce Getpricelist Example
  slug: bigcommerce-getpricelist-example
- key_count: 6
  name: Bigcommerce Getpricelistrecord Example
  slug: bigcommerce-getpricelistrecord-example
- key_count: 6
  name: Bigcommerce Getpricelistrecords Example
  slug: bigcommerce-getpricelistrecords-example
- key_count: 6
  name: Bigcommerce Getpricelistrecordsbyvariantid Example
  slug: bigcommerce-getpricelistrecordsbyvariantid-example
- key_count: 6
  name: Bigcommerce Getpricelists Example
  slug: bigcommerce-getpricelists-example
- key_count: 6
  name: Bigcommerce Getprices Example
  slug: bigcommerce-getprices-example
- key_count: 6
  name: Bigcommerce Getproduct Example
  slug: bigcommerce-getproduct-example
- key_count: 6
  name: Bigcommerce Getproductcomplexrules Example
  slug: bigcommerce-getproductcomplexrules-example
- key_count: 6
  name: Bigcommerce Getproductimage Example
  slug: bigcommerce-getproductimage-example
- key_count: 6
  name: Bigcommerce Getproductimages Example
  slug: bigcommerce-getproductimages-example
- key_count: 6
  name: Bigcommerce Getproductmetafield Example
  slug: bigcommerce-getproductmetafield-example
- key_count: 6
  name: Bigcommerce Getproductmetafields Example
  slug: bigcommerce-getproductmetafields-example
- key_count: 6
  name: Bigcommerce Getproductmodifiers Example
  slug: bigcommerce-getproductmodifiers-example
- key_count: 6
  name: Bigcommerce Getproductmodifiervalue Example
  slug: bigcommerce-getproductmodifiervalue-example
- key_count: 6
  name: Bigcommerce Getproductmodifiervalues Example
  slug: bigcommerce-getproductmodifiervalues-example
- key_count: 6
  name: Bigcommerce Getproductreview Example
  slug: bigcommerce-getproductreview-example
- key_count: 6
  name: Bigcommerce Getproductvariant Example
  slug: bigcommerce-getproductvariant-example
- key_count: 6
  name: Bigcommerce Getproductvariantmetafield Example
  slug: bigcommerce-getproductvariantmetafield-example
- key_count: 6
  name: Bigcommerce Getproductvariantoptionvalue Example
  slug: bigcommerce-getproductvariantoptionvalue-example
- key_count: 6
  name: Bigcommerce Getproductvariantoptionvalues Example
  slug: bigcommerce-getproductvariantoptionvalues-example
- key_count: 6
  name: Bigcommerce Getproductvariants Example
  slug: bigcommerce-getproductvariants-example
- key_count: 6
  name: Bigcommerce Getproductvideo Example
  slug: bigcommerce-getproductvideo-example
- key_count: 6
  name: Bigcommerce Getproductvideos Example
  slug: bigcommerce-getproductvideos-example
- key_count: 6
  name: Bigcommerce Getredirect Example
  slug: bigcommerce-getredirect-example
- key_count: 6
  name: Bigcommerce Getredirects Example
  slug: bigcommerce-getredirects-example
- key_count: 6
  name: Bigcommerce Getredirectscount Example
  slug: bigcommerce-getredirectscount-example
- key_count: 6
  name: Bigcommerce Getsettingsavailablefilters Example
  slug: bigcommerce-getsettingsavailablefilters-example
- key_count: 6
  name: Bigcommerce Getsettingsemailstatuses Example
  slug: bigcommerce-getsettingsemailstatuses-example
- key_count: 6
  name: Bigcommerce Getsettingsenabledsearchfilters Example
  slug: bigcommerce-getsettingsenabledsearchfilters-example
- key_count: 6
  name: Bigcommerce Getsettingslocale Example
  slug: bigcommerce-getsettingslocale-example
- key_count: 6
  name: Bigcommerce Getsettingsrobotstxt Example
  slug: bigcommerce-getsettingsrobotstxt-example
- key_count: 6
  name: Bigcommerce Getsettingsstorefrontsearch Example
  slug: bigcommerce-getsettingsstorefrontsearch-example
- key_count: 6
  name: Bigcommerce Getsettingsstorefrontseo Example
  slug: bigcommerce-getsettingsstorefrontseo-example
- key_count: 6
  name: Bigcommerce Getsettingsstorefrontstatus Example
  slug: bigcommerce-getsettingsstorefrontstatus-example
- key_count: 6
  name: Bigcommerce Getsiteroute Example
  slug: bigcommerce-getsiteroute-example
- key_count: 6
  name: Bigcommerce Getsiteroutes Example
  slug: bigcommerce-getsiteroutes-example
- key_count: 6
  name: Bigcommerce Getstoreinformation Example
  slug: bigcommerce-getstoreinformation-example
- key_count: 6
  name: Bigcommerce Getstoretheme Example
  slug: bigcommerce-getstoretheme-example
- key_count: 6
  name: Bigcommerce Getstorethemejob Example
  slug: bigcommerce-getstorethemejob-example
- key_count: 6
  name: Bigcommerce Getstorethemes Example
  slug: bigcommerce-getstorethemes-example
- key_count: 6
  name: Bigcommerce Getsystemtimestamp Example
  slug: bigcommerce-getsystemtimestamp-example
- key_count: 6
  name: Bigcommerce Gettaxclass Example
  slug: bigcommerce-gettaxclass-example
- key_count: 6
  name: Bigcommerce Gettaxclasses Example
  slug: bigcommerce-gettaxclasses-example
- key_count: 6
  name: Bigcommerce Gettaxproviderconnection Example
  slug: bigcommerce-gettaxproviderconnection-example
- key_count: 6
  name: Bigcommerce Gettaxzones Example
  slug: bigcommerce-gettaxzones-example
- key_count: 6
  name: Bigcommerce Getthemecustomtemplates Example
  slug: bigcommerce-getthemecustomtemplates-example
- key_count: 6
  name: Bigcommerce Getwishlist Example
  slug: bigcommerce-getwishlist-example
- key_count: 6
  name: Bigcommerce Getwishlists Example
  slug: bigcommerce-getwishlists-example
- key_count: 6
  name: Bigcommerce Paymentspost Example
  slug: bigcommerce-paymentspost-example
- key_count: 6
  name: Bigcommerce Postcookieconsent Example
  slug: bigcommerce-postcookieconsent-example
- key_count: 6
  name: Bigcommerce Requestshippingrates Example
  slug: bigcommerce-requestshippingrates-example
- key_count: 6
  name: Bigcommerce Setpricelistrecord Example
  slug: bigcommerce-setpricelistrecord-example
- key_count: 6
  name: Bigcommerce Updateabandonedcartemailtemplate Example
  slug: bigcommerce-updateabandonedcartemailtemplate-example
- key_count: 6
  name: Bigcommerce Updatebanner Example
  slug: bigcommerce-updatebanner-example
- key_count: 6
  name: Bigcommerce Updateblogpost Example
  slug: bigcommerce-updateblogpost-example
- key_count: 6
  name: Bigcommerce Updatebrand Example
  slug: bigcommerce-updatebrand-example
- key_count: 6
  name: Bigcommerce Updatebrandmetafield Example
  slug: bigcommerce-updatebrandmetafield-example
- key_count: 6
  name: Bigcommerce Updatebulkpricingrule Example
  slug: bigcommerce-updatebulkpricingrule-example
- key_count: 6
  name: Bigcommerce Updatecart Example
  slug: bigcommerce-updatecart-example
- key_count: 6
  name: Bigcommerce Updatecartlineitem Example
  slug: bigcommerce-updatecartlineitem-example
- key_count: 6
  name: Bigcommerce Updatecartmetafield Example
  slug: bigcommerce-updatecartmetafield-example
- key_count: 6
  name: Bigcommerce Updatecategorymetafield Example
  slug: bigcommerce-updatecategorymetafield-example
- key_count: 6
  name: Bigcommerce Updatechannelcartsettings Example
  slug: bigcommerce-updatechannelcartsettings-example
- key_count: 6
  name: Bigcommerce Updatecheckout Example
  slug: bigcommerce-updatecheckout-example
- key_count: 6
  name: Bigcommerce Updatecheckoutbillingaddress Example
  slug: bigcommerce-updatecheckoutbillingaddress-example
- key_count: 6
  name: Bigcommerce Updatecheckoutconsignment Example
  slug: bigcommerce-updatecheckoutconsignment-example
- key_count: 6
  name: Bigcommerce Updatecheckoutlineitem Example
  slug: bigcommerce-updatecheckoutlineitem-example
- key_count: 6
  name: Bigcommerce Updatecheckoutsettings Example
  slug: bigcommerce-updatecheckoutsettings-example
- key_count: 6
  name: Bigcommerce Updatecheckouturl Example
  slug: bigcommerce-updatecheckouturl-example
- key_count: 6
  name: Bigcommerce Updatecoupon Example
  slug: bigcommerce-updatecoupon-example
- key_count: 6
  name: Bigcommerce Updatecustomerformfieldvalues Example
  slug: bigcommerce-updatecustomerformfieldvalues-example
- key_count: 6
  name: Bigcommerce Updatecustomers Example
  slug: bigcommerce-updatecustomers-example
- key_count: 6
  name: Bigcommerce Updatecustomersaddresses Example
  slug: bigcommerce-updatecustomersaddresses-example
- key_count: 6
  name: Bigcommerce Updatecustomerssettings Example
  slug: bigcommerce-updatecustomerssettings-example
- key_count: 6
  name: Bigcommerce Updatecustomerssettingschannel Example
  slug: bigcommerce-updatecustomerssettingschannel-example
- key_count: 6
  name: Bigcommerce Updatecustomsinformation Example
  slug: bigcommerce-updatecustomsinformation-example
- key_count: 6
  name: Bigcommerce Updateemailtemplate Example
  slug: bigcommerce-updateemailtemplate-example
- key_count: 6
  name: Bigcommerce Updategiftcertificate Example
  slug: bigcommerce-updategiftcertificate-example
- key_count: 6
  name: Bigcommerce Updateglobalcartsettings Example
  slug: bigcommerce-updateglobalcartsettings-example
- key_count: 6
  name: Bigcommerce Updatehooksadmin Example
  slug: bigcommerce-updatehooksadmin-example
- key_count: 6
  name: Bigcommerce Updatepage Example
  slug: bigcommerce-updatepage-example
- key_count: 6
  name: Bigcommerce Updatepages Example
  slug: bigcommerce-updatepages-example
- key_count: 6
  name: Bigcommerce Updatepricelist Example
  slug: bigcommerce-updatepricelist-example
- key_count: 6
  name: Bigcommerce Updateproduct Example
  slug: bigcommerce-updateproduct-example
- key_count: 6
  name: Bigcommerce Updateproductimage Example
  slug: bigcommerce-updateproductimage-example
- key_count: 6
  name: Bigcommerce Updateproductmetafield Example
  slug: bigcommerce-updateproductmetafield-example
- key_count: 6
  name: Bigcommerce Updateproductmodifiervalue Example
  slug: bigcommerce-updateproductmodifiervalue-example
- key_count: 6
  name: Bigcommerce Updateproductreview Example
  slug: bigcommerce-updateproductreview-example
- key_count: 6
  name: Bigcommerce Updateproducts Example
  slug: bigcommerce-updateproducts-example
- key_count: 6
  name: Bigcommerce Updateproducttaxproperties Example
  slug: bigcommerce-updateproducttaxproperties-example
- key_count: 6
  name: Bigcommerce Updateproductvariant Example
  slug: bigcommerce-updateproductvariant-example
- key_count: 6
  name: Bigcommerce Updateproductvariantmetafield Example
  slug: bigcommerce-updateproductvariantmetafield-example
- key_count: 6
  name: Bigcommerce Updateproductvariantoption Example
  slug: bigcommerce-updateproductvariantoption-example
- key_count: 6
  name: Bigcommerce Updateproductvariantoptionvalue Example
  slug: bigcommerce-updateproductvariantoptionvalue-example
- key_count: 6
  name: Bigcommerce Updateproductvideo Example
  slug: bigcommerce-updateproductvideo-example
- key_count: 6
  name: Bigcommerce Updateredirect Example
  slug: bigcommerce-updateredirect-example
- key_count: 6
  name: Bigcommerce Updatesettingsemailstatuses Example
  slug: bigcommerce-updatesettingsemailstatuses-example
- key_count: 6
  name: Bigcommerce Updatesettingsenabledsearchfilters Example
  slug: bigcommerce-updatesettingsenabledsearchfilters-example
- key_count: 6
  name: Bigcommerce Updatesettingslocale Example
  slug: bigcommerce-updatesettingslocale-example
- key_count: 6
  name: Bigcommerce Updatesettingsstorefrontsearch Example
  slug: bigcommerce-updatesettingsstorefrontsearch-example
- key_count: 6
  name: Bigcommerce Updatesettingsstorefrontseo Example
  slug: bigcommerce-updatesettingsstorefrontseo-example
- key_count: 6
  name: Bigcommerce Updatesettingsstorefrontstatus Example
  slug: bigcommerce-updatesettingsstorefrontstatus-example
- key_count: 6
  name: Bigcommerce Updatesiteroutes Example
  slug: bigcommerce-updatesiteroutes-example
- key_count: 6
  name: Bigcommerce Updatetaxproviderconnection Example
  slug: bigcommerce-updatetaxproviderconnection-example
- key_count: 6
  name: Bigcommerce Updatetaxrates Example
  slug: bigcommerce-updatetaxrates-example
- key_count: 6
  name: Bigcommerce Updatetaxzones Example
  slug: bigcommerce-updatetaxzones-example
- key_count: 6
  name: Bigcommerce Updatevariantsbatch Example
  slug: bigcommerce-updatevariantsbatch-example
- key_count: 6
  name: Bigcommerce Updatewishlist Example
  slug: bigcommerce-updatewishlist-example
- key_count: 6
  name: Bigcommerce Uploadstoretheme Example
  slug: bigcommerce-uploadstoretheme-example
- key_count: 6
  name: Bigcommerce Upsertcategorytrees Example
  slug: bigcommerce-upsertcategorytrees-example
- key_count: 6
  name: Bigcommerce Upsertcustomersattributevalues Example
  slug: bigcommerce-upsertcustomersattributevalues-example
- key_count: 6
  name: Bigcommerce Upsertcustomtemplateassociations Example
  slug: bigcommerce-upsertcustomtemplateassociations-example
- key_count: 6
  name: Bigcommerce Upsertpricelistrecords Example
  slug: bigcommerce-upsertpricelistrecords-example
- key_count: 6
  name: Bigcommerce Upsertsitecertificate Example
  slug: bigcommerce-upsertsitecertificate-example
- key_count: 6
  name: Bigcommerce Validateconnectionoptions Example
  slug: bigcommerce-validateconnectionoptions-example
- key_count: 6
  name: Bigcommerce Validatecustomercredentials Example
  slug: bigcommerce-validatecustomercredentials-example
features:
- 'Standard $29/mo: up to $50K online revenue, 0% transaction fees'
- 'Plus $79/mo: up to $180K, customer groups, abandoned cart saver'
- 'Pro $299/mo: up to $400K, advanced reporting, priority support'
- 'Enterprise custom: $1M+ revenue, unlimited API, B2B price lists'
- 'All plans: unlimited products, staff, storage, bandwidth'
- 'REST API: 450 req/30s Standard/Plus, 600 Pro, unlimited Enterprise'
- 'Storefront GraphQL: 60 req/min'
- OAuth 2.0 for app authentication
- Webhooks v3 for store event subscriptions
- BigCommerce Channels for multi-storefront
- BigCommerce for WordPress
- Headless commerce with Catalyst (Next.js)
- Multi-Storefront for managing multiple sites
- B2B Edition for wholesale (separate license)
- Advanced multi-currency
- Single-page checkout (customizable on Pro+)
finops:
- name: Bigcommerce Finops
  service_category: E-Commerce
  slug: bigcommerce-finops
graphqls:
- description: ''
  name: BigCommerce GraphQL API
  slug: bigcommerce-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigcommerce.png
integrations:
- description: Accept card payments via Stripe payment gateway integration.
  name: Stripe
- description: Accept PayPal and Venmo payments on BigCommerce storefronts.
  name: PayPal
- description: Sync orders and manage fulfillment with ShipStation.
  name: ShipStation
- description: Sync customer and order data with Salesforce CRM.
  name: Salesforce
- description: Integrate BigCommerce with NetSuite ERP for unified commerce.
  name: NetSuite
- description: Sync customer and order data to Klaviyo for email marketing automation.
  name: Klaviyo
- description: Sync product catalog to Google Shopping for paid and organic visibility.
  name: Google Shopping
json_schemas:
- name: 301RedirectImportExportJobRead
  property_count: 9
  slug: bigcommerce-301redirectimportexportjobread
- name: 301RedirectRead
  property_count: 5
  slug: bigcommerce-301redirectread
- name: 301RedirectUpsert
  property_count: 3
  slug: bigcommerce-301redirectupsert
- name: AbandondedCartEmail
  property_count: 6
  slug: bigcommerce-abandondedcartemail
- name: ''
  property_count: 4
  slug: bigcommerce-abandondedcartemailpayload
- name: AbandonedCartEmailModel
  property_count: 3
  slug: bigcommerce-abandonedcartemailmodel
- name: abandonedCartInfo_Full
  property_count: 1
  slug: bigcommerce-abandonedcartinfo-full
- name: AbandonedCartSettings
  property_count: 1
  slug: bigcommerce-abandonedcartsettings
- name: Activate
  property_count: 2
  slug: bigcommerce-activate
- name: ActiveTheme
  property_count: 4
  slug: bigcommerce-activetheme
- name: address_Base
  property_count: 13
  slug: bigcommerce-address-base
- name: address_Full
  property_count: 15
  slug: bigcommerce-address-full
- name: address_Post
  property_count: 13
  slug: bigcommerce-address-post
- name: address_Put
  property_count: 13
  slug: bigcommerce-address-put
- name: Address
  property_count: 10
  slug: bigcommerce-address
- name: addresses
  property_count: 2
  slug: bigcommerce-addresses
- name: Address Properties
  property_count: 13
  slug: bigcommerce-addressproperties
- name: Address Response
  property_count: 0
  slug: bigcommerce-addressresponse
- name: AddressTypeEnumValues
  property_count: 0
  slug: bigcommerce-addresstypeenumvalues
- name: adjuster_Full
  property_count: 2
  slug: bigcommerce-adjuster-full
- name: adjusters_Full
  property_count: 4
  slug: bigcommerce-adjusters-full
- name: Adjustment Amount
  property_count: 0
  slug: bigcommerce-adjustmentamount
- name: Amount
  property_count: 0
  slug: bigcommerce-amount
- name: Amount Bound Item
  property_count: 5
  slug: bigcommerce-amountbounditem
- name: AnalyticsProvider
  property_count: 4
  slug: bigcommerce-analyticsprovider
- name: AnalyticsProviders
  property_count: 0
  slug: bigcommerce-analyticsproviders
- name: anyTypePage
  property_count: 10
  slug: bigcommerce-anytypepage
- name: Applied Coupon
  property_count: 4
  slug: bigcommerce-appliedcoupon
- name: Applied Discount
  property_count: 2
  slug: bigcommerce-applieddiscount
- name: AssignmentForGetResponse
  property_count: 4
  slug: bigcommerce-assignmentforgetresponse
- name: AssignmentForPutRequest
  property_count: 2
  slug: bigcommerce-assignmentforputrequest
- name: AssignmentForPutResponse
  property_count: 2
  slug: bigcommerce-assignmentforputresponse
- name: AssignmentsForGetResponse
  property_count: 2
  slug: bigcommerce-assignmentsforgetresponse
- name: AssignmentsForRequest
  property_count: 3
  slug: bigcommerce-assignmentsforrequest
- name: attribute_Full
  property_count: 6
  slug: bigcommerce-attribute-full
- name: attribute_Post
  property_count: 2
  slug: bigcommerce-attribute-post
- name: attribute_Put
  property_count: 2
  slug: bigcommerce-attribute-put
- name: attributeValue_Base
  property_count: 4
  slug: bigcommerce-attributevalue-base
- name: Attribute Value
  property_count: 6
  slug: bigcommerce-attributevalue
- name: authentication
  property_count: 3
  slug: bigcommerce-authentication
- name: AvailableFilter
  property_count: 0
  slug: bigcommerce-availablefilter
- name: AvailableNormalFilter
  property_count: 4
  slug: bigcommerce-availablenormalfilter
- name: AvailableOtherFilter
  property_count: 3
  slug: bigcommerce-availableotherfilter
- name: AvailablePriceFilter
  property_count: 5
  slug: bigcommerce-availablepricefilter
- name: AVS Results
  property_count: 4
  slug: bigcommerce-avsresult
- name: Bank Account Instrument
  property_count: 5
  slug: bigcommerce-bankaccountinstrument
- name: banner_Base
  property_count: 9
  slug: bigcommerce-banner-base
- name: banner_Full
  property_count: 0
  slug: bigcommerce-banner-full
- name: banner_Put
  property_count: 0
  slug: bigcommerce-banner-put
- name: BaseError
  property_count: 2
  slug: bigcommerce-baseerror
- name: Base Item
  property_count: 19
  slug: bigcommerce-baseitem
- name: Base Rate Request
  property_count: 6
  slug: bigcommerce-baseoptions
- name: Base Options
  property_count: 3
  slug: bigcommerce-baseoptionsschema
- name: BatchOperationMeta
  property_count: 3
  slug: bigcommerce-batchoperationmeta
- name: beta4DetailedErrors
  property_count: 0
  slug: bigcommerce-beta4detailederrors
- name: beta4ErrorResponse
  property_count: 0
  slug: bigcommerce-beta4errorresponse
- name: beta5DetailedErrors
  property_count: 0
  slug: bigcommerce-beta5detailederrors
- name: beta5ErrorResponse
  property_count: 0
  slug: bigcommerce-beta5errorresponse
- name: betaDetailedErrors
  property_count: 0
  slug: bigcommerce-betadetailederrors
- name: betaErrorResponse
  property_count: 0
  slug: bigcommerce-betaerrorresponse
- name: BigCommerceProtectedAppSections
  property_count: 0
  slug: bigcommerce-bigcommerceprotectedappsections
- name: BillingAddress
  property_count: 12
  slug: bigcommerce-billingaddress
- name: blogPost_Base_Post
  property_count: 10
  slug: bigcommerce-blogpost-base-post
- name: blogPost_Base_Res
  property_count: 13
  slug: bigcommerce-blogpost-base-res
- name: blogPost_Base
  property_count: 13
  slug: bigcommerce-blogpost-base
- name: blogPost_Full
  property_count: 0
  slug: bigcommerce-blogpost-full
- name: blogTags
  property_count: 0
  slug: bigcommerce-blogtags
- name: brand_Full
  property_count: 8
  slug: bigcommerce-brand-full
- name: bulkPricingRule_Full
  property_count: 4
  slug: bigcommerce-bulkpricingrule-full
- name: BulkPricingTier
  property_count: 4
  slug: bigcommerce-bulkpricingtier
- name: callback_category_data
  property_count: 1
  slug: bigcommerce-callback-category-data
- name: Card
  property_count: 9
  slug: bigcommerce-card
- name: Card Instrument
  property_count: 9
  slug: bigcommerce-cardinstrument
- name: Carrier Quote Object
  property_count: 2
  slug: bigcommerce-carrierquoteobject
- name: Cart_Full
  property_count: 17
  slug: bigcommerce-cart-full
- name: Cart_Line_Item_Update_Post
  property_count: 3
  slug: bigcommerce-cart-line-item-update-post
- name: Cart_Line_Item_Update_Put
  property_count: 3
  slug: bigcommerce-cart-line-item-update-put
- name: Custom item
  property_count: 0
  slug: bigcommerce-cart-postcustomitem
- name: Item with modifier
  property_count: 5
  slug: bigcommerce-cart-postmodifier
- name: Item with variant
  property_count: 6
  slug: bigcommerce-cart-postvariant
- name: cart_Put
  property_count: 2
  slug: bigcommerce-cart-put
- name: Cart Coupon
  property_count: 5
  slug: bigcommerce-cartcoupon
- name: Cart Create Post Data
  property_count: 7
  slug: bigcommerce-cartcreatepostdata
- name: cartLineItemGiftCertificate_Put
  property_count: 6
  slug: bigcommerce-cartlineitemgiftcertificate-put
- name: Gift Wrapping Request Data
  property_count: 2
  slug: bigcommerce-cartlineitemgiftwrapping-put
- name: cartLineItemPut
  property_count: 4
  slug: bigcommerce-cartlineitemput
- name: Cart Request Data
  property_count: 3
  slug: bigcommerce-cartrequestdata
- name: CartSettings
  property_count: 1
  slug: bigcommerce-cartsettings
- name: Cart Update Put Request Data
  property_count: 1
  slug: bigcommerce-cartupdateputrequestdata
- name: Cart Update Request
  property_count: 2
  slug: bigcommerce-cartupdaterequest
- name: CatalogSettings
  property_count: 2
  slug: bigcommerce-catalogsettings
- name: categoriesTree_Resp
  property_count: 2
  slug: bigcommerce-categoriestree-resp
- name: categoriesTreeNode_Full
  property_count: 5
  slug: bigcommerce-categoriestreenode-full
- name: category_Full
  property_count: 15
  slug: bigcommerce-category-full
- name: Category ID
  property_count: 0
  slug: bigcommerce-category-id
- name: Category
  property_count: 0
  slug: bigcommerce-category
- name: Category UUID
  property_count: 0
  slug: bigcommerce-category-uuid
- name: categoryAccessLevel
  property_count: 2
  slug: bigcommerce-categoryaccesslevel
- name: Category
  property_count: 11
  slug: bigcommerce-categorybase
- name: CategoryList
  property_count: 2
  slug: bigcommerce-categorylist
- name: CategoryListingModeEnumValues
  property_count: 0
  slug: bigcommerce-categorylistingmodeenumvalues
- name: CategoryNode
  property_count: 7
  slug: bigcommerce-categorynode
- name: CategoryNodeTree
  property_count: 2
  slug: bigcommerce-categorynodetree
- name: CategoryTree
  property_count: 2
  slug: bigcommerce-categorytree
- name: CategoryTreeList
  property_count: 2
  slug: bigcommerce-categorytreelist
- name: CategoryTreeListRequest
  property_count: 0
  slug: bigcommerce-categorytreelistrequest
- name: CertificateResponse
  property_count: 2
  slug: bigcommerce-certificateresponse
- name: CertificateWrite
  property_count: 3
  slug: bigcommerce-certificatewrite
- name: channel_menus_Post
  property_count: 2
  slug: bigcommerce-channel-menus-post
- name: ChannelAbandonedCartSettings
  property_count: 8
  slug: bigcommerce-channelabandonedcartsettings
- name: ChannelAbandonedCartSettingsRequest
  property_count: 0
  slug: bigcommerce-channelabandonedcartsettingsrequest
- name: ChannelAbandonedCartSettingsResponse
  property_count: 2
  slug: bigcommerce-channelabandonedcartsettingsresponse
- name: ChannelCartSettings
  property_count: 1
  slug: bigcommerce-channelcartsettings
- name: ChannelCartSettingsRequest
  property_count: 0
  slug: bigcommerce-channelcartsettingsrequest
- name: ChannelCartSettingsResponse
  property_count: 2
  slug: bigcommerce-channelcartsettingsresponse
- name: ChannelConfigMeta
  property_count: 1
  slug: bigcommerce-channelconfigmeta
- name: ChannelDateCreated
  property_count: 0
  slug: bigcommerce-channeldatecreated
- name: ChannelDateModified
  property_count: 0
  slug: bigcommerce-channeldatemodified
- name: ChannelId
  property_count: 0
  slug: bigcommerce-channelid
- name: ChannelIdForListing
  property_count: 0
  slug: bigcommerce-channelidforlisting
- name: ChannelListingDateCreated
  property_count: 0
  slug: bigcommerce-channellistingdatecreated
- name: ChannelListingDateModified
  property_count: 0
  slug: bigcommerce-channellistingdatemodified
- name: ChannelListingVariantDateCreated
  property_count: 0
  slug: bigcommerce-channellistingvariantdatecreated
- name: ChannelListingVariantDateModified
  property_count: 0
  slug: bigcommerce-channellistingvariantdatemodified
- name: ChannelName
  property_count: 0
  slug: bigcommerce-channelname
- name: ChannelOrderSettings
  property_count: 1
  slug: bigcommerce-channelordersettings
- name: ChannelPlatform
  property_count: 0
  slug: bigcommerce-channelplatform
- name: ChannelProductDescription
  property_count: 0
  slug: bigcommerce-channelproductdescription
- name: ChannelProductMultipleVariants
  property_count: 0
  slug: bigcommerce-channelproductmultiplevariants
- name: ChannelProductName
  property_count: 0
  slug: bigcommerce-channelproductname
- name: ChannelProductVariantDescription
  property_count: 0
  slug: bigcommerce-channelproductvariantdescription
- name: ChannelProductVariantFull
  property_count: 9
  slug: bigcommerce-channelproductvariantfull
- name: ChannelProductVariantName
  property_count: 0
  slug: bigcommerce-channelproductvariantname
- name: ChannelProductVariantPartial
  property_count: 6
  slug: bigcommerce-channelproductvariantpartial
- name: ''
  property_count: 0
  slug: bigcommerce-channelstatus
- name: ChannelType
  property_count: 0
  slug: bigcommerce-channeltype
- name: ChannelWithCurrencies
  property_count: 13
  slug: bigcommerce-channelwithcurrencies
- name: ChannelWithoutCurrencies
  property_count: 12
  slug: bigcommerce-channelwithoutcurrencies
- name: Check Connection Options Request Payload
  property_count: 1
  slug: bigcommerce-checkconnectionoptionsrequestpayload
- name: Check Connection Options Response Payload
  property_count: 2
  slug: bigcommerce-checkconnectionoptionsresponsepayload
- name: checkout_Full
  property_count: 19
  slug: bigcommerce-checkout-full
- name: Checkout_Put
  property_count: 1
  slug: bigcommerce-checkout-put
- name: Checkout
  property_count: 19
  slug: bigcommerce-checkout
- name: checkoutCart
  property_count: 13
  slug: bigcommerce-checkoutcart
- name: Checkout Coupon
  property_count: 5
  slug: bigcommerce-checkoutcoupon
- name: checkoutGiftCertificates
  property_count: 0
  slug: bigcommerce-checkoutgiftcertificates
- name: checkouts_Resp
  property_count: 1
  slug: bigcommerce-checkouts-resp
- name: Checkouts Settings
  property_count: 4
  slug: bigcommerce-checkoutssettings
- name: Checkouts settings request
  property_count: 4
  slug: bigcommerce-checkoutssettingsrequest
- name: checkoutTax
  property_count: 2
  slug: bigcommerce-checkouttax
- name: Collection Meta
  property_count: 1
  slug: bigcommerce-collectionmeta
- name: complexRule_Base
  property_count: 12
  slug: bigcommerce-complexrule-base
- name: complexRuleConditionBase
  property_count: 6
  slug: bigcommerce-complexruleconditionbase
- name: config_Full
  property_count: 24
  slug: bigcommerce-config-full
- name: ConfiguredFilter
  property_count: 0
  slug: bigcommerce-configuredfilter
- name: ConfiguredFilters
  property_count: 0
  slug: bigcommerce-configuredfilters
- name: ConfiguredFiltersOverride
  property_count: 2
  slug: bigcommerce-configuredfiltersoverride
- name: Connection Options Instance
  property_count: 0
  slug: bigcommerce-connectionoptionsinstance
- name: consent_Full
  property_count: 3
  slug: bigcommerce-consent-full
- name: consentAllow
  property_count: 0
  slug: bigcommerce-consentallow
- name: ConsentPreferences
  property_count: 2
  slug: bigcommerce-consentpreferences
- name: consignment_Full
  property_count: 11
  slug: bigcommerce-consignment-full
- name: consignmentAvailableShippingOptions
  property_count: 0
  slug: bigcommerce-consignmentavailableshippingoptions
- name: ConsignmentFormField
  property_count: 2
  slug: bigcommerce-consignmentformfield
- name: ConsignmentLineItem
  property_count: 1
  slug: bigcommerce-consignmentlineitem
- name: Consignments
  property_count: 1
  slug: bigcommerce-consignments
- name: consignmentShippingOption_Base
  property_count: 6
  slug: bigcommerce-consignmentshippingoption-base
- name: Contact Entity
  property_count: 2
  slug: bigcommerce-contactentity
- name: ContactFields
  property_count: 0
  slug: bigcommerce-contactfields
- name: ContentSortEnumValues
  property_count: 0
  slug: bigcommerce-contentsortenumvalues
- name: count_Full
  property_count: 1
  slug: bigcommerce-count-full
- name: count_Response
  property_count: 1
  slug: bigcommerce-count-response
- name: countriesState_Full
  property_count: 4
  slug: bigcommerce-countriesstate-full
- name: countriesStates_Full
  property_count: 2
  slug: bigcommerce-countriesstates-full
- name: country_Base
  property_count: 3
  slug: bigcommerce-country-base
- name: country_Full
  property_count: 0
  slug: bigcommerce-country-full
- name: coupon_Base
  property_count: 12
  slug: bigcommerce-coupon-base
- name: coupon_Full
  property_count: 0
  slug: bigcommerce-coupon-full
- name: Coupon Code Field
  property_count: 0
  slug: bigcommerce-couponcode
- name: Coupon Code Request
  property_count: 1
  slug: bigcommerce-couponcoderequest
- name: Coupon Resource
  property_count: 2
  slug: bigcommerce-couponsresource
- name: CreateBatchPriceListAssignmentsRequest
  property_count: 0
  slug: bigcommerce-createbatchpricelistassignmentsrequest
- name: Create Categories
  property_count: 0
  slug: bigcommerce-createcategories
- name: CreateChannelReq
  property_count: 8
  slug: bigcommerce-createchannelreq
- name: Create Consignment Request
  property_count: 0
  slug: bigcommerce-createconsignmentrequest
- name: CreateMultipleListingsReq
  property_count: 0
  slug: bigcommerce-createmultiplelistingsreq
- name: CreateReturn
  property_count: 0
  slug: bigcommerce-createreturn
- name: CreateReturnRequest
  property_count: 2
  slug: bigcommerce-createreturnrequest
- name: CreateReturnRequestItem
  property_count: 4
  slug: bigcommerce-createreturnrequestitem
- name: Credit Card
  property_count: 5
  slug: bigcommerce-creditcard
- name: currency_Base
  property_count: 13
  slug: bigcommerce-currency-base
- name: currency_Full
  property_count: 0
  slug: bigcommerce-currency-full
- name: currency_Post
  property_count: 0
  slug: bigcommerce-currency-post
- name: currency_Put
  property_count: 0
  slug: bigcommerce-currency-put
- name: Currency
  property_count: 1
  slug: bigcommerce-currency
- name: CurrencyNotRequiredWithChannelId
  property_count: 3
  slug: bigcommerce-currencynotrequiredwithchannelid
- name: CurrencyRequiredWithChannelId
  property_count: 3
  slug: bigcommerce-currencyrequiredwithchannelid
- name: CurrencyRequiredWithoutChannelId
  property_count: 2
  slug: bigcommerce-currencyrequiredwithoutchannelid
- name: Custom
  property_count: 1
  slug: bigcommerce-custom
- name: CustomAppSections
  property_count: 0
  slug: bigcommerce-customappsections
- name: customer_Base
  property_count: 0
  slug: bigcommerce-customer-base
- name: customer_Full
  property_count: 18
  slug: bigcommerce-customer-full
- name: customer_Post
  property_count: 16
  slug: bigcommerce-customer-post
- name: customer_Put
  property_count: 16
  slug: bigcommerce-customer-put
- name: customerAddresses_Base
  property_count: 11
  slug: bigcommerce-customeraddresses-base
- name: customerAddresses_CustomerPost
  property_count: 12
  slug: bigcommerce-customeraddresses-customerpost
- name: customerAttributes_Base
  property_count: 2
  slug: bigcommerce-customerattributes-base
- name: customerAuthentication_PostPut
  property_count: 0
  slug: bigcommerce-customerauthentication-postput
- name: customerChannelIds
  property_count: 0
  slug: bigcommerce-customerchannelids
- name: CustomerChannelSettingsObject
  property_count: 3
  slug: bigcommerce-customerchannelsettingsobject
- name: CustomerCreateData
  property_count: 6
  slug: bigcommerce-customercreatedata
- name: Customer Details
  property_count: 2
  slug: bigcommerce-customerdetails
- name: Customer Group
  property_count: 2
  slug: bigcommerce-customergroup
- name: Customer Login SSO
  property_count: 8
  slug: bigcommerce-customerloginsso
- name: CustomerSettingsObject
  property_count: 2
  slug: bigcommerce-customersettingsobject
- name: CustomerStoredCreditAmounts
  property_count: 0
  slug: bigcommerce-customerstoredcreditamounts
- name: Custom Field
  property_count: 2
  slug: bigcommerce-customfield
- name: Product Custom Field Data
  property_count: 3
  slug: bigcommerce-customfielddata
- name: Custom Field Post
  property_count: 2
  slug: bigcommerce-customfieldpost
- name: Custom Field Put
  property_count: 2
  slug: bigcommerce-customfieldput
- name: customFields
  property_count: 2
  slug: bigcommerce-customfields
- name: customsInformationRequest
  property_count: 5
  slug: bigcommerce-customsinformation-request
- name: customsInformation
  property_count: 7
  slug: bigcommerce-customsinformation
- name: CustomTemplateAssociation
  property_count: 8
  slug: bigcommerce-customtemplateassociation
- name: CustomTemplateAssociation
  property_count: 4
  slug: bigcommerce-customtemplateassociationupsert
- name: customUrl_Full
  property_count: 2
  slug: bigcommerce-customurl-full
- name: CVV Result
  property_count: 2
  slug: bigcommerce-cvvresult
- name: Data
  property_count: 1
  slug: bigcommerce-data
- name: dateFormat
  property_count: 3
  slug: bigcommerce-dateformat
- name: Date Range
  property_count: 2
  slug: bigcommerce-daterange
- name: Date Value
  property_count: 2
  slug: bigcommerce-datevalue
- name: DeclareCustomerConsentRequest
  property_count: 2
  slug: bigcommerce-declarecustomerconsentrequest
- name: default_product_sort
  property_count: 1
  slug: bigcommerce-default-product-sort
- name: DefaultCurrency
  property_count: 0
  slug: bigcommerce-defaultcurrency
- name: Deny
  property_count: 0
  slug: bigcommerce-deny
- name: description
  property_count: 1
  slug: bigcommerce-description
- name: DetailedErrors
  property_count: 0
  slug: bigcommerce-detailederrors
- name: Dimension Value
  property_count: 2
  slug: bigcommerce-dimensionvalue
- name: EmailTemplate
  property_count: 4
  slug: bigcommerce-emailtemplate
- name: EmailTemplatesCollection
  property_count: 0
  slug: bigcommerce-emailtemplatescollection
- name: EmailTemplateUpdate
  property_count: 3
  slug: bigcommerce-emailtemplateupdate
- name: Empty meta response.
  property_count: 0
  slug: bigcommerce-emptymeta
- name: EmptyResponse
  property_count: 2
  slug: bigcommerce-emptyresponse
- name: EnabledBrandFilter
  property_count: 8
  slug: bigcommerce-enabledbrandfilter
- name: EnabledCategoryFilter
  property_count: 7
  slug: bigcommerce-enabledcategoryfilter
- name: EnabledCurrencies
  property_count: 0
  slug: bigcommerce-enabledcurrencies
- name: EnabledFilter
  property_count: 0
  slug: bigcommerce-enabledfilter
- name: EnabledFilters
  property_count: 0
  slug: bigcommerce-enabledfilters
- name: EnabledFiltersOverride
  property_count: 2
  slug: bigcommerce-enabledfiltersoverride
- name: EnabledMiscFilter
  property_count: 10
  slug: bigcommerce-enabledmiscfilter
- name: EnabledPriceFilter
  property_count: 5
  slug: bigcommerce-enabledpricefilter
- name: EnabledProductFilter
  property_count: 8
  slug: bigcommerce-enabledproductfilter
- name: EnabledRatingFilter
  property_count: 5
  slug: bigcommerce-enabledratingfilter
- name: ''
  property_count: 11
  slug: bigcommerce-enabledtransactionalemails
- name: error_Base
  property_count: 4
  slug: bigcommerce-error-base
- name: error_Full
  property_count: 3
  slug: bigcommerce-error-full
- name: Error
  property_count: 4
  slug: bigcommerce-error
- name: ErrorAdditional
  property_count: 1
  slug: bigcommerce-erroradditional
- name: ErrorBasic
  property_count: 3
  slug: bigcommerce-errorbasic
- name: ErrorDetail
  property_count: 0
  slug: bigcommerce-errordetail
- name: errorDetailed_Full
  property_count: 1
  slug: bigcommerce-errordetailed-full
- name: errorMultiStatus
  property_count: 4
  slug: bigcommerce-errormultistatus
- name: ErrorRequest
  property_count: 1
  slug: bigcommerce-errorrequest
- name: errorResponse_409
  property_count: 0
  slug: bigcommerce-errorresponse-409
- name: errorResponse_422
  property_count: 0
  slug: bigcommerce-errorresponse-422
- name: ErrorResponse
  property_count: 5
  slug: bigcommerce-errorresponse
- name: ErrorResponse400
  property_count: 1
  slug: bigcommerce-errorresponse400
- name: ErrorResponse404
  property_count: 1
  slug: bigcommerce-errorresponse404
- name: ErrorResponse409
  property_count: 1
  slug: bigcommerce-errorresponse409
- name: ErrorResponse422
  property_count: 1
  slug: bigcommerce-errorresponse422
- name: _errors
  property_count: 0
  slug: bigcommerce-errors
- name: ExternalId
  property_count: 0
  slug: bigcommerce-externalid
- name: Failed
  property_count: 0
  slug: bigcommerce-failed
- name: FailedQuoteError
  property_count: 3
  slug: bigcommerce-failedquoteerror
- name: formField
  property_count: 2
  slug: bigcommerce-formfield
- name: FormFieldGroups
  property_count: 3
  slug: bigcommerce-formfieldgroups
- name: FormFields
  property_count: 0
  slug: bigcommerce-formfields
- name: Customer Address Form Field Value
  property_count: 3
  slug: bigcommerce-formfieldvalue-address
- name: Customer Form Field Value
  property_count: 3
  slug: bigcommerce-formfieldvalue-customer
- name: formFieldValue_Full
  property_count: 0
  slug: bigcommerce-formfieldvalue-full
- name: Generic Form Field Value
  property_count: 2
  slug: bigcommerce-formfieldvalue
- name: forward
  property_count: 2
  slug: bigcommerce-forward
- name: Error Response
  property_count: 4
  slug: bigcommerce-generalerror
- name: Error Response
  property_count: 4
  slug: bigcommerce-generalerrorwitherrors
- name: Get Categories
  property_count: 0
  slug: bigcommerce-getcategories
- name: GetCertificatesResponse
  property_count: 2
  slug: bigcommerce-getcertificatesresponse
- name: GetReturnableItems
  property_count: 0
  slug: bigcommerce-getreturnableitems
- name: GetReturnsSettings
  property_count: 2
  slug: bigcommerce-getreturnssettings
- name: giftCertificate_Base
  property_count: 5
  slug: bigcommerce-giftcertificate-base
- name: giftCertificate_Full
  property_count: 0
  slug: bigcommerce-giftcertificate-full
- name: giftCertificate_Post
  property_count: 0
  slug: bigcommerce-giftcertificate-post
- name: giftCertificate_Put
  property_count: 0
  slug: bigcommerce-giftcertificate-put
- name: Gift Certificate
  property_count: 5
  slug: bigcommerce-giftcertificate
- name: Gift Certificate Request
  property_count: 1
  slug: bigcommerce-giftcertificaterequest
- name: Gift Wrapping
  property_count: 3
  slug: bigcommerce-giftwrapping
- name: GlobalAbandonedCartSettingsRequest
  property_count: 0
  slug: bigcommerce-globalabandonedcartsettingsrequest
- name: GlobalAbandonedCartSettingsResponse
  property_count: 2
  slug: bigcommerce-globalabandonedcartsettingsresponse
- name: GlobalCartSettingsRequest
  property_count: 0
  slug: bigcommerce-globalcartsettingsrequest
- name: GlobalCartSettingsResponse
  property_count: 2
  slug: bigcommerce-globalcartsettingsresponse
- name: GlobalOrderSettings
  property_count: 1
  slug: bigcommerce-globalordersettings
- name: handling_type
  property_count: 0
  slug: bigcommerce-handling-type
- name: harmonizedSystemCodes
  property_count: 0
  slug: bigcommerce-harmonizedsystemcodes
- name: HistoryEvent
  property_count: 6
  slug: bigcommerce-historyevent
- name: HSTSMaxAgeEnumValues
  property_count: 0
  slug: bigcommerce-hstsmaxageenumvalues
- name: IconUrl
  property_count: 0
  slug: bigcommerce-iconurl
- name: id
  property_count: 1
  slug: bigcommerce-id
- name: image_url
  property_count: 1
  slug: bigcommerce-image-url
- name: ImportErrors
  property_count: 0
  slug: bigcommerce-importerrors
- name: ImportExportJobStatus
  property_count: 0
  slug: bigcommerce-importexportjobstatus
- name: ImportExportJobType
  property_count: 0
  slug: bigcommerce-importexportjobtype
- name: IndexMeta
  property_count: 1
  slug: bigcommerce-indexmeta
- name: InstallCertificateData
  property_count: 2
  slug: bigcommerce-installcertificatedata
- name: CertificateInfo
  property_count: 8
  slug: bigcommerce-installedcertificatedetail
- name: InventoryNotificationsSettings
  property_count: 2
  slug: bigcommerce-inventorynotificationssettings
- name: InventorySettings
  property_count: 10
  slug: bigcommerce-inventorysettings
- name: is_visible
  property_count: 1
  slug: bigcommerce-is-visible
- name: IsListableFromUI
  property_count: 0
  slug: bigcommerce-islistablefromui
- name: IsVisible
  property_count: 0
  slug: bigcommerce-isvisible
- name: Item
  property_count: 3
  slug: bigcommerce-item
- name: item_type
  property_count: 0
  slug: bigcommerce-item-type
- name: Item Custom
  property_count: 5
  slug: bigcommerce-itemcustom
- name: Item Custom
  property_count: 5
  slug: bigcommerce-itemcustomget
- name: ''
  property_count: 0
  slug: bigcommerce-itemdigital
- name: ''
  property_count: 0
  slug: bigcommerce-itemdigitalget
- name: Item Gift Certificate
  property_count: 8
  slug: bigcommerce-itemgiftcertificate
- name: Item Gift Certificate
  property_count: 8
  slug: bigcommerce-itemgiftcertificateget
- name: ItemPhysical
  property_count: 0
  slug: bigcommerce-itemphysical
- name: ''
  property_count: 0
  slug: bigcommerce-itemphysicalget
- name: ItemPricing
  property_count: 11
  slug: bigcommerce-itempricing
- name: ItemReferenceId
  property_count: 2
  slug: bigcommerce-itemreferenceid
- name: ItemsRefund
  property_count: 0
  slug: bigcommerce-itemsrefund
- name: Job
  property_count: 7
  slug: bigcommerce-job
- name: Job Id
  property_count: 1
  slug: bigcommerce-jobid
- name: Job Response
  property_count: 2
  slug: bigcommerce-jobresponse
- name: Key Value Pair
  property_count: 2
  slug: bigcommerce-keyvaluepair
- name: Key Value Pair Schema
  property_count: 8
  slug: bigcommerce-keyvaluepairschema
- name: layout_file
  property_count: 1
  slug: bigcommerce-layout-file
- name: Line Item Gift Certificate Request Data
  property_count: 7
  slug: bigcommerce-lineitemgiftcertificaterequestdata
- name: Line Item Request Data
  property_count: 5
  slug: bigcommerce-lineitemrequestdata
- name: line_items
  property_count: 4
  slug: bigcommerce-lineitems
- name: LineItemsGet
  property_count: 4
  slug: bigcommerce-lineitemsget
- name: requestLineItems
  property_count: 0
  slug: bigcommerce-lineitemsrequest
- name: links_Full
  property_count: 3
  slug: bigcommerce-links-full
- name: Links
  property_count: 3
  slug: bigcommerce-links
- name: Listing
  property_count: 10
  slug: bigcommerce-listing
- name: ListingId
  property_count: 0
  slug: bigcommerce-listingid
- name: ListingState
  property_count: 0
  slug: bigcommerce-listingstate
- name: Locale
  property_count: 3
  slug: bigcommerce-locale
- name: LocaleCollection
  property_count: 0
  slug: bigcommerce-localecollection
- name: LocaleObject
  property_count: 2
  slug: bigcommerce-localeobject
- name: LogoSettings
  property_count: 4
  slug: bigcommerce-logosettings
- name: LogoSettingsUpdate
  property_count: 2
  slug: bigcommerce-logosettingsupdate
- name: MeasurementUnitsSettings
  property_count: 6
  slug: bigcommerce-measurementunitssettings
- name: Merchant Calculated Override
  property_count: 2
  slug: bigcommerce-merchantoverride
- name: Message
  property_count: 2
  slug: bigcommerce-message
- name: meta_description
  property_count: 1
  slug: bigcommerce-meta-description
- name: meta_keywords
  property_count: 1
  slug: bigcommerce-meta-keywords
- name: Meta
  property_count: 1
  slug: bigcommerce-meta
- name: metaCollection_Full
  property_count: 1
  slug: bigcommerce-metacollection-full
- name: Response meta
  property_count: 0
  slug: bigcommerce-metacollection-open
- name: _metaCollection
  property_count: 1
  slug: bigcommerce-metacollection
- name: metaCollectionFull
  property_count: 1
  slug: bigcommerce-metacollectionfull
- name: MetaData
  property_count: 3
  slug: bigcommerce-metadata
- name: Response meta
  property_count: 0
  slug: bigcommerce-metaempty-full
- name: _metaEmpty
  property_count: 0
  slug: bigcommerce-metaempty
- name: Response meta
  property_count: 0
  slug: bigcommerce-metaemptyfull
- name: MetaError
  property_count: 0
  slug: bigcommerce-metaerror
- name: metafield_Base
  property_count: 5
  slug: bigcommerce-metafield-base
- name: metafield_Full
  property_count: 0
  slug: bigcommerce-metafield-full
- name: metafield_Post
  property_count: 5
  slug: bigcommerce-metafield-post
- name: metafield_Put
  property_count: 5
  slug: bigcommerce-metafield-put
- name: Metafield
  property_count: 0
  slug: bigcommerce-metafield
- name: MetafieldBase_Post
  property_count: 5
  slug: bigcommerce-metafieldbase-post
- name: MetafieldBase_Put
  property_count: 5
  slug: bigcommerce-metafieldbase-put
- name: MetafieldBase
  property_count: 7
  slug: bigcommerce-metafieldbase
- name: MetaFieldCollectionDeleteResponseSuccess
  property_count: 3
  slug: bigcommerce-metafieldcollectiondeleteresponsesuccess
- name: MetaFieldCollectionPostPutResponses
  property_count: 3
  slug: bigcommerce-metafieldcollectionpostputresponses
- name: MetaFieldCollectionResponse_Batch_POST_PUT
  property_count: 3
  slug: bigcommerce-metafieldcollectionresponse-batch-post-put
- name: MetaFieldCollectionResponse_Batch
  property_count: 2
  slug: bigcommerce-metafieldcollectionresponse-batch
- name: MetaFieldCollectionResponse_POST_PUT
  property_count: 3
  slug: bigcommerce-metafieldcollectionresponse-post-put
- name: MetaFieldCollectionResponse
  property_count: 2
  slug: bigcommerce-metafieldcollectionresponse
- name: MetaFieldCollectionResponsePartialSuccess_DELETE
  property_count: 3
  slug: bigcommerce-metafieldcollectionresponsepartialsuccess-delete
- name: MetaFieldCollectionResponsePartialSuccess_POST_PUT
  property_count: 3
  slug: bigcommerce-metafieldcollectionresponsepartialsuccess-post-put
- name: MetafieldPost_Batch
  property_count: 0
  slug: bigcommerce-metafieldpost-batch
- name: MetafieldPost
  property_count: 0
  slug: bigcommerce-metafieldpost
- name: MetafieldPut_Batch
  property_count: 0
  slug: bigcommerce-metafieldput-batch
- name: MetafieldPut
  property_count: 0
  slug: bigcommerce-metafieldput
- name: MetafieldResponse
  property_count: 0
  slug: bigcommerce-metafieldresponse
- name: Response meta
  property_count: 0
  slug: bigcommerce-metaopen
- name: MetaPagination
  property_count: 1
  slug: bigcommerce-metapagination
- name: MetaPaginationObject
  property_count: 1
  slug: bigcommerce-metapaginationobject
- name: MetaRefund
  property_count: 3
  slug: bigcommerce-metarefund
- name: MetaWithFullPagination
  property_count: 1
  slug: bigcommerce-metawithfullpagination
- name: MetaWithPartialPagination
  property_count: 1
  slug: bigcommerce-metawithpartialpagination
- name: Error Response
  property_count: 4
  slug: bigcommerce-methodnotallowederror
- name: Money Value
  property_count: 2
  slug: bigcommerce-moneyvalue
- name: MultiStatus
  property_count: 3
  slug: bigcommerce-multistatus
- name: name
  property_count: 1
  slug: bigcommerce-name
- name: new-model
  property_count: 0
  slug: bigcommerce-new-model
- name: Update Consignment Request
  property_count: 5
  slug: bigcommerce-newupdateconsignment
- name: No Content
  property_count: 4
  slug: bigcommerce-nocontent
- name: Not Found
  property_count: 4
  slug: bigcommerce-notfound
- name: NotifyAtMinutes
  property_count: 0
  slug: bigcommerce-notifyatminutes
- name: Offline
  property_count: 1
  slug: bigcommerce-offline
- name: Response meta
  property_count: 0
  slug: bigcommerce-openmeta
- name: order_Nate
  property_count: 23
  slug: bigcommerce-order-nate
- name: Order
  property_count: 1
  slug: bigcommerce-order
- name: Order Item Digital
  property_count: 23
  slug: bigcommerce-orderitemdigital
- name: Order Item Gift Certificate
  property_count: 5
  slug: bigcommerce-orderitemgiftcertificate
- name: Order Line Item
  property_count: 3
  slug: bigcommerce-orderlineitem
- name: page_Base_Res
  property_count: 20
  slug: bigcommerce-page-base-res
- name: page_Base
  property_count: 20
  slug: bigcommerce-page-base
- name: page_Full
  property_count: 0
  slug: bigcommerce-page-full
- name: ''
  property_count: 0
  slug: bigcommerce-page
- name: page_title
  property_count: 1
  slug: bigcommerce-page-title
- name: PageBase
  property_count: 7
  slug: bigcommerce-pagebase
- name: pageMeta
  property_count: 3
  slug: bigcommerce-pagemeta
- name: PagePut
  property_count: 18
  slug: bigcommerce-pageput
- name: PagePutBulk
  property_count: 19
  slug: bigcommerce-pageputbulk
- name: PageResponseObject
  property_count: 0
  slug: bigcommerce-pageresponse
- name: ''
  property_count: 2
  slug: bigcommerce-pagescollectionresponse
- name: pagination_Full
  property_count: 6
  slug: bigcommerce-pagination-full
- name: pagination_Partial
  property_count: 4
  slug: bigcommerce-pagination-partial
- name: Pagination
  property_count: 6
  slug: bigcommerce-pagination
- name: parent_id
  property_count: 1
  slug: bigcommerce-parent-id
- name: PartialSuccessNoContentResponse
  property_count: 2
  slug: bigcommerce-partialsuccessnocontentresponse
- name: PartialSuccessResponse
  property_count: 3
  slug: bigcommerce-partialsuccessresponse
- name: payment_Base
  property_count: 3
  slug: bigcommerce-payment-base
- name: paymentMethod_Full
  property_count: 6
  slug: bigcommerce-paymentmethod-full
- name: paymentMethodStoredInstrument
  property_count: 8
  slug: bigcommerce-paymentmethodstoredinstrument
- name: Payment Option
  property_count: 6
  slug: bigcommerce-paymentoption
- name: Payment Request
  property_count: 3
  slug: bigcommerce-paymentrequest
- name: PayPal Account Instrument
  property_count: 4
  slug: bigcommerce-paypalaccountinstrument
- name: PickupConsignment
  property_count: 7
  slug: bigcommerce-pickupconsignment
- name: PickupConsignmentLocation
  property_count: 11
  slug: bigcommerce-pickupconsignmentlocation
- name: Pickup Option
  property_count: 1
  slug: bigcommerce-pickupoption
- name: placement_Base
  property_count: 4
  slug: bigcommerce-placement-base
- name: placement_Full
  property_count: 0
  slug: bigcommerce-placement-full
- name: placement_Post
  property_count: 0
  slug: bigcommerce-placement-post
- name: placement_Put
  property_count: 0
  slug: bigcommerce-placement-put
- name: post_Site
  property_count: 2
  slug: bigcommerce-post-site
- name: Refund Quotes Request - BATCH
  property_count: 0
  slug: bigcommerce-postrefundquotesrequest
- name: Refunds Request - BATCH
  property_count: 0
  slug: bigcommerce-postrefundsrequest
- name: PreferredOutcome
  property_count: 3
  slug: bigcommerce-preferredoutcome
- name: PriceListAssignmentsBatchErrorResponse
  property_count: 5
  slug: bigcommerce-pricelistassignmentsbatcherrorresponse
- name: PriceRange
  property_count: 2
  slug: bigcommerce-pricerange
- name: PriceRecordBase
  property_count: 5
  slug: bigcommerce-pricerecordbase
- name: PriceRecordBatchErrorResponse
  property_count: 2
  slug: bigcommerce-pricerecordbatcherrorresponse
- name: PriceRecordBatchItem
  property_count: 5
  slug: bigcommerce-pricerecordbatchitem
- name: PriceRecordIdentifiers
  property_count: 0
  slug: bigcommerce-pricerecordidentifiers
- name: PricingRequest
  property_count: 4
  slug: bigcommerce-pricingrequest
- name: PricingResponse
  property_count: 2
  slug: bigcommerce-pricingresponse
- name: Problem
  property_count: 3
  slug: bigcommerce-problem
- name: product_Base
  property_count: 67
  slug: bigcommerce-product-base
- name: product_Full
  property_count: 0
  slug: bigcommerce-product-full
- name: product_Put_Collection
  property_count: 0
  slug: bigcommerce-product-put-collection
- name: product_Put
  property_count: 0
  slug: bigcommerce-product-put
- name: ProductCategoryAssignment
  property_count: 2
  slug: bigcommerce-productcategoryassignment
- name: ProductChannelAssignment
  property_count: 2
  slug: bigcommerce-productchannelassignment
- name: productCustomField_Base
  property_count: 3
  slug: bigcommerce-productcustomfield-base
- name: productCustomField_Put
  property_count: 3
  slug: bigcommerce-productcustomfield-put
- name: ProductId
  property_count: 0
  slug: bigcommerce-productid
- name: productImage_Base
  property_count: 5
  slug: bigcommerce-productimage-base
- name: productImage_Full
  property_count: 0
  slug: bigcommerce-productimage-full
- name: productImage_Put
  property_count: 0
  slug: bigcommerce-productimage-put
- name: productModifier_Base
  property_count: 5
  slug: bigcommerce-productmodifier-base
- name: productModifier_Full
  property_count: 0
  slug: bigcommerce-productmodifier-full
- name: productModifierOptionValue_Base
  property_count: 5
  slug: bigcommerce-productmodifieroptionvalue-base
- name: productModifierOptionValue_Full
  property_count: 0
  slug: bigcommerce-productmodifieroptionvalue-full
- name: productOption_Base
  property_count: 7
  slug: bigcommerce-productoption-base
- name: productOption_Full
  property_count: 0
  slug: bigcommerce-productoption-full
- name: Product Option
  property_count: 4
  slug: bigcommerce-productoption
- name: productOptionConfig_Full
  property_count: 24
  slug: bigcommerce-productoptionconfig-full
- name: productOptionOptionValue_Base
  property_count: 4
  slug: bigcommerce-productoptionoptionvalue-base
- name: productOptionOptionValue_Full
  property_count: 0
  slug: bigcommerce-productoptionoptionvalue-full
- name: Product Option Selection
  property_count: 2
  slug: bigcommerce-productoptionselection
- name: ProductSortEnumValues
  property_count: 0
  slug: bigcommerce-productsortenumvalues
- name: productSortOrder
  property_count: 2
  slug: bigcommerce-productsortorder
- name: ProductTaxProperty
  property_count: 2
  slug: bigcommerce-producttaxproperty
- name: productVariant_Base
  property_count: 18
  slug: bigcommerce-productvariant-base
- name: productVariant_Full
  property_count: 0
  slug: bigcommerce-productvariant-full
- name: productVariant_Post
  property_count: 0
  slug: bigcommerce-productvariant-post
- name: productVariant_Put_Product
  property_count: 19
  slug: bigcommerce-productvariant-put-product
- name: productVariant_Put
  property_count: 0
  slug: bigcommerce-productvariant-put
- name: productVariantOptionValue_Base
  property_count: 2
  slug: bigcommerce-productvariantoptionvalue-base
- name: productVariantOptionValue_Full
  property_count: 0
  slug: bigcommerce-productvariantoptionvalue-full
- name: productVideo_Base
  property_count: 5
  slug: bigcommerce-productvideo-base
- name: productVideo_Full
  property_count: 0
  slug: bigcommerce-productvideo-full
- name: Property
  property_count: 6
  slug: bigcommerce-property
- name: PropertyPOST
  property_count: 3
  slug: bigcommerce-propertypost
- name: PropertyPUT
  property_count: 4
  slug: bigcommerce-propertyput
- name: publishedDate
  property_count: 3
  slug: bigcommerce-publisheddate
- name: put_Site
  property_count: 1
  slug: bigcommerce-put-site
- name: ''
  property_count: 1
  slug: bigcommerce-putcheckouturl
- name: Quantity Bound Item
  property_count: 4
  slug: bigcommerce-quantitybounditem
- name: Rate Options Instance
  property_count: 0
  slug: bigcommerce-rateoptionsinstance
- name: Rate Options Schema
  property_count: 0
  slug: bigcommerce-rateoptionsschema
- name: Rate Quote Object
  property_count: 9
  slug: bigcommerce-ratequoteobject
- name: Rate Request Item
  property_count: 12
  slug: bigcommerce-raterequestitem
- name: Rate Request Payload
  property_count: 3
  slug: bigcommerce-raterequestpayload
- name: Rate Response Payload
  property_count: 3
  slug: bigcommerce-rateresponsepayload
- name: ReadShared
  property_count: 7
  slug: bigcommerce-readshared
- name: Reason
  property_count: 3
  slug: bigcommerce-reason
- name: ReceivedItems_Base
  property_count: 0
  slug: bigcommerce-receiveditems-base
- name: ReceivedItems_Put
  property_count: 0
  slug: bigcommerce-receiveditems-put
- name: redirect
  property_count: 4
  slug: bigcommerce-redirect
- name: Redirect_urls_Post
  property_count: 1
  slug: bigcommerce-redirect-urls-post
- name: RedirectTo
  property_count: 3
  slug: bigcommerce-redirectto
- name: Reference Value
  property_count: 2
  slug: bigcommerce-referencevalue
- name: Refund
  property_count: 10
  slug: bigcommerce-refund
- name: RefundID_Get
  property_count: 2
  slug: bigcommerce-refundid-get
- name: Refund Item
  property_count: 5
  slug: bigcommerce-refunditem
- name: Refund Method
  property_count: 0
  slug: bigcommerce-refundmethod
- name: Refund Payment
  property_count: 6
  slug: bigcommerce-refundpayment
- name: RefundQuote_Full
  property_count: 7
  slug: bigcommerce-refundquote-full
- name: RefundQuote_Post
  property_count: 1
  slug: bigcommerce-refundquote-post
- name: RefundRequest_Post
  property_count: 3
  slug: bigcommerce-refundrequest-post
- name: AdjustRequest
  property_count: 0
  slug: bigcommerce-request-adjust
- name: DocumentRequest
  property_count: 7
  slug: bigcommerce-request-document
- name: ItemRequest
  property_count: 9
  slug: bigcommerce-request-item
- name: TaxProperty
  property_count: 2
  slug: bigcommerce-request-item-tax-property
- name: QuoteRequest
  property_count: 5
  slug: bigcommerce-request-quote
- name: Create Cart Request Object
  property_count: 0
  slug: bigcommerce-requestcart
- name: Line Item Request Data
  property_count: 0
  slug: bigcommerce-requestcartpostlineitem
- name: Request Context
  property_count: 1
  slug: bigcommerce-requestcontext
- name: Request Headers
  property_count: 1
  slug: bigcommerce-requestheaders
- name: Line Item Gift Certificate Request Data
  property_count: 7
  slug: bigcommerce-requestlineitemgiftcertificate
- name: Contact Entity
  property_count: 2
  slug: bigcommerce-requestlineitemgiftcertificaterecipient
- name: Contact Entity
  property_count: 2
  slug: bigcommerce-requestlineitemgiftcertificatesender
- name: requestLineItemPut
  property_count: 0
  slug: bigcommerce-requestlineitemput
- name: Gift Wrapping Request Data
  property_count: 2
  slug: bigcommerce-requestpostorputgiftwrapping
- name: Connection Status
  property_count: 1
  slug: bigcommerce-response-connection
- name: Document
  property_count: 5
  slug: bigcommerce-response-document
- name: Item
  property_count: 2
  slug: bigcommerce-response-item
- name: Quote
  property_count: 2
  slug: bigcommerce-response-quote
- name: TaxPrice
  property_count: 5
  slug: bigcommerce-response-taxprice
- name: Cart Read
  property_count: 14
  slug: bigcommerce-responsecart
- name: Base Item
  property_count: 20
  slug: bigcommerce-responsecartbaseitem
- name: Response Cart Coupons
  property_count: 0
  slug: bigcommerce-responsecartcoupons
- name: Currency
  property_count: 1
  slug: bigcommerce-responsecartcurrency
- name: responseCartDiscounts
  property_count: 0
  slug: bigcommerce-responsecartdiscounts
- name: Response Line Items Object
  property_count: 4
  slug: bigcommerce-responsecartlineitems
- name: Item Custom
  property_count: 6
  slug: bigcommerce-responsecartlineitemscustomitems
- name: Item Digital
  property_count: 0
  slug: bigcommerce-responsecartlineitemsdigitalitems
- name: Base Item
  property_count: 20
  slug: bigcommerce-responsecartlineitemsdigitalitemsallof0
- name: Applied Discount
  property_count: 2
  slug: bigcommerce-responsecartlineitemsdigitalitemsallof0discountsitems
- name: Product Option
  property_count: 4
  slug: bigcommerce-responsecartlineitemsdigitalitemsallof0optionsitems
- name: Item Gift Certificate
  property_count: 8
  slug: bigcommerce-responsecartlineitemsgiftcertificates
- name: Contact Entity
  property_count: 2
  slug: bigcommerce-responsecartlineitemsgiftcertificatesrecipient
- name: Contact Entity
  property_count: 2
  slug: bigcommerce-responsecartlineitemsgiftcertificatessender
- name: Item Physical
  property_count: 0
  slug: bigcommerce-responsecartlineitemsitemsphysicalitemsitems
- name: Product Option
  property_count: 4
  slug: bigcommerce-responsecartlineitemsitemsphysicalitemsitemsallof0optionsite
- name: responseCartLineItemsItemsPhysicalItemsItemsAllOf1
  property_count: 2
  slug: bigcommerce-responsecartlineitemsitemsphysicalitemsitemsallof1
- name: Gift Wrapping
  property_count: 3
  slug: bigcommerce-responsecartlineitemsphysicalitemgiftwrapping
- name: ResponseErrorBrief
  property_count: 3
  slug: bigcommerce-responseerrorbrief
- name: ResponseErrorDetailed
  property_count: 4
  slug: bigcommerce-responseerrordetailed
- name: ResponseErrorItemized
  property_count: 4
  slug: bigcommerce-responseerroritemized
- name: ResponseMeta
  property_count: 1
  slug: bigcommerce-responsemeta
- name: Return_Full
  property_count: 7
  slug: bigcommerce-return-full
- name: ReturnItem
  property_count: 8
  slug: bigcommerce-returnitem
- name: ReviewedItems_Base
  property_count: 0
  slug: bigcommerce-revieweditems-base
- name: ReviewedItems_Put
  property_count: 0
  slug: bigcommerce-revieweditems-put
- name: RobotsTxtSettings
  property_count: 1
  slug: bigcommerce-robotstxtsettings
- name: SalesTax
  property_count: 5
  slug: bigcommerce-salestax
- name: SaveError
  property_count: 4
  slug: bigcommerce-saveerror
- name: scratch
  property_count: 1
  slug: bigcommerce-scratch
- name: script_Base
  property_count: 12
  slug: bigcommerce-script-base
- name: script_Full
  property_count: 0
  slug: bigcommerce-script-full
- name: script_Post
  property_count: 0
  slug: bigcommerce-script-post
- name: script_Put
  property_count: 0
  slug: bigcommerce-script-put
- name: script_Response
  property_count: 2
  slug: bigcommerce-script-response
- name: script_responseCollection
  property_count: 2
  slug: bigcommerce-script-responsecollection
- name: search_keywords
  property_count: 1
  slug: bigcommerce-search-keywords
- name: ContextIdentifier
  property_count: 2
  slug: bigcommerce-searchfilteroverridecontextidentifier
- name: ScopeIdentifier
  property_count: 2
  slug: bigcommerce-searchfilteroverridescopeidentifier
- name: searchKeywords
  property_count: 1
  slug: bigcommerce-searchkeywords
- name: SEOSettings
  property_count: 4
  slug: bigcommerce-seosettings
- name: shipping_type
  property_count: 0
  slug: bigcommerce-shipping-type
- name: Shipping Address
  property_count: 7
  slug: bigcommerce-shippingaddress
- name: ShippingConsignment
  property_count: 30
  slug: bigcommerce-shippingconsignment
- name: site_Full
  property_count: 6
  slug: bigcommerce-site-full
- name: site_Post
  property_count: 2
  slug: bigcommerce-site-post
- name: site_Put
  property_count: 1
  slug: bigcommerce-site-put
- name: Site
  property_count: 8
  slug: bigcommerce-site
- name: SiteCreate
  property_count: 3
  slug: bigcommerce-sitecreate
- name: siteRoute_Base
  property_count: 3
  slug: bigcommerce-siteroute-base
- name: siteRoute_Full
  property_count: 0
  slug: bigcommerce-siteroute-full
- name: siteRoutes_Route_Base
  property_count: 3
  slug: bigcommerce-siteroutes-route-base
- name: sort_order
  property_count: 1
  slug: bigcommerce-sort-order
- name: SpamProtectionRequest
  property_count: 1
  slug: bigcommerce-spamprotectionrequest
- name: Status_Full
  property_count: 0
  slug: bigcommerce-status-full
- name: Status
  property_count: 0
  slug: bigcommerce-status
- name: StatusUpdate_Full
  property_count: 2
  slug: bigcommerce-statusupdate-full
- name: store/app/uninstalled
  property_count: 0
  slug: bigcommerce-store-app-uninstalled
- name: store/cart/abandoned
  property_count: 0
  slug: bigcommerce-store-cart-abandoned
- name: store/cart/converted
  property_count: 0
  slug: bigcommerce-store-cart-converted
- name: store/cart/couponApplied
  property_count: 0
  slug: bigcommerce-store-cart-couponapplied
- name: store/cart/created
  property_count: 0
  slug: bigcommerce-store-cart-created
- name: store/cart/deleted
  property_count: 0
  slug: bigcommerce-store-cart-deleted
- name: store/cart/lineItem/created
  property_count: 0
  slug: bigcommerce-store-cart-lineitem-created
- name: store/cart/lineItem/deleted
  property_count: 0
  slug: bigcommerce-store-cart-lineitem-deleted
- name: store/cart/lineItem/updated
  property_count: 0
  slug: bigcommerce-store-cart-lineitem-updated
- name: store/cart/lineItem/*
  property_count: 0
  slug: bigcommerce-store-cart-lineitem-wildcard
- name: store/cart/updated
  property_count: 0
  slug: bigcommerce-store-cart-updated
- name: store/cart/*
  property_count: 0
  slug: bigcommerce-store-cart-wildcard
- name: store/category/created
  property_count: 0
  slug: bigcommerce-store-category-created
- name: store/category/deleted
  property_count: 0
  slug: bigcommerce-store-category-deleted
- name: store/category/updated
  property_count: 0
  slug: bigcommerce-store-category-updated
- name: store/category/*
  property_count: 0
  slug: bigcommerce-store-category-wildcard
- name: store/channel/created
  property_count: 0
  slug: bigcommerce-store-channel-created
- name: store/channel/updated
  property_count: 0
  slug: bigcommerce-store-channel-updated
- name: store/channel/*
  property_count: 0
  slug: bigcommerce-store-channel-wildcard
- name: store/customer/address/created
  property_count: 0
  slug: bigcommerce-store-customer-address-created
- name: store/customer/address/deleted
  property_count: 0
  slug: bigcommerce-store-customer-address-deleted
- name: store/customer/address/updated
  property_count: 0
  slug: bigcommerce-store-customer-address-updated
- name: store/customer/created
  property_count: 0
  slug: bigcommerce-store-customer-created
- name: store/customer/deleted
  property_count: 0
  slug: bigcommerce-store-customer-deleted
- name: store/customer/payment/instrument/default/updated
  property_count: 0
  slug: bigcommerce-store-customer-payment-instrument-default-updated
- name: store/customer/updated
  property_count: 0
  slug: bigcommerce-store-customer-updated
- name: store/customer/*
  property_count: 0
  slug: bigcommerce-store-customer-wildcard
- name: store/information/updated
  property_count: 0
  slug: bigcommerce-store-information-updated
- name: store/order/archived
  property_count: 0
  slug: bigcommerce-store-order-archived
- name: store/order/created
  property_count: 0
  slug: bigcommerce-store-order-created
- name: store/order/message/created
  property_count: 0
  slug: bigcommerce-store-order-message-created
- name: store/order/refund/created
  property_count: 0
  slug: bigcommerce-store-order-refund-created
- name: store/order/statusUpdated
  property_count: 0
  slug: bigcommerce-store-order-statusupdated
- name: store/order/updated
  property_count: 0
  slug: bigcommerce-store-order-updated
- name: store/order/*
  property_count: 0
  slug: bigcommerce-store-order-wildcard
- name: store/product/created
  property_count: 0
  slug: bigcommerce-store-product-created
- name: store/product/deleted
  property_count: 0
  slug: bigcommerce-store-product-deleted
- name: store/product/inventory/order/updated
  property_count: 0
  slug: bigcommerce-store-product-inventory-order-updated
- name: store/product/inventory/updated
  property_count: 0
  slug: bigcommerce-store-product-inventory-updated
- name: store/product/updated
  property_count: 0
  slug: bigcommerce-store-product-updated
- name: store/product/*
  property_count: 0
  slug: bigcommerce-store-product-wildcard
- name: store/shipment/created
  property_count: 0
  slug: bigcommerce-store-shipment-created
- name: store/shipment/deleted
  property_count: 0
  slug: bigcommerce-store-shipment-deleted
- name: store/shipment/updated
  property_count: 0
  slug: bigcommerce-store-shipment-updated
- name: store/shipment/*
  property_count: 0
  slug: bigcommerce-store-shipment-wildcard
- name: store/sku/created
  property_count: 0
  slug: bigcommerce-store-sku-created
- name: store/sku/deleted
  property_count: 0
  slug: bigcommerce-store-sku-deleted
- name: store/sku/inventory/order/updated
  property_count: 0
  slug: bigcommerce-store-sku-inventory-order-updated
- name: store/sku/inventory/updated
  property_count: 0
  slug: bigcommerce-store-sku-inventory-updated
- name: store/sku/updated
  property_count: 0
  slug: bigcommerce-store-sku-updated
- name: store/sku/*
  property_count: 0
  slug: bigcommerce-store-sku-wildcard
- name: store/subscriber/created
  property_count: 0
  slug: bigcommerce-store-subscriber-created
- name: store/subscriber/deleted
  property_count: 0
  slug: bigcommerce-store-subscriber-deleted
- name: store/subscriber/updated
  property_count: 0
  slug: bigcommerce-store-subscriber-updated
- name: store/subscriber/*
  property_count: 0
  slug: bigcommerce-store-subscriber-wildcard
- name: StoreCredit
  property_count: 1
  slug: bigcommerce-storecredit
- name: StoredBankAccount
  property_count: 2
  slug: bigcommerce-storedbankaccount
- name: Stored Card
  property_count: 3
  slug: bigcommerce-storedcard
- name: StoredPayPalAccount
  property_count: 2
  slug: bigcommerce-storedpaypalaccount
- name: StorefrontCategorySettings
  property_count: 3
  slug: bigcommerce-storefrontcategorysettings
- name: StorefrontProductSettings
  property_count: 12
  slug: bigcommerce-storefrontproductsettings
- name: StorefrontSearchSettings
  property_count: 4
  slug: bigcommerce-storefrontsearchsettings
- name: StorefrontSecuritySettings
  property_count: 4
  slug: bigcommerce-storefrontsecuritysettings
- name: ''
  property_count: 3
  slug: bigcommerce-storefrontstatus
- name: Store Information
  property_count: 38
  slug: bigcommerce-storeinformation
- name: Store Profile
  property_count: 5
  slug: bigcommerce-storeprofile
- name: subscriber_Base
  property_count: 6
  slug: bigcommerce-subscriber-base
- name: subscriber_Full
  property_count: 0
  slug: bigcommerce-subscriber-full
- name: subscriber_Post
  property_count: 0
  slug: bigcommerce-subscriber-post
- name: subscriber_Put
  property_count: 0
  slug: bigcommerce-subscriber-put
- name: Subscriber
  property_count: 0
  slug: bigcommerce-subscriber
- name: Subscription
  property_count: 7
  slug: bigcommerce-subscription
- name: SubscriptionRequest
  property_count: 3
  slug: bigcommerce-subscriptionrequest
- name: Success
  property_count: 0
  slug: bigcommerce-success
- name: SuccessBatchResponse
  property_count: 2
  slug: bigcommerce-successbatchresponse
- name: SuccessNoContentResponse
  property_count: 1
  slug: bigcommerce-successnocontentresponse
- name: SuccessResponse
  property_count: 2
  slug: bigcommerce-successresponse
- name: SystemLog
  property_count: 7
  slug: bigcommerce-systemlog
- name: Tax_Rate
  property_count: 6
  slug: bigcommerce-tax-rate
- name: Tax_RatePOST
  property_count: 5
  slug: bigcommerce-tax-ratepost
- name: Tax_RatePUT
  property_count: 6
  slug: bigcommerce-tax-rateput
- name: Tax_Settings
  property_count: 7
  slug: bigcommerce-tax-settings
- name: Tax_Zone
  property_count: 5
  slug: bigcommerce-tax-zone
- name: Tax_ZonePOST
  property_count: 4
  slug: bigcommerce-tax-zonepost
- name: Tax_ZonePUT
  property_count: 5
  slug: bigcommerce-tax-zoneput
- name: taxClass_Full
  property_count: 4
  slug: bigcommerce-taxclass-full
- name: TaxClass
  property_count: 3
  slug: bigcommerce-taxclass
- name: Tax Exempt (Order Level)
  property_count: 4
  slug: bigcommerce-taxexemptitem
- name: TaxPrice
  property_count: 4
  slug: bigcommerce-taxprice
- name: TaxZone
  property_count: 5
  slug: bigcommerce-taxzone
- name: Template
  property_count: 3
  slug: bigcommerce-template
- name: Theme
  property_count: 4
  slug: bigcommerce-theme
- name: themeConfiguration_Full
  property_count: 6
  slug: bigcommerce-themeconfiguration-full
- name: themeConfiguration_Write
  property_count: 2
  slug: bigcommerce-themeconfiguration-write
- name: themeRegion
  property_count: 1
  slug: bigcommerce-themeregion
- name: Theme Response
  property_count: 2
  slug: bigcommerce-themeresponse
- name: Themes Collection Meta
  property_count: 1
  slug: bigcommerce-themescollectionmeta
- name: Themes Collection Response
  property_count: 2
  slug: bigcommerce-themescollectionresponse
- name: timeStamp_Full
  property_count: 1
  slug: bigcommerce-timestamp-full
- name: timeZone
  property_count: 5
  slug: bigcommerce-timezone
- name: Token_Base
  property_count: 1
  slug: bigcommerce-token-base
- name: Token_Full
  property_count: 2
  slug: bigcommerce-token-full
- name: Tokenized Card
  property_count: 6
  slug: bigcommerce-tokenizedcard
- name: TokenPostImpersonation
  property_count: 2
  slug: bigcommerce-tokenpostimpersonation
- name: TokenPostSimple
  property_count: 1
  slug: bigcommerce-tokenpostsimple
- name: Total
  property_count: 0
  slug: bigcommerce-total
- name: Transaction_Post
  property_count: 13
  slug: bigcommerce-transaction-post
- name: ''
  property_count: 0
  slug: bigcommerce-transaction
- name: Transit Time Object
  property_count: 2
  slug: bigcommerce-transittimeobject
- name: TranslationDefinition
  property_count: 2
  slug: bigcommerce-translationdefinition
- name: Tree ID
  property_count: 0
  slug: bigcommerce-tree-id
- name: Tree
  property_count: 3
  slug: bigcommerce-tree
- name: typeBlog
  property_count: 0
  slug: bigcommerce-typeblog
- name: typeContactForm
  property_count: 0
  slug: bigcommerce-typecontactform
- name: typeFeed
  property_count: 0
  slug: bigcommerce-typefeed
- name: typeLink
  property_count: 0
  slug: bigcommerce-typelink
- name: typePage
  property_count: 0
  slug: bigcommerce-typepage
- name: typeRaw
  property_count: 0
  slug: bigcommerce-typeraw
- name: UpdateCategories
  property_count: 0
  slug: bigcommerce-updatecategories
- name: UpdateChannelReq
  property_count: 6
  slug: bigcommerce-updatechannelreq
- name: Update Consignment Request
  property_count: 4
  slug: bigcommerce-updateconsignmentrequest
- name: UpdateMultipleListingsReq
  property_count: 0
  slug: bigcommerce-updatemultiplelistingsreq
- name: UpdateReturnStatuses
  property_count: 0
  slug: bigcommerce-updatereturnstatuses
- name: UpdateReturnStatusesRequest
  property_count: 0
  slug: bigcommerce-updatereturnstatusesrequest
- name: UpsertListingWithListingIdReq
  property_count: 7
  slug: bigcommerce-upsertlistingwithlistingidreq
- name: UpsertListingWithoutListingIdReq
  property_count: 6
  slug: bigcommerce-upsertlistingwithoutlistingidreq
- name: UpsertMultipleChannelsCurrencyAssignmentsReq
  property_count: 0
  slug: bigcommerce-upsertmultiplechannelscurrencyassignmentsreq
- name: Url
  property_count: 2
  slug: bigcommerce-url
- name: ValidateCustomerCredentialsObject
  property_count: 3
  slug: bigcommerce-validatecustomercredentialsobject
- name: ValidateCustomerCredentialsResponseObject
  property_count: 2
  slug: bigcommerce-validatecustomercredentialsresponseobject
- name: VariantId
  property_count: 0
  slug: bigcommerce-variantid
- name: VariantState
  property_count: 0
  slug: bigcommerce-variantstate
- name: Variation
  property_count: 4
  slug: bigcommerce-variation
- name: views
  property_count: 1
  slug: bigcommerce-views
- name: webhook_Base
  property_count: 5
  slug: bigcommerce-webhook-base
- name: ''
  property_count: 0
  slug: bigcommerce-webhook-callback-base
- name: webhook_Full
  property_count: 0
  slug: bigcommerce-webhook-full
- name: webhook_Put
  property_count: 5
  slug: bigcommerce-webhook-put
- name: Weight Value
  property_count: 2
  slug: bigcommerce-weightvalue
- name: Which Theme To Download
  property_count: 0
  slug: bigcommerce-whichthemetodownload
- name: widget_Base
  property_count: 3
  slug: bigcommerce-widget-base
- name: widget_Full
  property_count: 0
  slug: bigcommerce-widget-full
- name: widget_Post
  property_count: 5
  slug: bigcommerce-widget-post
- name: widget_Put
  property_count: 0
  slug: bigcommerce-widget-put
- name: ''
  property_count: 0
  slug: bigcommerce-widgetschema
- name: widgetSchemaArray
  property_count: 7
  slug: bigcommerce-widgetschemaarray
- name: widgetSchemaConditional
  property_count: 3
  slug: bigcommerce-widgetschemaconditional
- name: widgetSchemaHidden
  property_count: 2
  slug: bigcommerce-widgetschemahidden
- name: widgetSchemaSetting_Base
  property_count: 6
  slug: bigcommerce-widgetschemasetting-base
- name: widgetSchemaTab
  property_count: 3
  slug: bigcommerce-widgetschematab
- name: widgetSchemaTabSections
  property_count: 2
  slug: bigcommerce-widgetschematabsections
- name: widgetSchemaTabSectionsSettings
  property_count: 0
  slug: bigcommerce-widgetschematabsectionssettings
- name: widgetTemplate_Base
  property_count: 4
  slug: bigcommerce-widgettemplate-base
- name: widgetTemplate_Full
  property_count: 0
  slug: bigcommerce-widgettemplate-full
- name: widgetTemplate_Post
  property_count: 5
  slug: bigcommerce-widgettemplate-post
- name: widgetTemplate_Put
  property_count: 0
  slug: bigcommerce-widgettemplate-put
- name: WidgetTemplatePreview
  property_count: 1
  slug: bigcommerce-widgettemplatepreview
- name: ''
  property_count: 1
  slug: bigcommerce-widgettemplatepreviewresponse
- name: wishlist_Full
  property_count: 6
  slug: bigcommerce-wishlist-full
- name: wishlist_Post
  property_count: 4
  slug: bigcommerce-wishlist-post
- name: wishlist_Put
  property_count: 4
  slug: bigcommerce-wishlist-put
- name: wishlistItem_Full
  property_count: 3
  slug: bigcommerce-wishlistitem-full
- name: wishlistItem_Post
  property_count: 1
  slug: bigcommerce-wishlistitem-post
- name: wrapping_type
  property_count: 0
  slug: bigcommerce-wrapping-type
- name: Collection Meta
  property_count: 3
  slug: bigcommerce-writecollectionpartialsuccessmeta
- name: Collection Meta
  property_count: 3
  slug: bigcommerce-writecollectionsuccessmeta
- name: ZoneCheck
  property_count: 4
  slug: bigcommerce-zonecheck
- name: Zone Options Instance
  property_count: 0
  slug: bigcommerce-zoneoptionsinstance
json_structures:
- name: Bigcommerce Structure
  property_count: 0
  slug: bigcommerce-structure
layout: provider
modified: '2026-05-30'
name: BigCommerce
nav: Providers
network: true
overview: 'BigCommerce publishes 153 APIs on the [APIs.io](https://apis.io/) network, including Abandoned Cart Emails API, Abandoned Cart Settings API, Abandoned Carts API, and 150 more. Tagged areas include E-Commerce, Retail, Catalog, Order, and Checkout.


  The BigCommerce catalog on APIs.io includes 1 event-driven AsyncAPI specification and 3 Spectral governance rulesets.


  BigCommerce''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Bigcommerce Plans Pricing
  plan_count: 4
  slug: bigcommerce-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Bigcommerce Rate Limits
  slug: bigcommerce-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: BigCommerce API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: bigcommerce-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: BigCommerce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bigcommerce-jsonschema-spectral-rules
- effective_rule_count: 72
  extends:
  - spectral:oas
  name: BigCommerce API Rules
  rule_count: 31
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 23
  slug: bigcommerce-spectral-rules
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 70.4
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 153
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigcommerce/refs/heads/main/screenshots/bigcommerce-2026-06-20T173231.png
security:
- kind: authentication
  name: Bigcommerce Authentication
  slug: bigcommerce-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bigcommerce Domain Security
  slug: bigcommerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bigcommerce Trust Center
  slug: bigcommerce-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR, FIPS 140
slug: bigcommerce
tags:
- E-Commerce
- Retail
- Catalog
- Order
- Checkout
- Payments
- Software-as-a-Service
use_cases:
- description: Build custom storefronts powered by BigCommerce APIs and GraphQL.
  name: Headless Commerce
- description: Sync orders, inventory, and customers with ERP systems via API.
  name: ERP Integration
- description: List products and sync inventory across Amazon, eBay, and other marketplaces.
  name: Marketplace Selling
- description: Replace the standard checkout with a branded custom checkout experience.
  name: Custom Checkout
- description: Build B2B wholesale portals with customer group pricing and quote workflows.
  name: Wholesale Portals
- description: Automate order fulfillment with warehouse management and 3PL systems.
  name: Order Fulfillment Automation
website: https://developer.bigcommerce.com/
---
