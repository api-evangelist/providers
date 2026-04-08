---
aid: square
url: https://raw.githubusercontent.com/api-evangelist/square/refs/heads/main/apis.yml
apis:
- aid: square:payments-api
  name: Square Payments API
  tags:
  - Commerce
  - Financial Technology
  - Payments
  - Point of Sale
  humanURL: https://developer.squareup.com/docs/payments-overview
  properties:
  - url: https://developer.squareup.com/docs/payments-overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/payments-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Payments API lets applications take and manage payments by charging payment methods supported by the Web Payments SDK or In-App Payments SDK, including credit cards, gift cards, digital wallets, and ACH bank transfers. It can also record cash or external payments received outside of Square.
- aid: square:orders-api
  name: Square Orders API
  tags:
  - Commerce
  - Orders
  - Point of Sale
  humanURL: https://developer.squareup.com/docs/orders-api/what-it-does
  properties:
  - url: https://developer.squareup.com/docs/orders-api/what-it-does
    type: Documentation
  - url: https://developer.squareup.com/reference/square/orders-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Orders API lets applications itemize payments using custom line items or catalog objects, send orders to physical Point of Sale devices for fulfillment, attach customers to payments, and search through all of a seller's past sales with itemization data.
- aid: square:catalog-api
  name: Square Catalog API
  tags:
  - Catalog
  - Commerce
  - Products
  humanURL: https://developer.squareup.com/docs/catalog-api/what-it-does
  properties:
  - url: https://developer.squareup.com/docs/catalog-api/what-it-does
    type: Documentation
  - url: https://developer.squareup.com/reference/square/catalog-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Catalog API programmatically catalogs a Square seller's products for sale and services for hire, enabling applications to create, update, and manage catalog items, categories, variations, and pricing.
- aid: square:inventory-api
  name: Square Inventory API
  tags:
  - Commerce
  - Inventory
  - Retail
  humanURL: https://developer.squareup.com/docs/inventory-api/what-it-does
  properties:
  - url: https://developer.squareup.com/docs/inventory-api/what-it-does
    type: Documentation
  - url: https://developer.squareup.com/reference/square/inventory-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Inventory API programmatically manages a Square seller's inventory of catalog items, including updating and tracking inventory changes and retrieving inventory counts.
- aid: square:customers-api
  name: Square Customers API
  tags:
  - Commerce
  - CRM
  - Customers
  humanURL: https://developer.squareup.com/docs/customers
  properties:
  - url: https://developer.squareup.com/docs/customers
    type: Documentation
  - url: https://developer.squareup.com/reference/square/customers-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Customers API lets applications create and manage customer profiles to streamline bookings, build loyalty programs, sell gift cards, and offer discounts. It enables syncing CRM systems with Square.
- aid: square:locations-api
  name: Square Locations API
  tags:
  - Business Management
  - Commerce
  - Locations
  humanURL: https://developer.squareup.com/docs/locations-api
  properties:
  - url: https://developer.squareup.com/docs/locations-api
    type: Documentation
  - url: https://developer.squareup.com/reference/square/locations-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Locations API lets applications create and manage the locations of a seller's business, including retrieving location details and managing location settings.
- aid: square:team-api
  name: Square Team API
  tags:
  - Business Management
  - Employees
  - Team
  humanURL: https://developer.squareup.com/docs/team/overview
  properties:
  - url: https://developer.squareup.com/docs/team/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/team-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Team API lets applications create and manage a roster of team members, configure jobs, and synchronize team member data with external platforms including accounting and payroll systems.
- aid: square:labor-api
  name: Square Labor API
  tags:
  - Business Management
  - Labor
  - Time Tracking
  humanURL: https://developer.squareup.com/docs/labor-api/what-it-does
  properties:
  - url: https://developer.squareup.com/docs/labor-api/what-it-does
    type: Documentation
  - url: https://developer.squareup.com/reference/square/labor-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Labor API is the timekeeping component of Square's team management APIs, enabling applications to manage time tracking and scheduling for team members, record hours worked, and handle breaks, wages, and declared cash tips for labor cost reporting and payroll.
- aid: square:bookings-api
  name: Square Bookings API
  tags:
  - Appointments
  - Bookings
  - Scheduling
  humanURL: https://developer.squareup.com/docs/bookings-api/what-it-is
  properties:
  - url: https://developer.squareup.com/docs/bookings-api/what-it-is
    type: Documentation
  - url: https://developer.squareup.com/reference/square/bookings-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Bookings API enables creating reservations of services provided by a seller's staff for customers at particular locations and times. Applications can create, update, cancel, and search for available bookings.
- aid: square:loyalty-api
  name: Square Loyalty API
  tags:
  - Customer Engagement
  - Loyalty
  - Rewards
  humanURL: https://developer.squareup.com/docs/loyalty-api/overview
  properties:
  - url: https://developer.squareup.com/docs/loyalty-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/loyalty-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Loyalty API allows applications to set up and manage loyalty programs, enroll buyers, accrue points, and redeem rewards. It works with the Orders API to manage loyalty accounts and rewards at participating locations.
