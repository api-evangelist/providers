---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 203
  human_in_the_loop: 5
  name: Sendgrid Agentic Access
  operation_count: 389
  slug: sendgrid-agentic-access
  summary_line: 389 operations · 203 acting · 5 human-in-the-loop
api_count: 44
apis:
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Account Provisioning API account operations.
  name: SendGrid Account API
  phrasing_intents:
  - id: ListAccount
    intent: List accounts under my partner organization
    question: Which customer accounts exist under my partner organization?
  - id: CreateAccount
    intent: Create a customer account with offerings
    question: How do I provision a new customer account under my partner organization?
  - id: DeleteAccount
    intent: Permanently delete a customer account
    question: What happens to API keys and SSO when a partner account is deleted?
  - id: AuthenticateAccount
    intent: Sign in to a customer account via SSO
    question: Can I log into a customer's account as its SSO admin?
  phrasing_ops: 4
  slug: sendgrid-account-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Account Provisioning API account state operations.
  name: SendGrid Account State API
  phrasing_intents:
  - id: GetAccountState
    intent: Check a customer account's state
    question: Is one of my partner customer accounts active or deactivated?
  - id: UpdateAccountState
    intent: Activate or deactivate a customer account
    question: Can a partner deactivate one of its customer accounts?
  phrasing_ops: 2
  slug: sendgrid-account-state-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Alerts API.
  name: SendGrid Alerts API
  phrasing_intents:
  - id: CreateAlert
    intent: Create a usage or stats alert
    question: Can I get emailed when I've used a certain percentage of my monthly sending limit?
  - id: ListAlert
    intent: List usage and stats alerts
    question: Which email alerts do I have set up on my account?
  - id: GetAlert
    intent: View one alert
    question: Who receives a particular alert and how often?
  - id: DeleteAlert
    intent: Delete an alert
    question: How do I stop getting a specific alert email?
  - id: UpdateAlert
    intent: Change an existing alert
    question: Can I send an existing alert to a different email address?
  phrasing_ops: 5
  slug: sendgrid-alerts-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid API Keys API.
  name: SendGrid API Keys API
  phrasing_intents:
  - id: CreateApiKey
    intent: Create an API key
    question: Can I create a key that only has permission to send mail?
  - id: ListApiKey
    intent: List all API keys
    question: Which API keys exist on my account?
  - id: GetApiKey
    intent: Get an API key's name and scopes
    question: What permissions does a particular API key have?
  - id: UpdateApiKeyName
    intent: Rename an API key
    question: Can I just rename an API key without changing its permissions?
  - id: UpdateApiKey
    intent: Replace an API key's name and scopes
    question: Can I change the permissions on an existing API key?
  - id: DeleteApiKey
    intent: Revoke an API key
    question: Can I revoke an API key that may have leaked?
  phrasing_ops: 6
  slug: sendgrid-api-keys-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Suppressions API: Blocks operations'
  name: SendGrid Blocks API
  phrasing_intents:
  - id: ListSuppressionBlock
    intent: List blocked email addresses
    question: Which addresses are on my blocks list because their servers rejected my mail?
  - id: DeleteSuppressionBlocks
    intent: Delete many or all blocks
    question: Can I clear my entire blocks list in one go?
  - id: GetSuppressionBlock
    intent: Get a specific block
    question: Is a particular address on my blocks list, and why?
  - id: DeleteSuppressionBlock
    intent: Delete a specific block
    question: Can I unblock a single address so it gets mail again?
  phrasing_ops: 4
  slug: sendgrid-blocks-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Suppressions API: Bounces operations'
  name: SendGrid Bounces API
  phrasing_intents:
  - id: ListSuppressionBounces
    intent: List bounced email addresses
    question: Which addresses have bounced recently?
  - id: DeleteSuppressionBounces
    intent: Delete many or all bounces
    question: Can I clear my entire bounce list in one go?
  - id: GetSuppressionBounces
    intent: Get the bounce for an email address
    question: Why did mail to a particular address bounce?
  - id: DeleteSuppressionBounce
    intent: Remove one address from bounces
    question: How do I remove a single address from my bounce list?
  - id: ListSuppressionBouncesClassifications
    intent: Get daily bounce totals by classification
    question: What kinds of bounces am I getting each day, by classification?
  - id: GetSuppressionBouncesClassifications
    intent: Get daily bounces for one classification
    question: How have bounces of one specific classification trended over time?
  phrasing_ops: 6
  slug: sendgrid-bounces-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: The Twilio SendGrid Bulk Email Address Validation API
  name: SendGrid Bulk Email Address Validation API
  phrasing_intents:
  - id: ListEmailJobForVerification
    intent: Get an upload URL for a bulk validation list
    question: How do I upload a file of email addresses to validate in bulk?
  - id: GetValidationsEmailJobs
    intent: List bulk email validation jobs
    question: What bulk email validation jobs have I run?
  - id: GetEmailJobForVerification
    intent: Check a bulk email validation job
    question: Is my bulk email validation job finished yet?
  phrasing_ops: 3
  slug: sendgrid-bulk-email-address-validation-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Legacy Marketing Campaigns: Campaigns API'
  name: SendGrid Campaigns API
  phrasing_intents:
  - id: CreateCampaign
    intent: Create a legacy marketing campaign
    question: What do I need before a legacy campaign can be sent or scheduled?
  - id: ListCampaign
    intent: List legacy marketing campaigns
    question: Which campaigns have I created in legacy Marketing Campaigns?
  - id: GetCampaign
    intent: Get a legacy campaign
    question: Where can I see the content and settings of a single legacy campaign?
  - id: DeleteCampaign
    intent: Delete a legacy campaign
    question: Can I permanently remove a legacy campaign I no longer need?
  - id: UpdateCampaign
    intent: Edit a legacy campaign's content
    question: Can I change the subject and body of a legacy campaign I already created?
  - id: ScheduleCampaign
    intent: Schedule a legacy campaign
    question: Can I pick a future date and time for a legacy campaign to send?
  - id: UpdateScheduledCampaign
    intent: Reschedule a legacy campaign
    question: Can I move an already scheduled campaign to a different send time?
  - id: GetScheduledCampaign
    intent: See when a legacy campaign is scheduled
    question: When is my legacy campaign set to go out?
  phrasing_ops: 11
  slug: sendgrid-campaigns-api-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Category Stats API
  name: SendGrid Categories API
  phrasing_intents:
  - id: ListCategory
    intent: List email categories
    question: What categories have I tagged my emails with?
  - id: ListCategoryStat
    intent: Get email stats per category
    question: How are emails in specific categories performing over time?
  - id: ListCategoryStatSum
    intent: Rank categories by total email stats
    question: Which of my categories got the most opens over a date range?
  phrasing_ops: 3
  slug: sendgrid-categories-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Contacts API
  name: SendGrid Contacts API
  phrasing_intents:
  - id: UpdateContact
    intent: Add or update marketing contacts
    question: How do I add new contacts or update existing ones in Marketing Campaigns?
  - id: DeleteContact
    intent: Delete marketing contacts
    question: How can I delete several marketing contacts at once by their IDs?
  - id: ListContact
    intent: Preview a sample of recent contacts
    question: Can I get a quick look at the 50 most recently added marketing contacts in SendGrid?
  - id: GetContact
    intent: Get one contact's full details
    question: What fields and custom data are stored on a single contact when I look it up by ID?
  - id: ListBatchedContact
    intent: Fetch many contacts by their IDs at once
    question: Can I fetch up to 100 contacts in one call if I already have their IDs?
  - id: DeleteContactIdentifier
    intent: Remove one identifier from a contact
    question: Can I remove just a phone number or external ID from a contact without deleting the contact?
  - id: ListContactCount
    intent: Count all stored contacts
    question: How many marketing contacts do I have stored in total?
  - id: ExportContact
    intent: Export contacts from lists or segments
    question: How do I export the contacts in a list or segment to a file?
  phrasing_ops: 15
  slug: sendgrid-contacts-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Custom Fields API'
  name: SendGrid Custom Fields API
  phrasing_intents:
  - id: CreateCustomField
    intent: Create a legacy custom field
    question: How many custom fields can I create in the legacy contacts database?
  - id: ListCustomField
    intent: List legacy custom fields
    question: What custom fields exist in my legacy contacts database?
  - id: GetCustomField
    intent: Get a legacy custom field
    question: How do I look up one legacy custom field by its ID?
  - id: DeleteCustomField
    intent: Delete a legacy custom field
    question: Can I delete a custom field from the legacy contacts database?
  - id: ListReservedField
    intent: List reserved legacy field names
    question: Which field names are reserved and can't be used for custom fields?
  - id: CreateFieldDefinition
    intent: Create a marketing custom field definition
    question: How do I add a new custom field for my marketing contacts?
  - id: ListFieldDefinition
    intent: List Marketing Campaigns field definitions
    question: What custom and reserved fields are defined for my marketing contacts?
  - id: UpdateFieldDefinition
    intent: Rename a marketing custom field
    question: Can I rename a custom field I defined for marketing contacts?
  phrasing_ops: 9
  slug: sendgrid-custom-fields-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Designs API
  name: SendGrid Designs API
  phrasing_intents:
  - id: CreateDesign
    intent: Create an email design
    question: How do I add a new email design from my own HTML?
  - id: ListDesign
    intent: List designs in my Design Library
    question: What email designs have I saved in my Design Library?
  - id: DuplicateDesign
    intent: Duplicate one of my designs
    question: Can I copy one of my own designs to start a new one?
  - id: GetDesign
    intent: Get one of my designs
    question: Where can I see the stored HTML and subject of one of my designs?
  - id: UpdateDesign
    intent: Edit a design
    question: Can I change just the subject of a design without touching its HTML?
  - id: DeleteDesign
    intent: Delete a design
    question: Is deleting a design from my library permanent?
  - id: ListPreBuiltDesign
    intent: List SendGrid pre-built designs
    question: Which ready-made email designs does SendGrid provide?
  - id: DuplicatePreBuiltDesign
    intent: Copy a pre-built design into my library
    question: How do I copy a pre-built design into my own Design Library?
  phrasing_ops: 9
  slug: sendgrid-designs-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Domain Authentication API
  name: SendGrid Domain Authentication API
  phrasing_intents:
  - id: EmailDnsRecord
    intent: Email domain DNS records to a co-worker
    question: Can I send the DNS records for domain authentication to a colleague who manages our DNS?
  - id: ListAuthenticatedDomain
    intent: List all authenticated domains
    question: Which sending domains have I authenticated in SendGrid?
  - id: AuthenticateDomain
    intent: Authenticate a new sending domain
    question: What do I need to start authenticating a new domain for sending email?
  - id: GetAuthenticatedDomain
    intent: Get one authenticated domain
    question: Where can I see the DNS records and validity of a single authenticated domain?
  - id: UpdateAuthenticatedDomain
    intent: Update an authenticated domain's settings
    question: Can I make an existing authenticated domain my default sending domain?
  - id: DeleteAuthenticatedDomain
    intent: Delete an authenticated domain
    question: Can I remove a domain authentication I no longer send from?
  - id: AssociateSubuserWithDomain
    intent: Assign an authenticated domain to a subuser
    question: Can a subuser send mail using a domain the parent account authenticated?
  - id: DisassociateSubuserFromDomain
    intent: Unassign one of a subuser's multiple domains
    question: How do I take one authenticated domain away from a subuser that has several assigned?
  phrasing_ops: 16
  slug: sendgrid-domain-authentication-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Email Activity API
  name: SendGrid Email Activity API
  phrasing_intents:
  - id: ListMessage
    intent: Search email activity with a query
    question: Can I find every message sent to a certain recipient in Email Activity?
  - id: GetMessage
    intent: Get full details of one message
    question: What happened to a specific email I sent, step by step?
  - id: RequestCsv
    intent: Request a CSV export of email activity
    question: Can I export my email activity to a CSV file?
  - id: DownloadCsv
    intent: Get the download link for an activity CSV
    question: Where do I download the email activity CSV I requested?
  phrasing_ops: 4
  slug: sendgrid-email-activity-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: The Twilio SendGrid Email Address Validation API
  name: SendGrid Email Address Validation API
  phrasing_intents:
  - id: ValidateEmail
    intent: Validate an email address
    question: Can I check whether an email address is valid before I send to it?
  phrasing_ops: 1
  slug: sendgrid-email-address-validation-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: The Twilio SendGrid Enforced TLS API
  name: SendGrid Enforced TLS API
  phrasing_intents:
  - id: ListEnforcedTlsSetting
    intent: Get Enforced TLS settings
    question: Am I currently requiring recipients to support TLS?
  - id: UpdateEnforcedTlsSetting
    intent: Update Enforced TLS settings
    question: How do I require recipients to support TLS?
  phrasing_ops: 2
  slug: sendgrid-enforced-tls-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Engagement Quality API
  name: SendGrid Engagement Quality API
  phrasing_intents:
  - id: ListEngagementQualityScore
    intent: Get my engagement quality scores
    question: What are my SendGrid Engagement Quality (SEQ) scores over the last month?
  - id: ListSubuserEngagementQualityScore
    intent: Get engagement quality scores for subusers
    question: Which of my subusers or customer accounts have weak engagement quality?
  phrasing_ops: 2
  slug: sendgrid-engagement-quality-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Event Webhook API
  name: SendGrid Event Webhook API
  phrasing_intents:
  - id: CreateEventWebhook
    intent: Create an Event Webhook
    question: Can I get delivery, open and bounce events posted to my own URL?
  - id: ListEventWebhook
    intent: List all Event Webhooks
    question: What Event Webhooks do I have configured and where do they post?
  - id: GetSignedEventWebhook
    intent: Get an Event Webhook's signing public key
    question: Where do I find the public key to verify signed Event Webhook requests?
  - id: UpdateSignedEventWebhook
    intent: Toggle signature verification on an Event Webhook
    question: Can I turn on signed requests for one of my Event Webhooks?
  - id: TestEventWebhook
    intent: Send a test event to a webhook URL
    question: Can I check that my endpoint receives Event Webhook posts before real data flows?
  - id: GetEventWebhook
    intent: Get one Event Webhook's settings
    question: What URL and events is a particular Event Webhook configured with?
  - id: UpdateEventWebhook
    intent: Update an Event Webhook's URL or events
    question: Can I change which events an existing webhook sends or where it posts?
  - id: DeleteEventWebhook
    intent: Delete an Event Webhook
    question: Can I remove an Event Webhook I no longer need?
  phrasing_ops: 8
  slug: sendgrid-event-webhook-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Third-Party Integrations for SendGrid Event Export
  name: SendGrid External Integration Endpoints API
  phrasing_intents:
  - id: GetIntegrationsByUser
    intent: List email event forwarding integrations
    question: Which integrations am I using to forward email events?
  - id: AddIntegration
    intent: Create an email event forwarding integration
    question: Can I forward my email events to an outside destination like Segment?
  - id: DeleteIntegration
    intent: Delete event forwarding integrations
    question: Can I delete several event integrations at once?
  - id: FindIntegrationById
    intent: Get one event forwarding integration
    question: What filters and settings does a specific integration have?
  - id: UpdateIntegration
    intent: Update an event forwarding integration
    question: Can I change which events an existing integration forwards?
  phrasing_ops: 5
  slug: sendgrid-external-integration-endpoints-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Suppressions API: Global Suppressions operations'
  name: SendGrid Global Suppressions API
  phrasing_intents:
  - id: CreateGlobalSuppression
    intent: Globally unsubscribe email addresses
    question: Can I stop all email to certain addresses across every group?
  - id: GetGlobalSuppression
    intent: Check whether an address is globally suppressed
    question: Is a specific address on my global unsubscribe list?
  - id: DeleteGlobalSuppression
    intent: Remove an address from global suppressions
    question: Can I resume sending to someone who globally unsubscribed?
  - id: ListGlobalSuppression
    intent: List all globally suppressed addresses
    question: Who has unsubscribed from all of my email?
  phrasing_ops: 4
  slug: sendgrid-global-suppressions-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Suppressions API: Invalid Emails operations'
  name: SendGrid Invalid Emails API
  phrasing_intents:
  - id: ListInvalidEmail
    intent: List invalid email addresses
    question: Which addresses were rejected as invalid or malformed?
  - id: DeleteInvalidEmails
    intent: Remove several or all invalid emails
    question: Can I wipe my whole invalid email list in one go?
  - id: GetInvalidEmail
    intent: Check if an address is marked invalid
    question: Why isn't mail reaching one address, is it on the invalid list?
  - id: DeleteInvalidEmail
    intent: Remove one address from the invalid list
    question: I fixed a typo in a customer's address, how do I take the old entry off the invalid list?
  phrasing_ops: 4
  slug: sendgrid-invalid-emails-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid IP Access Management API
  name: SendGrid IP Access Management API
  phrasing_intents:
  - id: ListAccessActivity
    intent: Review recent account access attempts
    question: Which IP addresses have recently tried to log in to my account or call the API?
  - id: AddIpToAllowList
    intent: Allow IP addresses to access the account
    question: How do I restrict account access to my office IP addresses?
  - id: ListAllowedIp
    intent: List IPs allowed to access the account
    question: Which IP addresses are currently on my account's allow list?
  - id: DeleteAllowedIps
    intent: Remove several IPs from the allow list
    question: Can I remove a batch of IPs from the allow list in one request?
  - id: GetAllowedIp
    intent: View one allowed IP rule
    question: What IP address does a specific allow-list rule ID cover?
  - id: DeleteAllowedIp
    intent: Remove one IP from the allow list
    question: How can I revoke access for a single allowed IP address?
  phrasing_ops: 6
  slug: sendgrid-ip-access-management-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid IP Address Management API
  name: SendGrid IP Address Management API
  phrasing_intents:
  - id: ListIp
    intent: List the IP addresses on my account
    question: Which sending IPs are on my account and which pools are they in?
  - id: AddIp
    intent: Add a dedicated IP address
    question: How do I add a new dedicated IP address to my account?
  - id: GetIp
    intent: Get details for one IP address
    question: Is a particular IP leased, warming up automatically, or assigned to the parent?
  - id: UpdateIp
    intent: Update an IP address's settings
    question: Can I turn off automatic warmup for one of my IPs?
  - id: ListSubUserAssignedToIp
    intent: List subusers assigned to an IP
    question: Which subusers are allowed to send from a given IP?
  - id: AddSubUsersToIp
    intent: Assign subusers to an IP in bulk
    question: How do I give several subusers access to one IP in a single request?
  - id: DeleteSubUsersFromIp
    intent: Unassign subusers from an IP in bulk
    question: Can I remove a batch of subusers from an IP at once?
  - id: ListIpPool
    intent: List IP pools with a sample of their IPs
    question: What IP pools do I have and which IPs are in each?
  phrasing_ops: 15
  slug: sendgrid-ip-address-management-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid IP Address API Operations
  name: SendGrid IP Addresses API
  phrasing_intents:
  - id: AddIp
    intent: Purchase additional IP addresses
    question: How do I add more IP addresses to my account?
  - id: ListIp
    intent: List all assigned and unassigned IPs
    question: Which of my IPs are still warming up, and which subusers use them?
  - id: GetIp
    intent: See which pools an IP address belongs to
    question: Which IP pools has a given IP address been added to?
  - id: ListAssignedIp
    intent: List only assigned IPs
    question: Which of my IP addresses are currently assigned?
  - id: ListRemainingIpCount
    intent: Check how many more IPs I can add
    question: How many more IP addresses can I still add this period, and at what price?
  phrasing_ops: 5
  slug: sendgrid-ip-addresses-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid IP Address Pool API Operations
  name: SendGrid IP Pools API
  phrasing_intents:
  - id: CreateIpPool
    intent: Create an IP pool
    question: Can I group my dedicated IPs into a pool for a certain type of mail?
  - id: ListIpPool
    intent: List all IP pools
    question: Which IP pools have I set up?
  - id: GetIpPool
    intent: List the IPs in a pool
    question: Which IP addresses are in a particular pool?
  - id: UpdateIpPool
    intent: Rename an IP pool
    question: Can I change the name of an existing IP pool?
  - id: DeleteIpPool
    intent: Delete an IP pool
    question: Can I delete an IP pool I don't use anymore?
  - id: AddIpToIpPool
    intent: Add an IP address to a pool
    question: Can the same IP address belong to more than one pool?
  - id: DeleteIpFromIpPool
    intent: Remove an IP address from a pool
    question: Can I take one IP out of a pool without deleting the pool?
  phrasing_ops: 7
  slug: sendgrid-ip-pools-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid IP Warmup API
  name: SendGrid IP Warmup API
  phrasing_intents:
  - id: WarmUpIp
    intent: Start warming up an IP address
    question: Can I gradually ramp up sending volume on a new dedicated IP?
  - id: ListWarmUpIp
    intent: List IPs in warmup
    question: Which of my IP addresses are currently warming up?
  - id: GetWarmUpIp
    intent: Get warmup status for an IP
    question: Is a specific IP still in warmup, and since when?
  - id: StopIpWarmUp
    intent: Stop warming up an IP address
    question: Can I take an IP out of warmup early?
  phrasing_ops: 4
  slug: sendgrid-ip-warmup-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Link Branding API
  name: SendGrid Link Branding API
  phrasing_intents:
  - id: CreateBrandedLink
    intent: Create link branding for a domain
    question: Can I make the tracked links in my emails use my own domain instead of the default one?
  - id: ListBrandedLink
    intent: List all branded links
    question: Which link branding domains do I have set up?
  - id: GetBrandedLink
    intent: Get one branded link
    question: Where can I see the DNS records and status of a specific branded link?
  - id: UpdateBrandedLink
    intent: Change a branded link's default status
    question: Can I make an existing branded link the default one used in my emails?
  - id: DeleteBrandedLink
    intent: Delete a branded link
    question: Can I remove link branding I no longer use?
  - id: ValidateBrandedLink
    intent: Validate a branded link's DNS
    question: I added the CNAMEs — can I check whether my link branding validates now?
  - id: AssociateBrandedLinkWithSubuser
    intent: Assign a branded link to a subuser
    question: Can a subuser use the parent account's link branding?
  - id: ListDefaultBrandedLink
    intent: Get the default branded link
    question: Which branded link is actually used when I send messages?
  phrasing_ops: 10
  slug: sendgrid-link-branding-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Lists API'
  name: SendGrid Lists API
  phrasing_intents:
  - id: CreateContactDbList
    intent: Create a legacy recipient list
    question: How do I create a new recipient list in the old contacts database?
  - id: ListContactDbList
    intent: List all legacy recipient lists
    question: What recipient lists do I have in the legacy contacts database?
  - id: DeleteContactDbLists
    intent: Delete several legacy recipient lists
    question: Can I delete several legacy recipient lists in one call?
  - id: GetContactDbList
    intent: Get one legacy recipient list
    question: How can I look up a single legacy recipient list by its ID?
  - id: UpdateContactDbList
    intent: Rename a legacy recipient list
    question: Can I rename one of my legacy recipient lists?
  - id: DeleteContactDbList
    intent: Delete a legacy recipient list
    question: If I delete a legacy recipient list, can the recipients on it be deleted too?
  - id: ListRecipientsFromContactDbList
    intent: List recipients on a legacy list
    question: Who are the recipients on a given legacy recipient list?
  - id: AddRecipientsToContactDbList
    intent: Add many recipients to a legacy list
    question: How do I put several existing recipients onto a legacy list at once?
  phrasing_ops: 17
  slug: sendgrid-lists-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Assign batch IDs to a send.
  name: SendGrid Mail Batch API
  phrasing_intents:
  - id: CreateMailBatch
    intent: Create a mail batch ID
    question: How do I group several mail sends so I can pause or cancel them together?
  - id: GetMailBatch
    intent: Validate a mail batch ID
    question: Is a particular batch ID still valid?
  phrasing_ops: 2
  slug: sendgrid-mail-batch-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio Mail Send API.
  name: SendGrid Mail Send API
  phrasing_intents:
  - id: SendMail
    intent: Send an email
    question: How do I send a transactional email through the v3 Web API?
  phrasing_ops: 1
  slug: sendgrid-mail-send-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Mail Settings API
  name: SendGrid Mail Settings API
  phrasing_intents:
  - id: ListMailSetting
    intent: List all mail settings and whether they're on
    question: Which mail settings are enabled on my SendGrid account?
  - id: UpdateAddressWhitelist
    intent: Update the address whitelist setting
    question: How can I make sure mail to my own domain is never suppressed?
  - id: ListAddressWhitelist
    intent: View the address whitelist setting
    question: Which email addresses or domains are exempt from suppression right now?
  - id: UpdateBouncePurge
    intent: Change bounce purge ages
    question: Can I automatically clear soft bounces after a set number of days?
  - id: ListBouncePurge
    intent: View bounce purge settings
    question: How long are hard and soft bounces kept before they are purged?
  - id: UpdateFooter
    intent: Set the footer added to every email
    question: How do I add a custom footer to every email I send?
  - id: ListFooter
    intent: View the email footer setting
    question: What custom footer is currently added to the bottom of my emails?
  - id: UpdateForwardBounce
    intent: Forward bounce reports to an address
    question: Can I get bounce reports forwarded to my own inbox?
  phrasing_ops: 13
  slug: sendgrid-mail-settings-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Account Provisioning API offerings operations.
  name: SendGrid Offering API
  phrasing_intents:
  - id: ListAccountOffering
    intent: Get a provisioned account's offerings
    question: What package and add-ons does one of my customer accounts have?
  - id: UpdateAccountOffering
    intent: Change a provisioned account's offerings
    question: Can I move a customer account to a different package?
  - id: ListOffering
    intent: List available offerings
    question: What packages and add-ons can I provision under my organization?
  phrasing_ops: 3
  slug: sendgrid-offering-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Parse Webhook API
  name: SendGrid Parse Webhook API
  phrasing_intents:
  - id: ListParseSetting
    intent: List inbound parse settings
    question: Which hostnames have inbound email parsing set up?
  - id: CreateParseSetting
    intent: Set up inbound email parsing for a hostname
    question: How do I receive incoming emails as POSTs to my app?
  - id: GetParseSetting
    intent: View one hostname's inbound parse setting
    question: Where does inbound mail for a particular hostname get posted?
  - id: UpdateParseSetting
    intent: Change an existing inbound parse setting
    question: Can I point an existing inbound parse hostname at a new webhook URL?
  - id: DeleteParseSetting
    intent: Stop parsing inbound mail for a hostname
    question: Can I turn off inbound parsing for one hostname?
  - id: ListParseStatic
    intent: Get inbound parse usage statistics
    question: How many inbound emails has the parse webhook processed?
  phrasing_ops: 6
  slug: sendgrid-parse-webhook-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Partner Settings API
  name: SendGrid Partner Settings API
  phrasing_intents:
  - id: ListPartnerSetting
    intent: List available partner settings
    question: Which partner settings can I enable on my account?
  phrasing_ops: 1
  slug: sendgrid-partner-settings-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Recipients' Data Erasure API
  name: SendGrid Point Delete System API
  phrasing_intents:
  - id: EraseRecipientEmailData
    intent: Erase recipients' personal email data
    question: Can I delete a person's email data to honor a privacy erasure request?
  phrasing_ops: 1
  slug: sendgrid-point-delete-system-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Recipients API'
  name: SendGrid Recipients API
  phrasing_intents:
  - id: AddRecipient
    intent: Add recipients to the contact database
    question: Can I add new recipients with custom field data to the legacy contact database?
  - id: UpdateRecipient
    intent: Update one or more recipients
    question: How can I change custom field data on existing recipients?
  - id: DeleteRecipients
    intent: Delete several recipients at once
    question: Can I bulk delete recipients by sending an array of their IDs?
  - id: ListRecipient
    intent: List legacy contact database recipients
    question: How do I page through all my legacy Marketing Campaigns recipients?
  - id: GetRecipient
    intent: Get a single recipient
    question: What details are stored for one recipient in my contact database?
  - id: DeleteRecipient
    intent: Permanently delete one recipient
    question: How do I permanently remove one person from all lists and segments, for example for a privacy request?
  - id: GetRecipientList
    intent: See which lists a recipient belongs to
    question: Which lists is a particular recipient on?
  - id: GetBillable
    intent: Get the billable recipient count
    question: How many Marketing Campaigns recipients am I being billed for?
  phrasing_ops: 15
  slug: sendgrid-recipients-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Reverse DNS API
  name: SendGrid Reverse DNS API
  phrasing_intents:
  - id: SetUpReverseDns
    intent: Set up reverse DNS for an IP
    question: Can I make a dedicated IP resolve back to my own domain?
  - id: ListReverseDns
    intent: List reverse DNS records
    question: Which of my IPs have reverse DNS set up?
  - id: GetReverseDns
    intent: Get a reverse DNS record
    question: What A record do I need for a particular reverse DNS setup?
  - id: DeleteReverseDns
    intent: Delete a reverse DNS record
    question: Can I remove reverse DNS from one of my IPs?
  - id: ValidateReverseDns
    intent: Validate a reverse DNS record
    question: I've added the A record — does my reverse DNS validate now?
  phrasing_ops: 5
  slug: sendgrid-reverse-dns-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Scheduled Sends API
  name: SendGrid Scheduled Sends API
  phrasing_intents:
  - id: CreateScheduledSend
    intent: Cancel or pause a scheduled send
    question: Can I pause a scheduled email batch before it goes out?
  - id: ListScheduledSend
    intent: List cancelled or paused scheduled sends
    question: Which scheduled sends have I paused or cancelled?
  - id: GetScheduledSend
    intent: Get the pause/cancel status of a batch
    question: Is a particular scheduled batch currently paused or cancelled?
  - id: UpdateScheduledSend
    intent: Switch a batch between pause and cancel
    question: Can I change a paused batch to cancelled instead?
  - id: DeleteScheduledSend
    intent: Lift a pause or cancellation on a batch
    question: Can I undo a pause on a scheduled batch so it sends again?
  phrasing_ops: 5
  slug: sendgrid-scheduled-sends-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Scopes API
  name: SendGrid Scopes API
  phrasing_intents:
  - id: ListScope
    intent: List the scopes this user can access
    question: Which API permissions does my current key or user actually have?
  - id: ListScopeRequest
    intent: List teammate access requests
    question: Which teammates have asked for extra access recently?
  - id: DenyScopeRequest
    intent: Deny a teammate's access request
    question: How do I reject a teammate's request for more permissions?
  - id: ApproveScopeRequest
    intent: Approve a teammate's access request
    question: Can I grant a teammate the access they requested?
  phrasing_ops: 4
  slug: sendgrid-scopes-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Segments API
  name: SendGrid Segmenting Contacts API
  phrasing_intents:
  - id: ListSegment
    intent: List contact segments (original segmentation)
    question: Which segments exist under the original segmentation endpoints?
  - id: GetSegment
    intent: Get a segment (original segmentation)
    question: Can I fetch a segment's query as JSON from the original segments endpoint?
  - id: DeleteSegment
    intent: Delete a segment but keep its contacts
    question: If I delete a segment, are its contacts deleted too?
  phrasing_ops: 3
  slug: sendgrid-segmenting-contacts-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Segments API V2
  name: SendGrid Segmenting Contacts V2 API
  phrasing_intents:
  - id: CreateSegment
    intent: Create a contact segment from a query
    question: How do I build a segment of contacts using a SQL-style query?
  - id: ListSegment
    intent: List contact segments (Segmentation 2.0)
    question: Which 2.0 segments have I built, and which lists are they based on?
  - id: UpdateSegment
    intent: Rename or change a segment's query
    question: Can I change the query of an existing segment?
  - id: GetSegment
    intent: Get a 2.0 segment and sample contacts
    question: What query defines a given 2.0 segment?
  - id: DeleteSegment
    intent: Delete a 2.0 segment
    question: How do I get rid of a 2.0 segment I no longer use?
  - id: RefreshSegment
    intent: Manually refresh a segment's membership
    question: Can I force a segment to recalculate its contacts right now?
  phrasing_ops: 6
  slug: sendgrid-segmenting-contacts-v2-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Segments API'
  name: SendGrid Segments API
  phrasing_intents:
  - id: CreateSegment
    intent: Create a legacy segment from conditions
    question: How do I build a segment of recipients who match certain field conditions?
  - id: ListSegment
    intent: List legacy contactdb segments
    question: What segments do I have in the legacy contacts database?
  - id: GetSegment
    intent: Get a legacy segment
    question: What conditions define a particular segment?
  - id: UpdateSegment
    intent: Update a legacy segment
    question: Can I change the conditions of an existing segment?
  - id: DeleteSegment
    intent: Delete a legacy segment
    question: When I delete a segment, can I also delete the contacts in it?
  - id: ListRecipientForSegment
    intent: List recipients in a legacy segment
    question: Which recipients currently match a given segment?
  phrasing_ops: 6
  slug: sendgrid-segments-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Send Test Email API
  name: SendGrid Send Test Email API
  phrasing_intents:
  - id: SendTestMarketingEmail
    intent: Send a test of a marketing email
    question: Can I preview a marketing email in real inboxes before sending the campaign?
  phrasing_ops: 1
  slug: sendgrid-send-test-email-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Legacy Marketing Campaigns Sender Identities API
  name: SendGrid Sender Identities API
  phrasing_intents:
  - id: CreateSender
    intent: Create a sender identity
    question: How many sender identities am I allowed to create?
  - id: ListSender
    intent: List sender identities
    question: Which sender identities have been created on my account?
  - id: GetSender
    intent: View a sender identity
    question: What from name, reply-to and address does one sender identity use?
  - id: UpdateSender
    intent: Update a sender identity
    question: Does changing the from email on a sender identity require re-verification?
  - id: DeleteSender
    intent: Delete a sender identity
    question: Can I remove a sender identity I no longer need?
  - id: ResetSenderVerification
    intent: Resend a sender identity verification email
    question: My sender identity never got verified, can I get the verification email again?
  phrasing_ops: 6
  slug: sendgrid-sender-identities-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Sender Verification API
  name: SendGrid Sender Verification API
  phrasing_intents:
  - id: CreateVerifiedSender
    intent: Request verification of a new single sender
    question: How do I verify a from address so I can send without authenticating my whole domain?
  - id: ListVerifiedSender
    intent: List verified and pending senders
    question: Which single senders on my account are verified and which are still pending?
  - id: UpdateVerifiedSender
    intent: Edit a single sender's details
    question: Can I change the nickname or reply-to on a verified single sender?
  - id: DeleteVerifiedSender
    intent: Delete a single sender
    question: Can I remove a single sender I no longer use?
  - id: ListVerifiedSenderDomain
    intent: List DMARC-restricted sender domains
    question: Why won't mail deliver when I use a free webmail address as my sender?
  - id: ResendVerifiedSender
    intent: Resend a single sender verification email
    question: The verification email for my single sender expired, can I get a new one?
  - id: ListVerifiedSenderStepsCompleted
    intent: Check which verification steps are done
    question: Have I completed domain authentication or single sender verification yet?
  - id: VerifySenderToken
    intent: Confirm a sender with its verification token
    question: What do I do with the token from a sender verification email?
  phrasing_ops: 8
  slug: sendgrid-sender-verification-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Senders API
  name: SendGrid Senders API
  phrasing_intents:
  - id: CreateSender
    intent: Create a marketing Sender
    question: How many unique Senders can I create?
  - id: ListSender
    intent: List all marketing Senders
    question: Which Sender identities have I set up for Marketing Campaigns?
  - id: GetSender
    intent: Get a Sender by ID
    question: What are the from address and mailing details of one Sender?
  - id: UpdateSender
    intent: Update a Sender
    question: If I change a Sender's from email, will it need to be verified again?
  - id: DeleteSender
    intent: Delete a Sender
    question: Can I delete a Sender identity I no longer use?
  - id: ResetSenderVerification
    intent: Resend a Sender verification email
    question: My Sender verification email never arrived; can it be sent again?
  phrasing_ops: 6
  slug: sendgrid-senders-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Single Sends API
  name: SendGrid Single Sends API
  phrasing_intents:
  - id: CreateSingleSend
    intent: Create a Single Send
    question: How do I set up a new Single Send marketing email?
  - id: ListSingleSend
    intent: List all Single Sends
    question: What Single Sends have I created so far?
  - id: DeleteSingleSends
    intent: Bulk delete Single Sends
    question: Can I delete several Single Sends at once by ID?
  - id: DuplicateSingleSend
    intent: Duplicate a Single Send
    question: Can I copy an existing Single Send instead of starting from scratch?
  - id: UpdateSingleSend
    intent: Update a draft Single Send
    question: Can I edit a Single Send draft without sending it?
  - id: GetSingleSend
    intent: Get a Single Send by ID
    question: What are the full details of one Single Send?
  - id: DeleteSingleSend
    intent: Delete a Single Send
    question: How do I permanently delete one Single Send?
  - id: ScheduleSingleSend
    intent: Send or schedule a Single Send
    question: Can I send a Single Send right now instead of scheduling it?
  phrasing_ops: 11
  slug: sendgrid-single-sends-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Suppressions API: Spam Reports operations'
  name: SendGrid Spam Reports API
  phrasing_intents:
  - id: ListSpamReport
    intent: List spam report suppressions
    question: Which recipients marked my emails as spam?
  - id: DeleteSpamReports
    intent: Remove several or all spam reports
    question: Can I clear every spam report suppression at once?
  - id: GetSpamReport
    intent: Check if an address reported spam
    question: Did a particular email address report my messages as spam?
  - id: DeleteSpamReport
    intent: Remove one address's spam report
    question: A customer asked to receive email again after flagging it, how do I unsuppress just them?
  phrasing_ops: 4
  slug: sendgrid-spam-reports-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Single Sign-On Certificate Operations
  name: SendGrid SSO Certificates API
  phrasing_intents:
  - id: CreateSsoCertificate
    intent: Add an SSO certificate to an integration
    question: Can I upload my identity provider's public certificate for single sign-on?
  - id: GetSsoCertificate
    intent: Get an SSO certificate
    question: Where can I check the details of a single SSO certificate?
  - id: UpdateSsoCertificate
    intent: Update an SSO certificate
    question: Can I rotate the public key on an existing SSO certificate?
  - id: DeleteSsoCertificate
    intent: Delete an SSO certificate
    question: Can I remove an expired certificate from my SSO setup?
  - id: ListSsoIntegrationCertificate
    intent: List certificates for an SSO integration
    question: Which certificates are attached to one of my SSO integrations?
  phrasing_ops: 5
  slug: sendgrid-sso-certificates-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Single Sign-On Settings Operations
  name: SendGrid SSO Settings API
  phrasing_intents:
  - id: CreateSsoIntegration
    intent: Connect a SAML single sign-on provider
    question: How do I set up SAML single sign-on for my team?
  - id: ListSsoIntegration
    intent: List SSO integrations
    question: Which single sign-on identity providers are connected to my account?
  - id: GetSsoIntegration
    intent: View one SSO integration
    question: What sign-in URL and entity ID does a particular SSO integration use?
  - id: UpdateSsoIntegration
    intent: Modify an existing SSO integration
    question: Can I change the sign-in URL of an SSO integration I already set up?
  - id: DeleteSsoIntegration
    intent: Delete an SSO integration
    question: Can I remove an identity provider configuration I no longer use?
  phrasing_ops: 5
  slug: sendgrid-sso-settings-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Single Sign-On Teammates Operations
  name: SendGrid SSO Teammates API
  phrasing_intents:
  - id: CreateSsoTeammate
    intent: Create an SSO teammate
    question: Can I add a teammate who signs in through single sign-on?
  - id: UpdateSsoTeammate
    intent: Edit an SSO teammate's permissions
    question: Can I change an SSO teammate's scopes or admin status?
  phrasing_ops: 2
  slug: sendgrid-sso-teammates-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Marketing Campaigns Stats API
  name: SendGrid Stats API
  phrasing_intents:
  - id: ListAutomationStat
    intent: Get stats for all Automations
    question: How are my marketing Automations performing overall?
  - id: GetAutomationStat
    intent: Get stats for one Automation
    question: Can I break down a single Automation's stats by step over a date range?
  - id: ListClickTrackingStat
    intent: Get link clicks for an Automation
    question: Which links in my Automation emails get the most clicks?
  - id: ExportAutomationStat
    intent: Export Automation stats as CSV
    question: Can I download my Automation stats as a CSV file?
  - id: ListSingleSendStat
    intent: Get stats for all Single Sends
    question: How did all my Single Send campaigns perform?
  - id: GetSingleSendStat
    intent: Get stats for one Single Send
    question: What were the opens and clicks for one particular Single Send?
  - id: ListSingleSendTrackingStat
    intent: Get link clicks for a Single Send
    question: Which URLs in a Single Send got clicked, and how often?
  - id: ExportSingleSendStat
    intent: Export Single Send stats as CSV
    question: Can I export my Single Send results to a CSV for a report?
  phrasing_ops: 15
  slug: sendgrid-stats-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Subusers API: Statistics Operations'
  name: SendGrid Subuser Statistics API
  phrasing_intents:
  - id: ListSubuserMonthlyStat
    intent: Get one subuser's monthly email stats
    question: How did a single subuser's email perform in a given month?
  - id: ListStat
    intent: Get email stats for chosen subusers
    question: Can I compare email statistics for several subusers over a date range?
  - id: ListMonthlyStat
    intent: Get monthly email stats for all subusers
    question: What were the monthly email numbers across all my subusers?
  - id: ListStatSum
    intent: Get total email metrics across all subusers
    question: What are the combined totals for each email metric across my subusers?
  phrasing_ops: 4
  slug: sendgrid-subuser-statistics-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: The Subuser Website Access API from SendGrid — 1 operation(s) for subuser website access.
  name: SendGrid Subuser Website Access API
  phrasing_intents:
  - id: UpdateSubuserWebsiteAccess
    intent: Enable or disable a subuser's website login
    question: Can I block a subuser from logging into the web app but keep their email sending?
  phrasing_ops: 1
  slug: sendgrid-subuser-website-access-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Subusers API
  name: SendGrid Subusers API
  phrasing_intents:
  - id: ListSubuser
    intent: List subusers
    question: Which subusers exist under my parent account?
  - id: CreateSubuser
    intent: Create a subuser
    question: How do I create a new subuser for a customer or team?
  - id: UpdateSubuser
    intent: Enable or disable a subuser
    question: Can I temporarily switch off a subuser without deleting it?
  - id: DeleteSubuser
    intent: Permanently delete a subuser
    question: Can a deleted subuser ever be recovered?
  - id: GetSubuserCredit
    intent: View a subuser's credit allocation
    question: How many sending credits does a subuser have and how often do they reset?
  - id: UpdateSubuserCredit
    intent: Set a subuser's credit allocation
    question: Can I give a subuser a fixed number of credits that resets monthly?
  - id: UpdateSubuserRemainingCredit
    intent: Adjust a subuser's remaining credits
    question: Can I top up or reduce the credits a subuser has left this period?
  - id: UpdateSubuserIp
    intent: Assign sending IPs to a subuser
    question: Can a subuser send from its own dedicated IP address?
  phrasing_ops: 9
  slug: sendgrid-subusers-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Suppressions API
  name: SendGrid Suppressions API
  phrasing_intents:
  - id: AddSuppressionToAsmGroup
    intent: Add emails to an unsubscribe group
    question: How do I unsubscribe addresses from a specific group?
  - id: ListSuppressionFromAsmGroup
    intent: List suppressions in an unsubscribe group
    question: Which email addresses have unsubscribed from a particular group?
  - id: DeleteSuppressionFromAsmGroup
    intent: Remove an email from an unsubscribe group
    question: Can I resubscribe someone to a group they unsubscribed from?
  - id: SearchSuppressionFromAsmGroup
    intent: Check which emails are suppressed in a group
    question: Given a list of addresses, which ones are unsubscribed from a group?
  - id: ListAsmSuppression
    intent: List all group suppressions
    question: What unsubscribes exist across all my suppression groups?
  - id: GetAsmSuppression
    intent: List groups an email has unsubscribed from
    question: Which groups has a particular person unsubscribed from?
  phrasing_ops: 6
  slug: sendgrid-suppressions-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Teammates API
  name: SendGrid Teammates API
  phrasing_intents:
  - id: InviteTeammate
    intent: Invite a teammate by email
    question: How do I invite a colleague to my account with specific permissions?
  - id: ListTeammate
    intent: List current teammates
    question: Who are the current teammates on my SendGrid account?
  - id: ListSubuserByTemplate
    intent: List subusers a teammate can access
    question: Which subusers can a given teammate reach, and with what scopes?
  - id: GetTeammate
    intent: Get a teammate by username
    question: What permissions does a specific teammate have?
  - id: UpdateTeammate
    intent: Change a teammate's permissions
    question: Can I promote a teammate to admin?
  - id: DeleteTeammate
    intent: Delete a teammate
    question: Who is allowed to remove a teammate from the account?
  - id: ListPendingTeammate
    intent: List pending teammate invitations
    question: Which teammate invitations are still waiting to be accepted?
  - id: DeletePendingTeammate
    intent: Cancel a pending teammate invite
    question: Can I withdraw a teammate invitation before it's accepted?
  phrasing_ops: 9
  slug: sendgrid-teammates-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Templates API
  name: SendGrid Templates API
  phrasing_intents:
  - id: CreateTemplate
    intent: Create a transactional template
    question: Can I create a new dynamic transactional template?
  - id: ListTemplate
    intent: List transactional templates
    question: Which transactional templates do I have?
  - id: DuplicateTemplate
    intent: Duplicate a transactional template
    question: Can I copy an existing template to start a new one from it?
  - id: GetTemplate
    intent: Get a transactional template
    question: Where can I see a single template and its versions?
  - id: UpdateTemplate
    intent: Rename a transactional template
    question: Can I change a transactional template's name without touching its content?
  - id: DeleteTemplate
    intent: Delete a transactional template
    question: Can I delete a transactional template I no longer send?
  phrasing_ops: 6
  slug: sendgrid-templates-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Templates API: Versions operations'
  name: SendGrid Templates Versions API
  phrasing_intents:
  - id: CreateTemplateVersion
    intent: Add a version to a transactional template
    question: How do I create a new version of a transactional template?
  - id: GetTemplateVersion
    intent: Get a transactional template version
    question: What content is in a specific version of my template?
  - id: UpdateTemplateVersion
    intent: Edit a transactional template version
    question: Is it possible to change the subject or HTML of an existing template version?
  - id: DeleteTemplateVersion
    intent: Delete a transactional template version
    question: Can I delete an old version of a transactional template?
  - id: ActivateTemplateVersion
    intent: Activate a transactional template version
    question: How do I make a particular version the active one for a template?
  phrasing_ops: 5
  slug: sendgrid-templates-versions-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Tracking Settings API
  name: SendGrid Tracking API
  phrasing_intents:
  - id: ListTrackingSetting
    intent: List all tracking settings
    question: Which email tracking features are turned on for my account?
  - id: ListClickTrackingSetting
    intent: Get click tracking setting
    question: Is click tracking currently enabled on my emails?
  - id: UpdateClickTrackingSetting
    intent: Turn click tracking on or off
    question: Can I stop SendGrid from rewriting the links in my emails?
  - id: ListGoogleAnalyticsTrackingSetting
    intent: Get Google Analytics tracking setting
    question: Are UTM parameters being added to my email links for Google Analytics?
  - id: UpdateGoogleAnalyticsTrackingSetting
    intent: Update Google Analytics UTM tracking
    question: Can I automatically tag my email links with UTM parameters for Google Analytics?
  - id: ListOpenTrackingSetting
    intent: Get open tracking setting
    question: Is open tracking turned on for my account?
  - id: UpdateOpenTrackingSetting
    intent: Turn open tracking on or off
    question: Can I disable the invisible image that tracks email opens?
  - id: ListSubscriptionTrackingSetting
    intent: Get subscription tracking setting
    question: Are unsubscribe links being added to the bottom of my emails?
  phrasing_ops: 9
  slug: sendgrid-tracking-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: 'Twilio SendGrid Suppressions API: Unsubscribe Group operations'
  name: SendGrid Unsubscribe Groups API
  phrasing_intents:
  - id: CreatAsmGroup
    intent: Create an unsubscribe group
    question: Can I let recipients opt out of just one type of email, like newsletters?
  - id: ListAsmGroup
    intent: List unsubscribe groups
    question: What unsubscribe groups have I created for my recipients to opt out of?
  - id: GetAsmGroup
    intent: Get an unsubscribe group
    question: How many people have unsubscribed from a particular group?
  - id: UpdateAsmGroup
    intent: Update an unsubscribe group
    question: Can I rename a suppression group or change its description?
  - id: DeleteAsmGroup
    intent: Delete an unsubscribe group
    question: What happens to one-click unsubscribes after I delete a suppression group?
  phrasing_ops: 5
  slug: sendgrid-unsubscribe-groups-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Users API.
  name: SendGrid Users API
  phrasing_intents:
  - id: ListAccount
    intent: Get account type and reputation
    question: What type of SendGrid account do I have and what's its reputation?
  - id: ListCredit
    intent: Check my email credit balance
    question: How many emails can I still send before per-email charges kick in?
  - id: ListEmail
    intent: Get the account email address
    question: Which email address is on file for my account?
  - id: UpdateEmail
    intent: Change the account email address
    question: How do I change the email address tied to my account?
  - id: UpdatePassword
    intent: Change my account password
    question: Can I change my password through the API?
  - id: ListProfile
    intent: Get my user profile
    question: What name, company and address are saved on my profile?
  - id: UpdateProfile
    intent: Update my user profile
    question: Can I update just my phone number on my profile without touching other fields?
  - id: ListUsername
    intent: Get my account username
    question: What is my current account username?
  phrasing_ops: 9
  slug: sendgrid-users-api-api
