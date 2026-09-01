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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 739
  human_in_the_loop: 6
  name: Shopify Agentic Access
  operation_count: 1547
  slug: shopify-agentic-access
  summary_line: 1547 operations · 739 acting · 6 human-in-the-loop
api_count: 3
apis:
- description: The GraphQL Admin API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillment, and more. GraphQL is th
  name: Shopify GraphQL Admin API
  slug: graphql-admin-api
- description: The Storefront API is a GraphQL API that provides commerce primitives to build custom, scalable, and performant shopping experiences on any platform, including the web, apps, and games. It enables cus
  name: Shopify Storefront API
  slug: storefront-api
- description: The Customer Account API offers a secure way to access private customer-scoped data, enabling you to build personalized, customer-authenticated experiences in your custom storefronts or apps. Customer
  name: Shopify Customer Account API
  slug: customer-account-api
- description: The Partner API provides access to data in the Partners Dashboard, including transactions that impact your earnings, app events, and for participating partners, Experts Marketplace opportunities. It i
  name: Shopify Partner API
  slug: partner-api
- description: The Payments Apps API enables approved Shopify Payments Partners to access their Shopify Payments account and payments app configuration data. It provides access to payment sessions and allows buildin
  name: Shopify Payments Apps API
  slug: payments-apps-api
- description: Liquid is a template language created by Shopify and available as an open source project on GitHub. The Liquid reference documents the tags, filters, and objects that you can use to build Shopify them
  name: Shopify Liquid API
  slug: liquid-api
- description: Shopify Functions allow developers to customize the backend logic that powers parts of Shopify. Functions are compiled to WebAssembly and enable custom discounts, payment customizations, delivery cust
  name: Shopify Functions API
  slug: functions-api
- description: The Discount Function API enables developers to create a single discount that applies to cart lines, order subtotals, and shipping rates. It replaces the previous separate Product, Order, and Shipping
  name: Shopify Discount Function API
  slug: discount-function-api
- description: Shopify webhooks enable apps to receive notifications about particular events in a shop. They are useful for keeping your app in sync with Shopify data or as a trigger to perform additional actions af
  name: Shopify Webhooks API
  slug: webhooks-api
- description: Shopify App Bridge enables apps to render UI in the Shopify app home surface and seamlessly integrate with the Shopify admin. It provides APIs for navigation menus, save bars, title bars, toast notifi
  name: Shopify App Bridge
  slug: app-bridge
- description: The App Home API provides the surface where apps render their main UI within the Shopify admin. It supports Polaris web components for building consistent, accessible interfaces that integrate seamles
  name: Shopify App Home API
  slug: app-home-api
- description: Checkout UI extensions let app developers build custom functionality that merchants can install at defined points in the checkout flow, including product information, shipping, payment, order summary,
  name: Shopify Checkout UI Extensions API
  slug: checkout-ui-extensions-api
- description: Multipass login is for store owners who have a separate website and a Shopify store, enabling seamless single sign-on by redirecting users and automatically logging them in. Requires a Shopify Plus pl
  name: Shopify Multipass API
  slug: multipass-api
- description: POS UI extensions enable app developers to build custom functionality for Shopify Point of Sale. Extensions can add functionality to the cart, post- purchase, and other POS surfaces for in-person reta
  name: Shopify POS UI Extensions API
  slug: pos-ui-extensions-api
- description: Admin UI extensions allow developers to extend the Shopify admin with custom UI components. Extensions can render in product details, order details, customer details, and other admin surfaces.
  name: Shopify Admin Extensions API
  slug: admin-extensions-api
- description: Hydrogen is Shopify's React-based framework for building custom storefronts powered by the Storefront API. It provides commerce-optimized components, hooks, and utilities for building fast, dynamic he
  name: Shopify Hydrogen
  slug: hydrogen
- description: 'Polaris is Shopify''s unified UI framework built on web components for delivering a consistent experience across the platform. It provides a library of UI components, tokens, and icons that developers '
  name: Shopify Polaris
  slug: polaris
- description: Shopify CLI is a command-line tool that helps developers create Shopify apps, themes, and custom storefronts. It accelerates development with scaffolding, local development servers, and deployment too
  name: Shopify CLI
  slug: shopify-cli
- description: The About API from Shopify — 6 operation(s) for about.
  name: Shopify About API
  slug: shopify-about-api
- description: Manage access scopes and tokens
  name: Shopify Access API
  slug: shopify-access-api
- description: The Account API from Shopify — 12 operation(s) for account.
  name: Shopify Account API
  slug: shopify-account-api
- description: The Accounts API from Shopify — 6 operation(s) for accounts.
  name: Shopify Accounts API
  slug: shopify-accounts-api
- description: The Activation API from Shopify — 6 operation(s) for activation.
  name: Shopify Activation API
  slug: shopify-activation-api
- description: The Active API from Shopify — 6 operation(s) for active.
  name: Shopify Active API
  slug: shopify-active-api
- description: The Address API from Shopify — 30 operation(s) for address.
  name: Shopify Address API
  slug: shopify-address-api
- description: The Addresses API from Shopify — 12 operation(s) for addresses.
  name: Shopify Addresses API
  slug: shopify-addresses-api
- description: The Admin API from Shopify — 6 operation(s) for admin.
  name: Shopify Admin API
  slug: shopify-admin-api
- description: The All API from Shopify — 107 operation(s) for all.
  name: Shopify All API
  slug: shopify-all-api
- description: The Amount API from Shopify — 6 operation(s) for amount.
  name: Shopify Amount API
  slug: shopify-amount-api
- description: The Another API from Shopify — 12 operation(s) for another.
  name: Shopify Another API
  slug: shopify-another-api
- description: The Applications API from Shopify — 86 operation(s) for applications.
  name: Shopify Applications API
  slug: shopify-applications-api
- description: The Approves API from Shopify — 1 operation(s) for approves.
  name: Shopify Approves API
  slug: shopify-approves-api
- description: The Article API from Shopify — 20 operation(s) for article.
  name: Shopify Article API
  slug: shopify-article-api
- description: The Assets API from Shopify — 6 operation(s) for assets.
  name: Shopify Assets API
  slug: shopify-assets-api
- description: The Associated API from Shopify — 31 operation(s) for associated.
  name: Shopify Associated API
  slug: shopify-associated-api
- description: The Authenticated API from Shopify — 2 operation(s) for authenticated.
  name: Shopify Authenticated API
  slug: shopify-authenticated-api
- description: The Authors API from Shopify — 6 operation(s) for authors.
  name: Shopify Authors API
  slug: shopify-authors-api
- description: The Available API from Shopify — 6 operation(s) for available.
  name: Shopify Available API
  slug: shopify-available-api
- description: The Balance API from Shopify — 7 operation(s) for balance.
  name: Shopify Balance API
  slug: shopify-balance-api
- description: The Belong API from Shopify — 6 operation(s) for belong.
  name: Shopify Belong API
  slug: shopify-belong-api
- description: The Belonging API from Shopify — 12 operation(s) for belonging.
  name: Shopify Belonging API
  slug: shopify-belonging-api
- description: The Blog API from Shopify — 14 operation(s) for blog.
  name: Shopify Blog API
  slug: shopify-blog-api
- description: The Blogs API from Shopify — 2 operation(s) for blogs.
  name: Shopify Blogs API
  slug: shopify-blogs-api
- description: The Bulk API from Shopify — 6 operation(s) for bulk.
  name: Shopify Bulk API
  slug: shopify-bulk-api
- description: The Calls API from Shopify — 2 operation(s) for calls.
  name: Shopify Calls API
  slug: shopify-calls-api
- description: The Cancel API from Shopify — 6 operation(s) for cancel.
  name: Shopify Cancel API
  slug: shopify-cancel-api
- description: The Cancels API from Shopify — 12 operation(s) for cancels.
  name: Shopify Cancels API
  slug: shopify-cancels-api
