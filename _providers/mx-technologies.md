---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 96
  human_in_the_loop: 0
  name: Mx Technologies Agentic Access
  operation_count: 221
  slug: mx-technologies-agentic-access
  summary_line: 221 operations · 96 acting
api_count: 2
apis:
- description: The legacy MX financial data connectivity API supporting over 48,000 data connections to thousands of financial institutions. Provides secure access to user accounts and transactions with industry-lea
  name: MX Atrium API
  slug: mx-atrium-api
- description: A RESTful authentication API used to authenticate users on the MX Platform and generate widget URLs for Personal Finance Management and Financial Insights widgets. Supports both XML and JSON encoding.
  name: MX SSO API
  slug: mx-sso-api
- description: An open finance API built to FDX standards enabling permissioned data sharing with consumer consent management. Supports Account Owner Identity, statements, transaction history, account verifications,
  name: MX Data Access API
  slug: mx-data-access-api
- description: Enables processing of bulk operations and batch requests on the MX platform, supporting large-scale data operations for financial institutions and fintech partners.
  name: MX Batch API
  slug: mx-batch-api
- description: Supports reporting functionality and analytics for financial institutions and fintech partners integrating with the MX platform.
  name: MX Reporting API
  slug: mx-reporting-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The accounts API from MX Technologies — 13 operation(s) for accounts.
  name: MX Technologies Accounts API
  phrasing_intents:
  - id: listUserAccounts
    intent: List a user's accounts by MX GUID
    question: Which bank and card accounts does a user have, looked up by their MX user GUID?
  - id: createManualAccount
    intent: Create a manual account by user GUID
    question: How do I add a hand-tracked account, like a cash envelope, for a user by their MX GUID?
  - id: readAccount
    intent: Read an account by user and account GUID
    question: How do I get the balance and details of one account directly under a user?
  - id: deleteManualAccount
    intent: Delete a manually created account
    question: How do I remove an account the user created by hand?
  - id: listAccountNumbersByAccount
    intent: Get full account numbers for an account by GUID
    question: How do I get the full account and routing numbers for one account using its MX GUID?
  - id: listAccountNumbersByMember
    intent: List account numbers across a member
    question: Can I get the account and routing numbers for every account in one bank connection at once?
  - id: listAccountOwnersByMember
    intent: List account owners for a member by GUID
    question: Who owns the accounts in a bank connection, looked up with MX GUIDs?
  - id: listMemberAccounts
    intent: List a member's accounts by GUID
    question: Which accounts came from one specific bank connection, using MX GUIDs?
  phrasing_ops: 18
  slug: mx-technologies-accounts-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The ach return API from MX Technologies — 2 operation(s) for ach return.
  name: MX Technologies ach return API
  phrasing_intents:
  - id: readACHRetrun
    intent: Read an ACH return
    question: How do I check the details of a single ACH return I reported?
  - id: listACHRetruns
    intent: List ACH returns
    question: Which ACH payments have bounced back, and with what return codes?
  - id: createACHReturn
    intent: Report an ACH return
    question: How do I tell MX that an ACH debit was returned, for example for insufficient funds?
  phrasing_ops: 3
  slug: mx-technologies-ach-return-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The budgets API from MX Technologies — 3 operation(s) for budgets.
  name: MX Technologies Budgets API
  phrasing_intents:
  - id: autoGenerateBudgets
    intent: Auto-generate budgets from spending history
    question: Can MX suggest budgets automatically based on what a user has been spending?
  - id: createBudget
    intent: Create a budget for a category
    question: How do I set a monthly spending limit for a category like Gas?
  - id: listAllBudgets
    intent: List a user's budgets
    question: What budgets has a user set up?
  - id: readSpecificBudget
    intent: Read one budget
    question: How much has a user budgeted for one specific budget?
  - id: updateSpecificBudget
    intent: Change an existing budget
    question: How do I raise a user's grocery budget?
  - id: deleteBudget
    intent: Delete a budget
    question: How do I remove a budget a user no longer wants?
  phrasing_ops: 6
  slug: mx-technologies-budgets-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The categories API from MX Technologies — 5 operation(s) for categories.
  name: MX Technologies Categories API
  phrasing_intents:
  - id: listDefaultCategories
    intent: List the standard spending categories
    question: What built-in transaction categories and subcategories does MX offer?
  - id: readDefaultCategory
    intent: Read one default category
    question: How do I look up the name and parent of a built-in category by its GUID?
  - id: listCategories
    intent: List a user's default and custom categories
    question: Which categories can a user assign, including the custom ones they made?
  - id: createCategory
    intent: Create a custom category for a user
    question: Can a user add their own spending category, like Pet Supplies?
  - id: listDefaultCategoriesByUser
    intent: List default categories scoped to a user
    question: How do I fetch only the standard categories, excluding custom ones, for a particular user?
  - id: deleteCategory
    intent: Delete a custom category
    question: How do I remove a custom category a user no longer needs?
  - id: readCategory
    intent: Read a user's category, custom or default
    question: How do I read a custom category a user created?
  - id: updateCategory
    intent: Rename or edit a custom category
    question: How do I rename a custom category a user created?
  phrasing_ops: 8
  slug: mx-technologies-categories-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The goals API from MX Technologies — 3 operation(s) for goals.
  name: MX Technologies Goals API
  phrasing_intents:
  - id: createGoal
    intent: Create a financial goal
    question: How do I set up a savings goal for a user?
  - id: listGoals
    intent: List a user's savings and debt goals
    question: What financial goals has a user set up?
  - id: deleteGoal
    intent: Delete a goal
    question: How do I remove a goal a user no longer wants?
  - id: readGoal
    intent: Read one goal
    question: What's the target amount and progress on a specific goal?
  - id: updateGoal
    intent: Update a goal
    question: Can I change the target amount or name of an existing goal?
  - id: repositionGoals
    intent: Reorder a user's goal priorities
    question: How do I change which goal is the user's top priority?
  phrasing_ops: 6
  slug: mx-technologies-goals-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The insights API from MX Technologies — 9 operation(s) for insights.
  name: MX Technologies Insights API
  phrasing_intents:
  - id: listInsightsByAccount
    intent: List insights for one account
    question: What financial insights has MX generated about a specific account?
  - id: listInsightsUser
    intent: List all insights for a user
    question: What money insights does a user have across all their accounts?
  - id: listCategoriesInsight
    intent: List the categories behind an insight
    question: Which spending categories is a particular insight about?
  - id: listAccountsInsight
    intent: List the accounts behind an insight
    question: Which of a user's accounts does a given insight refer to?
  - id: listMerchantsInsight
    intent: List the merchants behind an insight
    question: Which merchants is a spending insight talking about?
  - id: listScheduledPaymentsInsight
    intent: List scheduled payments behind an insight
    question: Which upcoming bills or recurring payments does an insight refer to?
  - id: listTransactionsInsight
    intent: List transactions behind an insight
    question: Which transactions caused a particular insight to be generated?
  - id: readInsightUser
    intent: Read a single insight
    question: What does one specific insight say, and when was it created?
  phrasing_ops: 10
  slug: mx-technologies-insights-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The institutions API from MX Technologies — 5 operation(s) for institutions.
  name: MX Technologies Institutions API
  phrasing_intents:
  - id: listInstitutions
    intent: Search institutions by name or capability
    question: Which banks can I connect to, and can I search them by name?
  - id: listFavoriteInstitutions
    intent: List my favorite institutions
    question: Which institutions have been set as our favorites, sorted by popularity?
  - id: readInstitution
    intent: Read one institution by code
    question: What details does MX have on a specific institution code?
  - id: listInstitutionCredentials
    intent: List login fields for an institution code
    question: What login fields does a user need to fill in to connect to a given institution code?
  - id: getInstitutionsByInstitutionIdentifierCredentials
    intent: List institution login fields (versioned)
    question: On the versioned API, which credentials do I collect before connecting to an institution identifier?
  phrasing_ops: 5
  slug: mx-technologies-institutions-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The investment holdings API from MX Technologies — 5 operation(s) for investment holdings.
  name: MX Technologies investment holdings API
  phrasing_intents:
  - id: listHoldingsByMember
    intent: List investment holdings for one member
    question: What stocks and funds are held across the accounts of one connected institution?
  - id: listHoldings
    intent: List all investment holdings for a user
    question: What investments does a user hold across every account?
  - id: readHolding
    intent: Read one investment holding
    question: What are the details of one specific holding, like shares and market value?
  - id: listHoldingsByAccount
    intent: List holdings in one investment account
    question: What's held inside a particular brokerage or retirement account?
  - id: deactivateUser
    intent: Turn off Investment Holdings for a user
    question: How do I stop a user from being enrolled in the investment holdings product?
  phrasing_ops: 5
  slug: mx-technologies-investment-holdings-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The managed data API from MX Technologies — 7 operation(s) for managed data.
  name: MX Technologies managed data API
  phrasing_intents:
  - id: listManagedInstitutions
    intent: List institutions available for managed data
    question: Which institutions can I use when loading my own account data into MX as partner-managed members?
  - id: listManagedMembers
    intent: List a user's partner-managed members
    question: What partner-managed members have I created for a given user?
  - id: createManagedMember
    intent: Create a partner-managed member
    question: How do I set up a member whose account data I push in myself instead of aggregating?
  - id: deleteManagedMember
    intent: Delete a partner-managed member
    question: How do I remove a member whose data I was supplying myself?
  - id: readManagedMember
    intent: Get one partner-managed member
    question: Can I look up the attributes of a single partner-managed member?
  - id: updateManagedMember
    intent: Update a partner-managed member
    question: How do I rename or change metadata on a partner-managed member?
  - id: listManagedAccounts
    intent: List accounts under a partner-managed member
    question: What accounts have I loaded under a partner-managed member?
  - id: createManagedAccount
    intent: Add an account to a partner-managed member
    question: How do I push a new checking or savings account into a partner-managed member?
  phrasing_ops: 16
  slug: mx-technologies-managed-data-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The managed data [deprecated] API from MX Technologies — 7 operation(s) for managed data [deprecated].
  name: MX Technologies managed data [deprecated] API
  phrasing_intents:
  - id: listManagedInstitutions
    intent: List managed-data institutions (deprecated)
    question: Which institutions does the deprecated managed-data API still list for partner-supplied members?
  - id: listManagedMembers
    intent: List a user's managed members (deprecated)
    question: Where do I list partner-managed members on the deprecated versioned API?
  - id: createManagedMember
    intent: Create a managed member (deprecated)
    question: Can I still create a partner-managed member through the deprecated versioned endpoint?
  - id: deleteManagedMember
    intent: Delete a managed member (deprecated)
    question: How do I delete a partner-managed member on the deprecated managed-data API?
  - id: readManagedMember
    intent: Read a managed member (deprecated)
    question: How do I read a partner-managed member using the deprecated managed-data API?
  - id: updateManagedMember
    intent: Update a managed member (deprecated)
    question: Can I edit a partner-managed member through the deprecated versioned endpoint?
  - id: listManagedAccounts
    intent: List a managed member's accounts (deprecated)
    question: Where are a partner-managed member's accounts listed on the deprecated versioned API?
  - id: createManagedAccount
    intent: Create a managed account (deprecated)
    question: Can I still add an account to a partner-managed member through the deprecated endpoint?
  phrasing_ops: 16
  slug: mx-technologies-managed-data-deprecated-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The members API from MX Technologies — 20 operation(s) for members.
  name: MX Technologies Members API
  phrasing_intents:
  - id: listMembers
    intent: List a user's connected members by MX GUID
    question: Which financial institution connections does a user have, looked up by their MX user GUID?
  - id: createMember
    intent: Connect a user to an institution by GUID
    question: How do I connect a user's bank login to MX when I only have their MX user GUID?
  - id: deleteMember
    intent: Permanently delete a member by GUID
    question: How do I disconnect and remove a user's bank connection when I only have MX GUIDs?
  - id: readMember
    intent: Look up one member by its MX GUID
    question: What are the details of a specific member when I have both the user and member GUIDs?
  - id: updateMember
    intent: Update a member's credentials by GUID
    question: How do I change the saved login credentials on an existing member using its GUID?
  - id: aggregateMember
    intent: Refresh a member's accounts and transactions by GUID
    question: How do I pull the latest accounts and transactions for a member using its GUID?
  - id: listMemberChallenges
    intent: List MFA challenges for a member by GUID
    question: What multi-factor questions does a member GUID need answered before aggregation can continue?
  - id: checkBalances
    intent: Refresh only balances for a member by GUID
    question: Can I update just account balances for a member GUID without pulling transactions?
  phrasing_ops: 26
  slug: mx-technologies-members-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The merchants API from MX Technologies — 3 operation(s) for merchants.
  name: MX Technologies Merchants API
  phrasing_intents:
  - id: readMerchantLocation
    intent: Read a merchant location
    question: Where exactly did a transaction happen, using its merchant location?
  - id: listMerchants
    intent: List or search merchants
    question: Which merchants are in the MX system, and can I search by name?
  - id: readMerchant
    intent: Read a merchant's logo, name and website
    question: What's the logo and website for a merchant on a transaction?
  phrasing_ops: 3
  slug: mx-technologies-merchants-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The microdeposits API from MX Technologies — 4 operation(s) for microdeposits.
  name: MX Technologies Microdeposits API
  phrasing_intents:
  - id: listUserMicrodeposits
    intent: List a user's microdeposits
    question: Which microdeposit verifications has a user started?
  - id: createMicrodeposit
    intent: Start or pre-initiate a microdeposit
    question: How do I verify a bank account with small test deposits when instant verification isn't available?
  - id: deleteMicrodeposit
    intent: Delete a microdeposit
    question: How do I cancel and remove a microdeposit verification I no longer need?
  - id: readUserMicrodeposit
    intent: Check the status of a microdeposit
    question: Has a user's microdeposit been verified yet?
  - id: verifyMicrodeposit
    intent: Submit the microdeposit amounts to verify
    question: How does a user confirm the two small amounts that landed in their account?
  - id: listUserVerifications
    intent: List a user's account verifications
    question: Which of a user's accounts have been verified, and what state is each verification in?
  phrasing_ops: 6
  slug: mx-technologies-microdeposits-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The monthly cash flow profile API from MX Technologies — 2 operation(s) for monthly cash flow profile.
  name: MX Technologies monthly cash flow profile API
  phrasing_intents:
  - id: readMonthlyCashFlowProfile
    intent: Read a user's monthly cash flow by MX GUID
    question: How much money typically comes in and goes out for a user each month, looked up by MX GUID?
  - id: updateMonthlyCashFlowProfile
    intent: Update monthly cash flow by MX GUID
    question: How do I adjust a user's monthly cash flow settings using their MX GUID?
  - id: getUsersByUserIdentifierMonthlyCashFlowProfile
    intent: Read monthly cash flow on the versioned API
    question: What does a user's monthly cash flow look like when I reference them by my own user ID?
  - id: putUsersByUserIdentifierMonthlyCashFlowProfile
    intent: Update monthly cash flow on the versioned API
    question: How do I update a user's cash flow profile using the ID I defined for them?
  phrasing_ops: 4
  slug: mx-technologies-monthly-cash-flow-profile-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The notifications API from MX Technologies — 2 operation(s) for notifications.
  name: MX Technologies Notifications API
  phrasing_intents:
  - id: createNotification
    intent: Send a push notification to a user
    question: How do I send a push message to a user in the mobile banking app?
  - id: listNotifications
    intent: List a user's notifications
    question: What notifications has a user been sent, including ones on channels other than push?
  - id: readNotifications
    intent: Read one notification
    question: What did a specific notification to a user say?
  phrasing_ops: 3
  slug: mx-technologies-notifications-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The processor token API from MX Technologies — 7 operation(s) for processor token.
  name: MX Technologies processor token API
  phrasing_intents:
  - id: requestAuthorizationCode
    intent: Request an authorization code for a processor
    question: How do I give a payment processor scoped access to a user's account data?
  - id: deprecatedRequestPaymentProcessorAuthorizationCode
    intent: Request a payment processor code (legacy)
    question: Is there an older endpoint that issues a payment processor authorization code by user, member and account?
  - id: listTokens
    intent: List processor tokens for a user, member or account
    question: Which processor tokens currently exist for a user or account?
  - id: requestAccountNumber
    intent: Get account and routing numbers (processor)
    question: As a processor, how do I get the routing and account number my access token is scoped to?
  - id: checkRealTimeAccountBalance
    intent: Check a real-time balance (processor)
    question: Can a processor get a live, real-time balance from the institution instead of a cached one?
  - id: readAccountBalance
    intent: Read the stored account balance (processor)
    question: As a processor, can I read the payment account's balance without a live refresh?
  - id: getAccountOwnerInfo
    intent: Get account owner information (processor)
    question: How does a processor find out who owns the authorized account?
  phrasing_ops: 7
  slug: mx-technologies-processor-token-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The rewards API from MX Technologies — 5 operation(s) for rewards.
  name: MX Technologies Rewards API
  phrasing_intents:
  - id: fetchRewards
    intent: Refresh a member's rewards data by GUID
    question: How do I trigger a fresh pull of loyalty points and rewards for a bank connection using MX GUIDs?
  - id: listRewards
    intent: List a member's rewards balances
    question: What points, miles or cash-back balances does a user have with a connected card?
  - id: readRewards
    intent: Read one reward for a member
    question: How do I look up the details of a single rewards balance?
  - id: creditCard
    intent: Look up a credit card product
    question: What are the details of a specific credit card product, like its rewards program?
  - id: postUsersByUserIdentifierMembersByMemberIdentifierFetchRewards
    intent: Refresh a member's rewards on the versioned API
    question: How do I trigger a rewards refresh for a connection identified by my own user and member IDs?
  phrasing_ops: 5
  slug: mx-technologies-rewards-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The spending plan API from MX Technologies — 9 operation(s) for spending plan.
  name: MX Technologies spending plan API
  phrasing_intents:
  - id: createSpendingPlanIterationItem
    intent: Add a planned item to a spending plan
    question: How do I add a planned amount for a category, like groceries, to a user's spending plan?
  - id: listSpendingPlanIterationItems
    intent: List line items in a spending plan
    question: What planned expenses and income items are in a user's current spending plan period?
  - id: createSpendingPlan
    intent: Create a spending plan for a user
    question: How do I start a new spending plan for someone?
  - id: listSpendingPlans
    intent: List a user's spending plans
    question: Does this user already have a spending plan set up?
  - id: deleteSpendingPlanAccount
    intent: Remove an account from a spending plan
    question: How do I drop an account out of a user's spending plan?
  - id: readSpendingPlanAccount
    intent: Read an account attached to a spending plan
    question: How do I see the details of one account included in a user's spending plan?
  - id: deleteSpendingPlanIterationItem
    intent: Delete a line item from a spending plan
    question: How do I take a planned expense out of a user's spending plan?
  - id: readSpendingPlanIterationItem
    intent: Read one spending plan line item
    question: How much was planned for a single line item in a spending plan?
  phrasing_ops: 15
  slug: mx-technologies-spending-plan-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The statements API from MX Technologies — 5 operation(s) for statements.
  name: MX Technologies Statements API
  phrasing_intents:
  - id: fetchStatements
    intent: Fetch new statements for a member by GUID
    question: How do I pull the latest account statements from a user's bank using MX GUIDs?
  - id: listStatementsByMember
    intent: List a member's available statements
    question: Which statements have already been retrieved for a member?
  - id: readStatementByMember
    intent: Read a statement's details as JSON
    question: Can I get the metadata of one statement as JSON rather than the PDF?
  - id: downloadStatementPDF
    intent: Download a statement PDF
    question: How do I download the actual PDF of a bank statement?
  - id: postUsersByUserIdentifierMembersByMemberIdentifierFetchStatements
    intent: Fetch statements for a member (versioned)
    question: On the versioned API, can I fetch statements for a member I reference by my own ID?
  phrasing_ops: 5
  slug: mx-technologies-statements-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The taggings API from MX Technologies — 2 operation(s) for taggings.
  name: MX Technologies Taggings API
  phrasing_intents:
  - id: listTaggings
    intent: List a user's tag-to-transaction links
    question: Which transactions has a user attached tags to?
  - id: createTagging
    intent: Attach a tag to a transaction
    question: How do I label a transaction with a tag like Business Trip?
  - id: deleteTagging
    intent: Remove a tag from a transaction
    question: How do I untag a transaction?
  - id: readTagging
    intent: Read one tagging
    question: Which tag and transaction does a particular tagging connect?
  - id: updateTagging
    intent: Change which tag a tagging uses
    question: How do I move a transaction's tag assignment to a different tag?
  phrasing_ops: 5
  slug: mx-technologies-taggings-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The tags API from MX Technologies — 2 operation(s) for tags.
  name: MX Technologies Tags API
  phrasing_intents:
  - id: listTags
    intent: List a user's transaction tags
    question: Which custom tags has a user created for labeling transactions?
  - id: createTag
    intent: Create a custom tag
    question: How do I add a custom tag like Vacation for a user?
  - id: deleteTag
    intent: Delete a tag
    question: How do I permanently remove a tag a user no longer uses?
  - id: readTag
    intent: Read one tag
    question: What are the attributes of a specific tag?
  - id: updateTag
    intent: Rename a tag
    question: How do I rename an existing tag?
  phrasing_ops: 5
  slug: mx-technologies-tags-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The transaction rules API from MX Technologies — 2 operation(s) for transaction rules.
  name: MX Technologies transaction rules API
  phrasing_intents:
  - id: listTransactionRules
    intent: List a user's transaction rules
    question: Which auto-categorization rules has a user set up?
  - id: createTransactionRule
    intent: Create a transaction categorization rule
    question: How do I make every transaction from a certain merchant land in the same category automatically?
  - id: readTransactionRule
    intent: Read one transaction rule
    question: What does a specific transaction rule match on and which category does it apply?
  - id: updateTransactionRule
    intent: Edit a transaction rule
    question: How do I change the category an existing transaction rule assigns?
  phrasing_ops: 4
  slug: mx-technologies-transaction-rules-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The transactions API from MX Technologies — 19 operation(s) for transactions.
  name: MX Technologies Transactions API
  phrasing_intents:
  - id: enhanceTransactions
    intent: Categorize and cleanse raw transactions
    question: Can I get messy bank transaction descriptions cleaned up and categorized without storing them?
  - id: createManualTransaction
    intent: Add a transaction to a manual account
    question: How do I record a cash purchase against an account the user created by hand?
  - id: listTransactionsByAccount
    intent: List transactions for one account by GUID
    question: What transactions have posted to one specific account, looked up by its MX account GUID?
  - id: updateTransactionByAccount
    intent: Update a transaction under its member account by GUID
    question: How do I edit a transaction when I address it through its member and account GUIDs?
  - id: extendHistory
    intent: Request 24 months of history for a member by GUID
    question: How do I pull up to two years of transaction history for a bank connection using its MX GUIDs?
  - id: listTransactionsByMember
    intent: List a member's transactions by GUID
    question: What transactions came in across every account of one bank connection, using MX GUIDs?
  - id: listTransactionsByTag
    intent: List transactions carrying a tag by user GUID
    question: Which transactions has a user labelled with a given tag, looked up by MX user GUID?
  - id: deleteTransactionRule
    intent: Delete a transaction rule
    question: How do I permanently remove an auto-categorization rule a user no longer wants?
  phrasing_ops: 25
  slug: mx-technologies-transactions-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The users API from MX Technologies — 3 operation(s) for users.
  name: MX Technologies Users API
  phrasing_intents:
  - id: listUsers
    intent: List the users you have created
    question: Which end users have I created on the MX platform?
  - id: createUser
    intent: Create a new end user
    question: How do I register a new end user before connecting their bank?
  - id: deleteUser
    intent: Permanently delete a user by MX GUID
    question: How do I permanently remove a user and their data using the MX user GUID?
  - id: readUser
    intent: Read a user by MX GUID
    question: How do I look up a user's attributes when I have their MX-assigned GUID?
  - id: updateUser
    intent: Update a user by MX GUID
    question: How do I change a user's email or metadata using their MX GUID?
  - id: deleteUsersByUserIdentifier
    intent: Delete a user on the versioned API
    question: How do I permanently delete a user I identify with my own ID?
  - id: getUsersByUserIdentifier
    intent: Read a user on the versioned API
    question: How do I read a user by the ID I assigned them in my own system?
  - id: putUsersByUserIdentifier
    intent: Update a user on the versioned API
    question: How do I update a user referenced by my own user ID?
  phrasing_ops: 8
  slug: mx-technologies-users-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The verifiable credentials API from MX Technologies — 3 operation(s) for verifiable credentials.
  name: MX Technologies verifiable credentials API
  phrasing_intents:
  - id: getIdentityData
    intent: Get a verifiable credential of identity data
    question: How do I get a signed verifiable credential proving a user's identity data?
  - id: getAccountsData
    intent: Get a verifiable credential of accounts data
    question: Can I get a verifiable credential listing a user's accounts at one institution?
  - id: getTransactionsData
    intent: Get a verifiable credential of transactions
    question: Can I get a verifiable credential of one account's transactions?
  phrasing_ops: 3
  slug: mx-technologies-verifiable-credentials-api
