---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 653
  human_in_the_loop: 18
  name: Tui Group Agentic Access
  operation_count: 1261
  slug: tui-group-agentic-access
  summary_line: 1261 operations · 653 acting · 18 human-in-the-loop
api_count: 21
apis:
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The account API from TUI Group — 5 operation(s) for account.
  name: TUI Group Account API
  slug: tui-group-account-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The AirlineProfile API from TUI Group — 2 operation(s) for airlineprofile.
  name: TUI Group Airline Profile API
  slug: tui-group-airlineprofile-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The AirShopping API from TUI Group — 2 operation(s) for airshopping.
  name: TUI Group Air Shopping API
  slug: tui-group-airshopping-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The apisMessage API from TUI Group — 1 operation(s) for apismessage.
  name: TUI Group APIS Message API
  slug: tui-group-apismessage-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The apo API from TUI Group — 2 operation(s) for apo.
  name: TUI Group Apo API
  slug: tui-group-apo-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Auth API from TUI Group — 2 operation(s) for auth.
  name: TUI Group Auth API
  slug: tui-group-auth-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The availability API from TUI Group — 6 operation(s) for availability.
  name: TUI Group Availability API
  slug: tui-group-availability-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The baggage API from TUI Group — 6 operation(s) for baggage.
  name: TUI Group Baggage API
  slug: tui-group-baggage-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The bagTag API from TUI Group — 1 operation(s) for bagtag.
  name: TUI Group Bag Tag API
  slug: tui-group-bagtag-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The boarding API from TUI Group — 5 operation(s) for boarding.
  name: TUI Group Boarding API
  slug: tui-group-boarding-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The boardingDevices API from TUI Group — 1 operation(s) for boardingdevices.
  name: TUI Group Boarding Devices API
  slug: tui-group-boardingdevices-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/addons API from TUI Group — 3 operation(s) for booking/addons.
  name: TUI Group Booking/addons API
  slug: tui-group-booking-addons-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking API from TUI Group — 53 operation(s) for booking.
  name: TUI Group Booking API
  slug: tui-group-booking-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/boardingpasses API from TUI Group — 4 operation(s) for booking/boardingpasses.
  name: TUI Group Booking/boardingpasses API
  slug: tui-group-booking-boardingpasses-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/checkin API from TUI Group — 10 operation(s) for booking/checkin.
  name: TUI Group Booking/checkin API
  slug: tui-group-booking-checkin-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/contacts API from TUI Group — 5 operation(s) for booking/contacts.
  name: TUI Group Booking/contacts API
  slug: tui-group-booking-contacts-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/history API from TUI Group — 9 operation(s) for booking/history.
  name: TUI Group Booking/history API
  slug: tui-group-booking-history-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/journeys API from TUI Group — 18 operation(s) for booking/journeys.
  name: TUI Group Booking/journeys API
  slug: tui-group-booking-journeys-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/passengers API from TUI Group — 50 operation(s) for booking/passengers.
  name: TUI Group Booking/passengers API
  slug: tui-group-booking-passengers-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/payments API from TUI Group — 62 operation(s) for booking/payments.
  name: TUI Group Booking/payments API
  slug: tui-group-booking-payments-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/retrieve API from TUI Group — 5 operation(s) for booking/retrieve.
  name: TUI Group Booking/retrieve API
  slug: tui-group-booking-retrieve-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/seatmaps API from TUI Group — 3 operation(s) for booking/seatmaps.
  name: TUI Group Booking/seatmaps API
  slug: tui-group-booking-seatmaps-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/seats API from TUI Group — 8 operation(s) for booking/seats.
  name: TUI Group Booking/seats API
  slug: tui-group-booking-seats-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/segments API from TUI Group — 7 operation(s) for booking/segments.
  name: TUI Group Booking/segments API
  slug: tui-group-booking-segments-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The booking/ssrs API from TUI Group — 12 operation(s) for booking/ssrs.
  name: TUI Group Booking/ssrs API
  slug: tui-group-booking-ssrs-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Bookings API from TUI Group — 71 operation(s) for bookings.
  name: TUI Group Bookings API
  slug: tui-group-bookings-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The bundles API from TUI Group — 3 operation(s) for bundles.
  name: TUI Group Bundles API
  slug: tui-group-bundles-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The checkin API from TUI Group — 4 operation(s) for checkin.
  name: TUI Group Checkin API
  slug: tui-group-checkin-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The CheckInHandler API from TUI Group — 2 operation(s) for checkinhandler.
  name: TUI Group Check In Handler API
  slug: tui-group-checkinhandler-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The collection API from TUI Group — 3 operation(s) for collection.
  name: TUI Group Collection API
  slug: tui-group-collection-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The configuration API from TUI Group — 1 operation(s) for configuration.
  name: TUI Group Configuration API
  slug: tui-group-configuration-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The contacts API from TUI Group — 1 operation(s) for contacts.
  name: TUI Group Contacts API
  slug: tui-group-contacts-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The contents API from TUI Group — 1 operation(s) for contents.
  name: TUI Group Contents API
  slug: tui-group-contents-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Add a stay API from TUI Group — 1 operation(s) for cruise add a stay.
  name: TUI Group Cruise Add a stay API
  slug: tui-group-cruise-add-a-stay-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Alternate Cabin and Board Search API from TUI Group — 1 operation(s) for cruise alternate cabin and board search.
  name: TUI Group Cruise Alternate Cabin and Board Search API
  slug: tui-group-cruise-alternate-cabin-and-board-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Alternate Flight Variant Search API from TUI Group — 1 operation(s) for cruise alternate flight variant search.
  name: TUI Group Cruise Alternate Flight Variant Search API
  slug: tui-group-cruise-alternate-flight-variant-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Alternate Stay Variant Search API from TUI Group — 1 operation(s) for cruise alternate stay variant search.
  name: TUI Group Cruise Alternate Stay Variant Search API
  slug: tui-group-cruise-alternate-stay-variant-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Cabin availability API from TUI Group — 1 operation(s) for cruise cabin availability.
  name: TUI Group Cruise Cabin availability API
  slug: tui-group-cruise-cabin-availability-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Search API from TUI Group — 1 operation(s) for cruise search.
  name: TUI Group Cruise Search API
  slug: tui-group-cruise-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Cruise Unique Search API from TUI Group — 1 operation(s) for cruise unique search.
  name: TUI Group Cruise Unique Search API
  slug: tui-group-cruise-unique-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The currency API from TUI Group — 1 operation(s) for currency.
  name: TUI Group Currency API
  slug: tui-group-currency-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The deviceManagers API from TUI Group — 1 operation(s) for devicemanagers.
  name: TUI Group Device Managers API
  slug: tui-group-devicemanagers-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The disruption API from TUI Group — 5 operation(s) for disruption.
  name: TUI Group Disruption API
  slug: tui-group-disruption-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The documents API from TUI Group — 2 operation(s) for documents.
  name: TUI Group Documents API
  slug: tui-group-documents-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The download API from TUI Group — 2 operation(s) for download.
  name: TUI Group Download API
  slug: tui-group-download-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The equipment API from TUI Group — 2 operation(s) for equipment.
  name: TUI Group Equipment API
  slug: tui-group-equipment-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The eTickets API from TUI Group — 4 operation(s) for etickets.
  name: TUI Group E Tickets API
  slug: tui-group-etickets-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The fareRules API from TUI Group — 2 operation(s) for farerules.
  name: TUI Group Fare Rules API
  slug: tui-group-farerules-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Flights API from TUI Group — 1 operation(s) for flights.
  name: TUI Group Flights API
  slug: tui-group-flights-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The G7 content API from TUI Group — 1 operation(s) for g7 content.
  name: TUI Group G7 content API
  slug: tui-group-g7-content-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The graph API from TUI Group — 3 operation(s) for graph.
  name: TUI Group Graph API
  slug: tui-group-graph-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Graphql API from TUI Group — 1 operation(s) for graphql.
  name: TUI Group Graphql API
  slug: tui-group-graphql-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The health API from TUI Group — 3 operation(s) for health.
  name: TUI Group Health API
  slug: tui-group-health-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The HolidayOffersController USL API API from TUI Group — 1 operation(s) for holidayofferscontroller usl api.
  name: TUI Group HolidayOffersController USL API
  slug: tui-group-holidayofferscontroller-usl-api-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: Operations around hotel availability details
  name: TUI Group Hotel Availability API
  slug: tui-group-hotel-availability-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: Operations to manage hotel inventory related information
  name: TUI Group Hotel Inventory API
  slug: tui-group-hotel-inventory-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The inventory API from TUI Group — 7 operation(s) for inventory.
  name: TUI Group Inventory API
  slug: tui-group-inventory-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The legs API from TUI Group — 4 operation(s) for legs.
  name: TUI Group Legs API
  slug: tui-group-legs-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Live Search Packages (Beta) API from TUI Group — 5 operation(s) for live search packages (beta).
  name: TUI Group Live Search Packages (Beta) API
  slug: tui-group-live-search-packages-beta-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The logs API from TUI Group — 2 operation(s) for logs.
  name: TUI Group Logs API
  slug: tui-group-logs-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The manifest API from TUI Group — 11 operation(s) for manifest.
  name: TUI Group Manifest API
  slug: tui-group-manifest-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The messages API from TUI Group — 5 operation(s) for messages.
  name: TUI Group Messages API
  slug: tui-group-messages-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Ndc API from TUI Group — 1 operation(s) for ndc.
  name: TUI Group Ndc API
  slug: tui-group-ndc-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The OfferPrice API from TUI Group — 2 operation(s) for offerprice.
  name: TUI Group Offer Price API
  slug: tui-group-offerprice-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: Operations for retrieving holiday offers and availability
  name: TUI Group Offers API
  slug: tui-group-offers-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The oneTimeTravelNotifications API from TUI Group — 4 operation(s) for onetimetravelnotifications.
  name: TUI Group One Time Travel Notifications API
  slug: tui-group-onetimetravelnotifications-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The OrderChange API from TUI Group — 2 operation(s) for orderchange.
  name: TUI Group Order Change API
  slug: tui-group-orderchange-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The OrderCreate API from TUI Group — 2 operation(s) for ordercreate.
  name: TUI Group Order Create API
  slug: tui-group-ordercreate-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The OrderQuote API from TUI Group — 2 operation(s) for orderquote.
  name: TUI Group Order Quote API
  slug: tui-group-orderquote-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The OrderReshop API from TUI Group — 2 operation(s) for orderreshop.
  name: TUI Group Order Reshop API
  slug: tui-group-orderreshop-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The OrderRetrieve API from TUI Group — 2 operation(s) for orderretrieve.
  name: TUI Group Order Retrieve API
  slug: tui-group-orderretrieve-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The organizationGroup API from TUI Group — 1 operation(s) for organizationgroup.
  name: TUI Group Organization Group API
  slug: tui-group-organizationgroup-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The organizationGroups API from TUI Group — 3 operation(s) for organizationgroups.
  name: TUI Group Organization Groups API
  slug: tui-group-organizationgroups-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The organizations API from TUI Group — 2 operation(s) for organizations.
  name: TUI Group Organizations API
  slug: tui-group-organizations-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The organizations2 API from TUI Group — 35 operation(s) for organizations2.
  name: TUI Group Organizations2 API
  slug: tui-group-organizations2-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Ota API from TUI Group — 12 operation(s) for ota.
  name: TUI Group Ota API
  slug: tui-group-ota-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Packages API from TUI Group — 1 operation(s) for packages.
  name: TUI Group Packages API
  slug: tui-group-packages-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Partner Content Api (Beta) API from TUI Group — 2 operation(s) for partner content api (beta).
  name: TUI Group Partner Content Api (Beta) API
  slug: tui-group-partner-content-api-beta-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The passengers API from TUI Group — 1 operation(s) for passengers.
  name: TUI Group Passengers API
  slug: tui-group-passengers-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The payments API from TUI Group — 1 operation(s) for payments.
  name: TUI Group Payments API
  slug: tui-group-payments-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The persons API from TUI Group — 41 operation(s) for persons.
  name: TUI Group Persons API
  slug: tui-group-persons-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Price calendar search API from TUI Group — 1 operation(s) for price calendar search.
  name: TUI Group Price calendar search API
  slug: tui-group-price-calendar-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The pricing API from TUI Group — 2 operation(s) for pricing.
  name: TUI Group Pricing API
  slug: tui-group-pricing-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The printers API from TUI Group — 13 operation(s) for printers.
  name: TUI Group Printers API
  slug: tui-group-printers-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The printers/reports API from TUI Group — 41 operation(s) for printers/reports.
  name: TUI Group Printers/reports API
  slug: tui-group-printers-reports-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The promotions API from TUI Group — 3 operation(s) for promotions.
  name: TUI Group Promotions API
  slug: tui-group-promotions-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The queues API from TUI Group — 9 operation(s) for queues.
  name: TUI Group Queues API
  slug: tui-group-queues-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The redis API from TUI Group — 2 operation(s) for redis.
  name: TUI Group Redis API
  slug: tui-group-redis-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The resources API from TUI Group — 159 operation(s) for resources.
  name: TUI Group Resources API
  slug: tui-group-resources-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Route Feed API from TUI Group — 1 operation(s) for route feed.
  name: TUI Group Route Feed API
  slug: tui-group-route-feed-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The scanners API from TUI Group — 1 operation(s) for scanners.
  name: TUI Group Scanners API
  slug: tui-group-scanners-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Search API from TUI Group — 1 operation(s) for search.
  name: TUI Group Search API
  slug: tui-group-search-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The SeatAvailability API from TUI Group — 4 operation(s) for seatavailability.
  name: TUI Group Seat Availability API
  slug: tui-group-seatavailability-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The seatmaps API from TUI Group — 2 operation(s) for seatmaps.
  name: TUI Group Seatmaps API
  slug: tui-group-seatmaps-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The seats API from TUI Group — 3 operation(s) for seats.
  name: TUI Group Seats API
  slug: tui-group-seats-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The segments API from TUI Group — 1 operation(s) for segments.
  name: TUI Group Segments API
  slug: tui-group-segments-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The ServiceList API from TUI Group — 4 operation(s) for servicelist.
  name: TUI Group Service List API
  slug: tui-group-servicelist-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The settings API from TUI Group — 37 operation(s) for settings.
  name: TUI Group Settings API
  slug: tui-group-settings-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Soap API from TUI Group — 1 operation(s) for soap.
  name: TUI Group Soap API
  slug: tui-group-soap-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The ssrs API from TUI Group — 1 operation(s) for ssrs.
  name: TUI Group Ssrs API
  slug: tui-group-ssrs-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Supply API from TUI Group — 1 operation(s) for supply.
  name: TUI Group Supply API
  slug: tui-group-supply-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The timestamp API from TUI Group — 2 operation(s) for timestamp.
  name: TUI Group Timestamp API
  slug: tui-group-timestamp-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The token API from TUI Group — 13 operation(s) for token.
  name: TUI Group Token API
  slug: tui-group-token-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The TravelMessage API from TUI Group — 10 operation(s) for travelmessage.
  name: TUI Group Travel Message API
  slug: tui-group-travelmessage-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The trip API from TUI Group — 38 operation(s) for trip.
  name: TUI Group Trip API
  slug: tui-group-trip-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The Unique offer USL API API from TUI Group — 1 operation(s) for unique offer usl api.
  name: TUI Group Unique offer USL API
  slug: tui-group-unique-offer-usl-api-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The user API from TUI Group — 11 operation(s) for user.
  name: TUI Group User API
  slug: tui-group-user-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The users API from TUI Group — 42 operation(s) for users.
  name: TUI Group Users API
  slug: tui-group-users-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The utilities API from TUI Group — 1 operation(s) for utilities.
  name: TUI Group Utilities API
  slug: tui-group-utilities-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The verifiedTravelDocuments API from TUI Group — 3 operation(s) for verifiedtraveldocuments.
  name: TUI Group Verified Travel Documents API
  slug: tui-group-verifiedtraveldocuments-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The voucherIssuance API from TUI Group — 3 operation(s) for voucherissuance.
  name: TUI Group Voucher Issuance API
  slug: tui-group-voucherissuance-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The vouchers API from TUI Group — 11 operation(s) for vouchers.
  name: TUI Group Vouchers API
  slug: tui-group-vouchers-api
