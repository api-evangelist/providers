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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 516
  human_in_the_loop: 2
  name: Twilio Agentic Access
  operation_count: 1053
  slug: twilio-agentic-access
  summary_line: 1053 operations · 516 acting · 2 human-in-the-loop
api_count: 55
apis:
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The A2p API from Twilio — 5 operation(s) for a2p.
  name: Twilio A2p API
  phrasing_intents:
  - id: CreateBrandRegistrationOtp
    intent: Resend the sole proprietor brand verification OTP
    question: My sole proprietor brand never got its verification text, can I send the one-time code again?
  - id: FetchBrandRegistrations
    intent: Check an A2P brand registration
    question: What is the approval status of my A2P 10DLC brand registration?
  - id: UpdateBrandRegistrations
    intent: Resubmit a brand registration
    question: Can I push a failed brand registration back through review after fixing my profile?
  - id: ListBrandRegistrations
    intent: List my A2P brand registrations
    question: Which brands have I registered for A2P 10DLC messaging?
  - id: CreateBrandRegistrations
    intent: Register a brand for A2P 10DLC
    question: How do I register my business as a brand before sending 10DLC texts in the US?
  - id: CreateBrandVetting
    intent: Attach an external vetting to a brand
    question: How do I add a secondary vetting score I already obtained to my brand?
  - id: ListBrandVetting
    intent: List secondary vettings for a brand
    question: What third-party vettings have been run on my brand?
  - id: FetchBrandVetting
    intent: View one brand vetting result
    question: What score did a particular vetting give my brand?
  phrasing_ops: 8
  slug: twilio-a2p-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Generate access tokens for SDKs
  name: Twilio Access Tokens API
  phrasing_intents:
  - id: createAccessToken
    intent: Create a Verify SDK access token
    question: What token does my mobile app need to register a push or TOTP factor?
  phrasing_ops: 1
  slug: twilio-access-tokens-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage Twilio accounts and subaccounts
  name: Twilio Accounts API
  phrasing_intents:
  - id: listAccounts
    intent: List subaccounts
    question: Which subaccounts sit under my main account?
  - id: createAccount
    intent: Create a subaccount
    question: How do I create a separate subaccount for each of my customers?
  - id: fetchAccount
    intent: Look up an account or subaccount
    question: What is the status of a specific subaccount?
  - id: updateAccount
    intent: Rename, suspend or close an account
    question: How do I suspend a subaccount for a customer who stopped paying?
  phrasing_ops: 4
  slug: twilio-accounts-api
- baseURL: https://monitor.twilio.com
  baseurl_source: declared
  description: The Alerts API from Twilio — 2 operation(s) for alerts.
  name: Twilio Alerts API
  phrasing_intents:
  - id: FetchAlert
    intent: Look up one debugger alert
    question: Can I see the full details of a single alert from my debugger?
  - id: ListAlert
    intent: List alerts by severity and date
    question: Which errors and warnings has my account raised this week?
  phrasing_ops: 2
  slug: twilio-alerts-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage alphanumeric sender IDs
  name: Twilio Alpha Senders API
  phrasing_intents:
  - id: listAlphaSenders
    intent: List alphanumeric sender IDs on a Messaging Service
    question: Which alphanumeric sender IDs are attached to my Messaging Service?
  - id: addAlphaSender
    intent: Add an alphanumeric sender ID to a Messaging Service
    question: How do I send SMS that shows my brand name instead of a phone number?
  phrasing_ops: 2
  slug: twilio-alpha-senders-api
- baseURL: https://microvisor.twilio.com
  baseurl_source: declared
  description: The Apps API from Twilio — 3 operation(s) for apps.
  name: Twilio Apps API
  phrasing_intents:
  - id: ListApp
    intent: List my Microvisor apps
    question: Which Microvisor apps have I uploaded to my account?
  - id: FetchApp
    intent: Look up a Microvisor app
    question: How do I see the details of one Microvisor app?
  - id: DeleteApp
    intent: Delete a Microvisor app
    question: Can I remove an old Microvisor app I'm no longer deploying?
  - id: FetchAppManifest
    intent: Get a Microvisor app's manifest
    question: Where can I read the manifest for a Microvisor app?
  phrasing_ops: 4
  slug: twilio-apps-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The Archives API from Twilio — 1 operation(s) for archives.
  name: Twilio Archives API
  phrasing_intents:
  - id: DeleteArchivedCall
    intent: Delete an archived call from Bulk Export
    question: How do I remove a call record from my Bulk Export archive?
  phrasing_ops: 1
  slug: twilio-archives-api
- baseURL: https://autopilot.twilio.com
  baseurl_source: declared
  description: The Assistants API from Twilio — 24 operation(s) for assistants.
  name: Twilio Assistants API
  phrasing_intents:
  - id: FetchAssistant
    intent: Look up an Autopilot assistant
    question: How do I see the settings of one Autopilot assistant I already built?
  - id: UpdateAssistant
    intent: Change an Autopilot assistant's settings
    question: Can I rename an existing Autopilot assistant without rebuilding it?
  - id: DeleteAssistant
    intent: Delete an Autopilot assistant
    question: How do I permanently remove a virtual assistant I no longer use?
  - id: ListAssistant
    intent: List my Autopilot assistants
    question: Which Autopilot assistants exist on my Twilio account?
  - id: CreateAssistant
    intent: Create a new Autopilot assistant
    question: How do I start building a new intelligent virtual assistant from scratch?
  - id: FetchDefaults
    intent: See an assistant's default tasks
    question: Which task does my assistant fall back to when it doesn't understand the user?
  - id: UpdateDefaults
    intent: Set an assistant's default tasks
    question: Can I change the fallback task my bot uses when it can't match an intent?
  - id: FetchDialogue
    intent: Read one assistant dialogue
    question: Can I review a single conversation my Autopilot bot had with an end user?
  phrasing_ops: 52
  slug: twilio-assistants-api
- baseURL: https://verify.twilio.com
  baseurl_source: declared
  description: The Attempts API from Twilio — 3 operation(s) for attempts.
  name: Twilio Attempts API
  phrasing_intents:
  - id: ListVerificationAttempt
    intent: List verification attempts
    question: Which verification codes were sent to a particular phone number?
  - id: FetchVerificationAttempt
    intent: Get one verification attempt
    question: What happened with one specific verification attempt?
  - id: FetchVerificationAttemptsSummary
    intent: Summarize verification conversion rates
    question: What percentage of my verification attempts actually converted?
  phrasing_ops: 3
  slug: twilio-attempts-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage primary and secondary auth tokens
  name: Twilio Auth Tokens API
  phrasing_intents:
  - id: promoteAuthToken
    intent: Promote the secondary auth token (legacy path)
    question: Can I promote my secondary auth token through the older unversioned endpoint?
  - id: createSecondaryAuthToken
    intent: Create a secondary auth token (legacy path)
    question: Can I create a secondary auth token through the legacy unversioned endpoint?
  - id: deleteSecondaryAuthToken
    intent: Delete the secondary auth token (legacy path)
    question: Can I delete my secondary auth token through the older unversioned path?
  phrasing_ops: 3
  slug: twilio-auth-tokens-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The ByocTrunks API from Twilio — 2 operation(s) for byoctrunks.
  name: Twilio ByocTrunks API
  phrasing_intents:
  - id: CreateByocTrunk
    intent: Create a BYOC trunk
    question: How do I connect my own carrier to Twilio with a new BYOC trunk?
  - id: ListByocTrunk
    intent: List my BYOC trunks
    question: Which Bring Your Own Carrier trunks do I have configured?
  - id: FetchByocTrunk
    intent: View a BYOC trunk
    question: What voice URL and connection policy is a BYOC trunk using?
  - id: UpdateByocTrunk
    intent: Change a BYOC trunk's settings
    question: Can I swap the connection policy on a BYOC trunk that already exists?
  - id: DeleteByocTrunk
    intent: Delete a BYOC trunk
    question: How do I remove a BYOC trunk for a carrier we stopped using?
  phrasing_ops: 5
  slug: twilio-byoctrunks-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Initiate, manage, and monitor voice calls
  name: Twilio Calls API
  phrasing_intents:
  - id: listCalls
    intent: List calls on an account
    question: Which calls did we place to a particular phone number last month?
  - id: createCall
    intent: Place an outbound phone call
    question: How do I make an outbound phone call and control it with TwiML?
  - id: fetchCall
    intent: Get one call's details
    question: How long did a specific call last and how did it end?
  - id: updateCall
    intent: Redirect or hang up a live call
    question: How do I hang up a call that is still in progress?
  - id: deleteCall
    intent: Delete a call record
    question: Can I remove an old call from my account's call log?
  phrasing_ops: 5
  slug: twilio-calls-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Manage push authentication challenges
  name: Twilio Challenges API
  phrasing_intents:
  - id: listChallenges
    intent: List push authentication challenges for a user
    question: Which login approval challenges has a user been sent recently?
  - id: createChallenge
    intent: Send a push authentication challenge
    question: How do I ask a user to approve a login from their phone with a push notification?
  phrasing_ops: 2
  slug: twilio-challenges-api
- baseURL: https://flex-api.twilio.com/v1
  baseurl_source: declared
  description: Manage Flex communication channels
  name: Twilio Channels API
  phrasing_intents:
  - id: listChannels
    intent: List Flex channels
    question: Which Flex chat channels are open for customer conversations?
  - id: createChannel
    intent: Open a Flex channel for a customer
    question: How do I start a new Flex chat channel when a customer reaches out?
  - id: fetchChannel
    intent: View a Flex channel
    question: What flow and task is a particular Flex channel attached to?
  - id: deleteChannel
    intent: Delete a Flex channel
    question: How do I remove a Flex channel once the conversation is over?
  phrasing_ops: 4
  slug: twilio-channels-api
- baseURL: https://wireless.twilio.com
  baseurl_source: declared
  description: The Commands API from Twilio — 2 operation(s) for commands.
  name: Twilio Commands API
  phrasing_intents:
  - id: FetchCommand
    intent: Look up a SIM command
    question: Was a command I sent to a SIM actually delivered?
  - id: DeleteCommand
    intent: Delete a SIM command record
    question: Can I delete a command record from my wireless account?
  - id: ListCommand
    intent: List SIM commands
    question: Which commands to my devices failed to deliver?
  - id: CreateCommand
    intent: Send a command to a SIM
    question: How do I send a text command to an IoT device through its SIM?
  phrasing_ops: 4
  slug: twilio-commands-api
- baseURL: https://trusthub.twilio.com
  baseurl_source: declared
  description: The ComplianceInquiries API from Twilio — 3 operation(s) for complianceinquiries.
  name: Twilio ComplianceInquiries API
  phrasing_intents:
  - id: CreateComplianceInquiry
    intent: Start an embedded compliance onboarding session
    question: How do I launch the embedded compliance form for a new customer profile?
  - id: UpdateComplianceInquiry
    intent: Resume or reopen a compliance inquiry
    question: My compliance inquiry session expired, can I pick it up again?
  - id: CreateComplianceTollfreeInquiry
    intent: Start a toll-free verification inquiry
    question: How do I get a toll-free number verified for texting through the embedded form?
  phrasing_ops: 3
  slug: twilio-complianceinquiries-api
- baseURL: https://video.twilio.com/v1
  baseurl_source: declared
  description: Configure automatic composition rules
  name: Twilio Composition Hooks API
  phrasing_intents:
  - id: listCompositionHooks
    intent: List composition hooks via the legacy endpoint
    question: Is there an unversioned endpoint that lists my composition hooks?
  - id: createCompositionHook
    intent: Create a composition hook via the legacy endpoint
    question: Can I still create an auto-composition hook through the legacy unversioned endpoint?
  - id: fetchCompositionHook
    intent: Look up a composition hook via the legacy endpoint
    question: Can I fetch a composition hook from the older unversioned path?
  - id: updateCompositionHook
    intent: Update a composition hook via the legacy endpoint
    question: Can I edit a composition hook through the legacy unversioned endpoint?
  - id: deleteCompositionHook
    intent: Delete a composition hook via the legacy endpoint
    question: Can I delete a composition hook through the older unversioned path?
  phrasing_ops: 5
  slug: twilio-composition-hooks-api
- baseURL: https://video.twilio.com/v1
  baseurl_source: declared
  description: Compose multiple recordings into a single file
  name: Twilio Compositions API
  phrasing_intents:
  - id: listCompositions
    intent: List compositions (legacy unversioned endpoint)
    question: Using the older unversioned compositions path, which video compositions are still processing?
  - id: createComposition
    intent: Compose room recordings (legacy unversioned endpoint)
    question: On the older unversioned endpoint, how do I merge a room's recordings into one media file?
  - id: fetchComposition
    intent: Get a composition (legacy unversioned endpoint)
    question: Through the older unversioned path, what is the status of one composition?
  - id: deleteComposition
    intent: Delete a composition (legacy unversioned endpoint)
    question: Through the older unversioned path, how do I delete a composition?
  - id: fetchCompositionSettings
    intent: Read default composition storage settings
    question: Where are my compositions being stored by default, and is encryption on?
  - id: createCompositionSettings
    intent: Configure where compositions are stored
    question: How do I send finished compositions to my own S3 bucket?
  - id: FetchComposition
    intent: Get a recording composition
    question: What is the status and duration of a specific recording composition?
  - id: DeleteComposition
    intent: Delete a recording composition
    question: How do I permanently delete a v1 recording composition?
  phrasing_ops: 10
  slug: twilio-compositions-api
- baseURL: https://video.twilio.com
  baseurl_source: declared
  description: The CompositionSettings API from Twilio — 1 operation(s) for compositionsettings.
  name: Twilio CompositionSettings API
  phrasing_intents:
  - id: FetchCompositionSettings
    intent: Read the default composition settings
    question: Are my video compositions stored in my own S3 bucket or encrypted?
  - id: CreateCompositionSettings
    intent: Set storage and encryption for compositions
    question: How do I store finished compositions in my own S3 bucket?
  phrasing_ops: 2
  slug: twilio-compositionsettings-api
- baseURL: https://insights.twilio.com
  baseurl_source: declared
  description: The Conferences API from Twilio — 7 operation(s) for conferences.
  name: Twilio Conferences API
  phrasing_intents:
  - id: FetchConference
    intent: Get a conference's insights summary
    question: Why did a particular conference end, and were any quality issues detected?
  - id: ListConference
    intent: Search conference insights summaries
    question: Which of my conferences had quality or configuration issues detected last week?
  - id: FetchConferenceParticipant
    intent: Get one participant's call quality summary
    question: What call quality metrics did one participant have during a conference?
  - id: ListConferenceParticipant
    intent: List participant summaries for a conference
    question: How did each participant's experience look in a past conference?
  - id: listConferences
    intent: List conferences on an account
    question: Which conference calls are in progress on my account right now?
  - id: fetchConference
    intent: Get a live conference resource
    question: Is a particular conference room still in progress?
  - id: updateConference
    intent: End or announce to a live conference
    question: How do I end a conference call for everyone at once?
  - id: listParticipants
    intent: List who is in a live conference
    question: Who is currently connected to my conference call?
  phrasing_ops: 9
  slug: twilio-conferences-api
- baseURL: https://microvisor.twilio.com
  baseurl_source: declared
  description: The Configs API from Twilio — 2 operation(s) for configs.
  name: Twilio Configs API
  phrasing_intents:
  - id: ListAccountConfig
    intent: List the config values on my account
    question: Which configuration keys are set on my account?
  - id: CreateAccountConfig
    intent: Add a new account config value
    question: Can I store a non-secret setting as an account-level config?
  - id: FetchAccountConfig
    intent: Look up one account config by key
    question: Can I read a single config value by its key?
  - id: UpdateAccountConfig
    intent: Change the value of an account config
    question: Can I change an existing config value without deleting it first?
  - id: DeleteAccountConfig
    intent: Delete an account config
    question: Can I remove a config entry I no longer need?
  phrasing_ops: 5
  slug: twilio-configs-api
- baseURL: https://conversations.twilio.com
  baseurl_source: declared
  description: The Configuration API from Twilio — 5 operation(s) for configuration.
  name: Twilio Configuration API
  phrasing_intents:
  - id: FetchConfiguration
    intent: Get account-wide Conversations settings
    question: What are the default Conversations settings on my account?
  - id: UpdateConfiguration
    intent: Change default Conversations settings
    question: Can I make conversations go inactive automatically after a period of silence?
  - id: ListConfigurationAddress
    intent: List Conversations address configurations
    question: Which phone numbers and WhatsApp addresses are set up to auto-create conversations?
  - id: CreateConfigurationAddress
    intent: Configure an address for Conversations
    question: How do I make incoming SMS to a number start a new conversation automatically?
  - id: FetchConfigurationAddress
    intent: Get one address configuration
    question: How is auto-creation set up for one particular phone number or WhatsApp address?
  - id: UpdateConfigurationAddress
    intent: Update an address configuration
    question: Can I turn off automatic conversation creation for an address I already configured?
  - id: DeleteConfigurationAddress
    intent: Remove an address configuration
    question: Can I stop an address from being handled by Conversations by deleting its configuration?
  - id: FetchConfigurationWebhook
    intent: Get account-level Conversations webhooks
    question: Where are my Conversations pre-event and post-event webhooks currently pointed?
  phrasing_ops: 11
  slug: twilio-configuration-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The ConnectionPolicies API from Twilio — 4 operation(s) for connectionpolicies.
  name: Twilio ConnectionPolicies API
  phrasing_intents:
  - id: CreateConnectionPolicy
    intent: Create a connection policy
    question: How do I start a new connection policy for sending calls to my own SIP servers?
  - id: ListConnectionPolicy
    intent: List connection policies
    question: Which connection policies have I set up for routing calls to my SIP infrastructure?
  - id: FetchConnectionPolicy
    intent: View a connection policy
    question: What are the details of one particular connection policy?
  - id: UpdateConnectionPolicy
    intent: Rename a connection policy
    question: Can I change the friendly name of a connection policy I already have?
  - id: DeleteConnectionPolicy
    intent: Delete a connection policy
    question: How do I remove a connection policy I no longer use?
  - id: CreateConnectionPolicyTarget
    intent: Add a SIP target to a connection policy
    question: How do I add a SIP address as a new target on a connection policy?
  - id: ListConnectionPolicyTarget
    intent: List the targets of a connection policy
    question: Which SIP endpoints does a connection policy send calls to?
  - id: FetchConnectionPolicyTarget
    intent: View one connection policy target
    question: What SIP address, priority and weight does a single policy target have?
  phrasing_ops: 10
  slug: twilio-connectionpolicies-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Manage marketing contacts
  name: Twilio Contacts API
  phrasing_intents:
  - id: listContacts
    intent: List marketing contacts
    question: Who is in my marketing contacts database?
  - id: upsertContacts
    intent: Add or update marketing contacts
    question: How are existing contacts matched when I upload a batch of contacts?
  - id: deleteContacts
    intent: Delete marketing contacts
    question: Can I remove several marketing contacts at once by ID?
  - id: searchContacts
    intent: Search marketing contacts with a query
    question: Can I find contacts matching conditions like a domain or a signup date?
  phrasing_ops: 4
  slug: twilio-contacts-api