- description: The Card API from Shopify — 24 operation(s) for card.
  name: Shopify Card API
  slug: shopify-card-api
- description: The Cards API from Shopify — 18 operation(s) for cards.
  name: Shopify Cards API
  slug: shopify-cards-api
- description: The Carrier API from Shopify — 12 operation(s) for carrier.
  name: Shopify Carrier API
  slug: shopify-carrier-api
- description: Manage the shopping cart
  name: Shopify Cart API
  slug: shopify-cart-api
- description: The Charge API from Shopify — 42 operation(s) for charge.
  name: Shopify Charge API
  slug: shopify-charge-api
- description: The Charges API from Shopify — 18 operation(s) for charges.
  name: Shopify Charges API
  slug: shopify-charges-api
- description: The Checkout API from Shopify — 36 operation(s) for checkout.
  name: Shopify Checkout API
  slug: shopify-checkout-api
- description: The Checkouts API from Shopify — 6 operation(s) for checkouts.
  name: Shopify Checkouts API
  slug: shopify-checkouts-api
- description: The Code API from Shopify — 36 operation(s) for code.
  name: Shopify Code API
  slug: shopify-code-api
- description: The Collect API from Shopify — 6 operation(s) for collect.
  name: Shopify Collect API
  slug: shopify-collect-api
- description: The Collection API from Shopify — 66 operation(s) for collection.
  name: Shopify Collection API
  slug: shopify-collection-api
- description: Retrieve collection data
  name: Shopify Collections API
  slug: shopify-collections-api
- description: The Comments API from Shopify — 8 operation(s) for comments.
  name: Shopify Comments API
  slug: shopify-comments-api
- description: The Complete API from Shopify — 6 operation(s) for complete.
  name: Shopify Complete API
  slug: shopify-complete-api
- description: The Configuration API from Shopify — 6 operation(s) for configuration.
  name: Shopify Configuration API
  slug: shopify-configuration-api
- description: The Connects API from Shopify — 6 operation(s) for connects.
  name: Shopify Connects API
  slug: shopify-connects-api
- description: The Contains API from Shopify — 6 operation(s) for contains.
  name: Shopify Contains API
  slug: shopify-contains-api
- description: The Count API from Shopify — 121 operation(s) for count.
  name: Shopify Count API
  slug: shopify-count-api
- description: The Countries API from Shopify — 12 operation(s) for countries.
  name: Shopify Countries API
  slug: shopify-countries-api
- description: The Country API from Shopify — 18 operation(s) for country.
  name: Shopify Country API
  slug: shopify-country-api
- description: The Counts API from Shopify — 6 operation(s) for counts.
  name: Shopify Counts API
  slug: shopify-counts-api
- description: The County API from Shopify — 6 operation(s) for county.
  name: Shopify County API
  slug: shopify-county-api
- description: The Create API from Shopify — 34 operation(s) for create.
  name: Shopify Create API
  slug: shopify-create-api
- description: The Creation API from Shopify — 18 operation(s) for creation.
  name: Shopify Creation API
  slug: shopify-creation-api
- description: The Credit API from Shopify — 12 operation(s) for credit.
  name: Shopify Credit API
  slug: shopify-credit-api
- description: The Currencies API from Shopify — 6 operation(s) for currencies.
  name: Shopify Currencies API
  slug: shopify-currencies-api
- description: The Current API from Shopify — 6 operation(s) for current.
  name: Shopify Current API
  slug: shopify-current-api
- description: The Custom API from Shopify — 24 operation(s) for custom.
  name: Shopify Custom API
  slug: shopify-custom-api
- description: Manage manual collections
  name: Shopify Custom Collections API
  slug: shopify-custom-collections-api
- description: Manage customer addresses
  name: Shopify Customer Addresses API
  slug: shopify-customer-addresses-api
- description: The Customer API from Shopify — 30 operation(s) for customer.
  name: Shopify Customer API
  slug: shopify-customer-api
- description: Manage customer records
  name: Shopify Customers API
  slug: shopify-customers-api
- description: The Date API from Shopify — 8 operation(s) for date.
  name: Shopify Date API
  slug: shopify-date-api
- description: The Days API from Shopify — 8 operation(s) for days.
  name: Shopify Days API
  slug: shopify-days-api
- description: The Deletes API from Shopify — 108 operation(s) for deletes.
  name: Shopify Deletes API
  slug: shopify-deletes-api
- description: The Disables API from Shopify — 6 operation(s) for disables.
  name: Shopify Disables API
  slug: shopify-disables-api
- description: The Discount API from Shopify — 36 operation(s) for discount.
  name: Shopify Discount API
  slug: shopify-discount-api
- description: The Dispute API from Shopify — 1 operation(s) for dispute.
  name: Shopify Dispute API
  slug: shopify-dispute-api
- description: The Disputes API from Shopify — 2 operation(s) for disputes.
  name: Shopify Disputes API
  slug: shopify-disputes-api
- description: The Enabled API from Shopify — 12 operation(s) for enabled.
  name: Shopify Enabled API
  slug: shopify-enabled-api
- description: The Endpoint API from Shopify — 8 operation(s) for endpoint.
  name: Shopify Endpoint API
  slug: shopify-endpoint-api
- description: The Events API from Shopify — 30 operation(s) for events.
  name: Shopify Events API
  slug: shopify-events-api
- description: The Existing API from Shopify — 78 operation(s) for existing.
  name: Shopify Existing API
  slug: shopify-existing-api
- description: The Files API from Shopify — 6 operation(s) for files.
  name: Shopify Files API
  slug: shopify-files-api
- description: The Format API from Shopify — 2 operation(s) for format.
  name: Shopify Format API
  slug: shopify-format-api
- description: The Fulfillment API from Shopify — 155 operation(s) for fulfillment.
  name: Shopify Fulfillment API
  slug: shopify-fulfillment-api
- description: Manage fulfillment workflows
  name: Shopify Fulfillment Orders API
  slug: shopify-fulfillment-orders-api
- description: Manage order fulfillments
  name: Shopify Fulfillments API
  slug: shopify-fulfillments-api
- description: The Generate API from Shopify — 6 operation(s) for generate.
  name: Shopify Generate API
  slug: shopify-generate-api
- description: The Get API from Shopify — 28 operation(s) for get.
  name: Shopify Get API
  slug: shopify-get-api
- description: The Gift API from Shopify — 30 operation(s) for gift.
  name: Shopify Gift API
  slug: shopify-gift-api
- description: The Have API from Shopify — 6 operation(s) for have.
  name: Shopify Have API
  slug: shopify-have-api
- description: The Holds API from Shopify — 1 operation(s) for holds.
  name: Shopify Holds API
  slug: shopify-holds-api
- description: The Identifiers API from Shopify — 75 operation(s) for identifiers.
  name: Shopify Identifiers API
  slug: shopify-identifiers-api
- description: The Image API from Shopify — 18 operation(s) for image.
  name: Shopify Image API
  slug: shopify-image-api
- description: The Images API from Shopify — 18 operation(s) for images.
  name: Shopify Images API
  slug: shopify-images-api
- description: The Information API from Shopify — 24 operation(s) for information.
  name: Shopify Information API
  slug: shopify-information-api
- description: The Inventory API from Shopify — 43 operation(s) for inventory.
  name: Shopify Inventory API
  slug: shopify-inventory-api
- description: Manage inventory item records
  name: Shopify Inventory Items API
  slug: shopify-inventory-items-api
- description: Manage inventory quantities at locations
  name: Shopify Inventory Levels API
  slug: shopify-inventory-levels-api
- description: The Invites API from Shopify — 6 operation(s) for invites.
  name: Shopify Invites API
  slug: shopify-invites-api
- description: The Issued API from Shopify — 6 operation(s) for issued.
  name: Shopify Issued API
  slug: shopify-issued-api