- baseURL: https://api.sendgrid.com
  baseurl_source: declared
  description: Twilio SendGrid Webhook Security API
  name: SendGrid Webhook Security API
  phrasing_intents:
  - id: CreateSecurityPolicy
    intent: Create a webhook security policy
    question: How do I make webhooks sign their requests so I can verify them?
  - id: ListAllSecurityPolicies
    intent: List webhook security policies
    question: Which webhook security policies are configured on my account?
  - id: UpdateSecurityPolicy
    intent: Update a webhook security policy
    question: Can I rotate or change the signing settings on an existing webhook policy?
  - id: GetSecurityPolicy
    intent: View one webhook security policy
    question: What settings does a specific webhook security policy have?
  - id: DeleteSecurityPolicy
    intent: Delete a webhook security policy
    question: Can I delete a webhook security policy that's still in use?
  phrasing_ops: 5
  slug: sendgrid-webhook-security-api
arazzos:
- description: Create a campaign, send a test to yourself, and send the campaign for real.
  name: SendGrid Campaign Test Then Send
  slug: sendgrid-campaign-test-then-send-workflow
- description: Create a marketing list, upsert contacts directly into it, and confirm they landed.
  name: SendGrid Create List and Add Contacts
  slug: sendgrid-create-list-add-contacts-workflow
