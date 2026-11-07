---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 196
  human_in_the_loop: 5
  name: Merge Agentic Access
  operation_count: 621
  slug: merge-agentic-access
  summary_line: 621 operations · 196 acting · 5 human-in-the-loop
api_count: 10
apis:
- description: 'Merge is the connective infrastructure for production AI. Three product lines: Merge Unified (one API for HRIS, ATS, Accounting, CRM, Ticketing, File Storage, Knowledge Base, Chat), Merge Agent Handle'
  name: Merge
  slug: merge
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_accessKeys API from Merge — 4 operation(s) for subpackage_accesskeys.
  name: Merge Subpackage Access Keys API
  phrasing_intents:
  - id: list
    intent: List active access keys
    question: Which Agent Handler access keys are currently active for my organization?
  - id: create
    intent: Create a scoped access key
    question: Can I create an access key limited to certain tool packs and registered users?
  - id: retrieve
    intent: Get an access key
    question: What scopes and expiration does a specific access key have?
  - id: regenerate
    intent: Rotate an access key's secret
    question: Can I rotate an access key's secret without changing its scopes or expiration?
  - id: revoke
    intent: Revoke an access key
    question: Can a revoked access key ever be restored?
  phrasing_ops: 5
  slug: merge-subpackage-accesskeys-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_accountDetails API from Merge — 8 operation(s) for subpackage_accountdetails.
  name: Merge Subpackage Account Details API
  phrasing_intents:
  - id: retrieve
    intent: Get details of a linked accounting account
    question: Which accounting platform is a given end user connected through?
  - id: getAtsV1AccountDetails
    intent: Get details of a linked ATS account
    question: What recruiting system is behind one of my customer's linked accounts?
  - id: getAccountDetails
    intent: Get linked account details from the root endpoint
    question: Is there a category-agnostic way to read a linked account's details?
  - id: getCrmV1AccountDetails
    intent: Get details of a linked CRM account
    question: Which CRM does a particular linked account connect to?
  - id: getFilestorageV1AccountDetails
    intent: Get details of a linked file storage account
    question: What file storage service is a linked account connected to?
  - id: getHrisV1AccountDetails
    intent: Get details of a linked HRIS account
    question: Which HR or payroll system does a given linked account use?
  - id: getKnowledgebaseV1AccountDetails
    intent: Get details of a linked knowledge base account
    question: Which knowledge base tool is a linked account connected to?
  - id: getTicketingV1AccountDetails
    intent: Get details of a linked ticketing account
    question: What help desk is behind one of my linked ticketing accounts?
  phrasing_ops: 8
  slug: merge-subpackage-accountdetails-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_accountingPeriods API from Merge — 2 operation(s) for subpackage_accountingperiods.
  name: Merge Subpackage Accounting Periods API
  phrasing_intents:
  - id: list
    intent: List accounting periods
    question: How do I get the fiscal periods defined in a customer's accounting system?
  - id: retrieve
    intent: Get one accounting period
    question: Can I check whether a single accounting period is open or closed?
  phrasing_ops: 2
  slug: merge-subpackage-accountingperiods-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_accounts API from Merge — 10 operation(s) for subpackage_accounts.
  name: Merge Subpackage Accounts API
  phrasing_intents:
  - id: list
    intent: List the chart of accounts
    question: How do I pull the chart of accounts from my customer's accounting software?
  - id: create
    intent: Add a ledger account to the chart of accounts
    question: Can I create a new general ledger account in a linked accounting system?
  - id: retrieve
    intent: Get one ledger account
    question: How do I read the balance and type of one general ledger account?
  - id: meta-post-retrieve
    intent: See which fields creating a ledger account takes
    question: What fields does the accounting platform need to create a GL account?
  - id: getCrmV1Accounts
    intent: List CRM company accounts
    question: How do I list the companies a sales team tracks in their CRM?
  - id: postCrmV1Accounts
    intent: Create a company account in the CRM
    question: Can I add a new customer company to a linked CRM?
  - id: getCrmV1AccountsById
    intent: Get one CRM account
    question: How do I read a single company record from the CRM?
  - id: partial-update
    intent: Update a CRM account
    question: Can I change the industry or owner on a CRM company record?
  phrasing_ops: 13
  slug: merge-subpackage-accounts-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_accountToken API from Merge — 16 operation(s) for subpackage_accounttoken.
  name: Merge Subpackage Account Token API
  phrasing_intents:
  - id: retrieve
    intent: Get an accounting linked account's account token
    question: How do I exchange an accounting integration's public token for an account token?
  - id: regenerate-create
    intent: Rotate an accounting linked account's token
    question: Can I rotate the account token of a connected accounting platform?
  - id: getAtsV1AccountTokenByPublicToken
    intent: Get a recruiting linked account's account token
    question: What account token do I get after a customer links their applicant tracking system?
  - id: postAtsV1AccountTokenRegenerate
    intent: Rotate a recruiting linked account's token
    question: How do I regenerate the token for a linked applicant tracking system?
  - id: getAccountTokenByPublicToken
    intent: Get a chat linked account's account token
    question: How do I turn a chat integration's public token into an account token?
  - id: postAccountTokenRegenerate
    intent: Rotate a chat linked account's token
    question: Can I rotate the account token of a linked chat workspace?
  - id: getCrmV1AccountTokenByPublicToken
    intent: Get a CRM linked account's account token
    question: What account token maps to the public token from a CRM link flow?
  - id: postCrmV1AccountTokenRegenerate
    intent: Rotate a CRM linked account's token
    question: How can I generate a new account token for a connected CRM?
  phrasing_ops: 16
  slug: merge-subpackage-accounttoken-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_activities API from Merge — 3 operation(s) for subpackage_activities.
  name: Merge Subpackage Activities API
  phrasing_intents:
  - id: list
    intent: List recruiting activities
    question: Can I pull the notes, emails and other activity logged on candidates?
  - id: create
    intent: Log a recruiting activity
    question: How do I log a note or email against a candidate in the ATS?
  - id: retrieve
    intent: Get a recruiting activity
    question: Can I look up one ATS activity by its ID?
  - id: meta-post-retrieve
    intent: Get fields required to log an activity
    question: Which fields are required to log an activity in this ATS?
  phrasing_ops: 4
  slug: merge-subpackage-activities-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_addresses API from Merge — 1 operation(s) for subpackage_addresses.
  name: Merge Subpackage Addresses API
  phrasing_intents:
  - id: retrieve
    intent: Get one accounting address
    question: Can I look up a single billing or shipping address from the accounting system by id?
  phrasing_ops: 1
  slug: merge-subpackage-addresses-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_applicationCredentials API from Merge — 2 operation(s) for subpackage_applicationcredentials.
  name: Merge Subpackage Application Credentials API
  phrasing_intents:
  - id: list
    intent: List OAuth application credentials
    question: Which OAuth apps has my organization registered for Agent Handler connectors?
  - id: create
    intent: Register an OAuth app for a connector
    question: How do I bring my own OAuth client ID and secret for a connector?
  - id: retrieve
    intent: Get one OAuth application credential
    question: Can I look up a single OAuth app credential by its id?
  - id: destroy
    intent: Delete an OAuth application credential
    question: What happens to user credentials when I delete an OAuth application credential?
  - id: partial-update
    intent: Update an OAuth application credential
    question: Can I rotate the client secret on an existing OAuth app credential?
  phrasing_ops: 5
  slug: merge-subpackage-applicationcredentials-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_applications API from Merge — 4 operation(s) for subpackage_applications.
  name: Merge Subpackage Applications API
  phrasing_intents:
  - id: list
    intent: List job applications
    question: Which applications has a given candidate submitted?
  - id: create
    intent: Submit a job application
    question: How do I apply a candidate to a job in the ATS?
  - id: retrieve
    intent: Get a job application
    question: What stage is a particular application at?
  - id: change-stage-create
    intent: Move an application to another interview stage
    question: How do I advance a candidate's application to the next interview stage?
  - id: meta-post-retrieve
    intent: See which fields a new application needs
    question: What fields are required to create an application in this ATS?
  phrasing_ops: 5
  slug: merge-subpackage-applications-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_articles API from Merge — 2 operation(s) for subpackage_articles.
  name: Merge Subpackage Articles API
  phrasing_intents:
  - id: list
    intent: List knowledge base articles
    question: Which articles are published in a connected knowledge base?
  - id: retrieve
    intent: Get a knowledge base article
    question: How do I fetch the content of one help-center article?
  phrasing_ops: 2
  slug: merge-subpackage-articles-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_associations API from Merge — 2 operation(s) for subpackage_associations.
  name: Merge Subpackage Associations API
  phrasing_intents:
  - id: custom-object-classes-custom-objects-associations-list
    intent: List associations of a custom object record
    question: What other records is a given custom object linked to in the CRM?
  - id: custom-object-classes-custom-objects-associations-update
    intent: Link two CRM records with an association
    question: How do I associate one CRM custom object record with another?
  phrasing_ops: 2
  slug: merge-subpackage-associations-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_associationTypes API from Merge — 3 operation(s) for subpackage_associationtypes.
  name: Merge Subpackage Association Types API
  phrasing_intents:
  - id: custom-object-classes-association-types-list
    intent: List association types for a custom object class
    question: What kinds of relationships can a CRM custom object type have?
  - id: custom-object-classes-association-types-create
    intent: Create an association type on a custom object class
    question: How do I define a new relationship type between CRM custom objects?
  - id: custom-object-classes-association-types-retrieve
    intent: Get an association type
    question: Can I look up one association type on a custom object class?
  - id: custom-object-classes-association-types-meta-post-retrieve
    intent: Get fields required to create an association type
    question: Which fields must I send to create an association type?
  phrasing_ops: 4
  slug: merge-subpackage-associationtypes-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_asyncPassthrough API from Merge — 16 operation(s) for subpackage_asyncpassthrough.
  name: Merge Subpackage Async Passthrough API
  phrasing_intents:
  - id: create
    intent: Queue an async passthrough to an accounting system
    question: How do I call an accounting endpoint that the unified API doesn't cover yet?
  - id: retrieve
    intent: Get an accounting async passthrough result
    question: Where do I pick up the response from an async accounting passthrough?
  - id: postAtsV1AsyncPassthrough
    intent: Queue an async passthrough to a recruiting system
    question: Can I reach an applicant tracking system endpoint the common model lacks?
  - id: getAtsV1AsyncPassthroughByAsyncPassthroughReceiptId
    intent: Get a recruiting async passthrough result
    question: What did my queued ATS passthrough request return?
  - id: postAsyncPassthrough
    intent: Queue an async passthrough to a chat platform
    question: How can I hit a chat platform endpoint that isn't in the unified model?
  - id: getAsyncPassthroughByAsyncPassthroughReceiptId
    intent: Get a chat async passthrough result
    question: Where is the output of my queued chat passthrough?
  - id: postCrmV1AsyncPassthrough
    intent: Queue an async passthrough to a CRM
    question: Can I call a CRM endpoint directly when the common model doesn't expose it?
  - id: getCrmV1AsyncPassthroughByAsyncPassthroughReceiptId
    intent: Get a CRM async passthrough result
    question: What response came back from my async CRM passthrough?
  phrasing_ops: 16
  slug: merge-subpackage-asyncpassthrough-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_asyncTasks API from Merge — 1 operation(s) for subpackage_asynctasks.
  name: Merge Subpackage Async Tasks API
  phrasing_intents:
  - id: retrieve
    intent: Check an async accounting write task
    question: Did my asynchronously created accounting record finish writing?
  phrasing_ops: 1
  slug: merge-subpackage-asynctasks-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_attachments API from Merge — 12 operation(s) for subpackage_attachments.
  name: Merge Subpackage Attachments API
  phrasing_intents:
  - id: list
    intent: List accounting attachments
    question: Can I pull every file attached to records in a customer's accounting system?
  - id: create
    intent: Upload an accounting attachment
    question: Can I push a receipt or document into a customer's accounting software?
  - id: retrieve
    intent: Get one accounting attachment
    question: What details come back for a single accounting attachment?
  - id: meta-post-retrieve
    intent: Get fields for creating accounting attachments
    question: Which fields does a customer's accounting integration accept when uploading an attachment?
  - id: getAtsV1Attachments
    intent: List candidate attachments in the ATS
    question: Can I get all resumes and cover letters stored for a candidate?
  - id: postAtsV1Attachments
    intent: Add an attachment to a candidate
    question: Can I upload a resume to a candidate in a customer's ATS?
  - id: getAtsV1AttachmentsById
    intent: Get one candidate attachment
    question: What type of document is a given ATS attachment, resume or offer letter?
  - id: getAtsV1AttachmentsMetaPost
    intent: Get fields for creating ATS attachments
    question: Which fields does an ATS integration require when uploading a candidate file?
  phrasing_ops: 15
  slug: merge-subpackage-attachments-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_auditLog API from Merge — 1 operation(s) for subpackage_auditlog.
  name: Merge Subpackage Audit Log API
  phrasing_intents:
  - id: list
    intent: List audit log events
    question: Who in our organization changed settings or keys recently?
  phrasing_ops: 1
  slug: merge-subpackage-auditlog-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_auditTrail API from Merge — 8 operation(s) for subpackage_audittrail.
  name: Merge Subpackage Audit Trail API
  phrasing_intents:
  - id: list
    intent: List audit trail events (accounting path)
    question: Who on my team changed settings in the accounting integration dashboard last week?
  - id: getAtsV1AuditTrail
    intent: List audit trail events (ATS path)
    question: What actions were logged in the recruiting integrations audit trail?
  - id: getAuditTrail
    intent: List audit trail events (root path)
    question: Is there an audit trail endpoint at the root path without a category prefix?
  - id: getCrmV1AuditTrail
    intent: List audit trail events (CRM path)
    question: Which team members made changes recorded in the CRM audit trail?
  - id: getFilestorageV1AuditTrail
    intent: List audit trail events (file storage path)
    question: What security and settings events appear in the file storage audit trail?
  - id: getHrisV1AuditTrail
    intent: List audit trail events (HRIS path)
    question: Who changed HR integration settings according to the HRIS audit trail?
  - id: getKnowledgebaseV1AuditTrail
    intent: List audit trail events (knowledge base path)
    question: What actions are logged in the knowledge base audit trail?
  - id: getTicketingV1AuditTrail
    intent: List audit trail events (ticketing path)
    question: Which dashboard actions were recorded in the ticketing audit trail?
  phrasing_ops: 8
  slug: merge-subpackage-audittrail-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_availableActions API from Merge — 1 operation(s) for subpackage_availableactions.
  name: Merge Subpackage Available Actions API
  phrasing_intents:
  - id: retrieve
    intent: Get available models and actions for an account
    question: Which Common Models and actions does a customer's linked account support?
  phrasing_ops: 1
  slug: merge-subpackage-availableactions-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_balanceSheets API from Merge — 2 operation(s) for subpackage_balancesheets.
  name: Merge Subpackage Balance Sheets API
  phrasing_intents:
  - id: list
    intent: List balance sheets
    question: Can I pull balance sheet reports from a customer's accounting system?
  - id: retrieve
    intent: Get a balance sheet
    question: What assets, liabilities and equity are on a specific balance sheet report?
  phrasing_ops: 2
  slug: merge-subpackage-balancesheets-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_bankFeedAccounts API from Merge — 3 operation(s) for subpackage_bankfeedaccounts.
  name: Merge Subpackage Bank Feed Accounts API
  phrasing_intents:
  - id: list
    intent: List bank feed accounts
    question: Which bank feed accounts are set up in a customer's accounting system?
  - id: create
    intent: Create a bank feed account
    question: How do I set up a new bank feed account so I can push transactions into the books?
  - id: retrieve
    intent: Get a bank feed account
    question: What details are stored for one specific bank feed account?
  - id: meta-post-retrieve
    intent: Get fields for creating bank feed accounts
    question: Which fields are required to create a bank feed account in an integration?
  phrasing_ops: 4
  slug: merge-subpackage-bankfeedaccounts-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_bankFeedTransactions API from Merge — 3 operation(s) for subpackage_bankfeedtransactions.
  name: Merge Subpackage Bank Feed Transactions API
  phrasing_intents:
  - id: list
    intent: List bank feed transactions
    question: How do I see the bank feed transactions pushed into an accounting platform?
  - id: create
    intent: Push a transaction into a bank feed
    question: Can I send a bank transaction into my customer's accounting bank feed?
  - id: retrieve
    intent: Get one bank feed transaction
    question: How do I read a single bank feed transaction?
  - id: meta-post-retrieve
    intent: See which fields a bank feed transaction takes
    question: Which fields does the platform require to create a bank feed transaction?
  phrasing_ops: 4
  slug: merge-subpackage-bankfeedtransactions-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_bankInfo API from Merge — 2 operation(s) for subpackage_bankinfo.
  name: Merge Subpackage Bank Info API
  phrasing_intents:
  - id: list
    intent: List employee bank accounts
    question: How do I list all employees' direct deposit bank accounts from an HR system?
  - id: retrieve
    intent: Get one employee bank account
    question: Can I read a single employee bank account record by id?
  phrasing_ops: 2
  slug: merge-subpackage-bankinfo-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_benefits API from Merge — 2 operation(s) for subpackage_benefits.
  name: Merge Subpackage Benefits API
  phrasing_intents:
  - id: list
    intent: List employee benefit enrollments
    question: Which benefits is a particular employee enrolled in?
  - id: retrieve
    intent: Get an employee benefit enrollment
    question: What does one employee's benefit enrollment record contain?
  phrasing_ops: 2
  slug: merge-subpackage-benefits-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_candidates API from Merge — 5 operation(s) for subpackage_candidates.
  name: Merge Subpackage Candidates API
  phrasing_intents:
  - id: list
    intent: List candidates
    question: How do I find a candidate by email address in the ATS?
  - id: create
    intent: Add a candidate
    question: How do I add a new candidate to a customer's applicant tracking system?
  - id: retrieve
    intent: Get a candidate
    question: What does the ATS have on file for one candidate?
  - id: partial-update
    intent: Update a candidate's profile
    question: How do I edit an existing candidate's contact details?
  - id: ignore-create
    intent: Stop syncing a candidate
    question: How do I exclude a candidate from future syncs, for example on a GDPR request?
  - id: meta-patch-retrieve
    intent: See which candidate fields can be updated
    question: Which fields can I change on a given candidate?
  - id: meta-post-retrieve
    intent: See which fields creating a candidate needs
    question: What fields are required to add a candidate in this ATS?
  phrasing_ops: 7
  slug: merge-subpackage-candidates-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_cashFlowStatements API from Merge — 2 operation(s) for subpackage_cashflowstatements.
  name: Merge Subpackage Cash Flow Statements API
  phrasing_intents:
  - id: list
    intent: List cash flow statements
    question: Can I pull cash flow statements from a customer's accounting system?
  - id: retrieve
    intent: Get a cash flow statement
    question: Can I open one cash flow statement with its operating, investing and financing sections?
  phrasing_ops: 2
  slug: merge-subpackage-cashflowstatements-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_collections API from Merge — 3 operation(s) for subpackage_collections.
  name: Merge Subpackage Collections API
  phrasing_intents:
  - id: list
    intent: List ticketing collections such as projects
    question: How do I get the projects or lists that group tickets in a help desk?
  - id: viewers-list
    intent: List who can view a ticketing collection
    question: Which users and teams have access to a particular ticket project?
  - id: retrieve
    intent: Get one ticketing collection
    question: How do I read a single ticket project or list?
  phrasing_ops: 3
  slug: merge-subpackage-collections-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_comments API from Merge — 3 operation(s) for subpackage_comments.
  name: Merge Subpackage Comments API
  phrasing_intents:
  - id: list
    intent: List ticket comments
    question: What comments have been left on a particular ticket?
  - id: create
    intent: Add a comment to a ticket
    question: How do I post a reply on a ticket in a connected helpdesk?
  - id: retrieve
    intent: Get a ticket comment
    question: How do I retrieve one specific ticket comment?
  - id: meta-post-retrieve
    intent: See which fields a ticket comment needs
    question: What fields are required to post a comment in this ticketing system?
  phrasing_ops: 4
  slug: merge-subpackage-comments-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_companies API from Merge — 2 operation(s) for subpackage_companies.
  name: Merge Subpackage Companies API
  phrasing_intents:
  - id: list
    intent: List companies in the HRIS
    question: Which legal entities or companies are set up in a customer's HR system?
  - id: retrieve
    intent: Get a company from the HRIS
    question: What legal name and EINs are recorded for one company in the HR system?
  phrasing_ops: 2
  slug: merge-subpackage-companies-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_companyInfo API from Merge — 2 operation(s) for subpackage_companyinfo.
  name: Merge Subpackage Company Info API
  phrasing_intents:
  - id: list
    intent: List company info from the accounting system
    question: How do I get the legal company profile stored in a customer's accounting software?
  - id: retrieve
    intent: Get one company info record
    question: Can I read the fiscal year and currency details for one company?
  phrasing_ops: 2
  slug: merge-subpackage-companyinfo-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_connectors API from Merge — 2 operation(s) for subpackage_connectors.
  name: Merge Subpackage Connectors API
  phrasing_intents:
  - id: list
    intent: List available connectors
    question: Which connectors can I add to a tool pack?
  - id: retrieve
    intent: Get a connector
    question: What tools does a specific connector offer?
  phrasing_ops: 2
  slug: merge-subpackage-connectors-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_contacts API from Merge — 14 operation(s) for subpackage_contacts.
  name: Merge Subpackage Contacts API
  phrasing_intents:
  - id: list
    intent: List customers and suppliers in the accounting system
    question: How do I pull every customer and vendor contact from a linked accounting platform through Merge?
  - id: create
    intent: Create a customer or vendor in accounting
    question: Can I add a new vendor to my customer's accounting ledger through a unified API?
  - id: retrieve
    intent: Get one accounting contact
    question: How can I look up a single vendor or customer record from the accounting integration?
  - id: partial-update
    intent: Update an accounting contact
    question: Can I change a supplier's details in the accounting system after it was created?
  - id: meta-patch-retrieve
    intent: See which accounting contact fields can be edited
    question: Which fields on an accounting contact am I allowed to update for this integration?
  - id: meta-post-retrieve
    intent: See which fields creating an accounting contact takes
    question: What fields does the linked accounting platform require when creating a new contact?
  - id: remote-field-classes-list
    intent: List custom field definitions for accounting contacts
    question: Which custom fields exist on contacts in my customer's accounting software?
  - id: getCrmV1Contacts
    intent: List CRM contacts
    question: How do I pull all the people from a customer's CRM?
  phrasing_ops: 19
  slug: merge-subpackage-contacts-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_containers API from Merge — 2 operation(s) for subpackage_containers.
  name: Merge Subpackage Containers API
  phrasing_intents:
  - id: list
    intent: List knowledge base containers
    question: Can I list the spaces, sections and folders in a customer's knowledge base?
  - id: retrieve
    intent: Get a knowledge base container
    question: Can I fetch one knowledge base container by ID?
  phrasing_ops: 2
  slug: merge-subpackage-containers-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_conversations API from Merge — 3 operation(s) for subpackage_conversations.
  name: Merge Subpackage Conversations API
  phrasing_intents:
  - id: list
    intent: List chat conversations
    question: Which channels and conversations exist in a linked chat workspace?
  - id: retrieve
    intent: Get a chat conversation
    question: How do I pull the details of one channel or conversation?
  - id: members-list
    intent: List members of a chat conversation
    question: Who is in a particular chat channel?
  phrasing_ops: 3
  slug: merge-subpackage-conversations-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_credentials API from Merge — 1 operation(s) for subpackage_credentials.
  name: Merge Subpackage Credentials API
  phrasing_intents:
  - id: registered-users-connectors-destroy
    intent: Delete a registered user's connector credentials
    question: How do I disconnect one user's stored credentials for a specific connector?
  phrasing_ops: 1
  slug: merge-subpackage-credentials-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_creditNotes API from Merge — 5 operation(s) for subpackage_creditnotes.
  name: Merge Subpackage Credit Notes API
  phrasing_intents:
  - id: list
    intent: List credit notes
    question: Can I pull all credit notes issued to customers from a connected accounting system?
  - id: create
    intent: Create a credit note
    question: How do I issue a new credit note in a customer's accounting software?
  - id: retrieve
    intent: Get a credit note
    question: What's the remaining credit and status on a specific credit note?
  - id: partial-update
    intent: Update a credit note
    question: Can I edit an existing credit note after it's been created?
  - id: application-create
    intent: Apply a credit note to an invoice
    question: Can I use a customer's credit note to pay down an open invoice?
  - id: meta-patch-retrieve
    intent: Get editable fields for a credit note
    question: Which fields on an existing credit note does the integration let me edit?
  - id: meta-post-retrieve
    intent: Get fields for creating credit notes
    question: Which fields are required to create a credit note in a given integration?
  phrasing_ops: 7
  slug: merge-subpackage-creditnotes-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_customObjectClasses API from Merge — 2 operation(s) for subpackage_customobjectclasses.
  name: Merge Subpackage Custom Object Classes API
  phrasing_intents:
  - id: list
    intent: List CRM custom object classes
    question: What custom object types has a customer defined in their CRM?
  - id: retrieve
    intent: Get a CRM custom object class
    question: Which fields make up a specific custom object class in the CRM?
  phrasing_ops: 2
  slug: merge-subpackage-customobjectclasses-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_customObjects API from Merge — 4 operation(s) for subpackage_customobjects.
  name: Merge Subpackage Custom Objects API
  phrasing_intents:
  - id: custom-object-classes-custom-objects-list
    intent: List records of a CRM custom object type
    question: Can I pull all records of a custom object type from a customer's CRM?
  - id: custom-object-classes-custom-objects-create
    intent: Create a CRM custom object record
    question: How do I add a record to a custom object type in the CRM?
  - id: custom-object-classes-custom-objects-retrieve
    intent: Get a CRM custom object record
    question: Can I fetch one custom object record by its ID?
  - id: custom-object-classes-custom-objects-meta-post-retrieve
    intent: Get fields required to create a custom object record
    question: Which fields must I send to create a record of a custom object type?
  - id: custom-object-classes-custom-objects-remote-field-classes-list
    intent: List field definitions across CRM custom objects
    question: What remote field classes exist on CRM custom objects?
  phrasing_ops: 5
  slug: merge-subpackage-customobjects-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_customRegexRules API from Merge — 4 operation(s) for subpackage_customregexrules.
  name: Merge Subpackage Custom Regex Rules API
  phrasing_intents:
  - id: list-custom-regex-rules
    intent: List organization custom regex rules
    question: Which custom regex detection rules has my organization defined for Agent Handler?
  - id: create-custom-regex-rule
    intent: Create an organization custom regex rule
    question: Can I add my own regex to detect sensitive data in tool calls across the whole organization?
  - id: get-custom-regex-rule
    intent: Get an organization custom regex rule
    question: What pattern and actions are configured on one of my org-level regex rules?
  - id: delete-custom-regex-rule
    intent: Delete an organization custom regex rule
    question: Can I remove an organization-wide regex rule I no longer need?
  - id: update-custom-regex-rule
    intent: Update an organization custom regex rule
    question: Can I change the pattern of an org-level regex rule after creating it?
  - id: list-custom-regex-rules-tool-pack
    intent: List a tool pack's custom regex rules
    question: Which regex rules apply to a particular tool pack, including inherited org defaults?
  - id: create-custom-regex-rule-tool-pack
    intent: Create a tool pack regex rule or override
    question: Can I override an organization regex rule for just one tool pack?
  - id: get-custom-regex-rule-tool-pack
    intent: Get a tool pack's custom regex rule
    question: What does a specific regex rule look like inside one tool pack?
  phrasing_ops: 10
  slug: merge-subpackage-customregexrules-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_deleteAccount API from Merge — 8 operation(s) for subpackage_deleteaccount.
  name: Merge Subpackage Delete Account API
  phrasing_intents:
  - id: delete
    intent: Delete an accounting linked account
    question: How do I disconnect a customer's accounting integration for good?
  - id: postAtsV1DeleteAccount
    intent: Delete a recruiting linked account
    question: Can I remove a customer's applicant tracking connection entirely?
  - id: postDeleteAccount
    intent: Delete a chat linked account
    question: How can I delete a customer's chat integration linked account?
  - id: postCrmV1DeleteAccount
    intent: Delete a CRM linked account
    question: Can I delete one customer's CRM linked account?
  - id: postFilestorageV1DeleteAccount
    intent: Delete a file storage linked account
    question: How do I remove a customer's file storage connection?
  - id: postHrisV1DeleteAccount
    intent: Delete an HRIS linked account
    question: Can I delete a customer's HR or payroll linked account?
  - id: postKnowledgebaseV1DeleteAccount
    intent: Delete a knowledge base linked account
    question: Can I remove a customer's knowledge base integration completely?
  - id: postTicketingV1DeleteAccount
    intent: Delete a ticketing linked account
    question: Can I delete one customer's ticketing linked account?
  phrasing_ops: 8
  slug: merge-subpackage-deleteaccount-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_departments API from Merge — 2 operation(s) for subpackage_departments.
  name: Merge Subpackage Departments API
  phrasing_intents:
  - id: list
    intent: List recruiting departments
    question: How do I get the departments jobs are organized under in an applicant tracking system?
  - id: retrieve
    intent: Get one recruiting department
    question: Can I read a single ATS department by id?
  phrasing_ops: 2
  slug: merge-subpackage-departments-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_dependents API from Merge — 2 operation(s) for subpackage_dependents.
  name: Merge Subpackage Dependents API
  phrasing_intents:
  - id: list
    intent: List employee dependents
    question: Who are the dependents on file for a given employee?
  - id: retrieve
    intent: Get an employee dependent
    question: How do I retrieve one dependent's record from the HR system?
  phrasing_ops: 2
  slug: merge-subpackage-dependents-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_drives API from Merge — 2 operation(s) for subpackage_drives.
  name: Merge Subpackage Drives API
  phrasing_intents:
  - id: list
    intent: List storage drives
    question: Can I list the drives in a customer's file storage account?
  - id: retrieve
    intent: Get a storage drive
    question: Can I look up one drive by its ID?
  phrasing_ops: 2
  slug: merge-subpackage-drives-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_eeocs API from Merge — 2 operation(s) for subpackage_eeocs.
  name: Merge Subpackage Eeocs API
  phrasing_intents:
  - id: list
    intent: List EEOC demographic records
    question: Can I pull the voluntary EEOC self-identification data candidates submitted?
  - id: retrieve
    intent: Get an EEOC record
    question: What race, gender, veteran and disability answers are on one EEOC record?
  phrasing_ops: 2
  slug: merge-subpackage-eeocs-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_embeddings API from Merge — 1 operation(s) for subpackage_embeddings.
  name: Merge Subpackage Embeddings API
  phrasing_intents:
  - id: create
    intent: Create text embeddings
    question: Can I turn a piece of text into vector embeddings?
  phrasing_ops: 1
  slug: merge-subpackage-embeddings-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_employeePayrollRuns API from Merge — 2 operation(s) for subpackage_employeepayrollruns.
  name: Merge Subpackage Employee Payroll Runs API
  phrasing_intents:
  - id: list
    intent: List employee payroll runs (paystubs)
    question: How do I get individual employees' pay results from an HR or payroll system?
  - id: retrieve
    intent: Get one employee payroll run
    question: Can I read a single employee's paystub-level payroll record?
  phrasing_ops: 2
  slug: merge-subpackage-employeepayrollruns-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_employees API from Merge — 6 operation(s) for subpackage_employees.
  name: Merge Subpackage Employees API
  phrasing_intents:
  - id: list
    intent: List employees recorded in the accounting system
    question: How do I get the staff list that lives in a customer's accounting software?
  - id: retrieve
    intent: Get one employee from the accounting system
    question: Can I read a single employee record stored in the accounting platform?
  - id: getHrisV1Employees
    intent: List employees from the HR system
    question: How do I pull the employee directory from my customer's HRIS?
  - id: getHrisV1EmployeesById
    intent: Get one employee from the HR system
    question: How do I read one person's full HRIS profile?
  - id: ignore-create
    intent: Stop syncing an HRIS employee
    question: How do I exclude one employee's record from future HR syncs?
  - id: meta-post-retrieve
    intent: See which fields creating an HRIS employee takes
    question: What fields does the HR platform require to create a new hire?
  phrasing_ops: 6
  slug: merge-subpackage-employees-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_employerBenefits API from Merge — 2 operation(s) for subpackage_employerbenefits.
  name: Merge Subpackage Employer Benefits API
  phrasing_intents:
  - id: list
    intent: List benefit plans the employer offers
    question: What benefit plans does the company offer its employees?
  - id: retrieve
    intent: Get an employer benefit plan
    question: What are the details of one company-offered benefit plan?
  phrasing_ops: 2
  slug: merge-subpackage-employerbenefits-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_employments API from Merge — 2 operation(s) for subpackage_employments.
  name: Merge Subpackage Employments API
  phrasing_intents:
  - id: list
    intent: List employments
    question: Can I pull job titles and pay rates for employees from the HR system?
  - id: retrieve
    intent: Get an employment
    question: Can I look up a single employment record by ID?
  phrasing_ops: 2
  slug: merge-subpackage-employments-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_engagements API from Merge — 5 operation(s) for subpackage_engagements.
  name: Merge Subpackage Engagements API
  phrasing_intents:
  - id: list
    intent: List CRM engagements
    question: Can I pull calls, meetings and emails logged in a customer's CRM?
  - id: create
    intent: Log a CRM engagement
    question: How do I log a call or meeting in a customer's CRM?
  - id: retrieve
    intent: Get a CRM engagement
    question: Can I see the details of one logged call or meeting?
  - id: partial-update
    intent: Update a CRM engagement
    question: Can I edit a meeting or call that's already logged in the CRM?
  - id: meta-patch-retrieve
    intent: Get fields allowed when updating an engagement
    question: Which fields can I change on a specific CRM engagement?
  - id: meta-post-retrieve
    intent: Get fields required to log an engagement
    question: Which fields are required to log a new engagement in this CRM?
  - id: remote-field-classes-list
    intent: List custom field definitions on engagements
    question: What custom fields does the CRM define on engagements?
  phrasing_ops: 7
  slug: merge-subpackage-engagements-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_engagementTypes API from Merge — 3 operation(s) for subpackage_engagementtypes.
  name: Merge Subpackage Engagement Types API
  phrasing_intents:
  - id: list
    intent: List CRM engagement types
    question: What kinds of engagements, like calls, emails or meetings, does a customer's CRM track?
  - id: retrieve
    intent: Get one CRM engagement type
    question: How do I read a single engagement type from the CRM?
  - id: remote-field-classes-list
    intent: List custom field definitions for engagement types
    question: Which custom fields are defined on CRM engagement types?
  phrasing_ops: 3
  slug: merge-subpackage-engagementtypes-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_expenseReports API from Merge — 6 operation(s) for subpackage_expensereports.
  name: Merge Subpackage Expense Reports API
  phrasing_intents:
  - id: list
    intent: List expense reports
    question: Which expense reports have employees submitted in the accounting system?
  - id: create
    intent: Submit an expense report
    question: How do I create an expense report in a connected accounting platform?
  - id: lines-list
    intent: List the lines on an expense report
    question: What individual expenses make up a given report?
  - id: retrieve
    intent: Get an expense report
    question: How do I pull the header details of one expense report?
  - id: lines-remote-field-classes-list
    intent: List custom field definitions for expense lines
    question: What custom fields can appear on expense report lines?
  - id: meta-post-retrieve
    intent: See which fields an expense report needs
    question: What fields must I send to create an expense report here?
  - id: remote-field-classes-list
    intent: List custom field definitions for expense reports
    question: What custom report-level fields exist on expense reports?
  phrasing_ops: 7
  slug: merge-subpackage-expensereports-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_expenses API from Merge — 7 operation(s) for subpackage_expenses.
  name: Merge Subpackage Expenses API
  phrasing_intents:
  - id: list
    intent: List expenses from the accounting system
    question: How do I pull recorded expenses from a customer's accounting software?
  - id: create
    intent: Record a single expense
    question: Can I write one new expense into a linked accounting platform?
  - id: retrieve
    intent: Get one expense
    question: How do I read a single expense and its lines?
  - id: lines-remote-field-classes-list
    intent: List custom field definitions for expense lines
    question: What custom fields exist on individual expense line items?
  - id: meta-post-retrieve
    intent: See which fields creating an expense takes
    question: Which fields does the accounting platform require to create an expense?
  - id: remote-field-classes-list
    intent: List custom field definitions for expenses
    question: What custom fields are defined at the expense header level?
  - id: async-bulk-create
    intent: Create many expenses in one batch
    question: Can I push a whole batch of expenses at once instead of one by one?
  - id: batch-objects-list
    intent: Check the status of an expense bulk batch
    question: Did my bulk expense upload finish, and which items failed?
  phrasing_ops: 8
  slug: merge-subpackage-expenses-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_fieldMapping API from Merge — 30 operation(s) for subpackage_fieldmapping.
  name: Merge Subpackage Field Mapping API
  phrasing_intents:
  - id: field-mappings-retrieve
    intent: List field mappings on an accounting linked account
    question: Which custom field mappings are set up on my customer's accounting connection?
  - id: field-mappings-create
    intent: Map a remote accounting field to a target field
    question: How do I pull a custom field out of a customer's accounting system into a common model?
  - id: field-mappings-destroy
    intent: Delete an accounting field mapping
    question: What happens to synced ledger data when I remove an accounting field mapping?
  - id: field-mappings-partial-update
    intent: Change an existing accounting field mapping
    question: Can I repoint an accounting field mapping at a different remote endpoint?
  - id: remote-fields-retrieve
    intent: List remote fields available from an accounting integration
    question: Which raw fields does my customer's accounting platform expose that I could map?
  - id: target-fields-retrieve
    intent: List organization-wide accounting target fields
    question: What organization-wide target fields have we defined for accounting data?
  - id: target-fields-create
    intent: Define a new accounting target field
    question: How do I add a custom field to accounting data for every customer at once?
  - id: getAtsV1FieldMappings
    intent: List field mappings on a recruiting linked account
    question: What field mappings exist on this customer's applicant tracking connection?
  phrasing_ops: 50
  slug: merge-subpackage-fieldmapping-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_files API from Merge — 6 operation(s) for subpackage_files.
  name: Merge Subpackage Files API
  phrasing_intents:
  - id: list
    intent: List files in connected file storage
    question: Can I list every file inside a particular folder of a customer's cloud drive?
  - id: create
    intent: Upload a file to connected file storage
    question: How do I upload a new file into a customer's cloud drive?
  - id: retrieve
    intent: Get a file's metadata
    question: Which folder and drive does a specific file belong to?
  - id: download-retrieve
    intent: Download a file's contents
    question: Can I download the actual bytes of a file from a customer's drive?
  - id: download-request-meta-retrieve
    intent: Get a direct download request for one file
    question: Can I download a file straight from the third-party provider instead of streaming it through the unified API?
  - id: download-request-meta-list
    intent: Get direct download requests for many files
    question: Can I get direct third-party download requests for a batch of files at once?
  - id: meta-post-retrieve
    intent: Get fields for uploading files
    question: Which fields does a storage integration require when uploading a file?
  phrasing_ops: 7
  slug: merge-subpackage-files-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_folders API from Merge — 3 operation(s) for subpackage_folders.
  name: Merge Subpackage Folders API
  phrasing_intents:
  - id: list
    intent: List folders
    question: Can I list the folders in a customer's cloud storage?
  - id: create
    intent: Create a folder
    question: How do I create a new folder in a customer's file storage?
  - id: retrieve
    intent: Get a folder
    question: Can I look up one folder by its ID?
  - id: meta-post-retrieve
    intent: Get fields required to create a folder
    question: Which fields are required to create a folder in this storage provider?
  phrasing_ops: 4
  slug: merge-subpackage-folders-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_forceResync API from Merge — 8 operation(s) for subpackage_forceresync.
  name: Merge Subpackage Force Resync API
  phrasing_intents:
  - id: sync-status-resync-create
    intent: Force a full resync of an accounting account
    question: How do I force every accounting model to sync again right now?
  - id: postAtsV1SyncStatusResync
    intent: Force a full resync of a recruiting account
    question: Can I trigger an immediate re-sync of all ATS data?
  - id: postSyncStatusResync
    intent: Force a full resync of a chat account
    question: How can I make the chat integration sync everything again?
  - id: postCrmV1SyncStatusResync
    intent: Force a full resync of a CRM account
    question: Can I force my CRM data to refresh immediately?
  - id: postFilestorageV1SyncStatusResync
    intent: Force a full resync of a file storage account
    question: How do I force a fresh sync of all files and folders?
  - id: postHrisV1SyncStatusResync
    intent: Force a full resync of an HRIS account
    question: Can I trigger an immediate resync of employee and payroll data?
  - id: postKnowledgebaseV1SyncStatusResync
    intent: Force a full resync of a knowledge base account
    question: How do I make a knowledge base re-sync every article now?
  - id: postTicketingV1SyncStatusResync
    intent: Force a full resync of a ticketing account
    question: Can I force all tickets to sync again right now?
  phrasing_ops: 8
  slug: merge-subpackage-forceresync-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_generateKey API from Merge — 8 operation(s) for subpackage_generatekey.
  name: Merge Subpackage Generate Key API
  phrasing_intents:
  - id: create
    intent: Create a remote API key (accounting path)
    question: How do I generate a new production API key from the accounting endpoint?
  - id: postAtsV1GenerateKey
    intent: Create a remote API key (ATS path)
    question: Can I mint a new remote key through the ATS category endpoint?
  - id: postGenerateKey
    intent: Create a remote API key (root path)
    question: Is there a generate-key endpoint at the root path with no category?
  - id: postCrmV1GenerateKey
    intent: Create a remote API key (CRM path)
    question: Can I generate a new remote key from the CRM API?
  - id: postFilestorageV1GenerateKey
    intent: Create a remote API key (file storage path)
    question: Can I create a remote key from the file storage category endpoint?
  - id: postHrisV1GenerateKey
    intent: Create a remote API key (HRIS path)
    question: Can I generate a new remote key through the HRIS endpoint?
  - id: postKnowledgebaseV1GenerateKey
    intent: Create a remote API key (knowledge base path)
    question: Can I create a remote key via the knowledge base category?
  - id: postTicketingV1GenerateKey
    intent: Create a remote API key (ticketing path)
    question: Can I generate a new remote key from the ticketing API?
  phrasing_ops: 8
  slug: merge-subpackage-generatekey-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_groups API from Merge — 9 operation(s) for subpackage_groups.
  name: Merge Subpackage Groups API
  phrasing_intents:
  - id: list
    intent: List chat groups and channels
    question: How do I list the groups in my customer's chat workspace?
  - id: retrieve
    intent: Get one chat group
    question: Can I read a single chat group and its members?
  - id: getFilestorageV1Groups
    intent: List file storage permission groups
    question: Which user groups exist in the linked file storage platform?
  - id: getFilestorageV1GroupsById
    intent: Get one file storage group
    question: How do I see who belongs to a single file storage group?
  - id: getHrisV1Groups
    intent: List HRIS groups such as teams and departments
    question: How do I get departments, teams and cost centers from an HR system?
  - id: getHrisV1GroupsById
    intent: Get one HRIS group
    question: How can I read one department or team record from HR?
  - id: types-list
    intent: List the distinct HRIS group types
    question: What kinds of groups (teams, departments, business units) does this HR system use?
  - id: getKnowledgebaseV1Groups
    intent: List knowledge base groups
    question: Which user groups are defined in the linked knowledge base?
  phrasing_ops: 9
  slug: merge-subpackage-groups-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_incomeStatements API from Merge — 2 operation(s) for subpackage_incomestatements.
  name: Merge Subpackage Income Statements API
  phrasing_intents:
  - id: list
    intent: List income statements
    question: Can I pull profit and loss reports from a customer's accounting system?
  - id: retrieve
    intent: Get an income statement
    question: What income, cost of sales and expenses are on a specific P&L report?
  phrasing_ops: 2
  slug: merge-subpackage-incomestatements-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_interviews API from Merge — 3 operation(s) for subpackage_interviews.
  name: Merge Subpackage Interviews API
  phrasing_intents:
  - id: list
    intent: List scheduled interviews
    question: Can I see every interview scheduled for a particular job application?
  - id: create
    intent: Schedule an interview
    question: How do I schedule a candidate interview in a customer's ATS?
  - id: retrieve
    intent: Get a scheduled interview
    question: When and where is a specific interview happening, and who's on the panel?
  - id: meta-post-retrieve
    intent: Get fields for scheduling interviews
    question: Which fields does an ATS require when scheduling an interview?
  phrasing_ops: 4
  slug: merge-subpackage-interviews-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_invoices API from Merge — 8 operation(s) for subpackage_invoices.
  name: Merge Subpackage Invoices API
  phrasing_intents:
  - id: list
    intent: List invoices
    question: Which invoices are still unpaid in my customer's accounting system?
  - id: create
    intent: Create an invoice
    question: How do I create an invoice in a connected accounting platform?
  - id: retrieve
    intent: Get an invoice
    question: What line items and totals are on a specific invoice?
  - id: partial-update
    intent: Update an existing invoice
    question: How do I change fields on an invoice that's already been created?
  - id: line-items-remote-field-classes-list
    intent: List custom field definitions for invoice line items
    question: What custom fields can appear on invoice line items?
  - id: meta-patch-retrieve
    intent: See which invoice fields can be updated
    question: Which fields am I allowed to edit on a given invoice?
  - id: meta-post-retrieve
    intent: See which fields creating an invoice needs
    question: What fields are required to create an invoice for this integration?
  - id: remote-field-classes-list
    intent: List custom field definitions for invoices
    question: What custom invoice-level fields does the accounting system expose?
  phrasing_ops: 10
  slug: merge-subpackage-invoices-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_issues API from Merge — 16 operation(s) for subpackage_issues.
  name: Merge Subpackage Issues API
  phrasing_intents:
  - id: list
    intent: List integration issues from the accounting API
    question: How do I see which accounting integrations are throwing errors for my organization?
  - id: retrieve
    intent: Get one issue via the accounting API
    question: Where can I read the details of a single sync problem reported under accounting?
  - id: getAtsV1Issues
    intent: List integration issues from the ATS API
    question: Which of my recruiting (ATS) integrations currently have problems?
  - id: getAtsV1IssuesById
    intent: Get one issue via the ATS API
    question: How can I look at a single recruiting integration issue in detail?
  - id: getIssues
    intent: List integration issues from the root endpoint
    question: Is there an unscoped endpoint that lists all integration issues for my organization?
  - id: getIssuesById
    intent: Get one issue from the root endpoint
    question: Can I fetch an issue by id without going through a category-specific path?
  - id: getCrmV1Issues
    intent: List integration issues from the CRM API
    question: Which CRM connections are reporting sync errors right now?
  - id: getCrmV1IssuesById
    intent: Get one issue via the CRM API
    question: How do I get details on one CRM sync issue?
  phrasing_ops: 16
  slug: merge-subpackage-issues-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_itemFulfillments API from Merge — 6 operation(s) for subpackage_itemfulfillments.
  name: Merge Subpackage Item Fulfillments API
  phrasing_intents:
  - id: list
    intent: List item fulfillments
    question: How do I see which orders have been shipped or fulfilled in my customer's accounting system?
  - id: create
    intent: Record a single item fulfillment
    question: Can I mark goods as fulfilled against an order in the linked accounting platform?
  - id: retrieve
    intent: Get one item fulfillment
    question: How do I read the lines on a single fulfillment?
  - id: lines-remote-field-classes-list
    intent: List custom field definitions for fulfillment lines
    question: What custom fields exist on individual fulfillment line items?
  - id: remote-field-classes-list
    intent: List custom field definitions for item fulfillments
    question: Which custom fields are defined at the item fulfillment header level?
  - id: async-bulk-create
    intent: Create many item fulfillments in one batch
    question: Can I submit a batch of fulfillments at once?
  - id: batch-objects-list
    intent: Check the status of a fulfillment bulk batch
    question: Did my bulk item fulfillment upload complete?
  phrasing_ops: 7
  slug: merge-subpackage-itemfulfillments-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_items API from Merge — 4 operation(s) for subpackage_items.
  name: Merge Subpackage Items API
  phrasing_intents:
  - id: list
    intent: List accounting items
    question: Can I pull the products and services list from a customer's accounting system?
  - id: create
    intent: Create an accounting item
    question: How do I add a new product or service item to the ledger?
  - id: retrieve
    intent: Get an accounting item
    question: Can I look up one product or service item by ID?
  - id: partial-update
    intent: Update an accounting item
    question: Can I change the price or name of an existing item?
  - id: meta-patch-retrieve
    intent: Get fields allowed when updating an item
    question: Which fields can I change on a specific accounting item?
  - id: meta-post-retrieve
    intent: Get fields required to create an item
    question: Which fields must I send to create a new item?
  phrasing_ops: 6
  slug: merge-subpackage-items-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_jobInterviewStages API from Merge — 2 operation(s) for subpackage_jobinterviewstages.
  name: Merge Subpackage Job Interview Stages API
  phrasing_intents:
  - id: list
    intent: List interview stages for jobs
    question: How do I get the hiring pipeline stages set up in an applicant tracking system?
  - id: retrieve
    intent: Get one job interview stage
    question: Can I read a single interview stage by id?
  phrasing_ops: 2
  slug: merge-subpackage-jobinterviewstages-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_jobPostings API from Merge — 2 operation(s) for subpackage_jobpostings.
  name: Merge Subpackage Job Postings API
  phrasing_intents:
  - id: list
    intent: List job postings
    question: Which job postings are live on the careers site right now?
  - id: retrieve
    intent: Get a job posting
    question: What does a particular public job posting say?
  phrasing_ops: 2
  slug: merge-subpackage-jobpostings-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_jobs API from Merge — 3 operation(s) for subpackage_jobs.
  name: Merge Subpackage Jobs API
  phrasing_intents:
  - id: list
    intent: List jobs
    question: Which job openings are currently open in the ATS?
  - id: retrieve
    intent: Get a job
    question: What departments, offices and hiring managers are on a given job?
  - id: screening-questions-list
    intent: List a job's screening questions
    question: What screening questions do applicants to a job have to answer?
  phrasing_ops: 3
  slug: merge-subpackage-jobs-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_journalEntries API from Merge — 5 operation(s) for subpackage_journalentries.
  name: Merge Subpackage Journal Entries API
  phrasing_intents:
  - id: list
    intent: List journal entries
    question: How do I pull manual journal entries from a customer's general ledger?
  - id: create
    intent: Post a journal entry
    question: Can I write a new journal entry into the linked accounting platform?
  - id: retrieve
    intent: Get one journal entry
    question: How do I read a single journal entry and its debit and credit lines?
  - id: lines-remote-field-classes-list
    intent: List custom field definitions for journal lines
    question: What custom fields exist on individual journal entry lines?
  - id: meta-post-retrieve
    intent: See which fields posting a journal entry takes
    question: Which fields are required to post a journal entry to this ledger?
  - id: remote-field-classes-list
    intent: List custom field definitions for journal entries
    question: Which custom fields are defined at the journal entry header level?
  phrasing_ops: 6
  slug: merge-subpackage-journalentries-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_leads API from Merge — 4 operation(s) for subpackage_leads.
  name: Merge Subpackage Leads API
  phrasing_intents:
  - id: list
    intent: List CRM leads
    question: Can I pull all leads owned by a particular sales rep from a customer's CRM?
  - id: create
    intent: Create a CRM lead
    question: How do I add a new lead to a customer's CRM?
  - id: retrieve
    intent: Get a CRM lead
    question: What company, source and owner are recorded on one lead?
  - id: meta-post-retrieve
    intent: Get fields for creating leads
    question: Which fields does a CRM integration require when creating a lead?
  - id: remote-field-classes-list
    intent: List custom field definitions for leads
    question: What custom fields are defined on leads in a customer's CRM?
  phrasing_ops: 5
  slug: merge-subpackage-leads-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_linkedAccounts API from Merge — 8 operation(s) for subpackage_linkedaccounts.
  name: Merge Subpackage Linked Accounts API
  phrasing_intents:
  - id: list
    intent: List accounting linked accounts
    question: Which customers have connected an accounting system to our product?
  - id: getAtsV1LinkedAccounts
    intent: List recruiting linked accounts
    question: Which of our customers have linked an applicant tracking system?
  - id: getLinkedAccounts
    intent: List chat linked accounts
    question: Which customers have connected a chat platform through us?
  - id: getCrmV1LinkedAccounts
    intent: List CRM linked accounts
    question: Which customers have hooked up a CRM, and which one?
  - id: getFilestorageV1LinkedAccounts
    intent: List file storage linked accounts
    question: Which customers have connected a file storage provider?
  - id: getHrisV1LinkedAccounts
    intent: List HRIS linked accounts
    question: Which customers have linked an HR or payroll system?
  - id: getKnowledgebaseV1LinkedAccounts
    intent: List knowledge base linked accounts
    question: Which customers have connected a knowledge base or help center?
  - id: getTicketingV1LinkedAccounts
    intent: List ticketing linked accounts
    question: Which customers have linked a helpdesk or ticketing tool?
  phrasing_ops: 8
  slug: merge-subpackage-linkedaccounts-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_linkToken API from Merge — 9 operation(s) for subpackage_linktoken.
  name: Merge Subpackage Link Token API
  phrasing_intents:
  - id: create
    intent: Create a Link token for accounting integrations
    question: How do I start the flow that lets a customer connect their accounting software?
  - id: create-for-registered-user
    intent: Create a connector link token for a registered user
    question: Can I generate a magic link so an Agent Handler registered user can authenticate a connector in their browser?
  - id: postAtsV1LinkToken
    intent: Create a Link token for ATS integrations
    question: What do I need to let a customer connect their applicant tracking system?
  - id: postLinkToken
    intent: Create a Link token via the root path
    question: Is there a root-level link-token endpoint without a category in the path?
  - id: postCrmV1LinkToken
    intent: Create a Link token for CRM integrations
    question: How can a customer connect their CRM through the embedded linking flow?
  - id: postFilestorageV1LinkToken
    intent: Create a Link token for file storage integrations
    question: What does a customer need to connect their cloud drive through Link?
  - id: postHrisV1LinkToken
    intent: Create a Link token for HRIS integrations
    question: How do I let a customer connect their HR or payroll system?
  - id: postKnowledgebaseV1LinkToken
    intent: Create a Link token for knowledge base integrations
    question: How can a customer connect their help center or wiki for syncing?
  phrasing_ops: 9
  slug: merge-subpackage-linktoken-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_locations API from Merge — 2 operation(s) for subpackage_locations.
  name: Merge Subpackage Locations API
  phrasing_intents:
  - id: list
    intent: List HR locations
    question: Can I list the office and home addresses recorded in the HR system?
  - id: retrieve
    intent: Get an HR location
    question: Can I look up one HRIS location by its ID?
  phrasing_ops: 2
  slug: merge-subpackage-locations-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_mcp API from Merge — 1 operation(s) for subpackage_mcp.
  name: Merge Subpackage MCP API
  phrasing_intents:
  - id: endpoint-post
    intent: List or call tools over the MCP endpoint
    question: How do I list the tools a registered user can call over MCP?
  phrasing_ops: 1
  slug: merge-subpackage-mcp-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_messages API from Merge — 3 operation(s) for subpackage_messages.
  name: Merge Subpackage Messages API
  phrasing_intents:
  - id: list
    intent: List chat messages
    question: Can I pull messages from a conversation in a customer's chat tool?
  - id: retrieve
    intent: Get a chat message
    question: Can I fetch one chat message by its ID?
  - id: replies-list
    intent: List replies in a message thread
    question: Can I list every reply in a chat thread?
  phrasing_ops: 3
  slug: merge-subpackage-messages-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_models API from Merge — 1 operation(s) for subpackage_models.
  name: Merge Subpackage Models API
  phrasing_intents:
  - id: list
    intent: List available public models
    question: Which public AI models can I use, and who provides them?
  phrasing_ops: 1
  slug: merge-subpackage-models-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_notes API from Merge — 4 operation(s) for subpackage_notes.
  name: Merge Subpackage Notes API
  phrasing_intents:
  - id: list
    intent: List CRM notes
    question: How do I pull the notes reps logged in a customer's CRM?
  - id: create
    intent: Add a note in the CRM
    question: Can I log a call summary as a note in the linked CRM?
  - id: retrieve
    intent: Get one CRM note
    question: How do I read a single note from the CRM?
  - id: meta-post-retrieve
    intent: See which fields creating a CRM note takes
    question: Which fields does the CRM require when I create a note?
  - id: remote-field-classes-list
    intent: List custom field definitions for CRM notes
    question: What custom fields has the CRM added to notes?
  phrasing_ops: 5
  slug: merge-subpackage-notes-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_offers API from Merge — 2 operation(s) for subpackage_offers.
  name: Merge Subpackage Offers API
  phrasing_intents:
  - id: list
    intent: List job offers
    question: Can I see all offers extended for a particular job application?
  - id: retrieve
    intent: Get a job offer
    question: When was a specific offer sent and what's its current status?
  phrasing_ops: 2
  slug: merge-subpackage-offers-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_offices API from Merge — 2 operation(s) for subpackage_offices.
  name: Merge Subpackage Offices API
  phrasing_intents:
  - id: list
    intent: List recruiting office locations
    question: How do I get the office locations jobs are posted for in an ATS?
  - id: retrieve
    intent: Get one recruiting office
    question: Can I read a single ATS office location by id?
  phrasing_ops: 2
  slug: merge-subpackage-offices-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_opportunities API from Merge — 5 operation(s) for subpackage_opportunities.
  name: Merge Subpackage Opportunities API
  phrasing_intents:
  - id: list
    intent: List CRM opportunities
    question: Can I pull every open deal from a customer's CRM?
  - id: create
    intent: Create a CRM opportunity
    question: How do I add a new deal to a customer's CRM?
  - id: retrieve
    intent: Get a CRM opportunity
    question: Can I look up one deal by its ID?
  - id: partial-update
    intent: Update a CRM opportunity
    question: Can I move a deal to a new stage or change its amount?
  - id: meta-patch-retrieve
    intent: Get fields allowed when updating an opportunity
    question: Which fields can I edit on a particular opportunity?
  - id: meta-post-retrieve
    intent: Get fields required to create an opportunity
    question: Which fields are required to create a deal in this CRM?
  - id: remote-field-classes-list
    intent: List custom field definitions on opportunities
    question: What custom deal fields does this CRM define?
  phrasing_ops: 7
  slug: merge-subpackage-opportunities-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_passthrough API from Merge — 8 operation(s) for subpackage_passthrough.
  name: Merge Subpackage Passthrough API
  phrasing_intents:
  - id: create
    intent: Call an unsupported accounting endpoint directly
    question: How do I reach an accounting platform endpoint that Merge's common model doesn't cover?
  - id: postAtsV1Passthrough
    intent: Call an unsupported ATS endpoint directly
    question: Can I hit a recruiting system's native endpoint that the ATS model lacks?
  - id: postPassthrough
    intent: Call an unsupported endpoint via the root passthrough
    question: Is there a top-level passthrough not tied to a specific category?
  - id: postCrmV1Passthrough
    intent: Call an unsupported CRM endpoint directly
    question: How can I read CRM data that isn't in the unified CRM model?
  - id: postFilestorageV1Passthrough
    intent: Call an unsupported file storage endpoint directly
    question: Can I upload through a file storage provider's native endpoint with multipart form data?
  - id: postHrisV1Passthrough
    intent: Call an unsupported HRIS endpoint directly
    question: How do I get HR data the HRIS common model doesn't expose?
  - id: postKnowledgebaseV1Passthrough
    intent: Call an unsupported knowledge base endpoint directly
    question: Can I call a knowledge base tool's own API path through Merge?
  - id: postTicketingV1Passthrough
    intent: Call an unsupported ticketing endpoint directly
    question: How do I reach a help desk endpoint that the ticketing model doesn't support?
  phrasing_ops: 8
  slug: merge-subpackage-passthrough-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_payGroups API from Merge — 2 operation(s) for subpackage_paygroups.
  name: Merge Subpackage Pay Groups API
  phrasing_intents:
  - id: list
    intent: List pay groups
    question: What pay groups are set up in the payroll system?
  - id: retrieve
    intent: Get a pay group
    question: How do I retrieve one pay group's details?
  phrasing_ops: 2
  slug: merge-subpackage-paygroups-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_paymentMethods API from Merge — 2 operation(s) for subpackage_paymentmethods.
  name: Merge Subpackage Payment Methods API
  phrasing_intents:
  - id: list
    intent: List accounting payment methods
    question: Which payment methods are set up in a customer's accounting system?
  - id: retrieve
    intent: Get an accounting payment method
    question: Can I look up one payment method by its ID?
  phrasing_ops: 2
  slug: merge-subpackage-paymentmethods-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_payments API from Merge — 6 operation(s) for subpackage_payments.
  name: Merge Subpackage Payments API
  phrasing_intents:
  - id: list
    intent: List payments
    question: Which payments were recorded against a given account last month?
  - id: create
    intent: Record a payment
    question: How do I record a payment in a customer's accounting software?
  - id: retrieve
    intent: Get a payment
    question: What invoices did a specific payment apply to?
  - id: partial-update
    intent: Update an existing payment
    question: How do I modify a payment that was already recorded?
  - id: line-items-remote-field-classes-list
    intent: List custom field definitions for payment line items
    question: What custom fields appear on payment line items?
  - id: meta-patch-retrieve
    intent: See which payment fields can be updated
    question: Which fields can I change on a recorded payment?
  - id: meta-post-retrieve
    intent: See which fields recording a payment needs
    question: What fields are required to record a new payment?
  - id: remote-field-classes-list
    intent: List custom field definitions for payments
    question: What custom payment-level fields exist in the accounting system?
  phrasing_ops: 8
  slug: merge-subpackage-payments-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_paymentTerms API from Merge — 2 operation(s) for subpackage_paymentterms.
  name: Merge Subpackage Payment Terms API
  phrasing_intents:
  - id: list
    intent: List payment terms
    question: Which payment terms like Net 30 are configured in a customer's books?
  - id: retrieve
    intent: Get a payment term
    question: How many days until due does a specific payment term allow?
  phrasing_ops: 2
  slug: merge-subpackage-paymentterms-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_payrollRuns API from Merge — 2 operation(s) for subpackage_payrollruns.
  name: Merge Subpackage Payroll Runs API
  phrasing_intents:
  - id: list
    intent: List company payroll runs
    question: How do I get the payroll runs a company has processed in its payroll system?
  - id: retrieve
    intent: Get one company payroll run
    question: Can I read the dates and status of a single payroll run?
  phrasing_ops: 2
  slug: merge-subpackage-payrollruns-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_phoneNumbers API from Merge — 1 operation(s) for subpackage_phonenumbers.
  name: Merge Subpackage Phone Numbers API
  phrasing_intents:
  - id: retrieve
    intent: Get one accounting phone number
    question: Can I look up a single phone number record from the accounting system?
  phrasing_ops: 1
  slug: merge-subpackage-phonenumbers-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_projects API from Merge — 2 operation(s) for subpackage_projects.
  name: Merge Subpackage Projects API
  phrasing_intents:
  - id: list
    intent: List accounting projects
    question: Which projects are active in the accounting system?
  - id: retrieve
    intent: Get an accounting project
    question: How do I look up one accounting project by ID?
  phrasing_ops: 2
  slug: merge-subpackage-projects-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_purchaseOrders API from Merge — 5 operation(s) for subpackage_purchaseorders.
  name: Merge Subpackage Purchase Orders API
  phrasing_intents:
  - id: list
    intent: List purchase orders
    question: Which purchase orders were issued last quarter?
  - id: create
    intent: Create a purchase order
    question: How do I raise a new purchase order in a connected accounting platform?
  - id: retrieve
    intent: Get a purchase order
    question: What items and vendor are on a specific purchase order?
  - id: line-items-remote-field-classes-list
    intent: List custom field definitions for PO line items
    question: What custom fields exist on purchase order line items?
  - id: meta-post-retrieve
    intent: See which fields a purchase order needs
    question: What fields are required to create a purchase order for this integration?
  - id: remote-field-classes-list
    intent: List custom field definitions for purchase orders
    question: What custom header fields are on purchase orders?
  phrasing_ops: 6
  slug: merge-subpackage-purchaseorders-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_regenerateKey API from Merge — 8 operation(s) for subpackage_regeneratekey.
  name: Merge Subpackage Regenerate Key API
  phrasing_intents:
  - id: create
    intent: Exchange remote keys (accounting path)
    question: How do I rotate my remote API key through the accounting endpoint?
  - id: postAtsV1RegenerateKey
    intent: Exchange remote keys (ATS path)
    question: Can I rotate my remote key using the ATS endpoint?
  - id: postRegenerateKey
    intent: Exchange remote keys (root path)
    question: Is there a regenerate-key endpoint at the root path without a category?
  - id: postCrmV1RegenerateKey
    intent: Exchange remote keys (CRM path)
    question: Can I rotate my remote key from the CRM API?
  - id: postFilestorageV1RegenerateKey
    intent: Exchange remote keys (file storage path)
    question: Can I rotate my remote key through the file storage endpoint?
  - id: postHrisV1RegenerateKey
    intent: Exchange remote keys (HRIS path)
    question: Can I rotate my remote key using the HRIS API?
  - id: postKnowledgebaseV1RegenerateKey
    intent: Exchange remote keys (knowledge base path)
    question: Can I rotate my remote key via the knowledge base category?
  - id: postTicketingV1RegenerateKey
    intent: Exchange remote keys (ticketing path)
    question: Can I rotate my remote key from the ticketing API?
  phrasing_ops: 8
  slug: merge-subpackage-regeneratekey-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_registeredUsers API from Merge — 2 operation(s) for subpackage_registeredusers.
  name: Merge Subpackage Registered Users API
  phrasing_intents:
  - id: list
    intent: List registered users
    question: Which registered users exist in my organization?
  - id: create
    intent: Register a user
    question: How do I register one of my app's users?
  - id: retrieve
    intent: Get a registered user
    question: How do I look up one registered user?
  - id: destroy
    intent: Delete a registered user
    question: What removes a registered user from my organization?
  - id: partial-update
    intent: Update a registered user
    question: How do I rename a registered user?
  phrasing_ops: 5
  slug: merge-subpackage-registeredusers-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_rejectReasons API from Merge — 2 operation(s) for subpackage_rejectreasons.
  name: Merge Subpackage Reject Reasons API
  phrasing_intents:
  - id: list
    intent: List candidate rejection reasons
    question: What rejection reasons are configured in a customer's ATS?
  - id: retrieve
    intent: Get a candidate rejection reason
    question: Can I look up one reject reason by ID?
  phrasing_ops: 2
  slug: merge-subpackage-rejectreasons-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_responses API from Merge — 1 operation(s) for subpackage_responses.
  name: Merge Subpackage Responses API
  phrasing_intents:
  - id: create
    intent: Generate an LLM response
    question: How do I get a model to answer a conversation through the gateway?
  phrasing_ops: 1
  slug: merge-subpackage-responses-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_roles API from Merge — 2 operation(s) for subpackage_roles.
  name: Merge Subpackage Roles API
  phrasing_intents:
  - id: list
    intent: List ticketing roles
    question: What user roles are defined in a customer's helpdesk or issue tracker?
  - id: retrieve
    intent: Get a ticketing role
    question: What permissions does a specific ticketing role grant?
  phrasing_ops: 2
  slug: merge-subpackage-roles-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_routing API from Merge — 2 operation(s) for subpackage_routing.
  name: Merge Subpackage Routing API
  phrasing_intents:
  - id: list-policies
    intent: List routing policies
    question: Which routing policies can I use, including the managed simulator policy?
  - id: list-strategies
    intent: List routing strategies
    question: What routing strategies are available, and what does each one do?
  phrasing_ops: 2
  slug: merge-subpackage-routing-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_salesOrders API from Merge — 7 operation(s) for subpackage_salesorders.
  name: Merge Subpackage Sales Orders API
  phrasing_intents:
  - id: list
    intent: List sales orders
    question: Can I pull every sales order from a customer's accounting system?
  - id: create
    intent: Create a sales order
    question: How do I record a new sales order in a customer's accounting platform?
  - id: retrieve
    intent: Get a sales order
    question: Can I look up one sales order by its ID?
  - id: lines-remote-field-classes-list
    intent: List custom field definitions on sales order lines
    question: What custom fields exist on sales order line items?
  - id: meta-post-retrieve
    intent: Get fields required to create a sales order
    question: Which fields must I send to create a sales order?
  - id: remote-field-classes-list
    intent: List custom field definitions on sales orders
    question: What custom header-level fields does the ledger define on sales orders?
  - id: async-bulk-create
    intent: Create many sales orders in one batch
    question: Can I create a batch of sales orders in one request?
  - id: batch-objects-list
    intent: Check a sales order bulk batch
    question: Did my bulk sales order batch finish, and what were the results?
  phrasing_ops: 8
  slug: merge-subpackage-salesorders-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_scopes API from Merge — 16 operation(s) for subpackage_scopes.
  name: Merge Subpackage Scopes API
  phrasing_intents:
  - id: default-scopes-retrieve
    intent: Get default accounting data scopes
    question: What Common Model and field permissions apply by default to every accounting Linked Account?
  - id: linked-account-scopes-retrieve
    intent: Get scopes for one accounting linked account
    question: Which accounting models and fields is one specific Linked Account allowed to sync?
  - id: linked-account-scopes-create
    intent: Override scopes for one accounting linked account
    question: Can I restrict which accounting fields one Linked Account syncs without touching the defaults?
  - id: getAtsV1DefaultScopes
    intent: Get default recruiting (ATS) data scopes
    question: What candidate and job data do all my ATS Linked Accounts sync by default?
  - id: getAtsV1LinkedAccountScopes
    intent: Get scopes for one ATS linked account
    question: Which candidate and application fields can one connected ATS actually sync?
  - id: postAtsV1LinkedAccountScopes
    intent: Override scopes for one ATS linked account
    question: Can I stop one customer's ATS connection from syncing certain candidate fields?
  - id: getDefaultScopes
    intent: Get default scopes via the root path
    question: Is there a default-scopes endpoint at the root path without a category prefix?
  - id: getLinkedAccountScopes
    intent: Get linked account scopes via the root path
    question: Can I read a Linked Account's scopes from the unprefixed root path?
  phrasing_ops: 24
  slug: merge-subpackage-scopes-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_scorecards API from Merge — 2 operation(s) for subpackage_scorecards.
  name: Merge Subpackage Scorecards API
  phrasing_intents:
  - id: list
    intent: List interview scorecards
    question: What scorecards have interviewers submitted for an application?
  - id: retrieve
    intent: Get an interview scorecard
    question: What did an interviewer record on a particular scorecard?
  phrasing_ops: 2
  slug: merge-subpackage-scorecards-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_stages API from Merge — 3 operation(s) for subpackage_stages.
  name: Merge Subpackage Stages API
  phrasing_intents:
  - id: list
    intent: List CRM pipeline stages
    question: What deal stages exist in a customer's CRM pipeline?
  - id: retrieve
    intent: Get a CRM pipeline stage
    question: What's the name of a specific opportunity stage?
  - id: remote-field-classes-list
    intent: List custom field definitions for stages
    question: Which custom fields are defined on pipeline stages in the CRM?
  phrasing_ops: 3
  slug: merge-subpackage-stages-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_standardEntityRules API from Merge — 4 operation(s) for subpackage_standardentityrules.
  name: Merge Subpackage Standard Entity Rules API
  phrasing_intents:
  - id: list-standard-entity-rules
    intent: List organization-wide sensitive data rules
    question: What standard entity rules apply across my whole organization?
  - id: get-standard-entity-rule
    intent: Get an organization sensitive data rule
    question: How is a particular entity type handled org-wide by default?
  - id: update-standard-entity-rule
    intent: Change an organization sensitive data rule
    question: How do I make the org redact a type of data coming in?
  - id: list-standard-entity-rules-tool-pack
    intent: List a tool pack's sensitive data rules
    question: Which entity rules are in effect for one tool pack, including inherited defaults?
  - id: get-standard-entity-rule-tool-pack
    intent: Get a tool pack's rule for one entity type
    question: How does a specific tool pack treat a given sensitive entity type?
  - id: upsert-standard-entity-rule-override-tool-pack
    intent: Override a sensitive data rule for a tool pack
    question: How do I give one tool pack a stricter rule than the organization default?
  - id: delete-standard-entity-rule-override-tool-pack
    intent: Remove a tool pack's sensitive data override
    question: How do I revert a tool pack to the organization's default entity rule?
  phrasing_ops: 7
  slug: merge-subpackage-standardentityrules-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_syncStatus API from Merge — 8 operation(s) for subpackage_syncstatus.
  name: Merge Subpackage Sync Status API
  phrasing_intents:
  - id: list
    intent: Check accounting sync status
    question: When did the accounting data for a linked account last finish syncing?
  - id: getAtsV1SyncStatus
    intent: Check ATS sync status
    question: Is candidate and job data from the recruiting system up to date?
  - id: getSyncStatus
    intent: Check sync status from the root endpoint
    question: Is there a top-level sync status endpoint not bound to a category?
  - id: getCrmV1SyncStatus
    intent: Check CRM sync status
    question: Has the CRM finished pulling contacts and opportunities for my customer?
  - id: getFilestorageV1SyncStatus
    intent: Check file storage sync status
    question: Are files and folders from the linked drive fully synced yet?
  - id: getHrisV1SyncStatus
    intent: Check HRIS sync status
    question: Is employee data from the HR system current?
  - id: getKnowledgebaseV1SyncStatus
    intent: Check knowledge base sync status
    question: Have articles from the knowledge base finished syncing?
  - id: getTicketingV1SyncStatus
    intent: Check ticketing sync status
    question: Are tickets from the help desk fully synced right now?
  phrasing_ops: 8
  slug: merge-subpackage-syncstatus-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_tags API from Merge — 4 operation(s) for subpackage_tags.
  name: Merge Subpackage Tags API
  phrasing_intents:
  - id: list
    intent: List candidate tags from the ATS
    question: How do I get the tags recruiters use on candidates in an applicant tracking system?
  - id: getTags
    intent: List my organization's available tags
    question: Which tags are available to my organization, both global and org-scoped?
  - id: getTicketingV1Tags
    intent: List help desk ticket tags
    question: How do I pull the labels used to tag tickets in a help desk?
  - id: retrieve
    intent: Get one help desk ticket tag
    question: Can I read a single ticket tag by its id?
  phrasing_ops: 4
  slug: merge-subpackage-tags-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_tasks API from Merge — 5 operation(s) for subpackage_tasks.
  name: Merge Subpackage Tasks API
  phrasing_intents:
  - id: list
    intent: List CRM tasks
    question: Can I pull every to-do from a customer's CRM?
  - id: create
    intent: Create a CRM task
    question: How do I add a follow-up task in a customer's CRM?
  - id: retrieve
    intent: Get a CRM task
    question: Can I look up one CRM task by its ID?
  - id: meta-patch-retrieve
    intent: Get fields allowed when updating a task
    question: Which fields on a particular CRM task can be changed?
  - id: meta-post-retrieve
    intent: Get fields required to create a task
    question: Which fields are required to create a CRM task?
  - id: remote-field-classes-list
    intent: List custom field definitions on tasks
    question: What custom fields does the CRM define on tasks?
  phrasing_ops: 6
  slug: merge-subpackage-tasks-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_taxRates API from Merge — 2 operation(s) for subpackage_taxrates.
  name: Merge Subpackage Tax Rates API
  phrasing_intents:
  - id: list
    intent: List tax rates
    question: Which tax rates are configured in a customer's accounting system?
  - id: retrieve
    intent: Get a tax rate
    question: Can I look up one tax rate by ID?
  phrasing_ops: 2
  slug: merge-subpackage-taxrates-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_teams API from Merge — 2 operation(s) for subpackage_teams.
  name: Merge Subpackage Teams API
  phrasing_intents:
  - id: list
    intent: List ticketing teams
    question: Which support teams exist in a customer's ticketing system?
  - id: retrieve
    intent: Get a ticketing team
    question: What's the name and description of a specific support team?
  phrasing_ops: 2
  slug: merge-subpackage-teams-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_tickets API from Merge — 7 operation(s) for subpackage_tickets.
  name: Merge Subpackage Tickets API
  phrasing_intents:
  - id: list
    intent: List tickets
    question: How do I pull all open tickets from a customer's helpdesk?
  - id: create
    intent: Create a ticket
    question: Can I open a new ticket in a customer's helpdesk through one API?
  - id: retrieve
    intent: Get a ticket
    question: Can I fetch the full details of one ticket by its ID?
  - id: partial-update
    intent: Update a ticket
    question: Can I change the status or assignee on an existing ticket?
  - id: viewers-list
    intent: List who can view a ticket
    question: Who are the users and teams that can see a particular ticket?
  - id: live-search-list
    intent: Search tickets live in the helpdesk
    question: Can I search tickets directly in the third-party helpdesk instead of synced data?
  - id: meta-patch-retrieve
    intent: Get fields allowed when updating a ticket
    question: Which ticket fields can I change when updating a specific ticket?
  - id: meta-post-retrieve
    intent: Get fields required to create a ticket
    question: Which fields are required to create a ticket in this helpdesk?
  phrasing_ops: 9
  slug: merge-subpackage-tickets-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_timeOff API from Merge — 3 operation(s) for subpackage_timeoff.
  name: Merge Subpackage Time Off API
  phrasing_intents:
  - id: list
    intent: List time off requests
    question: Who has approved time off next week?
  - id: create
    intent: Request time off
    question: How do I submit a leave request into a customer's HR system?
  - id: retrieve
    intent: Get a time off request
    question: What are the dates and status of one time off request?
  - id: meta-post-retrieve
    intent: See which fields a time off request needs
    question: What fields must a time off request include for this HR platform?
  phrasing_ops: 4
  slug: merge-subpackage-timeoff-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_timeOffBalances API from Merge — 2 operation(s) for subpackage_timeoffbalances.
  name: Merge Subpackage Time Off Balances API
  phrasing_intents:
  - id: list
    intent: List employee time off balances
    question: How much vacation or sick time does each employee have left in the HR system?
  - id: retrieve
    intent: Get one time off balance
    question: Can I read a single time off balance record by id?
  phrasing_ops: 2
  slug: merge-subpackage-timeoffbalances-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_timesheetEntries API from Merge — 3 operation(s) for subpackage_timesheetentries.
  name: Merge Subpackage Timesheet Entries API
  phrasing_intents:
  - id: list
    intent: List employees' timesheet entries
    question: How do I pull all timesheet entries synced from a customer's HRIS?
  - id: create
    intent: Record a timesheet entry
    question: How do I log hours worked for an employee in the HRIS?
  - id: retrieve
    intent: Get a timesheet entry
    question: Can I look up one timesheet entry by ID?
  - id: meta-post-retrieve
    intent: Get fields required to record a timesheet entry
    question: Which fields must I send to create a timesheet entry?
  phrasing_ops: 4
  slug: merge-subpackage-timesheetentries-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_toolDescriptionOverrides API from Merge — 2 operation(s) for subpackage_tooldescriptionoverrides.
  name: Merge Subpackage Tool Description Overrides API
  phrasing_intents:
  - id: list
    intent: List organization tool description overrides
    question: Which connector tool descriptions have we customized across the organization?
  - id: bulk-upsert-delete
    intent: Bulk set or remove org tool descriptions
    question: Can I rewrite the descriptions agents see for several connector tools in one call?
  - id: list-tool-pack
    intent: List a tool pack's tool description overrides
    question: Which tool descriptions are overridden inside one specific tool pack?
  - id: bulk-upsert-delete-tool-pack
    intent: Bulk set or remove a tool pack's tool descriptions
    question: Can I customize tool descriptions for just one tool pack instead of the whole org?
  phrasing_ops: 4
  slug: merge-subpackage-tooldescriptionoverrides-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_toolPacks API from Merge — 4 operation(s) for subpackage_toolpacks.
  name: Merge Subpackage Tool Packs API
  phrasing_intents:
  - id: list
    intent: List tool packs
    question: Which tool packs have I set up?
  - id: create
    intent: Create a tool pack
    question: How do I bundle several connectors into a new tool pack?
  - id: retrieve
    intent: Get a tool pack
    question: Where can I see a single tool pack's settings?
  - id: destroy
    intent: Delete a tool pack
    question: Can I permanently remove a tool pack I no longer use?
  - id: partial-update
    intent: Update a tool pack
    question: How do I rename a tool pack or change its description?
  - id: list-connectors
    intent: List connectors in a tool pack
    question: Which connectors are attached to a tool pack, and which tools are on?
  - id: replace-connectors
    intent: Replace a tool pack's connector list
    question: How do I set a tool pack's connectors to exactly a new list?
  - id: bulk-upsert-delete-connectors
    intent: Add or adjust some connectors in a tool pack
    question: Can I add a connector to a tool pack without touching the others?
  phrasing_ops: 9
  slug: merge-subpackage-toolpacks-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_toolSearch API from Merge — 1 operation(s) for subpackage_toolsearch.
  name: Merge Subpackage Tool Search API
  phrasing_intents:
  - id: search-tools
    intent: Find tools that match what a user wants to do
    question: Which tools in a tool pack fit what my user is trying to accomplish?
  phrasing_ops: 1
  slug: merge-subpackage-toolsearch-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_trackingCategories API from Merge — 2 operation(s) for subpackage_trackingcategories.
  name: Merge Subpackage Tracking Categories API
  phrasing_intents:
  - id: list
    intent: List tracking categories
    question: What classes, departments or locations are used as tracking categories?
  - id: retrieve
    intent: Get a tracking category
    question: How do I look up a single tracking category by ID?
  phrasing_ops: 2
  slug: merge-subpackage-trackingcategories-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_transactions API from Merge — 2 operation(s) for subpackage_transactions.
  name: Merge Subpackage Transactions API
  phrasing_intents:
  - id: list
    intent: List accounting transactions
    question: Can I pull ledger transactions from a customer's accounting system?
  - id: retrieve
    intent: Get an accounting transaction
    question: Can I look up one transaction by its ID?
  phrasing_ops: 2
  slug: merge-subpackage-transactions-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_users API from Merge — 14 operation(s) for subpackage_users.
  name: Merge Subpackage Users API
  phrasing_intents:
  - id: list
    intent: List recruiting system users
    question: How do I see every recruiter and hiring manager account in a linked ATS?
  - id: retrieve
    intent: Get a recruiting system user
    question: What details does the ATS hold about one specific recruiter?
  - id: getUsers
    intent: List chat workspace users
    question: Who are the members of a connected messaging workspace?
  - id: getUsersById
    intent: Get a chat workspace user
    question: How do I look up one person in a linked chat workspace?
  - id: getCrmV1Users
    intent: List CRM users
    question: Which sales reps have logins in the connected CRM?
  - id: getCrmV1UsersById
    intent: Get a CRM user
    question: How do I retrieve one CRM user's record?
  - id: ignore-create
    intent: Stop syncing a CRM user
    question: How do I exclude a CRM user from future syncs?
  - id: remote-field-classes-list
    intent: List custom field definitions for CRM users
    question: What custom fields exist on users in the connected CRM?
  phrasing_ops: 14
  slug: merge-subpackage-users-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_vendorCredits API from Merge — 5 operation(s) for subpackage_vendorcredits.
  name: Merge Subpackage Vendor Credits API
  phrasing_intents:
  - id: list
    intent: List vendor credits
    question: Can I see all credits my suppliers have issued in a connected accounting system?
  - id: create
    intent: Create a vendor credit
    question: How do I record a credit from a supplier in a customer's books?
  - id: retrieve
    intent: Get a vendor credit
    question: What's the total and vendor on a specific vendor credit?
  - id: partial-update
    intent: Update a vendor credit
    question: Can I edit a vendor credit that's already in the books?
  - id: application-create
    intent: Apply a vendor credit to an invoice
    question: Can I use a supplier's credit to reduce a bill I owe them?
  - id: meta-patch-retrieve
    intent: Get editable fields for a vendor credit
    question: Which fields of an existing vendor credit can the integration update?
  - id: meta-post-retrieve
    intent: Get fields for creating vendor credits
    question: Which fields are required to create a vendor credit in an integration?
  phrasing_ops: 7
  slug: merge-subpackage-vendorcredits-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The subpackage_vendors API from Merge — 2 operation(s) for subpackage_vendors.
  name: Merge Subpackage Vendors API
  phrasing_intents:
  - id: list
    intent: List execution vendors and their models
    question: Which execution vendors are available and what models does each serve?
  - id: retrieve
    intent: Get an execution vendor
    question: What models is a specific execution vendor currently serving?
  phrasing_ops: 2
  slug: merge-subpackage-vendors-api
