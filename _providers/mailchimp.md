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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 216
  human_in_the_loop: 1
  name: Mailchimp Agentic Access
  operation_count: 401
  slug: mailchimp-agentic-access
  summary_line: 401 operations · 216 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: An open source, API-first, modular commerce stack built using Node.js, React, and GraphQL. Formerly known as Reaction Commerce, the project has been discontinued but documentation remains available.
  name: Mailchimp Open Commerce
  slug: mailchimp-open-commerce
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Automations API from Mailchimp — 13 operation(s) for automations.
  name: Mailchimp Automations API
  phrasing_intents:
  - id: getAutomations
    intent: List classic automations
    question: What classic automations are set up in my Mailchimp account?
  - id: postAutomations
    intent: Create a classic automation
    question: How do I create a new classic automation workflow?
  - id: getAutomationsId
    intent: Get details of one automation workflow
    question: What are the settings and trigger of a specific automation?
  - id: postAutomationsIdActionsPauseAllEmails
    intent: Pause every email in an automation
    question: How do I pause an entire automation workflow at once?
  - id: postAutomationsIdActionsStartAllEmails
    intent: Start every email in an automation
    question: How do I turn on all emails in an automation workflow?
  - id: archiveAutomations
    intent: Archive an automation permanently
    question: Can I permanently end an automation but keep its report data?
  - id: getAutomationsIdEmails
    intent: List the emails in an automation
    question: Which emails make up a particular automation workflow?
  - id: getAutomationsIdEmailsId
    intent: Get one email in an automation
    question: What are the settings of a single email inside an automation?
  phrasing_ops: 18
  slug: mailchimp-automations-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Batches API from Mailchimp — 2 operation(s) for batches.
  name: Mailchimp Batches API
  phrasing_intents:
  - id: getBatches
    intent: List batch operation requests
    question: Which batch operation requests have I submitted recently?
  - id: postBatches
    intent: Run many API calls as one batch
    question: How do I send hundreds of API calls in a single batch request?
  - id: getBatchesId
    intent: Check a batch request's progress
    question: Has my batch request finished, and how many operations failed?
  - id: deleteBatchesId
    intent: Stop a running batch request
    question: Can I cancel a long-running batch that's blocking my other batches?
  phrasing_ops: 4
  slug: mailchimp-batches-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Campaigns API from Mailchimp — 18 operation(s) for campaigns.
  name: Mailchimp Campaigns API
  phrasing_intents:
  - id: getCampaigns
    intent: List email campaigns in the account
    question: How do I see every campaign in my Mailchimp account?
  - id: postCampaigns
    intent: Create a new email campaign
    question: How do I create a new regular email campaign through the API?
  - id: getCampaignsId
    intent: Get details of one campaign
    question: Where can I look up the settings and status of a single campaign?
  - id: patchCampaignsId
    intent: Update an existing campaign's settings
    question: How do I change the subject line or from name on a campaign I already created?
  - id: deleteCampaignsId
    intent: Delete a campaign
    question: How do I permanently remove a campaign from my account?
  - id: postCampaignsIdActionsCancelSend
    intent: Cancel a campaign that is mid-send
    question: Can I stop a campaign after I hit send but before everyone receives it?
  - id: postCampaignsIdActionsReplicate
    intent: Duplicate a campaign
    question: How do I make a copy of a campaign I already sent?
  - id: postCampaignsIdActionsSend
    intent: Send a campaign now
    question: How do I send a campaign immediately instead of scheduling it?
  phrasing_ops: 22
  slug: mailchimp-campaigns-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Conversations API from Mailchimp — 4 operation(s) for conversations.
  name: Mailchimp Conversations API
  phrasing_intents:
  - id: getConversations
    intent: List past campaign reply conversations
    question: Where can I find replies subscribers sent to my older campaigns?
  - id: getConversationsId
    intent: Get one conversation
    question: Can I pull up the details of a single past conversation?
  - id: getConversationsIdMessages
    intent: List messages in a conversation
    question: What messages were exchanged in a particular conversation?
  - id: getConversationsIdMessagesId
    intent: Get one message in a conversation
    question: Can I read a single message from a past conversation?
  phrasing_ops: 4
  slug: mailchimp-conversations-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Ecommerce API from Mailchimp — 10 operation(s) for ecommerce.
  name: Mailchimp Ecommerce API
  phrasing_intents:
  - id: getEcommerceOrders
    intent: List orders across every connected store
    question: Can I see every ecommerce order across all the stores in my Mailchimp account at once?
  - id: getEcommerceStores
    intent: List connected ecommerce stores
    question: Which online stores are connected to my Mailchimp account?
  - id: postEcommerceStores
    intent: Connect a new ecommerce store
    question: How do I connect a new online store to a Mailchimp audience?
  - id: getEcommerceStoresId
    intent: Get details of one store
    question: What settings and contact details does a specific connected store have?
  - id: patchEcommerceStoresId
    intent: Update a store's settings
    question: Can I change a connected store's name, domain or timezone after setting it up?
  - id: deleteEcommerceStoresId
    intent: Delete a store and all its data
    question: What happens to customers, orders and products when I delete a connected store?
  - id: getEcommerceStoresIdCarts
    intent: List a store's shopping carts
    question: Which shopping carts are currently tracked for my store, including abandoned ones?
  - id: postEcommerceStoresIdCarts
    intent: Add a shopping cart to a store
    question: How do I send a shopper's cart to Mailchimp so abandoned-cart emails can go out?
  phrasing_ops: 60
  slug: mailchimp-ecommerce-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The Exports API from Mailchimp — 7 operation(s) for exports.
  name: Mailchimp Exports API
  phrasing_intents:
  - id: postExportsInfo
    intent: Check an export job's status and download link
    question: Is my transactional export job finished, and where do I download the zip?
  - id: postExportsList
    intent: List transactional export jobs
    question: Which export jobs have I started on my transactional account?
  - id: postExportsRejects
    intent: Export the rejection denylist to CSV
    question: How do I download my full denylist of rejected email addresses?
  - id: postExportsWhitelist
    intent: Export the allowlist (legacy whitelist endpoint)
    question: Is the older exports/whitelist call still available for exporting my allowlist?
  - id: postExportsAllowlist
    intent: Export the rejection allowlist to CSV
    question: How do I download a CSV of every address on my rejection allowlist?
  - id: postExportsActivity
    intent: Export sending activity history to CSV
    question: Can I export my transactional sending history for a date range?
  phrasing_ops: 6
  slug: mailchimp-exports-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Lists API from Mailchimp — 11 operation(s) for lists.
  name: Mailchimp Lists API
  phrasing_intents:
  - id: getLists
    intent: List all audiences in the account
    question: Which audiences do I have in my Mailchimp account?
  - id: postLists
    intent: Create a new audience
    question: How do I create a brand new audience list?
  - id: getListsId
    intent: Get details and stats for one audience
    question: How many contacts and what settings does one specific audience have?
  - id: patchListsId
    intent: Update an audience's settings
    question: How do I rename an audience or change its permission reminder text?
  - id: deleteListsId
    intent: Delete an entire audience
    question: What do I lose if I delete a whole audience, including its subscriber history?
  - id: postListsId
    intent: Batch subscribe or unsubscribe many contacts
    question: Can I subscribe or unsubscribe hundreds of contacts to a list in one call?
  - id: getListsIdAbuseReports
    intent: List abuse complaints for an audience
    question: Have any subscribers marked my emails as spam on this list?
  - id: getListsIdAbuseReportsId
    intent: Get one abuse report
    question: What are the details of a single spam complaint, such as who filed it and on which campaign?
  phrasing_ops: 70
  slug: mailchimp-lists-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The Messages API from Mailchimp — 13 operation(s) for messages.
  name: Mailchimp Messages API
  phrasing_intents:
  - id: postMessagesSendSms
    intent: Send a transactional SMS
    question: Can I send a one-off transactional text message to a phone number?
  - id: postMessagesSend
    intent: Send a transactional email
    question: How do I send a single transactional email like a password reset?
  - id: postMessagesSendTemplate
    intent: Send a transactional email from a stored template
    question: Can I send a transactional email using one of my saved Transactional templates by name?
  - id: postMessagesSendMcTemplate
    intent: Send a transactional email from a Mailchimp template
    question: Can I send a transactional message using a template designed in the Mailchimp editor?
  - id: postMessagesSearch
    intent: Search recently sent transactional emails
    question: How can I find a transactional email I sent to a specific address last week?
  - id: postMessagesSearchTimeSeries
    intent: Get hourly stats for matching sent emails
    question: How many of my matching transactional emails were sent, opened and clicked per hour?
  - id: postMessagesInfo
    intent: Get delivery details for one sent email
    question: Was a particular transactional email delivered, bounced or opened?
  - id: postMessagesContent
    intent: Get the full content of a sent email
    question: Can I see the exact HTML and text body of an email I recently sent?
  phrasing_ops: 13
  slug: mailchimp-messages-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: Manage custom metadata fields that can be attached to messages for tracking and filtering.
  name: Mailchimp Metadata API
  phrasing_intents:
  - id: postMetadataList
    intent: List custom message metadata fields
    question: Which custom metadata fields are indexed on my transactional messages?
  - id: postMetadataAdd
    intent: Add a custom metadata field to index
    question: How do I start indexing a custom field like order_id on my transactional emails?
  - id: postMetadataUpdate
    intent: Change a metadata field's view template
    question: Can I change how an existing metadata field renders in my activity log?
  - id: postMetadataDelete
    intent: Delete a custom metadata field
    question: Why does a metadata field I deleted still appear in my list for a while?
  phrasing_ops: 4
  slug: mailchimp-metadata-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: Manage the rejection blacklist, which prevents delivery to addresses that have previously bounced or been reported as spam.
  name: Mailchimp Rejects API
  phrasing_intents:
  - id: postRejectsAdd
    intent: Block an email address from receiving mail
    question: How do I stop transactional email from going to a specific address?
  - id: postRejectsList
    intent: List denylisted email addresses
    question: Which email addresses are on my rejection denylist?
  - id: postRejectsDelete
    intent: Remove an email address from the denylist
    question: How do I unblock an email address so it can receive mail again?
  - id: postRejectsAddSms
    intent: Block a phone number from receiving SMS
    question: How do I stop text messages from going to a certain phone number?
  - id: postRejectsListSms
    intent: List denylisted phone numbers
    question: Which phone numbers are blocked from receiving my SMS?
  - id: postRejectsDeleteSms
    intent: Remove a phone number from the SMS denylist
    question: How do I unblock a phone number so it can get texts again?
  phrasing_ops: 6
  slug: mailchimp-rejects-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Reporting API from Mailchimp — 12 operation(s) for reporting.
  name: Mailchimp Reporting API
  phrasing_intents:
  - id: getReportingFacebookAds
    intent: List Facebook ad reports
    question: How are all my Facebook ads performing in Mailchimp?
  - id: getReportingFacebookAdsId
    intent: Get one Facebook ad's report
    question: What were the results of a specific Facebook ad?
  - id: getReportingFacebookAdsIdEcommerceProductActivity
    intent: Break down product sales from a Facebook ad
    question: Which products did people buy after clicking a Facebook ad?
  - id: getReportingLandingPagesId
    intent: Get one landing page's report
    question: How many visits and signups did a specific landing page get?
  - id: getReportingLandingPages
    intent: List landing page reports
    question: How are all my landing pages performing?
  - id: getReportingSurveys
    intent: List survey reports
    question: Which of my surveys have results I can look at?
  - id: getReportingSurveysId
    intent: Get one survey's report
    question: How many responses has a specific survey received?
  - id: getReportingSurveysIdQuestions
    intent: List per-question reports for a survey
    question: How did people answer each question in my survey?
  phrasing_ops: 12
  slug: mailchimp-reporting-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Reports API from Mailchimp — 24 operation(s) for reports.
  name: Mailchimp Reports API
  phrasing_intents:
  - id: getReports
    intent: List reports for sent campaigns
    question: Where can I see performance reports for all my sent campaigns?
  - id: getReportsId
    intent: Get the performance report for one campaign
    question: What were the open and click rates for a specific campaign I sent?
  - id: getReportsIdAbuseReportsId
    intent: List spam complaints for a campaign
    question: Did anyone mark my campaign as spam?
  - id: getReportsIdAbuseReportsIdId
    intent: Get one abuse complaint on a campaign
    question: Can I see the details of a single spam complaint on a campaign?
  - id: getReportsIdAdvice
    intent: Get improvement advice from a campaign's stats
    question: What advice does Mailchimp give based on how my campaign performed?
  - id: getReportsIdClickDetails
    intent: List link click stats for a campaign
    question: Which links in my campaign got the most clicks?
  - id: getReportsIdClickDetailsId
    intent: Get click stats for one link in a campaign
    question: How many people clicked one particular link in my email?
  - id: getReportsIdClickDetailsIdMembers
    intent: List subscribers who clicked a campaign link
    question: Who exactly clicked a specific link in my campaign?
  phrasing_ops: 22
  slug: mailchimp-reports-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Root API from Mailchimp — 1 operation(s) for root.
  name: Mailchimp Root API
  phrasing_intents:
  - id: getRoot
    intent: Get links to all top-level API resources
    question: What resources are available from the Mailchimp Marketing API root?
  phrasing_ops: 1
  slug: mailchimp-root-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: Retrieve sender information and statistics for verified sending domains and email addresses.
  name: Mailchimp Senders API
  phrasing_intents:
  - id: postSendersList
    intent: List senders that have used the account
    question: Which from addresses have tried to send through my Transactional account?
  - id: postSendersDomains
    intent: List sender domains on the account
    question: What sending domains have been added to my Transactional account?
  - id: postSendersAddDomain
    intent: Add a sender domain
    question: Can I add a sending domain before I actually send from it?
  - id: postSendersDeleteDomain
    intent: Delete an unverified sender domain
    question: How do I remove a sender domain I added by mistake?
  - id: postSendersCheckDomain
    intent: Check a sender domain's SPF and DKIM
    question: Are the SPF and DKIM records set up correctly for my sending domain?
  - id: postSendersVerifyDomain
    intent: Send a domain ownership verification email
    question: How do I prove I own a sending domain?
  - id: postSendersInfo
    intent: Get stats for one sender address
    question: How are emails from a specific sender address performing?
  - id: postSendersTimeSeries
    intent: Get hourly sending history for a sender
    question: Can I see hour-by-hour stats for a sender over the last 30 days?
  phrasing_ops: 8
  slug: mailchimp-senders-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: Manage subaccounts for organizing sending and reporting within a single Mandrill account.
  name: Mailchimp Subaccounts API
  phrasing_intents:
  - id: postSubaccountsList
    intent: List transactional subaccounts
    question: What subaccounts exist on my transactional email account?
  - id: postSubaccountsAdd
    intent: Create a subaccount
    question: How do I set up a separate subaccount for one of my customers?
  - id: postSubaccountsInfo
    intent: Get a subaccount's details
    question: What's the status, reputation and quota of one subaccount?
  - id: postSubaccountsUpdate
    intent: Update a subaccount
    question: Can I rename an existing subaccount or change its notes?
  - id: postSubaccountsDelete
    intent: Delete a subaccount
    question: What happens to a subaccount's email and stats if I delete it?
  - id: postSubaccountsPause
    intent: Pause a subaccount's sending
    question: Can I temporarily stop one subaccount from sending email?
  - id: postSubaccountsResume
    intent: Resume a paused subaccount
    question: How do I restart sending on a subaccount I paused?
  phrasing_ops: 7
  slug: mailchimp-subaccounts-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Surveys API from Mailchimp — 12 operation(s) for surveys.
  name: Mailchimp Surveys API
  phrasing_intents:
  - id: postListsIdSurveysIdActionsPublish
    intent: Publish a survey
    question: How do I publish a draft survey so people can respond?
  - id: postListsIdSurveysIdActionsUnpublish
    intent: Unpublish a survey
    question: How do I take a published survey offline?
  - id: postListsIdSurveysIdActionsCreateEmail
    intent: Create a campaign that links to a survey
    question: How do I create an email campaign that sends people to my survey?
  phrasing_ops: 3
  slug: mailchimp-surveys-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The Tags API from Mailchimp — 5 operation(s) for tags.
  name: Mailchimp Tags API
  phrasing_intents:
  - id: postTagsList
    intent: List transactional message tags
    question: What tags have I used on my transactional messages?
  - id: postTagsDelete
    intent: Delete a message tag and its stats
    question: How do I permanently delete a tag from my sent messages?
  - id: postTagsInfo
    intent: Get stats for one message tag
    question: How are messages with a particular tag performing?
  - id: postTagsTimeSeries
    intent: Get hourly history for one message tag
    question: Can I see hour-by-hour stats for a single tag over the last 30 days?
  - id: postTagsAllTimeSeries
    intent: Get hourly history across all tags
    question: What are the combined hourly stats across all my tags for the past month?
  phrasing_ops: 5
  slug: mailchimp-tags-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Templates API from Mailchimp — 11 operation(s) for templates.
  name: Mailchimp Templates API
  phrasing_intents:
  - id: getTemplates
    intent: List marketing email templates
    question: Which email templates are available in my marketing account?
  - id: postTemplates
    intent: Create a classic marketing template from HTML
    question: How do I upload my own HTML as a reusable campaign template?
  - id: getTemplatesId
    intent: Get a marketing template's details
    question: What type, category and thumbnail does a specific campaign template have?
  - id: patchTemplatesId
    intent: Update a marketing template's name, HTML or folder
    question: Can I replace the HTML of an existing campaign template?
  - id: deleteTemplatesId
    intent: Delete a marketing template
    question: Can I delete a campaign template I no longer use?
  - id: getTemplatesIdDefaultContent
    intent: View a template's editable sections
    question: Which sections of a campaign template can I edit, and what's their default content?
  - id: postTemplatesAdd
    intent: Add a transactional email template
    question: How do I create a transactional email template with a default subject and from address?
  - id: postTemplatesInfo
    intent: Get a transactional template's details
    question: What code, subject and labels does a named transactional template have?
  phrasing_ops: 14
  slug: mailchimp-templates-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: Retrieve information about the authenticated Mandrill account.
  name: Mailchimp Users API
  phrasing_intents:
  - id: postUsersInfo
    intent: Get the API-connected user's account info
    question: Which transactional account and reputation is my API key tied to?
  - id: postUsersPing
    intent: Check that an API key works
    question: Is my transactional API key valid?
  - id: postUsersPing2
    intent: Check an API key with a JSON ping response
    question: Can I validate my API key and get the ping answer back as JSON?
  - id: postUsersSenders
    intent: List senders that have used the account
    question: Which from addresses have tried to send through my transactional account?
  phrasing_ops: 4
  slug: mailchimp-users-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The Webhooks API from Mailchimp — 9 operation(s) for webhooks.
  name: Mailchimp Webhooks API
  phrasing_intents:
  - id: postWebhooksList
    intent: List webhooks on the account
    question: Which webhooks are configured on my Transactional account?
  - id: postWebhooksAdd
    intent: Add a webhook for message events
    question: How do I get message events like opens and bounces posted to my server?
  - id: postWebhooksInfo
    intent: Get details of one webhook
    question: What URL and events is a specific webhook set to?
  - id: postWebhooksUpdate
    intent: Update an existing webhook
    question: How do I change the URL an existing webhook posts to?
  - id: postWebhooksDelete
    intent: Delete a webhook
    question: How do I remove a webhook I no longer need?
  phrasing_ops: 5
  slug: mailchimp-webhooks-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The accountExport API from Mailchimp — 1 operation(s) for accountexport.
  name: Mailchimp Account Export API
  phrasing_intents:
  - id: getAccountExportId
    intent: Check one account export's status
    question: Is my account export finished, and where can I download it?
  phrasing_ops: 1
  slug: mailchimp-accountexport-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The audiences API from Mailchimp — 2 operation(s) for audiences.
  name: Mailchimp Audiences API
  phrasing_intents:
  - id: getAudienceContactList
    intent: List omni-channel contacts in an audience
    question: Who are the email and SMS contacts in one of my audiences?
  - id: createAudienceContact
    intent: Add an omni-channel contact to an audience
    question: How do I add a contact with both an email address and an SMS number?
  - id: getAudienceContact
    intent: Get one omni-channel contact
    question: What channels and merge fields does one contact in my audience have?
  - id: patchAudienceContact
    intent: Update an omni-channel contact
    question: How do I change the SMS number or email on an existing contact?
  phrasing_ops: 4
  slug: mailchimp-audiences-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The authorizedApps API from Mailchimp — 2 operation(s) for authorizedapps.
  name: Mailchimp Authorized Apps API
  phrasing_intents:
  - id: getAuthorizedApps
    intent: List apps connected to the account
    question: Which third-party applications have access to my Mailchimp account?
  - id: getAuthorizedAppsId
    intent: Get details of one authorized app
    question: What do I know about a specific connected application?
  phrasing_ops: 2
  slug: mailchimp-authorizedapps-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The batchWebhooks API from Mailchimp — 2 operation(s) for batchwebhooks.
  name: Mailchimp Batch Webhooks API
  phrasing_intents:
  - id: getBatchWebhooks
    intent: List batch completion webhooks
    question: Which webhooks fire when my batch operations finish?
  - id: postBatchWebhooks
    intent: Add a batch completion webhook
    question: How can I get notified when a batch request finishes processing?
  - id: getBatchWebhook
    intent: Get one batch webhook
    question: What URL does a particular batch webhook call, and is it enabled?
  - id: patchBatchWebhooks
    intent: Update a batch webhook
    question: Can I change the URL of an existing batch webhook?
  - id: deleteBatchWebhookId
    intent: Delete a batch webhook
    question: How do I stop batch completion notifications going to an old URL?
  phrasing_ops: 5
  slug: mailchimp-batchwebhooks-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The campaignFolders API from Mailchimp — 2 operation(s) for campaignfolders.
  name: Mailchimp Campaign Folders API
  phrasing_intents:
  - id: getCampaignFolders
    intent: List campaign folders
    question: Which folders am I using to organize my campaigns?
  - id: postCampaignFolders
    intent: Create a campaign folder
    question: How do I make a new folder to group my campaigns?
  - id: getCampaignFoldersId
    intent: Get one campaign folder
    question: What's the name and campaign count of a specific campaign folder?
  - id: patchCampaignFoldersId
    intent: Rename a campaign folder
    question: Can I rename an existing campaign folder?
  - id: deleteCampaignFoldersId
    intent: Delete a campaign folder
    question: What happens to the campaigns inside a folder when I delete it?
  phrasing_ops: 5
  slug: mailchimp-campaignfolders-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The connectedSites API from Mailchimp — 5 operation(s) for connectedsites.
  name: Mailchimp Connected Sites API
  phrasing_intents:
  - id: getConnectedSites
    intent: List connected websites
    question: Which websites have I connected to my Mailchimp account?
  - id: postConnectedSites
    intent: Connect a new website
    question: How do I connect my website so I can track visitors and add pop-up forms?
  - id: getConnectedSitesId
    intent: Get one connected site
    question: What's the tracking script URL for a specific connected site?
  - id: deleteConnectedSitesId
    intent: Remove a connected site
    question: Can I disconnect a website from my Mailchimp account?
  - id: postConnectedSitesIdActionsVerifyScriptInstallation
    intent: Verify a connected site's script is installed
    question: Is the Mailchimp tracking script actually installed on my website?
  - id: postConnectedSitesIdActionsEnablePixel
    intent: Turn on the tracking pixel for a site
    question: How do I enable the Mailchimp tracking pixel on a connected site?
  - id: postConnectedSitesIdActionsDisablePixel
    intent: Turn off the tracking pixel for a site
    question: Can I stop the Mailchimp pixel from tracking visitors on one of my sites?
  phrasing_ops: 7
  slug: mailchimp-connectedsites-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The contacts API from Mailchimp — 6 operation(s) for contacts.
  name: Mailchimp Contacts API
  phrasing_intents:
  - id: getAudienceContacts
    intent: List audiences in the account
    question: What audiences do I have in my Mailchimp account?
  - id: getAudienceId
    intent: Get details of one audience
    question: Where can I see the details of a single audience?
  - id: getAudienceContactList
    intent: List contacts in an audience
    question: Who are the omni-channel contacts in one of my audiences?
  - id: createAudienceContact
    intent: Add a contact to an audience
    question: How do I add a new contact with an email and SMS channel to an audience?
  - id: getAudienceContact
    intent: Get one contact in an audience
    question: Can I look up a single contact in an audience by id or channel hash?
  - id: patchAudienceContact
    intent: Update an existing contact
    question: How do I change the merge fields on a contact that's already in my audience?
  - id: postAudiencesContactsActionsArchive
    intent: Archive a contact
    question: How do I archive a contact so they stop counting in my audience?
  - id: postAudiencesContactsActionsForget
    intent: Forget a contact
    question: How do I make Mailchimp forget a contact entirely?
  phrasing_ops: 8
  slug: mailchimp-contacts-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The inbound API from Mailchimp — 9 operation(s) for inbound.
  name: Mailchimp Inbound API
  phrasing_intents:
  - id: postInboundDomains
    intent: List inbound email domains
    question: Which domains are set up to receive inbound email on my transactional account?
  - id: postInboundAddDomain
    intent: Add an inbound email domain
    question: How do I start receiving inbound email for my own domain?
  - id: postInboundCheckDomain
    intent: Check MX settings for an inbound domain
    question: Are the MX records for my inbound domain pointed correctly?
  - id: postInboundDeleteDomain
    intent: Delete an inbound email domain
    question: What happens to incoming mail when I remove an inbound domain?
  - id: postInboundRoutes
    intent: List inbound routes for a domain or SMS number
    question: Which mailbox patterns and webhooks are routing mail for an inbound domain?
  - id: postInboundAddRoute
    intent: Add an inbound route to a webhook
    question: How do I forward mail sent to support@ on my inbound domain to a webhook?
  - id: postInboundUpdateRoute
    intent: Update an inbound mailbox route
    question: Can I change the webhook URL an existing inbound route posts to?
  - id: postInboundDeleteRoute
    intent: Delete an inbound mailbox route
    question: Can I remove a single inbound route without deleting the whole domain?
  phrasing_ops: 9
  slug: mailchimp-inbound-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The mctemplates API from Mailchimp — 4 operation(s) for mctemplates.
  name: Mailchimp Mctemplates API
  phrasing_intents:
  - id: postMcTemplatesInfo
    intent: Get a Mailchimp Transactional template
    question: What versions and details does one of my Mailchimp templates have for transactional use?
  - id: postMcTemplatesList
    intent: List Mailchimp Transactional templates
    question: Which Mailchimp templates are available for transactional sends?
  - id: postMcTemplatesRender
    intent: Render a Mailchimp template with merge variables
    question: Can I preview how a Mailchimp template looks with merge variables filled in?
  - id: postMcTemplatesTimeSeries
    intent: Get hourly send stats for a Mailchimp template
    question: How has a transactional template performed hour by hour over the last 30 days?
  phrasing_ops: 4
  slug: mailchimp-mctemplates-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The ping API from Mailchimp — 1 operation(s) for ping.
  name: Mailchimp Ping API
  phrasing_intents:
  - id: getPing
    intent: Check that the Marketing API is up
    question: Is the Mailchimp Marketing API reachable right now?
  phrasing_ops: 1
  slug: mailchimp-ping-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The searchCampaigns API from Mailchimp — 1 operation(s) for searchcampaigns.
  name: Mailchimp Search Campaigns API
  phrasing_intents:
  - id: getSearchCampaigns
    intent: Search campaigns by keyword
    question: How can I find a past email campaign by a word in its subject or content?
  phrasing_ops: 1
  slug: mailchimp-searchcampaigns-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The searchMembers API from Mailchimp — 1 operation(s) for searchmembers.
  name: Mailchimp Search Members API
  phrasing_intents:
  - id: getSearchMembers
    intent: Search contacts by name or email
    question: Can I find a subscriber by name or email across all my audiences?
  phrasing_ops: 1
  slug: mailchimp-searchmembers-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The sms-campaigns API from Mailchimp — 6 operation(s) for sms-campaigns.
  name: Mailchimp Sms Campaigns API
  phrasing_intents:
  - id: getSmsCampaigns
    intent: List SMS campaigns
    question: What SMS campaigns do I have in my account?
  - id: postSmsCampaigns
    intent: Create an SMS campaign
    question: How do I create a new text message campaign?
  - id: getSmsCampaignsId
    intent: Get one SMS campaign
    question: What's the status and audience of a specific SMS campaign?
  - id: patchSmsCampaignsId
    intent: Update an SMS campaign's settings
    question: How do I rename an SMS campaign or move it to another folder?
  - id: deleteSmsCampaignsId
    intent: Delete an SMS campaign
    question: Can I remove an SMS campaign from my account?
  - id: postSmsCampaignsIdActionsSend
    intent: Send an SMS campaign now
    question: How do I send an SMS campaign immediately?
  - id: postSmsCampaignsIdActionsSchedule
    intent: Schedule an SMS campaign
    question: Can I schedule a text campaign to go out at a specific time?
  - id: postSmsCampaignsIdActionsCancelSend
    intent: Cancel a scheduled or sending SMS campaign
    question: Can I stop an SMS campaign that is already sending?
  phrasing_ops: 10
  slug: mailchimp-sms-campaigns-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The urls API from Mailchimp — 4 operation(s) for urls.
  name: Mailchimp URLS API
  phrasing_intents:
  - id: postUrlsTrackingDomains
    intent: List click tracking domains
    question: Which custom tracking domains are set up for my transactional email links?
  - id: postUrlsAddTrackingDomain
    intent: Add a click tracking domain
    question: How do I use my own domain for tracked links in transactional email?
  - id: postUrlsDeleteTrackingDomain
    intent: Delete an unverified tracking domain
    question: How do I remove a tracking domain I added but never verified?
  - id: postUrlsCheckTrackingDomain
    intent: Check a tracking domain's CNAME setup
    question: Is the CNAME record for my tracking domain configured correctly?
  phrasing_ops: 4
  slug: mailchimp-urls-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The verifiedDomains API from Mailchimp — 3 operation(s) for verifieddomains.
  name: Mailchimp Verified Domains API
  phrasing_intents:
  - id: getVerifiedDomain
    intent: Get a sending domain's verification details
    question: Is a particular sending domain verified and authenticated yet?
  - id: deleteVerifiedDomain
    intent: Remove a verified sending domain
    question: Can I delete a sending domain I no longer send from?
  - id: verifyDomain
    intent: Verify a sending domain with its code
    question: How do I finish verifying a domain with the code I got by email?
  - id: getVerifiedDomains
    intent: List sending domains
    question: Which sending domains are on my Mailchimp account?
  - id: createVerifiedDomain
    intent: Add a sending domain to verify
    question: How do I add a new domain I want to send email from?
  phrasing_ops: 5
  slug: mailchimp-verifieddomains-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The ips API from Mailchimp — 13 operation(s) for ips.
  name: Mailchimp Ips API
  phrasing_intents:
  - id: postIpsList
    intent: List dedicated sending IPs
    question: Which dedicated IPs does my Mailchimp Transactional account have?
  - id: postIpsInfo
    intent: Get details of one dedicated IP
    question: What pool and warmup status does a particular dedicated IP have?
  - id: postIpsProvision
    intent: Request an additional dedicated IP
    question: How do I request another dedicated IP for my account?
  - id: postIpsStartWarmup
    intent: Start warming up a dedicated IP
    question: How do I begin warming up a new dedicated IP?
  - id: postIpsCancelWarmup
    intent: Cancel a dedicated IP's warmup
    question: Can I stop the warmup process on a dedicated IP early?
  - id: postIpsSetPool
    intent: Move a dedicated IP to another pool
    question: How do I move a dedicated IP into a different IP pool?
  - id: postIpsDelete
    intent: Delete a dedicated IP
    question: How do I permanently remove a dedicated IP from my account?
  - id: postIpsListPools
    intent: List dedicated IP pools
    question: What IP pools have I set up?
  phrasing_ops: 13
  slug: mailchimp-ips-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Account Exports API from Mailchimp — 1 operation(s) for account exports.
  name: Mailchimp Account Exports API
  phrasing_intents:
  - id: getAccountExports
    intent: List account data exports
    question: Which full account exports have I requested before?
  - id: postAccountExport
    intent: Start an account data export
    question: How do I export my whole Mailchimp account's data?
  phrasing_ops: 2
  slug: mailchimp-account-exports-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Activity Feed API from Mailchimp — 1 operation(s) for activity feed.
  name: Mailchimp Activity Feed API
  phrasing_intents:
  - id: getActivityFeedChimpChatter
    intent: Get the latest account activity (Chimp Chatter)
    question: What's been happening in my Mailchimp account lately?
  phrasing_ops: 1
  slug: mailchimp-activity-feed-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The customer Journeys API from Mailchimp — 1 operation(s) for customer journeys.
  name: Mailchimp customer Journeys API
  phrasing_intents:
  - id: postCustomerJourneysJourneysIdStepsIdActionsTrigger
    intent: Trigger a Customer Journey step for a contact
    question: How do I push a contact into a Customer Journey from my own app?
  phrasing_ops: 1
  slug: mailchimp-customer-journeys-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The facebook Ads API from Mailchimp — 2 operation(s) for facebook ads.
  name: Mailchimp facebook Ads API
  phrasing_intents:
  - id: getAllFacebookAds
    intent: List Facebook ads
    question: Which Facebook ads have I created from my marketing account?
  - id: getFacebookAdsId
    intent: Get one Facebook ad's details
    question: What's the status, budget and audience of one specific Facebook ad?
  phrasing_ops: 2
  slug: mailchimp-facebook-ads-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The File Manager API from Mailchimp — 5 operation(s) for file manager.
  name: Mailchimp File Manager API
  phrasing_intents:
  - id: getFileManagerFiles
    intent: List all files in the File Manager
    question: What images and files have I uploaded to the Mailchimp File Manager?
  - id: postFileManagerFiles
    intent: Upload an image or file
    question: How do I upload an image to use in my email campaigns?
  - id: getFileManagerFilesId
    intent: Get details of one stored file
    question: What's the URL and size of a specific file in my File Manager?
  - id: patchFileManagerFilesId
    intent: Rename a file or move it between folders
    question: How do I rename an uploaded file?
  - id: deleteFileManagerFilesId
    intent: Delete a stored file
    question: How do I delete an image from the File Manager?
  - id: getFileManagerFolders
    intent: List File Manager folders
    question: What folders exist in my File Manager?
  - id: postFileManagerFolders
    intent: Create a File Manager folder
    question: How do I create a new folder to organize my images?
  - id: getFileManagerFoldersId
    intent: Get details of one File Manager folder
    question: How many files are in a particular folder?
  phrasing_ops: 11
  slug: mailchimp-file-manager-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Landing Pages API from Mailchimp — 5 operation(s) for landing pages.
  name: Mailchimp Landing Pages API
  phrasing_intents:
  - id: getAllLandingPages
    intent: List landing pages
    question: What landing pages have I built?
  - id: postAllLandingPages
    intent: Create a landing page
    question: How do I create a new landing page from a template?
  - id: getLandingPageId
    intent: Get one landing page
    question: Is a specific landing page published, and what's its URL?
  - id: patchLandingPageId
    intent: Update a landing page's settings
    question: How do I change a landing page's title or description?
  - id: deleteLandingPageId
    intent: Delete a landing page
    question: Can I permanently delete a landing page?
  - id: postLandingPageIdActionsPublish
    intent: Publish a landing page
    question: How do I make a draft landing page live?
  - id: postLandingPageIdActionsUnpublish
    intent: Unpublish a landing page
    question: Can I take a landing page offline without deleting it?
  - id: getLandingPageIdContent
    intent: Get a landing page's HTML
    question: Can I download the HTML behind one of my landing pages?
  phrasing_ops: 8
  slug: mailchimp-landing-pages-api
