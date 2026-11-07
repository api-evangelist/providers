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
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 207
  human_in_the_loop: 0
  name: Cvent Registration Agentic Access
  operation_count: 489
  slug: cvent-registration-agentic-access
  summary_line: 489 operations · 207 acting
api_count: 2
apis:
- description: The Cvent Registration REST API is the registration surface of the unified Cvent Platform REST API. It allows integrations to create and manage events, registration types, fees, sessions, contacts, at
  name: Cvent Registration REST API
  slug: rest-api
- description: Cvent Webhooks deliver real-time push notifications when registration, attendee, session, and meeting request events occur in Cvent. Webhook subscribers receive event payloads at a configured URL, ena
  name: Cvent Registration Webhooks
  slug: webhooks
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event registrations and attendees
  name: Cvent Registration Attendees API
  phrasing_intents:
  - id: getEaEventsByEventIdAttendees
    intent: List the attendees of one event
    question: Who is registered for a specific event?
  - id: postEaEventsByEventIdAttendees
    intent: Register contacts as attendees of an event
    question: How do I register existing contacts into one specific event by its event ID?
  - id: getEaEventsByEventIdAttendeesByAttendeeId
    intent: Get one attendee of a specific event
    question: How do I look up an attendee within a particular event?
  - id: putEaEventsByEventIdAttendeesByAttendeeId
    intent: Cancel or modify an attendee within an event
    question: How do I cancel one attendee's registration within a specific event?
  - id: listDurations
    intent: List how long attendees engaged in sessions
    question: How long did attendees actually spend in sessions, appointments or videos?
  - id: createAttendee
    intent: Invite or register contacts for an event
    question: How do I add existing contacts to an event as attendees?
  - id: listAttendees
    intent: List attendees in the account
    question: Who are the attendees across my Cvent account?
  - id: listAttendeesPostFilter
    intent: Search attendees with a long filter
    question: What if my attendee filter is too long to fit in a query string?
  phrasing_ops: 16
  slug: cvent-registration-attendees-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Contact/address book
  name: Cvent Registration Contacts API
  phrasing_intents:
  - id: getEaContacts
    intent: List contacts through the /ea endpoint
    question: How do I page through contacts on the /ea/contacts endpoint?
  - id: postEaContacts
    intent: Create a single contact through the /ea endpoint
    question: How do I add one contact with name, email and company on the /ea endpoint?
  - id: getEaContactsByContactId
    intent: Get a contact from the /ea endpoint
    question: How do I read one contact by ID from /ea/contacts?
  - id: putEaContactsByContactId
    intent: Update a contact through the /ea endpoint
    question: How do I change a contact's email or job title on the /ea endpoint?
  - id: deleteEaContactsByContactId
    intent: Delete a contact through the /ea endpoint
    question: How do I delete a contact using the /ea/contacts endpoint?
  - id: createContactGroup
    intent: Create a contact group
    question: How do I set up a new contact group for a mailing or distribution list?
  - id: listContactGroups
    intent: List contact groups
    question: What contact groups exist in my Cvent address book?
  - id: getContactGroupById
    intent: Get a contact group
    question: What are the details of one specific contact group?
  phrasing_ops: 33
  slug: cvent-registration-contacts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event lifecycle and configuration
  name: Cvent Registration Events API
  phrasing_intents:
  - id: getEaEvents
    intent: List events through the /ea events endpoint
    question: How do I page through events on the /ea/events endpoint with a continuation token?
  - id: postEaEvents
    intent: Create an event through the /ea endpoint
    question: What does it take to create an event synchronously on the /ea/events endpoint?
  - id: getEaEventsByEventId
    intent: Get an event from the /ea endpoint
    question: How do I read a single event's record from /ea/events by its event ID?
  - id: putEaEventsByEventId
    intent: Replace an event through the /ea endpoint
    question: How do I overwrite a whole event record on the /ea/events endpoint?
  - id: deleteEaEventsByEventId
    intent: Delete an event through the /ea endpoint
    question: How do I remove an event entirely using the /ea/events endpoint?
  - id: postEaEventsByEventIdCopy
    intent: Copy an event through the /ea endpoint
    question: How do I duplicate an event using the /ea copy endpoint?
  - id: listAdmissionItems
    intent: List admission items
    question: How do I see the admission items (ticket types) set up across my Cvent events?
  - id: listAdmissionItemsPostFilters
    intent: Filter admission items with a body filter
    question: My admission item filter is too long for the URL; can I send it in the request body instead?
  phrasing_ops: 58
  slug: cvent-registration-events-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor management
  name: Cvent Registration Exhibitors API
  phrasing_intents:
  - id: getEaEventsByEventIdExhibitors
    intent: List an event's exhibitors
    question: Which exhibitors are signed up for my event?
  phrasing_ops: 1
  slug: cvent-registration-exhibitors-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Agenda sessions
  name: Cvent Registration Sessions API
  phrasing_intents:
  - id: getEaEventsByEventIdSessions
    intent: List the sessions of one event
    question: What sessions are on the agenda of one specific event?
  - id: getSessionLocation
    intent: List an event's session locations
    question: Which rooms or session locations are set up for my Cvent event?
  - id: addSessionLocation
    intent: Add a session location to an event
    question: How do I add a new room as a session location for an event?
  - id: createProgramItem
    intent: Create a program item within a session
    question: How do I add a talk or panel as a program item inside a session?
  - id: listProgramItems
    intent: List session program items
    question: What talks, workshops and panels are scheduled as program items inside my sessions?
  - id: filterProgramItemDocuments
    intent: Filter documents linked to program items
    question: Which documents are attached to session program items across my events?
  - id: listProgramItemsPostFilters
    intent: Search program items with a long filter
    question: My program item filter is too long for the URL; is there a POST version?
  - id: updateProgramItem
    intent: Update a session program item
    question: How do I rename or change the duration of an existing program item?
  phrasing_ops: 30
  slug: cvent-registration-sessions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webhook subscriptions
  name: Cvent Registration Webhooks API
  phrasing_intents:
  - id: getEaWebhooks
    intent: List webhook subscriptions
    question: What webhook subscriptions are set up on my account?
  - id: postEaWebhooks
    intent: Create a webhook subscription
    question: How do I subscribe a URL to receive webhook notifications?
  phrasing_ops: 2
  slug: cvent-registration-webhooks-api
