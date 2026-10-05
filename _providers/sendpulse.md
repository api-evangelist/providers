---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 382
  human_in_the_loop: 7
  name: Sendpulse Agentic Access
  operation_count: 635
  slug: sendpulse-agentic-access
  summary_line: 635 operations · 382 acting · 7 human-in-the-loop
api_count: 20
apis:
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The account API from SendPulse — 1 operation(s) for account.
  name: SendPulse Account API
  phrasing_intents:
  - id: getAccount
    intent: Get my account plan and usage overview
    question: Which pricing plan is my SendPulse chatbot account on?
  phrasing_ops: 1
  slug: sendpulse-account-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Attachments API from SendPulse — 3 operation(s) for attachments.
  name: SendPulse Attachments API
  phrasing_intents:
  - id: createAttachment
    intent: Attach an uploaded file to a CRM record
    question: How do I attach a file from the file manager to a deal or contact?
  - id: createAttachmentsBatch
    intent: Attach several uploaded files in one request
    question: Can I attach multiple files to CRM records in one go?
  - id: updateAttachment
    intent: Replace the file on an existing attachment
    question: Can I point an existing attachment at a different file?
  - id: deleteAttachment
    intent: Delete a file attachment
    question: Can I remove a file attached to a deal or contact?
  phrasing_ops: 4
  slug: sendpulse-attachments-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Automation Flows.
  name: SendPulse Automation Flows API
  phrasing_intents:
  - id: getAutomationFlows
    intent: List automation flows
    question: Which automation flows exist in my account?
  - id: getAutomationFlowStats
    intent: Get overall statistics for an automation flow
    question: How is one automation flow performing overall?
  phrasing_ops: 2
  slug: sendpulse-automation-flows-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Balance.
  name: SendPulse Balance API
  phrasing_intents:
  - id: getBalance
    intent: Get the overall account balance
    question: How much money is left in my SendPulse account?
  - id: getBalanceByCurrency
    intent: Get the account balance in a currency
    question: What is my balance expressed in a specific currency?
  - id: getDetailedBalance
    intent: Get detailed balance, tariffs and limits
    question: Which tariff plans and limits apply to each service on my account?
  phrasing_ops: 3
  slug: sendpulse-balance-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Blacklist.
  name: SendPulse Blacklist API
  phrasing_intents:
  - id: getBlacklist
    intent: List blacklisted email addresses
    question: Which email addresses are on my blacklist?
  - id: addToBlacklist
    intent: Add email addresses to the blacklist
    question: How do I block email addresses from ever receiving my mailings?
  - id: removeFromBlacklist
    intent: Remove email addresses from the blacklist
    question: Can I unblock an address I blacklisted by mistake?
  phrasing_ops: 3
  slug: sendpulse-blacklist-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Board attributes API from SendPulse — 2 operation(s) for board attributes.
  name: SendPulse Board attributes API
  phrasing_intents:
  - id: getBoardAttributes
    intent: List the task attributes defined on a board
    question: What custom fields do tasks on a particular board have?
  - id: createBoardAttribute
    intent: Create a task attribute on a board
    question: How do I add a custom field to all tasks on a board?
  - id: updateBoardAttribute
    intent: Update a board's task attribute definition
    question: How do I rename a custom field on a task board?
  phrasing_ops: 3
  slug: sendpulse-board-attributes-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The bots API from SendPulse — 2 operation(s) for bots.
  name: SendPulse Bots API
  phrasing_intents:
  - id: getBots
    intent: List connected chatbots
    question: Which chatbots are connected to my account?
  - id: getBotStatistics
    intent: Get statistics for a chatbot
    question: What are the general statistics for one of my bots?
  phrasing_ops: 2
  slug: sendpulse-bots-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Bounces API from SendPulse — 2 operation(s) for bounces.
  name: SendPulse Bounces API
  phrasing_intents:
  - id: getSmtpBouncesDay
    intent: List email bounces for one day
    question: Which SMTP emails bounced on a given day?
  - id: getSmtpBouncesTotal
    intent: Count total email bounces
    question: How many bounces has my SMTP sending had in total?
  phrasing_ops: 2
  slug: sendpulse-bounces-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Campaigns.
  name: SendPulse Campaigns API
  phrasing_intents:
  - id: createCampaign
    intent: Create and send or schedule an email campaign
    question: How do I send an email campaign to one of my mailing lists?
  - id: getCampaigns
    intent: List email campaigns and their status
    question: Where can I see the history and status of all my SendPulse email campaigns?
  - id: getCampaignById
    intent: Get details and stats for one email campaign
    question: What are the open and delivery stats for a specific email campaign?
  - id: updateCampaign
    intent: Edit a scheduled email campaign's name or subject
    question: Can I change the subject line of an email campaign that is still scheduled?
  - id: cancelCampaign
    intent: Cancel a pending email campaign
    question: Can I stop an email campaign that is already pending or processing?
  - id: getCampaignCountryStats
    intent: Break down email campaign opens by country
    question: Which countries opened my email campaign the most?
  - id: getCampaignReferralStats
    intent: Break down link clicks in an email campaign
    question: Which links in my email campaign got clicked the most?
  - id: getCampaignsByList
    intent: List the campaigns sent to a mailing list
    question: What email campaigns have been sent to a particular mailing list?
  phrasing_ops: 24
  slug: sendpulse-campaigns-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The chats API from SendPulse — 3 operation(s) for chats.
  name: SendPulse Chats API
  phrasing_intents:
  - id: getChats
    intent: List chatbot conversations
    question: Which contacts have chatted with my bot recently?
  - id: getChatMessages
    intent: Get the messages in a contact's chat
    question: What has a specific contact said to my chatbot?
  - id: reactToChatMessage
    intent: React to a contact's chat message
    question: Can I react with an emoji to a message a contact sent?
  phrasing_ops: 3
  slug: sendpulse-chats-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Checklist Items API from SendPulse — 2 operation(s) for checklist items.
  name: SendPulse Checklist Items API
  phrasing_intents:
  - id: createChecklistItems
    intent: Add an item to a checklist
    question: How do I add a new item to a checklist?
  - id: reorderChecklistItem
    intent: Reorder an item in a checklist
    question: Can I change the position of an item in a checklist?
  - id: updateChecklistItem
    intent: Edit or tick off a checklist item
    question: Can I mark a checklist item as done?
  - id: deleteChecklistItem
    intent: Delete a checklist item
    question: Can I delete one item from a checklist?
  phrasing_ops: 4
  slug: sendpulse-checklist-items-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Company API from SendPulse — 4 operation(s) for company.
  name: SendPulse Company API
  phrasing_intents:
  - id: getCompaniesShortData
    intent: Look up companies in a compact summary form
    question: Can I get just the short summary of CRM companies matching a name or email?
  - id: getCompaniesList
    intent: Search and list CRM companies with full details
    question: Which CRM companies were created between two dates, with their full records?
  - id: createCompany
    intent: Create a company in the CRM
    question: How do I add a new company record to my CRM?
  - id: getCompanyById
    intent: Get a company's details
    question: What does the CRM have on file for a particular company?
  - id: updateCompany
    intent: Update a company's details
    question: How do I rename an existing company in the CRM?
  - id: deleteCompany
    intent: Delete a company
    question: How do I remove a company from my CRM entirely?
  phrasing_ops: 6
  slug: sendpulse-company-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Company Attributes API from SendPulse — 2 operation(s) for company attributes.
  name: SendPulse Company Attributes API
  phrasing_intents:
  - id: getCompanyAttributes
    intent: List company attribute definitions
    question: What custom fields are defined for companies in my CRM?
  - id: createCompanyAttribute
    intent: Create a company attribute
    question: How do I add a new custom field for companies?
  - id: updateCompanyAttribute
    intent: Update a company attribute definition
    question: How do I rename a custom company field?
  - id: deleteCompanyAttribute
    intent: Delete a company attribute
    question: How do I remove a custom company field I don't need?
  phrasing_ops: 4
  slug: sendpulse-company-attributes-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Company history API from SendPulse — 1 operation(s) for company history.
  name: SendPulse Company history API
  phrasing_intents:
  - id: getCompanyHistory
    intent: Get a company's change history
    question: What changes have been made to a company record in my CRM?
  phrasing_ops: 1
  slug: sendpulse-company-history-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Compliance API from SendPulse — 2 operation(s) for compliance.
  name: SendPulse Compliance API
  phrasing_intents:
  - id: addSmsBlacklist
    intent: Add phone numbers to the SMS blacklist
    question: How do I stop SMS from going to certain phone numbers?
  - id: removeSmsBlacklist
    intent: Remove phone numbers from the SMS blacklist
    question: Can I unblock a number so it receives SMS again?
  - id: getSmsBlacklist
    intent: List phone numbers on the SMS blacklist
    question: Which phone numbers are blocked from receiving my SMS?
  - id: getViberBlacklist
    intent: List phone numbers on the Viber blacklist
    question: Which phone numbers are excluded from my Viber campaigns?
  - id: addViberBlacklist
    intent: Add phone numbers to the Viber blacklist
    question: How do I exclude a phone number from Viber messages?
  - id: removeViberBlacklist
    intent: Remove phone numbers from the Viber blacklist
    question: Can I let a blocked number receive Viber campaigns again?
  phrasing_ops: 6
  slug: sendpulse-compliance-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Configuration API from SendPulse — 9 operation(s) for configuration.
  name: SendPulse Configuration API
  phrasing_intents:
  - id: getSmsSenders
    intent: List SMS sender IDs
    question: Which SMS sender IDs are registered on my account?
  - id: getSmtpIps
    intent: List the IP addresses used to send email
    question: Which IP addresses does my transactional email go out from?
  - id: getSmtpSenders
    intent: List sender email addresses
    question: Which sender email addresses are set up on my account?
  - id: getSmtpAllowedDomains
    intent: List allowed sender domains for SMTP
    question: Which domains am I allowed to send SMTP email from?
  - id: addSmtpSender
    intent: Add a sender email address
    question: How do I add a new from-address for sending email?
  - id: addSmtpDomain
    intent: Add an allowed sender domain for SMTP
    question: Can I add my own domain so I can send SMTP email from it?
  - id: getViberSenders
    intent: List Viber sender names
    question: Which Viber sender names do I have?
  - id: getViberSenderProfile
    intent: Get a Viber sender name's profile
    question: Can I see the details of one Viber sender name?
  phrasing_ops: 9
  slug: sendpulse-configuration-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact Attributes API from SendPulse — 2 operation(s) for contact attributes.
  name: SendPulse Contact Attributes API
  phrasing_intents:
  - id: getContactAttributes
    intent: List CRM contact attributes
    question: What custom fields exist for my CRM contacts?
  - id: createContactAttribute
    intent: Create a custom contact attribute
    question: How do I add a new custom field to my CRM contacts?
  - id: updateContactAttribute
    intent: Update a contact attribute
    question: Can I rename a contact attribute or change its display order?
  - id: deleteContactAttribute
    intent: Delete a contact attribute
    question: Can I delete a custom contact field I no longer use?
  phrasing_ops: 4
  slug: sendpulse-contact-attributes-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact attributes Value API from SendPulse — 2 operation(s) for contact attributes value.
  name: SendPulse Contact attributes Value API
  phrasing_intents:
  - id: getContactAttributes
    intent: List a contact's attribute values
    question: What custom attribute values are set on a contact?
  - id: addContactAttributeValue
    intent: Set an attribute value on a contact
    question: How do I add a custom attribute value to a contact?
  - id: updateContactAttributeValue
    intent: Change a contact's existing attribute value
    question: Can I change an attribute value a contact already has?
  - id: deleteContactAttributeValue
    intent: Clear an attribute value from a contact
    question: Can I remove a custom attribute value from a contact?
  phrasing_ops: 4
  slug: sendpulse-contact-attributes-value-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact Attributes Values API from SendPulse — 1 operation(s) for contact attributes values.
  name: SendPulse Contact Attributes Values API
  phrasing_intents:
  - id: batchStoreContactAttributeValues
    intent: Set several attribute values on a contact
    question: Can I set many custom attribute values on a contact in one request?
  phrasing_ops: 1
  slug: sendpulse-contact-attributes-values-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact email addresses API from SendPulse — 2 operation(s) for contact email addresses.
  name: SendPulse Contact email addresses API
  phrasing_intents:
  - id: addContactEmails
    intent: Add an email address to a CRM contact
    question: How do I add another email address to a contact?
  - id: updateContactEmail
    intent: Change a contact's email address
    question: Can I correct a typo in a contact's email?
  - id: deleteContactEmail
    intent: Remove an email address from a contact
    question: Can I delete an old email address from a contact?
  phrasing_ops: 3
  slug: sendpulse-contact-email-addresses-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact history API from SendPulse — 1 operation(s) for contact history.
  name: SendPulse Contact history API
  phrasing_intents:
  - id: getContactHistory
    intent: Get a contact's activity history
    question: What happened with a CRM contact over the last month?
  phrasing_ops: 1
  slug: sendpulse-contact-history-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact phone number API from SendPulse — 2 operation(s) for contact phone number.
  name: SendPulse Contact phone number API
  phrasing_intents:
  - id: addContactPhone
    intent: Add a phone number to a CRM contact
    question: How do I add another phone number to an existing contact?
  - id: updateContactPhone
    intent: Change a CRM contact's phone number
    question: How do I fix a wrong phone number saved on a CRM contact?
  - id: deleteContactPhone
    intent: Remove a phone number from a CRM contact
    question: How do I delete an old phone number from a contact?
  phrasing_ops: 3
  slug: sendpulse-contact-phone-number-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contact tags API from SendPulse — 3 operation(s) for contact tags.
  name: SendPulse Contact tags API
  phrasing_intents:
  - id: addTagToContact
    intent: Add a tag to a CRM contact
    question: How do I tag a contact in the CRM?
  - id: deleteContactTagFromContact
    intent: Remove a tag from a CRM contact
    question: Can I take a tag off one contact without deleting the tag?
  - id: listContactTags
    intent: List contact tags with usage counts
    question: What contact tags exist and how many contacts use each one?
  - id: createContactTag
    intent: Create a contact tag
    question: How do I create a new tag for CRM contacts?
  - id: updateContactTag
    intent: Rename or recolor a contact tag
    question: Can I rename a contact tag?
  - id: deleteContactTag
    intent: Delete a contact tag
    question: Can I delete a contact tag entirely?
  phrasing_ops: 6
  slug: sendpulse-contact-tags-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contacts API from SendPulse — 51 operation(s) for contacts.
  name: SendPulse Contacts API
  phrasing_intents:
  - id: getContactsList
    intent: Filter and list CRM contacts
    question: Which CRM contacts were created in a given date range?
  - id: getContactListByEmail
    intent: Find CRM contacts by email address
    question: Is there already a CRM contact with this email address?
  - id: createContact
    intent: Create a CRM contact (deprecated endpoint)
    question: Does the older deprecated create-contact endpoint still accept phones, emails and tags in one call?
  - id: postContactsCreate
    intent: Create a CRM contact
    question: What's the current way to add a new contact to my CRM?
  - id: getContactById
    intent: Get a CRM contact's details
    question: What does the CRM know about a contact, including phones, emails and deal count?
  - id: updateContact
    intent: Update a CRM contact
    question: How do I change the name on an existing CRM contact?
  - id: deleteContactById
    intent: Delete a CRM contact
    question: How do I permanently remove a contact from my CRM?
  - id: getContactDeals
    intent: List a contact's deals
    question: Which deals is a CRM contact involved in?
  phrasing_ops: 57
  slug: sendpulse-contacts-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Contacts messengers API from SendPulse — 2 operation(s) for contacts messengers.
  name: SendPulse Contacts messengers API
  phrasing_intents:
  - id: addContactMessenger
    intent: Add a messenger account to a contact
    question: How do I link a messenger login to a CRM contact?
  - id: updateContactMessenger
    intent: Update a contact's messenger account
    question: Can I change the login of a messenger already on a contact?
  - id: removeContactMessenger
    intent: Remove a messenger account from a contact
    question: Can I unlink a messenger from a contact?
  phrasing_ops: 3
  slug: sendpulse-contacts-messengers-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Conversions.
  name: SendPulse Conversions API
  phrasing_intents:
  - id: getConversions
    intent: Get conversions for an automation flow
    question: How many conversions did my automation flow generate?
  phrasing_ops: 1
  slug: sendpulse-conversions-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Course tariffs API from SendPulse — 1 operation(s) for course tariffs.
  name: SendPulse Course tariffs API
  phrasing_intents:
  - id: getCourseTariffs
    intent: List a course's pricing tariffs
    question: What pricing tariffs are available for a course?
  phrasing_ops: 1
  slug: sendpulse-course-tariffs-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Courses API from SendPulse — 1 operation(s) for courses.
  name: SendPulse Courses API
  phrasing_intents:
  - id: getCourses
    intent: List all my online courses
    question: What online courses have I created in SendPulse?
  phrasing_ops: 1
  slug: sendpulse-courses-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Custom Tab API from SendPulse — 3 operation(s) for custom tab.
  name: SendPulse Custom Tab API
  phrasing_intents:
  - id: getCustomTabs
    intent: List my custom tabs
    question: What custom tabs have I set up in the CRM?
  - id: createCustomTab
    intent: Create a custom tab
    question: How do I add a new custom tab to group attributes on a deal or contact card?
  - id: updateCustomTab
    intent: Rename, reorder or hide a custom tab
    question: Can I change the order of my custom tabs?
  - id: deleteCustomTab
    intent: Delete a custom tab
    question: How do I get rid of a custom tab I no longer need?
  - id: addCustomTabRelation
    intent: Link attributes to a custom tab
    question: How do I place an attribute inside one of my custom tabs?
  - id: deleteCustomTabRelation
    intent: Unlink attributes from a custom tab
    question: How do I take an attribute out of a custom tab without deleting the tab?
  phrasing_ops: 6
  slug: sendpulse-custom-tab-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deal attribute Value API from SendPulse — 3 operation(s) for deal attribute value.
  name: SendPulse Deal attribute Value API
  phrasing_intents:
  - id: getDealAttributeValues
    intent: Get the attribute values set on a deal
    question: What custom field values are filled in on a particular deal?
  - id: addDealAttribute
    intent: Set an attribute value on a deal
    question: How do I fill in a custom field on a deal for the first time?
  - id: listDealAttributesByPipeline
    intent: List deal attribute values across a pipeline
    question: Can I pull the attribute values of every deal in one pipeline at once?
  - id: updateDealAttributeValue
    intent: Overwrite an existing deal attribute value
    question: How do I change a custom field value that's already set on a deal?
  phrasing_ops: 4
  slug: sendpulse-deal-attribute-value-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deal Attributes API from SendPulse — 3 operation(s) for deal attributes.
  name: SendPulse Deal Attributes API
  phrasing_intents:
  - id: listPipelineAttributes
    intent: List deal attribute definitions in a pipeline
    question: Which custom deal fields are defined for a sales pipeline?
  - id: createPipelineAttribute
    intent: Define a new deal attribute on a pipeline
    question: How do I add a custom field to deals in one pipeline?
  - id: updatePipelineAttribute
    intent: Change a pipeline's deal attribute definition
    question: How do I rename a custom deal field in a pipeline?
  - id: deletePipelineAttribute
    intent: Delete a deal attribute definition from a pipeline
    question: How do I remove a custom deal field from a pipeline for good?
  - id: deleteDealAttribute
    intent: Remove an attribute from a single deal
    question: How do I clear a custom field from one deal without touching the pipeline definition?
  phrasing_ops: 5
  slug: sendpulse-deal-attributes-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deal contacts API from SendPulse — 2 operation(s) for deal contacts.
  name: SendPulse Deal contacts API
  phrasing_intents:
  - id: getDealContacts
    intent: List the contacts in a deal
    question: Who are the contacts involved in a deal?
  - id: addContactToDeal
    intent: Add a contact to a deal
    question: How do I link an existing contact to a deal?
  - id: removeDealContact
    intent: Remove a contact from a deal
    question: Can I take a contact off a deal without deleting the contact?
  phrasing_ops: 3
  slug: sendpulse-deal-contacts-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deal Expiration API from SendPulse — 1 operation(s) for deal expiration.
  name: SendPulse Deal Expiration API
  phrasing_intents:
  - id: upsertDealExpiration
    intent: Set or change a deal's expiration
    question: Can I set a deadline on a deal and get notified before it expires?
  - id: removeDealExpiration
    intent: Remove a deal's expiration
    question: Can I clear the expiration date from a deal?
  phrasing_ops: 2
  slug: sendpulse-deal-expiration-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deal history API from SendPulse — 1 operation(s) for deal history.
  name: SendPulse Deal history API
  phrasing_intents:
  - id: getDealHistory
    intent: Get a deal's change history for a period
    question: What changed on a deal over the last month?
  phrasing_ops: 1
  slug: sendpulse-deal-history-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deal notes API from SendPulse — 2 operation(s) for deal notes.
  name: SendPulse Deal notes API
  phrasing_intents:
  - id: getDealComments
    intent: List notes on a deal
    question: What notes have been left on a deal?
  - id: addDealComment
    intent: Add a note to a deal
    question: How do I add a note to a deal?
  - id: updateDealComment
    intent: Edit a note on a deal
    question: Can I edit a note I already added to a deal?
  - id: deleteDealComment
    intent: Remove a note from a deal
    question: Can I delete a note from a deal?
  phrasing_ops: 4
  slug: sendpulse-deal-notes-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Deals API from SendPulse — 4 operation(s) for deals.
  name: SendPulse Deals API
  phrasing_intents:
  - id: getDealsList
    intent: Search and filter deals in the CRM
    question: Which deals in my CRM are still active?
  - id: createDeal
    intent: Create a new deal in a pipeline
    question: How do I add a new deal to a sales pipeline?
  - id: getDeal
    intent: Get the details of a deal
    question: What stage is a particular deal at and who owns it?
  - id: updateDealById
    intent: Update a deal's details
    question: Can I change the amount, status or stage of an existing deal?
  - id: deleteDeal
    intent: Delete a deal
    question: Can I permanently delete a deal from my CRM?
  - id: changeDealPipeline
    intent: Move a deal to another pipeline
    question: Can I move a deal from one sales pipeline to another?
  phrasing_ops: 6
  slug: sendpulse-deals-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The dialogs API from SendPulse — 1 operation(s) for dialogs.
  name: SendPulse Dialogs API
  phrasing_intents:
  - id: getDialogs
    intent: List chat dialogs across channels
    question: Can I see my conversations from all chat channels in one list?
  phrasing_ops: 1
  slug: sendpulse-dialogs-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: directory entity
  name: SendPulse Directory API
  phrasing_intents:
  - id: createDirectory
    intent: Create a folder in file storage
    question: How do I create a new folder in my file storage?
  - id: getDirectory
    intent: Get the file storage directory tree
    question: What folders are in my file storage?
  - id: getDirectorySize
    intent: Get file storage usage statistics
    question: How much file storage space am I using?
  - id: getDirectoryContents
    intent: List the contents of a folder
    question: What files are inside a specific folder?
  - id: findDirectoryFiles
    intent: Search for files in a folder
    question: Can I search for a file by name inside a folder?
  phrasing_ops: 5
  slug: sendpulse-directory-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The ECommerce Product API from SendPulse — 14 operation(s) for ecommerce product.
  name: SendPulse ECommerce Product API
  phrasing_intents:
  - id: getProductsByFilter
    intent: Search the product catalog with filters
    question: Can I find products in my catalog by category and price range?
  - id: getCategoryProduct
    intent: Get a product within a specific category
    question: Can I look up a product through the category it belongs to?
  - id: addProductToDeal
    intent: Add a product to a CRM deal
    question: How do I attach a product from my catalog to a sales deal?
  - id: getProductsByDealId
    intent: List the products on a deal
    question: Which products are attached to a particular deal?
  - id: updateProductsInDeal
    intent: Change quantity or amount of a deal product
    question: Can I change how many units of a product are in a deal?
  - id: getProductsByContactDeals
    intent: List products across a contact's deals
    question: What products has a given contact got across all of their deals?
  - id: detachProductFromDeal
    intent: Remove a product from a deal
    question: How do I take a product off a deal?
  - id: getProductById
    intent: Get a product by its ID
    question: Can I fetch a single product just by its ID?
  phrasing_ops: 19
  slug: sendpulse-ecommerce-product-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Element Statistics.
  name: SendPulse Element Statistics API
  phrasing_intents:
  - id: getElementTotalStats
    intent: Get stats for every element of an automation flow
    question: Can I see performance numbers for each step of my automation flow at once?
  - id: getStartStats
    intent: Get stats for a flow's Start element
    question: How many contacts entered my automation through its Start trigger?
  - id: getEmailStats
    intent: Get stats for an Email element in a flow
    question: What are the opens and clicks for the email step in my automation?
  - id: getPushStats
    intent: Get stats for a Push element in a flow
    question: How did the web push step in my automation flow perform?
  - id: getSmsStats
    intent: Get stats for an SMS element in a flow
    question: How many automated SMS messages were delivered by my flow?
  - id: getMessengerStats
    intent: Get stats for a Messenger element in a flow
    question: How did the messenger message step in my automation perform?
  - id: getFilterStats
    intent: Get stats for a Filter element in a flow
    question: How many contacts passed the filter step in my automation?
  - id: getConditionStats
    intent: Get stats for a Condition element in a flow
    question: How many contacts went down each branch of my automation condition?
  phrasing_ops: 10
  slug: sendpulse-element-statistics-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Email address.
  name: SendPulse Email address API
  phrasing_intents:
  - id: updateContactVariables
    intent: Update a subscriber's variables in a mailing list
    question: How do I change custom field values for one subscriber in a mailing list?
  - id: getEmailInfo
    intent: Find which mailing lists an email belongs to
    question: Which mailing lists is this email address subscribed to?
  - id: deleteEmailGlobally
    intent: Remove an email from all mailing lists
    question: How do I wipe a subscriber from every mailing list at once?
  - id: getEmailDetails
    intent: Get list membership details for an email
    question: When and from what source was this email added to my lists?
  - id: getMultipleEmailsInfo
    intent: Check subscriber status for many emails at once
    question: Can I check the subscription status of a batch of email addresses in one call?
  - id: getEmailCampaignStats
    intent: Get campaign engagement stats for one subscriber
    question: Which campaigns did a particular subscriber open or click?
  - id: getEmailCampaignInfo
    intent: See what happened to an email in one campaign
    question: Did a specific recipient open or bounce a particular campaign?
  - id: getEmailFromList
    intent: Get a subscriber's status and variables in one list
    question: What variables and status does a subscriber have in a specific mailing list?
  phrasing_ops: 9
  slug: sendpulse-email-address-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Emails API from SendPulse — 7 operation(s) for emails.
  name: SendPulse Emails API
  phrasing_intents:
  - id: getCompanyEmails
    intent: List a company's email addresses
    question: What email addresses are stored for a CRM company?
  - id: createCompanyEmail
    intent: Add an email address to a company
    question: How do I add one email address to a company in the CRM?
  - id: batchCreateCompanyEmails
    intent: Add several email addresses to a company
    question: Can I add many email addresses to a company in one request?
  - id: updateCompanyEmail
    intent: Update a company's email address
    question: How do I correct an email address saved on a company?
  - id: deleteCompanyEmail
    intent: Delete a company's email address
    question: Can I remove an outdated email address from a company?
  - id: sendSmtpEmail
    intent: Send a transactional email over SMTP
    question: How do I send a transactional email through the SMTP service?
  - id: getSmtpEmails
    intent: List transactional emails sent via SMTP
    question: Which transactional emails did I send through SMTP last week?
  - id: getSmtpEmailsTotal
    intent: Count total SMTP emails sent
    question: How many emails have I sent through SMTP in total?
  phrasing_ops: 10
  slug: sendpulse-emails-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Events.
  name: SendPulse Events API
  phrasing_intents:
  - id: deleteLogs
    intent: Delete event logs
    question: Can I clear out the logs of automation events I've sent?
  phrasing_ops: 1
  slug: sendpulse-events-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: file entity
  name: SendPulse File API
  phrasing_intents:
  - id: uploadFile
    intent: Upload files to storage
    question: How do I upload a file to my storage folder?
  - id: deleteFile
    intent: Delete a file from storage
    question: Can I delete a file from storage?
  - id: checkFileExist
    intent: Check whether a file exists
    question: Is there already a file at a given storage path?
  - id: filterFiles
    intent: List files in a folder by date
    question: Which files were uploaded to a folder in a date range?
  phrasing_ops: 4
  slug: sendpulse-file-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The File Manager API from SendPulse — 1 operation(s) for file manager.
  name: SendPulse File Manager API
  phrasing_intents:
  - id: uploadFiles
    intent: Upload files to the file manager
    question: How do I upload files so I can attach them later?
  phrasing_ops: 1
  slug: sendpulse-file-manager-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The flows API from SendPulse — 3 operation(s) for flows.
  name: SendPulse Flows API
  phrasing_intents:
  - id: getFlows
    intent: List a chatbot's flows
    question: What flows have I built for my chatbot?
  - id: runFlow
    intent: Run a chatbot flow for a contact by flow ID
    question: How do I start a specific chatbot flow for one subscriber?
  - id: runFlowByTrigger
    intent: Run a chatbot flow by trigger keyword
    question: Can I launch a bot flow by its trigger keyword instead of its ID?
  phrasing_ops: 3
  slug: sendpulse-flows-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Mailing List Verification.
  name: SendPulse Mailing List Verification API
  phrasing_intents:
  - id: verifyMailingList
    intent: Start verifying a mailing list
    question: How can I clean an entire mailing list of invalid addresses?
  - id: getVerificationProgress
    intent: Check mailing list verification progress
    question: How far along is the verification of my mailing list?
  - id: getVerificationResults
    intent: Get per-address results of a list verification
    question: Which addresses in my verified mailing list came back invalid?
  - id: getVerifiedLists
    intent: List mailing lists that have been verified
    question: Which of my mailing lists have already been through verification?
  phrasing_ops: 4
  slug: sendpulse-mailing-list-verification-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Mailing lists.
  name: SendPulse Mailing lists API
  phrasing_intents:
  - id: createMailingList
    intent: Create a mailing list
    question: How do I create a new mailing list?
  - id: getMailingLists
    intent: List mailing lists
    question: What mailing lists do I have in my account?
  - id: getMailingListById
    intent: Get a mailing list's details
    question: What details are available about one specific mailing list?
  - id: updateMailingList
    intent: Rename a mailing list
    question: Can I rename an existing mailing list?
  - id: deleteMailingList
    intent: Delete a mailing list
    question: How do I permanently delete a mailing list?
  - id: getMailingListVariables
    intent: List a mailing list's variables
    question: Which variables are defined on a mailing list?
  - id: getEmailsFromMailingList
    intent: List contacts in a mailing list
    question: How do I get all the email contacts in a mailing list?
  - id: addEmailsToMailingList
    intent: Add contacts to a mailing list
    question: Can I add subscribers to a mailing list with double opt-in?
  phrasing_ops: 14
  slug: sendpulse-mailing-lists-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The ManagerSettings API from SendPulse — 5 operation(s) for managersettings.
  name: SendPulse Manager Settings API
  phrasing_intents:
  - id: listManagerSettingsSections
    intent: List manager settings sections
    question: What sections can managers be assigned to?
  - id: getManagerSettingsManagers
    intent: List all managers
    question: Who are all the managers in my account?
  - id: createManagerSettings
    intent: Assign managers to a section
    question: How do I assign managers to a section?
  - id: updateManagerSetting
    intent: Change managers on a manager setting
    question: Can I change which managers belong to an existing manager setting?
  - id: deleteManagersFromManagerSetting
    intent: Remove managers from a manager setting
    question: Can I remove certain managers from a section assignment?
  - id: getManagersBySection
    intent: List managers assigned to a section
    question: Which managers are assigned to a given section?
  phrasing_ops: 6
  slug: sendpulse-managersettings-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The messengers API from SendPulse — 3 operation(s) for messengers.
  name: SendPulse Messengers API
  phrasing_intents:
  - id: getCompanyMessengers
    intent: List a company's messenger accounts
    question: Which messenger accounts are stored for a company?
  - id: createCompanyMessenger
    intent: Add a messenger account to a company
    question: How do I add a messenger account to a company record?
  - id: batchCreateCompanyMessengers
    intent: Add several messengers to a company
    question: Can I add many messenger accounts to a company at once?
  - id: updateCompanyMessenger
    intent: Update a company's messenger account
    question: Can I edit a messenger handle saved on a company?
  - id: deleteCompanyMessenger
    intent: Delete a company's messenger account
    question: Can I remove a messenger account from a company?
  phrasing_ops: 5
  slug: sendpulse-messengers-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Messengers types API from SendPulse — 1 operation(s) for messengers types.
  name: SendPulse Messengers types API
  phrasing_intents:
  - id: getMessengerTypes
    intent: List supported messenger types
    question: Which messenger types can I store for contacts?
  phrasing_ops: 1
  slug: sendpulse-messengers-types-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Payments API from SendPulse — 6 operation(s) for payments.
  name: SendPulse Payments API
  phrasing_intents:
  - id: getAllPayments
    intent: List all my payments
    question: What payments have been recorded across my whole account?
  - id: getDealPayments
    intent: List payments for a deal
    question: Which payments have been made against a particular deal?
  - id: getPaymentsByContactId
    intent: List payments made by a contact
    question: What has a specific contact paid me?
  - id: createPayment
    intent: Record a manual payment
    question: How do I log a payment I received offline against a deal?
  - id: approvePayment
    intent: Approve a manual payment
    question: How do I mark a manually entered payment as approved?
  - id: cancelPayment
    intent: Cancel a manual payment
    question: How do I cancel a manual payment that was entered by mistake?
  phrasing_ops: 6
  slug: sendpulse-payments-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Phones API from SendPulse — 3 operation(s) for phones.
  name: SendPulse Phones API
  phrasing_intents:
  - id: getCompanyPhones
    intent: List a company's phone numbers
    question: What phone numbers are stored for a CRM company?
  - id: createCompanyPhone
    intent: Add a phone number to a company
    question: How do I add one phone number to a company record?
  - id: batchCreateCompanyPhones
    intent: Add several phone numbers to a company at once
    question: Can I add multiple phone numbers to a company in one request?
  - id: updateCompanyPhone
    intent: Change a company phone number
    question: How do I correct a phone number already saved on a company?
  - id: deleteCompanyPhone
    intent: Delete a company phone number
    question: How do I remove an outdated phone number from a company?
  phrasing_ops: 5
  slug: sendpulse-phones-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Pipeline Steps API from SendPulse — 2 operation(s) for pipeline steps.
  name: SendPulse Pipeline Steps API
  phrasing_intents:
  - id: createPipelineStep
    intent: Add a stage to a sales pipeline
    question: How do I add a new stage to a deal pipeline?
  - id: getPipelineSteps
    intent: List the stages of a sales pipeline
    question: What stages does my sales pipeline have?
  - id: updatePipelineStep
    intent: Update a stage in a sales pipeline
    question: Can I rename or recolor an existing pipeline stage?
  - id: deletePipelineStep
    intent: Delete a stage from a sales pipeline
    question: Can I remove a stage from my pipeline?
  phrasing_ops: 4
  slug: sendpulse-pipeline-steps-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Pipelines API from SendPulse — 2 operation(s) for pipelines.
  name: SendPulse Pipelines API
  phrasing_intents:
  - id: createPipeline
    intent: Create a deal pipeline
    question: How do I create a new sales pipeline?
  - id: getPipelines
    intent: List deal pipelines
    question: What sales pipelines do I have?
  - id: getPipelineById
    intent: Get a pipeline by ID
    question: Can I get the statuses and settings of one pipeline?
  - id: updatePipeline
    intent: Update a pipeline
    question: Can I rename an existing pipeline?
  phrasing_ops: 4
  slug: sendpulse-pipelines-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Popup API from SendPulse — 5 operation(s) for popup.
  name: SendPulse Popup API
  phrasing_intents:
  - id: getPopupConditions
    intent: List available pop-up display conditions
    question: What display conditions can I use to trigger a pop-up?
  - id: listQuizPopupsByProject
    intent: List quiz pop-ups in a project
    question: Which quiz pop-ups do I have on a project?
  - id: listPopupsByProjectId
    intent: List pop-ups in a project
    question: What pop-ups are set up for my website project?
  - id: setPopupState
    intent: Enable or disable a pop-up
    question: Can I turn a pop-up off on my website without deleting it?
  - id: deletePopup
    intent: Delete a pop-up
    question: Can I permanently delete a pop-up?
  phrasing_ops: 5
  slug: sendpulse-popup-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Popup statistic API from SendPulse — 3 operation(s) for popup statistic.
  name: SendPulse Popup statistic API
  phrasing_intents:
  - id: getPopupStatistics
    intent: Get views and interactions for a pop-up
    question: How many visitors saw and interacted with my pop-up?
  - id: getNpsStatisticsByPopupId
    intent: Get vote counts per NPS option
    question: How many votes did each NPS score button get?
  - id: getPopupAggregatedNpsStatistics
    intent: Get the aggregated NPS result for a pop-up
    question: What is the overall Net Promoter Score from my survey pop-up?
  phrasing_ops: 3
  slug: sendpulse-popup-statistic-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Project API from SendPulse — 2 operation(s) for project.
  name: SendPulse Project API
  phrasing_intents:
  - id: listWidgets
    intent: List projects
    question: What projects do I have set up?
  - id: createWidget
    intent: Create a project
    question: How do I create a new project for my website?
  phrasing_ops: 2
  slug: sendpulse-project-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Project statistic API from SendPulse — 1 operation(s) for project statistic.
  name: SendPulse Project statistic API
  phrasing_intents:
  - id: getProjectWidgetStatistics
    intent: Get pop-up statistics for a project
    question: How many site visitors saw the pop-ups in my project?
  phrasing_ops: 1
  slug: sendpulse-project-statistic-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Reports.
  name: SendPulse Reports API
  phrasing_intents:
  - id: createVerificationReport
    intent: Generate a list verification report
    question: How do I generate a downloadable report of my list verification results?
  - id: viewVerificationReport
    intent: Preview a list verification report
    question: Can I preview a verification report before downloading it?
  - id: downloadVerificationReport
    intent: Download a list verification report
    question: How do I download the full verification report file?
  phrasing_ops: 3
  slug: sendpulse-reports-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Schools API from SendPulse — 1 operation(s) for schools.
  name: SendPulse Schools API
  phrasing_intents:
  - id: getSchools
    intent: List online schools
    question: Which online schools do I have set up?
  phrasing_ops: 1
  slug: sendpulse-schools-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Senders.
  name: SendPulse Senders API
  phrasing_intents:
  - id: getSenders
    intent: List sender addresses
    question: Which From addresses are authorized on my account?
  - id: addSender
    intent: Add a sender address
    question: How do I register a new From address for my emails?
  - id: deleteSender
    intent: Delete a sender address
    question: Can I remove a sender address I don't use anymore?
  - id: requestSenderActivationCode
    intent: Send a sender activation code
    question: How do I get the activation code for a new sender address?
  - id: activateSender
    intent: Activate a sender with its code
    question: Where do I enter the code to verify a sender address?
  phrasing_ops: 5
  slug: sendpulse-senders-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Single Email Verification.
  name: SendPulse Single Email Verification API
  phrasing_intents:
  - id: verifySingleEmail
    intent: Submit one email address for verification
    question: Can I check whether a single email address is valid before I send to it?
  - id: getSingleVerificationResult
    intent: Get the verification result for one email
    question: What was the verification result for an email address I submitted?
  phrasing_ops: 2
  slug: sendpulse-single-email-verification-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Students API from SendPulse — 7 operation(s) for students.
  name: SendPulse Students API
  phrasing_intents:
  - id: createStudent
    intent: Enroll a new student in a course
    question: How do I add a student to one of my online courses?
  - id: getStudentsAuditory
    intent: Search all students across the school
    question: Which students across my whole school have paid?
  - id: getStudentCourseStatistics
    intent: Get a student's course progress statistics
    question: How far has a student progressed through their courses?
  - id: deleteStudent
    intent: Remove a student from the school
    question: Can I remove a student from my school entirely?
  - id: removeStudentFromCourse
    intent: Remove a student from one course
    question: Can I unenroll a student from a single course but keep them in the school?
  - id: getStudentsByCourse
    intent: List students enrolled in a course
    question: Who is enrolled in a particular course?
  - id: markStudentsAsPaid
    intent: Mark students as paid for a course
    question: Can I mark students as having paid for a course?
  phrasing_ops: 7
  slug: sendpulse-students-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Students groups API from SendPulse — 1 operation(s) for students groups.
  name: SendPulse Students groups API
  phrasing_intents:
  - id: listGroupsByCourse
    intent: List a course's student groups
    question: What student groups exist for a course?
  phrasing_ops: 1
  slug: sendpulse-students-groups-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Subscribers API from SendPulse — 6 operation(s) for subscribers.
  name: SendPulse Subscribers API
  phrasing_intents:
  - id: getSubscriberById
    intent: Get a pop-up subscriber's details
    question: What information do I have about one pop-up subscriber?
  - id: getSubscribersByPopup
    intent: List subscribers collected by a pop-up
    question: Who signed up through a particular pop-up?
  - id: listSubscribersByProject
    intent: List pop-up subscribers in a project
    question: Which subscribers did all the pop-ups in one project collect?
  - id: getWebPushSubscriptions
    intent: List web push subscribers of a website
    question: Who has subscribed to push notifications on my website?
  - id: getWebPushSubscribersTotal
    intent: Count web push subscribers of a website
    question: How many push notification subscribers does my website have?
  - id: setWebPushSubscriberState
    intent: Activate or deactivate a web push subscriber
    question: Can I pause push notifications for one subscriber?
  phrasing_ops: 6
  slug: sendpulse-subscribers-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Tags.
  name: SendPulse Tags API
  phrasing_intents:
  - id: getTags
    intent: List email and phone tags
    question: What tags have I created in my account?
  - id: createTag
    intent: Create a colored tag
    question: How do I create a new tag with a color?
  - id: updateTag
    intent: Rename or recolor a tag
    question: Can I change the name and color of an existing tag?
  - id: deleteTag
    intent: Delete a tag
    question: How do I delete a tag from my account?
  - id: pinTagToEmail
    intent: Assign tags to an email address
    question: Can I label a subscriber's email address with tags?
  - id: pinTagToPhone
    intent: Assign tags to a phone number
    question: Can I attach tags to an SMS subscriber's phone number?
  - id: unpinTagFromEmail
    intent: Remove tags from an email address
    question: How do I take a tag off an email address?
  - id: unpinTagFromPhone
    intent: Remove tags from a phone number
    question: Can I unassign tags from a phone number?
  phrasing_ops: 8
  slug: sendpulse-tags-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Tariff API from SendPulse — 1 operation(s) for tariff.
  name: SendPulse Tariff API
  phrasing_intents:
  - id: getTariffLimits
    intent: Get my pop-up tariff plan limits
    question: What are the limits of my current pop-up tariff plan?
  phrasing_ops: 1
  slug: sendpulse-tariff-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Task Attributes API from SendPulse — 2 operation(s) for task attributes.
  name: SendPulse Task Attributes API
  phrasing_intents:
  - id: createTaskAttributeValue
    intent: Set a custom field value on a task
    question: How do I fill in a custom field on a task?
  - id: updateTaskAttributeValue
    intent: Change a task's custom field value
    question: How do I change a custom field value already set on a task?
  - id: deleteAttributeValue
    intent: Delete a custom field value from a task
    question: How do I clear a custom field value from a task?
  phrasing_ops: 3
  slug: sendpulse-task-attributes-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Task Checklist API from SendPulse — 4 operation(s) for task checklist.
  name: SendPulse Task Checklist API
  phrasing_intents:
  - id: createTaskChecklist
    intent: Add an empty checklist to a task
    question: Can I add a blank checklist to a task?
  - id: updateTaskChecklistSingle
    intent: Rename a single task checklist
    question: Can I rename one checklist on a task without touching its items?
  - id: getTaskChecklists
    intent: List a task's checklists
    question: What checklists are on a task?
  - id: createTaskChecklists
    intent: Create several checklists with items on a task
    question: How do I add multiple checklists, items included, to a task?
  - id: updateTaskChecklists
    intent: Update several task checklists with items
    question: Can I update multiple checklists and their items on a task at once?
  - id: deleteTaskChecklist
    intent: Delete a checklist from a task
    question: Can I delete a checklist from a task?
  phrasing_ops: 6
  slug: sendpulse-task-checklist-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Task Comments API from SendPulse — 2 operation(s) for task comments.
  name: SendPulse Task Comments API
  phrasing_intents:
  - id: addTaskComment
    intent: Add a comment to a task
    question: How do I comment on a CRM task?
  - id: updateTaskComment
    intent: Edit a comment on a task
    question: Can I edit a comment I left on a task?
  phrasing_ops: 2
  slug: sendpulse-task-comments-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Task Entity API from SendPulse — 4 operation(s) for task entity.
  name: SendPulse Task Entity API
  phrasing_intents:
  - id: detachContactFromTask
    intent: Unlink a contact from a task
    question: How do I remove a contact that's linked to a task?
  - id: detachDealFromTask
    intent: Unlink a deal from a task
    question: How do I remove a deal that's linked to a task?
  - id: detachTaskFromTask
    intent: Unlink a subtask from its parent task
    question: How do I separate a subtask from its parent task?
  - id: attachEntitiesToTask
    intent: Link contacts, deals or tasks to a task
    question: How do I connect a task to the deals and contacts it's about?
  phrasing_ops: 4
  slug: sendpulse-task-entity-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Task history API from SendPulse — 1 operation(s) for task history.
  name: SendPulse Task history API
  phrasing_intents:
  - id: getTaskHistory
    intent: Get a task's change history for a period
    question: What changed on a task during the past week?
  phrasing_ops: 1
  slug: sendpulse-task-history-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Task Tags API from SendPulse — 3 operation(s) for task tags.
  name: SendPulse Task Tags API
  phrasing_intents:
  - id: detachTagFromTask
    intent: Remove a tag from a task
    question: How do I untag a single task without deleting the tag itself?
  - id: getTaskTags
    intent: List task tags
    question: What tags are available for labeling tasks?
  - id: createTaskTag
    intent: Create a task tag
    question: How do I make a new colored label for tasks?
  - id: updateTaskTag
    intent: Rename or recolor a task tag
    question: How do I change the color of an existing task tag?
  - id: deleteTaskTag
    intent: Delete a task tag
    question: How do I delete a task tag from the whole account?
  phrasing_ops: 5
  slug: sendpulse-task-tags-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Tasks API from SendPulse — 6 operation(s) for tasks.
  name: SendPulse Tasks API
  phrasing_intents:
  - id: listTasks
    intent: Search tasks with filters
    question: Which tasks are assigned to a given person on my board?
  - id: createTask
    intent: Create a task
    question: How do I create a task on a board with a due date?
  - id: getTaskRepeatTemplates
    intent: List task repeat templates
    question: What repeat templates are available for recurring tasks?
  - id: getTaskById
    intent: Get a task by ID
    question: Can I fetch the full details of one task?
  - id: updateTaskById
    intent: Update a task
    question: How do I change a task's due date or assignee?
  - id: deleteTask
    intent: Delete a task
    question: Can I delete a task I no longer need?
  - id: setTaskParent
    intent: Set or clear a task's parent task
    question: Can I make a task a subtask of another task?
  - id: changeTaskStepOrder
    intent: Reorder a task or move it to another step
    question: Can I change a task's position within its step?
  phrasing_ops: 8
  slug: sendpulse-tasks-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Tasks boards API from SendPulse — 2 operation(s) for tasks boards.
  name: SendPulse Tasks boards API
  phrasing_intents:
  - id: getBoards
    intent: List task boards
    question: What task boards do I have?
  - id: createBoard
    intent: Create a task board
    question: How do I create a new board for tasks?
  - id: getBoardById
    intent: Get a task board and its settings
    question: What settings does a particular task board have?
  - id: updateBoard
    intent: Update a task board
    question: Can I rename a task board or change its settings?
  phrasing_ops: 4
  slug: sendpulse-tasks-boards-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Tasks steps API from SendPulse — 2 operation(s) for tasks steps.
  name: SendPulse Tasks steps API
  phrasing_intents:
  - id: createBoardSteps
    intent: Add a step to a task board
    question: How do I add a new column or step to a task board?
  - id: updateBoardStep
    intent: Update or reorder a board step
    question: Can I rename a step on my task board?
  phrasing_ops: 2
  slug: sendpulse-tasks-steps-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Telephony API from SendPulse — 4 operation(s) for telephony.
  name: SendPulse Telephony API
  phrasing_intents:
  - id: getTelephonyCalls
    intent: Search all telephony calls
    question: Which calls came in across my whole account last week?
  - id: getContactCalls
    intent: List a contact's calls
    question: What calls have we had with a particular contact?
  - id: getDealCalls
    intent: List calls linked to a deal
    question: Which calls are attached to a deal?
  - id: attachCallToDeal
    intent: Attach a call to a deal
    question: How do I link a phone call to a deal?
  phrasing_ops: 4
  slug: sendpulse-telephony-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Templates.
  name: SendPulse Templates API
  phrasing_intents:
  - id: createTemplate
    intent: Create an email template from HTML
    question: How do I upload my own HTML as a reusable email template?
  - id: updateTemplate
    intent: Edit an existing email template's HTML
    question: Can I replace the HTML of a template I already created?
  - id: getTemplateById
    intent: Get an email template by ID
    question: What metadata is stored for one of my email templates?
  - id: getTemplateBySlug
    intent: Get an email template by its name slug
    question: Can I look up a template by its name slug instead of the ID?
  - id: getTemplates
    intent: List email templates
    question: Which email templates do I have available?
  phrasing_ops: 5
  slug: sendpulse-templates-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: (keywords)
  name: SendPulse Triggers API
  phrasing_intents:
  - id: getTriggers
    intent: List a chatbot's triggers
    question: What triggers are set up for my chatbot?
  phrasing_ops: 1
  slug: sendpulse-triggers-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Unsubscribe API from SendPulse — 3 operation(s) for unsubscribe.
  name: SendPulse Unsubscribe API
  phrasing_intents:
  - id: unsubscribeSmtpRecipients
    intent: Unsubscribe recipients from SMTP emails
    question: How do I stop sending transactional emails to a recipient?
  - id: removeSmtpUnsubscribe
    intent: Remove an email from the SMTP unsubscribe list
    question: Can I take an email back off the SMTP unsubscribed list?
  - id: getSmtpUnsubscribed
    intent: List SMTP unsubscribed recipients
    question: Who has unsubscribed from my transactional emails?
  - id: searchSmtpUnsubscribe
    intent: Check a contact's SMTP subscription status
    question: Is a given email address unsubscribed from SMTP sends?
  - id: resubscribeSmtpRecipient
    intent: Resubscribe a recipient to SMTP emails
    question: How do I resubscribe someone who opted out of transactional email?
  phrasing_ops: 5
  slug: sendpulse-unsubscribe-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Users API from SendPulse — 1 operation(s) for users.
  name: SendPulse Users API
  phrasing_intents:
  - id: getUsers
    intent: List team members
    question: Who are the team members on my account?
  phrasing_ops: 1
  slug: sendpulse-users-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The variables API from SendPulse — 1 operation(s) for variables.
  name: SendPulse Variables API
  phrasing_intents:
  - id: listBotVariables
    intent: List a chatbot's variables
    question: What variables are defined for my chatbot?
  phrasing_ops: 1
  slug: sendpulse-variables-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: Endpoints related to Webhooks.
  name: SendPulse Webhooks API
  phrasing_intents:
  - id: getWebhooks
    intent: List email service webhooks
    question: Which webhooks are set up to receive my email events?
  - id: createWebhook
    intent: Create a webhook for email events
    question: How do I get notified at my URL when emails are opened or bounce?
  - id: getWebhookById
    intent: Get a webhook's details
    question: What URL and events does a particular email webhook use?
  - id: updateWebhook
    intent: Change a webhook's URL
    question: How do I point an existing email webhook at a new endpoint?
  - id: deleteWebhook
    intent: Delete a webhook
    question: How do I stop sending email events to a webhook?
  phrasing_ops: 5
  slug: sendpulse-webhooks-api