- baseURL: https://api.merge.dev/api/hris/v1
  baseurl_source: declared
  description: The Hris API from Merge — 4 operation(s) for hris.
  name: Merge Hris API
  phrasing_intents:
  - id: field-mappings-create
    intent: Create an HRIS field mapping
    question: Can I map a custom field from a customer's HR system onto the Employee model?
  - id: field-mappings-destroy
    intent: Delete an HRIS field mapping
    question: What happens to already-synced data when I remove a field mapping?
  - id: field-mappings-partial-update
    intent: Update an HRIS field mapping
    question: Can I point an existing field mapping at a different remote field path?
  - id: remote-fields-retrieve
    intent: List remote fields available for mapping
    question: Which third-party fields in a customer's HR system can I map or override?
  - id: target-fields-retrieve
    intent: List organization-wide HRIS target fields
    question: What organization-wide target fields have been added to the HR Common Models?
  phrasing_ops: 5
  slug: merge-hris-api
arazzos:
- description: Submit a batch of expenses asynchronously, then poll the batch until it finishes and branch on the final status.
  name: Merge Accounting Bulk Create Expenses and Poll the Batch
  slug: merge-accounting-bulk-create-expenses-poll-workflow
- description: Create a customer contact, raise an invoice against that contact, and confirm the invoice.
  name: Merge Accounting Bill a Customer
  slug: merge-accounting-create-contact-and-invoice-workflow
