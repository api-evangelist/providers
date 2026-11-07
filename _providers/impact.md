---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
api_count: 69
apis:
- description: Remote Model Context Protocol server for impact.com. Fifteen documented tools give an AI assistant account-scoped access to performance analytics, invoices, partner and program discovery, promo codes,
  name: Impact MCP Server
  slug: mcp-server
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Account API from Impact — 2 operation(s) for account.
  name: Impact Account API
  phrasing_intents:
  - id: upsertAccount
    intent: Create or update a referral account
    question: How do I tell impact.com that an account's subscription status changed?
  - id: getAccount
    intent: Look up a referral account
    question: What information is stored for one referral account?
  phrasing_ops: 2
  slug: impact-account-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for managing partner company account information.
  name: Impact Accounts API
  phrasing_intents:
  - id: retrieveCompanyInformation
    intent: Get a partner's company profile
    question: What profile details are on my partner account?
  - id: updateCompanyInformation
    intent: Update a partner's company profile
    question: How do I update my partner profile description and logo?
  phrasing_ops: 2
  slug: impact-accounts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Action Inquiries API from Impact — 4 operation(s) for action inquiries.
  name: Impact Action Inquiries API
  phrasing_intents:
  - id: listActionInquiries
    intent: List inquiries partners raised on a campaign
    question: Which missing-commission inquiries have partners filed against my campaign?
  - id: updateActionInquiry
    intent: Resolve an action inquiry
    question: How do I approve or reject a partner's action inquiry?
  - id: getActionInquiryById
    intent: Get an inquiry's details as a brand
    question: What did a partner claim in a specific action inquiry on my program?
  - id: getMediapartnersByAccountSIDActionInquiries
    intent: List a partner's action inquiries
    question: Which action inquiries have I submitted as a partner?
  - id: createActionInquiry
    intent: File an action inquiry for a missing sale
    question: How do I claim a sale that wasn't tracked?
  - id: retrieveActionInquiry
    intent: Check one of my action inquiries
    question: What's the status of an inquiry I filed as a partner?
  phrasing_ops: 6
  slug: impact-action-inquiries-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Action Updates API from Impact — 2 operation(s) for action updates.
  name: Impact Action Updates API
  phrasing_intents:
  - id: listActionUpdates
    intent: List the changelog of a brand's actions
    question: Which actions in my program changed state or amount recently?
  - id: getActionUpdateById
    intent: Get one action update record
    question: What exactly changed in one specific action update?
  phrasing_ops: 2
  slug: impact-action-updates-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Actions API from Impact — 10 operation(s) for actions.
  name: Impact Actions API
  phrasing_intents:
  - id: listActions
    intent: List actions recorded for a brand's program
    question: Which conversions has my brand program recorded as actions over the last month?
  - id: updateActionOrItems
    intent: Update an action or its line items
    question: Can I change the amount or quantity on a line item of an action a partner already earned?
  - id: reverseAction
    intent: Reverse an action and cancel its payout
    question: How do I reverse a fraudulent conversion so the partner doesn't get paid for it?
  - id: getActionById
    intent: Get a brand action's details
    question: Where can a brand see the full record of one specific action by its ID?
  - id: listActionItems
    intent: List the line items in a brand action
    question: Which products were part of an order a partner drove for my brand?
  - id: getActionItemBySku
    intent: Get one line item of a brand action by SKU
    question: Can a brand look up a single product line inside an action using its SKU?
  - id: getMediapartnersByAccountSIDActions
    intent: List actions attributed to a partner
    question: Which conversions have been credited to me as a partner in the past week?
  - id: retrieveAction
    intent: Retrieve an action credited to a partner
    question: As a partner, how can I see the full details of one action I earned?
  phrasing_ops: 12
  slug: impact-actions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Ads API from Impact — 7 operation(s) for ads.
  name: Impact Ads API
  phrasing_intents:
  - id: listAds
    intent: List a brand's ads
    question: Which ads has my brand created on impact.com, newest first?
  - id: createAd
    intent: Create a banner, coupon or text link ad
    question: How do I create a new banner ad for my program?
  - id: getAdById
    intent: Get a brand ad's details
    question: What are the settings on one of the ads my brand created?
  - id: updateAd
    intent: Update an existing ad
    question: How do I swap the creative on an ad I already published?
  - id: getMediapartnersByAccountSIDAds
    intent: List ads available to a partner
    question: What ads can I promote as a partner?
  - id: retrieveAd
    intent: Retrieve an ad as a partner
    question: What details does a partner get about a single ad?
  - id: retrieveAdCode
    intent: Get an ad's HTML code
    question: How do I get the HTML embed code for an ad?
  - id: retrieveAdIFrameCode
    intent: Get an ad's iframe code
    question: Is there an iframe version of an ad I can drop into my site?
  phrasing_ops: 9
  slug: impact-ads-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Advertiser accounts managed by this agency.
  name: Impact Advertisers API
  phrasing_intents:
  - id: listAdvertisers
    intent: List an agency's advertisers
    question: Which advertisers does my agency manage on impact.com?
  - id: getAdvertiser
    intent: Get one advertiser my agency manages
    question: What are the full account details for one advertiser I manage?
  phrasing_ops: 2
  slug: impact-advertisers-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The API Submissions API from Impact — 2 operation(s) for api submissions.
  name: Impact API Submissions API
  phrasing_intents:
  - id: listApiSubmissions
    intent: List API conversion submissions
    question: Which records have I submitted through the API?
  - id: getApiSubmissionById
    intent: Get an API submission's status and errors
    question: Did a conversion I sent through the API process successfully?
  phrasing_ops: 2
  slug: impact-api-submissions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Call Data API from Impact — 1 operation(s) for call data.
  name: Impact Call Data API
  phrasing_intents:
  - id: logCallDataGet
    intent: Log a tracked phone call via query string
    question: How do I send call tracking data to impact.com with a simple GET URL?
  - id: logCallDataPost
    intent: Log a tracked phone call via form post
    question: Can I post call tracking data as a form-encoded body instead of a URL?
  phrasing_ops: 2
  slug: impact-call-data-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Catalog Items API from Impact — 3 operation(s) for catalog items.
  name: Impact Catalog Items API
  phrasing_intents:
  - id: listCatalogItems
    intent: List or search items in a product catalog
    question: Which products are in one of my brand's catalogs?
  - id: createCatalogItem
    intent: Add a product to a catalog
    question: How do I add a new product to a catalog so partners can promote it?
  - id: getCatalogItemById
    intent: Get a catalog item's details
    question: What price and stock status does one catalog product currently have?
  - id: updateCatalogItem
    intent: Update a single catalog item
    question: Can I change the price or stock availability of one product in my catalog?
  - id: deleteCatalogItem
    intent: Delete a catalog item
    question: Can I remove a discontinued product from a catalog?
  - id: bulkUpdateCatalogItems
    intent: Bulk update up to 500 catalog items
    question: How do I update prices on hundreds of catalog products in one request?
  phrasing_ops: 6
  slug: impact-catalog-items-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Catalogs API from Impact — 8 operation(s) for catalogs.
  name: Impact Catalogs API
  phrasing_intents:
  - id: listCatalogs
    intent: List a brand's product catalogs
    question: Which product catalogs does my brand have on impact.com?
  - id: getCatalogById
    intent: Get a brand catalog's details
    question: What settings does one of my brand's catalogs have?
  - id: updateCatalogPullSettings
    intent: Update a catalog's pull-from-URL settings
    question: How do I make a catalog sync automatically from a remote file URL?
  - id: uploadCatalogFile
    intent: Upload a full catalog file
    question: Can I replace an entire product catalog by uploading one file?
  - id: getMediapartnersByAccountSIDCatalogs
    intent: List catalogs available to a partner
    question: What product catalogs can I access as a partner?
  - id: retrieveCatalog
    intent: Retrieve a catalog as a partner
    question: What details can a partner see about a brand's catalog?
  - id: listCatalogItems
    intent: List the items in one catalog
    question: What products are in a particular catalog?
  - id: retrieveCatalogItem
    intent: Retrieve a single catalog item
    question: How do I get the details of one product in a catalog?
  phrasing_ops: 9
  slug: impact-catalogs-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The ClickExport API from Impact — 2 operation(s) for clickexport.
  name: Impact Click Export API
  phrasing_intents:
  - id: exportClicks
    intent: Export a brand program's daily clicks
    question: Can my brand export all clicks on a program for a given day?
  - id: getMediapartnersByAccountSIDClickExport
    intent: Export a partner's clicks
    question: As a partner, how can I export the clicks I sent?
  phrasing_ops: 2
  slug: impact-clickexport-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Clicks API from Impact — 2 operation(s) for clicks.
  name: Impact Clicks API
  phrasing_intents:
  - id: getClickById
    intent: Get click details on a brand campaign
    question: How do I look up a click by its im_ref on my campaign?
  - id: retrieveClick
    intent: Retrieve a click as a partner
    question: As a partner, can I see details of a click I drove?
  phrasing_ops: 2
  slug: impact-clicks-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Your agency's company profile, addresses, and key contacts.
  name: Impact Company Information API
  phrasing_intents:
  - id: getCompanyInformation
    intent: Get an agency's company profile
    question: What company details does impact.com hold for my agency?
  - id: updateCompanyInformation
    intent: Update an agency's company profile
    question: Can my agency change its timezone or currency through the API?
  - id: getAdvertisersByAccountSIDCompanyInformation
    intent: Get a brand's company information
    question: What company details are on my brand account?
  - id: putAdvertisersByAccountSIDCompanyInformation
    intent: Update a brand's company information
    question: How do I change my brand's billing address?
  phrasing_ops: 4
  slug: impact-company-information-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Submit content for impact.com compliance monitoring and retrieve job status and results.
  name: Impact Compliance Content API
  phrasing_intents:
  - id: createComplianceContent
    intent: Submit content for compliance monitoring
    question: How can my agency send partner web pages to be checked for brand compliance?
  - id: getComplianceSubmissionStatus
    intent: Check a compliance submission's status
    question: Has my compliance content submission finished processing?
  - id: getComplianceSubmissionResults
    intent: Get per-item compliance results
    question: Which items in my compliance submission passed or failed?
  phrasing_ops: 3
  slug: impact-compliance-content-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Contacts API from Impact — 2 operation(s) for contacts.
  name: Impact Contacts API
  phrasing_intents:
  - id: listContacts
    intent: List contacts on a campaign
    question: Who are the partner contacts on my campaign?
  - id: createContact
    intent: Add a partner contact
    question: How do I add a new contact for a partner account?
  - id: getContactById
    intent: Get a contact's details
    question: What info do I have on a specific partner contact?
  - id: updateContact
    intent: Update a contact
    question: Can I change a system-created contact's title?
  - id: deleteContact
    intent: Delete a contact
    question: Can I permanently remove a contact I created?
  phrasing_ops: 5
  slug: impact-contacts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Contracts API from Impact — 5 operation(s) for contracts.
  name: Impact Contracts API
  phrasing_intents:
  - id: listContracts
    intent: List partner contracts on a brand campaign
    question: Which partner contracts are active on my campaign?
  - id: getContractById
    intent: Get a contract's details as a brand
    question: What terms are in a specific partner contract on my campaign?
  - id: acceptContract
    intent: Accept a pending partner contract
    question: How do I accept a contract proposal a partner is waiting on?
  - id: declineContract
    intent: Decline a pending partner contract
    question: How do I turn down a partner's pending contract proposal?
  - id: getMediapartnersByAccountSIDContracts
    intent: List a partner's contracts
    question: What contracts do I hold as a partner across brands?
  - id: retrieveContract
    intent: Retrieve a contract as a partner
    question: What are the payout terms in one of my partner contracts?
  phrasing_ops: 6
  slug: impact-contracts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Conversions API from Impact — 2 operation(s) for conversions.
  name: Impact Conversions API
  phrasing_intents:
  - id: submitConversion
    intent: Submit a conversion as a brand
    question: How does my brand report a sale to impact.com for attribution?
  - id: createConversion
    intent: Submit a conversion as a partner
    question: Can a partner post their own conversion events to impact.com?
  phrasing_ops: 2
  slug: impact-conversions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Deals API from Impact — 4 operation(s) for deals.
  name: Impact Deals API
  phrasing_intents:
  - id: listDeals
    intent: List a brand's deals
    question: Which deals has my brand set up across programs?
  - id: createDeal
    intent: Create a deal
    question: How do I set up a percent-off or BOGO deal for my partners to promote?
  - id: getDealById
    intent: Get a brand's deal details
    question: What are the terms of one of my brand's deals?
  - id: updateDeal
    intent: Update a deal
    question: Can I extend a deal's end date or change its discount after it's live?
  - id: deleteDeal
    intent: Delete a deal permanently
    question: Can a deal I no longer run be removed entirely?
  - id: getMediapartnersByAccountSIDCampaignsByCampaignIdDeals
    intent: List deals in a program a partner joined
    question: Which deals can I promote as a partner in a given program?
  - id: retrieveDeal
    intent: Retrieve a deal in a partner's program
    question: As a partner, where do I see the full terms of one deal in a program?
  phrasing_ops: 7
  slug: impact-deals-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Deferred Deep Linking API from Impact — 1 operation(s) for deferred deep linking.
  name: Impact Deferred Deep Linking API
  phrasing_intents:
  - id: getDeferredDeepLink
    intent: Resolve a deferred deep link after install
    question: How does my app find out which link a user clicked before installing it?
  phrasing_ops: 1
  slug: impact-deferred-deep-linking-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Inbound webhook payloads that impact.com sends to a partner-configured URL when events occur.
  name: Impact Event Notifications API
  phrasing_intents:
  - id: receiveEventNotificationPost
    intent: Receive an event notification as JSON
    question: What JSON body does impact.com post to my endpoint when an event happens?
  - id: receiveEventNotificationGet
    intent: Receive an event notification as a GET
    question: What query parameters arrive when impact.com pings my URL with a GET?
  phrasing_ops: 2
  slug: impact-event-notifications-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Exception List Items API from Impact — 2 operation(s) for exception list items.
  name: Impact Exception List Items API
  phrasing_intents:
  - id: listExceptionListItems
    intent: List items in an exception list
    question: Which values are on one of my exception lists?
  - id: createExceptionListItems
    intent: Add items to an exception list
    question: Can I add one value, or upload a file of many, to an exception list?
  - id: replaceExceptionListItems
    intent: Replace all items in an exception list from a file
    question: Can I swap an exception list's entire contents with a new CSV or XLSX file?
  - id: deleteAllExceptionListItems
    intent: Delete all items from an exception list
    question: Can I empty an exception list in one call?
  - id: getExceptionListItemById
    intent: Get one exception list item
    question: What are the details of a single entry in an exception list?
  - id: deleteExceptionListItem
    intent: Delete one item from an exception list
    question: Can I remove just one value from an exception list without touching the rest?
  phrasing_ops: 6
  slug: impact-exception-list-items-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Exception Lists API from Impact — 4 operation(s) for exception lists.
  name: Impact Exception Lists API
  phrasing_intents:
  - id: listExceptionLists
    intent: List a brand's exception lists
    question: Which commission exception lists exist on my campaigns?
  - id: createExceptionList
    intent: Create an exception list
    question: How do I set up an alternate commission list for certain SKUs?
  - id: getExceptionListById
    intent: Get an exception list as a brand
    question: What's configured on one of my brand's exception lists?
  - id: updateExceptionList
    intent: Update an exception list
    question: Can I rename an exception list or change its type?
  - id: retrieveExceptionList
    intent: Retrieve an exception list as a partner
    question: As a partner, how do I see an exception list referenced in my contract?
  - id: listExceptionListItems
    intent: List the items in an exception list
    question: Which SKUs or categories trigger an alternate commission rate?
  phrasing_ops: 6
  slug: impact-exception-lists-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: 'Endpoints for working with bulk data exports: create a new export, look up the status of an existing export, download a completed export, and list recent exports.'
  name: Impact Export API
  phrasing_intents:
  - id: listExports
    intent: List past exports
    question: Which exports have been run in my referral tenant recently?
  - id: createExport
    intent: Start an asynchronous data export
    question: How do I export my referral program data to a file?
  - id: getExport
    intent: Check an export's status
    question: Is my export finished yet or still pending?
  - id: downloadExport
    intent: Download a completed export file
    question: Where do I get the file once an export has completed?
  phrasing_ops: 4
  slug: impact-export-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The FTP Submissions API from Impact — 3 operation(s) for ftp submissions.
  name: Impact FTP Submissions API
  phrasing_intents:
  - id: listFtpSubmissions
    intent: List FTP file submissions
    question: Which conversion files have I uploaded over FTP recently?
  - id: getFtpSubmissionById
    intent: Get an FTP batch submission's details
    question: How many records in one FTP batch file were accepted?
  - id: getFtpSubmissionErrorDetails
    intent: List errors in an FTP batch file
    question: Why did rows in my FTP upload fail?
  phrasing_ops: 3
  slug: impact-ftp-submissions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoint for creating and resuming identity verification sessions.
  name: Impact Identity Verification API
  phrasing_intents:
  - id: createIdentityVerificationSession
    intent: Start or resume identity verification
    question: How do I launch identity verification for a partner user?
  phrasing_ops: 1
  slug: impact-identity-verification-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Invoices API from Impact — 6 operation(s) for invoices.
  name: Impact Invoices API
  phrasing_intents:
  - id: listInvoices
    intent: List a brand's partner invoices
    question: Which partner invoices has my brand received this quarter?
  - id: getInvoiceById
    intent: Get a brand's partner invoice details
    question: What's on a specific partner invoice my brand was billed?
  - id: downloadInvoicePdf
    intent: Download a brand's partner invoice as PDF
    question: Can a brand get a PDF copy of a partner invoice for accounting?
  - id: getMediapartnersByAccountSIDInvoices
    intent: List a partner's invoices
    question: Which invoices have been issued to me as a partner?
  - id: retrieveInvoice
    intent: Retrieve a partner's invoice
    question: As a partner, can I look up one invoice from either invoicing method?
  - id: downloadInvoice
    intent: Download a partner's invoice PDF
    question: How can a partner download one of their invoices as a PDF file?
  phrasing_ops: 6
  slug: impact-invoices-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Schedule, monitor, replay, and download large-scale asynchronous jobs.
  name: Impact Jobs API
  phrasing_intents:
  - id: listJobs
    intent: List an agency's scheduled jobs
    question: Which export jobs has my agency account scheduled on impact.com?
  - id: getJob
    intent: Check an agency job's status
    question: Has the report export my agency queued finished yet?
  - id: downloadJobResult
    intent: Download an agency job's result file
    question: How do I get the file an agency export job produced?
  - id: replayJob
    intent: Re-run an agency job
    question: Can my agency re-run a finished export to get fresh data for the same window?
  - id: getAdvertisersByAccountSIDJobs
    intent: List a brand account's jobs
    question: Where can I see all the jobs my brand account has created?
  - id: getJobById
    intent: Get a brand job's status
    question: Is the export job on my brand account still processing?
  - id: getAdvertisersByAccountSIDJobsByJobIdDownload
    intent: Download a brand job's result file
    question: How do I download the file from a completed advertiser export?
  - id: putAdvertisersByAccountSIDJobsByJobIdReplay
    intent: Re-queue a brand job
    question: Can I re-queue a cancelled advertiser job to pick up additional results?
  phrasing_ops: 12
  slug: impact-jobs-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Legal Entities API from Impact — 2 operation(s) for legal entities.
  name: Impact Legal Entities API
  phrasing_intents:
  - id: listLegalEntities
    intent: List an account's legal entities
    question: Which legal entities are tied to my brand account?
  - id: getLegalEntity
    intent: Get a legal entity
    question: What details are held for one legal entity on my account?
  phrasing_ops: 2
  slug: impact-legal-entities-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for listing, creating, retrieving, updating, and deleting partner media properties.
  name: Impact Media Properties API
  phrasing_intents:
  - id: listMediaProperties
    intent: List a partner's media properties
    question: Which websites, apps and social accounts are registered as my media properties?
  - id: createMediaProperty
    intent: Register a new media property
    question: How do I add a new website or social channel as a media property?
  - id: retrieveMediaProperty
    intent: Retrieve a media property
    question: What details are stored for one of my media properties?
  - id: updateMediaProperty
    intent: Update a media property
    question: Can I change the URL or follower count on an existing media property?
  - id: deleteMediaProperty
    intent: Delete a media property
    question: Can I remove a website I no longer run from my media properties?
  phrasing_ops: 5
  slug: impact-media-properties-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Notes API from Impact — 2 operation(s) for notes.
  name: Impact Notes API
  phrasing_intents:
  - id: listNotes
    intent: List notes on a campaign
    question: What notes have we logged about partners on this campaign?
  - id: createNote
    intent: Add a note about a partner
    question: How do I record a note about a partner?
  - id: getNoteById
    intent: Get a note's details
    question: What does a specific partner note say?
  - id: updateNote
    intent: Edit a note
    question: Can I change the text of a note I already wrote?
  - id: deleteNote
    intent: Delete a note
    question: Can I permanently remove a partner note?
  phrasing_ops: 5
  slug: impact-notes-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Special methods designed for Client-facing applications like the Mobile and Javascript SDKs.
  name: Impact Open Endpoint API
  phrasing_intents:
  - id: openGetUser
    intent: Look up a user with share links (open endpoint)
    question: Can I fetch a referral user along with their share links through the open endpoint?
  - id: openUserUpsert
    intent: Create or update a user and account (open endpoint)
    question: Can I update a referral participant and create their account in one call if it doesn't exist?
  - id: openCreateUser
    intent: Create a new user and account (open endpoint)
    question: How do I register a brand-new referral participant and their account together?
  - id: openDeleteUser
    intent: Delete a user (open endpoint)
    question: Can I remove a referral user without deleting the account they belong to?
  - id: openGetUserByCode
    intent: Find a user by referral code (open endpoint)
    question: Can a front end resolve a referral code to its user through the open endpoint?
  phrasing_ops: 5
  slug: impact-open-endpoint-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Page Load API from Impact — 1 operation(s) for page load.
  name: Impact Page Load API
  phrasing_intents:
  - id: trackPageLoad
    intent: Track a page load or app open
    question: Can I record a landing page view so a partner gets credit for the traffic?
  phrasing_ops: 1
  slug: impact-page-load-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Partner Groups API from Impact — 2 operation(s) for partner groups.
  name: Impact Partner Groups API
  phrasing_intents:
  - id: listPartnerGroups
    intent: List partner groups on a campaign
    question: What partner groups exist on my campaign?
  - id: createPartnerGroup
    intent: Create a partner group
    question: How do I create a group to organize partners?
  - id: getPartnerGroupById
    intent: Get a partner group and its members
    question: Which partners belong to a particular group?
  - id: updatePartnerGroup
    intent: Rename or change members of a partner group
    question: How do I add partners to an existing group?
  - id: deletePartnerGroup
    intent: Delete a partner group
    question: What happens to partners when I delete their group?
  phrasing_ops: 5
  slug: impact-partner-groups-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Partners API from Impact — 2 operation(s) for partners.
  name: Impact Partners API
  phrasing_intents:
  - id: listPartners
    intent: List a brand's partners
    question: Who are all the partners in my program?
  - id: createPartner
    intent: Create a direct partner account
    question: How do I sign up a partner directly into my program?
  - id: getPartnerById
    intent: Get a partner's details
    question: What do we know about a specific partner in our program?
  - id: updatePartner
    intent: Set a partner's custom tracking values
    question: How do I set the custom MPValue fields used in a partner's tracking links?
  phrasing_ops: 4
  slug: impact-partners-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Phone Numbers API from Impact — 2 operation(s) for phone numbers.
  name: Impact Phone Numbers API
  phrasing_intents:
  - id: listPhoneNumbers
    intent: List tracking phone numbers
    question: What call tracking phone numbers does my account have?
  - id: getPhoneNumberById
    intent: Get a tracking phone number's details
    question: When was a specific tracking number last assigned or released?
  phrasing_ops: 2
  slug: impact-phone-numbers-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Programs API from Impact — 5 operation(s) for programs.
  name: Impact Programs API
  phrasing_intents:
  - id: listPrograms
    intent: List a brand's programs
    question: Which programs does my brand account run?
  - id: getProgramById
    intent: Get a brand program's details
    question: What settings does one of my brand's programs have?
  - id: getMediapartnersByAccountSIDCampaigns
    intent: List programs a partner has joined
    question: Which brand programs have I signed up for as a partner?
  - id: retrieveProgram
    intent: Retrieve a program a partner joined
    question: As a partner, what are the details of a program I joined?
  - id: retrieveProgramLogo
    intent: Download a program's logo image
    question: Can I get a brand program's logo to show on my site?
  phrasing_ops: 5
  slug: impact-programs-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Promo Code Exception List Items API from Impact — 2 operation(s) for promo code exception list items.
  name: Impact Promo Code Exception List Items API
  phrasing_intents:
  - id: listPromoCodeExceptionListItems
    intent: List codes in a promo code exception list
    question: Which promo codes are in one of my exception lists?
  - id: createPromoCodeExceptionListItem
    intent: Add a code to a promo code exception list
    question: How do I add a promo code to an exception list?
  - id: deleteAllPromoCodeExceptionListItems
    intent: Clear every item from a promo code exception list
    question: Can I wipe all the codes out of a promo code exception list at once?
  - id: getPromoCodeExceptionListItemById
    intent: Get one promo code exception list item
    question: What are the details of a single entry on a promo code exception list?
  - id: deletePromoCodeExceptionListItem
    intent: Remove one item from a promo code exception list
    question: How do I take a single code off a promo code exception list?
  phrasing_ops: 5
  slug: impact-promo-code-exception-list-items-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Promo Code Exception Lists API from Impact — 4 operation(s) for promo code exception lists.
  name: Impact Promo Code Exception Lists API
  phrasing_intents:
  - id: createPromoCodeExceptionList
    intent: Create a promo code exception list
    question: How do I set up a list of promo codes that pay a different commission rate?
  - id: getPromoCodeExceptionListById
    intent: Get a brand's promo code exception list
    question: As a brand, what's configured on one of my promo code exception lists?
  - id: updatePromoCodeExceptionList
    intent: Rename or retarget a promo code exception list
    question: Can I rename a promo code exception list or change its action trackers?
  - id: retrievePromoCodeExceptionList
    intent: Retrieve a partner's promo code exception list
    question: As a partner, can I view a promo code exception list referenced in my contract?
  - id: listPromoCodeExceptionListItems
    intent: List codes in a promo code exception list
    question: Which promo codes trigger an alternate commission rate for me as a partner?
  phrasing_ops: 5
  slug: impact-promo-code-exception-lists-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Promo Codes API from Impact — 4 operation(s) for promo codes.
  name: Impact Promo Codes API
  phrasing_intents:
  - id: listPromoCodes
    intent: List a brand's promo codes
    question: Which promo codes has my brand issued?
  - id: createPromoCode
    intent: Create a promo code for a partner
    question: How do I give a partner their own promo code?
  - id: getPromoCodeById
    intent: Get a brand promo code's details
    question: Who is a specific promo code on my program assigned to?
  - id: expirePromoCode
    intent: Expire a promo code
    question: How do I deactivate a promo code without deleting it?
  - id: getMediapartnersByAccountSIDPromoCodes
    intent: List promo codes available to a partner
    question: What promo codes can I use as a partner?
  - id: retrievePromoCode
    intent: Retrieve a promo code as a partner
    question: What are the full details of a promo code I was given?
  phrasing_ops: 6
  slug: impact-promo-codes-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for listing and retrieving brand promotions available to your partner account.
  name: Impact Promotions API
  phrasing_intents:
  - id: listPromotions
    intent: List brand promotions available to a partner
    question: Which brand promotions can I promote right now?
  - id: retrievePromotion
    intent: Retrieve a promotion
    question: What are the details of one specific brand promotion?
  phrasing_ops: 2
  slug: impact-promotions-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: A Referral tracks who has referred whom.
  name: Impact Referral API
  phrasing_intents:
  - id: listReferrals
    intent: List referrals in a tenant
    question: Which referrals have been made in my referral program?
  - id: getReferral
    intent: Look up a referral
    question: What are the details of one specific referral?
  - id: moderateReferrals
    intent: Approve or deny referrals
    question: How do I approve or deny several pending referrals at once?
  - id: openListReferrals
    intent: List a user's referrals (open endpoint)
    question: Can a front-end widget show the referrals a given user made or received?
  phrasing_ops: 4
  slug: impact-referral-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: 'Endpoints for working with referral codes: look up a code and its associated reward, or apply a code to a referred account. For background on what referral codes are, see the Referral Code Overview.'
  name: Impact Referral Code API
  phrasing_intents:
  - id: getCode
    intent: Look up a referral code (deprecated)
    question: Is the older referral code lookup still supported?
  - id: openValidateCode
    intent: Validate a referral code from the client
    question: How do I check a referral code from my mobile or web app?
  - id: openApplyCode
    intent: Apply a referral code to a user
    question: How do I mark a new user as referred by someone's code?
  phrasing_ops: 3
  slug: impact-referral-code-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Report Export API from Impact — 2 operation(s) for report export.
  name: Impact Report Export API
  phrasing_intents:
  - id: exportReport
    intent: Export a brand report as a job
    question: How do I export a large brand report without waiting on the request?
  - id: exportReports
    intent: Export a partner report as a job
    question: How does a partner export a report in the background?
  - id: exportReport
    intent: Export an agency report as a job
    question: How does my agency export a report asynchronously?
  phrasing_ops: 3
  slug: impact-report-export-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: List available reports, fetch their metadata, and run them synchronously.
  name: Impact Reports API
  phrasing_intents:
  - id: listReports
    intent: List reports available to a partner
    question: Which reports can I run programmatically as a partner?
  - id: runReport
    intent: Run a partner report synchronously (legacy)
    question: Can I pull partner report rows inline for a date range?
  - id: retrieveMetadata
    intent: Get a partner report's filters and columns
    question: Which filters does a partner report accept before I run it?
  phrasing_ops: 3
  slug: impact-reports-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Legacy synchronous reports endpoint. Subject to pagination limits — prefer `ReportExport` for large datasets.
  name: Impact Reports (Legacy) API
  phrasing_intents:
  - id: listAllReports
    intent: List reports available to an agency
    question: Which reports can my agency run through the API?
  - id: runReport
    intent: Run an agency report synchronously (legacy)
    question: Can my agency run a report and get the rows back immediately?
  - id: getReportMetadata
    intent: Get an agency report's filters and columns
    question: Which filters and output columns does a given agency report have?
  - id: getAdvertisersByAccountSIDReports
    intent: List reports available to a brand
    question: Which reports can my brand account access?
  - id: getAdvertisersByAccountSIDReportsByReportId
    intent: Run a brand report synchronously (legacy)
    question: Can a brand run a report and get records back inline, without an export job?
  - id: getAdvertisersByAccountSIDReportsByReportIdMetaData
    intent: Get a brand report's filters and attributes
    question: What filters and attributes does one of my brand reports expose?
  phrasing_ops: 6
  slug: impact-reports-legacy-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: A Reward keeps track of a prize, discount or credit that someone has received. All reward types other than gift card integrated rewards can be cancelled using the impact.com API, or through the impact
  name: Impact Reward API
  phrasing_intents:
  - id: getRewards
    intent: List an account's referral rewards
    question: What rewards has a customer account earned from referrals?
  - id: lookupReward
    intent: Look up a single reward
    question: How do I check the details of one specific reward?
  - id: debitReward
    intent: Redeem referral credit
    question: How do I redeem part of a user's referral credit?
  - id: cancelReward
    intent: Cancel a referral reward
    question: Can I cancel a reward someone earned through a referral?
  - id: createReward
    intent: Give a user a reward
    question: How do I manually grant a reward to a user?
  phrasing_ops: 5
  slug: impact-reward-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Reward Balances summarizes the Rewards in someone's account.
  name: Impact Reward Balance API
  phrasing_intents:
  - id: listRewardBalances
    intent: List reward balances for an account
    question: How much referral credit has an account earned so far?
  - id: debitRewardBalance
    intent: Redeem credit from a reward balance
    question: Can I redeem referral credit an account has earned?
  phrasing_ops: 2
  slug: impact-reward-balance-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Routing Rules API from Impact — 2 operation(s) for routing rules.
  name: Impact Routing Rules API
  phrasing_intents:
  - id: listRoutingRules
    intent: List a program's routing rules
    question: Which block and redirect rules are set on my program?
  - id: getRoutingRuleById
    intent: Get a routing rule's details
    question: What condition and action does a specific routing rule use?
  phrasing_ops: 2
  slug: impact-routing-rules-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for retrieving the share links of a given user. Share links are organised by engagement medium and share medium. For background on how they work, see the Share Links Overview.
  name: Impact Share Links API
  phrasing_intents:
  - id: getSharelinks
    intent: Get a user's share links (deprecated)
    question: Is the flat share-links lookup deprecated?
  - id: getShareURLs
    intent: Get a user's share URLs with an API key
    question: How do I get a referral user's share URLs from my server?
  - id: openGetShareURLs
    intent: Get a user's share URLs from the client
    question: Can my web or mobile app fetch a user's share URLs with their JWT?
  phrasing_ops: 3
  slug: impact-share-links-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for browsing partner storefronts, their groups, and the catalog items inside them.
  name: Impact Stores API
  phrasing_intents:
  - id: listStores
    intent: List stores available to a partner
    question: Which brand stores can I browse as a partner?
  - id: retrieveStore
    intent: Retrieve a store and its groups
    question: What curated product groups does a particular store have?
  - id: listStoreItems
    intent: List products in a store group
    question: Which products are inside one group of a store?
  phrasing_ops: 3
  slug: impact-stores-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Tasks API from Impact — 4 operation(s) for tasks.
  name: Impact Tasks API
  phrasing_intents:
  - id: listTasks
    intent: List a program's tasks as a brand
    question: What open tasks exist on my program?
  - id: getTaskById
    intent: Get a program task as a brand
    question: What's in a specific task on my brand's program?
  - id: getMediapartnersByAccountSIDTasks
    intent: List tasks assigned to a partner
    question: What tasks have brands assigned to me as a partner?
  - id: getMediapartnersByAccountSIDTasksByTaskId
    intent: Get a task assigned to a partner
    question: What does a task assigned to my partner account ask me to do?
  phrasing_ops: 4
  slug: impact-tasks-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for creating, completing, and retrieving partner tax documents.
  name: Impact Tax Documents API
  phrasing_intents:
  - id: retrieveLatestTaxDocument
    intent: Get a partner's latest tax document
    question: What's the most recent tax form I saved as a partner?
  - id: createTaxDocument
    intent: Start a new tax document submission
    question: How do I begin filling in a W-9 or W-8 form as a partner?
  - id: retrieveTaxDocumentById
    intent: Retrieve a specific tax document
    question: Can I look up one tax document I submitted by its ID?
  - id: listAllTaxDocuments
    intent: List all of a partner's tax documents
    question: Which tax documents have ever been submitted for my partner account?
  - id: completeTaxDocumentSubmission
    intent: Record a completed tax form submission
    question: After a partner finishes the Comply Exchange iframe, how is the form marked as submitted?
  phrasing_ops: 5
  slug: impact-tax-documents-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Tracking Links API from Impact — 2 operation(s) for tracking links.
  name: Impact Tracking Links API
  phrasing_intents:
  - id: createTrackingLink
    intent: Generate a tracking link for a partner (brand)
    question: As a brand, can I generate a tracking link on behalf of one of my partners?
  - id: postMediapartnersByAccountSIDProgramsByProgramIdTrackingLinks
    intent: Create a tracking link as a partner
    question: How do I create my own tracking link for a program I promote?
  phrasing_ops: 2
  slug: impact-tracking-links-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Tracking Value Requests API from Impact — 2 operation(s) for tracking value requests.
  name: Impact Tracking Value Requests API
  phrasing_intents:
  - id: listTrackingValueRequests
    intent: List partner tracking value requests
    question: Which promo code or vanity URL requests are partners waiting on me to approve?
  - id: getTrackingValueRequestById
    intent: Get a tracking value request
    question: What exactly did a partner ask for in one tracking value request?
  - id: approveTrackingValueRequest
    intent: Approve a tracking value request
    question: How do I approve a partner's request for a dedicated promo code?
  - id: rejectTrackingValueRequest
    intent: Reject a tracking value request
    question: Can I decline a partner's tracking value request?
  phrasing_ops: 4
  slug: impact-tracking-value-requests-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: The Unsubscribed Contacts API from Impact — 1 operation(s) for unsubscribed contacts.
  name: Impact Unsubscribed Contacts API
  phrasing_intents:
  - id: listUnsubscribedContacts
    intent: List contacts who opted out of Outreach
    question: Who has unsubscribed from my program's Outreach emails?
  - id: unsubscribeContact
    intent: Unsubscribe a contact from Outreach
    question: How do I stop sending Outreach emails to a partner's contact?
  phrasing_ops: 2
  slug: impact-unsubscribed-contacts-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: API for managing users, including creation, lookup, and blocking.
  name: Impact User API
  phrasing_intents:
  - id: createUser
    intent: Create or update a referral program user
    question: How do I add a participant to my referral program or update their details?
  - id: findUserByReferralCode
    intent: Look up a user by referral code
    question: Who does this referral code belong to in my referral program?
  - id: getUser
    intent: Look up a user by ID
    question: What personal details are stored for a referral user, looked up by their ID?
  - id: getUserPII
    intent: Get the personal data stored for a user
    question: What personally identifiable information does impact.com hold about one of my users?
  - id: blockUser
    intent: Block a user from making referrals
    question: Can I stop a suspicious user from earning successful referrals?
  - id: unblockUser
    intent: Unblock a user so they can refer again
    question: How can I lift a block on a referral participant?
  - id: listUsers
    intent: List users in referral programs
    question: Which participants are enrolled in my Advocate referral programs?
  - id: openGetUser
    intent: Look up a user with share links (open endpoint)
    question: Can I fetch a referral user along with their share links through the open endpoint?
  phrasing_ops: 12
  slug: impact-user-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for listing and retrieving partner-account users.
  name: Impact Users API
  phrasing_intents:
  - id: listUsers
    intent: List users with access to a partner account
    question: Who has access to my partner account?
  - id: retrieveUser
    intent: Retrieve a partner account user
    question: What details are stored for one person on my partner account?
  phrasing_ops: 2
  slug: impact-users-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: 'Endpoints for managing webhook subscriptions: list current subscriptions, register new endpoint URLs, remove existing ones, and send a test event to verify a subscription.'
  name: Impact Webhook API
  phrasing_intents:
  - id: createWebhook
    intent: Subscribe a URL to webhooks
    question: How do I start receiving webhook events at my endpoint?
  - id: listWebhooks
    intent: List webhook subscriptions
    question: Which URLs are subscribed to receive my webhook events?
  - id: deleteWebhook
    intent: Remove a webhook subscription
    question: How do I stop events going to a webhook URL?
  - id: testWebhook
    intent: Send a test webhook event
    question: Can I send a test event to check my webhook works?
  phrasing_ops: 4
  slug: impact-webhook-api