- description: The Item API from Shopify — 30 operation(s) for item.
  name: Shopify Item API
  slug: shopify-item-api
- description: The Items API from Shopify — 12 operation(s) for items.
  name: Shopify Items API
  slug: shopify-items-api
- description: The Jobs API from Shopify — 18 operation(s) for jobs.
  name: Shopify Jobs API
  slug: shopify-jobs-api
- description: The Keys API from Shopify — 6 operation(s) for keys.
  name: Shopify Keys API
  slug: shopify-keys-api
- description: The Levels API from Shopify — 31 operation(s) for levels.
  name: Shopify Levels API
  slug: shopify-levels-api
- description: The Line API from Shopify — 6 operation(s) for line.
  name: Shopify Line API
  slug: shopify-line-api
- description: The Listing API from Shopify — 9 operation(s) for listing.
  name: Shopify Listing API
  slug: shopify-listing-api
- description: The Listings API from Shopify — 9 operation(s) for listings.
  name: Shopify Listings API
  slug: shopify-listings-api
- description: The Lists API from Shopify — 291 operation(s) for lists.
  name: Shopify Lists API
  slug: shopify-lists-api
- description: The Location API from Shopify — 48 operation(s) for location.
  name: Shopify Location API
  slug: shopify-location-api
- description: Retrieve store locations
  name: Shopify Locations API
  slug: shopify-locations-api
- description: The Make API from Shopify — 6 operation(s) for make.
  name: Shopify Make API
  slug: shopify-make-api
- description: The Managed API from Shopify — 6 operation(s) for managed.
  name: Shopify Managed API
  slug: shopify-managed-api
- description: The Many API from Shopify — 6 operation(s) for many.
  name: Shopify Many API
  slug: shopify-many-api
- description: The Mark API from Shopify — 12 operation(s) for mark.
  name: Shopify Mark API
  slug: shopify-mark-api
- description: The Match API from Shopify — 12 operation(s) for match.
  name: Shopify Match API
  slug: shopify-match-api
- description: The Merchant API from Shopify — 6 operation(s) for merchant.
  name: Shopify Merchant API
  slug: shopify-merchant-api
- description: The Metafields API from Shopify — 12 operation(s) for metafields.
  name: Shopify Metafields API
  slug: shopify-metafields-api
- description: The Modifies API from Shopify — 6 operation(s) for modifies.
  name: Shopify Modifies API
  slug: shopify-modifies-api
- description: The Modify API from Shopify — 12 operation(s) for modify.
  name: Shopify Modify API
  slug: shopify-modify-api
- description: The Move API from Shopify — 6 operation(s) for move.
  name: Shopify Move API
  slug: shopify-move-api
- description: The Moves API from Shopify — 6 operation(s) for moves.
  name: Shopify Moves API
  slug: shopify-moves-api
- description: The Multiple API from Shopify — 6 operation(s) for multiple.
  name: Shopify Multiple API
  slug: shopify-multiple-api
- description: The Number API from Shopify — 6 operation(s) for number.
  name: Shopify Number API
  slug: shopify-number-api
- description: The Numbers API from Shopify — 1 operation(s) for numbers.
  name: Shopify Numbers API
  slug: shopify-numbers-api
- description: The Open API from Shopify — 6 operation(s) for open.
  name: Shopify Open API
  slug: shopify-open-api
- description: The Operations API from Shopify — 6 operation(s) for operations.
  name: Shopify Operations API
  slug: shopify-operations-api
- description: The Order API from Shopify — 129 operation(s) for order.
  name: Shopify Order API
  slug: shopify-order-api
- description: The Ordered API from Shopify — 9 operation(s) for ordered.
  name: Shopify Ordered API
  slug: shopify-ordered-api
- description: Manage orders
  name: Shopify Orders API
  slug: shopify-orders-api
- description: The Particular API from Shopify — 6 operation(s) for particular.
  name: Shopify Particular API
  slug: shopify-particular-api
- description: The Past API from Shopify — 8 operation(s) for past.
  name: Shopify Past API
  slug: shopify-past-api
- description: The Payments API from Shopify — 18 operation(s) for payments.
  name: Shopify Payments API
  slug: shopify-payments-api
- description: The Payouts API from Shopify — 6 operation(s) for payouts.
  name: Shopify Payouts API
  slug: shopify-payouts-api
- description: The Policies API from Shopify — 6 operation(s) for policies.
  name: Shopify Policies API
  slug: shopify-policies-api
- description: Search suggestions for products, collections, pages, and articles
  name: Shopify Predictive Search API
  slug: shopify-predictive-search-api
- description: The Previously API from Shopify — 1 operation(s) for previously.
  name: Shopify Previously API
  slug: shopify-previously-api
- description: The Private API from Shopify — 2 operation(s) for private.
  name: Shopify Private API
  slug: shopify-private-api
- description: The Product API from Shopify — 54 operation(s) for product.
  name: Shopify Product API
  slug: shopify-product-api
- description: Manage images associated with products
  name: Shopify Product Images API
  slug: shopify-product-images-api
- description: Get product recommendations
  name: Shopify Product Recommendations API
  slug: shopify-product-recommendations-api
- description: Manage product variants
  name: Shopify Product Variants API
  slug: shopify-product-variants-api
- description: Manage products in a Shopify store
  name: Shopify Products API
  slug: shopify-products-api
- description: The Progress API from Shopify — 6 operation(s) for progress.
  name: Shopify Progress API
  slug: shopify-progress-api
- description: The Providing API from Shopify — 6 operation(s) for providing.
  name: Shopify Providing API
  slug: shopify-providing-api
- description: The Province API from Shopify — 6 operation(s) for province.
  name: Shopify Province API
  slug: shopify-province-api
- description: The Public API from Shopify — 6 operation(s) for public.
  name: Shopify Public API
  slug: shopify-public-api
- description: The Publish API from Shopify — 9 operation(s) for publish.
  name: Shopify Publish API
  slug: shopify-publish-api
- description: The Published API from Shopify — 30 operation(s) for published.
  name: Shopify Published API
  slug: shopify-published-api
- description: The Queries API from Shopify — 12 operation(s) for queries.
  name: Shopify Queries API
  slug: shopify-queries-api
- description: The Rates API from Shopify — 6 operation(s) for rates.
  name: Shopify Rates API
  slug: shopify-rates-api
- description: The Ready API from Shopify — 2 operation(s) for ready.
  name: Shopify Ready API
  slug: shopify-ready-api
- description: The Recurring API from Shopify — 18 operation(s) for recurring.
  name: Shopify Recurring API
  slug: shopify-recurring-api
- description: The Redirect API from Shopify — 12 operation(s) for redirect.
  name: Shopify Redirect API
  slug: shopify-redirect-api
- description: The Redirects API from Shopify — 12 operation(s) for redirects.
  name: Shopify Redirects API
  slug: shopify-redirects-api
- description: The Refund API from Shopify — 6 operation(s) for refund.
  name: Shopify Refund API
  slug: shopify-refund-api
- description: The Refunds API from Shopify — 6 operation(s) for refunds.
  name: Shopify Refunds API
  slug: shopify-refunds-api
- description: The Releases API from Shopify — 1 operation(s) for releases.
  name: Shopify Releases API
  slug: shopify-releases-api
- description: The Reports API from Shopify — 12 operation(s) for reports.
  name: Shopify Reports API
  slug: shopify-reports-api
- description: The Requests API from Shopify — 42 operation(s) for requests.
  name: Shopify Requests API
  slug: shopify-requests-api
- description: The Required API from Shopify — 8 operation(s) for required.
  name: Shopify Required API
  slug: shopify-required-api
- description: The Resource API from Shopify — 12 operation(s) for resource.
  name: Shopify Resource API
  slug: shopify-resource-api
- description: The Retrieves API from Shopify — 619 operation(s) for retrieves.
  name: Shopify Retrieves API
  slug: shopify-retrieves-api