- baseURL: https://prod.api.tui/flight/newskies/rest
  baseurl_source: declared
  description: The watchList API from TUI Group — 4 operation(s) for watchlist.
  name: TUI Group Watch List API
  slug: tui-group-watchlist-api
artifact_total: 139
collections:
- collection_type: open
  name: TravelMessage.v31
  slug: open-tui-group-tui-b2bota-g7-travelmessage
- collection_type: open
  name: CheckInHandler Service API
  slug: open-tui-group-tui-checkinhandler-service-api
- collection_type: open
  name: TUI Cruise Booking APIs
  slug: open-tui-group-tui-cruise-booking-apis
- collection_type: open
  name: Cruise Cabin Availability
  slug: open-tui-group-tui-cruise-cabin-availability
- collection_type: open
  name: TUI Cruise Price and Availability.
  slug: open-tui-group-tui-cruise-price-and-availability
- collection_type: open
  name: NSKCC Availability Search API
  slug: open-tui-group-tui-flight-availability-search-api
- collection_type: open
  name: flight-ndc-gateway-navitaire
  slug: open-tui-group-tui-flight-ndc-gateway
- collection_type: open
  name: HolidayOffersController API
  slug: open-tui-group-tui-holiday-offers-controller-api
- collection_type: open
  name: Meta Partner Package Live Search
  slug: open-tui-group-tui-meta-partner-package-live-search