- baseURL: https://api.sendpulse.com
  baseurl_source: declared
  description: The Websites API from SendPulse — 4 operation(s) for websites.
  name: SendPulse Websites API
  phrasing_intents:
  - id: getWebPushWebsitesTotal
    intent: Count my web push websites
    question: How many websites do I have set up for web push notifications?
  - id: getWebPushWebsites
    intent: List my web push websites
    question: Which websites are connected to my web push account?
  - id: getWebPushVariables
    intent: List the variables defined for a push website
    question: What subscriber variables are defined on one of my web push sites?
  - id: getWebPushWebsiteInfo
    intent: Get details of a web push website
    question: What details are stored for a specific web push website?
  phrasing_ops: 4
  slug: sendpulse-websites-api
artifact_total: 108
asyncapis:
- description: ''
  name: Sendpulse Webhooks
  slug: sendpulse-webhooks
collections:
- collection_type: open
  name: SendPulse Account API
  slug: open-sendpulse-account-api
- collection_type: open
  name: SendPulse Account Address Books API
  slug: open-sendpulse-address-books-api
- collection_type: open
  name: SendPulse Account Authorization API
  slug: open-sendpulse-authorization-api
- collection_type: open
  name: SendPulse Account Automation 360 API
  slug: open-sendpulse-automation-360-api