- baseURL: https://content.twilio.com
  baseurl_source: declared
  description: The Content API from Twilio — 3 operation(s) for content.
  name: Twilio Content API
  phrasing_intents:
  - id: FetchApprovalFetch
    intent: Check a content template's approval status
    question: Has my message template been approved for WhatsApp yet?
  - id: FetchContent
    intent: Look up one content template
    question: What does a specific message template contain, including its variables?
  - id: DeleteContent
    intent: Delete a content template
    question: How do I remove a message template we no longer send?
  - id: ListContent
    intent: List my content templates
    question: Which message templates have I created on my account?
  phrasing_ops: 4
  slug: twilio-content-api
- baseURL: https://content.twilio.com
  baseurl_source: declared
  description: The ContentAndApprovals API from Twilio — 1 operation(s) for contentandapprovals.
  name: Twilio ContentAndApprovals API
  phrasing_intents:
  - id: ListContentAndApprovals
    intent: List content templates with approval status
    question: Which of my content templates have been approved for sending?
  phrasing_ops: 1
  slug: twilio-contentandapprovals-api
- baseURL: https://conversations.twilio.com
  baseurl_source: declared
  description: The Conversations API from Twilio — 10 operation(s) for conversations.
  name: Twilio Conversations API
  phrasing_intents:
  - id: CreateConversation
    intent: Start a new conversation
    question: How do I open a new multi-channel conversation thread?
  - id: ListConversation
    intent: List conversations
    question: Which conversations in my default service are still active?
  - id: UpdateConversation
    intent: Update a conversation's name, state or timers
    question: Can I rename an existing conversation or change its state to closed?
  - id: DeleteConversation
    intent: Delete a conversation
    question: Can I remove an entire conversation thread from my service?
  - id: FetchConversation
    intent: Look up a conversation
    question: Can I look up a conversation by its unique name rather than its SID?
  - id: CreateConversationMessage
    intent: Post a message to a conversation
    question: How do I send a message into a conversation on behalf of a participant?
  - id: ListConversationMessage
    intent: List messages in a conversation
    question: Can I read a conversation's message history newest first?
  - id: UpdateConversationMessage
    intent: Edit a message already in a conversation
    question: Can I edit the text of a message after it was posted to a conversation?
  phrasing_ops: 22
  slug: twilio-conversations-api
- baseURL: https://accounts.twilio.com
  baseurl_source: declared
  description: The Credentials API from Twilio — 10 operation(s) for credentials.
  name: Twilio Credentials API
  phrasing_intents:
  - id: ListCredentialAws
    intent: List the AWS credentials stored on my account
    question: Which AWS credentials have I stored in my Twilio account?
  - id: CreateCredentialAws
    intent: Store a new AWS access key credential
    question: What format does an AWS access key and secret need when I save it as a credential?
  - id: FetchCredentialAws
    intent: Look up one stored AWS credential
    question: Can I look up a single AWS credential by its SID?
  - id: UpdateCredentialAws
    intent: Rename a stored AWS credential
    question: Can I rename an AWS credential after I've saved it?
  - id: DeleteCredentialAws
    intent: Delete a stored AWS credential
    question: Can I permanently remove an AWS credential I no longer use?
  - id: ListCredentialPublicKey
    intent: List the public key credentials on my account
    question: Which public keys have I registered as credentials on my account?
  - id: CreateCredentialPublicKey
    intent: Register a new public key credential
    question: Can I upload a PEM public key to my account as a credential?
  - id: FetchCredentialPublicKey
    intent: Look up one public key credential
    question: Can I retrieve a single public key credential by its SID?
  phrasing_ops: 24
  slug: twilio-credentials-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Deactivations API from Twilio — 1 operation(s) for deactivations.
  name: Twilio Deactivations API
  phrasing_intents:
  - id: FetchDeactivation
    intent: Get US numbers deactivated on a given date
    question: Which US phone numbers were deactivated by carriers on a specific day?
  phrasing_ops: 1
  slug: twilio-deactivations-api
- baseURL: https://microvisor.twilio.com
  baseurl_source: declared
  description: The Devices API from Twilio — 6 operation(s) for devices.
  name: Twilio Devices API
  phrasing_intents:
  - id: ListDevice
    intent: List my Microvisor devices
    question: Which Microvisor devices are registered to my account?
  - id: FetchDevice
    intent: Get one Microvisor device
    question: Which app is targeted to a specific device, and is logging on?
  - id: UpdateDevice
    intent: Update, retarget or restart a device
    question: How do I deploy a different app to one of my Microvisor devices?
  - id: ListDeviceConfig
    intent: List a device's config values
    question: Which configuration keys are set on a Microvisor device?
  - id: CreateDeviceConfig
    intent: Add a config value to a device
    question: How do I push a new configuration setting to a Microvisor device?
  - id: FetchDeviceConfig
    intent: Read one config value on a device
    question: What value does a particular config key currently have on my device?
  - id: UpdateDeviceConfig
    intent: Change a config value on a device
    question: How do I change an existing configuration value on a Microvisor device?
  - id: DeleteDeviceConfig
    intent: Delete a config value from a device
    question: Can I remove a configuration key from a device?
  phrasing_ops: 13
  slug: twilio-devices-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The DialingPermissions API from Twilio — 4 operation(s) for dialingpermissions.
  name: Twilio DialingPermissions API
  phrasing_intents:
  - id: FetchDialingPermissionsCountry
    intent: Check voice dialing permissions for a country
    question: Am I allowed to place calls to numbers in Brazil from my account?
  - id: ListDialingPermissionsCountry
    intent: List voice dialing permissions by country
    question: Which countries can my account call right now?
  - id: CreateDialingPermissionsCountryBulkUpdate
    intent: Change dialing permissions for several countries
    question: How do I turn on calling to several countries at once?
  - id: ListDialingPermissionsHrsPrefixes
    intent: List high-risk special number prefixes for a country
    question: Which number prefixes count as high-risk special services in a given country?
  phrasing_ops: 4
  slug: twilio-dialingpermissions-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Validate email addresses
  name: Twilio Email Validation API
  phrasing_intents:
  - id: validateEmail
    intent: Check if an email address is deliverable
    question: Is this email address real and able to receive mail?
  phrasing_ops: 1
  slug: twilio-email-validation-api
- baseURL: https://trusthub.twilio.com
  baseurl_source: declared
  description: The EndUserTypes API from Twilio — 2 operation(s) for endusertypes.
  name: Twilio EndUserTypes API
  phrasing_intents:
  - id: ListEndUserType
    intent: List Trust Hub end-user types
    question: What kinds of end users can I register in Trust Hub?
  - id: FetchEndUserType
    intent: Look up an end-user type
    question: Which fields does a particular end-user type require?
  phrasing_ops: 2
  slug: twilio-endusertypes-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Manage end-user entities for TOTP and push
  name: Twilio Entities API
  phrasing_intents:
  - id: listEntities
    intent: List end-user entities in a Verify service
    question: Which end users have been set up for TOTP or push authentication?
  - id: createEntity
    intent: Create an end-user entity for authentication
    question: How do I register an end user before enrolling them in TOTP or push?
  phrasing_ops: 2
  slug: twilio-entities-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The ESimProfiles API from Twilio — 2 operation(s) for esimprofiles.
  name: Twilio ESimProfiles API
  phrasing_intents:
  - id: CreateEsimProfile
    intent: Order an eSIM profile
    question: How do I order an eSIM profile for an IoT device?
  - id: ListEsimProfile
    intent: List eSIM profiles
    question: Which eSIM profiles have I ordered, and what state are they in?
  - id: FetchEsimProfile
    intent: Look up one eSIM profile
    question: Has a specific eSIM profile finished downloading to its device?
  phrasing_ops: 3
  slug: twilio-esimprofiles-api
- baseURL: https://monitor.twilio.com
  baseurl_source: declared
  description: The Events API from Twilio — 2 operation(s) for events.
  name: Twilio Events API
  phrasing_intents:
  - id: FetchEvent
    intent: Look up one account audit event
    question: Can I see the full record of a single audit event on my account?
  - id: ListEvent
    intent: Search my account's audit event history
    question: What changes has a particular user or API key made on my account?
  phrasing_ops: 2
  slug: twilio-events-api
- baseURL: https://bulkexports.twilio.com
  baseurl_source: declared
  description: The Exports API from Twilio — 6 operation(s) for exports.
  name: Twilio Exports API
  phrasing_intents:
  - id: FetchDay
    intent: Get one day's export file for a resource type
    question: Can I download the exported message records for a single UTC day?
  - id: ListDay
    intent: List the daily export files available
    question: Which days have export files ready for my messages?
  - id: FetchExport
    intent: Look up the export for a resource type
    question: What does the export resource for Messages link to?
  - id: FetchExportConfiguration
    intent: Check automatic daily export settings
    question: Is automatic daily export turned on for my call records?
  - id: UpdateExportConfiguration
    intent: Turn automatic daily exports on or off
    question: Can I have a file generated automatically every day once the day is over?
  - id: ListExportCustomJob
    intent: List custom date-range export jobs
    question: Which custom export jobs have I requested for my messages?
  - id: CreateExportCustomJob
    intent: Request an export for a custom date range
    question: Can I export a whole month of call records in one job?
  - id: FetchJob
    intent: Check on one custom export job
    question: Has my custom export job finished yet?
  phrasing_ops: 9
  slug: twilio-exports-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Manage authentication factors (TOTP, push)
  name: Twilio Factors API
  phrasing_intents:
  - id: listFactors
    intent: List an end user's authentication factors
    question: Which TOTP or push factors has a user enrolled?
  - id: createFactor
    intent: Enroll a TOTP or push factor for a user
    question: How do I let a user set up an authenticator app for two-factor login?
  phrasing_ops: 2
  slug: twilio-factors-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The Fleets API from Twilio — 2 operation(s) for fleets.
  name: Twilio Fleets API
  phrasing_intents:
  - id: CreateFleet
    intent: Create a Super SIM fleet
    question: How do I group my Super SIMs into a fleet with shared settings?
  - id: ListFleet
    intent: List my Super SIM fleets
    question: Which Super SIM fleets are on my account?
  - id: FetchFleet
    intent: Look up one Super SIM fleet
    question: Can I check the data limit and command URLs on one fleet?
  - id: UpdateFleet
    intent: Change an existing Super SIM fleet's settings
    question: Can I move an existing fleet to a different network access profile?
  phrasing_ops: 4
  slug: twilio-fleets-api
- baseURL: https://flex-api.twilio.com/v1
  baseurl_source: declared
  description: Manage Flex Flow routing
  name: Twilio Flex Flows API
  phrasing_intents:
  - id: listFlexFlows
    intent: List my Flex Flows
    question: Which Flex Flows decide how inbound contacts reach my agents?
  - id: createFlexFlow
    intent: Create a Flex Flow
    question: How do I route a new inbound contact channel into Flex?
  - id: fetchFlexFlow
    intent: Get one Flex Flow
    question: What channel type and integration does a specific Flex Flow use?
  - id: updateFlexFlow
    intent: Update a Flex Flow
    question: How do I switch an existing Flex Flow to a different Studio flow?
  - id: deleteFlexFlow
    intent: Delete a Flex Flow
    question: Can I permanently remove a Flex Flow I no longer route contacts through?
  phrasing_ops: 5
  slug: twilio-flex-flows-api
- baseURL: https://studio.twilio.com
  baseurl_source: declared
  description: The Flows API from Twilio — 12 operation(s) for flows.
  name: Twilio Flows API
  phrasing_intents:
  - id: ListExecution
    intent: List the executions of a Studio Flow
    question: Which executions has my Studio Flow run recently?
  - id: CreateExecution
    intent: Trigger a Studio Flow for a contact
    question: How do I start a Studio Flow from my own code instead of an inbound message?
  - id: FetchExecution
    intent: Look up one Flow execution
    question: Can I check the status of a single Studio Flow execution?
  - id: DeleteExecution
    intent: Delete a Flow execution and its steps
    question: Can I delete an execution record along with all of its steps?
  - id: UpdateExecution
    intent: End a running Flow execution
    question: Can I stop a Studio Flow execution that is stuck mid-flow?
  - id: FetchExecutionContext
    intent: Get the latest context of a Flow execution
    question: Can I see the variables and widget data a Flow execution has collected so far?
  - id: ListExecutionStep
    intent: List the steps an execution went through
    question: Which widgets did a Flow execution pass through, in order?
  - id: FetchExecutionStep
    intent: Look up one step of a Flow execution
    question: Can I inspect a single step of an execution by its SID?
  phrasing_ops: 19
  slug: twilio-flows-api
- baseURL: https://verify.twilio.com
  baseurl_source: declared
  description: The Forms API from Twilio — 1 operation(s) for forms.
  name: Twilio Forms API
  phrasing_intents:
  - id: FetchForm
    intent: Get the forms for a form type
    question: What form definition does the push factor enrollment use?
  phrasing_ops: 1
  slug: twilio-forms-api
- baseURL: https://numbers.twilio.com
  baseurl_source: declared
  description: The HostedNumber API from Twilio — 6 operation(s) for hostednumber.
  name: Twilio HostedNumber API
  phrasing_intents:
  - id: FetchAuthorizationDocument
    intent: Check a letter of authorization for hosting
    question: Has the letter of authorization for my hosted numbers been signed yet?
  - id: DeleteAuthorizationDocument
    intent: Cancel an authorization document request
    question: Can I withdraw a letter of authorization I sent out for signing?
  - id: ListAuthorizationDocument
    intent: List authorization documents
    question: Which letters of authorization are still waiting to be signed?
  - id: CreateAuthorizationDocument
    intent: Send a letter of authorization for signing
    question: How do I get the number owner to sign a letter of authorization for hosting?
  - id: FetchBulkHostedNumberOrder
    intent: Check a bulk number hosting order
    question: How far along is my bulk request to host many numbers?
  - id: ListDependentHostedNumberOrder
    intent: List orders covered by an authorization document
    question: Which hosted number orders depend on a given letter of authorization?
  - id: FetchHostedNumberOrder
    intent: Check a hosted number order
    question: Where is my request to host a phone number in the verification process?
  - id: DeleteHostedNumberOrder
    intent: Cancel a hosted number order
    question: Can I cancel a number hosting request after submitting it?
  phrasing_ops: 10
  slug: twilio-hostednumber-api
- baseURL: https://flex-api.twilio.com/v1
  baseurl_source: declared
  description: Access Flex Insights questionnaires and assessments
  name: Twilio Insights API
  phrasing_intents:
  - id: listQuestionnaires
    intent: List quality management questionnaires
    question: Which quality management questionnaires exist in Flex Insights?
  - id: createQuestionnaire
    intent: Create a quality management questionnaire
    question: Can I create a new questionnaire for scoring agent conversations?
  phrasing_ops: 2
  slug: twilio-insights-api
- baseURL: https://flex-api.twilio.com/v1
  baseurl_source: declared
  description: Manage customer interactions
  name: Twilio Interactions API
  phrasing_intents:
  - id: createInteraction
    intent: Start a customer interaction in Flex
    question: How do I open a new customer interaction and route it to an agent?
  - id: fetchInteraction
    intent: Get one customer interaction
    question: What is the current state of a particular customer interaction?
  - id: listInteractionChannels
    intent: List channels in an interaction
    question: Which channels has a customer used within one interaction?
  - id: fetchInteractionChannel
    intent: Get one channel of an interaction
    question: What status is a single channel within an interaction in?
  - id: updateInteractionChannel
    intent: Change an interaction channel's status or routing
    question: How do I close out one channel of a customer interaction?
  phrasing_ops: 5
  slug: twilio-interactions-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The IpCommands API from Twilio — 2 operation(s) for ipcommands.
  name: Twilio IpCommands API
  phrasing_intents:
  - id: CreateIpCommand
    intent: Send an IP Command to a Super SIM device
    question: How do I push a small data payload to an IoT device over its Super SIM?
  - id: ListIpCommand
    intent: List IP Commands sent to or from Super SIMs
    question: Which IP Commands have my Super SIM devices sent or received?
  - id: FetchIpCommand
    intent: Look up one IP Command
    question: Was a specific IP Command delivered to the device?
  phrasing_ops: 3
  slug: twilio-ipcommands-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The IpRecords API from Twilio — 2 operation(s) for iprecords.
  name: Twilio IpRecords API
  phrasing_intents:
  - id: CreateIpRecord
    intent: Register an IP address or range
    question: How do I register an IPv4 address or CIDR block with Twilio?
  - id: ListIpRecord
    intent: List registered IP records
    question: Which IP addresses have I registered with my account?
  - id: FetchIpRecord
    intent: Look up one IP record
    question: What address and range does a specific IP record cover?
  - id: UpdateIpRecord
    intent: Rename an IP record
    question: Can I change the label on an IP record without re-registering the address?
  - id: DeleteIpRecord
    intent: Remove an IP record
    question: How do I unregister an IP address we no longer use?
  phrasing_ops: 5
  slug: twilio-iprecords-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage API keys for authentication
  name: Twilio Keys API
  phrasing_intents:
  - id: listKeys
    intent: List API keys
    question: Which API keys exist on my account?
  - id: createKey
    intent: Create an API key
    question: How do I generate a new API key instead of using my auth token?
  - id: fetchKey
    intent: Get one API key
    question: When was a particular API key created and what is it called?
  - id: updateKey
    intent: Rename an API key
    question: Can I relabel an API key so I remember which service uses it?
  - id: deleteKey
    intent: Revoke an API key
    question: How do I revoke an API key that may have leaked?
  phrasing_ops: 5
  slug: twilio-keys-api
