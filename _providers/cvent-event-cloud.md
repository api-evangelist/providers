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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 46.1
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 189
  human_in_the_loop: 0
  name: Cvent Event Cloud Agentic Access
  operation_count: 383
  slug: cvent-event-cloud-agentic-access
  summary_line: 383 operations · 189 acting
api_count: 2
apis:
- description: RESTful API for managing events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub data. Uses OAuth 2.0 client credentials. Authorization code flo
  name: Cvent Platform REST API (Event Cloud)
  slug: rest-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event registrations and attendees
  name: Cvent Event Cloud Attendees API
  phrasing_intents:
  - id: listDurations
    intent: List attendee engagement durations
    question: How long did attendees spend in each session, appointment or video?
  - id: createAttendee
    intent: Add contacts to an event as attendees
    question: How do I add existing contacts to an event as attendees?
  - id: listAttendees
    intent: List attendees in the account
    question: Who are the attendees across my Cvent account?
  - id: listAttendeesPostFilter
    intent: Search attendees with a long filter in the body
    question: My attendee filter is too long for the URL — how else can I query attendees?
  - id: getAttendeeById
    intent: Get one attendee
    question: What's the registration status of a specific attendee?
  - id: updateAttendee
    intent: Update an attendee's registration
    question: How do I change an attendee's status or registration type?
  - id: updateAttendeeSubscriptionStatus
    intent: Change an attendee's email subscription
    question: How do I unsubscribe an attendee from an event's emails?
  - id: updateInternalInfoAnswers
    intent: Update an attendee's internal information answers
    question: How do I record planner-only internal information for an attendee?
  phrasing_ops: 12
  slug: cvent-event-cloud-attendees-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Contact/address book
  name: Cvent Event Cloud Contacts API
  phrasing_intents:
  - id: createContactGroup
    intent: Create a contact group
    question: Can I create a new group to organize contacts, like a distribution list?
  - id: listContactGroups
    intent: List contact groups
    question: What contact groups exist in my address book?
  - id: getContactGroupById
    intent: Get a contact group
    question: Can I see the details of one contact group, like its type and note?
  - id: updateContactGroup
    intent: Update a contact group
    question: Can I rename an existing contact group?
  - id: deleteContactGroup
    intent: Delete a contact group
    question: Can I delete a contact group I no longer use?
  - id: getContactIdsByContactGroup
    intent: List contact IDs in a group
    question: Which contacts belong to a given contact group?
  - id: addContactToContactGroup
    intent: Add a contact to a group
    question: Can I put a single contact into a contact group?
  - id: removeContactFromContactGroup
    intent: Remove a contact from a group
    question: Can I take one contact out of a contact group without deleting them?
  phrasing_ops: 28
  slug: cvent-event-cloud-contacts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event lifecycle and configuration
  name: Cvent Event Cloud Events API
  phrasing_intents:
  - id: listAdmissionItems
    intent: List admission items across events
    question: Which admission items have been set up across my Cvent events?
  - id: listAdmissionItemsPostFilters
    intent: Filter admission items with a body filter
    question: Is there a way to send a long admission item filter in the request body instead of the URL?
  - id: getEventQuestions
    intent: List event registration questions
    question: What questions are asked on my event registration forms?
  - id: getChoicesForQuestion
    intent: Get the answer choices for an event question
    question: What answer options can attendees pick for a given event question?
  - id: getEvents
    intent: List events
    question: How do I get a list of all the events in my Cvent account?
  - id: createEventAsync
    intent: Create a new event asynchronously
    question: How do I create a brand new event through the API?
  - id: getEventAsyncStatus
    intent: Check whether an async event creation finished
    question: Has the event I submitted for creation finished being created yet?
  - id: getEventCopyStatus
    intent: Check the status of an event copy
    question: Is my event copy job done yet?
  phrasing_ops: 52
  slug: cvent-event-cloud-events-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Agenda sessions
  name: Cvent Event Cloud Sessions API
  phrasing_intents:
  - id: getSessionLocation
    intent: List an event's session locations
    question: Which rooms or locations are set up for sessions at my event?
  - id: addSessionLocation
    intent: Add a session location to an event
    question: Can I add a new room where sessions will take place at my event?
  - id: createProgramItem
    intent: Add a program item to a session
    question: Can I add a talk or panel as part of a session's schedule?
  - id: listProgramItems
    intent: List session program items
    question: How do I see the talks, workshops and panels scheduled inside my sessions?
  - id: filterProgramItemDocuments
    intent: Filter documents attached to program items
    question: Which documents are attached to my session program items?
  - id: listProgramItemsPostFilters
    intent: Search program items with a body filter
    question: Is there a way to query session program items with a filter too long for the URL?
  - id: updateProgramItem
    intent: Update a session program item
    question: Can I rename a talk or change its duration in a session's program?
  - id: deleteProgramItem
    intent: Delete a session program item
    question: Can I remove a talk from a session's program?
  phrasing_ops: 29
  slug: cvent-event-cloud-sessions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'An appointment is a meeting scheduled between two or more parties. These APIs allow you to get information about your Cvent Appointments: appointment attendees, their interests, and availabilities. * '
  name: Cvent Event Cloud Appointments API
  phrasing_intents:
  - id: listAppointmentAttendees
    intent: List appointment attendees
    question: Who is taking part in appointments at my events?
  - id: getAppointmentAttendeeById
    intent: Get one appointment attendee
    question: What are the details of a specific appointment attendee?
  - id: listAvailability
    intent: List appointment availability times
    question: When have hosts and attendees said they're available for appointments?
  - id: getAvailabilityById
    intent: Get one appointment availability time
    question: What does a specific availability time slot contain?
  - id: listAppointmentEvents
    intent: List appointment events
    question: Which of my events have appointment scheduling set up?
  - id: getAppointmentEventById
    intent: Get one appointment event
    question: What are the settings of a particular appointment event?
  - id: listAvailableTimes
    intent: Find open times to book an appointment
    question: What time slots and locations are still open for booking appointments?
  - id: listAppointmentTypes
    intent: List appointment types for an appointment event
    question: What kinds of appointments can be booked in an appointment event?
  phrasing_ops: 16
  slug: cvent-event-cloud-appointments-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Attendee Activities API gives valuable insight into your customer's experience at your Cvent event. Now, you can get a fuller picture of your customer's journey, including onsite activities, offsi
  name: Cvent Event Cloud Attendee Activities API
  phrasing_intents:
  - id: listAttendeeActivities
    intent: List attendee activities
    question: What have attendees been doing, like page visits and session joins?
  - id: createAttendeeActivity
    intent: Record an external activity for an attendee
    question: How do I log something an attendee did in another system as a Cvent activity?
  - id: listExternalAttendeeActivitiesMetadata
    intent: List external activity type definitions
    question: Which external activity types have been defined for attendee tracking?
  - id: createExternalAttendeeActivityMetadata
    intent: Define a new external activity type
    question: How do I define a new kind of external attendee activity before logging it?
  - id: deleteExternalAttendeeActivityMetadata
    intent: Delete an external activity type definition
    question: How do I remove an external activity type I no longer use?
  - id: updateExternalAttendeeActivityMetadata
    intent: Update an external activity type definition
    question: How do I change the name or fields of an existing external activity type?
  phrasing_ops: 6
  slug: cvent-event-cloud-attendee-activities-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'The Attendee Insights feature provides valuable information about your event attendees. It assists planners, marketers, and exhibitors in targeting customers effectively, thereby enhancing engagement '
  name: Cvent Event Cloud Attendee Insights API
  phrasing_intents:
  - id: listAttendeeInsights
    intent: List engagement scores and their events
    question: Which engagement scores have been set up for my events?
  - id: getAttendeeInsightsById
    intent: Get an engagement score definition
    question: How is a particular engagement score configured?
  - id: getScores
    intent: List attendees' engagement scores
    question: Which attendees were most engaged at my event?
  - id: getStats
    intent: Summarize an engagement score's results
    question: What is the overall distribution of engagement scores for an event?
  phrasing_ops: 4
  slug: cvent-event-cloud-attendee-insights-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These APIs retrieve and manage attendee messages—communications exchanged between attendees within channels. Channels are virtual spaces created for one-on-one or group conversations, allowing attende
  name: Cvent Event Cloud Attendee Messages API
  phrasing_intents:
  - id: getAttendeeMessagesMembers
    intent: List members of attendee chat channels
    question: Who is in a chat channel that attendees started at my event?
  phrasing_ops: 1
  slug: cvent-event-cloud-attendee-messages-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Audience Segments allow planners to segment their attendees into groups and better manage the attendee experience based on their defined segments. Audience Segments APIs will enable you to get, create
  name: Cvent Event Cloud Audience Segments API
  phrasing_intents:
  - id: listAttendeeAudienceSegments
    intent: List an attendee's audience segments
    question: Which audience segments is an attendee currently part of?
  - id: disassociateAttendeeFromAudienceSegments
    intent: Remove an attendee from all segments
    question: Can I pull an attendee out of every audience segment at once?
  - id: listAssociatedAudienceSegments
    intent: Search an attendee's segments with a body filter
    question: Can I query an attendee's segment memberships with a filter in the request body?
  - id: createAudienceSegment
    intent: Create an audience segment
    question: Can I create a new audience segment for an event, like VIPs or first-timers?
  - id: listAudienceSegments
    intent: List audience segments
    question: What audience segments exist in my account?
  - id: listAudienceSegmentsPostFilter
    intent: Search audience segments with a body filter
    question: Can I search audience segments with a filter sent in the request body?
  - id: getAudienceSegmentById
    intent: Get an audience segment
    question: Can I view the name and description of one audience segment?
  - id: updateAudienceSegment
    intent: Update an audience segment
    question: Can I rename an audience segment?
  phrasing_ops: 12
  slug: cvent-event-cloud-audience-segments-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Endpoints for obtaining, refreshing, and validating OAuth2 access tokens.
  name: Cvent Event Cloud Authentication API
  phrasing_intents:
  - id: oauth2Authorize
    intent: Start the OAuth2 authorization code flow
    question: How do I send a user to Cvent to authorize my app?
  - id: oauth2Token
    intent: Get an access token
    question: How do I exchange an authorization code for a Cvent access token?
  - id: validateToken
    intent: Check whether an access token is valid
    question: Is my current access token still valid?
  phrasing_ops: 3
  slug: cvent-event-cloud-authentication-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Badge print jobs can be scheduled to a printer pool, so a printer in the printer pool can consume the job and print the badge.
  name: Cvent Event Cloud Badge Print Job API
  phrasing_intents:
  - id: createBadgePrintJob
    intent: Send a badge to print
    question: Can I send an attendee's badge to a printer pool on site?
  - id: getEventBadgePrintJobs
    intent: List an event's badge print jobs
    question: Which badges have been sent to print at my event?
  - id: getBadgePrintJob
    intent: Get a badge print job
    question: Did a particular badge print job finish?
  phrasing_ops: 3
  slug: cvent-event-cloud-badge-print-job-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Badge printer pools are set up from Cvent UI. You can use this API to retrieve badge printer pools.
  name: Cvent Event Cloud Badge Printer Pools API
  phrasing_intents:
  - id: getBadgePrinterPools
    intent: List an event's badge printer pools
    question: Which badge printer pools are set up for onsite check-in at my event?
  - id: getBadgePrinterPool
    intent: Get one badge printer pool
    question: Which printers belong to a specific badge printer pool?
  phrasing_ops: 2
  slug: cvent-event-cloud-badge-printer-pools-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Budget is an event feature used to organize spending and track [allocations](https://support.cvent.com/s/communityarticle/Setting-Up-Budget-Allocations). Use this API to view budget items, cards and c
  name: Cvent Event Cloud Budget API
  phrasing_intents:
  - id: getAccountBudgetItems
    intent: List budget items across all events
    question: What budget items exist across every event in my Cvent account?
  - id: getAccountVendors
    intent: List account-level budget vendors
    question: Which budget vendors are configured at the account level?
  - id: getCards
    intent: List payment cards on the account
    question: What payment cards are linked to my Cvent account?
  - id: getCardTransactions
    intent: List card transactions
    question: What card transactions have been recorded on my account?
  - id: createCardTransaction
    intent: Record a card transaction
    question: How do I log a corporate card charge against an event?
  - id: deleteCardTransaction
    intent: Delete a card transaction
    question: How do I remove a card transaction entered by mistake?
  - id: updateCardTransaction
    intent: Update a card transaction record
    question: Can I correct a card transaction that's already been recorded?
  - id: getCurrencyConversionRate
    intent: List conversion rates for a currency
    question: What exchange rates are defined for a currency in my account?
  phrasing_ops: 24
  slug: cvent-event-cloud-budget-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'The Bulk API provides a simple interface to upload large amounts of data into Cvent. The API processes the uploaded data asynchronously making API calls on behalf of the caller. Consumers of the bulk '
  name: Cvent Event Cloud Bulk API
  phrasing_intents:
  - id: createBulkJob
    intent: Create a bulk job
    question: How do I run the same API operation over thousands of records?
  - id: getBulkJobById
    intent: Check a bulk job's status
    question: Has my bulk job finished, and how many records failed?
  - id: cancelBulkJob
    intent: Cancel a running bulk job
    question: How do I stop a bulk job that's processing?
  - id: uploadBulkJobData
    intent: Upload records to a bulk job
    question: Is there a limit on how many records I can upload to a bulk job per call?
  - id: listBulkJobResult
    intent: List a bulk job's per-record results
    question: Which records in my bulk job failed and why?
  - id: runBulkJob
    intent: Start processing a bulk job
    question: How do I kick off a bulk job after uploading its data?
  phrasing_ops: 6
  slug: cvent-event-cloud-bulk-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Planners use eMarketing campaigns to contact an audience, such as newsletters, press releases, or product updates. Campaign emails are used as newsletters, promotions, advertisements, or marketing mes
  name: Cvent Event Cloud Campaigns API
  phrasing_intents:
  - id: getCampaigns
    intent: List eMarketing campaigns
    question: What eMarketing campaigns are in my Cvent account?
  - id: getEmailTemplates
    intent: List a campaign's email templates
    question: Which email templates belong to an eMarketing campaign?
  - id: sendEMarketingEmails
    intent: Send a campaign email to recipients
    question: How do I send an eMarketing email to people on a campaign's recipient list?
  - id: getEmarketingEmailStatus
    intent: Check the status of an eMarketing send
    question: Did my eMarketing email send go out?
  phrasing_ops: 4
  slug: cvent-event-cloud-campaigns-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '**Card Tokenization**: Tokenization is the process Cvent uses to collect sensitive card details and personally identifiable information (PII), directly from your customers in a secure manner. This gua'
  name: Cvent Event Cloud Card Tokens API
  phrasing_intents:
  - id: createCardTokens
    intent: Tokenize a credit card
    question: Can I turn a credit card into a short-lived token to use in other calls instead of the raw card?
  phrasing_ops: 1
  slug: cvent-event-cloud-card-tokens-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These API's provide compliance support for regulated industries. **Communication Compliance** lets you view communication activities across your account. Various written forms of communication are cap
  name: Cvent Event Cloud Compliance API
  phrasing_intents:
  - id: getConfiguration
    intent: Get communication compliance settings
    question: Which communication types is my account recording in the compliance log?
  - id: updateConfiguration
    intent: Change which communications get logged
    question: Can I choose which types of messages are recorded in the communication log?
  - id: getCommunicationLogMessages
    intent: List communication log messages
    question: What emails and messages has my account sent, for compliance records?
  - id: filterCommunicationLogMessages
    intent: Search the communication log with a body filter
    question: Can I search the communication log with a long filter in the request body?
  phrasing_ops: 4
  slug: cvent-event-cloud-compliance-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Custom Fields are created by event planners to track important information about specific objects like events, contacts, or sessions. Use these APIs to view, create, and update custom fields in your a
  name: Cvent Event Cloud Custom Fields API
  phrasing_intents:
  - id: listCustomFields
    intent: List custom fields in the account
    question: What custom fields are defined for contacts, events or sessions in my account?
  - id: createCustomField
    intent: Create a custom field
    question: How do I add a new custom field to capture extra data?
  - id: updateCustomField
    intent: Update a custom field
    question: How do I rename or deactivate an existing custom field?
  - id: getCustomField
    intent: Get a custom field
    question: What type and choices does a particular custom field have?
  - id: updateCustomFieldAdvancedLogic
    intent: Set conditional display logic on a custom field
    question: How do I show a custom field only when another field has a certain answer?
  - id: createCustomFieldTranslation
    intent: Add a translation to a custom field
    question: How do I add a translation for a custom field in a new language?
  - id: updateCustomFieldTranslation
    intent: Update a custom field's translation
    question: How do I fix an existing translation of a custom field label?
  phrasing_ops: 7
  slug: cvent-event-cloud-custom-fields-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Discounts provide a way to reduce the cost of event registration items. Use these APIs to manage event discounts, including creating, updating, and linking discounts to agenda items.
  name: Cvent Event Cloud Discounts API
  phrasing_intents:
  - id: listEventDiscounts
    intent: List an event's discounts
    question: What discount codes are being used in my event?
  - id: createEventDiscount
    intent: Create a discount in an event
    question: Can I create a new discount code for an event?
  - id: listDiscountedAgendaItems
    intent: List agenda items tied to discounts
    question: Which sessions or admission items have a discount attached?
  - id: updateEventDiscount
    intent: Update an event discount
    question: Can I change an existing discount's settings?
  - id: linkAgendaItemToDiscount
    intent: Apply a discount to an agenda item
    question: Can I make a discount apply to a specific session or admission item?
  - id: unlinkAgendaItemFromDiscount
    intent: Stop a discount applying to an agenda item
    question: Can I remove a discount from one agenda item?
  phrasing_ops: 6
  slug: cvent-event-cloud-discounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event planners use emails to invite registrants, market their events and request feedback from attendees. Use these APIs to get historical data about your emails and see relevant details like the type
  name: Cvent Event Cloud Emails API
  phrasing_intents:
  - id: getBounceDetails
    intent: List email bounces
    question: Which emails from my account bounced?
  - id: getEmailsHistory
    intent: List sent email history
    question: What emails has my account sent recently?
  - id: getEmailStatus
    intent: Check the status of an email request
    question: What happened to the emails in a specific send request?
  phrasing_ops: 3
  slug: cvent-event-cloud-emails-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event Credits reward attendees for participating in your events. Planners can award credits for the entire event, specific sessions, or both. You can also award credits after attendees complete survey
  name: Cvent Event Cloud Event Credits API
  phrasing_intents:
  - id: getAttendeeCredits
    intent: List attendee event credits
    question: Which attendees earned event credits, and how many?
  phrasing_ops: 1
  slug: cvent-event-cloud-event-credits-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: EventFeatures related APIs
  name: Cvent Event Cloud Event Features API
  phrasing_intents:
  - id: getEventFeatures
    intent: List features available for an event
    question: Which features, like the attendee hub or appointments, are available on my event?
  - id: updateEventFeatures
    intent: Enable or disable an event feature
    question: How do I turn an event feature on or off?
  - id: launchEventFeatures
    intent: Launch an event feature to its audience
    question: How do I make an event feature live for attendees?
  - id: listEventWeblinks
    intent: List an event's weblinks
    question: What are the registration and website links for my event?
  phrasing_ops: 4
  slug: cvent-event-cloud-event-features-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event roles are event specific permission sets for your organization's users. Use these APIs to retrieve, create, update, and delete event role assignments to your organization's users.
  name: Cvent Event Cloud Event Role API
  phrasing_intents:
  - id: listEventRoleAssignment
    intent: List event role assignments
    question: Who holds which role, like planner or approver, on an event?
  phrasing_ops: 1
  slug: cvent-event-cloud-event-role-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event travel lets planners capture air & hotel requests from attendees and track air actuals, hotel reservations and alternate travel answers at your event. Use these endpoints to retrieve your air, h
  name: Cvent Event Cloud Event Travel API
  phrasing_intents:
  - id: getAirActualDetail
    intent: Get attendees' booked flight details for an event
    question: What flights have attendees actually booked for my event?
  - id: getAirRequests
    intent: Get attendees' flight requests for an event
    question: Which attendees have requested flights for my event?
  - id: getAlternateTravelAnswers
    intent: Get travel answers from attendees who opted out
    question: What did attendees say when they declined air or hotel booking for my event?
  - id: getHotelRequests
    intent: Get attendees' hotel requests for an event
    question: Which attendees requested a hotel room for my event?
  - id: getHousingReservationRequests
    intent: Get housing reservation requests for an event
    question: What housing reservation requests have attendees made through the housing system?
  phrasing_ops: 5
  slug: cvent-event-cloud-event-travel-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: An Events+ Hub persists basic information needed to assign an owner and optionally customize the public presentation.
  name: Cvent Event Cloud Events+ Hub API
  phrasing_intents:
  - id: listHubs
    intent: List Events+ hubs
    question: Which Events+ hubs does my account have and who owns them?
  - id: getHubMembers
    intent: List members of an Events+ hub
    question: Who are the members of a particular Events+ hub?
  phrasing_ops: 2
  slug: cvent-event-cloud-events-hub-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Exhibitor -** An exhibitor is an organization that is sponsoring or exhibiting at your event. This API allows you to get information about your exhibitors. * **Registration Pack -** Registration P'
  name: Cvent Event Cloud Exhibitor API
  phrasing_intents:
  - id: getExhibitorCategories
    intent: List an event's exhibitor categories
    question: What exhibitor categories are set up for my Cvent event?
  - id: createExhibitorCategory
    intent: Create an exhibitor category for an event
    question: How do I add a new exhibitor category to an event?
  - id: updateExhibitorCategory
    intent: Update an existing exhibitor category
    question: Can I rename an exhibitor category that already exists on my event?
  - id: deleteExhibitorCategory
    intent: Delete an exhibitor category
    question: How do I remove an exhibitor category from an event entirely?
  - id: updateExhibitorCategoryBanner
    intent: Assign a banner image to an exhibitor category
    question: How do I put a banner image on an exhibitor category?
  - id: deleteExhibitorCategoryImage
    intent: Remove the banner from an exhibitor category
    question: Can I take the banner image off an exhibitor category without deleting the category?
  - id: listExhibitors
    intent: List the exhibitors in a category
    question: Which exhibitors are assigned to a particular exhibitor category?
  - id: addExhibitorToExhibitorCategory
    intent: Assign an exhibitor to a category
    question: Can I put an exhibitor into an exhibitor category?
  phrasing_ops: 30
  slug: cvent-event-cloud-exhibitor-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor Content operations for an exhibitor. This API allows you to upload & get exhibitor content data such as files, weblinks.
  name: Cvent Event Cloud Exhibitor Content API
  phrasing_intents:
  - id: listExhibitorFiles
    intent: List an exhibitor's files
    question: What brochures and files has an exhibitor attached to their booth profile?
  - id: getExhibitorFile
    intent: Get one exhibitor file
    question: What are the display name and order of a specific exhibitor file?
  - id: updateExhibitorFile
    intent: Attach an uploaded file to an exhibitor
    question: How do I attach a file I already uploaded to an exhibitor's profile?
  - id: disassociateExhibitorFile
    intent: Detach a file from an exhibitor
    question: How do I remove a file from an exhibitor's booth content?
  - id: listExhibitorWeblinks
    intent: List an exhibitor's weblinks
    question: What web links has an exhibitor added to their profile?
  - id: createExhibitorWeblink
    intent: Add a weblink to an exhibitor
    question: How do I add a website link to an exhibitor's booth profile?
  - id: getExhibitorWeblink
    intent: Get one exhibitor weblink
    question: What URL and name does a specific exhibitor weblink have?
  - id: updateExhibitorWeblink
    intent: Update an exhibitor weblink
    question: How do I change the URL of an existing exhibitor link?
  phrasing_ops: 9
  slug: cvent-event-cloud-exhibitor-content-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Exhibitor Admin -** Exhibitor Admins are administrators that have access to the exhibitor portal. In the portal, they are able to complete pre-event tasks, manage their team, purchase LeadCapture '
  name: Cvent Event Cloud Exhibitor Team API
  phrasing_intents:
  - id: listExhibitorAdmins
    intent: List an exhibitor's admins
    question: Who are the admins managing an exhibitor at my event?
  - id: postExhibitorAdmin
    intent: Add an exhibitor admin
    question: Can I give someone admin access to manage an exhibitor's booth?
  - id: getExhibitorAdmin
    intent: Get an exhibitor admin
    question: What is the contact email of a specific exhibitor admin?
  - id: updateExhibitorAdmin
    intent: Update an exhibitor admin
    question: Can I change an exhibitor admin's email address?
  - id: listBoothStaff
    intent: List an exhibitor's booth staff
    question: Who is staffing an exhibitor's booth at my event?
  - id: associateBoothStaff
    intent: Add an attendee as booth staff
    question: Can I make a registered attendee a booth staff member for an exhibitor?
  - id: getBoothStaff
    intent: Get a booth staff member
    question: Which attendee is behind a given booth staff record?
  - id: deleteBoothStaff
    intent: Remove a booth staff member
    question: Can I take someone off an exhibitor's booth staff?
  phrasing_ops: 8
  slug: cvent-event-cloud-exhibitor-team-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Allows you to upload files and get file location using the file ID. File ID can be used with other APIs to associate the file to an entity. For example: * <a href="#operation/addSessionDoc">Add Docume'
  name: Cvent Event Cloud File API
  phrasing_intents:
  - id: uploadFile
    intent: Upload a file
    question: How do I upload an image so I can attach it as a banner or logo?
  - id: getFile
    intent: Get an uploaded file's location
    question: Where is an uploaded file stored?
  phrasing_ops: 2
  slug: cvent-event-cloud-file-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These APIs allow you to create hooks. When triggered, a hook sends a request to your service to get updated data related to the related Cvent object. For more information on using hooks, see the [gett
  name: Cvent Event Cloud Hooks API
  phrasing_intents:
  - id: ListContactHooks
    intent: List contact hooks
    question: What contact hooks are configured in my account?
  - id: createContactHook
    intent: Create a contact hook
    question: How do I have Cvent call my system to fetch contact information?
  - id: updateContactHook
    intent: Update a contact hook
    question: Can I change the callback URI on an existing contact hook?
  - id: deleteContactHook
    intent: Delete a contact hook
    question: How do I stop Cvent from calling a contact hook?
  phrasing_ops: 4
  slug: cvent-event-cloud-hooks-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Leads -** Leads include leads gathered by LeadCapture, Appointments, and Inbound Leads. Use this API to get information for the lead and how it was captured. * **Lead Qualification Question -** Cu'
  name: Cvent Event Cloud Leads API
  phrasing_intents:
  - id: getEliteratureRequests
    intent: List e-literature requests
    question: Which attendees asked exhibitors for digital brochures or e-literature?
  - id: getLeadQualificationAnswers
    intent: Get a lead's qualification answers
    question: How did a captured lead answer the exhibitor's qualification questions?
  - id: getLeads
    intent: List leads
    question: What leads have exhibitors captured at my events?
  - id: getLeadsPostFiltersData
    intent: Search leads with a body filter
    question: Can I search leads with a filter sent in the request body?
  phrasing_ops: 4
  slug: cvent-event-cloud-leads-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Process forms automate data collection and notifications related to planning and executing events. Process form submissions are responses to a specific process form, providing data the form requests. '
  name: Cvent Event Cloud Process Form API
  phrasing_intents:
  - id: listProcessFormSubmission
    intent: List process form submissions
    question: What process form submissions have come in?
  phrasing_ops: 1
  slug: cvent-event-cloud-process-form-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Seating lets you plan seating at your events by configuring tables and assigning seats to your attendees. The seating APIs allow you to create, update, and delete seating, tables, seats, and seating a
  name: Cvent Event Cloud Seating API
  phrasing_intents:
  - id: listSeating
    intent: List an event's seating charts
    question: What seating arrangements are set up for my event?
  - id: getEventTableAssignments
    intent: List table assignments across all seatings
    question: Where is every guest seated across all the seating charts of my event?
  - id: getSeating
    intent: Get one seating chart
    question: What are the details of a single seating chart?
  - id: getTableAssignment
    intent: List table assignments in one seating
    question: Who is assigned to tables in a particular seating chart?
  - id: listTables
    intent: List tables in a seating
    question: What tables are in a seating chart?
  - id: getTable
    intent: Get one table's details
    question: What are the details of a specific table?
  - id: listSeats
    intent: List seats at a table
    question: Which seats are at a particular table?
  - id: getSeat
    intent: Get one seat's details
    question: What are the details of a single seat?
  phrasing_ops: 8
  slug: cvent-event-cloud-seating-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Retrieves Check-In & Check-Out Signatures Of Attendees
  name: Cvent Event Cloud Signatures API
  phrasing_intents:
  - id: getSignatures
    intent: List check-in and check-out signatures
    question: Which attendees signed in or out at check-in?
  phrasing_ops: 1
  slug: cvent-event-cloud-signatures-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Speakers are individuals presenting at your event's session(s). Use Speaker APIs to read existing speaker data, create new speakers or update existing speakers in your events.
  name: Cvent Event Cloud Speakers API
  phrasing_intents:
  - id: getSessionProgramSpeakers
    intent: List program item and speaker links
    question: Which speakers are assigned to which program items across my sessions?
  - id: listSessionProgramSpeakersPostFilters
    intent: Search program item speakers with a body filter
    question: Can I search program item speaker links with a long filter sent in the body?
  - id: createSessionProgramSpeaker
    intent: Add a speaker to a program item
    question: Can I put a speaker on a specific talk inside a session?
  - id: getSessionProgramSpeaker
    intent: Get a program item's speaker link
    question: Is a particular speaker attached to a given program item?
  - id: deleteSessionProgramSpeaker
    intent: Remove a speaker from a program item
    question: Can I take a speaker off one talk without removing them from the whole session?
  - id: listSpeakersCategories
    intent: List speaker categories
    question: What speaker categories are set up, like Keynote or Panelist?
  - id: addSpeakerCategory
    intent: Create a speaker category
    question: Can I add a new category for grouping speakers?
  - id: listSpeakers
    intent: List speakers
    question: Who are all the speakers across my events?
  phrasing_ops: 19
  slug: cvent-event-cloud-speakers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Surveys are lists of questions deployed to your contacts. Surveys can be standalone or can be associated to a Cvent event. Use these APIs to search for surveys and retrieve the associated questions an
  name: Cvent Event Cloud Surveys API
  phrasing_intents:
  - id: getAllEventSurveyResponses
    intent: List survey responses across all events
    question: How do I pull every event survey response across all my events at once?
  - id: getEventSurveys
    intent: List the surveys attached to an event
    question: Which surveys are attached to my event?
  - id: getEventSurveyQuestions
    intent: List questions in an event survey
    question: What questions does a particular event survey ask?
  - id: getEventSurveyRespondents
    intent: List respondents to an event survey
    question: Who has responded to a specific survey at my event?
  - id: createEventSurveyRespondent
    intent: Add a respondent to an event survey
    question: How do I add an attendee as a respondent to an event survey?
  - id: updateEventSurveyRespondent
    intent: Update an event survey respondent
    question: How do I change details on an existing event survey respondent, like their score?
  - id: createEventSurveyResponses
    intent: Submit answers for an event survey respondent
    question: How do I submit survey answers on behalf of an event survey respondent?
  - id: getEventSurveyResponses
    intent: List responses to one event survey
    question: What did attendees answer on a specific survey for my event?
  phrasing_ops: 23
  slug: cvent-event-cloud-surveys-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Use these APIs view your REST API usage and limits metrics. For more details on limits - [Rate Limits](#section/Getting-Started/Rate-Limits)
  name: Cvent Event Cloud Usage API
  phrasing_intents:
  - id: getUsage
    intent: Check recent API call usage
    question: How many API calls has my account made in the last seven days?
  - id: getUsageTier
    intent: Check the account's API usage tier
    question: What API usage tier is my account on?
  phrasing_ops: 2
  slug: cvent-event-cloud-usage-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The [SCIM](https://www.simplecloud.info/) standard allows for easier cross-domain identity management. This API allows you to manage your account users and SCIM groups (representing Cvent user roles).
  name: Cvent Event Cloud User SCIM API
  phrasing_intents:
  - id: getUserGroups
    intent: List SCIM groups (user roles)
    question: Which Cvent user roles are exposed as SCIM groups?
  - id: getResourceTypes
    intent: List SCIM resource types
    question: What SCIM resource types does the service support?
  - id: getResourceType
    intent: Get one SCIM resource type
    question: What endpoint and schema does a given SCIM resource type use?
  - id: getSchemas
    intent: List SCIM user and group schemas
    question: What SCIM schemas and extensions describe users and role groups?
  - id: getSchema
    intent: Get one SCIM schema
    question: What attributes are defined in a specific SCIM schema?
  - id: getServiceProviderConfig
    intent: Get the SCIM service provider configuration
    question: Does the SCIM service support filtering, patch or bulk?
  - id: createUser
    intent: Provision a new user via SCIM
    question: How do I provision a new Cvent user from my identity provider?
  - id: listUsers
    intent: List provisioned users via SCIM
    question: Which users are provisioned in my Cvent account over SCIM?
  phrasing_ops: 11
  slug: cvent-event-cloud-user-scim-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Operations for managing account users and user groups, including creation, retrieval, update, and deletion. Use these endpoints to administer user access and roles within your account.
  name: Cvent Event Cloud Users API
  phrasing_intents:
  - id: getAccountUserGroups
    intent: List account user groups
    question: What user groups exist in my Cvent account?
  - id: createAccountUserGroup
    intent: Create an account user group
    question: How do I create a new user group in my account?
  - id: getAccountUserGroup
    intent: Get one account user group
    question: What are the details of a specific user group?
  - id: updateAccountUserGroup
    intent: Update an account user group
    question: Can I rename an existing user group?
  - id: deleteAccountUserGroup
    intent: Delete an account user group
    question: How do I delete a user group I no longer need?
  - id: addUserToAccountUserGroup
    intent: Add a user to a user group
    question: How do I put a user into an account user group?
  - id: deleteUserFromAccountUserGroup
    intent: Remove a user from a user group
    question: How do I take a user out of a group without deleting the group?
  phrasing_ops: 7
  slug: cvent-event-cloud-users-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Videos can be added to Cvent events with renditions at various resolutions, audio files, reactions tracks, and text tracks. Attendee viewership is tracked to get insight into durations, devices used a
  name: Cvent Event Cloud Video API
  phrasing_intents:
  - id: listVideos
    intent: List videos
    question: What videos are stored for my account or event?
  - id: getVideoViews
    intent: List video views
    question: How many times have my event videos been watched, and by whom?
  - id: listAudioTracks
    intent: List a video's audio tracks
    question: What audio tracks, such as other languages, does a video have?
  - id: listVideoRenditions
    intent: List a video's renditions
    question: Which resolutions or renditions are available for a video?
  - id: createTextTrack
    intent: Add a caption track to a video
    question: How do I add subtitles to a video?
  - id: listVideoTextTracks
    intent: List a video's captions and text tracks
    question: Which caption or subtitle tracks exist on a video?
  - id: updateTextTrack
    intent: Update a video's text track
    question: Can I replace the caption file on an existing text track?
  phrasing_ops: 7
  slug: cvent-event-cloud-video-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webcasts are virtual or livestreaming components of your Cvent events. Use these APIs to integrate your virtual events from outside sources into your Cvent workflows, create and delete webcasts from w
  name: Cvent Event Cloud Webcasts API
  phrasing_intents:
  - id: createWebcast
    intent: Create a webcast for an event
    question: How do I set up a live stream for a session at my event?
  - id: listWebcasts
    intent: List webcasts
    question: What webcasts are set up for my virtual event?
  - id: listAttendeeLinks
    intent: List attendee links across webcasts
    question: Which personal join links have been issued to attendees across all webcasts?
  - id: listPlayers
    intent: List webcast players
    question: What video player details are configured for my webcasts?
  - id: getWebcastById
    intent: Get a webcast
    question: Can I see the settings of a single webcast, like its format and status?
  - id: deleteWebcast
    intent: Delete a webcast
    question: Can I delete a webcast from my event?
  - id: updateWebcast
    intent: Update a webcast
    question: Can I change a webcast's title or status after it is created?
  - id: createAttendeeLinks
    intent: Bulk create attendee links for a webcast
    question: Can I generate join links for a batch of attendees on a webcast?
  phrasing_ops: 11
  slug: cvent-event-cloud-webcasts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'RegLink APIs allow you to exchange data with Cvent Passkey events and hotel reservation-booking engines. Generally, there are four primary categories of functionality that RegLink APIs support: * **Sy'
  name: Cvent Event Cloud Housing API
  phrasing_intents:
  - id: createConnection
    intent: Connect an integration to a housing event
    question: How do I authorize my integration against a Passkey housing event?
  - id: getHousingEventsSummaries
    intent: List summaries of my housing events
    question: Which housing events do I have access to?
  - id: getHousingEventInfo
    intent: Get a housing event's details
    question: What are the dates and settings of a specific housing event?
  - id: getHousingEventHotels
    intent: List hotels in a housing event
    question: Which hotels are part of my housing event's room block?
  - id: getHousingEventHotel
    intent: Get one hotel's details in a housing event
    question: What information is available about a single hotel in the block?
  - id: getHousingEventHotelAvailability
    intent: Check a hotel's available room nights
    question: Which nights still have rooms available at a hotel in my block?
  - id: getHousingEventRoomTypes
    intent: List a hotel's room types
    question: What room types does a hotel offer for my housing event?
  - id: getRoomTypeDetails
    intent: Get a room type's details
    question: What does a specific room type at a hotel include?
  phrasing_ops: 21
  slug: cvent-event-cloud-housing-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: APIs for managing hotel-related operations.
  name: Cvent Event Cloud Housing Hotels API
  phrasing_intents:
  - id: updateHotelRoomRates
    intent: Update a hotel room's rates
    question: How do I change the nightly rate for a room type at a housing hotel?
  phrasing_ops: 1
  slug: cvent-event-cloud-housing-hotels-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: When planning an event, meeting request forms are customizable online questionnaires to capture information about the event and facilitate the approval of events. When a meeting request form is submit
  name: Cvent Event Cloud Meeting Request API
  phrasing_intents:
  - id: getMeetingRequestByEventId
    intent: Get the meeting request behind an event
    question: Which meeting request was an event created from?
  - id: listMRF
    intent: List meeting request forms
    question: What meeting request forms are set up in my account?
  - id: getMRFById
    intent: Get a meeting request form
    question: What questions and settings does a specific meeting request form have?
  - id: createMeetingRequest
    intent: Bulk create meeting requests on a form
    question: How do I submit new meeting requests into an active form from another system?
  - id: updateMeetingRequest
    intent: Bulk update meeting requests on a form
    question: How do I add information to several existing meeting requests at once?
  - id: listMeetingRequest
    intent: List meeting requests submitted on a form
    question: Which meeting requests have been submitted through a given form?
  - id: getMeetingRequestById
    intent: Get a single meeting request
    question: What did the requester fill in on a specific meeting request?
  - id: listMeetingRequestDocuments
    intent: List documents attached to a meeting request
    question: What documents were uploaded with a meeting request?
  phrasing_ops: 8
  slug: cvent-event-cloud-meeting-request-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Beta - All APIs are in Beta. Proposal Drafts are editable copies of proposals. This API allows you to edit proposal data privately before publishing.
  name: Cvent Event Cloud Proposal Draft API
  phrasing_intents:
  - id: createProposalDraft
    intent: Create a proposal draft for an RFP
    question: Can a venue start a draft proposal in response to an RFP?
  phrasing_ops: 1
  slug: cvent-event-cloud-proposal-draft-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP additional details APIs for managing past event references and other miscellaneous RFP operations.
  name: Cvent Event Cloud RFP Additional Details API
  phrasing_intents:
  - id: listRfpPastEvents
    intent: List past events saved on an RFP
    question: What past event history did the planner include with an RFP?
  phrasing_ops: 1
  slug: cvent-event-cloud-rfp-additional-details-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP (Request for Proposal) management APIs for core RFP operations including CRUD operations for base RFPs.
  name: Cvent Event Cloud RFP Management API
  phrasing_intents:
  - id: getRfpLeadSource
    intent: Get an RFP lead source
    question: Where did an RFP originate, such as which software or website?
  - id: getRfpLeadSourceSection
    intent: Get an RFP lead source section
    question: Which specific form or domain within a lead source did an RFP come through?
  - id: getRFP
    intent: Get an RFP
    question: Can I pull the basic details of a venue sourcing RFP?
  phrasing_ops: 3
  slug: cvent-event-cloud-rfp-management-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP requirements APIs for managing RFP-specific requirements including guest rooms, meeting rooms, custom questions, custom fields, and attachments (CRUD operations).
  name: Cvent Event Cloud RFP Requirements API
  phrasing_intents:
  - id: listRfpAgendaItems
    intent: List agenda items on an RFP
    question: What meeting space agenda items are included in an RFP?
  - id: listRfpAgendaItemSchedules
    intent: List schedules for an RFP's agenda items
    question: On which days and times are an RFP's agenda items scheduled?
  - id: listRfpAttachments
    intent: List attachments on an RFP
    question: What files were attached to an RFP for suppliers to see?
  - id: listRfpCustomFields
    intent: List custom field answers on an RFP
    question: What were the custom field answers on an RFP?
  - id: getRfpGuestRooms
    intent: Get an RFP's guest room requirements
    question: How many sleeping rooms per night does an RFP ask for?
  - id: listRfpInternalDocuments
    intent: List internal documents on an RFP
    question: Which internal-only documents are stored on an RFP?
  - id: listRfpQuestions
    intent: List questions on an RFP
    question: What standard and custom questions does an RFP ask suppliers?
  phrasing_ops: 7
  slug: cvent-event-cloud-rfp-requirements-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Suppliers are the venues and service providers that receive and respond to RFPs. Use these APIs to manage supplier associations, view recipient history, and create award details.
  name: Cvent Event Cloud RFP Suppliers API
  phrasing_intents:
  - id: listRfpRecipientsHistory
    intent: List who was copied on an RFP
    question: Who has been copied as a recipient on an RFP over time?
  - id: getRfpSuppliers
    intent: List suppliers on an RFP
    question: Which venues or suppliers received a particular RFP?
  phrasing_ops: 2
  slug: cvent-event-cloud-rfp-suppliers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The travel account, or corporation that represents the demand-side of travel RFPs.
  name: Cvent Event Cloud Travel Accounts API
  phrasing_intents:
  - id: ListTravelAccounts
    intent: List travel accounts
    question: Which travel accounts are set up in my Cvent account?
  - id: ListSupplierAccounts
    intent: List supplier travel accounts
    question: What supplier travel accounts exist across my account?
  - id: getTravelAccount
    intent: Get a travel account
    question: What are the details of a specific travel account?
  - id: getSupplierAccount
    intent: Get the supplier account for a travel account
    question: Which supplier account belongs to a given travel account?
  phrasing_ops: 4
  slug: cvent-event-cloud-travel-accounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Travel RFP APIs provide access to travel programs and proposals. A travel program represents a request for proposal (RFP) that defines the specific travel needs and requirements of a travel accoun
  name: Cvent Event Cloud Travel RFPs API
  phrasing_intents:
  - id: ListTravelPrograms
    intent: List travel programs
    question: What corporate travel programs do I have in Cvent?
  - id: ListTravelProgramsQuestions
    intent: List questions across all travel programs
    question: What RFP questions are used across all my travel programs?
  - id: getTravelProgram
    intent: Get one travel program
    question: What are the details of a specific travel program?
  - id: ListTravelProgramQuestions
    intent: List one travel program's questions
    question: Which questions are asked in a particular travel program's RFP?
  - id: getTravelProgramQuestion
    intent: Get one travel program question
    question: What does a specific question in a travel program ask?
  - id: ListTravelProposals
    intent: List travel proposals
    question: Which hotel proposals have come back for my travel RFPs?
  - id: ListTravelProposalBids
    intent: List travel proposal bids
    question: What bids have suppliers submitted on travel proposals?
  - id: GetTravelProposalBid
    intent: Get one travel proposal bid
    question: What does a specific supplier bid on a travel proposal contain?
  phrasing_ops: 9
  slug: cvent-event-cloud-travel-rfps-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Travel Supplier APIs provide access to Cvent data related to hotels, apartments, and other travel providers. This includes information related to properties, and sleeping rooms.
  name: Cvent Event Cloud Travel Suppliers API
  phrasing_intents:
  - id: PropertyApiListBrands
    intent: List hotel supplier brands
    question: What hotel brands are in the travel supplier directory?
  - id: PropertyApiGetBrand
    intent: Get a supplier brand
    question: Can I look up a hotel brand by its brand code?
  - id: PropertyApiListChains
    intent: List hotel supplier chains
    question: Which hotel chains are available as travel suppliers?
  - id: PropertyApiGetChain
    intent: Get a supplier chain
    question: Can I get the details of one hotel chain by ID?
  - id: PropertyApiListProperties
    intent: List supplier hotel properties
    question: Which hotel properties can I find in the supplier directory?
  - id: PropertyApiGetProperty
    intent: Get a supplier property
    question: Can I pull the details of one hotel property by its ID?
  - id: BtApiGetPropertyRooms
    intent: List supplier property rooms
    question: What room types do supplier properties offer?
  - id: PropertyApiGetPropertyRoom
    intent: Get a supplier property room
    question: Can I read the data for one hotel room by its room ID?
  phrasing_ops: 8
  slug: cvent-event-cloud-travel-suppliers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Manage meeting rooms for a venue, including creating and updating room details, configuring capacities and amenities, and associating images.
  name: Cvent Event Cloud Venue Meeting Rooms API
  phrasing_intents:
  - id: createMeetingRoom
    intent: Create a meeting room at a venue
    question: How do I add a new meeting room to my venue profile?
  - id: listMeetingRoomsOverviews
    intent: List a venue's meeting room overviews
    question: What meeting rooms does my venue have?
  - id: updateMeetingRoom
    intent: Replace a meeting room's full details
    question: Does a full update of a meeting room overwrite fields I leave out?
  - id: patchMeetingRoom
    intent: Partially update a meeting room
    question: Can I change just one field on a meeting room and leave the rest alone?
  - id: getMeetingRoomOverview
    intent: Get one meeting room's overview
    question: What's the size and capacity of a specific meeting room?
  phrasing_ops: 5
  slug: cvent-event-cloud-venue-meeting-rooms-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Manage venue profile details including type, contact information, address, and other venue properties.
  name: Cvent Event Cloud Venue Profiles API
  phrasing_intents:
  - id: updateVenueDetails
    intent: Replace a venue's details
    question: Can I overwrite all the details on a venue profile, like name, address and phone numbers?
  - id: patchVenueDetails
    intent: Change a few of a venue's details
    question: Can I change just the website or cancellation policy on a venue without resending everything?
  - id: getVenueDetailsOverview
    intent: Get a venue's details overview
    question: Can I get a quick overview of a venue's profile details?
  - id: updateVenueFacility
    intent: Replace a venue's facility information
    question: Can I overwrite a venue's facility info, like meeting rooms, sleeping rooms and capacity?
  - id: patchVenueFacility
    intent: Change part of a venue's facility information
    question: Can I update only the year renovated on a venue facility and keep everything else?
  phrasing_ops: 5
  slug: cvent-event-cloud-venue-profiles-api
arazzos:
- description: Created from /Users/mkothari/git-cvent-public/rest-sdks/.speakeasy/temp/overlay_RizoNFXzgC.yaml
  name: Test Suite
  slug: cvent-event-cloud-sdk-tests.arazzo
artifact_total: 108
asyncapis:
- description: ''
  name: Cvent Event Cloud Webhooks
  slug: cvent-event-cloud-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cvent REST APIs — Event Cloud Appointments API
  slug: open-cvent-event-cloud-appointments-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendee Activities API
  slug: open-cvent-event-cloud-attendee-activities-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendee Insights API
  slug: open-cvent-event-cloud-attendee-insights-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendee Messages API
  slug: open-cvent-event-cloud-attendee-messages-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendees API
  slug: open-cvent-event-cloud-attendees-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Audience Segments API
  slug: open-cvent-event-cloud-audience-segments-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Authentication API
  slug: open-cvent-event-cloud-authentication-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Badge Print Job API
  slug: open-cvent-event-cloud-badge-print-job-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Badge Printer Pools API
  slug: open-cvent-event-cloud-badge-printer-pools-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Budget API
  slug: open-cvent-event-cloud-budget-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Bulk API
  slug: open-cvent-event-cloud-bulk-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Campaigns API
  slug: open-cvent-event-cloud-campaigns-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Card Tokens API
  slug: open-cvent-event-cloud-card-tokens-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Compliance API
  slug: open-cvent-event-cloud-compliance-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Contacts API
  slug: open-cvent-event-cloud-contacts-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Custom Fields API
  slug: open-cvent-event-cloud-custom-fields-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Discounts API
  slug: open-cvent-event-cloud-discounts-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Emails API
  slug: open-cvent-event-cloud-emails-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Credits API
  slug: open-cvent-event-cloud-event-credits-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Features API
  slug: open-cvent-event-cloud-event-features-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Role API
  slug: open-cvent-event-cloud-event-role-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Travel API
  slug: open-cvent-event-cloud-event-travel-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Events API
  slug: open-cvent-event-cloud-events-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Events+ Hub API
  slug: open-cvent-event-cloud-events-hub-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Exhibitor API
  slug: open-cvent-event-cloud-exhibitor-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Exhibitor Content API
  slug: open-cvent-event-cloud-exhibitor-content-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Exhibitor Team API
  slug: open-cvent-event-cloud-exhibitor-team-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud File API
  slug: open-cvent-event-cloud-file-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Hooks API
  slug: open-cvent-event-cloud-hooks-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Leads API
  slug: open-cvent-event-cloud-leads-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Process Form API
  slug: open-cvent-event-cloud-process-form-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Seating API
  slug: open-cvent-event-cloud-seating-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Sessions API
  slug: open-cvent-event-cloud-sessions-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Signatures API
  slug: open-cvent-event-cloud-signatures-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Speakers API
  slug: open-cvent-event-cloud-speakers-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Surveys API
  slug: open-cvent-event-cloud-surveys-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Usage API
  slug: open-cvent-event-cloud-usage-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud User SCIM API
  slug: open-cvent-event-cloud-user-scim-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Users API
  slug: open-cvent-event-cloud-users-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Video API
  slug: open-cvent-event-cloud-video-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Webcasts API
  slug: open-cvent-event-cloud-webcasts-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/capabilities/cvent-event-cloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cvent-event-cloud-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/agentic-access/cvent-event-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-event-cloud-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/security/cvent-event-cloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cvent-event-cloud-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/security/cvent-event-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvent-event-cloud-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/authentication/cvent-event-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cvent-event-cloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/scopes/cvent-event-cloud-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cvent-event-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/event-management-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/overview
- group: other
  title: ''
  type: AttendeeHub
  url: https://www.cvent.com/en/attendee-hub
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/event-management-software/cvent-pricing
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/cvent-general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cvent.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/llms/cvent-event-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cvent-event-cloud-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: docs
  title: ''
  type: Guides
  url: https://developers.cvent.com/docs/rest-api/guides/rest-guides
- group: start
  title: ''
  type: SignUp
  url: https://developers.cvent.com/applications
- group: auth
  title: ''
  type: TrustCenterURL
  url: https://trust.cvent.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cvent/rest-sdks
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/packages/cvent-event-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/cvent-event-cloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/packages/cvent-event-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/cvent-event-cloud-packages.yml
- group: docs
  title: ''
  type: SDKDocumentation
  url: https://developers.cvent.com/docs/rest-api/sdks
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/well-known/cvent-event-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cvent-event-cloud-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/mcp/cvent-event-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cvent-event-cloud-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/mcp/cvent-event-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cvent-event-cloud-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/overlays/cvent-event-cloud-overlays.yml
  title: ''
  type: Overlay
  url: overlays/cvent-event-cloud-overlays.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/arazzo/cvent-event-cloud-sdk-tests.arazzo.yaml
  title: ''
  type: Arazzo
  url: arazzo/cvent-event-cloud-sdk-tests.arazzo.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/conformance/cvent-event-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cvent-event-cloud-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/security/cvent-event-cloud-trust-center.yml
  title: ''
  type: Compliance
  url: security/cvent-event-cloud-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/errors/cvent-event-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cvent-event-cloud-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/lifecycle/cvent-event-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-event-cloud-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/lifecycle/cvent-event-cloud-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cvent-event-cloud-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/conventions/cvent-event-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cvent-event-cloud-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/changelog/cvent-event-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cvent-event-cloud-changelog.yml
- group: operate
  title: ''
  type: ChangeLogURL
  url: https://developers.cvent.com/docs/rest-api/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/components/cvent-event-cloud-components.yml
  title: ''
  type: Components
  url: components/cvent-event-cloud-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/data-model/cvent-event-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cvent-event-cloud-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/asyncapi/cvent-event-cloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cvent-event-cloud-webhooks.yml
- group: docs
  title: ''
  type: WebhooksDocumentation
  url: https://developers.cvent.com/docs/webhooks/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/plans/cvent-event-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cvent-event-cloud-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/rate-limits/cvent-event-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cvent-event-cloud-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/finops/cvent-event-cloud-finops.yml
  title: ''
  type: FinOps
  url: finops/cvent-event-cloud-finops.yml
created: '2024-01-01'
description: 'Cvent Event Cloud is the event management product line of the Cvent Platform. It supports the full event lifecycle: event creation, registration, marketing, agenda and session management, mobile event apps, onsite check-in, virtual and hybrid event delivery via the Attendee Hub, surveys, and analytics. Cvent publishes its own OpenAPI specification in public git at github.com/cvent/rest-sdks (cvent-public-spec/openapi.yaml) — 346 paths, 458 operations, 1,302 schemas — and generates its first-party TypeScript, .NET and Java SDKs from it with Speakeasy, applying five published OpenAPI Overlay 1.0.0 documents in the process. Access is OAuth 2.0, client credentials for server-to-server and authorization code for planner administrators, with the token endpoint at api-platform.cvent.com/ea/oauth2/token and 235 declared scopes. Regional bases split North America (api-platform.cvent.com/ea) from Europe (api-platform-eur.cvent.com/ea) with no cross-region read. Cvent also runs a live
  remote MCP server at mcp.cvent.com/mcp secured with OAuth 2.1 and PKCE, publishes a dated biweekly changelog, a 40-message webhook catalogue, SCIM 2.0 user provisioning, and a Custom Widgets browser SDK for embedding components in Cvent-hosted event pages.'
finops:
- name: Cvent Event Cloud Finops
  service_category: API
  slug: cvent-event-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-event-cloud.png
layout: provider
mcp_servers:
- description: 'Cvent runs a hosted, remote MCP server at https://mcp.cvent.com/mcp. It is protected by OAuth 2.1 with PKCE and advertises its own authorization requirements per RFC 9728: an unauthenticated tools/lis'
  name: Cvent MCP Server
  slug: cvent-mcp-server
modified: '2026-08-13'
name: Cvent Event Cloud
nav: Providers
network: true
overview: 'Cvent Event Cloud publishes 55 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 52 more. Tagged areas include Attendee Hub, Attendees, Bulk, Contacts, and Event Cloud.


  The Cvent Event Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cvent Event Cloud''s developer surface includes authentication, API reference, pricing, support, engineering blog, documentation, getting-started guide, and 42 more developer resources.'
plans:
- name: Cvent Event Cloud Plans Pricing
  plan_count: 3
  slug: cvent-event-cloud-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 6
  name: Cvent Event Cloud Rate Limits
  slug: cvent-event-cloud-rate-limits
scopes:
- name: Cvent Event Cloud Scopes
  scope_count: 235
  slug: cvent-event-cloud-scopes
  summary_line: 235 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 72.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 65.5
    developer_ergonomics: 67.3
    discoverability: 75.0
    operational_transparency: 81.6
  previous_composite: 71.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/screenshots/cvent-event-cloud-2026-06-20T175402.png
security:
- kind: authentication
  name: Cvent Event Cloud Authentication
  slug: cvent-event-cloud-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cvent Event Cloud Domain Security
  slug: cvent-event-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Event Cloud Trust Center
  slug: cvent-event-cloud-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-event-cloud
tags:
- Attendee Hub
- Attendees
- Bulk
- Contacts
- Event Cloud
- Event Management
- Event Marketing
- Event
- Exhibitors
- Hybrid Events
- MCP
- Authentication
- OnSite
- OpenAPI
- Overlays
- Registration
- REST
- SCIM
- SDK
- Sessions
- Speakers
- Surveys
- Virtual Events
- Webcasts
- Webhook
website: https://www.cvent.com/en/event-management-software
---
