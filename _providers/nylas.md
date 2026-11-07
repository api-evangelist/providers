---
access_model:
  confidence: medium
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
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 127
  human_in_the_loop: 1
  name: Nylas Agentic Access
  operation_count: 210
  slug: nylas-agentic-access
  summary_line: 210 operations · 127 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Contacts. Read, create, update and delete a grant's contacts and contact groups.
  name: Nylas Contacts API
  phrasing_intents:
  - id: post-contact
    intent: Add a contact to an address book
    question: How do I add a new person to a user's address book?
  - id: list-contact
    intent: List or filter a user's contacts
    question: Which contacts in someone's address book have a given email address?
  - id: get-contact
    intent: Get one contact
    question: What details do we have for a specific contact?
  - id: put-contact
    intent: Update a contact's details
    question: Can I change an existing contact's job title or notes?
  - id: delete-contact
    intent: Delete a contact
    question: How do I remove someone from a user's address book?
  - id: list-contact-groups
    intent: List contact groups
    question: What contact groups does this account have?
  phrasing_ops: 6
  slug: nylas-contacts-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Drafts. Compose, update, send and delete drafts, manage attachments, and generate draft bodies and replies with Smart Compose.
  name: Nylas Drafts API
  phrasing_intents:
  - id: get-drafts
    intent: List a user's email drafts
    question: How do I see all the drafts sitting in a user's Drafts folder?
  - id: post-draft
    intent: Save a new email draft
    question: Can I save an email as a draft without sending it?
  - id: get-draft-id
    intent: Retrieve a single email draft
    question: How can I open one specific draft to check its contents?
  - id: put-drafts-id
    intent: Edit an existing email draft
    question: Can I change the recipients or body of a draft I already saved?
  - id: delete-drafts-id
    intent: Delete an email draft
    question: How do I throw away a draft I don't need?
  - id: send-draft-id
    intent: Send a saved draft
    question: How do I send an email that's currently saved as a draft?
  phrasing_ops: 6
  slug: nylas-drafts-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Events. Create, update, delete and list calendar events, including recurring events, group events and RSVP handling.
  name: Nylas Events API
  phrasing_intents:
  - id: get-all-events
    intent: List events on a user's calendar
    question: How do I list upcoming events on a connected user's calendar?
  - id: create-event
    intent: Create a calendar event
    question: How do I put a new meeting on someone's calendar?
  - id: import-events
    intent: Import all events from a calendar for syncing
    question: What's the best way to pull every event, including recurring exceptions, into my own database?
  - id: get-events-id
    intent: Retrieve a single calendar event
    question: How can I get the details of one specific calendar event?
  - id: put-events-id
    intent: Update or reschedule a calendar event
    question: How do I reschedule an existing calendar event to a new time?
  - id: delete-events-id
    intent: Delete a calendar event
    question: How do I remove a meeting from a user's calendar?
  - id: send-rsvp
    intent: Respond yes, no or maybe to an event invite
    question: How do I accept or decline a meeting invitation on a user's behalf?
  phrasing_ops: 7
  slug: nylas-events-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Messages. List, search, read, update and delete email messages. Send immediately, schedule a send and cancel a scheduled send, with folders, signatures and attachments alongside.
  name: Nylas Messages API
  phrasing_intents:
  - id: get-messages
    intent: List or search a user's email messages
    question: How do I list the emails in a connected user's mailbox?
  - id: get-messages-id
    intent: Retrieve a single email message
    question: How can I fetch the full contents of one email by its message ID?
  - id: put-messages-id
    intent: Mark, star or move an email message
    question: How do I mark an email as read or unread through the API?
  - id: delete-message
    intent: Delete an email message
    question: Does deleting an email send it to Trash or remove it permanently?
  - id: clean-messages
    intent: Clean up email bodies into plain content
    question: Can I strip signatures, links and images out of email bodies to get clean text?
  - id: send-message
    intent: Send or schedule an email from a user's mailbox
    question: How do I send an email on behalf of a connected user?
  - id: get-schedules
    intent: List a user's scheduled emails
    question: Which emails does this user have scheduled to send later?
  - id: get-schedule-by-id
    intent: Check the status of one scheduled email
    question: How can I check whether a specific scheduled email has been sent yet?
  phrasing_ops: 9
  slug: nylas-messages-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Threads. List, search, read and update email threads, and manage thread-level folders and state.
  name: Nylas Threads API
  phrasing_intents:
  - id: get-threads
    intent: List or search email threads
    question: Which email conversations have unread messages?
  - id: get-threads-id
    intent: Get one email thread
    question: What messages and participants are in a particular conversation?
  - id: put-threads-id
    intent: Star, mark read or move a thread
    question: Can I mark a whole conversation as read in one call?
  - id: delete-threads-id
    intent: Move a thread to the trash
    question: What happens to the messages when I delete a thread?
  phrasing_ops: 4
  slug: nylas-threads-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Meeting notetaker. Send a notetaker to a Google Meet, Microsoft Teams or Zoom call, then retrieve the recording, transcript, summary and action items. Available grant-scoped, or standalone with no con
  name: Nylas Notetaker API
  phrasing_intents:
  - id: get-all-notetakers
    intent: List Notetaker bots for a grant
    question: Which Notetaker bots are scheduled to join my upcoming meetings?
  - id: invite-notetaker
    intent: Invite a Notetaker bot to a meeting
    question: How do I send a Nylas Notetaker bot into a video meeting to record it?
  - id: get-notetaker
    intent: Get one Notetaker bot's details
    question: What are the details and current state of a specific Notetaker bot?
  - id: update-notetaker
    intent: Reschedule or rename a scheduled Notetaker
    question: Can I change when a scheduled Notetaker bot joins the meeting?
  - id: delete-notetaker
    intent: Permanently delete a Notetaker and its data
    question: How can I permanently erase a Notetaker along with its recordings and transcripts?
  - id: get-notetaker-history
    intent: View a Notetaker's event and state history
    question: What state changes has a Notetaker bot gone through during a meeting?
  - id: cancel-notetaker
    intent: Cancel a Notetaker before it joins
    question: How can I stop a scheduled Notetaker from joining a meeting it hasn't entered yet?
  - id: post-notetaker-leave
    intent: Make a Notetaker leave an ongoing meeting
    question: How do I pull a Notetaker bot out of a meeting it's currently attending?
  phrasing_ops: 9
  slug: nylas-notetaker-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Amazon SNS notification channels allow you to receive Nylas event notifications through Amazon Simple Notification Service (SNS) instead of webhooks. To use Amazon SNS notifications, you need to set u
  name: Nylas Amazon SNS Notifications API
  phrasing_intents:
  - id: create-sns-channel
    intent: Create an Amazon SNS notification channel
    question: How do I deliver Nylas notifications to an Amazon SNS topic?
  - id: get-sns-channels
    intent: List Amazon SNS notification channels
    question: Which Amazon SNS topics is my application sending notifications to?
  - id: get-sns-by-id
    intent: Get one Amazon SNS channel
    question: What topic ARN and triggers are set on a particular SNS channel?
  - id: put-sns-by-id
    intent: Update an Amazon SNS channel
    question: Can I change the IAM role on an existing SNS channel?
  - id: delete-sns-by-id
    intent: Delete an Amazon SNS channel
    question: How do I stop notifications going to an Amazon SNS topic?
  phrasing_ops: 5
  slug: nylas-amazon-sns-notifications-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Before you begin, you should already have: - Linked your v2 and v3 Nylas organizations. If you''re not sure if your organizations are linked and you have a contract with us, [contact Nylas Support](/do'
  name: Nylas App migration API
  phrasing_intents:
  - id: migration_link_v2v3_apps
    intent: Link a v2 application to a v3 application
    question: How do I connect my old v2 app to a new v3 app before migrating?
  - id: migration_import_v2_app
    intent: Import v2 app settings into the linked v3 app
    question: Can I copy my v2 application's settings into the linked v3 app?
  - id: migration_clone_single_account
    intent: Migrate one v2 account to a v3 grant
    question: How do I test-migrate a single v2 connected account to v3?
  - id: migration_snapshot_batch_clone
    intent: Batch-migrate v2 accounts to v3 grants
    question: How do I migrate all my remaining v2 accounts to v3 in one job?
  - id: migration_get_jobs
    intent: Check migration job progress
    question: What's the progress of my running v2-to-v3 migration jobs?
  phrasing_ops: 5
  slug: nylas-app-migration-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'In the context of the Nylas APIs, an "application" is the object record of your Nylas application. <div id="admonition-info">🔍 <b>The term "application" can refer to any of three concepts</b>: your Ny'
  name: Nylas Applications API
  phrasing_intents:
  - id: get_application
    intent: View my Nylas application settings
    question: How can I see the region, environment and branding of my application?
  - id: update_application
    intent: Update application branding and hosted auth
    question: Can I change the branding shown on my application's hosted authentication page?
  - id: get_all_callback_uris
    intent: List my application's callback URIs
    question: Which redirect URIs are registered on my application?
  - id: add_callback_uri
    intent: Register a new callback URI
    question: How do I add a redirect URI so users return to my app after authenticating?
  - id: get_application_callback_uri
    intent: Retrieve one callback URI
    question: Can I look up a single callback URI by its ID?
  - id: update_callback_uri
    intent: Change an existing callback URI
    question: Can I edit the URL or platform of a callback URI I already registered?
  - id: delete_callback_uri
    intent: Remove a callback URI
    question: How do I delete a redirect URI I no longer use?
  phrasing_ops: 7
  slug: nylas-applications-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: You can use the `attachments` schema in a [Send Message request](/docs/reference/api/messages/send-message/) to send attachments, regardless of the email provider. You use the [Drafts](/docs/reference
  name: Nylas Attachments API
  phrasing_intents:
  - id: get-attachments-id
    intent: Get an attachment's metadata
    question: What's the filename, size and type of an email attachment?
  - id: get-attachments-id-download
    intent: Download an attachment file
    question: How do I download the actual file attached to an email?
  - id: create-attachment-upload-session
    intent: Start an upload session for a large attachment
    question: How do I attach a file larger than the normal size limit to an email?
  - id: complete-attachment-upload-session
    intent: Finish a large attachment upload
    question: What do I do after uploading file bytes to the pre-signed URL?
  phrasing_ops: 4
  slug: nylas-attachments-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Nylas provides two ways to handle authentication: - **Bring Your Own (BYO) Authentication**, which uses the [`/v3/connect/custom` endpoint](/docs/reference/api/manage-grants/byo_auth/). In BYO Authent'
  name: Nylas Authentication APIs API
  phrasing_intents:
  - id: get_oauth2_flow
    intent: Start a hosted OAuth authorization
    question: How do I send a user to Nylas to connect their email account?
  - id: exchange_oauth2_token
    intent: Exchange an OAuth code or refresh token
    question: How do I trade the authorization code from hosted auth for an access token?
  - id: revoke_oauth2_token_and_grant
    intent: Revoke an OAuth access token
    question: Does revoking an access token also revoke the user's grant?
  - id: info_oauth2_token
    intent: Inspect an OAuth token
    question: What grant and scopes does a given access token belong to?
  - id: byo_auth
    intent: Create a grant with your own OAuth tokens
    question: Can I create a grant from a refresh token I already obtained myself?
  phrasing_ops: 5
  slug: nylas-authentication-apis-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Nylas Scheduler uses the `/v3/scheduling/availability` endpoint to retrieve availability information. When you make a request, Nylas validates the provided session ID and uses it to retrieve the relat
  name: Nylas Availability API
  phrasing_intents:
  - id: get-availability
    intent: Get bookable slots for a scheduling page
    question: What open time slots does my scheduling page offer next week?
  phrasing_ops: 1
  slug: nylas-availability-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Nylas Scheduler uses the `/v3/scheduling/bookings` endpoint to manage bookings. Bookings work the same way when the organizer is an [Agent Account](/docs/v3/scheduler/agent-accounts/): the event is cr'
  name: Nylas Bookings API
  phrasing_intents:
  - id: post-bookings
    intent: Book a meeting from a scheduling page
    question: How do I book a time slot for a guest on a scheduling configuration?
  - id: get-bookings-id
    intent: Retrieve a scheduled booking
    question: How can I see the details of a booking someone made?
  - id: patch-bookings-id
    intent: Reschedule an existing booking
    question: How do I move a booked meeting to a different time?
  - id: put-bookings-id
    intent: Confirm or reject a pending booking
    question: How do I approve a booking request that's waiting for confirmation?
  - id: delete-bookings-id
    intent: Cancel a booking and its event
    question: What happens to the calendar event when I cancel a booking?
  phrasing_ops: 5
  slug: nylas-bookings-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: The Nylas Calendar API allows you to create and manage calendars, and access the events they contain. Nylas uses the same commands to manage calendars across providers, and you can refer to specific c
  name: Nylas Calendar API
  phrasing_intents:
  - id: get-all-calendars
    intent: List a user's calendars
    question: What calendars does this connected account have?
  - id: create-calendar
    intent: Create a new calendar
    question: How do I add a new calendar to a user's account?
  - id: get-calendars-id
    intent: Get one calendar's details
    question: What are the settings of a user's primary calendar?
  - id: put-calendars-id
    intent: Update a calendar's name, color or details
    question: Can I change the color of an existing calendar?
  - id: delete-calendars-id
    intent: Delete a calendar
    question: Can I delete a secondary calendar from a user's account?
  - id: post-availability
    intent: Find open time slots across participants
    question: When are several teammates all free for a 30-minute meeting?
  - id: post-calendars-free-busy
    intent: Get free/busy blocks for email addresses
    question: Which times are people busy according to their calendars?
  phrasing_ops: 7
  slug: nylas-calendar-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: A configuration is a collection of event settings and preferences. Nylas Scheduler stores Configuration objects in the Scheduler database and loads them as Scheduling Pages in the Scheduler UI. A conf
  name: Nylas Configurations API
  phrasing_intents:
  - id: post-configurations
    intent: Create a scheduling Configuration
    question: How do I set up a new booking page with its own scheduling rules?
  - id: get-configurations
    intent: List scheduling Configurations
    question: What scheduling pages and Configurations does this user have?
  - id: get-configurations-id
    intent: Get one scheduling Configuration
    question: What rules and participants are on a specific scheduling Configuration?
  - id: put-configurations-id
    intent: Update a scheduling Configuration
    question: Can I change the settings of an existing booking page?
  - id: delete-configurations-id
    intent: Delete a scheduling Configuration
    question: Can I delete a Configuration that still has active sessions?
  phrasing_ops: 5
  slug: nylas-configurations-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'A Nylas connector credential is a special type of record that securely stores information (such as provider settings) that allows you to connect using an administrator account. Nylas securely stores, '
  name: Nylas Connector credentials API
  phrasing_intents:
  - id: create_credential
    intent: Add a credential to a provider connector
    question: How do I manually add a credential record to a connector?
  - id: get_credential_all
    intent: List credentials on a provider connector
    question: Which credentials are stored for a given provider connector?
  - id: get_credential_by_id
    intent: Retrieve one connector credential
    question: How can I look up a specific credential on a connector?
  - id: patch_credential_by_id
    intent: Update a connector credential
    question: How do I rename a credential on a connector?
  - id: delete_credential_by_id
    intent: Delete a non-default connector credential
    question: Can I delete the active credential on a connector?
  phrasing_ops: 5
  slug: nylas-connector-credentials-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: In Nylas, a connector (formerly called an "integration") stores information that allows your Nylas application to connect to a third party services, such as a provider auth application from Google (GC
  name: Nylas Connectors (Integrations) API
  phrasing_intents:
  - id: create_connector
    intent: Set up a connector for a provider
    question: What's the first step to let users authenticate with a new email provider?
  - id: get_connector_all
    intent: List my application's provider connectors
    question: Which email and calendar provider connectors are set up in my app?
  - id: get_connector_by_provider
    intent: Retrieve the connector for a provider
    question: How can I see the settings and scopes of the connector for a given provider?
  - id: update_connector_by_provider
    intent: Change a connector's scopes or settings
    question: Can I change the OAuth scopes requested by a provider connector?
  - id: delete_connector_by_provider
    intent: Delete a provider connector
    question: What happens to existing grants if I delete a connector?
  - id: detect_provider_by_email
    intent: Detect a user's email provider from an address
    question: Can I figure out which email provider an address belongs to before authenticating?
  phrasing_ops: 6
  slug: nylas-connectors-integrations-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: In Nylas v2, you used the unique Nylas ID to locate data and objects in Nylas's synced data. In Nylas v3, you use the provider ID directly. These APIs look up the provider IDs for your v2 data. Becaus
  name: Nylas Data migration API
  phrasing_intents:
  - id: translate_v2id_to_provider_id
    intent: Translate v2 IDs into v3 provider IDs
    question: How do I map my old v2 object IDs to v3 provider IDs during a migration?
  phrasing_ops: 1
  slug: nylas-data-migration-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: To simplify your experience, the Nylas Email API uses the same commands to manage both folders and labels, and can refer to specific folders using the provider's `folder_id`. The Email API also expose
  name: Nylas Folders API
  phrasing_intents:
  - id: get-folder
    intent: List a mailbox's folders and labels
    question: What folders or labels exist in this user's mailbox?
  - id: post-folder
    intent: Create a mail folder or label
    question: How do I create a new folder or label in someone's mailbox?
  - id: get-folders-id
    intent: Get one folder
    question: What are the details of a specific mail folder?
  - id: put-folders-id
    intent: Rename, move or recolor a folder
    question: Can I rename an existing mail folder?
  - id: delete-folders-id
    intent: Delete a mail folder
    question: How do I delete a folder or label from a mailbox?
  phrasing_ops: 5
  slug: nylas-folders-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Group meetings let you host events with multiple participants. Unlike one-on-one meetings, group events are designed for collaborative scheduling where multiple attendees are invited to the same event
  name: Nylas Group Events API
  phrasing_intents:
  - id: get-group-events
    intent: List group events in a time range
    question: Which group sessions are scheduled on a Configuration this week?
  - id: create-group-event
    intent: Create a group event with a capacity
    question: How do I set up a class or webinar that several people can book into?
  - id: put-group-event
    intent: Update a group event
    question: Can I raise the capacity of a group event people already booked?
  - id: delete-group-event
    intent: Delete a group event
    question: How do I cancel and remove a group session entirely?
  - id: import-group-events
    intent: Import existing events as group events
    question: Can I bring existing calendar events into a group events Configuration?
  - id: validate-time-slot
    intent: Check a group event slot is still valid
    question: Is a group event time slot still bookable, or was it changed or filled?
  phrasing_ops: 6
  slug: nylas-group-events-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'The Lists endpoints let you manage typed collections of values (email addresses, domains, or top-level domains) that can be referenced by Rules using the `in_list` condition operator. Lists provide a '
  name: Nylas Lists API
  phrasing_intents:
  - id: create-list
    intent: Create a list of domains, TLDs or addresses
    question: How do I create a blocklist of email domains for my agent account rules?
  - id: list-lists
    intent: List all lists in the application
    question: What domain, TLD and email address lists have I created for my rules?
  - id: get-list
    intent: Get one list's details
    question: What's the type and item count of a specific list?
  - id: update-list
    intent: Rename or redescribe a list
    question: Can I rename an existing list without changing its type?
  - id: delete-list
    intent: Delete a list and all its items
    question: What happens to rules that reference a list after I delete it?
  - id: add-list-items
    intent: Add values to a list
    question: How do I add more domains to an existing list?
  - id: list-list-items
    intent: List the values in a list
    question: Which domains or addresses are currently in a given list?
  - id: remove-list-items
    intent: Remove specific values from a list
    question: Can I take a few addresses out of a list without deleting the list?
  phrasing_ops: 8
  slug: nylas-lists-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'The Manage API Keys endpoints let you create, list, and delete API keys from your Nylas application outside of the Nylas Dashboard. ## Nylas Service Account <div id="admonition-warning">⚠️ <b>Before y'
  name: Nylas Manage API keys API
  phrasing_intents:
  - id: create-api-key
    intent: Create a new API key
    question: How do I generate a new API key for my application?
  - id: get-api-keys
    intent: List an application's API keys
    question: Which API keys exist for my application?
  - id: get-api-key
    intent: Retrieve one API key
    question: Can I look up a single API key's details and expiry?
  - id: delete-api-key
    intent: Revoke an API key
    question: How do I revoke an API key that may have leaked?
  phrasing_ops: 4
  slug: nylas-manage-api-keys-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: The Manage Domains endpoints let you register, verify, update, and delete email domains for use with [Transactional Send](/docs/v3/getting-started/transactional-send/) and [Nylas Agent Accounts](/docs
  name: Nylas Manage Domains API
  phrasing_intents:
  - id: create-domain
    intent: Register a new sending email domain
    question: How do I register a domain so I can send transactional email from it?
  - id: list-domains
    intent: List my organization's email domains
    question: Which email domains are registered for my organization?
  - id: get-domain
    intent: Retrieve one registered domain
    question: Can I look up a single registered domain by its ID?
  - id: update-domain
    intent: Rename a registered domain
    question: Can I change the label of a domain I already registered?
  - id: delete-domain
    intent: Delete a registered email domain
    question: How do I remove an email domain from my organization?
  - id: get-domain-info
    intent: Get the DNS records a domain needs
    question: Which DNS records do I need to add at my DNS host to verify a domain?
  - id: verify-domain
    intent: Run a DNS verification check on a domain
    question: I've added the DNS records, how do I trigger verification of my domain?
  phrasing_ops: 7
  slug: nylas-manage-domains-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Grants are the main objects that power Nylas, because they _grant_ your Nylas application specific scopes of access (for example, permission to read email messages) to the user's resources and data on
  name: Nylas Manage Grants API
  phrasing_intents:
  - id: byo_auth
    intent: Create a grant from my own OAuth refresh token
    question: If I run the OAuth flow myself, how do I connect a user's account with their refresh token?
  - id: get-all-grants
    intent: List connected user accounts (grants)
    question: How do I list every user account connected to my application?
  - id: get_grant_by_id
    intent: Look up one connected account
    question: How can I tell whether a specific user's grant has expired?
  - id: patch_grant_by_id
    intent: Rotate a grant's refresh token or scopes
    question: Can I store a new refresh token on a grant without recreating it?
  - id: delete_grant_by_id
    intent: Disconnect a user's account (delete grant)
    question: What happens if I delete a grant and the user later signs in again?
  - id: get_grant_by_access_token
    intent: Identify the grant behind my access token
    question: Which grant does the access token I'm using belong to?
  phrasing_ops: 6
  slug: nylas-manage-grants-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: The Policies endpoints let you define the operational configuration for Nylas Agent Accounts, including message limits, attachment constraints, spam detection settings, and linked rules for inbound me
  name: Nylas Policies API
  phrasing_intents:
  - id: create-policy
    intent: Create a sending and spam policy
    question: How do I set message limits and spam detection for Agent Accounts?
  - id: list-policies
    intent: List agent account policies
    question: What policies have I defined for my Agent Accounts?
  - id: get-policy
    intent: Get one policy
    question: What limits and spam settings does a particular policy have?
  - id: update-policy
    intent: Update a policy's limits, rules or spam settings
    question: Can I change the message limits on an existing policy?
  - id: delete-policy
    intent: Delete a policy
    question: Is deleting a policy reversible?
  phrasing_ops: 5
  slug: nylas-policies-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Nylas offers two ways to get notifications of what's happening on the provider. You can either subscribe to webhook notifications, or you can set up a notification channel. Nylas offers Pub/Sub and Am
  name: Nylas Pub/Sub Notifications API
  phrasing_intents:
  - id: get_mock_webhook_payload
    intent: Preview a sample notification payload
    question: What does a notification body look like for a specific trigger type?
  - id: create-pubsub-channel
    intent: Create a Pub/Sub notification channel
    question: How do I send Nylas notifications to a Google Pub/Sub topic?
  - id: get-pubsub-channels
    intent: List Pub/Sub notification channels
    question: Which Google Pub/Sub channels is my application sending notifications to?
  - id: get-pubsub-by-id
    intent: Get one Pub/Sub channel
    question: What topic and triggers are set on a particular Pub/Sub channel?
  - id: put-pubsub-by-id
    intent: Update a Pub/Sub channel
    question: How do I restart a Pub/Sub channel I paused?
  - id: delete-pubsub-by-id
    intent: Delete a Pub/Sub channel
    question: How do I stop sending notifications to a Pub/Sub topic?
  phrasing_ops: 6
  slug: nylas-pub-sub-notifications-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'The Nylas Contacts API allows you to return information about rooms that you can book for meetings, conferences, and other events. ## Room resource booking scopes The table below lists the Microsoft a'
  name: Nylas Room resources API
  phrasing_intents:
  - id: list-room-resources
    intent: List meeting rooms and resources
    question: Which conference rooms can this account book?
  phrasing_ops: 1
  slug: nylas-room-resources-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: The Rules endpoints let you define automated filtering and routing logic for Nylas Agent Accounts. Each rule specifies a `trigger` (`inbound` or `outbound`), matching conditions, and actions to perfor
  name: Nylas Rules API
  phrasing_intents:
  - id: create-rule
    intent: Create an inbound or outbound email rule
    question: Can I automatically act on incoming mail from a particular sender domain?
  - id: list-rules
    intent: List my application's email rules
    question: Which inbound and outbound email rules are defined for my app?
  - id: get-rule
    intent: Retrieve one email rule
    question: How can I see the conditions and actions of a specific rule?
  - id: update-rule
    intent: Edit or disable an email rule
    question: Can I temporarily turn off a rule without deleting it?
  - id: delete-rule
    intent: Delete an email rule
    question: What happens to policies that reference a rule after I delete it?
  - id: list-rule-evaluations
    intent: See which rules ran on a user's mail
    question: How can I audit which rules were evaluated against a user's incoming messages?
  phrasing_ops: 6
  slug: nylas-rules-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Nylas Scheduler uses session IDs to authorize requests to the [`/v3/scheduling/availability`](/docs/reference/api/availability/) and [`/v3/scheduling/bookings`](/docs/reference/api/bookings/) endpoint
  name: Nylas Sessions API
  phrasing_intents:
  - id: post-sessions
    intent: Start a scheduling session for the booking UI
    question: How do I create a short-lived session for the Scheduling Component?
  - id: delete-session
    intent: End a scheduling session
    question: How do I invalidate a scheduling session before it expires?
  phrasing_ops: 2
  slug: nylas-sessions-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: The Nylas Signatures API lets you create and store HTML email signatures on Nylas, and reference them by ID when sending messages or creating drafts. Nylas appends the signature to the end of the emai
  name: Nylas Signatures API
  phrasing_intents:
  - id: list-signatures
    intent: List a user's email signatures
    question: Which email signatures has this user saved?
  - id: post-signature
    intent: Create an email signature
    question: How many signatures can one user have?
  - id: get-signature
    intent: Retrieve one email signature
    question: How can I view the HTML of a specific signature?
  - id: put-signature
    intent: Edit an email signature
    question: Does a signature keep its ID when I edit it?
  - id: delete-signature
    intent: Delete an email signature
    question: How do I permanently remove a saved signature?
  phrasing_ops: 5
  slug: nylas-signatures-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'The Smart Compose endpoints extend the Nylas Messages API. Currently, Smart Compose supports only two methods of getting AI responses: you can either receive them as a REST response in a single JSON b'
  name: Nylas Smart compose API
  phrasing_intents:
  - id: post-smart-compose
    intent: Draft a new email with AI from a prompt
    question: Can AI write a new email for me from a short prompt?
  - id: post-smart-compose-reply
    intent: Draft an AI reply to a specific email
    question: Can AI suggest a reply to an email I received?
  phrasing_ops: 2
  slug: nylas-smart-compose-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Nylas Notetaker is a real-time meeting bot that you can invite to your online meetings. It records and transcribes your discussion, and delivers results to you using the Nylas API and webhook notifica
  name: Nylas Standalone Notetaker API
  phrasing_intents:
  - id: get-all-standalone-notetakers
    intent: List standalone meeting Notetaker bots
    question: Which Notetaker bots have I invited to meetings?
  - id: invite-standalone-notetaker
    intent: Send a Notetaker bot to a meeting
    question: How do I send a bot to record and transcribe a video meeting?
  - id: get-standalone-notetaker
    intent: Look up a standalone Notetaker's details
    question: How can I see the current state and settings of a Notetaker I invited?
  - id: update-standalone-notetaker
    intent: Change a scheduled Notetaker's settings
    question: Can I change the join time of a Notetaker that's already scheduled?
  - id: delete-standalone-notetaker
    intent: Permanently delete a Notetaker and its data
    question: How do I erase a Notetaker along with its recordings and transcripts?
  - id: get-standalone-notetaker-history
    intent: View a Notetaker's event and state history
    question: How can I see every state change a Notetaker went through during a meeting?
  - id: cancel-standalone-notetaker
    intent: Cancel a Notetaker before it joins the meeting
    question: How do I stop a scheduled Notetaker from joining a meeting?
  - id: post-standalone-notetaker-leave
    intent: Make a Notetaker leave a meeting in progress
    question: How do I remove the recording bot from a meeting that's already underway?
  phrasing_ops: 9
  slug: nylas-standalone-notetaker-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Nylas' Transactional Send endpoint lets you send messages directly from an email domain that you've verified with Nylas. You can use this to send password reset emails, account verifications, or syste
  name: Nylas Transactional send API
  phrasing_intents:
  - id: send-transactional-email
    intent: Send a transactional email from my domain
    question: How do I send a transactional email from my own verified domain?
  phrasing_ops: 1
  slug: nylas-transactional-send-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Nylas Scheduler uses the `/v3/scheduling/should-redirect/<V2_SCHEDULER_SLUG>` endpoint to redirect existing v2 Scheduling Pages to v3.
  name: Nylas v2 Redirects API
  phrasing_intents:
  - id: v2-redirect
    intent: Redirect an old v2 scheduling page to v3
    question: Where does my old v2 scheduling page link point in v3?
  phrasing_ops: 1
  slug: nylas-v2-redirects-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Your application receives information about changes to user accounts and data through Nylas webhooks. <div id="admonition-info"> 🔍 <b>The term "webhook" can refer to any of three component parts</b>: '
  name: Nylas Webhook Notifications API
  phrasing_intents:
  - id: post-webhook-destinations
    intent: Create a webhook destination
    question: How do I start receiving webhooks when new messages or events arrive?
  - id: get-webhook-destinations-application
    intent: List all webhook destinations
    question: Which webhook URLs is my Nylas application sending notifications to?
  - id: get-webhook-by-id
    intent: Get one webhook destination
    question: What triggers and URL are set on a particular webhook destination?
  - id: put-webhook-by-id
    intent: Update a webhook destination
    question: Can I change which triggers an existing webhook listens for?
  - id: delete-webhook-by-id
    intent: Delete a webhook destination
    question: How do I stop Nylas from sending notifications to an old webhook URL?
  - id: post-new-secret
    intent: Rotate a webhook's signing secret
    question: How can I rotate the secret used to sign webhook notifications?
  - id: get_mock_webhook_payload
    intent: Preview a sample webhook payload
    question: What does a webhook notification body look like for a given trigger?
  - id: send_test_event
    intent: Send a test event to a webhook URL
    question: How do I check that my webhook endpoint is set up correctly?
  phrasing_ops: 8
  slug: nylas-webhook-notifications-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Workspaces group and organize grants in a Nylas application by a common attribute, such as the email address domain (for example, `nylas.com`). ## Assign grants to workspaces Nylas offers two endpoint'
  name: Nylas Workspaces API
  phrasing_intents:
  - id: get-all-workspaces
    intent: List all workspaces
    question: What workspaces exist in my Nylas application?
  - id: create-workspace
    intent: Create a workspace for a domain
    question: How do I create a workspace for my company's email domain?
  - id: get-workspace
    intent: Get one workspace
    question: What policy and rules are attached to a particular workspace?
  - id: update-workspace
    intent: Update a workspace's name, policy or rules
    question: Can I switch the policy attached to an existing workspace?
  - id: delete-workspace
    intent: Delete a workspace
    question: What happens to a workspace's grants when I delete it?
  - id: autogroup-workspace
    intent: Auto-group grants into workspaces
    question: How do I automatically sort grants into workspaces by email domain?
  - id: manually-assign-workspace
    intent: Assign or remove grants in a workspace
    question: Can I manually move specific grants into a workspace?
  phrasing_ops: 7
  slug: nylas-workspaces-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Application-level templates let you create reusable messages with dynamic content. Each template is linked to the Nylas application associated with the API key specified in a [Create Template request]
  name: Nylas Application-level templates API
  phrasing_intents:
  - id: list-app-level-templates
    intent: List application-level email templates
    question: Which email templates are defined for my whole application?
  - id: create-app-level-template
    intent: Create an application-level email template
    question: How do I create a reusable email template for my application?
  - id: get-app-level-template
    intent: Retrieve an application-level template
    question: How can I view the subject and body of one of my app templates?
  - id: update-app-level-template
    intent: Edit an application-level template
    question: Can I change the subject line of an existing application template?
  - id: delete-app-level-template
    intent: Delete an application-level template
    question: How do I remove an email template from my application?
  - id: render-template-html
    intent: Preview raw template HTML with variables
    question: Can I render ad-hoc template HTML with variables without saving a template first?
  - id: render-app-level-template
    intent: Render a saved application template
    question: How do I see what a saved app template looks like once variables are filled in?
  phrasing_ops: 7
  slug: nylas-application-level-templates-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Application-level workflows automatically send messages to certain users when a defined event is triggered. For example, if you want to send a confirmation message when a user schedules a booking, you
  name: Nylas Application-level workflows API
  phrasing_intents:
  - id: list-workflows
    intent: List application-level email workflows
    question: Which automated email workflows are set up for my whole application?
  - id: create-workflow
    intent: Create an application-level email workflow
    question: Can I automatically send a templated email when a trigger event happens across my app?
  - id: get-workflow
    intent: Retrieve an application-level workflow
    question: How can I see the trigger and template an app workflow uses?
  - id: update-workflow
    intent: Edit or pause an application-level workflow
    question: Can I pause an app-wide workflow without deleting it?
  - id: delete-workflow
    intent: Delete an application-level workflow
    question: How do I remove an automated workflow from my application?
  phrasing_ops: 5
  slug: nylas-application-level-workflows-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Grant-level templates let you create reusable messages with dynamic content. Each template is linked to the grant specified in a [Create Template request](/docs/reference/api/grant-level-templates/cre
  name: Nylas Grant-level templates API
  phrasing_intents:
  - id: get-grant-level-templates
    intent: List a user's email templates
    question: What email templates are saved for this user's grant?
  - id: create-grant-level-template
    intent: Create a user email template
    question: How do I save a reusable email template for one user?
  - id: get-grant-level-template
    intent: Get one user email template
    question: What's the subject and body of a specific saved template?
  - id: update-grant-level-template
    intent: Edit a user email template
    question: Can I change the subject line of an existing template?
  - id: delete-grant-level-template
    intent: Delete a user email template
    question: How do I remove a template a user no longer needs?
  - id: render-grant-level-template
    intent: Render a saved template with variables
    question: What will a saved template look like once I fill in its variables?
  - id: render-grant-level-template-html
    intent: Render ad-hoc template HTML with variables
    question: Can I preview raw template HTML with variables without saving it first?
  phrasing_ops: 7
  slug: nylas-grant-level-templates-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Grant-level workflows automatically send messages to certain users when a defined event is triggered. For example, if you want to send a confirmation message when a user schedules a booking, you can c
  name: Nylas Grant-level workflows API
  phrasing_intents:
  - id: list-grant-workflows
    intent: List a user's grant-level workflows
    question: Which automated email workflows are set up for one connected user?
  - id: create-grant-workflow
    intent: Create a workflow for one connected user
    question: Can I set up an automated email for just one user's account when an event triggers?
  - id: get-grant-workflow
    intent: Retrieve a user's workflow
    question: How can I view one workflow on a specific user's grant?
  - id: update-grant-workflow
    intent: Edit or pause a user's workflow
    question: Can I pause a workflow for one user without affecting others?
  - id: delete-grant-workflow
    intent: Delete a user's workflow
    question: How do I remove an automated workflow from one user's account?
  phrasing_ops: 5
  slug: nylas-grant-level-workflows-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Create and manage IAM credentials of type `api_key` attached to principals. Credentials inherit the principal's policy, and creation returns the secret only once. Requests require an organization-boun
  name: Nylas IAM credentials API
  slug: nylas-iam-credentials-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: Manage reusable IAM identities, their resource bindings, roles, and direct permissions. Requests require an organization-bound IAM API key with the corresponding `iam.principals.*` permission. Start w
  name: Nylas IAM principals API
  slug: nylas-iam-principals-api
- baseURL: https://api.us.nylas.com
  baseurl_source: declared
  description: 'Notetaker Configurations let you manage reusable settings for Notetaker bots. Configurations form a hierarchy — application, workspace, calendar, recurring event, and per-notetaker — where each level '
  name: Nylas Notetaker Configurations API
  slug: nylas-notetaker-configurations-api
artifact_total: 163
asyncapis:
- description: 'Change notifications Nylas pushes for grants, messages, message tracking, folders, calendars, events, contacts, Scheduler bookings, Notetaker, ExtractAI, Transactional Email and Agent Accounts. Every '
  name: Nylas Notifications
  slug: nylas-notifications-asyncapi
- description: ''
  name: Nylas Webhooks
  slug: nylas-webhooks
collections:
- collection_type: open
  name: Nylas API (v3) Admin API
  slug: open-nylas-admin-api
- collection_type: open
  name: Nylas API (v3) Admin Auth API
  slug: open-nylas-auth-api
- collection_type: open
  name: Nylas API (v3) Admin Calendars API
  slug: open-nylas-calendars-api
- collection_type: open
  name: Nylas API (v3) Admin Contacts API
  slug: open-nylas-contacts-api
- collection_type: open
  name: Nylas API (v3) Admin Drafts API
  slug: open-nylas-drafts-api
- collection_type: open
  name: Nylas API (v3) Admin Events API
  slug: open-nylas-events-api
- collection_type: open
  name: Nylas API (v3) Admin Grants API
  slug: open-nylas-grants-api
- collection_type: open
  name: Nylas API (v3) Admin Messages API
  slug: open-nylas-messages-api
- collection_type: open
  name: Nylas API (v3) Admin Scheduling API
  slug: open-nylas-scheduling-api
- collection_type: open
  name: Nylas API (v3) Admin Threads API
  slug: open-nylas-threads-api
- collection_type: open
  name: Nylas API (v3)
  slug: open-nylas
common:
- group: build
  href: https://artifacts.apis.io/nylas/integrations/nylas-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/nylas-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/nylas/overlays/nylas-amazon-sns-notifications-api-phrasing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nylas-amazon-sns-notifications-api-phrasing-overlay.yaml
- group: build
  href: https://artifacts.apis.io/nylas/cli/nylas-cli.yml
  title: ''
  type: CLI
  url: cli/nylas-cli.yml
- group: commercial
  href: https://artifacts.apis.io/nylas/finops/nylas-finops.yml
  title: ''
  type: FinOps
  url: finops/nylas-finops.yml
- group: operate
  href: https://artifacts.apis.io/nylas/rate-limits/nylas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nylas-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nylas/plans/nylas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nylas-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nylas/rules/nylas-rules.yml
  title: ''
  type: Spectral
  url: rules/nylas-rules.yml
- group: design
  href: https://artifacts.apis.io/nylas/json-ld/nylas-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nylas-context.jsonld
- group: agent
  href: https://artifacts.apis.io/nylas/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nylas/asyncapi/nylas-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/nylas-webhooks.yml
- group: design
  href: https://artifacts.apis.io/nylas/data-model/nylas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nylas-data-model.yml
- group: operate
  href: https://artifacts.apis.io/nylas/changelog/nylas-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nylas-changelog.yml
- group: design
  href: https://artifacts.apis.io/nylas/conventions/nylas-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nylas-conventions.yml
- group: design
  href: https://artifacts.apis.io/nylas/errors/nylas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nylas-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/nylas/llms/nylas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nylas-llms.txt
- group: build
  href: https://artifacts.apis.io/nylas/mcp/nylas-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nylas-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/nylas/hosts/nylas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nylas-hosts.yml
- group: other
  href: https://artifacts.apis.io/nylas/vendors/nylas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nylas-vendors.yml
- group: build
  href: https://artifacts.apis.io/nylas/packages/nylas-packages.yml
  title: ''
  type: Packages
  url: packages/nylas-packages.yml
- group: docs
  href: https://artifacts.apis.io/nylas/openapi/_original/nylas-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/nylas-api-openapi.yml
- group: docs
  href: https://artifacts.apis.io/nylas/asyncapi/nylas-notifications-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/nylas-notifications-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/nylas/json-schema/nylas-notification-envelope.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/nylas-notification-envelope.schema.json
- group: design
  href: https://artifacts.apis.io/nylas/json-ld/nylas-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/nylas-context.jsonld
- group: design
  href: https://artifacts.apis.io/nylas/rules/nylas-rules.yml
  title: ''
  type: SpectralRules
  url: rules/nylas-rules.yml
- group: other
  href: https://artifacts.apis.io/nylas/capabilities/nylas-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nylas-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/nylas/agentic-access/nylas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nylas-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nylas/security/nylas-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nylas-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/nylas/security/nylas-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nylas-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nylas/security/nylas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nylas-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nylas/authentication/nylas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nylas-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nylas
- group: company
  title: ''
  type: Website
  url: https://www.nylas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nylas.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nylas.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nylas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nylas.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nylas.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status-v3.nylas.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nylas.com/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nylas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nylas.com/docs/reference/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nylas.com/docs/reference/notifications/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nylas.com/docs/reference/ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nylas.com/docs/v3/getting-started/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nylas/nylas-java
- group: build
  title: ''
  type: CLI
  url: https://cli.nylas.com/
- group: build
  title: ''
  type: Postman
  url: https://developer.nylas.com/docs/v3/api-references/postman/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/trynylas/workspace/nylas-api/overview
- group: agent
  title: ''
  type: AgentSkills
  url: https://developer.nylas.com/.well-known/agent-skills/index.json
- group: operate
  title: ''
  type: Support
  url: https://developer.nylas.com/docs/support/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.nylas.com/docs/changelogs/
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://developer.nylas.com/docs/support/product-lifecycle/
- group: auth
  title: ''
  type: Security
  url: https://www.nylas.com/security/
- group: auth
  title: ''
  type: OAuthScopes
  url: https://developer.nylas.com/docs/dev-guide/scopes/
- group: start
  title: ''
  type: Console
  url: https://developer.nylas.com/docs/reference/api/
- group: build
  title: ''
  type: CodeSamples
  url: https://github.com/nylas-samples
- group: build
  title: ''
  type: Examples
  url: https://developer.nylas.com/docs/cookbook/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nylas.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.nylas.com/company/about/
- group: other
  title: ''
  type: Subprocessors
  url: https://www.nylas.com/security/subprocessors/
- group: other
  title: ''
  type: DataResidency
  url: https://developer.nylas.com/docs/dev-guide/platform/data-residency/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.nylas.com/privacy-policy/
- group: other
  title: ''
  type: AITransparency
  url: https://developer.nylas.com/docs/v3/notetaker/custom-announcements/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nylas.com/public
- group: design
  title: ''
  type: Webhooks
  url: https://developer.nylas.com/docs/v3/notifications/
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.nylas.com/docs/api/errors/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.nylas.com/docs/dev-guide/platform/rate-limits/
- group: design
  title: ''
  type: Idempotency
  url: https://developer.nylas.com/docs/v3/email/idempotent-send/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nylas.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://dashboard-v3.nylas.com/register
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.us.nylas.com
- group: agent
  href: https://artifacts.apis.io/nylas/mcp/nylas-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nylas-mcp.yml
- group: design
  href: https://artifacts.apis.io/nylas/vocabulary/nylas-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nylas-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nylas/conformance/nylas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nylas-conformance.yml
- group: other
  href: https://artifacts.apis.io/nylas/a2a/nylas-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nylas-a2a.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://developer.nylas.com/.well-known/security.txt
- group: other
  title: ''
  type: ContentSignal
  url: https://developer.nylas.com/robots.txt
- group: other
  title: ''
  type: APICatalog
  url: https://developer.nylas.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/nylas/well-known/nylas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nylas-well-known.yml
created: '2025-02-06'
description: Nylas provides a unified SaaS platform that enables applications to integrate email, calendar, contacts, scheduling, and meeting notetaking across major providers such as Google, Microsoft, iCloud, Yahoo, and generic IMAP services. The API suite includes REST endpoints for messaging, calendar events, contact management, authentication flows, and administrative controls, supporting both standard OAuth and Nylas‑Connect mechanisms. It also offers SDKs for multiple languages, a CLI, and a hosted MCP server for autonomous agent accounts, facilitating AI‑driven interactions without direct OAuth handling. Official SDKs cover Node.js, Python, Ruby and Kotlin/Java, alongside a CLI, a hosted MCP server, and Agent Accounts that provision a Nylas-hosted mailbox and calendar for autonomous agents without requiring an OAuth flow.
finops:
- has_sources: true
  method: provider-published
  name: Nylas Finops
  primary_unit: connected account, Agent Account, GB, outgoing email, Notetaker minute
  service_category: API
  slug: nylas-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nylas.png
json_schemas:
- name: 200-delete
  property_count: 0
  slug: nylas-200-delete
- name: Amazon SNS Channel Payload
  property_count: 6
  slug: nylas-amazon-sns-input-payload
- name: Android
  property_count: 4
  slug: nylas-android-callbackw-settings
- name: ApplicationObject
  property_count: 9
  slug: nylas-application-object
- name: AutodetectObject
  property_count: 4
  slug: nylas-autodetect-object
- name: Open Hours
  property_count: 5
  slug: nylas-availability-open-hours
- name: availability_rules
  property_count: 5
  slug: nylas-availability-rules
- name: availability_specific_time_availability
  property_count: 4
  slug: nylas-availability-specific-time-availability
- name: Nylas booking.cancelled notification object
  property_count: 3
  slug: nylas-booking-cancelled.schema
- name: Nylas booking.created notification object
  property_count: 5
  slug: nylas-booking-created.schema
- name: Nylas booking.pending notification object
  property_count: 5
  slug: nylas-booking-pending.schema
- name: Nylas booking.reminder notification object
  property_count: 3
  slug: nylas-booking-reminder.schema
- name: Nylas booking.rescheduled notification object
  property_count: 5
  slug: nylas-booking-rescheduled.schema
- name: booking_update_group
  property_count: 5
  slug: nylas-booking-update-group
- name: booking_update
  property_count: 2
  slug: nylas-booking-update
- name: Nylas calendar.created notification object
  property_count: 14
  slug: nylas-calendar-created.schema
- name: Nylas calendar.deleted notification object
  property_count: 11
  slug: nylas-calendar-deleted.schema
- name: Nylas calendar.updated notification object
  property_count: 14
  slug: nylas-calendar-updated.schema
- name: configuration
  property_count: 8
  slug: nylas-configuration
- name: ConnectorObject
  property_count: 5
  slug: nylas-connector-object
- name: Nylas contact.deleted notification object
  property_count: 3
  slug: nylas-contact-deleted.schema
- name: Nylas contact.updated notification object
  property_count: 21
  slug: nylas-contact-updated.schema
- name: CredentialObject
  property_count: 4
  slug: nylas-credential-object
- name: Destination Payload
  property_count: 5
  slug: nylas-destination-input-payload
- name: Destination Update Payload
  property_count: 6
  slug: nylas-destination-update-payload
- name: Domain
  property_count: 15
  slug: nylas-domain-object
- name: DomainVerificationResponse
  property_count: 6
  slug: nylas-domain-verification-response
- name: create_event
  property_count: 15
  slug: nylas-event-create
- name: Nylas event.created notification object
  property_count: 28
  slug: nylas-event-created.schema
- name: Nylas event.deleted notification object
  property_count: 6
  slug: nylas-event-deleted.schema
- name: Nylas event.updated notification object
  property_count: 27
  slug: nylas-event-updated.schema
- name: Nylas folder.created notification object
  property_count: 5
  slug: nylas-folder-created.schema
- name: Nylas folder.deleted notification object
  property_count: 5
  slug: nylas-folder-deleted.schema
- name: Nylas folder.updated notification object
  property_count: 5
  slug: nylas-folder-updated.schema
- name: Input Payload
  property_count: 1
  slug: nylas-get-mock-payload-input
- name: Nylas grant.created notification object
  property_count: 8
  slug: nylas-grant-created.schema
- name: Nylas grant.deleted notification object
  property_count: 5
  slug: nylas-grant-deleted.schema
- name: Nylas grant.expired notification object
  property_count: 6
  slug: nylas-grant-expired.schema
- name: Nylas grant.imap_sync_completed notification object
  property_count: 5
  slug: nylas-grant-imap-sync-completed.schema
- name: GrantObject
  property_count: 18
  slug: nylas-grant-object
- name: GrantRuleEvaluation
  property_count: 12
  slug: nylas-grant-rule-evaluation-object
- name: Nylas grant.updated notification object
  property_count: 7
  slug: nylas-grant-updated.schema
- name: group-configuration
  property_count: 7
  slug: nylas-group-configuration
- name: iOS
  property_count: 4
  slug: nylas-ios-callbackw-settings
- name: JS
  property_count: 4
  slug: nylas-js-callbackw-settings
- name: ListItem
  property_count: 4
  slug: nylas-list-item-object
- name: List
  property_count: 9
  slug: nylas-list-object
- name: Nylas message.bounce_detected notification object
  property_count: 2
  slug: nylas-message-bounce-detected.schema
- name: Nylas message.bounced notification object
  property_count: 2
  slug: nylas-message-bounced.schema
- name: Nylas message.complaint notification object
  property_count: 2
  slug: nylas-message-complaint.schema
- name: Nylas message.created.cleaned notification object
  property_count: 20
  slug: nylas-message-created-cleaned.schema
- name: Nylas message.created.metadata notification object
  property_count: 16
  slug: nylas-message-created-metadata.schema
- name: Nylas message.created notification object
  property_count: 18
  slug: nylas-message-created.schema
- name: Nylas message.deleted notification object
  property_count: 4
  slug: nylas-message-deleted.schema
- name: Nylas message.delivered notification object
  property_count: 2
  slug: nylas-message-delivered.schema
- name: Nylas message.intelligence.order notification object
  property_count: 12
  slug: nylas-message-intelligence-order.schema
- name: Nylas message.intelligence.return notification object
  property_count: 11
  slug: nylas-message-intelligence-return.schema
- name: Nylas message.intelligence.tracking notification object
  property_count: 12
  slug: nylas-message-intelligence-tracking.schema
- name: Nylas message.intelligence.travel notification object
  property_count: 7
  slug: nylas-message-intelligence-travel.schema
- name: Nylas message.link_clicked.legacy notification object
  property_count: 3
  slug: nylas-message-link-clicked-legacy.schema
- name: Nylas message.link_clicked notification object
  property_count: 8
  slug: nylas-message-link-clicked.schema
- name: Nylas message.opened.legacy notification object
  property_count: 3
  slug: nylas-message-opened-legacy.schema
- name: Nylas message.opened notification object
  property_count: 8
  slug: nylas-message-opened.schema
- name: Nylas message.rejected notification object
  property_count: 2
  slug: nylas-message-rejected.schema
- name: Nylas message.send_failed notification object
  property_count: 4
  slug: nylas-message-send-failed.schema
- name: Nylas message.send_success notification object
  property_count: 2
  slug: nylas-message-send-success.schema
- name: Nylas message.transactional.bounced notification object
  property_count: 2
  slug: nylas-message-transactional-bounced.schema
- name: Nylas message.transactional.complaint notification object
  property_count: 2
  slug: nylas-message-transactional-complaint.schema
- name: Nylas message.transactional.delivered notification object
  property_count: 2
  slug: nylas-message-transactional-delivered.schema
- name: Nylas message.transactional.rejected notification object
  property_count: 2
  slug: nylas-message-transactional-rejected.schema
- name: Nylas message.updated.metadata notification object
  property_count: 16
  slug: nylas-message-updated-metadata.schema
- name: Nylas message.updated notification object
  property_count: 15
  slug: nylas-message-updated.schema
- name: Metadata
  property_count: 0
  slug: nylas-metadata
- name: MigrationJob
  property_count: 11
  slug: nylas-migration-job
- name: Nylas notetaker.created notification object
  property_count: 10
  slug: nylas-notetaker-created.schema
- name: Nylas notetaker.deleted notification object
  property_count: 4
  slug: nylas-notetaker-deleted.schema
- name: Nylas notetaker.media notification object
  property_count: 11
  slug: nylas-notetaker-media.schema
- name: Nylas notetaker.meeting_state notification object
  property_count: 11
  slug: nylas-notetaker-meeting-state.schema
- name: Nylas notetaker.updated notification object
  property_count: 10
  slug: nylas-notetaker-updated.schema
- name: Nylas notification envelope
  property_count: 7
  slug: nylas-notification-envelope.schema
- name: Policy
  property_count: 9
  slug: nylas-policy-object
- name: Destination Payload
  property_count: 5
  slug: nylas-pubsub-input-payload
- name: RedirectURIObject
  property_count: 0
  slug: nylas-redirect-uriobject
- name: Rule
  property_count: 12
  slug: nylas-rule-object
- name: Input Payload
  property_count: 2
  slug: nylas-send-test-event-input
- name: Nylas thread.replied.legacy notification object
  property_count: 3
  slug: nylas-thread-replied-legacy.schema
- name: Nylas thread.replied notification object
  property_count: 11
  slug: nylas-thread-replied.schema
- name: tracking_domain_name
  property_count: 0
  slug: nylas-tracking-domain-name
- name: transactional_send_message
  property_count: 12
  slug: nylas-transactional-send-message
- name: translate_v2v3_id
  property_count: 5
  slug: nylas-translate-v2v3-id
- name: trigger_types
  property_count: 0
  slug: nylas-trigger-types
- name: Web or Desktop
  property_count: 3
  slug: nylas-web-desktop-callback-no-settings
- name: WorkspaceObject
  property_count: 10
  slug: nylas-workspace-object
jsonld:
- class_count: 6
  name: Nylas Context
  property_count: 16
  slug: nylas-context
layout: provider
mcp_servers:
- description: ''
  name: Nylas MCP Server
  slug: nylas-mcp-server
modified: '2026-04-28'
name: Nylas
nav: Providers
network: true
overview: 'Nylas publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contacts API, Drafts API, Events API, and 40 more. Tagged areas include Calendar, Communications, Contacts, Email, and Messaging.


  The Nylas catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Nylas'' developer surface includes CLI, changelog, authentication, documentation, engineering blog, API reference, getting-started guide, and 75 more developer resources.'
plans:
- name: Nylas Plans Pricing
  plan_count: 5
  slug: nylas-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 10
  name: Nylas Rate Limits
  slug: nylas-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: Nylas API Rules
  rule_count: 21
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 4
  slug: nylas-rules
score:
  band: exemplar
  composite: 92.6
  coverage:
    artifact_dirs: 37
    catalog_earned: 90.6
    catalog_earned_first_party: 0.0
    catalog_gap: 24.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 96.8
    contract_governance: 45.5
    contract_quality: 85.9
    developer_ergonomics: 94.6
    discoverability: 86.7
    operational_transparency: 83.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 91.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 44
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 56.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/nylas/nylas-2026-06-20T190645.png
security:
- kind: authentication
  name: Nylas Authentication
  slug: nylas-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Nylas Domain Security
  slug: nylas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nylas Vulnerability Disclosure
  slug: nylas-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Nylas Trust Center
  slug: nylas-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: nylas-bookings-create-and-confirm
  slug: nylas-bookings-create-and-confirm
- name: nylas-events-management
  slug: nylas-events-management
- name: send-message
  slug: nylas-send_message
slug: nylas
tags:
- Calendar
- Communications
- Contacts
- Email
- Messaging
- Scheduling
- A2A
website: https://www.nylas.com/
---
