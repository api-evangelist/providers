---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
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
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 188
  human_in_the_loop: 3
  name: Activecampaign Agentic Access
  operation_count: 368
  slug: activecampaign-agentic-access
  summary_line: 368 operations · 188 acting · 3 human-in-the-loop
api_count: 9
apis:
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Accounts API from ActiveCampaign — 13 operation(s) for accounts.
  name: ActiveCampaign Accounts API
  phrasing_intents:
  - id: create-an-account-new
    intent: Create a CRM account
    question: How do I add a new company account to my CRM?
  - id: list-all-accounts
    intent: List CRM accounts
    question: Which company accounts do I have in ActiveCampaign?
  - id: update-an-account-new
    intent: Update a CRM account
    question: How do I change the name or details of an existing account?
  - id: retrieve-an-account
    intent: Get one CRM account
    question: What details are stored on a specific company account?
  - id: delete-an-account
    intent: Delete a CRM account
    question: How do I remove a single company account from my CRM?
  - id: create-an-account-note
    intent: Add a note to an account
    question: Can I attach a note to a company account?
  - id: update-a-account-note
    intent: Edit a note on an account
    question: Can I edit a note I already left on an account?
  - id: bulk-delete-accounts
    intent: Delete several accounts at once
    question: Can I delete many company accounts in one request?
  phrasing_ops: 25
  slug: activecampaign-accounts-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Addresses API from ActiveCampaign — 4 operation(s) for addresses.
  name: ActiveCampaign Addresses API
  phrasing_intents:
  - id: create-an-address
    intent: Add a sender address
    question: How do I add a new company postal address for my emails?
  - id: list-all-addresses
    intent: List mailing addresses
    question: Which physical sender addresses are saved in my ActiveCampaign account?
  - id: retrieve-an-address
    intent: Get a sender address
    question: Where can I view one saved address by its ID?
  - id: update-an-address
    intent: Update a sender address
    question: Can I change the details of an address after our office moved?
  - id: delete-an-address
    intent: Delete a sender address
    question: How do I remove an address we no longer use?
  - id: delete-an-addressgroup
    intent: Unlink an address from a user group
    question: Can I detach an address from a specific user group without deleting it?
  - id: delete-an-addresslist
    intent: Unlink an address from a list
    question: Is it possible to stop a list from using a particular address?
  phrasing_ops: 7
  slug: activecampaign-addresses-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The AI API from ActiveCampaign — 2 operation(s) for ai.
  name: ActiveCampaign AI API
  phrasing_intents:
  - id: createAIBroadcast
    intent: Generate a new SMS broadcast with AI
    question: Can AI draft a new SMS broadcast from a short prompt?
  - id: updateAIBroadcast
    intent: Rewrite an SMS broadcast with AI
    question: Can AI rewrite an SMS broadcast I already created?
  - id: getAIBroadcastStatus
    intent: Check an AI broadcast request's status
    question: Is my AI-generated SMS broadcast ready yet?
  phrasing_ops: 3
  slug: activecampaign-ai-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Automations API from ActiveCampaign — 3 operation(s) for automations.
  name: ActiveCampaign Automations API
  phrasing_intents:
  - id: list-all-automations
    intent: List all automations
    question: What automations have I built in ActiveCampaign?
  - id: get_automations-1
    intent: Get an automation by automationId
    question: How do I fetch one automation using the automationId path variant?
  - id: getAutomationsById
    intent: Get an automation by id
    question: Can I retrieve one automation through the id path variant rather than automationId?
  phrasing_ops: 3
  slug: activecampaign-automations-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Branding API from ActiveCampaign — 2 operation(s) for branding.
  name: ActiveCampaign Branding API
  phrasing_intents:
  - id: get-branding
    intent: Get a branding configuration
    question: What logo, colors and site name does a branding record hold?
  - id: update-branding
    intent: Update branding settings
    question: How do I change the logo or colors on my white-label branding?
  - id: brandings
    intent: List branding configurations
    question: Which branding configurations exist on my ActiveCampaign account?
  phrasing_ops: 3
  slug: activecampaign-branding-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Broadcasts API from ActiveCampaign — 11 operation(s) for broadcasts.
  name: ActiveCampaign Broadcasts API
  phrasing_intents:
  - id: listBroadcasts
    intent: List SMS broadcast messages
    question: Which SMS broadcasts have I sent or scheduled?
  - id: createBroadcast
    intent: Create an SMS broadcast
    question: How do I send a text message blast to a list in ActiveCampaign?
  - id: getBroadcast
    intent: Get an SMS broadcast
    question: What text, audience and schedule does a specific SMS broadcast have?
  - id: updateBroadcast
    intent: Update an SMS broadcast
    question: Can I change the text of an SMS broadcast before it sends?
  - id: deleteBroadcast
    intent: Delete an SMS broadcast
    question: How do I remove an SMS broadcast I no longer need?
  - id: listBroadcastLists
    intent: List SMS broadcast lists
    question: Which lists can I send SMS broadcasts to?
  phrasing_ops: 6
  slug: activecampaign-broadcasts-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Bulk Import API from ActiveCampaign — 2 operation(s) for bulk import.
  name: ActiveCampaign Bulk Import API
  phrasing_intents:
  - id: bulk-import-contacts
    intent: Bulk import contacts
    question: How do I import hundreds of contacts in one request?
  - id: bulk-import-status-list
    intent: List bulk contact import jobs
    question: What bulk contact imports are running or finished in ActiveCampaign?
  - id: bulk-import-status-info
    intent: Check one bulk import's progress
    question: Did a specific import batch finish successfully?
  phrasing_ops: 3
  slug: activecampaign-bulk-import-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Calendars API from ActiveCampaign — 2 operation(s) for calendars.
  name: ActiveCampaign Calendars API
  phrasing_intents:
  - id: create-a-calendar-feed
    intent: Create a calendar feed
    question: How do I create a calendar feed so tasks show in my calendar app?
  - id: list-all-calendar-feeds
    intent: List calendar feeds
    question: What calendar feeds are set up for tasks in ActiveCampaign?
  - id: list-all-calendar-feeds-1
    intent: Retrieve a calendar feed
    question: How do I look up one calendar feed by its ID?
  - id: update-a-calendar-feed
    intent: Update a calendar feed
    question: How do I change the name or contents of an existing calendar feed?
  - id: remove-a-calendar-feed
    intent: Delete a calendar feed
    question: How do I delete a calendar feed I no longer use?
  phrasing_ops: 5
  slug: activecampaign-calendars-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Campaigns API from ActiveCampaign — 6 operation(s) for campaigns.
  name: ActiveCampaign Campaigns API
  phrasing_intents:
  - id: list-all-campaigns
    intent: List email campaigns
    question: What email campaigns have I sent from ActiveCampaign?
  - id: retrieve-links-associated-campaign
    intent: Get the tracked links in a campaign
    question: Which links are included and tracked in a campaign?
  - id: retrieve-a-campaign
    intent: Retrieve an email campaign
    question: How do I get the details and stats of one campaign?
  - id: edit-campaign
    intent: Edit a campaign's settings
    question: How do I change the lists or segment a campaign sends to?
  - id: create-campaign
    intent: Create an email campaign
    question: How do I create a new email campaign through the API?
  - id: duplicate-campaign
    intent: Duplicate an existing campaign
    question: How do I copy an old campaign to reuse it?
  phrasing_ops: 6
  slug: activecampaign-campaigns-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Contacts API from ActiveCampaign — 28 operation(s) for contacts.
  name: ActiveCampaign Contacts API
  phrasing_intents:
  - id: create-a-new-contact
    intent: Create a new contact
    question: How do I add a brand-new contact to my account through the API?
  - id: list-all-contacts
    intent: Search and filter contacts
    question: How do I find contacts in ActiveCampaign by email address or phone number?
  - id: sync-a-contacts-data
    intent: Create or update a contact by email
    question: Can I upsert a contact so it is created if new and updated if the email already exists?
  - id: get-contact
    intent: Retrieve a contact
    question: How do I look up one contact's full record when I know its ID?
  - id: update-a-contact-new
    intent: Update an existing contact
    question: How do I change the name or phone on a contact I already have the ID for?
  - id: delete-contact
    intent: Delete a contact
    question: How do I permanently remove a contact from my account?
  - id: update-list-status-for-contact
    intent: Subscribe or unsubscribe a contact from a list
    question: How do I subscribe a contact to one of my mailing lists?
  - id: list-all-contactautomations-for-contact
    intent: List the automations one contact is in
    question: Which automations is a particular contact currently enrolled in?
  phrasing_ops: 36
  slug: activecampaign-contacts-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Credits API from ActiveCampaign — 1 operation(s) for credits.
  name: ActiveCampaign Credits API
  phrasing_intents:
  - id: getSmsCreditData
    intent: Check SMS credit usage and balance
    question: How many SMS credits do I have left this period?
  phrasing_ops: 1
  slug: activecampaign-credits-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Custom Objects API from ActiveCampaign — 9 operation(s) for custom objects.
  name: ActiveCampaign Custom Objects API
  phrasing_intents:
  - id: list-all-schemas
    intent: List custom object schemas
    question: What custom object schemas exist in my ActiveCampaign account?
  - id: create-a-schema
    intent: Create a custom object schema
    question: How do I define a new custom object type with its own fields?
  - id: retrieve-a-schema
    intent: Retrieve a custom object schema
    question: How do I see the fields and relationships defined on one schema?
  - id: delete-a-schema
    intent: Delete a custom object schema
    question: How do I remove a custom object schema I no longer use?
  - id: update-a-schema
    intent: Update a custom object schema
    question: How do I add new fields to an existing custom object schema?
  - id: delete-a-field-1
    intent: Delete a field from a schema
    question: How do I remove one field from a custom object schema?
  - id: create-a-public-schema
    intent: Create a public custom object schema
    question: How do I create a public schema that child accounts can extend?
  - id: create-a-child-schema
    intent: Create a child schema from a public schema
    question: How do I extend a public schema into a child schema in my account?
  phrasing_ops: 13
  slug: activecampaign-custom-objects-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Deals API from ActiveCampaign — 25 operation(s) for deals.
  name: ActiveCampaign Deals API
  phrasing_intents:
  - id: create-a-deal-new
    intent: Create a deal
    question: How do I add a new sales deal to a pipeline?
  - id: list-all-deals
    intent: List and filter deals
    question: Which open deals are in a given pipeline stage in ActiveCampaign?
  - id: retrieve-a-deal
    intent: Get a single deal
    question: Where can I see the full details of one specific deal by its ID?
  - id: update-a-deal-new
    intent: Update a deal
    question: Can I change the value or stage of an existing deal?
  - id: delete-a-deal
    intent: Delete a deal
    question: Is it possible to permanently remove a deal from my CRM?
  - id: create-a-deal-note
    intent: Add a note to a deal
    question: How do I attach a note to a specific deal?
  - id: update-a-deal-note
    intent: Edit a note on a deal
    question: Can I edit a note I already added to a deal?
  - id: bulk-update-deal-owners
    intent: Reassign owners on many deals
    question: Can I reassign a batch of deals to a different sales rep at once?
  phrasing_ops: 47
  slug: activecampaign-deals-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Ecommerce API from ActiveCampaign — 8 operation(s) for ecommerce.
  name: ActiveCampaign Ecommerce API
  phrasing_intents:
  - id: create-customer
    intent: Create an e-commerce customer
    question: How do I add a shopper from my store as an e-commerce customer?
  - id: list-all-customers
    intent: List e-commerce customers
    question: Which shoppers have been synced from my store?
  - id: get-customer
    intent: Get an e-commerce customer
    question: What store data is held for one e-commerce customer?
  - id: update-customer
    intent: Update an e-commerce customer
    question: Can I change a shopper's email or external ID after syncing?
  - id: delete-customer
    intent: Delete an e-commerce customer
    question: How do I remove a shopper from my synced store data?
  - id: create-order
    intent: Create an e-commerce order
    question: How do I send a store purchase or abandoned cart into ActiveCampaign?
  - id: list-all-orders
    intent: List e-commerce orders
    question: Which orders have come in from my store?
  - id: get-order
    intent: Get an e-commerce order
    question: What was in a particular order and what did it total?
  phrasing_ops: 13
  slug: activecampaign-ecommerce-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Event Tracking API from ActiveCampaign — 3 operation(s) for event tracking.
  name: ActiveCampaign Event Tracking API
  phrasing_intents:
  - id: create-a-new-event-name-only
    intent: Register a new tracked event name
    question: How do I add a new custom event name to track?
  - id: list-all-event-types
    intent: List tracked event names
    question: Which custom event names am I tracking?
  - id: retrieve-event-tracking-status
    intent: Check whether event tracking is on
    question: Is event tracking enabled on my ActiveCampaign account?
  - id: enable-disable-event-tracking
    intent: Turn event tracking on or off
    question: How do I switch on event tracking for my account?
  - id: remove-event-name-only
    intent: Delete a tracked event name
    question: How do I stop tracking a custom event name?
  phrasing_ops: 5
  slug: activecampaign-event-tracking-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Failures API from ActiveCampaign — 1 operation(s) for failures.
  name: ActiveCampaign Failures API
  phrasing_intents:
  - id: getBroadcastFailures
    intent: See why an SMS broadcast failed to deliver
    question: Why did some messages in my SMS broadcast fail?
  phrasing_ops: 1
  slug: activecampaign-failures-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Fields API from ActiveCampaign — 7 operation(s) for fields.
  name: ActiveCampaign Fields API
  phrasing_intents:
  - id: create-a-contact-custom-field
    intent: Create a contact custom field
    question: How do I add a custom field like Company Size to contacts?
  - id: retrieve-fields
    intent: List contact custom fields
    question: What custom contact fields exist in my ActiveCampaign account?
  - id: update-a-field
    intent: Update a contact custom field
    question: Can I rename a contact custom field or change its type?
  - id: retrieve-a-custom-field-contact
    intent: Get a contact custom field
    question: Where do I see the definition of one contact custom field?
  - id: delete-a-field
    intent: Delete a contact custom field
    question: How do I delete a contact custom field I don't need?
  - id: create-a-custom-field-relationship-to-lists
    intent: Attach a custom field to lists
    question: Can I make a custom field available only on certain lists?
  - id: create-custom-field-options
    intent: Add options to a dropdown custom field
    question: How do I add choices to a dropdown or checkbox custom field?
  - id: delete-a-custom-field-relationship-to-lists
    intent: Detach a custom field from a list
    question: Can I stop a custom field from showing on a particular list?
  phrasing_ops: 13
  slug: activecampaign-fields-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Forms API from ActiveCampaign — 3 operation(s) for forms.
  name: ActiveCampaign Forms API
  phrasing_intents:
  - id: retrieve-forms
    intent: Get a signup form
    question: Where can I see the configuration of one ActiveCampaign form?
  - id: delete_forms{id}
    intent: Delete a signup form
    question: How do I delete a form we no longer use?
  - id: put_forms{id}
    intent: Update a signup form
    question: Can I edit an existing signup form?
  - id: forms-1
    intent: List signup forms
    question: Which signup forms exist in my account?
  - id: post_forms
    intent: Create a signup form
    question: How do I create a new signup form?
  - id: post_formoptin
    intent: Submit a form opt-in
    question: Can I record a contact opting in through a form?
  phrasing_ops: 6
  slug: activecampaign-forms-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Groups API from ActiveCampaign — 7 operation(s) for groups.
  name: ActiveCampaign Groups API
  phrasing_intents:
  - id: add-custom-field-to-field-group
    intent: Add a custom field to a field group
    question: How do I put a custom field into a field group?
  - id: get-all-custom-field-groups
    intent: List custom field group memberships
    question: Which custom fields are placed in which field groups?
  - id: delete-custom-field-field-group
    intent: Delete a custom field group membership
    question: How do I take a custom field out of its field group?
  - id: get-custom-field-to-field-group
    intent: Retrieve a custom field group membership
    question: How do I look up one custom field group entry by its ID?
  - id: create-a-custom-field-group
    intent: Create a custom field group
    question: How do I create a new custom field group with a name and display order?
  - id: update-custom-field-field-group
    intent: Move or reorder a field in a field group
    question: How do I change the order of a custom field inside its field group?
  - id: create-a-new-group
    intent: Create a user permission group
    question: How do I create a new user group with its own permissions?
  - id: list-all-groups
    intent: List user permission groups
    question: What user groups are set up in my ActiveCampaign account?
  phrasing_ops: 12
  slug: activecampaign-groups-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Lists API from ActiveCampaign — 5 operation(s) for lists.
  name: ActiveCampaign Lists API
  phrasing_intents:
  - id: create-new-list
    intent: Create a contact list
    question: How do I create a new mailing list?
  - id: retrieve-all-lists
    intent: List contact lists
    question: Which mailing lists do I have in ActiveCampaign?
  - id: retrieve-a-list
    intent: Get a contact list
    question: Where do I see the settings for one mailing list?
  - id: delete-a-list
    intent: Delete a contact list
    question: How do I delete a mailing list?
  - id: create-a-list-group-permission
    intent: Grant a user group access to a list
    question: Can I give a user group permission to a specific list?
  - id: exclusions-retrieve-an-exclusion
    intent: Get a list exclusion
    question: Where do I see the details of one exclusion rule?
  - id: update-an-exclusion
    intent: Update a list exclusion
    question: Can I change which lists an exclusion applies to?
  - id: exclusions-retrieve-a-list
    intent: List exclusions
    question: Which email addresses or patterns are excluded from my lists?
  phrasing_ops: 8
  slug: activecampaign-lists-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Messages API from ActiveCampaign — 2 operation(s) for messages.
  name: ActiveCampaign Messages API
  phrasing_intents:
  - id: create-a-new-message
    intent: Create an email message
    question: How do I create a new email message with a subject and body?
  - id: list-all-messages
    intent: List email messages
    question: Which email messages exist in my ActiveCampaign account?
  - id: retrieve-a-message
    intent: Get an email message
    question: What subject and content does a particular message have?
  - id: update-a-message
    intent: Update an email message
    question: Can I change the subject line of an existing message?
  - id: delete-a-message
    intent: Delete an email message
    question: How do I remove an email message I no longer need?
  phrasing_ops: 5
  slug: activecampaign-messages-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Metrics API from ActiveCampaign — 5 operation(s) for metrics.
  name: ActiveCampaign Metrics API
  phrasing_intents:
  - id: getBroadcastMetrics
    intent: Get metrics for specific SMS broadcasts
    question: How did my SMS broadcasts perform over a given date range?
  - id: getBroadcastSnapshot
    intent: Get a snapshot of all SMS broadcasts
    question: What is the overall summary of all my SMS broadcasts for last month?
  - id: getBroadcastSnapshotByIds
    intent: Get a snapshot for chosen SMS broadcasts
    question: Can I get the summary snapshot for only selected SMS broadcasts?
  - id: exportBroadcastMetrics
    intent: Export SMS broadcast metrics as CSV
    question: How do I download SMS broadcast performance as a CSV file?
  phrasing_ops: 4
  slug: activecampaign-metrics-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Notes API from ActiveCampaign — 2 operation(s) for notes.
  name: ActiveCampaign Notes API
  phrasing_intents:
  - id: retrieve-list-of-all-notes
    intent: List all notes
    question: What notes have been written across my ActiveCampaign account?
  - id: create-a-note
    intent: Create a note
    question: How do I add a note to a contact, deal or account record?
  - id: retrieve-a-note
    intent: Get a note
    question: Where do I read a single note by its ID?
  - id: update-a-note
    intent: Update a note
    question: Can I edit the text of an existing note?
  - id: delete-note
    intent: Delete a note
    question: How do I delete a note?
  phrasing_ops: 5
  slug: activecampaign-notes-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Other API from ActiveCampaign — 14 operation(s) for other.
  name: ActiveCampaign Other API
  phrasing_intents:
  - id: list-contact-activities
    intent: List a contact's recent activity
    question: What has a contact been doing recently in ActiveCampaign?
  - id: retrieve-a-contacts-geo-ip-address
    intent: Get a contact's geo IP location
    question: Where is a contact located based on their IP address?
  - id: list-all-email-activities
    intent: List email activities
    question: Which emails have been exchanged with a specific contact?
  - id: get-a-single-record-using-external-id
    intent: Get a custom object record by external ID
    question: Can I find a custom object record using the ID from my own system?
  - id: create-connection
    intent: Create an integration connection
    question: How do I connect an online store so its orders sync in?
  - id: list-all-connections
    intent: List e-commerce store connections
    question: Which stores or integrations are connected to my account for deep data?
  - id: get-connection
    intent: Get an integration connection
    question: What service, name and status does a particular connection have?
  - id: update-connection
    intent: Update an integration connection
    question: Can I change the name or logo of an existing store connection?
  phrasing_ops: 18
  slug: activecampaign-other-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Personalizations API from ActiveCampaign — 5 operation(s) for personalizations.
  name: ActiveCampaign Personalizations API
  phrasing_intents:
  - id: list-variables
    intent: List personalization variables
    question: What personalization variables can I use in my ActiveCampaign emails?
  - id: create-variable
    intent: Create a personalization variable
    question: How do I create a reusable personalization variable for email content?
  - id: retrieve-variable
    intent: Retrieve a personalization variable
    question: How do I see the content of one personalization variable?
  - id: edit-variable
    intent: Edit a personalization variable
    question: How do I change the content of a personalization variable I already made?
  - id: delete-variable
    intent: Delete a personalization variable
    question: How do I delete a single personalization variable?
  - id: bulk-delete-variables
    intent: Delete several personalization variables at once
    question: Can I delete many personalization variables in one call?
  - id: get_{personalizationId}lock
    intent: Lock a personalization variable
    question: How do I lock a personalization variable so it can't be edited?
  - id: patch_new-endpoint
    intent: Unlock a personalization variable
    question: How do I unlock a locked personalization variable?
  phrasing_ops: 8
  slug: activecampaign-personalizations-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Recipients API from ActiveCampaign — 2 operation(s) for recipients.
  name: ActiveCampaign Recipients API
  phrasing_intents:
  - id: getBroadcastRecipients
    intent: List recipients of an SMS broadcast
    question: Who received a specific SMS broadcast?
  - id: exportBroadcastRecipients
    intent: Export SMS broadcast recipients to CSV
    question: How do I download a CSV of everyone who got a text broadcast?
  phrasing_ops: 2
  slug: activecampaign-recipients-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Saved Responses API from ActiveCampaign — 2 operation(s) for saved responses.
  name: ActiveCampaign Saved Responses API
  phrasing_intents:
  - id: saved-responses
    intent: Create a saved email response
    question: How do I save a reusable reply template for one-to-one emails?
  - id: list-all-saved-responses
    intent: List saved email responses
    question: What canned replies have I saved in ActiveCampaign?
  - id: get-a-savedresponse
    intent: Retrieve a saved email response
    question: How do I read the text of one saved response?
  - id: update-a-saved-response
    intent: Update a saved email response
    question: How do I edit the wording of an existing saved response?
  - id: retrieve-a-savedresponse
    intent: Delete a saved email response
    question: How do I delete a canned reply I no longer use?
  phrasing_ops: 5
  slug: activecampaign-saved-responses-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Scores API from ActiveCampaign — 2 operation(s) for scores.
  name: ActiveCampaign Scores API
  phrasing_intents:
  - id: retrieve-a-score
    intent: Get a scoring rule
    question: How is a specific scoring rule set up?
  - id: list-all-scores
    intent: List scoring rules
    question: Which scores are defined in ActiveCampaign?
  phrasing_ops: 2
  slug: activecampaign-scores-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Site Tracking API from ActiveCampaign — 2 operation(s) for site tracking.
  name: ActiveCampaign Site Tracking API
  phrasing_intents:
  - id: retrieve-site-tracking-code
    intent: Get the site tracking code snippet
    question: Where do I get the JavaScript snippet to install site tracking on my website?
  - id: retrieve-site-tracking-status
    intent: Check whether site tracking is enabled
    question: Is site tracking currently turned on for my account?
  - id: enable-disable-site-tracking
    intent: Turn site tracking on or off
    question: How do I switch site tracking on for my account?
  phrasing_ops: 3
  slug: activecampaign-site-tracking-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Tags API from ActiveCampaign — 2 operation(s) for tags.
  name: ActiveCampaign Tags API
  phrasing_intents:
  - id: create-a-new-tag
    intent: Create a tag
    question: How do I create a new tag for contacts?
  - id: retrieve-all-tags
    intent: List or search tags
    question: What tags have I created in ActiveCampaign?
  - id: retrieve-a-tag
    intent: Get a tag
    question: What name and description does a specific tag have?
  - id: update-a-tag
    intent: Rename or edit a tag
    question: Can I rename an existing tag?
  - id: delete-a-tag
    intent: Delete a tag
    question: How do I delete a tag I no longer use?
  phrasing_ops: 5
  slug: activecampaign-tags-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Tasks API from ActiveCampaign — 6 operation(s) for tasks.
  name: ActiveCampaign Tasks API
  phrasing_intents:
  - id: create-a-task-outcome
    intent: Create a task outcome
    question: How do I add a new outcome like 'Left voicemail' for tasks?
  - id: list-all-task-outcomes
    intent: List task outcomes
    question: What outcomes can a completed CRM task be marked with?
  - id: retrieve-a-task-outcome
    intent: Get a task outcome
    question: What title and sentiment does a specific task outcome have?
  - id: update-a-task-outcome
    intent: Update a task outcome
    question: Can I rename a task outcome or change its sentiment?
  - id: delete-a-task-outcome
    intent: Delete a task outcome
    question: How do I permanently remove a task outcome?
  - id: create-a-task-outcome-1
    intent: Link an outcome to a task type
    question: How do I make an outcome available for a particular task type?
  - id: list-all-task-type-outcome-relations
    intent: List task type to outcome links
    question: Which outcomes are available for each task type?
  - id: retrieve-a-task-type-outcome-relation
    intent: Get a task type to outcome link
    question: What task type and outcome does a single relation connect?
  phrasing_ops: 11
  slug: activecampaign-tasks-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Templates API from ActiveCampaign — 1 operation(s) for templates.
  name: ActiveCampaign Templates API
  phrasing_intents:
  - id: retrieve-a-template
    intent: Retrieve an email template
    question: How do I fetch one of my saved email templates by ID?
  - id: ListWhatsAppTemplates
    intent: List WhatsApp message templates
    question: What WhatsApp templates do I have in ActiveCampaign?
  - id: GetWhatsAppTemplate
    intent: Retrieve a WhatsApp template
    question: How do I check the approval status of a specific WhatsApp template?
  - id: channels_whatsapp_template_update
    intent: Update a WhatsApp template
    question: How do I edit the text or language of a WhatsApp template?
  - id: DeleteWhatsAppTemplate
    intent: Delete a WhatsApp template
    question: How do I delete a WhatsApp template I no longer need?
  - id: SendAWhatsAppTemplateMessage
    intent: Send a WhatsApp template message
    question: How do I send a WhatsApp message to a phone number using an approved template?
  phrasing_ops: 6
  slug: activecampaign-templates-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Users API from ActiveCampaign — 5 operation(s) for users.
  name: ActiveCampaign Users API
  phrasing_intents:
  - id: create-user
    intent: Create a user
    question: How do I add a new teammate as a user?
  - id: list-all-users
    intent: List account users
    question: Who has a user login on my ActiveCampaign account?
  - id: get-user
    intent: Get a user by ID
    question: What details are stored for a user with a given ID?
  - id: update-user
    intent: Update a user
    question: Can I change a teammate's name, email or group?
  - id: delete-user
    intent: Delete a user
    question: How do I remove a teammate who has left?
  - id: get-user-email
    intent: Find a user by email
    question: Which user account belongs to a given email address?
  - id: get-user-username
    intent: Find a user by username
    question: Who is the user behind a particular username?
  - id: get-user-loggedin
    intent: Get the logged-in user
    question: Which user does my API key belong to?
  phrasing_ops: 8
  slug: activecampaign-users-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Webhooks API from ActiveCampaign — 3 operation(s) for webhooks.
  name: ActiveCampaign Webhooks API
  phrasing_intents:
  - id: create-webhook
    intent: Create a webhook
    question: How do I get notified at my URL when a contact subscribes?
  - id: get-a-list-of-webhooks
    intent: List webhooks
    question: Which webhooks are configured in my ActiveCampaign account?
  - id: get-webhook
    intent: Get a webhook
    question: Where can I see the settings of one webhook?
  - id: update-webhook
    intent: Update a webhook
    question: Can I change the URL or events on an existing webhook?
  - id: delete-webhook
    intent: Delete a webhook
    question: How do I stop and remove a webhook?
  - id: get-a-list-of-webhook-events
    intent: List available webhook events
    question: What events can a webhook subscribe to?
  phrasing_ops: 6
  slug: activecampaign-webhooks-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Manage documents attached to AI customization profiles.
  name: ActiveCampaign AI Customization Documents API
  phrasing_intents:
  - id: get_ai_customizations_documents_list
    intent: List documents on an AI profile
    question: Which reference documents are uploaded to an AI customization profile?
  - id: post_ai_customizations_documents_upload
    intent: Upload a document to an AI profile
    question: How do I give the AI my brand guidelines as a document?
  - id: get_ai_customizations_documents_get
    intent: Get an AI profile document
    question: Where do I see the details of one document on an AI profile?
  - id: delete_ai_customizations_documents_delete
    intent: Delete an AI profile document
    question: Can I remove an outdated document from an AI profile?
  - id: patch_ai_customizations_documents_update
    intent: Enable, disable or retag an AI document
    question: Can I turn off a document so the AI ignores it without deleting it?
  - id: get_ai_customizations_documents_download
    intent: Get a download link for an AI document
    question: How can I download the original file I uploaded to an AI profile?
  phrasing_ops: 6
  slug: activecampaign-ai-customization-documents-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Manage custom instructions for AI customization profiles.
  name: ActiveCampaign AI Customization Instructions API
  phrasing_intents:
  - id: get_ai_customizations_instructions_list
    intent: List custom AI instructions for a profile
    question: What custom instructions guide the AI for a given customization profile?
  - id: post_ai_customizations_instructions_create
    intent: Add a custom AI instruction
    question: How do I tell the AI to always write in a certain tone?
  - id: get_ai_customizations_instructions_get
    intent: Get one custom AI instruction
    question: What does a specific AI instruction say and is it enabled?
  - id: delete_ai_customizations_instructions_delete
    intent: Delete a custom AI instruction
    question: How do I remove an AI instruction I no longer want applied?
  - id: patch_ai_customizations_instructions_update
    intent: Edit or toggle a custom AI instruction
    question: Can I turn off an AI instruction without deleting it?
  phrasing_ops: 5
  slug: activecampaign-ai-customization-instructions-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Manage AI customization profiles.
  name: ActiveCampaign AI Customization Profiles API
  phrasing_intents:
  - id: get_ai_customizations_profiles_list
    intent: List AI customization profiles
    question: What AI customization profiles have I set up in ActiveCampaign?
  - id: post_ai_customizations_profiles_create
    intent: Create an AI customization profile
    question: How do I create a new AI customization profile?
  - id: get_ai_customizations_profiles_get
    intent: Retrieve an AI customization profile
    question: How do I look up one AI customization profile by ID?
  - id: delete_ai_customizations_profiles_delete
    intent: Delete an AI customization profile
    question: How do I delete an AI customization profile I no longer use?
  - id: patch_ai_customizations_profiles_update
    intent: Rename an AI customization profile
    question: How do I rename an existing AI customization profile?
  - id: get_ai_customizations_profiles_get_by_child_account
    intent: Get the AI profile assigned to a child account
    question: Which AI customization profile is a given child account using?
  - id: patch_ai_customizations_profiles_assign_accounts
    intent: Assign child accounts to an AI profile
    question: How do I assign several child accounts to one AI customization profile?
  phrasing_ops: 7
  slug: activecampaign-ai-customization-profiles-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Create and manage snapshots of reseller child accounts.
  name: ActiveCampaign Child Account Snapshots API
  phrasing_intents:
  - id: get_child_account_snapshots_get_list
    intent: List child account cloning statuses
    question: Are my child account cloning jobs finished yet?
  - id: get_child_account_snapshots_list_snapshot_by_reseller
    intent: List account snapshots
    question: Which account snapshots do I have as a reseller?
  - id: post_child_account_snapshots_create_snapshot
    intent: Snapshot an account for cloning
    question: How do I capture an account's setup as a snapshot to reuse for child accounts?
  - id: delete_child_account_snapshots_delete_snapshot
    intent: Delete an account snapshot
    question: Can I remove a snapshot I no longer need?
  phrasing_ops: 4
  slug: activecampaign-child-account-snapshots-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Manage reseller child accounts.
  name: ActiveCampaign Child Accounts API
  phrasing_intents:
  - id: get_child_accounts_get_list
    intent: List child accounts
    question: What child accounts sit under my ActiveCampaign reseller account?
  - id: post_child_accounts_create
    intent: Create a child account
    question: How do I provision a new child account for a client?
  - id: get_child_accounts_get_for_snapshots
    intent: List accounts eligible for snapshots
    question: Which of my accounts can be used as the source for a snapshot?
  phrasing_ops: 3
  slug: activecampaign-child-accounts-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Conversations API from ActiveCampaign — 2 operation(s) for conversations.
  name: ActiveCampaign Conversations API
  phrasing_intents:
  - id: ListConversations
    intent: List WhatsApp inbox conversations
    question: Which WhatsApp conversations are in my ActiveCampaign inbox?
  - id: UpdateAConversation
    intent: Replace a WhatsApp conversation record
    question: How do I fully overwrite a WhatsApp conversation with all its required fields?
  - id: PartiallyUpdateAConversation
    intent: Change a WhatsApp conversation's status or assignee
    question: Can I close a WhatsApp conversation without resending the whole record?
  phrasing_ops: 3
  slug: activecampaign-conversations-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Count History API from ActiveCampaign — 2 operation(s) for count history.
  name: ActiveCampaign Count History API
  phrasing_intents:
  - id: get_count_history_by_segment_id
    intent: Get a segment's latest count history
    question: How has the size of a segment changed over time?
  - id: get_count_history_with_timestamp
    intent: Page segment count history from a timestamp
    question: How do I get the next page of a segment's count history?
  phrasing_ops: 2
  slug: activecampaign-count-history-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Read-only CRM pipeline reporting and metrics.
  name: ActiveCampaign CRM Reporting API
  phrasing_intents:
  - id: get_crm_reporting_list_pipelines
    intent: Report on each sales pipeline
    question: Which pipelines brought in the most revenue this quarter?
  - id: get_crm_reporting_pipelines_summary
    intent: Summarize deal metrics across pipelines
    question: What is my total deal revenue and average deal size for a period?
  phrasing_ops: 2
  slug: activecampaign-crm-reporting-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Configure CRM synchronization for HQ pipelines.
  name: ActiveCampaign CRM Sync API
  phrasing_intents:
  - id: get_crm_sync_list_pipelines
    intent: List pipelines with CRM sync status
    question: Which of my pipelines are syncing to the external CRM?
  - id: get_crm_sync_get_pipeline_sync_config
    intent: Get a pipeline's CRM sync setup
    question: Is CRM sync turned on for a particular pipeline?
  - id: put_crm_sync_put_pipeline_sync_config
    intent: Turn CRM sync on or off for a pipeline
    question: How do I enable CRM sync for one pipeline?
  phrasing_ops: 3
  slug: activecampaign-crm-sync-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Manage CRM synchronization settings.
  name: ActiveCampaign CRM Sync Settings API
  phrasing_intents:
  - id: get_crm_sync_settings_get
    intent: Get CRM sync settings
    question: How often is my CRM sync currently running?
  - id: put_crm_sync_settings_update
    intent: Change CRM sync frequency
    question: Can I make the CRM sync run more often?
  phrasing_ops: 2
  slug: activecampaign-crm-sync-settings-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Event API from ActiveCampaign — 1 operation(s) for event.
  name: ActiveCampaign Event API
  phrasing_intents:
  - id: track-event
    intent: Track a custom event for a contact
    question: How do I record a custom event, like a purchase or signup, against a contact?
  phrasing_ops: 1
  slug: activecampaign-event-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Storage quota information for the partner.
  name: ActiveCampaign Files API
  phrasing_intents:
  - id: get_files_quota_status
    intent: Check file storage quota
    question: How much file storage have I used in ActiveCampaign?
  phrasing_ops: 1
  slug: activecampaign-files-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Flows API from ActiveCampaign — 5 operation(s) for flows.
  name: ActiveCampaign Flows API
  phrasing_intents:
  - id: ListFlowExecution
    intent: List WhatsApp flow runs
    question: Which WhatsApp flows have been run and when?
  - id: ListFlowExecutionContact
    intent: List contacts in WhatsApp flow runs
    question: Which contacts are currently active in a WhatsApp flow?
  - id: GetFlowExecutionContact
    intent: Get one contact's WhatsApp flow run
    question: Where do I see a single contact's progress through a flow run?
  - id: GetFlowExecution
    intent: Get a WhatsApp flow run
    question: Where can I check the details of one flow execution?
  - id: CreateAFlowExecution
    intent: Run a WhatsApp flow for contacts
    question: How do I start a WhatsApp flow for a list of contacts?
  phrasing_ops: 5
  slug: activecampaign-flows-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Retrieve and update partner insight cards.
  name: ActiveCampaign Insight Cards API
  phrasing_intents:
  - id: get_insight_cards_get_list_latest
    intent: List the latest insight cards
    question: What are the latest insight cards ActiveCampaign has generated for my account?
  - id: patch_insight_cards_update_state
    intent: Update an insight card's state
    question: How do I mark an insight card as dismissed or acted on?
  phrasing_ops: 2
  slug: activecampaign-insight-cards-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Supported language and timezone catalogs.
  name: ActiveCampaign Locales API
  phrasing_intents:
  - id: get_locales_get_catalogs
    intent: List supported languages and timezones
    question: Which languages and timezones can a child account be set to?
  phrasing_ops: 1
  slug: activecampaign-locales-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Return all Contact id's that match the given Segment and provided Additional Criteria
  name: ActiveCampaign Match All API
  phrasing_intents:
  - id: create_match_all_request
    intent: Find all contacts matching a new segment definition
    question: How do I get every contact ID that matches segment conditions I define on the fly?
  - id: create_match_all_request_with_segment_id
    intent: Find all contacts in a saved segment
    question: How do I list every contact that matches a segment I already have?
  - id: get_result_set_by_id
    intent: Get the results of a match-all run
    question: How do I check whether my segment match-all run has finished?
  - id: find_contact_id_by_ac_playload
    intent: Check which given contacts match a segment
    question: Can I test whether a handful of specific contacts fall into a segment?
  - id: get_result_set_by_run_id
    intent: Get the results of a match-some run
    question: Where do I collect the results of a match-some request?
  phrasing_ops: 5
  slug: activecampaign-match-all-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Evaluate Contact Id against the provided SegmentId. Returns `true` if Contact matches the given Segment
  name: ActiveCampaign Match One API
  phrasing_intents:
  - id: create_match_one_request
    intent: Check if a contact is in a segment
    question: Does a particular contact currently match a segment?
  - id: segment_match_check_by_external_id
    intent: Check a segment match using an external ID
    question: Can I check a segment match for a contact scoped to an external ID?
  phrasing_ops: 2
  slug: activecampaign-match-one-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Most Recent Count History API from ActiveCampaign — 1 operation(s) for most recent count history.
  name: ActiveCampaign Most Recent Count History API
  phrasing_intents:
  - id: get_recent_count_history
    intent: Get latest contact counts for segments
    question: How many contacts matched my segments the last time they ran?
  phrasing_ops: 1
  slug: activecampaign-most-recent-count-history-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Saved Segments have a name and are visible on the app/segments page. Saved Segments have Summaries
  name: ActiveCampaign Saved Segment Summaries API
  phrasing_intents:
  - id: get_saved_segment_summaries
    intent: List summaries of saved segments
    question: What saved segments do I have and how big is each one?
  - id: get_saved_segment_summaries_by_id
    intent: Get one saved segment's summary
    question: How do I see the summary for one saved segment?
  phrasing_ops: 2
  slug: activecampaign-saved-segment-summaries-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: Segment JSON structure is extremely flexible. Only segments that are supported by the segment-builder are guaranteed to work as expected. Specific Conditions types only support a subset of FieldDO and
  name: ActiveCampaign Segments API
  phrasing_intents:
  - id: create_segment
    intent: Create a contact segment
    question: How do I build a new segment of contacts from conditions?
  - id: retrieve_segment
    intent: Get a segment's current definition
    question: What conditions make up a segment right now?
  - id: update_segment
    intent: Update a segment
    question: Can I change the conditions of an existing segment?
  - id: delete_segment
    intent: Delete a segment and its history
    question: What happens to a segment's past versions when I delete it?
  - id: get_segment_historic
    intent: See a segment as it was at a past time
    question: What did a segment's conditions look like last month?
  - id: segment_revert_to_history
    intent: Revert a segment to an earlier version
    question: Can I undo changes to a segment by rolling it back?
  phrasing_ops: 6
  slug: activecampaign-segments-api