- baseURL: https://server.api.mailchimp.com/3.0
  baseurl_source: declared
  description: The Template Folders API from Mailchimp — 2 operation(s) for template folders.
  name: Mailchimp Template Folders API
  phrasing_intents:
  - id: getTemplateFolders
    intent: List template folders
    question: What folders do I use to organize my email templates?
  - id: postTemplateFolders
    intent: Create a template folder
    question: How do I create a new folder to group my templates?
  - id: getTemplateFoldersId
    intent: Get one template folder
    question: What's the name and template count of one specific template folder?
  - id: patchTemplateFoldersId
    intent: Rename a template folder
    question: How do I rename one of my template folders?
  - id: deleteTemplateFoldersId
    intent: Delete a template folder
    question: What happens to the templates inside a folder when I delete it?
  phrasing_ops: 5
  slug: mailchimp-template-folders-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The authorized-apps API from Mailchimp — 2 operation(s) for authorized-apps.
  name: Mailchimp Authorized Apps API
  slug: mailchimp-authorized-apps-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The batch-webhooks API from Mailchimp — 2 operation(s) for batch-webhooks.
  name: Mailchimp Batch Webhooks API
  slug: mailchimp-batch-webhooks-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The campaign-folders API from Mailchimp — 2 operation(s) for campaign-folders.
  name: Mailchimp Campaign Folders API
  slug: mailchimp-campaign-folders-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The connected-sites API from Mailchimp — 3 operation(s) for connected-sites.
  name: Mailchimp Connected Sites API
  slug: mailchimp-connected-sites-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The search-campaigns API from Mailchimp — 1 operation(s) for search-campaigns.
  name: Mailchimp Search Campaigns API
  slug: mailchimp-search-campaigns-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The search-members API from Mailchimp — 1 operation(s) for search-members.
  name: Mailchimp Search Members API
  slug: mailchimp-search-members-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The segments API from Mailchimp — 6 operation(s) for segments.
  name: Mailchimp Segments API
  slug: mailchimp-segments-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The snapshots API from Mailchimp — 3 operation(s) for snapshots.
  name: Mailchimp Snapshots API
  slug: mailchimp-snapshots-api
