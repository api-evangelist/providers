---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-01'
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
- description: The REST API's will allow you to create, manage, or delete accounts, add comments, traces, reminders, create or close invoices for example.
  name: Oracle Hospitality Accounts Receivables API
  slug: oracle-hospitality-accountsreceivables-api
- description: The Accounts Receivables Config module offers the capability of creating, managing, and retrieving of Accounts Receivables configuration.
  name: Oracle Hospitality Accounts Receivables Config API
  slug: oracle-hospitality-accountsreceivablesconfig-api
- description: The Activity REST APIs allow you to view, create, update, and complete an Activity in OPERA Cloud. You are also able to perform more actions such as add attachments.
  name: Oracle Hospitality Activity API
  slug: oracle-hospitality-activity-api
- description: The Activity Configuration APIs offers capability of creating, managing, and retrieving Activity configuration elements, such as Activity Type code, Activity Result codes.
  name: Oracle Hospitality Activity Management API
  slug: oracle-hospitality-activitymanagement-api
- description: The API to Fulfill Upsell Offers to customers and third parties API from Oracle Hospitality — 1 operation(s) for api to fulfill upsell offers to customers and third parties.
  name: Oracle Hospitality API to Fulfill Upsell Offers to customers and third parties API
  slug: oracle-hospitality-api-to-fulfill-upsell-offers-to-customers-and-third-parties-api
- description: The ARI Publication service provides ability to send distribution partners with hotel property inventory level, room rates, and restrictions.
  name: Oracle Hospitality ARI Publication API
  slug: oracle-hospitality-ari-publication-api
- description: Authentication service
  name: Oracle Hospitality Authentication API
  slug: oracle-hospitality-authentication-api
- description: The Availability APIs allow you to manage a properties room-rate availability, which is configured for a channel. This also includes operations to manage restrictions and hurdles.
  name: Oracle Hospitality Availability API
  slug: oracle-hospitality-availability-api
- description: The Availability Asynchronous module provides capability for an external system to retrieve availability related data using an asynchronous approach.
  name: Oracle Hospitality Availability Async API
  slug: oracle-hospitality-availabilityasync-api
- description: The AvailabilityExternal API from Oracle Hospitality — 2 operation(s) for availabilityexternal.
  name: Oracle Hospitality Availability External API
  slug: oracle-hospitality-availabilityexternal-api
- description: This module provides APIs to service Back Office operations for property, such as managing end-of-day, getting the properties current business date, and perform cashier closure.
  name: Oracle Hospitality Back Office Operations API
  slug: oracle-hospitality-backofficeoperations-api
- description: The BEProcessor Service offers capability of creating, managing, and retrieving of BE Processor configuration.
  name: Oracle Hospitality BE Processor API
  slug: oracle-hospitality-beprocessor-api
- description: These APIs will allow you to completely create and manage your block in OPERA Cloud - including all related functionalities of a block such as manage Room allocation, Status update, block reservations
  name: Oracle Hospitality Block API
  slug: oracle-hospitality-block-api
- description: The Block Async Service Web Service provides capability to implement block related asynchronous operations in OPERA Cloud.
  name: Oracle Hospitality Block Async API
  slug: oracle-hospitality-blockasync-api
- description: The Block Configuration module offers capability of creating, managing, and retrieving of Block configuration.
  name: Oracle Hospitality Block Config API
  slug: oracle-hospitality-blockconfig-api
- description: The Block External module provides operations for OPERA Cloud to access blocks from an external interfaces. It also offers capability for downloading external blocks into OPERA Cloud.
  name: Oracle Hospitality Block External API
  slug: oracle-hospitality-blockexternal-api
- description: Block Statistics provide statistical data of blocks that exist in OPERA Cloud.
  name: Oracle Hospitality Block Stats API
  slug: oracle-hospitality-blockstats-api
- description: 'Cashiering module provides APIs to service front desk billing requirements, as well as any requirements related to a reservation''s folio. You can retrieve a guest folio, post billing charges to guest '
  name: Oracle Hospitality Cashiering API
  slug: oracle-hospitality-cashiering-api
