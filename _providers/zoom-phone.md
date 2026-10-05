---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 242
  human_in_the_loop: 8
  name: Zoom Phone Agentic Access
  operation_count: 419
  slug: zoom-phone-agentic-access
  summary_line: 419 operations · 242 acting · 8 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Accounts API from Zoom Phone — 2 operation(s) for accounts.
  name: Zoom Phone Accounts API
  phrasing_intents:
  - id: listZoomPhoneAccountSettings
    intent: List an account's Zoom Phone settings by type
    question: What Zoom Phone settings are configured for the account, by setting type?
  - id: listCustomizeOutboundCallerNumbers
    intent: List account-level custom caller ID numbers
    question: Which numbers can be shown as our account-level outbound caller ID?
  - id: addOutboundCallerNumbers
    intent: Add account-level custom caller ID numbers
    question: How do I add a number to the account's customized outbound caller ID list?
  - id: deleteOutboundCallerNumbers
    intent: Remove account-level custom caller ID numbers
    question: How do I stop a number being offered as the account's custom caller ID?
  phrasing_ops: 4
  slug: zoom-phone-accounts-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Alerts API from Zoom Phone — 2 operation(s) for alerts.
  name: Zoom Phone Alerts API
  phrasing_intents:
  - id: ListAlertSettingsWithPagingQuery
    intent: List phone alert settings
    question: Which alerts are configured to warn us about call quality or queue problems?
  - id: AddAnAlertSetting
    intent: Create a phone alert setting
    question: Can I get emailed when a call queue crosses a threshold during business hours?
  - id: GetAlertSettingDetails
    intent: Get an alert setting's details
    question: What conditions and recipients does a specific alert setting use?
  - id: DeleteAnAlertSetting
    intent: Delete an alert setting
    question: Can I delete an alert rule that keeps firing for nothing?
  - id: UpdateAnAlertSetting
    intent: Update an alert setting
    question: Can I change the recipients or frequency of an existing alert?
  phrasing_ops: 5
  slug: zoom-phone-alerts-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Audio Library API from Zoom Phone — 3 operation(s) for audio library.
  name: Zoom Phone Audio Library API
  phrasing_intents:
  - id: GetAudioItem
    intent: Get an audio library item
    question: What are the details of one audio file in my phone audio library?
  - id: DeleteAudioItem
    intent: Delete an audio library item
    question: Can I delete a greeting from my phone audio library?
  - id: UpdateAudioItem
    intent: Rename an audio library item
    question: How do I rename an audio file in the library?
  - id: ListAudioItems
    intent: List a user's audio library
    question: Which personal audio files does a user have?
  - id: AddAnAudio
    intent: Create a text-to-speech audio item
    question: Can I generate a greeting from text instead of recording one?
  - id: AddAudioItem
    intent: Upload voice files to the audio library
    question: How do I upload recorded voice files to a user's audio library?
  phrasing_ops: 6
  slug: zoom-phone-audio-library-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Auto Receptionists API from Zoom Phone — 10 operation(s) for auto receptionists.
  name: Zoom Phone Auto Receptionists API
  phrasing_intents:
  - id: listAutoReceptionists
    intent: List auto receptionists
    question: Which auto receptionists are set up in my phone system?
  - id: addAutoReceptionist
    intent: Create an auto receptionist
    question: How do I set up a new auto receptionist to answer calls with a greeting menu?
  - id: getAutoReceptionistDetail
    intent: Get an auto receptionist's details
    question: What extension, timezone and phone numbers does a given auto receptionist have?
  - id: deleteAutoReceptionist
    intent: Delete a non-primary auto receptionist
    question: Can I delete an auto receptionist that is not the primary one?
  - id: updateAutoReceptionist
    intent: Update an auto receptionist
    question: Can I rename an auto receptionist or change its extension number?
  - id: getAutoReceptionistCallHandlingSettings
    intent: Get an auto receptionist's call handling
    question: How does an auto receptionist route callers after hours?
  - id: updateAutoReceptionistCallHandlingSettings
    intent: Update an auto receptionist's call handling
    question: Can I change the greeting an auto receptionist plays during closed hours?
  - id: assignPhoneNumbersAutoReceptionist
    intent: Assign phone numbers to an auto receptionist
    question: How do I point a main company number at an auto receptionist?
  phrasing_ops: 19
  slug: zoom-phone-auto-receptionists-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Billing Account API from Zoom Phone — 2 operation(s) for billing account.
  name: Zoom Phone Billing Account API
  phrasing_intents:
  - id: listBillingAccount
    intent: List billing accounts
    question: Which Zoom Phone billing accounts are available to us?
  - id: GetABillingAccount
    intent: Get a billing account's details
    question: What's in a particular Zoom Phone billing account?
  phrasing_ops: 2
  slug: zoom-phone-billing-account-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Blocked List API from Zoom Phone — 2 operation(s) for blocked list.
  name: Zoom Phone Blocked List API
  phrasing_intents:
  - id: listBlockedList
    intent: List blocked numbers
    question: Which phone numbers are blocked on our account?
  - id: addAnumberToBlockedList
    intent: Block a phone number
    question: How do I stop a spam number from calling our users?
  - id: getABlockedList
    intent: Get a blocked number entry
    question: What are the details of one blocked number entry?
  - id: deleteABlockedList
    intent: Unblock a number by deleting its entry
    question: How do I unblock a number that was blocked by mistake?
  - id: updateBlockedList
    intent: Update a blocked number entry
    question: Can I change a blocked entry from inbound to outbound?
  phrasing_ops: 5
  slug: zoom-phone-blocked-list-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Call Handling API from Zoom Phone — 2 operation(s) for call handling.
  name: Zoom Phone Call Handling API
  phrasing_intents:
  - id: getCallHandling
    intent: Get an extension's call handling settings
    question: How does a call queue or user extension route calls during business, closed and holiday hours?
  - id: addCallHandling
    intent: Add a call handling subsetting to an extension
    question: Can I add a new holiday or forwarding rule to a call queue's call handling?
  - id: deleteCallHandling
    intent: Delete a call handling subsetting from an extension
    question: Can I remove a forwarding destination from an extension's call handling?
  - id: updateCallHandling
    intent: Update an extension's call handling setting
    question: Can I change how a call queue routes callers during closed hours?
  phrasing_ops: 4
  slug: zoom-phone-call-handling-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Call Logs API from Zoom Phone — 15 operation(s) for call logs.
  name: Zoom Phone Call Logs API
  phrasing_intents:
  - id: getCallElement
    intent: Get a call element by ID
    question: Can I look up a single call element, one leg of a call, by its ID?
  - id: accountCallHistory
    intent: List the account's call history (new edition)
    question: Which calls across the whole company went unanswered or to voicemail last month?
  - id: getCallPath
    intent: Get one call history record by UUID
    question: Can I see the full path a call took, every hop, from its call history UUID?
  - id: addClientCodeToCallHistory
    intent: Tag a call history record with a client code
    question: Can I attach a billing client code to a call in the new call history?
  - id: getCallHistoryDetail
    intent: Get call history detail by call history ID
    question: Where do I get the detailed breakdown of a call history entry by its ID?
  - id: accountCallLogs
    intent: List the account's call logs (older edition)
    question: Can I pull every missed call in the account from the older call logs endpoint?
  - id: getCallLogDetails
    intent: Get call log details (older edition)
    question: Can I retrieve a single call log from the older call logs edition?
  - id: addClientCodeToCallLog
    intent: Tag a call log with a client code (older edition)
    question: Can I add a client code to a call in the older call logs edition?
  phrasing_ops: 15
  slug: zoom-phone-call-logs-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Call Queues API from Zoom Phone — 18 operation(s) for call queues.
  name: Zoom Phone Call Queues API
  phrasing_intents:
  - id: callqueueanalytics
    intent: Report call queue analytics for a date range
    question: What does the call queue analytics overview show for last month?
  - id: listCallQueues
    intent: List the call queues on the account
    question: Which call queues are set up in our Zoom Phone account?
  - id: createCallQueue
    intent: Create a call queue
    question: How do I set up a new call queue for our sales team?
  - id: getACallQueue
    intent: Get a call queue's details
    question: What extension and members does a specific call queue have?
  - id: deleteACallQueue
    intent: Delete a call queue
    question: Can I permanently remove a call queue we no longer use?
  - id: updateCallQueue
    intent: Update a call queue's profile
    question: How do I rename a call queue or change its extension?
  - id: getCallQueueCallHandlingSetting
    intent: Get a call queue's call handling for an hour type
    question: What happens to calls into a queue after business hours?
  - id: updateCallQueueCallHandlingSetting
    intent: Change a call queue's call handling for an hour type
    question: How do I change the way a call queue distributes calls during business hours?
  phrasing_ops: 32
  slug: zoom-phone-call-queues-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Carrier Reseller API from Zoom Phone — 2 operation(s) for carrier reseller.
  name: Zoom Phone Carrier Reseller API
  phrasing_intents:
  - id: listCRPhoneNumbers
    intent: List carrier reseller numbers
    question: Which numbers in our carrier reseller master account can be pushed to subaccounts?
  - id: createCRPhoneNumbers
    intent: Add numbers to a carrier reseller account
    question: How do I load new numbers into our carrier reseller master account?
  - id: activeCRPhoneNumbers
    intent: Activate carrier reseller numbers
    question: How do I mark reseller phone numbers as active?
  - id: deleteCRPhoneNumber
    intent: Delete a carrier reseller number
    question: How do I delete or unassign a number from a carrier reseller account?
  phrasing_ops: 4
  slug: zoom-phone-carrier-reseller-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Cloud Peering Provider Exchange API from Zoom Phone — 2 operation(s) for cloud peering provider exchange.
  name: Zoom Phone Cloud Peering Provider Exchange API
  phrasing_intents:
  - id: Listpeeringphonenumbersforprovider
    intent: List numbers a carrier pushed to customers
    question: As a peering carrier, which numbers have I pushed to different Zoom customers?
  - id: listPeeringPhoneNumbers
    intent: List peering numbers provisioned to a customer
    question: Which numbers has our partner provisioned into this Zoom customer account?
  - id: addPeeringPhoneNumbers
    intent: Add peering numbers to a customer account
    question: How does a provider exchange partner add numbers to a customer's Zoom account?
  - id: deletePeeringPhoneNumbers
    intent: Remove peering numbers from a customer account
    question: How do I pull numbers I previously added back out of a customer's account?
  - id: updatePeeringPhoneNumbers
    intent: Update peering numbers in a customer account
    question: How do I change the status of numbers I provisioned through cloud peering?
  phrasing_ops: 5
  slug: zoom-phone-cloud-peering-provider-exchange-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Common Areas API from Zoom Phone — 14 operation(s) for common areas.
  name: Zoom Phone Common Areas API
  phrasing_intents:
  - id: listCommonAreas
    intent: List common area phones
    question: Which common area phones are set up across our account?
  - id: addCommonArea
    intent: Add a common area
    question: How do I set up a shared lobby phone as a common area?
  - id: Generateactivationcodesforcommonareas
    intent: Generate activation codes for common areas
    question: How do I get activation codes so shared phones can sign in as common areas?
  - id: listActivationCodes
    intent: List common area activation codes
    question: Where can I see the activation codes already issued to our common areas?
  - id: ApplyTemplatetoCommonAreas
    intent: Apply a setting template to common areas
    question: Can I push one setting template to many common areas in bulk?
  - id: getACommonArea
    intent: Get a common area's details
    question: What extension and numbers does a particular common area phone have?
  - id: deleteCommonArea
    intent: Delete a common area
    question: Can I remove a common area phone we no longer need?
  - id: updateCommonArea
    intent: Update a common area's profile
    question: How do I change a common area's display name or extension?
  phrasing_ops: 19
  slug: zoom-phone-common-areas-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Dashboard API from Zoom Phone — 11 operation(s) for dashboard.
  name: Zoom Phone Dashboard API
  phrasing_intents:
  - id: listCallLogsMetrics
    intent: List monthly call log metrics
    question: Which calls last month had poor voice quality according to the dashboard?
  - id: getCallQoS
    intent: Get quality of service data for a call
    question: Can I see jitter, packet loss and latency for a specific phone call?
  - id: getCallLogMetricsDetails
    intent: Get dashboard details for one call
    question: Where can I get the dashboard's call details for a single call ID?
  - id: listUserDefaultEmergencyAddress
    intent: List users with a personal default emergency address
    question: Which users rely on their own default emergency address instead of the site address?
  - id: listUserDetectablePersonalLocation
    intent: List users with detectable personal locations
    question: Which users have created personal locations tied to network data for emergency calling?
  - id: listUserLocationSharingPermission
    intent: List users who allow location sharing
    question: Which users have allowed their devices to share location with the Zoom app?
  - id: listUserNomadicEmergencyServices
    intent: List users enabled for nomadic emergency services
    question: Which users are enabled for nomadic emergency services?
  - id: listPhoneRealtimelocation
    intent: List current locations of IP desk phones
    question: Where are our IP desk phones currently detected?
  phrasing_ops: 11
  slug: zoom-phone-dashboard-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Device Line Keys API from Zoom Phone — 1 operation(s) for device line keys.
  name: Zoom Phone Device Line Keys API
  phrasing_intents:
  - id: listDeviceLineKeySetting
    intent: Get a desk phone's line key layout
    question: Which line keys are set up on a shared desk phone, and in what positions?
  - id: batchUpdateDeviceLineKeySetting
    intent: Rearrange a desk phone's line key positions
    question: Can I reorder the line keys on a desk phone in one update?
  phrasing_ops: 2
  slug: zoom-phone-device-line-keys-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Dial by Name Directory API from Zoom Phone — 2 operation(s) for dial by name directory.
  name: Zoom Phone Dial by Name Directory API
  phrasing_intents:
  - id: ListUsersFromDirectory
    intent: List users in or out of the dial-by-name directory
    question: Which users can callers reach by spelling their name in the directory?
  - id: AddUsersToDirectory
    intent: Add users to the dial-by-name directory
    question: Can I make new employees reachable through the dial-by-name directory?
  - id: DeleteUsersFromDirectory
    intent: Remove users from the dial-by-name directory
    question: Can I hide someone from the dial-by-name directory?
  - id: ListUsersFromDirectoryBySite
    intent: List directory users via the site path
    question: Can I list a site's dial-by-name directory members using the site-scoped endpoint?
  - id: AddUsersToDirectoryBySite
    intent: Add users to a site's directory via the site path
    question: Can I add extensions to a specific site's name directory through the site-scoped endpoint?
  - id: DeleteUsersFromDirectoryBySite
    intent: Remove users from a site's directory via the site path
    question: Can I remove extensions from a site's name directory using the site-scoped endpoint?
  phrasing_ops: 6
  slug: zoom-phone-dial-by-name-directory-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Emergency Addresses API from Zoom Phone — 2 operation(s) for emergency addresses.
  name: Zoom Phone Emergency Addresses API
  phrasing_intents:
  - id: listEmergencyAddresses
    intent: List emergency addresses
    question: Which emergency addresses are registered for 911 calls in my account?
  - id: addEmergencyAddress
    intent: Add an emergency address
    question: How do I register a new office address for emergency calling?
  - id: getEmergencyAddress
    intent: Get an emergency address
    question: Can I see the full details of one emergency address by ID?
  - id: deleteEmergencyAddress
    intent: Delete an emergency address
    question: Can I remove an emergency address for an office we closed?
  - id: updateEmergencyAddress
    intent: Update an emergency address
    question: Can I correct the suite number or zip code on an existing emergency address?
  phrasing_ops: 5
  slug: zoom-phone-emergency-addresses-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Emergency Service Locations API from Zoom Phone — 3 operation(s) for emergency service locations.
  name: Zoom Phone Emergency Service Locations API
  phrasing_intents:
  - id: batchAddLocations
    intent: Add emergency service locations in bulk
    question: Can I upload many emergency service locations in one request?
  - id: listLocations
    intent: List emergency service locations
    question: Which emergency service locations are defined on our account?
  - id: addLocation
    intent: Add an emergency service location
    question: How do I add a single emergency location tied to a network?
  - id: getLocation
    intent: Get an emergency service location
    question: What network details does one emergency location use?
  - id: deleteLocation
    intent: Delete an emergency service location
    question: Can I remove an emergency location we no longer use?
  - id: updateLocation
    intent: Update an emergency service location
    question: How do I change the IP range or BSSID of an emergency location?
  phrasing_ops: 6
  slug: zoom-phone-emergency-service-locations-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The External Contacts API from Zoom Phone — 2 operation(s) for external contacts.
  name: Zoom Phone External Contacts API
  phrasing_intents:
  - id: listExternalContacts
    intent: List external contacts
    question: Which external contacts are saved on our phone account?
  - id: addExternalContact
    intent: Add an external contact
    question: How do I add an outside vendor to the phone directory?
  - id: getAExternalContact
    intent: Get an external contact
    question: What numbers and email are stored for one external contact?
  - id: deleteAExternalContact
    intent: Delete an external contact
    question: Can I remove an outside contact from the directory?
  - id: updateExternalContact
    intent: Update an external contact
    question: How do I change an external contact's phone numbers or email?
  phrasing_ops: 5
  slug: zoom-phone-external-contacts-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Fax API from Zoom Phone — 6 operation(s) for fax.
  name: Zoom Phone Fax API
  phrasing_intents:
  - id: UploadFaxFiles
    intent: Upload a file to send as a fax
    question: How do I upload a document before sending it as a fax?
  - id: Getuser'sfaxlogs
    intent: List one extension's fax logs
    question: Which faxes has a particular extension sent or received?
  - id: SendEFax
    intent: Send a fax
    question: How do I send a fax from a Zoom Phone number?
  - id: GetAccount'sFaxLogs
    intent: List fax logs across the account
    question: What faxes were sent and received across the whole account last week?
  - id: GetFaxLogDetails
    intent: Get a fax log's details
    question: What are the details of one specific fax?
  - id: DeleteFaxLog
    intent: Delete a fax log
    question: Can I delete a fax record from the logs?
  - id: UpdateFaxLogReadStatus
    intent: Mark a fax as read or unread
    question: How do I mark a received fax as read?
  - id: Downloadfaxfile
    intent: Download a fax document
    question: How do I download the actual document of a fax I received?
  phrasing_ops: 8
  slug: zoom-phone-fax-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Firmware Update Rules API from Zoom Phone — 3 operation(s) for firmware update rules.
  name: Zoom Phone Firmware Update Rules API
  phrasing_intents:
  - id: ListFirmwareRules
    intent: List firmware update rules
    question: What firmware update rules are set up for our desk phones?
  - id: AddFirmwareRule
    intent: Add a firmware update rule
    question: How do I pin a desk phone model to a specific firmware version?
  - id: GetFirmwareRuleDetail
    intent: Get a firmware update rule
    question: Which firmware version and phone model does a given update rule target?
  - id: DeleteFirmwareUpdateRule
    intent: Delete a firmware update rule
    question: How do I delete a firmware update rule?
  - id: UpdateFirmwareRule
    intent: Change a firmware update rule
    question: Can I change the firmware version an existing rule pushes?
  - id: ListFirmwares
    intent: List available desk phone firmware
    question: Which firmware versions are available to update our desk phones to?
  phrasing_ops: 6
  slug: zoom-phone-firmware-update-rules-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Group Call Pickup API from Zoom Phone — 4 operation(s) for group call pickup.
  name: Zoom Phone Group Call Pickup API
  phrasing_intents:
  - id: listGCP
    intent: List group call pickup groups
    question: Which call pickup groups exist in my phone system?
  - id: addGCP
    intent: Create a group call pickup group
    question: How do I set up a group so coworkers can answer each other's ringing phones?
  - id: GetGCP
    intent: Get a group call pickup group
    question: What extension, delay and sound settings does a pickup group have?
  - id: deleteGCP
    intent: Delete a group call pickup group
    question: Can I remove a call pickup group we no longer need?
  - id: updateGCP
    intent: Update a group call pickup group
    question: Can I rename a pickup group or change its extension number?
  - id: listGCPMembers
    intent: List members of a call pickup group
    question: Who is in a particular call pickup group?
  - id: addGCPMembers
    intent: Add members to a call pickup group
    question: Can I add new teammates to an existing call pickup group?
  - id: removeGCPMembers
    intent: Remove a member from a call pickup group
    question: Can I take one person out of a call pickup group?
  phrasing_ops: 8
  slug: zoom-phone-group-call-pickup-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Groups API from Zoom Phone — 2 operation(s) for groups.
  name: Zoom Phone Groups API
  phrasing_intents:
  - id: GetGroupPolicyDetails
    intent: Get a group's phone policy
    question: What Zoom Phone policy applies to a particular user group?
  - id: updateGroupPolicy
    intent: Update a group's phone policy
    question: How do I change a Zoom Phone policy for one group of users?
  - id: getGroupPhoneSettings
    intent: Get a group's phone settings
    question: What phone settings does a user group have?
  phrasing_ops: 3
  slug: zoom-phone-groups-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Inbound Blocked List API from Zoom Phone — 5 operation(s) for inbound blocked list.
  name: Zoom Phone Inbound Blocked List API
  phrasing_intents:
  - id: ListExtensionLevelInboundBlockRules
    intent: List an extension's inbound block rules
    question: Which numbers are blocked from calling or texting a particular call queue or user?
  - id: AddExtensiontLevelInboundBlockRules
    intent: Block an inbound number for one extension
    question: Can I block a spam number from reaching just one user or call queue?
  - id: DeleteExtensiontLevelInboundBlockRules
    intent: Delete an extension's inbound block rule
    question: Can I unblock a number that was blocked only for a single extension?
  - id: ListAccountLevelInboundBlockedStatistics
    intent: List statistics of extension-level blocked numbers
    question: Which numbers are being blocked by many extensions across the account?
  - id: DeleteAccountLevelInboundBlockedStatistics
    intent: Delete an inbound blocked statistic
    question: Can I clear a blocked-number statistic entry from the extension rollup?
  - id: MarkPhoneNumberAsBlockedForAllExtensions
    intent: Promote a blocked number to block all extensions
    question: Can I take a number one extension blocked and block it for everyone in the account?
  - id: ListAccountLevelInboundBlockRules
    intent: List account-wide inbound block rules
    question: Which numbers are blocked company-wide from calling or texting us?
  - id: AddAccountLevelInboundBlockRules
    intent: Block an inbound number for the whole account
    question: How do I block a robocaller from reaching every extension in the company?
  phrasing_ops: 10
  slug: zoom-phone-inbound-blocked-list-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The IVR API from Zoom Phone — 1 operation(s) for ivr.
  name: Zoom Phone IVR API
  phrasing_intents:
  - id: getAutoReceptionistIVR
    intent: Get an auto receptionist's IVR menu
    question: What key-press options does our main auto receptionist offer?
  - id: updateAutoReceptionistIVR
    intent: Update an auto receptionist's IVR menu
    question: How do I change what pressing a key does in our phone menu?
  phrasing_ops: 2
  slug: zoom-phone-ivr-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Line Keys API from Zoom Phone — 2 operation(s) for line keys.
  name: Zoom Phone Line Keys API
  phrasing_intents:
  - id: listLineKeySetting
    intent: Get an extension's line key layout
    question: What is assigned to each line key on a user's desk phone?
  - id: BatchUpdateLineKeySetting
    intent: Rearrange an extension's line keys
    question: How do I change the order of line keys on a desk phone?
  - id: DeleteLineKey
    intent: Delete a line key
    question: Can I remove a single line key from a desk phone?
  phrasing_ops: 3
  slug: zoom-phone-line-keys-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Monitoring Groups API from Zoom Phone — 4 operation(s) for monitoring groups.
  name: Zoom Phone Monitoring Groups API
  phrasing_intents:
  - id: listMonitoringGroup
    intent: List monitoring groups
    question: Which monitoring groups are set up for supervisors on our account?
  - id: createMonitoringGroup
    intent: Create a monitoring group
    question: How do I let supervisors listen in or barge into agents' calls?
  - id: getMonitoringGroupById
    intent: Get a monitoring group's details
    question: What privileges and prompt does a particular monitoring group have?
  - id: deleteMonitoringGroup
    intent: Delete a monitoring group
    question: Can I delete a monitoring group altogether?
  - id: updateMonitoringGroup
    intent: Update a monitoring group
    question: How do I change what supervisors in a monitoring group are allowed to do?
  - id: listMembers
    intent: List monitors or monitored members of a group
    question: Who are the supervisors in a monitoring group?
  - id: addMembers
    intent: Add members to a monitoring group
    question: How do I add supervisors to a monitoring group?
  - id: removeMembers
    intent: Remove all monitors or monitored members
    question: Can I clear every supervisor out of a monitoring group in one go?
  phrasing_ops: 9
  slug: zoom-phone-monitoring-groups-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Outbound Calling API from Zoom Phone — 12 operation(s) for outbound calling.
  name: Zoom Phone Outbound Calling API
  phrasing_intents:
  - id: GetCommonAreaOutboundCallingCountriesAndRegions
    intent: See which countries a common area phone can call
    question: Which countries and regions is the lobby common area phone allowed to dial out to?
  - id: UpdateCommonAreaOutboundCallingCountriesOrRegions
    intent: Change a common area's allowed calling countries
    question: How do I block international dialing to certain countries from a common area phone?
  - id: listCommonAreaOutboundCallingExceptionRule
    intent: List a common area's outbound calling exceptions
    question: What outbound calling exception rules are set on a common area phone?
  - id: AddCommonAreaOutboundCallingExceptionRule
    intent: Add an outbound calling exception to a common area
    question: How do I let a common area phone dial one specific number prefix in an otherwise blocked country?
  - id: deleteCommonAreaOutboundCallingExceptionRule
    intent: Delete a common area's outbound calling exception
    question: How do I remove a calling exception rule from a common area phone?
  - id: UpdateCommonAreaOutboundCallingExceptionRule
    intent: Edit a common area's outbound calling exception
    question: Can I change the number pattern on an existing common area calling exception?
  - id: GetAccountOutboundCallingCountriesAndRegions
    intent: See account-wide allowed calling countries
    question: Which countries can our whole Zoom Phone account place outbound calls to?
  - id: UpdateAccountOutboundCallingCountriesOrRegions
    intent: Change account-wide allowed calling countries
    question: How do I block outbound calls to a country for everyone on the account?
  phrasing_ops: 24
  slug: zoom-phone-outbound-calling-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Phone Devices API from Zoom Phone — 8 operation(s) for phone devices.
  name: Zoom Phone Devices API
  phrasing_intents:
  - id: listPhoneDevices
    intent: List desk phone devices
    question: Which desk phones on our account are still unassigned?
  - id: addPhoneDevice
    intent: Add a desk phone
    question: How do I register a new desk phone by its MAC address?
  - id: syncPhoneDevice
    intent: Resync zero-touch desk phones
    question: How do I push a resync to all our zero-touch provisioned desk phones?
  - id: getADevice
    intent: Get a desk phone's details
    question: What model, status and assignee does a specific desk phone have?
  - id: deleteADevice
    intent: Remove a desk phone or ATA
    question: How do I remove a desk phone or analog adapter from Zoom Phone?
  - id: updateADevice
    intent: Update a desk phone
    question: How do I rename a desk phone?
  - id: addExtensionsToADevice
    intent: Assign users or common areas to a desk phone
    question: How do I share one desk phone between several extensions?
  - id: deleteExtensionFromADevice
    intent: Unassign an extension from a desk phone
    question: How do I take one user off a shared desk phone?
  phrasing_ops: 11
  slug: zoom-phone-phone-devices-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Phone Numbers API from Zoom Phone — 10 operation(s) for phone numbers.
  name: Zoom Phone Numbers API
  phrasing_intents:
  - id: addBYOCNumber
    intent: Add bring-your-own-carrier numbers to Zoom Phone
    question: How do I bring my own carrier's phone numbers into Zoom Phone?
  - id: listAccountPhoneNumbers
    intent: List the account's Zoom Phone numbers
    question: Which Zoom Phone numbers in our account are still unassigned?
  - id: deleteUnassignedPhoneNumbers
    intent: Delete unassigned Zoom Phone numbers
    question: How do I release Zoom Phone numbers nobody is using?
  - id: updateSiteForUnassignedPhoneNumbers
    intent: Move unassigned numbers to a site
    question: How do I move spare phone numbers from one site to another?
  - id: getPhoneNumberDetails
    intent: Get a Zoom Phone number's details
    question: Who is a specific Zoom Phone number assigned to?
  - id: updatePhoneNumberDetails
    intent: Update a Zoom Phone number
    question: How do I set a Zoom Phone number to SMS-only or voice-only capability?
  - id: assignPhoneNumber
    intent: Assign a phone number to a user
    question: How do I give a Zoom Phone user a direct phone number?
  - id: UnassignPhoneNumber
    intent: Unassign a phone number from a user
    question: How do I take a phone number away from a Zoom Phone user?
  phrasing_ops: 14
  slug: zoom-phone-phone-numbers-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Phone Plan API from Zoom Phone — 1 operation(s) for phone plan.
  name: Zoom Phone Plan API
  phrasing_intents:
  - id: Listphonenumberplaninformation
    intent: Get phone number plan usage and availability
    question: How many phone numbers does our plan include, and how many are still available?
  phrasing_ops: 1
  slug: zoom-phone-phone-plan-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Phone Plans API from Zoom Phone — 2 operation(s) for phone plans.
  name: Zoom Phone Plans API
  phrasing_intents:
  - id: listCallingPlans
    intent: List calling plans
    question: Which Zoom Phone calling plans does our account have?
  - id: listPhonePlans
    intent: List phone plan packages and number usage
    question: What Zoom Phone plan packages do we have, and how many phone numbers are used?
  phrasing_ops: 2
  slug: zoom-phone-phone-plans-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Phone Roles API from Zoom Phone — 4 operation(s) for phone roles.
  name: Zoom Phone Roles API
  phrasing_intents:
  - id: ListPhoneRoles
    intent: List phone roles
    question: Which phone admin roles exist in our account?
  - id: DuplicatePhoneRole
    intent: Duplicate a phone role
    question: Can I create a new phone role by copying an existing one?
  - id: getRoleInformation
    intent: Get a phone role's details
    question: What does a particular phone role include?
  - id: DeletePhoneRole
    intent: Delete a phone role
    question: Can I delete a phone role we no longer use?
  - id: UpdatePhoneRole
    intent: Rename or redescribe a phone role
    question: How do I rename a phone role?
  - id: ListRoleMembers
    intent: List users in or not in a phone role
    question: Who is assigned to a given phone role?
  - id: AddRoleMembers
    intent: Add users to a phone role
    question: How do I assign users to a phone role?
  - id: DelRoleMembers
    intent: Remove users from a phone role
    question: Can I take users out of a phone role?
  phrasing_ops: 11
  slug: zoom-phone-phone-roles-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Private Directory API from Zoom Phone — 2 operation(s) for private directory.
  name: Zoom Phone Private Directory API
  phrasing_intents:
  - id: listPrivateDirectoryMembers
    intent: List private directory members
    question: Who is hidden in our private phone directory?
  - id: addMembersToAPrivateDirectory
    intent: Add members to the private directory
    question: How do I hide executives' extensions in a private directory?
  - id: removeAMemberFromAPrivateDirectory
    intent: Remove a member from the private directory
    question: Can I take someone out of the private directory?
  - id: updateAPrivateDirectoryMember
    intent: Change a private member's web portal visibility
    question: Can a private directory member still be searchable on the web portal?
  phrasing_ops: 4
  slug: zoom-phone-private-directory-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Provider Exchange API from Zoom Phone — 2 operation(s) for provider exchange.
  name: Zoom Phone Provider Exchange API
  phrasing_intents:
  - id: listCarrierPeeringPhoneNumbers
    intent: List numbers a carrier pushed via phone peering
    question: Which numbers has my carrier pushed to Zoom customers under the phone peering endpoint?
  - id: listPeeringPhoneNumbers
    intent: List Provider Exchange peering numbers
    question: What numbers have we sent to Zoom through the Provider Exchange?
  - id: addPeeringPhoneNumbers
    intent: Add numbers through the Provider Exchange
    question: How does a peering partner add phone numbers to Zoom via the Provider Exchange?
  - id: deletePeeringPhoneNumbers
    intent: Remove numbers from the Provider Exchange
    question: How do I withdraw numbers we added to Zoom through the Provider Exchange?
  - id: updatePeeringPhoneNumbers
    intent: Update numbers in the Provider Exchange
    question: Can I update numbers already sent to Zoom via the Provider Exchange?
  phrasing_ops: 5
  slug: zoom-phone-provider-exchange-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Provision Templates API from Zoom Phone — 2 operation(s) for provision templates.
  name: Zoom Phone Provision Templates API
  phrasing_intents:
  - id: listAccountProvisionTemplate
    intent: List desk phone provision templates
    question: Which provision templates exist for configuring our desk phones?
  - id: addProvisionTemplate
    intent: Create a provision template
    question: How do I create a template to push the same config to many desk phones?
  - id: GetProvisionTemplate
    intent: Get a provision template
    question: What configuration content does a specific provision template contain?
  - id: deleteProvisionTemplate
    intent: Delete a provision template
    question: Can I delete a provision template we no longer use?
  - id: updateProvisionTemplate
    intent: Update a provision template
    question: Can I rename a provision template or edit its description?
  phrasing_ops: 5
  slug: zoom-phone-provision-templates-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Recordings API from Zoom Phone — 8 operation(s) for recordings.
  name: Zoom Phone Recordings API
  phrasing_intents:
  - id: getPhoneRecordingByCallElementId
    intent: Get the recording for a call element
    question: Can I fetch the recording attached to one specific leg of a call?
  - id: getPhoneRecordingsByCallIdOrCallLogId
    intent: Get a recording by call ID or call log ID
    question: Can I find the recording and its file URL from a call ID or call log ID?
  - id: phoneDownloadRecordingFile
    intent: Download a call recording file
    question: Can I download the audio file of a phone recording?
  - id: phoneDownloadRecordingTranscript
    intent: Download a call recording transcript
    question: Can I get the text transcript of a recorded phone call?
  - id: getPhoneRecordings
    intent: List call recordings across the account
    question: Which calls were recorded across the company last month?
  - id: deleteCallRecording
    intent: Delete a call recording
    question: Can I delete a call recording that shouldn't have been kept?
  - id: UpdateAutoDeleteField
    intent: Turn auto delete on or off for a recording
    question: Can I exempt one recording from automatic deletion after the retention period?
  - id: UpdateRecordingStatus
    intent: Recover a recording from the trash
    question: Can I restore a call recording that was moved to the trash?
  phrasing_ops: 9
  slug: zoom-phone-recordings-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Reports API from Zoom Phone — 4 operation(s) for reports.
  name: Zoom Phone Reports API
  phrasing_intents:
  - id: GetCallChargesUsageReport
    intent: Get the monthly call charges report
    question: How much did our phone calls cost last month?
  - id: Getfaxchargesusagereport
    intent: Get the monthly fax charges report
    question: What did we spend on faxes through the phone system this month?
  - id: getPSOperationLogs
    intent: Get the phone system admin operation logs
    question: Which admin changed phone system settings, and when?
  - id: GetSMSChargesUsageReport
    intent: Get the monthly SMS/MMS charges report
    question: How much are we paying for text messages each month?
  phrasing_ops: 4
  slug: zoom-phone-reports-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Routing Rules API from Zoom Phone — 2 operation(s) for routing rules.
  name: Zoom Phone Routing Rules API
  phrasing_intents:
  - id: listRoutingRule
    intent: List directory backup routing rules
    question: Which backup routing rules apply when a dialed number matches no user?
  - id: addRoutingRule
    intent: Add a directory backup routing rule
    question: How do I route unmatched dialed numbers to a SIP group with a regex?
  - id: getRoutingRule
    intent: Get a directory backup routing rule
    question: What pattern and translation does one backup routing rule use?
  - id: deleteRoutingRule
    intent: Delete a directory backup routing rule
    question: Can I remove a backup routing rule we no longer need?
  - id: updateRoutingRule
    intent: Update a directory backup routing rule
    question: How do I change the regex pattern of a backup routing rule?
  phrasing_ops: 5
  slug: zoom-phone-routing-rules-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Setting API from Zoom Phone — 4 operation(s) for setting.
  name: Zoom Phone Setting API
  phrasing_intents:
  - id: Listportednumbers
    intent: List port orders in number management
    question: Which numbers have we ported, as recorded in number management?
  - id: Getportednumbersdetails
    intent: Get a port order from number management
    question: What's the status of one port order according to number management?
  - id: ListSIPgroups
    intent: List SIP groups for a product
    question: Which SIP groups exist for a given product in number management?
  - id: ListBYOCSIPtrunks
    intent: List BYOC SIP trunks for a product
    question: Which BYOC SIP trunks are assigned for a particular product?
  phrasing_ops: 4
  slug: zoom-phone-setting-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Setting Templates API from Zoom Phone — 2 operation(s) for setting templates.
  name: Zoom Phone Setting Templates API
  phrasing_intents:
  - id: listSettingTemplates
    intent: List phone setting templates
    question: Which phone setting templates have been created?
  - id: addSettingTemplate
    intent: Create a phone setting template
    question: How do I create a template of default phone settings?
  - id: getSettingTemplate
    intent: Get a setting template's details
    question: What settings does a particular phone template define?
  - id: updateSettingTemplate
    intent: Update a phone setting template
    question: How do I change the policy or user settings in a phone template?
  phrasing_ops: 4
  slug: zoom-phone-setting-templates-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Settings API from Zoom Phone — 6 operation(s) for settings.
  name: Zoom Phone Settings API
  phrasing_intents:
  - id: GetAccountPolicyDetails
    intent: Get an account-level phone policy
    question: What is our account-wide Zoom Phone policy for a given policy type?
  - id: updateAccountPolicy
    intent: Update an account-level phone policy
    question: How do I change a Zoom Phone policy for the whole account?
  - id: listPortedNumbers
    intent: List number port orders
    question: Which numbers have we ported into Zoom Phone, and what's their order status?
  - id: getPortedNumbersDetails
    intent: Get a number port order's details
    question: What's the status of a specific number porting order?
  - id: phoneSetting
    intent: Get Zoom Phone account settings
    question: Is BYOC or multiple sites turned on for our Zoom Phone account?
  - id: updatePhoneSettings
    intent: Update Zoom Phone account settings
    question: How do I enable multiple sites on our Zoom Phone account?
  - id: listSipGroups
    intent: List SIP groups
    question: Which SIP groups exist on our Zoom Phone account?
  - id: listBYOCSIPTrunk
    intent: List BYOC SIP trunks
    question: Which bring-your-own-carrier SIP trunks are assigned to our account?
  phrasing_ops: 8
  slug: zoom-phone-settings-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Shared Line Appearance API from Zoom Phone — 1 operation(s) for shared line appearance.
  name: Zoom Phone Shared Line Appearance API
  phrasing_intents:
  - id: listSharedLineAppearances
    intent: List shared line appearances
    question: Which users share line appearances with others on our account?
  phrasing_ops: 1
  slug: zoom-phone-shared-line-appearance-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Shared Line Group API from Zoom Phone — 13 operation(s) for shared line group.
  name: Zoom Phone Shared Line Group API
  phrasing_intents:
  - id: listSharedLineGroups
    intent: List shared line groups
    question: Which shared line groups are set up on our Zoom Phone account?
  - id: createASharedLineGroup
    intent: Create a shared line group
    question: How do I set up a shared line so a team can answer one phone number together?
  - id: getASharedLineGroup
    intent: Get a shared line group's details
    question: What members and numbers belong to a particular shared line group?
  - id: getSharedLineGroupCallHandlingSetting
    intent: Get a shared line group's call handling
    question: How are calls routed to a shared line group after business hours?
  - id: updateSharedLineGroupCallHandlingSetting
    intent: Change a shared line group's call handling
    question: How do I change where a shared line group's calls go during closed hours?
  - id: getSharedLineGroupPolicy
    intent: Get a shared line group's policy
    question: What policy settings apply to a shared line group, like voicemail access?
  - id: updateSharedLineGroupPolicy
    intent: Update a shared line group's policy
    question: How do I let members check a shared line group's voicemail by phone?
  - id: getSharedLineGroupSettings
    intent: Get a shared line group's settings
    question: What settings are configured on a shared line group, by setting type?
  phrasing_ops: 22
  slug: zoom-phone-shared-line-group-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Sites API from Zoom Phone — 4 operation(s) for sites.
  name: Zoom Phone Sites API
  phrasing_intents:
  - id: listPhoneSites
    intent: List phone sites
    question: Which phone sites does our Zoom Phone account have?
  - id: createPhoneSite
    intent: Create a phone site
    question: How do I add a new office location as a phone site?
  - id: getASite
    intent: Get a phone site's details
    question: What are the details of one phone site, like its site code?
  - id: deletePhoneSite
    intent: Delete a phone site and move its assets
    question: Can I delete a phone site and move its users and numbers elsewhere?
  - id: updateSiteDetails
    intent: Update a phone site's details
    question: How do I rename a phone site or change its site code?
  - id: listSiteCustomizeOutboundCallerNumbers
    intent: List a site's custom outbound caller ID numbers
    question: Which numbers can be used as a site-level custom outbound caller ID?
  - id: addSiteOutboundCallerNumbers
    intent: Add custom outbound caller ID numbers to a site
    question: How do I add numbers to a site's custom outbound caller ID list?
  - id: deleteSiteOutboundCallerNumbers
    intent: Remove custom outbound caller ID numbers from a site
    question: Can I take numbers off a site's custom outbound caller ID list?
  phrasing_ops: 12
  slug: zoom-phone-sites-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The SMS API from Zoom Phone — 7 operation(s) for sms.
  name: Zoom Phone SMS API
  phrasing_intents:
  - id: postSmsMessage
    intent: Send an SMS or MMS message
    question: Can I send a text message from a Zoom Phone number to a customer?
  - id: accountSmsSession
    intent: List SMS conversations across the account
    question: Which text conversations happened across the whole company this month?
  - id: smsSessionDetails
    intent: Get the messages in an SMS session
    question: Can I read the full message thread of one SMS conversation?
  - id: smsByMessageId
    intent: Get one SMS message by ID
    question: Can I look up a single text message inside a conversation?
  - id: smsSessionSync
    intent: Sync the messages in an SMS session
    question: Can I fetch only new messages in a conversation since my last sync?
  - id: userSmsSession
    intent: List a user's SMS conversations
    question: Which text conversations does a specific user have?
  - id: GetSmsSessions
    intent: Sync a user's SMS sessions newest first
    question: Can I get a user's conversations ordered most recent first, like the phone app shows?
  phrasing_ops: 7
  slug: zoom-phone-sms-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The SMS Campaign API from Zoom Phone — 6 operation(s) for sms campaign.
  name: Zoom Phone SMS Campaign API
  phrasing_intents:
  - id: listAccountSMSCampaigns
    intent: List SMS campaigns
    question: What 10DLC SMS campaigns are registered on our account?
  - id: GetSMSCampaign
    intent: Get an SMS campaign
    question: What are the details and numbers of a particular SMS campaign?
  - id: assignCampaignPhoneNumbers
    intent: Assign phone numbers to an SMS campaign
    question: How do I add our numbers to a 10DLC SMS campaign?
  - id: getNumberCampaignOptStatus
    intent: Check opt-in status for an SMS campaign
    question: Has a customer opted out of a specific SMS campaign's numbers?
  - id: updateNumberCampaignOptStatus
    intent: Opt a consumer in or out of an SMS campaign
    question: How do I record that a customer opted out of our campaign texts?
  - id: unassignCampaignPhoneNumber
    intent: Remove a number from an SMS campaign
    question: How do I take a phone number out of an SMS campaign?
  - id: getUserNumberCampaignOptStatus
    intent: Check a user's numbers' campaign opt statuses
    question: Which consumers have opted out of texts from my own Zoom Phone numbers?
  phrasing_ops: 7
  slug: zoom-phone-sms-campaign-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The SMS Campaigns API from Zoom Phone — 3 operation(s) for sms campaigns.
  name: Zoom Phone SMS Campaigns API
  phrasing_intents:
  - id: listAccountSMSCampaigns
    intent: List SMS campaigns
    question: Which 10DLC SMS campaigns are registered on my account?
  - id: GetSMSCampaign
    intent: Get an SMS campaign
    question: What is the status and phone number list of a specific SMS campaign?
  - id: assignCampaignPhoneNumbers
    intent: Assign phone numbers to an SMS campaign
    question: How do I attach our business numbers to a 10DLC campaign so they can text?
  - id: unassignCampaignPhoneNumber
    intent: Unassign phone numbers from an SMS campaign
    question: Can I pull a phone number out of a 10DLC campaign?
  phrasing_ops: 4
  slug: zoom-phone-sms-campaigns-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The SMS Consent API from Zoom Phone — 4 operation(s) for sms consent.
  name: Zoom Phone SMS Consent API
  phrasing_intents:
  - id: getNumberConsentOptStatus
    intent: Check opt-in status under an SMS consent policy
    question: Has a customer opted out of texts from our numbers under a consent policy?
  - id: ListSMSConsents
    intent: List SMS consent policies
    question: What SMS consent policies does our account have?
  - id: CreateSMSConsent
    intent: Create an SMS consent policy
    question: How do I set up opt-in, opt-out and help messages for business texting?
  - id: DeleteSMSConsents
    intent: Delete SMS consent policies
    question: How do I delete consent policies we no longer use?
  - id: GetSMSConsent
    intent: Get an SMS consent policy
    question: What opt-in and opt-out settings does a particular consent policy have?
  - id: UpdateSMSConsent
    intent: Update an SMS consent policy
    question: How do I rename or deactivate an SMS consent policy?
  - id: ListConsentPhoneNumbers
    intent: List numbers under an SMS consent policy
    question: Which of our phone numbers are covered by a given SMS consent policy?
  - id: AssignPhoneNumbersToConsent
    intent: Assign numbers to an SMS consent policy
    question: How do I put more of our numbers under an SMS consent policy?
  phrasing_ops: 9
  slug: zoom-phone-sms-consent-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Users API from Zoom Phone — 13 operation(s) for users.
  name: Zoom Phone Users API
  phrasing_intents:
  - id: listPhoneUsers
    intent: List users who have a Zoom Phone license
    question: Which people in my account have a Zoom Phone license assigned?
  - id: updateUsersPropertiesInBatch
    intent: Move or activate several phone users at once
    question: Can I move up to ten phone users to a different site in one request?
  - id: batchAddUsers
    intent: Add up to ten phone users in one batch
    question: Can I onboard several existing Zoom users onto the phone system at the same time?
  - id: phoneUser
    intent: Get a user's Zoom Phone profile
    question: Where can I see a user's phone profile, like their extension, site and calling plan?
  - id: updateUserProfile
    intent: Update a user's phone profile
    question: Can I change a user's phone extension number or move them to another site?
  - id: addUserCallForwardSetting
    intent: Add call forwarding numbers for a user
    question: Can I forward a user's incoming calls to an external number during closed hours?
  - id: deleteUserCallForwardSetting
    intent: Remove call forwarding numbers from a user
    question: Can I stop a user's calls from forwarding to an external number for a given hour type?
  - id: getUserCallHandlingSetting
    intent: Get a user's call handling setting
    question: How are a user's incoming calls routed during business hours versus closed hours?
  phrasing_ops: 24
  slug: zoom-phone-users-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Voicemails API from Zoom Phone — 6 operation(s) for voicemails.
  name: Zoom Phone Voicemails API
  phrasing_intents:
  - id: getVoicemailDetailsByCallElementId
    intent: Get a voicemail by call element
    question: Can I find the voicemail left during a specific call element?
  - id: getVoicemailDetailsByCallIdOrCallLogId
    intent: Get the voicemail from a user's call log
    question: Did a caller leave a voicemail on a call in my call history?
  - id: phoneUserVoiceMails
    intent: List a user's voicemails
    question: What voicemails are in a user's mailbox?
  - id: accountVoiceMails
    intent: List voicemails across the account
    question: Which voicemails have been left anywhere on the account?
  - id: phoneDownloadVoicemailFile
    intent: Download a voicemail audio file
    question: How do I download the audio of a voicemail?
  - id: getVoicemailDetails
    intent: Get a voicemail's details
    question: What are the details of one voicemail message?
  - id: deleteVoicemail
    intent: Delete a voicemail
    question: Can I delete a voicemail message from the account?
  - id: updateVoicemailReadStatus
    intent: Mark a voicemail as read or unread
    question: How do I mark a voicemail as read?
  phrasing_ops: 8
  slug: zoom-phone-voicemails-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Zoom Rooms API from Zoom Phone — 7 operation(s) for zoom rooms.
  name: Zoom Phone Zoom Rooms API
  phrasing_intents:
  - id: listZoomRooms
    intent: List Zoom Rooms with a Zoom Phone license
    question: Which Zoom Rooms already have Zoom Phone enabled?
  - id: addZoomRoom
    intent: Add a Zoom Room to Zoom Phone
    question: How do I turn on Zoom Phone for a conference room?
  - id: listUnassignedZoomRooms
    intent: List Zoom Rooms without Zoom Phone
    question: Which Zoom Rooms don't have a phone assigned yet?
  - id: getZoomRoom
    intent: Get a Zoom Room's phone setup
    question: What extension, numbers and calling plans does a Zoom Room have?
  - id: RemoveZoomRoom
    intent: Remove a Zoom Room from Zoom Phone
    question: How do I turn off Zoom Phone for a conference room?
  - id: updateZoomRoom
    intent: Update a Zoom Room's phone settings
    question: How do I change a Zoom Room's phone extension?
  - id: assignCallingPlanToRoom
    intent: Assign calling plans to a Zoom Room
    question: How do I give a conference room an international calling plan?
  - id: unassignCallingPlanFromRoom
    intent: Remove a calling plan from a Zoom Room
    question: How do I take a calling plan off a Zoom Room?
  phrasing_ops: 10
  slug: zoom-phone-zoom-rooms-api