- baseURL: https://api.mailchimp.com
  baseurl_source: declared
  description: The verified-domains API from Mailchimp — 3 operation(s) for verified-domains.
  name: Mailchimp Verified Domains API
  slug: mailchimp-verified-domains-api
- baseURL: https://mandrillapp.com/api/1.3
  baseurl_source: declared
  description: The Allow Lists API from Mailchimp — 3 operation(s) for allow lists.
  name: Mailchimp Allow Lists API
  phrasing_intents:
  - id: postAllowlistsAdd
    intent: Add an email address to the allowlist
    question: How do I make sure transactional mail to a specific address is never rejected?
  - id: postAllowlistsList
    intent: List or search allowlisted addresses
    question: Which email addresses are on my rejection allowlist?
  - id: postAllowlistsDelete
    intent: Remove an address from the allowlist
    question: Can I take an email address back off my allowlist?
  phrasing_ops: 3
  slug: mailchimp-allow-lists-api
arazzos:
- description: Subscribe a member to an audience and attach an internal note to them.
  name: Mailchimp Add Member and Attach a Note
  slug: mailchimp-add-member-note-workflow
- description: Subscribe a member to an audience and immediately apply a tag.
  name: Mailchimp Add Member and Tag
  slug: mailchimp-add-member-tag-workflow