- description: The CashieringAsync API from Oracle Hospitality — 2 operation(s) for cashieringasync.
  name: Oracle Hospitality Cashiering Async API
  slug: oracle-hospitality-cashieringasync-api
- description: 'Cashiering configurations affect the control and management of financial transactions at your property. You can configure cashiering components for articles for sale, cancellation handling, deposits, '
  name: Oracle Hospitality Cashiering Config API
  slug: oracle-hospitality-cashieringconfig-api
- description: The ChainConfigService Web Service offers capability of creating, managing, and retrieving of chain configuration.
  name: Oracle Hospitality Chain Config API
  slug: oracle-hospitality-chainconfig-api
- description: The Channel APIs allows you to view, configure and manage the mappings for your channel rate codes, negotiated rates, room types, global descriptions, letters, credit card types and channel codes.
  name: Oracle Hospitality Channel API
  slug: oracle-hospitality-channel-api
- description: These Commission APIs allow you to get, update, and remove commissions on an Account Receivable (AR) profile in OPERA Cloud.
  name: Oracle Hospitality Commission Config API
  slug: oracle-hospitality-commissionconfig-api
- description: Commission web service provides commission processing service like payment processing, payment activity and search.
  name: Oracle Hospitality Commissions API
  slug: oracle-hospitality-commissions-api
- description: The Content API from Oracle Hospitality — 5 operation(s) for content.
  name: Oracle Hospitality Content API
  slug: oracle-hospitality-content-api
- description: The Content Notification service provides ability to send distribution partners with hotel property inventory level, room rates, and restrictions.
  name: Oracle Hospitality Content Notification API
  slug: oracle-hospitality-content-notification-api
- description: The Credit Card Internal Service contains operations used internally by OPERA Cloud.
  name: Oracle Hospitality Credit Card API
  slug: oracle-hospitality-creditcard-api
- description: The CRM Async Web Service provides capability to implement stay records related asynchronous operations in OPERA Cloud.
  name: Oracle Hospitality CRM Async API
  slug: oracle-hospitality-crmasync-api
- description: Customer Management web service caters operations for Customer Management activities.
  name: Oracle Hospitality Customer Management API
  slug: oracle-hospitality-customermanagement-api
- description: The DataValueMappingService Web Service offers capability to convert Opera values to external vendor's values or vice versa.
  name: Oracle Hospitality Data Value Mapping API
  slug: oracle-hospitality-datavaluemapping-api
- description: Distribution Property Controls
  name: Oracle Hospitality Distribution Controls API
  slug: oracle-hospitality-distribution-controls-api
- description: The EndOfDay Configuration module offers the capability of creating, managing, and retrieving a properties End of Day configuration.
  name: Oracle Hospitality End Of Day Config API
  slug: oracle-hospitality-endofdayconfig-api
- description: The Event APIs will allow you to retrieve, create, manage and delete events and related event functionality such as event resources, catering packages and even event waitlists.
  name: Oracle Hospitality Event Management API
  slug: oracle-hospitality-eventmanagement-api
- description: The Export Service provides operations used by Opera to configure and generate file exports of Opera data.
  name: Oracle Hospitality Export API
  slug: oracle-hospitality-export-api
- description: The ExternalConfig API from Oracle Hospitality — 1 operation(s) for externalconfig.
  name: Oracle Hospitality External Config API
  slug: oracle-hospitality-externalconfig-api
- description: The ExternalSystemsConfig API from Oracle Hospitality — 27 operation(s) for externalsystemsconfig.
  name: Oracle Hospitality External Systems Config API
  slug: oracle-hospitality-externalsystemsconfig-api
- description: The Front Desk Statistics module will provide statistical data related to front desk operations in a property.
  name: Oracle Hospitality FOF Stats API
  slug: oracle-hospitality-fofstats-api
- description: Front Desk module provides APIs related to a guests stay in the property. For example, checking a guest into the property, providing room information, splitting reservations, as well as adding wake-up
  name: Oracle Hospitality Front Desk Operations API
  slug: oracle-hospitality-frontdeskoperations-api
- description: The FrontOffice External module provides operations for OPERA Cloud to access FrontOffice operations from external interfaces.
  name: Oracle Hospitality Front Office External API
  slug: oracle-hospitality-frontofficeexternal-api