- baseURL: https://youraccountname.api-us1.com/api/3
  baseurl_source: declared
  description: The Template API from ActiveCampaign — 1 operation(s) for template.
  name: ActiveCampaign Template API
  phrasing_intents:
  - id: create-shareable-campaign-template-link
    intent: Create a shareable link to a campaign template
    question: How do I share one of my campaign templates with someone outside my account?
  phrasing_ops: 1
  slug: activecampaign-template-api
arazzos:
- description: Create an account record then associate an existing contact with it.
  name: ActiveCampaign Create Account and Associate a Contact
  slug: activecampaign-create-account-add-contact-workflow
- description: Create an account record then attach an explanatory note to it.
  name: ActiveCampaign Create Account and Add a Note
  slug: activecampaign-create-account-add-note-workflow
- description: Create a contact then enroll it into a marketing automation.
  name: ActiveCampaign Create Contact and Enroll in Automation
  slug: activecampaign-create-contact-add-to-automation-workflow
- description: Create a contact, subscribe it to a list, then apply a tag in one pass.
  name: ActiveCampaign Create Contact, Subscribe to List, and Tag
  slug: activecampaign-create-contact-add-to-list-tag-workflow
- description: Resolve an account by name, create a contact, then associate them.
  name: ActiveCampaign Create Contact and Associate to an Account by Name
  slug: activecampaign-create-contact-associate-account-by-name-workflow