- baseURL: https://api.mx.com
  baseurl_source: declared
  description: The widgets API from MX Technologies — 4 operation(s) for widgets.
  name: MX Technologies Widgets API
  phrasing_intents:
  - id: requestConnectWidgetURL
    intent: Get a Connect widget URL (deprecated)
    question: Is there an older endpoint that returns just an embeddable MX Connect URL?
  - id: requestOAuthWindowURI
    intent: Get an OAuth window URI for a member by GUID
    question: How do I get the OAuth login link for a member I know by its MX GUID?
  - id: requestWidgetURL
    intent: Get an embeddable widget URL
    question: How do I embed the Connect, spending or insights widget in my app?
  - id: getUsersByUserIdentifierMembersByMemberIdentifierOauthWindowUri
    intent: Get an OAuth window URI (versioned)
    question: On the versioned API, how do I get an OAuth link for a member referenced by my own ID?
  phrasing_ops: 4
  slug: mx-technologies-widgets-api
artifact_total: 71
asyncapis:
- description: ''
  name: Mx Technologies Webhooks
  slug: mx-technologies-webhooks
collections:
- collection_type: open
  name: MX Platform accounts API
  slug: open-mx-technologies-accounts-api
- collection_type: open
  name: MX Platform accounts ach return API
  slug: open-mx-technologies-ach-return-api