- collection_type: open
  name: SendPulse Account Email Blacklist API
  slug: open-sendpulse-email-blacklist-api
- collection_type: open
  name: SendPulse Account Email Campaigns API
  slug: open-sendpulse-email-campaigns-api
- collection_type: open
  name: SendPulse Account Senders API
  slug: open-sendpulse-senders-api
- collection_type: open
  name: SendPulse Account SMS API
  slug: open-sendpulse-sms-api
- collection_type: open
  name: SendPulse Account SMTP API
  slug: open-sendpulse-smtp-api
- collection_type: open
  name: SendPulse Account Web Push API
  slug: open-sendpulse-web-push-api
- collection_type: open
  name: SendPulse API
  slug: open-sendpulse
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/capabilities/sendpulse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sendpulse-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-bulk-email-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-bulk-email-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-smtp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-smtp-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-sms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-sms-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-crm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-crm-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-a360-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-a360-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-chatbots-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-chatbots-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-whatsapp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-whatsapp-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-telegram-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-telegram-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-facebook-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-facebook-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-instagram-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-instagram-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-viber-chatbot-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-viber-chatbot-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-tiktok-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-tiktok-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-live-chat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-live-chat-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-web-push-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-web-push-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-viber-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-viber-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-verifier-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-verifier-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-edu-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-edu-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-popups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-popups-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/overlays/sendpulse-file-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendpulse-file-manager-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://sendpulse.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendpulse.com/integrations/api
- group: docs
  title: ''
  type: Documentation
  url: https://sendpulse.com/integrations/api