- description: These APIs will allow you to configure profile related configuration related to Administration.
  name: Oracle Hospitality Hotel Config API
  slug: oracle-hospitality-hotelconfig-api
- description: Operations related to e-commerce tokenization for OPERA Cloud Properties.
  name: Oracle Hospitality Hotels API
  slug: oracle-hospitality-hotels-api
- description: 'These APIs allows for retrieving and managing a room''s housekeeping data and front office status, for example update room 101 to be Out Of Order. Additionally, you can view room discrepancies between '
  name: Oracle Hospitality Housekeeping API
  slug: oracle-hospitality-housekeeping-api
- description: The Integration Processor Service provides a set of operations which help the external customers and vendors to process Business Events generated in OPERA.
  name: Oracle Hospitality Integration Processor API
  slug: oracle-hospitality-integrationprocessor-api
- description: The Inventory APIs allow you to manage a properties room inventory, as well as manage overbooking/sell limits at different levels. It also contains operations to get Item Inventory.
  name: Oracle Hospitality Inventory API
  slug: oracle-hospitality-inventory-api
- description: The Inventory Asynchronous module provides capability for an external system to retrieve inventory related data using an asynchronous approach.
  name: Oracle Hospitality Inventory Async API
  slug: oracle-hospitality-inventoryasync-api
- description: 'The Inventory Statistics APIs provide the ability to fetch hotels inventory statistics or block inventory statistics for a specified date range provided in the request. It also contains operations to '
  name: Oracle Hospitality INV Stats API
  slug: oracle-hospitality-invstats-api
- description: The Leisure Management module offers a set of APIs to manage the activities for a guest like spa, golf, tours etc. The external system can create, change, cancel activities and send these updates to O
  name: Oracle Hospitality Leisure Management API
  slug: oracle-hospitality-leisuremanagement-api
- description: The Leisure Management Configuration module offers a set of operations to manage the configuration of activities like Status codes, locations, types etc. User can create, change, remove and fetch Stat
  name: Oracle Hospitality Leisure Management Config API
  slug: oracle-hospitality-leisuremanagementconfig-api
- description: The Lookup API from Oracle Hospitality — 2 operation(s) for lookup.
  name: Oracle Hospitality Lookup API
  slug: oracle-hospitality-lookup-api
- description: The LOV Service provides various List of Values for drop-down components and single/multi-select LOVs for the user interface. This is a generic service in that the particular LOV is requested by code.
  name: Oracle Hospitality LOV API
  slug: oracle-hospitality-lov-api
- description: These APIs will allow you to configure membership configuration such as membership rates, levels, groups, benefit programs and membership awards.
  name: Oracle Hospitality Membership Config API
  slug: oracle-hospitality-membershipconfig-api
- description: The OEDSConfig API from Oracle Hospitality — 1 operation(s) for oedsconfig.
  name: Oracle Hospitality OEDS Config API
  slug: oracle-hospitality-oedsconfig-api
- description: Distribution Onboarding
  name: Oracle Hospitality Onboarding API
  slug: oracle-hospitality-onboarding-api
- description: Opera Content Service offers capability to manage big content using MTOM
  name: Oracle Hospitality Opera Content API
  slug: oracle-hospitality-operacontent-api
- description: The PackageCategory API from Oracle Hospitality — 1 operation(s) for packagecategory.
  name: Oracle Hospitality Package Category API
  slug: oracle-hospitality-packagecategory-api
- description: The Profile APIs allow you to view, create, update, and delete profiles in OPERA Cloud. Each time a new profile in created in OPERA Cloud, a profileID is assigned. Use this profileID to retrieve and u
  name: Oracle Hospitality Profile API
  slug: oracle-hospitality-profile-api
- description: APIs for Customer Relationship Management (profile) configuration including preference groups and preferences.
  name: Oracle Hospitality Profile Configuration API
  slug: oracle-hospitality-profileconfiguration-api
- description: The Profile External module allows you to retrieve and manage profiles from an external system.
  name: Oracle Hospitality Profile External API
  slug: oracle-hospitality-profileexternal-api