- baseURL: https://api.impact.com/Advertisers/{AccountSID}/
  baseurl_source: declared
  description: Endpoints for retrieving and updating your bank account, PayPal, and payment scheduling settings.
  name: Impact Withdrawal Settings API
  phrasing_intents:
  - id: retrieveWithdrawalSettings
    intent: Get a partner's withdrawal settings
    question: What bank account and payout schedule is on my partner account?
  - id: updateWithdrawalSettings
    intent: Update a partner's withdrawal settings
    question: How do I change where my partner earnings are paid out?
  - id: retrieveRequiredBankingFields
    intent: Get required banking fields for a country
    question: Which banking fields are mandatory for payouts in my country?
  phrasing_ops: 3
  slug: impact-withdrawal-settings-api
artifact_total: 74
asyncapis:
- description: ''
  name: Impact Webhooks
  slug: impact-webhooks
common:
- group: other
  href: https://artifacts.apis.io/impact/capabilities/impact-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/impact-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/impact/overlays/impact-brand-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/impact-brand-overlay.yaml
- group: other
  href: https://artifacts.apis.io/impact/overlays/impact-partner-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/impact-partner-overlay.yaml
- group: other
  href: https://artifacts.apis.io/impact/overlays/impact-agency-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/impact-agency-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/impact/security/impact-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/impact/security/impact-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/impact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.impact.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ImpactInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/impactdotcom