- group: docs
  title: ''
  type: APIReference
  url: https://sendpulse.com/integrations/api/bulk-email
- group: start
  title: ''
  type: GettingStarted
  url: https://sendpulse.com/integrations/api
- group: operate
  title: ''
  type: Support
  url: https://sendpulse.com/knowledge-base
- group: operate
  title: ''
  type: HelpCenter
  url: https://sendpulse.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://sendpulse.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendpulse
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendpulse
- group: commercial
  title: ''
  type: Pricing
  url: https://sendpulse.com/prices
- group: start
  title: ''
  type: SignUp
  url: https://sendpulse.com/register
- group: start
  title: ''
  type: Login
  url: https://login.sendpulse.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendpulse.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendpulse.com/legal/pp
- group: operate
  title: ''
  type: Roadmap
  url: https://sendpulse.com/updates/upcoming
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendpulse.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendpulse.com/updates
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/agentic-access/sendpulse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendpulse-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/authentication/sendpulse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendpulse-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/scopes/sendpulse-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sendpulse-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/conventions/sendpulse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendpulse-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/errors/sendpulse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendpulse-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/rate-limits/sendpulse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sendpulse-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/plans/sendpulse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendpulse-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/finops/sendpulse-finops.yml
  title: ''
  type: FinOps
  url: finops/sendpulse-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/lifecycle/sendpulse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sendpulse-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/changelog/sendpulse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sendpulse-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/data-model/sendpulse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendpulse-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/asyncapi/sendpulse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sendpulse-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/packages/sendpulse-packages.yml
  title: ''
  type: Packages
  url: packages/sendpulse-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/packages/sendpulse-packages.yml
  title: ''
  type: SDKs
  url: packages/sendpulse-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/mcp/sendpulse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sendpulse-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/mcp/sendpulse-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sendpulse-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/llms/sendpulse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendpulse-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/well-known/sendpulse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sendpulse-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/well-known/sendpulse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sendpulse-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/conformance/sendpulse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendpulse-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/security/sendpulse-trust-center.yml
  title: ''
  type: Compliance
  url: security/sendpulse-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/security/sendpulse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sendpulse-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/security/sendpulse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sendpulse-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/security/sendpulse-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sendpulse-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/security/sendpulse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendpulse-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.sendpulse.com/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://sendpulse.com/knowledge-base/account-settings/mcp-server
