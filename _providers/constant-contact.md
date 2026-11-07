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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 60
  human_in_the_loop: 2
  name: Constant Contact Agentic Access
  operation_count: 120
  slug: constant-contact-agentic-access
  summary_line: 120 operations · 60 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use the account endpoints and methods to get account information.
  name: Constant Contact Account Services API
  phrasing_intents:
  - id: getUserPrivileges
    intent: Check what my access token is allowed to do
    question: Which user privileges does my current access token carry?
  - id: getAccountById
    intent: Get my account summary details
    question: What account details can I pull for my Constant Contact login, like organization name and time zone?
  - id: putCustomerById
    intent: Update my account contact details
    question: Can I change the contact email or phone number on my account?
  - id: getPhysicalAddress
    intent: Get the organization's physical address
    question: What physical address is shown in the footer of my emails?
  - id: addPhysicalAddress
    intent: Add a physical address to a new account
    question: My account has no physical address yet — how do I add the first one so I can send email?
  - id: putPhysicalAddress
    intent: Change the organization's existing physical address
    question: Can I correct the physical address I already set for my account?
  - id: retrieveEmailAddresses
    intent: List the account's sender email addresses
    question: Which email addresses on my account are confirmed and usable as a from address?
  - id: addAccountEmailAddress
    intent: Add a new sender email address
    question: How do I add another email address I can send campaigns from?
  phrasing_ops: 8
  slug: constant-contact-account-services-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Bulk activities endpoints are used to manage large numbers of contacts, lists, and tags.
  name: Constant Contact Bulk Activities API
  phrasing_intents:
  - id: getActivityStatusCollection
    intent: List bulk activities and their status
    question: Which of my bulk jobs failed or timed out?
  - id: getActivity
    intent: Check the status of one bulk activity
    question: Has my contact import finished yet?
  - id: postContactsExport
    intent: Export contacts to a CSV file
    question: Can I export all my contacts to a CSV?
  - id: getContactsExport
    intent: Download a finished contacts export file
    question: Where do I download the CSV once my contact export is done?
  - id: postContactDelete
    intent: Bulk delete contacts
    question: Can I delete hundreds of contacts at once?
  - id: contactsCSVImport
    intent: Import contacts from a CSV file
    question: Can I upload a CSV of contacts and add them to a list?
  - id: bulkImportContactsJSON
    intent: Import contacts from a JSON payload
    question: Can I bulk add or update contacts by sending JSON instead of a file?
  - id: postListRemoveContact
    intent: Remove contacts from lists in bulk
    question: Can I take a group of contacts off several lists without deleting them?
  phrasing_ops: 14
  slug: constant-contact-bulk-activities-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Endpoints and methods to get, create, delete, and update one or more contact lists.
  name: Constant Contact Lists API
  phrasing_intents:
  - id: getList
    intent: Get one contact list
    question: What are the details of a specific contact list?
  - id: putList
    intent: Rename or edit a contact list
    question: Can I rename a contact list or change its description?
  - id: deleteListActivity
    intent: Delete a single contact list
    question: What happens to members when I delete one list?
  - id: getLists
    intent: List all contact lists
    question: Which contact lists do I have in my account?
  - id: createList
    intent: Create a contact list
    question: How do I make a new contact list?
  - id: getListIdXrefs
    intent: Map old V2 list IDs to V3 list IDs
    question: I have list IDs stored from the V2 API — what are their V3 equivalents?
  phrasing_ops: 6
  slug: constant-contact-contact-lists-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Endpoints and methods to get, create, delete, and update one or more contact tags.
  name: Constant Contact Tags API
  phrasing_intents:
  - id: getTag
    intent: Get one tag's details
    question: What are the details of a specific tag?
  - id: putTag
    intent: Rename a tag
    question: Can I rename a tag I already created?
  - id: deleteTag
    intent: Delete a single tag
    question: Does deleting one tag remove it from all my contacts?
  - id: getTags
    intent: List all tags
    question: Which tags exist in my account?
  - id: postTag
    intent: Create a tag
    question: How do I create a new contact tag?
  phrasing_ops: 5
  slug: constant-contact-contact-tags-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Endpoints and methods to get, create, delete, and update one or more contacts.
  name: Constant Contact Contacts API
  phrasing_intents:
  - id: getContact
    intent: Get one contact
    question: What information do I have about a specific contact?
  - id: putContact
    intent: Update an existing contact
    question: Can I change a contact's name or email by their contact ID?
  - id: deleteContact
    intent: Delete a single contact
    question: What happens to a contact after I delete them — can they come back?
  - id: getContacts
    intent: Search and list contacts
    question: Which contacts have unsubscribed since last month?
  - id: createContact
    intent: Create a new contact
    question: How do I add a single new contact?
  - id: createOrUpdateContact
    intent: Create or update a contact from a sign-up
    question: Can I add someone if they're new, or update them if they already exist, in one call?
  - id: getContactIdXrefs
    intent: Map old V2 contact IDs to V3 contact IDs
    question: I stored contact IDs from the V2 API — how do I get the new V3 IDs?
  - id: getSmsEngagementHistory
    intent: Get a contact's SMS consent history
    question: When did a contact give or withdraw SMS consent?
  phrasing_ops: 10
  slug: constant-contact-contacts-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Endpoints and methods to get, create, delete, and update on one or more custom fields.
  name: Constant Contact Contacts Custom Fields API
  phrasing_intents:
  - id: getCustomField
    intent: Get one custom field
    question: What type and label does a specific custom field have?
  - id: putCustomField
    intent: Update a custom field
    question: Can I rename a custom field's label?
  - id: deleteCustomField
    intent: Delete a single custom field
    question: Can I remove one custom field I no longer use?
  - id: getCustomFields
    intent: List all custom fields
    question: Which custom fields are defined in my account?
  - id: postCustomFields
    intent: Create a custom field
    question: How do I add a custom field to store membership level?
  phrasing_ops: 5
  slug: constant-contact-contacts-custom-fields-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Contact reporting endpoints are used to gather activity reports for campaigns sent to a contact.
  name: Constant Contact Contacts Reporting API
  phrasing_intents:
  - id: getContactTracking
    intent: Get a contact's tracking activity
    question: What has a contact opened, clicked or bounced recently?
  - id: getContactOpenClickRate
    intent: Get a contact's average open and click rates
    question: What is a contact's average open and click rate?
  - id: getContactTrackingCount
    intent: Summarize a contact's actions per email
    question: Which recent emails did a contact receive and what did they do with each?
  phrasing_ops: 3
  slug: constant-contact-contacts-reporting-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use email campaigns A/B Test endpoints and methods to get, create, delete and update A/B tests.
  name: Constant Contact Email Campaigns AB Tests API
  phrasing_intents:
  - id: retrieveEmailCampaignABTestUsingGET
    intent: Get an email's A/B test settings
    question: What alternate subject line and test size is my A/B test using?
  - id: createEmailCampaignABTestUsingPOST
    intent: Create a subject line A/B test
    question: Can I A/B test two subject lines on an email?
  - id: deleteEmailCampaignABTestUsingDELETE
    intent: Delete a draft A/B test
    question: Can I remove an A/B test and go back to a regular email?
  phrasing_ops: 3
  slug: constant-contact-email-campaigns-ab-tests-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use email campaign endpoints and methods to get, create, and update email campaigns.
  name: Constant Contact Email Campaigns API
  phrasing_intents:
  - id: retrieveEmailCampaignsUsingGET
    intent: List email campaigns
    question: Which email campaigns have I created?
  - id: createEmailCampaignUsingPOST
    intent: Create a new email campaign
    question: How do I create an email campaign with custom HTML?
  - id: retrieveEmailCampaignUsingGET
    intent: Get one email campaign
    question: What's the status of a specific email campaign?
  - id: removeEmailCampaignUsingDELETE
    intent: Delete an email campaign
    question: Can I delete a campaign that's already scheduled?
  - id: renameEmailCampaignUsingPATCH
    intent: Rename an email campaign
    question: Can I rename an email campaign without touching its content?
  - id: retrieveXrefMappingsUsingGET
    intent: Map old V2 campaign IDs to V3 IDs
    question: I stored email campaign IDs from the V2 API — what are the V3 identifiers?
  - id: retrieveEmailCampaignActivityUsingGET
    intent: Get an email campaign activity's content
    question: Where can I see the HTML content and subject of an email campaign activity?
  - id: updateEmailCampaignActivityUsingPUT
    intent: Edit an email's content and sender details
    question: Can I change the subject line or from name of an email I haven't sent?
  phrasing_ops: 11
  slug: constant-contact-email-campaigns-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use the email reporting endpoints and methods to get reporting data for email campaigns you sent to contacts.
  name: Constant Contact Email Reporting API
  phrasing_intents:
  - id: getCampaignActivityLinkStats
    intent: Report clicks per link in an email
    question: Which links in my email got the most unique clicks?
  - id: getSends
    intent: Report who an email was sent to
    question: Which contacts was a particular email actually sent to?
  - id: getOpens
    intent: Report every open of an email
    question: Every time someone opened my email — when and on what device?
  - id: getUniqueOpens
    intent: Report unique openers of an email
    question: Who opened my email, counting each contact only once?
  - id: getDidNotOpens
    intent: Report contacts who did not open an email
    question: Which contacts received my email but never opened it?
  - id: getClicks
    intent: Report clicks on an email
    question: Who clicked links in my email and when?
  - id: getForwards
    intent: Report forwards of an email
    question: Who forwarded my email using the footer forward link?
  - id: getOptouts
    intent: Report unsubscribes from an email
    question: Which contacts unsubscribed after this email?
  phrasing_ops: 12
  slug: constant-contact-email-reporting-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use email scheduling endpoints and methods to schedule an email campaign activity, unschedule an email campaign activity, and GET schedule information.
  name: Constant Contact Email Scheduling API
  phrasing_intents:
  - id: retrieveEmailSchedulesUsingGET
    intent: Check when an email is scheduled to send
    question: When is my email scheduled to go out?
  - id: scheduleEmailCampaignActivityUsingPOST
    intent: Send or schedule an email
    question: Can I send an email right now or schedule it for later?
  - id: unscheduleEmailCampaignActivityUsingDELETE
    intent: Unschedule an email
    question: Can I stop a scheduled email from sending?
  - id: testSendCampaignActivityUsingPOST
    intent: Send a test email
    question: Can I send myself a test before the real send?
  - id: retrieveEmailCampaignActivityPreviewUsingGET
    intent: Preview an email's HTML
    question: What will my email look like before I send it?
  - id: retrieveEmailSendHistoryUsingGET
    intent: Get an email's send history
    question: How many times has this email been sent, and to which lists?
  phrasing_ops: 6
  slug: constant-contact-email-scheduling-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Endpoints and methods used to create and manage events.
  name: Constant Contact Events API
  phrasing_intents:
  - id: findEvents
    intent: List events
    question: Which events do I have, and what's their status?
  - id: addDefaultEvent
    intent: Create a draft event with defaults
    question: Can I create an event that already has a registration form and landing page?
  - id: getEvent_2
    intent: Get one event's details
    question: What are the details of a specific event?
  - id: patchEvent
    intent: Update an event
    question: Can I change an event's title or time after it's live?
  - id: copyEvent
    intent: Duplicate an existing event
    question: Can I copy last year's event with its forms and landing page?
  - id: checkInTickets
    intent: Check in event tickets
    question: Can I mark attendees' tickets as checked in at the door?
  - id: undoCheckInTickets
    intent: Undo ticket check-in
    question: I checked in the wrong ticket — can I reverse it?
  - id: getRegistrationInfo
    intent: Get one event registration
    question: What did a specific attendee submit when registering?
  phrasing_ops: 11
  slug: constant-contact-events-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use landing pages reporting endpoints and methods to get reporting data about how a contact interacted with a campaign activity.
  name: Constant Contact Landing Pages Reporting API
  phrasing_intents:
  - id: getUniqueContactClicks
    intent: Report contacts who clicked landing page links
    question: Which contacts clicked links on my landing page?
  - id: getUniqueContactOpens
    intent: Report unique contacts who opened a landing page
    question: Which contacts viewed my landing page, counting each once?
  - id: getContactOpens
    intent: Report every landing page open by contacts
    question: Each time a contact opened my landing page, when did it happen?
  - id: getUniqueContactUpdates
    intent: Report contacts who updated details on a landing page
    question: Which contacts updated their information through my landing page?
  - id: getContactAdds
    intent: Report contacts added from a landing page
    question: How many new contacts did my landing page bring in?
  - id: getUniqueContactSMSOptIns
    intent: Report SMS opt-ins from a landing page
    question: Which contacts opted in to text messages from my landing page?
  phrasing_ops: 6
  slug: constant-contact-landing-pages-reporting-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use segments to target a subset of your contacts that are most likely to engage with a particular campaign.
  name: Constant Contact Segments API
  phrasing_intents:
  - id: getAccountSegments
    intent: List all segments
    question: Which segments have I built?
  - id: createSegment
    intent: Create a segment
    question: Can I create a segment of contacts who clicked in the last 30 days?
  - id: getSegmentDetail
    intent: Get one segment's criteria
    question: What criteria define a particular segment?
  - id: updateSegment
    intent: Update a segment's name and criteria
    question: Can I change the rules that define a segment?
  - id: deleteSegment
    intent: Delete a segment
    question: Is it safe to delete a segment that a scheduled campaign uses?
  - id: updateSegmentName
    intent: Rename a segment
    question: Can I just rename a segment without touching its criteria?
  phrasing_ops: 6
  slug: constant-contact-segments-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use SMS reporting endpoints and methods to get reporting data about SMS campaigns.
  name: Constant Contact SMS Reporting API
  phrasing_intents:
  - id: getAllBulkSmsCampaignSummaries
    intent: Summarize SMS campaign performance
    question: How did my SMS campaigns perform since a given date?
  phrasing_ops: 1
  slug: constant-contact-sms-reporting-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use partner endpoints to manage client Constant Contact accounts under your partner account.
  name: Constant Contact Technology Partners API
  phrasing_intents:
  - id: getPartnerSiteOwners
    intent: List partner client accounts
    question: Which client accounts are managed under my partner account?
  - id: provision
    intent: Create a partner client account
    question: Can I create a new client account for a customer as a partner?
  - id: getPlan
    intent: Get a client account's billing plan
    question: What billing plan is a client account on?
  - id: setPlan
    intent: Change a client account's billing plan
    question: Can I upgrade a client account to a different plan?
  - id: cancelAccount
    intent: Cancel a client account
    question: Can I cancel a client's account on a future date?
  - id: partnerAccountOperationsPostSync
    intent: Call the API on behalf of a client account
    question: As a partner, can I make API calls as one of my client accounts?
  - id: createSSOUser
    intent: Add a user to an SSO client account
    question: Can I add a new user to a client account that uses single sign-on?
  - id: partnerUnsubscribeContacts
    intent: Unsubscribe contacts across client accounts
    question: Can I unsubscribe an email address from every client account I manage?
  phrasing_ops: 8
  slug: constant-contact-technology-partners-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use partner webhooks to subscribe to billing event notifications from Constant Contact.
  name: Constant Contact Technology Partners Webhooks API
  phrasing_intents:
  - id: getWebhooksCollection
    intent: List my webhook subscriptions
    question: Which webhook topics is my partner app subscribed to?
  - id: getWebhooksTopic
    intent: Get one webhook topic subscription
    question: What callback URL is set for the account-cancelled webhook?
  - id: putWebhooksTopic
    intent: Subscribe to a webhook topic or change its callback
    question: Can I get notified when a client upgrades or downgrades billing tier?
  - id: deleteWebhooksSubscriptions
    intent: Unsubscribe from a webhook topic
    question: Can I stop receiving a webhook topic?
  - id: testSendWebhooksTopic
    intent: Send a test webhook notification
    question: Can I trigger a test webhook to check my endpoint works?
  phrasing_ops: 5
  slug: constant-contact-technology-partners-webhooks-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: Use the automation endpoints and methods to manage automation campaigns
  name: Constant Contact Automations API
  phrasing_intents:
  - id: listAutomations
    intent: List automation workflows
    question: Which automation workflows do I have set up?
  - id: createAutomationCampaignUsingPost
    intent: Create an automation workflow
    question: Can I build an automation that triggers when a contact joins a list?
  - id: retrieveAutomationCampaignUsingGet
    intent: Get one automation workflow
    question: What triggers and steps are in a specific automation?
  - id: updateAutomationCampaignUsingPut
    intent: Update an automation workflow
    question: Can I edit an existing automation after it's been created?
  phrasing_ops: 4
  slug: constant-contact-automations-api