- collection_type: open
  name: MX Platform accounts budgets API
  slug: open-mx-technologies-budgets-api
- collection_type: open
  name: MX Platform accounts categories API
  slug: open-mx-technologies-categories-api
- collection_type: open
  name: MX Platform accounts goals API
  slug: open-mx-technologies-goals-api
- collection_type: open
  name: MX Platform accounts insights API
  slug: open-mx-technologies-insights-api
- collection_type: open
  name: MX Platform accounts institutions API
  slug: open-mx-technologies-institutions-api
- collection_type: open
  name: MX Platform accounts investment holdings API
  slug: open-mx-technologies-investment-holdings-api
- collection_type: open
  name: MX Platform accounts managed data API
  slug: open-mx-technologies-managed-data-api
- collection_type: open
  name: MX Platform accounts managed data [deprecated] API
  slug: open-mx-technologies-managed-data-deprecated-api
- collection_type: open
  name: MX Platform accounts members API
  slug: open-mx-technologies-members-api
- collection_type: open
  name: MX Platform accounts merchants API
  slug: open-mx-technologies-merchants-api
- collection_type: open
  name: MX Platform accounts microdeposits API
  slug: open-mx-technologies-microdeposits-api
- collection_type: open
  name: MX Platform accounts monthly cash flow profile API
  slug: open-mx-technologies-monthly-cash-flow-profile-api