artifact_total: 64
asyncapis:
- description: ''
  name: Zoom Phone Webhooks
  slug: zoom-phone-webhooks
collections:
- collection_type: open
  name: Phone
  slug: open-zoom-phone-api
- collection_type: open
  name: Number Management
  slug: open-zoom-phone-number-management
- collection_type: open
  name: Phone
  slug: open-zoom-phone-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/plans/zoom-phone-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zoom-phone-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/capabilities/zoom-phone-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zoom-phone-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/agentic-access/zoom-phone-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zoom-phone-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/security/zoom-phone-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zoom-phone-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/security/zoom-phone-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoom-phone-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/security/zoom-phone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zoom-phone-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/authentication/zoom-phone-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zoom-phone-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/scopes/zoom-phone-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zoom-phone-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoom.com/en/products/voip-phone/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zoom.us/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zoom.us/docs/api/phone/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.zoom.us/docs/integrations/oauth/
- group: design
  title: ''
  type: OAuthMetadata
  url: https://zoom.us/.well-known/oauth-authorization-server
- group: commercial
  title: ''
  type: Pricing
  url: https://zoom.us/pricing/zoom-phone
- group: other
  title: ''
  type: AppMarketplace
  url: https://marketplace.zoom.us/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/zoom-developer/zoom-public-workspace/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoom
- group: build
  title: ''
  type: SDK
  url: https://github.com/zoom/rivet-javascript
- group: company
  title: ''
  type: Blog
  url: https://developers.zoom.us/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.zoomstatus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zoom.us/docs/api/phone/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zoom.us/docs/phone/start/
- group: start
  title: ''
  type: Quickstart
  url: https://developers.zoom.us/docs/phone/first-app/
- group: operate
  title: ''
  type: Support
  url: https://developers.zoom.us/support/
- group: operate
  title: ''
  type: Community
  url: https://devforum.zoom.us/
- group: start
  title: ''
  type: SignUp
  url: https://zoom.us/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoom.com/en/trust/terms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zoom.us/docs/en-us/zoom_api_license_and_tou.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoom.com/en/trust/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zoom-developer/zoom-public-workspace/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.zoom.us/changelog/?product=phone
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoom.us/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.zoom.us/docs/build/lifecycle/
- group: auth
  title: ''
  type: Security
  url: https://www.zoom.com/en/trust/reporting-vulnerability/
- group: auth
  title: ''
  type: Compliance
  url: https://www.zoom.com/en/trust/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/packages/zoom-phone-packages.yml
  title: ''
  type: SDKs
  url: packages/zoom-phone-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/mcp/zoom-phone-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zoom-phone-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/packages/zoom-phone-packages.yml
  title: ''
  type: Packages
  url: packages/zoom-phone-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/well-known/zoom-phone-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zoom-phone-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/well-known/zoom-phone-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zoom-phone-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/well-known/zoom-phone-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/zoom-phone-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/mcp/zoom-phone-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/zoom-phone-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/llms/zoom-phone-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zoom-phone-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/overlays/zoom-phone-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoom-phone-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/overlays/zoom-phone-number-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoom-phone-number-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/overlays/zoom-phone-webhooks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoom-phone-webhooks-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/conformance/zoom-phone-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zoom-phone-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/errors/zoom-phone-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zoom-phone-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/lifecycle/zoom-phone-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zoom-phone-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/changelog/zoom-phone-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zoom-phone-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/conventions/zoom-phone-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zoom-phone-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/rate-limits/zoom-phone-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zoom-phone-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/components/zoom-phone-components.yml
  title: ''
  type: Components
  url: components/zoom-phone-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/data-model/zoom-phone-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zoom-phone-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/asyncapi/zoom-phone-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zoom-phone-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-25'