- description: Create a legacy Marketing Campaign targeting lists and schedule it for delivery.
  name: SendGrid Create and Schedule Campaign
  slug: sendgrid-create-schedule-campaign-workflow
- description: Create a Single Send draft, schedule it for delivery, and read it back.
  name: SendGrid Create and Schedule Single Send
  slug: sendgrid-create-schedule-singlesend-workflow
- description: Create a marketing list, build a segment filtered on that list, and refresh it.
  name: SendGrid Create Segment From List
  slug: sendgrid-create-segment-from-list-workflow
- description: Create a Marketing Campaigns sender and resend its verification when not auto-verified.
  name: SendGrid Create Sender and Resend Verification
  slug: sendgrid-create-sender-resend-verification-workflow
- description: Create a Single Sender identity and check whether sender verification has completed.
  name: SendGrid Create Verified Sender
  slug: sendgrid-create-verified-sender-workflow
- description: Create a reusable design, create a recipient list, and build a Single Send that uses both.
  name: SendGrid Design to Single Send
  slug: sendgrid-design-to-singlesend-workflow
- description: Duplicate an existing transactional template and read the new copy back.
  name: SendGrid Duplicate Template
  slug: sendgrid-duplicate-template-workflow
- description: Create a dynamic transactional template, add a version, and send mail using it.
  name: SendGrid Dynamic Template Send
  slug: sendgrid-dynamic-template-send-workflow