- description: The Risk API from Shopify — 12 operation(s) for risk.
  name: Shopify Risk API
  slug: shopify-risk-api
- description: The Rules API from Shopify — 6 operation(s) for rules.
  name: Shopify Rules API
  slug: shopify-rules-api
- description: The Saved API from Shopify — 24 operation(s) for saved.
  name: Shopify Saved API
  slug: shopify-saved-api
- description: The Scheduled API from Shopify — 4 operation(s) for scheduled.
  name: Shopify Scheduled API
  slug: shopify-scheduled-api
- description: The Scopes API from Shopify — 1 operation(s) for scopes.
  name: Shopify Scopes API
  slug: shopify-scopes-api
- description: The Script API from Shopify — 18 operation(s) for script.
  name: Shopify Script API
  slug: shopify-script-api
- description: The Search API from Shopify — 18 operation(s) for search.
  name: Shopify Search API
  slug: shopify-search-api
- description: The Searches API from Shopify — 24 operation(s) for searches.
  name: Shopify Searches API
  slug: shopify-searches-api
- description: The Sends API from Shopify — 18 operation(s) for sends.
  name: Shopify Sends API
  slug: shopify-sends-api
- description: The Sent API from Shopify — 24 operation(s) for sent.
  name: Shopify Sent API
  slug: shopify-sent-api
- description: The Sessions API from Shopify — 6 operation(s) for sessions.
  name: Shopify Sessions API
  slug: shopify-sessions-api
- description: The Sets API from Shopify — 12 operation(s) for sets.
  name: Shopify Sets API
  slug: shopify-sets-api
- description: The Shipping API from Shopify — 12 operation(s) for shipping.
  name: Shopify Shipping API
  slug: shopify-shipping-api
- description: Retrieve shop configuration
  name: Shopify Shop API
  slug: shopify-shop-api
- description: The Single API from Shopify — 183 operation(s) for single.
  name: Shopify Single API
  slug: shopify-single-api
- description: The Smart API from Shopify — 24 operation(s) for smart.
  name: Shopify Smart API
  slug: shopify-smart-api
- description: Manage automated collections
  name: Shopify Smart Collections API
  slug: shopify-smart-collections-api
- description: The Spam API from Shopify — 2 operation(s) for spam.
  name: Shopify Spam API
  slug: shopify-spam-api
- description: The Specific API from Shopify — 78 operation(s) for specific.
  name: Shopify Specific API
  slug: shopify-specific-api
- description: The Storefront API from Shopify — 12 operation(s) for storefront.
  name: Shopify Storefront API
  slug: shopify-storefront-api
- description: The Subscriptions API from Shopify — 18 operation(s) for subscriptions.
  name: Shopify Subscriptions API
  slug: shopify-subscriptions-api
- description: The Summaries API from Shopify — 18 operation(s) for summaries.
  name: Shopify Summaries API
  slug: shopify-summaries-api
- description: The Tender API from Shopify — 6 operation(s) for tender.
  name: Shopify Tender API
  slug: shopify-tender-api
- description: The Theme API from Shopify — 18 operation(s) for theme.
  name: Shopify Theme API
  slug: shopify-theme-api
- description: The Themes API from Shopify — 6 operation(s) for themes.
  name: Shopify Themes API
  slug: shopify-themes-api
- description: The Time API from Shopify — 4 operation(s) for time.
  name: Shopify Time API
  slug: shopify-time-api
- description: The Tokens API from Shopify — 19 operation(s) for tokens.
  name: Shopify Tokens API
  slug: shopify-tokens-api
- description: The Topic API from Shopify — 12 operation(s) for topic.
  name: Shopify Topic API
  slug: shopify-topic-api
- description: The Tracking API from Shopify — 7 operation(s) for tracking.
  name: Shopify Tracking API
  slug: shopify-tracking-api
- description: The Transactions API from Shopify — 7 operation(s) for transactions.
  name: Shopify Transactions API
  slug: shopify-transactions-api
- description: The Type API from Shopify — 6 operation(s) for type.
  name: Shopify Type API
  slug: shopify-type-api
- description: The Update API from Shopify — 13 operation(s) for update.
  name: Shopify Update API
  slug: shopify-update-api
- description: The Usage API from Shopify — 6 operation(s) for usage.
  name: Shopify Usage API
  slug: shopify-usage-api
- description: The Used API from Shopify — 6 operation(s) for used.
  name: Shopify Used API
  slug: shopify-used-api
- description: The Users API from Shopify — 18 operation(s) for users.
  name: Shopify Users API
  slug: shopify-users-api
- description: The Variants API from Shopify — 6 operation(s) for variants.
  name: Shopify Variants API
  slug: shopify-variants-api
- description: The Vault API from Shopify — 6 operation(s) for vault.
  name: Shopify Vault API
  slug: shopify-vault-api
- description: The Versions API from Shopify — 26 operation(s) for versions.
  name: Shopify Versions API
  slug: shopify-versions-api
- description: Create and manage webhook subscriptions
  name: Shopify Webhook Subscriptions API
  slug: shopify-webhook-subscriptions-api
- description: The Zip API from Shopify — 6 operation(s) for zip.
  name: Shopify Zip API
  slug: shopify-zip-api
- description: The Zones API from Shopify — 6 operation(s) for zones.
  name: Shopify Zones API
  slug: shopify-zones-api
arazzos:
- description: Confirm a product exists, add a new variant to it, then read the variant list back.
  name: Shopify Add a Variant to an Existing Product
  slug: shopify-add-variant-to-product-workflow
- description: Read a product and branch on its status, archiving it only when it is still active.
  name: Shopify Archive a Stale Product
  slug: shopify-archive-stale-product-workflow
- description: Confirm an order, cancel it with a reason and restock, then read the cancelled order back.
  name: Shopify Cancel and Restock an Order
  slug: shopify-cancel-and-refund-order-workflow
- description: Tag an order, close it to mark it completed, then read the closed order back.
  name: Shopify Tag and Close an Order
  slug: shopify-close-and-archive-order-workflow
- description: Create a custom collection, confirm a product, then read the collection back.
  name: Shopify Create Collection With a Product
  slug: shopify-create-collection-with-product-workflow
- description: Create a customer record, attach a mailing address, then read the customer back.
  name: Shopify Create Customer With Address
  slug: shopify-create-customer-with-address-workflow
- description: Place an order, locate its fulfillment order, create a fulfillment with tracking, and read the order back.
  name: Shopify Create Order and Fulfill
  slug: shopify-create-order-and-fulfill-workflow
- description: Create a product, add a priced variant to it, then read the finished product back.
  name: Shopify Create Product With Variant
  slug: shopify-create-product-with-variant-workflow
- description: Find a custom collection by title, then list the products it contains.
  name: Shopify Find Collection and List Its Products
  slug: shopify-find-collection-and-list-products-workflow
- description: Resolve an order's fulfillment order, create a fulfillment with tracking, and confirm the result.
  name: Shopify Fulfill an Existing Order
  slug: shopify-fulfill-existing-order-workflow
- description: Create a product, add a variant, resolve a location, and set its starting inventory.
  name: Shopify Launch a Product With Stock
  slug: shopify-launch-product-with-stock-workflow
- description: Create a pending (quote-style) order, mark it paid, then read the completed order back.
  name: Shopify Quote to Paid Order
  slug: shopify-quote-to-paid-order-workflow
- description: Create a webhook subscription for a topic, then read it back to confirm registration.
  name: Shopify Register a Webhook Subscription
  slug: shopify-register-webhook-workflow
- description: Read a variant to find its inventory item, resolve a location, and set the available quantity.
  name: Shopify Restock a Product Variant
  slug: shopify-restock-product-variant-workflow
- description: Resolve the primary location, set an item's available quantity there, then verify the new level.
  name: Shopify Set Inventory at a Location
  slug: shopify-set-inventory-at-location-workflow
