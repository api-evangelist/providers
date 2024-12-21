---
aid: plaid
url: https://raw.githubusercontent.com/api-search/banking/main/_apis/plaid/apis.md
apis:
  - aid: plaid:plaid-asset-report-api
    name: Plaid Asset Report API
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
    score: 428
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/assets/
    overlays:
      - url: overlays/plaid-asset-report--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-asset-report--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-asset-report--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/assets/
        type: Documentation
    description: >-
      Create, delete, retrieve and share Asset Reports with information about a
      user's assets and transactions.
  - aid: plaid:plaid-base-report-api
    name: Plaid Base Report API
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
    score: 213
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/check/api/
    overlays:
      - url: overlays/plaid-cra--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-cra--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-cra--openapi-original.yml
        type: OpenAPI
    description: API for retrieving a base report for an account.
  - aid: plaid:plaid-consumer-report-api
    name: Plaid Consumer Report API
    tags: []
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/check/api/
    overlays:
      - url: overlays/plaid-consumer-report-pdf-get--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/plaid-consumer-report-pdf-get--openapi-original.yml
        type: OpenAPI
    description: >-
      Consumer Report provides lenders, property managers, and buy now pay later
      providers real-time visibility into a borrower's finances, along with
      signals only made possible through our vantage point as the leading open
      banking network.
  - aid: plaid:plaid-statements-api
    name: Plaid Statements API
    tags:
      - Associated
      - Items
      - Statements
      - Download
      - Single
      - Data
      - Refresh
    score: 155
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/statements/
    overlays:
      - url: overlays/plaid-statements--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-statements--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-statements--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/statements/
        type: Documentation
    description: API reference for Statements endpoints and webhooks.
  - aid: plaid:plaid-item-api
    name: Plaid Item API
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
    score: 760
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/items/
    overlays:
      - url: overlays/plaid-item--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-item--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-item--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/items/
        type: Documentation
    description: API reference for retrieving and deleting Items.
  - aid: plaid:plaid-application-api
    name: Plaid Application API
    tags: []
    score: 295
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/items/
    overlays:
      - url: overlays/plaid-application--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-application--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-application--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/items/
        type: Documentation
    description: For managing application data.
  - aid: plaid:plaid-profile-api
    name: Plaid Profile API
    tags: []
    score: 218
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/
    overlays:
      - url: overlays/plaid-profile--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-profile--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-profile--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/
        type: Documentation
    description: Use to manage Plaid profile data.
  - aid: plaid:plaid-auth-api
    name: Plaid Auth API
    tags: []
    score: 218
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/auth/
    overlays:
      - url: overlays/plaid-auth--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-auth--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-auth--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/auth/
        type: Documentation
    description: >+
      Retrieve bank account information to set up electronic funds transfers,
      such as ACH payments in the US, EFT payments in Canada, BACS payments in
      the UK, and IBAN / SIC payments in the EU.

  - aid: plaid:plaid-transactions-api
    name: Plaid Transactions API
    tags: []
    score: 1113
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/transactions/
    overlays:
      - url: overlays/plaid-transactions--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-transactions--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-transactions--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transactions/
        type: Documentation
    description: >-
      Retrieve and refresh up to 24 months of historical transaction data,
      including geolocation, merchant, and category information.
  - aid: plaid:plaid-institutions-api
    name: Plaid Institutions API
    tags: []
    score: 278
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/institutions/
    overlays:
      - url: overlays/plaid-institutions--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-institutions--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-institutions--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/institutions/
        type: Documentation
    description: >-
      Institutions endpoints support querying all institutions, as well as
      looking up a single institution to retrieve up-to-date information about
      its health status and capabilities. This can be useful for apps whose
      business logic may depend on institution capabilities, such as Payment
      Initiation. API-provided institution health data can also be used for
      in-app UIs.
  - aid: plaid:plaid-accounts-api
    name: Plaid Accounts API
    tags: []
    score: 208
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/accounts/
    overlays:
      - url: overlays/plaid-accounts--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-accounts--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-accounts--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/accounts/
        type: Documentation
    description: >-
      API reference for retrieving account information and seeing all possible
      account types and subtypes
  - aid: plaid:plaid-categories-api
    name: Plaid Categories API
    tags: []
    score: 44
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/transactions/#categoriesget
    overlays:
      - url: overlays/plaid-categories--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-categories--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-categories--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transactions/
        type: Documentation
    description: >-
      To access detailed information on categories returned by Plaid, simply
      make a request to the /categories/get endpoint of the API.
  - aid: plaid:plaid-sandbox-api
    name: Plaid Sandbox API
    tags: []
    score: 635
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/sandbox/
    overlays:
      - url: overlays/plaid-sandbox--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-sandbox--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-sandbox--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/sandbox/
        type: Documentation
    description: >-
      The Plaid Sandbox is a free and fully-featured environment for application
      development and testing. All Plaid functionality of both the Plaid API and
      Plaid Link is supported in the Sandbox environment. 
  - aid: plaid:plaid-accounts-api
    name: Plaid Accounts API
    tags:
      - Accounts
      - Balance
      - Data
      - Real Time
    score: 66
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/accounts/
    overlays:
      - url: overlays/plaid-accounts--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-accounts--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-accounts--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/accounts/
        type: Documentation
    description: >-
      API reference for retrieving account information and seeing all possible
      account types and subtypes
  - aid: plaid:plaid-entity-api-delete
    name: Plaid Entity API - DELETE
    tags: []
    overlays:
      - url: overlays/plaid-identity--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/plaid-identity--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: plaid:plaid-dashboard-user-api
    name: Plaid Dashboard User API
    tags:
      - Dashboard
      - Users
    score: 58
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/account/activity/
    overlays:
      - url: overlays/plaid-dashboard-user--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-dashboard-user--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-dashboard-user--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/account/activity/
        type: Documentation
    description: >-
      The Plaid Dashboard Activity Log shows the past 14 days of API activity.
      Using the dashboard, you can see a record of all requests and responses,
      as well as all webhooks sent by the Plaid API, and all Link events.
  - aid: plaid:plaid-entity-verification-api
    name: Plaid Entity Verification API
    tags:
      - Entities
      - Identity
      - Verification
      - Verifications
      - Retry
      - Autofill
    score: 122
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/identity-verification/
    overlays:
      - url: overlays/plaid-identity-verification--openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/plaid-identity-verification--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-identity-verification--openapi-original.yml
        type: OpenAPI
    description: API reference for Identity Verification endpoints and webhooks.
  - aid: plaid:plaid-watchlist-screening-api
    name: Plaid Watchlist Screening API
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
    score: 440
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/monitor/
    overlays:
      - url: overlays/plaid-watchlist-screening--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-watchlist-screening--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-watchlist-screening--openapi-original.yml
        type: OpenAPI
    description: API reference for Monitor endpoints and webhooks.
  - aid: plaid:plaid-beacon-api
    name: Plaid Beacon API
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
    score: 279
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/beacon/
    overlays:
      - url: overlays/plaid-beacon--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-beacon--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-beacon--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/beacon/
        type: Documentation
    description: API reference for Beacon endpoints and webhooks.
  - aid: plaid:plaid-entity-verification-api
    name: Plaid Entity Verification API
    tags:
      - Entities
      - Identity
      - Verification
      - Verifications
      - Retry
      - Autofill
    score: 122
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/identity-verification/
    overlays:
      - url: overlays/plaid-identity-verification--openapi-search.yml
        type: OpenAPI
      - url: >-
          overlays/plaid-identity-verification--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-identity-verification--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/identity-verification/
        type: Documentation
    description: API reference for Identity Verification endpoints and webhooks.
  - aid: plaid:plaid-processor-api
    name: Plaid Processor API
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
    score: 529
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/processor-partners/
    overlays:
      - url: overlays/plaid-processor--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-processor--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-processor--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/processor-partners/
        type: Documentation
    description: >-
      Partner processor endpoints are used by Plaid partners to integrate with
      Plaid. Instead of using an access_token associated with a Plaid Item,
      these endpoints use a processor_token to identify a single financial
      account. 
  - aid: plaid:plaid-webhook-verification-api
    name: Plaid Webhook Verification API
    tags: []
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/webhooks/webhook-verification/
    overlays:
      - url: overlays/plaid-webhook-verification--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/plaid-webhook-verification--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/webhooks/webhook-verification/
        type: Documentation
    description: >-
      Plaid signs all outgoing webhooks so that you can verify the authenticity
      of any incoming webhooks to your application. 
  - aid: plaid:plaid-liabilities-api
    name: Plaid Liabilities API
    tags:
      - Data
      - Liabilities
      - Processor
    score: 60
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/liabilities/
    overlays:
      - url: overlays/plaid-liabilities--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-liabilities--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-liabilities--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/liabilities/
        type: Documentation
    description: API reference for Liabilities endpoints and webhooks.
  - aid: plaid:plaid-payment-initiation-api
    name: Plaid Payment Initiation API
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
    score: 275
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/payment-initiation/
    overlays:
      - url: overlays/plaid-payment-initiation--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-payment-initiation--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-payment-initiation--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/payment-initiation/
        type: Documentation
    description: >-
      Make payment transfers from your app. Plaid supports both domestic
      payments denominated in local currencies and international payments,
      generally denominated in Euro. 
  - aid: plaid:plaid-beacon-api
    name: Plaid Beacon API
    tags:
      - Beacon
      - Users
      - Reviews
      - Data
      - Identity
      - History
      - Information
    score: 168
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/beacon/
    overlays:
      - url: overlays/plaid-user--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-user--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-user--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/beacon/
        type: Documentation
    description: API reference for Beacon endpoints and webhooks.
  - aid: plaid:plaid-credit-api
    name: Plaid Credit API
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
    score: 535
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/assets/
    overlays:
      - url: overlays/plaid-credit--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-credit--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-credit--openapi-original.yml
        type: OpenAPI
    description: API reference for credit endpoints and webhooks
  - aid: plaid:plaid-investments-api
    name: Plaid Investments API
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
    score: 109
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/investments/
    overlays:
      - url: overlays/plaid-investments--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-investments--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-investments--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/investments/
        type: Documentation
    description: Needs descriptionView holdings and transactions from investment accounts.
  - aid: plaid:plaid-deposit-switch-api
    name: Plaid Deposit Switch API
    tags:
      - Deposit
      - Switch
      - Tokens
      - Alt
      - Exchange
      - Plaid
      - Using
    score: 102
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/
    overlays:
      - url: overlays/plaid-deposit-switch--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-deposit-switch--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-deposit-switch--openapi-original.yml
        type: OpenAPI
    description: For managing deposit swtiches.
  - aid: plaid:plaid-link-api
    name: Plaid Link API
    tags:
      - Checks
      - Eligibility
      - Link
      - Profiles
      - Tokens
      - Correlation
      - Exchange
      - OAuth
    score: 102
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/link/
    overlays:
      - url: overlays/plaid-link--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-link--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-link--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/link/
        type: Documentation
    description: Use Link to connect to your users' financial accounts with the Plaid API
  - aid: plaid:plaid-transfer-api
    name: Plaid Transfer API
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
    score: 1358
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/transfer/
    overlays:
      - url: overlays/plaid-transfer--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-transfer--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-transfer--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transfer/
        type: Documentation
    description: API reference for Transfer endpoints and webhooks.
  - aid: plaid:plaid-bank-transfer-api
    name: Plaid Bank Transfer API
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
    score: 372
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/transfer/
    overlays:
      - url: overlays/plaid-bank-transfer--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-bank-transfer--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-bank-transfer--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transfer/
        type: Documentation
    description: API reference for Transfer endpoints and webhooks.
  - aid: plaid:plaid-employers-api
    name: Plaid Employers API
    tags:
      - Databases
      - Employer
      - Employers
      - Search
    score: 38
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/income/
    overlays:
      - url: overlays/plaid-employers--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-employers--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-employers--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/income/
        type: Documentation
    description: API for managingn employer information.
  - aid: plaid:plaid-income-api
    name: Plaid Income API
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
    score: 164
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/income/
    overlays:
      - url: overlays/plaid-income--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-income--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-income--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/income/
        type: Documentation
    description: Verify income and paystubs with Income.
  - aid: plaid:plaid-beta-api
    name: Plaid Beta API
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
    score: 170
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/
    overlays:
      - url: overlays/plaid-beta--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-beta--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-beta--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/
        type: Documentation
    description: Beta API operations that are available.
  - aid: plaid:plaid-signal-api
    name: Plaid Signal API
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
    score: 238
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/signal/
    overlays:
      - url: overlays/plaid-signal--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-signal--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-signal--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/signal/
        type: Documentation
    description: |
      Assess the return risk of an ACH debit to prevent NSFs and other returns
  - aid: plaid:plaid-wallet-api
    name: Plaid Wallet API
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
    score: 143
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/virtual-accounts/
    overlays:
      - url: overlays/plaid-wallet--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-wallet--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-wallet--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/virtual-accounts/
        type: Documentation
    description: API reference for Virtual Accounts endpoints and webhooks
  - aid: plaid:plaid-paymet-profile-api-delete
    name: Plaid Paymet Profile API - DELETE
    tags: []
    overlays:
      - url: overlays/plaid-paymet-profile--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/plaid-paymet-profile--openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: plaid:plaid-sandb-ox-api
    name: Plaid Sandb ox API
    tags:
      - Login
      - Payments
      - Profiles
      - Reset
      - Sandbox
    score: 120
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/sandbox/
    overlays:
      - url: overlays/plaid-payment-profile--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-payment-profile--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-payment-profile--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/payment-initiation/add-to-app/
        type: Documentation
    description: >-
      The Plaid Sandbox is a free and fully-featured environment for application
      development and testing. All Plaid functionality of both the Plaid API and
      Plaid Link is supported in the Sandbox environment. 
  - aid: plaid:plaid-partner-api
    name: Plaid Partner API
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
    score: 155
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/partner/
    overlays:
      - url: overlays/plaid-partner--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-partner--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-partner--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/partner/
        type: Documentation
    description: Create and manage end customers
  - aid: plaid:plaid-link-delivery-api
    name: Plaid Link Delivery API
    tags:
      - Deliveries
      - Hosted
      - Link
      - Sessions
    score: 70
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/link/hosted-link/
    overlays:
      - url: overlays/plaid-link-delivery--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-link-delivery--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-link-delivery--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/link/hosted-link/
        type: Documentation
    description: >-
      Hosted Link is the easiest and fastest way to integrate with Plaid. With
      Hosted Link, Plaid hosts the Link experience. Customers can use this link
      in web browsers or open it in a secure web context within a mobile app,
      eliminating the need for front-end implementation work. 
  - aid: plaid:plaid-fdx-api
    name: Plaid FDX API
    tags:
      - Fdx
      - Notifications
      - Receiver
      - Webhooks
    score: 43
    baseURL: https://production.plaid.com
    humanURL: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
    overlays:
      - url: overlays/plaid-fdx--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-fdx--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: properties/plaid-fdx--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
        type: Documentation
    description: >-
      The Core Exchange API specifications are a subset of the Financial Data
      Exchange (FDX) API specification, the usage thereof (or any part thereof)
      constitutes acceptance of the FDX API License Agreement, which can be
      found at https://financialdataexchange.org/.
