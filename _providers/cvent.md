---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
- acting_count: 196
  human_in_the_loop: 0
  name: Cvent Agentic Access
  operation_count: 469
  slug: cvent-agentic-access
  summary_line: 469 operations · 196 acting
api_count: 2
apis:
- description: The unified Cvent Platform REST API providing programmatic access to events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub resources. OAuth 2.
  name: Cvent REST API
  slug: rest-api
- description: Cvent Webhooks notify external applications when actions occur in Cvent and send relevant data to a specified URL, automatically pushing event, attendee, speaker, and meeting request data to subscribe
  name: Cvent Webhooks API
  slug: webhooks
- description: The Cvent Supplier Network (CSN) API provides integration with a database of 280,000+ hotels, suppliers, and destinations worldwide. Planners search and compare venues and manage RFPs; suppliers creat
  name: Cvent Supplier Network (CSN) API
  slug: csn-api
- description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) connecting Cvent registration with Passkey hotel reservations. Send registrant info, fetch event and hotel availabil
  name: Cvent Passkey RegLink API
  slug: passkey-reglink
- description: The Cvent SOAP API is the original legacy API for pushing and pulling data between Cvent and internal systems. Supports contact and event management, custom fields, address book, and metadata. Being s
  name: Cvent SOAP API (Legacy)
  slug: soap-api
- description: The Cvent Custom Widgets API allows developers to build custom interactive widgets for Cvent Event Registration pages. SDK for widget elements, configuration files, and navigation methods.
  name: Cvent Custom Widgets API
  slug: custom-widgets
- description: Cvent SSO enables identity provider integration via SAML and OpenID Connect for planner login, access portals, event registrant and Attendee Hub, Events+, and portal applications.
  name: Cvent Single Sign-On (SSO) Integration
  slug: sso
- description: The Cvent White Label API enables venues and suppliers to embed Cvent RFP functionality into their own websites with custom branding, theming, and analytics for embedded RFP forms.
  name: Cvent White Label API
  slug: white-label