- baseURL: https://content.twilio.com
  baseurl_source: declared
  description: The LegacyContent API from Twilio — 1 operation(s) for legacycontent.
  name: Twilio LegacyContent API
  phrasing_intents:
  - id: ListLegacyContent
    intent: List legacy content templates
    question: Which of my older message templates are still stored as legacy content?
  phrasing_ops: 1
  slug: twilio-legacycontent-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The LinkShortening API from Twilio — 5 operation(s) for linkshortening.
  name: Twilio LinkShortening API
  phrasing_intents:
  - id: UpdateDomainCertV4
    intent: Upload a TLS certificate for a short-link domain
    question: How do I upload my own TLS certificate so shortened links work over HTTPS?
  - id: FetchDomainCertV4
    intent: Check the TLS certificate on a short-link domain
    question: Is the TLS certificate on my branded link-shortening domain valid and uploaded?
  - id: DeleteDomainCertV4
    intent: Remove the TLS certificate from a short-link domain
    question: Can I remove the certificate I uploaded for a link-shortening domain?
  - id: UpdateDomainConfig
    intent: Configure fallback, click webhook and HTTPS for a domain
    question: How do I get a webhook every time a recipient clicks a shortened link?
  - id: FetchDomainConfig
    intent: View a short-link domain's configuration
    question: Where do unmatched visits to my short-link domain get redirected?
  - id: FetchDomainConfigMessagingService
    intent: View domain config through a Messaging Service
    question: What link-shortening domain settings apply to a given Messaging Service?
  - id: CreateLinkshorteningMessagingService
    intent: Attach a short-link domain to a Messaging Service
    question: How do I make a Messaging Service shorten links with my branded domain?
  - id: DeleteLinkshorteningMessagingService
    intent: Detach a short-link domain from a Messaging Service
    question: How do I stop a Messaging Service from using my branded short-link domain?
  phrasing_ops: 9
  slug: twilio-linkshortening-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Manage contact lists
  name: Twilio Lists API
  phrasing_intents:
  - id: listContactLists
    intent: List my marketing contact lists
    question: Which marketing contact lists do I have?
  - id: createContactList
    intent: Create a marketing contact list
    question: How do I start a new contact list for a marketing campaign?
  - id: fetchContactList
    intent: Get one marketing contact list
    question: Can I see the details of a single contact list?
  - id: updateContactList
    intent: Rename a marketing contact list
    question: Is there a way to rename an existing contact list?
  - id: deleteContactList
    intent: Delete a marketing contact list
    question: How do I delete a contact list I no longer need?
  phrasing_ops: 5
  slug: twilio-lists-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Send email messages
  name: Twilio Mail Send API
  phrasing_intents:
  - id: sendEmail
    intent: Send an email
    question: How do I send one email to several recipients with personalized fields?
  phrasing_ops: 1
  slug: twilio-mail-send-api
- baseURL: https://preview.twilio.com
  baseurl_source: declared
  description: The Marketplace API from Twilio — 8 operation(s) for marketplace.
  name: Twilio Marketplace API
  phrasing_intents:
  - id: FetchMarketplaceAvailableAddOn
    intent: View an add-on available to install
    question: What does a particular marketplace add-on do before I install it?
  - id: ListMarketplaceAvailableAddOn
    intent: Browse add-ons available in the marketplace
    question: Which add-ons can I install from the marketplace?
  - id: FetchMarketplaceAvailableAddOnExtension
    intent: View one extension of an available add-on
    question: Which product does a specific extension of a marketplace add-on hook into?
  - id: ListMarketplaceAvailableAddOnExtension
    intent: List extensions offered by an available add-on
    question: What extensions come with a marketplace add-on I'm considering?
  - id: CreateMarketplaceInstalledAddOn
    intent: Install a marketplace add-on
    question: How do I install an add-on from the marketplace?
  - id: ListMarketplaceInstalledAddOn
    intent: List add-ons installed on my account
    question: Which marketplace add-ons have I already installed?
  - id: DeleteMarketplaceInstalledAddOn
    intent: Uninstall a marketplace add-on
    question: Can I uninstall an add-on I no longer use?
  - id: FetchMarketplaceInstalledAddOn
    intent: View an installed add-on
    question: What configuration is an installed add-on currently running with?
  phrasing_ops: 12
  slug: twilio-marketplace-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage media attachments for MMS messages
  name: Twilio Media API
  phrasing_intents:
  - id: listMedia
    intent: List media attached to an MMS message
    question: Which images or files came attached to an MMS message?
  - id: fetchMedia
    intent: Fetch one media item from a message
    question: What content type and size is a particular MMS attachment?
  - id: deleteMedia
    intent: Delete a media item from a message
    question: Can I delete a photo someone sent me by MMS so it's no longer stored?
  phrasing_ops: 3
  slug: twilio-media-api
- baseURL: https://media.twilio.com
  baseurl_source: declared
  description: The MediaProcessors API from Twilio — 2 operation(s) for mediaprocessors.
  name: Twilio MediaProcessors API
  phrasing_intents:
  - id: CreateMediaProcessor
    intent: Start a media processor
    question: How do I start a Media Extension like the video composer on a live video room?
  - id: ListMediaProcessor
    intent: List media processors
    question: Which of my media processors have failed?
  - id: FetchMediaProcessor
    intent: Get one media processor
    question: Is a particular media processor still running?
  - id: UpdateMediaProcessor
    intent: Stop a running media processor
    question: How do I end a media processor before its maximum duration?
  phrasing_ops: 4
  slug: twilio-mediaprocessors-api
- baseURL: https://media.twilio.com
  baseurl_source: declared
  description: The MediaRecordings API from Twilio — 2 operation(s) for mediarecordings.
  name: Twilio MediaRecordings API
  phrasing_intents:
  - id: DeleteMediaRecording
    intent: Delete a media recording
    question: How do I permanently remove a media recording?
  - id: FetchMediaRecording
    intent: View a media recording
    question: Has a specific media recording finished processing?
  - id: ListMediaRecording
    intent: List media recordings
    question: Which media recordings failed to process?
  phrasing_ops: 3
  slug: twilio-mediarecordings-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Send and manage SMS and MMS messages
  name: Twilio Messages API
  phrasing_intents:
  - id: listMessages
    intent: List sent and received messages
    question: Which text messages did my account send to a particular phone number?
  - id: createMessage
    intent: Send an SMS or MMS message
    question: How do I send a text message to a customer's phone number with Twilio?
  - id: fetchMessage
    intent: Look up one message
    question: Was a particular text message delivered, and what did it cost?
  - id: updateMessage
    intent: Redact or cancel a message
    question: Can I wipe the body of a sent message so its content is no longer stored?
  - id: deleteMessage
    intent: Delete a message record
    question: Can I remove a message so it no longer shows up in my account logs?
  phrasing_ops: 5
  slug: twilio-messages-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Configure messaging services for scalable messaging
  name: Twilio Messaging Services API
  phrasing_intents:
  - id: listMessagingServices
    intent: List messaging services
    question: Which messaging services exist on my account?
  - id: createMessagingService
    intent: Create a messaging service
    question: How do I set up a messaging service to manage a pool of senders?
  - id: fetchMessagingService
    intent: View a messaging service
    question: What webhooks and sender settings does a given messaging service use?
  - id: updateMessagingService
    intent: Change a messaging service's settings
    question: Can I change the inbound webhook or status callback on an existing messaging service?
  - id: deleteMessagingService
    intent: Delete a messaging service
    question: Can I remove a messaging service I no longer need?
  phrasing_ops: 5
  slug: twilio-messaging-services-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The NetworkAccessProfiles API from Twilio — 4 operation(s) for networkaccessprofiles.
  name: Twilio NetworkAccessProfiles API
  phrasing_intents:
  - id: CreateNetworkAccessProfile
    intent: Create a network access profile
    question: How do I restrict my SIMs to a chosen set of cellular networks?
  - id: ListNetworkAccessProfile
    intent: List network access profiles
    question: Which network access profiles have I set up for my SIMs?
  - id: FetchNetworkAccessProfile
    intent: View a network access profile
    question: What does a particular network access profile look like?
  - id: UpdateNetworkAccessProfile
    intent: Rename a network access profile
    question: Can I change the unique name of an existing network access profile?
  - id: ListNetworkAccessProfileNetwork
    intent: List networks allowed by an access profile
    question: Which cellular networks does a given access profile allow?
  - id: CreateNetworkAccessProfileNetwork
    intent: Allow a network in an access profile
    question: Can I add one more carrier network to an existing access profile?
  - id: DeleteNetworkAccessProfileNetwork
    intent: Remove a network from an access profile
    question: Can I block my SIMs from a carrier by taking it off their access profile?
  - id: FetchNetworkAccessProfileNetwork
    intent: View a network within an access profile
    question: Is a specific network part of my access profile, and what are its details?
  phrasing_ops: 8
  slug: twilio-networkaccessprofiles-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The Networks API from Twilio — 2 operation(s) for networks.
  name: Twilio Networks API
  phrasing_intents:
  - id: FetchNetwork
    intent: Get one cellular network
    question: What country and MCC/MNC codes belong to a specific network resource?
  - id: ListNetwork
    intent: List the cellular networks available
    question: Which cellular networks are listed for a given country?
  phrasing_ops: 2
  slug: twilio-networks-api
- baseURL: https://conversations.twilio.com
  baseurl_source: declared
  description: The ParticipantConversations API from Twilio — 1 operation(s) for participantconversations.
  name: Twilio ParticipantConversations API
  phrasing_intents:
  - id: ListParticipantConversation
    intent: List conversations a participant is in
    question: Which conversations is a given chat user taking part in?
  phrasing_ops: 1
  slug: twilio-participantconversations-api
- baseURL: https://video.twilio.com/v1
  baseurl_source: declared
  description: Manage room participants
  name: Twilio Participants API
  phrasing_intents:
  - id: listParticipants
    intent: List participants who joined a video room
    question: Who has connected to a particular video room?
  - id: fetchParticipant
    intent: Look up one participant in a video room
    question: What details are stored about a single participant in a room?
  - id: updateParticipant
    intent: Disconnect a participant from a video room
    question: Can I remove someone from a video room from my server?
  - id: listPublishedTracks
    intent: List tracks a participant has published
    question: Which audio and video tracks has a participant published to the room?
  - id: fetchSubscribeRules
    intent: Get a participant's subscribe rules
    question: What rules decide which tracks a participant receives?
  - id: updateSubscribeRules
    intent: Control which tracks a participant receives
    question: Can I stop a participant from receiving certain tracks in a room?
  phrasing_ops: 6
  slug: twilio-participants-api
- baseURL: https://lookups.twilio.com/v2
  baseurl_source: declared
  description: Query phone number data and intelligence
  name: Twilio Phone Numbers API
  phrasing_intents:
  - id: fetchPhoneNumber
    intent: Look up information about a phone number
    question: Is this a mobile, landline or VoIP number, and who is the caller?
  - id: listPhoneNumbers
    intent: List phone numbers in a Messaging Service
    question: Which phone numbers are in my Messaging Service sender pool?
  - id: addPhoneNumber
    intent: Add a phone number to a Messaging Service
    question: How do I add one of my numbers to a Messaging Service's sender pool?
  phrasing_ops: 3
  slug: twilio-phone-numbers-api
- baseURL: https://media.twilio.com
  baseurl_source: declared
  description: The PlayerStreamers API from Twilio — 3 operation(s) for playerstreamers.
  name: Twilio PlayerStreamers API
  phrasing_intents:
  - id: FetchPlayerStreamer
    intent: View a live stream player streamer
    question: What state is my live stream's PlayerStreamer in right now?
  - id: UpdatePlayerStreamer
    intent: End a live stream PlayerStreamer
    question: How do I stop a PlayerStreamer that is still live?
  - id: CreatePlayerStreamer
    intent: Create a PlayerStreamer for a live stream
    question: How do I set up a new PlayerStreamer to broadcast a live stream?
  - id: ListPlayerStreamer
    intent: List my PlayerStreamers
    question: Which of my live streams are currently started?
  - id: CreatePlayerStreamerPlaybackGrant
    intent: Issue a playback grant so viewers can watch
    question: How do I give a viewer's player access to watch my live stream?
  - id: FetchPlayerStreamerPlaybackGrant
    intent: Get a PlayerStreamer playback grant
    question: Can I read back the playback grant already issued for a PlayerStreamer?
  phrasing_ops: 6
  slug: twilio-playerstreamers-api
- baseURL: https://flex-api.twilio.com/v1
  baseurl_source: declared
  description: Manage Flex plugins
  name: Twilio Plugins API
  phrasing_intents:
  - id: listPlugins
    intent: List Flex plugins
    question: Which Flex plugins are registered on my account?
  - id: createPlugin
    intent: Register a new Flex plugin
    question: How do I register a new plugin for my Flex agent UI?
  phrasing_ops: 2
  slug: twilio-plugins-api
- baseURL: https://trusthub.twilio.com
  baseurl_source: declared
  description: The Policies API from Twilio — 2 operation(s) for policies.
  name: Twilio Policies API
  phrasing_intents:
  - id: ListPolicies
    intent: List regulatory compliance policies
    question: Which regulatory policies define what a phone number bundle must include?
  - id: FetchPolicies
    intent: Look up one regulatory policy's requirements
    question: What documents and end-user details does a specific regulatory policy require?
  phrasing_ops: 2
  slug: twilio-policies-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage call queues
  name: Twilio Queues API
  phrasing_intents:
  - id: listQueues
    intent: List my call queues
    question: Which call queues are set up on my Twilio account?
  - id: createQueue
    intent: Create a call queue
    question: How do I set up a queue for callers to wait in until an agent is free?
  - id: fetchQueue
    intent: Look up a call queue
    question: How do I check the settings of one specific call queue?
  - id: updateQueue
    intent: Rename or resize a call queue
    question: Can I raise the maximum size of a queue that already exists?
  - id: deleteQueue
    intent: Delete a call queue
    question: How do I remove a call queue I don't use anymore?
  phrasing_ops: 5
  slug: twilio-queues-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Configure rate limiting for verification requests
  name: Twilio Rate Limits API
  phrasing_intents:
  - id: listRateLimits
    intent: List rate limits on a Verify service
    question: Which rate limits have I defined on my Verify service?
  - id: createRateLimit
    intent: Create a rate limit on a Verify service
    question: How do I cap how often verification codes can be requested on my service?
  - id: listBuckets
    intent: List the buckets of a rate limit
    question: What maximums and time intervals are set on one of my rate limits?
  - id: createBucket
    intent: Add a bucket to a rate limit
    question: How do I allow at most a set number of verification requests per time window?
  phrasing_ops: 4
  slug: twilio-rate-limits-api
- baseURL: https://video.twilio.com/v1
  baseurl_source: declared
  description: Manage recording rules for rooms
  name: Twilio Recording Rules API
  phrasing_intents:
  - id: fetchRecordingRules
    intent: See which tracks a video room records
    question: Which participants' tracks are being recorded in my video room right now?
  - id: updateRecordingRules
    intent: Change which tracks a video room records
    question: How do I start recording only audio tracks in a live video room?
  phrasing_ops: 2
  slug: twilio-recording-rules-api
- baseURL: https://video.twilio.com/v1
  baseurl_source: declared
  description: Manage video and audio recordings
  name: Twilio Recordings API
  phrasing_intents:
  - id: listRoomRecordings
    intent: List the recordings made in a video room
    question: Which recordings were captured in a particular video room?
  - id: fetchRecording
    intent: Look up a video recording via the legacy path
    question: Is there an unversioned endpoint that fetches a video recording without an account SID?
  - id: deleteRecording
    intent: Delete a video recording via the legacy path
    question: Can I delete a video recording through the unversioned endpoint without an account SID?
  - id: fetchRecordingSettings
    intent: View my default recording storage settings
    question: Are my video recordings being stored in my own S3 bucket?
  - id: createRecordingSettings
    intent: Configure where and how recordings are stored
    question: Can I send recordings straight to my own S3 bucket instead of keeping them hosted?
  - id: listCallRecordings
    intent: List the recordings of one call
    question: Which recordings were made during a specific phone call?
  - id: createCallRecording
    intent: Start recording a call in progress
    question: Can I start recording a phone call that is already underway?
  - id: listRecordings
    intent: List all call recordings on an account
    question: What call recordings does my account hold overall?
  phrasing_ops: 13
  slug: twilio-recordings-api
- baseURL: https://numbers.twilio.com
  baseurl_source: declared
  description: The RegulatoryCompliance API from Twilio — 18 operation(s) for regulatorycompliance.
  name: Twilio RegulatoryCompliance API
  phrasing_intents:
  - id: CreateBundle
    intent: Create a regulatory compliance bundle
    question: How do I start a regulatory bundle so I can buy phone numbers in a regulated country?
  - id: ListBundle
    intent: List regulatory compliance bundles
    question: Which of my regulatory bundles are still waiting on review or were rejected?
  - id: FetchBundle
    intent: Get one regulatory bundle
    question: What is the current review status of one particular regulatory bundle?
  - id: UpdateBundle
    intent: Update or submit a regulatory bundle
    question: How do I submit a draft regulatory bundle for review once it is complete?
  - id: DeleteBundle
    intent: Delete a regulatory bundle
    question: Can I permanently remove a regulatory bundle I no longer need?
  - id: CreateBundleCopy
    intent: Copy a regulatory bundle
    question: Can I duplicate an approved regulatory bundle along with its identities and documents?
  - id: ListBundleCopy
    intent: List copies made of a bundle
    question: Which copies have been made from one of my regulatory bundles?
  - id: CreateEndUser
    intent: Register a compliance end user
    question: How do I add the business or person who will own a regulated phone number?
  phrasing_ops: 31
  slug: twilio-regulatorycompliance-api
- baseURL: https://conversations.twilio.com
  baseurl_source: declared
  description: The Roles API from Twilio — 2 operation(s) for roles.
  name: Twilio Roles API
  phrasing_intents:
  - id: CreateRole
    intent: Create a user role with permissions
    question: How do I define a new role that limits what users can do in conversations?
  - id: ListRole
    intent: List user roles
    question: Which user roles are defined in my default conversations service?
  - id: UpdateRole
    intent: Change a role's permissions
    question: Can I change the permissions on a role that already exists?
  - id: DeleteRole
    intent: Delete a user role
    question: Can I remove a role I no longer use from my service?
  - id: FetchRole
    intent: View a user role
    question: What permissions does a particular role grant?
  phrasing_ops: 5
  slug: twilio-roles-api
- baseURL: https://video.twilio.com/v1
  baseurl_source: declared
  description: Create and manage video rooms
  name: Twilio Rooms API
  phrasing_intents:
  - id: listRooms
    intent: List video rooms (older unversioned endpoint)
    question: Which video rooms are on my account, using the older unversioned Rooms list?
  - id: createRoom
    intent: Create a video room (older unversioned endpoint)
    question: Can I pick between group, small group and peer-to-peer when creating a room on the older unversioned endpoint?
  - id: fetchRoom
    intent: Look up a video room (older unversioned endpoint)
    question: Can I look up a room by its unique name instead of its SID on the older unversioned endpoint?
  - id: updateRoom
    intent: End an in-progress video room (older unversioned endpoint)
    question: Can I force a live video call to end through the older unversioned Rooms endpoint?
  - id: FetchRoom
    intent: Fetch a video room by SID (v1)
    question: What does the v1 Rooms API return when I fetch a single room by its SID?
  - id: UpdateRoom
    intent: Complete a video room (v1)
    question: Can I mark a room completed through the v1 Rooms API to kick everyone out?
  - id: CreateRoom
    intent: Create a video room with recording rules (v1)
    question: Can I set recording rules or make a large room when creating a room on v1?
  - id: ListRoom
    intent: List video rooms (v1)
    question: Can the v1 room list show only completed rooms instead of in-progress ones?
  phrasing_ops: 23
  slug: twilio-rooms-api