- baseURL: https://api.cc.email/v3
  baseurl_source: declared
  description: The Social API from Constant Contact — 4 operation(s) for social.
  name: Constant Contact Social API
  phrasing_intents:
  - id: getSocialProfilesUsingGET
    intent: List connected social media profiles
    question: Which Facebook, LinkedIn or Instagram pages can I post to?
  - id: getSocialConnectionsUsingGET
    intent: List social network connections
    question: Which social network accounts are authorized with my account?
  - id: getSocialHashtagGroupsUsingGET
    intent: List saved hashtag groups
    question: What hashtag groups have I saved for social posts?
  - id: createSocialPostUsingPOST
    intent: Create or schedule a social media post
    question: Can I schedule a social post to several profiles at once?
  phrasing_ops: 4
  slug: constant-contact-social-api
artifact_total: 72
asyncapis:
- description: ''
  name: Constant Contact Webhooks
  slug: constant-contact-webhooks
collections:
- collection_type: open
  name: AppConnect V3 Account Services API
  slug: open-constant-contact-account-services-api
- collection_type: open
  name: AppConnect V3 Account Services Bulk Activities API
  slug: open-constant-contact-bulk-activities-api
- collection_type: open
  name: AppConnect V3 Account Services Contact Lists API
  slug: open-constant-contact-contact-lists-api