- group: company
  title: ''
  type: Blog
  url: https://impact.com/press-releases/
- group: commercial
  title: ''
  type: Pricing
  url: https://impact.com/get-started/
- group: other
  title: ''
  type: X
  url: https://x.com/impactdotcom
- group: commercial
  href: https://artifacts.apis.io/impact/plans/impact-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/impact-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/impact/rate-limits/impact-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/impact-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/impact/finops/impact-finops.yml
  title: ''
  type: FinOps
  url: finops/impact-finops.yml
- group: company
  href: https://artifacts.apis.io/impact/blogs/blogs.json
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  href: https://artifacts.apis.io/impact/json-ld/impact-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/impact-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.impact.com/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.impact.com/brand-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.impact.com/rest-apis/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.impact.com/
- group: start
  title: ''
  type: SignUp
  url: https://impact.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impact.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impact.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.impact.com/
- group: operate
  href: https://artifacts.apis.io/impact/lifecycle/impact-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/impact-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/impact/lifecycle/impact-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/impact-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/impact/changelog/impact-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/impact-changelog.yml
- group: design
  href: https://artifacts.apis.io/impact/conventions/impact-conventions.yml
  title: ''
  type: Conventions
  url: conventions/impact-conventions.yml
- group: design
  href: https://artifacts.apis.io/impact/errors/impact-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/impact-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/impact/authentication/impact-authentication.yml
  title: ''
  type: Authentication
  url: authentication/impact-authentication.yml