- description: Add an address to the global suppression list and read it back to confirm.
  name: SendGrid Global Suppress and Check
  slug: sendgrid-global-suppress-check-workflow
- description: Create a list, upsert contacts into it, and branch on the list's contact count.
  name: SendGrid List Add Contacts and Count
  slug: sendgrid-list-add-contacts-count-workflow
- description: Create a segment, manually refresh it, then read it back to inspect its membership.
  name: SendGrid Refresh Segment and Get
  slug: sendgrid-refresh-segment-get-workflow
- description: Find contacts with an SGQL query and add the matched address to the global suppression list.
  name: SendGrid Search Contacts and Suppress
  slug: sendgrid-search-contacts-suppress-workflow
- description: Send a single transactional email and branch on whether it was accepted.
  name: SendGrid Send Transactional Mail
  slug: sendgrid-send-transactional-mail-workflow
- description: List Single Sends, branch on whether any exist, and pull aggregate stats for one.
  name: SendGrid Single Send Stats
  slug: sendgrid-singlesend-stats-workflow
- description: Create an unsubscribe suppression group, add addresses to it, and list its suppressions.
  name: SendGrid Suppression Group Add
  slug: sendgrid-suppression-group-add-workflow
- description: Create a template, add a version, activate that version, and read the template back.
  name: SendGrid Template Version Activate
  slug: sendgrid-template-version-activate-workflow