- description: Profiles have many Lists of Values, storing the available options a user can select when updating a profile. This module allows you to get available ListOfValues for Profile Preferences and AR Address
  name: Oracle Hospitality Profile LOV API
  slug: oracle-hospitality-profilelov-api
- description: This will allow you to create a guest profile enrollment in OPERA Cloud. Enrollment relates to a membership program, so as an example you can enrol the guest Mr Tom Smith into a Membership / loyalty p
  name: Oracle Hospitality Profile Membership API
  slug: oracle-hospitality-profilemembership-api
- description: These APIs will allow you to retrieve statistical data for a specified profile.
  name: Oracle Hospitality Profile Statistics API
  slug: oracle-hospitality-profilestatistics-api
- description: The ProvisioningService Web Service offers capability of provisioning and deprovisioning properties and chains in Opera.
  name: Oracle Hospitality Provisioning API
  slug: oracle-hospitality-provisioning-api
- description: The Rate Plan APIs allow for creating, managing, and retrieving rates and their related components such as negotiated rates and packages.
  name: Oracle Hospitality Rate Plan API
  slug: oracle-hospitality-rateplan-api
- description: The RatePlanAsync API from Oracle Hospitality — 18 operation(s) for rateplanasync.
  name: Oracle Hospitality Rate Plan Async API
  slug: oracle-hospitality-rateplanasync-api
- description: The Report Service provides information about available report modules which may be generated, along with their parameters.
  name: Oracle Hospitality Report API
  slug: oracle-hospitality-report-api
- description: Reservation API
  name: Oracle Hospitality Reservation API
  slug: oracle-hospitality-reservation-api
- description: 'Reservation Notification API operations allow a channel to deliver, modify and cancel a reservation created and already confirmed from an external system (for example an OTA).<br/> It is usually used '
  name: Oracle Hospitality Reservation Notification API
  slug: oracle-hospitality-reservation-notification-api
- description: Reservation Request API operations allow a channel to create, modify and cancel reservations in Oracle Hospitality Distribution.<br/> It is usually used in conjunction with OPERA Cloud Distribution Sh
  name: Oracle Hospitality Reservation Request API
  slug: oracle-hospitality-reservation-request-api
- description: The Reservation Asynchronous module provides capability for an external system to retrieve reservation related data using an asynchronous approach.
  name: Oracle Hospitality Reservation Async API
  slug: oracle-hospitality-reservationasync-api
- description: The Reservation Configuration module offers capability of creating, managing, and retrieving of Reservation configuration.
  name: Oracle Hospitality Reservation Config API
  slug: oracle-hospitality-reservationconfig-api
- description: The Reservation External module provides operations for OPERA Cloud to access reservations from external interfaces.
  name: Oracle Hospitality Reservation External API
  slug: oracle-hospitality-reservationexternal-api
- description: The Resource Config Service Web Service offers capability to configure Master Data needed for Hotel Resources such as managing Inventory Items, Item Pools, Item Classes, etc.
  name: Oracle Hospitality Resource Config API
  slug: oracle-hospitality-resourceconfig-api
- description: The REST APIs allow you to perform all actions related to Room Rotation from configuring point calculations for owner rooms, adjustment options for room prioritization and automatic assignment based o
  name: Oracle Hospitality Room Rotation API
  slug: oracle-hospitality-roomrotation-api
- description: The REST APIs allow you to perform all actions related to Room Rotation from configuring point calculations for owner rooms, adjustment options for room prioritization and automatic assignment based o
  name: Oracle Hospitality Room Rotation Config API
  slug: oracle-hospitality-roomrotationconfig-api
- description: The Reservation Statistics Service provides statistical data for reservations that exist in OPERA Cloud.
  name: Oracle Hospitality RSV Stats API
  slug: oracle-hospitality-rsvstats-api
- description: The Shop API from Oracle Hospitality — 6 operation(s) for shop.
  name: Oracle Hospitality Shop API
  slug: oracle-hospitality-shop-api
- description: These APIs will allow you to view, create, update, and delete profiles in OPERA Cloud.
  name: Oracle Hospitality Suspended Stay API
  slug: oracle-hospitality-suspendedstay-api
- description: The Upsell Offers API from Oracle Hospitality — 1 operation(s) for upsell offers.
  name: Oracle Hospitality Upsell Offers API
  slug: oracle-hospitality-upsell-offers-api