- group: auth
  href: https://artifacts.apis.io/impact/scopes/impact-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/impact-scopes.yml
- group: design
  href: https://artifacts.apis.io/impact/conformance/impact-conformance.yml
  title: ''
  type: Conformance
  url: conformance/impact-conformance.yml
- group: auth
  href: https://artifacts.apis.io/impact/security/impact-trust-center.yml
  title: ''
  type: Compliance
  url: security/impact-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/impact/security/impact-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/impact-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/impact/security/impact-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/impact-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/impact/well-known/impact-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/impact-security.txt
- group: agent
  href: https://artifacts.apis.io/impact/well-known/impact-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/impact-well-known.yml
- group: build
  href: https://artifacts.apis.io/impact/packages/impact-packages.yml
  title: ''
  type: Packages
  url: packages/impact-packages.yml
- group: build
  href: https://artifacts.apis.io/impact/packages/impact-packages.yml
  title: ''
  type: SDKs
  url: packages/impact-packages.yml
- group: design
  href: https://artifacts.apis.io/impact/components/impact-components.yml
  title: ''
  type: Components
  url: components/impact-components.yml
- group: design
  href: https://artifacts.apis.io/impact/data-model/impact-data-model.yml
  title: ''
  type: DataModel
  url: data-model/impact-data-model.yml