- description: Create a contact then write a value to one of its custom fields.
  name: ActiveCampaign Create Contact and Set Custom Field Value
  slug: activecampaign-create-contact-set-custom-field-workflow
- description: Define a new contact custom field then set its value on a contact.
  name: ActiveCampaign Create Contact Custom Field and Set Its Value
  slug: activecampaign-create-custom-field-set-on-contact-workflow
- description: Create a deal in a pipeline stage then attach an explanatory note.
  name: ActiveCampaign Create Deal and Add a Note
  slug: activecampaign-create-deal-add-note-workflow
- description: Create a deal then schedule a follow-up task against it.
  name: ActiveCampaign Create Deal and Schedule a Task
  slug: activecampaign-create-deal-add-task-workflow
- description: Resolve a contact by email, creating it if missing, then open a deal.
  name: ActiveCampaign Find Contact by Email and Create a Deal
  slug: activecampaign-create-deal-for-contact-by-email-workflow
- description: Create a deal then write a value to one of its custom fields.
  name: ActiveCampaign Create Deal and Set Custom Field Value
  slug: activecampaign-create-deal-set-custom-field-workflow
- description: Create a mailing list then subscribe an existing contact to it.
  name: ActiveCampaign Create List and Subscribe a Contact
  slug: activecampaign-create-list-add-contact-workflow