- description: Read an order and branch on its fulfillment status to apply the appropriate tag.
  name: Shopify Tag an Order by Fulfillment Status
  slug: shopify-tag-order-by-fulfillment-status-workflow
- description: Confirm an order, update a fulfillment's tracking details, then read the order back.
  name: Shopify Update Fulfillment Tracking
  slug: shopify-update-fulfillment-tracking-workflow
- description: Read an inventory item, update its unit cost and tracking flag, then read it back.
  name: Shopify Update an Inventory Item Cost
  slug: shopify-update-inventory-item-cost-workflow
- description: Search for a customer by email and update it if it exists, otherwise create it.
  name: Shopify Upsert a Customer by Email
  slug: shopify-upsert-customer-by-email-workflow
- description: Find or create a customer by email, then place an order for that customer.
  name: Shopify Upsert Customer Then Place Order
  slug: shopify-upsert-customer-then-order-workflow
- description: Find a product by exact title and update it if it exists, otherwise create it.
  name: Shopify Upsert a Product by Title
  slug: shopify-upsert-product-by-title-workflow
- description: Find a webhook subscription for a topic and update its address if it exists, otherwise create it.
  name: Shopify Upsert a Webhook by Topic
  slug: shopify-upsert-webhook-by-topic-workflow
artifact_total: 482
asyncapis:
- description: ''
  name: Shopify Webhooks
  slug: shopify-webhooks
collections:
- collection_type: postman
  name: Shopify Admin REST API
  slug: postman-shopify-admin-rest-api
- collection_type: postman
  name: Shopify Ajax API
  slug: postman-shopify-ajax-api
- collection_type: postman
  name: Shopify  API
  slug: postman-shopify-api
- collection_type: postman
  name: Shopify Multipass API
  slug: postman-shopify-multipass-api
- collection_type: postman
  name: Shopify Webhooks API
  slug: postman-shopify-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shopify Admin REST About API
  slug: open-shopify-about-api
- collection_type: open
  name: Shopify Admin REST About Access API
  slug: open-shopify-access-api
- collection_type: open
  name: Shopify Admin REST About Account API
  slug: open-shopify-account-api
- collection_type: open
  name: Shopify Admin REST About Accounts API
  slug: open-shopify-accounts-api
- collection_type: open
  name: Shopify Admin REST About Activation API
  slug: open-shopify-activation-api
- collection_type: open
  name: Shopify Admin REST About Active API
  slug: open-shopify-active-api
- collection_type: open
  name: Shopify Admin REST About Address API
  slug: open-shopify-address-api
- collection_type: open
  name: Shopify Admin REST About Addresses API
  slug: open-shopify-addresses-api
- collection_type: open
  name: Shopify REST About Admin API
  slug: open-shopify-admin-api
- collection_type: open
  name: Shopify Admin REST API
  slug: open-shopify-admin-rest-api
- collection_type: open
  name: Shopify Ajax API
  slug: open-shopify-ajax-api
- collection_type: open
  name: Shopify Admin REST About All API
  slug: open-shopify-all-api
- collection_type: open
  name: Shopify Admin REST About Amount API
  slug: open-shopify-amount-api
- collection_type: open
  name: Shopify Admin REST About Another API
  slug: open-shopify-another-api
- collection_type: open
  name: Shopify  API
  slug: open-shopify-api
- collection_type: open
  name: Shopify Admin REST About Applications API
  slug: open-shopify-applications-api
- collection_type: open
  name: Shopify Admin REST About Approves API
  slug: open-shopify-approves-api
- collection_type: open
  name: Shopify Admin REST About Article API
  slug: open-shopify-article-api
- collection_type: open
  name: Shopify Admin REST About Assets API
  slug: open-shopify-assets-api
- collection_type: open
  name: Shopify Admin REST About Associated API
  slug: open-shopify-associated-api
- collection_type: open
  name: Shopify Admin REST About Authenticated API
  slug: open-shopify-authenticated-api
- collection_type: open
  name: Shopify Admin REST About Authors API
  slug: open-shopify-authors-api
- collection_type: open
  name: Shopify Admin REST About Available API
  slug: open-shopify-available-api
- collection_type: open
  name: Shopify Admin REST About Balance API
  slug: open-shopify-balance-api
- collection_type: open
  name: Shopify Admin REST About Belong API
  slug: open-shopify-belong-api
- collection_type: open
  name: Shopify Admin REST About Belonging API
  slug: open-shopify-belonging-api
- collection_type: open
  name: Shopify Admin REST About Blog API
  slug: open-shopify-blog-api
- collection_type: open
  name: Shopify Admin REST About Blogs API
  slug: open-shopify-blogs-api
- collection_type: open
  name: Shopify Admin REST About Bulk API
  slug: open-shopify-bulk-api
- collection_type: open
  name: Shopify Admin REST About Calls API
  slug: open-shopify-calls-api
- collection_type: open
  name: Shopify Admin REST About Cancel API
  slug: open-shopify-cancel-api
- collection_type: open
  name: Shopify Admin REST About Cancels API
  slug: open-shopify-cancels-api
- collection_type: open
  name: Shopify Admin REST About Card API
  slug: open-shopify-card-api
- collection_type: open
  name: Shopify Admin REST About Cards API
  slug: open-shopify-cards-api
- collection_type: open
  name: Shopify Admin REST About Carrier API
  slug: open-shopify-carrier-api
- collection_type: open
  name: Shopify Admin REST About Cart API
  slug: open-shopify-cart-api
- collection_type: open
  name: Shopify Admin REST About Charge API
  slug: open-shopify-charge-api
- collection_type: open
  name: Shopify Admin REST About Charges API
  slug: open-shopify-charges-api
- collection_type: open
  name: Shopify Admin REST About Checkout API
  slug: open-shopify-checkout-api
- collection_type: open
  name: Shopify Admin REST About Checkouts API
  slug: open-shopify-checkouts-api
- collection_type: open
  name: Shopify Admin REST About Code API
  slug: open-shopify-code-api
- collection_type: open
  name: Shopify Admin REST About Collect API
  slug: open-shopify-collect-api
- collection_type: open
  name: Shopify Admin REST About Collection API
  slug: open-shopify-collection-api
- collection_type: open
  name: Shopify Admin REST About Collections API
  slug: open-shopify-collections-api
- collection_type: open
  name: Shopify Admin REST About Comments API
  slug: open-shopify-comments-api
- collection_type: open
  name: Shopify Admin REST About Complete API
  slug: open-shopify-complete-api
- collection_type: open
  name: Shopify Admin REST About Configuration API
  slug: open-shopify-configuration-api
- collection_type: open
  name: Shopify Admin REST About Connects API
  slug: open-shopify-connects-api
- collection_type: open
  name: Shopify Admin REST About Contains API
  slug: open-shopify-contains-api
- collection_type: open
  name: Shopify Admin REST About Count API
  slug: open-shopify-count-api
- collection_type: open
  name: Shopify Admin REST About Countries API
  slug: open-shopify-countries-api
- collection_type: open
  name: Shopify Admin REST About Country API
  slug: open-shopify-country-api
- collection_type: open
  name: Shopify Admin REST About Counts API
  slug: open-shopify-counts-api
- collection_type: open
  name: Shopify Admin REST About County API
  slug: open-shopify-county-api
- collection_type: open
  name: Shopify Admin REST About Create API
  slug: open-shopify-create-api
- collection_type: open
  name: Shopify Admin REST About Creation API
  slug: open-shopify-creation-api
- collection_type: open
  name: Shopify Admin REST About Credit API
  slug: open-shopify-credit-api
- collection_type: open
  name: Shopify Admin REST About Currencies API
  slug: open-shopify-currencies-api
- collection_type: open
  name: Shopify Admin REST About Current API
  slug: open-shopify-current-api
- collection_type: open
  name: Shopify Admin REST About Custom API
  slug: open-shopify-custom-api