- baseURL: https://accounts.twilio.com
  baseurl_source: declared
  description: The SafeList API from Twilio — 5 operation(s) for safelist.
  name: Twilio SafeList API
  phrasing_intents:
  - id: CreateSafelist
    intent: Add a phone number to SafeList (v1 endpoint)
    question: Is the v1 SafeList endpoint still usable for adding a number?
  - id: FetchSafelist
    intent: Check a number on SafeList (v1 endpoint)
    question: On the v1 SafeList endpoint, where the number goes in the query string, is a phone number safelisted?
  - id: DeleteSafelist
    intent: Remove a phone number from SafeList (v1 endpoint)
    question: On the v1 SafeList endpoint, how do I remove a number passed as a query parameter?
  - id: createSafelistNumber
    intent: Safelist a number (legacy unversioned endpoint)
    question: On the older unversioned path, how do I add a verified caller ID to the account safelist?
  - id: fetchSafelistNumber
    intent: Check a safelisted number (legacy endpoint)
    question: Through the older unversioned path, is a number on the safelist?
  - id: deleteSafelistNumber
    intent: Unsafelist a number (legacy unversioned endpoint)
    question: Through the older unversioned path, how do I remove a number from the safelist?
  - id: postV2SafeListNumbers
    intent: Add a phone number to SafeList
    question: How do I protect one of my own numbers from being blocked by fraud guard?
  - id: getV2SafeListNumbersByPhoneNumber
    intent: Check whether a number is on SafeList
    question: Is a given phone number already on my v2 SafeList?
  phrasing_ops: 9
  slug: twilio-safelist-api
- baseURL: https://events.twilio.com
  baseurl_source: declared
  description: The Schemas API from Twilio — 3 operation(s) for schemas.
  name: Twilio Schemas API
  phrasing_intents:
  - id: FetchSchema
    intent: Get an event schema and its versions
    question: What does the payload of a given event type look like, and which versions exist?
  - id: ListSchemaVersion
    intent: List the versions of an event schema
    question: How many versions of an event schema have been published?
  - id: FetchSchemaVersion
    intent: Get one specific version of an event schema
    question: Can I pull the exact definition of an older version of an event schema?
  phrasing_ops: 3
  slug: twilio-schemas-api
- baseURL: https://microvisor.twilio.com
  baseurl_source: declared
  description: The Secrets API from Twilio — 2 operation(s) for secrets.
  name: Twilio Secrets API
  phrasing_intents:
  - id: ListAccountSecret
    intent: List the secrets stored on my account
    question: Which secrets have I stored at the account level?
  - id: CreateAccountSecret
    intent: Store a new account secret
    question: Can I store an API key or password as an account-level secret?
  - id: FetchAccountSecret
    intent: Look up one account secret by key
    question: Can I retrieve a single secret by its key name?
  - id: UpdateAccountSecret
    intent: Change the value of an account secret
    question: Can I rotate the value of an existing secret without renaming it?
  - id: DeleteAccountSecret
    intent: Delete an account secret
    question: Can I permanently remove a secret I no longer use?
  phrasing_ops: 5
  slug: twilio-secrets-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Manage verified sender identities
  name: Twilio Senders API
  phrasing_intents:
  - id: listVerifiedSenders
    intent: List verified email senders
    question: Which from-addresses have I verified for sending email?
  - id: createVerifiedSender
    intent: Add a verified email sender
    question: How do I register a new from-address so I can send email from it?
  phrasing_ops: 2
  slug: twilio-senders-api
- baseURL: https://conversations.twilio.com
  baseurl_source: declared
  description: The Services API from Twilio — 131 operation(s) for services.
  name: Twilio Services API
  phrasing_intents:
  - id: CreateService
    intent: Create a Conversations service (v1)
    question: Can I create a separate conversation service to isolate one app's data?
  - id: ListService
    intent: List Conversations services (v1)
    question: Which conversation services are set up on my account under the v1 Services endpoint?
  - id: DeleteService
    intent: Delete a Conversations service (v1)
    question: Can I delete a conversation service together with all its conversations and users?
  - id: FetchService
    intent: Get a Conversations service (v1)
    question: Can I look up one conversation service by its SID on the v1 endpoint?
  - id: UpdateService
    intent: Update a v1 service's messaging settings
    question: Can I turn on Sticky Sender or Smart Encoding on a v1 service?
  - id: DeleteServiceBinding
    intent: Remove a push binding from a Conversations service
    question: How can I stop push notifications reaching a device that left my Conversations app?
  - id: FetchServiceBinding
    intent: Get a push binding in a Conversations service
    question: Can I look up one device push registration in my Conversations service?
  - id: ListServiceBinding
    intent: List push bindings in a Conversations service
    question: Which devices are registered for push in my Conversations service?
  phrasing_ops: 265
  slug: twilio-services-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The Settings API from Twilio — 1 operation(s) for settings.
  name: Twilio Settings API
  phrasing_intents:
  - id: FetchDialingPermissionsSettings
    intent: Check a sub-account's dialing permission inheritance
    question: Does this sub-account inherit voice dialing permissions from the parent project?
  - id: UpdateDialingPermissionsSettings
    intent: Set a sub-account's dialing permission inheritance
    question: Can I stop a sub-account from inheriting the master project's voice dialing permissions?
  phrasing_ops: 2
  slug: twilio-settings-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The SettingsUpdates API from Twilio — 1 operation(s) for settingsupdates.
  name: Twilio SettingsUpdates API
  phrasing_intents:
  - id: ListSettingsUpdate
    intent: List Super SIM settings updates
    question: Has the settings update pushed to my Super SIM finished successfully?
  phrasing_ops: 1
  slug: twilio-settingsupdates-api
- baseURL: https://api.twilio.com/2010-04-01
  baseurl_source: declared
  description: Manage short codes for messaging services
  name: Twilio Short Codes API
  phrasing_intents:
  - id: listShortCodes
    intent: List short codes on a Messaging Service
    question: Which short codes are in my Messaging Service's sender pool?
  - id: addShortCode
    intent: Add a short code to a Messaging Service
    question: How do I add my approved short code to a Messaging Service?
  phrasing_ops: 2
  slug: twilio-short-codes-api
- baseURL: https://events.twilio.com
  baseurl_source: declared
  description: The Sinks API from Twilio — 4 operation(s) for sinks.
  name: Twilio Sinks API
  phrasing_intents:
  - id: FetchSink
    intent: Get one event streams sink
    question: What type and status does a specific event sink have?
  - id: DeleteSink
    intent: Delete a sink
    question: How do I get rid of an event streams destination I no longer use?
  - id: UpdateSink
    intent: Rename a sink
    question: How do I change the description on an existing event sink?
  - id: CreateSink
    intent: Create an event streams sink
    question: How do I send event stream data to a destination of my own?
  - id: ListSink
    intent: List my event streams sinks
    question: Which of my event sinks have failed validation?
  - id: CreateSinkTest
    intent: Send a test event to a sink
    question: How do I check that my sink can actually receive events?
  - id: CreateSinkValidate
    intent: Confirm a sink received its test event
    question: Once the test event arrives, how do I mark my sink as validated?
  phrasing_ops: 7
  slug: twilio-sinks-api
- baseURL: https://routes.twilio.com
  baseurl_source: declared
  description: The SipDomains API from Twilio — 1 operation(s) for sipdomains.
  name: Twilio SipDomains API
  phrasing_intents:
  - id: UpdateSipDomain
    intent: Change a SIP domain's voice region
    question: Can I move my SIP domain's calls to a different voice region?
  - id: FetchSipDomain
    intent: Look up a SIP domain's routing
    question: Which voice region is my SIP domain routed through?
  phrasing_ops: 2
  slug: twilio-sipdomains-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The SmsCommands API from Twilio — 2 operation(s) for smscommands.
  name: Twilio SmsCommands API
  phrasing_intents:
  - id: CreateSmsCommand
    intent: Send an SMS command to a SIM
    question: How do I send a machine-to-machine text command to an IoT device's SIM?
  - id: ListSmsCommand
    intent: List SMS commands for Super SIMs
    question: Which SMS commands have been sent to or received from a particular Super SIM?
  - id: FetchSmsCommand
    intent: Get one SMS command
    question: Was a specific SMS command delivered to the device?
  phrasing_ops: 3
  slug: twilio-smscommands-api
- baseURL: https://voice.twilio.com
  baseurl_source: declared
  description: The SourceIpMappings API from Twilio — 2 operation(s) for sourceipmappings.
  name: Twilio SourceIpMappings API
  phrasing_intents:
  - id: CreateSourceIpMapping
    intent: Map an IP record to a SIP domain
    question: How do I tie traffic from a known IP address to one of my SIP domains?
  - id: ListSourceIpMapping
    intent: List source IP mappings
    question: Which IP records are mapped to which SIP domains on my account?
  - id: FetchSourceIpMapping
    intent: View a source IP mapping
    question: Which SIP domain does a particular source IP mapping point at?
  - id: UpdateSourceIpMapping
    intent: Point a source IP mapping at a new SIP domain
    question: Can I move an existing IP mapping over to a different SIP domain?
  - id: DeleteSourceIpMapping
    intent: Delete a source IP mapping
    question: How do I stop an IP record from being mapped to a SIP domain?
  phrasing_ops: 5
  slug: twilio-sourceipmappings-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Retrieve email analytics and statistics
  name: Twilio Stats API
  phrasing_intents:
  - id: fetchGlobalStats
    intent: Get aggregate email delivery statistics
    question: How many of my emails were delivered, opened and clicked last month?
  phrasing_ops: 1
  slug: twilio-stats-api
- baseURL: https://events.twilio.com
  baseurl_source: declared
  description: The Subscriptions API from Twilio — 4 operation(s) for subscriptions.
  name: Twilio Subscriptions API
  phrasing_intents:
  - id: ListSubscribedEvent
    intent: List the event types in a subscription
    question: Which event types is one of my Event Streams subscriptions receiving?
  - id: CreateSubscribedEvent
    intent: Add an event type to a subscription
    question: How do I start receiving one more event type on a subscription I already have?
  - id: FetchSubscribedEvent
    intent: Check one event type on a subscription
    question: Is a particular event type included in my subscription, and on which schema version?
  - id: UpdateSubscribedEvent
    intent: Change a subscribed event's schema version
    question: Can I move an event type I'm already subscribed to onto a newer schema version?
  - id: DeleteSubscribedEvent
    intent: Remove an event type from a subscription
    question: How do I stop getting one event type without deleting the whole subscription?
  - id: ListSubscription
    intent: List my event subscriptions
    question: What Event Streams subscriptions exist on my Twilio account?
  - id: CreateSubscription
    intent: Create an event subscription
    question: How do I route selected account events to a sink I've set up?
  - id: FetchSubscription
    intent: Look up an event subscription
    question: How can I see which sink one of my subscriptions points at?
  phrasing_ops: 10
  slug: twilio-subscriptions-api
- baseURL: https://trusthub.twilio.com
  baseurl_source: declared
  description: The SupportingDocuments API from Twilio — 2 operation(s) for supportingdocuments.
  name: Twilio SupportingDocuments API
  phrasing_intents:
  - id: CreateSupportingDocument
    intent: Add a supporting document
    question: How do I submit a business document for Trust Hub compliance review?
  - id: ListSupportingDocument
    intent: List my Trust Hub supporting documents
    question: Which compliance documents have I uploaded to Trust Hub?
  - id: FetchSupportingDocument
    intent: Look up a supporting document
    question: What's the review status of a compliance document I submitted?
  - id: UpdateSupportingDocument
    intent: Update a supporting document
    question: Can I correct the attributes on a supporting document I already submitted?
  - id: DeleteSupportingDocument
    intent: Delete a supporting document
    question: How do I remove an outdated compliance document from Trust Hub?
  phrasing_ops: 5
  slug: twilio-supportingdocuments-api
- baseURL: https://trusthub.twilio.com
  baseurl_source: declared
  description: The SupportingDocumentTypes API from Twilio — 2 operation(s) for supportingdocumenttypes.
  name: Twilio SupportingDocumentTypes API
  phrasing_intents:
  - id: ListSupportingDocumentType
    intent: List the supporting document types accepted
    question: What kinds of supporting documents does Trust Hub accept?
  - id: FetchSupportingDocumentType
    intent: Look up one supporting document type
    question: Which fields does a particular supporting document type require?
  phrasing_ops: 2
  slug: twilio-supportingdocumenttypes-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Manage email suppressions and bounces
  name: Twilio Suppressions API
  phrasing_intents:
  - id: listBounces
    intent: List email addresses that bounced
    question: Which email addresses have bounced my messages recently?
  - id: deleteBounces
    intent: Clear addresses from the bounce list
    question: Can I remove a fixed address from my bounce list so mail reaches it again?
  - id: listBlocks
    intent: List email addresses that are blocked
    question: Which recipients' mail servers have blocked my email?
  - id: listGlobalUnsubscribes
    intent: List globally unsubscribed recipients
    question: Who has unsubscribed from all of my email?
  phrasing_ops: 4
  slug: twilio-suppressions-api
- baseURL: https://api.sendgrid.com/v3
  baseurl_source: declared
  description: Manage dynamic email templates
  name: Twilio Templates API
  phrasing_intents:
  - id: listTemplates
    intent: List my email templates
    question: Which transactional email templates do I have?
  - id: createTemplate
    intent: Create an email template
    question: How do I create a new transactional email template?
  - id: fetchTemplate
    intent: Look up an email template
    question: How can I see the details and versions of one email template?
  - id: updateTemplate
    intent: Rename an email template
    question: Can I rename an email template after it's created?
  - id: deleteTemplate
    intent: Delete an email template
    question: How do I delete an email template I no longer send?
  - id: createTemplateVersion
    intent: Add a version to an email template
    question: How do I add new HTML content and a subject line to an email template?
  - id: ListVerificationTemplate
    intent: List Verify message templates
    question: What message templates are available for my verification codes?
  phrasing_ops: 7
  slug: twilio-templates-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Tollfree API from Twilio — 2 operation(s) for tollfree.
  name: Twilio Tollfree API
  phrasing_intents:
  - id: FetchTollfreeVerification
    intent: Get one toll-free verification
    question: Has my toll-free number's verification been approved yet?
  - id: UpdateTollfreeVerification
    intent: Edit a toll-free verification request
    question: My toll-free verification was rejected because the website was down; can I edit and resubmit it?
  - id: DeleteTollfreeVerification
    intent: Delete a toll-free verification
    question: Can I withdraw a toll-free verification request entirely?
  - id: ListTollfreeVerification
    intent: List toll-free verifications
    question: Which of my toll-free numbers are still waiting on verification?
  - id: CreateTollfreeVerification
    intent: Submit a toll-free number for verification
    question: How do I get my toll-free number verified so I can send text messages from it?
  phrasing_ops: 5
  slug: twilio-tollfree-api
- baseURL: https://intelligence.twilio.com
  baseurl_source: declared
  description: The Transcripts API from Twilio — 6 operation(s) for transcripts.
  name: Twilio Transcripts API
  phrasing_intents:
  - id: FetchMedia
    intent: Get download links for a transcript's recording
    question: Where can I download the audio behind a Voice Intelligence transcript?
  - id: ListOperatorResult
    intent: List all language-operator results for a transcript
    question: What did all the language understanding operators find in one transcript?
  - id: FetchOperatorResult
    intent: Get one operator's result for a transcript
    question: What did one specific operator, like my custom classifier, return for a transcript?
  - id: ListSentence
    intent: Read the sentences of a transcript
    question: How do I get the actual text of a call, sentence by sentence?
  - id: CreateTranscript
    intent: Transcribe a recording into a new transcript
    question: How do I send a call recording to Twilio Voice Intelligence for transcription?
  - id: ListTranscript
    intent: Search transcripts in a Voice Intelligence service
    question: Which transcripts has my Voice Intelligence service produced this week?
  - id: FetchTranscript
    intent: Look up one transcript
    question: What is the processing status of a single transcript?
  - id: DeleteTranscript
    intent: Delete a transcript
    question: How do I permanently delete a call transcript for privacy reasons?
  phrasing_ops: 8
  slug: twilio-transcripts-api
- baseURL: https://pricing.twilio.com
  baseurl_source: declared
  description: The Trunking API from Twilio — 3 operation(s) for trunking.
  name: Twilio Trunking API
  phrasing_intents:
  - id: ListTrunkingCountry
    intent: List countries with SIP trunking pricing
    question: Which countries have Elastic SIP Trunking pricing published?
  - id: FetchTrunkingCountry
    intent: Get SIP trunking prices for a country
    question: What does it cost to terminate trunking calls in a specific country?
  - id: FetchTrunkingNumber
    intent: Get the trunking price to call a number
    question: How much will a trunked call to a specific phone number cost?
  phrasing_ops: 3
  slug: twilio-trunking-api
- baseURL: https://routes.twilio.com
  baseurl_source: declared
  description: The Trunks API from Twilio — 12 operation(s) for trunks.
  name: Twilio Trunks API
  phrasing_intents:
  - id: UpdateTrunks
    intent: Assign an inbound processing region to a SIP trunk
    question: How do I move a SIP trunk domain's inbound voice processing to a different region?
  - id: FetchTrunks
    intent: See which inbound processing region a SIP trunk uses
    question: Which inbound processing region is my SIP trunk domain assigned to?
  - id: FetchCredentialList
    intent: Get one credential list attached to a trunk
    question: Can I see the details of a specific credential list attached to my SIP trunk?
  - id: DeleteCredentialList
    intent: Detach a credential list from a trunk
    question: How do I stop a credential list from authenticating calls on my SIP trunk?
  - id: CreateCredentialList
    intent: Attach a credential list to a trunk
    question: How do I require SIP credentials for calls coming into my trunk?
  - id: ListCredentialList
    intent: List the credential lists on a trunk
    question: Which credential lists are protecting my SIP trunk right now?
  - id: FetchIpAccessControlList
    intent: Get one IP access control list on a trunk
    question: Can I look up a single IP access control list associated with my trunk?
  - id: DeleteIpAccessControlList
    intent: Remove an IP access control list from a trunk
    question: How do I stop an IP allowlist from applying to my SIP trunk?
  phrasing_ops: 26
  slug: twilio-trunks-api