- description: The legacy Cvent SOAP API, still served and still publishing its WSDL at api.cvent.com/soap/V200611.ASMX?WSDL (HTTP 200, 330,911 bytes, targetNamespace http://api.cvent.com/2006-11). Cvent maintains a
  name: Cvent SOAP API (legacy V200611)
  slug: soap-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Account-level orders and transactions for event registration commerce. Added to the Cvent contract in the 2026-08-20 release. Read-only.
  name: Cvent Registration Orders and Transactions API
  phrasing_intents:
  - id: getAccountOrders
    intent: List orders across the account
    question: Can I pull every registration order across all events in my account?
  - id: getAccountOrderById
    intent: Get an order
    question: How do I look up a single order by its ID?
  - id: getAccountOrderItemsByOrderId
    intent: List the line items in an order
    question: What items were purchased in a given order?
  - id: getAccountOrderItem
    intent: Get one order line item
    question: How do I fetch a single line item from an order?
  phrasing_ops: 4
  slug: cvent-registration-orders-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Post-event and in-event surveys attached to the registration record.
  name: Cvent Registration Surveys API
  phrasing_intents:
  - id: getAllEventSurveyResponses
    intent: List survey responses across all events
    question: Can I pull every event survey response in my account in one feed?
  - id: getEventSurveys
    intent: List surveys attached to an event
    question: What surveys are attached to one of my events?
  - id: getEventSurveyQuestions
    intent: List questions in an event survey
    question: What questions does a particular event survey ask?
  - id: getEventSurveyRespondents
    intent: List respondents to an event survey
    question: Who has responded to a survey at my event?
  - id: createEventSurveyRespondent
    intent: Add a respondent to an event survey
    question: How do I register an attendee as a respondent on an event survey before recording answers?
  - id: updateEventSurveyRespondent
    intent: Update an event survey respondent
    question: How do I change the score or details of an existing event survey respondent?
  - id: createEventSurveyResponses
    intent: Submit answers for an event survey respondent
    question: How do I record a respondent's answers to an event survey question?
  - id: getEventSurveyResponses
    intent: List responses to one event survey
    question: What answers did attendees give on a specific event survey?
  phrasing_ops: 23
  slug: cvent-registration-surveys-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Speaker records, speaker documents and speaker-to-session assignment.
  name: Cvent Registration Speakers API
  phrasing_intents:
  - id: getSessionProgramSpeakers
    intent: List program item speaker assignments
    question: Which speakers are assigned to which session program items?
  - id: listSessionProgramSpeakersPostFilters
    intent: Search program item speakers with a long filter
    question: Can I send a long filter in the body to find program item speaker pairings?
  - id: createSessionProgramSpeaker
    intent: Add a speaker to a program item
    question: How do I assign a speaker to a single talk inside a session?
  - id: getSessionProgramSpeaker
    intent: Get a program item speaker link
    question: Is a given speaker attached to a specific program item?
  - id: deleteSessionProgramSpeaker
    intent: Remove a speaker from a program item
    question: How do I take a speaker off one program item but leave them on the session?
  - id: listSpeakersCategories
    intent: List speaker categories
    question: What speaker categories, like keynote or panelist, are defined?
  - id: addSpeakerCategory
    intent: Create a speaker category
    question: How do I add a new speaker category such as Moderator?
  - id: listSpeakers
    intent: List speakers
    question: Who are the speakers across my Cvent events?
  phrasing_ops: 19
  slug: cvent-registration-speakers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Table assignment, seating, badge print jobs and badge printer pools for on-site check-in.
  name: Cvent Registration Seating and Badging API
  phrasing_intents:
  - id: listSeating
    intent: List an event's seating charts
    question: What seating arrangements are set up for my event?
  - id: getEventTableAssignments
    intent: List table assignments across all seatings
    question: Who is assigned to which table across every seating chart in my event?
  - id: getSeating
    intent: Get one seating chart
    question: What are the details of a specific seating chart?
  - id: getTableAssignment
    intent: List assignments within one seating
    question: Who is seated where in one particular seating chart?
  - id: listTables
    intent: List the tables in a seating
    question: Which tables are in a seating chart?
  - id: getTable
    intent: Get one table's details
    question: What are the details of a particular table in a seating?
  - id: listSeats
    intent: List the seats at a table
    question: Which seats are at a given table?
  - id: getSeat
    intent: Get one seat's details
    question: What do we know about a specific seat at a table?
  phrasing_ops: 8
  slug: cvent-registration-seating-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Discount codes and their association to order items.
  name: Cvent Registration Discounts API
  phrasing_intents:
  - id: listEventDiscounts
    intent: List an event's discounts
    question: Which discount codes are in use for my event, including account-level ones?
  - id: createEventDiscount
    intent: Create a discount in an event
    question: How do I add a new discount code to an event?
  - id: listDiscountedAgendaItems
    intent: List agenda items tied to discounts
    question: Which sessions or admission items currently have a discount applied in my event?
  - id: updateEventDiscount
    intent: Update an event discount
    question: How do I change an existing discount in my event?
  - id: linkAgendaItemToDiscount
    intent: Apply a discount to an agenda item
    question: How do I make a discount apply to a specific session or admission item?
  - id: unlinkAgendaItemFromDiscount
    intent: Remove a discount from an agenda item
    question: How do I stop a discount from applying to one agenda item?
  phrasing_ops: 6
  slug: cvent-registration-discounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Custom field definitions and answers on contacts, events and sessions.
  name: Cvent Registration Custom Fields API
  phrasing_intents:
  - id: listCustomFields
    intent: List custom fields in the account
    question: What custom fields exist for contacts or events in my account?
  - id: createCustomField
    intent: Create a custom field
    question: How do I add a new custom field to capture extra data?
  - id: updateCustomField
    intent: Update a custom field
    question: Can I rename or deactivate an existing custom field?
  - id: getCustomField
    intent: Get one custom field's definition
    question: What type and choices does a particular custom field have?
  - id: updateCustomFieldAdvancedLogic
    intent: Set advanced logic between custom fields
    question: Can the choices in one custom field depend on the answer to another?
  - id: createCustomFieldTranslation
    intent: Add a translation to a custom field
    question: How do I add a new language translation to a custom field?
  - id: updateCustomFieldTranslation
    intent: Update a custom field's translation
    question: Can I correct an existing translation of a custom field?
  phrasing_ops: 7
  slug: cvent-registration-custom-fields-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Registration travel — air, ground and arrival/departure data attached to an attendee.
  name: Cvent Registration Event Travel API
  phrasing_intents:
  - id: getAirActualDetail
    intent: List attendees' booked flights for an event
    question: Which flights did attendees actually book to get to my event?
  - id: getAirRequests
    intent: List attendees' flight requests for an event
    question: What flight requests have attendees submitted for my event?
  - id: getAlternateTravelAnswers
    intent: List alternate travel answers from opt-outs
    question: Which attendees opted out of air or hotel booking, and what did they answer instead?
  - id: getHotelRequests
    intent: List attendees' hotel requests for an event
    question: What hotel requests have attendees made for my event?
  - id: getHousingReservationRequests
    intent: List housing reservation requests for an event
    question: Which attendees submitted housing reservation requests for my event?
  phrasing_ops: 5
  slug: cvent-registration-event-travel-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Attendee activities, attendee insights (engagement scores) and attendee messages.
  name: Cvent Registration Attendee Activities API
  phrasing_intents:
  - id: listAttendeeActivities
    intent: List attendee activities
    question: What have attendees been doing at my events, like check-ins or session views?
  - id: createAttendeeActivity
    intent: Record an external attendee activity
    question: How do I log something an attendee did in another system against their event record?
  - id: listExternalAttendeeActivitiesMetadata
    intent: List external activity definitions
    question: Which external activity types have been defined for attendee tracking?
  - id: createExternalAttendeeActivityMetadata
    intent: Define a new external activity type
    question: How do I register a new type of external attendee activity before sending it?
  - id: deleteExternalAttendeeActivityMetadata
    intent: Delete an external activity definition
    question: How do I remove an external activity type I no longer track?
  - id: updateExternalAttendeeActivityMetadata
    intent: Update an external activity definition
    question: How do I change the name or fields of an external activity type I defined?
  phrasing_ops: 6
  slug: cvent-registration-attendee-activities-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Read the account's REST usage tier (Free / Standard / Premium) and current quota consumption before planning a batch.
  name: Cvent Registration Usage and Quota API
  phrasing_intents:
  - id: getUsage
    intent: Check recent API call usage
    question: How many API calls has my account made over the last seven days?
  - id: getUsageTier
    intent: Check the account's API usage tier
    question: Which API usage tier is my account on?
  phrasing_ops: 2
  slug: cvent-registration-usage-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'An appointment is a meeting scheduled between two or more parties. These APIs allow you to get information about your Cvent Appointments: appointment attendees, their interests, and availabilities. * '
  name: Cvent Registration Appointments API
  phrasing_intents:
  - id: listAppointmentAttendees
    intent: List appointment attendees
    question: Who are the attendees taking part in appointment scheduling?
  - id: getAppointmentAttendeeById
    intent: Get an appointment attendee
    question: How do I look up one appointment attendee's details?
  - id: listAvailability
    intent: List appointment availability times
    question: When are people available for appointments across my appointment events?
  - id: getAvailabilityById
    intent: Get an appointment availability time
    question: How do I fetch one specific availability time block?
  - id: listAppointmentEvents
    intent: List appointment events
    question: Which events have appointment scheduling set up?
  - id: getAppointmentEventById
    intent: Get an appointment event
    question: How do I get the settings of one appointment event?
  - id: listAvailableTimes
    intent: Find open appointment slots and locations
    question: What times and locations are still open to book appointments in an appointment event?
  - id: listAppointmentTypes
    intent: List appointment types in an appointment event
    question: What kinds of appointments can be booked in an appointment event?
  phrasing_ops: 16
  slug: cvent-registration-appointments-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'The Attendee Insights feature provides valuable information about your event attendees. It assists planners, marketers, and exhibitors in targeting customers effectively, thereby enhancing engagement '
  name: Cvent Registration Attendee Insights API
  phrasing_intents:
  - id: listAttendeeInsights
    intent: List engagement scores
    question: Which engagement scores have been set up for my events?
  - id: getAttendeeInsightsById
    intent: Get an engagement score's configuration
    question: How is a particular engagement score configured?
  - id: getScores
    intent: List attendees' engagement scores
    question: Which attendees were most engaged at my event?
  - id: getStats
    intent: Summarize an engagement score's statistics
    question: What does the overall score distribution look like for an engagement score?
  phrasing_ops: 4
  slug: cvent-registration-attendee-insights-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These APIs retrieve and manage attendee messages—communications exchanged between attendees within channels. Channels are virtual spaces created for one-on-one or group conversations, allowing attende
  name: Cvent Registration Attendee Messages API
  phrasing_intents:
  - id: getAttendeeMessagesMembers
    intent: List members of attendee chat channels
    question: Who is in an attendee-to-attendee chat channel at my event?
  phrasing_ops: 1
  slug: cvent-registration-attendee-messages-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Audience Segments allow planners to segment their attendees into groups and better manage the attendee experience based on their defined segments. Audience Segments APIs will enable you to get, create
  name: Cvent Registration Audience Segments API
  phrasing_intents:
  - id: listAttendeeAudienceSegments
    intent: List an attendee's audience segments
    question: Which audience segments is a particular attendee currently in?
  - id: disassociateAttendeeFromAudienceSegments
    intent: Remove an attendee from all audience segments
    question: How do I pull an attendee out of every audience segment at once?
  - id: listAssociatedAudienceSegments
    intent: Search an attendee's segments with a body filter
    question: Can I send a long filter in the body to check an attendee's segment memberships?
  - id: createAudienceSegment
    intent: Create an audience segment
    question: How do I create a new audience segment for an event?
  - id: listAudienceSegments
    intent: List audience segments
    question: What audience segments have been set up in my account?
  - id: listAudienceSegmentsPostFilter
    intent: Search audience segments with a long filter
    question: My audience segment filter is too long for the URL; can I POST it?
  - id: getAudienceSegmentById
    intent: Get an audience segment
    question: What are the details of one audience segment?
  - id: updateAudienceSegment
    intent: Update an audience segment
    question: How do I rename an existing audience segment?
  phrasing_ops: 12
  slug: cvent-registration-audience-segments-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Endpoints for obtaining, refreshing, and validating OAuth2 access tokens.
  name: Cvent Registration Authentication API
  phrasing_intents:
  - id: oauth2Authorize
    intent: Start the OAuth2 authorization code flow
    question: How do I send a user to Cvent to authorize my app and get an authorization code?
  - id: oauth2Token
    intent: Get an access token
    question: How do I exchange my client credentials for an API access token?
  - id: validateToken
    intent: Check that an access token is valid
    question: Is my current access token still valid?
  phrasing_ops: 3
  slug: cvent-registration-authentication-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Badge print jobs can be scheduled to a printer pool, so a printer in the printer pool can consume the job and print the badge.
  name: Cvent Registration Badge Print Job API
  phrasing_intents:
  - id: createBadgePrintJob
    intent: Send a badge to a printer pool
    question: How do I print an attendee's badge on-site?
  - id: getEventBadgePrintJobs
    intent: List badge print jobs for an event
    question: What badge print jobs have been sent for my event?
  - id: getBadgePrintJob
    intent: Check a badge print job
    question: Has a specific badge print job finished?
  phrasing_ops: 3
  slug: cvent-registration-badge-print-job-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Badge printer pools are set up from Cvent UI. You can use this API to retrieve badge printer pools.
  name: Cvent Registration Badge Printer Pools API
  phrasing_intents:
  - id: getBadgePrinterPools
    intent: List badge printer pools for an event
    question: Which badge printer pools are set up for my event?
  - id: getBadgePrinterPool
    intent: Get one badge printer pool
    question: What printers are in a specific badge printer pool?
  phrasing_ops: 2
  slug: cvent-registration-badge-printer-pools-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Budget is an event feature used to organize spending and track [allocations](https://support.cvent.com/s/communityarticle/Setting-Up-Budget-Allocations). Use this API to view budget items, cards and c
  name: Cvent Registration Budget API
  phrasing_intents:
  - id: getAccountBudgetItems
    intent: List budget items across all events
    question: What budget line items were recorded across every event in my account last quarter?
  - id: getAccountVendors
    intent: List account-level budget vendors
    question: Which vendors are configured in the account's budget admin settings?
  - id: getCards
    intent: List the account's payment cards
    question: What payment cards are on file for our Cvent account?
  - id: getCardTransactions
    intent: List card transactions
    question: What charges have been made on our event payment cards?
  - id: createCardTransaction
    intent: Record a new card transaction
    question: How do I log a corporate card charge against an event?
  - id: deleteCardTransaction
    intent: Delete a card transaction record
    question: How do I remove a card transaction that was logged by mistake?
  - id: updateCardTransaction
    intent: Correct an existing card transaction
    question: Can I fix the amount on a card transaction I already recorded?
  - id: getCurrencyConversionRate
    intent: List conversion rates for a currency
    question: What exchange rates are set for euros in my account?
  phrasing_ops: 24
  slug: cvent-registration-budget-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'The Bulk API provides a simple interface to upload large amounts of data into Cvent. The API processes the uploaded data asynchronously making API calls on behalf of the caller. Consumers of the bulk '
  name: Cvent Registration Bulk API
  phrasing_intents:
  - id: createBulkJob
    intent: Create a bulk job
    question: How do I run the same API operation over thousands of records?
  - id: getBulkJobById
    intent: Check a bulk job's status
    question: How far along is my bulk job, and how many records succeeded?
  - id: cancelBulkJob
    intent: Cancel a bulk job
    question: How do I stop a bulk job that's already running?
  - id: uploadBulkJobData
    intent: Upload records to a bulk job
    question: How do I add records to a bulk job before running it?
  - id: listBulkJobResult
    intent: List a bulk job's per-record results
    question: Which records in my bulk job failed?
  - id: runBulkJob
    intent: Start processing a bulk job
    question: How do I kick off a bulk job after uploading its data?
  phrasing_ops: 6
  slug: cvent-registration-bulk-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Planners use eMarketing campaigns to contact an audience, such as newsletters, press releases, or product updates. Campaign emails are used as newsletters, promotions, advertisements, or marketing mes
  name: Cvent Registration Campaigns API
  phrasing_intents:
  - id: getCampaigns
    intent: List eMarketing campaigns
    question: What eMarketing campaigns do we have running in Cvent?
  - id: getEmailTemplates
    intent: List a campaign's email templates
    question: Which email templates belong to a marketing campaign?
  - id: sendEMarketingEmails
    intent: Send a campaign email to recipients
    question: How do I send an eMarketing email to people on a campaign's recipient list?
  - id: getEmarketingEmailStatus
    intent: Check the status of a campaign email send
    question: Did my eMarketing email send go through?
  phrasing_ops: 4
  slug: cvent-registration-campaigns-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '**Card Tokenization**: Tokenization is the process Cvent uses to collect sensitive card details and personally identifiable information (PII), directly from your customers in a secure manner. This gua'
  name: Cvent Registration Card Tokens API
  phrasing_intents:
  - id: createCardTokens
    intent: Tokenize a credit card
    question: How do I turn a credit card into a token I can pass to other Cvent calls?
  phrasing_ops: 1
  slug: cvent-registration-card-tokens-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These API's provide compliance support for regulated industries. **Communication Compliance** lets you view communication activities across your account for archival or analysis. Various written forms
  name: Cvent Registration Compliance API
  phrasing_intents:
  - id: getConfiguration
    intent: Get the communication log configuration
    question: Which communication types is my account recording in the compliance log?
  - id: updateConfiguration
    intent: Choose which communications get logged
    question: How do I turn on logging of chats or emails for compliance?
  - id: getCommunicationLogMessages
    intent: List logged communication messages
    question: What emails, chats and session Q&A messages has my account logged between two dates?
  - id: filterCommunicationLogMessages
    intent: Search the communication log with a body filter
    question: Can I send a long filter in the request body to search the communication log?
  phrasing_ops: 4
  slug: cvent-registration-compliance-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event planners use emails to invite registrants, market their events and request feedback from attendees. Use these APIs to get historical data about your emails and see relevant details like the type
  name: Cvent Registration Emails API
  phrasing_intents:
  - id: getBounceDetails
    intent: List email bounces
    question: Which of my emails bounced in the last month?
  - id: getEmailsHistory
    intent: List sent email history
    question: What emails has my account sent recently?
  - id: getEmailStatus
    intent: Check delivery status of an email send
    question: Were the emails from my send-to-recipients request delivered?
  phrasing_ops: 3
  slug: cvent-registration-emails-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event Credits reward attendees for participating in your events. Planners can award credits for the entire event, specific sessions, or both. You can also award credits after attendees complete survey
  name: Cvent Registration Event Credits API
  phrasing_intents:
  - id: getAttendeeCredits
    intent: List attendees' event credits
    question: Which attendees have earned event credits across my events?
  phrasing_ops: 1
  slug: cvent-registration-event-credits-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: EventFeatures related APIs
  name: Cvent Registration Event Features API
  phrasing_intents:
  - id: getEventFeatures
    intent: List features available for an event
    question: Which features are enabled or available on my event?
  - id: updateEventFeatures
    intent: Enable or disable an event feature
    question: How do I turn a feature on or off for an event?
  - id: launchEventFeatures
    intent: Launch an event feature to its audience
    question: How do I make an event feature live for attendees?
  - id: listEventWeblinks
    intent: List an event's weblinks
    question: What are the registration and website links for my event?
  phrasing_ops: 4
  slug: cvent-registration-event-features-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event roles are event specific permission sets for your organization's users. Use these APIs to retrieve, create, update, and delete event role assignments to your organization's users.
  name: Cvent Registration Event Role API
  phrasing_intents:
  - id: listEventRoleAssignment
    intent: List event role assignments
    question: Which users hold which roles on an event?
  phrasing_ops: 1
  slug: cvent-registration-event-role-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: An Events+ Hub persists basic information needed to assign an owner and optionally customize the public presentation.
  name: Cvent Registration Events+ Hub API
  phrasing_intents:
  - id: listHubs
    intent: List Events+ hubs
    question: Which Events+ hubs does my account have, and what status are they in?
  - id: getHubMembers
    intent: List members of an Events+ hub
    question: Who are the members of a particular Events+ hub?
  phrasing_ops: 2
  slug: cvent-registration-events-hub-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Exhibitor -** An exhibitor is an organization that is sponsoring or exhibiting at your event. This API allows you to get information about your exhibitors. * **Registration Pack -** Registration P'
  name: Cvent Registration Exhibitor API
  phrasing_intents:
  - id: getExhibitorCategories
    intent: List an event's exhibitor categories
    question: What exhibitor categories are set up for my Cvent event?
  - id: createExhibitorCategory
    intent: Create an exhibitor category for an event
    question: How do I add a new exhibitor category to an event?
  - id: updateExhibitorCategory
    intent: Update an existing exhibitor category
    question: Can I rename an exhibitor category that already exists?
  - id: deleteExhibitorCategory
    intent: Delete an exhibitor category
    question: How do I remove an exhibitor category from an event entirely?
  - id: updateExhibitorCategoryBanner
    intent: Assign a banner image to an exhibitor category
    question: How do I put a banner image on an exhibitor category?
  - id: deleteExhibitorCategoryImage
    intent: Remove the banner from an exhibitor category
    question: Can I take the banner image off an exhibitor category?
  - id: listExhibitors
    intent: List the exhibitors in a category
    question: Which exhibitors are assigned to a particular exhibitor category?
  - id: addExhibitorToExhibitorCategory
    intent: Assign an exhibitor to a category
    question: How do I put an exhibitor into an exhibitor category?
  phrasing_ops: 30
  slug: cvent-registration-exhibitor-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor Content operations for an exhibitor. This API allows you to upload & get exhibitor content data such as files, weblinks.
  name: Cvent Registration Exhibitor Content API
  phrasing_intents:
  - id: listExhibitorFiles
    intent: List an exhibitor's files
    question: What files, like brochures, are attached to an exhibitor at my event?
  - id: getExhibitorFile
    intent: Get one exhibitor file
    question: Can I fetch the details of just one exhibitor file?
  - id: updateExhibitorFile
    intent: Attach an uploaded file to an exhibitor
    question: How do I attach a file I've uploaded to an exhibitor's profile?
  - id: disassociateExhibitorFile
    intent: Detach a file from an exhibitor
    question: Is there a way to unlink a file from an exhibitor's content?
  - id: listExhibitorWeblinks
    intent: List an exhibitor's weblinks
    question: What web links are shown on an exhibitor's profile?
  - id: createExhibitorWeblink
    intent: Add a weblink to an exhibitor
    question: How do I add a website link to an exhibitor's profile?
  - id: getExhibitorWeblink
    intent: Get one exhibitor weblink
    question: Can I retrieve just one exhibitor weblink by its ID?
  - id: updateExhibitorWeblink
    intent: Update an exhibitor weblink
    question: How do I change the URL of an existing exhibitor link?
  phrasing_ops: 9
  slug: cvent-registration-exhibitor-content-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Exhibitor Admin -** Exhibitor Admins are administrators that have access to the exhibitor portal. In the portal, they are able to complete pre-event tasks, manage their team, purchase LeadCapture '
  name: Cvent Registration Exhibitor Team API
  phrasing_intents:
  - id: listExhibitorAdmins
    intent: List an exhibitor's admins
    question: Who are the admins managing an exhibitor at my event?
  - id: postExhibitorAdmin
    intent: Add an admin to an exhibitor
    question: How do I give someone admin access for an exhibitor?
  - id: getExhibitorAdmin
    intent: Get an exhibitor admin
    question: What is the contact email of a specific exhibitor admin?
  - id: updateExhibitorAdmin
    intent: Update an exhibitor admin
    question: How do I change an exhibitor admin's email address?
  - id: listBoothStaff
    intent: List an exhibitor's booth staff
    question: Who is staffing an exhibitor's booth at my event?
  - id: associateBoothStaff
    intent: Assign an attendee as booth staff
    question: How do I make a registered attendee part of an exhibitor's booth staff?
  - id: getBoothStaff
    intent: Get a booth staff member
    question: Which attendee is behind a given booth staff record?
  - id: deleteBoothStaff
    intent: Remove a booth staff member
    question: How do I take someone off an exhibitor's booth staff?
  phrasing_ops: 8
  slug: cvent-registration-exhibitor-team-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Allows you to upload files and get file location using the file ID. File ID can be used with other APIs to associate the file to an entity. For example: * <a href="#operation/addSessionDoc">Add Docume'
  name: Cvent Registration File API
  phrasing_intents:
  - id: uploadFile
    intent: Upload a file to attach to records
    question: How do I upload an image or document so I can attach it to an exhibitor or payment?
  - id: getFile
    intent: Get where an uploaded file lives
    question: Where is an uploaded file stored?
  phrasing_ops: 2
  slug: cvent-registration-file-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These APIs allow you to create hooks. When triggered, a hook sends a request to your service to get updated data related to the related Cvent object. For more information on using hooks, see the [gett
  name: Cvent Registration Hooks API
  phrasing_intents:
  - id: ListContactHooks
    intent: List contact hooks
    question: What contact hooks are configured in my account?
  - id: createContactHook
    intent: Create a contact hook
    question: How do I have Cvent call my system to fetch contact information?
  - id: updateContactHook
    intent: Update a contact hook's callback
    question: Can I change the callback URI of an existing contact hook?
  - id: deleteContactHook
    intent: Delete a contact hook
    question: How do I stop Cvent from calling a contact hook?
  phrasing_ops: 4
  slug: cvent-registration-hooks-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'RegLink APIs allow you to exchange data with Cvent Passkey events and hotel reservation-booking engines. Generally, there are four primary categories of functionality that RegLink APIs support: * **Sy'
  name: Cvent Registration Housing API
  phrasing_intents:
  - id: createConnection
    intent: Connect an integration to a housing event
    question: How does an integration partner get authorized to a Passkey housing event?
  - id: getHousingEventsSummaries
    intent: List the housing events I can access
    question: Which housing events does my integration have access to?
  - id: getHousingEventInfo
    intent: Get a housing event's details
    question: What are the dates and attendee types for a housing event?
  - id: getHousingEventHotels
    intent: List hotels in a housing event's room block
    question: Which hotels are in the room block for a housing event?
  - id: getHousingEventHotel
    intent: Get one hotel's details in a housing event
    question: What's the address and description of a specific hotel in my event's block?
  - id: getHousingEventHotelAvailability
    intent: Check which nights a hotel has rooms
    question: Which nights still have rooms available at a hotel in my block?
  - id: getHousingEventRoomTypes
    intent: List a hotel's room types for an event
    question: What room types, like king or double queen, does a block hotel offer?
  - id: getRoomTypeDetails
    intent: Get a room type's description and images
    question: What does a specific room type include and what does it look like?
  phrasing_ops: 21
  slug: cvent-registration-housing-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: APIs for managing hotel-related operations.
  name: Cvent Registration Housing Hotels API
  phrasing_intents:
  - id: updateHotelRoomRates
    intent: Update a hotel room's rates
    question: How do I change the nightly rate for a room type at a housing hotel?
  phrasing_ops: 1
  slug: cvent-registration-housing-hotels-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Leads -** Leads include leads gathered by LeadCapture, Appointments, and Inbound Leads. Use this API to get information for the lead and how it was captured. * **Lead Qualification Question -** Cu'
  name: Cvent Registration Leads API
  phrasing_intents:
  - id: getEliteratureRequests
    intent: List e-literature requests
    question: Which attendees requested exhibitor e-literature at my events?
  - id: getLeadQualificationAnswers
    intent: Get a lead's qualification answers
    question: How did a captured lead answer the exhibitor's qualification questions?
  - id: getLeads
    intent: List exhibitor leads
    question: What leads have exhibitors captured at my events?
  - id: getLeadsPostFiltersData
    intent: Search leads with a body filter
    question: Can I search leads by sending a long filter in the request body?
  phrasing_ops: 4
  slug: cvent-registration-leads-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: When planning an event, meeting request forms are customizable online questionnaires to capture information about the event and facilitate the approval of events. When a meeting request form is submit
  name: Cvent Registration Meeting Request API
  phrasing_intents:
  - id: getMeetingRequestByEventId
    intent: Get the meeting request behind an event
    question: Which meeting request was an event created from?
  - id: listMRF
    intent: List meeting request forms
    question: What meeting request forms do we have set up?
  - id: getMRFById
    intent: Get a meeting request form
    question: How do I see the questions and settings of one meeting request form?
  - id: createMeetingRequest
    intent: Bulk-create meeting requests on a form
    question: How do I submit new meeting requests to an active form through the API?
  - id: updateMeetingRequest
    intent: Bulk-update meeting requests on a form
    question: How do I add information to several existing meeting requests at once?
  - id: listMeetingRequest
    intent: List meeting requests submitted on a form
    question: Which meeting requests have been submitted through a given form?
  - id: getMeetingRequestById
    intent: Get a single meeting request
    question: How do I pull up one submitted meeting request?
  - id: listMeetingRequestDocuments
    intent: List documents attached to a meeting request
    question: What documents were attached to a meeting request?
  phrasing_ops: 8
  slug: cvent-registration-meeting-request-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Process forms automate data collection and notifications related to planning and executing events. Process form submissions are responses to a specific process form, providing data the form requests. '
  name: Cvent Registration Process Form API
  phrasing_intents:
  - id: listProcessFormSubmission
    intent: List process form submissions
    question: What process form submissions have come in?
  phrasing_ops: 1
  slug: cvent-registration-process-form-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Beta - All APIs are in Beta. Proposal Drafts are editable copies of proposals. This API allows you to edit proposal data privately before publishing.
  name: Cvent Registration Proposal Draft API
  phrasing_intents:
  - id: createProposalDraft
    intent: Create a draft venue proposal for an RFP
    question: How does a venue start a draft proposal in response to an RFP?
  phrasing_ops: 1
  slug: cvent-registration-proposal-draft-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP additional details APIs for managing past event references and other miscellaneous RFP operations.
  name: Cvent Registration RFP Additional Details API
  phrasing_intents:
  - id: listRfpPastEvents
    intent: List an RFP's past event history
    question: What past events did the planner list when creating an RFP?
  phrasing_ops: 1
  slug: cvent-registration-rfp-additional-details-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP (Request for Proposal) management APIs for core RFP operations including CRUD operations for base RFPs.
  name: Cvent Registration RFP Management API
  phrasing_intents:
  - id: getRfpLeadSource
    intent: Get where an RFP came from
    question: Which software or website did an RFP originate from?
  - id: getRfpLeadSourceSection
    intent: Get the specific channel within an RFP lead source
    question: Which form, domain or integration within a lead source did an RFP come through?
  - id: getRFP
    intent: Get an RFP's details
    question: How do I pull up the basic details of an RFP?
  phrasing_ops: 3
  slug: cvent-registration-rfp-management-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP requirements APIs for managing RFP-specific requirements including guest rooms, meeting rooms, custom questions, custom fields, and attachments (CRUD operations).
  name: Cvent Registration RFP Requirements API
  phrasing_intents:
  - id: listRfpAgendaItems
    intent: List an RFP's agenda items
    question: What meeting and function agenda items did the planner request in an RFP?
  - id: listRfpAgendaItemSchedules
    intent: List schedules for an RFP's agenda items
    question: When are the requested agenda items in an RFP scheduled to happen?
  - id: listRfpAttachments
    intent: List an RFP's attachments
    question: What files did the planner attach to an RFP for suppliers?
  - id: listRfpCustomFields
    intent: List an RFP's custom field answers
    question: What answers were given to custom fields on an RFP?
  - id: getRfpGuestRooms
    intent: Get an RFP's guest room requirements
    question: How many hotel guest rooms does an RFP ask for?
  - id: listRfpInternalDocuments
    intent: List an RFP's internal documents
    question: Which internal-only documents are stored on an RFP?
  - id: listRfpQuestions
    intent: List an RFP's questions
    question: What standard and custom questions does an RFP ask suppliers?
  phrasing_ops: 7
  slug: cvent-registration-rfp-requirements-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Suppliers are the venues and service providers that receive and respond to RFPs. Use these APIs to manage supplier associations, view recipient history, and create award details.
  name: Cvent Registration RFP Suppliers API
  phrasing_intents:
  - id: listRfpRecipientsHistory
    intent: List who was copied on an RFP
    question: Who has been copied as a recipient on an RFP over time?
  - id: getRfpSuppliers
    intent: List suppliers on an RFP
    question: Which venues and hotels were sent a given RFP?
  phrasing_ops: 2
  slug: cvent-registration-rfp-suppliers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Retrieves Check-In & Check-Out Signatures Of Attendees
  name: Cvent Registration Signatures API
  phrasing_intents:
  - id: getSignatures
    intent: List check-in and check-out signatures
    question: Where can I get the signatures attendees gave at check-in or check-out?
  phrasing_ops: 1
  slug: cvent-registration-signatures-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Transactions represent the financial exchanges that occur within your account. Use these APIs to retrieve and manage transaction data, including charges, refunds, and adjustments associated with your '
  name: Cvent Registration Transactions API
  phrasing_intents:
  - id: getAccountTransactions
    intent: List registration transactions in the account
    question: What payment transactions happened in my account?
  - id: getTransaction
    intent: Get one transaction
    question: What are the details of a specific transaction?
  - id: getAccountTransactionItems
    intent: List the line items of a transaction
    question: What line items make up a transaction?
  - id: getAccountTransactionItem
    intent: Get one transaction line item
    question: What's in a single line item of a transaction?
  phrasing_ops: 4
  slug: cvent-registration-transactions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The travel account, or corporation that represents the demand-side of travel RFPs.
  name: Cvent Registration Travel Accounts API
  phrasing_intents:
  - id: ListTravelAccounts
    intent: List travel accounts
    question: What travel accounts are set up in my Cvent account?
  - id: ListSupplierAccounts
    intent: List supplier travel accounts
    question: Which supplier travel accounts exist across all my travel accounts?
  - id: getTravelAccount
    intent: Get a travel account
    question: What are the details of one travel account?
  - id: getSupplierAccount
    intent: Get the supplier account for a travel account
    question: Which supplier account sits under a specific travel account?
  phrasing_ops: 4
  slug: cvent-registration-travel-accounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Travel RFP APIs provide access to travel programs and proposals. A travel program represents a request for proposal (RFP) that defines the specific travel needs and requirements of a travel accoun
  name: Cvent Registration Travel RFPs API
  phrasing_intents:
  - id: ListTravelPrograms
    intent: List travel programs
    question: What corporate travel programs do we have in Cvent?
  - id: ListTravelProgramsQuestions
    intent: List questions across all travel programs
    question: What questions are asked across all of our travel programs?
  - id: getTravelProgram
    intent: Get a travel program's details
    question: What are the details of a specific travel program?
  - id: ListTravelProgramQuestions
    intent: List questions for one travel program
    question: Which questions does a particular travel program ask hotels?
  - id: getTravelProgramQuestion
    intent: Get one travel program question
    question: What exactly does a specific travel program question ask?
  - id: ListTravelProposals
    intent: List travel proposals
    question: What travel proposals have hotels submitted?
  - id: ListTravelProposalBids
    intent: List travel proposal bids
    question: What bids have come in on our travel proposals?
  - id: GetTravelProposalBid
    intent: Get one travel proposal bid
    question: What rates were offered in a specific travel proposal bid?
  phrasing_ops: 9
  slug: cvent-registration-travel-rfps-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Travel Supplier APIs provide access to Cvent data related to hotels, apartments, and other travel providers. This includes information related to properties, and sleeping rooms.
  name: Cvent Registration Travel Suppliers API
  phrasing_intents:
  - id: PropertyApiListBrands
    intent: List hotel supplier brands
    question: Which hotel brands are available in the travel supplier directory?
  - id: PropertyApiGetBrand
    intent: Get a supplier brand
    question: What details are stored for one hotel brand code?
  - id: PropertyApiListChains
    intent: List hotel supplier chains
    question: Which hotel chains are in the travel supplier directory?
  - id: PropertyApiGetChain
    intent: Get a supplier chain
    question: What information is held for one hotel chain?
  - id: PropertyApiListProperties
    intent: List supplier properties
    question: Which hotels and venues are listed as supplier properties?
  - id: PropertyApiGetProperty
    intent: Get a supplier property
    question: What are the details of one specific hotel property?
  - id: BtApiGetPropertyRooms
    intent: List supplier property rooms
    question: What room types do supplier properties offer?
  - id: PropertyApiGetPropertyRoom
    intent: Get a supplier property room
    question: What data is stored for one specific hotel room?
  phrasing_ops: 8
  slug: cvent-registration-travel-suppliers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The [SCIM](https://www.simplecloud.info/) standard allows for easier cross-domain identity management. This API allows you to manage your account users and SCIM groups (representing Cvent user roles).
  name: Cvent Registration User SCIM API
  phrasing_intents:
  - id: getUserGroups
    intent: List SCIM groups representing user roles
    question: Which Cvent user roles are exposed as SCIM groups?
  - id: getResourceTypes
    intent: List SCIM resource types
    question: What SCIM resource types does the provisioning endpoint support?
  - id: getResourceType
    intent: Get one SCIM resource type
    question: What does the User resource type definition contain?
  - id: getSchemas
    intent: List SCIM user and group schemas
    question: What SCIM schemas and extensions describe users and groups?
  - id: getSchema
    intent: Get one SCIM schema definition
    question: What attributes are in the enterprise user extension schema?
  - id: getServiceProviderConfig
    intent: Get the SCIM service provider configuration
    question: Does the SCIM service support filtering, patching or bulk operations?
  - id: createUser
    intent: Provision a new user
    question: How do I provision a new Cvent user through SCIM?
  - id: listUsers
    intent: List provisioned users
    question: Which users exist in my account via SCIM?
  phrasing_ops: 11
  slug: cvent-registration-user-scim-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Operations for managing account users and user groups, including creation, retrieval, update, and deletion. Use these endpoints to administer user access and roles within your account.
  name: Cvent Registration Users API
  phrasing_intents:
  - id: getAccountUserGroups
    intent: List account user groups
    question: What user groups exist in my Cvent account?
  - id: createAccountUserGroup
    intent: Create an account user group
    question: How do I create a new user group for my team?
  - id: getAccountUserGroup
    intent: Get an account user group
    question: Can I look up one user group by its ID?
  - id: updateAccountUserGroup
    intent: Rename or update a user group
    question: How do I rename an existing user group?
  - id: deleteAccountUserGroup
    intent: Delete an account user group
    question: We no longer need a user group; can I delete it?
  - id: addUserToAccountUserGroup
    intent: Add a user to a user group
    question: How do I put a user into a user group?
  - id: deleteUserFromAccountUserGroup
    intent: Remove a user from a user group
    question: Can I take someone out of a user group?
  phrasing_ops: 7
  slug: cvent-registration-users-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Manage meeting rooms for a venue, including creating and updating room details, configuring capacities and amenities, and associating images.
  name: Cvent Registration Venue Meeting Rooms API
  phrasing_intents:
  - id: createMeetingRoom
    intent: Add a meeting room to a venue
    question: How do I add a new meeting room to my venue's profile?
  - id: listMeetingRoomsOverviews
    intent: List a venue's meeting rooms
    question: What meeting rooms does a venue have?
  - id: updateMeetingRoom
    intent: Replace a meeting room's details
    question: Can I overwrite all of a meeting room's data in one go?
  - id: patchMeetingRoom
    intent: Partially update a meeting room
    question: Can I change just one field on a meeting room without resending everything?
  - id: associateMeetingRoomImage
    intent: Set a meeting room's image
    question: How do I attach an uploaded JPEG to a meeting room?
  - id: listMeetingRoomImages
    intent: Get a meeting room's image
    question: Does a meeting room have a photo attached?
  - id: disassociateMeetingRoomImage
    intent: Remove a meeting room's image
    question: How do I take the photo off a meeting room?
  - id: getMeetingRoomOverview
    intent: Get one meeting room's overview
    question: What are the dimensions, capacities and amenities of a specific meeting room?
  phrasing_ops: 8
  slug: cvent-registration-venue-meeting-rooms-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Manage venue profile details including type, contact information, address, and other venue properties.
  name: Cvent Registration Venue Profiles API
  phrasing_intents:
  - id: updateVenueDetails
    intent: Replace a venue's profile details
    question: How do I overwrite all of a venue's profile details at once?
  - id: patchVenueDetails
    intent: Partially update a venue's details
    question: Can I change just one field of a venue's details without resending everything?
  - id: getVenueDetailsOverview
    intent: Get an overview of a venue's details
    question: What does a venue's profile currently say?
  - id: updateVenueFacility
    intent: Replace a venue's facility information
    question: How do I overwrite all of a venue's facility info, like meeting rooms and capacity?
  - id: patchVenueFacility
    intent: Partially update a venue's facility information
    question: Can I update only the year renovated for a venue's facility?
  phrasing_ops: 5
  slug: cvent-registration-venue-profiles-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Videos can be added to Cvent events with renditions at various resolutions, audio files, reactions tracks, and text tracks. Attendee viewership is tracked to get insight into durations, devices used a
  name: Cvent Registration Video API
  phrasing_intents:
  - id: listVideos
    intent: List videos in the account or event
    question: What videos are in my Cvent account?
  - id: getVideoViews
    intent: List video views
    question: Who has watched our event videos?
  - id: listAudioTracks
    intent: List a video's audio tracks
    question: Which audio tracks or language dubs does a video have?
  - id: listVideoRenditions
    intent: List a video's renditions
    question: What resolutions or renditions exist for a video?
  - id: createTextTrack
    intent: Add a caption track to a video
    question: How do I add a VTT caption file to a video?
  - id: listVideoTextTracks
    intent: List a video's captions and subtitles
    question: Does a video already have captions or subtitles?
  - id: updateTextTrack
    intent: Update or replace a video's text track
    question: Can I replace the VTT file on an existing caption track?
  phrasing_ops: 7
  slug: cvent-registration-video-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webcasts are virtual or livestreaming components of your Cvent events. Use these APIs to integrate your virtual events from outside sources into your Cvent workflows, create and delete webcasts from w
  name: Cvent Registration Webcasts API
  phrasing_intents:
  - id: createWebcast
    intent: Create a webcast for an event
    question: How do I create a webcast for a session in my event?
  - id: listWebcasts
    intent: List webcasts
    question: What webcasts are set up for my Cvent events?
  - id: listAttendeeLinks
    intent: List attendee links across webcasts
    question: What personal webcast join links have been issued to attendees across all webcasts?
  - id: listPlayers
    intent: List webcast players
    question: Which video player details are associated with my webcasts?
  - id: getWebcastById
    intent: Get a webcast
    question: What are the settings of one specific webcast?
  - id: deleteWebcast
    intent: Delete a webcast
    question: How do I delete a webcast from an event?
  - id: updateWebcast
    intent: Update a webcast
    question: How do I change the title or status of an existing webcast?
  - id: createAttendeeLinks
    intent: Bulk-create attendee links for a webcast
    question: How do I generate join links for attendees of a webcast?
  phrasing_ops: 11
  slug: cvent-registration-webcasts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: OAuth 2.0 token issuance
  name: Cvent Registration O Auth API
  phrasing_intents:
  - id: postEaOauth2Token
    intent: Get an OAuth access token
    question: How do I exchange my client credentials for a Bearer access token?
  phrasing_ops: 1
  slug: cvent-registration-oauth-api
artifact_total: 84
asyncapis:
- description: ''
  name: Cvent Registration Webhooks
  slug: cvent-registration-webhooks
collections:
- collection_type: open
  name: Cvent Registration REST Attendees API
  slug: open-cvent-registration-attendees-api
- collection_type: open
  name: Cvent Registration REST Attendees Contacts API
  slug: open-cvent-registration-contacts-api
- collection_type: open
  name: Cvent Registration REST Attendees Events API
  slug: open-cvent-registration-events-api
- collection_type: open
  name: Cvent Registration REST Attendees Exhibitors API
  slug: open-cvent-registration-exhibitors-api
- collection_type: open
  name: Cvent Registration REST Attendees OAuth API
  slug: open-cvent-registration-oauth-api
- collection_type: open
  name: Cvent Registration REST Attendees Sessions API
  slug: open-cvent-registration-sessions-api
- collection_type: open
  name: Cvent Registration REST Attendees Webhooks API
  slug: open-cvent-registration-webhooks-api
- collection_type: open
  name: Cvent Registration REST API
  slug: open-cvent-registration
common:
- group: other
  href: https://artifacts.apis.io/cvent-registration/capabilities/cvent-registration-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cvent-registration-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cvent-registration/agentic-access/cvent-registration-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-registration-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/security/cvent-registration-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cvent-registration-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/security/cvent-registration-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvent-registration-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/authentication/cvent-registration-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cvent-registration-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/scopes/cvent-registration-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cvent-registration-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/event-management-software/online-registration-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/reference/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cvent.com/docs/rest-api/explanation/concepts
- group: auth
  title: ''
  type: OAuthTokenEndpoint
  url: https://api-platform.cvent.com/ea/oauth2/token
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/event-management-software/cvent-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/product-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cvent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvent/
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog/feed.xml
- group: other
  href: https://artifacts.apis.io/cvent-registration/overlays/_index.yml
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: other
  href: https://artifacts.apis.io/cvent-registration/overlays/cvent-registration-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-registration-public-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-registration/wsdl/cvent-registration-soap-v200611.wsdl
  title: ''
  type: WSDL
  url: wsdl/cvent-registration-soap-v200611.wsdl
- group: agent
  href: https://artifacts.apis.io/cvent-registration/llms/cvent-registration-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cvent-registration-llms.txt
- group: build
  href: https://artifacts.apis.io/cvent-registration/packages/cvent-registration-packages.yml
  title: ''
  type: Packages
  url: packages/cvent-registration-packages.yml
- group: build
  href: https://artifacts.apis.io/cvent-registration/packages/cvent-registration-packages.yml
  title: ''
  type: SDKs
  url: packages/cvent-registration-packages.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/conformance/cvent-registration-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cvent-registration-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/conformance/cvent-registration-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cvent-registration-conformance.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/errors/cvent-registration-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cvent-registration-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/lifecycle/cvent-registration-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-registration-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cvent-registration/lifecycle/cvent-registration-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cvent-registration-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/conventions/cvent-registration-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cvent-registration-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cvent-registration/changelog/cvent-registration-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cvent-registration-changelog.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/components/cvent-registration-components.yml
  title: ''
  type: Components
  url: components/cvent-registration-components.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/data-model/cvent-registration-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cvent-registration-data-model.yml
- group: design
  href: https://artifacts.apis.io/cvent-registration/asyncapi/cvent-registration-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cvent-registration-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/cvent-registration/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cvent-registration/mcp/cvent-registration-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cvent-registration-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/security/cvent-registration-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cvent-registration-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cvent-registration/security/cvent-registration-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cvent-registration-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/cvent-registration/plans/cvent-registration-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cvent-registration-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cvent-registration/rate-limits/cvent-registration-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cvent-registration-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cvent-registration/finops/cvent-registration-finops.yml
  title: ''
  type: FinOps
  url: finops/cvent-registration-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://developers.cvent.com/applications
- group: start
  title: ''
  type: Login
  url: https://developers.cvent.com/login
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.cvent.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cvent/rest-sdks
created: '2024-01-15'
description: Cvent Registration is the event registration product within the Cvent Event Cloud, providing online registration websites, attendee data capture, payment processing, registration travel, group registration, custom field collection, and badge / on-site check-in workflows. Registration data is exposed programmatically through the unified Cvent Platform REST API at api-platform.cvent.com (OAuth 2.0 client credentials), with a dedicated Registration Guide on the Cvent developer portal. Real-time registration changes are also delivered through Cvent Webhooks. Earlier integrations relied on the legacy Cvent SOAP API.
finops:
- has_sources: true
  method: derived
  name: Cvent Registration Finops
  primary_unit: ''
  service_category: ''
  slug: cvent-registration-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-registration.png
layout: provider
modified: '2026-09-07'
name: Cvent Registration
nav: Providers
network: true
overview: 'Cvent Registration publishes 62 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 59 more. Tagged areas include Attendee Management, Attendees, Conferences, Event Management, and Event.


  The Cvent Registration catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cvent Registration''s developer surface includes authentication, API reference, support, pricing, engineering blog, changelog, documentation, and 42 more developer resources.'
plans:
- name: Cvent Registration Plans Pricing
  plan_count: 2
  slug: cvent-registration-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 6
  name: Cvent Registration Rate Limits
  slug: cvent-registration-rate-limits
rules:
- authorship: generated
  effective_rule_count: 118
  extends:
  - spectral:oas
  name: Cvent Registration API Rules
  rule_count: 77
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 31
  slug: cvent-registration-rules
scopes:
- name: Cvent Registration Scopes
  scope_count: 238
  slug: cvent-registration-scopes
  summary_line: 238 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 76.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 65.4
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 59
    mcp: derived
    skills: derived
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
    score: 38.9
screenshot: https://apis.io/screenshots/cvent-registration/cvent-registration-2026-06-20T175407.png
security:
- kind: authentication
  name: Cvent Registration Authentication
  slug: cvent-registration-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cvent Registration Domain Security
  slug: cvent-registration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cvent Registration Vulnerability Disclosure
  slug: cvent-registration-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cvent Registration Trust Center
  slug: cvent-registration-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
skill_count: 3
skills:
- name: cvent-registration-onsite-check-in
  slug: cvent-registration-onsite-check-in
- name: cvent-registration-register-attendee
  slug: cvent-registration-register-attendee
- name: cvent-registration-webhook-subscription
  slug: cvent-registration-webhook-subscription
slug: cvent-registration
tags:
- Attendee Management
- Attendees
- Conferences
- Event Management
- Event
- OAuth
- On-Site Check-In
- Registration
- REST API
- SCIM
- SDK
- SOAP
- Ticketing
- Webhook
- Authentication
website: https://www.cvent.com/en/event-management-software/online-registration-software
---
