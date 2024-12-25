---
aid: paypal
url: >-

  https://raw.githubusercontent.com/api-search/payments/main/_apis/paypal/apis.md
apis:
  - aid: paypal:paypal-billing-subscriptions-api
    name: Paypal Billing Subscriptions API
    tags: []
    overlays:
      - url: >-

          overlays/https://raw.githubusercontent.com/paypal/paypal-rest-api-specifications/main/openapi/billing_subscriptions_v1.json-openapi-search.yml
        type: APIs.io Search
    description: |-

      You can use billing plans and subscriptions to create subscriptions that
      process recurring PayPal payments for physical or digital goods, or
      services. A plan includes pricing and billing cycle information that
      defines the amount and frequency of charge for a subscription. You can
      also define a fixed plan, such as a $5 basic plan or a volume- or
      graduated-based plan with pricing tiers based on the quantity purchased.
      For more information, see <a href=\"/docs/subscriptions/\">Subscriptions
      Overview</a>.
  - aid: paypal:paypal-catalog-products-api
    name: Paypal Catalog Products API
    tags: []
    overlays:
      - url: >-

          overlays/https://raw.githubusercontent.com/paypal/paypal-rest-api-specifications/main/openapi/catalogs_products_v1.json-openapi-search.yml
        type: APIs.io Search
    description: |-

      Merchants can use the Catalog Products API to create products, which are
      goods and services.
  - aid: paypal:paypal-orders-api
    name: Paypal Orders API
    tags: []
    overlays:
      - url: >-

          overlays/https://raw.githubusercontent.com/paypal/paypal-rest-api-specifications/main/openapi/checkout_orders_v2.json-openapi-search.yml
        type: APIs.io Search
    description: |-

      An order represents a payment between two or more parties. Use the Orders
      API to create, update, retrieve, authorize, and capture orders.
  - aid: paypal:paypal-disputes-api
    name: Paypal Disputes API
    tags: []
    overlays:
      - url: >-

          overlays/https://raw.githubusercontent.com/paypal/paypal-rest-api-specifications/main/openapi/customer_disputes_v1.json-openapi-search.yml
        type: APIs.io Search
    description: |-

      Occasionally, something goes wrong with a customer's order. To dispute a
      charge, a customer can create a dispute with PayPal. PayPal merchants,
      partners, and external developers can use the PayPal Disputes API to
      manage customer disputes.
name: Paypal
tags:
  - Payments
  - Invoices
type: Index
score: 25
access: 3rd-Party
created: 2024/04/14
modified: '2024-11-14'
position: Consumer
description: |-

  PayPal allows any business or individual with an email address to securely,
  conveniently and cost-effectively send and receive payments online. Our
  network builds on the existing financial infrastructure of bank accounts and
  credit cards to create a global, real-time payment solution.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---