- description: The Cvent Salesforce App integrates Cvent event data with Salesforce CRM, enabling users to view events from Salesforce, invite contacts and leads, and sync attendee data bidirectionally.
  name: Cvent Salesforce App
  slug: salesforce-app
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Attendee entity primarily refers to the person throughout the lifecycle of an event including registration, enrollment into sessions, and participation. Once contacts are added to events, an Atten
  name: Cvent Attendees API
  phrasing_intents:
  - id: listDurations
    intent: List how long attendees engaged in sessions
    question: How long did attendees spend in sessions or watching videos?
  - id: createAttendee
    intent: Add contacts to an event as attendees
    question: How do I register existing contacts for an event?
  - id: listAttendees
    intent: List attendees in the account
    question: Who is registered across my events?
  - id: listAttendeesPostFilter
    intent: Search attendees with a long filter in the body
    question: My attendee filter is too long for the URL; what can I use instead?
  - id: getAttendeeById
    intent: Get one attendee
    question: What's the registration status of a specific attendee?
  - id: updateAttendee
    intent: Update an attendee's registration
    question: Can I change an attendee's registration type after they've signed up?
  - id: updateAttendeeSubscriptionStatus
    intent: Change an attendee's email subscription
    question: How do I unsubscribe an attendee from event emails?
  - id: updateInternalInfoAnswers
    intent: Update an attendee's internal information answers
    question: How do I record internal-only notes on an attendee?
  phrasing_ops: 12
  slug: cvent-attendees-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'A contact is a record in your account’s address book that represents an individual. The data stored within these records includes personal information, group memberships, and historical data on event '
  name: Cvent Contacts API
  phrasing_intents:
  - id: createContactGroup
    intent: Create a contact group
    question: How do I set up a new group to organize contacts, like a VIP list?
  - id: listContactGroups
    intent: List contact groups
    question: What contact groups do I have in my Cvent address book?
  - id: getContactGroupById
    intent: Get a contact group
    question: How do I look up one contact group's details?
  - id: updateContactGroup
    intent: Update a contact group
    question: How do I rename an existing contact group?
  - id: deleteContactGroup
    intent: Delete a contact group
    question: How do I delete a contact group I no longer use?
  - id: getContactIdsByContactGroup
    intent: List contact IDs in a group
    question: Which contacts belong to a particular contact group?
  - id: addContactToContactGroup
    intent: Add a contact to a contact group
    question: How do I put a contact into one of my contact groups?
  - id: removeContactFromContactGroup
    intent: Remove a contact from a contact group
    question: How do I take someone out of a contact group without deleting their contact record?
  phrasing_ops: 28
  slug: cvent-contacts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Events are used to collect registrations and allow attendees to select their schedule. Use these APIs to get information about your events and use the event ID to get further details about the event, '
  name: Cvent Events API
  phrasing_intents:
  - id: listAdmissionItems
    intent: List admission items across events
    question: What admission items are set up in my Cvent account?
  - id: listAdmissionItemsPostFilters
    intent: Filter admission items with a long body filter
    question: How can I query admission items when my filter is too long for the URL?
  - id: getEventQuestions
    intent: List registration questions defined for events
    question: Which registration questions have been configured on my events?
  - id: getChoicesForQuestion
    intent: Get the answer choices for an event question
    question: What answer options does a particular event question offer?
  - id: getEvents
    intent: List events
    question: What events do we have in Cvent?
  - id: createEventAsync
    intent: Create a new event asynchronously
    question: How do I create a brand-new event through the API?
  - id: getEventAsyncStatus
    intent: Check whether an async event creation finished
    question: Is the event I asked Cvent to create ready yet?
  - id: getEventCopyStatus
    intent: Check the status of an event copy
    question: Has my event copy finished running?
  phrasing_ops: 52
  slug: cvent-events-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: A session is a presentation, discussion, or activity. Use these APIs to get information about your sessions and use the session ID to get further data within the event.
  name: Cvent Sessions API
  phrasing_intents:
  - id: getSessionLocation
    intent: List an event's session locations
    question: Which rooms or locations are set up for sessions at my event?
  - id: addSessionLocation
    intent: Add a session location to an event
    question: How do I add a new room where sessions can be held at my event?
  - id: createProgramItem
    intent: Create a program item within a session
    question: How do I add a talk or panel to a session's schedule?
  - id: listProgramItems
    intent: List session program items
    question: Where can I see the talks, workshops and panels scheduled inside my sessions?
  - id: filterProgramItemDocuments
    intent: Search program item documents with a filter
    question: How can I find which documents are attached to session program items across my events?
  - id: listProgramItemsPostFilters
    intent: Search program items with a long body filter
    question: My program item filter is too long for the URL — can I send it in the request body instead?
  - id: updateProgramItem
    intent: Update a session program item
    question: How do I rename or change the length of a talk already in a session's program?
  - id: deleteProgramItem
    intent: Delete a session program item
    question: How do I remove a talk or panel from a session's program entirely?
  phrasing_ops: 29
  slug: cvent-sessions-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: An appointment is a meeting scheduled between two or more parties. These APIs allow you to get
  name: Cvent Appointments API
  phrasing_intents:
  - id: listAppointmentAttendees
    intent: List appointment attendees
    question: Who are the attendees taking part in appointments?
  - id: getAppointmentAttendeeById
    intent: Get one appointment attendee
    question: What details do you have on a particular appointment attendee?
  - id: listAvailability
    intent: List appointment availability times
    question: When have people said they are available for appointments?
  - id: getAvailabilityById
    intent: Get one appointment availability time
    question: What is the time range on a specific availability record?
  - id: listAppointmentEvents
    intent: List appointment events
    question: Which events have appointment scheduling set up?
  - id: getAppointmentEventById
    intent: Get an appointment event
    question: What are the settings of a particular appointment event?
  - id: listAvailableTimes
    intent: Find open slots to book an appointment
    question: What open times and locations can I book an appointment in?
  - id: listAppointmentTypes
    intent: List appointment types for an appointment event
    question: What kinds of appointments can be booked at an appointment event?
  phrasing_ops: 16
  slug: cvent-appointments-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Attendee Activities API gives valuable insight into your customer's experience at your Cvent event.
  name: Cvent Attendee Activities API
  phrasing_intents:
  - id: listAttendeeActivities
    intent: List attendee activities
    question: What have attendees been doing at my events, like check-ins or session views?
  - id: createAttendeeActivity
    intent: Record an external attendee activity
    question: How do I push an activity from another system into an attendee's Cvent timeline?
  - id: listExternalAttendeeActivitiesMetadata
    intent: List external activity type definitions
    question: Which external activity types have been defined for attendee tracking?
  - id: createExternalAttendeeActivityMetadata
    intent: Define a new external activity type
    question: How do I register a new kind of external activity before sending attendee activities?
  - id: deleteExternalAttendeeActivityMetadata
    intent: Delete an external activity type definition
    question: How do I delete an external activity type I no longer track?
  - id: updateExternalAttendeeActivityMetadata
    intent: Update an external activity type definition
    question: How do I change the fields on an external activity type I defined?
  phrasing_ops: 6
  slug: cvent-attendee-activities-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'The Attendee Insights feature provides valuable information about your event attendees. It assists planners, marketers, and exhibitors in targeting customers effectively, thereby enhancing engagement '
  name: Cvent Attendee Insights API
  phrasing_intents:
  - id: listAttendeeInsights
    intent: List engagement scores
    question: Which engagement scores have we set up across events?
  - id: getAttendeeInsightsById
    intent: Get an engagement score definition
    question: How is a particular engagement score configured?
  - id: getScores
    intent: List attendees' engagement scores
    question: Which attendees were most engaged according to an engagement score?
  - id: getStats
    intent: Summarize an engagement score
    question: What is the overall distribution of engagement for an event?
  phrasing_ops: 4
  slug: cvent-attendee-insights-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: These APIs retrieve and manage attendee messages—communications exchanged between attendees within channels. Channels are virtual spaces created for one-on-one or group conversations, allowing attende
  name: Cvent Attendee Messages API
  phrasing_intents:
  - id: getAttendeeMessagesMembers
    intent: List members of attendee chat channels
    question: Who is in a chat channel that attendees started with each other?
  phrasing_ops: 1
  slug: cvent-attendee-messages-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Audience Segments allow planners to segment their attendees into groups and
  name: Cvent Audience Segments API
  phrasing_intents:
  - id: listAttendeeAudienceSegments
    intent: List an attendee's active audience segments
    question: Which audience segments does a given attendee currently belong to?
  - id: disassociateAttendeeFromAudienceSegments
    intent: Remove an attendee from all segments
    question: How do I pull an attendee out of every audience segment at once?
  - id: listAssociatedAudienceSegments
    intent: Search an attendee's segments with a body filter
    question: Can I send a long filter in the body to find an attendee's active segments?
  - id: createAudienceSegment
    intent: Create an audience segment
    question: How do I create a new audience segment for targeting attendees at an event?
  - id: listAudienceSegments
    intent: List audience segments
    question: What audience segments exist for an event?
  - id: listAudienceSegmentsPostFilter
    intent: Search audience segments with a body filter
    question: My audience segment filter is too long — can I send it in the request body?
  - id: getAudienceSegmentById
    intent: Get an audience segment
    question: How do I look up one audience segment's details?
  - id: updateAudienceSegment
    intent: Update an audience segment
    question: How do I rename an audience segment?
  phrasing_ops: 12
  slug: cvent-audience-segments-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Badge print jobs can be scheduled to a printer pool, so a printer in the printer pool can consume the job and print the badge.
  name: Cvent Badge Print Job API
  phrasing_intents:
  - id: createBadgePrintJob
    intent: Send a badge to print
    question: How do I print an attendee's badge on a printer pool?
  - id: getEventBadgePrintJobs
    intent: List badge print jobs for an event
    question: Which badges have been sent to print at my event?
  - id: getBadgePrintJob
    intent: Check a badge print job
    question: Did a specific badge finish printing?
  phrasing_ops: 3
  slug: cvent-badge-print-job-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Badge printer pools are set up from Cvent UI. You can use this API to retrieve badge printer pools.
  name: Cvent Badge Printer Pools API
  phrasing_intents:
  - id: getBadgePrinterPools
    intent: List badge printer pools at an event
    question: Which badge printer pools are available at my event?
  - id: getBadgePrinterPool
    intent: Get one badge printer pool
    question: What printers are in a specific badge printer pool?
  phrasing_ops: 2
  slug: cvent-badge-printer-pools-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Budget is an event feature used to organize spending and track [allocations](https://support.cvent.com/s/communityarticle/Setting-Up-Budget-Allocations). Use this API to view budget items, cards and c
  name: Cvent Budget API
  phrasing_intents:
  - id: getAccountBudgetItems
    intent: List budget items across all events
    question: Which budget items changed across all my events in a date range?
  - id: getAccountVendors
    intent: List account-level budget vendors
    question: Which vendors are set up under Admin > Budget > Vendors in my account?
  - id: getCards
    intent: List payment cards on the account
    question: What payment cards are registered on my Cvent account?
  - id: getCardTransactions
    intent: List card transactions
    question: Which card charges were recorded against my account last month?
  - id: createCardTransaction
    intent: Record a card transaction
    question: How do I log a company card charge against an event?
  - id: deleteCardTransaction
    intent: Delete a card transaction
    question: How do I remove a card transaction that was logged by mistake?
  - id: updateCardTransaction
    intent: Update a recorded card transaction
    question: Can I correct the amount on a card transaction I already recorded?
  - id: getCurrencyConversionRate
    intent: List conversion rates for a currency
    question: What conversion rates are defined for euros in my account?
  phrasing_ops: 24
  slug: cvent-budget-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Bulk API provides a simple interface to upload large amounts of data into Cvent. The API processes the uploaded data asynchronously making API calls on behalf of the caller.
  name: Cvent Bulk API
  phrasing_intents:
  - id: createBulkJob
    intent: Create a bulk job
    question: How do I run the same API call over thousands of records at once?
  - id: getBulkJobById
    intent: Check a bulk job's status
    question: How far along is my bulk job, and how many records failed?
  - id: cancelBulkJob
    intent: Cancel a running bulk job
    question: How do I stop a bulk job that is already processing?
  - id: uploadBulkJobData
    intent: Upload records to a bulk job
    question: How do I load data into a bulk job before running it?
  - id: listBulkJobResult
    intent: List results of a bulk job
    question: Which records in my bulk job succeeded or failed?
  - id: runBulkJob
    intent: Run a bulk job on its uploaded data
    question: How do I start processing the data I uploaded to a bulk job?
  phrasing_ops: 6
  slug: cvent-bulk-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Planners use eMarketing campaigns to contact an audience, such as newsletters, press releases, or product updates. Campaign emails are used as newsletters, promotions, advertisements, or marketing mes
  name: Cvent Campaigns API
  phrasing_intents:
  - id: getCampaigns
    intent: List eMarketing campaigns
    question: What eMarketing campaigns do we have running?
  - id: getEmailTemplates
    intent: List a campaign's email templates
    question: Which email templates belong to a campaign?
  - id: sendEMarketingEmails
    intent: Send a campaign email to recipients
    question: How do I send an eMarketing email to people on my recipient list?
  - id: getEmarketingEmailStatus
    intent: Check the delivery status of a campaign send
    question: Did my eMarketing email actually go out?
  phrasing_ops: 4
  slug: cvent-campaigns-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '**Card Tokenization**: Tokenization is the process Cvent uses to collect sensitive card details and'
  name: Cvent Card Tokens API
  phrasing_intents:
  - id: createCardTokens
    intent: Tokenize a credit card
    question: How do I avoid sending raw card numbers to other Cvent API calls?
  phrasing_ops: 1
  slug: cvent-card-tokens-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: These API's provide compliance support for regulated industries.
  name: Cvent Compliance API
  phrasing_intents:
  - id: getConfiguration
    intent: Get communication compliance settings
    question: Which communication types is my account recording for compliance?
  - id: updateConfiguration
    intent: Change which communications are logged
    question: How do I choose which message types get recorded in the communication log?
  - id: getCommunicationLogMessages
    intent: List communication log messages
    question: How do I review emails, chats and session Q&A logged for compliance?
  - id: filterCommunicationLogMessages
    intent: Search communication logs with a body filter
    question: Can I post a long filter to search the compliance communication log?
  phrasing_ops: 4
  slug: cvent-compliance-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Custom Fields are created by event planners to track important information about specific objects like events, contacts, or sessions. Use these APIs to view, create, and update custom fields in your a
  name: Cvent Custom Fields API
  phrasing_intents:
  - id: listCustomFields
    intent: List custom fields in the account
    question: What custom fields are defined for contacts in my account?
  - id: createCustomField
    intent: Create a custom field
    question: How do I add a new custom question field to my account?
  - id: updateCustomField
    intent: Update a custom field
    question: Can I rename an existing custom field?
  - id: getCustomField
    intent: Get one custom field
    question: What type and choices does a specific custom field have?
  - id: updateCustomFieldAdvancedLogic
    intent: Make a field's choices depend on another field
    question: How do I show different choices depending on the answer to another field?
  - id: createCustomFieldTranslation
    intent: Add a translation to a custom field
    question: How do I translate a custom field into another language?
  - id: updateCustomFieldTranslation
    intent: Update a custom field's existing translation
    question: Can I fix the French translation already on a custom field?
  phrasing_ops: 7
  slug: cvent-custom-fields-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Discounts provide a way to reduce the cost of event registration items. Use these APIs to manage event discounts, including creating, updating, and linking discounts to agenda items.
  name: Cvent Discounts API
  phrasing_intents:
  - id: listEventDiscounts
    intent: List an event's discounts
    question: What discount codes are being used in my event?
  - id: createEventDiscount
    intent: Create a discount in an event
    question: How do I set up a new discount code for my event?
  - id: listDiscountedAgendaItems
    intent: List agenda items tied to discounts
    question: Which sessions or admission items in my event have discounts attached?
  - id: updateEventDiscount
    intent: Update an event discount
    question: How do I change an existing discount code in my event?
  - id: linkAgendaItemToDiscount
    intent: Apply a discount to an agenda item
    question: How do I make a discount apply to a specific session or admission item?
  - id: unlinkAgendaItemFromDiscount
    intent: Stop a discount applying to an agenda item
    question: How do I remove a discount from one session without deleting the discount?
  phrasing_ops: 6
  slug: cvent-discounts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event planners use emails to invite registrants, market their events and request feedback from attendees. Use these APIs to get historical data about your emails and see relevant details like the type
  name: Cvent Emails API
  phrasing_intents:
  - id: getBounceDetails
    intent: List email bounces
    question: Which of my emails bounced last month?
  - id: getEmailsHistory
    intent: List sent email history
    question: What emails has my account sent recently?
  - id: getEmailStatus
    intent: Check delivery status of an email send
    question: How do I check whether an email send request was delivered?
  phrasing_ops: 3
  slug: cvent-emails-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event Credits reward attendees for participating in your events. Planners can award credits for the entire event, specific sessions, or both. You can also award credits after attendees complete survey
  name: Cvent Event Credits API
  phrasing_intents:
  - id: getAttendeeCredits
    intent: List attendee event credits
    question: What event credits have attendees earned across my account?
  phrasing_ops: 1
  slug: cvent-event-credits-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: EventFeatures related APIs
  name: Cvent Event Features API
  phrasing_intents:
  - id: getEventFeatures
    intent: List features available for an event
    question: Which features are enabled or available on my event?
  - id: updateEventFeatures
    intent: Enable or disable an event feature
    question: How do I turn an event feature on or off?
  - id: launchEventFeatures
    intent: Launch an event feature to attendees
    question: How do I make an event feature live for attendees?
  - id: listEventWeblinks
    intent: List an event's weblinks
    question: What public links, like the registration page, does my event have?
  phrasing_ops: 4
  slug: cvent-event-features-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event roles are event specific permission sets for your organization's users. Use these APIs to retrieve, create, update, and delete event role assignments to your organization's users.
  name: Cvent Event Role API
  phrasing_intents:
  - id: listEventRoleAssignment
    intent: List event role assignments
    question: Which users hold which roles on an event?
  phrasing_ops: 1
  slug: cvent-event-role-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event travel lets planners capture air & hotel requests from attendees and track air actuals, hotel reservations and alternate travel answers at your event. Use these endpoints to retrieve your air, h
  name: Cvent Event Travel API
  phrasing_intents:
  - id: getAirActualDetail
    intent: Get attendees' booked flight details
    question: What flights did attendees actually book for an event?
  - id: getAirRequests
    intent: Get attendees' flight requests
    question: Which attendees have requested flights for my event?
  - id: getAlternateTravelAnswers
    intent: Get travel answers from attendees who opted out
    question: What did attendees say when they declined air or hotel booking?
  - id: getHotelRequests
    intent: Get attendees' hotel requests
    question: Which attendees asked for hotel rooms at my event?
  - id: getHousingReservationRequests
    intent: Get attendees' housing reservation requests
    question: What housing reservation requests have attendees submitted?
  phrasing_ops: 5
  slug: cvent-event-travel-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Exhibitor Content operations for an exhibitor. This API allows you to upload & get exhibitor content data such as files, weblinks.
  name: Cvent Exhibitor Content API
  phrasing_intents:
  - id: listExhibitorFiles
    intent: List an exhibitor's files
    question: What files, like brochures, has an exhibitor attached to their listing?
  - id: getExhibitorFile
    intent: Get one of an exhibitor's files
    question: What are the display name and order of a specific exhibitor file?
  - id: updateExhibitorFile
    intent: Attach an uploaded file to an exhibitor
    question: How do I attach a file I already uploaded to an exhibitor's profile?
  - id: disassociateExhibitorFile
    intent: Detach a file from an exhibitor
    question: How do I remove a file from an exhibitor's listing?
  - id: listExhibitorWeblinks
    intent: List an exhibitor's weblinks
    question: What website links does an exhibitor show on their profile?
  - id: createExhibitorWeblink
    intent: Add a weblink to an exhibitor
    question: How do I add a website link to an exhibitor's booth profile?
  - id: getExhibitorWeblink
    intent: Get one of an exhibitor's weblinks
    question: Where does a specific exhibitor weblink point?
  - id: updateExhibitorWeblink
    intent: Update an exhibitor weblink
    question: How do I change the URL of an existing exhibitor link?
  phrasing_ops: 9
  slug: cvent-exhibitor-content-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '* **Exhibitor Admin -** Exhibitor Admins are administrators that have access to the exhibitor portal. In the portal, they are able to complete pre-event tasks, manage their team, purchase LeadCapture '
  name: Cvent Exhibitor Team API
  phrasing_intents:
  - id: listExhibitorAdmins
    intent: List an exhibitor's admins
    question: Who are the admins managing an exhibitor's profile at my event?
  - id: postExhibitorAdmin
    intent: Add an admin to an exhibitor
    question: How do I give someone admin access to manage an exhibitor at my event?
  - id: getExhibitorAdmin
    intent: Get an exhibitor admin
    question: How do I look up the name and email of a specific exhibitor admin?
  - id: updateExhibitorAdmin
    intent: Update an exhibitor admin
    question: How do I change an exhibitor admin's email address?
  - id: listBoothStaff
    intent: List an exhibitor's booth staff
    question: Who is working the booth for a particular exhibitor?
  - id: associateBoothStaff
    intent: Make an attendee booth staff for an exhibitor
    question: How do I assign a registered attendee to staff an exhibitor's booth?
  - id: getBoothStaff
    intent: Get a booth staff member
    question: Which attendee is behind a given booth staff record?
  - id: deleteBoothStaff
    intent: Remove a booth staff member
    question: How do I take someone off an exhibitor's booth staff?
  phrasing_ops: 8
  slug: cvent-exhibitor-team-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Allows you to upload files and get file location using the file ID. File ID can be used with other APIs to associate the file to an entity. For example:'
  name: Cvent File API
  phrasing_intents:
  - id: uploadFile
    intent: Upload a file for use with other Cvent records
    question: How do I upload an image so I can attach it as a logo or banner?
  - id: getFile
    intent: Get the location of an uploaded file
    question: Where is a file I uploaded stored?
  phrasing_ops: 2
  slug: cvent-file-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RegLink APIs allow you to exchange data with Cvent Passkey events and hotel reservation-booking engines.
  name: Cvent Housing API
  phrasing_intents:
  - id: createConnection
    intent: Connect an integration to a Passkey housing event
    question: How do I authorize my integration for a Passkey event using an access code?
  - id: getHousingEventsSummaries
    intent: List housing events my integration can access
    question: Which housing events does my integration have access to?
  - id: getHousingEventInfo
    intent: Get details of a housing event
    question: What dates and attendee types are configured for a housing event?
  - id: getHousingEventHotels
    intent: List hotels in a housing event's room block
    question: Which hotels are in the room block for my housing event?
  - id: getHousingEventHotel
    intent: Get one hotel's details in a housing event
    question: What's the address of a specific hotel in my housing block?
  - id: getHousingEventHotelAvailability
    intent: Check a hotel's available room nights
    question: Which nights still have rooms available at a hotel in my block?
  - id: getHousingEventRoomTypes
    intent: List room types at a hotel
    question: What room types, like Standard King, does a hotel offer for my event?
  - id: getRoomTypeDetails
    intent: Get a room type's description and images
    question: What does a particular room type look like, with description and photos?
  phrasing_ops: 21
  slug: cvent-housing-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: APIs for managing hotel-related operations.
  name: Cvent Housing Hotels API
  phrasing_intents:
  - id: updateHotelRoomRates
    intent: Update a hotel room's rates
    question: How do I change the nightly rate for a hotel room type in my housing block?
  phrasing_ops: 1
  slug: cvent-housing-hotels-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '* **Leads -** Leads include leads gathered by LeadCapture, Appointments, and Inbound Leads. Use this API to get information for the lead and how it was captured.'
  name: Cvent Leads API
  phrasing_intents:
  - id: getEliteratureRequests
    intent: List e-literature requests
    question: Which attendees asked exhibitors for digital brochures?
  - id: getLeadQualificationAnswers
    intent: Get a lead's qualification answers
    question: What did a lead answer to an exhibitor's qualification questions?
  - id: getLeads
    intent: List leads
    question: How do I export the leads exhibitors captured at my events?
  - id: getLeadsPostFiltersData
    intent: Search leads with a body filter
    question: My leads filter is too long for the URL — can I send it in the body?
  phrasing_ops: 4
  slug: cvent-leads-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: When planning an event, meeting request forms are customizable online questionnaires to capture information about the event and facilitate the approval of events. When a meeting request form is submit
  name: Cvent Meeting Request API
  phrasing_intents:
  - id: getMeetingRequestByEventId
    intent: Get the meeting request behind an event
    question: Which meeting request was this event created from?
  - id: listMRF
    intent: List meeting request forms
    question: What meeting request forms do we have set up?
  - id: getMRFById
    intent: Get a meeting request form
    question: What questions and settings does a particular meeting request form have?
  - id: createMeetingRequest
    intent: Bulk create meeting requests on a form
    question: How do I submit new meeting requests through an active form via the API?
  - id: updateMeetingRequest
    intent: Bulk update meeting requests on a form
    question: How do I add answers to several existing meeting requests at once?
  - id: listMeetingRequest
    intent: List meeting requests submitted on a form
    question: Which meeting requests have been submitted through a given form?
  - id: getMeetingRequestById
    intent: Get a single meeting request
    question: What did someone ask for in a specific meeting request?
  - id: listMeetingRequestDocuments
    intent: List documents attached to a meeting request
    question: What attachments came with a meeting request?
  phrasing_ops: 8
  slug: cvent-meeting-request-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Orders represent a collection of order items purchased by an attendee. Use these APIs to get information about orders and order items.
  name: Cvent Orders API
  phrasing_intents:
  - id: getAccountOrders
    intent: List orders across the account
    question: What orders have been placed across all our events?
  - id: getAccountOrderById
    intent: Get an order
    question: What is in a specific order and what did it total?
  - id: getAccountOrderItemsByOrderId
    intent: List the items on an order
    question: Which line items make up a particular order?
  - id: getAccountOrderItem
    intent: Get one item on an order
    question: What are the price and quantity of one line on an order?
  phrasing_ops: 4
  slug: cvent-orders-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Process forms automate data collection and notifications related to planning and executing events. Process form submissions are responses to a specific process form, providing data the form requests. '
  name: Cvent Process Form API
  phrasing_intents:
  - id: listProcessFormSubmission
    intent: List process form submissions
    question: What process form submissions have come in?
  phrasing_ops: 1
  slug: cvent-process-form-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Beta - All APIs are in Beta. Proposal Drafts are editable copies of proposals. This API allows you to edit proposal data privately before publishing.
  name: Cvent Proposal Draft API
  phrasing_intents:
  - id: createProposalDraft
    intent: Create a draft proposal for an RFP
    question: How do I start a draft proposal in response to an RFP?
  phrasing_ops: 1
  slug: cvent-proposal-draft-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RFP additional details APIs for managing past event references and other miscellaneous RFP operations.
  name: Cvent RFP Additional Details API
  phrasing_intents:
  - id: listRfpPastEvents
    intent: List past events recorded on an RFP
    question: What past events did the planner list when creating an RFP?
  phrasing_ops: 1
  slug: cvent-rfp-additional-details-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RFP (Request for Proposal) management APIs for core RFP operations including CRUD operations for base RFPs.
  name: Cvent RFP Management API
  phrasing_intents:
  - id: getRfpLeadSource
    intent: Get an RFP lead source
    question: Where did a given RFP originate from?
  - id: getRfpLeadSourceSection
    intent: Get an RFP lead source section
    question: Which specific form or website section did an RFP come from?
  - id: getRFP
    intent: Get an RFP
    question: What are the basic details of a specific RFP?
  phrasing_ops: 3
  slug: cvent-rfp-management-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RFP requirements APIs for managing RFP-specific requirements including guest rooms, meeting rooms, custom questions, custom fields, and attachments (CRUD operations).
  name: Cvent RFP Requirements API
  phrasing_intents:
  - id: listRfpAgendaItems
    intent: List an RFP's agenda items
    question: What meetings and functions are requested in an RFP's agenda?
  - id: listRfpAgendaItemSchedules
    intent: List schedules for an RFP's agenda items
    question: When are the agenda items on an RFP scheduled to happen?
  - id: listRfpAttachments
    intent: List an RFP's attachments
    question: What files were attached to an RFP sent to venues?
  - id: listRfpCustomFields
    intent: List an RFP's custom field answers
    question: What answers were given to custom fields on an RFP?
  - id: getRfpGuestRooms
    intent: Get an RFP's guest room requirements
    question: How many guest rooms does an RFP request?
  - id: listRfpInternalDocuments
    intent: List an RFP's internal documents
    question: Which internal-only documents are stored on an RFP?
  - id: listRfpQuestions
    intent: List an RFP's questions
    question: What standard and custom questions are asked in an RFP?
  phrasing_ops: 7
  slug: cvent-rfp-requirements-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Suppliers are the venues and service providers that receive and respond to RFPs. Use these APIs to manage supplier associations, view recipient history, and create award details.
  name: Cvent RFP Suppliers API
  phrasing_intents:
  - id: listRfpRecipientsHistory
    intent: List who was copied on an RFP
    question: Who has been copied on an RFP over time?
  - id: getRfpSuppliers
    intent: List suppliers on an RFP
    question: Which venues or suppliers received a particular RFP?
  phrasing_ops: 2
  slug: cvent-rfp-suppliers-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Seating lets you plan seating at your events by configuring tables and assigning seats to your attendees. The seating APIs allow you to create, update, and delete seating, tables, seats, and seating a
  name: Cvent Seating API
  phrasing_intents:
  - id: listSeating
    intent: List seating charts for an event
    question: What seating charts are set up for my event?
  - id: getEventTableAssignments
    intent: List table assignments across all seatings
    question: Where is every attendee seated across all seating charts at my event?
  - id: getSeating
    intent: Get one seating chart
    question: What are the details of a specific seating chart?
  - id: getTableAssignment
    intent: List table assignments in one seating
    question: Who is assigned to tables in one particular seating chart?
  - id: listTables
    intent: List tables in a seating chart
    question: How many tables are in a seating chart?
  - id: getTable
    intent: Get one table in a seating chart
    question: What are the details of a specific table in a seating chart?
  - id: listSeats
    intent: List seats at a table
    question: Which seats are at a given table?
  - id: getSeat
    intent: Get one seat
    question: What are the details of a single seat at a table?
  phrasing_ops: 8
  slug: cvent-seating-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Retrieves Check-In & Check-Out Signatures Of Attendees
  name: Cvent Signatures API
  phrasing_intents:
  - id: getSignatures
    intent: List check-in and check-out signatures
    question: Where can I find the signatures attendees gave at check-in or check-out?
  phrasing_ops: 1
  slug: cvent-signatures-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Speakers are individuals presenting at your event's session(s). Use Speaker APIs to read existing speaker data, create new speakers or update existing speakers in your events.
  name: Cvent Speakers API
  phrasing_intents:
  - id: getSessionProgramSpeakers
    intent: List program item and speaker links
    question: Which speakers are assigned to which talks inside sessions?
  - id: listSessionProgramSpeakersPostFilters
    intent: Search program item speakers with a body filter
    question: My filter for program item speakers is long — can I send it in the request body?
  - id: createSessionProgramSpeaker
    intent: Add a speaker to a program item
    question: How do I assign a speaker to a specific talk within a session?
  - id: getSessionProgramSpeaker
    intent: Get one program item speaker link
    question: How do I check whether a speaker is on a particular program item?
  - id: deleteSessionProgramSpeaker
    intent: Remove a speaker from a program item
    question: How do I take a speaker off one talk without removing them from the whole session?
  - id: listSpeakersCategories
    intent: List speaker categories
    question: What speaker categories like keynote or panelist are set up?
  - id: addSpeakerCategory
    intent: Create a speaker category
    question: How do I add a new speaker category such as moderator?
  - id: listSpeakers
    intent: List speakers
    question: How do I get all the speakers across my events?
  phrasing_ops: 19
  slug: cvent-speakers-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Surveys are lists of questions deployed to your contacts. Surveys can be standalone or can be associated to a Cvent event. Use these APIs to search for surveys and retrieve the associated questions an
  name: Cvent Surveys API
  phrasing_intents:
  - id: getAllEventSurveyResponses
    intent: List survey responses across all events
    question: How can I pull every event survey response across all my events at once?
  - id: getEventSurveys
    intent: List surveys attached to an event
    question: Which surveys are attached to my event?
  - id: getEventSurveyQuestions
    intent: List the questions in an event survey
    question: What questions does an event's feedback survey ask?
  - id: getEventSurveyRespondents
    intent: List respondents to an event survey
    question: Who has responded to a survey on my event?
  - id: createEventSurveyRespondent
    intent: Add a respondent to an event survey
    question: How do I register someone as a respondent on an event survey?
  - id: updateEventSurveyRespondent
    intent: Update an event survey respondent
    question: How do I change details on an existing event survey respondent?
  - id: createEventSurveyResponses
    intent: Submit answers for an event survey respondent
    question: How do I record a respondent's answers to an event survey?
  - id: getEventSurveyResponses
    intent: List responses to one event survey
    question: What answers came back on a specific event survey?
  phrasing_ops: 23
  slug: cvent-surveys-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Transactions represent the financial exchanges that occur within your account. Use these APIs to retrieve and manage transaction data, including charges, refunds, and adjustments associated with your '
  name: Cvent Transactions API
  phrasing_intents:
  - id: getAccountTransactions
    intent: List registration transactions in the account
    question: What payment transactions happened in my account this week?
  - id: getTransaction
    intent: Get one transaction
    question: What are the details of a specific payment transaction?
  - id: getAccountTransactionItems
    intent: List the line items of a transaction
    question: Which items were charged in a particular transaction?
  - id: getAccountTransactionItem
    intent: Get one transaction line item
    question: What was charged on a single line of a transaction?
  phrasing_ops: 4
  slug: cvent-transactions-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The travel account, or corporation that represents the demand-side of travel RFPs.
  name: Cvent Travel Accounts API
  phrasing_intents:
  - id: ListTravelAccounts
    intent: List travel accounts
    question: What corporate travel accounts are set up?
  - id: ListSupplierAccounts
    intent: List supplier travel accounts
    question: Which supplier travel accounts exist across all my travel programs?
  - id: getTravelAccount
    intent: Get a travel account
    question: How do I look up one travel account's details?
  - id: getSupplierAccount
    intent: Get the supplier account for a travel account
    question: Which supplier account is tied to a given travel account?
  phrasing_ops: 4
  slug: cvent-travel-accounts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Travel RFP APIs provide access to travel programs and proposals. A travel program
  name: Cvent Travel RFPs API
  phrasing_intents:
  - id: ListTravelPrograms
    intent: List travel programs
    question: Which corporate travel programs do we run hotel RFPs for?
  - id: ListTravelProgramsQuestions
    intent: List questions across all travel programs
    question: What RFP questions are used across all our travel programs?
  - id: getTravelProgram
    intent: Get one travel program
    question: What are the details of a specific travel program?
  - id: ListTravelProgramQuestions
    intent: List questions for one travel program
    question: Which questions does one particular travel program ask hotels?
  - id: getTravelProgramQuestion
    intent: Get one travel program question
    question: What does a specific question in a travel program ask?
  - id: ListTravelProposals
    intent: List travel proposals
    question: Which hotel proposals have come in for our travel programs?
  - id: ListTravelProposalBids
    intent: List travel proposal bids
    question: What bids have hotels submitted on travel proposals?
  - id: GetTravelProposalBid
    intent: Get one travel proposal bid
    question: What rates did a hotel offer in a specific bid?
  phrasing_ops: 9
  slug: cvent-travel-rfps-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Travel Supplier APIs provide access to Cvent data related to hotels, apartments, and other travel providers. This includes information related to properties, and sleeping rooms.
  name: Cvent Travel Suppliers API
  phrasing_intents:
  - id: PropertyApiListBrands
    intent: List hotel supplier brands
    question: Which hotel brands are in the travel supplier directory?
  - id: PropertyApiGetBrand
    intent: Get a supplier brand
    question: How do I look up one hotel brand by its brand code?
  - id: PropertyApiListChains
    intent: List hotel supplier chains
    question: What hotel chains are available as travel suppliers?
  - id: PropertyApiGetChain
    intent: Get a supplier chain
    question: How do I look up a hotel chain by its chain ID?
  - id: PropertyApiListProperties
    intent: List supplier properties
    question: Which hotel properties are in the supplier directory?
  - id: PropertyApiGetProperty
    intent: Get a supplier property
    question: How do I get the details of one hotel property?
  - id: BtApiGetPropertyRooms
    intent: List supplier property rooms
    question: What room types do supplier properties offer?
  - id: PropertyApiGetPropertyRoom
    intent: Get a supplier property room
    question: How do I read the details of one hotel room type?
  phrasing_ops: 8
  slug: cvent-travel-suppliers-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Use these APIs view your REST API usage and limits metrics. For more details on limits - [Rate Limits](#section/Getting-Started/Rate-Limits)
  name: Cvent Usage API
  phrasing_intents:
  - id: getUsage
    intent: Check recent API call usage
    question: How many API calls has our account made in the last week?
  - id: getUsageTier
    intent: Get the account's API usage tier
    question: Which API usage tier is our account on?
  phrasing_ops: 2
  slug: cvent-usage-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The [SCIM](https://www.simplecloud.info/) standard allows for easier cross-domain identity management. This API allows you to manage your account users and SCIM groups (representing Cvent user roles).
  name: Cvent User SCIM API
  phrasing_intents:
  - id: getUserGroups
    intent: List SCIM groups representing user roles
    question: Which user roles are exposed as SCIM groups in my account?
  - id: getResourceTypes
    intent: List supported SCIM resource types
    question: What SCIM resource types does Cvent support?
  - id: getResourceType
    intent: Get one SCIM resource type
    question: What endpoint and schema does the User resource type use?
  - id: getSchemas
    intent: List SCIM user and group schemas
    question: What SCIM schemas and extensions describe users and groups?
  - id: getSchema
    intent: Get one SCIM schema definition
    question: Which attributes are in the enterprise user extension schema?
  - id: getServiceProviderConfig
    intent: Get the SCIM service provider configuration
    question: Does the SCIM service support filtering, patch or bulk operations?
  - id: createUser
    intent: Provision a new user
    question: How do I provision a new user account through SCIM?
  - id: listUsers
    intent: List provisioned users
    question: Which users are provisioned in my account through SCIM?
  phrasing_ops: 11
  slug: cvent-user-scim-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Operations for managing account users and user groups, including creation, retrieval, update, and deletion. Use these endpoints to administer user access and roles within your account.
  name: Cvent Users API
  phrasing_intents:
  - id: getAccountUserGroups
    intent: List account user groups
    question: What user groups exist in our Cvent account?
  - id: createAccountUserGroup
    intent: Create an account user group
    question: How do I set up a new user group for our planners?
  - id: getAccountUserGroup
    intent: Get an account user group
    question: What are the details of a particular user group?
  - id: updateAccountUserGroup
    intent: Rename or update a user group
    question: How do I rename an existing user group?
  - id: deleteAccountUserGroup
    intent: Delete an account user group
    question: How do I delete a user group we no longer need?
  - id: addUserToAccountUserGroup
    intent: Add a user to a user group
    question: How do I put a user into a user group?
  - id: deleteUserFromAccountUserGroup
    intent: Remove a user from a user group
    question: How do I take a user out of a user group?
  phrasing_ops: 7
  slug: cvent-users-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Manage meeting rooms for a venue, including creating and updating room details, configuring capacities and amenities, and associating images.
  name: Cvent Venue Meeting Rooms API
  phrasing_intents:
  - id: createMeetingRoom
    intent: Add a meeting room to a venue
    question: How do I add a new meeting room to a venue profile?
  - id: listMeetingRoomsOverviews
    intent: List a venue's meeting rooms
    question: What meeting rooms does a venue have?
  - id: updateMeetingRoom
    intent: Replace a meeting room's details
    question: How do I overwrite all of a meeting room's data in one go?
  - id: patchMeetingRoom
    intent: Partially update a meeting room
    question: How do I change just one field on a meeting room, leaving the rest alone?
  - id: associateMeetingRoomImage
    intent: Set a meeting room's image
    question: How do I attach an uploaded photo to a meeting room?
  - id: listMeetingRoomImages
    intent: Get a meeting room's image
    question: Does a meeting room have a photo attached?
  - id: disassociateMeetingRoomImage
    intent: Remove a meeting room's image
    question: How do I take the photo off a meeting room?
  - id: getMeetingRoomOverview
    intent: Get a meeting room's overview
    question: What are the capacity and dimensions of one specific meeting room?
  phrasing_ops: 8
  slug: cvent-venue-meeting-rooms-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Manage venue profile details including type, contact information, address, and other venue properties.
  name: Cvent Venue Profiles API
  phrasing_intents:
  - id: updateVenueDetails
    intent: Replace a venue's profile details
    question: How do I overwrite all of a venue's profile details at once?
  - id: patchVenueDetails
    intent: Change a few venue details
    question: Can I update just a venue's website without resending everything?
  - id: getVenueDetailsOverview
    intent: Get an overview of a venue's details
    question: What does my venue's profile currently say?
  - id: updateVenueFacility
    intent: Replace a venue's facility information
    question: How do I overwrite all facility info, like meeting space and sleeping rooms, for a venue?
  - id: patchVenueFacility
    intent: Change a few venue facility values
    question: Can I update only the year renovated for a venue's facility?
  phrasing_ops: 5
  slug: cvent-venue-profiles-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Videos can be added to Cvent events with renditions at various resolutions, audio files, reactions tracks, and text tracks. Attendee viewership is tracked to get insight into durations, devices used a
  name: Cvent Video API
  phrasing_intents:
  - id: listVideos
    intent: List videos in the account or event
    question: What videos are stored for my account or event?
  - id: getVideoViews
    intent: List video views
    question: Who watched our event videos, and when?
  - id: listAudioTracks
    intent: List a video's audio tracks
    question: What audio tracks or languages does a video have?
  - id: listVideoRenditions
    intent: List a video's renditions
    question: What resolutions or renditions exist for a video?
  - id: createTextTrack
    intent: Add a caption track to a video
    question: How do I add a VTT caption file to a video?
  - id: listVideoTextTracks
    intent: List a video's captions and subtitles
    question: Which caption or subtitle tracks are on a video?
  - id: updateTextTrack
    intent: Update or replace a video's text track
    question: Can I replace the VTT file on an existing caption track?
  phrasing_ops: 7
  slug: cvent-video-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Webcasts are virtual or livestreaming components of your Cvent events. Use these APIs to integrate your virtual events from outside sources into your Cvent workflows, create and delete webcasts from w
  name: Cvent Webcasts API
  phrasing_intents:
  - id: createWebcast
    intent: Create a webcast
    question: How do I set up a live stream for a session in my event?
  - id: listWebcasts
    intent: List webcasts
    question: What webcasts are set up for my events?
  - id: listAttendeeLinks
    intent: List attendee links across all webcasts
    question: How do I see every attendee's personal webcast join link across my account?
  - id: listPlayers
    intent: List webcast player details
    question: Which video players are configured for my webcasts?
  - id: getWebcastById
    intent: Get a webcast
    question: How do I check the settings and status of one webcast?
  - id: deleteWebcast
    intent: Delete a webcast
    question: How do I delete a webcast?
  - id: updateWebcast
    intent: Update a webcast
    question: How do I change the title or status of an existing webcast?
  - id: createAttendeeLinks
    intent: Bulk create attendee links for a webcast
    question: How do I generate join links for attendees of a webcast?
  phrasing_ops: 11
  slug: cvent-webcasts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Endpoints for obtaining, refreshing, and validating OAuth2 access tokens.
  name: Cvent Authentication API
  phrasing_intents:
  - id: oauth2Authorize
    intent: Start the OAuth2 authorization code flow
    question: How do I send a user to Cvent to authorize my app?
  - id: oauth2Token
    intent: Get or refresh an access token
    question: How do I exchange an authorization code for an access token?
  - id: validateToken
    intent: Check that an access token is valid
    question: Is my current access token still valid?
  phrasing_ops: 3
  slug: cvent-authentication-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: An Events+ Hub persists basic information needed to assign an owner and optionally customize the public presentation.
  name: Cvent Events+ Hub API
  phrasing_intents:
  - id: listHubs
    intent: List Events+ hubs
    question: What Events+ hubs does my account have?
  - id: getHubMembers
    intent: List members of an Events+ hub
    question: Who are the members of a particular Events+ hub?
  phrasing_ops: 2
  slug: cvent-events-hub-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '* **Exhibitor -** An exhibitor is an organization that is sponsoring or exhibiting at your event. This API allows you to get information about your exhibitors. * **Registration Pack -** Registration P'
  name: Cvent Exhibitor API
  phrasing_intents:
  - id: getExhibitorCategories
    intent: List an event's exhibitor categories
    question: What exhibitor categories are set up for my event?
  - id: createExhibitorCategory
    intent: Create an exhibitor category for an event
    question: How do I add a new exhibitor category to my event?
  - id: updateExhibitorCategory
    intent: Update an existing exhibitor category
    question: Can I rename an exhibitor category that already exists?
  - id: deleteExhibitorCategory
    intent: Delete an exhibitor category
    question: How do I remove an exhibitor category I no longer need?
  - id: updateExhibitorCategoryBanner
    intent: Set the banner image on an exhibitor category
    question: Can I put a banner image on an exhibitor category using a file I uploaded?
  - id: deleteExhibitorCategoryImage
    intent: Remove the banner from an exhibitor category
    question: How do I take the banner image off an exhibitor category?
  - id: listExhibitors
    intent: List the exhibitors in an exhibitor category
    question: Which exhibitors are assigned to a particular exhibitor category?
  - id: addExhibitorToExhibitorCategory
    intent: Assign an exhibitor to a category
    question: How do I put an exhibitor into an exhibitor category?
  phrasing_ops: 30
  slug: cvent-exhibitor-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: These APIs allow you to create hooks. When triggered, a hook sends a request to your service to get updated data related to the related Cvent object. For more information on using hooks, see the [gett
  name: Cvent Hooks API
  phrasing_intents:
  - id: ListContactHooks
    intent: List contact hooks
    question: What contact hooks are configured in my account?
  - id: createContactHook
    intent: Create a contact hook
    question: How do I have Cvent request contact information from my system?
  - id: updateContactHook
    intent: Update a contact hook
    question: Can I point an existing contact hook to a new callback URL?
  - id: deleteContactHook
    intent: Delete a contact hook
    question: How do I stop Cvent calling a contact hook?
  phrasing_ops: 4
  slug: cvent-hooks-api
artifact_total: 82
asyncapis:
- description: ''
  name: Cvent Webhooks Catalog
  slug: cvent-webhooks-catalog
common:
- group: commercial
  href: https://artifacts.apis.io/cvent/finops/cvent-finops.yml
  title: ''
  type: FinOps
  url: finops/cvent-finops.yml
- group: other
  href: https://artifacts.apis.io/cvent/capabilities/cvent-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cvent-capability-edges.yml
- group: operate
  title: ''
  type: SupportArticles
  url: https://support.cvent.com/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cvent/custom-widgets-labs/issues
- group: agent
  href: https://artifacts.apis.io/cvent/agentic-access/cvent-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cvent/security/cvent-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cvent-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cvent/security/cvent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvent-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cvent/authentication/cvent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cvent-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cvent/scopes/cvent-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cvent-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/
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
  type: OAuthTokenEndpoint
  url: https://api-platform.cvent.com/ea/oauth2/token
- group: other
  title: ''
  type: Standards
  url: https://developers.cvent.com/docs/rest-api/reference/api-standards
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cvent.com/docs/rest-api/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com
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
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.cvent.com/en/security
- group: learn
  title: ''
  type: Training
  url: https://www.cvent.com/en/academy
- group: operate
  title: ''
  type: Community
  url: https://community.cvent.com/home
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cvent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cvent
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://developers.cvent.com/signup
- group: start
  title: ''
  type: Login
  url: https://developers.cvent.com/login
- group: start
  title: ''
  type: Console
  url: https://developers.cvent.com/applications
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/product-terms-of-use
- group: docs
  title: ''
  type: SDKDocumentation
  url: https://developers.cvent.com/docs/rest-api/sdks
- group: build
  href: https://artifacts.apis.io/cvent/packages/cvent-packages.yml
  title: ''
  type: Packages
  url: packages/cvent-packages.yml
- group: build
  href: https://artifacts.apis.io/cvent/packages/cvent-packages.yml
  title: ''
  type: SDKs
  url: packages/cvent-packages.yml
- group: agent
  href: https://artifacts.apis.io/cvent/llms/cvent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cvent-llms.txt
- group: other
  href: https://artifacts.apis.io/cvent/overlays/cvent-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-public-overlay.yaml
- group: design
  href: https://artifacts.apis.io/cvent/conformance/cvent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cvent-conformance.yml
- group: auth
  href: https://artifacts.apis.io/cvent/security/cvent-trust-center.yml
  title: ''
  type: Compliance
  url: security/cvent-trust-center.yml
- group: design
  href: https://artifacts.apis.io/cvent/errors/cvent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cvent-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cvent/lifecycle/cvent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cvent/lifecycle/cvent-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cvent-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cvent/conventions/cvent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cvent-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cvent/changelog/cvent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cvent-changelog.yml
- group: design
  href: https://artifacts.apis.io/cvent/components/cvent-components.yml
  title: ''
  type: Components
  url: components/cvent-components.yml
- group: design
  href: https://artifacts.apis.io/cvent/data-model/cvent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cvent-data-model.yml
- group: design
  href: https://artifacts.apis.io/cvent/asyncapi/cvent-webhooks-catalog.yml
  title: ''
  type: Webhooks
  url: asyncapi/cvent-webhooks-catalog.yml
- group: agent
  href: https://artifacts.apis.io/cvent/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/cvent/security/cvent-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cvent-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cvent/security/cvent-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cvent-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/cvent/rate-limits/cvent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cvent-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cvent/plans/cvent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cvent-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/cvent/wsdl/cvent-soap-api-v200611.wsdl
  title: ''
  type: WSDL
  url: wsdl/cvent-soap-api-v200611.wsdl
- group: build
  title: ''
  type: SDKSourceCode
  url: https://github.com/cvent/rest-sdks
created: '2025-11-19'
description: Cvent is a leading meetings, events, and hospitality technology provider with over 4,800 employees and 22,000+ customers worldwide. The Cvent platform spans Event Cloud (event management, registration, mobile event apps, virtual and hybrid events, Attendee Hub, surveys, Diagramming, and analytics) and Hospitality Cloud (Cvent Supplier Network, Passkey, Venue Sourcing, and Sales & Catering). Programmatic access is delivered through the unified Cvent Platform REST API (api-platform.cvent.com) using OAuth 2.0 client credentials, with legacy SOAP, BadgeKit, Jifflenow, and CSN APIs documented for historical integrations. The developer portal at developers.cvent.com hosts API references, guides, OpenAPI downloads, webhooks, SSO, custom widgets, white-label, and integration documentation.
finops:
- has_sources: true
  method: derived
  name: Cvent Finops
  primary_unit: ''
  service_category: ''
  slug: cvent-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent.png
layout: provider
modified: '2026-09-16'
name: Cvent
nav: Providers
network: true
overview: 'Cvent publishes 65 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 62 more. Tagged areas include Attendee Hub, Attendee Management, Conferences, Diagramming, and Event Management.


  The Cvent catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cvent''s developer surface includes authentication, API reference, changelog, support, pricing, training material, engineering blog, and 48 more developer resources.'
plans:
- name: Cvent Plans Pricing
  plan_count: 2
  slug: cvent-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 7
  name: Cvent Rate Limits
  slug: cvent-rate-limits
rules:
- authorship: generated
  effective_rule_count: 118
  extends:
  - spectral:oas
  name: Cvent API Rules
  rule_count: 77
  severity_counts:
    error: 47
    hint: 0
    info: 5
    warn: 25
  slug: cvent-rules
scopes:
- name: Cvent Scopes
  scope_count: 238
  slug: cvent-scopes
  summary_line: 238 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 76.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 56.5
    catalog_earned_first_party: 20.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 62.9
    developer_ergonomics: 73.2
    discoverability: 64.3
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
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
screenshot: https://apis.io/screenshots/cvent/cvent-2026-06-20T175359.png
security:
- kind: authentication
  name: Cvent Authentication
  slug: cvent-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Domain Security
  slug: cvent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cvent Vulnerability Disclosure
  slug: cvent-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cvent Trust Center
  slug: cvent-trust-center
  summary_line: ISO 27001, ISO 27701, SOC 1 Type II, SOC 2 Type II, PCI DSS Level 1, CSA STAR, TX-RAMP
skill_count: 6
skills:
- name: cvent-authenticate-and-check-quota
  slug: cvent-authenticate-and-check-quota
- name: cvent-build-event-agenda
  slug: cvent-build-event-agenda
- name: cvent-bulk-load-data
  slug: cvent-bulk-load-data
- name: cvent-manage-event-registration
  slug: cvent-manage-event-registration
- name: cvent-provision-users-scim
  slug: cvent-provision-users-scim
- name: cvent-sync-contacts
  slug: cvent-sync-contacts
slug: cvent
tags:
- Attendee Hub
- Attendee Management
- Conferences
- Diagramming
- Event Management
- Event Marketing
- Event
- Exhibitors
- Hospitality
- Hospitality Cloud
- Hybrid Events
- Meetings
- OAuth
- Passkeys
- Registration
- REST API
- SOAP API
- SSO
- Supplier Network
- Surveys
- Venue Management
- Venue Sourcing
- Virtual Events
- Webhook
- White Label
- Identity Federation
- Authentication
website: https://www.cvent.com/
---