name: Plaid
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
score: 1200
common:
  - url: https://developer.plaid.com/en/
    type: Portal
  - url: https://plaid.com/docs/quickstart/
    type: Quickstarts
  - url: https://plaid.com/docs/sandbox/
    type: Sandbox
  - url: https://plaid.com/docs/errors/
    type: Errors
  - url: https://plaid.com/docs/launch-checklist/
    type: Launch Checklist
  - url: https://plaid.com/docs/support/
    type: Support
  - url: https://plaid.com/docs/changelog/
    type: Change Log
  - url: https://dashboard.plaid.com/signin
    type: Login
  - url: https://plaid.com/docs/api/libraries/
    type: Libraries
  - url: https://plaid.com/docs/api/versioning/
    type: Versions
  - url: https://plaid.com/docs/api/postman/
    type: Postman Collection
  - url: https://plaid.com/docs/api/webhooks/
    type: Webhooks
created: '2024-07-07T00:00:00.000Z'
modified: '2024-07-07T00:00:00.000Z'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: /overlays/api-evangelist-ratings.yml
    type: API Evangelist Ratings
description: >-
  Plaid is focused on democratizing financial services through technology. We
  build beautiful consumer experiences, developer-friendly infrastructure, and
  intelligent tools that give everyone the ability to create amazing products
  that solve big problems.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
slug: plaid
---