- collection_type: open
  name: MX Platform accounts notifications API
  slug: open-mx-technologies-notifications-api
- collection_type: open
  name: MX Platform accounts processor token API
  slug: open-mx-technologies-processor-token-api
- collection_type: open
  name: MX Platform accounts rewards API
  slug: open-mx-technologies-rewards-api
- collection_type: open
  name: MX Platform accounts spending plan API
  slug: open-mx-technologies-spending-plan-api
- collection_type: open
  name: MX Platform accounts statements API
  slug: open-mx-technologies-statements-api
- collection_type: open
  name: MX Platform accounts taggings API
  slug: open-mx-technologies-taggings-api
- collection_type: open
  name: MX Platform accounts tags API
  slug: open-mx-technologies-tags-api
- collection_type: open
  name: MX Platform accounts transaction rules API
  slug: open-mx-technologies-transaction-rules-api
- collection_type: open
  name: MX Platform accounts transactions API
  slug: open-mx-technologies-transactions-api
- collection_type: open
  name: MX Platform accounts users API
  slug: open-mx-technologies-users-api
- collection_type: open
  name: MX Platform accounts verifiable credentials API
  slug: open-mx-technologies-verifiable-credentials-api
- collection_type: open
  name: MX Platform accounts widgets API
  slug: open-mx-technologies-widgets-api