- collection_type: open
  name: AppConnect V3 Account Services Contact Tags API
  slug: open-constant-contact-contact-tags-api
- collection_type: open
  name: AppConnect V3 Account Services Contacts API
  slug: open-constant-contact-contacts-api
- collection_type: open
  name: AppConnect V3 Account Services Contacts Custom Fields API
  slug: open-constant-contact-contacts-custom-fields-api
- collection_type: open
  name: AppConnect V3 Account Services Contacts Reporting API
  slug: open-constant-contact-contacts-reporting-api
- collection_type: open
  name: AppConnect V3 Account Services Email Campaigns AB Tests API
  slug: open-constant-contact-email-campaigns-ab-tests-api
- collection_type: open
  name: AppConnect V3 Account Services Email Campaigns API
  slug: open-constant-contact-email-campaigns-api
- collection_type: open
  name: AppConnect V3 Account Services Email Reporting API
  slug: open-constant-contact-email-reporting-api
- collection_type: open
  name: AppConnect V3 Account Services Email Scheduling API
  slug: open-constant-contact-email-scheduling-api
- collection_type: open
  name: AppConnect V3 Account Services Events API
  slug: open-constant-contact-events-api
- collection_type: open
  name: AppConnect V3 Account Services Landing Pages Reporting API
  slug: open-constant-contact-landing-pages-reporting-api