- baseURL: https://trusthub.twilio.com
  baseurl_source: declared
  description: The TrustProducts API from Twilio — 8 operation(s) for trustproducts.
  name: Twilio TrustProducts API
  phrasing_intents:
  - id: CreateTrustProduct
    intent: Create a trust product
    question: How do I start a new trust product under a specific policy?
  - id: ListTrustProduct
    intent: List trust products
    question: Which of my trust products are approved and which are still in review?
  - id: FetchTrustProduct
    intent: Get one trust product
    question: What is the verification status of one particular trust product?
  - id: UpdateTrustProduct
    intent: Update or submit a trust product
    question: How do I submit a finished trust product for review?
  - id: DeleteTrustProduct
    intent: Delete a trust product
    question: Can I permanently remove a trust product I no longer need?
  - id: CreateTrustProductChannelEndpointAssignment
    intent: Assign a phone number to a trust product
    question: How do I attach a phone number to an approved trust product?
  - id: ListTrustProductChannelEndpointAssignment
    intent: List phone numbers assigned to a trust product
    question: Which phone numbers or channel endpoints are covered by my trust product?
  - id: FetchTrustProductChannelEndpointAssignment
    intent: Get one phone number assignment
    question: Can I look up a single channel endpoint assignment on a trust product?
  phrasing_ops: 16
  slug: twilio-trustproducts-api
- baseURL: https://events.twilio.com
  baseurl_source: declared
  description: The Types API from Twilio — 2 operation(s) for types.
  name: Twilio Types API
  phrasing_intents:
  - id: ListEventType
    intent: List available Event Streams event types
    question: What event types can I subscribe to with Event Streams?
  - id: FetchEventType
    intent: Look up one event type
    question: What does a specific event type describe and which schema does it follow?
  phrasing_ops: 2
  slug: twilio-types-api
- baseURL: https://preview.twilio.com
  baseurl_source: declared
  description: The Understand API from Twilio — 21 operation(s) for understand.
  name: Twilio Understand API
  phrasing_intents:
  - id: FetchUnderstandAssistant
    intent: View an Understand assistant
    question: What name, callback URL and query logging setting does my Understand assistant have?
  - id: UpdateUnderstandAssistant
    intent: Change an Understand assistant's settings
    question: Can I turn off query logging on my assistant so user input isn't stored?
  - id: DeleteUnderstandAssistant
    intent: Delete an Understand assistant
    question: How do I get rid of an assistant I no longer use?
  - id: FetchUnderstandAssistantFallbackActions
    intent: See what an assistant does when it doesn't understand
    question: What does my assistant say when user input matches no task?
  - id: UpdateUnderstandAssistantFallbackActions
    intent: Set an assistant's fallback actions
    question: How do I change the reply an assistant gives when it can't match any task?
  - id: FetchUnderstandAssistantInitiationActions
    intent: See an assistant's opening actions on calls
    question: What does my assistant say first when it answers an inbound phone call?
  - id: UpdateUnderstandAssistantInitiationActions
    intent: Set an assistant's opening actions on calls
    question: Can I change what my assistant says first on an inbound call?
  - id: FetchUnderstandDialogue
    intent: View a dialogue with an assistant
    question: What happened in a specific conversation between a user and my assistant?
  phrasing_ops: 46
  slug: twilio-understand-api
- baseURL: https://conversations.twilio.com
  baseurl_source: declared
  description: The Users API from Twilio — 4 operation(s) for users.
  name: Twilio Users API
  phrasing_intents:
  - id: CreateUser
    intent: Add a conversation user
    question: How do I create a chat user with my own application identity?
  - id: ListUser
    intent: List conversation users
    question: Which users exist in my default Conversations service?
  - id: UpdateUser
    intent: Update a conversation user
    question: Can I change the role of an existing conversation user?
  - id: DeleteUser
    intent: Remove a conversation user
    question: How can I delete a chat user from my default service?
  - id: FetchUser
    intent: Get one conversation user
    question: What attributes and role does a particular chat user have?
  - id: UpdateUserConversation
    intent: Update a user's settings in a conversation
    question: Can I mute notifications for a user in one conversation?
  - id: DeleteUserConversation
    intent: Remove a user from a conversation
    question: How do I take a user out of one conversation without deleting the user?
  - id: FetchUserConversation
    intent: Get a user's view of one conversation
    question: How many unread messages does a user have in a specific conversation?
  phrasing_ops: 9
  slug: twilio-users-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Check verification codes
  name: Twilio Verification Checks API
  phrasing_intents:
  - id: createVerificationCheck
    intent: Check a user's verification code
    question: How do I confirm the one-time code a user typed in is correct?
  phrasing_ops: 1
  slug: twilio-verification-checks-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Send and manage verification codes
  name: Twilio Verifications API
  phrasing_intents:
  - id: createVerification
    intent: Send a verification code
    question: How do I text a one-time passcode to a user to confirm their phone number?
  - id: fetchVerification
    intent: Check a verification's status
    question: Is a verification I started still pending or already approved?
  - id: updateVerification
    intent: Cancel or approve a pending verification
    question: How do I cancel a verification code I sent so it can't be used?
  phrasing_ops: 3
  slug: twilio-verifications-api
- baseURL: https://insights.twilio.com
  baseurl_source: declared
  description: The Video API from Twilio — 4 operation(s) for video.
  name: Twilio Video API
  phrasing_intents:
  - id: FetchVideoParticipantSummary
    intent: Get call-quality analysis for a room participant
    question: What did the Video Log Analyzer record about one participant's session?
  - id: ListVideoParticipantSummary
    intent: List participant summaries for a room
    question: Which participants does the Log Analyzer have data for in a given room?
  - id: FetchVideoRoomSummary
    intent: Get call-quality analysis for a room
    question: What does the Video Log Analyzer say about how a room performed?
  - id: ListVideoRoomSummary
    intent: List room summaries from the Log Analyzer
    question: Which peer-to-peer or group rooms ran in a given time window, according to the Log Analyzer?
  phrasing_ops: 4
  slug: twilio-video-api
- baseURL: https://insights.twilio.com
  baseurl_source: declared
  description: The Voice API from Twilio — 10 operation(s) for voice.
  name: Twilio Voice API
  phrasing_intents:
  - id: FetchAccountSettings
    intent: Check Voice Insights settings
    question: Is Voice Insights Advanced Features turned on for my account?
  - id: UpdateAccountSettings
    intent: Change Voice Insights settings
    question: How do I switch on Voice Insights Advanced Features?
  - id: UpdateAnnotation
    intent: Annotate a call with feedback
    question: How do I mark a call as spam in Voice Insights?
  - id: FetchAnnotation
    intent: Read the annotation on a call
    question: What feedback did we record against a particular call, like its score or quality issues?
  - id: FetchCall
    intent: Look up a call in Voice Insights
    question: Can I pull up the Voice Insights record for a single call by its SID?
  - id: ListCallSummaries
    intent: Search call summaries across my account
    question: Which of my calls in the last day had dropped-call or echo problems?
  - id: ListEvent
    intent: List signaling events for a call
    question: What events happened during a call, step by step?
  - id: ListMetric
    intent: List quality metrics for a call
    question: Where do I get jitter and packet loss style metrics for a single call?
  phrasing_ops: 12
  slug: twilio-voice-api
- baseURL: https://flex-api.twilio.com/v1
  baseurl_source: declared
  description: Manage web chat channels
  name: Twilio Web Channels API
  phrasing_intents:
  - id: createWebChannel
    intent: Start a Flex web chat channel for a customer
    question: How do I open a new Flex web chat for a customer from my own site?
  - id: fetchWebChannel
    intent: Look up a Flex web chat channel
    question: Can I pull up the details of one web chat channel?
  - id: updateWebChannel
    intent: Update the status of a web chat channel
    question: Can I mark a web chat as inactive once the customer leaves?
  - id: deleteWebChannel
    intent: Delete a Flex web chat channel
    question: Can I delete a web chat channel after the conversation is over?
  phrasing_ops: 4
  slug: twilio-web-channels-api
- baseURL: https://verify.twilio.com/v2
  baseurl_source: declared
  description: Configure event webhooks
  name: Twilio Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List a Verify service's webhooks
    question: Which webhooks are registered on my Verify service?
  - id: createWebhook
    intent: Add a webhook to a Verify service
    question: How do I get notified at my own URL when verification events happen?
  phrasing_ops: 2
  slug: twilio-webhooks-api
- baseURL: https://taskrouter.twilio.com
  baseurl_source: declared
  description: The Workspaces API from Twilio — 36 operation(s) for workspaces.
  name: Twilio Workspaces API
  phrasing_intents:
  - id: FetchActivity
    intent: Look up one worker activity state
    question: What are the details of a single TaskRouter activity like Offline or Break?
  - id: UpdateActivity
    intent: Rename a worker activity
    question: Can I rename an existing TaskRouter activity without recreating it?
  - id: DeleteActivity
    intent: Delete a worker activity
    question: How do I remove an activity state my agents no longer use?
  - id: ListActivity
    intent: List the activity states in a workspace
    question: Which activity states are defined in my TaskRouter workspace?
  - id: CreateActivity
    intent: Create a new worker activity state
    question: How do I add a new agent status like Lunch to my TaskRouter workspace?
  - id: FetchEvent
    intent: Look up a single workspace event
    question: What exactly happened in one specific TaskRouter event?
  - id: ListEvent
    intent: Browse the event history of a workspace
    question: Where can I see the audit trail of what happened to tasks and workers in a workspace?
  - id: FetchTask
    intent: Look up one routed task
    question: What is the current status and priority of a specific task in TaskRouter?
  phrasing_ops: 60
  slug: twilio-workspaces-api
- baseURL: https://supersim.twilio.com
  baseurl_source: declared
  description: The Sims API from Twilio — 6 operation(s) for sims.
  name: Twilio Sims API
  phrasing_intents:
  - id: ListBillingPeriod
    intent: List a Super SIM's billing periods
    question: How do I see the billing periods a Super SIM has been charged for?
  - id: CreateSim
    intent: Register a Super SIM to my account
    question: How do I claim a new Super SIM card I just received?
  - id: ListSim
    intent: List my Super SIMs
    question: Which of my Super SIMs are active right now?
  - id: FetchSim
    intent: Look up a Super SIM
    question: How do I check the status and fleet of one Super SIM?
  - id: UpdateSim
    intent: Activate, move or rename a Super SIM
    question: Can I activate or deactivate a Super SIM remotely?
  - id: DeleteSim
    intent: Delete a SIM from my account
    question: How do I remove a SIM resource from my account entirely?
  - id: ListSimIpAddress
    intent: List a Super SIM's IP addresses
    question: What IP address has my Super SIM been assigned?
  - id: ListDataSession
    intent: List a SIM's data sessions
    question: When did my wireless SIM last open a data connection?
  phrasing_ops: 9
  slug: twilio-sims-api
- baseURL: https://knowledge.twilio.com
  baseurl_source: declared
  description: 'Enterprise Knowledge v2: knowledge bases (control plane), knowledge sources, chunks, search and long-running operations that feed grounded answers to Twilio conversational AI.'
  name: Twilio Enterprise Knowledge API
  slug: twilio-enterprise-knowledge-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The ChatV3Channel API from Twilio — 1 operation(s) for chatv3channel.
  name: Twilio Chat V3Channel API
  slug: twilio-chatv3channel-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Define and manage intelligence configuration. The Configurations resource defines how and when language operators execute on conversations via rules that encapsulate triggers, context, and actions. An
  name: Twilio Configurations API
  slug: twilio-configurations-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The ContentV2Content API from Twilio — 1 operation(s) for contentv2content.
  name: Twilio Content V2Content API
  slug: twilio-contentv2content-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The ContentV2ContentAndApprovals API from Twilio — 1 operation(s) for contentv2contentandapprovals.
  name: Twilio Content V2Content And Approvals API
  slug: twilio-contentv2contentandapprovals-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: 'Conversation summaries are high-level recaps automatically generated from conversations that run through Conversation Orchestrator. Like observations, they are created when a conversation reaches the '
  name: Twilio Conversation Summaries API
  slug: twilio-conversationsummaries-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: 'A Data Mapping connects an external data source to a Memory Store by mapping fields from the data source to Traits in a Trait Group. This allows for the enrichment of profiles with data from external '
  name: Twilio Data Mapping API
  slug: twilio-datamapping-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The IamV1ApiKey API from Twilio — 1 operation(s) for iamv1apikey.
  name: Twilio Iam V1Api Key API
  slug: twilio-iamv1apikey-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The IamV1GetApiKeys API from Twilio — 1 operation(s) for iamv1getapikeys.
  name: Twilio Iam V1Get API Keys API
  slug: twilio-iamv1getapikeys-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The IamV1NewApiKey API from Twilio — 1 operation(s) for iamv1newapikey.
  name: Twilio Iam V1New API Key API
  slug: twilio-iamv1newapikey-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The IamV1RolePermission API from Twilio — 1 operation(s) for iamv1rolepermission.
  name: Twilio Iam V1Role Permission API
  slug: twilio-iamv1rolepermission-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Every customer interaction must be attached to the correct profile. Conversation Memory manages this through Identifiers which are normalized, unique values like phone numbers or email addresses. When
  name: Twilio Identifiers API
  slug: twilio-identifiers-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Identity Resolution Settings endpoints allow you to define and manage the logic used to identify, merge, and resolve customer profiles within a specific Memory Store. These settings ensure that in
  name: Twilio Identity Resolution Settings API
  slug: twilio-identityresolutionsettings-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The KnowledgeBases API from Twilio — 2 operation(s) for knowledgebases.
  name: Twilio Knowledge Bases API
  slug: twilio-knowledgebases-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Send typing indicators to OTT channel recipients (WhatsApp, Apple Messages for Business, RCS).
  name: Twilio Messaging V3Typing Indicator API
  slug: twilio-messagingv3typingindicator-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The NumbersV3HostedNumbersHostedNumberOrder API from Twilio — 1 operation(s) for numbersv3hostednumbershostednumberorder.
  name: Twilio Numbers V3Hosted Numbers Hosted Number Order API
  slug: twilio-numbersv3hostednumbershostednumberorder-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Oauth2 API from Twilio — 2 operation(s) for oauth2.
  name: Twilio Oauth2 API
  slug: twilio-oauth2-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The OauthV1Authorize API from Twilio — 1 operation(s) for oauthv1authorize.
  name: Twilio OAUTH V1Authorize API
  slug: twilio-oauthv1authorize-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The OauthV1Token API from Twilio — 1 operation(s) for oauthv1token.
  name: Twilio OAUTH V1Token API
  slug: twilio-oauthv1token-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The OauthV2Authorize API from Twilio — 1 operation(s) for oauthv2authorize.
  name: Twilio OAUTH V2Authorize API
  slug: twilio-oauthv2authorize-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The OauthV2Metadata API from Twilio — 1 operation(s) for oauthv2metadata.
  name: Twilio OAUTH V2Metadata API
  slug: twilio-oauthv2metadata-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The OauthV2Token API from Twilio — 1 operation(s) for oauthv2token.
  name: Twilio OAUTH V2Token API
  slug: twilio-oauthv2token-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Observations are small contextual text snippets automatically extracted from conversations that run through Conversation Orchestrator. They capture useful details like customer preferences, stated nee
  name: Twilio Observations API
  slug: twilio-observations-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Retrieve the status and result of asynchronous operations. Write endpoints that trigger long-running processes return an operation ID that can be used here to check status.
  name: Twilio Operations API
  slug: twilio-operations-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Retrieve results produced by language operators after they run on conversations, including associated execution metadata generated at runtime. Use these results to support real-time agent augmentation
  name: Twilio Operator Results API
  slug: twilio-operatorresults-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Define and manage language operators. Conversational Intelligence uses GenAI-powered language operators to transform conversation text into structured insights. Language operators produce structured o
  name: Twilio Operators API
  slug: twilio-operators-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The OrganizationAccounts API from Twilio — 2 operation(s) for organizationaccounts.
  name: Twilio Organization Accounts API
  slug: twilio-organizationaccounts-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Profiles are the canonical customer records in a Memory Store. Each profile holds traits, organized into trait groups, that identify and describe a customer and let Twilio attach future conversation d
  name: Twilio Profile API
  slug: twilio-profile-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Retrieval APIs resolve profiles and return relevant memory at the moment an agent needs them. Profile lookup is leveraged by the Conversation Orchestrator. When an inbound message arrives on a con
  name: Twilio Retrieval API
  slug: twilio-retrieval-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The RoutesV3PhoneNumber API from Twilio — 1 operation(s) for routesv3phonenumber.
  name: Twilio Routes V3Phone Number API
  slug: twilio-routesv3phonenumber-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The RoutesV3ShortCode API from Twilio — 1 operation(s) for routesv3shortcode.
  name: Twilio Routes V3Short Code API
  slug: twilio-routesv3shortcode-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Manual execution of rules on a conversation.
  name: Twilio Rule Executions API
  slug: twilio-ruleexecutions-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: SCIM 2.0 User endpoints
  name: Twilio SCIM API
  slug: twilio-scim-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Memory Store is the parent container for all Conversation Memory data. Profiles, identifiers, traits, observations, and summaries all live inside a specific store, and that store defines the bound
  name: Twilio Store API
  slug: twilio-store-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Trait Groups are the organized containers used to group related facts about a profile, such as contact details or account preferences. Trait schemas within each Trait Group must be defined before cust
  name: Twilio Trait Group API
  slug: twilio-traitgroup-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Traits are key value pairs that store facts about a profile such as firstName, lastName, or dietaryRestrictions. Trait values can only be written to a profile if the trait definition already exists an
  name: Twilio Traits API
  slug: twilio-traits-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Twilio Insights synchronous Query and Metadata resources.
  name: Twilio Twilio Insights API
  slug: twilio-twilioinsights-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Twilio Insights asynchronous QueryJobs resource (long-running query operations).
  name: Twilio Twilio Insights Async API
  slug: twilio-twilioinsightsasync-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Twilio Insights Config API for custom measure field mapping registration.
  name: Twilio Twilio Insights Config API
  slug: twilio-twilioinsightsconfig-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The V3Transcriptions API from Twilio — 2 operation(s) for v3transcriptions.
  name: Twilio V3Transcriptions API
  slug: twilio-v3transcriptions-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Customer Profiles API from Twilio — 8 operation(s) for customer profiles.
  name: Twilio Customer Profiles API
  slug: twilio-customer-profiles-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The End Users API from Twilio — 2 operation(s) for end users.
  name: Twilio End Users API
  slug: twilio-end-users-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Rate Plans API from Twilio — 2 operation(s) for rate plans.
  name: Twilio Rate Plans API
  slug: twilio-rate-plans-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Recording Settings API from Twilio — 1 operation(s) for recording settings.
  name: Twilio Recording Settings API
  slug: twilio-recording-settings-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: Role assignment operations
  name: Twilio Role Assignments API
  slug: twilio-role-assignments-api
- baseURL: https://messaging.twilio.com
  baseurl_source: declared
  description: The Usage Records API from Twilio — 1 operation(s) for usage records.
  name: Twilio Usage Records API
  slug: twilio-usage-records-api
arazzos:
- description: List in-progress conferences, fetch a matching one by SID, then dial a new participant into it.
  name: Twilio Find an In-Progress Conference and Add a Participant
  slug: twilio-conference-find-and-add-participant-workflow
