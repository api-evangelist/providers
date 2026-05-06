---
aid: plaid
url: https://raw.githubusercontent.com/api-evangelist/plaid/refs/heads/main/apis.yml
apis:
  - aid: plaid:plaid-asset-report-api
    name: Plaid Asset Report API
    tags:
      - Assets
      - Audit
      - Copy
      - Credit
      - Endpoints
      - Filter
      - Format
      - Freddie
      - PDF
      - Refresh
      - Reports
    score: 428
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/assets/
    overlays:
      - url: overlays/plaid-asset-report--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-asset-report--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-asset-report--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/assets/
        type: Documentation
    description: Plaid Asset Report API is a powerful tool that allows users to access detailed information on their financial assets and liabilities. By aggregating data from various financial institutions, the API provides a comprehensive overview of an individual's financial standing, including account balances, transaction history, and asset allocation. This data can be invaluable for individuals looking to track their financial health, make informed investment decisions, or plan for future expenses. With the Plaid Asset Report API, users can quickly and securely access their financial information in real-time, allowing for greater insight and control over their financial well-being.
  - aid: plaid:plaid-base-report-api
    name: Plaid Base Report API
    tags:
      - Accounts
      - Applicants
      - Applications
      - Bank
      - Base
      - Cash
      - CRA
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
      - url: openapi/plaid-cra--openapi-original.yml
        type: OpenAPI
    description: The Plaid Base Report API is a tool that allows users to access and analyze detailed financial data from various sources, such as bank accounts, credit cards, and investment accounts. This API provides a comprehensive overview of an individual's financial transactions and balances, allowing users to track their spending habits, monitor their financial health, and make informed decisions about their financial future. With the Plaid Base Report API, users can securely and efficiently access their financial information in one centralized location, making it easier to manage and optimize their financial well-being.
  - aid: plaid:plaid-consumer-report-api
    name: Plaid Consumer Report API
    tags: []
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/check/api/
    overlays:
      - url: overlays/plaid-consumer-report-pdf-get--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/plaid-consumer-report-pdf-get--openapi-original.yml
        type: OpenAPI
    description: The Plaid Consumer Report API allows businesses to access detailed financial data about their customers in order to make more informed decisions. By connecting to customers' bank accounts and credit card accounts, the API provides real-time insights into their spending habits, credit history, and overall financial health. This valuable information can be used to personalize offerings, assess credit risk, and improve customer experiences. With the Plaid Consumer Report API, businesses can gain a comprehensive understanding of their customers' financial profiles, enabling them to tailor products and services to better meet their needs.
  - aid: plaid:plaid-statements-api
    name: Plaid Statements API
    tags:
      - Associated
      - Data
      - Download
      - Items
      - Refresh
      - Single
      - Statements
    score: 155
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/statements/
    overlays:
      - url: overlays/plaid-statements--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-statements--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-statements--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/statements/
        type: Documentation
    description: Plaid Statements API allows developers to access and retrieve bank statement data from their users' bank accounts. This data includes information such as transaction history, account balances, and pending transactions. By integrating with the Plaid Statements API, developers can offer their users a comprehensive and real-time view of their financial transactions, making it easier for them to track their spending, budget effectively, and manage their money more efficiently. Additionally, Plaid's robust security measures ensure that sensitive financial information is securely transmitted and protected.
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
      - Unlink
      - URL
      - User's
      - Users
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
      - url: openapi/plaid-item--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/items/
        type: Documentation
    description: The Plaid Item API is a tool that allows developers to retrieve detailed information about a user's financial accounts and transactions. By connecting to a user's bank or credit card account through Plaid's platform, developers can access real-time data such as account balances, transaction history, and account details. This information can then be used to build tailored financial apps and services, provide personalized insights and recommendations, and streamline the overall financial management process for users. The Plaid Item API also offers advanced security features, ensuring that sensitive financial data is protected and secure.
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
      - url: openapi/plaid-application--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/items/
        type: Documentation
    description: The Plaid Application API is a financial technology tool that allows developers to easily access and integrate with a wealth of financial data and services. This API helps developers build applications that can securely connect to users' bank accounts, verify account information, authenticate transactions, and more. By leveraging the Plaid API, developers can create custom financial solutions that improve user experience, streamline processes, and enhance overall security. Overall, the Plaid Application API is a powerful tool for driving innovation and efficiency in the financial technology space.
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
      - url: openapi/plaid-profile--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/
        type: Documentation
    description: Plaid Profile API is a tool that allows developers to securely access detailed information about their users' financial profiles. By integrating this API into their applications, developers can retrieve data such as account balances, transaction history, income, and spending habits in a quick and efficient manner. This information can then be used to provide personalized financial services, recommendations, and insights to users. With Plaid Profile API, developers can streamline the onboarding process for new users, improve the user experience, and offer more tailored financial solutions.
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
      - url: openapi/plaid-auth--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/auth/
        type: Documentation
    description: Plaid Auth API is a powerful tool that allows developers to securely access and retrieve financial data from users bank accounts. By integrating with this API, developers can streamline the account verification process and provide a seamless user experience. The API handles the authentication process and retrieves transaction history, account balances, and other financial information in a secure and compliant manner. This enables developers to build innovative financial applications, such as budgeting tools, payment solutions, and personalized financial advice services. Plaid Auth API helps developers to securely access and leverage financial data, ultimately enhancing the capabilities of their applications and delivering valuable insights to users.
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
      - url: openapi/plaid-transactions--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transactions/
        type: Documentation
    description: Plaid Transactions API is a powerful tool that allows developers to access detailed, clean, and categorized transaction data from users' financial accounts in real-time. By integrating with Plaid Transactions API, businesses can offer their customers a seamless and streamlined experience, as well as gain valuable insights into their spending habits and financial health. With robust security features and compliance measures in place, Plaid Transactions API ensures that sensitive financial information is kept safe and protected. Overall, Plaid Transactions API is a game-changer for businesses looking to optimize their financial services and provide personalized, data-driven experiences for their customers.
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
      - url: openapi/plaid-institutions--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/institutions/
        type: Documentation
    description: Plaid Institutions API is a tool designed to make it easier for developers to integrate financial institutions into their applications. By using this API, developers can access data from thousands of financial institutions, allowing users to securely connect their accounts, view balances and transaction history, and perform other financial tasks within the app. This API simplifies the process of working with multiple financial institutions, enabling developers to create more comprehensive and user-friendly financial applications. Additionally, Plaid Institutions API offers robust security measures to protect users' sensitive financial information, ensuring peace of mind for both developers and users.
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
      - url: openapi/plaid-categories--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transactions/
        type: Documentation
    description: The Plaid Categories API is a tool that provides developers with access to a comprehensive list of financial categories that can be used to classify transactions. This API allows users to categorize transactions by different types such as groceries, entertainment, bills, and more. By utilizing the Plaid Categories API, developers can access and organize transaction data in a more efficient and accurate manner, ultimately leading to better insights into spending habits and financial management. This tool can be especially useful for fintech companies, budgeting apps, and personal finance tools looking to provide users with detailed and meaningful financial data.
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
      - url: openapi/plaid-sandbox--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/sandbox/
        type: Documentation
    description: The Plaid Sandbox API is a tool that allows developers to easily test and experiment with the Plaid platform in a simulated environment. This API enables users to create and access fake financial accounts, transactions, and user profiles, allowing them to simulate real-world scenarios and interactions with the Plaid API. By using the Sandbox API, developers can quickly build and test applications that interact with financial data without the need for live, sensitive information. This API provides a safe and secure way for developers to familiarize themselves with the Plaid platform and streamline the development process.
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
      - url: openapi/plaid-accounts--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/accounts/
        type: Documentation
    description: Plaid Accounts API is a financial technology tool that enables developers to securely access and retrieve detailed information about a user's banking and financial accounts. By integrating with Plaid's API, developers can streamline the process of verifying account ownership, account balances, transaction history, and other essential financial data. This enables developers to build innovative new financial applications, services, and experiences that can help users better manage their money and make more informed financial decisions. Plaid Accounts API offers a robust and reliable solution for connecting with various financial institutions and retrieving accurate and up-to-date account information in a secure and efficient manner.
  - aid: plaid:plaid-entity-api-delete
    name: Plaid Entity API - DELETE
    tags: []
    overlays:
      - url: overlays/plaid-identity--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/plaid-identity--openapi-original.yml
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
      - url: openapi/plaid-dashboard-user--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/account/activity/
        type: Documentation
    description: The Plaid Dashboard User API is designed to provide users with comprehensive access to their financial data from various institutions in one centralized location. By connecting to multiple financial accounts, the API allows users to view a holistic picture of their finances, including account balances, transaction history, and spending patterns. This information can be used to track expenses, set budgeting goals, and better understand overall financial health. Additionally, the API provides real-time updates and notifications to keep users informed of any changes or trends in their financial situation. Overall, the Plaid Dashboard User API offers a convenient and secure way for individuals to manage and optimize their financial well-being.
  - aid: plaid:plaid-entity-verification-api
    name: Plaid Entity Verification API
    tags:
      - Autofill
      - Entities
      - Identity
      - Retry
      - Verification
      - Verifications
    score: 122
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/identity-verification/
    overlays:
      - url: overlays/plaid-identity-verification--openapi-search.yml
        type: OpenAPI
      - url: |-

          overlays/plaid-identity-verification--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-identity-verification--openapi-original.yml
        type: OpenAPI
    description: Plaid Entity Verification API is a powerful tool that allows businesses to verify the identity and ownership of individuals or entities with ease. With this API, companies can quickly and securely verify important information such as names, addresses, and account ownership to ensure the legitimacy of their customers. By leveraging Plaid's extensive network of financial institutions and data sources, businesses can streamline their verification processes, reduce fraud, and enhance the overall security of their operations. This API provides a seamless and efficient solution for businesses looking to enhance their risk management practices and build trust with their customers.
  - aid: plaid:plaid-watchlist-screening-api
    name: Plaid Watchlist Screening API
    tags:
      - Entities
      - History
      - Hit
      - Hits
      - Indiv
      - Individual
      - Person
      - Program
      - Programs
      - Reviews
      - Screening
      - Screenings
      - Ual
      - Watchlist
    score: 440
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/monitor/
    overlays:
      - url: overlays/plaid-watchlist-screening--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-watchlist-screening--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-watchlist-screening--openapi-original.yml
        type: OpenAPI
    description: Plaid Watchlist Screening API is a tool that helps companies comply with regulations by screening individuals and entities against various watchlists and sanctions lists. This API allows businesses to easily check if a customer or transaction is associated with any known criminal or illicit activities, helping them mitigate risks and ensure they are not inadvertently doing business with sanctioned individuals or entities. The API is easy to integrate into existing systems and provides real-time results, allowing businesses to make informed decisions quickly and efficiently. Overall, Plaid Watchlist Screening API helps companies maintain compliance and uphold their reputation by reducing the potential for illegal activity.
  - aid: plaid:plaid-beacon-api
    name: Plaid Beacon API
    tags:
      - Accounts
      - Bank
      - Beacon
      - Data
      - Duplicate
      - Evaluate
      - History
      - Identity
      - Reports
      - Reviews
      - Risk
      - Syndication
      - Syndications
      - Users
    score: 279
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/beacon/
    overlays:
      - url: overlays/plaid-beacon--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-beacon--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-beacon--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/beacon/
        type: Documentation
    description: Plaid Beacon API is a powerful tool that allows developers to securely access and share financial data with authorized third parties. By integrating this API into their applications, businesses can streamline their financial processes, improve customer experiences, and enhance data security. With Plaid Beacon API, developers can easily connect to a variety of financial institutions, retrieve account balances and transaction histories, verify account ownership, and automate financial tasks such as payments and transfers. This API empowers businesses to leverage financial data in innovative ways, enabling them to make more informed decisions and provide personalized services to their customers.
  - aid: plaid:plaid-processor-api
    name: Plaid Processor API
    tags:
      - Access
      - Accounts
      - ACH
      - Apex
      - Associated
      - Authentication
      - Balance
      - Bank
      - Controls
      - Data
      - Decision
      - Entities
      - Evaluate
      - Fetch
      - Identity
      - Incremental
      - Initiated
      - Liabilities
      - Match
      - Opt In
      - Permissions
      - Planned
      - Prepare
      - Processor
      - Processor's
      - Products
      - Recurring
      - Refresh
      - Reports
      - Scores
      - Sets
      - Signals
      - Streams
      - Stripe
      - Sync
      - Token's
      - Tokens
      - Transactions
      - Transfers
      - URL
      - Webhooks
      - Whether
    score: 529
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/processor-partners/
    overlays:
      - url: overlays/plaid-processor--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-processor--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-processor--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/processor-partners/
        type: Documentation
    description: The Plaid Processor API is a powerful tool that allows developers to easily integrate and access financial data from thousands of financial institutions. By using the API, developers can retrieve transaction data, account balances, and other important financial information from users' accounts. This data can then be used to power a wide range of financial applications, from budgeting tools to personal finance management apps. The Plaid Processor API also provides developers with the ability to securely authenticate users' bank accounts and make seamless transfers between accounts. Overall, the Plaid Processor API simplifies the process of accessing and managing financial data, making it easier for developers to create innovative financial products and services.
  - aid: plaid:plaid-webhook-verification-api
    name: Plaid Webhook Verification API
    tags: []
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/webhooks/webhook-verification/
    overlays:
      - url: overlays/plaid-webhook-verification--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/plaid-webhook-verification--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/webhooks/webhook-verification/
        type: Documentation
    description: Plaid Webhook Verification API is a tool designed to help businesses verify the authenticity of webhook notifications sent by Plaid, a popular financial technology platform. This API allows businesses to confirm that the incoming webhook notifications are indeed from Plaid and have not been tampered with during transit. By verifying the signatures attached to the webhook notifications, businesses can ensure the integrity and security of their data and prevent potential fraud or unauthorized access to sensitive information. Additionally, the Plaid Webhook Verification API helps businesses maintain compliance with data protection regulations and build trust with their customers by providing a secure and reliable messaging system.
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
      - url: openapi/plaid-liabilities--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/liabilities/
        type: Documentation
    description: The Plaid Liabilities API is a financial tool that allows developers to access detailed information about a user's liabilities, such as credit card balances, loans, and other debts. By connecting with a user's financial accounts, the API can provide real-time updates on the status of their liabilities, including current balances, due dates, interest rates, and minimum payments. This information can help users better manage their debts and make more informed financial decisions. Additionally, developers can use the API to create innovative financial products and services that help users pay down their debts and improve their overall financial health.
  - aid: plaid:plaid-payment-initiation-api
    name: Plaid Payment Initiation API
    tags:
      - Consent
      - Details
      - Execute
      - Existing
      - Initiation
      - Payments
      - Recipient
      - Recipients
      - Reverse
      - Revoke
      - Single
      - Tokens
      - Using
    score: 275
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/payment-initiation/
    overlays:
      - url: overlays/plaid-payment-initiation--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-payment-initiation--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-payment-initiation--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/payment-initiation/
        type: Documentation
    description: The Plaid Payment Initiation API allows businesses to initiate payments directly from their customers' bank accounts, providing a seamless and convenient way to facilitate transactions. By leveraging Plaid's secure infrastructure and established connections with financial institutions, businesses can securely transfer funds between accounts without the need for manual input. This API streamlines the payment process, reduces transaction costs, and minimizes the risk of errors or delays. With Plaid Payment Initiation API, businesses can offer their customers a more user-friendly and efficient payment experience.
  - aid: plaid:plaid-beacon-api
    name: Plaid Beacon API
    tags:
      - Beacon
      - Data
      - History
      - Identity
      - Information
      - Reviews
      - Users
    score: 168
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/beacon/
    overlays:
      - url: overlays/plaid-user--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-user--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-user--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/beacon/
        type: Documentation
    description: Plaid Beacon API is a powerful tool that allows developers to securely access and share financial data with authorized third parties. By integrating this API into their applications, businesses can streamline their financial processes, improve customer experiences, and enhance data security. With Plaid Beacon API, developers can easily connect to a variety of financial institutions, retrieve account balances and transaction histories, verify account ownership, and automate financial tasks such as payments and transfers. This API empowers businesses to leverage financial data in innovative ways, enabling them to make more informed decisions and provide personalized services to their customers.
  - aid: plaid:plaid-credit-api
    name: Plaid Credit API
    tags:
      - (Aka
      - (Beta)
      - (VOE)
      - Accounts
      - Assets
      - Assets),
      - Associated
      - Audit
      - Available
      - Bank
      - Beta
      - Checks
      - Clients
      - Configurations
      - Conversions
      - Copy
      - Credit
      - Data
      - Digital
      - Document(s)
      - Documents
      - Eligibility
      - Employment
      - Endpoints
      - Format
      - Fraud
      - Freddie
      - Income
      - Individual's
      - Information
      - Insights
      - Link
      - Manually
      - Notifications
      - Optimize
      - Parsing
      - Partners
      - Payroll
      - PDF
      - Precheck
      - Proactive
      - Profiles
      - Refresh
      - Relay
      - Reports
      - Risk
      - Sessions
      - Share
      - Shared
      - Signals
      - Statements
      - Subscribe
      - Summaries
      - Tokens
      - Unsubscribe
      - Uploaded
      - Uploads
      - Used
      - Users
      - Verification
      - VOA
      - Webhooks
    score: 535
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/assets/
    overlays:
      - url: overlays/plaid-credit--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-credit--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-credit--openapi-original.yml
        type: OpenAPI
    description: Plaid Credit API is a financial service that allows users to access their credit information in real time. By connecting to various financial institutions, Plaid Credit API can provide an overview of a users credit score, outstanding balances, payment history, and other important credit-related information. This data can be used by developers and businesses to create personalized financial tools and services that help users better manage their credit and make informed financial decisions. With its secure and reliable platform, Plaid Credit API simplifies the process of accessing credit information and empowers users to take control of their financial well-being.
  - aid: plaid:plaid-investments-api
    name: Plaid Investments API
    tags:
      - Authentication
      - Authorize
      - Data
      - Holdings
      - Investments
      - Needed
      - Refresh
      - Transactions
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
      - url: openapi/plaid-investments--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/investments/
        type: Documentation
    description: Plaid Investments API is a powerful tool that allows developers to easily access and integrate investment data into their applications. By connecting directly to financial institutions, Plaid Investments API enables users to securely retrieve information about a user's investment accounts, including holdings, transactions, and performance metrics. This information can then be used to provide valuable insights, track investments, and help users make more informed decisions about their financial future. With Plaid Investments API, developers can streamline the process of managing and analyzing investment data, ultimately creating a more seamless and efficient user experience.
  - aid: plaid:plaid-deposit-switch-api
    name: Plaid Deposit Switch API
    tags:
      - Alt
      - Deposit
      - Exchange
      - Plaid
      - Switch
      - Tokens
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
      - url: openapi/plaid-deposit-switch--openapi-original.yml
        type: OpenAPI
    description: The Plaid Deposit Switch API is a powerful tool that allows users to easily switch their direct deposit information from one financial institution to another. This API streamlines the process of moving funds by automating the necessary steps to update payroll information, reducing the time and effort required for individuals to make the switch. By enabling secure and efficient data transfer between banks, the Plaid Deposit Switch API simplifies the process of transitioning to a new account, providing users with a seamless experience when transferring their direct deposits.
  - aid: plaid:plaid-link-api
    name: Plaid Link API
    tags:
      - Checks
      - Correlation
      - Eligibility
      - Exchange
      - Link
      - OAuth
      - Profiles
      - Tokens
    score: 102
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/link/
    overlays:
      - url: overlays/plaid-link--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-link--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-link--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/link/
        type: Documentation
    description: Plaid Link API is a tool designed to simplify the process of connecting users' financial accounts to third-party applications. By providing a secure and seamless way for users to input their account credentials, Plaid Link API enables developers to access real-time financial data and perform transactions on behalf of their users. This API streamlines the integration of financial services into applications, making it easier for users to manage their finances and for developers to implement financial features without having to build their own infrastructure for data aggregation and security. Overall, Plaid Link API revolutionizes the way financial data is accessed and utilized in the digital age.
  - aid: plaid:plaid-transfer-api
    name: Plaid Transfer API
    tags:
      - (Deprecated)
      - About
      - Accounts
      - Advance
      - Associated
      - Authorization
      - Available
      - Balance
      - Behalf
      - Between
      - Cancels
      - Capabilities
      - Clock
      - Clocks
      - Configurations
      - Converting
      - Creating
      - Creation
      - Deposit
      - Diligence
      - Distribute
      - Documents
      - Eligibility
      - Events
      - Fire
      - Funding
      - Funds
      - Generate
      - Held
      - Historical
      - Included
      - Information
      - Intent
      - Invoke
      - Items
      - Ledgers
      - Manually
      - Metrics
      - Migrate
      - Move
      - Objects
      - Onboarding
      - Originator
      - Originator's
      - Originators
      - Originators'
      - Pending
      - Plaid
      - Plaid Hosted
      - Platforms
      - Products
      - Questionnaires
      - Recurring
      - Refunds
      - Repayment
      - Repayments
      - RTP
      - Sandbox
      - Simulate
      - Status
      - Submit
      - Sweep
      - Sweeps
      - Sync
      - Tests
      - Transfers
      - Triggers
      - UI
      - Uploads
      - URL
      - Usage
      - Webhooks
      - Withdraw
    score: 1358
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/transfer/
    overlays:
      - url: overlays/plaid-transfer--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-transfer--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-transfer--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transfer/
        type: Documentation
    description: Plaid Transfer API is a powerful tool that enables developers to easily integrate ACH (Automated Clearing House) payments into their applications. This API allows users to securely link their bank accounts and initiate transfers with just a few lines of code. With Plaid Transfer API, developers can automate payment processes, streamline financial transactions, and provide a seamless user experience. By leveraging the capabilities of this API, businesses can improve efficiency, reduce manual tasks, and enhance the overall payment experience for their customers.
  - aid: plaid:plaid-bank-transfer-api
    name: Plaid Bank Transfer API
    tags:
      - Accounts
      - Balance
      - Bank
      - Cancels
      - Events
      - Fire
      - Manually
      - Migrate
      - Processor
      - Sandbox
      - Simulate
      - Sweep
      - Sweeps
      - Sync
      - Transfers
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
      - url: openapi/plaid-bank-transfer--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/transfer/
        type: Documentation
    description: Plaid Bank Transfer API is a service that allows developers to securely initiate and manage bank transfers within their applications. By integrating this API, developers can streamline the process of transferring funds between bank accounts, enabling users to easily send and receive money without having to leave the app. The API also provides real-time notifications and updates on transfer status, ensuring a seamless and transparent experience for both the developer and the end-user. Additionally, Plaid Bank Transfer API offers robust security measures to protect sensitive financial information, making it a reliable and trusted solution for facilitating bank transfers.
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
      - url: openapi/plaid-employers--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/income/
        type: Documentation
    description: The Plaid Employers API is a tool that allows businesses to securely access and verify their employees' income and employment information. By integrating with the API, employers can streamline the process of verifying income for various purposes such as loan applications, background checks, and employee onboarding. This API provides a fast and reliable way for businesses to access up-to-date information about their employees' income and employment status, helping them make more informed decisions about their workforce. Additionally, the Plaid Employers API offers advanced security features to protect sensitive employee data and ensure compliance with privacy regulations. Overall, this API facilitates efficient and secure communication between employers and financial institutions, enabling businesses to verify their employees' income and employment information with ease.
  - aid: plaid:plaid-income-api
    name: Plaid Income API
    tags:
      - (Deprecated)
      - Checks
      - Conversions
      - Digital
      - Documents
      - Download
      - Eligibility
      - Fire
      - Income
      - Information
      - Instances
      - Manually
      - Optimize
      - Original
      - Paystubs
      - Precheck
      - Sandbox
      - Taxes
      - Taxforms
      - Used
      - Verification
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
      - url: openapi/plaid-income--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/income/
        type: Documentation
    description: Plaid Income API is a powerful tool that allows developers to access and analyze a user's income information quickly and securely. By integrating this API into their applications, developers can provide users with insights into their income sources, including direct deposits, self-employment earnings, and more. With this information, users can better understand their financial health and make informed decisions about budgeting, saving, and investing. Plaid Income API helps to streamline the process of gathering and analyzing income data, making it easier for users to track their earnings and make strategic financial choices.
  - aid: plaid:plaid-beta-api
    name: Plaid Beta API
    tags:
      - /Transactions/Enrich
      - Access
      - Accounts
      - Associated
      - Bank
      - Based
      - Beta
      - Categories
      - Credit
      - Data
      - Employment
      - Enhance
      - Information
      - Insights
      - Items
      - Locally Held
      - Obtain
      - Rules
      - Sent
      - Tokens
      - Transactions
      - Used
      - Users
      - Verification
    score: 170
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/
    overlays:
      - url: overlays/plaid-beta--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-beta--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-beta--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/
        type: Documentation
    description: Plaid Beta API is a powerful tool that enables developers to access and utilize financial data from various institutions. By integrating with Plaid's API, developers can securely connect to bank accounts, retrieve transaction data, and perform various financial operations. This API allows for seamless integration of banking information into websites, apps, and other digital platforms, providing users with real-time insights into their finances. With Plaid Beta API, developers can create innovative financial tools and services that enhance user experiences and streamline financial processes.
  - aid: plaid:plaid-signal-api
    name: Plaid Signal API
    tags:
      - ACH
      - Decision
      - Evaluate
      - Initiated
      - Items
      - Opt In
      - Planned
      - Prepare
      - Processor
      - Reports
      - Signals
      - Tokens
      - Transactions
      - Whether
    score: 238
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/signal/
    overlays:
      - url: overlays/plaid-signal--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-signal--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-signal--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/signal/
        type: Documentation
    description: The Plaid Signal API is a powerful tool that allows developers to receive real-time notifications and alerts about their users' financial activities. By integrating this API into their applications, developers can stay informed about important events such as large transactions, account balance changes, and potential fraudulent activity. This level of visibility enables developers to provide better and more secure user experiences, ultimately leading to increased trust and satisfaction among their customers. With the Plaid Signal API, developers can take proactive measures to protect their users' financial well-being and ensure that their applications remain secure and reliable.
  - aid: plaid:plaid-wallet-api
    name: Plaid Wallet API
    tags:
      - E Wallet
      - E Wallets
      - Execute
      - Fetch
      - Transactions
      - Using
      - Wallet
    score: 143
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/products/virtual-accounts/
    overlays:
      - url: overlays/plaid-wallet--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-wallet--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-wallet--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/products/virtual-accounts/
        type: Documentation
    description: Plaid Wallet API is a powerful tool that allows developers to easily integrate financial data and transaction capabilities into their apps and websites. With Plaid Wallet API, users can securely connect their bank accounts, view their balances and transactions, and make payments or transfers all within the same platform. This API provides a seamless and user-friendly experience for managing personal finances, allowing users to stay on top of their financial health and make informed decisions. Overall, Plaid Wallet API streamlines the process of accessing and using banking information, making it a valuable resource for both developers and consumers alike.
  - aid: plaid:plaid-paymet-profile-api-delete
    name: Plaid Paymet Profile API - DELETE
    tags: []
    overlays:
      - url: overlays/plaid-paymet-profile--openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/plaid-paymet-profile--openapi-original.yml
        type: OpenAPI
    description: Plaid Payment Profile API - DELETE is a feature that allows users to delete a payment profile from their account. This function can be useful for users who no longer want a particular payment profile linked to their account or for those who want to update their payment information. By using this API, users can easily remove outdated or incorrect payment profiles and ensure that only the most up-to-date and accurate information is stored in their account. This helps to keep their financial transactions secure and organized.
  - aid: plaid:plaid-sandb-ox-api
    name: Plaid Sandb Ox API
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
      - url: openapi/plaid-payment-profile--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/payment-initiation/add-to-app/
        type: Documentation
    description: Plaid Sandbox API is a tool provided by Plaid that allows developers to test and experiment with their applications in a simulated environment. The API provides access to a variety of fake financial data, such as bank account information, transactions, and balances, that can be used to simulate real-world scenarios without affecting actual user accounts. This allows developers to quickly and easily test the functionality of their applications, identify bugs and issues, and make necessary adjustments before deploying their products in a production environment. Overall, the Plaid Sandbox API helps developers streamline the development process and ensure the reliability and security of their applications.
  - aid: plaid:plaid-partner-api
    name: Plaid Partner API
    tags:
      - Creates
      - Customers
      - Enable
      - Enables
      - Environments
      - Given
      - Information
      - Institutions
      - OAuth
      - OAuth Institution
      - Partners
      - Plaid
      - Production
      - Registrations
      - Reseller
      - Reseller's
    score: 155
    baseURL: https://production.plaid.com
    humanURL: https://plaid.com/docs/api/partner/
    overlays:
      - url: overlays/plaid-partner--openapi-search.yml
        type: OpenAPI
      - url: overlays/plaid-partner--openapi-api-evangelist-ratings.yml
        type: API Evangelist Ratings
    properties:
      - url: openapi/plaid-partner--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/api/partner/
        type: Documentation
    description: The Plaid Partner API is a powerful tool that allows developers to seamlessly integrate financial services and applications with their own platforms. By providing a secure and reliable way to connect to banks and financial institutions, the Plaid Partner API enables users to access and manage their financial data in real-time. With features such as account verification, transaction history, and balance reporting, the API streamlines the process of interacting with financial information, making it easier for businesses to create innovative financial products and services for their customers. Overall, the Plaid Partner API helps to democratize access to financial data and empower developers to build cutting-edge financial solutions for consumers.
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
      - url: openapi/plaid-link-delivery--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.com/docs/link/hosted-link/
        type: Documentation
    description: Plaid Link Delivery API is a powerful tool that allows developers to seamlessly integrate Plaid's account linking technology into their applications. This API streamlines the process of connecting users' bank accounts to financial services, making it easy for users to securely and quickly access their financial data. With Plaid Link Delivery API, developers can customize the account linking experience to match their brand and user experience requirements, while maintaining strict security protocols to protect sensitive information. By leveraging this API, developers can provide a user-friendly and efficient way for customers to connect their accounts and access their financial information, ultimately enhancing the overall user experience of their applications.
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
      - url: openapi/plaid-fdx--openapi-original.yml
        type: OpenAPI
      - url: https://plaid.github.io/core-exchange/api-versions/six-dot-zero
        type: Documentation
    description: Plaid FDX API is a powerful tool that allows developers to easily access financial data from a variety of sources, including banks, credit unions, and other financial institutions. This API provides a secure and efficient way to retrieve information such as account balances, transaction history, and user profiles. By using Plaid FDX API, developers can create innovative financial applications that help users better manage their money and make informed decisions about their finances. With its robust set of features and comprehensive data coverage, Plaid FDX API is an essential tool for any developer looking to build cutting-edge financial technology solutions.