- description: Create a Merge Link token for the Accounting category, exchange the public token for an account token, and confirm the linked accounting platform.
  name: Merge Accounting Link an Account
  slug: merge-accounting-link-account-workflow
- description: Find a candidate's application, resolve a target interview stage for its job, and move the application into that stage.
  name: Merge ATS Advance an Application Stage
  slug: merge-ats-advance-application-stage-workflow
- description: Create a candidate, resolve an open job, and submit an application linking the candidate to that job.
  name: Merge ATS Add a Candidate and Application
  slug: merge-ats-create-candidate-and-application-workflow
- description: Create a Merge Link token for the ATS category, exchange the public token for an account token, and confirm the linked applicant tracking system.
  name: Merge ATS Link an Account
  slug: merge-ats-link-account-workflow
- description: Create a CRM account, attach a primary contact to it, and confirm the contact was written.
  name: Merge CRM Create an Account with a Contact
  slug: merge-crm-create-account-and-contact-workflow
- description: Resolve a pipeline stage and an account, then create an opportunity placed at that stage on that account.
  name: Merge CRM Open an Opportunity
  slug: merge-crm-create-opportunity-workflow
- description: Create a Merge Link token for the CRM category, exchange the public token for an account token, and confirm the linked CRM.
  name: Merge CRM Link an Account
  slug: merge-crm-link-account-workflow