- description: Confirm a conversation exists, post a reply message, then list the per-channel delivery receipts.
  name: Twilio Reply to a Conversation and Track Delivery Receipts
  slug: twilio-conversation-reply-and-track-receipts-workflow
- description: Create a voice call queue with a size limit, then fetch it back to confirm its configuration.
  name: Twilio Create a Call Queue and Confirm It
  slug: twilio-create-and-confirm-queue-workflow
- description: Stand up a Conversations thread, attach an SMS participant by address, and post the first message.
  name: Twilio Create a Conversation, Add a Participant, and Send a Message
  slug: twilio-create-conversation-add-participant-send-message-workflow
- description: Create a Conversations thread, then attach a conversation-scoped webhook that targets your service.
  name: Twilio Create a Conversation and Attach a Scoped Webhook
  slug: twilio-create-conversation-with-webhook-workflow
- description: Create a Twilio Video room, then fetch it so a client can join.
  name: Twilio Create a Video Room
  slug: twilio-create-video-room-workflow
- description: Fetch a call by SID and, when it is still in progress, update it to completed to end the call.
  name: Twilio Inspect a Call and Hang It Up If Live
  slug: twilio-end-active-call-workflow
- description: Look up a phone number to fetch carrier, line type, and caller name intelligence before using it.
  name: Twilio Look Up a Phone Number
  slug: twilio-lookup-phone-number-workflow
- description: Look up a phone number for validity and line type, then send an SMS only when the number is valid.
  name: Twilio Validate a Number then Send a Message
  slug: twilio-lookup-then-send-message-workflow
- description: Look up a phone number, and only when it is a valid mobile number start a Verify verification.
  name: Twilio Validate a Number then Start a Verification
  slug: twilio-lookup-then-start-verification-workflow
- description: Place an outbound call with a TwiML URL, then fetch the call resource to follow its progress.
  name: Twilio Make a Call and Track Its Status
  slug: twilio-make-call-track-status-workflow
- description: Create a messaging service, attach a phone number to its sender pool, then fetch the service back.
  name: Twilio Provision a Messaging Service and Attach a Sender Number
  slug: twilio-provision-messaging-service-add-number-workflow
- description: Start an outbound call, begin recording the in-progress call, then fetch the recording resource.
  name: Twilio Place a Call and Record It
  slug: twilio-record-active-call-workflow
- description: Schedule a future message via a messaging service, then cancel it while it is still scheduled.
  name: Twilio Schedule a Message and Cancel It Before Send
  slug: twilio-schedule-and-cancel-message-workflow
- description: Discover phone number orders, provision (host) a number, then confirm the order.
  name: Twilio Search and Buy a Number
  slug: twilio-search-and-buy-number-workflow
- description: Send an SMS, then redact the stored message body by updating it to an empty string for privacy.
  name: Twilio Send a Message and Redact Its Body
  slug: twilio-send-and-redact-message-workflow
- description: Send an SMS/MMS and poll the message resource until it reaches a terminal delivery status.
  name: Twilio Send a Message and Track Delivery Status
  slug: twilio-send-message-track-status-workflow
- description: Send an MMS with a media URL, fetch the message back, then list the media attached to it.
  name: Twilio Send an MMS and List Its Media
  slug: twilio-send-mms-and-list-media-workflow
- description: Create a messaging service, then send a message through it using the sender-pool pattern.
  name: Twilio Send via Messaging Service
  slug: twilio-send-via-messaging-service-workflow
- description: Publish a new Studio Flow from a definition, then trigger an execution of it for a contact.
  name: Twilio Studio Create a Flow and Run an Execution
  slug: twilio-studio-create-flow-and-execute-workflow
- description: Start a Studio Flow execution for a contact, fetch the execution, and list the steps it traversed.
  name: Twilio Studio Trigger a Flow Execution and Track Its Steps
  slug: twilio-studio-trigger-execution-track-steps-workflow
- description: Create a Sync Service, add a Document to it, then update the Document's data.
  name: Twilio Sync Document Lifecycle
  slug: twilio-sync-document-lifecycle-workflow
- description: Create a TaskRouter Workspace, then create a Task inside it for routing.
  name: Twilio Create a TaskRouter Workspace and Task
  slug: twilio-taskrouter-workspace-and-task-workflow
- description: Trigger an execution of a published Studio Flow for a contact, then fetch the execution status.
  name: Twilio Trigger a Studio Flow Execution
  slug: twilio-trigger-studio-execution-workflow
- description: Create a Verify service, start a verification to a phone number, then check the code to confirm it.
  name: Twilio Verify a Phone Number
  slug: twilio-verify-phone-number-workflow
- description: Create a Verify service, start a verification on it, and check the supplied code.
  name: Twilio Verify Provision a Service and Run a Verification
  slug: twilio-verify-provision-service-and-verify-workflow
- description: Start a Verify verification over a channel, then check a user-supplied code against it.
  name: Twilio Verify Start and Check a Verification
  slug: twilio-verify-start-and-check-workflow
- description: Start a verification, fetch it to read its status, and cancel it if it is still pending.
  name: Twilio Verify Start, Poll, and Cancel a Verification
  slug: twilio-verify-start-poll-and-cancel-workflow
artifact_total: 559
asyncapis:
- description: 'AsyncAPI 2.6 specification for Twilio''s public WebSocket APIs: - **Media Streams** — Bidirectional and one-way raw audio over WebSocket. Twilio acts as the WebSocket *client* and connects out to a cus'
  name: Twilio Real-Time WebSocket APIs
  slug: twilio-asyncapi
collections:
- collection_type: postman
  name: Twilio - Accounts
  slug: postman-accounts-openapi-original
- collection_type: postman
  name: Twilio Assistants
  slug: postman-assistant-openapi-original
- collection_type: postman
  name: Twilio - Autopilot
  slug: postman-autopilot-openapi-original
- collection_type: postman
  name: Twilio - Bulkexports
  slug: postman-bulk-exports-openapi-original
- collection_type: postman
  name: Twilio - Content
  slug: postman-content-openapi-original
- collection_type: postman
  name: Twilio - Conversations
  slug: postman-conversations-openapi-original
- collection_type: postman
  name: Twilio - Events
  slug: postman-events-openapi-original
- collection_type: postman
  name: Twilio - Frontline
  slug: postman-frontline-openapi-original
- collection_type: postman
  name: Twilio - Insights
  slug: postman-insights-openapi-original
- collection_type: postman
  name: Twilio - Intelligence
  slug: postman-intelligence-openapi-original
- collection_type: postman
  name: Twilio - Ip_messaging
  slug: postman-ip-message-openapi-original
- collection_type: postman
  name: Twilio Marketplace API
  slug: postman-marketplace-openapi-original
- collection_type: postman
  name: Twilio - Media
  slug: postman-media-openapi-original
- collection_type: postman
  name: Twilio - Messaging
  slug: postman-messaging-openapi-original
- collection_type: postman
  name: Twilio - Microvisor
  slug: postman-microvisor-openapi-original
- collection_type: postman
  name: Twilio - Monitor
  slug: postman-monitor-openapi-original
- collection_type: postman
  name: Twilio - Notify
  slug: postman-notify-openapi-original
- collection_type: postman
  name: Twilio - Numbers
  slug: postman-numbers-openapi-original
- collection_type: postman
  name: Twilio - Pricing
  slug: postman-pricing-openapi-original
- collection_type: postman
  name: Twilio - Proxy
  slug: postman-proxy-openapi-original
- collection_type: postman
  name: Twilio - Routes
  slug: postman-routes-openapi-original
- collection_type: postman
  name: Twilio - Serverless
  slug: postman-serverless-openapi-original
- collection_type: postman
  name: Twilio - Studio
  slug: postman-studio-openapi-original
- collection_type: postman
  name: Twilio - Supersim
  slug: postman-super-sim-openapi-original
- collection_type: postman
  name: Twilio - Sync
  slug: postman-sync-openapi-original
- collection_type: postman
  name: Twilio - Taskrouter
  slug: postman-task-router-openapi-original
- collection_type: postman
  name: Twilio - Trunking
  slug: postman-trunking-openapi-original
- collection_type: postman
  name: Twilio - Trusthub
  slug: postman-trust-hub-openapi-original
- collection_type: postman
  name: Twilio Accounts API
  slug: postman-twilio-accounts
- collection_type: postman
  name: Twilio Flex API
  slug: postman-twilio-flex
- collection_type: postman
  name: Twilio Lookup API
  slug: postman-twilio-lookup
- collection_type: postman
  name: Twilio Messaging API
  slug: postman-twilio-messaging
- collection_type: postman
  name: Twilio SendGrid Email API
  slug: postman-twilio-sendgrid
- collection_type: postman
  name: Twilio Verify API
  slug: postman-twilio-verify
- collection_type: postman
  name: Twilio Video API
  slug: postman-twilio-video
- collection_type: postman
  name: Twilio Voice API
  slug: postman-twilio-voice
- collection_type: postman
  name: Twilio - Verify
  slug: postman-verify-openapi-original
- collection_type: postman
  name: Twilio - Video
  slug: postman-video-openapi-original
- collection_type: postman
  name: Twilio - Voice
  slug: postman-voice-openapi-original
- collection_type: postman
  name: Twilio - Wireless
  slug: postman-wireless-openapi-original
- collection_type: open
  name: Twilio - Accounts A2p API
  slug: open-twilio-a2p-api
- collection_type: open
  name: Twilio - Accounts A2p Access Tokens API
  slug: open-twilio-access-tokens-api
- collection_type: open
  name: Twilio - A2p Accounts API
  slug: open-twilio-accounts-api
- collection_type: open
  name: Twilio Accounts API
  slug: open-twilio-accounts
- collection_type: open
  name: Twilio - Accounts A2p Alerts API
  slug: open-twilio-alerts-api
- collection_type: open
  name: Twilio - Accounts A2p Alpha Senders API
  slug: open-twilio-alpha-senders-api
- collection_type: open
  name: Twilio - Accounts A2p Apps API
  slug: open-twilio-apps-api
- collection_type: open
  name: Twilio - Accounts A2p Archives API
  slug: open-twilio-archives-api
- collection_type: open
  name: Twilio - Accounts A2p Assistants API
  slug: open-twilio-assistants-api
- collection_type: open
  name: Twilio - Accounts A2p Attempts API
  slug: open-twilio-attempts-api
- collection_type: open
  name: Twilio - Accounts A2p Auth Tokens API
  slug: open-twilio-auth-tokens-api
- collection_type: open
  name: Twilio - Accounts A2p Auth Tokens API
  slug: open-twilio-authtokens-api
- collection_type: open
  name: Twilio - Accounts A2p Byoc Trunks API
  slug: open-twilio-byoctrunks-api
- collection_type: open
  name: Twilio - Accounts A2p Calls API
  slug: open-twilio-calls-api
- collection_type: open
  name: Twilio - Accounts A2p Challenges API
  slug: open-twilio-challenges-api
- collection_type: open
  name: Twilio - Accounts A2p Channels API
  slug: open-twilio-channels-api
- collection_type: open
  name: Twilio - Accounts A2p Commands API
  slug: open-twilio-commands-api
- collection_type: open
  name: Twilio - Accounts A2p Compliance Inquiries API
  slug: open-twilio-complianceinquiries-api
- collection_type: open
  name: Twilio - Accounts A2p Composition Hooks API
  slug: open-twilio-composition-hooks-api
- collection_type: open
  name: Twilio - Accounts A2p Composition Hooks API
  slug: open-twilio-compositionhooks-api
- collection_type: open
  name: Twilio - Accounts A2p Compositions API
  slug: open-twilio-compositions-api
- collection_type: open
  name: Twilio - Accounts A2p Composition Settings API
  slug: open-twilio-compositionsettings-api
- collection_type: open
  name: Twilio - Accounts A2p Conferences API
  slug: open-twilio-conferences-api
- collection_type: open
  name: Twilio - Accounts A2p Configs API
  slug: open-twilio-configs-api
- collection_type: open
  name: Twilio - Accounts A2p Configuration API
  slug: open-twilio-configuration-api
- collection_type: open
  name: Twilio - Accounts A2p Connection Policies API
  slug: open-twilio-connectionpolicies-api
- collection_type: open
  name: Twilio - Accounts A2p Contacts API
  slug: open-twilio-contacts-api
- collection_type: open
  name: Twilio - Accounts A2p Content API
  slug: open-twilio-content-api
- collection_type: open
  name: Twilio - Accounts A2p Content And Approvals API
  slug: open-twilio-contentandapprovals-api
- collection_type: open
  name: Twilio - Accounts A2p Conversations API
  slug: open-twilio-conversations-api
- collection_type: open
  name: Twilio - Accounts A2p Credentials API
  slug: open-twilio-credentials-api
- collection_type: open
  name: Twilio - Accounts A2p Customer Profiles API
  slug: open-twilio-customerprofiles-api
- collection_type: open
  name: Twilio - Accounts A2p Deactivations API
  slug: open-twilio-deactivations-api
- collection_type: open
  name: Twilio - Accounts A2p Devices API
  slug: open-twilio-devices-api
- collection_type: open
  name: Twilio - Accounts A2p Dialing Permissions API
  slug: open-twilio-dialingpermissions-api
- collection_type: open
  name: Twilio - Accounts A2p Email Validation API
  slug: open-twilio-email-validation-api
- collection_type: open
  name: Twilio - Accounts A2p End Users API
  slug: open-twilio-endusers-api
- collection_type: open
  name: Twilio - Accounts A2p End User Types API
  slug: open-twilio-endusertypes-api
- collection_type: open
  name: Twilio - Accounts A2p Entities API
  slug: open-twilio-entities-api
- collection_type: open
  name: Twilio - Accounts A2p E Sim Profiles API
  slug: open-twilio-esimprofiles-api
- collection_type: open
  name: Twilio - Accounts A2p Events API
  slug: open-twilio-events-api
- collection_type: open
  name: Twilio - Accounts A2p Exports API
  slug: open-twilio-exports-api
- collection_type: open
  name: Twilio - Accounts A2p Factors API
  slug: open-twilio-factors-api
- collection_type: open
  name: Twilio - Accounts A2p Fleets API
  slug: open-twilio-fleets-api
- collection_type: open
  name: Twilio - Accounts A2p Flex Flows API
  slug: open-twilio-flex-flows-api
- collection_type: open
  name: Twilio Flex API
  slug: open-twilio-flex
- collection_type: open
  name: Twilio - Accounts A2p Flows API
  slug: open-twilio-flows-api
- collection_type: open
  name: Twilio - Accounts A2p Forms API
  slug: open-twilio-forms-api
- collection_type: open
  name: Twilio - Accounts A2p Hosted Number API
  slug: open-twilio-hostednumber-api
- collection_type: open
  name: Twilio - Accounts A2p Insights API
  slug: open-twilio-insights-api
- collection_type: open
  name: Twilio - Accounts A2p Interactions API
  slug: open-twilio-interactions-api
- collection_type: open
  name: Twilio - Accounts A2p Ip Commands API
  slug: open-twilio-ipcommands-api
- collection_type: open
  name: Twilio - Accounts A2p Ip Records API
  slug: open-twilio-iprecords-api
- collection_type: open
  name: Twilio - Accounts A2p Keys API
  slug: open-twilio-keys-api
- collection_type: open
  name: Twilio - Accounts A2p Legacy Content API
  slug: open-twilio-legacycontent-api
- collection_type: open
  name: Twilio - Accounts A2p Link Shortening API
  slug: open-twilio-linkshortening-api
- collection_type: open
  name: Twilio - Accounts A2p Lists API
  slug: open-twilio-lists-api
- collection_type: open
  name: Twilio Lookup API
  slug: open-twilio-lookup
- collection_type: open
  name: Twilio - Accounts A2p Mail Send API
  slug: open-twilio-mail-send-api
- collection_type: open
  name: Twilio - Accounts A2p Marketplace API
  slug: open-twilio-marketplace-api
- collection_type: open
  name: Twilio - Accounts A2p Media API
  slug: open-twilio-media-api
- collection_type: open
  name: Twilio - Accounts A2p Media Processors API
  slug: open-twilio-mediaprocessors-api
- collection_type: open
  name: Twilio - Accounts A2p Media Recordings API
  slug: open-twilio-mediarecordings-api
- collection_type: open
  name: Twilio - Accounts A2p Messages API
  slug: open-twilio-messages-api
- collection_type: open
  name: Twilio - Accounts A2p Messaging Services API
  slug: open-twilio-messaging-services-api
- collection_type: open
  name: Twilio Messaging API
  slug: open-twilio-messaging
- collection_type: open
  name: Twilio - Accounts A2p Network Access Profiles API
  slug: open-twilio-networkaccessprofiles-api
- collection_type: open
  name: Twilio - Accounts A2p Networks API
  slug: open-twilio-networks-api
- collection_type: open
  name: Twilio - Accounts A2p Participant Conversations API
  slug: open-twilio-participantconversations-api
- collection_type: open
  name: Twilio - Accounts A2p Participants API
  slug: open-twilio-participants-api
- collection_type: open
  name: Twilio - Accounts A2p Phone Numbers API
  slug: open-twilio-phone-numbers-api
- collection_type: open
  name: Twilio - Accounts A2p Phone Numbers API
  slug: open-twilio-phonenumbers-api
- collection_type: open
  name: Twilio - Accounts A2p Player Streamers API
  slug: open-twilio-playerstreamers-api
- collection_type: open
  name: Twilio - Accounts A2p Plugins API
  slug: open-twilio-plugins-api
- collection_type: open
  name: Twilio - Accounts A2p Policies API
  slug: open-twilio-policies-api
- collection_type: open
  name: Twilio - Accounts A2p Queues API
  slug: open-twilio-queues-api
- collection_type: open
  name: Twilio - Accounts A2p Rate Limits API
  slug: open-twilio-rate-limits-api
- collection_type: open
  name: Twilio - Accounts A2p Rate Plans API
  slug: open-twilio-rateplans-api
- collection_type: open
  name: Twilio - Accounts A2p Recording Rules API
  slug: open-twilio-recording-rules-api
- collection_type: open
  name: Twilio - Accounts A2p Recordings API
  slug: open-twilio-recordings-api
- collection_type: open
  name: Twilio - Accounts A2p Recording Settings API
  slug: open-twilio-recordingsettings-api
- collection_type: open
  name: Twilio - Accounts A2p Regulatory Compliance API
  slug: open-twilio-regulatorycompliance-api
- collection_type: open
  name: Twilio - Accounts A2p Roles API
  slug: open-twilio-roles-api
- collection_type: open
  name: Twilio - Accounts A2p Rooms API
  slug: open-twilio-rooms-api
- collection_type: open
  name: Twilio - Accounts A2p Safe List API
  slug: open-twilio-safelist-api