- aid: square:gift-cards-api
  name: Square Gift Cards API
  tags:
  - Commerce
  - Customer Engagement
  - Gift Cards
  humanURL: https://developer.squareup.com/docs/gift-cards/using-gift-cards-api
  properties:
  - url: https://developer.squareup.com/docs/gift-cards/using-gift-cards-api
    type: Documentation
  - url: https://developer.squareup.com/reference/square/gift-cards-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Gift Cards API enables sellers to launch a gifting program with digital and physical gift cards. Applications can create, retrieve, link, and unlink gift cards, and manage gift card activities such as activating, loading, and redeeming.
- aid: square:invoices-api
  name: Square Invoices API
  tags:
  - Billing
  - Invoices
  - Payments
  humanURL: https://developer.squareup.com/docs/invoices-api/overview
  properties:
  - url: https://developer.squareup.com/docs/invoices-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/invoices-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Invoices API lets applications request or automatically collect payments from customers for orders created using the Orders API. It supports creating, updating, publishing, and managing invoices with multiple payment schedules and methods.
- aid: square:subscriptions-api
  name: Square Subscriptions API
  tags:
  - Commerce
  - Recurring Payments
  - Subscriptions
  humanURL: https://developer.squareup.com/docs/subscriptions-api/overview
  properties:
  - url: https://developer.squareup.com/docs/subscriptions-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/subscriptions-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Subscriptions API enables sellers to generate recurring revenue by offering scheduled fulfillment of products or services. Applications can create and manage subscription plans with configurable billing periods, pricing, and discounts.
- aid: square:checkout-api
  name: Square Checkout API
  tags:
  - Checkout
  - Commerce
  - Payments
  humanURL: https://developer.squareup.com/docs/checkout-api
  properties:
  - url: https://developer.squareup.com/docs/checkout-api
    type: Documentation
  - url: https://developer.squareup.com/reference/square/checkout-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Checkout API creates Square-hosted checkout pages for collecting payments. Applications can generate payment links with a simple API call, supporting credit cards, debit cards, Google Pay, Apple Pay, Afterpay, and Cash App.
- aid: square:terminal-api
  name: Square Terminal API
  tags:
  - In-Person Payments
  - Point of Sale
  - Terminal
  humanURL: https://developer.squareup.com/docs/terminal-api/overview
  properties:
  - url: https://developer.squareup.com/docs/terminal-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/terminal-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Terminal API lets developers integrate Square in-person payments so custom POS applications can use Square Terminal for card chip and NFC payments, with EMV certification and PCI compliance built in.
- aid: square:refunds-api
  name: Square Refunds API
  tags:
  - Commerce
  - Payments
  - Refunds
  humanURL: https://developer.squareup.com/docs/payments-refunds
  properties:
  - url: https://developer.squareup.com/docs/payments-refunds
    type: Documentation
  - url: https://developer.squareup.com/reference/square/refunds-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Refunds API lets applications refund the entire payment amount or a portion of it for card payments, and record refunds of cash or external payments.
- aid: square:disputes-api
  name: Square Disputes API
  tags:
  - Chargebacks
  - Disputes
  - Payments
  humanURL: https://developer.squareup.com/docs/disputes-api/overview
  properties:
  - url: https://developer.squareup.com/docs/disputes-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/disputes-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Disputes API manages payment disputes and chargebacks, allowing applications to list disputes, retrieve dispute details, challenge disputes by submitting evidence, and accept disputes.
- aid: square:merchants-api
  name: Square Merchants API
  tags:
  - Business Management
  - Commerce
  - Merchants
  humanURL: https://developer.squareup.com/docs/merchants-api
  properties:
  - url: https://developer.squareup.com/docs/merchants-api
    type: Documentation
  - url: https://developer.squareup.com/reference/square/merchants-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Merchants API groups individual seller locations into larger organizations, with each merchant representing one organization or business that sells with Square.
- aid: square:cards-api
  name: Square Cards API
  tags:
  - Cards
  - Commerce
  - Payments
  humanURL: https://developer.squareup.com/docs/cards-api/overview
  properties:
  - url: https://developer.squareup.com/docs/cards-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/cards-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Cards API lets applications save a credit or debit card on file for a customer, enabling faster future payments without re-entering card details.
- aid: square:vendors-api
  name: Square Vendors API
  tags:
  - Inventory
  - Suppliers
  - Vendors
  humanURL: https://developer.squareup.com/docs/vendors-api/manage-vendors-in-apps
  properties:
  - url: https://developer.squareup.com/docs/vendors-api/manage-vendors-in-apps
    type: Documentation
  - url: https://developer.squareup.com/reference/square/vendors-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Vendors API lets applications manage vendors and suppliers for a seller, enabling creation, retrieval, and updating of vendor information.