- collection_type: open
  name: Meta Partner Packages & Flights
  slug: open-tui-group-tui-meta-partner-packages-flights
- collection_type: open
  name: Meta-Search-Generic API
  slug: open-tui-group-tui-meta-search-generic-api
- collection_type: open
  name: NewSkies-Digital-Api
  slug: open-tui-group-tui-newskies-digital-api
- collection_type: open
  name: NewSkies-GoNow-Api
  slug: open-tui-group-tui-newskies-gonow-api
- collection_type: open
  name: NewSkies Payment API
  slug: open-tui-group-tui-newskies-payment-api
- collection_type: open
  name: TUI NewSkies PriceFile Api
  slug: open-tui-group-tui-newskies-pricefile-api
- collection_type: open
  name: OTA Content API
  slug: open-tui-group-tui-ota-content-api
- collection_type: open
  name: Partner Content API
  slug: open-tui-group-tui-partner-content-api
- collection_type: open
  name: WallDy API
  slug: open-tui-group-tui-search-walldy-api
- collection_type: open
  name: Ship Content API
  slug: open-tui-group-tui-ship-content-api
- collection_type: open
  name: Supply
  slug: open-tui-group-tui-supply
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tui-group-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-newskies-digital-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-newskies-gonow-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-newskies-payment-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-flight-availability-search-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-newskies-pricefile-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-checkinhandler-service-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-flight-ota-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-ota-content-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-search-walldy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-holiday-offers-controller-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-meta-search-generic-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-partner-content-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tui-group-tui-ship-content-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tui-group-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tui-group-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tui-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.tui.com/p/Policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tui-group-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tui-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tui-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tui-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tui-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tui-group-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tui-group-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tui-group-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tui-group-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tui-group-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tui-group-rate-limits.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tui-group-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tui-group-security.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tui-group-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tui-group-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tui-group-packages.yml
- group: design
  title: ''
  type: Components
  url: components/tui-group-components.yml