- description: Resolve a contact by email, log an engagement against that contact, and confirm the engagement.
  name: Merge CRM Log an Engagement on a Contact
  slug: merge-crm-log-engagement-workflow
- description: Read sync status and open issues for both an HRIS and a CRM linked account in a single monitoring pass.
  name: Merge Cross-Category Sync Health Check
  slug: merge-cross-category-sync-health-check-workflow
- description: List files in a linked file storage account, read the first file's metadata, and download its contents.
  name: Merge File Storage Browse and Download a File
  slug: merge-filestorage-browse-and-download-workflow
- description: Create a Merge Link token for the File Storage category, exchange the public token for an account token, and confirm the linked file storage provider.
  name: Merge File Storage Link an Account
  slug: merge-filestorage-link-account-workflow
- description: Resolve an employee on a linked HRIS account and submit a time off request on their behalf.
  name: Merge HRIS Submit a Time Off Request
  slug: merge-hris-create-time-off-workflow
- description: Create a Merge Link token, exchange the returned public token for an account token, and confirm the linked HRIS account.
  name: Merge HRIS Link an Account
  slug: merge-hris-link-account-workflow
- description: List employees from a linked HRIS account, then read each employee's record and time off requests.
  name: Merge HRIS Employee Directory with Time Off
  slug: merge-hris-list-employees-and-time-off-workflow
- description: Exchange a public token for an account token, list knowledge base containers, and list the articles within the first container.
  name: Merge Knowledge Base Link and Browse Articles
  slug: merge-knowledgebase-link-and-browse-workflow
- description: Create a ticket on a linked ticketing system, add an opening comment to it, and confirm the ticket.
  name: Merge Ticketing Open a Ticket with a First Comment
  slug: merge-ticketing-create-ticket-with-comment-workflow
- description: Create a Merge Link token for the Ticketing category, exchange the public token for an account token, and confirm the linked ticketing system.
  name: Merge Ticketing Link an Account
  slug: merge-ticketing-link-account-workflow
artifact_total: 1384
collections:
- collection_type: postman
  name: Accounting
  slug: postman-merge-accounting-api
- collection_type: postman
  name: Agent Handler
  slug: postman-merge-agent-handler-api
- collection_type: postman
  name: ATS
  slug: postman-merge-ats-api
- collection_type: postman
  name: Chat
  slug: postman-merge-chat-api
- collection_type: postman
  name: CRM
  slug: postman-merge-crm-api
- collection_type: postman
  name: File Storage
  slug: postman-merge-file-storage-api
- collection_type: postman
  name: API Overview
  slug: postman-merge-gateway-api
- collection_type: postman
  name: HRIS
  slug: postman-merge-hris-api
- collection_type: postman
  name: Knowledge Base
  slug: postman-merge-knowledge-base-api
- collection_type: postman
  name: Ticketing
  slug: postman-merge-ticketing-api
- collection_type: open
  name: Accounting  API
  slug: open-merge-default-api
- collection_type: open
  name: Accounting subpackage_accessKeys API
  slug: open-merge-subpackage-accesskeys-api
- collection_type: open
  name: Accounting subpackage_accountDetails API
  slug: open-merge-subpackage-accountdetails-api
- collection_type: open
  name: Accounting subpackage_accountingPeriods API
  slug: open-merge-subpackage-accountingperiods-api
- collection_type: open
  name: Accounting subpackage_accounts API
  slug: open-merge-subpackage-accounts-api
- collection_type: open
  name: Accounting subpackage_accountToken API
  slug: open-merge-subpackage-accounttoken-api
- collection_type: open
  name: Accounting subpackage_activities API
  slug: open-merge-subpackage-activities-api
- collection_type: open
  name: Accounting subpackage_addresses API
  slug: open-merge-subpackage-addresses-api
- collection_type: open
  name: Accounting subpackage_applicationCredentials API
  slug: open-merge-subpackage-applicationcredentials-api
- collection_type: open
  name: Accounting subpackage_applications API
  slug: open-merge-subpackage-applications-api
- collection_type: open
  name: Accounting subpackage_articles API
  slug: open-merge-subpackage-articles-api
- collection_type: open
  name: Accounting subpackage_associations API
  slug: open-merge-subpackage-associations-api
- collection_type: open
  name: Accounting subpackage_associationTypes API
  slug: open-merge-subpackage-associationtypes-api
- collection_type: open
  name: Accounting subpackage_asyncPassthrough API
  slug: open-merge-subpackage-asyncpassthrough-api
- collection_type: open
  name: Accounting subpackage_asyncTasks API
  slug: open-merge-subpackage-asynctasks-api
- collection_type: open
  name: Accounting subpackage_attachments API
  slug: open-merge-subpackage-attachments-api
- collection_type: open
  name: Accounting subpackage_auditLog API
  slug: open-merge-subpackage-auditlog-api
- collection_type: open
  name: Accounting subpackage_auditTrail API
  slug: open-merge-subpackage-audittrail-api
- collection_type: open
  name: Accounting subpackage_availableActions API
  slug: open-merge-subpackage-availableactions-api
- collection_type: open
  name: Accounting subpackage_balanceSheets API
  slug: open-merge-subpackage-balancesheets-api
- collection_type: open
  name: Accounting subpackage_bankFeedAccounts API
  slug: open-merge-subpackage-bankfeedaccounts-api
- collection_type: open
  name: Accounting subpackage_bankFeedTransactions API
  slug: open-merge-subpackage-bankfeedtransactions-api
- collection_type: open
  name: Accounting subpackage_bankInfo API
  slug: open-merge-subpackage-bankinfo-api
- collection_type: open
  name: Accounting subpackage_benefits API
  slug: open-merge-subpackage-benefits-api
- collection_type: open
  name: Accounting subpackage_candidates API
  slug: open-merge-subpackage-candidates-api
- collection_type: open
  name: Accounting subpackage_cashFlowStatements API
  slug: open-merge-subpackage-cashflowstatements-api
- collection_type: open
  name: Accounting subpackage_collections API
  slug: open-merge-subpackage-collections-api
- collection_type: open
  name: Accounting subpackage_comments API
  slug: open-merge-subpackage-comments-api
- collection_type: open
  name: Accounting subpackage_companies API
  slug: open-merge-subpackage-companies-api
- collection_type: open
  name: Accounting subpackage_companyInfo API
  slug: open-merge-subpackage-companyinfo-api
- collection_type: open
  name: Accounting subpackage_connectors API
  slug: open-merge-subpackage-connectors-api
- collection_type: open
  name: Accounting subpackage_contacts API
  slug: open-merge-subpackage-contacts-api
- collection_type: open
  name: Accounting subpackage_containers API
  slug: open-merge-subpackage-containers-api
- collection_type: open
  name: Accounting subpackage_conversations API
  slug: open-merge-subpackage-conversations-api
- collection_type: open
  name: Accounting subpackage_credentials API
  slug: open-merge-subpackage-credentials-api
- collection_type: open
  name: Accounting subpackage_creditNotes API
  slug: open-merge-subpackage-creditnotes-api
- collection_type: open
  name: Accounting subpackage_customObjectClasses API
  slug: open-merge-subpackage-customobjectclasses-api
- collection_type: open
  name: Accounting subpackage_customObjects API
  slug: open-merge-subpackage-customobjects-api
- collection_type: open
  name: Accounting subpackage_customRegexRules API
  slug: open-merge-subpackage-customregexrules-api
- collection_type: open
  name: Accounting subpackage_deleteAccount API
  slug: open-merge-subpackage-deleteaccount-api
- collection_type: open
  name: Accounting subpackage_departments API
  slug: open-merge-subpackage-departments-api
- collection_type: open
  name: Accounting subpackage_dependents API
  slug: open-merge-subpackage-dependents-api
- collection_type: open
  name: Accounting subpackage_drives API
  slug: open-merge-subpackage-drives-api
- collection_type: open
  name: Accounting subpackage_eeocs API
  slug: open-merge-subpackage-eeocs-api
- collection_type: open
  name: Accounting subpackage_embeddings API
  slug: open-merge-subpackage-embeddings-api
- collection_type: open
  name: Accounting subpackage_employeePayrollRuns API
  slug: open-merge-subpackage-employeepayrollruns-api
- collection_type: open
  name: Accounting subpackage_employees API
  slug: open-merge-subpackage-employees-api
- collection_type: open
  name: Accounting subpackage_employerBenefits API
  slug: open-merge-subpackage-employerbenefits-api
- collection_type: open
  name: Accounting subpackage_employments API
  slug: open-merge-subpackage-employments-api
- collection_type: open
  name: Accounting subpackage_engagements API
  slug: open-merge-subpackage-engagements-api
- collection_type: open
  name: Accounting subpackage_engagementTypes API
  slug: open-merge-subpackage-engagementtypes-api
- collection_type: open
  name: Accounting subpackage_expenseReports API
  slug: open-merge-subpackage-expensereports-api
- collection_type: open
  name: Accounting subpackage_expenses API
  slug: open-merge-subpackage-expenses-api
- collection_type: open
  name: Accounting subpackage_fieldMapping API
  slug: open-merge-subpackage-fieldmapping-api
- collection_type: open
  name: Accounting subpackage_files API
  slug: open-merge-subpackage-files-api
- collection_type: open
  name: Accounting subpackage_folders API
  slug: open-merge-subpackage-folders-api
- collection_type: open
  name: Accounting subpackage_forceResync API
  slug: open-merge-subpackage-forceresync-api
- collection_type: open
  name: Accounting subpackage_generateKey API
  slug: open-merge-subpackage-generatekey-api
- collection_type: open
  name: Accounting subpackage_groups API
  slug: open-merge-subpackage-groups-api
- collection_type: open
  name: Accounting subpackage_incomeStatements API
  slug: open-merge-subpackage-incomestatements-api
- collection_type: open
  name: Accounting subpackage_interviews API
  slug: open-merge-subpackage-interviews-api
- collection_type: open
  name: Accounting subpackage_invoices API
  slug: open-merge-subpackage-invoices-api
- collection_type: open
  name: Accounting subpackage_issues API
  slug: open-merge-subpackage-issues-api
- collection_type: open
  name: Accounting subpackage_itemFulfillments API
  slug: open-merge-subpackage-itemfulfillments-api
- collection_type: open
  name: Accounting subpackage_items API
  slug: open-merge-subpackage-items-api
- collection_type: open
  name: Accounting subpackage_jobInterviewStages API
  slug: open-merge-subpackage-jobinterviewstages-api
- collection_type: open
  name: Accounting subpackage_jobPostings API
  slug: open-merge-subpackage-jobpostings-api
- collection_type: open
  name: Accounting subpackage_jobs API
  slug: open-merge-subpackage-jobs-api
- collection_type: open
  name: Accounting subpackage_journalEntries API
  slug: open-merge-subpackage-journalentries-api
- collection_type: open
  name: Accounting subpackage_leads API
  slug: open-merge-subpackage-leads-api
- collection_type: open
  name: Accounting subpackage_linkedAccounts API
  slug: open-merge-subpackage-linkedaccounts-api
- collection_type: open
  name: Accounting subpackage_linkToken API
  slug: open-merge-subpackage-linktoken-api
- collection_type: open
  name: Accounting subpackage_locations API
  slug: open-merge-subpackage-locations-api
- collection_type: open
  name: Accounting subpackage_mcp API
  slug: open-merge-subpackage-mcp-api
- collection_type: open
  name: Accounting subpackage_messages API
  slug: open-merge-subpackage-messages-api
- collection_type: open
  name: Accounting subpackage_models API
  slug: open-merge-subpackage-models-api
- collection_type: open
  name: Accounting subpackage_notes API
  slug: open-merge-subpackage-notes-api
- collection_type: open
  name: Accounting subpackage_offers API
  slug: open-merge-subpackage-offers-api
- collection_type: open
  name: Accounting subpackage_offices API
  slug: open-merge-subpackage-offices-api
- collection_type: open
  name: Accounting subpackage_opportunities API
  slug: open-merge-subpackage-opportunities-api
- collection_type: open
  name: Accounting subpackage_passthrough API
  slug: open-merge-subpackage-passthrough-api
- collection_type: open
  name: Accounting subpackage_payGroups API
  slug: open-merge-subpackage-paygroups-api
- collection_type: open
  name: Accounting subpackage_paymentMethods API
  slug: open-merge-subpackage-paymentmethods-api
- collection_type: open
  name: Accounting subpackage_payments API
  slug: open-merge-subpackage-payments-api
- collection_type: open
  name: Accounting subpackage_paymentTerms API
  slug: open-merge-subpackage-paymentterms-api
- collection_type: open
  name: Accounting subpackage_payrollRuns API
  slug: open-merge-subpackage-payrollruns-api
- collection_type: open
  name: Accounting subpackage_phoneNumbers API
  slug: open-merge-subpackage-phonenumbers-api
- collection_type: open
  name: Accounting subpackage_projects API
  slug: open-merge-subpackage-projects-api
- collection_type: open
  name: Accounting subpackage_purchaseOrders API
  slug: open-merge-subpackage-purchaseorders-api
- collection_type: open
  name: Accounting subpackage_regenerateKey API
  slug: open-merge-subpackage-regeneratekey-api
- collection_type: open
  name: Accounting subpackage_registeredUsers API
  slug: open-merge-subpackage-registeredusers-api
- collection_type: open
  name: Accounting subpackage_rejectReasons API
  slug: open-merge-subpackage-rejectreasons-api
- collection_type: open
  name: Accounting subpackage_responses API
  slug: open-merge-subpackage-responses-api
- collection_type: open
  name: Accounting subpackage_roles API
  slug: open-merge-subpackage-roles-api
- collection_type: open
  name: Accounting subpackage_routing API
  slug: open-merge-subpackage-routing-api
- collection_type: open
  name: Accounting subpackage_salesOrders API
  slug: open-merge-subpackage-salesorders-api
- collection_type: open
  name: Accounting subpackage_scopes API
  slug: open-merge-subpackage-scopes-api
- collection_type: open
  name: Accounting subpackage_scorecards API
  slug: open-merge-subpackage-scorecards-api
- collection_type: open
  name: Accounting subpackage_stages API
  slug: open-merge-subpackage-stages-api
- collection_type: open
  name: Accounting subpackage_standardEntityRules API
  slug: open-merge-subpackage-standardentityrules-api
- collection_type: open
  name: Accounting subpackage_syncStatus API
  slug: open-merge-subpackage-syncstatus-api
- collection_type: open
  name: Accounting subpackage_tags API
  slug: open-merge-subpackage-tags-api
- collection_type: open
  name: Accounting subpackage_tasks API
  slug: open-merge-subpackage-tasks-api
- collection_type: open
  name: Accounting subpackage_taxRates API
  slug: open-merge-subpackage-taxrates-api
- collection_type: open
  name: Accounting subpackage_teams API
  slug: open-merge-subpackage-teams-api
- collection_type: open
  name: Accounting subpackage_tickets API
  slug: open-merge-subpackage-tickets-api
- collection_type: open
  name: Accounting subpackage_timeOff API
  slug: open-merge-subpackage-timeoff-api
- collection_type: open
  name: Accounting subpackage_timeOffBalances API
  slug: open-merge-subpackage-timeoffbalances-api
- collection_type: open
  name: Accounting subpackage_timesheetEntries API
  slug: open-merge-subpackage-timesheetentries-api
- collection_type: open
  name: Accounting subpackage_toolDescriptionOverrides API
  slug: open-merge-subpackage-tooldescriptionoverrides-api
- collection_type: open
  name: Accounting subpackage_toolPacks API
  slug: open-merge-subpackage-toolpacks-api
- collection_type: open
  name: Accounting subpackage_toolSearch API
  slug: open-merge-subpackage-toolsearch-api
- collection_type: open
  name: Accounting subpackage_trackingCategories API
  slug: open-merge-subpackage-trackingcategories-api
- collection_type: open
  name: Accounting subpackage_transactions API
  slug: open-merge-subpackage-transactions-api
- collection_type: open
  name: Accounting subpackage_users API
  slug: open-merge-subpackage-users-api
- collection_type: open
  name: Accounting subpackage_vendorCredits API
  slug: open-merge-subpackage-vendorcredits-api
- collection_type: open
  name: Accounting subpackage_vendors API
  slug: open-merge-subpackage-vendors-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.merge.dev/pricing/unified
- group: other
  href: https://artifacts.apis.io/merge/capabilities/merge-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/merge-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/merge/agentic-access/merge-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/merge-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/merge/security/merge-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/merge-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/merge/security/merge-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/merge-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/merge/security/merge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/merge-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/merge/authentication/merge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/merge-authentication.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-accounting-bulk-create-expenses-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-accounting-bulk-create-expenses-poll-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-accounting-create-contact-and-invoice-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-accounting-create-contact-and-invoice-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-accounting-link-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-accounting-link-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-ats-advance-application-stage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-ats-advance-application-stage-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-ats-create-candidate-and-application-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-ats-create-candidate-and-application-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-ats-link-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-ats-link-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-crm-create-account-and-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-crm-create-account-and-contact-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-crm-create-opportunity-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-crm-create-opportunity-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-crm-link-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-crm-link-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-crm-log-engagement-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-crm-log-engagement-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-cross-category-sync-health-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-cross-category-sync-health-check-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-filestorage-browse-and-download-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-filestorage-browse-and-download-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-filestorage-link-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-filestorage-link-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-hris-create-time-off-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-hris-create-time-off-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-hris-link-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-hris-link-account-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-hris-list-employees-and-time-off-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-hris-list-employees-and-time-off-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-knowledgebase-link-and-browse-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-knowledgebase-link-and-browse-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-ticketing-create-ticket-with-comment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-ticketing-create-ticket-with-comment-workflow.yml
- group: design
  href: https://artifacts.apis.io/merge/arazzo/merge-ticketing-link-account-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/merge-ticketing-link-account-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/merge-api
- group: company
  title: ''
  type: Website
  url: https://www.merge.dev/
- group: auth
  title: ''
  type: Security
  url: https://www.merge.dev/security
- group: other
  title: ''
  type: Customers
  url: https://www.merge.dev/case-studies
- group: company
  title: ''
  type: Blog
  url: https://www.merge.dev/blog
- group: other
  title: ''
  type: eBooks
  url: https://www.merge.dev/resources?content-type=Ebooks
- group: operate
  title: ''
  type: Support
  url: https://help.merge.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.merge.dev/changelog
- group: learn
  title: ''
  type: Webinars
  url: https://www.merge.dev/resources?content-type=Webinars
- group: commercial
  title: ''
  type: Pricing
  url: https://www.merge.dev/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.merge.dev/
- group: other
  title: ''
  type: APICatalog
  url: https://docs.merge.dev/.well-known/api-catalog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.merge.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.merge.dev/legal/privacy-policy
- group: auth
  title: ''
  type: GDPR
  url: https://www.merge.dev/eu
- group: start
  title: ''
  type: Login
  url: https://app.merge.dev/login
- group: start
  title: ''
  type: Signup
  url: https://app.merge.dev/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.merge.dev/
- group: auth
  title: ''
  type: Trust
  url: https://trust.merge.dev/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/merge-api
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/merge-api/merge-python-client
- group: build
  title: ''
  type: NodeSDK
  url: https://github.com/merge-api/merge-node-client
- group: build
  title: ''
  type: GoSDK
  url: https://github.com/merge-api/merge-go-client
- group: build
  title: ''
  type: JavaSDK
  url: https://github.com/merge-api/merge-java-client
- group: build
  title: ''
  type: RubySDK
  url: https://github.com/merge-api/merge-ruby-client
- group: build
  title: ''
  type: CSharpSDK
  url: https://github.com/merge-api/merge-csharp-client