- description: Stand up a pipeline, add a stage to it, then open the first deal.
  name: ActiveCampaign Create Pipeline, Stage, and First Deal
  slug: activecampaign-create-pipeline-stage-deal-workflow
- description: Find an automation by name then enroll an existing contact into it.
  name: ActiveCampaign Resolve Automation by Name and Enroll Contact
  slug: activecampaign-enroll-contact-in-automation-by-name-workflow
- description: Search deals by title then attach a note to the matched deal.
  name: ActiveCampaign Find a Deal by Title and Add a Note
  slug: activecampaign-find-deal-add-note-workflow
- description: Look up a contact by email, create it if missing, then apply a tag.
  name: ActiveCampaign Find or Create Contact, Then Tag
  slug: activecampaign-find-or-create-contact-tag-workflow
- description: Resolve a tag by name, creating it if needed, then tag a contact.
  name: ActiveCampaign Find or Create Tag, Then Apply to Contact
  slug: activecampaign-find-or-create-tag-and-apply-workflow
- description: Resolve a list by name then subscribe an existing contact to it.
  name: ActiveCampaign Subscribe Contact to a List Resolved by Name
  slug: activecampaign-subscribe-contact-to-list-by-name-workflow
- description: Upsert a contact by email via sync, then subscribe it to a list.
  name: ActiveCampaign Sync Contact and Subscribe to List
  slug: activecampaign-sync-contact-add-to-list-workflow
