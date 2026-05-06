---
aid: klarna
url: |-

  https://raw.githubusercontent.com/api-search/api-reference-introduction-klarna/refs/heads/main/apis.yml
apis:
  - aid: klarna:klarna-payments-api
    name: Klarna Payments API V1
    tags:
      - Payments
    humanURL: https://docs.klarna.com/api/payments/
    properties:
      - url: https://docs.klarna.com/api/payments/
        name: Klarna Payments API
        type: Documentation
        description: |-

          The payments API is used to create a session to offer Klarna's payment
          methods as part of your checkout. As soon as the purchase is completed
          the order should be read and handled using the Order Management API.
      - url: openapi/klarna-payments-api-openapi.yml
        type: OpenAPI
    description: The payments API is used to create a session to offer Klarna's payment methods as part of your checkout. As soon as the purchase is completed the order should be read and handled using the [`Order Management API`](https://docs.klarna.com/api/ordermanagement).
  - aid: klarna:klarna-customer-token-api
    name: Klarna Payments API V1
    tags:
      - Customers
      - Tokens
    humanURL: https://docs.klarna.com/api/customertoken/
    properties:
      - url: https://docs.klarna.com/api/customertoken/
        name: Klarna Customer Token API
        type: Documentation
        description: |-

          The Customer Token API is used to charge customers with a tokenized
          Klarna payment method and can be used for recurring purchases,
          subscriptions and for storing a customer's payment method. Tokens are
          created using the generate a customer token call in the payments API.
      - url: openapi/klarna-customer-token-api-openapi.yml
        type: OpenAPI
    description: The Customer Token API is used to charge customers with a tokenized Klarna payment method and can be used for recurring purchases, subscriptions and for storing a customer's payment method. Tokens are created using the [`generate a customer token`](https://docs.klarna.com/api/payments/) call in the payments API.
  - aid: klarna:kustom-checkout-api
    name: Checkout API V3
    tags:
      - Checkout
    humanURL: https://docs.klarna.com/api/checkout/
    properties:
      - url: https://docs.klarna.com/api/checkout/
        name: Kustom Checkout API
        type: Documentation
        description: |-

          The checkout API is used to create a checkout with Klarna and update
          the checkout order during the purchase. As soon as the purchase is
          completed the order should be read and handled using the Order
          Management API. Read more on Klarna checkout.
      - url: openapi/kustom-checkout-api-openapi.yml
        type: OpenAPI
    description: The checkout API is used to create a checkout with Klarna and update the checkout order during the purchase. As soon as the purchase is completed the order should be read and handled using the [Order Management API](https://docs.klarna.com/api/ordermanagement). Read more on [Klarna checkout](https://docs.klarna.com/kco/).
  - aid: klarna:kustom-checkout-callback-api
    name: Checkout API V3
    tags:
      - Checkout
    humanURL: https://docs.klarna.com/api/checkout-merchant/
    properties:
      - url: https://docs.klarna.com/api/checkout-merchant/
        name: Kustom Checkout Callback API
        type: Documentation
        description: |-

          Klarna provides a number of different callbacks during the customer's
          checkout session. The callbacks can be used to update the order when
          the customer changes their address as well as to do a final check to
          validate the order before it is submitted.
      - url: openapi/kustom-checkout-callback-api-openapi.yml
        type: OpenAPI
    description: Klarna provides a number of different callbacks during the customer's checkout session. The callbacks can be used to update the order when the customer changes their address as well as to do a final check to validate the order before it is submitted. The callbacks are sent as POST requests to the endpoint you specify when creating the order. Your response is interpreted using the response code and body. Read more on [here](https://docs.klarna.com/kco/).
  - aid: klarna:hosted-payment-page-api
    name: Hosted Payment Page (HPP)
    tags:
      - Hosted
      - Pages
      - Payments
    humanURL: https://docs.klarna.com/api/hpp-merchant/
    properties:
      - url: https://docs.klarna.com/api/hpp-merchant/
        name: Hosted Payment Page API
        type: Documentation
        description: |-

          Hosted Payment Page (HPP) API is a service that lets you integrate
          Klarna Payments without the need of hosting the web page that manages
          the client side of Klarna Payments. A complete HPP payment session
          will involve three of Klarna services.
      - url: openapi/hosted-payment-page-api-openapi.yml
        type: OpenAPI
    description: Hosted Payment Page (HPP) API is a service that lets you integrate Klarna Payments without the need of hosting the web page that manages the client side of Klarna Payments.
  - aid: klarna:order-management-api
    name: Klarna Order Management API
    tags:
      - Orders
    humanURL: https://docs.klarna.com/api/ordermanagement/
    properties:
      - url: https://docs.klarna.com/api/ordermanagement/
        name: Order Management API
        type: Documentation
        description: |-

          The Order Management API is used for handling an order after the
          customer has completed the purchase. It is used for all actions you
          need to manage your orders. Examples being: updating, capturing,
          reading and refunding an order.
      - url: openapi/order-management-api-openapi.yml
        type: OpenAPI
    description: 'The Order Management API is used for handling an order after the customer has completed the purchase. It is used for all actions you need to manage your orders. Examples being: updating, capturing, reading and refunding an order. Read more on the [Order management](https://docs.klarna.com/order-management/) process. # Authentication.'
  - aid: klarna:merchant-card-service-api
    name: Merchant Card Service API
    tags:
      - Cards
      - Merchants
    humanURL: https://docs.klarna.com/api/merchant-card-service/
    properties:
      - url: https://docs.klarna.com/api/merchant-card-service/
        name: Merchant Card Service API
        type: Documentation
        description: |-

          The Merchant Card Service (MCS) API is used to settle orders with
          virtual credit cards.
      - url: openapi/merchant-card-service-api-openapi.yml
        type: OpenAPI
    description: The Merchant Card Service (MCS) API is used to settle orders with virtual credit cards. Read more on [Merchant card service](https://docs.klarna.com/merchant-card-service/).
  - aid: klarna:shipping-service-callback-api
    name: Shipping Service Callback API
    tags:
      - Callbacks
      - Shipping
    humanURL: https://docs.klarna.com/api/merchant-shipping-introduction/
    properties:
      - url: https://docs.klarna.com/api/merchant-shipping-introduction/
        name: Shipping Service Callback API
        type: Documentation
        description: |-

          Integrator: the Integrator implements the Klarna Shipping Service
          Callback API as described in the documentation. The Integrator is the
          upstream provider of shipping options for KSS.
    description: The Integrator implements the Klarna Shipping Service Callback API as described in the documentation. The Integrator is the upstream provider of shipping options for KSS.
  - aid: klarna:klarna-settlements-api
    name: Klarna Settlements API
    tags:
      - Settlements
    humanURL: https://docs.klarna.com/api/settlements/
    properties:
      - url: https://docs.klarna.com/api/settlements/
        name: Settlements API
        type: Documentation
        description: |-

          The Settlements API helps you with the reconciliation of payments,
          made by Klarna to your bank account. Every payment has a unique
          payment_reference that can be found in the settlement reports and on
          your bank statement.
      - url: openapi/klarna-settlements-api-openapi.yml
        type: OpenAPI
    description: 'The Settlements API helps you with the reconciliation of payments, made by Klarna to your bank account. Every payment has a unique payment_reference that can be found in the settlement reports and on your bank statement. Read more on [Settlement reports](https://docs.klarna.com/settlement-reports/). # Authentication.'
  - aid: klarna:klarna-disputes-api
    name: Disputes API V2
    tags:
      - Disputes
      - Payments
    humanURL: https://docs.klarna.com/api/disputes-api/disputes-api_2.0.0/
    properties:
      - url: https://docs.klarna.com/api/disputes-api/disputes-api_2.0.0/
        name: Disputes API
        type: Documentation
        description: |-

          The Disputes API offers Klarna partners and merchants an easy way to
          handle customer disputes.
      - url: openapi/klarna-disputes-api-openapi.yml
        type: OpenAPI
    description: The Disputes API offers Klarna partners and merchants an easy way to handle customer disputes.
name: Klarna
tags:
  - Payments
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://docs.klarna.com/api/authentication/
    name: API Authentication
    type: Authentication
  - url: https://docs.klarna.com/api/errors/
    name: Errors
    type: Errors
  - url: https://docs.klarna.com/api/rate-limit/
    name: Rate limit
    type: RateLimits
  - url: https://docs.klarna.com/
    name: Klarna Docs
    type: Documentation
  - url: |-

      https://docs.klarna.com/resources/developer-tools/error-handling/error-codes-and-messages/
    name: Klarna Docs - Error codes and messages
    type: Errors
  - url: https://docs.klarna.com/resources/business-tools/glossary/
    name: Klarna Docs - Glossary
    type: Glossary
  - url: https://docs.klarna.com/platform-solutions/
    name: Klarna Docs - Platform integrations
    type: Integrations
  - url: |-

      https://www.klarna.com/international/terms-and-conditions/?_gl=1*1842tzc*_ga*NDI0ODM2NTg2LjE3MzE0NTIyMDk.*_ga_F4RYPWHEGX*MTczMjU2NzcwMy4zLjEuMTczMjU2ODQyMS4wLjAuMjE4NDI5NzU5
    name: Terms and Conditions | Klarna International
    type: TermsOfService
  - url: https://status.klarna.com/
    name: Klarna Status
    type: Status
  - url: https://status.klarna.com/history
    name: Klarna Status - Incident History
    type: StatusHistory
created: '2024-11-12T00:00:00.000Z'
modified: '2026-04-28'
position: Consuming
description: Klarna Bank AB, commonly referred to as Klarna, is a Swedish fintech company that provides online financial services. The company provides payment processing services for the e-commerce industry, managing store claims and customer payments. The company is a "buy now, pay later" service provider.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