common:
- group: other
  href: https://artifacts.apis.io/mx-technologies/capabilities/mx-technologies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mx-technologies-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/rules/mx-technologies-rules.yml
  title: ''
  type: Spectral
  url: rules/mx-technologies-rules.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/rules/mx-technologies-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/mx-technologies-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/json-ld/mx-technologies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mx-technologies-context.jsonld
- group: other
  href: https://artifacts.apis.io/mx-technologies/a2a/mx-technologies-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mx-technologies-a2a.yml
- group: other
  href: https://artifacts.apis.io/mx-technologies/hosts/mx-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mx-technologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/mx-technologies/vendors/mx-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mx-technologies-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.mx.com/news/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mx.com/api-reference/platform-api/v20260929/overview/introduction
- group: agent
  href: https://artifacts.apis.io/mx-technologies/mcp/mx-technologies-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mx-technologies-mcp.yml
- group: other
  href: https://artifacts.apis.io/mx-technologies/overlays/mx-technologies-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mx-technologies-platform-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mx/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mx.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mx.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://support.mx.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mx.com/api-reference/platform-api/overview/versioning
- group: auth
  title: ''
  type: Security
  url: https://mx.com/security-policy/
- group: auth
  href: https://artifacts.apis.io/mx-technologies/well-known/mx-technologies-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mx-technologies-security.txt