- collection_type: open
  name: AppConnect V3 Account Services Segments API
  slug: open-constant-contact-segments-api
- collection_type: open
  name: AppConnect V3 Account Services SMS Reporting API
  slug: open-constant-contact-sms-reporting-api
- collection_type: open
  name: AppConnect V3 Account Services Technology Partners API
  slug: open-constant-contact-technology-partners-api
- collection_type: open
  name: AppConnect V3 Account Services Technology Partners Webhooks API
  slug: open-constant-contact-technology-partners-webhooks-api
- collection_type: open
  name: AppConnect V3
  slug: open-constant-contact-v3
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/constant-contact/overview
- group: commercial
  href: https://artifacts.apis.io/constant-contact/finops/constant-contact-finops.yml
  title: ''
  type: FinOps
  url: finops/constant-contact-finops.yml
- group: other
  href: https://artifacts.apis.io/constant-contact/capabilities/constant-contact-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/constant-contact-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/constant-contact/scopes/constant-contact-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/constant-contact-scopes.yml
- group: agent
  href: https://artifacts.apis.io/constant-contact/agentic-access/constant-contact-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/constant-contact-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/constant-contact/security/constant-contact-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/constant-contact-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/constant-contact/authentication/constant-contact-authentication.yml
  title: ''
  type: Authentication
  url: authentication/constant-contact-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/constant-contact
