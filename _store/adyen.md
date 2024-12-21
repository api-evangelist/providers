---
aid: adyen
url: https://raw.githubusercontent.com/api-search/payments/main/_apis/adyen/apis.md
apis:
  - aid: adyen:adyen-accounting-notifications-api
    name: Adyen Accounting Notifications API
    tags: []
    overlays:
      - url: overlays/accounting-notifications-openapi-search.yml
        type: APIs.io Search
      - url: overlays/accounting-notifications-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen sends notifications through webhooks to inform your system about
      incoming and outgoing transfers in your platform. You can use these
      webhooks to build your implementation. For example, you can use this
      information to update balances in your own dashboards or to keep track of
      incoming funds.
  - aid: adyen:adyen-account-api
    name: Adyen Account API
    tags:
      - Accounts
      - Arrangements
      - Bank
      - Close
      - Documents
      - Forms
      - Holders
      - Legal
      - Methods
      - Payouts
      - Processing
      - Shareholders
      - Signatories
      - States
      - Stores
      - Suspend
      - Taxes
      - Triggers
      - Unsuspend
      - Uploaded
      - Uploads
      - Verification
    overlays:
      - url: overlays/accounts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/accounts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
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
    overlays:
      - url: overlays/authentication-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/authentication-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen sends webhooks to inform your system about events related to
      cardholder authentication.
  - aid: adyen:adyen-balance-control-api
    name: Adyen Balance Control API
    tags:
      - Balance
      - Transfers
    overlays:
      - url: overlays/balance-control-openapi-search.yml
        type: APIs.io Search
      - url: overlays/balance-control-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Balance Control API lets you transfer funds between merchant accounts
      that belong to the same legal entity and are under the same company
      account.
  - aid: adyen:adyen-binlookup-api
    name: Adyen BinLookup API
    tags:
      - Availability
      - Available
      - Checks
      - Cost
      - Estimates
      - Fees
      - If
      - Is
      - Secure
    overlays:
      - url: overlays/binlookup-openapi-search.yml
        type: APIs.io Search
      - url: overlays/binlookup-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The BIN Lookup API provides endpoints for retrieving information, such as
      cost estimates, and 3D Secure supported version based on a given BIN.
  - aid: adyen:adyen-checkout-api
    name: Adyen Checkout API
    tags:
      - Checkout
      - Payments
    humanURL: https://docs.adyen.com/api-explorer/Checkout/latest/overview
    overlays:
      - url: overlays/checkout-openapi-search.yml
        type: APIs.io Search
      - url: overlays/checkout-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen Checkout API provides a simple and flexible way to initiate and
      authorise online payments. You can use the same integration for payments
      made with cards (including 3D Secure), mobile wallets, and local payment
      methods (for example, iDEAL and Sofort).
  - aid: adyen:adyen-configuration-api
    name: Adyen Configuration API
    tags:
      - Configurations
      - Cards
      - Balance Accounts
      - Business Accounts
      - Accounts
    overlays:
      - url: overlays/configuration-openapi-search.yml
        type: APIs.io Search
      - url: overlays/configuration-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Configuration API enables you to create a platform where you can
      onboard your users as account holders and create balance accounts, cards,
      and business accounts.
  - aid: adyen:adyen-configuration-webhooks-api
    name: Adyen Configuration Webhooks API
    tags: []
    overlays:
      - url: overlays/configuration-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/configuration-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen sends webhooks to inform your system about events that occur in your
      platform. These events include, for example, when an account holders
      capabilities are updated, or when a sweep configuration is created or
      updated. When an event occurs, Adyen makes an HTTP POST request to a URL
      on your server and includes the details of the event in the request body.
      You can use these webhooks to build your implementation.
  - aid: adyen:adyen-data-protection-api
    name: Adyen Data Protection API
    tags:
      - Erasure
      - Subjects
      - Submit
    overlays:
      - url: overlays/data-protection-openapi-search.yml
        type: APIs.io Search
      - url: overlays/data-protection-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen Data Protection API provides a way for you to process [Subject
      Erasure Requests](https://gdpr-info.eu/art-17-gdpr/) as mandated in GDPR.
      Use our API to submit a request to delete shopper''s data, including
      payment details and other related information (for example, delivery
      address or shopper email).
  - aid: adyen:adyen-disputes-api
    name: Adyen Disputes API
    tags:
      - Accept
      - Applicable
      - Defend
      - Defense
      - Disputes
      - Documents
      - Reasons
      - Supply
    overlays:
      - url: overlays/disputes-openapi-search.yml
        type: APIs.io Search
      - url: overlays/disputes-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      You can use the Disputes API to automate the dispute handling process so
      that you can respond to disputes and chargebacks as soon as they are
      initiated. The Disputes API lets you retrieve defense reasons, supply and
      delete defense documents, and accept or defend disputes.
  - aid: adyen:adyen-funds-api
    name: Adyen Funds API
    tags:
      - Accounts
      - Balance
      - Balances
      - Benefactor's
      - Beneficiary
      - Between
      - Current
      - Debit
      - Designate
      - Direct
      - Funds
      - Holders
      - Most
      - Out
      - Paid
      - Pay
      - Payouts
      - Platforms
      - Recent
      - Refunds
      - Send
      - Since
      - The
      - Transactions
      - Transfers
    overlays:
      - url: overlays/funds-openapi-search.yml
        type: APIs.io Search
      - url: overlays/funds-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Fund API provides endpoints for managing the funds in the accounts on
      your platform. These management operations include, for example, the
      transfer of funds from one account to another, the payout of funds to an
      account holder, and the retrieval of balances in an account.
  - aid: adyen:adyen-hosted-onboarding-api
    name: Adyen Hosted Onboarding API
    tags:
      - Adyen-hosted
      - Compliance
      - Link
      - Onboarding
      - PCI
      - Page
      - Questionnaires
      - URL
    overlays:
      - url: overlays/hosted-onboarding-openapi-search.yml
        type: APIs.io Search
      - url: overlays/hosted-onboarding-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Fund API provides endpoints for managing the funds in the accounts on
      your platform. These management operations include, for example, the
      transfer of funds from one account to another, the payout of funds to an
      account holder, and the retrieval of balances in an account.
  - aid: adyen:adyen-legal-entity-api
    name: Adyen Legal Entity API
    tags:
      - Accept
      - Acceptance
      - Adyen-hosted
      - Business
      - Checks
      - Confirm
      - Data
      - Details
      - Documents
      - Entities
      - Errors
      - Generate
      - Hosted
      - Information
      - Instruments
      - Legal
      - Line
      - Lines
      - Link
      - Links
      - Onboarding
      - PCI
      - Page
      - Pciid
      - Questionnaires
      - Reviews
      - Services
      - Sign
      - Status
      - Templates
      - Terms
      - Terms Of Service Documents
      - Theme
      - Themes
      - Transfers
      - Under
      - Uploads
      - Verification
    overlays:
      - url: overlays/legal-entity-openapi-search.yml
        type: APIs.io Search
      - url: overlays/legal-entity-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Legal Entity Management API enables you to manage legal entities that
      contain information required for verification.
  - aid: adyen:adyen-legal-entity-api
    name: Adyen Legal Entity API
    tags:
      - Accept
      - Acceptance
      - Adyen-hosted
      - Business
      - Checks
      - Confirm
      - Data
      - Details
      - Documents
      - Entities
      - Errors
      - Generate
      - Hosted
      - Information
      - Instruments
      - Legal
      - Line
      - Lines
      - Link
      - Links
      - Onboarding
      - PCI
      - Page
      - Pciid
      - Questionnaires
      - Reviews
      - Services
      - Sign
      - Status
      - Templates
      - Terms
      - Terms Of Service Documents
      - Theme
      - Themes
      - Transfers
      - Under
      - Uploads
      - Verification
    overlays:
      - url: overlays/legal-entity-openapi-search.yml
        type: APIs.io Search
      - url: overlays/legal-entity-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Legal Entity Management API enables you to manage legal entities that
      contain information required for verification.
  - aid: adyen:adyen-management-api
    name: Adyen Management API
    tags:
      - Accounts
      - Actions
      - Activate
      - Allowed
      - Android
      - Apple
      - Applications
      - Billing
      - Cancel
      - Certificates
      - Clients
      - Companies
      - Conditions
      - Configurations
      - Credentials
      - Descriptions
      - Details
      - Domains
      - Entities
      - Generate
      - HMAC
      - Keys
      - Locations
      - Logic
      - Logo
      - Logos
      - Me
      - Merchants
      - Methods
      - Models
      - Orders
      - Origin
      - Origins
      - Pay
      - Payments
      - Payouts
      - Products
      - Reassign
      - References
      - Removes
      - Rules
      - Sets
      - Settings
      - Shipping
      - Split
      - Store
      - Stores
      - Terminal
      - Terminals
      - Tests
      - The
      - Up
      - Uploads
      - Users
      - Webhooks
    overlays:
      - url: overlays/management-openapi-search.yml
        type: APIs.io Search
      - url: overlays/management-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Configure and manage your Adyen company and merchant accounts, stores, and
      payment terminals.
  - aid: adyen:adyen-management-webhooks-api
    name: Adyen Management Webhooks API
    tags: []
    overlays:
      - url: overlays/management-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/management-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
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
    tags:
      - Configurations
      - Notifications
      - Subscribe
      - Subscriptions
      - Tests
    overlays:
      - url: overlays/notification-configurations-openapi-search.yml
        type: APIs.io Search
      - url: >-
          overlays/notification-configurations-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
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
    overlays:
      - url: overlays/notification-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/notification-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
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
    overlays:
      - url: overlays/notifications-openapi-search.yml
        type: APIs.io Search
      - url: overlays/notifications-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Notification API sends notifications to the endpoints specified in a
      given subscription. Subscriptions are managed through the Notification
      Configuration API. The API specifications listed here detail the format of
      each notification. For more information, refer to our
      [documentation](https://docs.adyen.com/marketplaces-and-platforms/classic/notifications).
  - aid: adyen:adyen-payments-api
    name: Adyen Payments API
    tags:
      - Amount
      - Authentication
      - Authorised
      - Authorization
      - Cancel
      - Capture
      - Captured
      - Change
      - Complete
      - Donate
      - Donations
      - In-person
      - Payments
      - Pending
      - References
      - Refunds
      - Results
      - The
      - Using
      - Your
      - ~!
    overlays:
      - url: overlays/payments-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payments-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      A set of API endpoints that allow you to initiate, settle, and modify
      payments on the Adyen payments platform. You can use the API to accept
      card payments (including One-Click and 3D Secure), bank transfers,
      ewallets, and many other payment methods.
  - aid: adyen:adyen-payouts-api
    name: Adyen Payouts API
    tags:
      - Cancel
      - Cards
      - Confirm
      - Detail
      - Details
      - Instant
      - Make
      - Party
      - Payouts
      - Store
      - Submit
      - Third
    overlays:
      - url: overlays/payouts-openapi-search.yml
        type: APIs.io Search
      - url: overlays/payouts-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      A set of API endpoints that allow you to store payout details, confirm, or
      decline a payout.\n\nFor more information, refer to [Online
      payouts](https://docs.adyen.com/online-payments/online-payouts).
  - aid: adyen:adyen-pos-terminal-api
    name: Adyen POS Terminal API
    tags:
      - Accounts
      - Assign
      - Details
      - Store
      - Stores
      - Terminal
      - Terminals
      - The
      - Under
    overlays:
      - url: overlays/pos-terminal-openapi-search.yml
        type: APIs.io Search
      - url: overlays/pos-terminal-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      This API provides endpoints for managing your point-of-sale (POS) payment
      terminals. You can use the API to obtain information about a specific
      terminal, retrieve overviews of your terminals and stores, and assign
      terminals to a merchant account or store.
  - aid: adyen:adyen-recurring-api
    name: Adyen Recurring API
    tags:
      - Accounts
      - Ask
      - Contracts
      - Details
      - Disable
      - Existing
      - Issuer
      - Linked
      - Notify
      - Payments
      - Permits
      - Recurring
      - Running
      - Schedules
      - Shopper
      - Stored
      - The
    overlays:
      - url: overlays/recurring-openapi-search.yml
        type: APIs.io Search
      - url: overlays/recurring-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Recurring APIs allow you to manage and remove your tokens or saved
      payment details. Tokens should be created with validation during a payment
      request. For more information, refer to our [Tokenization
      documentation](https://docs.adyen.com/online-payments/tokenization).
  - aid: adyen:adyen-report-webhooks-api
    name: Adyen Report Webhooks API
    tags: []
    overlays:
      - url: overlays/report-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/report-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen sends webhooks to inform your system that reports were generated and
      are ready to be downloaded. You can download reports programmatically by
      making an HTTP GET request, or manually from your [Balance Platform
      Customer Area](https://balanceplatform-test.adyen.com/balanceplatform).
  - aid: adyen:adyen-stored-value-api
    name: Adyen Stored Value API
    tags:
      - Balance
      - Cards
      - Change
      - Changes
      - Checks
      - Issues
      - Load
      - Loads
      - Merge
      - Methods
      - Payments
      - Status
      - The
      - Transactions
      - Voids
    overlays:
      - url: overlays/stored-value-openapi-search.yml
        type: APIs.io Search
      - url: overlays/stored-value-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: A set of API endpoints to manage stored value products.
  - aid: adyen:adyen-terminal-api
    name: Adyen Terminal API
    tags:
      - Acquisition
      - Administrative
      - Balance
      - Balance Inquiry
      - Card Acquisitions
      - Card Reader Applications
      - Cards
      - Diagnosis
      - Display
      - Enable
      - Enable Service
      - Gettotals
      - Inputs
      - Inquiries
      - Login
      - Logout
      - Loyalty
      - Payments
      - Print
      - Readers
      - Reconciliation
      - Reversals
      - Services
      - Status
      - Stored
      - Stored Values
      - Totals
      - Transaction Status
      - Transactions
      - Value
    overlays:
      - url: overlays/terminal-openapi-search.yml
        type: APIs.io Search
      - url: overlays/terminal-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Adyen Terminal API lets you make payments, issue refunds, collect
      shopper information, and perform other shopper-terminal interactions using
      a payment terminal supplied by Adyen.
  - aid: adyen:adyen-test-cards-api
    name: Adyen Test Cards API
    tags:
      - Cards
      - Creates
      - More
      - One
      - Ranges
      - Tests
    overlays:
      - url: overlays/test-cards-openapi-search.yml
        type: APIs.io Search
      - url: overlays/test-cards-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      The Test Cards API provides endpoints for generating custom test card
      numbers. For more information, refer to [Custom test
      cards](https://docs.adyen.com/development-resources/testing/create-test-cards)
      documentation.
  - aid: adyen:adyen-transaction-webhooks-api
    name: Adyen Transaction Webhooks API
    tags: []
    overlays:
      - url: overlays/transaction-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/transaction-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen sends webhooks to inform your system about incoming and outgoing
      transfers in your platform. You can use these webhooks to build your
      implementation. For example, you can use this information to update
      balances in your own dashboards or to keep track of incoming funds.
  - aid: adyen:adyen-transfer-webhooks-api
    name: Adyen Transfer Webhooks API
    tags: []
    overlays:
      - url: overlays/transfer-webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/transfer-webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      Adyen sends webhooks to inform your system about incoming and outgoing
      transfers in your platform. You can use these webhooks to build your
      implementation. For example, you can use this information to update
      balances in your own dashboards or to keep track of incoming funds.
  - aid: adyen:adyen-transfers-api
    name: Adyen Transfers API
    tags:
      - Accounts
      - Capital
      - Details
      - Funds
      - Grants
      - Grants""
      - Payouts
      - References
      - Returns
      - Transactions
      - Transfers
    overlays:
      - url: overlays/transfers-openapi-search.yml
        type: APIs.io Search
      - url: overlays/transfers-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
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
    overlays:
      - url: overlays/webhooks-openapi-search.yml
        type: APIs.io Search
      - url: overlays/webhooks-openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    description: >-
      We use webhooks to send you updates about payment status updates, newly
      available reports, and other events that you can subscribe to. For more
      information, refer to our
      [documentation](https://docs.adyen.com/development-resources/webhooks).
name: Adyen
tags: []
created: 2024/04/14
modified: '2024-07-03'
description: >-
  End-to-end payments, data, and financial management in a single solution. Meet
  the financial technology platform that helps you realize your ambitions
  faster.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
slug: adyen
---