description: 'Zoom Phone is the cloud PBX / UCaaS voice product of Zoom Communications, headquartered in San Jose, California, and sold worldwide from its United States home market. It replaces on-premise telephony with a cloud calling service — extensions, auto receptionists, IVR, call queues, shared line groups, voicemail, call recording, fax, emergency (E911) addressing, and SMS/MMS — delivered either on Zoom-provided PSTN service, on a customer''s own carrier through BYOC and Cloud Peering (Provider Exchange), or resold through carrier partners. In the telecom value chain Zoom Phone sits above the network as a UCaaS application layer that buys wholesale connectivity and number inventory from carriers rather than operating a mobile network, and its API posture reflects the software half of that split rather than the carrier half: the Zoom Phone API is fully self-serve, published as downloadable OpenAPI 3.0 with 391 documented operations across 46 resource groups, a 71-event webhook catalog,
  a separate Number Management API covering number allocation, BYOC numbers, ported number orders, SIP trunks and 10DLC SMS campaigns, OAuth 2.0 with fine-grained phone:* scopes, a public Postman workspace, and an official Node/TypeScript SDK. It is not a mobile network operator, is not a GSMA Open Gateway signatory, and exposes no CAMARA network APIs — no CAMARA reference was found anywhere in its developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Zoom operates a fleet of first-party hosted MCP servers at mcp.zoom.us, advertised through an MCP server card at /.well-known/mcp/server-card.json on the developer host and published to the official M
  name: Zoom MCP Server (Workspace)
  slug: zoom-mcp-server-workspace