- aid: square:cash-drawers-api
  name: Square Cash Drawers API
  tags:
  - Cash Drawers
  - Point of Sale
  - Reporting
  humanURL: https://developer.squareup.com/docs/cashdrawershift-api/reporting
  properties:
  - url: https://developer.squareup.com/docs/cashdrawershift-api/reporting
    type: Documentation
  - url: https://developer.squareup.com/reference/square/cash-drawers-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Cash Drawers API is a reporting API for businesses that use a cash drawer with their Square Point of Sale terminals, providing filtered and paged lists of cash drawer shift data for a given location.
- aid: square:bank-accounts-api
  name: Square Bank Accounts API
  tags:
  - Bank Accounts
  - Financial Technology
  - Payments
  humanURL: https://developer.squareup.com/docs/bank-accounts-api
  properties:
  - url: https://developer.squareup.com/docs/bank-accounts-api
    type: Documentation
  - url: https://developer.squareup.com/reference/square/bank-accounts-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Bank Accounts API lets applications retrieve a list of a seller's bank accounts and get details about specific bank accounts linked to a Square account.
- aid: square:payouts-api
  name: Square Payouts API
  tags:
  - Financial Technology
  - Payments
  - Payouts
  humanURL: https://developer.squareup.com/docs/payouts-api/overview
  properties:
  - url: https://developer.squareup.com/docs/payouts-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/payouts-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Payouts API lets applications get a list of deposits and withdrawals from a seller's bank accounts, providing visibility into funds movement.
- aid: square:apple-pay-api
  name: Square Apple Pay API
  tags:
  - Apple Pay
  - Digital Wallets
  - Payments
  humanURL: https://developer.squareup.com/docs/web-payments/apple-pay
  properties:
  - url: https://developer.squareup.com/docs/web-payments/apple-pay
    type: Documentation
  - url: https://developer.squareup.com/reference/square/apple-pay-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Apple Pay API provides an easy way for platform developers to bulk activate Web Apple Pay with Square for merchants using their platform.
- aid: square:sites-api
  name: Square Sites API
  tags:
  - Ecommerce
  - Sites
  - Square Online
  humanURL: https://developer.squareup.com/docs/sites-api/overview
  properties:
  - url: https://developer.squareup.com/docs/sites-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/sites-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Sites API lets applications retrieve basic details about Square Online sites belonging to a seller, such as site ID, title, and domain. It is used in combination with the Snippets API.
- aid: square:snippets-api
  name: Square Snippets API
  tags:
  - Ecommerce
  - Snippets
  - Square Online
  humanURL: https://developer.squareup.com/docs/snippets-api/overview
  properties:
  - url: https://developer.squareup.com/docs/snippets-api/overview
    type: Documentation
  - url: https://developer.squareup.com/reference/square/snippets-api
    type: Reference
  - url: openapi/square-openapi.yml
    type: OpenAPI
  description: The Snippets API lets applications add custom scripts to a Square Online site. Snippets can run as modals, pop ups, or background jobs, offering a range of functionality to extend Square Online features.
name: Square
tags:
- Bookings
- Catalog
- Checkout
- Customers
- Disputes
- Ecommerce
- Financial Technology
- Gift Cards
- Inventory
- Invoicing
- Labor
- Locations
- Loyalty
- Merchants
- Orders
- Payments
- Point of Sale
- Refunds
- Retail
- Subscriptions
- Team
- Terminal
- Webhooks
type: Index
image: https://images.squarespace-cdn.com/content/v1/5e3b09f5e4e7d30f0b8c8e8f/square-logo.png
access: 3rd-Party
common:
- url: https://developer.squareup.com/docs/sdks
  name: Square SDKs
  type: SDKs
  description: Learn about the available Square SDKs that you can use to build solutions.
- url: https://developer.squareup.com/docs/oauth-api/overview
  name: OAuth API
  type: Authentication
  description: 'null'
- url: https://developer.squareup.com/docs/webhooks/webhook-subscriptions-api
  name: Webhook Subscriptions API
  type: Webhooks
  description: 'null'
- url: https://developer.squareup.com/forums/
  name: Square Developer Forums - Forums for asking about Square APIs and SDKs
  type: Forums
  description: 'null'
- url: https://squareup.com/us/en/partnerships
  name: 'Square Partner Program: Help Sellers Run Their Businesses'
  type: Partners
  description: 'null'
- url: https://squareup.com/us/en/pricing
  name: Square Processing Fees, Plans, and Software Pricing
  type: Pricing
  description: 'null'
- url: https://squareup.com/help/us/en
  name: Square Support Center - US
  type: Support
  description: 'null'
created: '2025-02-08'
modified: '2026-04-07'
position: Consumer
description: Square provides APIs for payment processing, point of sale, and business management solutions enabling developers to build custom commerce applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