- group: build
  title: ''
  type: KotlinSDK
  url: https://github.com/merge-api/merge-sdk-kotlin
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/merge-api/merge-mcp
- group: agent
  title: ''
  type: ClaudeSkills
  url: https://github.com/merge-api/merge-unified-skills
- group: agent
  title: ''
  type: ClaudeSkills
  url: https://github.com/merge-api/merge-gateway-skills
- group: build
  title: ''
  type: VercelAISDK
  url: https://github.com/merge-api/merge-gateway-ai-sdk-provider
- group: build
  title: ''
  type: AgentPlugins
  url: https://github.com/merge-api/ah-plugins
- group: design
  title: ''
  type: ReactComponent
  url: https://github.com/merge-api/react-merge-link
- group: design
  title: ''
  type: ReactComponent
  url: https://github.com/merge-api/react-agent-handler-link
- group: design
  title: ''
  type: ReactComponent
  url: https://github.com/merge-api/react-agent-handler-chat
- group: build
  title: ''
  type: SampleApp
  url: https://github.com/merge-api/agent-handler-chat-demo
- group: design
  title: ''
  type: WorkflowIntegration
  url: https://github.com/merge-api/n8n-nodes-merge
- group: design
  title: ''
  type: VueComponent
  url: https://github.com/merge-api/vue-merge-link
- group: build
  title: ''
  type: SDKs
  url: https://docs.merge.dev/sdk/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/mergeapi/workspace/merge-public-workspace/overview
- group: build
  title: ''
  type: IntegrationDirectory
  url: https://www.merge.dev/integrations
- group: build
  title: ''
  type: DeveloperTools
  url: https://www.merge.dev/features/developer-tools
- group: other
  title: ''
  type: Observability
  url: https://www.merge.dev/features/integration-observability
- group: build
  title: ''
  type: IntegrationManagement
  url: https://www.merge.dev/features/integrations-management
- group: auth
  title: ''
  type: Authentication
  url: https://docs.merge.dev/basics/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.merge.dev/guides/testing-via-postman/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.merge.dev/get-started/unified-api/
- group: design
  href: https://artifacts.apis.io/merge/rules/merge-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/merge-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/merge/vocabulary/merge-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/merge-vocabulary.yaml
- group: commercial
  href: https://artifacts.apis.io/merge/plans/merge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/merge-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/merge/rate-limits/merge-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/merge-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/merge/finops/merge-finops.yml
  title: ''
  type: FinOps
  url: finops/merge-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.merge.dev/llms.txt
created: '2025-06-05'
description: Merge is the connective infrastructure for production AI. The Merge Unified API offers one API surface across HRIS, ATS, Accounting, CRM, Ticketing, File Storage, Knowledge Base, and Chat. Merge Agent Handler exposes pre-built enterprise connectors to AI agents via REST + MCP. Merge Gateway provides a unified LLM API across OpenAI, Anthropic, Google, Mistral, Cohere, and xAI with routing, caching, and observability.
examples:
- key_count: 18
  name: Accounting Api Invoice Example
  slug: accounting-api-invoice-example
- key_count: 10
  name: Agent Handler Tool Pack Example
  slug: agent-handler-tool-pack-example
- key_count: 13
  name: Ats Api Application Example
  slug: ats-api-application-example
- key_count: 16
  name: Ats Api Candidate Example
  slug: ats-api-candidate-example
- key_count: 13
  name: Chat Api Message Example
  slug: chat-api-message-example
- key_count: 14
  name: Crm Api Opportunity Example
  slug: crm-api-opportunity-example
- key_count: 13
  name: File Storage Api File Example
  slug: file-storage-api-file-example
- key_count: 8
  name: Gateway Response Example
  slug: gateway-response-example
- key_count: 21
  name: Hris Api Employee Example
  slug: hris-api-employee-example
- key_count: 11
  name: Knowledge Base Api Article Example
  slug: knowledge-base-api-article-example
- key_count: 19
  name: Ticketing Api Ticket Example
  slug: ticketing-api-ticket-example
features:
- 'Launch: 3 free production accounts; $650/mo for up to 10; $65 per additional account; 100 req/min'
- 'Professional: contract pricing, custom fields, field-level scopes, 400 req/min, 30-day log retention'
- 'Enterprise: 600 req/min, audit trail, 90+ day log retention, dedicated CSM and Slack channel'
- 'Gateway BYOK: $0.05 per million tokens routed'
- 'Agent Handler: consumption-based after free tier'
- 200+ unified integrations across HRIS, ATS, CRM, Accounting, Ticketing, File Storage, Knowledge Base, Chat
- Unified Schema (read + write) with Field Mappings for custom fields
- Merge Link UI and Magic Link (no-code) for end-customer authorization
- 'Sync frequencies: 1, 3, 6, 12, 24 hours (Pro+)'
- Webhooks for record changes
- Bearer token + X-Account-Token header authentication
- Three regional API hosts (US, EU, APAC)
- 60-day or unlimited sandbox access
- SOC 2 Type 2, ISO 27001, GDPR, HIPAA-ready
- Agent Handler MCP server surface for AI agents
- Gateway intelligent routing across OpenAI, Anthropic, Google, Mistral, Cohere, xAI
finops:
- has_sources: true
  method: derived
  name: Merge Finops
  primary_unit: linked account
  service_category: ''
  slug: merge-finops
  template: false
image: /assets/icons/merge.png
json_schemas:
- name: Invoice
  property_count: 18
  slug: accounting-api-invoice
- name: ToolPack
  property_count: 10
  slug: agent-handler-tool-pack
- name: Application
  property_count: 13
  slug: ats-api-application
- name: Candidate
  property_count: 16
  slug: ats-api-candidate
- name: Message
  property_count: 13
  slug: chat-api-message
- name: Opportunity
  property_count: 14
  slug: crm-api-opportunity
- name: File
  property_count: 13
  slug: file-storage-api-file
- name: GatewayResponse
  property_count: 8
  slug: gateway-response
- name: Employee
  property_count: 21
  slug: hris-api-employee
- name: Article
  property_count: 11
  slug: knowledge-base-api-article
- name: AccessKey
  property_count: 9
  slug: merge-accesskey
- name: AccessKeyCreate
  property_count: 11
  slug: merge-accesskeycreate
- name: AccessRoleEnum
  property_count: 0
  slug: merge-accessroleenum
- name: Account
  property_count: 18
  slug: merge-account
- name: AccountAccountTypeEnum
  property_count: 0
  slug: merge-accountaccounttypeenum
- name: AccountDetails
  property_count: 14
  slug: merge-accountdetails
- name: AccountDetailsAndActions
  property_count: 14
  slug: merge-accountdetailsandactions
- name: AccountDetailsAndActionsIntegration
  property_count: 8
  slug: merge-accountdetailsandactionsintegration
- name: AccountDetailsAndActionsStatusEnum
  property_count: 0
  slug: merge-accountdetailsandactionsstatusenum
- name: AccountEndpointRequest
  property_count: 1
  slug: merge-accountendpointrequest
- name: AccountFieldMappings
  property_count: 2
  slug: merge-accountfieldmappings
- name: AccountingAttachment
  property_count: 10
  slug: merge-accountingattachment
- name: AccountingAttachmentEndpointRequest
  property_count: 1
  slug: merge-accountingattachmentendpointrequest
- name: AccountingAttachmentFieldMappings
  property_count: 2
  slug: merge-accountingattachmentfieldmappings
- name: AccountingAttachmentRequest
  property_count: 5
  slug: merge-accountingattachmentrequest
- name: AccountingAttachmentResponse
  property_count: 4
  slug: merge-accountingattachmentresponse
- name: AccountingPeriod
  property_count: 10
  slug: merge-accountingperiod
- name: AccountingPeriodFieldMappings
  property_count: 2
  slug: merge-accountingperiodfieldmappings
- name: AccountingPhoneNumber
  property_count: 4
  slug: merge-accountingphonenumber
- name: AccountingPhoneNumberRequest
  property_count: 4
  slug: merge-accountingphonenumberrequest
- name: AccountIntegration
  property_count: 10
  slug: merge-accountintegration
- name: AccountIntegrationCategoryBetaStatus
  property_count: 0
  slug: merge-accountintegrationcategorybetastatus
- name: AccountRequest
  property_count: 13
  slug: merge-accountrequest
- name: AccountResponse
  property_count: 4
  slug: merge-accountresponse
- name: AccountsGetParametersClassification
  property_count: 0
  slug: merge-accountsgetparametersclassification
- name: AccountsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-accountsgetparametersexpandschemaitems
- name: AccountsGetParametersRemoteFields
  property_count: 0
  slug: merge-accountsgetparametersremotefields
- name: AccountsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-accountsgetparametersshowenumorigins
- name: AccountsGetParametersStatus
  property_count: 0
  slug: merge-accountsgetparametersstatus
- name: AccountsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-accountsidgetparametersexpandschemaitems
- name: AccountsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-accountsidgetparametersremotefields
- name: AccountsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-accountsidgetparametersshowenumorigins
- name: AccountStatusEnum
  property_count: 0
  slug: merge-accountstatusenum
- name: AccountToken
  property_count: 3
  slug: merge-accounttoken
- name: AccountTypeEnum
  property_count: 0
  slug: merge-accounttypeenum
- name: ActionsEnum
  property_count: 0
  slug: merge-actionsenum
- name: ActivitiesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-activitiesgetparametersexpandschemaitems
- name: ActivitiesGetParametersRemoteFields
  property_count: 0
  slug: merge-activitiesgetparametersremotefields
- name: ActivitiesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-activitiesgetparametersshowenumorigins
- name: ActivitiesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-activitiesidgetparametersexpandschemaitems
- name: ActivitiesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-activitiesidgetparametersremotefields
- name: ActivitiesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-activitiesidgetparametersshowenumorigins
- name: Activity
  property_count: 14
  slug: merge-activity
- name: ActivityEndpointRequest
  property_count: 2
  slug: merge-activityendpointrequest
- name: ActivityFieldMappings
  property_count: 2
  slug: merge-activityfieldmappings
- name: ActivityRequest
  property_count: 8
  slug: merge-activityrequest
- name: ActivityResponse
  property_count: 4
  slug: merge-activityresponse
- name: ActivityTypeEnum
  property_count: 0
  slug: merge-activitytypeenum
- name: Address
  property_count: 10
  slug: merge-address
- name: AddressesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-addressesidgetparametersremotefields
- name: AddressesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-addressesidgetparametersshowenumorigins
- name: AddressRequest
  property_count: 9
  slug: merge-addressrequest
- name: AddressTypeEnum
  property_count: 0
  slug: merge-addresstypeenum
- name: AdvancedMetadata
  property_count: 6
  slug: merge-advancedmetadata
- name: ApiV1AuditLogGetParametersEventType
  property_count: 0
  slug: merge-apiv1auditloggetparameterseventtype
- name: ApiV1ToolPacksToolPackIdRegisteredUsersRegisteredUserIdMcpPostParametersFormat
  property_count: 0
  slug: merge-apiv1toolpackstoolpackidregisteredusersregistereduseridmcppo
- name: ApiV1ToolPacksToolPackIdRegisteredUsersRegisteredUserIdSearchPostResponsesContentApplicationJsonSchemaToolsItemsInputSchema
  property_count: 0
  slug: merge-apiv1toolpackstoolpackidregisteredusersregistereduseridsearc
- name: Application
  property_count: 17
  slug: merge-application
- name: ApplicationCredentialPublicCreate
  property_count: 4
  slug: merge-applicationcredentialpubliccreate
- name: ApplicationCredentialPublicResponse
  property_count: 7
  slug: merge-applicationcredentialpublicresponse
- name: ApplicationEndpointRequest
  property_count: 2
  slug: merge-applicationendpointrequest
- name: ApplicationFieldMappings
  property_count: 2
  slug: merge-applicationfieldmappings
- name: ApplicationRequest
  property_count: 13
  slug: merge-applicationrequest
- name: ApplicationResponse
  property_count: 4
  slug: merge-applicationresponse
- name: ApplicationsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-applicationsgetparametersexpandschemaitems
- name: ApplicationsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-applicationsidgetparametersexpandschemaitems
- name: ApplyCreditNoteRequest
  property_count: 3
  slug: merge-applycreditnoterequest
- name: ApplyVendorCreditRequest
  property_count: 3
  slug: merge-applyvendorcreditrequest
- name: Article
  property_count: 24
  slug: merge-article
- name: ArticleFieldMappings
  property_count: 0
  slug: merge-articlefieldmappings
- name: ArticlesGetParametersExpand
  property_count: 0
  slug: merge-articlesgetparametersexpand
- name: ArticlesGetParametersType
  property_count: 0
  slug: merge-articlesgetparameterstype
- name: ArticlesIdGetParametersExpand
  property_count: 0
  slug: merge-articlesidgetparametersexpand
- name: ArticleTypeEnum
  property_count: 0
  slug: merge-articletypeenum
- name: Association
  property_count: 5
  slug: merge-association
- name: AssociationSubType
  property_count: 4
  slug: merge-associationsubtype
- name: AssociationType
  property_count: 10
  slug: merge-associationtype
- name: AssociationTypeRequestRequest
  property_count: 6
  slug: merge-associationtyperequestrequest
- name: AsyncBulkCreateResponse
  property_count: 1
  slug: merge-asyncbulkcreateresponse
- name: AsyncPassthroughReciept
  property_count: 1
  slug: merge-asyncpassthroughreciept
- name: AsyncPostTask
  property_count: 2
  slug: merge-asyncposttask
- name: AsyncPostTaskResult
  property_count: 2
  slug: merge-asyncposttaskresult
- name: AsyncPostTaskStatusEnum
  property_count: 0
  slug: merge-asyncposttaskstatusenum
- name: Attachment
  property_count: 11
  slug: merge-attachment
- name: AttachmentEndpointRequest
  property_count: 2
  slug: merge-attachmentendpointrequest
- name: AttachmentFieldMappings
  property_count: 2
  slug: merge-attachmentfieldmappings
- name: AttachmentRequest
  property_count: 6
  slug: merge-attachmentrequest
- name: AttachmentResponse
  property_count: 4
  slug: merge-attachmentresponse
- name: AttachmentsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-attachmentsgetparametersexpandschemaitems
- name: AttachmentsGetParametersRemoteFields
  property_count: 0
  slug: merge-attachmentsgetparametersremotefields
- name: AttachmentsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-attachmentsgetparametersshowenumorigins
- name: AttachmentsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-attachmentsidgetparametersexpandschemaitems
- name: AttachmentsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-attachmentsidgetparametersremotefields
- name: AttachmentsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-attachmentsidgetparametersshowenumorigins
- name: AttachmentTypeEnum
  property_count: 0
  slug: merge-attachmenttypeenum
- name: AuditLogEvent
  property_count: 8
  slug: merge-auditlogevent
- name: AuditLogEventPublic
  property_count: 8
  slug: merge-auditlogeventpublic
- name: AuthOptionPublic
  property_count: 2
  slug: merge-authoptionpublic
- name: AvailableActions
  property_count: 3
  slug: merge-availableactions
- name: BalanceSheet
  property_count: 16
  slug: merge-balancesheet
- name: BalanceSheetFieldMappings
  property_count: 2
  slug: merge-balancesheetfieldmappings
- name: BalanceSheetsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-balancesheetsgetparametersexpandschemaitems
- name: BalanceSheetsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-balancesheetsidgetparametersexpandschemaitems
- name: BankFeedAccount
  property_count: 17
  slug: merge-bankfeedaccount
- name: BankFeedAccountAccountTypeEnum
  property_count: 0
  slug: merge-bankfeedaccountaccounttypeenum
- name: BankFeedAccountEndpointRequest
  property_count: 1
  slug: merge-bankfeedaccountendpointrequest
- name: BankFeedAccountFieldMappings
  property_count: 2
  slug: merge-bankfeedaccountfieldmappings
- name: BankFeedAccountRequest
  property_count: 12
  slug: merge-bankfeedaccountrequest
- name: BankFeedAccountResponse
  property_count: 4
  slug: merge-bankfeedaccountresponse
- name: BankFeedTransaction
  property_count: 15
  slug: merge-bankfeedtransaction
- name: BankFeedTransactionEndpointRequest
  property_count: 1
  slug: merge-bankfeedtransactionendpointrequest
- name: BankFeedTransactionRequestRequest
  property_count: 11
  slug: merge-bankfeedtransactionrequestrequest
- name: BankFeedTransactionResponse
  property_count: 4
  slug: merge-bankfeedtransactionresponse
- name: BankFeedTransactionsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-bankfeedtransactionsgetparametersexpandschemaitems
- name: BankFeedTransactionsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-bankfeedtransactionsidgetparametersexpandschemaitems
- name: BankInfo
  property_count: 13
  slug: merge-bankinfo
- name: BankInfoFieldMappings
  property_count: 2
  slug: merge-bankinfofieldmappings
- name: BankInfoGetParametersAccountType
  property_count: 0
  slug: merge-bankinfogetparametersaccounttype
- name: BankInfoGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-bankinfogetparametersexpandschemaitems
- name: BankInfoGetParametersOrderBy
  property_count: 0
  slug: merge-bankinfogetparametersorderby
- name: BankInfoGetParametersRemoteFields
  property_count: 0
  slug: merge-bankinfogetparametersremotefields
- name: BankInfoGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-bankinfogetparametersshowenumorigins
- name: BankInfoIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-bankinfoidgetparametersexpandschemaitems
- name: BankInfoIdGetParametersRemoteFields
  property_count: 0
  slug: merge-bankinfoidgetparametersremotefields
- name: BankInfoIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-bankinfoidgetparametersshowenumorigins
- name: BatchObject
  property_count: 3
  slug: merge-batchobject
- name: BatchObjectItemResponse
  property_count: 2
  slug: merge-batchobjectitemresponse
- name: BatchObjectsResponse
  property_count: 4
  slug: merge-batchobjectsresponse
- name: BatchObjectsResponseStatusEnum
  property_count: 0
  slug: merge-batchobjectsresponsestatusenum
- name: BatchObjectStatusEnum
  property_count: 0
  slug: merge-batchobjectstatusenum
- name: Benefit
  property_count: 15
  slug: merge-benefit
- name: BenefitFieldMappings
  property_count: 2
  slug: merge-benefitfieldmappings
- name: BenefitPlanTypeEnum
  property_count: 0
  slug: merge-benefitplantypeenum
- name: BenefitsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-benefitsgetparametersexpandschemaitems
- name: BenefitsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-benefitsidgetparametersexpandschemaitems
- name: BulkToolDescriptionOverrideInput
  property_count: 3
  slug: merge-bulktooldescriptionoverrideinput
- name: Candidate
  property_count: 23
  slug: merge-candidate
- name: CandidateEndpointRequest
  property_count: 2
  slug: merge-candidateendpointrequest
- name: CandidateFieldMappings
  property_count: 2
  slug: merge-candidatefieldmappings
- name: CandidateRequest
  property_count: 17
  slug: merge-candidaterequest
- name: CandidateResponse
  property_count: 4
  slug: merge-candidateresponse
- name: candidates_ignoreCreate_Response_200
  property_count: 0
  slug: merge-candidates-ignorecreate-response-200
- name: CandidatesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-candidatesgetparametersexpandschemaitems
- name: CandidatesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-candidatesidgetparametersexpandschemaitems
- name: CardinalityEnum
  property_count: 0
  slug: merge-cardinalityenum
- name: CashFlowStatement
  property_count: 18
  slug: merge-cashflowstatement
- name: CashFlowStatementFieldMappings
  property_count: 2
  slug: merge-cashflowstatementfieldmappings
- name: CashFlowStatementsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-cashflowstatementsgetparametersexpandschemaitems
- name: CashFlowStatementsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-cashflowstatementsidgetparametersexpandschemaitems
- name: CategoriesEnum
  property_count: 0
  slug: merge-categoriesenum
- name: CategoryEnum
  property_count: 0
  slug: merge-categoryenum
- name: CategoryTypeEnum
  property_count: 0
  slug: merge-categorytypeenum
- name: ClassificationEnum
  property_count: 0
  slug: merge-classificationenum
- name: Collection
  property_count: 16
  slug: merge-collection
- name: CollectionAccessLevelEnum
  property_count: 0
  slug: merge-collectionaccesslevelenum
- name: CollectionFieldMappings
  property_count: 2
  slug: merge-collectionfieldmappings
- name: CollectionsCollectionIdViewersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-collectionscollectionidviewersgetparametersexpandschemaitems
- name: CollectionsGetParametersCollectionType
  property_count: 0
  slug: merge-collectionsgetparameterscollectiontype
- name: CollectionsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-collectionsgetparametersexpandschemaitems
- name: CollectionsGetParametersRemoteFields
  property_count: 0
  slug: merge-collectionsgetparametersremotefields
- name: CollectionsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-collectionsgetparametersshowenumorigins
- name: CollectionsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-collectionsidgetparametersexpandschemaitems
- name: CollectionsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-collectionsidgetparametersremotefields
- name: CollectionsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-collectionsidgetparametersshowenumorigins
- name: CollectionTypeEnum
  property_count: 0
  slug: merge-collectiontypeenum
- name: Comment
  property_count: 14
  slug: merge-comment
- name: CommentEndpointRequest
  property_count: 1
  slug: merge-commentendpointrequest
- name: CommentFieldMappings
  property_count: 2
  slug: merge-commentfieldmappings
- name: CommentRequest
  property_count: 8
  slug: merge-commentrequest
- name: CommentResponse
  property_count: 4
  slug: merge-commentresponse
- name: CommentsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-commentsgetparametersexpandschemaitems
- name: CommentsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-commentsidgetparametersexpandschemaitems
- name: CommonModelScopeAPI
  property_count: 1
  slug: merge-commonmodelscopeapi
- name: CommonModelScopesBodyRequest
  property_count: 3
  slug: merge-commonmodelscopesbodyrequest
- name: Company
  property_count: 10
  slug: merge-company
- name: CompanyFieldMappings
  property_count: 2
  slug: merge-companyfieldmappings
- name: CompanyInfo
  property_count: 17
  slug: merge-companyinfo
- name: CompanyInfoFieldMappings
  property_count: 2
  slug: merge-companyinfofieldmappings
- name: CompanyInfoGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-companyinfogetparametersexpandschemaitems
- name: CompanyInfoIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-companyinfoidgetparametersexpandschemaitems
- name: CompletedAccountInitialScreenEnum
  property_count: 0
  slug: merge-completedaccountinitialscreenenum
- name: ComponentTypeEnum
  property_count: 0
  slug: merge-componenttypeenum
- name: ConnectorDetailPublicResponse
  property_count: 9
  slug: merge-connectordetailpublicresponse
- name: ConnectorPublic
  property_count: 8
  slug: merge-connectorpublic
- name: ConnectorPublicAuthScope
  property_count: 0
  slug: merge-connectorpublicauthscope
- name: ConnectorTool
  property_count: 4
  slug: merge-connectortool
- name: ConnectorToolMini
  property_count: 3
  slug: merge-connectortoolmini
- name: Contact
  property_count: 19
  slug: merge-contact
- name: ContactEndpointRequest
  property_count: 1
  slug: merge-contactendpointrequest
- name: ContactFieldMappings
  property_count: 2
  slug: merge-contactfieldmappings
- name: ContactRequest
  property_count: 13
  slug: merge-contactrequest
- name: ContactResponse
  property_count: 4
  slug: merge-contactresponse
- name: contacts_ignoreCreate_Response_200
  property_count: 0
  slug: merge-contacts-ignorecreate-response-200
- name: ContactsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-contactsgetparametersexpandschemaitems
- name: ContactsGetParametersRemoteFields
  property_count: 0
  slug: merge-contactsgetparametersremotefields
- name: ContactsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-contactsgetparametersshowenumorigins
- name: ContactsGetParametersStatus
  property_count: 0
  slug: merge-contactsgetparametersstatus
- name: ContactsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-contactsidgetparametersexpandschemaitems
- name: ContactsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-contactsidgetparametersremotefields
- name: ContactsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-contactsidgetparametersshowenumorigins
- name: Container
  property_count: 18
  slug: merge-container
- name: ContainerFieldMappings
  property_count: 0
  slug: merge-containerfieldmappings
- name: ContainersGetParametersExpand
  property_count: 0
  slug: merge-containersgetparametersexpand
- name: ContainersGetParametersType
  property_count: 0
  slug: merge-containersgetparameterstype
- name: ContainersIdGetParametersExpand
  property_count: 0
  slug: merge-containersidgetparametersexpand
- name: ContainerTypeEnum
  property_count: 0
  slug: merge-containertypeenum
- name: Conversation
  property_count: 14
  slug: merge-conversation
- name: ConversationFieldMappings
  property_count: 2
  slug: merge-conversationfieldmappings
- name: ConversationsConversationIdMembersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-conversationsconversationidmembersgetparametersexpandschemai
- name: ConversationsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-conversationsgetparametersexpandschemaitems
- name: ConversationsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-conversationsidgetparametersexpandschemaitems
- name: CountryEnum
  property_count: 0
  slug: merge-countryenum
- name: CreateFieldMappingRequest
  property_count: 10
  slug: merge-createfieldmappingrequest
- name: CreateTargetFieldRequest
  property_count: 3
  slug: merge-createtargetfieldrequest
- name: CreditNote
  property_count: 25
  slug: merge-creditnote
- name: CreditNoteApplyLineForCreditNote
  property_count: 7
  slug: merge-creditnoteapplylineforcreditnote
- name: CreditNoteApplyLineForCreditNoteRequest
  property_count: 6
  slug: merge-creditnoteapplylineforcreditnoterequest
- name: CreditNoteApplyLineForInvoice
  property_count: 7
  slug: merge-creditnoteapplylineforinvoice
- name: CreditNoteEndpointRequest
  property_count: 1
  slug: merge-creditnoteendpointrequest
- name: CreditNoteFieldMappings
  property_count: 2
  slug: merge-creditnotefieldmappings
- name: CreditNoteLineItem
  property_count: 19
  slug: merge-creditnotelineitem
- name: CreditNoteLineItemRequest
  property_count: 17
  slug: merge-creditnotelineitemrequest
- name: CreditNoteRequest
  property_count: 18
  slug: merge-creditnoterequest
- name: CreditNoteResponse
  property_count: 4
  slug: merge-creditnoteresponse
- name: CreditNotesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-creditnotesgetparametersexpandschemaitems
- name: CreditNotesGetParametersRemoteFields
  property_count: 0
  slug: merge-creditnotesgetparametersremotefields
- name: CreditNotesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-creditnotesgetparametersshowenumorigins
- name: CreditNotesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-creditnotesidgetparametersexpandschemaitems
- name: CreditNotesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-creditnotesidgetparametersremotefields
- name: CreditNotesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-creditnotesidgetparametersshowenumorigins
- name: CreditNoteStatusEnum
  property_count: 0
  slug: merge-creditnotestatusenum
- name: CreditOrDebitEnum
  property_count: 0
  slug: merge-creditordebitenum
- name: CRMAccountEndpointRequest
  property_count: 1
  slug: merge-crmaccountendpointrequest
