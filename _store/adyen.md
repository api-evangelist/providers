---
aid: adyen

url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/adyen.yml

apis:

  - aid: adyen:adyen-accounting-notifications-api

    name: Adyen Accounting Notifications API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://cal-test.adyen.com

    humanURL: >-

      https://docs.adyen.com/marketplaces-and-platforms/classic/configure-notifications/

    overlays:

      - url: overlays/accounting-notifications-openapi-search.yml

        type: APIs.io Search

      - url: overlays/accounting-notifications-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/classic/configure-notifications/

        type: Documentation

      - url: openapi/accounting-notifications-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends notifications through webhooks to inform your system about

      incoming and outgoing transfers in your platform. You can use these

      webhooks to build your implementation. For example, you can use this

      information to update balances in your own dashboards or to keep track of

      incoming funds.

  - aid: adyen:adyen-account-api

    name: Adyen Account API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://cal-test.adyen.com

    humanURL: https://docs.adyen.com/api-explorer/Account/6/overview

    overlays:

      - url: overlays/accounts-openapi-search.yml

        type: APIs.io Search

      - url: overlays/accounts-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/Account/6/overview

        type: Documentation

      - url: openapi/accounts-openapi-original.yml

        type: OpenAPI

    description: >-

      This API is used for the classic integration. If you are just starting

      your implementation, refer to our new integration guide instead. The

      Account API provides endpoints for managing account-related entities on

      your platform. These related entities include account holders, accounts,

      bank accounts, shareholders, and verification-related documents. The

      management operations include actions such as creation, retrieval,

      updating, and deletion of them.

  - aid: adyen:adyen-authentication-webhooks-api

    name: Adyen Authentication Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://cal-test.adyen.com

    humanURL: https://docs.adyen.com/development-resources/webhooks/

    overlays:

      - url: overlays/authentication-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/authentication-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/development-resources/webhooks/

        type: Documentation

      - url: openapi/authentication-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends webhooks to inform your system about events related to

      cardholder authentication.

  - aid: adyen:adyen-balance-control-api

    name: Adyen Balance Control API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://cal-test.adyen.com

    humanURL: https://docs.adyen.com/api-explorer/BalanceControl/1/overview

    overlays:

      - url: overlays/balance-control-openapi-search.yml

        type: APIs.io Search

      - url: overlays/balance-control-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/BalanceControl/1/overview

        type: Documentation

      - url: openapi/balance-control-openapi-original.yml

        type: OpenAPI

    description: >-

      The Balance Control API lets you transfer funds between merchant accounts

      that belong to the same legal entity and are under the same company

      account.

  - aid: adyen:adyen-binlookup-api

    name: Adyen BinLookup API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://pal-test.adyen.com

    humanURL: https://docs.adyen.com/api-explorer/BinLookup/52/overview

    overlays:

      - url: overlays/binlookup-openapi-search.yml

        type: APIs.io Search

      - url: overlays/binlookup-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/BinLookup/52/overview

        type: Documentation

      - url: openapi/binlookup-openapi-original.yml

        type: OpenAPI

    description: >-

      The BIN Lookup API provides endpoints for retrieving information, such as

      cost estimates, and 3D Secure supported version based on a given BIN.

  - aid: adyen:adyen-checkout-api

    name: Adyen Checkout API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/Checkout/71/overview

    overlays:

      - url: overlays/checkout-openapi-search.yml

        type: APIs.io Search

      - url: overlays/checkout-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/Checkout/71/overview

        type: Documentation

      - url: openapi/checkout-openapi-original.yml

        type: OpenAPI

    description: This is the description of your API.

  - aid: adyen:adyen-configuration-api

    name: Adyen Configuration API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/balanceplatform/2/overview

    overlays:

      - url: overlays/configuration-openapi-search.yml

        type: APIs.io Search

      - url: overlays/configuration-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/balanceplatform/2/overview

        type: Documentation

      - url: openapi/configuration-openapi-original.yml

        type: OpenAPI

    description: >-

      The Configuration API enables you to create a platform where you can

      onboard your users as account holders and create balance accounts, cards,

      and business accounts.

  - aid: adyen:adyen-configuration-webhooks-api

    name: Adyen Configuration Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/1/overview

    overlays:

      - url: overlays/configuration-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/configuration-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/api-explorer/balanceplatform-webhooks/1/overview

        type: Documentation

      - url: openapi/configuration-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends webhooks to inform your system about events that occur in your

      platform. These events include, for example, when an account holders

      capabilities are updated, or when a sweep configuration is created or

      updated. When an event occurs, Adyen makes an HTTP POST request to a URL

      on your server and includes the details of the event in the request body.

      You can use these webhooks to build your implementation.

  - aid: adyen:adyen-data-protection-api

    name: Adyen Data Protection API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://gdpr-info.eu/art-17-gdpr/

    overlays:

      - url: overlays/data-protection-openapi-search.yml

        type: APIs.io Search

      - url: overlays/data-protection-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://gdpr-info.eu/art-17-gdpr/

        type: Documentation

      - url: openapi/data-protection-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen Data Protection API provides a way for you to process [Subject

      Erasure Requests](https://gdpr-info.eu/art-17-gdpr/) as mandated in GDPR.

      Use our API to submit a request to delete shopper''s data, including

      payment details and other related information (for example, delivery

      address or shopper email).

  - aid: adyen:adyen-disputes-api

    name: Adyen Disputes API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/risk-management/disputes-api

    overlays:

      - url: overlays/disputes-openapi-search.yml

        type: APIs.io Search

      - url: overlays/disputes-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/risk-management/disputes-api

        type: Documentation

      - url: openapi/disputes-openapi-original.yml

        type: OpenAPI

    description: >-

      You can use the Disputes API to automate the dispute handling process so

      that you can respond to disputes and chargebacks as soon as they are

      initiated. The Disputes API lets you retrieve defense reasons, supply and

      delete defense documents, and accept or defend disputes.

  - aid: adyen:adyen-funds-api

    name: Adyen Funds API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/fund-transfer/

    overlays:

      - url: overlays/funds-openapi-search.yml

        type: APIs.io Search

      - url: overlays/funds-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/classic/fund-transfer/

        type: Documentation

      - url: openapi/funds-openapi-original.yml

        type: OpenAPI

    description: >-

      The Fund API provides endpoints for managing the funds in the accounts on

      your platform. These management operations include, for example, the

      transfer of funds from one account to another, the payout of funds to an

      account holder, and the retrieval of balances in an account.

  - aid: adyen:adyen-hosted-onboarding-api

    name: Adyen Hosted Onboarding API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/hosted/

    overlays:

      - url: overlays/hosted-onboarding-openapi-search.yml

        type: APIs.io Search

      - url: overlays/hosted-onboarding-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/collect-verification-details/hosted/

        type: Documentation

      - url: openapi/hosted-onboarding-openapi-original.yml

        type: OpenAPI

    description: >-

      The Fund API provides endpoints for managing the funds in the accounts on

      your platform. These management operations include, for example, the

      transfer of funds from one account to another, the payout of funds to an

      account holder, and the retrieval of balances in an account.

  - aid: adyen:adyen-legal-entity-api

    name: Adyen Legal Entity API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/marketplaces-and-platforms/legal-entity-management-api/

    overlays:

      - url: overlays/legal-entity-openapi-search.yml

        type: APIs.io Search

      - url: overlays/legal-entity-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/legal-entity-management-api/

        type: Documentation

      - url: openapi/legal-entity-openapi-original.yml

        type: OpenAPI

    description: >-

      The Legal Entity Management API enables you to manage legal entities that

      contain information required for verification.

  - aid: adyen:adyen-legal-entity-api

    name: Adyen Legal Entity API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/marketplaces-and-platforms/legal-entity-management-api/

    overlays:

      - url: overlays/legal-entity-openapi-search.yml

        type: APIs.io Search

      - url: overlays/legal-entity-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/legal-entity-management-api/

        type: Documentation

      - url: openapi/legal-entity-openapi-original.yml

        type: OpenAPI

    description: >-

      The Legal Entity Management API enables you to manage legal entities that

      contain information required for verification.

  - aid: adyen:adyen-management-api

    name: Adyen Management API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/Management/3/overview

    overlays:

      - url: overlays/management-openapi-search.yml

        type: APIs.io Search

      - url: overlays/management-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/Management/3/overview

        type: Documentation

      - url: openapi/management-openapi-original.yml

        type: OpenAPI

    description: >-

      Configure and manage your Adyen company and merchant accounts, stores, and

      payment terminals.

  - aid: adyen:adyen-management-webhooks-api

    name: Adyen Management Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/#/ManagementService/latest/overview

    overlays:

      - url: overlays/management-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/management-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/api-explorer/#/ManagementService/latest/overview

        type: Documentation

      - url: openapi/management-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen uses webhooks to inform your system about events that happen with

      your Adyen company and merchant accounts, stores, payment terminals, and

      payment methods when using [Management

      API](https://docs.adyen.com/api-explorer/#/ManagementService/latest/overview).

      When a and includes the details of the event in the request body. See

      [Webhooks](https://docs.adyen.com/development-resources/webhooks) for more

      information.

  - aid: adyen:adyen-notification-configuration-api

    name: Adyen Notification Configuration API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/notifications

    overlays:

      - url: overlays/notification-configurations-openapi-search.yml

        type: APIs.io Search

      - url: >-

          overlays/notification-configurations-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/classic/notifications

        type: Documentation

      - url: openapi/notification-configurations-openapi-original.yml

        type: OpenAPI

    description: >-

      This API is used for the classic integration. If you are just starting

      your implementation, refer to our [new integration

      guide](https://docs.adyen.com/marketplaces-and-platforms) instead.\n\nThe

      Notification Configuration API provides endpoints for setting up and

      testing notifications that inform you of events on your platform, for

      example when a verification check or a payout has been completed.\n\nFor

      more information, refer to our

      [documentation](https://docs.adyen.com/marketplaces-and-platforms/classic/notifications).

  - aid: adyen:adyen-notification-webhooks-api

    name: Adyen Notification Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/point-of-sale/design-your-integration/notifications/

    overlays:

      - url: overlays/notification-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/notification-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/point-of-sale/design-your-integration/notifications/

        type: Documentation

      - url: openapi/notification-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends notifications through webhooks to inform your system about

      events that occur in the balance platform. These events include, for

      example, a card user making a payment, or a merchant starting a refund.

      When an event occurs, Adyen makes an HTTP POST request to a URL on your

      server and includes the details of the event in the request body. You can

      use the webhooks to build your implementation. For example, you can use

      this information to update balances in your own dashboards or to keep

      track of incoming funds.

  - aid: adyen:adyen-notifications-api

    name: Adyen Notifications API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/marketplaces-and-platforms/classic/notifications

    overlays:

      - url: overlays/notifications-openapi-search.yml

        type: APIs.io Search

      - url: overlays/notifications-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/classic/notifications

        type: Documentation

      - url: openapi/notifications-openapi-original.yml

        type: OpenAPI

    description: >-

      The Notification API sends notifications to the endpoints specified in a

      given subscription. Subscriptions are managed through the Notification

      Configuration API. The API specifications listed here detail the format of

      each notification. For more information, refer to our

      [documentation](https://docs.adyen.com/marketplaces-and-platforms/classic/notifications).

  - aid: adyen:adyen-payments-api

    name: Adyen Payments API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/online-payments/

    overlays:

      - url: overlays/payments-openapi-search.yml

        type: APIs.io Search

      - url: overlays/payments-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/online-payments/

        type: Documentation

      - url: openapi/payments-openapi-original.yml

        type: OpenAPI

    description: >-

      A set of API endpoints that allow you to initiate, settle, and modify

      payments on the Adyen payments platform. You can use the API to accept

      card payments (including One-Click and 3D Secure), bank transfers,

      ewallets, and many other payment methods.

  - aid: adyen:adyen-payouts-api

    name: Adyen Payouts API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/online-payments/online-payouts

    overlays:

      - url: overlays/payouts-openapi-search.yml

        type: APIs.io Search

      - url: overlays/payouts-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/online-payments/online-payouts

        type: Documentation

      - url: openapi/payouts-openapi-original.yml

        type: OpenAPI

    description: >-

      A set of API endpoints that allow you to store payout details, confirm, or

      decline a payout.\n\nFor more information, refer to [Online

      payouts](https://docs.adyen.com/online-payments/online-payouts).

  - aid: adyen:adyen-pos-terminal-api

    name: Adyen POS Terminal API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/

    overlays:

      - url: overlays/pos-terminal-openapi-search.yml

        type: APIs.io Search

      - url: overlays/pos-terminal-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/

        type: Documentation

      - url: openapi/pos-terminal-openapi-original.yml

        type: OpenAPI

    description: >-

      This API provides endpoints for managing your point-of-sale (POS) payment

      terminals. You can use the API to obtain information about a specific

      terminal, retrieve overviews of your terminals and stores, and assign

      terminals to a merchant account or store.

  - aid: adyen:adyen-recurring-api

    name: Adyen Recurring API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/online-payments/tokenization

    overlays:

      - url: overlays/recurring-openapi-search.yml

        type: APIs.io Search

      - url: overlays/recurring-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/online-payments/tokenization

        type: Documentation

      - url: openapi/recurring-openapi-original.yml

        type: OpenAPI

    description: >-

      The Recurring APIs allow you to manage and remove your tokens or saved

      payment details. Tokens should be created with validation during a payment

      request. For more information, refer to our [Tokenization

      documentation](https://docs.adyen.com/online-payments/tokenization).

  - aid: adyen:adyen-report-webhooks-api

    name: Adyen Report Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/report-webhooks/1/overview

    overlays:

      - url: overlays/report-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/report-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/report-webhooks/1/overview

        type: Documentation

      - url: openapi/report-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends webhooks to inform your system that reports were generated and

      are ready to be downloaded. You can download reports programmatically by

      making an HTTP GET request, or manually from your [Balance Platform

      Customer Area](https://balanceplatform-test.adyen.com/balanceplatform).

  - aid: adyen:adyen-stored-value-api

    name: Adyen Stored Value API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/

    overlays:

      - url: overlays/stored-value-openapi-search.yml

        type: APIs.io Search

      - url: overlays/stored-value-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/payment-methods/gift-cards/stored-value-api/

        type: Documentation

      - url: openapi/stored-value-openapi-original.yml

        type: OpenAPI

    description: A set of API endpoints to manage stored value products.

  - aid: adyen:adyen-terminal-api

    name: Adyen Terminal API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/terminal-api-reference/

    overlays:

      - url: overlays/terminal-openapi-search.yml

        type: APIs.io Search

      - url: overlays/terminal-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/terminal-api-reference/

        type: Documentation

      - url: openapi/terminal-openapi-original.yml

        type: OpenAPI

    description: >-

      The Adyen Terminal API lets you make payments, issue refunds, collect

      shopper information, and perform other shopper-terminal interactions using

      a payment terminal supplied by Adyen.

  - aid: adyen:adyen-test-cards-api

    name: Adyen Test Cards API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/development-resources/testing/create-test-cards

    overlays:

      - url: overlays/test-cards-openapi-search.yml

        type: APIs.io Search

      - url: overlays/test-cards-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/development-resources/testing/create-test-cards

        type: Documentation

      - url: openapi/test-cards-openapi-original.yml

        type: OpenAPI

    description: >-

      The Test Cards API provides endpoints for generating custom test card

      numbers. For more information, refer to [Custom test

      cards](https://docs.adyen.com/development-resources/testing/create-test-cards)

      documentation.

  - aid: adyen:adyen-transaction-webhooks-api

    name: Adyen Transaction Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/marketplaces-and-platforms/business-accounts/transactions/transaction-webhooks/

    overlays:

      - url: overlays/transaction-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/transaction-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/business-accounts/transactions/transaction-webhooks/

        type: Documentation

      - url: openapi/transaction-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends webhooks to inform your system about incoming and outgoing

      transfers in your platform. You can use these webhooks to build your

      implementation. For example, you can use this information to update

      balances in your own dashboards or to keep track of incoming funds.

  - aid: adyen:adyen-transfer-webhooks-api

    name: Adyen Transfer Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/api-explorer/transfer-webhooks/3/overview

    overlays:

      - url: overlays/transfer-webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/transfer-webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/api-explorer/transfer-webhooks/3/overview

        type: Documentation

      - url: openapi/transfer-webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      Adyen sends webhooks to inform your system about incoming and outgoing

      transfers in your platform. You can use these webhooks to build your

      implementation. For example, you can use this information to update

      balances in your own dashboards or to keep track of incoming funds.

  - aid: adyen:adyen-transfers-api

    name: Adyen Transfers API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: >-

      https://docs.adyen.com/marketplaces-and-platforms/payout-to-users/on-demand-payouts

    overlays:

      - url: overlays/transfers-openapi-search.yml

        type: APIs.io Search

      - url: overlays/transfers-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: >-

          https://docs.adyen.com/marketplaces-and-platforms/payout-to-users/on-demand-payouts

        type: Documentation

      - url: openapi/transfers-openapi-original.yml

        type: OpenAPI

    description: >-

      This API provides endpoints that you can use to transfer funds, whether

      when [paying out to a transfer

      instrument](https://docs.adyen.com/marketplaces-and-platforms/payout-to-users/on-demand-payouts),

      [sending funds to third

      parties](https://docs.adyen.com/marketplaces-and-platforms/business-accounts/send-receive-funds)

      for users with business bank accounts, or to [request a payout for a grant

      offer](https://docs.adyen.com/marketplaces-and-platforms/capital). The API

      also supports use cases for [getting transactions for business bank

      accounts](https://docs.adyen.com/marketplaces-and-platforms/business-accounts/transactions-api)

      and getting [grants and its outstanding

      balances](https://docs.adyen.com/marketplaces-and-platforms/capital#get-balances).

  - aid: adyen:adyen-webhooks-api

    name: Adyen Webhooks API

    tags: []

    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

    baseURL: https://api.example.com

    humanURL: https://docs.adyen.com/development-resources/webhooks

    overlays:

      - url: overlays/webhooks-openapi-search.yml

        type: APIs.io Search

      - url: overlays/webhooks-openapi-api-evangelist-ratings.yml

        type: API Evangelist Ratings

    properties:

      - url: https://docs.adyen.com/development-resources/webhooks

        type: Documentation

      - url: openapi/webhooks-openapi-original.yml

        type: OpenAPI

    description: >-

      We use webhooks to send you updates about payment status updates, newly

      available reports, and other events that you can subscribe to. For more

      information, refer to our

      [documentation](https://docs.adyen.com/development-resources/webhooks).

name: Adyen

tags:

  - Payments

image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg

common:

  - url: https://www.adyen.com/legal/terms-and-conditions

    type: Terms of Service

  - url: https://www.adyen.com/authentication-3d-secure

    type: Authentication

  - url: https://www.adyen.com/pricing

    type: Plans

  - url: https://docs.adyen.com/

    type: Documentation

  - url: https://www.adyen.com/newsletter

    type: Newsletter

  - url: https://www.adyen.com/knowledge-hub

    type: Knowledge

  - url: https://authn-live.adyen.com/authn/ui/login

    type: Login

  - url: https://help.adyen.com/en_US

    type: Support

  - url: https://help.adyen.com/en_US/contact

    type: Contact

  - url: https://help.adyen.com/en_US/academy/webinars

    type: Webinars

  - url: https://www.adyen.com/policies-and-disclaimer/privacy-policy

    type: Privacy

  - url: https://github.com/Adyen/adyen-openapi

    type: OpenAPI

created: 2023/11/13

modified: '2024-12-24'

description: >-

  End-to-end payments, data, and financial management in a single solution. Meet

  the financial technology platform that helps you realize your ambitions

  faster.

maintainers:

  - FN: API Evangelist

    url: http://apievangelist.com

    email: info@apievangelist.com

specificationVersion: '0.16'

---