- collection_type: open
  name: Shopify Admin REST About Custom Collections API
  slug: open-shopify-custom-collections-api
- collection_type: open
  name: Shopify Admin REST About Customer Addresses API
  slug: open-shopify-customer-addresses-api
- collection_type: open
  name: Shopify Admin REST About Customer API
  slug: open-shopify-customer-api
- collection_type: open
  name: Shopify Admin REST About Customers API
  slug: open-shopify-customers-api
- collection_type: open
  name: Shopify Admin REST About Date API
  slug: open-shopify-date-api
- collection_type: open
  name: Shopify Admin REST About Days API
  slug: open-shopify-days-api
- collection_type: open
  name: Shopify Admin REST About Deletes API
  slug: open-shopify-deletes-api
- collection_type: open
  name: Shopify Admin REST About Disables API
  slug: open-shopify-disables-api
- collection_type: open
  name: Shopify Admin REST About Discount API
  slug: open-shopify-discount-api
- collection_type: open
  name: Shopify Admin REST About Dispute API
  slug: open-shopify-dispute-api
- collection_type: open
  name: Shopify Admin REST About Disputes API
  slug: open-shopify-disputes-api
- collection_type: open
  name: Shopify Admin REST About Enabled API
  slug: open-shopify-enabled-api
- collection_type: open
  name: Shopify Admin REST About Endpoint API
  slug: open-shopify-endpoint-api
- collection_type: open
  name: Shopify Admin REST About Events API
  slug: open-shopify-events-api
- collection_type: open
  name: Shopify Admin REST About Existing API
  slug: open-shopify-existing-api
- collection_type: open
  name: Shopify Admin REST About Files API
  slug: open-shopify-files-api
- collection_type: open
  name: Shopify Admin REST About Format API
  slug: open-shopify-format-api
- collection_type: open
  name: Shopify Admin REST About Fulfillment API
  slug: open-shopify-fulfillment-api
- collection_type: open
  name: Shopify Admin REST About Fulfillment Orders API
  slug: open-shopify-fulfillment-orders-api
- collection_type: open
  name: Shopify Admin REST About Fulfillments API
  slug: open-shopify-fulfillments-api
- collection_type: open
  name: Shopify Admin REST About Generate API
  slug: open-shopify-generate-api
- collection_type: open
  name: Shopify Admin REST About Get API
  slug: open-shopify-get-api
- collection_type: open
  name: Shopify Admin REST About Gift API
  slug: open-shopify-gift-api
- collection_type: open
  name: Shopify Admin REST About Have API
  slug: open-shopify-have-api
- collection_type: open
  name: Shopify Admin REST About Holds API
  slug: open-shopify-holds-api
- collection_type: open
  name: Shopify Admin REST About Identifiers API
  slug: open-shopify-identifiers-api
- collection_type: open
  name: Shopify Admin REST About Image API
  slug: open-shopify-image-api
- collection_type: open
  name: Shopify Admin REST About Images API
  slug: open-shopify-images-api
- collection_type: open
  name: Shopify Admin REST About Information API
  slug: open-shopify-information-api
- collection_type: open
  name: Shopify Admin REST About Inventory API
  slug: open-shopify-inventory-api
- collection_type: open
  name: Shopify Admin REST About Inventory Items API
  slug: open-shopify-inventory-items-api
- collection_type: open
  name: Shopify Admin REST About Inventory Levels API
  slug: open-shopify-inventory-levels-api
- collection_type: open
  name: Shopify Admin REST About Invites API
  slug: open-shopify-invites-api
- collection_type: open
  name: Shopify Admin REST About Issued API
  slug: open-shopify-issued-api
- collection_type: open
  name: Shopify Admin REST About Item API
  slug: open-shopify-item-api
- collection_type: open
  name: Shopify Admin REST About Items API
  slug: open-shopify-items-api
- collection_type: open
  name: Shopify Admin REST About Jobs API
  slug: open-shopify-jobs-api
- collection_type: open
  name: Shopify Admin REST About Keys API
  slug: open-shopify-keys-api
- collection_type: open
  name: Shopify Admin REST About Levels API
  slug: open-shopify-levels-api
- collection_type: open
  name: Shopify Admin REST About Line API
  slug: open-shopify-line-api
- collection_type: open
  name: Shopify Admin REST About Listing API
  slug: open-shopify-listing-api
- collection_type: open
  name: Shopify Admin REST About Listings API
  slug: open-shopify-listings-api
- collection_type: open
  name: Shopify Admin REST About Lists API
  slug: open-shopify-lists-api
- collection_type: open
  name: Shopify Admin REST About Location API
  slug: open-shopify-location-api
- collection_type: open
  name: Shopify Admin REST About Locations API
  slug: open-shopify-locations-api
- collection_type: open
  name: Shopify Admin REST About Make API
  slug: open-shopify-make-api
- collection_type: open
  name: Shopify Admin REST About Managed API
  slug: open-shopify-managed-api
- collection_type: open
  name: Shopify Admin REST About Many API
  slug: open-shopify-many-api
- collection_type: open
  name: Shopify Admin REST About Mark API
  slug: open-shopify-mark-api
- collection_type: open
  name: Shopify Admin REST About Match API
  slug: open-shopify-match-api
- collection_type: open
  name: Shopify Admin REST About Merchant API
  slug: open-shopify-merchant-api
- collection_type: open
  name: Shopify Admin REST About Metafields API
  slug: open-shopify-metafields-api
- collection_type: open
  name: Shopify Admin REST About Modifies API
  slug: open-shopify-modifies-api
- collection_type: open
  name: Shopify Admin REST About Modify API
  slug: open-shopify-modify-api
- collection_type: open
  name: Shopify Admin REST About Move API
  slug: open-shopify-move-api
- collection_type: open
  name: Shopify Admin REST About Moves API
  slug: open-shopify-moves-api
- collection_type: open
  name: Shopify Admin REST About Multipass API
  slug: open-shopify-multipass-api
- collection_type: open
  name: Shopify Admin REST About Multiple API
  slug: open-shopify-multiple-api
- collection_type: open
  name: Shopify Admin REST About Number API
  slug: open-shopify-number-api
- collection_type: open
  name: Shopify Admin REST About Numbers API
  slug: open-shopify-numbers-api
- collection_type: open
  name: Shopify Admin REST About Open API
  slug: open-shopify-open-api
- collection_type: open
  name: Shopify Admin REST About Operations API
  slug: open-shopify-operations-api
- collection_type: open
  name: Shopify Admin REST About Order API
  slug: open-shopify-order-api
- collection_type: open
  name: Shopify Admin REST About Ordered API
  slug: open-shopify-ordered-api
- collection_type: open
  name: Shopify Admin REST About Orders API
  slug: open-shopify-orders-api
- collection_type: open
  name: Shopify Admin REST About Particular API
  slug: open-shopify-particular-api
- collection_type: open
  name: Shopify Admin REST About Past API
  slug: open-shopify-past-api
- collection_type: open
  name: Shopify Admin REST About Payments API
  slug: open-shopify-payments-api
- collection_type: open
  name: Shopify Admin REST About Payouts API
  slug: open-shopify-payouts-api
- collection_type: open
  name: Shopify Admin REST About Policies API
  slug: open-shopify-policies-api
- collection_type: open
  name: Shopify Admin REST About Predictive Search API
  slug: open-shopify-predictive-search-api
- collection_type: open
  name: Shopify Admin REST About Previously API
  slug: open-shopify-previously-api
- collection_type: open
  name: Shopify Admin REST About Private API
  slug: open-shopify-private-api
- collection_type: open
  name: Shopify Admin REST About Product API
  slug: open-shopify-product-api
- collection_type: open
  name: Shopify Admin REST About Product Images API
  slug: open-shopify-product-images-api
- collection_type: open
  name: Shopify Admin REST About Product Recommendations API
  slug: open-shopify-product-recommendations-api