- name: CRMAccountResponse
  property_count: 4
  slug: merge-crmaccountresponse
- name: CRMAssociationTypeEndpointRequest
  property_count: 1
  slug: merge-crmassociationtypeendpointrequest
- name: CRMAssociationTypeResponse
  property_count: 4
  slug: merge-crmassociationtyperesponse
- name: CRMContactEndpointRequest
  property_count: 1
  slug: merge-crmcontactendpointrequest
- name: CRMContactResponse
  property_count: 4
  slug: merge-crmcontactresponse
- name: CRMCustomObjectEndpointRequest
  property_count: 1
  slug: merge-crmcustomobjectendpointrequest
- name: CRMCustomObjectResponse
  property_count: 4
  slug: merge-crmcustomobjectresponse
- name: CustomObject
  property_count: 7
  slug: merge-customobject
- name: CustomObjectClass
  property_count: 9
  slug: merge-customobjectclass
- name: CustomObjectClassesCustomObjectClassIdAssociationTypesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-customobjectclassescustomobjectclassidassociationtypesgetpar
- name: CustomObjectClassesCustomObjectClassIdAssociationTypesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-customobjectclassescustomobjectclassidassociationtypesidgetp
- name: CustomObjectClassesCustomObjectClassIdCustomObjectsObjectIdAssociationsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-customobjectclassescustomobjectclassidcustomobjectsobjectida
- name: CustomObjectClassesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-customobjectclassesgetparametersexpandschemaitems
- name: CustomObjectClassesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-customobjectclassesidgetparametersexpandschemaitems
- name: CustomObjectRequest
  property_count: 3
  slug: merge-customobjectrequest
- name: CustomRegexOverrideCreateInput
  property_count: 7
  slug: merge-customregexoverridecreateinput
- name: CustomRegexOverrideCreateInputInboundAction
  property_count: 0
  slug: merge-customregexoverridecreateinputinboundaction
- name: CustomRegexOverrideCreateInputOutboundAction
  property_count: 0
  slug: merge-customregexoverridecreateinputoutboundaction
- name: CustomRegexRuleCreateInput
  property_count: 6
  slug: merge-customregexrulecreateinput
- name: CustomRegexRuleCreateInputInboundAction
  property_count: 0
  slug: merge-customregexrulecreateinputinboundaction
- name: CustomRegexRuleCreateInputOutboundAction
  property_count: 0
  slug: merge-customregexrulecreateinputoutboundaction
- name: CustomRegexRuleResponse
  property_count: 10
  slug: merge-customregexruleresponse
- name: CustomRegexRuleResponseOutboundAction
  property_count: 0
  slug: merge-customregexruleresponseoutboundaction
- name: DataPassthroughRequest
  property_count: 8
  slug: merge-datapassthroughrequest
- name: DebugModelLogSummary
  property_count: 3
  slug: merge-debugmodellogsummary
- name: DebugModeLog
  property_count: 3
  slug: merge-debugmodelog
- name: Deduction
  property_count: 11
  slug: merge-deduction
- name: DeductionFieldMappings
  property_count: 2
  slug: merge-deductionfieldmappings
- name: delete-account_delete_Response_200
  property_count: 0
  slug: merge-delete-account-delete-response-200
- name: deleteAccount_delete_Response_200
  property_count: 0
  slug: merge-deleteaccount-delete-response-200
- name: Department
  property_count: 8
  slug: merge-department
- name: DepartmentFieldMappings
  property_count: 2
  slug: merge-departmentfieldmappings
- name: Dependent
  property_count: 18
  slug: merge-dependent
- name: DependentFieldMappings
  property_count: 2
  slug: merge-dependentfieldmappings
- name: DirectionEnum
  property_count: 0
  slug: merge-directionenum
- name: DisabilityStatusEnum
  property_count: 0
  slug: merge-disabilitystatusenum
- name: DocumentContentSourceType
  property_count: 0
  slug: merge-documentcontentsourcetype
- name: DownloadRequestMeta
  property_count: 4
  slug: merge-downloadrequestmeta
- name: Drive
  property_count: 11
  slug: merge-drive
- name: DriveFieldMappings
  property_count: 2
  slug: merge-drivefieldmappings
- name: Earning
  property_count: 10
  slug: merge-earning
- name: EarningFieldMappings
  property_count: 2
  slug: merge-earningfieldmappings
- name: EarningTypeEnum
  property_count: 0
  slug: merge-earningtypeenum
- name: EEOC
  property_count: 13
  slug: merge-eeoc
- name: EeocFieldMappings
  property_count: 2
  slug: merge-eeocfieldmappings
- name: EeocsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-eeocsgetparametersexpandschemaitems
- name: EeocsGetParametersRemoteFields
  property_count: 0
  slug: merge-eeocsgetparametersremotefields
- name: EeocsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-eeocsgetparametersshowenumorigins
- name: EeocsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-eeocsidgetparametersexpandschemaitems
- name: EeocsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-eeocsidgetparametersremotefields
- name: EeocsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-eeocsidgetparametersshowenumorigins
- name: EffectEnum
  property_count: 0
  slug: merge-effectenum
- name: EmailAddress
  property_count: 5
  slug: merge-emailaddress
- name: EmailAddressRequest
  property_count: 4
  slug: merge-emailaddressrequest
- name: EmailAddressTypeEnum
  property_count: 0
  slug: merge-emailaddresstypeenum
- name: EmbeddingDataSchema
  property_count: 3
  slug: merge-embeddingdataschema
- name: EmbeddingRequestSchema
  property_count: 4
  slug: merge-embeddingrequestschema
- name: EmbeddingRequestSchemaInput
  property_count: 0
  slug: merge-embeddingrequestschemainput
- name: EmbeddingResponseSchema
  property_count: 4
  slug: merge-embeddingresponseschema
- name: EmbeddingUsage
  property_count: 2
  slug: merge-embeddingusage
- name: Employee
  property_count: 14
  slug: merge-employee
- name: EmployeeFieldMappings
  property_count: 2
  slug: merge-employeefieldmappings
- name: EmployeePayrollRun
  property_count: 17
  slug: merge-employeepayrollrun
- name: EmployeePayrollRunFieldMappings
  property_count: 2
  slug: merge-employeepayrollrunfieldmappings
- name: EmployeePayrollRunsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-employeepayrollrunsgetparametersexpandschemaitems
- name: EmployeePayrollRunsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-employeepayrollrunsidgetparametersexpandschemaitems
- name: employees_ignoreCreate_Response_200
  property_count: 0
  slug: merge-employees-ignorecreate-response-200
- name: EmployeesGetParametersEmploymentStatus
  property_count: 0
  slug: merge-employeesgetparametersemploymentstatus
- name: EmployeesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-employeesgetparametersexpandschemaitems
- name: EmployeesGetParametersRemoteFields
  property_count: 0
  slug: merge-employeesgetparametersremotefields
- name: EmployeesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-employeesgetparametersshowenumorigins
- name: EmployeesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-employeesidgetparametersexpandschemaitems
- name: EmployeesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-employeesidgetparametersremotefields
- name: EmployeesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-employeesidgetparametersshowenumorigins
- name: EmployerBenefit
  property_count: 11
  slug: merge-employerbenefit
- name: EmployerBenefitFieldMappings
  property_count: 2
  slug: merge-employerbenefitfieldmappings
- name: Employment
  property_count: 17
  slug: merge-employment
- name: EmploymentFieldMappings
  property_count: 2
  slug: merge-employmentfieldmappings
- name: EmploymentsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-employmentsgetparametersexpandschemaitems
- name: EmploymentsGetParametersOrderBy
  property_count: 0
  slug: merge-employmentsgetparametersorderby
- name: EmploymentsGetParametersRemoteFields
  property_count: 0
  slug: merge-employmentsgetparametersremotefields
- name: EmploymentsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-employmentsgetparametersshowenumorigins
- name: EmploymentsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-employmentsidgetparametersexpandschemaitems
- name: EmploymentsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-employmentsidgetparametersremotefields
- name: EmploymentsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-employmentsidgetparametersshowenumorigins
- name: EmploymentStatusEnum
  property_count: 0
  slug: merge-employmentstatusenum
- name: EmploymentTypeEnum
  property_count: 0
  slug: merge-employmenttypeenum
- name: EnabledActionsEnum
  property_count: 0
  slug: merge-enabledactionsenum
- name: EncodingEnum
  property_count: 0
  slug: merge-encodingenum
- name: EndUserDetailsRequest
  property_count: 17
  slug: merge-enduserdetailsrequest
- name: Engagement
  property_count: 18
  slug: merge-engagement
- name: EngagementEndpointRequest
  property_count: 1
  slug: merge-engagementendpointrequest
- name: EngagementFieldMappings
  property_count: 2
  slug: merge-engagementfieldmappings
- name: EngagementRequest
  property_count: 13
  slug: merge-engagementrequest
- name: EngagementResponse
  property_count: 4
  slug: merge-engagementresponse
- name: EngagementsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-engagementsgetparametersexpandschemaitems
- name: EngagementsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-engagementsidgetparametersexpandschemaitems
- name: EngagementType
  property_count: 7
  slug: merge-engagementtype
- name: ErrorValidationProblem
  property_count: 7
  slug: merge-errorvalidationproblem
- name: EthnicityEnum
  property_count: 0
  slug: merge-ethnicityenum
- name: EventTypeEnum
  property_count: 0
  slug: merge-eventtypeenum
- name: Expense
  property_count: 24
  slug: merge-expense
- name: ExpenseBatchItemRequest
  property_count: 2
  slug: merge-expensebatchitemrequest
- name: ExpenseBulkRequest
  property_count: 1
  slug: merge-expensebulkrequest
- name: ExpenseEndpointRequest
  property_count: 1
  slug: merge-expenseendpointrequest
- name: ExpenseFieldMappings
  property_count: 2
  slug: merge-expensefieldmappings
- name: ExpenseLine
  property_count: 20
  slug: merge-expenseline
- name: ExpenseLineRequest
  property_count: 19
  slug: merge-expenselinerequest
- name: ExpenseReport
  property_count: 19
  slug: merge-expensereport
- name: ExpenseReportEndpointRequest
  property_count: 1
  slug: merge-expensereportendpointrequest
- name: ExpenseReportFieldMappings
  property_count: 2
  slug: merge-expensereportfieldmappings
- name: ExpenseReportLine
  property_count: 24
  slug: merge-expensereportline
- name: ExpenseReportRequest
  property_count: 13
  slug: merge-expensereportrequest
- name: ExpenseReportResponse
  property_count: 4
  slug: merge-expensereportresponse
- name: ExpenseReportsExpenseReportIdLinesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-expensereportsexpensereportidlinesgetparametersexpandschemai
- name: ExpenseReportsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-expensereportsgetparametersexpandschemaitems
- name: ExpenseReportsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-expensereportsidgetparametersexpandschemaitems
- name: ExpenseReportStatusEnum
  property_count: 0
  slug: merge-expensereportstatusenum
- name: ExpenseRequest
  property_count: 18
  slug: merge-expenserequest
- name: ExpenseResponse
  property_count: 4
  slug: merge-expenseresponse
- name: ExpensesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-expensesgetparametersexpandschemaitems
- name: ExpensesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-expensesidgetparametersexpandschemaitems
- name: ExternalTargetFieldAPI
  property_count: 3
  slug: merge-externaltargetfieldapi
- name: ExternalTargetFieldAPIResponse
  property_count: 27
  slug: merge-externaltargetfieldapiresponse
- name: FeedStatusEnum
  property_count: 0
  slug: merge-feedstatusenum
- name: FieldFormatEnum
  property_count: 0
  slug: merge-fieldformatenum
- name: FieldMappingApiInstance
  property_count: 6
  slug: merge-fieldmappingapiinstance
- name: FieldMappingApiInstanceRemoteField
  property_count: 3
  slug: merge-fieldmappingapiinstanceremotefield
- name: FieldMappingApiInstanceRemoteFieldRemoteEndpointInfo
  property_count: 3
  slug: merge-fieldmappingapiinstanceremotefieldremoteendpointinfo
- name: FieldMappingApiInstanceResponse
  property_count: 27
  slug: merge-fieldmappingapiinstanceresponse
- name: FieldMappingApiInstanceTargetField
  property_count: 3
  slug: merge-fieldmappingapiinstancetargetfield
- name: FieldMappingInstanceResponse
  property_count: 4
  slug: merge-fieldmappinginstanceresponse
- name: FieldPermissionDeserializer
  property_count: 2
  slug: merge-fieldpermissiondeserializer
- name: FieldPermissionDeserializerRequest
  property_count: 2
  slug: merge-fieldpermissiondeserializerrequest
- name: FieldTypeEnum
  property_count: 0
  slug: merge-fieldtypeenum
- name: File
  property_count: 19
  slug: merge-file
- name: FileFieldMappings
  property_count: 2
  slug: merge-filefieldmappings
- name: FileRequest
  property_count: 12
  slug: merge-filerequest
- name: FilesDownloadRequestMetaGetParametersOrderBy
  property_count: 0
  slug: merge-filesdownloadrequestmetagetparametersorderby
- name: FilesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-filesgetparametersexpandschemaitems
- name: FilesGetParametersOrderBy
  property_count: 0
  slug: merge-filesgetparametersorderby
- name: FilesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-filesidgetparametersexpandschemaitems
- name: FileStorageFileEndpointRequest
  property_count: 1
  slug: merge-filestoragefileendpointrequest
- name: FileStorageFileResponse
  property_count: 4
  slug: merge-filestoragefileresponse
- name: FileStorageFolderEndpointRequest
  property_count: 1
  slug: merge-filestoragefolderendpointrequest
- name: FileStorageFolderResponse
  property_count: 4
  slug: merge-filestoragefolderresponse
- name: FlsaStatusEnum
  property_count: 0
  slug: merge-flsastatusenum
- name: Folder
  property_count: 16
  slug: merge-folder
- name: FolderFieldMappings
  property_count: 2
  slug: merge-folderfieldmappings
- name: FolderRequest
  property_count: 9
  slug: merge-folderrequest
- name: FoldersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-foldersgetparametersexpandschemaitems
- name: FoldersIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-foldersidgetparametersexpandschemaitems
- name: FunctionTool
  property_count: 4
  slug: merge-functiontool
- name: GenderEnum
  property_count: 0
  slug: merge-genderenum
- name: GenerateRemoteKeyRequest
  property_count: 1
  slug: merge-generateremotekeyrequest
- name: Group
  property_count: 11
  slug: merge-group
- name: GroupFieldMappings
  property_count: 2
  slug: merge-groupfieldmappings
- name: groups_typesList_Response_200
  property_count: 1
  slug: merge-groups-typeslist-response-200
- name: GroupsGetParametersExpand
  property_count: 0
  slug: merge-groupsgetparametersexpand
- name: GroupsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-groupsgetparametersexpandschemaitems
- name: GroupsGetParametersRemoteFields
  property_count: 0
  slug: merge-groupsgetparametersremotefields
- name: GroupsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-groupsgetparametersshowenumorigins
- name: GroupsIdGetParametersExpand
  property_count: 0
  slug: merge-groupsidgetparametersexpand
- name: GroupsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-groupsidgetparametersexpandschemaitems
- name: GroupsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-groupsidgetparametersremotefields
- name: GroupsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-groupsidgetparametersshowenumorigins
- name: GroupTypeEnum
  property_count: 0
  slug: merge-grouptypeenum
- name: HTTPValidationError
  property_count: 1
  slug: merge-httpvalidationerror
- name: IgnoreCommonModelRequest
  property_count: 2
  slug: merge-ignorecommonmodelrequest
- name: ImageContentSourceType
  property_count: 0
  slug: merge-imagecontentsourcetype
- name: IncomeStatement
  property_count: 19
  slug: merge-incomestatement
- name: IncomeStatementFieldMappings
  property_count: 2
  slug: merge-incomestatementfieldmappings
- name: IncomeStatementsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-incomestatementsgetparametersexpandschemaitems
- name: IncomeStatementsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-incomestatementsidgetparametersexpandschemaitems
- name: IndividualCommonModelScopeDeserializer
  property_count: 3
  slug: merge-individualcommonmodelscopedeserializer
- name: IndividualCommonModelScopeDeserializerRequest
  property_count: 3
  slug: merge-individualcommonmodelscopedeserializerrequest
- name: InterviewsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-interviewsgetparametersexpandschemaitems
- name: InterviewsGetParametersRemoteFields
  property_count: 0
  slug: merge-interviewsgetparametersremotefields
- name: InterviewsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-interviewsgetparametersshowenumorigins
- name: InterviewsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-interviewsidgetparametersexpandschemaitems
- name: InterviewsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-interviewsidgetparametersremotefields
- name: InterviewsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-interviewsidgetparametersshowenumorigins
- name: Invoice
  property_count: 37
  slug: merge-invoice
- name: InvoiceBatchItemRequest
  property_count: 2
  slug: merge-invoicebatchitemrequest
- name: InvoiceBulkRequest
  property_count: 1
  slug: merge-invoicebulkrequest
- name: InvoiceEndpointRequest
  property_count: 1
  slug: merge-invoiceendpointrequest
- name: InvoiceFieldMappings
  property_count: 2
  slug: merge-invoicefieldmappings
- name: InvoiceLineItem
  property_count: 23
  slug: merge-invoicelineitem
- name: InvoiceLineItemFieldMappings
  property_count: 2
  slug: merge-invoicelineitemfieldmappings
- name: InvoiceLineItemRequest
  property_count: 20
  slug: merge-invoicelineitemrequest
- name: InvoiceRequest
  property_count: 27
  slug: merge-invoicerequest
- name: InvoiceResponse
  property_count: 4
  slug: merge-invoiceresponse
- name: InvoicesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-invoicesgetparametersexpandschemaitems
- name: InvoicesGetParametersRemoteFields
  property_count: 0
  slug: merge-invoicesgetparametersremotefields
- name: InvoicesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-invoicesgetparametersshowenumorigins
- name: InvoicesGetParametersStatus
  property_count: 0
  slug: merge-invoicesgetparametersstatus
- name: InvoicesGetParametersType
  property_count: 0
  slug: merge-invoicesgetparameterstype
- name: InvoicesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-invoicesidgetparametersexpandschemaitems
- name: InvoicesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-invoicesidgetparametersremotefields
- name: InvoicesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-invoicesidgetparametersshowenumorigins
- name: InvoiceStatusEnum
  property_count: 0
  slug: merge-invoicestatusenum
- name: InvoiceTypeEnum
  property_count: 0
  slug: merge-invoicetypeenum
- name: Issue
  property_count: 8
  slug: merge-issue
- name: IssuesGetParametersStatus
  property_count: 0
  slug: merge-issuesgetparametersstatus
- name: IssueStatusEnum
  property_count: 0
  slug: merge-issuestatusenum
- name: Item
  property_count: 18
  slug: merge-item
- name: ItemEndpointRequest
  property_count: 1
  slug: merge-itemendpointrequest
- name: ItemFieldMappings
  property_count: 2
  slug: merge-itemfieldmappings
- name: ItemFormatEnum
  property_count: 0
  slug: merge-itemformatenum
- name: ItemFulfillment
  property_count: 17
  slug: merge-itemfulfillment
- name: ItemFulfillmentBatchItemRequest
  property_count: 2
  slug: merge-itemfulfillmentbatchitemrequest
- name: ItemFulfillmentBulkRequest
  property_count: 1
  slug: merge-itemfulfillmentbulkrequest
- name: ItemFulfillmentEndpointRequest
  property_count: 1
  slug: merge-itemfulfillmentendpointrequest
- name: ItemFulfillmentFieldMappings
  property_count: 2
  slug: merge-itemfulfillmentfieldmappings
- name: ItemFulfillmentLine
  property_count: 12
  slug: merge-itemfulfillmentline
- name: ItemFulfillmentLineRequest
  property_count: 10
  slug: merge-itemfulfillmentlinerequest
- name: ItemFulfillmentRequestRequest
  property_count: 10
  slug: merge-itemfulfillmentrequestrequest
- name: ItemFulfillmentResponse
  property_count: 4
  slug: merge-itemfulfillmentresponse
- name: ItemFulfillmentsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-itemfulfillmentsgetparametersexpandschemaitems
- name: ItemFulfillmentsGetParametersRemoteFields
  property_count: 0
  slug: merge-itemfulfillmentsgetparametersremotefields
- name: ItemFulfillmentsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-itemfulfillmentsgetparametersshowenumorigins
- name: ItemFulfillmentsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-itemfulfillmentsidgetparametersexpandschemaitems
- name: ItemFulfillmentsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-itemfulfillmentsidgetparametersremotefields
- name: ItemFulfillmentsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-itemfulfillmentsidgetparametersshowenumorigins
- name: ItemFulfillmentStatusEnum
  property_count: 0
  slug: merge-itemfulfillmentstatusenum
- name: ItemRequestRequest
  property_count: 12
  slug: merge-itemrequestrequest
- name: ItemResponse
  property_count: 4
  slug: merge-itemresponse
- name: ItemSchema
  property_count: 3
  slug: merge-itemschema
- name: ItemsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-itemsgetparametersexpandschemaitems
- name: ItemsGetParametersRemoteFields
  property_count: 0
  slug: merge-itemsgetparametersremotefields
- name: ItemsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-itemsgetparametersshowenumorigins
- name: ItemsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-itemsidgetparametersexpandschemaitems
- name: ItemsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-itemsidgetparametersremotefields
- name: ItemsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-itemsidgetparametersshowenumorigins
- name: ItemTypeEnum
  property_count: 0
  slug: merge-itemtypeenum
- name: Job
  property_count: 21
  slug: merge-job
- name: JobFieldMappings
  property_count: 2
  slug: merge-jobfieldmappings
- name: JobInterviewStage
  property_count: 10
  slug: merge-jobinterviewstage
- name: JobInterviewStageFieldMappings
  property_count: 2
  slug: merge-jobinterviewstagefieldmappings
- name: JobInterviewStagesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobinterviewstagesgetparametersexpandschemaitems
- name: JobInterviewStagesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobinterviewstagesidgetparametersexpandschemaitems
- name: JobPosting
  property_count: 15
  slug: merge-jobposting
- name: JobPostingFieldMappings
  property_count: 2
  slug: merge-jobpostingfieldmappings
- name: JobPostingsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobpostingsgetparametersexpandschemaitems
- name: JobPostingsGetParametersStatus
  property_count: 0
  slug: merge-jobpostingsgetparametersstatus
- name: JobPostingsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobpostingsidgetparametersexpandschemaitems
- name: JobPostingStatusEnum
  property_count: 0
  slug: merge-jobpostingstatusenum
- name: JobsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobsgetparametersexpandschemaitems
- name: JobsGetParametersRemoteFields
  property_count: 0
  slug: merge-jobsgetparametersremotefields
- name: JobsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-jobsgetparametersshowenumorigins
- name: JobsGetParametersStatus
  property_count: 0
  slug: merge-jobsgetparametersstatus
- name: JobsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobsidgetparametersexpandschemaitems
- name: JobsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-jobsidgetparametersremotefields
- name: JobsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-jobsidgetparametersshowenumorigins
- name: JobsJobIdScreeningQuestionsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-jobsjobidscreeningquestionsgetparametersexpandschemaitems
- name: JobStatusEnum
  property_count: 0
  slug: merge-jobstatusenum
- name: JobTypeEnum
  property_count: 0
  slug: merge-jobtypeenum
- name: JournalEntriesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-journalentriesgetparametersexpandschemaitems
- name: JournalEntriesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-journalentriesidgetparametersexpandschemaitems
- name: JournalEntry
  property_count: 23
  slug: merge-journalentry
- name: JournalEntryEndpointRequest
  property_count: 1
  slug: merge-journalentryendpointrequest
- name: JournalEntryFieldMappings
  property_count: 2
  slug: merge-journalentryfieldmappings
- name: JournalEntryRequest
  property_count: 14
  slug: merge-journalentryrequest
- name: JournalEntryResponse
  property_count: 4
  slug: merge-journalentryresponse
- name: JournalLine
  property_count: 18
  slug: merge-journalline
- name: JournalLineRequest
  property_count: 16
  slug: merge-journallinerequest
- name: LanguageEnum
  property_count: 0
  slug: merge-languageenum
- name: LastSyncResultEnum
  property_count: 0
  slug: merge-lastsyncresultenum
- name: Lead
  property_count: 24
  slug: merge-lead
- name: LeadEndpointRequest
  property_count: 1
  slug: merge-leadendpointrequest
- name: LeadFieldMappings
  property_count: 2
  slug: merge-leadfieldmappings
- name: LeadRequest
  property_count: 16
  slug: merge-leadrequest
- name: LeadResponse
  property_count: 4
  slug: merge-leadresponse
- name: LeadsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-leadsgetparametersexpandschemaitems
- name: LeadsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-leadsidgetparametersexpandschemaitems
- name: LeadStatusEnum
  property_count: 0
  slug: merge-leadstatusenum
- name: LinkedAccountCommonModelScopeDeserializerRequest
  property_count: 1
  slug: merge-linkedaccountcommonmodelscopedeserializerrequest
- name: LinkedAccountsGetParametersCategory
  property_count: 0
  slug: merge-linkedaccountsgetparameterscategory
- name: LinkedAccountStatus
  property_count: 2
  slug: merge-linkedaccountstatus
- name: linkToken_createForRegisteredUser_Response_201
  property_count: 2
  slug: merge-linktoken-createforregistereduser-response-201
- name: LinkToken
  property_count: 3
  slug: merge-linktoken
- name: Location
  property_count: 16
  slug: merge-location
- name: LocationFieldMappings
  property_count: 2
  slug: merge-locationfieldmappings
- name: LocationsGetParametersLocationType
  property_count: 0
  slug: merge-locationsgetparameterslocationtype
- name: LocationsGetParametersRemoteFields
  property_count: 0
  slug: merge-locationsgetparametersremotefields
- name: LocationsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-locationsgetparametersshowenumorigins
- name: LocationsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-locationsidgetparametersremotefields
- name: LocationsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-locationsidgetparametersshowenumorigins
- name: LocationTypeEnum
  property_count: 0
  slug: merge-locationtypeenum
- name: MaritalStatusEnum
  property_count: 0
  slug: merge-maritalstatusenum
- name: mcp_endpointPost_Response_200
  property_count: 3
  slug: merge-mcp-endpointpost-response-200
- name: Member
  property_count: 11
  slug: merge-member
- name: MemberFieldMappings
  property_count: 2
  slug: merge-memberfieldmappings
- name: Message
  property_count: 13
  slug: merge-message
- name: MessagesGetParametersOrderBy
  property_count: 0
  slug: merge-messagesgetparametersorderby
- name: MessagesMessageIdRepliesGetParametersOrderBy
  property_count: 0
  slug: merge-messagesmessageidrepliesgetparametersorderby
- name: MetaResponse
  property_count: 5
  slug: merge-metaresponse
- name: MethodEnum
  property_count: 0
  slug: merge-methodenum
- name: MethodTypeEnum
  property_count: 0
  slug: merge-methodtypeenum
- name: ModelOperation
  property_count: 4
  slug: merge-modeloperation