artifact_total: 221
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
- group: other
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
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-outbound-aripublication-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-outbound-lookup-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-outbound-notification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-book-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-content-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-controls-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-distribution-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-hdpbaoauth2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-onboard-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-resnotif-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-distribution-v1-shop-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-nor1-v1-upselloffers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-outbound-crmoutbound-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-outbound-cshoutbound-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-outbound-fofoutbound-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-act-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-actcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-ars-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-blk-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-blkasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-blkcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-bof-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-chl-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-cms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-crm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-crmasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-crmcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-csh-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-cshasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-dvm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-ecommtokenization-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-entcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-evm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-evmcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-expcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-fof-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-fofcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-hsk-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-int-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-intcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-inv-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-invasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-lms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-lov-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-medcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-oauth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-ops-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-par-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-parasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-repcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rmcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rmr-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rmrcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rsv-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rsvasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rsvcfg-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rtp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-rtpasync-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-hospitality-property-v1-tokenexchange-overlay.yaml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oracle-hospitality-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-hospitality-authentication.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/oracle-hospitality-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oracle-hospitality-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/oracle-hospitality-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/cloud-compliance/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oracle-hospitality-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/oracle-hospitality-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-hospitality-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.oracle.com/cd/F29336_01/doc.201/f27480/c_versioning.htm
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-hospitality-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-hospitality-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.oracle.com/corporate/security-practices/assurance/vulnerability/reporting.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/oracle-hospitality-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oracle-hospitality-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oracle-hospitality-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oracle-hospitality-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oracle-hospitality-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oracle-hospitality-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/oracle-hospitality-outbound-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/oracle-hospitality-outbound-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
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
  title: ''
  type: GraphQL
  url: graphql/oracle-hospitality-rna-base.graphql
created: '2026-07-28'
description: 'Oracle Hospitality is Oracle Corporation''s hotel and food-and-beverage technology line, built on the 2014 acquisition of MICROS Systems and anchored by OPERA Cloud, the property management system that runs the front desk, reservations, housekeeping, cashiering and event sales for a large share of the world''s branded hotel rooms, alongside OPERA Cloud Distribution, Simphony point of sale and Nor1 upsell. Home market is the United States. It sits in the middle of the hotel distribution chain rather than at either end: it is the system of record a property runs on, and the switch through which that property''s availability, rates and inventory reach GDS, OTA and web channels and through which reservations come back. Its API posture is unusually open at the specification layer and firmly gated at the credential layer - Oracle publishes 59 Swagger 2.0 specifications covering roughly 3,500 operations to a public GitHub repository under the Universal Permissive License, and publishes
  the full Oracle Hospitality Integration Platform (OHIP) developer guide openly, but there is no self-serve signup: partners must purchase Oracle Hospitality Integration Cloud Service through the Oracle Store or a CPQ form, production access requires an Oracle Partner Network reference number, and distribution channel partners additionally need an Oracle-issued global Channel Code and an Oracle Cloud Marketplace listing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle.png
layout: provider
mcp_servers:
- description: ''
  name: Oracle Hospitality MCP Server
  slug: oracle-hospitality-mcp-server
modified: '2026-08-21'
name: Oracle Hospitality
nav: Providers
network: true
overview: 'Oracle Hospitality publishes 79 APIs on the [APIs.io](https://apis.io/) network, including OPERA Cloud Business Events Streaming API, Accounts Receivables API, Accounts Receivables Config API, and 76 more. Tagged areas include Travel, United States, Hospitality, Hotels, and Property Management.


  The Oracle Hospitality catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oracle Hospitality''s developer surface includes authentication, developer portal, documentation, support, sandbox, changelog, API reference, and 106 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 9
  name: Oracle Hospitality Rate Limits
  slug: oracle-hospitality-rate-limits
scopes:
- name: Oracle Hospitality Scopes
  scope_count: 1
  slug: oracle-hospitality-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 60.8
    developer_ergonomics: 70.8
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 81.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 65.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 78
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-hospitality/refs/heads/main/screenshots/oracle-hospitality-2026-08-07T190821.png
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
website: https://www.oracle.com/hospitality/
---