- collection_type: open
  name: Shopify Admin REST About Product Variants API
  slug: open-shopify-product-variants-api
- collection_type: open
  name: Shopify Admin REST About Products API
  slug: open-shopify-products-api
- collection_type: open
  name: Shopify Admin REST About Progress API
  slug: open-shopify-progress-api
- collection_type: open
  name: Shopify Admin REST About Providing API
  slug: open-shopify-providing-api
- collection_type: open
  name: Shopify Admin REST About Province API
  slug: open-shopify-province-api
- collection_type: open
  name: Shopify Admin REST About Public API
  slug: open-shopify-public-api
- collection_type: open
  name: Shopify Admin REST About Publish API
  slug: open-shopify-publish-api
- collection_type: open
  name: Shopify Admin REST About Published API
  slug: open-shopify-published-api
- collection_type: open
  name: Shopify Admin REST About Queries API
  slug: open-shopify-queries-api
- collection_type: open
  name: Shopify Admin REST About Rates API
  slug: open-shopify-rates-api
- collection_type: open
  name: Shopify Admin REST About Ready API
  slug: open-shopify-ready-api
- collection_type: open
  name: Shopify Admin REST About Recurring API
  slug: open-shopify-recurring-api
- collection_type: open
  name: Shopify Admin REST About Redirect API
  slug: open-shopify-redirect-api
- collection_type: open
  name: Shopify Admin REST About Redirects API
  slug: open-shopify-redirects-api
- collection_type: open
  name: Shopify Admin REST About Refund API
  slug: open-shopify-refund-api
- collection_type: open
  name: Shopify Admin REST About Refunds API
  slug: open-shopify-refunds-api
- collection_type: open
  name: Shopify Admin REST About Releases API
  slug: open-shopify-releases-api
- collection_type: open
  name: Shopify Admin REST About Reports API
  slug: open-shopify-reports-api
- collection_type: open
  name: Shopify Admin REST About Requests API
  slug: open-shopify-requests-api
- collection_type: open
  name: Shopify Admin REST About Required API
  slug: open-shopify-required-api
- collection_type: open
  name: Shopify Admin REST About Resource API
  slug: open-shopify-resource-api
- collection_type: open
  name: Shopify Admin REST About Retrieves API
  slug: open-shopify-retrieves-api
- collection_type: open
  name: Shopify Admin REST About Risk API
  slug: open-shopify-risk-api
- collection_type: open
  name: Shopify Admin REST About Rules API
  slug: open-shopify-rules-api
- collection_type: open
  name: Shopify Admin REST About Saved API
  slug: open-shopify-saved-api
- collection_type: open
  name: Shopify Admin REST About Scheduled API
  slug: open-shopify-scheduled-api
- collection_type: open
  name: Shopify Admin REST About Scopes API
  slug: open-shopify-scopes-api
- collection_type: open
  name: Shopify Admin REST About Script API
  slug: open-shopify-script-api
- collection_type: open
  name: Shopify Admin REST About Search API
  slug: open-shopify-search-api
- collection_type: open
  name: Shopify Admin REST About Searches API
  slug: open-shopify-searches-api
- collection_type: open
  name: Shopify Admin REST About Sends API
  slug: open-shopify-sends-api
- collection_type: open
  name: Shopify Admin REST About Sent API
  slug: open-shopify-sent-api
- collection_type: open
  name: Shopify Admin REST About Sessions API
  slug: open-shopify-sessions-api
- collection_type: open
  name: Shopify Admin REST About Sets API
  slug: open-shopify-sets-api
- collection_type: open
  name: Shopify Admin REST About Shipping API
  slug: open-shopify-shipping-api
- collection_type: open
  name: Shopify Admin REST About Shop API
  slug: open-shopify-shop-api
- collection_type: open
  name: Shopify Admin REST About Single API
  slug: open-shopify-single-api
- collection_type: open
  name: Shopify Admin REST About Smart API
  slug: open-shopify-smart-api
- collection_type: open
  name: Shopify Admin REST About Smart Collections API
  slug: open-shopify-smart-collections-api
- collection_type: open
  name: Shopify Admin REST About Spam API
  slug: open-shopify-spam-api
- collection_type: open
  name: Shopify Admin REST About Specific API
  slug: open-shopify-specific-api
- collection_type: open
  name: Shopify Admin REST About Storefront API
  slug: open-shopify-storefront-api
- collection_type: open
  name: Shopify Admin REST About Subscriptions API
  slug: open-shopify-subscriptions-api
- collection_type: open
  name: Shopify Admin REST About Summaries API
  slug: open-shopify-summaries-api
- collection_type: open
  name: Shopify Admin REST About Tender API
  slug: open-shopify-tender-api
- collection_type: open
  name: Shopify Admin REST About Theme API
  slug: open-shopify-theme-api
- collection_type: open
  name: Shopify Admin REST About Themes API
  slug: open-shopify-themes-api
- collection_type: open
  name: Shopify Admin REST About Time API
  slug: open-shopify-time-api
- collection_type: open
  name: Shopify Admin REST About Tokens API
  slug: open-shopify-tokens-api
- collection_type: open
  name: Shopify Admin REST About Topic API
  slug: open-shopify-topic-api
- collection_type: open
  name: Shopify Admin REST About Tracking API
  slug: open-shopify-tracking-api
- collection_type: open
  name: Shopify Admin REST About Transactions API
  slug: open-shopify-transactions-api
- collection_type: open
  name: Shopify Admin REST About Type API
  slug: open-shopify-type-api
- collection_type: open
  name: Shopify Admin REST About Update API
  slug: open-shopify-update-api
- collection_type: open
  name: Shopify Admin REST About Usage API
  slug: open-shopify-usage-api
- collection_type: open
  name: Shopify Admin REST About Used API
  slug: open-shopify-used-api
- collection_type: open
  name: Shopify Admin REST About Users API
  slug: open-shopify-users-api
- collection_type: open
  name: Shopify Admin REST About Variants API
  slug: open-shopify-variants-api
- collection_type: open
  name: Shopify Admin REST About Vault API
  slug: open-shopify-vault-api
- collection_type: open
  name: Shopify Admin REST About Versions API
  slug: open-shopify-versions-api
- collection_type: open
  name: Shopify Admin REST About Webhook Subscriptions API
  slug: open-shopify-webhook-subscriptions-api
- collection_type: open
  name: Shopify Admin REST About Webhooks API
  slug: open-shopify-webhooks-api
- collection_type: open
  name: Shopify Admin REST About Zip API
  slug: open-shopify-zip-api
- collection_type: open
  name: Shopify Admin REST About Zones API
  slug: open-shopify-zones-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shopify-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shopify-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopify-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/shopify/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-add-variant-to-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-archive-stale-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-cancel-and-refund-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-close-and-archive-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-collection-with-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-customer-with-address-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-order-and-fulfill-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-product-with-variant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-find-collection-and-list-products-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-fulfill-existing-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-launch-product-with-stock-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-quote-to-paid-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-register-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-restock-product-variant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-set-inventory-at-location-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-tag-order-by-fulfillment-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-update-fulfillment-tracking-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-update-inventory-item-cost-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-customer-by-email-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-customer-then-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-product-by-title-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-webhook-by-topic-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopify
- group: docs
  title: ''
  type: Documentation
  url: https://shopify.dev/docs
- group: design
  title: ''
  type: Versioning
  url: https://shopify.dev/docs/api/usage/versioning
- group: auth
  title: ''
  type: Authentication
  url: https://shopify.dev/docs/api/usage/authentication
- group: build
  title: ''
  type: CLI
  url: https://shopify.dev/docs/api/shopify-cli
- group: docs
  title: ''
  type: Documentation
  url: https://shopify.dev/docs/api
- group: start
  title: ''
  type: Portal
  url: https://shopify.dev
- group: build
  title: ''
  type: SDKs
  url: https://shopify.dev/docs/api/libraries-and-templates