- name: ModelPermissionDeserializer
  property_count: 1
  slug: merge-modelpermissiondeserializer
- name: ModelPermissionDeserializerRequest
  property_count: 1
  slug: merge-modelpermissiondeserializerrequest
- name: ModelPricing
  property_count: 3
  slug: merge-modelpricing
- name: Models_list_Response_200
  property_count: 0
  slug: merge-models-list-response-200
- name: MultipartFormFieldRequest
  property_count: 5
  slug: merge-multipartformfieldrequest
- name: Note
  property_count: 16
  slug: merge-note
- name: NoteEndpointRequest
  property_count: 1
  slug: merge-noteendpointrequest
- name: NoteFieldMappings
  property_count: 2
  slug: merge-notefieldmappings
- name: NoteRequest
  property_count: 9
  slug: merge-noterequest
- name: NoteResponse
  property_count: 4
  slug: merge-noteresponse
- name: NotesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-notesgetparametersexpandschemaitems
- name: NotesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-notesidgetparametersexpandschemaitems
- name: ObjectClassDescriptionRequest
  property_count: 2
  slug: merge-objectclassdescriptionrequest
- name: Offer
  property_count: 14
  slug: merge-offer
- name: OfferFieldMappings
  property_count: 2
  slug: merge-offerfieldmappings
- name: OffersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-offersgetparametersexpandschemaitems
- name: OffersGetParametersRemoteFields
  property_count: 0
  slug: merge-offersgetparametersremotefields
- name: OffersGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-offersgetparametersshowenumorigins
- name: OffersGetParametersStatus
  property_count: 0
  slug: merge-offersgetparametersstatus
- name: OffersIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-offersidgetparametersexpandschemaitems
- name: OffersIdGetParametersRemoteFields
  property_count: 0
  slug: merge-offersidgetparametersremotefields
- name: OffersIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-offersidgetparametersshowenumorigins
- name: OfferStatusEnum
  property_count: 0
  slug: merge-offerstatusenum
- name: Office
  property_count: 9
  slug: merge-office
- name: OfficeFieldMappings
  property_count: 2
  slug: merge-officefieldmappings
- name: OpportunitiesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-opportunitiesgetparametersexpandschemaitems
- name: OpportunitiesGetParametersRemoteFields
  property_count: 0
  slug: merge-opportunitiesgetparametersremotefields
- name: OpportunitiesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-opportunitiesgetparametersshowenumorigins
- name: OpportunitiesGetParametersStatus
  property_count: 0
  slug: merge-opportunitiesgetparametersstatus
- name: OpportunitiesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-opportunitiesidgetparametersexpandschemaitems
- name: OpportunitiesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-opportunitiesidgetparametersremotefields
- name: OpportunitiesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-opportunitiesidgetparametersshowenumorigins
- name: Opportunity
  property_count: 19
  slug: merge-opportunity
- name: OpportunityEndpointRequest
  property_count: 1
  slug: merge-opportunityendpointrequest
- name: OpportunityFieldMappings
  property_count: 2
  slug: merge-opportunityfieldmappings
- name: OpportunityRequest
  property_count: 13
  slug: merge-opportunityrequest
- name: OpportunityResponse
  property_count: 4
  slug: merge-opportunityresponse
- name: OpportunityStatusEnum
  property_count: 0
  slug: merge-opportunitystatusenum
- name: OriginTypeEnum
  property_count: 0
  slug: merge-origintypeenum
- name: OutputMessage
  property_count: 5
  slug: merge-outputmessage
- name: OutputMessageContentItems
  property_count: 0
  slug: merge-outputmessagecontentitems
- name: OutputMessageFinishReason
  property_count: 0
  slug: merge-outputmessagefinishreason
- name: OverallRecommendationEnum
  property_count: 0
  slug: merge-overallrecommendationenum
- name: PaginatedAccessKeyList
  property_count: 4
  slug: merge-paginatedaccesskeylist
- name: PaginatedAccountDetailsAndActionsList
  property_count: 3
  slug: merge-paginatedaccountdetailsandactionslist
- name: PaginatedAccountingAttachmentList
  property_count: 3
  slug: merge-paginatedaccountingattachmentlist
- name: PaginatedAccountingPeriodList
  property_count: 3
  slug: merge-paginatedaccountingperiodlist
- name: PaginatedAccountList
  property_count: 3
  slug: merge-paginatedaccountlist
- name: PaginatedActivityList
  property_count: 3
  slug: merge-paginatedactivitylist
- name: PaginatedApplicationCredentialPublicResponseList
  property_count: 4
  slug: merge-paginatedapplicationcredentialpublicresponselist
- name: PaginatedApplicationList
  property_count: 3
  slug: merge-paginatedapplicationlist
- name: PaginatedArticleList
  property_count: 3
  slug: merge-paginatedarticlelist
- name: PaginatedAssociationList
  property_count: 3
  slug: merge-paginatedassociationlist
- name: PaginatedAssociationTypeList
  property_count: 3
  slug: merge-paginatedassociationtypelist
- name: PaginatedAttachmentList
  property_count: 3
  slug: merge-paginatedattachmentlist
- name: PaginatedAuditLogEventList
  property_count: 3
  slug: merge-paginatedauditlogeventlist
- name: PaginatedAuditLogEventPublicList
  property_count: 4
  slug: merge-paginatedauditlogeventpubliclist
- name: PaginatedBalanceSheetList
  property_count: 3
  slug: merge-paginatedbalancesheetlist
- name: PaginatedBankFeedAccountList
  property_count: 3
  slug: merge-paginatedbankfeedaccountlist
- name: PaginatedBankFeedTransactionList
  property_count: 3
  slug: merge-paginatedbankfeedtransactionlist
- name: PaginatedBankInfoList
  property_count: 3
  slug: merge-paginatedbankinfolist
- name: PaginatedBenefitList
  property_count: 3
  slug: merge-paginatedbenefitlist
- name: PaginatedCandidateList
  property_count: 3
  slug: merge-paginatedcandidatelist
- name: PaginatedCashFlowStatementList
  property_count: 3
  slug: merge-paginatedcashflowstatementlist
- name: PaginatedCollectionList
  property_count: 3
  slug: merge-paginatedcollectionlist
- name: PaginatedCommentList
  property_count: 3
  slug: merge-paginatedcommentlist
- name: PaginatedCompanyInfoList
  property_count: 3
  slug: merge-paginatedcompanyinfolist
- name: PaginatedCompanyList
  property_count: 3
  slug: merge-paginatedcompanylist
- name: PaginatedConnectorDetailPublicResponseList
  property_count: 4
  slug: merge-paginatedconnectordetailpublicresponselist
- name: PaginatedContactList
  property_count: 3
  slug: merge-paginatedcontactlist
- name: PaginatedContainerList
  property_count: 3
  slug: merge-paginatedcontainerlist
- name: PaginatedConversationList
  property_count: 3
  slug: merge-paginatedconversationlist
- name: PaginatedCreditNoteList
  property_count: 3
  slug: merge-paginatedcreditnotelist
- name: PaginatedCustomObjectClassList
  property_count: 3
  slug: merge-paginatedcustomobjectclasslist
- name: PaginatedCustomObjectList
  property_count: 3
  slug: merge-paginatedcustomobjectlist
- name: PaginatedCustomRegexRuleResponseList
  property_count: 4
  slug: merge-paginatedcustomregexruleresponselist
- name: PaginatedDepartmentList
  property_count: 3
  slug: merge-paginateddepartmentlist
- name: PaginatedDependentList
  property_count: 3
  slug: merge-paginateddependentlist
- name: PaginatedDownloadRequestMetaList
  property_count: 3
  slug: merge-paginateddownloadrequestmetalist
- name: PaginatedDriveList
  property_count: 3
  slug: merge-paginateddrivelist
- name: PaginatedEEOCList
  property_count: 3
  slug: merge-paginatedeeoclist
- name: PaginatedEmployeeList
  property_count: 3
  slug: merge-paginatedemployeelist
- name: PaginatedEmployeePayrollRunList
  property_count: 3
  slug: merge-paginatedemployeepayrollrunlist
- name: PaginatedEmployerBenefitList
  property_count: 3
  slug: merge-paginatedemployerbenefitlist
- name: PaginatedEmploymentList
  property_count: 3
  slug: merge-paginatedemploymentlist
- name: PaginatedEngagementList
  property_count: 3
  slug: merge-paginatedengagementlist
- name: PaginatedEngagementTypeList
  property_count: 3
  slug: merge-paginatedengagementtypelist
- name: PaginatedExpenseList
  property_count: 3
  slug: merge-paginatedexpenselist
- name: PaginatedExpenseReportLineList
  property_count: 3
  slug: merge-paginatedexpensereportlinelist
- name: PaginatedExpenseReportList
  property_count: 3
  slug: merge-paginatedexpensereportlist
- name: PaginatedFileList
  property_count: 3
  slug: merge-paginatedfilelist
- name: PaginatedFolderList
  property_count: 3
  slug: merge-paginatedfolderlist
- name: PaginatedGroupList
  property_count: 3
  slug: merge-paginatedgrouplist
- name: PaginatedIncomeStatementList
  property_count: 3
  slug: merge-paginatedincomestatementlist
- name: PaginatedInvoiceList
  property_count: 3
  slug: merge-paginatedinvoicelist
- name: PaginatedIssueList
  property_count: 3
  slug: merge-paginatedissuelist
- name: PaginatedItemFulfillmentList
  property_count: 3
  slug: merge-paginateditemfulfillmentlist
- name: PaginatedItemList
  property_count: 3
  slug: merge-paginateditemlist
- name: PaginatedJobInterviewStageList
  property_count: 3
  slug: merge-paginatedjobinterviewstagelist
- name: PaginatedJobList
  property_count: 3
  slug: merge-paginatedjoblist
- name: PaginatedJobPostingList
  property_count: 3
  slug: merge-paginatedjobpostinglist
- name: PaginatedJournalEntryList
  property_count: 3
  slug: merge-paginatedjournalentrylist
- name: PaginatedLeadList
  property_count: 3
  slug: merge-paginatedleadlist
- name: PaginatedLocationList
  property_count: 3
  slug: merge-paginatedlocationlist
- name: PaginatedMemberList
  property_count: 3
  slug: merge-paginatedmemberlist
- name: PaginatedMessageList
  property_count: 3
  slug: merge-paginatedmessagelist
- name: PaginatedNoteList
  property_count: 3
  slug: merge-paginatednotelist
- name: PaginatedOfferList
  property_count: 3
  slug: merge-paginatedofferlist
- name: PaginatedOfficeList
  property_count: 3
  slug: merge-paginatedofficelist
- name: PaginatedOpportunityList
  property_count: 3
  slug: merge-paginatedopportunitylist
- name: PaginatedPayGroupList
  property_count: 3
  slug: merge-paginatedpaygrouplist
- name: PaginatedPaymentList
  property_count: 3
  slug: merge-paginatedpaymentlist
- name: PaginatedPaymentMethodList
  property_count: 3
  slug: merge-paginatedpaymentmethodlist
- name: PaginatedPaymentTermList
  property_count: 3
  slug: merge-paginatedpaymenttermlist
- name: PaginatedPayrollRunList
  property_count: 3
  slug: merge-paginatedpayrollrunlist
- name: PaginatedProjectList
  property_count: 3
  slug: merge-paginatedprojectlist
- name: PaginatedPublicCombinedCustomRegexRuleList
  property_count: 4
  slug: merge-paginatedpubliccombinedcustomregexrulelist
- name: PaginatedPublicCombinedSecurityRuleList
  property_count: 4
  slug: merge-paginatedpubliccombinedsecurityrulelist
- name: PaginatedPurchaseOrderList
  property_count: 3
  slug: merge-paginatedpurchaseorderlist
- name: PaginatedRegisteredUserPublicResponseList
  property_count: 4
  slug: merge-paginatedregistereduserpublicresponselist
- name: PaginatedRejectReasonList
  property_count: 3
  slug: merge-paginatedrejectreasonlist
- name: PaginatedRemoteFieldClassList
  property_count: 3
  slug: merge-paginatedremotefieldclasslist
- name: PaginatedRemoteUserList
  property_count: 3
  slug: merge-paginatedremoteuserlist
- name: PaginatedRoleList
  property_count: 3
  slug: merge-paginatedrolelist
- name: PaginatedSalesOrderList
  property_count: 3
  slug: merge-paginatedsalesorderlist
- name: PaginatedScheduledInterviewList
  property_count: 3
  slug: merge-paginatedscheduledinterviewlist
- name: PaginatedScorecardList
  property_count: 3
  slug: merge-paginatedscorecardlist
- name: PaginatedScreeningQuestionList
  property_count: 3
  slug: merge-paginatedscreeningquestionlist
- name: PaginatedStageList
  property_count: 3
  slug: merge-paginatedstagelist
- name: PaginatedStandardEntityRuleResponseList
  property_count: 4
  slug: merge-paginatedstandardentityruleresponselist
- name: PaginatedSyncStatusList
  property_count: 3
  slug: merge-paginatedsyncstatuslist
- name: PaginatedTagList
  property_count: 3
  slug: merge-paginatedtaglist
- name: PaginatedTaskList
  property_count: 3
  slug: merge-paginatedtasklist
- name: PaginatedTaxRateList
  property_count: 3
  slug: merge-paginatedtaxratelist
- name: PaginatedTeamList
  property_count: 3
  slug: merge-paginatedteamlist
- name: PaginatedTicketList
  property_count: 3
  slug: merge-paginatedticketlist
- name: PaginatedTimeOffBalanceList
  property_count: 3
  slug: merge-paginatedtimeoffbalancelist
- name: PaginatedTimeOffList
  property_count: 3
  slug: merge-paginatedtimeofflist
- name: PaginatedTimesheetEntryList
  property_count: 3
  slug: merge-paginatedtimesheetentrylist
- name: PaginatedToolDescriptionOverrideList
  property_count: 4
  slug: merge-paginatedtooldescriptionoverridelist
- name: PaginatedToolPackPublicList
  property_count: 4
  slug: merge-paginatedtoolpackpubliclist
- name: PaginatedToolPackToolDescriptionOverrideList
  property_count: 4
  slug: merge-paginatedtoolpacktooldescriptionoverridelist
- name: PaginatedTrackingCategoryList
  property_count: 3
  slug: merge-paginatedtrackingcategorylist
- name: PaginatedTransactionList
  property_count: 3
  slug: merge-paginatedtransactionlist
- name: PaginatedUserList
  property_count: 3
  slug: merge-paginateduserlist
- name: PaginatedVendorCreditList
  property_count: 3
  slug: merge-paginatedvendorcreditlist
- name: PaginatedViewerList
  property_count: 3
  slug: merge-paginatedviewerlist
- name: PatchedAccountRequest
  property_count: 12
  slug: merge-patchedaccountrequest
- name: PatchedApplicationCredentialUpdate
  property_count: 3
  slug: merge-patchedapplicationcredentialupdate
- name: PatchedCandidateEndpointRequest
  property_count: 2
  slug: merge-patchedcandidateendpointrequest
- name: PatchedCandidateRequest
  property_count: 17
  slug: merge-patchedcandidaterequest
- name: PatchedContactEndpointRequest
  property_count: 1
  slug: merge-patchedcontactendpointrequest
- name: PatchedContactRequest
  property_count: 13
  slug: merge-patchedcontactrequest
- name: PatchedCreditNoteEndpointRequest
  property_count: 1
  slug: merge-patchedcreditnoteendpointrequest
- name: PatchedCRMAccountEndpointRequest
  property_count: 1
  slug: merge-patchedcrmaccountendpointrequest
- name: PatchedCRMContactEndpointRequest
  property_count: 1
  slug: merge-patchedcrmcontactendpointrequest
- name: PatchedCustomRegexRuleUpdateInput
  property_count: 7
  slug: merge-patchedcustomregexruleupdateinput
- name: PatchedCustomRegexRuleUpdateInputInboundAction
  property_count: 0
  slug: merge-patchedcustomregexruleupdateinputinboundaction
- name: PatchedCustomRegexRuleUpdateInputOutboundAction
  property_count: 0
  slug: merge-patchedcustomregexruleupdateinputoutboundaction
- name: PatchedEditFieldMappingRequest
  property_count: 5
  slug: merge-patchededitfieldmappingrequest
- name: PatchedEngagementEndpointRequest
  property_count: 1
  slug: merge-patchedengagementendpointrequest
- name: PatchedEngagementRequest
  property_count: 13
  slug: merge-patchedengagementrequest
- name: PatchedInvoiceEndpointRequest
  property_count: 1
  slug: merge-patchedinvoiceendpointrequest
- name: PatchedItemEndpointRequest
  property_count: 1
  slug: merge-patcheditemendpointrequest
- name: PatchedItemRequestRequest
  property_count: 12
  slug: merge-patcheditemrequestrequest
- name: PatchedOpportunityEndpointRequest
  property_count: 1
  slug: merge-patchedopportunityendpointrequest
- name: PatchedOpportunityRequest
  property_count: 13
  slug: merge-patchedopportunityrequest
- name: PatchedPaymentEndpointRequest
  property_count: 1
  slug: merge-patchedpaymentendpointrequest
- name: PatchedPaymentRequest
  property_count: 15
  slug: merge-patchedpaymentrequest
- name: PatchedRegisteredUserPublicRequest
  property_count: 5
  slug: merge-patchedregistereduserpublicrequest
- name: PatchedRegisteredUserPublicRequestUserType
  property_count: 0
  slug: merge-patchedregistereduserpublicrequestusertype
- name: PatchedTicketEndpointRequest
  property_count: 1
  slug: merge-patchedticketendpointrequest
- name: PatchedTicketRequest
  property_count: 21
  slug: merge-patchedticketrequest
- name: PatchedToolPackCustomRegexOverride
  property_count: 10
  slug: merge-patchedtoolpackcustomregexoverride
- name: PatchedToolPackCustomRegexOverrideInboundAction
  property_count: 0
  slug: merge-patchedtoolpackcustomregexoverrideinboundaction
- name: PatchedToolPackCustomRegexOverrideOutboundAction
  property_count: 0
  slug: merge-patchedtoolpackcustomregexoverrideoutboundaction
- name: PatchedToolPackPublicWrite
  property_count: 4
  slug: merge-patchedtoolpackpublicwrite
- name: PatchedVendorCreditEndpointRequest
  property_count: 1
  slug: merge-patchedvendorcreditendpointrequest
- name: PatchedVendorCreditRequest
  property_count: 10
  slug: merge-patchedvendorcreditrequest
- name: PayCurrencyEnum
  property_count: 0
  slug: merge-paycurrencyenum
- name: PayFrequencyEnum
  property_count: 0
  slug: merge-payfrequencyenum
- name: PayGroup
  property_count: 8
  slug: merge-paygroup
- name: PayGroupFieldMappings
  property_count: 2
  slug: merge-paygroupfieldmappings
- name: Payment
  property_count: 21
  slug: merge-payment
- name: PaymentEndpointRequest
  property_count: 1
  slug: merge-paymentendpointrequest
- name: PaymentFieldMappings
  property_count: 2
  slug: merge-paymentfieldmappings
- name: PaymentLineItem
  property_count: 8
  slug: merge-paymentlineitem
- name: PaymentLineItemRequest
  property_count: 8
  slug: merge-paymentlineitemrequest
- name: PaymentMethod
  property_count: 10
  slug: merge-paymentmethod
- name: PaymentMethodFieldMappings
  property_count: 2
  slug: merge-paymentmethodfieldmappings
- name: PaymentRequest
  property_count: 15
  slug: merge-paymentrequest
- name: PaymentResponse
  property_count: 4
  slug: merge-paymentresponse
- name: PaymentsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-paymentsgetparametersexpandschemaitems
- name: PaymentsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-paymentsidgetparametersexpandschemaitems
- name: PaymentTerm
  property_count: 12
  slug: merge-paymentterm
- name: PaymentTermFieldMappings
  property_count: 2
  slug: merge-paymenttermfieldmappings
- name: PaymentTermsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-paymenttermsgetparametersexpandschemaitems
- name: PaymentTermsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-paymenttermsidgetparametersexpandschemaitems
- name: PaymentTypeEnum
  property_count: 0
  slug: merge-paymenttypeenum
- name: PayPeriodEnum
  property_count: 0
  slug: merge-payperiodenum
- name: PayrollRun
  property_count: 12
  slug: merge-payrollrun
- name: PayrollRunFieldMappings
  property_count: 2
  slug: merge-payrollrunfieldmappings
- name: PayrollRunsGetParametersRemoteFields
  property_count: 0
  slug: merge-payrollrunsgetparametersremotefields
- name: PayrollRunsGetParametersRunType
  property_count: 0
  slug: merge-payrollrunsgetparametersruntype
- name: PayrollRunsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-payrollrunsgetparametersshowenumorigins
- name: PayrollRunsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-payrollrunsidgetparametersremotefields
- name: PayrollRunsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-payrollrunsidgetparametersshowenumorigins
- name: Permission
  property_count: 10
  slug: merge-permission
- name: PermissionFieldMappings
  property_count: 2
  slug: merge-permissionfieldmappings
- name: PermissionRequest
  property_count: 7
  slug: merge-permissionrequest
- name: PermissionTypeEnum
  property_count: 0
  slug: merge-permissiontypeenum
- name: PhoneNumber
  property_count: 5
  slug: merge-phonenumber
- name: PhoneNumberRequest
  property_count: 4
  slug: merge-phonenumberrequest
- name: PhoneNumberTypeEnum
  property_count: 0
  slug: merge-phonenumbertypeenum
- name: PolicyTypeEnum
  property_count: 0
  slug: merge-policytypeenum
- name: PostingStatusEnum
  property_count: 0
  slug: merge-postingstatusenum
- name: PriorityEnum
  property_count: 0
  slug: merge-priorityenum
- name: Project
  property_count: 10
  slug: merge-project
- name: ProjectFieldMappings
  property_count: 2
  slug: merge-projectfieldmappings
- name: ProjectsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-projectsgetparametersexpandschemaitems
- name: ProjectsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-projectsidgetparametersexpandschemaitems
- name: PublicCombinedCustomRegexRule
  property_count: 8
  slug: merge-publiccombinedcustomregexrule
- name: PublicCombinedSecurityRule
  property_count: 9
  slug: merge-publiccombinedsecurityrule
- name: PublicModel
  property_count: 7
  slug: merge-publicmodel
- name: PublicModelAvailabilityStatus
  property_count: 0
  slug: merge-publicmodelavailabilitystatus
- name: PublicModelsListResponse
  property_count: 4
  slug: merge-publicmodelslistresponse
- name: PublicVendor
  property_count: 6
  slug: merge-publicvendor
- name: PublicVendorAvailabilityStatus
  property_count: 0
  slug: merge-publicvendoravailabilitystatus
- name: PublicVendorModelCapabilities
  property_count: 6
  slug: merge-publicvendormodelcapabilities
- name: PublicVendorModelCapabilitiesInputItems
  property_count: 0
  slug: merge-publicvendormodelcapabilitiesinputitems
- name: PublicVendorModelCapabilitiesOutputItems
  property_count: 0
  slug: merge-publicvendormodelcapabilitiesoutputitems
- name: PublicVendorModelInfo
  property_count: 6
  slug: merge-publicvendormodelinfo
- name: PublicVendorModelInfoAvailabilityStatus
  property_count: 0
  slug: merge-publicvendormodelinfoavailabilitystatus
- name: PublicVendorsListResponse
  property_count: 4
  slug: merge-publicvendorslistresponse
- name: PurchaseOrder
  property_count: 27
  slug: merge-purchaseorder
- name: PurchaseOrderEndpointRequest
  property_count: 1
  slug: merge-purchaseorderendpointrequest
- name: PurchaseOrderFieldMappings
  property_count: 2
  slug: merge-purchaseorderfieldmappings
- name: PurchaseOrderLineItem
  property_count: 19
  slug: merge-purchaseorderlineitem
- name: PurchaseOrderLineItemRequest
  property_count: 17
  slug: merge-purchaseorderlineitemrequest
- name: PurchaseOrderRequest
  property_count: 18
  slug: merge-purchaseorderrequest
- name: PurchaseOrderResponse
  property_count: 4
  slug: merge-purchaseorderresponse
- name: PurchaseOrdersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-purchaseordersgetparametersexpandschemaitems
- name: PurchaseOrdersGetParametersRemoteFields
  property_count: 0
  slug: merge-purchaseordersgetparametersremotefields
- name: PurchaseOrdersGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-purchaseordersgetparametersshowenumorigins
- name: PurchaseOrdersIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-purchaseordersidgetparametersexpandschemaitems
- name: PurchaseOrdersIdGetParametersRemoteFields
  property_count: 0
  slug: merge-purchaseordersidgetparametersremotefields
- name: PurchaseOrdersIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-purchaseordersidgetparametersshowenumorigins
- name: PurchaseOrderStatusEnum
  property_count: 0
  slug: merge-purchaseorderstatusenum
- name: RaceEnum
  property_count: 0
  slug: merge-raceenum
- name: ReasonEnum
  property_count: 0
  slug: merge-reasonenum
- name: RegenerateAccountToken
  property_count: 2
  slug: merge-regenerateaccounttoken
- name: RegisteredUserPublicRequest
  property_count: 5
  slug: merge-registereduserpublicrequest
- name: RegisteredUserPublicRequestUserType
  property_count: 0
  slug: merge-registereduserpublicrequestusertype
- name: RegisteredUserPublicResponse
  property_count: 7
  slug: merge-registereduserpublicresponse
- name: RejectReason
  property_count: 8
  slug: merge-rejectreason
- name: RejectReasonFieldMappings
  property_count: 2
  slug: merge-rejectreasonfieldmappings
- name: RelationshipEnum
  property_count: 0
  slug: merge-relationshipenum
- name: RemoteData
  property_count: 2
  slug: merge-remotedata
- name: RemoteEndpointInfo
  property_count: 3
  slug: merge-remoteendpointinfo
- name: RemoteField
  property_count: 2
  slug: merge-remotefield
- name: RemoteFieldAPI
  property_count: 6
  slug: merge-remotefieldapi
- name: RemoteFieldApiCoverage
  property_count: 0
  slug: merge-remotefieldapicoverage
- name: RemoteFieldAPIResponse
  property_count: 27
  slug: merge-remotefieldapiresponse
- name: RemoteFieldClass
  property_count: 11
  slug: merge-remotefieldclass
- name: RemoteFieldClassForCustomObjectClass
  property_count: 10
  slug: merge-remotefieldclassforcustomobjectclass
- name: RemoteFieldClassForCustomObjectClassItemSchema
  property_count: 3
  slug: merge-remotefieldclassforcustomobjectclassitemschema
- name: RemoteFieldRequest
  property_count: 2
  slug: merge-remotefieldrequest
- name: RemoteKey
  property_count: 2
  slug: merge-remotekey
- name: RemoteKeyForRegenerationRequest
  property_count: 1
  slug: merge-remotekeyforregenerationrequest