- description: Upsert a contact by email, set a custom field, then apply a tag.
  name: ActiveCampaign Sync Contact, Set Custom Field, and Tag
  slug: activecampaign-sync-contact-set-custom-field-tag-workflow
- description: Apply a tag to an existing contact then enroll it in an automation.
  name: ActiveCampaign Tag a Contact and Enroll in Automation
  slug: activecampaign-tag-contact-and-enroll-automation-workflow
artifact_total: 223
asyncapis:
- description: AsyncAPI description of ActiveCampaign's outbound webhook surface. When a webhook is configured (via the dashboard or the REST API at POST /api/3/webhooks), ActiveCampaign delivers events as HTTP POST
  name: ActiveCampaign Webhooks
  slug: activecampaign-webhooks-asyncapi
collections:
- collection_type: postman
  name: ActiveCampaign SMS Broadcast API
  slug: postman-activecampaign-sms
- collection_type: postman
  name: ActiveCampaign API v3
  slug: postman-activecampaign-v3
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts API
  slug: open-activecampaign-accounts-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Addresses API
  slug: open-activecampaign-addresses-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts AI API
  slug: open-activecampaign-ai-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Automations API
  slug: open-activecampaign-automations-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Branding API
  slug: open-activecampaign-branding-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Broadcasts API
  slug: open-activecampaign-broadcasts-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Bulk Import API
  slug: open-activecampaign-bulk-import-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Calendars API
  slug: open-activecampaign-calendars-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Campaigns API
  slug: open-activecampaign-campaigns-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Contacts API
  slug: open-activecampaign-contacts-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Credits API
  slug: open-activecampaign-credits-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Custom Objects API
  slug: open-activecampaign-custom-objects-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Deals API
  slug: open-activecampaign-deals-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Ecommerce API
  slug: open-activecampaign-ecommerce-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Event Tracking API
  slug: open-activecampaign-event-tracking-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Exports API
  slug: open-activecampaign-exports-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Failures API
  slug: open-activecampaign-failures-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Fields API
  slug: open-activecampaign-fields-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Forms API
  slug: open-activecampaign-forms-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Groups API
  slug: open-activecampaign-groups-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Lists API
  slug: open-activecampaign-lists-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Messages API
  slug: open-activecampaign-messages-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Metrics API
  slug: open-activecampaign-metrics-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Notes API
  slug: open-activecampaign-notes-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Other API
  slug: open-activecampaign-other-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Personalizations API
  slug: open-activecampaign-personalizations-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Recipients API
  slug: open-activecampaign-recipients-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Saved Responses API
  slug: open-activecampaign-saved-responses-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Scores API
  slug: open-activecampaign-scores-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Site Tracking API
  slug: open-activecampaign-site-tracking-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast API
  slug: open-activecampaign-sms
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Snapshots API
  slug: open-activecampaign-snapshots-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Tags API
  slug: open-activecampaign-tags-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Tasks API
  slug: open-activecampaign-tasks-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Templates API
  slug: open-activecampaign-templates-api
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Users API
  slug: open-activecampaign-users-api
