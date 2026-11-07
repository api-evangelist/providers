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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 59
apis:
- description: Provides information of Sales activities related to Accounts, Contacts, and Blocks for the selected Property. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OP
  name: OPERA Cloud RnA Activities GraphQL API
  slug: opera-cloud-rna-activities
- description: Detailed Accounts Receivable data, including Adjustments, Payments, Invoices and Posting for AR Accounts, with linked reservation data. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only Grap
  name: OPERA Cloud RnA ARAccountsReceivable GraphQL API
  slug: opera-cloud-rna-ar-accounts-receivable
- description: Detailed information on accounts receivable transactions including aging bucket of invoices, open transaction amounts, folio information and the account details. Compatible with OPERA Cloud RnA releas
  name: OPERA Cloud RnA ARAgingReport GraphQL API
  slug: opera-cloud-rna-ar-aging-report
- description: Ledger details showing activity in accounts receivables including reservation and transaction details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Clo
  name: OPERA Cloud RnA ARLedger GraphQL API
  slug: opera-cloud-rna-ar-ledger
- description: 'Provide booking reservation information with extended or additional details such as blocks, routing, etc. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA '
  name: OPERA Cloud RnA BookingReservationExtended GraphQL API
  slug: opera-cloud-rna-booking-reservation-extended
- description: Detailed information on blocks and any changes to the number of rooms or revenue, by stay date, property and Block Owner. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject ar
  name: OPERA Cloud RnA BookingsBlockProductionChanges GraphQL API
  slug: opera-cloud-rna-bookings-block-production-changes
- description: Detailed information on the status changes throughout the production period of a block, including the new and old status codes, rooms and associated revenues, by property and Block Owner. Compatible w
  name: OPERA Cloud RnA BookingsBlockStatusChanges GraphQL API
  slug: opera-cloud-rna-bookings-block-status-changes
- description: Block header and grid details, including actual and potential room and revenue statistics, catering events, and the associated profile and reservations data. Compatible with OPERA Cloud RnA release 26
  name: OPERA Cloud RnA BookingsBlock GraphQL API
  slug: opera-cloud-rna-bookings-block
- description: Detailed information on reservations booked in the past and future, including market code, rate code, reservation status, guest information and associated room and revenue details. Compatible with OPE
  name: OPERA Cloud RnA BookingsReservation GraphQL API
  slug: opera-cloud-rna-bookings-reservation
- description: Event revenue forecast details for defined periods broken down by Event Type, Revenue Group and Revenue Type. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OP
  name: OPERA Cloud RnA CateringEventForecast GraphQL API
  slug: opera-cloud-rna-catering-event-forecast
- description: Event posting details including revenues by property, Block, Event and Revenue groups. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & A
  name: OPERA Cloud RnA CateringEventPostings GraphQL API
  slug: opera-cloud-rna-catering-event-postings
- description: Detailed information on the status changes throughout the production period of an event, including the new and old status codes, change date, revenue and attendees. Compatible with OPERA Cloud RnA rel
  name: OPERA Cloud RnA CateringEventStatusChanges GraphQL API
  slug: opera-cloud-rna-catering-event-status-changes
- description: Event type definitions. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <gateway URL>/rna/v1/graph
  name: OPERA Cloud RnA CateringEventTypes GraphQL API
  slug: opera-cloud-rna-catering-event-types
- description: 'Event and Block details including group profile information, menu, packages and revenues broken down by event type. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in '
  name: OPERA Cloud RnA CateringEventsAndResources GraphQL API
  slug: opera-cloud-rna-catering-events-and-resources
- description: 'Provides detailed information on actions and the users who completed the action, including date, time, activity type, and description. Also providing the capability to combine with reservation, block '
  name: OPERA Cloud RnA ChangesLog GraphQL API
  slug: opera-cloud-rna-changes-log
- description: 'The Chain Configuration Subject Area contains configuration/setting attributes from components such as Enterprise Administration, Financial Administration, Booking Administration and Client Relations '
  name: OPERA Cloud RnA ConfigurationChain GraphQL API
  slug: opera-cloud-rna-configuration-chain
- description: The Resort Configuration Subject Area contains configuration/setting attributes from components such as Enterprise Administration, Financial Administration, Booking Administration and Client Relations
  name: OPERA Cloud RnA ConfigurationResort GraphQL API
  slug: opera-cloud-rna-configuration-resort
- description: This subject area contains data for billing folio settlements to be used for exporting to an external system for efolios. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject ar
  name: OPERA Cloud RnA EFolio GraphQL API
  slug: opera-cloud-rna-e-folio
- description: Provides detailed information of all configured external codes/values (i.e. general ledger codes) mapped to codes used in OPERA (i.e transaction codes, market codes). It contains a comprehensive set o
  name: OPERA Cloud RnA ExportMappings GraphQL API
  slug: opera-cloud-rna-export-mappings
- description: Detailed information on the commissions module, including Reservation and Travel Agent profile information, with commission codes, amounts, payment activity and processing status. Commission informati
  name: OPERA Cloud RnA FinancialCommissions GraphQL API
  slug: opera-cloud-rna-financial-commissions
- description: Deposit ledger details including individual transactions, folio information, calendar and financial period and the reservation details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only Grap
  name: OPERA Cloud RnA FinancialDepositLedger GraphQL API
  slug: opera-cloud-rna-financial-deposit-ledger
- description: Guest ledger details including individual reservations, posted transaction details with debit and credit amounts. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in th
  name: OPERA Cloud RnA FinancialGuestLedger GraphQL API
  slug: opera-cloud-rna-financial-guest-ledger
- description: Transaction code header details including flags, group, and sub-group details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics
  name: OPERA Cloud RnA FinancialTransactionCodes GraphQL API
  slug: opera-cloud-rna-financial-transaction-codes
- description: Provide financial transaction information with extended or additional details such as routing, cashiers, currency, etc. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area
  name: OPERA Cloud RnA FinancialTransactionDetailsExtended GraphQL API
  slug: opera-cloud-rna-financial-transaction-details-extended
- description: Detailed information on all posted transactions including net and gross amounts, currency, calendar and financial period, market and rate code. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-o
  name: OPERA Cloud RnA FinancialTransactionDetails GraphQL API
  slug: opera-cloud-rna-financial-transaction-details
- description: Summarized information on posted transactions including transaction group, sub group and codes, broken down by property and business date. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only G
  name: OPERA Cloud RnA FinancialTransactionsSummary GraphQL API
  slug: opera-cloud-rna-financial-transactions-summary
- description: Exchange Configurations data including External Systems, External Databases, Business Events, Interface Setup, Interface Controls and Interface Mappings. Compatible with OPERA Cloud RnA release 26.1.0
  name: OPERA Cloud RnA IntegrationConfigurations GraphQL API
  slug: opera-cloud-rna-integration-configurations
- description: 'All Function Space Details and Configured Options Including Room Type, Occupancy, Function Type, Room Setup, Notes and Physical Dimensions. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only '
  name: OPERA Cloud RnA InventoryFunctionSpaces GraphQL API
  slug: opera-cloud-rna-inventory-function-spaces
- description: Details on Tasks, Task Sheets and Credits and providing Information on Rooms, Room Attributes and Statuses for the current date. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL sub
  name: OPERA Cloud RnA InventoryHousekeepingManagementRoom GraphQL API
  slug: opera-cloud-rna-inventory-housekeeping-management-room
- description: Details on Tasks, Task Sheets and Credits for the current date. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data API
  name: OPERA Cloud RnA InventoryHousekeepingManagementTaskSheet GraphQL API
  slug: opera-cloud-rna-inventory-housekeeping-management-task-sheet
- description: Provides detailed information on room maintenance and out of order/service assignments broken down by property, time and room dimensions. Also provides reservations and profile details for service req
  name: OPERA Cloud RnA InventoryRoomsManagement GraphQL API
  slug: opera-cloud-rna-inventory-rooms-management
- description: 'Comprehensive Information on Guest Room Details and Configuration. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data '
  name: OPERA Cloud RnA InventoryRooms GraphQL API
  slug: opera-cloud-rna-inventory-rooms
- description: The Profiles-Accounts subject area contains Account Room Night and Revenue statistics broken down between Group and Individual stays and can be summarized by Property, Stay Date, Business Segment, Own
  name: OPERA Cloud RnA ProfilesAccounts GraphQL API
  slug: opera-cloud-rna-profiles-accounts
- description: All associated addresses including primary and secondary addresses, and address types which can be associated with the proper profile and profile type. Compatible with OPERA Cloud RnA release 26.1.0.0
  name: OPERA Cloud RnA ProfilesAddresses GraphQL API
  slug: opera-cloud-rna-profiles-addresses
- description: All associated communication details including communication types and roles, which can be associated with the proper profile and profile type. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-o
  name: OPERA Cloud RnA ProfilesCommunications GraphQL API
  slug: opera-cloud-rna-profiles-communications
- description: The Contacts subject area contains Room Night and Revenue statistics broken down between booked and stays reservations and can be summarized by Property, Stay Date, Business Segment and Owner. Compati
  name: OPERA Cloud RnA ProfilesContacts GraphQL API
  slug: opera-cloud-rna-profiles-contacts
- description: 'Guest profile data including contact information, VIP codes, memberships and stay statistics with room and revenue details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject '
  name: OPERA Cloud RnA ProfilesIndividuals GraphQL API
  slug: opera-cloud-rna-profiles-individuals
- description: Detailed information on the Loyalty Program providing details on the Membership, Profiles, Stay Information and the ability to track Claims. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only
  name: OPERA Cloud RnA ProfilesLoyaltyClaims GraphQL API
  slug: opera-cloud-rna-profiles-loyalty-claims
- description: Detailed information on the Loyalty Program providing details on the Membership, Profiles, Stay Information and the ability to track Awards. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only
  name: OPERA Cloud RnA ProfilesLoyaltyTransactions GraphQL API
  slug: opera-cloud-rna-profiles-loyalty-transactions
- description: Detailed information on the Loyalty Program providing details on the Membership, Profiles, Stay Information and the ability to track Awards and Claims. Compatible with OPERA Cloud RnA release 26.1.0.0
  name: OPERA Cloud RnA ProfilesLoyalty GraphQL API
  slug: opera-cloud-rna-profiles-loyalty
- description: Provides information on Stay Records statistics of guest stay and its respective Membership Transactions details for a profile. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subj
  name: OPERA Cloud RnA ProfilesMembershipTransactions GraphQL API
  slug: opera-cloud-rna-profiles-membership-transactions
- description: Profile note types and note details, including internal and confidential flags, and the profile details they are associated with. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL su
  name: OPERA Cloud RnA ProfilesNotes GraphQL API
  slug: opera-cloud-rna-profiles-notes
- description: Relationship type definition. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <gateway URL>/rna/v1
  name: OPERA Cloud RnA ProfilesRelationshipTypes GraphQL API
  slug: opera-cloud-rna-profiles-relationship-types
- description: 'The Profile - Relationships subject area contains relationship details including the relationship type, description and role and the profiles that are linked through the relationship. Compatible with '
  name: OPERA Cloud RnA ProfilesRelationships GraphQL API
  slug: opera-cloud-rna-profiles-relationships
- description: Provides information on Stay Records statistics of guest stay and its respective Membership Transactions details for a profile. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subj
  name: OPERA Cloud RnA ProfilesStayRecords GraphQL API
  slug: opera-cloud-rna-profiles-stay-records
- description: Promotion Coupon Codes details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <gateway URL>/rna/
  name: OPERA Cloud RnA PromotionCouponCodes GraphQL API
  slug: opera-cloud-rna-promotion-coupon-codes
- description: Property definition with marketing, financial, and housekeeping details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA)
  name: OPERA Cloud RnA Property GraphQL API
  slug: opera-cloud-rna-property
- description: Rate bucket definition. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <gateway URL>/rna/v1/graph
  name: OPERA Cloud RnA RatesBuckets GraphQL API
  slug: opera-cloud-rna-rates-buckets
- description: Rate category definition including begin and end date and rate class association. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analyt
  name: OPERA Cloud RnA RatesCategories GraphQL API
  slug: opera-cloud-rna-rates-categories
- description: Rate class definition with begin and end date. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <ga
  name: OPERA Cloud RnA RatesClasses GraphQL API
  slug: opera-cloud-rna-rates-classes
- description: Rate Header information including room types, package elements, market and source code and associated flags. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPE
  name: OPERA Cloud RnA RatesCodeDetails GraphQL API
  slug: opera-cloud-rna-rates-code-details
- description: 'Rate detail information including all rate header details, room type, rate tiers and rate amounts per occupant. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the '
  name: OPERA Cloud RnA RatesCodes GraphQL API
  slug: opera-cloud-rna-rates-codes
- description: 'Deposit and cancellation rules schedules and details by date, rate code and days prior to arrival or after booking. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in '
  name: OPERA Cloud RnA RatesDepositAndCancellationRules GraphQL API
  slug: opera-cloud-rna-rates-deposit-and-cancellation-rules
- description: Rate yielding and hurdle information including date, amount , length of stay and room type. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reportin
  name: OPERA Cloud RnA RatesHurdles GraphQL API
  slug: opera-cloud-rna-rates-hurdles
- description: Rate yielding and hurdle information including date, amount , length of stay and room type. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reportin
  name: OPERA Cloud RnA RatesRateSeasons GraphQL API
  slug: opera-cloud-rna-rates-rate-seasons
- description: Rate restriction definition including restriction type, date applied, room and rate code with day of the week and length of the stay details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-onl
  name: OPERA Cloud RnA RatesRestrictions GraphQL API
  slug: opera-cloud-rna-rates-restrictions
- description: 'Rate tier definition by length of stays. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <gateway '
  name: OPERA Cloud RnA RatesTiers GraphQL API
  slug: opera-cloud-rna-rates-tiers