- description: Run the send checklist for a campaign and only send if it is ready.
  name: Mailchimp Pre-Send Checklist then Send Campaign
  slug: mailchimp-checklist-then-send-campaign-workflow
- description: Create a new audience (list) and subscribe an initial member to it.
  name: Mailchimp Create Audience and Add First Member
  slug: mailchimp-create-audience-add-member-workflow
- description: Create a campaign, set its content, then send a test email to reviewers.
  name: Mailchimp Create Campaign, Set Content, and Send Test
  slug: mailchimp-create-campaign-content-test-workflow
- description: Create a regular campaign, set its HTML content, then schedule delivery.
  name: Mailchimp Create Campaign, Set Content, and Schedule
  slug: mailchimp-create-campaign-set-content-schedule-workflow
- description: Create a regular campaign, set its HTML content, then send it.
  name: Mailchimp Create Campaign, Set Content, and Send
  slug: mailchimp-create-campaign-set-content-send-workflow
- description: Add a custom audience field, then add a member that populates it.
  name: Mailchimp Create Merge Field and Add Member
  slug: mailchimp-create-merge-field-add-member-workflow
- description: Create a static segment (tag-style group), then add a member to it.
  name: Mailchimp Create Static Segment and Add Members
  slug: mailchimp-create-static-segment-add-members-workflow
- description: Create a reusable template, build a campaign from it, then send.
  name: Mailchimp Create Template, Build Campaign, and Send
  slug: mailchimp-create-template-campaign-send-workflow
- description: List classic automations, pick the first, and pause all its emails.
  name: Mailchimp Find and Pause an Automation
  slug: mailchimp-find-and-pause-automation-workflow
- description: List classic automations, pick the first, and start all its emails.
  name: Mailchimp Find and Start an Automation
  slug: mailchimp-find-and-start-automation-workflow
- description: Search campaigns by query, then retrieve the report for the first match.
  name: Mailchimp Find Campaign and Pull Its Report
  slug: mailchimp-find-campaign-pull-report-workflow
- description: Search a member by email, flag them VIP, then apply a VIP tag.
  name: Mailchimp Find Member, Mark VIP, and Tag
  slug: mailchimp-find-member-mark-vip-tag-workflow
- description: Add a member to an audience and place them into a static segment.
  name: Mailchimp Onboard Member into a Static Segment
  slug: mailchimp-onboard-member-to-segment-workflow
- description: Idempotently add or update a member with PUT, then tag them.
  name: Mailchimp Add-or-Update Member and Tag
  slug: mailchimp-put-member-tag-workflow
- description: Clone an existing campaign and send a test of the copy to reviewers.
  name: Mailchimp Replicate Campaign and Send Test
  slug: mailchimp-replicate-campaign-test-workflow
- description: Create a static segment, then batch add and remove members in one call.
  name: Mailchimp Sync Static Segment Members
  slug: mailchimp-sync-static-segment-members-workflow
- description: Find a member by email and update them, otherwise add them to the audience.
  name: Mailchimp Upsert Audience Member
  slug: mailchimp-upsert-member-workflow
artifact_total: 401
asyncapis:
- description: AsyncAPI description of Mailchimp Marketing audience webhooks. Mailchimp delivers list/audience events to a customer-configured callback URL via HTTP POST with an `application/x-www-form-urlencoded` b
  name: Mailchimp Marketing Webhooks
  slug: mailchimp-marketing-webhooks-asyncapi
collections:
- collection_type: postman
  name: Mailchimp Marketing API
  slug: postman-mailchimp-marketing-api
- collection_type: postman
  name: Mailchimp Transactional API
  slug: postman-mailchimp-transactional-api
- collection_type: open
  name: Mailchimp Marketing Abuse API
  slug: open-mailchimp-abuse-api
- collection_type: open
  name: Mailchimp Marketing Abuse Account Export API
  slug: open-mailchimp-account-export-api
- collection_type: open
  name: Mailchimp Marketing Abuse Accounts API
  slug: open-mailchimp-accounts-api
- collection_type: open
  name: Mailchimp Marketing Abuse Actions API
  slug: open-mailchimp-actions-api
- collection_type: open
  name: Mailchimp Marketing Abuse Activity API
  slug: open-mailchimp-activity-api
- collection_type: open
  name: Mailchimp Marketing Abuse Advice API
  slug: open-mailchimp-advice-api
- collection_type: open
  name: Mailchimp Marketing Abuse Allowlists API
  slug: open-mailchimp-allowlists-api
- collection_type: open
  name: Mailchimp Marketing Abuse Answers API
  slug: open-mailchimp-answers-api