created: '2026-06-25'
description: SendPulse is a multichannel marketing automation platform covering bulk email, SMTP transactional email, SMS, web push, website pop-ups, a CRM, an online course builder, and chatbots across WhatsApp, Telegram, Facebook Messenger, Instagram, Viber, TikTok and its own live chat widget. It publishes nineteen first-party OpenAPI 3.1 specifications totalling 635 operations from https://api.sendpulse.com/.well-known/openapi/, indexed by a master index.yaml and mirrored by an llms.txt, an llms-full.txt, a service-directory.json and an ai-plugin.json. Authentication is OAuth 2.0 client_credentials against POST /oauth/access_token (one-hour Bearer tokens) or a static account API key in the same Authorization header. SendPulse also operates a first-party remote MCP server at https://mcp.sendpulse.com/mcp with 147 published tools covering chatbots, CRM, courses, email and SMTP.
finops:
- name: Sendpulse Finops
  service_category: Marketing and Communications
  slug: sendpulse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendpulse.png
layout: provider
mcp_servers:
- description: First-party remote MCP server operated by SendPulse over Streamable HTTP. It fronts the SendPulse REST API so an AI client can read statistics, manage contacts and deals, run campaigns and send messag
  name: SendPulse MCP Server
  slug: sendpulse-mcp-server