- group: start
  href: https://artifacts.apis.io/impact/sandbox/impact-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/impact-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/impact/llms/impact-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/impact-llms.txt
- group: agent
  href: https://artifacts.apis.io/impact/mcp/impact-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/impact-mcp.yml
- group: build
  href: https://artifacts.apis.io/impact/mcp/impact-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/impact-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/impact/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/impact/asyncapi/impact-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/impact-webhooks.yml
- group: docs
  href: https://artifacts.apis.io/impact/graphql/impact-advocate-graphql.yml
  title: ''
  type: GraphQL
  url: graphql/impact-advocate-graphql.yml
- group: company
  title: ''
  type: Blog
  url: https://impact.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saasquatch
created: '2026-06-13'
description: impact.com is a partnership management platform for affiliate, creator, influencer and customer-referral programs. It publishes four REST API personas - Brand v14, Partner v16, Agency v3 and Advocate v13 - across 69 OpenAPI 3.1 documents and 245 operations, a remote OAuth 2.1 MCP server at mcp.impact.com, first-party agent skills, an Advocate GraphQL endpoint, webhook and postback event delivery, and an agent-readable developer portal that serves llms.txt, per-page markdown and a live documentation question interface.
finops:
- has_sources: true
  method: derived
  name: Impact Finops
  primary_unit: ''
  service_category: ''
  slug: impact-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impact.png