name: Plaid
tags:
  - Bank Accounts
  - Financial
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
  - type: Features
    data:
      - Auth API for ACH account/routing verification (~$1.50/linked account)
      - Identity API for KYC name/address/phone match (~$0.30/call)
      - Income API for income verification
      - Transactions API with /sync cursor for incremental pulls (~$0.45/call)
      - Balance API for real-time balance check (~$0.10/call)
      - Investments, Liabilities, Assets, Statements products
      - Plaid Link prebuilt UI for OAuth bank connection
      - 12,000+ supported financial institutions
      - Sandbox environment with synthetic data
      - Default 100 req/day/Item rate limit
      - Webhooks for transaction updates and item events
      - Pay-as-you-go default; Growth tier with discounts and SSO
      - Custom contracts $1k-$10k+/month with 30-50% volume discounts at scale
      - Plaid Beacon for fraud network signals
      - Plaid Transfer for ACH payment initiation
      - Plaid Signal for ACH risk scoring
    sources:
      - https://plaid.com/pricing/
    updated: '2026-05-04'
created: '2024-07-07T00:00:00.000Z'
modified: '2026-05-04'
description: Plaid is a financial technology company that provides an API platform for businesses to connect with user's financial accounts and facilitate transactions. Plaid's technology enables applications to securely access and authenticate user banking information, allowing them to offer services such as bank account verification, payment initiation, and personal finance management. By acting as the interface between financial institutions and third-party platforms, Plaid streamlines the process of integrating financial data into software applications, enabling businesses to create innovative and user-friendly financial products.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.16'
type: Contract
position: Consuming
access: 3rd-Party
---
