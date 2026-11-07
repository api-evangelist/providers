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
  - scopes
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 2
  name: Znanylekarz Agentic Access
  operation_count: 44
  slug: znanylekarz-agentic-access
  summary_line: 44 operations · 24 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Addresses is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#addresses).
  name: ZnanyLekarz Addresses API
  phrasing_intents:
  - id: getAddresses
    intent: List a doctor's practice addresses
    question: Which addresses does a doctor practice at within a facility on ZnanyLekarz?
  - id: getAddress
    intent: Get one of a doctor's addresses
    question: How do I look up the details of one specific doctor address?
  - id: updateAddress
    intent: Change insurance support on a doctor's address
    question: Can I change whether a doctor's address accepts insured patients?
  - id: removeAddressIntegration
    intent: Remove the integration mark from an address
    question: How do I stop Docplanner treating an address as integrated with my system?
  phrasing_ops: 4
  slug: znanylekarz-addresses-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a API Notification Callbacks is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/callbacks/push-vs-pull.html).
  name: ZnanyLekarz API Notification Callbacks API
  phrasing_intents:
  - id: PushNotifications
    intent: Receive pushed event notifications at my endpoint
    question: What does the event payload look like when ZnanyLekarz pushes notifications to my endpoint?
  - id: PullNotification
    intent: Pull the next pending notification
    question: How do I fetch the oldest notification I haven't pulled yet?
  - id: PullMultipleNotification
    intent: Pull a batch of pending notifications
    question: Can I pull up to 100 notifications in one request?
  - id: ReleaseNotifications
    intent: Re-dispatch notifications that failed processing
    question: How can I get pushed notifications that weren't processed correctly sent again?
  phrasing_ops: 4
  slug: znanylekarz-api-notification-callbacks-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: 'More information on how we define what a Bookings is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#bookings). ## addBooking In order '
  name: ZnanyLekarz Bookings API
  phrasing_intents:
  - id: getBookings
    intent: List a doctor's bookings in a date range
    question: How do I see all appointments booked with a doctor at an address between two dates?
  - id: getBooking
    intent: View a single booking
    question: How do I look up the details of one specific appointment?
  - id: cancelBooking
    intent: Cancel a patient's booking
    question: How do I cancel a patient's appointment on ZnanyLekarz?
  - id: moveBooking
    intent: Reschedule a booking to a new time or doctor
    question: How do I reschedule an existing appointment to a different time?
  - id: confirmBooking
    intent: Confirm a patient's booking
    question: How do I mark an appointment as confirmed?
  - id: requestOpinion
    intent: Ask a patient by SMS to leave a review
    question: Can I send a patient an SMS asking them to review the doctor after a visit booked in our clinic software?
  phrasing_ops: 6
  slug: znanylekarz-bookings-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Calendar Breaks is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#calendar-breaks).
  name: ZnanyLekarz Calendar Breaks API
  phrasing_intents:
  - id: getCalendarBreaks
    intent: List calendar breaks in a date range
    question: Which breaks are blocked out in a doctor's calendar this month?
  - id: addCalendarBreak
    intent: Block out a break in a doctor's calendar
    question: How do I add a lunch break or day off to a doctor's calendar?
  - id: getCalendarBreak
    intent: View one calendar break
    question: How do I check the start and end of one specific calendar break?
  - id: moveCalendarBreak
    intent: Move a calendar break to a new time
    question: Can I shift an existing break to a different time range instead of recreating it?
  - id: deleteCalendarBreak
    intent: Delete a calendar break
    question: How do I remove a break so the doctor's time is open again?
  phrasing_ops: 5
  slug: znanylekarz-calendar-breaks-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: Simple operations on the calendar belonging to the address
  name: ZnanyLekarz Calendars API
  phrasing_intents:
  - id: getCalendar
    intent: Check an address's calendar status
    question: Is the online calendar turned on for a doctor's address?
  - id: enableCalendar
    intent: Turn on the calendar for an address
    question: How do I enable online booking on a doctor's address calendar?
  - id: disableCalendar
    intent: Turn off the calendar for an address
    question: How do I stop patients booking at an address by disabling its calendar?
  phrasing_ops: 3
  slug: znanylekarz-calendars-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Doctors is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#doctors).
  name: ZnanyLekarz Doctors API
  phrasing_intents:
  - id: getDoctors
    intent: List the doctors in a facility
    question: Which doctors work in my facility on ZnanyLekarz?
  - id: getDoctor
    intent: Get one doctor's details
    question: How do I look up a single doctor's profile in a facility?
  phrasing_ops: 2
  slug: znanylekarz-doctors-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Facility is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#facilities).
  name: ZnanyLekarz Facilities API
  phrasing_intents:
  - id: getFacilities
    intent: List my facilities
    question: Which facilities does my ZnanyLekarz integration have access to?
  - id: getFacility
    intent: Get one facility's details
    question: How do I fetch the details of a single facility?
  phrasing_ops: 2
  slug: znanylekarz-facilities-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Insurances is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#insurances).
  name: ZnanyLekarz Insurances API
  phrasing_intents:
  - id: getInsuranceProviders
    intent: List available insurance providers
    question: Which insurance companies are in the ZnanyLekarz dictionary?
  - id: getInsurancePlans
    intent: List an insurer's plans
    question: What plans does a given insurance provider offer?
  - id: getAddressInsuranceProviders
    intent: List insurers accepted at an address
    question: Which insurance providers does a doctor accept at a specific address?
  - id: addAddressInsuranceProvider
    intent: Add a new insurer to an address
    question: How do I start accepting a new insurance company at a doctor's address?
  - id: updateOrCreateAddressInsuranceProvider
    intent: Set an insurer's plans on an address
    question: How do I update the accepted plans for an insurer that may or may not already be on an address?
  - id: deleteAddressInsuranceProvider
    intent: Remove an insurer from an address
    question: How do I stop accepting an insurance provider at a doctor's address?
  phrasing_ops: 6
  slug: znanylekarz-insurances-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Patient Presence is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/patient-presence.html).
  name: ZnanyLekarz Patient Presence API
  phrasing_intents:
  - id: markPatientPresence
    intent: Mark a patient as present at a visit
    question: How do I record that a patient showed up for their appointment?
  - id: markPatientAbsence
    intent: Mark a patient as a no-show
    question: How do I record that a patient didn't turn up for their visit?
  phrasing_ops: 2
  slug: znanylekarz-patient-presence-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Services is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#services).
  name: ZnanyLekarz Services API
  phrasing_intents:
  - id: getServices
    intent: List the dictionary of services
    question: Which services are in the ZnanyLekarz service dictionary?
  - id: getAddressServices
    intent: List services offered at an address
    question: What services does a doctor offer at a particular address, with prices?
  - id: addAddressService
    intent: Add a service to a doctor's address
    question: How do I start offering a new service at a doctor's address?
  - id: getAddressService
    intent: Get one service offered at an address
    question: How do I see the price and duration of one service a doctor offers at an address?
  - id: updateAddressService
    intent: Update a service's price or settings
    question: How do I change the price of a service a doctor already offers at an address?
  - id: deleteAddressService
    intent: Remove a service from an address
    question: How do I stop offering a service at one of a doctor's addresses?
  phrasing_ops: 6
  slug: znanylekarz-services-api
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: More information on how we define what a Slots is, its use cases and more can be found [here](https://integrations.docplanner.com/guide/api-objects/resources.html#slots).
  name: ZnanyLekarz Slots API
  phrasing_intents:
  - id: getSlots
    intent: List free appointment slots at an address
    question: What free appointment times does a doctor have at an address next month?
  - id: replaceSlots
    intent: Replace an address's slots for date ranges
    question: How do I push my clinic's availability so it overrides existing slots?
  - id: bookSlot
    intent: Book a patient into a free slot
    question: How do I book an appointment for a patient in an open slot?
  - id: deleteSlots
    intent: Delete all slots on a given date
    question: How do I wipe a doctor's open slots for one day?
  phrasing_ops: 4
  slug: znanylekarz-slots-api
artifact_total: 59
asyncapis:
- description: ''
  name: Znanylekarz Notifications
  slug: znanylekarz-notifications
collections:
- collection_type: postman
  name: Docplanner Integrations API
  slug: postman-znanylekarz-integrations-api
common:
- group: agent
  href: https://artifacts.apis.io/znanylekarz/agentic-access/znanylekarz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/znanylekarz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/rules/znanylekarz-rules.yml
  title: ''
  type: Spectral
  url: rules/znanylekarz-rules.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/json-ld/znanylekarz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/znanylekarz-context.jsonld
- group: design
  href: https://artifacts.apis.io/znanylekarz/vocabulary/znanylekarz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/znanylekarz-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/znanylekarz/hosts/znanylekarz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/znanylekarz-hosts.yml
- group: other
  href: https://artifacts.apis.io/znanylekarz/vendors/znanylekarz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/znanylekarz-vendors.yml
- group: other
  href: https://artifacts.apis.io/znanylekarz/overlays/znanylekarz-integrations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/znanylekarz-integrations-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.znanylekarz.pl/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.docplanner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.docplanner.com/guide/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.docplanner.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.docplanner.com/guide/integration-process.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/run-collection/7fd8db9bb1fd14e0f0f7
- group: operate
  title: ''
  type: Support
  url: https://help.docplanner.com/
- group: company
  title: ''
  type: Blog
  url: https://www.znanylekarz.pl/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocPlanner
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.znanylekarz.pl/cennik/znanylekarz-dla-lekarzy
- group: start
  title: ''
  type: SignUp
  url: https://www.znanylekarz.pl/rejestracja-wybor
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.znanylekarz.pl/regulamin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.znanylekarz.pl/prywatnosc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docplanner.com/
- group: build
  href: https://artifacts.apis.io/znanylekarz/packages/znanylekarz-packages.yml
  title: ''
  type: Packages
  url: packages/znanylekarz-packages.yml
- group: build
  href: https://artifacts.apis.io/znanylekarz/packages/znanylekarz-packages.yml
  title: ''
  type: SDKs
  url: packages/znanylekarz-packages.yml
- group: agent
  href: https://artifacts.apis.io/znanylekarz/well-known/znanylekarz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/znanylekarz-well-known.yml
- group: auth
  href: https://artifacts.apis.io/znanylekarz/well-known/znanylekarz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/znanylekarz-security.txt
- group: auth
  href: https://artifacts.apis.io/znanylekarz/security/znanylekarz-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/znanylekarz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/znanylekarz/security/znanylekarz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/znanylekarz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/znanylekarz/security/znanylekarz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/znanylekarz-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/znanylekarz/authentication/znanylekarz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/znanylekarz-authentication.yml
- group: auth
  href: https://artifacts.apis.io/znanylekarz/scopes/znanylekarz-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/znanylekarz-scopes.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/conventions/znanylekarz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/znanylekarz-conventions.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/errors/znanylekarz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/znanylekarz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/conformance/znanylekarz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/znanylekarz-conformance.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/lifecycle/znanylekarz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/znanylekarz-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/znanylekarz/changelog/znanylekarz-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/znanylekarz-changelog.yml
- group: design
  href: https://artifacts.apis.io/znanylekarz/data-model/znanylekarz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/znanylekarz-data-model.yml
- group: start
  href: https://artifacts.apis.io/znanylekarz/sandbox/znanylekarz-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/znanylekarz-sandbox.yml
- group: build
  href: https://artifacts.apis.io/znanylekarz/examples/znanylekarz-examples.yml
  title: ''
  type: Examples
  url: examples/znanylekarz-examples.yml
- group: commercial
  href: https://artifacts.apis.io/znanylekarz/plans/znanylekarz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/znanylekarz-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/znanylekarz/rate-limits/znanylekarz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/znanylekarz-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/znanylekarz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-05'
description: ZnanyLekarz is the Polish healthcare marketplace and practice-management platform operated by Docplanner Group, connecting patients with over 146,000 listed doctors and equipping medical practices with online booking, calendar management, appointment reminders, patient reviews, e-prescriptions, video consultations and online payments. ZnanyLekarz.pl is the founding brand of the Docplanner Group and the Polish locale of the group's marketplace, which also trades as Doctoralia, MioDottore, Jameda, Doktor Takvimi and Znamylekar. Its public developer surface is the Docplanner Integrations API — an OAuth 2.0 REST API served on the www.znanylekarz.pl host that lets medical-software vendors synchronise facilities, doctors, addresses, services, insurance providers, calendars, breaks, slots and bookings, and receive push or pull event notifications when patients book, move, confirm or cancel visits.
finops:
- has_sources: true
  method: derived
  name: Znanylekarz Finops
  primary_unit: subscription
  service_category: ''
  slug: znanylekarz-finops
  template: false
image: https://platform.docplanner.com/img/pl/open-graph/og-v0.png
json_schemas:
- name: AddAddressInsuranceProviderRequest
  property_count: 2
  slug: znanylekarz-add-address-insurance-provider-request
- name: AddAddressServiceRequest
  property_count: 8
  slug: znanylekarz-add-address-service-request
- name: AddCalendarBreakRequest
  property_count: 4
  slug: znanylekarz-add-calendar-break-request
- name: AddressInsuranceProviders
  property_count: 1
  slug: znanylekarz-address-insurance-providers
- name: Address
  property_count: 10
  slug: znanylekarz-address
- name: AddressService
  property_count: 11
  slug: znanylekarz-address-service
- name: AddressServices
  property_count: 1
  slug: znanylekarz-address-services
- name: Addresses
  property_count: 1
  slug: znanylekarz-addresses
- name: BookSlotRequest
  property_count: 9
  slug: znanylekarz-book-slot-request
- name: Booking
  property_count: 18
  slug: znanylekarz-booking
- name: Bookings
  property_count: 5
  slug: znanylekarz-bookings
- name: CalendarBreak
  property_count: 4
  slug: znanylekarz-calendar-break
- name: CalendarBreaks
  property_count: 1
  slug: znanylekarz-calendar-breaks
- name: Calendar
  property_count: 1
  slug: znanylekarz-calendar
- name: CancelBookingRequest
  property_count: 1
  slug: znanylekarz-cancel-booking-request
- name: ConfirmBookingRequest
  property_count: 1
  slug: znanylekarz-confirm-booking-request
- name: Doctor
  property_count: 6
  slug: znanylekarz-doctor
- name: Doctors
  property_count: 1
  slug: znanylekarz-doctors
- name: Facilities
  property_count: 1
  slug: znanylekarz-facilities
- name: Facility
  property_count: 3
  slug: znanylekarz-facility
- name: InsurancePlans
  property_count: 1
  slug: znanylekarz-insurance-plans
- name: InsuranceProviders
  property_count: 1
  slug: znanylekarz-insurance-providers
- name: MoveBookingRequest
  property_count: 4
  slug: znanylekarz-move-booking-request
- name: MoveCalendarBreakRequest
  property_count: 2
  slug: znanylekarz-move-calendar-break-request
- name: Notification
  property_count: 3
  slug: znanylekarz-notification
- name: OpinionRequest
  property_count: 1
  slug: znanylekarz-opinion-request
- name: PullMultipleNotificationsResponse
  property_count: 2
  slug: znanylekarz-pull-multiple-notifications-response
- name: ReplaceSlotsRequest
  property_count: 1
  slug: znanylekarz-replace-slots-request
- name: Services
  property_count: 1
  slug: znanylekarz-services
- name: Slots
  property_count: 1
  slug: znanylekarz-slots
- name: UpdateAddressRequest
  property_count: 1
  slug: znanylekarz-update-address-request
- name: UpdateAddressServiceRequest
  property_count: 7
  slug: znanylekarz-update-address-service-request
- name: UpdateOrCreateAddressInsuranceProviderRequest
  property_count: 2
  slug: znanylekarz-update-or-create-address-insurance-provider-request
jsonld:
- class_count: 81
  name: Znanylekarz Context
  property_count: 85
  slug: znanylekarz-context
layout: provider
modified: '2026-09-05'
name: ZnanyLekarz
nav: Providers
network: true
overview: 'ZnanyLekarz publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, API Notification Callbacks API, Bookings API, and 8 more. Tagged areas include Company, Healthcare, Health Tech, Appointments, and Booking.


  The ZnanyLekarz catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ZnanyLekarz''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Znanylekarz Plans Pricing
  plan_count: 4
  slug: znanylekarz-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Znanylekarz Rate Limits
  slug: znanylekarz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: ZnanyLekarz API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 2
  slug: znanylekarz-rules
scopes:
- name: Znanylekarz Scopes
  scope_count: 1
  slug: znanylekarz-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 75.8
  coverage:
    artifact_dirs: 36
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 73.4
    developer_ergonomics: 75.6
    discoverability: 66.1
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 75.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/znanylekarz/znanylekarz-2026-10-11T195534.png
security:
- kind: authentication
  name: Znanylekarz Authentication
  slug: znanylekarz-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Znanylekarz Domain Security
  slug: znanylekarz-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Znanylekarz Vulnerability Disclosure
  slug: znanylekarz-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: znanylekarz-consume-notifications
  slug: znanylekarz-consume-notifications
- name: znanylekarz-manage-bookings
  slug: znanylekarz-manage-bookings
- name: znanylekarz-publish-availability
  slug: znanylekarz-publish-availability
slug: znanylekarz
tags:
- Company
- Healthcare
- Health Tech
- Appointments
- Booking
- Medical
- Marketplace
- Doctors
- Scheduling
- Poland
- Practice Management
- Telehealth
website: https://www.znanylekarz.pl/
---
