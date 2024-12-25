---

name: Plaid
description: >-
  Plaid is focused on democratizing financial services through technology. We
  build beautiful consumer experiences, developer-friendly infrastructure, and
  intelligent tools that give everyone the ability to create amazing products
  that solve big problems.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/banking/main/_apis/plaid/apis.md
created: '2024-07-07T00:00:00.000Z'
modified: '2024-07-07T00:00:00.000Z'
specificationVersion: '0.16'
tags: []
apis:
  - name: Plaid Asset Report API
    description: >-
      Create, delete, retrieve and share Asset Reports with information about a
      user's assets and transactions.
    tags:
      - Assets
      - Reports
      - PDF
      - Refresh
      - Filter
      - Audit
      - Copy
      - Credit
      - Endpoints
      - Format
      - Freddie
    properties:
      - type: OpenAPI
        url: properties/plaid-asset-report--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/assets/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-asset-report--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-asset-report--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/assets/
    baseURL: https://production.plaid.com
    score: 428
    aid: plaid:plaid-asset-report-api
  - name: Plaid Base Report API
    description: API for retrieving a base report for an account.
    tags:
      - Accounts
      - Applicants
      - Applications
      - Bank
      - Base
      - CRA
      - Cash
      - Data
      - Decisions
      - Flows
      - Income
      - Information
      - Insights
      - Loan
      - Loans
      - Partners
      - Register
      - Reports
      - Unregister
      - Used
      - Verification
    properties:
      - type: OpenAPI
        url: properties/plaid-cra--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-cra--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-cra--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/check/api/
    score: 213
    baseURL: https://production.plaid.com
    aid: plaid:plaid-base-report-api
  - name: Plaid Consumer Report API
    description: >-
      Consumer Report provides lenders, property managers, and buy now pay later
      providers real-time visibility into a borrower's finances, along with
      signals only made possible through our vantage point as the leading open
      banking network.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-consumer-report-pdf-get--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-consumer-report-pdf-get--openapi-search.yml
    humanURL: https://plaid.com/docs/check/api/
    baseURL: https://production.plaid.com
    aid: plaid:plaid-consumer-report-api
  - name: Plaid Statements API
    description: API reference for Statements endpoints and webhooks.
    tags:
      - Associated
      - Items
      - Statements
      - Download
      - Single
      - Data
      - Refresh
    properties:
      - type: OpenAPI
        url: properties/plaid-statements--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/statements/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-statements--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-statements--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/statements/
    score: 155
    baseURL: https://production.plaid.com
    aid: plaid:plaid-statements-api
  - name: Plaid Item API
    description: API reference for retrieving and deleting Items.
    tags:
      - Access
      - Access Token
      - Accounts
      - Activity
      - Applications
      - Ate
      - Connected
      - Consent
      - Errors
      - Events
      - Exchange
      - Fire
      - Force
      - Historical
      - Import
      - Inval
      - Invalidate
      - Items
      - Login
      - Logs
      - Public
      - Reset
      - Sandbox
      - Scopes
      - Sets
      - States
      - Status
      - Tests
      - Tokens
      - URL
      - Unlink
      - Users
      - User's
      - Verification
      - Webhooks
    properties:
      - type: OpenAPI
        url: properties/plaid-item--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/items/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-item--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-item--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/items/
    score: 760
    baseURL: https://production.plaid.com
    aid: plaid:plaid-item-api
  - name: Plaid Application API
    description: For managing application data.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-application--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/items/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-application--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-application--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/items/
    score: 295
    baseURL: https://production.plaid.com
    aid: plaid:plaid-application-api
  - name: Plaid Profile API
    description: Use to manage Plaid profile data.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-profile--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-profile--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-profile--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/
    score: 218
    baseURL: https://production.plaid.com
    aid: plaid:plaid-profile-api
  - name: Plaid Auth API
    description: >+
      Retrieve bank account information to set up electronic funds transfers,
      such as ACH payments in the US, EFT payments in Canada, BACS payments in
      the UK, and IBAN / SIC payments in the EU.

    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-auth--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/auth/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-auth--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-auth--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/auth/
    baseURL: https://production.plaid.com
    score: 218
    aid: plaid:plaid-auth-api
  - name: Plaid Transactions API
    description: >-
      Retrieve and refresh up to 24 months of historical transaction data,
      including geolocation, merchant, and category information.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-transactions--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/transactions/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-transactions--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-transactions--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/transactions/
    baseURL: https://production.plaid.com
    score: 1113
    aid: plaid:plaid-transactions-api
  - name: Plaid Institutions API
    description: >-
      Institutions endpoints support querying all institutions, as well as
      looking up a single institution to retrieve up-to-date information about
      its health status and capabilities. This can be useful for apps whose
      business logic may depend on institution capabilities, such as Payment
      Initiation. API-provided institution health data can also be used for
      in-app UIs.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-institutions--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/institutions/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-institutions--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-institutions--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/institutions/
    baseURL: https://production.plaid.com
    score: 278
    aid: plaid:plaid-institutions-api
  - name: Plaid Accounts API
    description: >-
      API reference for retrieving account information and seeing all possible
      account types and subtypes
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-accounts--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/accounts/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-accounts--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-accounts--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/accounts/
    baseURL: https://production.plaid.com
    score: 208
    aid: plaid:plaid-accounts-api
  - name: Plaid Categories API
    description: >-
      To access detailed information on categories returned by Plaid, simply
      make a request to the /categories/get endpoint of the API.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-categories--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/transactions/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-categories--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-categories--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/transactions/#categoriesget
    baseURL: https://production.plaid.com
    score: 44
    aid: plaid:plaid-categories-api
  - name: Plaid Sandbox API
    description: >-
      The Plaid Sandbox is a free and fully-featured environment for application
      development and testing. All Plaid functionality of both the Plaid API and
      Plaid Link is supported in the Sandbox environment. 
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-sandbox--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/sandbox/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-sandbox--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-sandbox--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/sandbox/
    score: 635
    baseURL: https://production.plaid.com
    aid: plaid:plaid-sandbox-api
  - name: Plaid Accounts API
    description: >-
      API reference for retrieving account information and seeing all possible
      account types and subtypes
    tags:
      - Accounts
      - Balance
      - Data
      - Real Time
    properties:
      - type: OpenAPI
        url: properties/plaid-accounts--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/accounts/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-accounts--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-accounts--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/accounts/
    score: 66
    baseURL: https://production.plaid.com
    aid: plaid:plaid-accounts-api
  - name: Plaid Entity API - DELETE
    description: Needs description.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-identity--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-identity--openapi-search.yml
    aid: plaid:plaid-entity-api-delete
  - name: Plaid Dashboard User API
    description: >-
      The Plaid Dashboard Activity Log shows the past 14 days of API activity.
      Using the dashboard, you can see a record of all requests and responses,
      as well as all webhooks sent by the Plaid API, and all Link events.
    tags:
      - Dashboard
      - Users
    properties:
      - type: OpenAPI
        url: properties/plaid-dashboard-user--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/account/activity/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-dashboard-user--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-dashboard-user--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/account/activity/
    baseURL: https://production.plaid.com
    score: 58
    aid: plaid:plaid-dashboard-user-api
  - name: Plaid Entity Verification API
    description: API reference for Identity Verification endpoints and webhooks.
    tags:
      - Entities
      - Identity
      - Verification
      - Verifications
      - Retry
      - Autofill
    properties:
      - type: OpenAPI
        url: properties/plaid-identity-verification--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-identity-verification--openapi-search.yml
      - type: API Evangelist Ratings
        url: >-
          overlays/plaid-identity-verification--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/identity-verification/
    score: 122
    baseURL: https://production.plaid.com
    aid: plaid:plaid-entity-verification-api
  - name: Plaid Watchlist Screening API
    description: API reference for Monitor endpoints and webhooks.
    tags:
      - Entities
      - Screening
      - Watchlist
      - History
      - Screenings
      - Hit
      - Hits
      - Program
      - Programs
      - Reviews
      - Indiv
      - Person
      - Ual
      - Individual
    properties:
      - type: OpenAPI
        url: properties/plaid-watchlist-screening--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-watchlist-screening--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-watchlist-screening--openapi-api-evangelist-ratings.yml
    score: 440
    humanURL: https://plaid.com/docs/api/products/monitor/
    baseURL: https://production.plaid.com
    aid: plaid:plaid-watchlist-screening-api
  - name: Plaid Beacon API
    description: API reference for Beacon endpoints and webhooks.
    tags:
      - Accounts
      - Bank
      - Beacon
      - Evaluate
      - Risk
      - Users
      - Reviews
      - Reports
      - Syndication
      - Syndications
      - Data
      - Identity
      - Duplicate
      - History
    properties:
      - type: OpenAPI
        url: properties/plaid-beacon--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/beacon/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-beacon--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-beacon--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/beacon/
    score: 279
    baseURL: https://production.plaid.com
    aid: plaid:plaid-beacon-api
  - name: Plaid Entity Verification API
    description: API reference for Identity Verification endpoints and webhooks.
    tags:
      - Entities
      - Identity
      - Verification
      - Verifications
      - Retry
      - Autofill
    properties:
      - type: OpenAPI
        url: properties/plaid-identity-verification--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/identity-verification/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-identity-verification--openapi-search.yml
      - type: API Evangelist Ratings
        url: >-
          overlays/plaid-identity-verification--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/identity-verification/
    score: 122
    baseURL: https://production.plaid.com
    aid: plaid:plaid-entity-verification-api
  - name: Plaid Processor API
    description: >-
      Partner processor endpoints are used by Plaid partners to integrate with
      Plaid. Instead of using an access_token associated with a Plaid Item,
      these endpoints use a processor_token to identify a single financial
      account. 
    tags:
      - Authentication
      - Data
      - Processor
      - Accounts
      - Associated
      - Tokens
      - Transactions
      - Incremental
      - Sync
      - Refresh
      - Fetch
      - Recurring
      - Streams
      - ACH
      - Evaluate
      - Planned
      - Signals
      - Decision
      - Initiated
      - Reports
      - Whether
      - Opt In
      - Prepare
      - Bank
      - Transfers
      - Liabilities
      - Entities
      - Identity
      - Match
      - Scores
      - Balance
      - Access
      - Controls
      - Permissions
      - Processor's
      - Products
      - Sets
      - Token's
      - URL
      - Webhooks
      - Stripe
      - Apex
    properties:
      - type: OpenAPI
        url: properties/plaid-processor--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/processor-partners/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-processor--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-processor--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/processor-partners/
    score: 529
    baseURL: https://production.plaid.com
    aid: plaid:plaid-processor-api
  - name: Plaid Webhook Verification API
    description: >-
      Plaid signs all outgoing webhooks so that you can verify the authenticity
      of any incoming webhooks to your application. 
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-webhook-verification--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/webhooks/webhook-verification/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-webhook-verification--openapi-search.yml
    humanURL: https://plaid.com/docs/api/webhooks/webhook-verification/
    baseURL: https://production.plaid.com
    aid: plaid:plaid-webhook-verification-api
  - name: Plaid Liabilities API
    description: API reference for Liabilities endpoints and webhooks.
    tags:
      - Data
      - Liabilities
      - Processor
    properties:
      - type: OpenAPI
        url: properties/plaid-liabilities--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/liabilities/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-liabilities--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-liabilities--openapi-api-evangelist-ratings.yml
    score: 60
    humanURL: https://plaid.com/docs/api/products/liabilities/
    baseURL: https://production.plaid.com
    aid: plaid:plaid-liabilities-api
  - name: Plaid Payment Initiation API
    description: >-
      Make payment transfers from your app. Plaid supports both domestic
      payments denominated in local currencies and international payments,
      generally denominated in Euro. 
    tags:
      - Initiation
      - Payments
      - Recipient
      - Existing
      - Reverse
      - Recipients
      - Tokens
      - Consent
      - Revoke
      - Execute
      - Single
      - Using
      - Details
    properties:
      - type: OpenAPI
        url: properties/plaid-payment-initiation--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/payment-initiation/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-payment-initiation--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-payment-initiation--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/payment-initiation/
    score: 275
    baseURL: https://production.plaid.com
    aid: plaid:plaid-payment-initiation-api
  - name: Plaid Beacon API
    description: API reference for Beacon endpoints and webhooks.
    tags:
      - Beacon
      - Users
      - Reviews
      - Data
      - Identity
      - History
      - Information
    properties:
      - type: OpenAPI
        url: properties/plaid-user--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/beacon/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-user--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-user--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/beacon/
    score: 168
    baseURL: https://production.plaid.com
    aid: plaid:plaid-beacon-api
  - name: Plaid Credit API
    description: API reference for credit endpoints and webhooks
    tags:
      - Audit
      - Copy
      - Credit
      - Tokens
      - Link
      - Sessions
      - Users
      - Assets
      - Income
      - Reports
      - Endpoints
      - Format
      - Freddie
      - (VOE)
      - (aka
      - Assets),
      - Available
      - Employment
      - VOA
      - Verification
      - Accounts
      - Bank
      - Beta
      - Information
      - Used
      - PDF
      - Refresh
      - Notifications
      - Proactive
      - Profiles
      - Subscribe
      - Unsubscribe
      - Webhooks
      - Configurations
      - Documents
      - Parsing
      - Payroll
      - Data
      - Statements
      - Uploaded
      - Uploads
      - Document(s)
      - Fraud
      - Insights
      - Manually
      - Risk
      - Signals
      - Checks
      - Conversions
      - Eligibility
      - Optimize
      - Precheck
      - Individual's
      - Summaries
      - Digital
      - Clients
      - Partners
      - Relay
      - Share
      - Associated
      - Shared
      - (beta)
    properties:
      - type: OpenAPI
        url: properties/plaid-credit--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-credit--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-credit--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/assets/
    score: 535
    baseURL: https://production.plaid.com
    aid: plaid:plaid-credit-api
  - name: Plaid Investments API
    description: Needs descriptionView holdings and transactions from investment accounts.
    tags:
      - Holdings
      - Investments
      - Transactions
      - Data
      - Refresh
      - Authentication
      - Authorize
      - Needed
      - Transfers
    properties:
      - type: OpenAPI
        url: properties/plaid-investments--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/investments/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-investments--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-investments--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/investments/
    score: 109
    baseURL: https://production.plaid.com
    aid: plaid:plaid-investments-api
  - name: Plaid Deposit Switch API
    description: For managing deposit swtiches.
    tags:
      - Deposit
      - Switch
      - Tokens
      - Alt
      - Exchange
      - Plaid
      - Using
    properties:
      - type: OpenAPI
        url: properties/plaid-deposit-switch--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-deposit-switch--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-deposit-switch--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/
    score: 102
    baseURL: https://production.plaid.com
    aid: plaid:plaid-deposit-switch-api
  - name: Plaid Link API
    description: Use Link to connect to your users' financial accounts with the Plaid API
    tags:
      - Checks
      - Eligibility
      - Link
      - Profiles
      - Tokens
      - Correlation
      - Exchange
      - OAuth
    properties:
      - type: OpenAPI
        url: properties/plaid-link--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/link/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-link--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-link--openapi-api-evangelist-ratings.yml
    score: 102
    humanURL: https://plaid.com/docs/link/
    baseURL: https://production.plaid.com
    aid: plaid:plaid-link-api
  - name: Plaid Transfer API
    description: API reference for Transfer endpoints and webhooks.
    tags:
      - Transfers
      - Recurring
      - Authorization
      - Cancels
      - (Deprecated)
      - Balance
      - Held
      - Plaid
      - Capabilities
      - Eligibility
      - Information
      - RTP
      - Configurations
      - Products
      - Ledgers
      - Available
      - Between
      - Distribute
      - Items
      - Move
      - Originators
      - Platforms
      - Deposit
      - Funds
      - Withdraw
      - Accounts
      - Associated
      - Funding
      - Originator
      - Metrics
      - Usage
      - Events
      - Sync
      - Sweep
      - Sweeps
      - Migrate
      - Intent
      - Invoke
      - Objects
      - UI
      - About
      - Historical
      - Repayment
      - Repayments
      - Included
      - Generate
      - Onboarding
      - Plaid Hosted
      - Questionnaires
      - URL
      - Behalf
      - Diligence
      - Submit
      - Documents
      - Uploads
      - Originator's
      - Status
      - Originators'
      - Refunds
      - Creating
      - Sandbox
      - Simulate
      - Converting
      - Pending
      - Creation
      - Triggers
      - Fire
      - Manually
      - Webhooks
      - Clock
      - Tests
      - Advance
      - Clocks
    properties:
      - type: OpenAPI
        url: properties/plaid-transfer--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/transfer/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-transfer--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-transfer--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/transfer/
    score: 1358
    baseURL: https://production.plaid.com
    aid: plaid:plaid-transfer-api
  - name: Plaid Bank Transfer API
    description: API reference for Transfer endpoints and webhooks.
    tags:
      - Bank
      - Processor
      - Transfers
      - Cancels
      - Events
      - Sync
      - Sweep
      - Sweeps
      - Accounts
      - Balance
      - Migrate
      - Sandbox
      - Simulate
      - Fire
      - Manually
      - Webhooks
    properties:
      - type: OpenAPI
        url: properties/plaid-bank-transfer--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/transfer/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-bank-transfer--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-bank-transfer--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/transfer/
    score: 372
    baseURL: https://production.plaid.com
    aid: plaid:plaid-bank-transfer-api
  - name: Plaid Employers API
    description: API for managingn employer information.
    tags:
      - Databases
      - Employer
      - Employers
      - Search
    properties:
      - type: OpenAPI
        url: properties/plaid-employers--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/income/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-employers--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-employers--openapi-api-evangelist-ratings.yml
    score: 38
    humanURL: https://plaid.com/docs/income/
    baseURL: https://production.plaid.com
    aid: plaid:plaid-employers-api
  - name: Plaid Income API
    description: Verify income and paystubs with Income.
    tags:
      - (Deprecated)
      - Income
      - Instances
      - Verification
      - Information
      - Paystubs
      - Used
      - Documents
      - Download
      - Original
      - Taxes
      - Taxforms
      - Checks
      - Conversions
      - Digital
      - Eligibility
      - Optimize
      - Precheck
      - Fire
      - Manually
      - Sandbox
      - Webhooks
    properties:
      - type: OpenAPI
        url: properties/plaid-income--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/income/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-income--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-income--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/income/
    score: 164
    baseURL: https://production.plaid.com
    aid: plaid:plaid-income-api
  - name: Plaid Beta API
    description: Beta API operations that are available.
    tags:
      - Accounts
      - Bank
      - Beta
      - Credit
      - Employment
      - Information
      - Used
      - Verification
      - Data
      - Enhance
      - Locally Held
      - Transactions
      - Categories
      - Rules
      - Access
      - Associated
      - Items
      - Tokens
      - /transactions/enrich
      - Based
      - Insights
      - Obtain
      - Sent
      - Users
    properties:
      - type: OpenAPI
        url: properties/plaid-beta--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-beta--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-beta--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/
    score: 170
    baseURL: https://production.plaid.com
    aid: plaid:plaid-beta-api
  - name: Plaid Signal API
    description: |
      Assess the return risk of an ACH debit to prevent NSFs and other returns
    tags:
      - ACH
      - Evaluate
      - Planned
      - Processor
      - Signals
      - Transactions
      - Decision
      - Initiated
      - Reports
      - Whether
      - Opt In
      - Prepare
      - Tokens
      - Items
      - Opt In
    properties:
      - type: OpenAPI
        url: properties/plaid-signal--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/signal/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-signal--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-signal--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/signal/
    score: 238
    baseURL: https://production.plaid.com
    aid: plaid:plaid-signal-api
  - name: Plaid Wallet API
    description: API reference for Virtual Accounts endpoints and webhooks
    tags:
      - E Wallet
      - Wallet
      - E Wallet
      - Fetch
      - E Wallets
      - E Wallet
      - Execute
      - Transactions
      - Using
      - E Wallet
      - E Wallet
    properties:
      - type: OpenAPI
        url: properties/plaid-wallet--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/products/virtual-accounts/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-wallet--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-wallet--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/products/virtual-accounts/
    score: 143
    baseURL: https://production.plaid.com
    aid: plaid:plaid-wallet-api
  - name: Plaid Paymet Profile API - DELETE
    description: Needs description.
    tags: []
    properties:
      - type: OpenAPI
        url: properties/plaid-paymet-profile--openapi-original.yml
    overlays:
      - type: OpenAPI
        url: overlays/plaid-paymet-profile--openapi-search.yml
    aid: plaid:plaid-paymet-profile-api-delete
  - name: Plaid Sandb ox API
    description: >-
      The Plaid Sandbox is a free and fully-featured environment for application
      development and testing. All Plaid functionality of both the Plaid API and
      Plaid Link is supported in the Sandbox environment. 
    tags:
      - Login
      - Payments
      - Profiles
      - Reset
      - Sandbox
    properties:
      - type: OpenAPI
        url: properties/plaid-payment-profile--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/payment-initiation/add-to-app/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-payment-profile--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-payment-profile--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/sandbox/
    score: 120
    baseURL: https://production.plaid.com
    aid: plaid:plaid-sandb-ox-api
  - name: Plaid Partner API
    description: Create and manage end customers
    tags:
      - Creates
      - Customers
      - Partners
      - Plaid
      - Reseller
      - Reseller's
      - Enable
      - Enables
      - Environments
      - Production
      - Given
      - Information
      - Institutions
      - OAuth
      - OAuth Institution
      - Registrations
    properties:
      - type: OpenAPI
        url: properties/plaid-partner--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/api/partner/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-partner--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-partner--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/api/partner/
    score: 155
    baseURL: https://production.plaid.com
    aid: plaid:plaid-partner-api
  - name: Plaid Link Delivery API
    description: >-
      Hosted Link is the easiest and fastest way to integrate with Plaid. With
      Hosted Link, Plaid hosts the Link experience. Customers can use this link
      in web browsers or open it in a secure web context within a mobile app,
      eliminating the need for front-end implementation work. 
    tags:
      - Deliveries
      - Hosted
      - Link
      - Sessions
    properties:
      - type: OpenAPI
        url: properties/plaid-link-delivery--openapi-original.yml
      - type: Documentation
        url: https://plaid.com/docs/link/hosted-link/
    overlays:
      - type: OpenAPI
        url: overlays/plaid-link-delivery--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-link-delivery--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.com/docs/link/hosted-link/
    score: 70
    baseURL: https://production.plaid.com
    aid: plaid:plaid-link-delivery-api
  - name: Plaid FDX API
    description: >-
      The Core Exchange API specifications are a subset of the Financial Data
      Exchange (FDX) API specification, the usage thereof (or any part thereof)
      constitutes acceptance of the FDX API License Agreement, which can be
      found at https://financialdataexchange.org/.
    tags:
      - Fdx
      - Notifications
      - Receiver
      - Webhooks
    properties:
      - type: OpenAPI
        url: properties/plaid-fdx--openapi-original.yml
      - type: Documentation
        url: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
    overlays:
      - type: OpenAPI
        url: overlays/plaid-fdx--openapi-search.yml
      - type: API Evangelist Ratings
        url: overlays/plaid-fdx--openapi-api-evangelist-ratings.yml
    humanURL: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
    score: 43
    baseURL: https://production.plaid.com
    aid: plaid:plaid-fdx-api
common:
  - type: Portal
    url: https://developer.plaid.com/en/
  - type: Quickstarts
    url: https://plaid.com/docs/quickstart/
  - type: Sandbox
    url: https://plaid.com/docs/sandbox/
  - type: Errors
    url: https://plaid.com/docs/errors/
  - type: Launch Checklist
    url: https://plaid.com/docs/launch-checklist/
  - type: Support
    url: https://plaid.com/docs/support/
  - type: Change Log
    url: https://plaid.com/docs/changelog/
  - type: Login
    url: https://dashboard.plaid.com/signin
  - type: Libraries
    url: https://plaid.com/docs/api/libraries/
  - type: Versions
    url: https://plaid.com/docs/api/versioning/
  - type: Postman Collection
    url: https://plaid.com/docs/api/postman/
  - type: Webhooks
    url: https://plaid.com/docs/api/webhooks/
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
overlays:
  - type: APIs.io Search
    url: overlays/apis-io-search.yml
  - type: API Evangelist Ratings
    url: /overlays/api-evangelist-ratings.yml
aid: plaid
score: 1200
---