- description: ''
  name: SendPulse MCP Server
  slug: mcp
modified: '2026-08-13'
name: SendPulse
nav: Providers
network: true
overview: 'SendPulse publishes 85 APIs on the [APIs.io](https://apis.io/) network, including Account API, Attachments API, Automation Flows API, and 82 more. Tagged areas include Marketing, Marketing Automation, Email, Transactional Email, and SMS.


  The SendPulse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SendPulse''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 59 more developer resources.'
plans:
- name: Sendpulse Plans Pricing
  plan_count: 8
  slug: sendpulse-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 9
  name: Sendpulse Rate Limits
  slug: sendpulse-rate-limits
scopes:
- name: Sendpulse Scopes
  scope_count: 1
  slug: sendpulse-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 70.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 96.8
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 81.6
  previous_composite: 69.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 85
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/sendpulse/refs/heads/main/screenshots/sendpulse-2026-08-17T080418.png
security:
- kind: authentication
  name: Sendpulse Authentication
  slug: sendpulse-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sendpulse Domain Security
  slug: sendpulse-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sendpulse Vulnerability Disclosure
  slug: sendpulse-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Sendpulse Trust Center
  slug: sendpulse-trust-center
  summary_line: CASA Tier 2
slug: sendpulse
tags:
- Marketing
- Marketing Automation
- Email
- Transactional Email
- SMS
- Web Push
- Chatbots
- CRM
- Multi-Channel
- Messaging
- Online Courses
- Popups
- Email Verification
- MCP
- Agent Ready
website: https://sendpulse.com/
---