- group: company
  title: ''
  type: Website
  url: https://www.constantcontact.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.constantcontact.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.constantcontact.com/api_guide/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.constantcontact.com/api_guide/auth_overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.constantcontact.com/api_reference/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.cc.email/v3/swagger.yaml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.constantcontact.com/
- group: operate
  title: ''
  type: Support
  url: https://www.constantcontact.com/help
- group: operate
  title: ''
  type: Community
  url: https://community.constantcontact.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.constantcontact.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/constantcontact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.constantcontact.com/legal/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.constantcontact.com/legal/terms-of-use
- group: design
  href: https://artifacts.apis.io/constant-contact/json-ld/constant-contact-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/constant-contact-context.jsonld
- group: docs
  href: https://artifacts.apis.io/constant-contact/json-schema/constant-contact-contact-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/constant-contact-contact-schema.json
- group: docs
  href: https://artifacts.apis.io/constant-contact/json-schema/constant-contact-campaign-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/constant-contact-campaign-schema.json
- group: design
  href: https://artifacts.apis.io/constant-contact/rules/constant-contact-rules.yml
  title: ''
  type: Spectral
  url: rules/constant-contact-rules.yml
- group: build
  href: https://artifacts.apis.io/constant-contact/packages/constant-contact-packages.yml
  title: ''
  type: Packages
  url: packages/constant-contact-packages.yml