- collection_type: open
  name: Mailchimp Marketing Abuse Applications API
  slug: open-mailchimp-applications-api
- collection_type: open
  name: Mailchimp Marketing Abuse Archive API
  slug: open-mailchimp-archive-api
- collection_type: open
  name: Mailchimp Marketing Abuse Authorized API
  slug: open-mailchimp-authorized-api
- collection_type: open
  name: Mailchimp Marketing Abuse Authorized Apps API
  slug: open-mailchimp-authorized-apps-api
- collection_type: open
  name: Mailchimp Marketing Abuse Automations API
  slug: open-mailchimp-automations-api
- collection_type: open
  name: Mailchimp Marketing Abuse Batch API
  slug: open-mailchimp-batch-api
- collection_type: open
  name: Mailchimp Marketing Abuse Batch Webhooks API
  slug: open-mailchimp-batch-webhooks-api
- collection_type: open
  name: Mailchimp Marketing Abuse Batches API
  slug: open-mailchimp-batches-api
- collection_type: open
  name: Mailchimp Marketing Abuse Campaign Folders API
  slug: open-mailchimp-campaign-folders-api
- collection_type: open
  name: Mailchimp Marketing Abuse Campaigns API
  slug: open-mailchimp-campaigns-api
- collection_type: open
  name: Mailchimp Marketing Abuse Cancels API
  slug: open-mailchimp-cancels-api
- collection_type: open
  name: Mailchimp Marketing Abuse Carts API
  slug: open-mailchimp-carts-api
- collection_type: open
  name: Mailchimp Marketing Abuse Categories API
  slug: open-mailchimp-categories-api
- collection_type: open
  name: Mailchimp Marketing Abuse Chatter API
  slug: open-mailchimp-chatter-api
- collection_type: open
  name: Mailchimp Marketing Abuse Checklist API
  slug: open-mailchimp-checklist-api
- collection_type: open
  name: Mailchimp Marketing Abuse Click API
  slug: open-mailchimp-click-api
- collection_type: open
  name: Mailchimp Marketing Abuse Clients API
  slug: open-mailchimp-clients-api
- collection_type: open
  name: Mailchimp Marketing Abuse Connected API
  slug: open-mailchimp-connected-api
- collection_type: open
  name: Mailchimp Marketing Abuse Connected_site_id API
  slug: open-mailchimp-connected-site-id-api
- collection_type: open
  name: Mailchimp Marketing Abuse Connected Sites API
  slug: open-mailchimp-connected-sites-api
- collection_type: open
  name: Mailchimp Marketing Abuse Content API
  slug: open-mailchimp-content-api
- collection_type: open
  name: Mailchimp Marketing Abuse Conversations API
  slug: open-mailchimp-conversations-api
- collection_type: open
  name: Mailchimp Marketing Abuse Customers API
  slug: open-mailchimp-customers-api
- collection_type: open
  name: Mailchimp Marketing Abuse Domains API
  slug: open-mailchimp-domains-api
- collection_type: open
  name: Mailchimp Marketing Abuse Ecommerce API
  slug: open-mailchimp-ecommerce-api
- collection_type: open
  name: Mailchimp Marketing Abuse Eepurl API
  slug: open-mailchimp-eepurl-api
- collection_type: open
  name: Mailchimp Marketing Abuse Email API
  slug: open-mailchimp-email-api
- collection_type: open
  name: Mailchimp Marketing Abuse Emails API
  slug: open-mailchimp-emails-api
- collection_type: open
  name: Mailchimp Marketing Abuse Events API
  slug: open-mailchimp-events-api
- collection_type: open
  name: Mailchimp Marketing Abuse Exports API
  slug: open-mailchimp-exports-api
- collection_type: open
  name: Mailchimp Marketing Abuse Facebook Ads API
  slug: open-mailchimp-facebook-ads-api
- collection_type: open
  name: Mailchimp Marketing Abuse Facebook API
  slug: open-mailchimp-facebook-api
- collection_type: open
  name: Mailchimp Marketing Abuse Feed API
  slug: open-mailchimp-feed-api
- collection_type: open
  name: Mailchimp Marketing Abuse Feedback API
  slug: open-mailchimp-feedback-api
- collection_type: open
  name: Mailchimp Marketing Abuse Fields API
  slug: open-mailchimp-fields-api
- collection_type: open
  name: Mailchimp Marketing Abuse File Manager API
  slug: open-mailchimp-file-manager-api
- collection_type: open
  name: Mailchimp Marketing Abuse Files API
  slug: open-mailchimp-files-api
- collection_type: open
  name: Mailchimp Marketing Abuse Folders API
  slug: open-mailchimp-folders-api
- collection_type: open
  name: Mailchimp Marketing Abuse Forms API
  slug: open-mailchimp-forms-api
- collection_type: open
  name: Mailchimp Marketing Abuse Goals API
  slug: open-mailchimp-goals-api
- collection_type: open
  name: Mailchimp Marketing Abuse Growth API
  slug: open-mailchimp-growth-api
- collection_type: open
  name: Mailchimp Marketing Abuse History API
  slug: open-mailchimp-history-api
- collection_type: open
  name: Mailchimp Marketing Abuse Images API
  slug: open-mailchimp-images-api
- collection_type: open
  name: Mailchimp Marketing Abuse Installation API
  slug: open-mailchimp-installation-api
- collection_type: open
  name: Mailchimp Marketing Abuse Interest API
  slug: open-mailchimp-interest-api
- collection_type: open
  name: Mailchimp Marketing Abuse Interests API
  slug: open-mailchimp-interests-api
- collection_type: open
  name: Mailchimp Marketing Abuse IPs API
  slug: open-mailchimp-ips-api
- collection_type: open
  name: Mailchimp Marketing Abuse Journeys API
  slug: open-mailchimp-journeys-api
- collection_type: open
  name: Mailchimp Marketing Abuse Landing API
  slug: open-mailchimp-landing-api
- collection_type: open
  name: Mailchimp Marketing Abuse Landing Pages API
  slug: open-mailchimp-landing-pages-api
- collection_type: open
  name: Mailchimp Marketing Abuse Lines API
  slug: open-mailchimp-lines-api
- collection_type: open
  name: Mailchimp Marketing Abuse List_id API
  slug: open-mailchimp-list-id-api
- collection_type: open
  name: Mailchimp Marketing Abuse Lists API
  slug: open-mailchimp-lists-api
- collection_type: open
  name: Mailchimp Marketing Abuse Locations API
  slug: open-mailchimp-locations-api
- collection_type: open
  name: Mailchimp Marketing Abuse Managers API
  slug: open-mailchimp-managers-api
- collection_type: open
  name: Mailchimp Marketing API
  slug: open-mailchimp-marketing-api-openapi-original
- collection_type: open
  name: Mailchimp Marketing API
  slug: open-mailchimp-marketing-api
- collection_type: open
  name: Mailchimp Marketing Webhooks
  slug: open-mailchimp-marketing-webhooks-asyncapi
- collection_type: open
  name: Mailchimp Marketing Abuse Members API
  slug: open-mailchimp-members-api
- collection_type: open
  name: Mailchimp Marketing Abuse Merge API
  slug: open-mailchimp-merge-api
- collection_type: open
  name: Mailchimp Marketing Abuse Messages API
  slug: open-mailchimp-messages-api
- collection_type: open
  name: Mailchimp Marketing Abuse Metadata API
  slug: open-mailchimp-metadata-api
- collection_type: open
  name: Mailchimp Marketing Abuse Month API
  slug: open-mailchimp-month-api
- collection_type: open
  name: Mailchimp Marketing Abuse Notes API
  slug: open-mailchimp-notes-api
- collection_type: open
  name: Mailchimp Marketing Abuse Open API
  slug: open-mailchimp-open-api
- collection_type: open
  name: Mailchimp Marketing Abuse Orders API
  slug: open-mailchimp-orders-api
- collection_type: open
  name: Mailchimp Marketing Abuse Outreach_id API
  slug: open-mailchimp-outreach-id-api
- collection_type: open
  name: Mailchimp Marketing Abuse Pages API
  slug: open-mailchimp-pages-api
- collection_type: open
  name: Mailchimp Marketing Abuse Pause API
  slug: open-mailchimp-pause-api
- collection_type: open
  name: Mailchimp Marketing Abuse Performance API
  slug: open-mailchimp-performance-api
- collection_type: open
  name: Mailchimp Marketing Abuse Pings API
  slug: open-mailchimp-pings-api
- collection_type: open
  name: Mailchimp Marketing Abuse Product API
  slug: open-mailchimp-product-api
- collection_type: open
  name: Mailchimp Marketing Abuse Products API
  slug: open-mailchimp-products-api
- collection_type: open
  name: Mailchimp Marketing Abuse Promo API
  slug: open-mailchimp-promo-api
- collection_type: open
  name: Mailchimp Marketing Abuse Promo_code_id API
  slug: open-mailchimp-promo-code-id-api
- collection_type: open
  name: Mailchimp Marketing Abuse Publish API
  slug: open-mailchimp-publish-api
- collection_type: open
  name: Mailchimp Marketing Abuse Questions API
  slug: open-mailchimp-questions-api
- collection_type: open
  name: Mailchimp Marketing Abuse Queues API
  slug: open-mailchimp-queues-api
- collection_type: open
  name: Mailchimp Marketing Abuse Rejects API
  slug: open-mailchimp-rejects-api
- collection_type: open
  name: Mailchimp Marketing Abuse Removed API
  slug: open-mailchimp-removed-api
- collection_type: open
  name: Mailchimp Marketing Abuse Replicate API
  slug: open-mailchimp-replicate-api
- collection_type: open
  name: Mailchimp Marketing Abuse Reporting API
  slug: open-mailchimp-reporting-api
- collection_type: open
  name: Mailchimp Marketing Abuse Reports API
  slug: open-mailchimp-reports-api
- collection_type: open
  name: Mailchimp Marketing Abuse Resend API
  slug: open-mailchimp-resend-api
- collection_type: open
  name: Mailchimp Marketing Abuse Response_id API
  slug: open-mailchimp-response-id-api
- collection_type: open
  name: Mailchimp Marketing Abuse Resume API
  slug: open-mailchimp-resume-api
- collection_type: open
  name: Mailchimp Marketing Abuse Root API
  slug: open-mailchimp-root-api
- collection_type: open
  name: Mailchimp Marketing Abuse Rules API
  slug: open-mailchimp-rules-api
- collection_type: open
  name: Mailchimp Marketing Abuse Schedules API
  slug: open-mailchimp-schedules-api
- collection_type: open
  name: Mailchimp Marketing Abuse Scripts API
  slug: open-mailchimp-scripts-api
- collection_type: open
  name: Mailchimp Marketing Abuse Search API
  slug: open-mailchimp-search-api
- collection_type: open
  name: Mailchimp Marketing Abuse Segments API
  slug: open-mailchimp-segments-api
- collection_type: open
  name: Mailchimp Marketing Abuse Send API
  slug: open-mailchimp-send-api