- group: build
  title: ''
  type: Postman
  url: https://developer.tui/api-catalog/flight-ndc-gateway-navitaire/postman-collection
- group: docs
  title: ''
  type: XMLSchema
  url: schemas/tui-b2bota-g7-travelmessage-v31.xsd
- group: company
  title: ''
  type: Website
  url: https://www.tuigroup.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tui/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tui/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tui/api-catalog
- group: start
  title: ''
  type: SignUp
  url: https://signup.developer.tui
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tui/docs/general/oauth2
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.tui/docs/getting-started_technical-integration
- group: other
  title: ''
  type: Environments
  url: https://developer.tui/docs/getting-started_environments
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tui/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developer.tui/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.tui/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.tui/privacy-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://vdp.tui.com/p/Policy
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.tui.com/.well-known/security.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuigroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tuigroup/
- group: other
  title: ''
  type: Email
  url: mailto:apiplatform@tui.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.tuigroup.com/en/investors
created: '2026-07-28'
description: 'TUI Group is the world''s largest integrated leisure tourism business — a vertically integrated tour operator that owns the hotels, the cruise ships, the airlines and the retail brands it sells through, serving 34.7 million customers a year across tour operators in 18 countries. The United Kingdom is its largest single source market: TUI UK & Ireland and the UK-registered carrier TUI Airways sit at the centre of the group, alongside Marella Cruises, TUI Musement and the TUI Blue, Robinson and TUI Magic Life hotel brands. The group is domiciled in Hannover, Germany and listed on the Frankfurt MDAX, having ended its London primary listing in 2023. TUI sits at the supply end of the travel distribution chain rather than the intermediation end — it is the principal that creates package holidays, not a GDS or a channel manager — and it distributes chiefly through its own retail estate and websites, supplemented by B2B feeds to travel agents, OTAs and metasearch partners. On the API
  front TUI runs a real, publicly readable developer portal at developer.tui fronted by Apigee X, with 21 documented API products covering flight shopping and booking, departure control, packages, accommodation content, cruise and metasearch distribution. The documentation is genuinely open — base URLs, endpoints, auth flows, quota tiers, downloadable Postman collections and a public OpenAPI 3.0 document for every one of the 21 products (1,261 operations in total, served from the portal''s Swagger UI) are all published without a login — but the runtime is not: every API product requires a partner-manager approval, most airline APIs additionally require a Navitaire New Skies agent profile and a production IP whitelist, and the TUI fly OTA API states plainly that step one is to conclude a contract. There is no self-serve key, no published developer terms of use (the portal''s terms page is still unfilled lorem-ipsum placeholder text), no idempotency contract on any booking or payment operation,
  no status page, no event or webhook surface, and no documented bulk-export or data-portability operation for a departing partner.'
layout: provider
modified: '2026-07-28'
name: TUI Group
nav: Providers
network: true
overview: 'TUI Group publishes 113 APIs on the [APIs.io](https://apis.io/) network, including Account API, Airline Profile API, Air Shopping API, and 110 more. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Tour Operator.


  TUI Group''s developer surface includes authentication, changelog, sandbox, documentation, API reference, signup flow, getting-started guide, and 49 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 6
  name: Tui Group Rate Limits
  slug: tui-group-rate-limits
scopes:
- name: Tui Group Scopes
  scope_count: 1
  slug: tui-group-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 54.1
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 113
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tui-group/refs/heads/main/screenshots/tui-group-2026-08-17T082459.png
security:
- kind: authentication
  name: Tui Group Authentication
  slug: tui-group-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Tui Group Domain Security
  slug: tui-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tui Group Vulnerability Disclosure
  slug: tui-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tui-group
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Tour Operator
- Distribution
- NDC
- Hospitality
- Hotels
- Cruise
- Booking
- Packages
- Metasearch
website: https://www.tuigroup.com/en
---