- description: Upsert contacts asynchronously and branch on whether they can be confirmed yet.
  name: SendGrid Upsert Contacts and Confirm
  slug: sendgrid-upsert-contacts-confirm-workflow
artifact_total: 364
asyncapis:
- description: The SendGrid Event Webhook delivers near real-time event data about your email activity via HTTP POST requests. SendGrid batches events into arrays and sends them to your configured webhook URL. Event
  name: SendGrid Event Webhook
  slug: sendgrid-event-webhook-asyncapi
- description: The SendGrid Inbound Parse Webhook processes all incoming email for a domain or subdomain, parses the contents and attachments, and then POSTs multipart/form-data to a URL that you specify. You can us
  name: SendGrid Inbound Parse Webhook
  slug: sendgrid-inbound-parse-asyncapi
collections:
- collection_type: postman
  name: Twilio SendGrid Account Provisioning API
  slug: postman-tsg_account_provisioning_v3
- collection_type: postman
  name: Twilio SendGrid Alerts API
  slug: postman-tsg_alerts_v3
- collection_type: postman
  name: Twilio SendGrid API Keys API
  slug: postman-tsg_api_keys_v3
- collection_type: postman
  name: Twilio SendGrid Domain Authentication API
  slug: postman-tsg_domain_authentication_v3