- collection_type: open
  name: Mailchimp Marketing Abuse Senders API
  slug: open-mailchimp-senders-api
- collection_type: open
  name: Mailchimp Marketing Abuse Sent API
  slug: open-mailchimp-sent-api
- collection_type: open
  name: Mailchimp Marketing Abuse Signup API
  slug: open-mailchimp-signup-api
- collection_type: open
  name: Mailchimp Marketing Abuse Steps API
  slug: open-mailchimp-steps-api
- collection_type: open
  name: Mailchimp Marketing Abuse Stores API
  slug: open-mailchimp-stores-api
- collection_type: open
  name: Mailchimp Marketing Abuse Subaccounts API
  slug: open-mailchimp-subaccounts-api
- collection_type: open
  name: Mailchimp Marketing Abuse Subscribers API
  slug: open-mailchimp-subscribers-api
- collection_type: open
  name: Mailchimp Marketing Abuse Surveys API
  slug: open-mailchimp-surveys-api
- collection_type: open
  name: Mailchimp Marketing Abuse Tags API
  slug: open-mailchimp-tags-api
- collection_type: open
  name: Mailchimp Marketing Abuse Template API
  slug: open-mailchimp-template-api
- collection_type: open
  name: Mailchimp Marketing Abuse Template Folders API
  slug: open-mailchimp-template-folders-api
- collection_type: open
  name: Mailchimp Marketing Abuse Templates API
  slug: open-mailchimp-templates-api
- collection_type: open
  name: Mailchimp Marketing Abuse Tests API
  slug: open-mailchimp-tests-api
- collection_type: open
  name: Mailchimp Transactional API
  slug: open-mailchimp-transactional-api-openapi-original
- collection_type: open
  name: Mailchimp Transactional API
  slug: open-mailchimp-transactional-api
- collection_type: open
  name: Mailchimp Marketing Abuse Trigger API
  slug: open-mailchimp-trigger-api
- collection_type: open
  name: Mailchimp Marketing Abuse Unsubscribed API
  slug: open-mailchimp-unsubscribed-api
- collection_type: open
  name: Mailchimp Marketing Abuse Users API
  slug: open-mailchimp-users-api
- collection_type: open
  name: Mailchimp Marketing Abuse Variants API
  slug: open-mailchimp-variants-api
- collection_type: open
  name: Mailchimp Marketing Abuse Verified API
  slug: open-mailchimp-verified-api
- collection_type: open
  name: Mailchimp Marketing Abuse Verified Domains API
  slug: open-mailchimp-verified-domains-api
- collection_type: open
  name: Mailchimp Marketing Abuse Verify API
  slug: open-mailchimp-verify-api
- collection_type: open
  name: Mailchimp Marketing Abuse Webhooks API
  slug: open-mailchimp-webhooks-api
common:
- group: design
  href: https://artifacts.apis.io/mailchimp/rules/mailchimp-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/mailchimp-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/rules/mailchimp-rules.yml
  title: ''
  type: Spectral
  url: rules/mailchimp-rules.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/rules/mailchimp-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/mailchimp-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/json-ld/mailchimp-transactional-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailchimp-transactional-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailchimp/asyncapi/mailchimp-marketing-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/mailchimp-marketing-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/mailchimp/mcp/mailchimp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mailchimp-mcp.yml
- group: other
  href: https://artifacts.apis.io/mailchimp/hosts/mailchimp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailchimp-hosts.yml
- group: build
  href: https://artifacts.apis.io/mailchimp/integrations/mailchimp-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/mailchimp-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/mailchimp/vendors/mailchimp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailchimp-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://mailchimp.com/newsroom/
- group: commercial
  href: https://artifacts.apis.io/mailchimp/finops/mailchimp-finops.yml
  title: ''
  type: FinOps
  url: finops/mailchimp-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://mailchimp.com/pricing/marketing/
- group: company
  title: ''
  type: Website
  url: https://www.mailchimp.com/
- group: other
  href: https://artifacts.apis.io/mailchimp/capabilities/mailchimp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mailchimp-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/mailchimp/overlays/mailchimp-marketing-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mailchimp-marketing-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mailchimp/agentic-access/mailchimp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailchimp-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/mailchimp/packages/mailchimp-packages.yml
  title: ''
  type: Packages
  url: packages/mailchimp-packages.yml
- group: build
  href: https://artifacts.apis.io/mailchimp/packages/mailchimp-packages.yml
  title: ''
  type: SDKs
  url: packages/mailchimp-packages.yml
- group: agent
  href: https://artifacts.apis.io/mailchimp/well-known/mailchimp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailchimp-well-known.yml
- group: auth
  href: https://artifacts.apis.io/mailchimp/well-known/mailchimp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailchimp-security.txt
- group: agent
  href: https://artifacts.apis.io/mailchimp/mcp/mailchimp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mailchimp-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mailchimp/llms/mailchimp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailchimp-llms.txt
- group: design
  href: https://artifacts.apis.io/mailchimp/conformance/mailchimp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailchimp-conformance.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/errors/mailchimp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailchimp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/lifecycle/mailchimp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mailchimp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/conventions/mailchimp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mailchimp-conventions.yml
- group: operate
  href: https://artifacts.apis.io/mailchimp/changelog/mailchimp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mailchimp-changelog.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/data-model/mailchimp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailchimp-data-model.yml
- group: start
  href: https://artifacts.apis.io/mailchimp/sandbox/mailchimp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mailchimp-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/mailchimp/security/mailchimp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mailchimp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailchimp/security/mailchimp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailchimp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mailchimp/authentication/mailchimp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailchimp-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mailchimp/overview
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-add-member-note-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-add-member-note-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-add-member-tag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-add-member-tag-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-checklist-then-send-campaign-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-checklist-then-send-campaign-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-audience-add-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-audience-add-member-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-campaign-content-test-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-campaign-content-test-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-campaign-set-content-schedule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-campaign-set-content-schedule-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-campaign-set-content-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-campaign-set-content-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-merge-field-add-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-merge-field-add-member-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-static-segment-add-members-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-static-segment-add-members-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-create-template-campaign-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-create-template-campaign-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-find-and-pause-automation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-find-and-pause-automation-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-find-and-start-automation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-find-and-start-automation-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-find-campaign-pull-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-find-campaign-pull-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-find-member-mark-vip-tag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-find-member-mark-vip-tag-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-onboard-member-to-segment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-onboard-member-to-segment-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-put-member-tag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-put-member-tag-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-replicate-campaign-test-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-replicate-campaign-test-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-sync-static-segment-members-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-sync-static-segment-members-workflow.yml
- group: design
  href: https://artifacts.apis.io/mailchimp/arazzo/mailchimp-upsert-member-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/mailchimp-upsert-member-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intuitmailchimp
- group: other
  title: ''
  type: Resources
  url: https://mailchimp.com/developer/tools/
- group: start
  title: ''
  type: Portal
  url: https://mailchimp.com/developer/
- group: operate
  title: ''
  type: ChangeLog
  url: https://mailchimp.com/developer/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://mailchimp.com/developer/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://mailchimp.com/pricing/marketing/
- group: build
  title: ''
  type: SDKs
  url: https://mailchimp.com/developer/marketing/guides/client-libraries-and-sdks/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailchimp.com/
- group: operate
  title: ''
  type: Support
  url: https://mailchimp.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailchimp.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailchimp.com/legal/privacy/
- group: other
  title: ''
  type: API Use Policy
  url: https://mailchimp.com/legal/api_use/
- group: start
  title: ''
  type: Signup
  url: https://login.mailchimp.com/signup/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailchimp
- group: start
  title: ''
  type: Login
  url: https://login.mailchimp.com/
- group: auth
  title: ''
  type: Authentication
  url: https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/mailchimp
- group: build
  title: ''
  type: SDKs
  url: https://mailchimp.com/developer/marketing/docs/mobile-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://mailchimp.com/developer/marketing/docs/fundamentals/
- group: docs
  title: ''
  type: APIReference
  url: https://mailchimp.com/developer/marketing/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://mailchimp.com/developer/marketing/guides/quick-start/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mailchimp/mailchimp-client-lib-codegen
- group: design
  href: https://artifacts.apis.io/mailchimp/vocabulary/mailchimp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailchimp-vocabulary.yml
- group: docs
  href: https://artifacts.apis.io/mailchimp/asyncapi/mailchimp-marketing-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/mailchimp-marketing-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://mailchimp.com/developer/marketing/guides/sync-audience-data-webhooks/
- group: auth
  title: ''
  type: Security
  url: https://mailchimp.com/about/security/#Responsible_Disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://mailchimp.com/about/security/
- group: auth
  href: https://artifacts.apis.io/mailchimp/security/mailchimp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mailchimp-trust-center.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://mailchimp.com/developer/marketing/docs/fundamentals/#api-versions
- group: agent
  href: https://artifacts.apis.io/mailchimp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/mailchimp/mcp/mailchimp-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mailchimp-tool-crosswalk.yml
- group: operate
  href: https://artifacts.apis.io/mailchimp/rate-limits/mailchimp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mailchimp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mailchimp/plans/mailchimp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailchimp-plans-pricing.yml
created: '2023-11-23'
description: 'Mailchimp is an Intuit company providing a marketing automation platform and email marketing service for managing mailing lists, creating email marketing campaigns, and automating marketing workflows. It exposes two distinct developer surfaces: the Marketing API (v3, REST, 298 operations at https://<dc>.api.mailchimp.com/3.0) covering audiences, members, tags, segments, campaigns, content, automations, customer journeys, reports, e-commerce stores and orders, file manager, templates, landing pages, batch operations and webhooks; and Mailchimp Transactional, formerly Mandrill (99 RPC-style POST methods at https://mandrillapp.com/api/1.0), for one-to-one transactional email and SMS, inbound processing, dedicated IP management and subaccounts. Authentication is an API key or OAuth 2 for the Marketing API and a body-parameter API key for Transactional. Mailchimp runs a hosted MCP server for the Transactional API, publishes eight official client libraries and two mobile SDKs, and
  delivers audience events as HMAC-signed webhooks.'
examples:
- key_count: 6
  name: Mailchimp Postallowlistsadd Example
  slug: mailchimp-postallowlistsadd-example
- key_count: 6
  name: Mailchimp Postallowlistsdelete Example
  slug: mailchimp-postallowlistsdelete-example
- key_count: 6
  name: Mailchimp Postallowlistslist Example
  slug: mailchimp-postallowlistslist-example
- key_count: 6
  name: Mailchimp Postexportsactivity Example
  slug: mailchimp-postexportsactivity-example
- key_count: 6
  name: Mailchimp Postexportsallowlist Example
  slug: mailchimp-postexportsallowlist-example
- key_count: 6
  name: Mailchimp Postexportsinfo Example
  slug: mailchimp-postexportsinfo-example
- key_count: 6
  name: Mailchimp Postexportslist Example
  slug: mailchimp-postexportslist-example
- key_count: 6
  name: Mailchimp Postexportsrejects Example
  slug: mailchimp-postexportsrejects-example