- collection_type: open
  name: ActiveCampaign API v3
  slug: open-activecampaign-v3
- collection_type: open
  name: ActiveCampaign SMS Broadcast Accounts Webhooks API
  slug: open-activecampaign-webhooks-api
- collection_type: open
  name: WhatsApp API
  slug: open-activecampaign-whatsapp-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-exports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-exports-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-snapshots-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-snapshots-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-segments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-segments-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-segment-matching-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-segment-matching-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-segment-match-one-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-segment-match-one-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-partners-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-partners-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-whatsapp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-whatsapp-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-trackcmp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-trackcmp-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/overlays/activecampaign-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/activecampaign-v2-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/security/activecampaign-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/activecampaign-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.activecampaign.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.activecampaign.com
- group: operate
  title: ''
  type: Support
  url: https://help.activecampaign.com
- group: start
  title: ''
  type: SignUp
  url: https://www.activecampaign.com/signup/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/a2a/activecampaign-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/activecampaign-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/agentic-access/activecampaign-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/activecampaign-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/security/activecampaign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/activecampaign-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/authentication/activecampaign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/activecampaign-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-account-add-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-account-add-contact-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-account-add-note-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-account-add-note-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-contact-add-to-automation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-contact-add-to-automation-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-contact-add-to-list-tag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-contact-add-to-list-tag-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-contact-associate-account-by-name-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-contact-associate-account-by-name-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-contact-set-custom-field-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-contact-set-custom-field-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-custom-field-set-on-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-custom-field-set-on-contact-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-deal-add-note-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-deal-add-note-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-deal-add-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-deal-add-task-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-deal-for-contact-by-email-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-deal-for-contact-by-email-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-deal-set-custom-field-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-deal-set-custom-field-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-list-add-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-list-add-contact-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-create-pipeline-stage-deal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-create-pipeline-stage-deal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-enroll-contact-in-automation-by-name-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-enroll-contact-in-automation-by-name-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-find-deal-add-note-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-find-deal-add-note-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-find-or-create-contact-tag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-find-or-create-contact-tag-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-find-or-create-tag-and-apply-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-find-or-create-tag-and-apply-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-subscribe-contact-to-list-by-name-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-subscribe-contact-to-list-by-name-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-sync-contact-add-to-list-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-sync-contact-add-to-list-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-sync-contact-set-custom-field-tag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-sync-contact-set-custom-field-tag-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/arazzo/activecampaign-tag-contact-and-enroll-automation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/activecampaign-tag-contact-and-enroll-automation-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/activecampaign