- group: agent
  href: https://artifacts.apis.io/mx-technologies/well-known/mx-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mx-technologies-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mx.com/trust/
- group: build
  href: https://artifacts.apis.io/mx-technologies/packages/mx-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/mx-technologies-packages.yml
- group: build
  href: https://artifacts.apis.io/mx-technologies/packages/mx-technologies-packages.yml
  title: ''
  type: SDKs
  url: packages/mx-technologies-packages.yml
- group: agent
  href: https://artifacts.apis.io/mx-technologies/llms/mx-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mx-technologies-llms.txt
- group: design
  href: https://artifacts.apis.io/mx-technologies/conventions/mx-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mx-technologies-conventions.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/errors/mx-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mx-technologies-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/lifecycle/mx-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mx-technologies-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mx-technologies/changelog/mx-technologies-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mx-technologies-changelog.yml
- group: start
  href: https://artifacts.apis.io/mx-technologies/sandbox/mx-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mx-technologies-sandbox.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/components/mx-technologies-components.yml
  title: ''
  type: Components
  url: components/mx-technologies-components.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/data-model/mx-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mx-technologies-data-model.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/conformance/mx-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mx-technologies-conformance.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/asyncapi/mx-technologies-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mx-technologies-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mx-technologies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mx.com/sign_up