- collection_type: postman
  name: Twilio SendGrid Email Activity API
  slug: postman-tsg_email_activity_v3
- collection_type: postman
  name: Twilio SendGrid Email Address Validation API
  slug: postman-tsg_email_validation_v3
- collection_type: postman
  name: Twilio SendGrid Enforced TLS API
  slug: postman-tsg_enforced_tls_v3
- collection_type: postman
  name: Twilio SendGrid Integrations API
  slug: postman-tsg_integrations_v3
- collection_type: postman
  name: Twilio SendGrid IP Access Management API
  slug: postman-tsg_ip_access_management_v3
- collection_type: postman
  name: Twilio SendGrid IP Address Management API
  slug: postman-tsg_ip_address_management_v3
- collection_type: postman
  name: Twilio SendGrid IP Warmup API
  slug: postman-tsg_ip_warmup_v3
- collection_type: postman
  name: Twilio SendGrid IP Address API
  slug: postman-tsg_ips_v3
- collection_type: postman
  name: Twilio SendGrid Link Branding API
  slug: postman-tsg_link_branding_v3
- collection_type: postman
  name: Twilio SendGrid Legacy Marketing Campaigns Campaigns API
  slug: postman-tsg_lmc_campaigns_v3
- collection_type: postman
  name: Twilio SendGrid Legacy Marketing Campaigns Contacts API
  slug: postman-tsg_lmc_contactdb_v3
- collection_type: postman
  name: Twilio SendGrid Legacy Marketing Campaigns Sender Identities API
  slug: postman-tsg_lmc_senders_v3
- collection_type: postman
  name: Twilio SendGrid Mail Settings API
  slug: postman-tsg_mail_settings_v3
- collection_type: postman
  name: Twilio SendGrid Mail API
  slug: postman-tsg_mail_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Contacts API
  slug: postman-tsg_mc_contacts_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Custom Fields API
  slug: postman-tsg_mc_custom_fields_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Designs
  slug: postman-tsg_mc_designs_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Lists API
  slug: postman-tsg_mc_lists_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Segments 2.0 API
  slug: postman-tsg_mc_segments_2
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Segments API
  slug: postman-tsg_mc_segments_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Senders API
  slug: postman-tsg_mc_senders_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Single Sends API
  slug: postman-tsg_mc_singlesends_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Statistics API
  slug: postman-tsg_mc_stats_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Send Test Email API
  slug: postman-tsg_mc_test_v3
- collection_type: postman
  name: Twilio SendGrid Partner API
  slug: postman-tsg_partner_v3
- collection_type: postman
  name: Twilio SendGrid Recipients' Data Erasure API
  slug: postman-tsg_recipients_data_erasure_v3
- collection_type: postman
  name: Twilio SendGrid Reverse DNS API
  slug: postman-tsg_reverse_dns_v3
- collection_type: postman
  name: Twilio SendGrid Scheduled Sends API
  slug: postman-tsg_scheduled_sends_v3
- collection_type: postman
  name: Twilio SendGrid Scopes API
  slug: postman-tsg_scopes_v3
- collection_type: postman
  name: Twilio SendGrid Engagement Quality API
  slug: postman-tsg_seq_v3
- collection_type: postman
  name: Twilio SendGrid Single Sign-On API
  slug: postman-tsg_sso_v3
- collection_type: postman
  name: Twilio SendGrid Statistics API
  slug: postman-tsg_stats_v3
- collection_type: postman
  name: Twilio SendGrid Subusers
  slug: postman-tsg_subusers_v3
- collection_type: postman
  name: Twilio SendGrid Suppressions API
  slug: postman-tsg_suppressions_v3
- collection_type: postman
  name: Twilio SendGrid Teammates API
  slug: postman-tsg_teammates_v3
- collection_type: postman
  name: Twilio SendGrid Templates API
  slug: postman-tsg_templates_v3
- collection_type: postman
  name: Twilio SendGrid Tracking Settings API
  slug: postman-tsg_tracking_settings_v3
- collection_type: postman
  name: Twilio SendGrid User API
  slug: postman-tsg_user_v3
- collection_type: postman
  name: Twilio SendGrid Verified Senders API
  slug: postman-tsg_verified_senders_v3
- collection_type: postman
  name: Twilio SendGrid Webhook Configuration API
  slug: postman-tsg_webhooks_v3
- collection_type: open
  name: Twilio SendGrid Provisioning Account API
  slug: open-sendgrid-account-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Account State API
  slug: open-sendgrid-account-state-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Alerts API
  slug: open-sendgrid-alerts-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account API Keys API
  slug: open-sendgrid-api-keys-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Blocks API
  slug: open-sendgrid-blocks-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Bounces API
  slug: open-sendgrid-bounces-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Bulk Email Address Validation API
  slug: open-sendgrid-bulk-email-address-validation-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Campaigns API API
  slug: open-sendgrid-campaigns-api-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Categories API
  slug: open-sendgrid-categories-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Contacts API
  slug: open-sendgrid-contacts-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Custom Fields API
  slug: open-sendgrid-custom-fields-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Designs API
  slug: open-sendgrid-designs-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Domain Authentication API
  slug: open-sendgrid-domain-authentication-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Email Activity API
  slug: open-sendgrid-email-activity-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Email Address Validation API
  slug: open-sendgrid-email-address-validation-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Enforced TLS API
  slug: open-sendgrid-enforced-tls-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Engagement Quality API
  slug: open-sendgrid-engagement-quality-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Event Webhook API
  slug: open-sendgrid-event-webhook-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account External Integration Endpoints API
  slug: open-sendgrid-external-integration-endpoints-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Global Suppressions API
  slug: open-sendgrid-global-suppressions-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Invalid Emails API
  slug: open-sendgrid-invalid-emails-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Access Management API
  slug: open-sendgrid-ip-access-management-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Address Management API
  slug: open-sendgrid-ip-address-management-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Addresses API
  slug: open-sendgrid-ip-addresses-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Pools API
  slug: open-sendgrid-ip-pools-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Warmup API
  slug: open-sendgrid-ip-warmup-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Link Branding API
  slug: open-sendgrid-link-branding-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Lists API
  slug: open-sendgrid-lists-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Mail Batch API
  slug: open-sendgrid-mail-batch-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Mail Send API
  slug: open-sendgrid-mail-send-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Mail Settings API
  slug: open-sendgrid-mail-settings-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Offering API
  slug: open-sendgrid-offering-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Parse Webhook API
  slug: open-sendgrid-parse-webhook-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Partner Settings API
  slug: open-sendgrid-partner-settings-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Point Delete System API
  slug: open-sendgrid-point-delete-system-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Recipients API
  slug: open-sendgrid-recipients-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Reverse DNS API
  slug: open-sendgrid-reverse-dns-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Scheduled Sends API
  slug: open-sendgrid-scheduled-sends-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Scopes API
  slug: open-sendgrid-scopes-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Segmenting Contacts API
  slug: open-sendgrid-segmenting-contacts-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Segmenting Contacts V2 API
  slug: open-sendgrid-segmenting-contacts-v2-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Segments API
  slug: open-sendgrid-segments-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Send Test Email API
  slug: open-sendgrid-send-test-email-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Sender Identities API
  slug: open-sendgrid-sender-identities-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Sender Verification API
  slug: open-sendgrid-sender-verification-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Senders API
  slug: open-sendgrid-senders-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Single Sends API
  slug: open-sendgrid-single-sends-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Spam Reports API
  slug: open-sendgrid-spam-reports-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account SSO Certificates API
  slug: open-sendgrid-sso-certificates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account SSO Settings API
  slug: open-sendgrid-sso-settings-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account SSO Teammates API
  slug: open-sendgrid-sso-teammates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Stats API
  slug: open-sendgrid-stats-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Subuser Statistics API
  slug: open-sendgrid-subuser-statistics-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Subuser Website Access API
  slug: open-sendgrid-subuser-website-access-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Subusers API
  slug: open-sendgrid-subusers-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Suppressions API
  slug: open-sendgrid-suppressions-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Teammates API
  slug: open-sendgrid-teammates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Templates API
  slug: open-sendgrid-templates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Templates Versions API
  slug: open-sendgrid-templates-versions-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Tracking API
  slug: open-sendgrid-tracking-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Unsubscribe Groups API
  slug: open-sendgrid-unsubscribe-groups-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Users API API
  slug: open-sendgrid-users-api-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Webhook Security API
  slug: open-sendgrid-webhook-security-api
common:
- group: design
  href: https://artifacts.apis.io/sendgrid/rules/sendgrid-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/sendgrid-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/rules/sendgrid-rules.yml
  title: ''
  type: Spectral
  url: rules/sendgrid-rules.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/rules/sendgrid-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/sendgrid-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/json-ld/sendgrid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sendgrid-context.jsonld
- group: design
  href: https://artifacts.apis.io/sendgrid/vocabulary/sendgrid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendgrid-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/sendgrid/a2a/sendgrid-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sendgrid-a2a.yml
- group: other
  href: https://artifacts.apis.io/sendgrid/hosts/sendgrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendgrid-hosts.yml
- group: build
  href: https://artifacts.apis.io/sendgrid/integrations/sendgrid-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/sendgrid-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/sendgrid/vendors/sendgrid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sendgrid-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.twilio.com/en-us/press
- group: other
  title: ''
  type: Leadership
  url: https://www.twilio.com/en-us/company/leadership
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/twilio/
- group: other
  href: https://artifacts.apis.io/sendgrid/capabilities/sendgrid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sendgrid-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/sendgrid/overlays/sendgrid-tsg_account_provisioning_v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sendgrid-tsg_account_provisioning_v3-overlay.yaml
- group: build
  href: https://artifacts.apis.io/sendgrid/packages/sendgrid-packages.yml
  title: ''
  type: Packages
  url: packages/sendgrid-packages.yml
- group: agent
  href: https://artifacts.apis.io/sendgrid/mcp/sendgrid-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sendgrid-mcp.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/conformance/sendgrid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendgrid-conformance.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/errors/sendgrid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendgrid-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/lifecycle/sendgrid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sendgrid-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/conventions/sendgrid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sendgrid-conventions.yml
- group: operate
  href: https://artifacts.apis.io/sendgrid/changelog/sendgrid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sendgrid-changelog.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/data-model/sendgrid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sendgrid-data-model.yml