- group: start
  title: ''
  type: Portal
  url: https://developers.activecampaign.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API
- group: auth
  title: ''
  type: Authentication
  url: https://developers.activecampaign.com/reference/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.activecampaign.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.activecampaign.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://www.activecampaign.com/about/faq
- group: operate
  title: ''
  type: Forums
  url: https://community.activecampaign.com/latest
- group: operate
  title: ''
  type: StatusPage
  url: https://status.activecampaign.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/acdevrel/activecampaign-developer-relations/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActiveCampaign
- group: build
  title: PHP SDK
  type: SDKs
  url: https://github.com/ActiveCampaign/activecampaign-api-php
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://github.com/ActiveCampaign/activecampaign-api-nodejs
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/rules/activecampaign-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/activecampaign-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/vocabulary/activecampaign-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/activecampaign-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/json-ld/activecampaign-sms-context.jsonld
  title: SMS API Context
  type: JSONLD
  url: json-ld/activecampaign-sms-context.jsonld
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/mcp/activecampaign-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/activecampaign-mcp.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/ActiveCampaign/activecampaign-plugin
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.activecampaign.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/well-known/activecampaign-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/activecampaign-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developers.activecampaign.com/.well-known/api-catalog
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/mcp/activecampaign-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/activecampaign-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/llms/activecampaign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/activecampaign-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/packages/activecampaign-packages.yml
  title: ''
  type: Packages
  url: packages/activecampaign-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/packages/activecampaign-packages.yml
  title: ''
  type: SDKs
  url: packages/activecampaign-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/conformance/activecampaign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/activecampaign-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.activecampaign.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.activecampaign.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/errors/activecampaign-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/activecampaign-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/lifecycle/activecampaign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/activecampaign-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/sandbox/activecampaign-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/activecampaign-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/conventions/activecampaign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/activecampaign-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/changelog/activecampaign-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/activecampaign-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/data-model/activecampaign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/activecampaign-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/plans/activecampaign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/activecampaign-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/rate-limits/activecampaign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/activecampaign-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/finops/activecampaign-finops.yml
  title: ''
  type: FinOps
  url: finops/activecampaign-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/security/activecampaign-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/activecampaign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/activecampaign
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/asyncapi/activecampaign-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/activecampaign-webhooks-asyncapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/asyncapi/activecampaign-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/activecampaign-webhooks-asyncapi.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.activecampaign.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.activecampaign.com/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://developers.activecampaign.com/reference/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.activecampaign.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/acdevrel/activecampaign-developer-relations/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.activecampaign.com/reference/overview
created: '2025-02-17'
description: 'ActiveCampaign is a marketing automation and customer experience platform used by more than 180,000 businesses for email marketing, marketing automation, CRM and sales automation. Its developer surface is unusually broad: nine published OpenAPI documents discoverable through a real RFC 9727 /.well-known/api-catalog, covering the v3 REST API, SMS Broadcast, WhatsApp messaging, Segments V2 and asynchronous segment matching, a reseller Partners API, trackcmp event ingest and a surviving v2 operation. It also ships an Ecommerce GraphQL API, an outbound webhook surface, a first-party remote MCP server with a published tool index, an A2A agent card, and an MIT-licensed Claude plugin of first-party Agent Skills. Authentication is a single unscoped Api-Token header; the base URL is per account.'
examples:
- key_count: 3
  name: Activecampaign Sms Ai Broadcast Request Example
  slug: activecampaign-sms-ai-broadcast-request-example
- key_count: 1
  name: Activecampaign Sms Ai Broadcast Response Example
  slug: activecampaign-sms-ai-broadcast-response-example
- key_count: 3
  name: Activecampaign Sms Ai Broadcast Status Example
  slug: activecampaign-sms-ai-broadcast-status-example
- key_count: 4
  name: Activecampaign Sms Ai Broadcast Update Request Example
  slug: activecampaign-sms-ai-broadcast-update-request-example
- key_count: 13
  name: Activecampaign Sms Broadcast Create Request Example
  slug: activecampaign-sms-broadcast-create-request-example
- key_count: 3
  name: Activecampaign Sms Broadcast List Example
  slug: activecampaign-sms-broadcast-list-example
- key_count: 2
  name: Activecampaign Sms Broadcast List Response Example
  slug: activecampaign-sms-broadcast-list-response-example
- key_count: 2
  name: Activecampaign Sms Broadcast Lists Response Example
  slug: activecampaign-sms-broadcast-lists-response-example
- key_count: 25
  name: Activecampaign Sms Broadcast Message Example
  slug: activecampaign-sms-broadcast-message-example
- key_count: 7
  name: Activecampaign Sms Broadcast Metrics Example
  slug: activecampaign-sms-broadcast-metrics-example
- key_count: 1
  name: Activecampaign Sms Broadcast Metrics Response Example
  slug: activecampaign-sms-broadcast-metrics-response-example
- key_count: 14
  name: Activecampaign Sms Broadcast Update Request Example
  slug: activecampaign-sms-broadcast-update-request-example
- key_count: 1
  name: Activecampaign Sms Credits Response Example
  slug: activecampaign-sms-credits-response-example
- key_count: 3
  name: Activecampaign Sms Failure Detail Example
  slug: activecampaign-sms-failure-detail-example
- key_count: 1
  name: Activecampaign Sms Failure Details Response Example
  slug: activecampaign-sms-failure-details-response-example
- key_count: 9
  name: Activecampaign Sms Recipient Example
  slug: activecampaign-sms-recipient-example
- key_count: 2
  name: Activecampaign Sms Recipients Response Example
  slug: activecampaign-sms-recipients-response-example
- key_count: 1
  name: Activecampaign Sms Snapshot Response Example
  slug: activecampaign-sms-snapshot-response-example
features:
- description: Create and send conversion-focused email campaigns with personalization and segmentation.
  name: Email Marketing
- description: Build automated customer journeys and workflows triggered by contact behavior and events.
  name: Marketing Automation
- description: Built-in sales CRM for managing deals, pipelines, tasks, and customer relationships.
  name: CRM
- description: Reach contacts via SMS broadcast campaigns with AI-powered content generation.
  name: SMS Marketing
- description: Automate growth and customer engagement through WhatsApp communications.
  name: WhatsApp Messaging
- description: Automate transactional alerts, password resets, and notifications via Postmark integration.
  name: Transactional Email
- description: Create custom data schemas to activate complex data for segmentation and personalized automation.
  name: Custom Objects
- description: Track contact behaviors and activities across web properties and integrations.
  name: Contact Event Tracking
- description: Receive real-time event notifications for contact, campaign, automation, and custom object activities.
  name: Webhooks
- description: Deploy conversion-ready landing pages for lead capture and campaigns.
  name: Landing Pages
- description: AI-powered orchestration and autonomous marketing agents for campaign suggestions and personalization.
  name: Active Intelligence
- description: Connect AI applications to ActiveCampaign using the Model Context Protocol server.
  name: MCP Server
finops:
- name: Activecampaign Finops
  service_category: API
  slug: activecampaign-finops
image: /assets/icons/activecampaign.png
integrations:
- description: Sync contact and deal data between ActiveCampaign and Salesforce CRM.
  name: Salesforce
- description: Connect ActiveCampaign to 1000+ apps via Zapier automation workflows.
  name: Zapier
- description: Send notifications and trigger automations from Slack using OAuth2 integration.
  name: Slack
- description: Sync scheduling data and trigger automations with custom objects via OAuth2.
  name: Calendly
- description: Integrate SMS workflows using Twilio with Basic Auth for outbound messaging.
  name: Twilio
- description: Sync ecommerce customers, orders, and products for automated campaigns.
  name: Shopify