- group: agent
  href: https://artifacts.apis.io/mx-technologies/agentic-access/mx-technologies-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mx-technologies-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mx-technologies/security/mx-technologies-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mx-technologies-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mx-technologies/security/mx-technologies-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mx-technologies-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mx-technologies/security/mx-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mx-technologies-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mx-technologies/authentication/mx-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mx-technologies-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mxenabled
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/mxenabled/openapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mxenabled
- group: other
  title: ''
  type: X
  url: https://x.com/mX
- group: company
  title: ''
  type: Blog
  url: https://www.mx.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mx.com/company/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mx.com
- group: commercial
  href: https://artifacts.apis.io/mx-technologies/plans/mx-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mx-technologies-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mx-technologies/rate-limits/mx-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mx-technologies-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mx-technologies/finops/mx-technologies-finops.yml
  title: ''
  type: FinOps
  url: finops/mx-technologies-finops.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/vocabulary/mx-technologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mx-technologies-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mx-technologies/json-ld/mx-technologies-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/mx-technologies-context.jsonld
created: '2026-06-12'
description: MX Technologies is a financial data connectivity platform that provides REST APIs for account aggregation, data cleansing, transaction categorization, and open banking connectivity across more than 16,000 financial institutions. The platform powers money experiences for over 2,000 banks, credit unions, and fintechs by turning raw, unstructured financial data into actionable intelligence. MX offers a suite of APIs including the Platform API for core aggregation and data services, the Atrium legacy API, SSO and authentication APIs, and a Data Access API built to FDX standards for permissioned open banking data sharing. Developers have access to OpenAPI specifications, SDKs in Node.js, Python, Java, Ruby, and Go, plus a hosted Connect Widget for rapid integration.
examples:
- key_count: 5
  name: Mx Technologies Platform Api Examples
  slug: mx-technologies-platform-api-examples