- group: start
  href: https://artifacts.apis.io/sendgrid/sandbox/sendgrid-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sendgrid-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/sendgrid/security/sendgrid-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sendgrid-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sendgrid/security/sendgrid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sendgrid-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/sendgrid/agentic-access/sendgrid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendgrid-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sendgrid/security/sendgrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendgrid-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sendgrid/authentication/sendgrid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendgrid-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendgrid/overview
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-campaign-test-then-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-campaign-test-then-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-create-list-add-contacts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-list-add-contacts-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-create-schedule-campaign-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-schedule-campaign-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-create-schedule-singlesend-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-schedule-singlesend-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-create-segment-from-list-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-segment-from-list-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-create-sender-resend-verification-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-sender-resend-verification-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-create-verified-sender-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-verified-sender-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-design-to-singlesend-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-design-to-singlesend-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-duplicate-template-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-duplicate-template-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-dynamic-template-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-dynamic-template-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-global-suppress-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-global-suppress-check-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-list-add-contacts-count-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-list-add-contacts-count-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-refresh-segment-get-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-refresh-segment-get-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-search-contacts-suppress-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-search-contacts-suppress-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-send-transactional-mail-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-send-transactional-mail-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-singlesend-stats-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-singlesend-stats-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-suppression-group-add-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-suppression-group-add-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-template-version-activate-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-template-version-activate-workflow.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/arazzo/sendgrid-upsert-contacts-confirm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-upsert-contacts-confirm-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://app.sendgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.twilio.com/docs/sendgrid
- group: docs
  title: ''
  type: APIReference
  url: https://www.twilio.com/docs/sendgrid/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.twilio.com/docs/sendgrid/for-developers/sending-email/api-getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication
- group: start
  title: ''
  type: Signup
  url: https://signup.sendgrid.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://sendgrid.com/en-us/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.sendgrid.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendgrid.com/
- group: company
  title: ''
  type: Blog
  url: https://sendgrid.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sendgrid
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/sendgrid/sendgrid-python
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/sendgrid/sendgrid-nodejs
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/sendgrid/sendgrid-java
- group: build
  title: ''
  type: C# SDK
  url: https://github.com/sendgrid/sendgrid-csharp
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/sendgrid/sendgrid-go
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/sendgrid/sendgrid-ruby
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/sendgrid/sendgrid-php
- group: build
  title: ''
  type: Libraries
  url: https://www.twilio.com/docs/sendgrid/for-developers/sending-email/libraries
- group: start
  title: ''
  type: GettingStarted
  url: https://sendgrid.com/en-us/solutions/email-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendgrid.com/policies/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendgrid.com/policies/privacy/
- group: auth
  title: ''
  type: Security
  url: https://sendgrid.com/en-us/policies/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.twilio.com/en-us/changelog?product=sendgrid-email-api,twilio-sendgrid-platform
- group: operate
  title: ''
  type: RateLimits
  url: https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/rate-limits
- group: company
  title: ''
  type: Website
  url: https://sendgrid.com/en-us
- group: start
  title: ''
  type: Login
  url: https://login.sendgrid.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sendgrid
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/sendgrid
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-email-send.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-email-send.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-webhooks.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-webhooks.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-suppressions.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-suppressions.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-account-setup.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-account-setup.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-email-settings.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-email-settings.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-engagement-quality.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-engagement-quality.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-inbound-parse.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-inbound-parse.md
- group: agent
  href: https://artifacts.apis.io/sendgrid/skills/sendgrid-deliverability-advisor.md
  title: ''
  type: AgentSkill
  url: skills/sendgrid-deliverability-advisor.md
- group: docs
  href: https://artifacts.apis.io/sendgrid/asyncapi/sendgrid-event-webhook-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/sendgrid-event-webhook-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/sendgrid/asyncapi/sendgrid-inbound-parse-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/sendgrid-inbound-parse-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/asyncapi/sendgrid-event-webhook-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/sendgrid-event-webhook-asyncapi.yml
- group: auth
  href: https://artifacts.apis.io/sendgrid/scopes/sendgrid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sendgrid-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/sendgrid/plans/sendgrid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendgrid-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sendgrid/rate-limits/sendgrid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sendgrid-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/sendgrid/packages/sendgrid-packages.yml
  title: ''
  type: SDKs
  url: packages/sendgrid-packages.yml
- group: operate
  href: https://artifacts.apis.io/sendgrid/lifecycle/sendgrid-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sendgrid-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/sendgrid/security/sendgrid-trust-center.yml
  title: ''
  type: Compliance
  url: security/sendgrid-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/sendgrid/finops/sendgrid-finops.yml
  title: ''
  type: FinOps
  url: finops/sendgrid-finops.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/rules/sendgrid-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/sendgrid-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/sendgrid/rules/sendgrid-asyncapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/sendgrid-asyncapi-spectral-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendgrid
- group: agent
  href: https://artifacts.apis.io/sendgrid/llms/sendgrid-twilio-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendgrid-twilio-docs-llms.txt
created: '2025-08-14'
description: SendGrid is a cloud-based email delivery platform, acquired by Twilio in 2019, that provides transactional and marketing email at scale over an HTTP v3 REST API and an SMTP relay. The platform spans Mail Send, dynamic transactional templates, Marketing Campaigns (contacts, lists, Segments 2.0, Single Sends), email address validation, suppression management, domain authentication (SPF/DKIM/DMARC), dedicated IP management and warm-up, subusers, Engagement Quality scoring, and detailed delivery statistics. Event data is delivered asynchronously through the Event Webhook and inbound mail through Inbound Parse. All APIs authenticate with a scoped bearer API key against api.sendgrid.com, with an EU data-residency host at api.eu.sendgrid.com. Developer documentation and the API reference are published on the Twilio documentation site.
features:
- Mail Send v3 API for transactional email
- SMTP Relay for legacy app integration
- Marketing Campaigns API and UI
- Contacts API with custom fields and segments
- Email Validation API
- Inbound Parse webhook
- 'Free Trial: 100 emails/day for 60 days'
- Essentials at $19.95/mo for 100k emails
- Pro at $89.95/mo for 2.5M emails with dedicated IP
- Premier custom pricing with $12k/year minimum
- 'Mail Send rate limit: 100/min Free, 600/min Paid'
- Subusers for billing and access isolation
- SPF, DKIM, DMARC authentication
- Activity Feed (3-day Essentials, 7-day Pro)
- Send Time Optimization (Pro+)
- Tiered IP warm-up service (Premier)
finops:
- has_sources: true
  method: derived
  name: Sendgrid Finops
  primary_unit: subscription
  service_category: ''
  slug: sendgrid-finops
  template: false
image: https://sendgrid.com/brand/sg-logo-300.png
json_schemas:
- name: AccountID
  property_count: 1
  slug: sendgrid-account-provisioning-account-id
- name: Account
  property_count: 2
  slug: sendgrid-account-provisioning-account
- name: Catalog
  property_count: 1
  slug: sendgrid-account-provisioning-catalog
- name: OfferingList
  property_count: 1
  slug: sendgrid-account-provisioning-offering-list
- name: Offering
  property_count: 3
  slug: sendgrid-account-provisioning-offering-v1
- name: Pagination
  property_count: 1
  slug: sendgrid-account-provisioning-pagination
- name: Profile
  property_count: 7
  slug: sendgrid-account-provisioning-profile
- name: StateRead
  property_count: 1
  slug: sendgrid-account-provisioning-state-read
- name: StateWrite
  property_count: 1
  slug: sendgrid-account-provisioning-state-write
- name: all_segments_response
  property_count: 11
  slug: sendgrid-all-segments200
- name: API Key Name and ID
  property_count: 2
  slug: sendgrid-api-key-response
- name: API Key Name, ID, and Scopes
  property_count: 3
  slug: sendgrid-api-key-scopes-response
- name: Domain Authentication - Mandatory Subdomain
  property_count: 12
  slug: sendgrid-authenticated-domain
- name: Domain Authentication
  property_count: 12
  slug: sendgrid-authenticated-domain-spf
- name: Blocks Response
  property_count: 0
  slug: sendgrid-blocks-response
- name: Bounce Response
  property_count: 4
  slug: sendgrid-bounce-response
- name: BounceType
  property_count: 0
  slug: sendgrid-bounce-type
- name: Campaigns Response
  property_count: 14
  slug: sendgrid-campaigns2xx
- name: 'Stats: Category Stats'
  property_count: 2
  slug: sendgrid-category-stats
- name: Classification
  property_count: 0
  slug: sendgrid-classification
- name: 'Settings: Click Tracking'
  property_count: 2
  slug: sendgrid-click-tracking
- name: contact-details2
  property_count: 25
  slug: sendgrid-contact-details
- name: contact-details3
  property_count: 25
  slug: sendgrid-contact-details3
- name: contact-export
  property_count: 10
  slug: sendgrid-contact-export
- name: contact-import
  property_count: 6
  slug: sendgrid-contact-import
- name: contact-request
  property_count: 14
  slug: sendgrid-contact-request
- name: ContactDB Custom field schema with ID.
  property_count: 3
  slug: sendgrid-contactdb-custom-field-id2xx
- name: ContactDB lists
  property_count: 3
  slug: sendgrid-contactdb-list2xx
- name: 'ContactDB: Recipient response'
  property_count: 6
  slug: sendgrid-contactdb-recipient-response201
- name: 'ContactDB: Recipient'
  property_count: 1
  slug: sendgrid-contactdb-recipient200
- name: 'ContactDB: Segments: Conditions'
  property_count: 4
  slug: sendgrid-contactdb-segments-conditions
- name: 'ContactDB:: Segments with ID'
  property_count: 5
  slug: sendgrid-contactdb-segments-id200
- name: Create a Segment request
  property_count: 4
  slug: sendgrid-contactdb-segments
- name: custom_field_definitions_response
  property_count: 3
  slug: sendgrid-custom-field-definitions-response
- name: Default
  property_count: 0
  slug: sendgrid-default
- name: Default1
  property_count: 0
  slug: sendgrid-default1
- name: Design Input
  property_count: 4
  slug: sendgrid-design-input
- name: Design Output
  property_count: 4
  slug: sendgrid-design-output
- name: Design Output - Summary
  property_count: 6
  slug: sendgrid-design-output-summary
- name: Enforced TLS Request Response
  property_count: 3
  slug: sendgrid-enforced-tls-request-response
- name: ErrorResponse
  property_count: 2
  slug: sendgrid-error-response
- name: EventName
  property_count: 0
  slug: sendgrid-event-name
- name: 'Event Webhook Response Body: All Webhooks'
  property_count: 2
  slug: sendgrid-event-webhook-all-response
- name: EventWebhookNoDatesResponse
  property_count: 19
  slug: sendgrid-event-webhook-no-dates-response
- name: Create and Update Event Webhook Request Body
  property_count: 17
  slug: sendgrid-event-webhook-request
- name: Send Event Webhook Test Request
  property_count: 5
  slug: sendgrid-event-webhook-test-request
- name: EventWebhookUnsignedResponse
  property_count: 20
  slug: sendgrid-event-webhook-unsigned-response
- name: FieldType
  property_count: 0
  slug: sendgrid-field-type