modified: '2026-09-16'
name: Zoom Phone
nav: Providers
network: true
overview: 'Zoom Phone publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Alerts API, Audio Library API, and 48 more. Tagged areas include Telecommunications, United States, UCaaS, Cloud PBX, and Voice.


  The Zoom Phone catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zoom Phone''s developer surface includes authentication, documentation, pricing, SDKs, engineering blog, API reference, getting-started guide, and 49 more developer resources.'
plans:
- name: Zoom Phone Plans Pricing
  plan_count: 0
  slug: zoom-phone-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Zoom Phone Rate Limits
  slug: zoom-phone-rate-limits
scopes:
- name: Zoom Phone Scopes
  scope_count: 435
  slug: zoom-phone-scopes
  summary_line: 435 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 62.9
    developer_ergonomics: 73.8
    discoverability: 75.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 67.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 49.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/zoom-phone/refs/heads/main/screenshots/zoom-phone-2026-08-17T080441.png
security:
- kind: authentication
  name: Zoom Phone Authentication
  slug: zoom-phone-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Zoom Phone Domain Security
  slug: zoom-phone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoom Phone Vulnerability Disclosure
  slug: zoom-phone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zoom Phone Trust Center
  slug: zoom-phone-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, CSA STAR
slug: zoom-phone
tags:
- Telecommunications
- United States
- UCaaS
- Cloud PBX
- Voice
- VoIP
- SIP
- Messaging
- SMS
- Phone Numbers
- Number Porting
- BYOC
- Carrier Peering
- Contact Center
- Communications
website: https://www.zoom.com/en/products/voip-phone/
---