- group: operate
  title: ''
  type: RateLimits
  url: https://shopify.dev/docs/api/usage/rate-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://shopify.dev/changelog
- group: design
  title: ''
  type: Versioning
  url: https://shopify.dev/docs/api/usage/versioning
- group: operate
  title: ''
  type: StatusPage
  url: https://www.shopifystatus.com
- group: operate
  title: ''
  type: Support
  url: https://community.shopify.dev/c/dev-platform/32
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shopify.com/legal/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopify.com/legal/privacy
- group: start
  title: ''
  type: Signup
  url: https://partners.shopify.com/signup
- group: design
  title: ''
  type: Webhooks
  url: https://shopify.dev/docs/apps/build/webhooks
- group: auth
  title: ''
  type: Security
  url: security/shopify-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: AuthenticationDocs
  url: https://shopify.dev/docs/apps/build/authentication-authorization
- group: auth
  title: ''
  type: Access Scopes
  url: https://shopify.dev/docs/api/usage/access-scopes
- group: operate
  title: ''
  type: Forums
  url: https://community.shopify.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shopify
- group: company
  title: ''
  type: Blog
  url: https://shopify.engineering/
- group: other
  title: ''
  type: Headless
  url: https://shopify.dev/docs/storefronts/headless
- group: other
  title: ''
  type: Design System
  url: https://shopify.dev/docs/api/polaris
- group: other
  title: ''
  type: App Bridge
  url: https://shopify.dev/docs/api/app-bridge
- group: other
  title: ''
  type: Application Marketplace
  url: https://apps.shopify.com
- group: company
  title: ''
  type: Partner Program
  url: https://www.shopify.com/partners
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@shopifydevs
- group: start
  title: ''
  type: GettingStarted
  url: https://shopify.dev/docs/apps/build
- group: build
  title: ''
  type: Extensions
  url: https://shopify.dev/docs/apps/build/app-extensions
- group: other
  title: ''
  type: Themes
  url: https://shopify.dev/docs/themes
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/shopify
- group: company
  title: ''
  type: Website
  url: https://www.shopify.com
- group: start
  title: ''
  type: Login
  url: https://accounts.shopify.com
- group: operate
  title: ''
  type: Community
  url: https://community.shopify.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://shopify.dev/docs/api/release-notes
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Shopify/shopify-app-js
- group: build
  title: ''
  type: SDKs
  url: https://shopify.dev/docs/storefronts/headless/additional-sdks
- group: agent
  title: ''
  type: LlmsText
  url: llms/shopify-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/shopify-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shopify-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shopify-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/shopify-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shopify-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/shopify-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shopify-admin-rest-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/shopify-ajax-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopify-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/shopify-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shopify-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopify-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopify-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://shopify.dev/docs/api/usage/versioning#deprecation-practices
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shopify-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopify-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shopify-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shopify-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shopify-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/shopify-cli.yml
- group: design
  title: ''
  type: Components
  url: components/shopify-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopify-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shopify-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shopify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shopify-rate-limits.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/shopify-storefront-api.graphql
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shopify.com/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://shopify.dev/docs/api
created: '2024-04-14'
description: Shopify is a complete commerce platform that lets you start, grow, and manage a business, selling online, in person, on marketplaces, through social channels, and now inside AI chats. Its developer platform exposes GraphQL Admin, Storefront and Customer Account APIs, a legacy Admin REST surface, 206 webhook topics, Shopify Functions, Hydrogen and the Shopify CLI, so apps and integrations can extend Shopify for merchants and buyers alike. Shopify also runs four MCP servers bound to the Universal Commerce Protocol, letting AI agents search a cross-merchant catalog, build carts, complete checkouts and track orders.
examples:
- key_count: 4
  name: Shopify Create Product Example
  slug: shopify-create-product-example
- key_count: 4
  name: Shopify List Orders Example
  slug: shopify-list-orders-example
features:
- REST Admin API with leaky-bucket throttling (40 req/app/store)
- GraphQL Admin API with cost-based throttling (1,000 pts on Standard, 2,000 on Plus)
- Storefront API for headless commerce
- 'Plans: Basic ($29), Grow ($79), Advanced ($299), Plus ($2,300)'
- Online card transaction fees from 2.25% (Plus) to 2.9% (Basic)
- Third-party gateway fees from 0% (Plus) to 2% (Basic)
- AI assistant for commerce included on all plans
- Up to 200 POS Pro locations on Plus
- B2B / wholesale on Plus
- Customizable checkout on Plus
- Bulk operations for large data exports without rate-limit hits
- Webhooks for order, customer, inventory, and product events
- OAuth 2.0 app authentication
- Shopify Functions for backend customization
- Shopify Markets for region-specific currencies and pricing
finops:
- name: Shopify Finops
  service_category: E-Commerce Platform
  slug: shopify-finops
graphqls:
- description: The GraphQL Admin API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillment, and more. GraphQL is th
  name: Shopify GraphQL API
  slug: shopify-graphql
image: https://cdn.shopify.com/shopifycloud/brochure/assets/brand-assets/shopify-logo.png
json_schemas:
- name: Shopify Collection
  property_count: 13
  slug: shopify-collection
- name: Shopify Customer
  property_count: 22
  slug: shopify-customer
- name: Shopify Fulfillment
  property_count: 18
  slug: shopify-fulfillment
- name: Shopify Inventory Item
  property_count: 12
  slug: shopify-inventory-item
- name: Shopify Order
  property_count: 36
  slug: shopify-order
- name: Shopify Product
  property_count: 18
  slug: shopify-product
json_structures:
- name: Shopify Order Structure
  property_count: 0
  slug: shopify-order-structure
- name: Shopify Product Structure
  property_count: 0
  slug: shopify-product-structure
jsonld:
- class_count: 75
  name: Shopify Context
  property_count: 29
  slug: shopify-context
layout: provider
mcp_servers:
- description: Shopify ships more MCP surface than any other commerce platform in this catalog, across four distinct servers. One is a hosted, anonymous, cross-merchant server on Shopify's own domain (Global Catalog
  name: Shopify Global Catalog MCP (remote) + Storefront/Cart/Checkout MCP + Dev MCP (stdio)
  slug: shopify-global-catalog-mcp-remote-storefrontcartcheckout-mcp-dev-mcp-stdio
modified: '2026-08-27'
name: Shopify
nav: Providers
network: true
overview: 'Shopify publishes 197 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Multipass API, About API, and 194 more. Tagged areas include Commerce, E-Commerce, Payments, Retail, and Shopping Cart.


  The Shopify catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Shopify''s developer surface includes authentication, documentation, CLI, developer portal, changelog, support, signup flow, and 90 more developer resources.'
plans:
- name: Shopify Plans Pricing
  plan_count: 4
  slug: shopify-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 7
  name: Shopify Rate Limits
  slug: shopify-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Shopify API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shopify-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Shopify API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 5
  slug: shopify-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Shopify API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: shopify-spectral-rules
scopes:
- name: Shopify Scopes
  scope_count: 0
  slug: shopify-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 84.0
  coverage:
    artifact_dirs: 39
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 47.0
    contract_quality: 85.3
    developer_ergonomics: 100.0
    discoverability: 66.7
    governance: 47.0
    operational_transparency: 71.1
  previous_composite: 84.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 197
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopify/refs/heads/main/screenshots/shopify-2026-06-20T165931.png
security:
- kind: authentication
  name: Shopify Authentication
  slug: shopify-authentication
  summary_line: apiKey/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Shopify Domain Security
  slug: shopify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shopify Vulnerability Disclosure
  slug: shopify-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Shopify Trust Center
  slug: shopify-trust-center
  summary_line: PCI DSS, SOC 2 Type II, SOC 3
slug: shopify
tags:
- Commerce
- E-Commerce
- Payments
- Retail
- Shopping Cart
- T1
website: https://www.shopify.com
---