jsonld:
- class_count: 0
  name: Impact Context
  property_count: 2
  slug: impact-context
layout: provider
mcp_servers:
- description: First-party remote Model Context Protocol server for the impact.com partnership management platform. Exposes account-scoped tools for performance analytics, invoices, partner and program discovery, pr
  name: impact.com MCP Server
  slug: impact-com-mcp-server
modified: '2026-08-13'
name: Impact
nav: Providers
network: true
overview: 'Impact publishes 61 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Action Inquiries API, and 58 more. Tagged areas include Affiliates, Partnerships, Performance Marketing, Commissions, and Tracking.


  The Impact catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Impact''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, signup flow, and 45 more developer resources.'
plans:
- name: Impact Plans Pricing
  plan_count: 0
  slug: impact-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Impact Rate Limits
  slug: impact-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Impact API Rules
  rule_count: 60
  severity_counts:
    error: 41
    hint: 0
    info: 7
    warn: 12
  slug: impact-rules
scopes:
- name: Impact Scopes
  scope_count: 0
  slug: impact-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 71.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 61.5
    catalog_earned_first_party: 12.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 92.1
  previous_composite: 72.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 60
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/impact/impact-2026-06-20T183254.png
security:
- kind: authentication
  name: Impact Authentication
  slug: impact-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Impact Domain Security
  slug: impact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Impact Vulnerability Disclosure
  slug: impact-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Impact Trust Center
  slug: impact-trust-center
  summary_line: SOC 1 Type II, ISO/IEC 27001:2022, PCI DSS Level 4
skill_count: 1
skills:
- name: partner-weekly-performance-digest
  slug: impact-partner-weekly-performance-digest
slug: impact
tags:
- Affiliates
- Partnerships
- Performance Marketing
- Commissions
- Tracking
- Creator Economy
- Partner Management
- Referrals
- Attribution
- Payouts
- Marketing
- Advertising
- MCP
- Agents
- Affiliate Marketing
- Influencer Marketing
- Referral Marketing
website: https://impact.com/
---