- name: FileType
  property_count: 0
  slug: sendgrid-file-type
- name: full_segment
  property_count: 12
  slug: sendgrid-full-segment
- name: Generation
  property_count: 0
  slug: sendgrid-generation
- name: GET Validations Email Jobs job_id 200 Response
  property_count: 1
  slug: sendgrid-get-validations-email-jobs-job-id200-response
- name: GET Validations Email Jobs 200 Response
  property_count: 1
  slug: sendgrid-get-validations-email-jobs200-response
- name: 'Settings: Google Analytics'
  property_count: 6
  slug: sendgrid-google-analytics-settings
- name: IntegrationInput
  property_count: 4
  slug: sendgrid-integration-input
- name: IntegrationPatch
  property_count: 4
  slug: sendgrid-integration-patch
- name: Integration
  property_count: 6
  slug: sendgrid-integration
- name: Invalid Email
  property_count: 3
  slug: sendgrid-invalid-email
- name: IP Access Response
  property_count: 1
  slug: sendgrid-ip-access-management2xx
- name: 'IP Pools: Pool Resp'
  property_count: 1
  slug: sendgrid-ip-pools200
- name: 'IP Warmup: IP'
  property_count: 0
  slug: sendgrid-ip-warmup200
- name: Items
  property_count: 0
  slug: sendgrid-items
- name: Link Branding 200 Response
  property_count: 9
  slug: sendgrid-link-branding200
- name: list
  property_count: 4
  slug: sendgrid-list
- name: 'Mail Settings: Address Whitelabel'
  property_count: 2
  slug: sendgrid-mail-settings-address-whitelabel200
- name: 'Mail Settings: Bounce Purge'
  property_count: 3
  slug: sendgrid-mail-settings-bounce-purge
- name: 'Mail Settings: Footer'
  property_count: 3
  slug: sendgrid-mail-settings-footer
- name: 'Mail Settings: Forward Bounce'
  property_count: 2
  slug: sendgrid-mail-settings-forward-bounce
- name: 'Mail Settings: Forward Spam'
  property_count: 2
  slug: sendgrid-mail-settings-forward-spam
- name: 'Mail Settings: Template'
  property_count: 2
  slug: sendgrid-mail-settings-template200
- name: metadata
  property_count: 4
  slug: sendgrid-metadata
- name: OutboundIpType
  property_count: 0
  slug: sendgrid-outbound-ip-type
- name: Parse Setting
  property_count: 4
  slug: sendgrid-parse-setting
- name: Single Sign-On Teammate Update Request Body
  property_count: 7
  slug: sendgrid-patch-sso-teammates-request
- name: Single Sign-On Teammates PATCH Response.
  property_count: 19
  slug: sendgrid-patch-sso-teammates200
- name: PermissionType
  property_count: 0
  slug: sendgrid-permission-type
- name: Campaigns Request
  property_count: 12
  slug: sendgrid-post-campaigns-request
- name: Single Sign-On Teammate Create Request Body
  property_count: 8
  slug: sendgrid-post-sso-teammates-request
- name: Single Sign-On Teammates POST Response.
  property_count: 8
  slug: sendgrid-post-sso-teammates201
- name: Update Email Validations Jobs 200 Response
  property_count: 3
  slug: sendgrid-put-validations-email-jobs200-response
- name: recipient-export
  property_count: 10
  slug: sendgrid-recipient-export
- name: EmailAddress
  property_count: 1
  slug: sendgrid-recipients-data-erasure-erase-recipients-request
- name: JobId
  property_count: 1
  slug: sendgrid-recipients-data-erasure-job-id
- name: Region1
  property_count: 0
  slug: sendgrid-region1
- name: Region4
  property_count: 0
  slug: sendgrid-region4
- name: reserved_field_definitions_response
  property_count: 0
  slug: sendgrid-reserved-field-definitions-response
- name: Reverse DNS
  property_count: 10
  slug: sendgrid-reverse-dns
- name: User Scheduled Send status
  property_count: 2
  slug: sendgrid-scheduled-send-status
- name: segment_refresh_response
  property_count: 1
  slug: sendgrid-segment-refresh202
- name: segment_summary
  property_count: 8
  slug: sendgrid-segment-summary
- name: segment_update
  property_count: 2
  slug: sendgrid-segment-update
- name: segment_response
  property_count: 15
  slug: sendgrid-segment2xx
- name: selfMetadata
  property_count: 1
  slug: sendgrid-self-metadata
- name: Sender ID Request
  property_count: 9
  slug: sendgrid-sender-id-request
- name: Sender ID
  property_count: 14
  slug: sendgrid-sender-id
- name: Sender Request
  property_count: 9
  slug: sendgrid-sender-request
- name: Sender
  property_count: 14
  slug: sendgrid-sender
- name: singlesend_response
  property_count: 10
  slug: sendgrid-singlesend-response
- name: singlesend_response_short
  property_count: 9
  slug: sendgrid-singlesend-response-short
- name: singlesend-schedule
  property_count: 2
  slug: sendgrid-singlesend-schedule
- name: singlesend_search
  property_count: 3
  slug: sendgrid-singlesend-search
- name: SinglesendsLinkStatsResponse
  property_count: 3
  slug: sendgrid-singlesends-link-stats-response
- name: SinglesendsResponse
  property_count: 2
  slug: sendgrid-singlesends-response
- name: Spam Reports Response
  property_count: 0
  slug: sendgrid-spam-reports-response
- name: Single Sign-On Certificate Body
  property_count: 5
  slug: sendgrid-sso-certificate-body
- name: Single Sign-On Integration
  property_count: 10
  slug: sendgrid-sso-integration
- name: 'Stats: Advanced Global Stats'
  property_count: 16
  slug: sendgrid-stats-advanced-global-stats
- name: Status
  property_count: 0
  slug: sendgrid-status
- name: Status1
  property_count: 0
  slug: sendgrid-status1
- name: Status2
  property_count: 0
  slug: sendgrid-status2
- name: Status3
  property_count: 0
  slug: sendgrid-status3
- name: 'Settings: Subscription Tracking'
  property_count: 6
  slug: sendgrid-subscription-tracking-settings
- name: Subuser Credits reset request body
  property_count: 3
  slug: sendgrid-subuser-credits-request
- name: Credits of a Subuser
  property_count: 5
  slug: sendgrid-subuser-credits
- name: Subuser::POST
  property_count: 5
  slug: sendgrid-subuser-post
- name: List all Subusers for a parent response
  property_count: 5
  slug: sendgrid-subuser
- name: subuser_stats
  property_count: 2
  slug: sendgrid-subuser-stats
- name: Suppression Group Request Base
  property_count: 3
  slug: sendgrid-suppression-group-request-base-props
- name: 'Suppressions: Suppression Group'
  property_count: 5
  slug: sendgrid-suppression-group
- name: 'Transactional Templates: Template'
  property_count: 6
  slug: sendgrid-transactional-template
- name: 'Transactional Templates: Version Output'
  property_count: 13
  slug: sendgrid-transactional-template-version-output
- name: 'Transactional Templates: Template Lean'
  property_count: 5
  slug: sendgrid-transactional-templates-template-lean
- name: Type
  property_count: 0
  slug: sendgrid-type
- name: Type1
  property_count: 0
  slug: sendgrid-type1
- name: Type2
  property_count: 0
  slug: sendgrid-type2
- name: Type3
  property_count: 0
  slug: sendgrid-type3
- name: 'User: Profile'
  property_count: 11
  slug: sendgrid-user-profile
- name: UserType
  property_count: 0
  slug: sendgrid-user-type
- name: UserType1
  property_count: 0
  slug: sendgrid-user-type1
- name: UserType2
  property_count: 0
  slug: sendgrid-user-type2
- name: Valid
  property_count: 0
  slug: sendgrid-valid
- name: Valid1
  property_count: 0
  slug: sendgrid-valid1
- name: Valid2
  property_count: 0
  slug: sendgrid-valid2
- name: Verdict
  property_count: 0
  slug: sendgrid-verdict
- name: Verified Sender Response Schema
  property_count: 14
  slug: sendgrid-verified-sender-response
jsonld:
- class_count: 120
  name: Sendgrid Context
  property_count: 127
  slug: sendgrid-context
layout: provider
modified: '2026-09-16'
name: SendGrid
nav: Providers
network: true
overview: 'SendGrid publishes 63 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account State API, Alerts API, and 60 more. Tagged areas include Email, Email API, Marketing Email, SMTP, and T1.


  The SendGrid catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  SendGrid''s developer surface includes changelog, sandbox, authentication, developer portal, documentation, API reference, getting-started guide, and 93 more developer resources.'
plans:
- name: Sendgrid Plans Pricing
  plan_count: 4
  slug: sendgrid-plans-pricing
- name: Sendgrid Price Estimates
  plan_count: 0
  slug: sendgrid-price-estimates
random_paper: 8
rate_limits:
- limit_count: 0
  name: Sendgrid Rate Limits
  slug: sendgrid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: SendGrid — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: sendgrid-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: SendGrid API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 3
  slug: sendgrid-rules
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: SendGrid API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: sendgrid-spectral-rules
scopes:
- name: Sendgrid Scopes
  scope_count: 185
  slug: sendgrid-scopes
  summary_line: 185 scopes
score:
  band: exemplar
  composite: 87.3
  coverage:
    artifact_dirs: 38
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 77.4
    developer_ergonomics: 89.3
    discoverability: 80.4
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 87.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 63
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
    score: 61.1
screenshot: https://apis.io/screenshots/sendgrid/sendgrid-2026-06-20T193652.png
security:
- kind: authentication
  name: Sendgrid Authentication
  slug: sendgrid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendgrid Domain Security
  slug: sendgrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sendgrid Vulnerability Disclosure
  slug: sendgrid-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sendgrid Trust Center
  slug: sendgrid-trust-center
  summary_line: SOC 2 Type II, SOC 2 Type I, ISO/IEC 27001:2013, ISO/IEC 27017:2015, ISO/IEC 27018:2019, PCI DSS Level 1, PCI DSS Level 4, HIPAA (eligible products & services), Binding Corporate Rules
skill_count: 8
skills:
- name: twilio-sendgrid-account-setup
  slug: sendgrid-account-setup
- name: twilio-sendgrid-deliverability-advisor
  slug: sendgrid-deliverability-advisor
- name: twilio-sendgrid-email-send
  slug: sendgrid-email-send
- name: twilio-sendgrid-email-settings
  slug: sendgrid-email-settings
- name: twilio-sendgrid-engagement-quality
  slug: sendgrid-engagement-quality
- name: twilio-sendgrid-inbound-parse
  slug: sendgrid-inbound-parse
- name: twilio-sendgrid-suppressions
  slug: sendgrid-suppressions
- name: twilio-sendgrid-webhooks
  slug: sendgrid-webhooks
slug: sendgrid
tags:
- Email
- Email API
- Marketing Email
- SMTP
- T1
- Transactional Email
- Email Marketing
- Deliverability
- Marketing
website: https://sendgrid.com/en-us
---