- group: build
  href: https://artifacts.apis.io/constant-contact/packages/constant-contact-packages.yml
  title: ''
  type: SDKs
  url: packages/constant-contact-packages.yml
- group: agent
  href: https://artifacts.apis.io/constant-contact/llms/constant-contact-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/constant-contact-llms.txt
- group: design
  href: https://artifacts.apis.io/constant-contact/conventions/constant-contact-conventions.yml
  title: ''
  type: Conventions
  url: conventions/constant-contact-conventions.yml
- group: design
  href: https://artifacts.apis.io/constant-contact/errors/constant-contact-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/constant-contact-problem-types.yml
- group: design
  href: https://artifacts.apis.io/constant-contact/conformance/constant-contact-conformance.yml
  title: ''
  type: Conformance
  url: conformance/constant-contact-conformance.yml
- group: design
  href: https://artifacts.apis.io/constant-contact/lifecycle/constant-contact-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/constant-contact-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/constant-contact/changelog/constant-contact-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/constant-contact-changelog.yml
- group: design
  href: https://artifacts.apis.io/constant-contact/data-model/constant-contact-data-model.yml
  title: ''
  type: DataModel
  url: data-model/constant-contact-data-model.yml
- group: design
  href: https://artifacts.apis.io/constant-contact/asyncapi/constant-contact-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/constant-contact-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/constant-contact/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/constant-contact/rate-limits/constant-contact-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/constant-contact-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/constant-contact/plans/constant-contact-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/constant-contact-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.constantcontact.com/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledgebase.constantcontact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.constantcontact.com/api_guide/index.html