finops:
- has_sources: false
  method: generated
  name: Mx Technologies Finops
  primary_unit: ''
  service_category: ''
  slug: mx-technologies-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mx-technologies.png
json_schemas:
- name: MX Platform API Schemas
  property_count: 0
  slug: mx-technologies-platform-api
jsonld:
- class_count: 9
  name: Mx Technologies Context
  property_count: 20
  slug: mx-technologies-context
layout: provider
modified: '2026-06-12'
name: MX Technologies
nav: Providers
network: true
overview: 'MX Technologies publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, ach return API, Budgets API, and 28 more. Tagged areas include Financial Data, Account Aggregation, Open Banking, Data Connectivity, and Fintech.


  The MX Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  MX Technologies'' developer surface includes API reference, support, changelog, sandbox, signup flow, authentication, documentation, and 47 more developer resources.'
plans:
- name: Mx Technologies Plans Pricing
  plan_count: 2
  slug: mx-technologies-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 8
  name: Mx Technologies Rate Limits
  slug: mx-technologies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: MX Technologies — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: mx-technologies-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: MX Technologies API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: mx-technologies-rules
score:
  band: strong
  composite: 65.0
  coverage:
    artifact_dirs: 38
    catalog_earned: 64.2
    catalog_earned_first_party: 0.0
    catalog_gap: 50.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 76.3
    developer_ergonomics: 49.4
    discoverability: 74.1
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 65.4
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mx-technologies/mx-technologies-2026-06-20T185910.png
security:
- kind: authentication
  name: Mx Technologies Authentication
  slug: mx-technologies-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mx Technologies Domain Security
  slug: mx-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mx Technologies Vulnerability Disclosure
  slug: mx-technologies-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mx Technologies Trust Center
  slug: mx-technologies-trust-center
  summary_line: SOC 2, PCI DSS
slug: mx-technologies
tags:
- Financial Data
- Account Aggregation
- Open Banking
- Data Connectivity
- Fintech
- Transaction Categorization
- Data Enhancement
- FDX
- Account Verification
- Personal Finance
- Data Aggregation
website: https://www.mx.com/
---