- name: RemoteResponse
  property_count: 7
  slug: merge-remoteresponse
- name: RemoteUser
  property_count: 13
  slug: merge-remoteuser
- name: RemoteUserFieldMappings
  property_count: 2
  slug: merge-remoteuserfieldmappings
- name: ReportItem
  property_count: 8
  slug: merge-reportitem
- name: RequestFormatEnum
  property_count: 0
  slug: merge-requestformatenum
- name: RequestTypeEnum
  property_count: 0
  slug: merge-requesttypeenum
- name: ResponseFormatJson
  property_count: 1
  slug: merge-responseformatjson
- name: ResponseRequest
  property_count: 16
  slug: merge-responserequest
- name: ResponseRequestInputItems
  property_count: 0
  slug: merge-responserequestinputitems
- name: ResponseRequestInputItemsDiscriminatorMappingMessageContent
  property_count: 0
  slug: merge-responserequestinputitemsdiscriminatormappingmessagecontent
- name: ResponseRequestInputItemsDiscriminatorMappingMessageContent1
  property_count: 0
  slug: merge-responserequestinputitemsdiscriminatormappingmessagecontent1
- name: ResponseRequestInputItemsDiscriminatorMappingMessageContentOneOf1Items
  property_count: 0
  slug: merge-responserequestinputitemsdiscriminatormappingmessagecontento
- name: ResponseRequestInputItemsDiscriminatorMappingMessageRole
  property_count: 0
  slug: merge-responserequestinputitemsdiscriminatormappingmessagerole
- name: ResponseRequestToolChoice
  property_count: 0
  slug: merge-responserequesttoolchoice
- name: ResponseResponse
  property_count: 9
  slug: merge-responseresponse
- name: ResponseTypeEnum
  property_count: 0
  slug: merge-responsetypeenum
- name: Role
  property_count: 10
  slug: merge-role
- name: RoleEnum
  property_count: 0
  slug: merge-roleenum
- name: RoleFieldMappings
  property_count: 2
  slug: merge-rolefieldmappings
- name: RolesEnum
  property_count: 0
  slug: merge-rolesenum
- name: Routing_listPolicies_Response_200
  property_count: 2
  slug: merge-routing-listpolicies-response-200
- name: Routing_listStrategies_Response_200
  property_count: 2
  slug: merge-routing-liststrategies-response-200
- name: RoutingLatency
  property_count: 4
  slug: merge-routinglatency
- name: RoutingMetadata
  property_count: 13
  slug: merge-routingmetadata
- name: RoutingPoliciesGetResponsesContentApplicationJsonSchemaDataItemsProvidersItems
  property_count: 2
  slug: merge-routingpoliciesgetresponsescontentapplicationjsonschemadatai
- name: RoutingStrategiesGetResponsesContentApplicationJsonSchemaDataItemsMlRouting
  property_count: 2
  slug: merge-routingstrategiesgetresponsescontentapplicationjsonschemadat
- name: RunStateEnum
  property_count: 0
  slug: merge-runstateenum
- name: RunTypeEnum
  property_count: 0
  slug: merge-runtypeenum
- name: SalesOrder
  property_count: 23
  slug: merge-salesorder
- name: SalesOrderBatchItemRequest
  property_count: 2
  slug: merge-salesorderbatchitemrequest
- name: SalesOrderBulkRequest
  property_count: 1
  slug: merge-salesorderbulkrequest
- name: SalesOrderEndpointRequest
  property_count: 1
  slug: merge-salesorderendpointrequest
- name: SalesOrderFieldMappings
  property_count: 2
  slug: merge-salesorderfieldmappings
- name: SalesOrderLine
  property_count: 15
  slug: merge-salesorderline
- name: SalesOrderLineRequest
  property_count: 13
  slug: merge-salesorderlinerequest
- name: SalesOrderRequestRequest
  property_count: 16
  slug: merge-salesorderrequestrequest
- name: SalesOrderResponse
  property_count: 4
  slug: merge-salesorderresponse
- name: SalesOrdersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-salesordersgetparametersexpandschemaitems
- name: SalesOrdersGetParametersRemoteFields
  property_count: 0
  slug: merge-salesordersgetparametersremotefields
- name: SalesOrdersGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-salesordersgetparametersshowenumorigins
- name: SalesOrdersIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-salesordersidgetparametersexpandschemaitems
- name: SalesOrdersIdGetParametersRemoteFields
  property_count: 0
  slug: merge-salesordersidgetparametersremotefields
- name: SalesOrdersIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-salesordersidgetparametersshowenumorigins
- name: SalesOrderStatusEnum
  property_count: 0
  slug: merge-salesorderstatusenum
- name: ScheduledInterview
  property_count: 17
  slug: merge-scheduledinterview
- name: ScheduledInterviewEndpointRequest
  property_count: 2
  slug: merge-scheduledinterviewendpointrequest
- name: ScheduledInterviewFieldMappings
  property_count: 2
  slug: merge-scheduledinterviewfieldmappings
- name: ScheduledInterviewRequest
  property_count: 10
  slug: merge-scheduledinterviewrequest
- name: ScheduledInterviewResponse
  property_count: 4
  slug: merge-scheduledinterviewresponse
- name: ScheduledInterviewStatusEnum
  property_count: 0
  slug: merge-scheduledinterviewstatusenum
- name: Scorecard
  property_count: 13
  slug: merge-scorecard
- name: ScorecardFieldMappings
  property_count: 2
  slug: merge-scorecardfieldmappings
- name: ScorecardsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-scorecardsgetparametersexpandschemaitems
- name: ScorecardsGetParametersRemoteFields
  property_count: 0
  slug: merge-scorecardsgetparametersremotefields
- name: ScorecardsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-scorecardsgetparametersshowenumorigins
- name: ScorecardsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-scorecardsidgetparametersexpandschemaitems
- name: ScorecardsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-scorecardsidgetparametersremotefields
- name: ScorecardsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-scorecardsidgetparametersshowenumorigins
- name: ScreeningQuestion
  property_count: 11
  slug: merge-screeningquestion
- name: ScreeningQuestionAnswer
  property_count: 7
  slug: merge-screeningquestionanswer
- name: ScreeningQuestionAnswerRequest
  property_count: 5
  slug: merge-screeningquestionanswerrequest
- name: ScreeningQuestionOption
  property_count: 6
  slug: merge-screeningquestionoption
- name: ScreeningQuestionTypeEnum
  property_count: 0
  slug: merge-screeningquestiontypeenum
- name: SecretOptionPublic
  property_count: 3
  slug: merge-secretoptionpublic
- name: SecretSchemaPublic
  property_count: 6
  slug: merge-secretschemapublic
- name: SelectiveSyncConfigurationsUsageEnum
  property_count: 0
  slug: merge-selectivesyncconfigurationsusageenum
- name: SharedCredentialGroup
  property_count: 3
  slug: merge-sharedcredentialgroup
- name: Stage
  property_count: 9
  slug: merge-stage
- name: StageFieldMappings
  property_count: 2
  slug: merge-stagefieldmappings
- name: StandardEntityOverridePutInput
  property_count: 3
  slug: merge-standardentityoverrideputinput
- name: StandardEntityOverridePutInputInboundAction
  property_count: 0
  slug: merge-standardentityoverrideputinputinboundaction
- name: StandardEntityOverridePutInputOutboundAction
  property_count: 0
  slug: merge-standardentityoverrideputinputoutboundaction
- name: StandardEntityRulePutInput
  property_count: 3
  slug: merge-standardentityruleputinput
- name: StandardEntityRulePutInputInboundAction
  property_count: 0
  slug: merge-standardentityruleputinputinboundaction
- name: StandardEntityRulePutInputOutboundAction
  property_count: 0
  slug: merge-standardentityruleputinputoutboundaction
- name: StandardEntityRuleResponse
  property_count: 7
  slug: merge-standardentityruleresponse
- name: StandardEntityRuleResponseOutboundAction
  property_count: 0
  slug: merge-standardentityruleresponseoutboundaction
- name: Status3c6Enum
  property_count: 0
  slug: merge-status3c6enum
- name: Status7d1Enum
  property_count: 0
  slug: merge-status7d1enum
- name: Status895Enum
  property_count: 0
  slug: merge-status895enum
- name: StatusFd5Enum
  property_count: 0
  slug: merge-statusfd5enum
- name: SyncStatus
  property_count: 9
  slug: merge-syncstatus
- name: Tag
  property_count: 7
  slug: merge-tag
- name: TagFieldMappings
  property_count: 2
  slug: merge-tagfieldmappings
- name: TagInput
  property_count: 2
  slug: merge-taginput
- name: TagSchema
  property_count: 8
  slug: merge-tagschema
- name: TagsListResponse
  property_count: 4
  slug: merge-tagslistresponse
- name: Task
  property_count: 18
  slug: merge-task
- name: TaskEndpointRequest
  property_count: 1
  slug: merge-taskendpointrequest
- name: TaskFieldMappings
  property_count: 2
  slug: merge-taskfieldmappings
- name: TaskRequest
  property_count: 13
  slug: merge-taskrequest
- name: TaskResponse
  property_count: 4
  slug: merge-taskresponse
- name: TasksGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-tasksgetparametersexpandschemaitems
- name: TasksIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-tasksidgetparametersexpandschemaitems
- name: TaskStatusEnum
  property_count: 0
  slug: merge-taskstatusenum
- name: Tax
  property_count: 11
  slug: merge-tax
- name: TaxComponent
  property_count: 9
  slug: merge-taxcomponent
- name: TaxFieldMappings
  property_count: 2
  slug: merge-taxfieldmappings
- name: TaxRate
  property_count: 16
  slug: merge-taxrate
- name: TaxRateFieldMappings
  property_count: 2
  slug: merge-taxratefieldmappings
- name: TaxRatesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-taxratesgetparametersexpandschemaitems
- name: TaxRatesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-taxratesidgetparametersexpandschemaitems
- name: Team
  property_count: 9
  slug: merge-team
- name: TeamFieldMappings
  property_count: 2
  slug: merge-teamfieldmappings
- name: Ticket
  property_count: 30
  slug: merge-ticket
- name: TicketAccessEnum
  property_count: 0
  slug: merge-ticketaccessenum
- name: TicketAccessLevelEnum
  property_count: 0
  slug: merge-ticketaccesslevelenum
- name: TicketActionsEnum
  property_count: 0
  slug: merge-ticketactionsenum
- name: TicketEndpointRequest
  property_count: 1
  slug: merge-ticketendpointrequest
- name: TicketFieldMappings
  property_count: 2
  slug: merge-ticketfieldmappings
- name: TicketingAttachmentEndpointRequest
  property_count: 1
  slug: merge-ticketingattachmentendpointrequest
- name: TicketingAttachmentResponse
  property_count: 4
  slug: merge-ticketingattachmentresponse
- name: TicketingContactEndpointRequest
  property_count: 1
  slug: merge-ticketingcontactendpointrequest
- name: TicketingContactResponse
  property_count: 4
  slug: merge-ticketingcontactresponse
- name: TicketRequest
  property_count: 22
  slug: merge-ticketrequest
- name: TicketResponse
  property_count: 4
  slug: merge-ticketresponse
- name: TicketsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-ticketsgetparametersexpandschemaitems
- name: TicketsGetParametersPriority
  property_count: 0
  slug: merge-ticketsgetparameterspriority
- name: TicketsGetParametersRemoteFields
  property_count: 0
  slug: merge-ticketsgetparametersremotefields
- name: TicketsGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-ticketsgetparametersshowenumorigins
- name: TicketsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-ticketsidgetparametersexpandschemaitems
- name: TicketsIdGetParametersRemoteFields
  property_count: 0
  slug: merge-ticketsidgetparametersremotefields
- name: TicketsIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-ticketsidgetparametersshowenumorigins
- name: TicketsLiveSearchGetParametersRemoteFields
  property_count: 0
  slug: merge-ticketslivesearchgetparametersremotefields
- name: TicketsLiveSearchGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-ticketslivesearchgetparametersshowenumorigins
- name: TicketStatusEnum
  property_count: 0
  slug: merge-ticketstatusenum
- name: TicketsTicketIdViewersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-ticketsticketidviewersgetparametersexpandschemaitems
- name: TimeOff
  property_count: 16
  slug: merge-timeoff
- name: TimeOffBalance
  property_count: 11
  slug: merge-timeoffbalance
- name: TimeOffBalanceFieldMappings
  property_count: 2
  slug: merge-timeoffbalancefieldmappings
- name: TimeOffBalancesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-timeoffbalancesgetparametersexpandschemaitems
- name: TimeOffBalancesGetParametersPolicyType
  property_count: 0
  slug: merge-timeoffbalancesgetparameterspolicytype
- name: TimeOffBalancesGetParametersRemoteFields
  property_count: 0
  slug: merge-timeoffbalancesgetparametersremotefields
- name: TimeOffBalancesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-timeoffbalancesgetparametersshowenumorigins
- name: TimeOffBalancesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-timeoffbalancesidgetparametersexpandschemaitems
- name: TimeOffBalancesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-timeoffbalancesidgetparametersremotefields
- name: TimeOffBalancesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-timeoffbalancesidgetparametersshowenumorigins
- name: TimeOffEndpointRequest
  property_count: 1
  slug: merge-timeoffendpointrequest
- name: TimeOffFieldMappings
  property_count: 2
  slug: merge-timeofffieldmappings
- name: TimeOffGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-timeoffgetparametersexpandschemaitems
- name: TimeOffGetParametersRemoteFields
  property_count: 0
  slug: merge-timeoffgetparametersremotefields
- name: TimeOffGetParametersRequestType
  property_count: 0
  slug: merge-timeoffgetparametersrequesttype
- name: TimeOffGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-timeoffgetparametersshowenumorigins
- name: TimeOffGetParametersStatus
  property_count: 0
  slug: merge-timeoffgetparametersstatus
- name: TimeOffIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-timeoffidgetparametersexpandschemaitems
- name: TimeOffIdGetParametersRemoteFields
  property_count: 0
  slug: merge-timeoffidgetparametersremotefields
- name: TimeOffIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-timeoffidgetparametersshowenumorigins
- name: TimeOffRequest
  property_count: 11
  slug: merge-timeoffrequest
- name: TimeOffResponse
  property_count: 4
  slug: merge-timeoffresponse
- name: TimeOffStatusEnum
  property_count: 0
  slug: merge-timeoffstatusenum
- name: TimesheetEntriesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-timesheetentriesgetparametersexpandschemaitems
- name: TimesheetEntriesGetParametersOrderBy
  property_count: 0
  slug: merge-timesheetentriesgetparametersorderby
- name: TimesheetEntriesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-timesheetentriesidgetparametersexpandschemaitems
- name: TimesheetEntry
  property_count: 11
  slug: merge-timesheetentry
- name: TimesheetEntryEndpointRequest
  property_count: 1
  slug: merge-timesheetentryendpointrequest
- name: TimesheetEntryFieldMappings
  property_count: 2
  slug: merge-timesheetentryfieldmappings
- name: TimesheetEntryRequest
  property_count: 6
  slug: merge-timesheetentryrequest
- name: TimesheetEntryResponse
  property_count: 4
  slug: merge-timesheetentryresponse
- name: ToolDescriptionOverride
  property_count: 7
  slug: merge-tooldescriptionoverride
- name: ToolPackConnectorBulkInput
  property_count: 4
  slug: merge-toolpackconnectorbulkinput
- name: ToolPackConnectorBulkInputAuthScope
  property_count: 0
  slug: merge-toolpackconnectorbulkinputauthscope
- name: ToolPackConnectorInput
  property_count: 4
  slug: merge-toolpackconnectorinput
- name: ToolPackConnectorInputAuthScope
  property_count: 0
  slug: merge-toolpackconnectorinputauthscope
- name: ToolPackPublic
  property_count: 4
  slug: merge-toolpackpublic
- name: ToolPackPublicWrite
  property_count: 4
  slug: merge-toolpackpublicwrite
- name: ToolResultInputContent
  property_count: 0
  slug: merge-toolresultinputcontent
- name: ToolResultInputContent1
  property_count: 0
  slug: merge-toolresultinputcontent1
- name: ToolResultInputContentOneOf1Items
  property_count: 0
  slug: merge-toolresultinputcontentoneof1items
- name: toolSearch_searchTools_Response_200
  property_count: 3
  slug: merge-toolsearch-searchtools-response-200
- name: ToolSearchRequest
  property_count: 3
  slug: merge-toolsearchrequest
- name: TrackingCategoriesGetParametersCategoryType
  property_count: 0
  slug: merge-trackingcategoriesgetparameterscategorytype
- name: TrackingCategoriesGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-trackingcategoriesgetparametersexpandschemaitems
- name: TrackingCategoriesGetParametersRemoteFields
  property_count: 0
  slug: merge-trackingcategoriesgetparametersremotefields
- name: TrackingCategoriesGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-trackingcategoriesgetparametersshowenumorigins
- name: TrackingCategoriesGetParametersStatus
  property_count: 0
  slug: merge-trackingcategoriesgetparametersstatus
- name: TrackingCategoriesIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-trackingcategoriesidgetparametersexpandschemaitems
- name: TrackingCategoriesIdGetParametersRemoteFields
  property_count: 0
  slug: merge-trackingcategoriesidgetparametersremotefields
- name: TrackingCategoriesIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-trackingcategoriesidgetparametersshowenumorigins
- name: TrackingCategory
  property_count: 11
  slug: merge-trackingcategory
- name: TrackingCategoryFieldMappings
  property_count: 2
  slug: merge-trackingcategoryfieldmappings
- name: Transaction
  property_count: 20
  slug: merge-transaction
- name: TransactionCurrencyEnum
  property_count: 0
  slug: merge-transactioncurrencyenum
- name: TransactionFieldMappings
  property_count: 2
  slug: merge-transactionfieldmappings
- name: TransactionLineItem
  property_count: 17
  slug: merge-transactionlineitem
- name: TransactionsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-transactionsgetparametersexpandschemaitems
- name: TransactionsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-transactionsidgetparametersexpandschemaitems
- name: Type2bbEnum
  property_count: 0
  slug: merge-type2bbenum
- name: TypeEnum
  property_count: 0
  slug: merge-typeenum
- name: UnitsEnum
  property_count: 0
  slug: merge-unitsenum
- name: UpdateApplicationStageRequest
  property_count: 2
  slug: merge-updateapplicationstagerequest
- name: Url
  property_count: 5
  slug: merge-url
- name: UrlRequest
  property_count: 4
  slug: merge-urlrequest
- name: UrlTypeEnum
  property_count: 0
  slug: merge-urltypeenum
- name: Usage
  property_count: 3
  slug: merge-usage
- name: User
  property_count: 16
  slug: merge-user
- name: UserFieldMappings
  property_count: 2
  slug: merge-userfieldmappings
- name: users_ignoreCreate_Response_200
  property_count: 0
  slug: merge-users-ignorecreate-response-200
- name: UsersGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-usersgetparametersexpandschemaitems
- name: UsersGetParametersRemoteFields
  property_count: 0
  slug: merge-usersgetparametersremotefields
- name: UsersGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-usersgetparametersshowenumorigins
- name: UsersIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-usersidgetparametersexpandschemaitems
- name: UsersIdGetParametersRemoteFields
  property_count: 0
  slug: merge-usersidgetparametersremotefields
- name: UsersIdGetParametersShowEnumOrigins
  property_count: 0
  slug: merge-usersidgetparametersshowenumorigins
- name: ValidationError
  property_count: 5
  slug: merge-validationerror
- name: ValidationErrorCtx
  property_count: 0
  slug: merge-validationerrorctx
- name: ValidationErrorLocItems
  property_count: 0
  slug: merge-validationerrorlocitems
- name: ValidationProblemSource
  property_count: 1
  slug: merge-validationproblemsource
- name: VendorCredit
  property_count: 19
  slug: merge-vendorcredit
- name: VendorCreditApplyLineForInvoice
  property_count: 7
  slug: merge-vendorcreditapplylineforinvoice
- name: VendorCreditApplyLineForVendorCredit
  property_count: 7
  slug: merge-vendorcreditapplylineforvendorcredit
- name: VendorCreditApplyLineForVendorCreditRequest
  property_count: 6
  slug: merge-vendorcreditapplylineforvendorcreditrequest
- name: VendorCreditEndpointRequest
  property_count: 1
  slug: merge-vendorcreditendpointrequest
- name: VendorCreditFieldMappings
  property_count: 2
  slug: merge-vendorcreditfieldmappings
- name: VendorCreditLine
  property_count: 15
  slug: merge-vendorcreditline
- name: VendorCreditRequest
  property_count: 13
  slug: merge-vendorcreditrequest
- name: VendorCreditResponse
  property_count: 4
  slug: merge-vendorcreditresponse
- name: VendorCreditsGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-vendorcreditsgetparametersexpandschemaitems
- name: VendorCreditsIdGetParametersExpandSchemaItems
  property_count: 0
  slug: merge-vendorcreditsidgetparametersexpandschemaitems
- name: VeteranStatusEnum
  property_count: 0
  slug: merge-veteranstatusenum
- name: Viewer
  property_count: 6
  slug: merge-viewer
- name: VisibilityEnum
  property_count: 0
  slug: merge-visibilityenum
- name: WarningValidationProblem
  property_count: 7
  slug: merge-warningvalidationproblem
- name: Ticket
  property_count: 19
  slug: ticketing-api-ticket
json_structures:
- name: Accounting Api Invoice Structure
  property_count: 17
  slug: accounting-api-invoice-structure
- name: Agent Handler Tool Pack Structure
  property_count: 10
  slug: agent-handler-tool-pack-structure
- name: Ats Api Candidate Structure
  property_count: 14
  slug: ats-api-candidate-structure
- name: Chat Api Message Structure
  property_count: 13
  slug: chat-api-message-structure
- name: Crm Api Opportunity Structure
  property_count: 14
  slug: crm-api-opportunity-structure
- name: File Storage Api File Structure
  property_count: 13
  slug: file-storage-api-file-structure
- name: Gateway Response Structure
  property_count: 8
  slug: gateway-response-structure
- name: Hris Api Employee Structure
  property_count: 21
  slug: hris-api-employee-structure
- name: Knowledge Base Api Article Structure
  property_count: 11
  slug: knowledge-base-api-article-structure
- name: Merge Structure
  property_count: 0
  slug: merge-structure
- name: Ticketing Api Ticket Structure
  property_count: 16
  slug: ticketing-api-ticket-structure
jsonld:
- class_count: 10
  name: Merge Accounting Api Context
  property_count: 24
  slug: merge-accounting-api-context
- class_count: 6
  name: Merge Agent Handler Context
  property_count: 10
  slug: merge-agent-handler-context
- class_count: 11
  name: Merge Ats Api Context
  property_count: 33
  slug: merge-ats-api-context
- class_count: 5
  name: Merge Chat Api Context
  property_count: 13
  slug: merge-chat-api-context
- class_count: 7
  name: Merge Crm Api Context
  property_count: 22
  slug: merge-crm-api-context
- class_count: 5
  name: Merge File Storage Api Context
  property_count: 17
  slug: merge-file-storage-api-context
- class_count: 7
  name: Merge Gateway Context
  property_count: 14
  slug: merge-gateway-context
- class_count: 13
  name: Merge Hris Api Context
  property_count: 39
  slug: merge-hris-api-context
- class_count: 6
  name: Merge Knowledge Base Api Context
  property_count: 14
  slug: merge-knowledge-base-api-context
- class_count: 4
  name: Merge Ticketing Api Context
  property_count: 20
  slug: merge-ticketing-api-context
layout: provider
mcp_servers:
- description: Python MCP server for the Merge Unified API.
  name: Merge MCP Server
  slug: merge-mcp-server
- description: Remote MCP server at ah-api.merge.dev over HTTP.
  name: Merge MCP Server
  slug: merge
modified: '2026-05-22'
name: Merge
nav: Providers
network: true
overview: 'Merge publishes 118 API contracts indexed on the [APIs.io](https://apis.io/) network, including Subpackage Access Keys API, Subpackage Account Details API, Subpackage Accounting Periods API, and 115 more. Tagged areas include Integration, Platform, Unified API, Agent Handler, and LLM Gateway.


  The Merge catalog on APIs.io includes 10 JSON-LD contexts and 2 Spectral governance rulesets.


  Merge''s developer surface includes pricing, authentication, engineering blog, support, changelog, documentation, signup flow, and 72 more developer resources.'
plans:
- name: Merge Plans Pricing
  plan_count: 3
  slug: merge-plans-pricing
- name: Merge Price Estimates
  plan_count: 0
  slug: merge-price-estimates
random_paper: 0
rate_limits:
- limit_count: 3
  name: Merge Rate Limits
  slug: merge-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Merge — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: merge-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Merge API Rules
  rule_count: 41
  severity_counts:
    error: 15
    hint: 0
    info: 7
    warn: 19
  slug: merge-spectral-rules
score:
  band: exemplar
  composite: 73.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 91.0
    catalog_earned_first_party: 24.0
    catalog_gap: 24.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 86.8
    contract_governance: 27.3
    contract_quality: 67.5
    developer_ergonomics: 52.4
    discoverability: 81.7
    operational_transparency: 78.9
  previous_composite: 73.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 117
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/merge/merge-2026-06-20T185219.png
security:
- kind: authentication
  name: Merge Authentication
  slug: merge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Merge Domain Security
  slug: merge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Merge Vulnerability Disclosure
  slug: merge-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Merge Trust Center
  slug: merge-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: merge
solutions:
- description: Single API for 80+ HR and payroll platforms.
  name: Unified HRIS
- description: Single API for 50+ applicant tracking systems.
  name: Unified ATS
- description: Single API for major accounting platforms.
  name: Unified Accounting
- description: Single API for 30+ ticketing and project management systems.
  name: Unified Ticketing
- description: Single API for 20+ CRM platforms.
  name: Unified CRM
- description: Single API for file storage platforms with File Picker.
  name: Unified File Storage
- description: Single API for Confluence, Notion, with ACL mapping for AI search/context.
  name: Unified Knowledge Base
- description: Single API for Microsoft Teams (Slack on roadmap) with five normalized object types.
  name: Unified Chat
- description: AI agent tool orchestration for thousands of pre-built integrations via REST + MCP.
  name: Agent Handler
- description: Unified LLM API across OpenAI, Anthropic, Google, Mistral, Cohere, xAI with routing and observability.
  name: Merge Gateway
tags:
- Integration
- Platform
- Unified API
- Agent Handler
- LLM Gateway
- Accounting
use_cases:
- name: Power AI features
- name: Auto-provision
- name: Knowledge base for AI
- name: Financial analysis
- name: Candidate sourcing
- name: Project analysis
- name: Source leads
- name: Reconcile vendor payments
- name: Reconcile customer payments
- name: Enterprise search
- name: Customer support monitoring
- name: Document management
- name: Agentic tool use
- name: Multi-vendor LLM routing
website: https://www.merge.dev/
---