- collection_type: open
  name: Twilio - Accounts A2p Schemas API
  slug: open-twilio-schemas-api
- collection_type: open
  name: Twilio - Accounts A2p Secrets API
  slug: open-twilio-secrets-api
- collection_type: open
  name: Twilio - Accounts A2p Senders API
  slug: open-twilio-senders-api
- collection_type: open
  name: Twilio SendGrid Email API
  slug: open-twilio-sendgrid
- collection_type: open
  name: Twilio - Accounts A2p Services API
  slug: open-twilio-services-api
- collection_type: open
  name: Twilio - Accounts A2p Settings API
  slug: open-twilio-settings-api
- collection_type: open
  name: Twilio - Accounts A2p Settings Updates API
  slug: open-twilio-settingsupdates-api
- collection_type: open
  name: Twilio - Accounts A2p Short Codes API
  slug: open-twilio-short-codes-api
- collection_type: open
  name: Twilio - Accounts A2p Sims API
  slug: open-twilio-sims-api
- collection_type: open
  name: Twilio - Accounts A2p Sinks API
  slug: open-twilio-sinks-api
- collection_type: open
  name: Twilio - Accounts A2p Sip Domains API
  slug: open-twilio-sipdomains-api
- collection_type: open
  name: Twilio - Accounts A2p Sms Commands API
  slug: open-twilio-smscommands-api
- collection_type: open
  name: Twilio - Accounts A2p Source Ip Mappings API
  slug: open-twilio-sourceipmappings-api
- collection_type: open
  name: Twilio - Accounts A2p Stats API
  slug: open-twilio-stats-api
- collection_type: open
  name: Twilio - Accounts A2p Subscriptions API
  slug: open-twilio-subscriptions-api
- collection_type: open
  name: Twilio - Accounts A2p Supporting Documents API
  slug: open-twilio-supportingdocuments-api
- collection_type: open
  name: Twilio - Accounts A2p Supporting Document Types API
  slug: open-twilio-supportingdocumenttypes-api
- collection_type: open
  name: Twilio - Accounts A2p Suppressions API
  slug: open-twilio-suppressions-api
- collection_type: open
  name: Twilio - Accounts A2p Templates API
  slug: open-twilio-templates-api
- collection_type: open
  name: Twilio - Accounts A2p Tollfree API
  slug: open-twilio-tollfree-api
- collection_type: open
  name: Twilio - Accounts A2p Transcripts API
  slug: open-twilio-transcripts-api
- collection_type: open
  name: Twilio - Accounts A2p Trunking API
  slug: open-twilio-trunking-api
- collection_type: open
  name: Twilio - Accounts A2p Trunks API
  slug: open-twilio-trunks-api
- collection_type: open
  name: Twilio - Accounts A2p Trust Products API
  slug: open-twilio-trustproducts-api
- collection_type: open
  name: Twilio - Accounts A2p Types API
  slug: open-twilio-types-api
- collection_type: open
  name: Twilio - Accounts A2p Understand API
  slug: open-twilio-understand-api
- collection_type: open
  name: Twilio - Accounts A2p Usage Records API
  slug: open-twilio-usagerecords-api
- collection_type: open
  name: Twilio - Accounts A2p Users API
  slug: open-twilio-users-api
- collection_type: open
  name: Twilio - Accounts A2p Verification Checks API
  slug: open-twilio-verification-checks-api
- collection_type: open
  name: Twilio - Accounts A2p Verifications API
  slug: open-twilio-verifications-api
- collection_type: open
  name: Twilio Verify API
  slug: open-twilio-verify
- collection_type: open
  name: Twilio - Accounts A2p Video API
  slug: open-twilio-video-api
- collection_type: open
  name: Twilio Video API
  slug: open-twilio-video
- collection_type: open
  name: Twilio - Accounts A2p Voice API
  slug: open-twilio-voice-api
- collection_type: open
  name: Twilio Voice API
  slug: open-twilio-voice
- collection_type: open
  name: Twilio - Accounts A2p Web Channels API
  slug: open-twilio-web-channels-api
- collection_type: open
  name: Twilio - Accounts A2p Webhooks API
  slug: open-twilio-webhooks-api
- collection_type: open
  name: Twilio - Accounts A2p Workspaces API
  slug: open-twilio-workspaces-api
common:
- group: commercial
  href: https://artifacts.apis.io/twilio/finops/twilio-finops.yml
  title: ''
  type: FinOps
  url: finops/twilio-finops.yml
- group: design
  href: https://artifacts.apis.io/twilio/rules/twilio-rules.yml
  title: ''
  type: Spectral
  url: rules/twilio-rules.yml
- group: design
  href: https://artifacts.apis.io/twilio/rules/twilio-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/twilio-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/twilio/rules/twilio-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/twilio-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/twilio/conventions/twilio-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/twilio-conventions.yml
- group: design
  href: https://artifacts.apis.io/twilio/errors/twilio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/twilio-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/twilio/llms/twilio-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twilio-docs-llms.txt
- group: build
  href: https://artifacts.apis.io/twilio/mcp/twilio-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/twilio-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/twilio/hosts/twilio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/twilio-hosts.yml
- group: other
  href: https://artifacts.apis.io/twilio/vendors/twilio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/twilio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/twilio/scopes/twilio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/twilio-scopes.yml
- group: operate
  href: https://artifacts.apis.io/twilio/rate-limits/twilio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/twilio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/twilio/plans/twilio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/twilio-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.twilio.com/
- group: other
  href: https://artifacts.apis.io/twilio/capabilities/twilio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/twilio-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/twilio/agentic-access/twilio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/twilio-agentic-access.yml
- group: start
  href: https://artifacts.apis.io/twilio/sandbox/twilio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/twilio-sandbox.yml
- group: design
  href: https://artifacts.apis.io/twilio/conventions/twilio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/twilio-conventions.yml
- group: operate
  href: https://artifacts.apis.io/twilio/changelog/twilio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/twilio-changelog.yml
- group: build
  href: https://artifacts.apis.io/twilio/cli/twilio-cli.yml
  title: ''
  type: CLI
  url: cli/twilio-cli.yml
- group: design
  href: https://artifacts.apis.io/twilio/components/twilio-components.yml
  title: ''
  type: Components
  url: components/twilio-components.yml
- group: design
  href: https://artifacts.apis.io/twilio/data-model/twilio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/twilio-data-model.yml
- group: design
  href: https://artifacts.apis.io/twilio/errors/twilio-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/twilio-error-codes.yml
- group: build
  href: https://artifacts.apis.io/twilio/packages/twilio-packages.yml
  title: ''
  type: Packages
  url: packages/twilio-packages.yml
- group: auth
  href: https://artifacts.apis.io/twilio/security/twilio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/twilio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/twilio/security/twilio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twilio-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/twilio/authentication/twilio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twilio-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/twilio/overview
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-conference-find-and-add-participant-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-conference-find-and-add-participant-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-conversation-reply-and-track-receipts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-conversation-reply-and-track-receipts-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-create-and-confirm-queue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-create-and-confirm-queue-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-create-conversation-add-participant-send-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-create-conversation-add-participant-send-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-create-conversation-with-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-create-conversation-with-webhook-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-end-active-call-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-end-active-call-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-lookup-then-send-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-lookup-then-send-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-lookup-then-start-verification-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-lookup-then-start-verification-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-make-call-track-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-make-call-track-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-provision-messaging-service-add-number-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-provision-messaging-service-add-number-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-record-active-call-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-record-active-call-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-schedule-and-cancel-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-schedule-and-cancel-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-send-and-redact-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-send-and-redact-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-send-message-track-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-send-message-track-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-send-mms-and-list-media-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-send-mms-and-list-media-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-studio-create-flow-and-execute-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-studio-create-flow-and-execute-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-studio-trigger-execution-track-steps-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-studio-trigger-execution-track-steps-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-verify-provision-service-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-verify-provision-service-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-verify-start-and-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-verify-start-and-check-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-verify-start-poll-and-cancel-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-verify-start-poll-and-cancel-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-verify-phone-number-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-verify-phone-number-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-lookup-phone-number-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-lookup-phone-number-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-send-via-messaging-service-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-send-via-messaging-service-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-search-and-buy-number-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-search-and-buy-number-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-create-video-room-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-create-video-room-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-taskrouter-workspace-and-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-taskrouter-workspace-and-task-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-sync-document-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-sync-document-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/twilio/arazzo/twilio-trigger-studio-execution-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/twilio-trigger-studio-execution-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twilio-inc-
- group: start
  title: ''
  type: SignUp
  url: https://www.twilio.com/try-twilio
- group: company
  title: ''
  type: About
  url: https://www.twilio.com/en-us/company
- group: operate
  title: ''
  type: Support
  url: https://support.twilio.com/
- group: build
  title: ''
  type: SDKs
  url: https://www.twilio.com/docs/libraries
- group: operate
  title: ''
  type: StatusPage
  url: https://status.twilio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.twilio.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.twilio.com/blog
- group: commercial
  title: ''
  type: Privacy
  url: https://www.twilio.com/en-us/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.twilio.com/en-us/legal/tos
- group: start
  title: ''
  type: Portal
  url: https://console.twilio.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.twilio.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.twilio.com/docs/usage/tutorials
- group: auth
  title: ''
  type: Authentication
  url: https://www.twilio.com/docs/iam/credentials/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twilio.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.twilio.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twilio
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/twilio/twilio-oai
- group: design
  title: ''
  type: ErrorCodes
  url: https://www.twilio.com/docs/api/errors
- group: design
  title: ''
  type: Webhooks
  url: https://www.twilio.com/docs/usage/webhooks
- group: operate
  title: ''
  type: RateLimits
  url: https://www.twilio.com/docs/usage/rest-api-best-practices
- group: auth
  title: ''
  type: Security
  url: https://www.twilio.com/en-us/legal/security-overview
- group: other
  title: ''
  type: API Overview
  url: https://www.twilio.com/docs/usage/api
- group: other
  title: ''
  type: Developer Hub
  url: https://www.twilio.com/en-us/developers
- group: company
  title: ''
  type: Partners
  url: https://www.twilio.com/en-us/partners
- group: docs
  title: ''
  type: OpenAPI Overview
  url: https://www.twilio.com/docs/openapi
- group: learn
  title: ''
  type: Webinars
  url: https://www.twilio.com/en-us/resource-center/webinars
- group: auth
  title: ''
  type: Trust Center
  url: https://security.twilio.com/
- group: build
  title: ''
  type: Code Exchange
  url: https://www.twilio.com/code-exchange
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/twilio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@twilio
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/twilio
- group: docs
  href: https://artifacts.apis.io/twilio/json-schema/twilio-message-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/twilio-message-schema.json
- group: docs
  href: https://artifacts.apis.io/twilio/json-schema/twilio-call-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/twilio-call-schema.json
- group: docs
  href: https://artifacts.apis.io/twilio/json-schema/twilio-account-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/twilio-account-schema.json
- group: docs
  href: https://artifacts.apis.io/twilio/json-schema/twilio-recording-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/twilio-recording-schema.json
- group: docs
  href: https://artifacts.apis.io/twilio/json-schema/twilio-verification-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/twilio-verification-schema.json
- group: docs
  href: https://artifacts.apis.io/twilio/json-schema/twilio-phone-number-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/twilio-phone-number-schema.json
- group: design
  href: https://artifacts.apis.io/twilio/json-ld/twilio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/twilio-context.jsonld
- group: design
  href: https://artifacts.apis.io/twilio/rules/twilio-rules.yml
  title: ''
  type: SpectralRules
  url: rules/twilio-rules.yml
- group: design
  href: https://artifacts.apis.io/twilio/vocabulary/twilio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/twilio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/twilio/json-structure/twilio-message-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/twilio-message-structure.json
- group: design
  href: https://artifacts.apis.io/twilio/json-structure/twilio-call-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/twilio-call-structure.json
- group: agent
  title: ''
  type: MCPServer
  url: https://www.twilio.com/en-us/blog/developers/introducing-twilio-mcp-skills
- group: agent
  href: https://artifacts.apis.io/twilio/mcp/twilio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/twilio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/twilio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/twilio/llms/twilio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twilio-llms.txt
- group: design
  href: https://artifacts.apis.io/twilio/conformance/twilio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twilio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.twilio.com/
- group: design
  href: https://artifacts.apis.io/twilio/lifecycle/twilio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/twilio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.twilio.com/docs/sync/versioning-and-support-lifecycle
- group: auth
  href: https://artifacts.apis.io/twilio/security/twilio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/twilio-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-messaging-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-voice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-voice-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-verify-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-verify-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-lookup-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-lookup-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-video-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-video-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-flex-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-flex-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-accounts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/twilio/overlays/twilio-sendgrid-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twilio-sendgrid-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.twilio.com/en-us/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.twilio.com/docs/usage/api
- group: start
  title: ''
  type: Login
  url: https://www.twilio.com/login
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
  type: Subprocessors
  url: https://www.twilio.com/en-us/legal/sub-processors
- group: other
  title: ''
  type: TransparencyReport
  url: https://www.twilio.com/en-us/legal/transparency
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.twilio.com/en-us/legal/data-protection-addendum
- group: other
  title: ''
  type: DataResidency
  url: https://www.twilio.com/docs/global-infrastructure
- group: other
  title: ''
  type: AITransparency
  url: https://www.twilio.com/docs/conversation-intelligence-classic/ai-nutrition-fact-labels
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.twilio.com/en-us/help/privacy
- group: other
  title: ''
  type: NoticeAndAction
  url: https://www.twilio.com/en-us/help/abuse
- group: other
  title: ''
  type: ExitAssistance
  url: https://www.twilio.com/docs/segment/connections/data-export-options
- group: operate
  title: ''
  type: SupportLifetime
  url: https://www.twilio.com/docs/sync/versioning-and-support-lifecycle
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/twilio/sendgrid-oai/blob/fb95a935c87b79f7f982ac34bd37adab1f697dbc/spectral.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/twilio/twilio-oai/blob/141f1201b55abcc16b3aa8089e71c4a927326975/spectral.yaml
created: 2024/04/14
description: Cloud communications platform providing APIs for SMS, voice, video, and authentication services. Twilio offers 30+ APIs covering messaging, voice, video, email, identity verification, IoT connectivity, and contact center solutions. Used by over 10 million developers globally with SDKs for Node.js, Python, Ruby, Java, PHP, C#, and Go.
examples:
- key_count: 4
  name: Twilio Create Video Room Example
  slug: twilio-create-video-room-example
- key_count: 4
  name: Twilio Lookup Phone Number Example
  slug: twilio-lookup-phone-number-example
- key_count: 4
  name: Twilio Make Call Example
  slug: twilio-make-call-example
- key_count: 4
  name: Twilio Send Message Example
  slug: twilio-send-message-example
- key_count: 4
  name: Twilio Start Verification Example
  slug: twilio-start-verification-example
finops:
- has_sources: true
  method: derived
  name: Twilio Finops
  primary_unit: active user
  service_category: ''
  slug: twilio-finops
  template: false
image: https://www.twilio.com/bundles/company-brand/img/logos/red/twilio-logo-red.png
json_schemas:
- name: AccessToken
  property_count: 10
  slug: twilio-access-token
- name: AccountList
  property_count: 5
  slug: twilio-account-list
- name: Twilio Account
  property_count: 10
  slug: twilio-account
- name: accounts.v1.auth_token_promotion
  property_count: 5
  slug: twilio-accounts-v1-auth-token-promotion
- name: accounts.v1.credential.credential_aws
  property_count: 6
  slug: twilio-accounts-v1-credential-credential-aws
- name: accounts.v1.credential.credential_public_key
  property_count: 6
  slug: twilio-accounts-v1-credential-credential-public-key
- name: accounts.v1.secondary_auth_token
  property_count: 5
  slug: twilio-accounts-v1-secondary-auth-token
- name: AlphaSender
  property_count: 4
  slug: twilio-alpha-sender
- name: AuthTokenPromotion
  property_count: 5
  slug: twilio-auth-token-promotion
- name: autopilot.v1.assistant.field_type.field_value
  property_count: 10
  slug: twilio-autopilot-v1-assistant-field-type-field-value
- name: autopilot.v1.assistant.model_build
  property_count: 10
  slug: twilio-autopilot-v1-assistant-model-build
- name: autopilot.v1.assistant.query
  property_count: 14
  slug: twilio-autopilot-v1-assistant-query
- name: autopilot.v1.assistant
  property_count: 14
  slug: twilio-autopilot-v1-assistant
- name: autopilot.v1.assistant.task.sample
  property_count: 10
  slug: twilio-autopilot-v1-assistant-task-sample
- name: autopilot.v1.restore_assistant
  property_count: 12
  slug: twilio-autopilot-v1-restore-assistant
- name: bulkexports.v1.export.export_custom_job
  property_count: 11
  slug: twilio-bulkexports-v1-export-export-custom-job
- name: CallList
  property_count: 7
  slug: twilio-call-list
- name: Twilio Call
  property_count: 26
  slug: twilio-call
- name: ChannelList
  property_count: 2
  slug: twilio-channel-list
- name: CompositionHookList
  property_count: 2
  slug: twilio-composition-hook-list
- name: CompositionHook
  property_count: 15
  slug: twilio-composition-hook
- name: Composition
  property_count: 19
  slug: twilio-composition
- name: CompositionSettings
  property_count: 8
  slug: twilio-composition-settings
- name: Conference
  property_count: 11
  slug: twilio-conference
- name: ContactListCollection
  property_count: 1
  slug: twilio-contact-list-collection
- name: ContactList
  property_count: 3
  slug: twilio-contact-list
- name: ContactRequest
  property_count: 12
  slug: twilio-contact-request
- name: content.v1.content.approval_fetch
  property_count: 4
  slug: twilio-content-v1-content-approval-fetch
- name: content.v1.content
  property_count: 10
  slug: twilio-content-v1-content
- name: conversations.v1.configuration_address
  property_count: 10
  slug: twilio-conversations-v1-configuration-address
- name: conversations.v1.configuration.configuration_webhook
  property_count: 7
  slug: twilio-conversations-v1-configuration-configuration-webhook
- name: conversations.v1.configuration
  property_count: 7
  slug: twilio-conversations-v1-configuration
- name: conversations.v1.conversation.conversation_message.conversation_message_receipt
  property_count: 11
  slug: twilio-conversations-v1-conversation-conversation-message-conversation-message-receipt
- name: conversations.v1.conversation.conversation_message
  property_count: 15
  slug: twilio-conversations-v1-conversation-conversation-message
- name: conversations.v1.conversation.conversation_participant
  property_count: 12
  slug: twilio-conversations-v1-conversation-conversation-participant
- name: conversations.v1.conversation
  property_count: 14
  slug: twilio-conversations-v1-conversation
- name: conversations.v1.credential
  property_count: 8
  slug: twilio-conversations-v1-credential