- key_count: 6
  name: Mailchimp Postipscreatepool Example
  slug: mailchimp-postipscreatepool-example
- key_count: 6
  name: Mailchimp Postipsdeletepool Example
  slug: mailchimp-postipsdeletepool-example
- key_count: 6
  name: Mailchimp Postipsinfo Example
  slug: mailchimp-postipsinfo-example
- key_count: 6
  name: Mailchimp Postipslist Example
  slug: mailchimp-postipslist-example
- key_count: 6
  name: Mailchimp Postipslistpools Example
  slug: mailchimp-postipslistpools-example
- key_count: 6
  name: Mailchimp Postmessagescancelscheduled Example
  slug: mailchimp-postmessagescancelscheduled-example
- key_count: 6
  name: Mailchimp Postmessagescontent Example
  slug: mailchimp-postmessagescontent-example
- key_count: 6
  name: Mailchimp Postmessagesinfo Example
  slug: mailchimp-postmessagesinfo-example
- key_count: 6
  name: Mailchimp Postmessageslistscheduled Example
  slug: mailchimp-postmessageslistscheduled-example
- key_count: 6
  name: Mailchimp Postmessagesparse Example
  slug: mailchimp-postmessagesparse-example
- key_count: 6
  name: Mailchimp Postmessagesreschedule Example
  slug: mailchimp-postmessagesreschedule-example
- key_count: 6
  name: Mailchimp Postmessagessearch Example
  slug: mailchimp-postmessagessearch-example
- key_count: 6
  name: Mailchimp Postmessagessearchtimeseries Example
  slug: mailchimp-postmessagessearchtimeseries-example
- key_count: 6
  name: Mailchimp Postmessagessend Example
  slug: mailchimp-postmessagessend-example
- key_count: 6
  name: Mailchimp Postmessagessendraw Example
  slug: mailchimp-postmessagessendraw-example
- key_count: 6
  name: Mailchimp Postmessagessendtemplate Example
  slug: mailchimp-postmessagessendtemplate-example
- key_count: 6
  name: Mailchimp Postmetadataadd Example
  slug: mailchimp-postmetadataadd-example
- key_count: 6
  name: Mailchimp Postmetadatadelete Example
  slug: mailchimp-postmetadatadelete-example
- key_count: 6
  name: Mailchimp Postmetadatalist Example
  slug: mailchimp-postmetadatalist-example
- key_count: 6
  name: Mailchimp Postmetadataupdate Example
  slug: mailchimp-postmetadataupdate-example
- key_count: 6
  name: Mailchimp Postrejectsadd Example
  slug: mailchimp-postrejectsadd-example
- key_count: 6
  name: Mailchimp Postrejectsdelete Example
  slug: mailchimp-postrejectsdelete-example
- key_count: 6
  name: Mailchimp Postrejectslist Example
  slug: mailchimp-postrejectslist-example
- key_count: 6
  name: Mailchimp Postsendersadddomain Example
  slug: mailchimp-postsendersadddomain-example
- key_count: 6
  name: Mailchimp Postsenderscheckdomain Example
  slug: mailchimp-postsenderscheckdomain-example
- key_count: 6
  name: Mailchimp Postsendersdomains Example
  slug: mailchimp-postsendersdomains-example
- key_count: 6
  name: Mailchimp Postsendersinfo Example
  slug: mailchimp-postsendersinfo-example
- key_count: 6
  name: Mailchimp Postsenderslist Example
  slug: mailchimp-postsenderslist-example
- key_count: 6
  name: Mailchimp Postsenderstimeseries Example
  slug: mailchimp-postsenderstimeseries-example
- key_count: 6
  name: Mailchimp Postsendersverifydomain Example
  slug: mailchimp-postsendersverifydomain-example
- key_count: 6
  name: Mailchimp Postsubaccountsadd Example
  slug: mailchimp-postsubaccountsadd-example
- key_count: 6
  name: Mailchimp Postsubaccountsdelete Example
  slug: mailchimp-postsubaccountsdelete-example
- key_count: 6
  name: Mailchimp Postsubaccountsinfo Example
  slug: mailchimp-postsubaccountsinfo-example
- key_count: 6
  name: Mailchimp Postsubaccountslist Example
  slug: mailchimp-postsubaccountslist-example
- key_count: 6
  name: Mailchimp Postsubaccountspause Example
  slug: mailchimp-postsubaccountspause-example
- key_count: 6
  name: Mailchimp Postsubaccountsresume Example
  slug: mailchimp-postsubaccountsresume-example
- key_count: 6
  name: Mailchimp Postsubaccountsupdate Example
  slug: mailchimp-postsubaccountsupdate-example
- key_count: 6
  name: Mailchimp Posttagsalltimeseries Example
  slug: mailchimp-posttagsalltimeseries-example
- key_count: 6
  name: Mailchimp Posttagsdelete Example
  slug: mailchimp-posttagsdelete-example
- key_count: 6
  name: Mailchimp Posttagsinfo Example
  slug: mailchimp-posttagsinfo-example
- key_count: 6
  name: Mailchimp Posttagslist Example
  slug: mailchimp-posttagslist-example
- key_count: 6
  name: Mailchimp Posttagstimeseries Example
  slug: mailchimp-posttagstimeseries-example
- key_count: 6
  name: Mailchimp Posttemplatesadd Example
  slug: mailchimp-posttemplatesadd-example
- key_count: 6
  name: Mailchimp Posttemplatesdelete Example
  slug: mailchimp-posttemplatesdelete-example
- key_count: 6
  name: Mailchimp Posttemplatesinfo Example
  slug: mailchimp-posttemplatesinfo-example
- key_count: 6
  name: Mailchimp Posttemplateslist Example
  slug: mailchimp-posttemplateslist-example
- key_count: 6
  name: Mailchimp Posttemplatespublish Example
  slug: mailchimp-posttemplatespublish-example
- key_count: 6
  name: Mailchimp Posttemplatesrender Example
  slug: mailchimp-posttemplatesrender-example
- key_count: 6
  name: Mailchimp Posttemplatestimeseries Example
  slug: mailchimp-posttemplatestimeseries-example
- key_count: 6
  name: Mailchimp Posttemplatesupdate Example
  slug: mailchimp-posttemplatesupdate-example
- key_count: 6
  name: Mailchimp Postusersinfo Example
  slug: mailchimp-postusersinfo-example
- key_count: 6
  name: Mailchimp Postusersping Example
  slug: mailchimp-postusersping-example
- key_count: 6
  name: Mailchimp Postuserssenders Example
  slug: mailchimp-postuserssenders-example
- key_count: 6
  name: Mailchimp Postwebhooksadd Example
  slug: mailchimp-postwebhooksadd-example
- key_count: 6
  name: Mailchimp Postwebhooksdelete Example
  slug: mailchimp-postwebhooksdelete-example
- key_count: 6
  name: Mailchimp Postwebhooksinfo Example
  slug: mailchimp-postwebhooksinfo-example
- key_count: 6
  name: Mailchimp Postwebhookslist Example
  slug: mailchimp-postwebhookslist-example
- key_count: 6
  name: Mailchimp Postwebhooksupdate Example
  slug: mailchimp-postwebhooksupdate-example
- key_count: 10
  name: Mailchimp Transactional Account Stats Example
  slug: mailchimp-transactional-account-stats-example
- key_count: 3
  name: Mailchimp Transactional Allowlist Entry Example
  slug: mailchimp-transactional-allowlist-entry-example
- key_count: 6
  name: Mailchimp Transactional Dedicated Ip Example
  slug: mailchimp-transactional-dedicated-ip-example
- key_count: 4
  name: Mailchimp Transactional Error Example
  slug: mailchimp-transactional-error-example
- key_count: 6
  name: Mailchimp Transactional Export Job Example
  slug: mailchimp-transactional-export-job-example
- key_count: 3
  name: Mailchimp Transactional Ip Pool Example
  slug: mailchimp-transactional-ip-pool-example
- key_count: 11
  name: Mailchimp Transactional Message Content Example
  slug: mailchimp-transactional-message-content-example
- key_count: 0
  name: Mailchimp Transactional Message Detail Example
  slug: mailchimp-transactional-message-detail-example
- key_count: 13
  name: Mailchimp Transactional Message Info Example
  slug: mailchimp-transactional-message-info-example
- key_count: 32
  name: Mailchimp Transactional Message Payload Example
  slug: mailchimp-transactional-message-payload-example
- key_count: 3
  name: Mailchimp Transactional Metadata Field Example
  slug: mailchimp-transactional-metadata-field-example
- key_count: 9
  name: Mailchimp Transactional Parsed Message Example
  slug: mailchimp-transactional-parsed-message-example
- key_count: 9
  name: Mailchimp Transactional Reject Entry Example
  slug: mailchimp-transactional-reject-entry-example
- key_count: 6
  name: Mailchimp Transactional Scheduled Message Example
  slug: mailchimp-transactional-scheduled-message-example
- key_count: 5
  name: Mailchimp Transactional Send Result Example
  slug: mailchimp-transactional-send-result-example
- key_count: 7
  name: Mailchimp Transactional Sender Domain Example
  slug: mailchimp-transactional-sender-domain-example
- key_count: 12
  name: Mailchimp Transactional Sender Info Example
  slug: mailchimp-transactional-sender-info-example
- key_count: 11
  name: Mailchimp Transactional Subaccount Info Example
  slug: mailchimp-transactional-subaccount-info-example
- key_count: 12
  name: Mailchimp Transactional Tag Info Example
  slug: mailchimp-transactional-tag-info-example
- key_count: 17
  name: Mailchimp Transactional Template Info Example
  slug: mailchimp-transactional-template-info-example
- key_count: 11
  name: Mailchimp Transactional Time Series Example
  slug: mailchimp-transactional-time-series-example
- key_count: 7
  name: Mailchimp Transactional User Info Example
  slug: mailchimp-transactional-user-info-example
- key_count: 10
  name: Mailchimp Transactional Webhook Info Example
  slug: mailchimp-transactional-webhook-info-example
features:
- 'Free: 250 contacts, ~500 sends/mo, 1 audience'
- 'Essentials at $13/mo (500 contacts): A/B testing, 4-step automations'
- 'Standard at $20/mo: 200 automation flows, Generative AI'
- 'Premium at $350/mo: predictive segmentation, multivariate testing'
- Marketing API v3 with REST + Batch operations
- 'Concurrency limit: 10 simultaneous connections per user'
- 'Batch operations: 1,000 ops/request, 500 open batches'
- Transactional Email (Mandrill) priced separately
- OAuth 2.0 and API keys
- Webhooks for subscribe/unsubscribe/profile/cleaned/upemail/campaign
- Audiences with tags, segments, custom fields
- Automations with conditional logic
- Customer Journey Builder
- Landing pages, popup forms, signup forms
- 'Reports: opens, clicks, bounces, conversions'
- Pricing scales with active contact count
finops:
- has_sources: true
  method: derived
  name: Mailchimp Finops
  primary_unit: month for 12 months
  service_category: ''
  slug: mailchimp-finops
  template: false