- description: Embed forms and capture leads from WordPress sites.
  name: WordPress
- description: Connect Wix websites for lead capture and customer journey automation.
  name: Wix
json_schemas:
- name: AIBroadcastRequest
  property_count: 3
  slug: activecampaign-sms-ai-broadcast-request
- name: AIBroadcastResponse
  property_count: 1
  slug: activecampaign-sms-ai-broadcast-response
- name: AIBroadcastStatus
  property_count: 3
  slug: activecampaign-sms-ai-broadcast-status
- name: AIBroadcastUpdateRequest
  property_count: 4
  slug: activecampaign-sms-ai-broadcast-update-request
- name: BroadcastCreateRequest
  property_count: 13
  slug: activecampaign-sms-broadcast-create-request
- name: BroadcastListResponse
  property_count: 2
  slug: activecampaign-sms-broadcast-list-response
- name: BroadcastList
  property_count: 3
  slug: activecampaign-sms-broadcast-list
- name: BroadcastListsResponse
  property_count: 2
  slug: activecampaign-sms-broadcast-lists-response
- name: BroadcastMessage
  property_count: 25
  slug: activecampaign-sms-broadcast-message
- name: BroadcastMetricsResponse
  property_count: 1
  slug: activecampaign-sms-broadcast-metrics-response
- name: BroadcastMetrics
  property_count: 7
  slug: activecampaign-sms-broadcast-metrics
- name: BroadcastUpdateRequest
  property_count: 14
  slug: activecampaign-sms-broadcast-update-request
- name: CreditsResponse
  property_count: 1
  slug: activecampaign-sms-credits-response
- name: FailureDetail
  property_count: 3
  slug: activecampaign-sms-failure-detail
- name: FailureDetailsResponse
  property_count: 1
  slug: activecampaign-sms-failure-details-response
- name: Recipient
  property_count: 9
  slug: activecampaign-sms-recipient
- name: RecipientsResponse
  property_count: 2
  slug: activecampaign-sms-recipients-response
- name: SnapshotResponse
  property_count: 1
  slug: activecampaign-sms-snapshot-response
json_structures:
- name: Activecampaign Sms Ai Broadcast Request Structure
  property_count: 3
  slug: activecampaign-sms-ai-broadcast-request-structure
- name: Activecampaign Sms Ai Broadcast Response Structure
  property_count: 1
  slug: activecampaign-sms-ai-broadcast-response-structure
- name: Activecampaign Sms Ai Broadcast Status Structure
  property_count: 3
  slug: activecampaign-sms-ai-broadcast-status-structure
- name: Activecampaign Sms Ai Broadcast Update Request Structure
  property_count: 4
  slug: activecampaign-sms-ai-broadcast-update-request-structure
- name: Activecampaign Sms Broadcast Create Request Structure
  property_count: 13
  slug: activecampaign-sms-broadcast-create-request-structure
- name: Activecampaign Sms Broadcast List Response Structure
  property_count: 2
  slug: activecampaign-sms-broadcast-list-response-structure
- name: Activecampaign Sms Broadcast List Structure
  property_count: 3
  slug: activecampaign-sms-broadcast-list-structure
- name: Activecampaign Sms Broadcast Lists Response Structure
  property_count: 2
  slug: activecampaign-sms-broadcast-lists-response-structure
- name: Activecampaign Sms Broadcast Message Structure
  property_count: 25
  slug: activecampaign-sms-broadcast-message-structure
- name: Activecampaign Sms Broadcast Metrics Response Structure
  property_count: 1
  slug: activecampaign-sms-broadcast-metrics-response-structure
- name: Activecampaign Sms Broadcast Metrics Structure
  property_count: 7
  slug: activecampaign-sms-broadcast-metrics-structure
- name: Activecampaign Sms Broadcast Update Request Structure
  property_count: 14
  slug: activecampaign-sms-broadcast-update-request-structure
- name: Activecampaign Sms Credits Response Structure
  property_count: 1
  slug: activecampaign-sms-credits-response-structure
- name: Activecampaign Sms Failure Detail Structure
  property_count: 3
  slug: activecampaign-sms-failure-detail-structure
- name: Activecampaign Sms Failure Details Response Structure
  property_count: 1
  slug: activecampaign-sms-failure-details-response-structure
- name: Activecampaign Sms Recipient Structure
  property_count: 9
  slug: activecampaign-sms-recipient-structure
- name: Activecampaign Sms Recipients Response Structure
  property_count: 2
  slug: activecampaign-sms-recipients-response-structure
- name: Activecampaign Sms Snapshot Response Structure
  property_count: 1
  slug: activecampaign-sms-snapshot-response-structure
jsonld:
- class_count: 18
  name: Activecampaign Sms Context
  property_count: 51
  slug: activecampaign-sms-context
layout: provider
mcp_servers:
- description: ActiveCampaign ships a first-party remote MCP server. The tool roster below is the provider's own published table at https://developers.activecampaign.com/page/mcp-available-tools/ (page updatedAt 202
  name: ActiveCampaign Remote MCP Server
  slug: activecampaign-remote-mcp-server
modified: '2026-08-13'
name: ActiveCampaign
nav: Providers
network: true
overview: 'ActiveCampaign publishes 55 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Addresses API, AI API, and 52 more. Tagged areas include Marketing Automation, Email Marketing, CRM, Sales Automation, and Customer Experience.


  The ActiveCampaign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  ActiveCampaign''s developer surface includes documentation, support, signup flow, authentication, developer portal, getting-started guide, pricing, and 80 more developer resources.'
plans:
- name: Activecampaign Plans Pricing
  plan_count: 4
  slug: activecampaign-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Activecampaign Rate Limits
  slug: activecampaign-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: ActiveCampaign API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: activecampaign-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: ActiveCampaign API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: activecampaign-jsonschema-spectral-rules
- effective_rule_count: 26
  extends: []
  name: ActiveCampaign API Rules
  rule_count: 26
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 12
  slug: activecampaign-spectral-rules
score:
  band: exemplar
  composite: 78.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 92.0
    catalog_earned_first_party: 20.0
    catalog_gap: 23.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 56.6
    developer_ergonomics: 71.4
    discoverability: 86.7
    operational_transparency: 76.3
  previous_composite: 77.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 33
      marker_coverage: 60.0
      total: 55
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/activecampaign/refs/heads/main/screenshots/activecampaign-2026-06-20T164212.png
security:
- kind: authentication
  name: Activecampaign Authentication
  slug: activecampaign-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Activecampaign Domain Security
  slug: activecampaign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Activecampaign Vulnerability Disclosure
  slug: activecampaign-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Activecampaign Trust Center
  slug: activecampaign-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 6
skills:
- name: postmark-email-best-practices
  slug: postmark-email-best-practices
- name: postmark-inbound
  slug: postmark-inbound
- name: postmark-send-email
  slug: postmark-send-email
- name: postmark-templates
  slug: postmark-templates
- name: postmark-webhooks
  slug: postmark-webhooks
- name: postmark
  slug: postmark
slug: activecampaign
solutions:
- description: Entry-level plan with marketing automation, up to 5 automation actions, and 1 user.
  name: Starter
- description: Mid-tier plan with unlimited automation actions, landing pages, and standard segmentation.
  name: Plus
- description: Advanced plan with predictive content, advanced segmentation, and 3 users.
  name: Pro
- description: Full-featured plan with custom objects, dedicated account team, and premium segmentation.
  name: Enterprise
tags:
- Marketing Automation
- Email Marketing
- CRM
- Sales Automation
- Customer Experience
- SMS Marketing
- E-Commerce
- Segmentation
- Webhook
- A2A
- Email
use_cases:
- description: Automate email sequences to nurture leads through the sales funnel based on behavior.
  name: Lead Nurturing
- description: Trigger post-purchase emails, abandoned cart recovery, and personalized product recommendations.
  name: E-Commerce Automation
- description: Automate onboarding sequences for SaaS products to improve activation and retention.
  name: Customer Onboarding
- description: Segment contacts using tags, custom fields, and custom objects for targeted campaigns.
  name: Contact Segmentation
- description: Manage deals, tasks, and pipeline stages with CRM and automation integration.
  name: Sales Pipeline Management
- description: Send targeted SMS campaigns to subscriber lists with engagement tracking.
  name: SMS Broadcast Campaigns
- description: Build real-time integrations using webhooks for contact and campaign activity events.
  name: Webhook-Driven Integrations
website: https://www.activecampaign.com
---