- name: CreateAccountConfigRequest
  property_count: 2
  slug: twilio-create-account-config-request
- name: CreateAuthorizationDocumentRequest
  property_count: 6
  slug: twilio-create-authorization-document-request
- name: CreateBrandRegistrationsRequest
  property_count: 5
  slug: twilio-create-brand-registrations-request
- name: CreateByocTrunkRequest
  property_count: 10
  slug: twilio-create-byoc-trunk-request
- name: CreateCallRequest
  property_count: 15
  slug: twilio-create-call-request
- name: CreateChannelRequest
  property_count: 10
  slug: twilio-create-channel-request
- name: CreateCommandRequest
  property_count: 7
  slug: twilio-create-command-request
- name: CreateComplianceInquiryRequest
  property_count: 1
  slug: twilio-create-compliance-inquiry-request
- name: CreateComplianceTollfreeInquiryRequest
  property_count: 21
  slug: twilio-create-compliance-tollfree-inquiry-request
- name: CreateCompositionHookRequest
  property_count: 10
  slug: twilio-create-composition-hook-request
- name: CreateCompositionRequest_2
  property_count: 9
  slug: twilio-create-composition-request-2
- name: CreateCompositionRequest
  property_count: 9
  slug: twilio-create-composition-request
- name: CreateConfigurationAddressRequest
  property_count: 12
  slug: twilio-create-configuration-address-request
- name: CreateConnectionPolicyTargetRequest
  property_count: 5
  slug: twilio-create-connection-policy-target-request
- name: CreateConversationRequest
  property_count: 11
  slug: twilio-create-conversation-request
- name: CreateCredentialAwsRequest
  property_count: 3
  slug: twilio-create-credential-aws-request
- name: CreateCredentialRequest
  property_count: 7
  slug: twilio-create-credential-request
- name: CreateDialingPermissionsCountryBulkUpdateRequest
  property_count: 1
  slug: twilio-create-dialing-permissions-country-bulk-update-request
- name: CreateEsimProfileRequest
  property_count: 4
  slug: twilio-create-esim-profile-request
- name: CreateFleetRequest
  property_count: 9
  slug: twilio-create-fleet-request
- name: CreateFlexFlowRequest
  property_count: 13
  slug: twilio-create-flex-flow-request
- name: CreateHostedNumberOrderRequest
  property_count: 16
  slug: twilio-create-hosted-number-order-request
- name: CreateInteractionRequest
  property_count: 2
  slug: twilio-create-interaction-request
- name: CreateIpCommandRequest
  property_count: 6
  slug: twilio-create-ip-command-request
- name: CreateIpRecordRequest
  property_count: 3
  slug: twilio-create-ip-record-request
- name: CreateMarketplaceInstalledAddOnRequest
  property_count: 4
  slug: twilio-create-marketplace-installed-add-on-request
- name: CreateMediaProcessorRequest
  property_count: 6
  slug: twilio-create-media-processor-request
- name: CreateMessageRequest
  property_count: 12
  slug: twilio-create-message-request
- name: CreateMessagingServiceRequest
  property_count: 10
  slug: twilio-create-messaging-service-request
- name: EmailValidation
  property_count: 1
  slug: twilio-email-validation
- name: FlexChannel
  property_count: 8
  slug: twilio-flex-channel
- name: FlexConfiguration
  property_count: 19
  slug: twilio-flex-configuration
- name: FlexFlowList
  property_count: 2
  slug: twilio-flex-flow-list
- name: FlexFlow
  property_count: 14
  slug: twilio-flex-flow
- name: insights.v1.conference.conference_participant
  property_count: 27
  slug: twilio-insights-v1-conference-conference-participant
- name: insights.v1.conference
  property_count: 23
  slug: twilio-insights-v1-conference
- name: Interaction
  property_count: 8
  slug: twilio-interaction
- name: KeyList
  property_count: 5
  slug: twilio-key-list
- name: Key
  property_count: 4
  slug: twilio-key
- name: ListAccountConfigResponse
  property_count: 2
  slug: twilio-list-account-config-response
- name: ListAlertResponse
  property_count: 2
  slug: twilio-list-alert-response
- name: ListAppResponse
  property_count: 2
  slug: twilio-list-app-response
- name: ListBrandRegistrationsResponse
  property_count: 2
  slug: twilio-list-brand-registrations-response
- name: ListBrandVettingResponse
  property_count: 2
  slug: twilio-list-brand-vetting-response
- name: ListByocTrunkResponse
  property_count: 2
  slug: twilio-list-byoc-trunk-response
- name: ListCommandResponse
  property_count: 2
  slug: twilio-list-command-response
- name: ListCompositionHookResponse
  property_count: 2
  slug: twilio-list-composition-hook-response
- name: ListCompositionResponse
  property_count: 2
  slug: twilio-list-composition-response
- name: ListConferenceParticipantResponse
  property_count: 2
  slug: twilio-list-conference-participant-response
- name: ListConferenceResponse
  property_count: 2
  slug: twilio-list-conference-response
- name: ListConnectionPolicyResponse
  property_count: 2
  slug: twilio-list-connection-policy-response
- name: ListConnectionPolicyTargetResponse
  property_count: 2
  slug: twilio-list-connection-policy-target-response
- name: ListContentAndApprovalsResponse
  property_count: 2
  slug: twilio-list-content-and-approvals-response
- name: ListContentResponse
  property_count: 2
  slug: twilio-list-content-response
- name: ListDependentHostedNumberOrderResponse
  property_count: 2
  slug: twilio-list-dependent-hosted-number-order-response
- name: ListDeviceConfigResponse
  property_count: 2
  slug: twilio-list-device-config-response
- name: ListDeviceSecretResponse
  property_count: 2
  slug: twilio-list-device-secret-response
- name: ListDialingPermissionsCountryResponse
  property_count: 2
  slug: twilio-list-dialing-permissions-country-response
- name: ListDialingPermissionsHrsPrefixesResponse
  property_count: 2
  slug: twilio-list-dialing-permissions-hrs-prefixes-response
- name: ListEndUserTypeResponse
  property_count: 2
  slug: twilio-list-end-user-type-response
- name: ListEsimProfileResponse
  property_count: 2
  slug: twilio-list-esim-profile-response
- name: ListEventResponse
  property_count: 2
  slug: twilio-list-event-response
- name: ListFleetResponse
  property_count: 2
  slug: twilio-list-fleet-response
- name: ListIpCommandResponse
  property_count: 2
  slug: twilio-list-ip-command-response
- name: ListIpRecordResponse
  property_count: 2
  slug: twilio-list-ip-record-response
- name: ListLegacyContentResponse
  property_count: 2
  slug: twilio-list-legacy-content-response
- name: ListMarketplaceAvailableAddOnExtensionResponse
  property_count: 2
  slug: twilio-list-marketplace-available-add-on-extension-response
- name: ListMediaProcessorResponse
  property_count: 2
  slug: twilio-list-media-processor-response
- name: ListMediaRecordingResponse
  property_count: 2
  slug: twilio-list-media-recording-response
- name: ListVerificationAttemptResponse
  property_count: 2
  slug: twilio-list-verification-attempt-response
- name: MediaList
  property_count: 4
  slug: twilio-media-list
- name: MediaResource
  property_count: 7
  slug: twilio-media-resource
- name: media.v1.media_processor
  property_count: 12
  slug: twilio-media-v1-media-processor
- name: media.v1.media_recording
  property_count: 15
  slug: twilio-media-v1-media-recording
- name: MessageList
  property_count: 7
  slug: twilio-message-list
- name: Twilio Message
  property_count: 20
  slug: twilio-message
- name: MessagingService
  property_count: 15
  slug: twilio-messaging-service
- name: messaging.v1.brand_registrations.brand_registration_otp
  property_count: 2
  slug: twilio-messaging-v1-brand-registrations-brand-registration-otp
- name: messaging.v1.brand_registrations.brand_vetting
  property_count: 10
  slug: twilio-messaging-v1-brand-registrations-brand-vetting
- name: messaging.v1.brand_registrations
  property_count: 20
  slug: twilio-messaging-v1-brand-registrations
- name: messaging.v1.domain_cert_v4
  property_count: 8
  slug: twilio-messaging-v1-domain-cert-v4
- name: messaging.v1.domain_config_messaging_service
  property_count: 9
  slug: twilio-messaging-v1-domain-config-messaging-service
- name: messaging.v1.domain_config
  property_count: 9
  slug: twilio-messaging-v1-domain-config
- name: messaging.v1.linkshortening_messaging_service_domain_association
  property_count: 3
  slug: twilio-messaging-v1-linkshortening-messaging-service-domain-association
- name: messaging.v1.linkshortening_messaging_service
  property_count: 3
  slug: twilio-messaging-v1-linkshortening-messaging-service
- name: microvisor.v1.account_config
  property_count: 4
  slug: twilio-microvisor-v1-account-config
- name: microvisor.v1.app.app_manifest
  property_count: 4
  slug: twilio-microvisor-v1-app-app-manifest
- name: microvisor.v1.app
  property_count: 8
  slug: twilio-microvisor-v1-app
- name: microvisor.v1.device.device_config
  property_count: 5
  slug: twilio-microvisor-v1-device-device-config
- name: microvisor.v1.device.device_secret
  property_count: 4
  slug: twilio-microvisor-v1-device-device-secret
- name: microvisor.v1.device
  property_count: 9
  slug: twilio-microvisor-v1-device
- name: monitor.v1.alert-instance
  property_count: 19
  slug: twilio-monitor-v1-alert-instance
- name: monitor.v1.event
  property_count: 14
  slug: twilio-monitor-v1-event
- name: NewKey
  property_count: 4
  slug: twilio-new-key
- name: numbers.v2.authorization_document
  property_count: 9
  slug: twilio-numbers-v2-authorization-document
- name: numbers.v2.bulk_hosted_number_order
  property_count: 9
  slug: twilio-numbers-v2-bulk-hosted-number-order
- name: numbers.v2.hosted_number_order
  property_count: 19
  slug: twilio-numbers-v2-hosted-number-order
- name: Participant
  property_count: 12
  slug: twilio-participant
- name: Twilio Phone Number
  property_count: 29
  slug: twilio-phone-number
- name: preview.marketplace.available_add_on.available_add_on_extension
  property_count: 6
  slug: twilio-preview-marketplace-available-add-on-available-add-on-extension
- name: preview.marketplace.available_add_on
  property_count: 7
  slug: twilio-preview-marketplace-available-add-on
- name: preview.marketplace.installed_add_on.installed_add_on_extension
  property_count: 7
  slug: twilio-preview-marketplace-installed-add-on-installed-add-on-extension
- name: preview.marketplace.installed_add_on
  property_count: 10
  slug: twilio-preview-marketplace-installed-add-on
- name: Twilio Recording
  property_count: 18
  slug: twilio-recording
- name: SecondaryAuthToken
  property_count: 5
  slug: twilio-secondary-auth-token
- name: SendEmailRequest
  property_count: 15
  slug: twilio-send-email-request
- name: studio.v2.flow.execution.execution_context
  property_count: 5
  slug: twilio-studio-v2-flow-execution-execution-context
- name: studio.v2.flow.execution.execution_step.execution_step_context
  property_count: 6
  slug: twilio-studio-v2-flow-execution-execution-step-execution-step-context
- name: studio.v2.flow.execution.execution_step
  property_count: 12
  slug: twilio-studio-v2-flow-execution-execution-step
- name: studio.v2.flow.execution
  property_count: 10
  slug: twilio-studio-v2-flow-execution
- name: studio.v2.flow.flow_revision
  property_count: 12
  slug: twilio-studio-v2-flow-flow-revision
- name: studio.v2.flow
  property_count: 15
  slug: twilio-studio-v2-flow
- name: supersim.v1.esim_profile
  property_count: 14
  slug: twilio-supersim-v1-esim-profile
- name: supersim.v1.fleet
  property_count: 15
  slug: twilio-supersim-v1-fleet
- name: supersim.v1.ip_command
  property_count: 13
  slug: twilio-supersim-v1-ip-command
- name: trusthub.v1.compliance_inquiry
  property_count: 4
  slug: twilio-trusthub-v1-compliance-inquiry
- name: trusthub.v1.compliance_tollfree_inquiry
  property_count: 4
  slug: twilio-trusthub-v1-compliance-tollfree-inquiry
- name: trusthub.v1.end_user_type
  property_count: 5
  slug: twilio-trusthub-v1-end-user-type
- name: UpdateAccountConfigRequest
  property_count: 1
  slug: twilio-update-account-config-request
- name: UpdateByocTrunkRequest
  property_count: 10
  slug: twilio-update-byoc-trunk-request
- name: UpdateCallRequest
  property_count: 4
  slug: twilio-update-call-request
- name: UpdateComplianceInquiryRequest
  property_count: 1
  slug: twilio-update-compliance-inquiry-request
- name: UpdateCompositionHookRequest
  property_count: 10
  slug: twilio-update-composition-hook-request
- name: UpdateConfigurationAddressRequest
  property_count: 9
  slug: twilio-update-configuration-address-request
- name: UpdateConnectionPolicyTargetRequest
  property_count: 5
  slug: twilio-update-connection-policy-target-request
- name: UpdateConversationRequest
  property_count: 11
  slug: twilio-update-conversation-request
- name: UpdateCredentialRequest
  property_count: 7
  slug: twilio-update-credential-request
- name: UpdateDeviceRequest
  property_count: 4
  slug: twilio-update-device-request
- name: UpdateDomainConfigRequest
  property_count: 4
  slug: twilio-update-domain-config-request
- name: UpdateFleetRequest
  property_count: 7
  slug: twilio-update-fleet-request
- name: UpdateIpRecordRequest
  property_count: 1
  slug: twilio-update-ip-record-request
- name: UpdateMediaProcessorRequest
  property_count: 1
  slug: twilio-update-media-processor-request
- name: Twilio Verification
  property_count: 14
  slug: twilio-verification
- name: verify.v2.form
  property_count: 4
  slug: twilio-verify-v2-form
- name: verify.v2.verification_attempt
  property_count: 11
  slug: twilio-verify-v2-verification-attempt
- name: verify.v2.verification_attempts_summary
  property_count: 5
  slug: twilio-verify-v2-verification-attempts-summary
- name: video.v1.composition_hook
  property_count: 15
  slug: twilio-video-v1-composition-hook
- name: video.v1.composition
  property_count: 21
  slug: twilio-video-v1-composition
- name: video.v1.composition_settings
  property_count: 8
  slug: twilio-video-v1-composition-settings
- name: voice.v1.byoc_trunk
  property_count: 15
  slug: twilio-voice-v1-byoc-trunk
- name: voice.v1.connection_policy.connection_policy_target
  property_count: 11
  slug: twilio-voice-v1-connection-policy-connection-policy-target
- name: voice.v1.connection_policy
  property_count: 7
  slug: twilio-voice-v1-connection-policy
- name: voice.v1.dialing_permissions.dialing_permissions_country_bulk_update
  property_count: 2
  slug: twilio-voice-v1-dialing-permissions-dialing-permissions-country-bulk-update
- name: voice.v1.dialing_permissions.dialing_permissions_country-instance
  property_count: 9
  slug: twilio-voice-v1-dialing-permissions-dialing-permissions-country-instance
- name: voice.v1.ip_record
  property_count: 8
  slug: twilio-voice-v1-ip-record
- name: wireless.v1.command
  property_count: 12
  slug: twilio-wireless-v1-command
json_structures:
- name: Twilio Call Structure
  property_count: 0
  slug: twilio-call-structure
- name: Twilio Message Structure
  property_count: 0
  slug: twilio-message-structure
jsonld:
- class_count: 0
  name: Twilio Context
  property_count: 12
  slug: twilio-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Twilio publishes two official Model Context Protocol (MCP) servers. A hosted, read-only documentation/discovery server at https://mcp.twilio.com/docs (Public Beta) that needs no account and exposes tw
  name: Twilio MCP servers (hosted twilio-docs + executing @twilio-alpha/mcp)
  slug: twilio-mcp-servers-hosted-twilio-docs-executing-twilio-alpha-mcp
modified: '2026-10-08'
name: Twilio
nav: Providers
network: true
overview: 'Twilio publishes 153 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2p API, Access Tokens API, Accounts API, and 150 more. Tagged areas include Authentication, Communications, Contact Center, Email, and IoT.


  The Twilio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 5 Spectral governance rulesets.


  Twilio''s developer surface includes sandbox, changelog, CLI, authentication, signup flow, support, engineering blog, and 125 more developer resources.'
plans:
- name: Twilio Plans Pricing
  plan_count: 6
  slug: twilio-plans-pricing
- name: Twilio Price Estimates
  plan_count: 0
  slug: twilio-price-estimates
random_paper: 16
rate_limits:
- limit_count: 3
  name: Twilio Rate Limits
  slug: twilio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Twilio — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: twilio-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Twilio — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: twilio-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Twilio API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 8
  slug: twilio-rules
- authorship: provider
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Twilio — sendgrid oai rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 1
  slug: twilio-sendgrid-oai-spectral-rules
- authorship: provider
  effective_rule_count: 45
  extends:
  - spectral:oas
  name: Twilio — twilio oai rules
  rule_count: 4
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 1
  slug: twilio-twilio-oai-spectral-rules
scopes:
- name: Twilio Scopes
  scope_count: 11
  slug: twilio-scopes
  summary_line: 11 scopes · clientCredentials
score:
  band: exemplar
  composite: 90.3
  coverage:
    artifact_dirs: 45
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 93.4
    contract_governance: 35.6
    contract_quality: 72.8
    developer_ergonomics: 78.6
    discoverability: 81.7
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 93.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 92.8
      derived: 0
      marker_coverage: 22.2
      total: 153
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 70.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/twilio/twilio-2026-11-03T115339.png
security:
- kind: authentication
  name: Twilio Authentication
  slug: twilio-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Twilio Domain Security
  slug: twilio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Twilio Vulnerability Disclosure
  slug: twilio-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Twilio Trust Center
  slug: twilio-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR
skill_count: 6
skills:
- name: twilio-conference-calls
  slug: twilio-conference-calls
- name: twilio-identity-verification-advisor
  slug: twilio-identity-verification-advisor
- name: twilio-lookup-phone-intelligence
  slug: twilio-lookup-phone-intelligence
- name: twilio-security-api-auth
  slug: twilio-security-api-auth
- name: twilio-sendgrid-email-send
  slug: twilio-sendgrid-email-send
- name: twilio-sms-send-message
  slug: twilio-sms-send-message
slug: twilio
tags:
- Authentication
- Communications
- Contact Center
- Email
- IoT
- Messaging
- Phone
- SMS
- T1
- Verification
- Video
- Voice
- Twilio
- Telecommunications
- Real-Time
- WhatsApp
website: https://www.twilio.com/
---