graphqls:
- description: An open source, API-first, modular commerce stack built using Node.js, React, and GraphQL. Formerly known as Reaction Commerce, the project has been discontinued but documentation remains available.
  name: Mailchimp GraphQL API
  slug: mailchimp-graphql
image: https://mailchimp.com/release/plums/cxp/images/apple-touch-icon.png
json_schemas:
- name: Mailchimp Audience (List)
  property_count: 21
  slug: audience
- name: Mailchimp Campaign
  property_count: 18
  slug: campaign
- name: AccountStats
  property_count: 10
  slug: mailchimp-accountstats
- name: AllowlistEntry
  property_count: 3
  slug: mailchimp-allowlistentry
- name: DedicatedIP
  property_count: 6
  slug: mailchimp-dedicatedip
- name: Error
  property_count: 4
  slug: mailchimp-error
- name: ExportJob
  property_count: 6
  slug: mailchimp-exportjob
- name: IPPool
  property_count: 3
  slug: mailchimp-ippool
- name: MessageContent
  property_count: 11
  slug: mailchimp-messagecontent
- name: MessageDetail
  property_count: 2
  slug: mailchimp-messagedetail
- name: MessageInfo
  property_count: 13
  slug: mailchimp-messageinfo
- name: MessagePayload
  property_count: 32
  slug: mailchimp-messagepayload
- name: MetadataField
  property_count: 3
  slug: mailchimp-metadatafield
- name: ParsedMessage
  property_count: 9
  slug: mailchimp-parsedmessage
- name: RejectEntry
  property_count: 9
  slug: mailchimp-rejectentry
- name: ScheduledMessage
  property_count: 6
  slug: mailchimp-scheduledmessage
- name: SenderDomain
  property_count: 7
  slug: mailchimp-senderdomain
- name: SenderInfo
  property_count: 12
  slug: mailchimp-senderinfo
- name: SendResult
  property_count: 5
  slug: mailchimp-sendresult
- name: SubaccountInfo
  property_count: 11
  slug: mailchimp-subaccountinfo
- name: TagInfo
  property_count: 12
  slug: mailchimp-taginfo
- name: TemplateInfo
  property_count: 17
  slug: mailchimp-templateinfo
- name: TimeSeries
  property_count: 11
  slug: mailchimp-timeseries
- name: AccountStats
  property_count: 10
  slug: mailchimp-transactional-account-stats
- name: AllowlistEntry
  property_count: 3
  slug: mailchimp-transactional-allowlist-entry
- name: DedicatedIP
  property_count: 6
  slug: mailchimp-transactional-dedicated-ip
- name: Error
  property_count: 4
  slug: mailchimp-transactional-error
- name: ExportJob
  property_count: 6
  slug: mailchimp-transactional-export-job
- name: IPPool
  property_count: 3
  slug: mailchimp-transactional-ip-pool
- name: MessageContent
  property_count: 11
  slug: mailchimp-transactional-message-content
- name: MessageDetail
  property_count: 0
  slug: mailchimp-transactional-message-detail
- name: MessageInfo
  property_count: 13
  slug: mailchimp-transactional-message-info
- name: MessagePayload
  property_count: 32
  slug: mailchimp-transactional-message-payload
- name: MetadataField
  property_count: 3
  slug: mailchimp-transactional-metadata-field
- name: ParsedMessage
  property_count: 9
  slug: mailchimp-transactional-parsed-message
- name: RejectEntry
  property_count: 9
  slug: mailchimp-transactional-reject-entry
- name: ScheduledMessage
  property_count: 6
  slug: mailchimp-transactional-scheduled-message
- name: SendResult
  property_count: 5
  slug: mailchimp-transactional-send-result
- name: SenderDomain
  property_count: 7
  slug: mailchimp-transactional-sender-domain
- name: SenderInfo
  property_count: 12
  slug: mailchimp-transactional-sender-info
- name: SubaccountInfo
  property_count: 11
  slug: mailchimp-transactional-subaccount-info
- name: TagInfo
  property_count: 12
  slug: mailchimp-transactional-tag-info
- name: TemplateInfo
  property_count: 17
  slug: mailchimp-transactional-template-info
- name: TimeSeries
  property_count: 11
  slug: mailchimp-transactional-time-series
- name: UserInfo
  property_count: 7
  slug: mailchimp-transactional-user-info
- name: WebhookInfo
  property_count: 10
  slug: mailchimp-transactional-webhook-info
- name: UserInfo
  property_count: 7
  slug: mailchimp-userinfo
- name: WebhookInfo
  property_count: 10
  slug: mailchimp-webhookinfo
- name: Mailchimp List Member
  property_count: 32
  slug: member
- name: Mailchimp Template
  property_count: 17
  slug: template
json_structures:
- name: Mailchimp Structure
  property_count: 0
  slug: mailchimp-structure
- name: Mailchimp Transactional Account Stats Structure
  property_count: 10
  slug: mailchimp-transactional-account-stats-structure
- name: Mailchimp Transactional Allowlist Entry Structure
  property_count: 3
  slug: mailchimp-transactional-allowlist-entry-structure
- name: Mailchimp Transactional Dedicated Ip Structure
  property_count: 6
  slug: mailchimp-transactional-dedicated-ip-structure
- name: Mailchimp Transactional Error Structure
  property_count: 4
  slug: mailchimp-transactional-error-structure
- name: Mailchimp Transactional Export Job Structure
  property_count: 6
  slug: mailchimp-transactional-export-job-structure
- name: Mailchimp Transactional Ip Pool Structure
  property_count: 3
  slug: mailchimp-transactional-ip-pool-structure
- name: Mailchimp Transactional Message Content Structure
  property_count: 11
  slug: mailchimp-transactional-message-content-structure
- name: Mailchimp Transactional Message Detail Structure
  property_count: 0
  slug: mailchimp-transactional-message-detail-structure
- name: Mailchimp Transactional Message Info Structure
  property_count: 13
  slug: mailchimp-transactional-message-info-structure
- name: Mailchimp Transactional Message Payload Structure
  property_count: 32
  slug: mailchimp-transactional-message-payload-structure
- name: Mailchimp Transactional Metadata Field Structure
  property_count: 3
  slug: mailchimp-transactional-metadata-field-structure
- name: Mailchimp Transactional Parsed Message Structure
  property_count: 9
  slug: mailchimp-transactional-parsed-message-structure
- name: Mailchimp Transactional Reject Entry Structure
  property_count: 9
  slug: mailchimp-transactional-reject-entry-structure
- name: Mailchimp Transactional Scheduled Message Structure
  property_count: 6
  slug: mailchimp-transactional-scheduled-message-structure
- name: Mailchimp Transactional Send Result Structure
  property_count: 5
  slug: mailchimp-transactional-send-result-structure
- name: Mailchimp Transactional Sender Domain Structure
  property_count: 7
  slug: mailchimp-transactional-sender-domain-structure
- name: Mailchimp Transactional Sender Info Structure
  property_count: 12
  slug: mailchimp-transactional-sender-info-structure
- name: Mailchimp Transactional Subaccount Info Structure
  property_count: 11
  slug: mailchimp-transactional-subaccount-info-structure
- name: Mailchimp Transactional Tag Info Structure
  property_count: 12
  slug: mailchimp-transactional-tag-info-structure
- name: Mailchimp Transactional Template Info Structure
  property_count: 17
  slug: mailchimp-transactional-template-info-structure
- name: Mailchimp Transactional Time Series Structure
  property_count: 11
  slug: mailchimp-transactional-time-series-structure
- name: Mailchimp Transactional User Info Structure
  property_count: 7
  slug: mailchimp-transactional-user-info-structure
- name: Mailchimp Transactional Webhook Info Structure
  property_count: 10
  slug: mailchimp-transactional-webhook-info-structure
jsonld:
- class_count: 0
  name: context Context
  property_count: 5
  slug: context
- class_count: 0
  name: Mailchimp Transactional Context
  property_count: 0
  slug: mailchimp-transactional-context
layout: provider
mcp_servers:
- description: Mailchimp publishes an official hosted MCP server for the Transactional (Mandrill) Messaging API. It exposes nine tools that mirror what the Transactional API can already do, plus onboarding/diagnosis
  name: Mailchimp MCP Server
  slug: mailchimp-mcp-yml
modified: '2026-08-13'
name: Mailchimp
nav: Providers
network: true
overview: 'Mailchimp publishes 54 API contracts indexed on the [APIs.io](https://apis.io/) network, including Automations API, Batches API, Campaigns API, and 51 more. Tagged areas include Campaigns, Email Marketing, Marketing Automation, Newsletters, and Transactional Email.


  The Mailchimp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Mailchimp''s developer surface includes pricing, changelog, sandbox, authentication, developer portal, engineering blog, support, and 78 more developer resources.'
plans:
- name: Mailchimp Plans Pricing
  plan_count: 4
  slug: mailchimp-plans-pricing
- name: Mailchimp Price Estimates
  plan_count: 0
  slug: mailchimp-price-estimates
random_paper: 12
rate_limits:
- limit_count: 4
  name: Mailchimp Rate Limits
  slug: mailchimp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Mailchimp — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mailchimp-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Mailchimp API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: mailchimp-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Mailchimp API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 9
  slug: mailchimp-spectral-rules
score:
  band: exemplar
  composite: 78.3
  coverage:
    artifact_dirs: 40
    catalog_earned: 87.5
    catalog_earned_first_party: 24.0
    catalog_gap: 27.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 94.7
    contract_governance: 24.2
    contract_quality: 65.5
    developer_ergonomics: 83.9
    discoverability: 80.8
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 78.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 83.0
      derived: 0
      marker_coverage: 0.0
      total: 53
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/mailchimp/mailchimp-2026-06-20T184854.png
security:
- kind: authentication
  name: Mailchimp Authentication
  slug: mailchimp-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Mailchimp Domain Security
  slug: mailchimp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mailchimp Vulnerability Disclosure
  slug: mailchimp-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mailchimp Trust Center
  slug: mailchimp-trust-center
  summary_line: SOC 2, ISO 27001, EU-U.S. Data Privacy Framework (incl. UK Extension and Swiss-U.S. DPF), GDPR, VPAT (Section 508 accessibility)
skill_count: 6
skills:
- name: mailchimp-bulk-sync-with-batches
  slug: mailchimp-bulk-sync-with-batches
- name: mailchimp-create-and-send-campaign
  slug: mailchimp-create-and-send-campaign
- name: mailchimp-pull-campaign-report
  slug: mailchimp-pull-campaign-report
- name: mailchimp-send-transactional-message
  slug: mailchimp-send-transactional-message
- name: mailchimp-sync-audience-with-webhooks
  slug: mailchimp-sync-audience-with-webhooks
- name: mailchimp-upsert-audience-member
  slug: mailchimp-upsert-audience-member
slug: mailchimp
tags:
- Campaigns
- Email Marketing
- Marketing Automation
- Newsletters
- Transactional Email
- Audience Management
- SMS
- E-Commerce
- Webhook
- Marketing Analytics
- Email
website: https://www.mailchimp.com/
---