created: '2025-03-01'
description: Constant Contact is a small-business email and digital marketing platform offering email campaigns, automation, SMS, contact management, surveys, and events. The Constant Contact V3 API is a REST + JSON, OAuth2-protected service published at api.cc.email/v3 covering accounts, contacts, lists, tags, custom fields, segments, email campaigns, A/B tests, schedules and tests, bulk activities (CSV/JSON import, export, list and tag mutations), events with registration and check-in, reporting, and partner provisioning.
features:
- 'Lite: $12/mo for 500 contacts (jumps to $50/mo at 1K)'
- 'Standard: mid-tier with A/B testing, segmentation'
- 'Premium: $80/mo at 500 contacts with 24x email ratio'
- 'Email overages: $0.002 per additional email'
- REST API v3 at api.cc.email/v3
- 'API limit: 4 req/sec, 10K req/day per app'
- OAuth 2.0
- Webhooks for contact and campaign events
- Contacts, lists, segments, custom fields
- Email Templates and Drag-and-Drop editor
- Marketing Automation (Standard+)
- Surveys, landing pages, social media posts
- Reporting on opens, clicks, bounces, conversions
- E-commerce integrations (Shopify, WooCommerce, etc.)
- Event marketing and registration
- List building tools and lead capture
finops:
- has_sources: true
  method: derived
  name: Constant Contact Finops
  primary_unit: subscription
  service_category: ''
  slug: constant-contact-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/constant-contact.png
json_schemas:
- name: Constant Contact Email Campaign
  property_count: 8
  slug: constant-contact-campaign
- name: Constant Contact Contact
  property_count: 17
  slug: constant-contact-contact
json_structures:
- name: Constant Contact Structure
  property_count: 0
  slug: constant-contact-structure
jsonld:
- class_count: 0
  name: Constant Contact Context
  property_count: 8
  slug: constant-contact-context
layout: provider
modified: '2026-09-16'
name: Constant Contact
nav: Providers
network: true
overview: 'Constant Contact publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Services API, Bulk Activities API, Lists API, and 16 more. Tagged areas include Campaigns, Contacts, Email Marketing, Event, and Reporting.


  The Constant Contact catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Constant Contact''s developer surface includes authentication, developer portal, getting-started guide, API reference, support, engineering blog, changelog, and 34 more developer resources.'
plans:
- name: Constant Contact Plans Pricing
  plan_count: 3
  slug: constant-contact-plans-pricing
- name: Constant Contact Price Estimates
  plan_count: 0
  slug: constant-contact-price-estimates
random_paper: 11
rate_limits:
- limit_count: 3
  name: Constant Contact Rate Limits
  slug: constant-contact-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Constant Contact — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: constant-contact-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Constant Contact API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: constant-contact-rules
scopes:
- name: Constant Contact Scopes
  scope_count: 6
  slug: constant-contact-scopes
  summary_line: 6 scopes · implicit/authorizationCode
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 73.5
    catalog_earned_first_party: 24.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 66.2
    developer_ergonomics: 67.3
    discoverability: 73.2
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/constant-contact/constant-contact-2026-06-20T175012.png
security:
- kind: authentication
  name: Constant Contact Authentication
  slug: constant-contact-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Constant Contact Domain Security
  slug: constant-contact-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: constant-contact-bulk-import-contacts
  slug: constant-contact-bulk-import-contacts
- name: constant-contact-report-campaign-performance
  slug: constant-contact-report-campaign-performance
- name: constant-contact-send-email-campaign
  slug: constant-contact-send-email-campaign
- name: constant-contact-subscribe-contact
  slug: constant-contact-subscribe-contact
slug: constant-contact
tags:
- Campaigns
- Contacts
- Email Marketing
- Event
- Reporting
- SMS
- Surveys
- Email
website: https://www.constantcontact.com/
---