- description: This Subject Area Contains the Budget Forecast Details of the Property(s). Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (Rn
  name: OPERA Cloud RnA ResortBudgetForecast GraphQL API
  slug: opera-cloud-rna-resort-budget-forecast
- description: Details on fixed charges including amount, frequency, and transaction code and the linked reservations. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cl
  name: OPERA Cloud RnA RevenueFixedCharges GraphQL API
  slug: opera-cloud-rna-revenue-fixed-charges
- description: Revenue group and type details. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the OPERA Cloud Reporting & Analytics (RnA) Data APIs, exposed at <gateway URL>/rna/
  name: OPERA Cloud RnA RevenueGroupsAndTypes GraphQL API
  slug: opera-cloud-rna-revenue-groups-and-types
- description: Package header details including package group setup and associated flags for selling and consumption options. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject area in the O
  name: OPERA Cloud RnA RevenuePackages GraphQL API
  slug: opera-cloud-rna-revenue-packages
- description: The Sales Manager Goals subject Area enable the end users to retrieve information / create reports to compare the goals set for the Sales Managers against completed activities, and against statistical
  name: OPERA Cloud RnA SalesManagerGoals GraphQL API
  slug: opera-cloud-rna-sales-manager-goals
- description: The Simple Report Activities Subject Area simplifies creating and building adhoc reports, including the ability to create new reports. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only Graph
  name: OPERA Cloud RnA SimpleReportsActivities GraphQL API
  slug: opera-cloud-rna-simple-reports-activities
- description: 'The Simple Reports Booking Blocks Subject Area simplifies creating and building adhoc reports, including the ability to create new reports. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only '
  name: OPERA Cloud RnA SimpleReportsBookingBlocks GraphQL API
  slug: opera-cloud-rna-simple-reports-booking-blocks
- description: The Simple Reports Bookings Reservation Subject Area simplifies creating and building adhoc reports, including the ability to create new reports. Compatible with OPERA Cloud RnA release 26.1.0.0. Read
  name: OPERA Cloud RnA SimpleReportsBookingsReservation GraphQL API
  slug: opera-cloud-rna-simple-reports-bookings-reservation
- description: 'The Simple Reports Events Subject Area simplifies creating and building adhoc reports, including the ability to create new reports. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL '
  name: OPERA Cloud RnA SimpleReportsEvents GraphQL API
  slug: opera-cloud-rna-simple-reports-events
- description: The Simple Reports Financial Transactions Subject Area simplifies creating and building adhoc reports, including the ability to create new reports. Compatible with OPERA Cloud RnA release 26.1.0.0. Re
  name: OPERA Cloud RnA SimpleReportsFinancialTransactions GraphQL API
  slug: opera-cloud-rna-simple-reports-financial-transactions
- description: The Simple Reports Profile-Individuals Subject Area simplifies creating and building adhoc reports, including the ability to create new reports. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-
  name: OPERA Cloud RnA SimpleReportsProfileIndividuals GraphQL API
  slug: opera-cloud-rna-simple-reports-profile-individuals
- description: Future on the books information including rooms, revenue and persons with breakdowns by room types, market code, source code and periods of time. Compatible with OPERA Cloud RnA release 26.1.0.0. Read
  name: OPERA Cloud RnA StatisticsForecastSummary GraphQL API
  slug: opera-cloud-rna-statistics-forecast-summary
- description: Detailed information on past and future reservations including occupancy and revenue figures with all profile data, broken down by Market, Rate code, Room type and Periods of time. Compatible with OPE
  name: OPERA Cloud RnA StatisticsHistoryAndForecast GraphQL API
  slug: opera-cloud-rna-statistics-history-and-forecast
- description: Past statistics including rooms and revenue figures, arrivals, departures and occupancy broken out by multiple time periods. Compatible with OPERA Cloud RnA release 26.1.0.0. Read-only GraphQL subject
  name: OPERA Cloud RnA StatisticsManagersReport GraphQL API
  slug: opera-cloud-rna-statistics-managers-report
- description: The Reservation Pace subject area contains daily rooms and revenue information on reservations on the books as of specific dates in the past (snapshot dates) summarized by Property, PACERATECODE, Room
  name: OPERA Cloud RnA StatisticsReservationPace GraphQL API
  slug: opera-cloud-rna-statistics-reservation-pace
- description: Summarized information on past reservations including number of persons, rooms and revenue figures, broken down by room type, market code, rate code and periods of time. Compatible with OPERA Cloud Rn
  name: OPERA Cloud RnA StatisticsReservationsDailySummary GraphQL API
  slug: opera-cloud-rna-statistics-reservations-daily-summary
- description: Detailed information on past reservations including occupancy and revenue figures with all profile data, broken down by Market, Rate code, room type and periods of time. Compatible with OPERA Cloud Rn
  name: OPERA Cloud RnA StatisticsReservationsDaily GraphQL API
  slug: opera-cloud-rna-statistics-reservations-daily
- description: Summarized booking data for both on the books and past stays including rooms, revenue and occupancy details broken out by Market Code, Rate code and periods of time. Compatible with OPERA Cloud RnA re
  name: OPERA Cloud RnA StatisticsReservationsSummary GraphQL API
  slug: opera-cloud-rna-statistics-reservations-summary
- description: Push delivery of OPERA Cloud Business Events as a GraphQL subscription over WebSocket. Each event carries the resource that changed, the event name, the old value and the new value. Subscription is pe
  name: OPERA Cloud Business Events Streaming API
  slug: opera-cloud-business-events-streaming
- baseURL: /ars/v1
  baseurl_source: spec
  description: The REST API's will allow you to create, manage, or delete accounts, add comments, traces, reminders, create or close invoices for example.
  name: Oracle Hospitality Accounts Receivables API
  phrasing_intents:
  - id: getReminders
    intent: Get reminder letters for AR accounts
    question: Where can I see the payment reminder letters sent to our accounts receivable holders?
  - id: postReminders
    intent: Generate AR payment reminder letters
    question: How do I generate a payment reminder letter for an accounts receivable holder in OPERA Cloud?
  - id: getAccounts
    intent: Find AR accounts for a profile
    question: Which accounts receivable accounts are attached to a given guest or company profile?
  - id: getRemindersHistory
    intent: Get reminder letter history for an AR account
    question: What reminder letters have already been sent to a particular AR account, and when?
  - id: getStatements
    intent: Get statements for one AR account (deprecated)
    question: How did the older per-account statements endpoint return billing statements for one AR account?
  - id: getARTransactions
    intent: List AR transactions for hotels
    question: How can I pull accounts receivable transactions for a set of hotels over a date range?
  - id: searchARTransactions
    intent: Search AR transactions with a request body
    question: Can I post a search body to find AR transactions instead of putting filters in the URL?
  - id: postAccount
    intent: Create an AR account for a profile
    question: How do I open a new accounts receivable account for a company profile at a hotel?
  phrasing_ops: 60
  slug: oracle-hospitality-accountsreceivables-api
- baseURL: /fof/config/v1
  baseurl_source: spec
  description: The Accounts Receivables Config module offers the capability of creating, managing, and retrieving of Accounts Receivables configuration.
  name: Oracle Hospitality Accounts Receivables Config API
  phrasing_intents:
  - id: putARAccountTypes
    intent: Modify existing AR account types
    question: How do I edit the description of an accounts receivable account type I already set up?
  - id: postARAccountTypes
    intent: Create new AR account types
    question: How do I add a brand-new accounts receivable account type for a property?
  - id: deleteARAccountTypes
    intent: Remove AR account types from a hotel
    question: How do I delete accounts receivable account types that a hotel no longer uses?
  - id: getARFlaggedReasons
    intent: List AR flagged reasons
    question: Which reasons can an AR account be flagged for?
  - id: putARFlaggedReasons
    intent: Change existing AR flagged reasons
    question: How do I reword an accounts receivable flagged reason that already exists?
  - id: postARFlaggedReasons
    intent: Create AR flagged reasons
    question: How do I add a new reason code for flagging an AR account?
  - id: deleteARFlaggedReasons
    intent: Remove AR flagged reasons
    question: How do I delete AR flagged reason codes we no longer use?
  - id: getARAccountTypes
    intent: List a hotel's AR account types
    question: Which accounts receivable account types are set up at my hotel?
  phrasing_ops: 10
  slug: oracle-hospitality-accountsreceivablesconfig-api
- baseURL: /act/v1
  baseurl_source: spec
  description: The Activity REST APIs allow you to view, create, update, and complete an Activity in OPERA Cloud. You are also able to perform more actions such as add attachments.
  name: Oracle Hospitality Activity API
  phrasing_intents:
  - id: getActivitiesByMultipleHotelIds
    intent: Search activities across several hotels
    question: What sales activities are open across all the hotels in my portfolio?
  - id: deleteMultipleActivities
    intent: Delete several activities by their IDs
    question: Can I delete a whole list of activities in one call?
  - id: putBulkActivities
    intent: Bulk update many activities at once
    question: Can I update a batch of activities in one request instead of one by one?
  - id: postMultipleActivitiesCompletion
    intent: Mark several activities as completed
    question: How do I close out a batch of finished activities in one request?
  - id: getEmails
    intent: Retrieve stored emails for accounts and contacts
    question: Which emails from our external mail system are stored against a sales account in OPERA?
  - id: searchEmails
    intent: Search stored emails by posting search criteria
    question: Is there a POST search for stored emails when my criteria are too long for a query string?
  - id: getActivityWithOutHotelId
    intent: Get an activity by ID without naming a hotel
    question: Can I look up an activity by its OPERA ID when I don't know which hotel it belongs to?
  - id: deleteActivitiesWithOutHotelId
    intent: Delete an activity by ID without naming a hotel
    question: Can I mark an activity deleted using only its ID, no hotel code?
  phrasing_ops: 23
  slug: oracle-hospitality-activity-api
- baseURL: /act/config/v1
  baseurl_source: spec
  description: The Activity Configuration APIs offers capability of creating, managing, and retrieving Activity configuration elements, such as Activity Type code, Activity Result codes.
  name: Oracle Hospitality Activity Management API
  phrasing_intents:
  - id: getActivityResultsConfig
    intent: List configured activity result codes
    question: Which activity result codes, like SUCCESS or CALLAGAIN, are set up in OPERA Cloud?
  - id: postActivityResultsConfig
    intent: Create an activity result code
    question: How do I add a new result code that sales staff pick when completing an activity?
  - id: deleteActivityResultsConfig
    intent: Delete an activity result code
    question: How do I remove an activity result code from OPERA Cloud?
  - id: putActivityResultsConfig
    intent: Update an activity result code
    question: How do I change the description of an existing activity result code?
  - id: getAutoTraceCodes
    intent: List auto trace codes
    question: What auto trace codes are configured for our property?
  - id: postAutoTraceCodes
    intent: Create an auto trace code
    question: How do I add a new auto trace code?
  - id: deleteAutoTraceCodes
    intent: Delete an auto trace code
    question: How do I remove an auto trace code we no longer need?
  - id: putAutoTraceCodes
    intent: Update an auto trace code
    question: How do I edit an auto trace code that already exists?
  phrasing_ops: 25
  slug: oracle-hospitality-activitymanagement-api
- baseURL: https://oracle.api.com/ohcgep/v1
  baseurl_source: spec
  description: The API to Fulfill Upsell Offers to customers and third parties API from Oracle Hospitality — 1 operation(s) for api to fulfill upsell offers to customers and third parties.
  name: Oracle Hospitality API to Fulfill Upsell Offers to customers and third parties API
  phrasing_intents:
  - id: postUpsellOffers
    intent: Apply a selected upsell offer to a reservation
    question: How do I add a room upgrade a guest accepted to their reservation?
  phrasing_ops: 1
  slug: oracle-hospitality-api-to-fulfill-upsell-offers-to-customers-and-third-parties-api
- baseURL: /aripublication/v1
  baseurl_source: spec
  description: The ARI Publication service provides ability to send distribution partners with hotel property inventory level, room rates, and restrictions.
  name: Oracle Hospitality ARI Publication API
  phrasing_intents:
  - id: postInventory
    intent: Publish room type inventory to distribution
    question: How do I push rooms-to-sell by date and room type out to distribution channels?
  - id: postRates
    intent: Publish rate plan rates to distribution
    question: How do I publish rate plan prices by date and room type to channels?
  - id: postRestrictions
    intent: Publish rate restrictions to distribution
    question: How do I send stay restrictions like closed-to-arrival for a rate plan and room type?
  phrasing_ops: 3
  slug: oracle-hospitality-ari-publication-api
- baseURL: /hdpba/oauth2/v1
  baseurl_source: spec
  description: Authentication service
  name: Oracle Hospitality Authentication API
  phrasing_intents:
  - id: getToken
    intent: Get a token for the OPERA Cloud Distribution APIs
    question: How do I get an access token for the OPERA Cloud Distribution REST APIs with my username and password?
  - id: postTokens
    intent: Get an OAuth token for OPERA Cloud REST APIs
    question: How do I obtain an OAuth access token for the Oracle Hospitality OPERA Cloud REST APIs?
  phrasing_ops: 2
  slug: oracle-hospitality-authentication-api
- baseURL: /chl/v1
  baseurl_source: spec
  description: The Availability APIs allow you to manage a properties room-rate availability, which is configured for a channel. This also includes operations to manage restrictions and hurdles.
  name: Oracle Hospitality Availability API
  phrasing_intents:
  - id: getRegionalRateParity
    intent: Compare rate parity across hotels in a region
    question: Are my rates consistent across channels for all hotels in a chain or region?
  - id: getChannelInventorySnapshotByRoomType
    intent: Get channel inventory snapshot for one room type
    question: What availability and restrictions does a booking channel see for one specific room type?
  - id: getGeneralAvailabilitySimulator
    intent: Simulate what a booking channel would see
    question: How can I preview the availability and rates a channel would return for a sample stay?
  - id: getChannelInventorySnapshot
    intent: Get a hotel's channel inventory snapshot
    question: What rooms and restrictions are all my booking channels seeing for a hotel right now?
  - id: getRateParity
    intent: Check a hotel's channel rate parity
    question: Is my hotel's rate the same on every booking channel?
  - id: getHotelAvailabilityCRO
    intent: Check availability across multiple hotels
    question: Which of my hotels have rooms available for given dates and party size?
  - id: searchHotelAvailabilityCRO
    intent: Search multi-hotel availability with a POST body
    question: Can I send multi-hotel availability criteria in a POST request body instead of a long query string?
  - id: getHotels
    intent: Search hotels for the sales process
    question: Which hotels in a city can I offer a guest for their dates?
  phrasing_ops: 34
  slug: oracle-hospitality-availability-api
- baseURL: /par/async/v1
  baseurl_source: spec
  description: The Availability Asynchronous module provides capability for an external system to retrieve availability related data using an asynchronous approach.
  name: Oracle Hospitality Availability Async API
  phrasing_intents:
  - id: postRestrictionsProcess
    intent: Send restrictions to OPERA Cloud asynchronously
    question: How do I push a batch of rate and inventory restrictions into OPERA Cloud from my external system?
  - id: getRestrictionsProcessStatus
    intent: Check if a restrictions request has finished
    question: Is there a lightweight HEAD check to see whether my restrictions request is done processing?
  - id: getRestrictions
    intent: Get the processing result of submitted restrictions
    question: What happened to the restrictions request I sent to OPERA — was it processed and what came back?
  phrasing_ops: 3
  slug: oracle-hospitality-availabilityasync-api
- baseURL: /par/v1
  baseurl_source: spec
  description: The AvailabilityExternal API from Oracle Hospitality — 2 operation(s) for availabilityexternal.
  name: Oracle Hospitality Availability External API
  phrasing_intents:
  - id: retriveExternalControlSegment
    intent: Look up a control segment in an external system
    question: How can OPERA look up a control segment held in an external revenue system?
  - id: getExternalYieldMarketType
    intent: Look up a yield market type in an external system
    question: Which yield market type does the external system assign to a hotel?
  phrasing_ops: 2
  slug: oracle-hospitality-availabilityexternal-api
- baseURL: /bof/v1
  baseurl_source: spec
  description: This module provides APIs to service Back Office operations for property, such as managing end-of-day, getting the properties current business date, and perform cashier closure.
  name: Oracle Hospitality Back Office Operations API
  phrasing_intents:
  - id: getBusinessDate
    intent: Get a hotel's current business date
    question: What business date is my hotel currently on after end of day?
  - id: pingBackOfficeOperationsService
    intent: Check the back office operations service status
    question: Is the OPERA Cloud back office operations service up?
  phrasing_ops: 2
  slug: oracle-hospitality-backofficeoperations-api
- baseURL: /int/config/v1
  baseurl_source: spec
  description: The BEProcessor Service offers capability of creating, managing, and retrieving of BE Processor configuration.
  name: Oracle Hospitality BE Processor API
  phrasing_intents:
  - id: pingBeProcessor
    intent: Check the business event processor status
    question: Is the OXI business event processor service up?
  phrasing_ops: 1
  slug: oracle-hospitality-beprocessor-api
- baseURL: /blk/v1
  baseurl_source: spec
  description: These APIs will allow you to completely create and manage your block in OPERA Cloud - including all related functionalities of a block such as manage Room allocation, Status update, block reservations
  name: Oracle Hospitality Block API
  phrasing_intents:
  - id: postSubAllocation
    intent: Create a sub allocation under a master allocation
    question: How do I carve a sub allocation out of a master allocation in OPERA Cloud?
  - id: getBlockActivityLog
    intent: Read the block activity log
    question: Who changed what on our group blocks, and when?
  - id: putBlockAllocationWash
    intent: Wash room allocation from a block over dates
    question: How do I release unsold group rooms from a block for a range of dates?
  - id: getBlockWashInfo
    intent: Get block details needed for a block wash
    question: What block information do I need before washing unused rooms from a group block?
  - id: getBlocks
    intent: Find blocks with query filters
    question: How can I list all group blocks arriving in a given date range?
  - id: postBlockValidate
    intent: Validate a block and its rate code overlaps
    question: Does this block rate code overlap with other blocks before I save it?
  - id: getBlockDailyStatistics
    intent: Get block daily statistics for a date range
    question: What do group block statistics look like day by day at my hotel?
  - id: searchBlocks
    intent: Search blocks with criteria in a request body
    question: Can I send block search criteria as a POST body instead of query parameters?
  phrasing_ops: 90
  slug: oracle-hospitality-block-api
- baseURL: /blk/async/v1
  baseurl_source: spec
  description: The Block Async Service Web Service provides capability to implement block related asynchronous operations in OPERA Cloud.
  name: Oracle Hospitality Block Async API
  phrasing_intents:
  - id: startBlockAllocationSummaryProcess
    intent: Request a hotel's block allocation summary
    question: How can I pull group block allocations, rates and room type stats for a date range?
  - id: getBlockAllocationSummaryProcessStatus
    intent: Check if a block allocation summary is ready
    question: Is my block allocation summary request finished processing?
  - id: getBlockAllocationSummary
    intent: Get a completed block allocation summary
    question: Where do I download the block allocation summary once the job is done?
  - id: startBlockAllocationProcess
    intent: Set room allocations and rates on a block
    question: How do I add room type allocations and rates to a group block?
  - id: getBlockAllocationProcessStatus
    intent: Check if a block allocation update finished
    question: Is my block room allocation job complete?
  - id: getBlockAllocationProcessInfo
    intent: Get results of a block allocation update
    question: Did setting allocations on my block trigger any overbooking warnings?
  - id: startAllocationRangesProcess
    intent: Set block allocations across date ranges
    question: How do I set a block's allocation for several date ranges and room types at once?
  - id: getAllocationRangesProcessStatus
    intent: Check if a block allocation ranges job finished
    question: Is the allocation ranges update on my block still running?
  phrasing_ops: 21
  slug: oracle-hospitality-blockasync-api
- baseURL: /blk/config/v1
  baseurl_source: spec
  description: The Block Configuration module offers capability of creating, managing, and retrieving of Block configuration.
  name: Oracle Hospitality Block Config API
  phrasing_intents:
  - id: getBlockStatusCodes
    intent: List block status codes
    question: What block status codes are configured for our chain?
  - id: postBlockStatusCode
    intent: Create a block status code
    question: How do I add a new block status such as Tentative Hold?
  - id: getNextBlockStatusCodes
    intent: Get allowed next statuses for a block status
    question: Which statuses can a block move to from its current status?
  - id: deleteBlockStatusCode
    intent: Delete a block status code
    question: How do I remove a block status we no longer use?
  - id: putBlockStatusCode
    intent: Change a block status code
    question: How do I edit the description or type of an existing block status?
  - id: putNextBlockStatusCodes
    intent: Set the next statuses for a block status
    question: How do I control which statuses a block can move to next?
  - id: setBlockCutoffScheduleRange
    intent: Set a cutoff schedule over a date range
    question: Can I apply cutoff days to blocks across a whole date range?
  - id: getBlockSalesAllowance
    intent: Get block sales allowance
    question: How many rooms are we allowed to sell to groups on each night?
  phrasing_ops: 32
  slug: oracle-hospitality-blockconfig-api
- baseURL: /blk/v1
  baseurl_source: spec
  description: The Block External module provides operations for OPERA Cloud to access blocks from an external interfaces. It also offers capability for downloading external blocks into OPERA Cloud.
  name: Oracle Hospitality Block External API
  phrasing_intents:
  - id: pingBlockExternalServiceStatus
    intent: Check the external block service status
    question: Is the block external service up?
  phrasing_ops: 1
  slug: oracle-hospitality-blockexternal-api
- baseURL: /blk/v1
  baseurl_source: spec
  description: Block Statistics provide statistical data of blocks that exist in OPERA Cloud.
  name: Oracle Hospitality Block Stats API
  phrasing_intents:
  - id: getBlockStats
    intent: Get group block statistics
    question: How are our group blocks performing over the next quarter?
  - id: pingBlockStatsService
    intent: Check the block stats service status
    question: Is the block statistics service up?
  phrasing_ops: 2
  slug: oracle-hospitality-blockstats-api
- baseURL: /csh/v1
  baseurl_source: spec
  description: 'Cashiering module provides APIs to service front desk billing requirements, as well as any requirements related to a reservation''s folio. You can retrieve a guest folio, post billing charges to guest '
  name: Oracle Hospitality Cashiering API
  phrasing_intents:
  - id: getCompRedemptions
    intent: List comp redemptions for a PTS member
    question: What complimentary redemptions can a guest with a PTS membership use?
  - id: authorizeCompRedemptions
    intent: Authorize comp redemptions for a PTS member
    question: How do I get complimentary redemptions approved for a PTS member before posting them?
  - id: postCompRedemptions
    intent: Post comp redemptions against a membership
    question: How can I post a complimentary redemption directly against a guest's PTS membership number?
  - id: reverseCompRedemptions
    intent: Reverse comp redemptions on a membership
    question: How do I undo a complimentary redemption that was posted to a player's membership?
  - id: asyncApproveCompPostings
    intent: Submit bulk comp postings for vendor approval
    question: Can I send a large batch of comp postings to the vendor for approval asynchronously?
  - id: approveCompPostings
    intent: Request approval of comp postings
    question: How do I request approval for comp postings right away rather than in bulk?
  - id: reverseCompPostings
    intent: Request reversal of comp postings
    question: How can I reverse comp postings that were already approved?
  - id: getCashierReportPostings
    intent: Get postings for a cashier report
    question: Which postings make up a cashier report for a given date range?
  phrasing_ops: 203
  slug: oracle-hospitality-cashiering-api
- baseURL: /csh/async/v1
  baseurl_source: spec
  description: The CashieringAsync API from Oracle Hospitality — 2 operation(s) for cashieringasync.
  name: Oracle Hospitality Cashiering Async API
  phrasing_intents:
  - id: startFinancialPostingsAsync
    intent: Start a net and VAT financial postings request
    question: How do I get financial postings with a net and VAT breakdown for my hotel?
  - id: getFinancialPostingsProcessStatusAsync
    intent: Check if a financial postings request is ready
    question: Is my net and VAT postings request finished yet?
  phrasing_ops: 2
  slug: oracle-hospitality-cashieringasync-api
- baseURL: /fof/config/v1
  baseurl_source: spec
  description: 'Cashiering configurations affect the control and management of financial transactions at your property. You can configure cashiering components for articles for sale, cancellation handling, deposits, '
  name: Oracle Hospitality Cashiering Config API
  phrasing_intents:
  - id: putArticles
    intent: Update existing articles for a hotel
    question: Can I change the price or description of an article that already exists?
  - id: postArticles
    intent: Create new articles under a transaction code
    question: How do I add new sellable articles, like chips or peanuts, under a minibar transaction code?
  - id: getArticles
    intent: Look up articles posted under transaction codes
    question: Which minibar items are set up as articles under a transaction code at my hotel?
  - id: deleteArticles
    intent: Delete articles from a hotel
    question: Can I remove an article that is no longer sold at the property?
  - id: putAuthorizationConfigRule
    intent: Update a credit card authorization rule
    question: Can I edit an existing credit card authorization rule for a rate code?
  - id: postAuthorizationConfigRule
    intent: Create a credit card authorization rule
    question: How do I set up a new authorization rule for a specific rate code or guarantee code?
  - id: deleteAuthorizationConfigRule
    intent: Delete a credit card authorization rule
    question: Can I delete the authorization rule tied to one rate code?
  - id: getAuthorizationConfigRules
    intent: List credit card authorization rules
    question: What credit card authorization rules does my hotel have configured?
  phrasing_ops: 270
  slug: oracle-hospitality-cashieringconfig-api
- baseURL: /blk/config/v1
  baseurl_source: spec
  description: The ChainConfigService Web Service offers capability of creating, managing, and retrieving of chain configuration.
  name: Oracle Hospitality Chain Config API
  phrasing_intents:
  - id: getBlockCancellationReasons
    intent: List block cancellation reasons
    question: What reasons can a sales manager pick from when a group block is cancelled in OPERA Cloud?
  - id: postBlockCancellationReasons
    intent: Create block cancellation reasons
    question: How do I add a new reason for cancelling a group block?
  - id: putBlockCancellationReasons
    intent: Update a block cancellation reason
    question: Can I rename or reword an existing block cancellation reason?
  - id: deleteBlockCancellationReasons
    intent: Delete a block cancellation reason
    question: Is it possible to remove a block cancellation reason we no longer use?
  - id: getBlockLostBookingCodes
    intent: List lost booking codes for blocks
    question: Which lost booking codes can I use to explain why we lost a group block?
  - id: postBlockLostBookingCodes
    intent: Create lost booking codes for blocks
    question: How do I add a new lost-business code for group blocks?
  - id: putBlockLostBookingCodes
    intent: Update a block lost booking code
    question: Can I edit the wording of an existing block lost booking code?
  - id: deleteBlockLostBookingCodes
    intent: Delete a block lost booking code
    question: Can I permanently delete a block lost booking code?
  phrasing_ops: 411
  slug: oracle-hospitality-chainconfig-api
- baseURL: /chl/v1
  baseurl_source: spec
  description: The Channel APIs allows you to view, configure and manage the mappings for your channel rate codes, negotiated rates, room types, global descriptions, letters, credit card types and channel codes.
  name: Oracle Hospitality Channel API
  phrasing_intents:
  - id: getChannels
    intent: List configured distribution channels
    question: Which booking channels are set up in OPERA Cloud for my property?
  - id: putChannels
    intent: Update existing channel configuration
    question: How do I change the settings of a booking channel that already exists?
  - id: postChannels
    intent: Add a new booking channel code
    question: How do I add a brand-new booking channel code to OPERA?
  - id: deleteChannelAccountContracts
    intent: Delete channel account contracts
    question: How do I remove a contract from a channel account?
  - id: copyChannelAccountContracts
    intent: Copy channel account contracts
    question: Can I duplicate an existing channel account contract instead of re-entering it?
  - id: getChannelAccounts
    intent: Search channel accounts
    question: Which channel accounts do we have on file in OPERA?
  - id: postChannelAccounts
    intent: Add new channel accounts
    question: How do I set up a new channel account?
  - id: putChannelAccounts
    intent: Update existing channel accounts
    question: How do I edit a channel account that already exists for an OPERA profile?
  phrasing_ops: 129
  slug: oracle-hospitality-channel-api
- baseURL: /fof/config/v1
  baseurl_source: spec
  description: These Commission APIs allow you to get, update, and remove commissions on an Account Receivable (AR) profile in OPERA Cloud.
  name: Oracle Hospitality Commission Config API
  phrasing_intents:
  - id: getCommissionCodes
    intent: List travel agent commission codes for hotels
    question: Which commission codes are configured for my hotels?
  - id: putCommissionCodes
    intent: Change existing commission codes
    question: How do I change the percentage or rules on an existing commission code?
  - id: postCommissionCodes
    intent: Create new commission codes
    question: How do I set up a new commission code for travel agents?
  - id: deleteCommissionCodes
    intent: Remove commission codes from hotels
    question: Can I delete a commission code we no longer pay out on?
  - id: getConfigBankAccounts
    intent: List bank accounts configured for commission payments
    question: Which bank accounts are set up to pay commissions from?
  - id: putConfigBankAccounts
    intent: Change existing commission bank accounts
    question: How do I update the details of a commission bank account that already exists?
  - id: deleteConfigBankAccounts
    intent: Remove a commission bank account
    question: Can I delete a bank account we closed from commission configuration?
  - id: postConfigBankAccounts
    intent: Create new commission bank accounts
    question: How do I add a new bank account for paying travel agent commissions?
  phrasing_ops: 15
  slug: oracle-hospitality-commissionconfig-api
- baseURL: /fof/v1
  baseurl_source: spec
  description: Commission web service provides commission processing service like payment processing, payment activity and search.
  name: Oracle Hospitality Commissions API
  phrasing_intents:
  - id: getBankAccounts
    intent: List commission bank accounts
    question: Which bank accounts does my hotel pay travel agent commissions from?
  - id: searchBankAccounts
    intent: Search commission bank accounts by criteria
    question: How do I search commission bank accounts by bank name with a POST body?
  - id: getReservationsForCommissions
    intent: List a travel agent's commissionable reservations
    question: Which reservations is a travel agent owed commission on?
  - id: searchReservationsForCommissions
    intent: Search a travel agent's commission reservations
    question: How do I search an agent's commission reservations by confirmation number in a request body?
  - id: changeCommissionCheck
    intent: Change a commission check
    question: How do I update a commission check issued from a bank account?
  - id: getCommissionPaymentsActivity
    intent: View commission payment activity for an account
    question: What commission payments have gone out from a bank account?
  - id: changeCommissionPaymentActivityByRange
    intent: Update commission payment activity by range
    question: How do I update a range of commission payment records at once?
  - id: reprintCommissionCheckByRange
    intent: Reprint a range of commission checks
    question: How do I reprint commission checks that failed to print?
  phrasing_ops: 23
  slug: oracle-hospitality-commissions-api
- baseURL: /content/v1
  baseurl_source: spec
  description: The Content API from Oracle Hospitality — 5 operation(s) for content.
  name: Oracle Hospitality Content API
  phrasing_intents:
  - id: getPropertiesSummary
    intent: List properties mapped to a distribution channel
    question: Which hotel properties are actively mapped to my distribution channel code?
  - id: getPropertyInfo
    intent: Get content details for one property
    question: How do I pull the descriptive content for a single hotel through my channel?
  - id: getRoomTypesInfo
    intent: List a property's room types
    question: What room types does a hotel offer to my channel?
  - id: getRatePlansInfo
    intent: List a property's rate plans
    question: Which rate plans can my channel sell at a given hotel?
  - id: getRateRooms
    intent: Map rate plans to room types for a property
    question: Which room types are sold under each rate plan at a hotel?
  phrasing_ops: 5
  slug: oracle-hospitality-content-api
- baseURL: /notification/v1
  baseurl_source: spec
  description: The Content Notification service provides ability to send distribution partners with hotel property inventory level, room rates, and restrictions.
  name: Oracle Hospitality Content Notification API
  phrasing_intents:
  - id: postContent
    intent: Send a property content notification to a channel
    question: How does a channel get notified when hotel property content changes?
  phrasing_ops: 1
  slug: oracle-hospitality-content-notification-api
- baseURL: /crm/async/v1
  baseurl_source: spec
  description: The CRM Async Web Service provides capability to implement stay records related asynchronous operations in OPERA Cloud.
  name: Oracle Hospitality CRM Async API
  phrasing_intents:
  - id: stayRecords
    intent: Upload stay records for loyalty processing
    question: How do I bulk upload guest stay records into OPERA Cloud CRM?
  - id: getStayRecordsProcessStatus
    intent: Check stay upload job status without a body
    question: Is there a lightweight HEAD check for whether a stay record upload job is done?
  - id: getStayRecordsProcess
    intent: Get the result of a stay record upload
    question: Has my stay record upload finished processing yet?
  - id: deleteSuspendedStays
    intent: Bulk delete suspended stay records
    question: How do I clear out suspended stay records that failed to import?
  - id: getSuspendedStaysDeleteStatus
    intent: Check suspended stay deletion job status
    question: Can I poll a HEAD status for the suspended stays delete job using the Location header id?
  - id: getSuspendedStaysDelete
    intent: Get the result of a suspended stay deletion
    question: Did my bulk delete of suspended stays complete?
  phrasing_ops: 6
  slug: oracle-hospitality-crmasync-api
- baseURL: /dvm/v1
  baseurl_source: spec
  description: The DataValueMappingService Web Service offers capability to convert Opera values to external vendor's values or vice versa.
  name: Oracle Hospitality Data Value Mapping API
  phrasing_intents:
  - id: getOperaHotelCode
    intent: Convert an external hotel ID to an OPERA code
    question: What OPERA hotel code corresponds to an external system's hotel ID?
  - id: getConvertedValues
    intent: Convert values between OPERA and an external system
    question: What does an external system's code translate to in OPERA for a hotel?
  - id: getDefaultValues
    intent: Get default mapping values for an external system
    question: What default values apply when an external system sends no mapped value?
  - id: getDvmConversionCodes
    intent: List conversion codes for an external system
    question: Which data value mapping conversion codes exist for an external system?
  - id: getDataValueMappings
    intent: List mappings for a conversion code
    question: What value mappings are set up under one conversion code?
  - id: postDataValueMappings
    intent: Create conversion code mappings
    question: How do I add a new value mapping under a conversion code?
  - id: putDataValueMappings
    intent: Update conversion code mappings
    question: How can I change an existing value mapping under a conversion code?
  - id: deleteDataValueMappings
    intent: Delete conversion code mappings
    question: Can I delete specific value mappings by their mapping IDs?
  phrasing_ops: 10
  slug: oracle-hospitality-datavaluemapping-api
- baseURL: /controls/v1
  baseurl_source: spec
  description: Distribution Property Controls
  name: Oracle Hospitality Distribution Controls API
  phrasing_intents:
  - id: getPropertyControls
    intent: Get a channel's property controls for a hotel
    question: What distribution controls does a booking channel have set for my property?
  phrasing_ops: 1
  slug: oracle-hospitality-distribution-controls-api
- baseURL: /fof/config/v1
  baseurl_source: spec
  description: The EndOfDay Configuration module offers the capability of creating, managing, and retrieving a properties End of Day configuration.
  name: Oracle Hospitality End Of Day Config API
  phrasing_intents:
  - id: pingEndOfDayConfigServices
    intent: Check the end of day configuration service
    question: Is the end of day configuration service responding?
  phrasing_ops: 1
  slug: oracle-hospitality-endofdayconfig-api
- baseURL: /exp/config/v1
  baseurl_source: spec
  description: The Export Service provides operations used by Opera to configure and generate file exports of Opera data.
  name: Oracle Hospitality Export API
  phrasing_intents:
  - id: getExportsAvailable
    intent: List available data exports
    question: Which data exports are set up and available for my hotels?
  - id: getExportColumnsAndFunctions
    intent: List columns and functions usable in exports
    question: What database columns and functions can I use when building an export?
  - id: postExportMappingCodes
    intent: Create export mapping codes
    question: How do I add new mapping codes for an export?
  - id: putExportMappingCodes
    intent: Update export mapping codes
    question: How do I change the codes that an export mapping translates values into?
  - id: putExportMappingLinkedTypes
    intent: Update export mapping linked codes
    question: How do I link OPERA codes to an export mapping type?
  - id: getExportMappingsByChain
    intent: List export mappings across the chain
    question: What export mappings are configured at the chain level?
  - id: postExportSchedules
    intent: Create export schedules
    question: How do I schedule an export to run automatically?
  - id: removeExportSchedules
    intent: Remove export schedules by job name
    question: How do I stop and delete a scheduled export job?
  phrasing_ops: 22
  slug: oracle-hospitality-export-api
- baseURL: /ent/config/v1
  baseurl_source: spec
  description: The ExternalConfig API from Oracle Hospitality — 1 operation(s) for externalconfig.
  name: Oracle Hospitality External Config API
  phrasing_intents:
  - id: pingExternalConfigServices
    intent: Check the external config service status
    question: Is the external configuration service up?
  phrasing_ops: 1
  slug: oracle-hospitality-externalconfig-api
- baseURL: /int/config/v1
  baseurl_source: spec
  description: The ExternalSystemsConfig API from Oracle Hospitality — 27 operation(s) for externalsystemsconfig.
  name: Oracle Hospitality External Systems Config API
  phrasing_intents:
  - id: getConfiguredExternalDevices
    intent: List external devices configured at a hotel
    question: Which external devices, like fiscal printers or payment terminals, are actually set up at my property?
  - id: getDeliveryMethods
    intent: Fetch delivery methods
    question: What delivery methods, like email or fax, are available for sending documents from a hotel?
  - id: putDeliveryMethods
    intent: Change existing delivery methods
    question: How do I edit a delivery method that's already configured?
  - id: deleteDeliveryMethods
    intent: Remove delivery methods
    question: How do I delete a delivery method a hotel no longer uses?
  - id: postDeliveryMethods
    intent: Create delivery methods
    question: How do I add a new way to deliver confirmations and folios, such as a new email channel?
  - id: getExternalDeviceConfigurations
    intent: Fetch external device configuration settings
    question: Where do I read the configuration settings and parameters behind external devices?
  - id: putExternalDeviceConfigurations
    intent: Change external device configurations
    question: How do I update the settings for an external device like a fiscal printer?
  - id: ping
    intent: Ping the external systems config service
    question: Is the external systems configuration service reachable?
  phrasing_ops: 43
  slug: oracle-hospitality-externalsystemsconfig-api
- baseURL: /fof/v1
  baseurl_source: spec
  description: The Front Desk Statistics module will provide statistical data related to front desk operations in a property.
  name: Oracle Hospitality FOF Stats API
  phrasing_intents:
  - id: getFrontOfficeStatistics
    intent: Get front office statistics for a date
    question: What are today's front office numbers, like arrivals and occupancy, for my hotel?
  - id: getFrontOfficeStatisticsWithDateRange
    intent: Get front office statistics over a date range
    question: How did front office statistics trend across a range of dates at my property?
  - id: getTaskSheetStatistics
    intent: Get housekeeping task sheet statistics
    question: How are housekeeping task sheets progressing at my property today?
  - id: getReservationQueueStatistics
    intent: Get reservation queue statistics
    question: How many reservations are waiting in the room queue at my hotel?
  - id: getReservationStatusStatistics
    intent: Count reservations by status per room type
    question: How many reservations in a given status are there for each room type?
  - id: getRoomsByRoomStatus
    intent: Count rooms by housekeeping and front office status
    question: How many rooms are clean, dirty or inspected right now, grouped by room type?
  - id: pingFOFStatsService
    intent: Check the front office statistics service
    question: Is the front office statistics service reachable?
  phrasing_ops: 7
  slug: oracle-hospitality-fofstats-api
- baseURL: /fof/v1
  baseurl_source: spec
  description: Front Desk module provides APIs related to a guests stay in the property. For example, checking a guest into the property, providing room information, splitting reservations, as well as adding wake-up
  name: Oracle Hospitality Front Desk Operations API
  phrasing_intents:
  - id: getResvForBatchCCAuth
    intent: Find reservations due a batch card authorization
    question: Which reservations still need their credit card authorized in the nightly batch?
  - id: processBatchCCAuth
    intent: Run batch credit card authorization
    question: How do I authorize credit cards for many reservations in one run?
  - id: getReservationsForBilling
    intent: Find reservations ready for billing
    question: Which reservations have open folios that the cashier needs to bill?
  - id: getDailyDocket
    intent: Get the daily docket
    question: What is on today's daily docket for the front office?
  - id: putDailyDocket
    intent: Change daily docket entries
    question: Can I edit entries already on the daily docket?
  - id: postDailyDocket
    intent: Create a daily docket entry
    question: What do I send to add a new item to the daily docket?
  - id: deleteDailyDocket
    intent: Delete a daily docket
    question: How do I remove a daily docket that is no longer needed?
  - id: postExternalRoomKeys
    intent: Request room keys from an external door lock
    question: How does OPERA Cloud send a key request to an external door lock system via outbound configuration?
  phrasing_ops: 61
  slug: oracle-hospitality-frontdeskoperations-api
- baseURL: /fof/v1
  baseurl_source: spec
  description: The FrontOffice External module provides operations for OPERA Cloud to access FrontOffice operations from external interfaces.
  name: Oracle Hospitality Front Office External API
  phrasing_intents:
  - id: postExternalRoomKeys
    intent: Request door lock room keys from an encoder
    question: How do I have a door lock system encode new room keys when a guest checks in?
  - id: postRoomKeysOutbound
    intent: Send an outbound room key request with user and time
    question: How do I send an outbound key request that records the request time and which user asked for it?
  phrasing_ops: 2
  slug: oracle-hospitality-frontofficeexternal-api
- baseURL: /crm/config/v1
  baseurl_source: spec
  description: These APIs will allow you to configure profile related configuration related to Administration.
  name: Oracle Hospitality Hotel Config API
  phrasing_intents:
  - id: getAvailablePreferences
    intent: List guest preferences available at a property
    question: Which guest preferences can staff pick from at a given hotel?
  - id: getCommunicationTypes
    intent: List communication types
    question: What communication types (phone, email, fax) are configured?
  - id: postCommunicationType
    intent: Create a communication type
    question: How do I add a new communication type like a messaging app to the configuration?
  - id: removeCommunicationType
    intent: Delete a communication type
    question: Can I remove a communication type we no longer use?
  - id: changeCommunicationType
    intent: Update a communication type
    question: Can I rename or change the role of an existing communication type?
  - id: pingHotelConfigServices
    intent: Check the hotel configuration service is up
    question: Is the hotel configuration service currently available?
  - id: getTemplateAirports
    intent: List template airports
    question: Which airports are defined at the template level for the chain?
  - id: postTemplateAirports
    intent: Create template airports
    question: How do I add an airport to the chain-wide template list?
  phrasing_ops: 455
  slug: oracle-hospitality-hotelconfig-api
- baseURL: /eComm/eToken/v1
  baseurl_source: spec
  description: Operations related to e-commerce tokenization for OPERA Cloud Properties.
  name: Oracle Hospitality Hotels API
  phrasing_intents:
  - id: postEcommTokenization
    intent: Start an e-commerce card tokenization transaction
    question: How do I start a card tokenization session through the e-commerce token form for a hotel?
  - id: getEcommTokenizationDetails
    intent: Check the result of an e-commerce tokenization
    question: Did the guest's card tokenization through the e-commerce form finish successfully?
  - id: openPaymentTokenExchange
    intent: Exchange a card number for a payment token
    question: Can I convert a raw card number into a token from the payment service provider?
  phrasing_ops: 3
  slug: oracle-hospitality-hotels-api
- baseURL: /hsk/v1
  baseurl_source: spec
  description: 'These APIs allows for retrieving and managing a room''s housekeeping data and front office status, for example update room 101 to be Out Of Order. Additionally, you can view room discrepancies between '
  name: Oracle Hospitality Housekeeping API
  phrasing_intents:
  - id: getHousekeepingAttendantsSchedule
    intent: View the housekeeping attendants' work schedule
    question: Which housekeeping attendants are scheduled to work at my hotel next week?
  - id: deleteHousekeepingAttendantSchedule
    intent: Remove an attendant's schedule for a day
    question: How do I take a housekeeping attendant off the schedule for a specific day?
  - id: autoGenerateTaskSheets
    intent: Automatically generate housekeeping task sheets
    question: Can OPERA build the day's housekeeping task sheets for me automatically?
  - id: getRoomConditions
    intent: List rooms that have a room condition set
    question: Which rooms at my hotel currently have a condition like show room or set aside?
  - id: setRoomCondition
    intent: Set, change or clear a condition on rooms
    question: How do I mark a room as set aside for a show or special use?
  - id: getFacilityForecast
    intent: Forecast housekeeping attendants and tasks needed
    question: How many housekeeping attendants will I need over the next few days?
  - id: deleteHouseKeepingTaskSheets
    intent: Delete every task sheet in a task sheet set
    question: Can I wipe out all task sheets in a task sheet set at once?
  - id: getHouseKeepingTasks
    intent: Get the existing housekeeping task sheets for a date
    question: What task sheets have been created for housekeeping today?
  phrasing_ops: 60
  slug: oracle-hospitality-housekeeping-api
- baseURL: /int/v1
  baseurl_source: spec
  description: The Integration Processor Service provides a set of operations which help the external customers and vendors to process Business Events generated in OPERA.
  name: Oracle Hospitality Integration Processor API
  phrasing_intents:
  - id: getBusinessEventsByExternalSystem
    intent: Dequeue business events for an external system chain-wide
    question: How can my integration pull queued OPERA business events for every hotel in the chain at once?
  - id: getBusinessEvents
    intent: Dequeue business events for one hotel
    question: Can I pull queued business events for just one property instead of the whole chain?
  phrasing_ops: 2
  slug: oracle-hospitality-integrationprocessor-api
- baseURL: /chl/v1
  baseurl_source: spec
  description: The Inventory APIs allow you to manage a properties room inventory, as well as manage overbooking/sell limits at different levels. It also contains operations to get Item Inventory.
  name: Oracle Hospitality Inventory API
  phrasing_intents:
  - id: getChannelSellLimits
    intent: Review daily sell limits for a channel
    question: How many rooms is a booking channel allowed to sell at my hotel each day?
  - id: changeChannelSellLimitsByDate
    intent: Set channel sell limits on specific dates
    question: How do I change a channel's sell limit for individual dates?
  - id: deleteChannelSellLimits
    intent: Delete a channel sell limit mapping
    question: How do I remove a channel sell limit mapping I no longer need?
  - id: changeChannelSellLimitsByDateRange
    intent: Set channel sell limits over a date range
    question: How do I apply the same sell limit to a channel across a whole date range?
  - id: getHotelInventory
    intent: Get room inventory for a hotel
    question: How many rooms does my hotel have available over a set of dates?
  - id: getItemInventory
    intent: Get item inventory for a date range
    question: How many rollaway beds or other inventory items are free at my hotel next week?
  - id: postHoldItemInventory
    intent: Place item inventory on hold
    question: How do I reserve inventory items like cribs so nobody else books them?
  - id: getHoldItemsInventory
    intent: List item inventory currently on hold
    question: Which inventory items are currently being held at my hotel?
  phrasing_ops: 13
  slug: oracle-hospitality-inventory-api
- baseURL: /inv/async/v1
  baseurl_source: spec
  description: The Inventory Asynchronous module provides capability for an external system to retrieve inventory related data using an asynchronous approach.
  name: Oracle Hospitality Inventory Async API
  phrasing_intents:
  - id: startRevenueInventoryStatisticsProcess
    intent: Start a revenue inventory statistics job
    question: How do I kick off an async job for a hotel's inventory revenue statistics?
  - id: getRevenueInventoryStatisticsProcessStatus
    intent: Check if a revenue statistics job is done
    question: Is my revenue inventory statistics job finished yet?
  - id: getRevenueInventoryStatistics
    intent: Fetch results of a revenue statistics job
    question: Where do I collect the revenue numbers once my inventory revenue job finishes?
  - id: startInventoryStatisticsProcess
    intent: Start a hotel inventory statistics job
    question: How do I request a hotel's occupancy and inventory statistics as a background job?
  - id: getInventoryStatisticsProcessStatus
    intent: Check if an inventory statistics job is done
    question: Are my hotel inventory statistics ready to download yet?
  - id: getInventoryStatisticsAsync
    intent: Fetch results of an inventory statistics job
    question: Where do I get the inventory statistics after the async process completes?
  - id: postSellLimitsProcess
    intent: Start an async job to create sell limits
    question: How do I create sell limits by date as a background process from an external system?
  - id: getSellLimitsProcessStatus
    intent: Check if a sell limits job is done
    question: Has my asynchronous sell limit creation finished yet?
  phrasing_ops: 9
  slug: oracle-hospitality-inventoryasync-api
- baseURL: /inv/v1
  baseurl_source: spec
  description: 'The Inventory Statistics APIs provide the ability to fetch hotels inventory statistics or block inventory statistics for a specified date range provided in the request. It also contains operations to '
  name: Oracle Hospitality INV Stats API
  phrasing_intents:
  - id: getBlockInventoryStatisticsMultipleHotelIds
    intent: Get group block inventory across several hotels
    question: How many rooms are held in group blocks across all my hotels?
  - id: getBlockInventoryStatistics
    intent: Get group block inventory for one hotel
    question: What's the group block room inventory at a single property?
  - id: getInventoryStatistics
    intent: Get a hotel's inventory statistics report
    question: What's my hotel's room inventory and availability for the next month?
  - id: pinginvStatsService
    intent: Check the inventory statistics service health
    question: Is the inventory statistics service up?
  phrasing_ops: 4
  slug: oracle-hospitality-invstats-api
- baseURL: /lms/v1
  baseurl_source: spec
  description: The Leisure Management module offers a set of APIs to manage the activities for a guest like spa, golf, tours etc. The external system can create, change, cancel activities and send these updates to O
  name: Oracle Hospitality Leisure Management API
  phrasing_intents:
  - id: getActivityBookings
    intent: Look up a guest's activity bookings
    question: How do I see which spa, golf or leisure activities a guest has booked at the hotel?
  - id: postActivityBookingForProfile
    intent: Create an activity booking for a profile
    question: How do I record a new leisure activity booking against a guest profile with no reservation?
  - id: putActivityBookingForProfile
    intent: Change a profile's activity booking
    question: How does an external activity scheduler update a booking held against a guest profile rather than a reservation?
  - id: deleteActivityBookingForProfile
    intent: Cancel a profile's activity booking
    question: How do I cancel a leisure activity booked against a guest profile?
  - id: postActivityBooking
    intent: Create an activity booking on a reservation
    question: How do I add a leisure activity booking to an in-house guest's reservation?
  - id: putActivityBooking
    intent: Change an activity booking on a reservation
    question: How does an external activity scheduler update an activity booked on a hotel reservation?
  - id: deleteActivityBooking
    intent: Cancel an activity booking on a reservation
    question: How do I cancel an activity booked on a guest's reservation?
  - id: postLocationNotification
    intent: Set or clear a guest location notification
    question: How do I tell the front desk where a guest can be found, for example at the spa?
  phrasing_ops: 9
  slug: oracle-hospitality-leisuremanagement-api
- baseURL: /lms/v1
  baseurl_source: spec
  description: The Leisure Management Configuration module offers a set of operations to manage the configuration of activities like Status codes, locations, types etc. User can create, change, remove and fetch Stat
  name: Oracle Hospitality Leisure Management Config API
  phrasing_intents:
  - id: postActivityLocations
    intent: Create an activity location
    question: How do I add a new place like the spa or tennis courts where leisure activities happen?
  - id: getActivityLocations
    intent: Look up activity locations for hotels
    question: Where can guests do activities at my resort — which activity locations are configured?
  - id: putActivityLocations
    intent: Change an existing activity location
    question: How do I rename or edit an activity location that already exists?
  - id: deleteActivityLocations
    intent: Remove an activity location
    question: How do I delete an activity location we closed?
  - id: copyActivityLocations
    intent: Copy an activity location to other properties
    question: How do I copy an activity location from one property to my other hotels?
  - id: postActivityStatusCodes
    intent: Create an activity status code
    question: How do I add a new status like 'waitlisted' for leisure activities?
  - id: getActivityStatusCodes
    intent: List activity status codes
    question: Which status codes can a leisure activity booking have at my hotel?
  - id: putActivityStatusCodes
    intent: Change an activity status code
    question: How do I edit the description of an existing activity status code?
  phrasing_ops: 17
  slug: oracle-hospitality-leisuremanagementconfig-api
- baseURL: /lookup/v1
  baseurl_source: spec
  description: The Lookup API from Oracle Hospitality — 2 operation(s) for lookup.
  name: Oracle Hospitality Lookup API
  phrasing_intents:
  - id: getExternalRoomTypes
    intent: List a channel partner's room types for a hotel
    question: Which room types does a channel partner map for my hotel in OPERA Cloud Distribution?
  - id: getExternalRatePlans
    intent: List a channel partner's rate plans for a hotel
    question: What rate plan codes does a channel partner send for my hotel?
  phrasing_ops: 2
  slug: oracle-hospitality-lookup-api
- baseURL: /lov/v1
  baseurl_source: spec
  description: The LOV Service provides various List of Values for drop-down components and single/multi-select LOVs for the user interface. This is a generic service in that the particular LOV is requested by code.
  name: Oracle Hospitality LOV API
  phrasing_intents:
  - id: getLOVNames
    intent: List the available list-of-values names
    question: Which list-of-values lookups can I call in OPERA Cloud?
  - id: getMembershipClassTypesLOV
    intent: List membership class types for an airline loyalty program
    question: What membership class types exist for an airline's frequent flyer program?
  - id: getPrintersLOV
    intent: List printers available for alert printing
    question: Which printers can alerts be sent to at our property?
  - id: getBlockBookingStatusesLOV
    intent: List booking statuses a group block can take
    question: What booking statuses can a group block be set to?
  - id: getBlockCurrentStatusesLOV
    intent: List the current status values for a block
    question: What is the list of current status values a group block can show?
  - id: getGdsRoomCategoryTemplatesLOV
    intent: List GDS room category templates for channels
    question: Which GDS room category templates are set up for our booking channels?
  - id: getGdsGuaranteeCodesLOV
    intent: List GDS guarantee codes for a booking channel
    question: What guarantee codes does a GDS booking channel accept?
  - id: getGdsRateCategoriesLOV
    intent: List GDS rate categories for a booking channel
    question: What GDS rate categories are available on a booking channel?
  phrasing_ops: 453
  slug: oracle-hospitality-lov-api
- baseURL: /crm/config/v1
  baseurl_source: spec
  description: These APIs will allow you to configure membership configuration such as membership rates, levels, groups, benefit programs and membership awards.
  name: Oracle Hospitality Membership Config API
  phrasing_intents:
  - id: getMembershipAwards
    intent: List loyalty membership awards
    question: Which membership awards are configured for our loyalty program?
  - id: postMembershipAwards
    intent: Create membership awards
    question: How do I add a new reward that loyalty members can redeem?
  - id: putMembershipAwards
    intent: Change an existing membership award
    question: Can I edit the details of a membership award that already exists?
  - id: deleteMembershipAwards
    intent: Delete a membership award
    question: Can I remove a loyalty award we no longer offer?
  - id: putUpsertMembershipAwards
    intent: Create or update a membership award by id
    question: Is there one call that creates a membership award if missing or updates it if it exists?
  - id: getMembershipBenefitPrograms
    intent: List benefit programs of a membership type
    question: Which benefit programs are set up for a given membership type?
  - id: postMembershipBenefitPrograms
    intent: Create a membership benefit program
    question: How do I set up a new benefit program for a membership type?
  - id: putMembershipBenefitPrograms
    intent: Change an existing benefit program
    question: Can I modify the rules of a benefit program that already exists?
  phrasing_ops: 98
  slug: oracle-hospitality-membershipconfig-api
- baseURL: /int/config/v1
  baseurl_source: spec
  description: The OEDSConfig API from Oracle Hospitality — 1 operation(s) for oedsconfig.
  name: Oracle Hospitality OEDS Config API
  phrasing_intents:
  - id: getOEDSConfigData
    intent: List OEDS API configuration
    question: Which OEDS APIs are configured for a given module?
  - id: changeOEDSConfigData
    intent: Update OEDS API configuration
    question: How can I change the OEDS configuration for a module's operation?
  phrasing_ops: 2
  slug: oracle-hospitality-oedsconfig-api
- baseURL: /onboard/v1
  baseurl_source: spec
  description: Distribution Onboarding
  name: Oracle Hospitality Onboarding API
  phrasing_intents:
  - id: putPropertyStatus
    intent: Update a property's connection status on a channel
    question: How do I mark a hotel as connected to my distribution channel?
  - id: getPropertyStatus
    intent: Check a property's onboarding status on a channel
    question: Is my hotel's connection to this distribution channel live yet?
  phrasing_ops: 2
  slug: oracle-hospitality-onboarding-api
- baseURL: /med/config/v1
  baseurl_source: spec
  description: Opera Content Service offers capability to manage big content using MTOM
  name: Oracle Hospitality Opera Content API
  phrasing_intents:
  - id: getCustomizedLetter
    intent: Retrieve a customized letter
    question: Can I pull up the customized letter generated for a guest by its letter ID?
  - id: getEmailFile
    intent: Download a stored email file
    question: Where can I retrieve the email file saved against a guest profile?
  - id: getFileAttachment
    intent: Retrieve a file attachment
    question: How do I download a file that was attached to a record in OPERA?
  - id: uploadFileAttachment
    intent: Upload a file attachment
    question: Can I attach a document to a reservation or profile in OPERA?
  - id: emailFolioReport
    intent: Email a folio report
    question: How do I email a guest their folio?
  - id: setCustomizedLetter
    intent: Update a reservation's customized letter
    question: Can I change the customized letter attached to a guest's reservation?
  - id: getFolioReport
    intent: Generate a reservation's folio report
    question: Can I get the folio for a specific folio window on a reservation?
  - id: getRegistrationCard
    intent: Get a reservation's registration card
    question: Can I print a guest's registration card for check-in?
  phrasing_ops: 11
  slug: oracle-hospitality-operacontent-api
- baseURL: /rsv/v1
  baseurl_source: spec
  description: The PackageCategory API from Oracle Hospitality — 1 operation(s) for packagecategory.
  name: Oracle Hospitality Package Category API
  phrasing_intents:
  - id: getReservationsByPackage
    intent: Find reservations consuming a package on a date
    question: Which reservations have a breakfast or other package to be consumed on a given date?
  phrasing_ops: 1
  slug: oracle-hospitality-packagecategory-api
- baseURL: /crm/v1
  baseurl_source: spec
  description: The Profile APIs allow you to view, create, update, and delete profiles in OPERA Cloud. Each time a new profile in created in OPERA Cloud, a profileID is assigned. Use this profileID to retrieve and u
  name: Oracle Hospitality Profile API
  phrasing_intents:
  - id: postMembershipNumber
    intent: Generate a membership number via an external system
    question: Can a new loyalty membership number be generated through an external system's membership endpoint?
  - id: getAddress
    intent: Look up cities and states
    question: Can I look up which city and state go with a postal code?
  - id: deleteCertificate
    intent: Delete a certificate
    question: How do I remove a certificate using the generic certificates endpoint?
  - id: postCompanyProfile
    intent: Create a company, travel agent, group or source profile
    question: How do I create a new company or travel agent profile in OPERA Cloud?
  - id: getCompanyProfile
    intent: Get a company profile by corporate ID
    question: What details are stored on a company profile if I know its corporate ID?
  - id: getDuplicateExternalSubscriptions
    intent: Find profiles linked to multiple external profiles
    question: Which OPERA Cloud profiles are subscribed to more than one external profile in the same external system?
  - id: getDuplicateOPERASubscriptions
    intent: Find external profiles linked to multiple OPERA profiles
    question: Which external profiles are linked to more than one OPERA Cloud profile?
  - id: getECertificates
    intent: List e-certificates on a profile
    question: What e-certificates does a guest profile have in OPERA Cloud?
  phrasing_ops: 110
  slug: oracle-hospitality-profile-api
- baseURL: /crm/config/v1
  baseurl_source: spec
  description: APIs for Customer Relationship Management (profile) configuration including preference groups and preferences.
  name: Oracle Hospitality Profile Configuration API
  phrasing_intents:
  - id: getAddressFormats
    intent: Look up configured address formats
    question: Which address formats are set up for guest profiles in OPERA Cloud?
  - id: putAddressFormats
    intent: Update existing address formats
    question: How do I change the layout of an address format that already exists?
  - id: deleteAddressFormats
    intent: Delete address formats
    question: How do I remove address formats we no longer use?
  - id: postAddressFormats
    intent: Create new address formats
    question: How can I add a new address format for a country we just started serving?
  - id: getClaimAdjustmentLimits
    intent: Look up claim adjustment limits (deprecated)
    question: What claim adjustment limits are configured for a property?
  - id: putClaimAdjustmentLimits
    intent: Change existing claim adjustment limits
    question: How do I modify claim adjustment limits that are already configured?
  - id: postClaimAdjustmentLimits
    intent: Create new claim adjustment limits
    question: How can I set up a new claim adjustment limit?
  - id: putUpsertClaimAdjustmentLimits
    intent: Create or update claim adjustment limits
    question: Can I create a claim adjustment limit or update it if it already exists in one call?
  phrasing_ops: 50
  slug: oracle-hospitality-profileconfiguration-api
- baseURL: /crm/v1
  baseurl_source: spec
  description: The Profile External module allows you to retrieve and manage profiles from an external system.
  name: Oracle Hospitality Profile External API
  phrasing_intents:
  - id: getExternalProfiles
    intent: Search guest profiles in an external system
    question: How do I look up a guest profile that lives in an external CRM or loyalty system?
  - id: downloadExternalProfile
    intent: Download a guest profile from an external system
    question: Once I find a profile in the external system, how do I pull it into OPERA?
  - id: getPlayerStatistics
    intent: Get a guest's gaming player statistics
    question: Can I see casino player statistics for a hotel guest from the gaming system?
  - id: getGamingOffers
    intent: List gaming offers available to a member
    question: What casino offers can I attach to a guest's profile from the gaming system?
  - id: checkIataNumber
    intent: Validate a travel agent's IATA number
    question: How do I check whether a travel agent's IATA number is valid?
  - id: getValidatedAddresses
    intent: Look up address suggestions from a validation vendor
    question: How do I get validated address suggestions for a guest's partially typed address?
  - id: getValidatedAddress
    intent: Get the full address for a validated address ID
    question: After picking an address suggestion, how do I get the complete address details?
  - id: validateMembershipNumber
    intent: Validate a loyalty membership number externally
    question: How can I check a guest's membership number against the external loyalty system?
  phrasing_ops: 11
  slug: oracle-hospitality-profileexternal-api
- baseURL: /crm/v1
  baseurl_source: spec
  description: Profiles have many Lists of Values, storing the available options a user can select when updating a profile. This module allows you to get available ListOfValues for Profile Preferences and AR Address
  name: Oracle Hospitality Profile LOV API
  phrasing_intents:
  - id: getAvailableARAddresses
    intent: List addresses usable for a profile's AR account
    question: Which of a profile's addresses can be used as the billing address on an accounts receivable account?
  - id: getAvailablePreferences
    intent: List preferences available for a profile
    question: What guest preferences can be assigned to a profile?
  phrasing_ops: 2
  slug: oracle-hospitality-profilelov-api
- baseURL: /crm/v1
  baseurl_source: spec
  description: This will allow you to create a guest profile enrollment in OPERA Cloud. Enrollment relates to a membership program, so as an example you can enrol the guest Mr Tom Smith into a Membership / loyalty p
  name: Oracle Hospitality Profile Membership API
  phrasing_intents:
  - id: postEnrollment
    intent: Enroll a guest in an external system's loyalty program
    question: How do I enroll a guest profile into a membership program run by an external loyalty system?
  - id: redeemAward
    intent: Redeem an award on an external system's profile
    question: How do I redeem a loyalty award for a guest identified by an external system's profile ID?
  - id: getMembershipDetails
    intent: Get memberships for an external system's profile
    question: What loyalty memberships does a guest have when I only know the external system's profile ID?
  - id: getAirlineTransactionsStatus
    intent: Check status of airline membership transactions
    question: Which membership transactions has the airline partner processed so far?
  - id: getAvailableAwardsBasedOnType
    intent: Find loyalty awards available by award type
    question: Which rate, product or room upgrade awards can a member choose from?
  - id: deleteAwards
    intent: Cancel an award granted to a member
    question: How do I cancel a loyalty award that was already granted to a member?
  - id: getAwardsToGrant
    intent: List awards that can be granted to a member
    question: Which awards could I grant to this member right now?
  - id: postEnrollments
    intent: Enroll a guest profile in a membership program
    question: How do I sign an existing guest profile up for our loyalty program in OPERA?
  phrasing_ops: 45
  slug: oracle-hospitality-profilemembership-api
- baseURL: /crm/v1
  baseurl_source: spec
  description: These APIs will allow you to retrieve statistical data for a specified profile.
  name: Oracle Hospitality Profile Statistics API
  phrasing_intents:
  - id: getProfileMembershipStatistics
    intent: Get a guest's membership points statistics
    question: How many loyalty points has a guest earned on a membership card?
  - id: getProfileStatistics
    intent: Get a guest profile's stay and revenue statistics
    question: How much revenue and how many stays has a guest profile generated at my hotels?
  - id: pingProfileStatsService
    intent: Check the profile statistics service status
    question: Is the profile statistics service responding?
  phrasing_ops: 3
  slug: oracle-hospitality-profilestatistics-api
- baseURL: /ops/v1
  baseurl_source: spec
  description: The ProvisioningService Web Service offers capability of provisioning and deprovisioning properties and chains in Opera.
  name: Oracle Hospitality Provisioning API
  phrasing_intents:
  - id: getCurrencies
    intent: List currencies valid in the environment
    question: Which currencies are valid in my OPERA Cloud environment?
  phrasing_ops: 1
  slug: oracle-hospitality-provisioning-api
- baseURL: /rtp/async/v1
  baseurl_source: spec
  description: The RatePlanAsync API from Oracle Hospitality — 18 operation(s) for rateplanasync.
  name: Oracle Hospitality Rate Plan Async API
  phrasing_intents:
  - id: startSetDailyRatePlanSchedulesProcess
    intent: Start a daily rate plan pricing update
    question: How do I push daily rate plan prices from my revenue system into OPERA Cloud?
  - id: getDailyRatePlanSchedulesProcessStatus
    intent: Check if a daily pricing update has finished
    question: Is my daily rate plan pricing upload still running?
  - id: getDailyRatePlanSchedules
    intent: Get results of a daily rate plan pricing update
    question: Which daily rate plan prices failed to load after my schedule upload?
  - id: startSetBestAvailableRatePlansProcess
    intent: Start setting best available rate plans
    question: How do I set best available rates by day or by length of stay?
  - id: getBestAvailableRatePlansProcessStatus
    intent: Check if a best available rate update finished
    question: Has my best available rate plans job completed yet?
  - id: getBestAvailableRatePlans
    intent: Get results of a best available rate update
    question: Which best available rate entries failed to process?
  - id: startHurdleRatesProcess
    intent: Start configuring hurdle rates
    question: How can my revenue system set hurdle rates for a hotel?
  - id: getHurdleRatesProcessStatus
    intent: Check if a hurdle rate job has finished
    question: Is my hurdle rate configuration job still in progress?
  phrasing_ops: 27
  slug: oracle-hospitality-rateplanasync-api
- baseURL: /rep/config/v1
  baseurl_source: spec
  description: The Report Service provides information about available report modules which may be generated, along with their parameters.
  name: Oracle Hospitality Report API
  phrasing_intents:
  - id: getAllReportGroups
    intent: List all report groups
    question: What report groups exist in OPERA Cloud for organizing reports?
  - id: getAllReports
    intent: List all reports for an integration
    question: Is there an integration-oriented endpoint that returns every report in OPERA Cloud?
  - id: postGenericReports
    intent: Create generic reports
    question: How do I create a new generic report in OPERA Cloud?
  - id: deleteGenericReports
    intent: Delete generic reports
    question: How do I delete a generic report I no longer need?
  - id: changeGenericReports
    intent: Update existing generic reports
    question: How do I change the definition of a generic report that already exists?
  - id: getReportParameters
    intent: Get the parameters a report accepts
    question: What input parameters does a particular report take before I run it?
  - id: copyReportTextConfiguration
    intent: Copy report text configuration between properties
    question: Can I copy report text configuration from one property to another?
  - id: getReports
    intent: Search reports by name, group or hotel
    question: How do I find a report by part of its name or description?
  phrasing_ops: 12
  slug: oracle-hospitality-report-api
- baseURL: /rsv/v1
  baseurl_source: spec
  description: Reservation API
  name: Oracle Hospitality Reservation API
  phrasing_intents:
  - id: postCall
    intent: Register a call on a reservation
    question: How do I log a phone call a guest made about their reservation?
  - id: getCallStatistics
    intent: Get reservation call statistics
    question: What call statistics can I pull for my reservation agents?
  - id: getExternalSystemReservations
    intent: Look up reservations by external system references
    question: Can I find hotel reservations using the reference numbers from my external system?
  - id: searchExternalSystemReservations
    intent: Search external-system reservations via request body
    question: Can I post a search body to find reservations tied to an external system's references?
  - id: getAwardUpgrades
    intent: Get award upgrades available at a property
    question: Which loyalty award upgrades can a member redeem at this hotel?
  - id: getAwards
    intent: Fetch certificates and awards on a reservation
    question: What certificates and awards are attached to a guest's reservation?
  - id: postReservationByBlock
    intent: Create a reservation inside a group block
    question: How do I book a room against a group block?
  - id: putCancellationPolicy
    intent: Change a property's cancellation policy
    question: Can I edit a cancellation policy that's already configured for my hotel?
  phrasing_ops: 179
  slug: oracle-hospitality-reservation-api
- baseURL: /book/v1
  baseurl_source: spec
  description: Reservation Request API operations allow a channel to create, modify and cancel reservations in Oracle Hospitality Distribution.<br/> It is usually used in conjunction with OPERA Cloud Distribution Sh
  name: Oracle Hospitality Reservation Request API
  phrasing_intents:
  - id: postReservation
    intent: Book a new hotel reservation from a channel
    question: How do I create a new hotel booking through the OPERA distribution channel API?
  - id: putReservation
    intent: Modify an existing reservation
    question: How do I change the dates or room on a booking a channel already made?
  - id: getReservation
    intent: Look up a reservation by confirmation number
    question: How can I pull up a booking using its confirmation number?
  - id: postCancelReservation
    intent: Cancel a reservation
    question: How do I cancel a guest's hotel booking from a channel?
  - id: postOnHoldReservation
    intent: Commit or ignore an on-hold reservation
    question: How do I confirm a reservation that is sitting on hold?
  phrasing_ops: 5
  slug: oracle-hospitality-reservation-request-api
- baseURL: /rsv/async/v1
  baseurl_source: spec
  description: The Reservation Asynchronous module provides capability for an external system to retrieve reservation related data using an asynchronous approach.
  name: Oracle Hospitality Reservation Async API
  phrasing_intents:
  - id: startReservationsDailySummaryProcess
    intent: Start a reservations daily summary job
    question: How do I request a daily reservation summary for a date range?
  - id: getReservationsProcessStatus
    intent: Check if a daily summary job is done
    question: Is my reservation daily summary still processing?
  - id: getReservationsDailySummary
    intent: Get the results of a daily summary job
    question: Where do I fetch the finished reservation daily summary?
  - id: startReservationDetailsMassUpdateProcess
    intent: Mass update reservation details
    question: Can I change the market or source code on many reservations at once?
  - id: startTracesMassUpdateProcess
    intent: Mass add traces to reservations
    question: How do I add the same trace for housekeeping to dozens of reservations?
  - id: startPreferencesMassUpdateProcess
    intent: Mass add preferences to reservations
    question: Can I add a guest preference like a high floor to many reservations at once?
  - id: startRoutingInstructionsMassUpdateProcess
    intent: Mass update reservation routing instructions
    question: How do I route charges to a master folio for a whole list of reservations?
  - id: startHousekeepingMassUpdateProcess
    intent: Mass update reservation housekeeping
    question: Can I set a housekeeping service schedule for a batch of reservations?
  phrasing_ops: 19
  slug: oracle-hospitality-reservationasync-api
- baseURL: /rsv/config/v1
  baseurl_source: spec
  description: The Reservation Configuration module offers capability of creating, managing, and retrieving of Reservation configuration.
  name: Oracle Hospitality Reservation Config API
  phrasing_intents:
  - id: getAlertCodeTemplates
    intent: List alert code templates
    question: Which alert code templates are set up at the template level in OPERA Cloud?
  - id: putAlertCodeTemplates
    intent: Update an alert code template
    question: How can I edit the wording of an existing alert code template?
  - id: deleteAlertCodeTemplates
    intent: Delete alert code templates
    question: Can I remove an alert code template I no longer need?
  - id: postAlertCodeTemplates
    intent: Create an alert code template
    question: How do I add a new alert code template that properties can reuse?
  - id: deleteAutoAttachElements
    intent: Delete auto attach element rules
    question: How can I remove an auto attach element rule from a property?
  - id: getECouponCodes
    intent: List eCoupon codes across properties
    question: Which eCoupon codes are configured across my properties?
  - id: deleteGlobalAlerts
    intent: Delete a global alert
    question: How do I delete a global alert so it stops appearing on reservations?
  - id: getGlobalAlerts
    intent: List global alerts for a property
    question: What global alerts fire automatically on reservations at my hotel?
  phrasing_ops: 79
  slug: oracle-hospitality-reservationconfig-api
- baseURL: /rsv/v1
  baseurl_source: spec
  description: The Reservation External module provides operations for OPERA Cloud to access reservations from external interfaces.
  name: Oracle Hospitality Reservation External API
  phrasing_intents:
  - id: pingReservationExternalService
    intent: Check the reservation external service version
    question: Is the OPERA Cloud reservation external service up?
  phrasing_ops: 1
  slug: oracle-hospitality-reservationexternal-api
- baseURL: /evm/config/v1
  baseurl_source: spec
  description: The Resource Config Service Web Service offers capability to configure Master Data needed for Hotel Resources such as managing Inventory Items, Item Pools, Item Classes, etc.
  name: Oracle Hospitality Resource Config API
  phrasing_intents:
  - id: copyEventForecasts
    intent: Copy event forecasts to another property
    question: Can I copy an event forecast from one property to another instead of rebuilding it?
  - id: getCateringContainers
    intent: List menu item catering containers
    question: Which catering container codes, like per dozen or per piece, are set up?
  - id: postCateringContainers
    intent: Create menu item catering containers
    question: How do I define a new unit a menu item is sold in, like per dozen?
  - id: putCateringContainers
    intent: Update a catering container code
    question: Can I rename or change the description of an existing catering container code?
  - id: deleteCateringContainers
    intent: Delete a catering container code
    question: Can I remove a catering container code we no longer sell menu items in?
  - id: getCateringItemRates
    intent: List catering item rate codes
    question: What catering item rate codes are configured?
  - id: postCateringItemRates
    intent: Create catering item rate codes
    question: How do I set up a new catering item rate code?
  - id: putCateringItemRates
    intent: Update a catering item rate code
    question: Can I change an existing catering item rate code's details?
  phrasing_ops: 88
  slug: oracle-hospitality-resourceconfig-api
- baseURL: /rmr/v1
  baseurl_source: spec
  description: The REST APIs allow you to perform all actions related to Room Rotation from configuring point calculations for owner rooms, adjustment options for room prioritization and automatic assignment based o
  name: Oracle Hospitality Room Rotation API
  phrasing_intents:
  - id: getReservationRotationPoints
    intent: List reservations with their rotation points
    question: How many rotation points did each departing reservation earn for its room owner?
  - id: searchReservationRotationPoints
    intent: Search reservation rotation points with a body
    question: Is there a POST search for reservation rotation points?
  - id: getReservationRotationPointsDetails
    intent: Get a reservation's rotation point details
    question: How were the rotation points on one reservation calculated and adjusted?
  - id: putReservationRotationPointsDetails
    intent: Adjust a reservation's rotation points
    question: How do I correct the rotation points credited for one reservation?
  - id: getRoomRotationPoints
    intent: Get rotation points per room
    question: What's each owned unit's rotation point balance on a given date?
  - id: putRoomRotationPoints
    intent: Adjust rotation points by room number
    question: How do I update the balance forward points on individual rooms?
  - id: getRoomOwnerships
    intent: Get the rooms a profile owns
    question: Which rooms does this guest own or refer through the rental program?
  - id: getRoomOwners
    intent: Find room owners
    question: Who owns a particular room in the rental pool?
  phrasing_ops: 10
  slug: oracle-hospitality-roomrotation-api
- baseURL: /rmr/config/v1
  baseurl_source: spec
  description: The REST APIs allow you to perform all actions related to Room Rotation from configuring point calculations for owner rooms, adjustment options for room prioritization and automatic assignment based o
  name: Oracle Hospitality Room Rotation Config API
  phrasing_intents:
  - id: getAdjustmentReasons
    intent: List room rotation adjustment reasons
    question: What adjustment reasons are configured for room rotation points?
  - id: postAdjustmentReasons
    intent: Create room rotation adjustment reasons
    question: How do I add a new reason for adjusting room rotation points?
  - id: putAdjustmentReasons
    intent: Update a room rotation adjustment reason
    question: How do I edit the description of an existing rotation adjustment reason?
  - id: deleteAdjustmentReasons
    intent: Delete a room rotation adjustment reason
    question: How do I remove a rotation adjustment reason we no longer use?
  - id: getRevenueTransactionCodes
    intent: List room rotation revenue transaction codes
    question: Which transaction codes count as room rotation revenue at my hotel?
  - id: putRevenueTransactionCodes
    intent: Set rotation revenue status on transaction codes
    question: How do I mark transaction codes as counting toward room rotation revenue?
  - id: getRotationPeriod
    intent: Get a hotel's room rotation period
    question: What is the current room rotation period configured for a property?
  - id: putRotationPeriod
    intent: Change a hotel's room rotation period
    question: How do I change the room rotation period for a property?
  phrasing_ops: 30
  slug: oracle-hospitality-roomrotationconfig-api
- baseURL: /rsv/v1
  baseurl_source: spec
  description: The Reservation Statistics Service provides statistical data for reservations that exist in OPERA Cloud.
  name: Oracle Hospitality RSV Stats API
  phrasing_intents:
  - id: getBlockReservationStatisticsByDateAndRoomPool
    intent: Get group block reservation stats by date
    question: How many rooms are picked up in group blocks per day and room pool?
  - id: getReservationPace
    intent: Get reservation booking pace
    question: How fast are reservations coming in for a given stay date?
  - id: getReservationStatistics
    intent: Run a reservation statistics report
    question: What reservation statistics can I pull for a hotel over a date range?
  - id: pingRSVStatsService
    intent: Check reservation statistics service version
    question: Is the reservation statistics service reachable?
  phrasing_ops: 4
  slug: oracle-hospitality-rsvstats-api
- baseURL: /shop/v1
  baseurl_source: spec
  description: The Shop API from Oracle Hospitality — 6 operation(s) for shop.
  name: Oracle Hospitality Shop API
  phrasing_intents:
  - id: getProperties
    intent: Compare availability and rates across hotels
    question: Which of our hotels have rooms available for my dates, and at what rate range?
  - id: getPropertyOffers
    intent: List room offers at one hotel
    question: What rooms and rates can a guest book at this hotel for my stay dates?
  - id: getPropertyOffer
    intent: Get one specific room offer
    question: What is the exact price for one room type and rate plan combination on my dates?
  - id: getPropertyAddons
    intent: List add-on packages for a stay
    question: What add-ons like breakfast or parking packages can a guest buy at this hotel?
  - id: getPropertyCalendar
    intent: Show lowest rates on a calendar for a hotel
    question: What is the cheapest nightly rate at this hotel for each day over the next two months?
  - id: getPropertyAlternateOffers
    intent: Suggest alternate dates with availability
    question: If my dates are sold out, which nearby arrival dates still have offers?
  phrasing_ops: 6
  slug: oracle-hospitality-shop-api
- baseURL: /crm/v1
  baseurl_source: spec
  description: These APIs will allow you to view, create, update, and delete profiles in OPERA Cloud.
  name: Oracle Hospitality Suspended Stay API
  phrasing_intents:
  - id: putProcessSuspendedStays
    intent: Process suspended stays
    question: How do I reprocess stays that were suspended during upload?
  - id: getSuspendedStay
    intent: Get one suspended stay record
    question: What revenue, rate and membership details are on a specific suspended stay record?
  - id: putSuspendedStay
    intent: Correct a suspended stay record
    question: Can I fix the rate code or room type on a suspended stay before reprocessing it?
  - id: deleteSuspendedStay
    intent: Delete a suspended stay record
    question: Can I remove a suspended stay from OPERA along with its revenue and error details?
  - id: getSuspendedStays
    intent: Search suspended stays
    question: Which stays are waiting to be manually processed after a failed upload?
  - id: getSuspendedStaysErrorsSummary
    intent: Summarize suspended stay errors
    question: What are the most common errors causing stays to be suspended?
  phrasing_ops: 6
  slug: oracle-hospitality-suspendedstay-api
- baseURL: https://oracle.api.com/ohcgep/v1
  baseurl_source: spec
  description: The Upsell Offers API from Oracle Hospitality — 1 operation(s) for upsell offers.
  name: Oracle Hospitality Upsell Offers API
  phrasing_intents:
  - id: getUpsellOffers
    intent: Get upsell offers available for a reservation
    question: What room upgrades or upsell offers can I show a guest before they arrive?
  phrasing_ops: 1
  slug: oracle-hospitality-upsell-offers-api
- baseURL: /fof/config/v1
  baseurl_source: spec
  description: The Credit Card Internal Service contains operations used internally by OPERA Cloud.
  name: Oracle Hospitality Credit card API
  phrasing_intents:
  - id: getAuthorizationRule
    intent: Get the credit card authorization rule
    question: Which credit card authorization rule applies to a reservation?
  - id: getCardReaderDelimiters
    intent: Get card reader delimiters
    question: What track delimiters does a card reader device use?
  - id: getCreditCardInfo
    intent: Get a reservation's card type and expiry
    question: How do I find the card type and expiration date of the card on a reservation?
  - id: validateCreditCardType
    intent: Validate a credit card type
    question: Can I check whether a card number matches the card type entered for a payment?
  - id: decodeCard
    intent: Decode swiped card track data
    question: How can I turn raw card-swipe track data into card details?
  - id: getCreditCardReaderDevices
    intent: List credit card reader devices
    question: Which credit card reader devices are set up?
  - id: getCreditCardUniqueId
    intent: Get a credit card's vaulted unique ID
    question: How do I get the vaulted unique ID for a credit card?
  - id: updateInterfaceCustomData
    intent: Update a hotel interface's custom data
    question: How can I change custom data on a hotel's payment interface?
  phrasing_ops: 16
  slug: oracle-hospitality-credit-card-api
- baseURL: /cms/v1
  baseurl_source: spec
  description: Customer Management web service caters operations for Customer Management activities.
  name: Oracle Hospitality Customer Management API
  phrasing_intents:
  - id: postTrackItItems
    intent: Log a new Track It item
    question: How do I log a guest's luggage for storage or a parcel that arrived for them?
  - id: putTrackItItems
    intent: Update a Track It item
    question: How do I update a stored bag or parcel record, like marking it delivered?
  - id: deleteTrackItItems
    intent: Delete a Track It item
    question: Can I delete a Track It record that was entered by mistake?
  - id: getTrackItItems
    intent: List Track It items for a property
    question: Which guest luggage, parcels or valet cars are we currently holding?
  - id: searchTrackItItems
    intent: Search Track It items with posted criteria
    question: Is there a POST search for Track It items when I have many filters?
  - id: pingCustomerManagementService
    intent: Check the customer management service health
    question: Is the customer management service up?
  phrasing_ops: 6
  slug: oracle-hospitality-customer-management-api
- baseURL: /evm/v1
  baseurl_source: spec
  description: The Event APIs will allow you to retrieve, create, manage and delete events and related event functionality such as event resources, catering packages and even event waitlists.
  name: Oracle Hospitality Event Management API
  phrasing_intents:
  - id: manageAlternateEvents
    intent: Manage alternate catering events
    question: How do I mark one catering event as an alternate to another event?
  - id: postCateringPackage
    intent: Add a catering package to a block
    question: How do I add an available catering package onto a group block?
  - id: getCateringPackages
    intent: List catering packages on a block
    question: Which catering packages are already booked on this group block?
  - id: changeCateringPackages
    intent: Update catering packages already on a block
    question: Can I edit a catering package that is already attached to a block?
  - id: copyCateringPackage
    intent: Copy a catering package to another date
    question: Can I duplicate a catering package onto another day of the same block?
  - id: getCateringPackageRevenue
    intent: Get revenue for a catering package
    question: How much revenue is a specific catering package on a block bringing in?
  - id: postCateringPackageRevenue
    intent: Add revenue to a catering package
    question: How do I record new revenue against a catering package on a block?
  - id: copyEventResources
    intent: Copy event resources to other events
    question: Can I copy the menus and items from one event to several other events?
  phrasing_ops: 45
  slug: oracle-hospitality-event-management-api
- baseURL: /rtp/v1
  baseurl_source: spec
  description: The Rate Plan APIs allow for creating, managing, and retrieving rates and their related components such as negotiated rates and packages.
  name: Oracle Hospitality Rate Plan API
  phrasing_intents:
  - id: postTemplateControlSegment
    intent: Create a control segment template
    question: How do I set up a new control segment template at the chain level?
  - id: removeTemplateControlSegment
    intent: Delete a control segment template
    question: Can I remove a control segment template that we no longer use?
  - id: changeTemplateControlSegment
    intent: Modify a control segment template
    question: Can I edit a chain-level control segment template after it has been created?
  - id: getTemplateControlSegments
    intent: List control segment templates
    question: Which control segment templates are defined for our chain?
  - id: getControlSegments
    intent: Search property control segments
    question: Which control segments are configured at a specific hotel?
  - id: getBestAvailableRates
    intent: Fetch best available rates for a hotel
    question: What are the best available rates set up at my hotel starting next week?
  - id: postBestAvailableRates
    intent: Create best available rates
    question: How do I load best available rates for a rate code into the property?
  - id: deleteBestAvailableRates
    intent: Delete best available rates for a date range
    question: Can I clear best available rates for a rate code over a date range?
  phrasing_ops: 112
  slug: oracle-hospitality-rate-plan-api
artifact_total: 230
asyncapis:
- description: 'Oracle publishes no AsyncAPI document for Oracle Hospitality. This document is DERIVED, by the API Evangelist enrichment pipeline, from two real, published surfaces: (1) the six outbound Swagger 2.0 s'
  name: Oracle Hospitality event and outbound-callback surface
  slug: oracle-hospitality-outbound-asyncapi
collections:
- collection_type: open
  name: OPERA Cloud Distribution ARI Publication
  slug: open-oracle-hospitality-distribution-outbound-aripublication
- collection_type: open
  name: OPERA Cloud Distribution Outbound Lookup
  slug: open-oracle-hospitality-distribution-outbound-lookup
- collection_type: open
  name: OPERA Cloud Distribution Content Notification
  slug: open-oracle-hospitality-distribution-outbound-notification
- collection_type: open
  name: OPERA Cloud Distribution Book
  slug: open-oracle-hospitality-distribution-v1-book
- collection_type: open
  name: OPERA Cloud Distribution Content
  slug: open-oracle-hospitality-distribution-v1-content
- collection_type: open
  name: OPERA Cloud Distribution Property Controls
  slug: open-oracle-hospitality-distribution-v1-controls
- collection_type: open
  name: OPERA Cloud Distribution Reservation Service
  slug: open-oracle-hospitality-distribution-v1-distribution
- collection_type: open
  name: OPERA Cloud Distribution Authentication API
  slug: open-oracle-hospitality-distribution-v1-hdpbaoauth2
- collection_type: open
  name: OPERA Cloud Distribution Onboarding
  slug: open-oracle-hospitality-distribution-v1-onboard
- collection_type: open
  name: OPERA Cloud Distribution Reservation Notification
  slug: open-oracle-hospitality-distribution-v1-resnotif
- collection_type: open
  name: OPERA Cloud Distribution Shop
  slug: open-oracle-hospitality-distribution-v1-shop
- collection_type: open
  name: Nor1 Integrated Upsell API
  slug: open-oracle-hospitality-nor1-v1-upselloffers
- collection_type: open
  name: OPERA Cloud Customer Relationship Management Outbound API
  slug: open-oracle-hospitality-property-outbound-crmoutbound
- collection_type: open
  name: OPERA Cloud Cashiering Outbound API
  slug: open-oracle-hospitality-property-outbound-cshoutbound
- collection_type: open
  name: OPERA Cloud Front Desk Operations Outbound API
  slug: open-oracle-hospitality-property-outbound-fofoutbound
- collection_type: open
  name: OPERA Cloud Activity API
  slug: open-oracle-hospitality-property-v1-act
- collection_type: open
  name: OPERA Cloud Activity Management API
  slug: open-oracle-hospitality-property-v1-actcfg
- collection_type: open
  name: OPERA Cloud Accounts Receivables API
  slug: open-oracle-hospitality-property-v1-ars
- collection_type: open
  name: OPERA Cloud Block API
  slug: open-oracle-hospitality-property-v1-blk
- collection_type: open
  name: OPERA Cloud Block Reservation Asynchronous API
  slug: open-oracle-hospitality-property-v1-blkasync
- collection_type: open
  name: OPERA Cloud Block Configuration API
  slug: open-oracle-hospitality-property-v1-blkcfg
- collection_type: open
  name: OPERA Cloud Back Office Operations API
  slug: open-oracle-hospitality-property-v1-bof
- collection_type: open
  name: OPERA Cloud Channel Configuration API
  slug: open-oracle-hospitality-property-v1-chl
- collection_type: open
  name: OPERA Cloud API for Customer Management Service
  slug: open-oracle-hospitality-property-v1-cms
- collection_type: open
  name: OPERA Cloud Customer Relationship Management API
  slug: open-oracle-hospitality-property-v1-crm
- collection_type: open
  name: OPERA Cloud CRM Asynchronous API
  slug: open-oracle-hospitality-property-v1-crmasync
- collection_type: open
  name: OPERA Cloud CRM Configuration API
  slug: open-oracle-hospitality-property-v1-crmcfg
- collection_type: open
  name: OPERA Cloud Cashiering API
  slug: open-oracle-hospitality-property-v1-csh
- collection_type: open
  name: OPERA Cloud Cashiering Asynchronous API
  slug: open-oracle-hospitality-property-v1-cshasync
- collection_type: open
  name: OPERA Cloud DataValueMapping Service API
  slug: open-oracle-hospitality-property-v1-dvm
- collection_type: open
  name: Cloud OPI Tokenization ECommerce API
  slug: open-oracle-hospitality-property-v1-ecommtokenization
- collection_type: open
  name: OPERA Cloud Enterprise Configuration API
  slug: open-oracle-hospitality-property-v1-entcfg
- collection_type: open
  name: OPERA Cloud Sales Event Management API
  slug: open-oracle-hospitality-property-v1-evm
- collection_type: open
  name: OPERA Cloud Event Configuration API
  slug: open-oracle-hospitality-property-v1-evmcfg
- collection_type: open
  name: OPERA Cloud Export Configuration API
  slug: open-oracle-hospitality-property-v1-expcfg
- collection_type: open
  name: OPERA Cloud Front Desk Operations Service
  slug: open-oracle-hospitality-property-v1-fof
- collection_type: open
  name: OPERA Cloud Front Desk Configuration API
  slug: open-oracle-hospitality-property-v1-fofcfg
- collection_type: open
  name: OPERA Cloud Housekeeping Service API
  slug: open-oracle-hospitality-property-v1-hsk
- collection_type: open
  name: OPERA Cloud Integration Processor API
  slug: open-oracle-hospitality-property-v1-int
- collection_type: open
  name: OPERA Cloud Integration Configuration API
  slug: open-oracle-hospitality-property-v1-intcfg
- collection_type: open
  name: OPERA Cloud Inventory API
  slug: open-oracle-hospitality-property-v1-inv
- collection_type: open
  name: Opera Cloud Inventory Asynchronous API
  slug: open-oracle-hospitality-property-v1-invasync
- collection_type: open
  name: OPERA Cloud Leisure Management API
  slug: open-oracle-hospitality-property-v1-lms
- collection_type: open
  name: OPERA Cloud List of Values Management API
  slug: open-oracle-hospitality-property-v1-lov
- collection_type: open
  name: OPERA Cloud Content Service
  slug: open-oracle-hospitality-property-v1-medcfg
- collection_type: open
  name: oAuth API for OHIP
  slug: open-oracle-hospitality-property-v1-oauth
- collection_type: open
  name: OPERA Provisioning Service API
  slug: open-oracle-hospitality-property-v1-ops
- collection_type: open
  name: OPERA Cloud Price Availability Rate API
  slug: open-oracle-hospitality-property-v1-par
- collection_type: open
  name: OPERA Cloud Price Availability Rate Async API
  slug: open-oracle-hospitality-property-v1-parasync
- collection_type: open
  name: OPERA Cloud Report Master Data Management API
  slug: open-oracle-hospitality-property-v1-repcfg
- collection_type: open
  name: OPERA Cloud Room Configuration API
  slug: open-oracle-hospitality-property-v1-rmcfg
- collection_type: open
  name: OPERA Cloud Room Rotation Service API
  slug: open-oracle-hospitality-property-v1-rmr
- collection_type: open
  name: OPERA Cloud Room Rotation Configuration Service API
  slug: open-oracle-hospitality-property-v1-rmrcfg
- collection_type: open
  name: OPERA Cloud Reservation API
  slug: open-oracle-hospitality-property-v1-rsv
- collection_type: open
  name: OPERA Cloud Reservation Asynchronous API
  slug: open-oracle-hospitality-property-v1-rsvasync
- collection_type: open
  name: OPERA Cloud Reservation Master Data Management API
  slug: open-oracle-hospitality-property-v1-rsvcfg
- collection_type: open
  name: OPERA Cloud Rate API
  slug: open-oracle-hospitality-property-v1-rtp
- collection_type: open
  name: Opera Cloud Rate Plan Asynchronous Service API
  slug: open-oracle-hospitality-property-v1-rtpasync
- collection_type: open
  name: OPI Token Exchange Service API
  slug: open-oracle-hospitality-property-v1-tokenexchange
common:
- group: commercial
  href: https://artifacts.apis.io/oracle-hospitality/plans/oracle-hospitality-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oracle-hospitality-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/capabilities/oracle-hospitality-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-hospitality-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/oracle/hospitality-api-docs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/oracle/hospitality-api-docs/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/oracle/hospitality-api-docs/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/oracle/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/oracle/hospitality-api-docs/blob/main/CONTRIBUTING.md
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-outbound-aripublication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-outbound-aripublication-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-outbound-lookup-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-outbound-lookup-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-outbound-notification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-outbound-notification-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-book-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-book-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-content-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-controls-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-controls-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-distribution-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-distribution-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-hdpbaoauth2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-hdpbaoauth2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-onboard-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-onboard-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-resnotif-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-resnotif-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-distribution-v1-shop-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-shop-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-nor1-v1-upselloffers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-nor1-v1-upselloffers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-outbound-crmoutbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-outbound-crmoutbound-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-outbound-cshoutbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-outbound-cshoutbound-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-outbound-fofoutbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-outbound-fofoutbound-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-act-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-act-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-actcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-actcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-ars-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-ars-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-blk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-blk-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-blkasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-blkasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-blkcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-blkcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-bof-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-bof-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-chl-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-chl-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-cms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-cms-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-crm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-crm-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-crmasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-crmasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-crmcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-crmcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-csh-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-csh-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-cshasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-cshasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-dvm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-dvm-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-ecommtokenization-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-ecommtokenization-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-entcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-entcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-evm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-evm-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-evmcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-evmcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-expcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-expcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-fof-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-fof-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-fofcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-fofcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-hsk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-hsk-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-int-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-int-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-intcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-intcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-inv-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-inv-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-invasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-invasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-lms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-lms-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-lov-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-lov-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-medcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-medcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-oauth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-oauth-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-ops-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-ops-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-par-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-par-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-parasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-parasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-repcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-repcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rmcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rmcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rmr-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rmr-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rmrcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rmrcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rsv-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rsv-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rsvasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rsvasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rsvcfg-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rsvcfg-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rtp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rtp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-rtpasync-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rtpasync-overlay.yaml
- group: other
  href: https://artifacts.apis.io/oracle-hospitality/overlays/oracle-hospitality-property-v1-tokenexchange-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-tokenexchange-overlay.yaml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: agent
  href: https://artifacts.apis.io/oracle-hospitality/mcp/oracle-hospitality-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/oracle-hospitality-mcp.yml
- group: auth
  href: https://artifacts.apis.io/oracle-hospitality/authentication/oracle-hospitality-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oracle-hospitality-authentication.yml
- group: auth
  href: https://artifacts.apis.io/oracle-hospitality/security/oracle-hospitality-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oracle-hospitality-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/hospitality/
- group: start
  title: ''
  type: Portal
  url: https://www.oracle.com/hospitality/integration-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/industries/hospitality/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/oracle/hospitality-api-docs
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/hospitalityapis/oracle-hospitality-apis/overview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/oracle-hospitality/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: License
  url: https://oss.oracle.com/licenses/upl
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_oauth_token_api.htm
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_limits.htm
- group: design
  title: ''
  type: Versioning
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_versioning.htm
- group: operate
  title: ''
  type: Support
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_getting_help_and_contacting_support.htm
- group: build
  href: https://artifacts.apis.io/oracle-hospitality/packages/oracle-hospitality-packages.yml
  title: ''
  type: Packages
  url: packages/oracle-hospitality-packages.yml
- group: agent
  href: https://artifacts.apis.io/oracle-hospitality/llms/oracle-hospitality-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oracle-hospitality-llms.txt
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/conformance/oracle-hospitality-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oracle-hospitality-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/cloud-compliance/
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/errors/oracle-hospitality-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oracle-hospitality-problem-types.yml
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/errors/oracle-hospitality-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/oracle-hospitality-error-codes.yml
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/lifecycle/oracle-hospitality-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-hospitality-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_versioning.htm
- group: auth
  href: https://artifacts.apis.io/oracle-hospitality/scopes/oracle-hospitality-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/oracle-hospitality-scopes.yml
- group: auth
  href: https://artifacts.apis.io/oracle-hospitality/security/oracle-hospitality-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-hospitality-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.oracle.com/corporate/security-practices/assurance/vulnerability/reporting.html
- group: auth
  href: https://artifacts.apis.io/oracle-hospitality/security/oracle-hospitality-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/oracle-hospitality-trust-center.yml
- group: start
  href: https://artifacts.apis.io/oracle-hospitality/sandbox/oracle-hospitality-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/oracle-hospitality-sandbox.yml
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/conventions/oracle-hospitality-conventions.yml
  title: ''
  type: Conventions
  url: conventions/oracle-hospitality-conventions.yml
- group: operate
  href: https://artifacts.apis.io/oracle-hospitality/changelog/oracle-hospitality-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oracle-hospitality-changelog.yml
- group: operate
  href: https://artifacts.apis.io/oracle-hospitality/rate-limits/oracle-hospitality-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/oracle-hospitality-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/data-model/oracle-hospitality-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oracle-hospitality-data-model.yml
- group: docs
  href: https://artifacts.apis.io/oracle-hospitality/asyncapi/oracle-hospitality-outbound-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/oracle-hospitality-outbound-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/oracle-hospitality/asyncapi/oracle-hospitality-outbound-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/oracle-hospitality-outbound-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/oracle-hospitality/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/oracle-hospitality/mcp/oracle-hospitality-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/oracle-hospitality-tool-crosswalk.yml
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/oracle/hospitality-api-docs/tree/main/rest-api-specs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_gs.htm
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_upcoming_major_changes.htm
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/hospitality/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.oracle.com/apex/f?p=DSTORE:PRODUCT:0:::6:P6_LPI,P6_PROD_HIER_ID:38393155522162790035848247,38391514880125550241393242
- group: start
  title: ''
  type: SignUp
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/t_getting_started_for_partners.htm
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/oracle/hospitality-api-docs
- group: docs
  href: https://artifacts.apis.io/oracle-hospitality/graphql/oracle-hospitality-rna-base.graphql
  title: ''
  type: GraphQL
  url: graphql/oracle-hospitality-rna-base.graphql
created: '2026-07-28'
description: 'Oracle Hospitality is Oracle Corporation''s hotel and food-and-beverage technology line, built on the 2014 acquisition of MICROS Systems and anchored by OPERA Cloud, the property management system that runs the front desk, reservations, housekeeping, cashiering and event sales for a large share of the world''s branded hotel rooms, alongside OPERA Cloud Distribution, Simphony point of sale and Nor1 upsell. Home market is the United States. It sits in the middle of the hotel distribution chain rather than at either end: it is the system of record a property runs on, and the switch through which that property''s availability, rates and inventory reach GDS, OTA and web channels and through which reservations come back. Its API posture is unusually open at the specification layer and firmly gated at the credential layer - Oracle publishes 59 Swagger 2.0 specifications covering roughly 3,500 operations to a public GitHub repository under the Universal Permissive License, and publishes
  the full Oracle Hospitality Integration Platform (OHIP) developer guide openly, but there is no self-serve signup: partners must purchase Oracle Hospitality Integration Cloud Service through the Oracle Store or a CPQ form, production access requires an Oracle Partner Network reference number, and distribution channel partners additionally need an Oracle-issued global Channel Code and an Oracle Cloud Marketplace listing.'
finops:
- has_sources: true
  method: derived
  name: Oracle Hospitality Finops
  primary_unit: 10,000 transactions
  service_category: ''
  slug: oracle-hospitality-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle.png
layout: provider
modified: '2026-08-21'
name: Oracle Hospitality
nav: Providers
network: true
overview: 'Oracle Hospitality publishes 153 API contracts indexed on the [APIs.io](https://apis.io/) network, including OPERA Cloud Business Events Streaming API, Accounts Receivables API, Accounts Receivables Config API, and 150 more. Tagged areas include Travel, United States, Hospitality, Hotels, and Property Management.


  The Oracle Hospitality catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Oracle Hospitality''s developer surface includes authentication, developer portal, documentation, support, sandbox, changelog, API reference, and 107 more developer resources.'
plans:
- name: Oracle Hospitality Plans Pricing
  plan_count: 1
  slug: oracle-hospitality-plans-pricing
- name: Oracle Hospitality Price Estimates
  plan_count: 0
  slug: oracle-hospitality-price-estimates
random_paper: 13
rate_limits:
- limit_count: 9
  name: Oracle Hospitality Rate Limits
  slug: oracle-hospitality-rate-limits
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Oracle Hospitality API Rules
  rule_count: 71
  severity_counts:
    error: 52
    hint: 0
    info: 5
    warn: 14
  slug: oracle-hospitality-rules
scopes:
- name: Oracle Hospitality Scopes
  scope_count: 1
  slug: oracle-hospitality-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: exemplar
  composite: 81.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 62.5
    catalog_earned_first_party: 20.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 89.5
    contract_governance: 31.8
    contract_quality: 57.9
    developer_ergonomics: 70.8
    discoverability: 69.6
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 81.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 24.7
      total: 77
    mcp: derived
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
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/oracle-hospitality/oracle-hospitality-2026-08-07T190821.png
security:
- kind: authentication
  name: Oracle Hospitality Authentication
  slug: oracle-hospitality-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Oracle Hospitality Domain Security
  slug: oracle-hospitality-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oracle Hospitality Vulnerability Disclosure
  slug: oracle-hospitality-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Oracle Hospitality Trust Center
  slug: oracle-hospitality-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, PCI DSS, HIPAA, HITRUST, FedRAMP, CSA STAR, IRAP, C5, ENS, FIPS 140
skill_count: 7
skills:
- name: Run a guest from arrival to departure
  slug: oracle-hospitality-arrival-to-departure
- name: Authenticate to the Oracle Hospitality Integration Platform
  slug: oracle-hospitality-authenticate
- name: Extract data in bulk from OPERA Cloud
  slug: oracle-hospitality-bulk-extract
- name: Consume OPERA Cloud Business Events
  slug: oracle-hospitality-business-events
- name: Connect a distribution channel to OPERA Cloud
  slug: oracle-hospitality-distribution-channel
- name: Drive housekeeping room status
  slug: oracle-hospitality-housekeeping
- name: Shop availability and create a reservation
  slug: oracle-hospitality-shop-and-book
slug: oracle-hospitality
tags:
- Travel
- United States
- Hospitality
- Hotels
- Property Management
- Distribution
- Channel Management
- Booking
- Reservations
- Point-of-Sale
- Restaurant
- Real-Time
website: https://www.oracle.com/hospitality/
---
