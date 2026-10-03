---
access_model:
  confidence: medium
  label: Paid · Partner / sandbox onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - documentation
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 455
  human_in_the_loop: 0
  name: Elation Health Agentic Access
  operation_count: 846
  slug: elation-health-agentic-access
  summary_line: 846 operations · 455 acting
api_count: 19
apis:
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Allergy and drug intolerance tracking
  name: Elation Health Allergies API
  phrasing_intents:
  - id: update-allergy
    intent: Replace an allergy (legacy PUT)
    question: Can I overwrite a patient's allergy record through the legacy PUT?
  - id: get-allergy
    intent: Get an allergy (legacy endpoint)
    question: How do I read one allergy entry by id on the legacy allergies path?
  - id: delete-allergy
    intent: Delete an allergy (legacy endpoint)
    question: How do I remove an allergy from a chart using the legacy endpoint?
  - id: allergies_partial_update
    intent: Update an allergy's status or notes (legacy PATCH)
    question: Can I mark an allergy inactive with the legacy PATCH call?
  - id: find-allergies
    intent: Find a patient's allergies (legacy endpoint)
    question: How do I see all allergies recorded for a patient on the legacy path?
  - id: create-allergy
    intent: Record an allergy (legacy endpoint)
    question: How do I add a new allergy to a patient's chart through the legacy endpoint?
  - id: allergies_list
    intent: List allergies (v2.0)
    question: What allergies does a patient have according to the 2.0 API?
  - id: allergies_create
    intent: Record an allergy (v2.0)
    question: How do I add an allergy with a Medi-Span id in the 2.0 API?
  phrasing_ops: 12
  slug: elation-allergies-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Scheduling and appointment management
  name: Elation Health Appointments API
  phrasing_intents:
  - id: delete-event
    intent: Delete a calendar event (legacy endpoint)
    question: How do I remove a scheduled event using the legacy appointments API?
  - id: get-event
    intent: Look up a calendar event (legacy endpoint)
    question: How do I pull up one scheduled event by its id on the legacy appointments path?
  - id: update-appointment
    intent: Replace a calendar event (legacy PUT)
    question: Can I overwrite an entire event record through the legacy appointments PUT?
  - id: update-event
    intent: Patch a calendar event (legacy PATCH)
    question: Can I change just part of an event with the legacy PATCH call?
  - id: create-event
    intent: Book a calendar event (legacy endpoint)
    question: How do I schedule a patient event with a physician through the legacy appointments API?
  - id: testinput
    intent: Find calendar events by slot type (legacy)
    question: How can I search the calendar for events of one time slot type?
  - id: find-appointment-rooms
    intent: List appointment rooms for a practice
    question: Which exam rooms can appointments be booked into at my practice?
  - id: update-appointment-slot
    intent: Assign a patient to an appointment slot
    question: Can I put a patient into an open appointment slot?
  phrasing_ops: 23
  slug: elation-appointments-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: OAuth2 token management
  name: Elation Health Authentication API
  phrasing_intents:
  - id: getToken
    intent: Get an OAuth2 access token
    question: How do I get an access token to call the Elation API?
  phrasing_ops: 1
  slug: elation-authentication-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Billing codes and bill management
  name: Elation Health Billing API
  phrasing_intents:
  - id: billing_codes_list
    intent: List billing codes
    question: Which billing codes are set up in my practice?
  - id: billing_codes_create
    intent: Add a billing code
    question: How do I add a new billing code with a fee?
  - id: billing_codes_retrieve
    intent: Get a billing code
    question: How do I look up one billing code by id?
  - id: billing_codes_update
    intent: Replace a billing code
    question: Can I overwrite a billing code's code and description in full?
  - id: billing_codes_partial_update
    intent: Change a billing code's fee
    question: Can I change the fee on a billing code without replacing it?
  - id: billing_codes_destroy
    intent: Delete a billing code
    question: How do I remove a billing code we no longer bill?
  phrasing_ops: 6
  slug: elation-billing-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Insurance company, plan, and policy management
  name: Elation Health Insurance API
  phrasing_intents:
  - id: insurance_companies_list
    intent: List insurance companies
    question: Which insurance companies are set up in the system?
  - id: insurance_companies_create
    intent: Add an insurance company
    question: How do I add a new insurance carrier with its payer id?
  - id: insurance_companies_retrieve
    intent: Get one insurance company
    question: What contact details are stored for a given insurance company?
  - id: insurance_companies_update
    intent: Replace an insurance company record
    question: Which call fully replaces an insurance company's details?
  - id: insurance_companies_partial_update
    intent: Update an insurance company's contact info
    question: Can I change just a carrier's phone or fax number?
  - id: insurance_companies_destroy
    intent: Delete an insurance company
    question: Can I delete a duplicate insurance company?
  phrasing_ops: 6
  slug: elation-insurance-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Laboratory order management
  name: Elation Health Lab Orders API
  phrasing_intents:
  - id: find-lab-orders
    intent: Find lab orders (legacy endpoint)
    question: Where can I look up a patient's lab orders on the legacy unversioned endpoint?
  - id: create-lab-order
    intent: Place a lab order (legacy endpoint)
    question: How do I place a new lab order for a patient through the legacy endpoint?
  - id: retrieve-the-printable-lab-order-view
    intent: Get a printable lab order (legacy path)
    question: Can I get a print-ready view of a lab order from the legacy printable path?
  - id: get-lab-order
    intent: Get a lab order (legacy endpoint)
    question: Can I fetch a single lab order by id on the legacy unversioned path?
  - id: update-lab-order
    intent: Replace a lab order (legacy PUT)
    question: Can I overwrite a whole lab order through the legacy PUT endpoint?
  - id: update-lab-order-1
    intent: Edit fields on a lab order (legacy PATCH)
    question: Can I change just the facility or follow-up method on a lab order with the legacy PATCH?
  - id: delete-lab-order
    intent: Delete a lab order (legacy endpoint)
    question: How do I remove a lab order using the legacy unversioned endpoint?
  - id: lab_orders_list
    intent: List lab orders (v2.0)
    question: Is it possible to page through all lab orders in a practice with the 2.0 API?
  phrasing_ops: 18
  slug: elation-lab-orders-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Medication and prescription management
  name: Elation Health Medications API
  phrasing_intents:
  - id: find-medications
    intent: Find a patient's medications (legacy)
    question: How can I search a patient's medications on the legacy endpoint?
  - id: create-medication
    intent: Prescribe or document a medication (legacy)
    question: How do I add a prescription to a chart through the legacy medications API?
  - id: get-medication
    intent: Look up a medication (legacy)
    question: How do I fetch one medication entry from the legacy endpoint?
  - id: medications_destroy
    intent: Delete a medication (legacy)
    question: Can I delete a medication using the legacy unversioned path?
  - id: medications_list
    intent: List medications
    question: What medications is a patient on in Elation?
  - id: medications_create
    intent: Add a medication to a chart
    question: How do I write a prescription for a patient with API v2?
  - id: deleteApi20MedicationsById
    intent: Delete a medication
    question: How do I delete a medication entered in error in v2?
  - id: medications_retrieve
    intent: Get one medication
    question: How do I see the directions and refills on one medication?
  phrasing_ops: 8
  slug: elation-medications-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Secure direct messaging
  name: Elation Health Messaging API
  phrasing_intents:
  - id: message_threads_list
    intent: List secure message threads
    question: How do I see all the secure message threads in the practice?
  - id: message_threads_create
    intent: Start a secure message thread
    question: How do I start a new secure message conversation about a patient?
  - id: message_threads_retrieve
    intent: Retrieve a secure message thread
    question: How do I open one secure message thread by ID?
  - id: message_threads_update
    intent: Replace a secure message thread
    question: How do I overwrite a thread's subject, members and patient in one call?
  - id: message_threads_partial_update
    intent: Partially update a secure message thread
    question: Can I add members to an existing thread with a PATCH?
  - id: message_threads_destroy
    intent: Delete a secure message thread
    question: How do I delete a message thread that was opened by mistake?
  phrasing_ops: 6
  slug: elation-messaging-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Patient profile management
  name: Elation Health Patients API
  phrasing_intents:
  - id: update-patient
    intent: Update a patient via the colon-style legacy path
    question: Is there an older Elation endpoint written as /patients/:id/ for editing a patient?
  - id: get-patient
    intent: Get a patient from the no-trailing-slash path
    question: Can I fetch a patient from a patients URL that has no trailing slash?
  - id: delete-patient
    intent: Delete a patient via the legacy endpoint
    question: How do I remove a patient chart using the older unversioned delete route?
  - id: update-patient-1
    intent: Patch a patient via the legacy endpoint
    question: Can I patch just part of a patient on the older unversioned PATCH route?
  - id: patients_retrieve
    intent: Retrieve a patient's details by ID
    question: How do I pull the details for one specific patient by their ID from the legacy endpoint?
  - id: patients_update
    intent: Replace all fields on a patient record
    question: Can I overwrite every field on a patient record at once, including pronouns and preferred language?
  - id: create-patient
    intent: Register a new patient via the legacy endpoint
    question: What is the minimum I need to register a patient through the older unversioned create call?
  - id: find-patients
    intent: Search patients across a practice
    question: How can I find patients by name and date of birth on the legacy patient search?
  phrasing_ops: 24
  slug: elation-patients-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Provider and staff management
  name: Elation Health Physicians API
  phrasing_intents:
  - id: find-physicians
    intent: Find physicians by name or NPI (legacy)
    question: How do I look up a physician in the practice by NPI on the older endpoint?
  - id: get-physician
    intent: Get a physician (legacy)
    question: How do I pull one physician's profile from the unversioned route?
  - id: update-physician-wip
    intent: Replace a physician profile (legacy)
    question: How do I overwrite a physician's profile, including telehealth settings, on the older PUT route?
  - id: update-physician-wip-1
    intent: Patch a physician profile (legacy)
    question: Can I change just a physician's license state on the older PATCH route?
  - id: update-physician-availabilities
    intent: Update physician availabilities (legacy)
    question: Is there an older unversioned route for setting a physician's available hours?
  - id: get-physician-availabilities
    intent: Get physician availabilities (legacy)
    question: Is there an older unversioned route for reading when a physician is available?
  - id: physicians_list
    intent: List physicians with paging
    question: How do I page through every physician in the v2.0 API?
  - id: physicians_retrieve
    intent: Retrieve a physician from the v2.0 API
    question: How do I fetch one physician by ID from /api/2.0?
  phrasing_ops: 12
  slug: elation-physicians-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Practice administration
  name: Elation Health Practices API
  phrasing_intents:
  - id: find-practices
    intent: List practices (legacy)
    question: Which practices can my credentials see on the older unversioned endpoint?
  - id: update-practice-wip-1
    intent: Patch practice details (legacy PATCH)
    question: Can I change only a practice's name with the legacy PATCH?
  - id: update-practice-wip
    intent: Replace practice details (legacy PUT)
    question: Which legacy PUT overwrites a practice's name and address?
  - id: get-practice
    intent: Look up a practice (legacy)
    question: What does the legacy endpoint return for one practice?
  - id: get-insurance-eligibility-usage
    intent: Check a practice's insurance eligibility usage
    question: How many insurance eligibility checks has my practice run?
  - id: practices_list
    intent: List practices
    question: How do I list the practices my API account has access to?
  - id: practices_retrieve
    intent: Get a practice's details
    question: What does a v2.0 practice record include, like physicians and service locations?
  - id: practices_partial_update
    intent: Edit part of a practice's details
    question: Can I change a practice's timezone without resending everything?
  phrasing_ops: 9
  slug: elation-practices-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Patient problem list management
  name: Elation Health Problems API
  phrasing_intents:
  - id: list-problems
    intent: Find a patient's problems (legacy endpoint)
    question: Can I see a patient's problem list through the older problems lookup?
  - id: create-problem
    intent: Add a problem to a chart (legacy endpoint)
    question: How do I add a diagnosis to a patient's problem list with the legacy endpoint?
  - id: get-problem
    intent: Get a problem (legacy endpoint)
    question: Can I read one problem entry on the legacy problems path?
  - id: delete-problem
    intent: Delete a problem (legacy endpoint)
    question: Is there a legacy call to remove a problem added in error?
  - id: patch-problem
    intent: Patch a problem (legacy PATCH)
    question: Can I mark a problem resolved with the legacy PATCH?
  - id: problems_update
    intent: Replace a problem (legacy PUT)
    question: How do I replace all fields of a problem on the unversioned path?
  - id: problems_list
    intent: List problems in API 2.0
    question: How do I list problems added within a date range in the 2.0 API?
  - id: problems_create
    intent: Create a problem in API 2.0
    question: How do I add a problem to a patient's chart with the 2.0 API?
  phrasing_ops: 12
  slug: elation-problems-api
- baseURL: https://app.elationemr.com/api/2.0/
  baseurl_source: declared
  description: Clinical encounter documentation
  name: Elation Health Visit Notes API
  phrasing_intents:
  - id: get-visit-note
    intent: Get a visit note (legacy endpoint)
    question: Can I read a single visit note through the older visit notes path?
  - id: delete-visit-note
    intent: Delete a visit note (legacy endpoint)
    question: Is it possible to delete a visit note through the original visit notes path?
  - id: sign-visit-note
    intent: Sign a draft visit note
    question: How do I sign a draft visit note so it's finalized?
  - id: visit_notes_update
    intent: Replace a visit note (legacy PUT)
    question: How do I replace every field of a visit note on the unversioned path?
  - id: find-visit-notes
    intent: Find visit notes (legacy endpoint)
    question: Can I find a patient's unsigned visit notes with the older search?
  - id: create-visit-note
    intent: Create a visit note (legacy endpoint)
    question: Can I document an encounter by creating a visit note on the legacy path?
  - id: visit_notes_list
    intent: List visit notes in API 2.0
    question: How do I list visit notes changed since a given time in the 2.0 API?
  - id: visit_notes_create
    intent: Create a visit note in API 2.0
    question: How do I create an encounter visit note with the 2.0 API?
  phrasing_ops: 14
  slug: elation-visit-notes-api
- description: HL7 FHIR R4 (v4.0.1) API with US Core v5.0.1 and SMART on FHIR 1.0.0 support, used for standards-based interoperability and ONC / CMS 21st Century Cures Act certified health IT use cases. Exposed to r
  name: Elation FHIR R4 API
  slug: fhir-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Allergy Documentation API from Elation Health — 2 operation(s) for allergy documentation.
  name: Elation Health Allergy Documentation API
  phrasing_intents:
  - id: create-allergy-documentation-nkda
    intent: Document no known drug allergies
    question: How do I record that a patient has no known drug allergies?
  - id: find-allergy-documentation-nkda
    intent: Find no-known-drug-allergy records
    question: Has this patient been documented as having no known drug allergies?
  - id: get-allergy-documentation-nkda
    intent: Get an NKDA documentation record
    question: What does a single NKDA documentation record contain?
  - id: delete-allergy-documentation-nkda
    intent: Remove an NKDA documentation record
    question: Can I remove an NKDA entry after the patient reports a drug allergy?
  phrasing_ops: 4
  slug: elation-health-allergy-documentation-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Allergy Documentation (NKDA) API from Elation Health — 2 operation(s) for allergy documentation (nkda).
  name: Elation Health Allergy Documentation (NKDA) API
  phrasing_intents:
  - id: allergy_documentation_list
    intent: List no-known-drug-allergy records
    question: Has a patient been documented as having no known drug allergies?
  - id: allergy_documentation_create
    intent: Document no known drug allergies
    question: How do I record that a patient has no known drug allergies?
  - id: allergy_documentation_destroy
    intent: Remove NKDA documentation
    question: How do I undo a no-known-drug-allergies note once an allergy is found?
  - id: allergy_documentation_retrieve
    intent: Get an NKDA documentation record
    question: Can I read a single NKDA documentation entry?
  phrasing_ops: 4
  slug: elation-health-allergy-documentation-nkda-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Ancillary Companies API from Elation Health — 4 operation(s) for ancillary companies.
  name: Elation Health Ancillary Companies API
  phrasing_intents:
  - id: find-ancillary-companies
    intent: Search ancillary companies by order type (legacy)
    question: Can I find the sleep or cardiac labs I can send orders to on the older unversioned endpoint?
  - id: get-ancillary-company
    intent: Look up an ancillary company (legacy)
    question: What does the legacy endpoint return for one ancillary company?
  - id: ancillary_companies_list
    intent: List ancillary companies for an order type
    question: How do I list, in the v2.0 API, the companies that can fulfil a given type of order?
  - id: ancillary_companies_retrieve
    intent: Get one ancillary company
    question: What details are stored for a single v2.0 ancillary company?
  phrasing_ops: 4
  slug: elation-health-ancillary-companies-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The API Settings API from Elation Health — 1 operation(s) for api settings.
  name: Elation Health API Settings API
  slug: elation-health-api-settings-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The App API from Elation Health — 4 operation(s) for app.
  name: Elation Health App API
  phrasing_intents:
  - id: subscribe-to-a-resource-updates
    intent: Subscribe to updates on a resource
    question: How do I get a webhook when patients or appointments change in Elation?
  - id: find-subscriptions
    intent: List my app's event subscriptions
    question: Which resource webhooks is my app currently subscribed to?
  - id: find-published-events
    intent: List events published to my app
    question: What change events have been published to my app recently?
  - id: delete-a-subscription
    intent: Unsubscribe from resource updates
    question: How do I stop receiving webhooks for a resource?
  - id: update-published-event-1
    intent: Patch the processing status of an event
    question: Can I set just the error content on a published event that failed?
  - id: update-published-event
    intent: Record processing results for an event
    question: How do I report back that my app processed an event, with status code and timestamp?
  - id: get-published-event
    intent: Get one published event
    question: How do I inspect a single event that was published to my app?
  phrasing_ops: 7
  slug: elation-health-app-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Appointment Rooms API from Elation Health — 1 operation(s) for appointment rooms.
  name: Elation Health Appointment Rooms API
  phrasing_intents:
  - id: appointments_rooms_retrieve
    intent: List appointment rooms for a practice
    question: Which exam rooms can appointments be booked into at my practice?
  phrasing_ops: 1
  slug: elation-health-appointment-rooms-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Appointment Types API from Elation Health — 4 operation(s) for appointment types.
  name: Elation Health Appointment Types API
  phrasing_intents:
  - id: find-appointment-types
    intent: Find appointment types (legacy)
    question: How do I see the appointment types set up on the legacy endpoint?
  - id: get-appointment-type
    intent: Look up an appointment type (legacy)
    question: Can I fetch a single appointment type from the legacy API?
  - id: update-appointment-type
    intent: Edit an appointment type (legacy PATCH)
    question: Can I change an appointment type's color or abbreviation with the legacy PATCH?
  - id: appointment_types_list
    intent: List appointment types
    question: Which appointment types does my practice offer in Elation?
  - id: appointment_types_create
    intent: Create an appointment type
    question: How do I add a new visit type with a default length?
  - id: appointment_types_destroy
    intent: Delete an appointment type
    question: How do I delete an appointment type we no longer use?
  - id: appointment_types_retrieve
    intent: Get one appointment type
    question: How do I read the settings of one appointment type in v2?
  - id: appointment_types_partial_update
    intent: Edit part of an appointment type
    question: Can I change just the color of an appointment type in v2?
  phrasing_ops: 9
  slug: elation-health-appointment-types-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Billing Codes API from Elation Health — 6 operation(s) for billing codes.
  name: Elation Health Billing Codes API
  phrasing_intents:
  - id: create-a-billing-code
    intent: Add a CPT billing code (legacy)
    question: How do I add a CPT code my practice can put on bills?
  - id: get-billing-code
    intent: Get a CPT billing code (Get)
    question: How do I get one CPT code my practice set up?
  - id: get-billing-codes
    intent: Search a practice's CPT codes
    question: Which CPT codes has my practice configured for billing, per the legacy unversioned endpoint?
  - id: update-a-billing-code
    intent: Update a CPT billing code (legacy)
    question: Can I change the charge on a CPT code with the older update call?
  - id: billing_codes_list
    intent: List CPT billing codes with paging
    question: Can I page through all billing codes with limit and offset?
  - id: billing_codes_create
    intent: Create a CPT billing code
    question: What's required to create a billing code with a description?
  - id: billing_codes_destroy
    intent: Delete a CPT billing code
    question: How do I delete a CPT code the practice no longer bills?
  - id: billing_codes_retrieve
    intent: Retrieve a CPT billing code
    question: Can I retrieve a billing code's description by id?
  phrasing_ops: 10
  slug: elation-health-billing-codes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Bills API from Elation Health — 6 operation(s) for bills.
  name: Elation Health Bills API
  phrasing_intents:
  - id: get-bill
    intent: Look up a bill (legacy endpoint)
    question: How do I fetch one bill from the legacy unversioned bills path?
  - id: patch-bill
    intent: Edit a bill (legacy PATCH)
    question: Can I record a billing error on a bill with the legacy PATCH?
  - id: delete-bill
    intent: Delete a bill (legacy draft endpoint)
    question: Can I delete a bill through the legacy bills API?
  - id: find-bills
    intent: Find bills by patient or service date (legacy)
    question: How can I search the legacy bills endpoint by service date range?
  - id: create-bill
    intent: Bill a visit note (legacy endpoint)
    question: How do I create a bill for a visit note through the legacy API?
  - id: release-a-bill-to-pms
    intent: Release a bill to the PMS (legacy)
    question: How do I push a bill to my practice management system with the legacy endpoint?
  - id: bills_list
    intent: List bills
    question: Which bills were created for a patient in Elation?
  - id: bills_create
    intent: Create a bill for a visit
    question: How do I create a bill with CPT codes for a visit in v2?
  phrasing_ops: 11
  slug: elation-health-bills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Broadcast Messages API from Elation Health — 2 operation(s) for broadcast messages.
  name: Elation Health Broadcast Messages API
  phrasing_intents:
  - id: find-broadcastmessages
    intent: List broadcast messages
    question: What broadcast messages have been sent to our practice's users?
  - id: create-a-broadcastmessage
    intent: Send a broadcast message
    question: How do I broadcast an announcement to everyone in the practice?
  - id: delete-a-broadcastmessage
    intent: Delete a broadcast message
    question: Can I take down a broadcast announcement after it's posted?
  phrasing_ops: 3
  slug: elation-health-broadcast-messages-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Cardiac Centers API from Elation Health — 4 operation(s) for cardiac centers.
  name: Elation Health Cardiac Centers API
  phrasing_intents:
  - id: find-cardiac-centers
    intent: Find cardiac centers (legacy)
    question: How do I find cardiac testing centers by company on the older endpoint?
  - id: get-cardiac-center
    intent: Get a cardiac center (legacy)
    question: How do I look up one cardiac center by ID on the older route?
  - id: cardiac_centers_list
    intent: List cardiac centers with paging
    question: How do I page through cardiac centers in the v2.0 API?
  - id: cardiac_centers_retrieve
    intent: Retrieve a cardiac center from v2.0
    question: How do I fetch a single cardiac center by ID from /api/2.0?
  phrasing_ops: 4
  slug: elation-health-cardiac-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Cardiac Order Tests API from Elation Health — 4 operation(s) for cardiac order tests.
  name: Elation Health Cardiac Order Tests API
  phrasing_intents:
  - id: get-cardiac-order-test
    intent: Get a cardiac test type (Get)
    question: How do I get a cardiac test that can be ordered, by id?
  - id: wip-find-cardiac-order-tests
    intent: Find cardiac tests by name
    question: Which cardiac tests can my practice order, like an echocardiogram?
  - id: create-cardiac-order-test
    intent: Add a cardiac test (legacy)
    question: How do I add an orderable cardiac test with the older create?
  - id: cardiac_order_tests_list
    intent: List cardiac tests with paging
    question: Can I page through all cardiac order tests?
  - id: cardiac_order_tests_create
    intent: Create a cardiac order test
    question: What's needed to create a new cardiac order test?
  - id: cardiac_order_tests_destroy
    intent: Delete a cardiac order test
    question: How do I delete a cardiac order test?
  - id: cardiac_order_tests_retrieve
    intent: Retrieve a cardiac order test
    question: Can I retrieve a single cardiac order test from the v2.0 API?
  phrasing_ops: 7
  slug: elation-health-cardiac-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Cardiac Orders API from Elation Health — 4 operation(s) for cardiac orders.
  name: Elation Health Cardiac Orders API
  phrasing_intents:
  - id: get-cardiac-order
    intent: Look up a cardiac order (legacy endpoint)
    question: How do I fetch a single cardiac order from the legacy unversioned path?
  - id: put-cardiac-order
    intent: Replace a cardiac order (legacy PUT)
    question: Can I resend a whole cardiac order through the legacy PUT?
  - id: patch-cardiac-order
    intent: Patch a cardiac order (legacy PATCH)
    question: Can I add ICD-10 codes to a cardiac order with the legacy PATCH?
  - id: delete-cardiac-order
    intent: Delete a cardiac order (legacy endpoint)
    question: How do I remove a cardiac order with the legacy API?
  - id: find-cardiac-orders
    intent: Find cardiac orders by patient (legacy)
    question: How can I search cardiac orders for one patient on the legacy endpoint?
  - id: create-cardiac-order
    intent: Order a cardiac test (legacy endpoint)
    question: How do I place a cardiac order through the legacy unversioned API?
  - id: cardiac_orders_list
    intent: List cardiac orders
    question: Which cardiac orders exist for a patient in Elation?
  - id: cardiac_orders_create
    intent: Place a cardiac order
    question: How do I order an ECG or other cardiac test for a patient through API v2?
  phrasing_ops: 12
  slug: elation-health-cardiac-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Caregaps API from Elation Health — 2 operation(s) for caregaps.
  name: Elation Health Caregaps API
  phrasing_intents:
  - id: caregaps_list_caregaps_api__quality_program__caregap__get
    intent: List care gaps in a quality program
    question: Which patients have open care gaps in a quality program?
  - id: caregaps_post_caregaps_api__quality_program__caregap__post
    intent: Open a care gap for a patient
    question: How do I open a new care gap for a patient under a quality measure?
  - id: caregaps_get_caregaps_api__quality_program__caregap__caregap_id___get
    intent: Get one care gap
    question: Can I look up the details of a specific care gap?
  - id: caregaps_delete_caregaps_api__quality_program__caregap__caregap_id___delete
    intent: Delete a care gap
    question: How do I delete a care gap that was opened in error?
  - id: caregaps_modify_caregaps_api__quality_program__caregap__caregap_id___patch
    intent: Close or reopen a care gap
    question: How do I mark a care gap as closed once the patient gets the screening?
  phrasing_ops: 5
  slug: elation-health-caregaps-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Ccda API from Elation Health — 4 operation(s) for ccda.
  name: Elation Health Ccda API
  phrasing_intents:
  - id: create-ccda
    intent: Import a CCDA document
    question: How do I upload a CCDA document into Elation?
  - id: get-ccda
    intent: Export a patient's chart as CCDA (legacy)
    question: How do I export a patient's chart as a CCDA v2.1 document on the legacy endpoint?
  - id: get-ccda-cehrt-2022
    intent: Export a CCDA for CEHRT 2022 certification
    question: Is there a CEHRT 2022 version of the patient CCDA export?
  - id: ccda_retrieve
    intent: Get a patient's CCDA
    question: How do I retrieve a patient's CCDA through API v2?
  phrasing_ops: 4
  slug: elation-health-ccda-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Clinical Documents API from Elation Health — 4 operation(s) for clinical documents.
  name: Elation Health Clinical Documents API
  phrasing_intents:
  - id: find-clinical-documents
    intent: Find clinical documents (legacy endpoint)
    question: What CCDA clinical documents have been imported, according to the legacy lookup?
  - id: create-clinical-document
    intent: Import a clinical document (legacy endpoint)
    question: How do I import a patient's CCDA XML file through the legacy endpoint?
  - id: get-clinical-document
    intent: Get a clinical document (legacy endpoint)
    question: Can I open one imported clinical document on the legacy path?
  - id: clinical_documents_list
    intent: List clinical documents in API 2.0
    question: How do I list a patient's imported clinical documents in the 2.0 API?
  - id: clinical_documents_create
    intent: Import a clinical document in API 2.0
    question: How do I upload a CCDA XML file for a patient with the 2.0 API?
  - id: clinical_documents_destroy
    intent: Delete a clinical document in API 2.0
    question: How do I delete an imported clinical document in the 2.0 API?
  - id: clinical_documents_retrieve
    intent: Retrieve a clinical document in API 2.0
    question: How do I retrieve a clinical document by ID in API 2.0?
  phrasing_ops: 7
  slug: elation-health-clinical-documents-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Clinical Questionnaires API from Elation Health — 2 operation(s) for clinical questionnaires.
  name: Elation Health Clinical Questionnaires API
  phrasing_intents:
  - id: find-clinical-questionnaire
    intent: List clinical questionnaires
    question: Which clinical questionnaires, like PHQ-9 style screeners, are available?
  - id: get-clinical-questionnaire
    intent: Get one clinical questionnaire
    question: What questions make up a specific clinical questionnaire?
  phrasing_ops: 2
  slug: elation-health-clinical-questionnaires-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Contacts API from Elation Health — 8 operation(s) for contacts.
  name: Elation Health Contacts API
  phrasing_intents:
  - id: get-contacts
    intent: Search referral contacts (legacy endpoint)
    question: Can I search my referral contacts by specialty and state with the older contacts search endpoint?
  - id: create-contact
    intent: Add a referral contact (legacy endpoint)
    question: How do I add an outside physician to my contacts through the legacy create endpoint?
  - id: find-contacts
    intent: List contacts by NPI (legacy endpoint)
    question: How do I look up a contact by NPI number on the legacy contacts list?
  - id: update-contacts
    intent: Replace a contact's details (legacy PUT)
    question: How do I overwrite every field on a contact with the legacy PUT endpoint?
  - id: update-contacts-1
    intent: Patch a contact's details (legacy PATCH)
    question: Can I change just one field on a contact using the legacy PATCH endpoint?
  - id: delete-contacts
    intent: Delete a contact (legacy endpoint)
    question: Is there a legacy endpoint for removing a contact from my address book?
  - id: fetch-contact
    intent: Fetch one contact (legacy endpoint)
    question: How do I fetch a single contact by its contact ID on the legacy path?
  - id: contacts_list
    intent: List contacts in API 2.0
    question: How do I page through all my practice's contacts in the 2.0 API?
  phrasing_ops: 14
  slug: elation-health-contacts-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Custom Blocks API from Elation Health — 1 operation(s) for custom blocks.
  name: Elation Health Custom Blocks API
  phrasing_intents:
  - id: list_custom_blocks
    intent: List custom note blocks
    question: What custom blocks are available for clinical notes?
  phrasing_ops: 1
  slug: elation-health-custom-blocks-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The parent resource for tracking batches of individual patient chart imports.
  name: Elation Health Data Import Request API
  phrasing_intents:
  - id: getDIRs
    intent: List data import requests
    question: What data import requests already exist for bringing charts into Elation?
  - id: createDIR
    intent: Open a data import request
    question: How do I start a new data import for a physician's patient charts?
  - id: getDIR
    intent: Check a data import request's progress
    question: How do I check the status of the patient chart imports under one request?
  - id: updateDIR
    intent: Replace a data import request
    question: Can I update a data import request by resending all its editable fields?
  - id: patchDIR
    intent: Change a data import request's status
    question: Can I change only the status of a data import request?
  - id: deleteDIR
    intent: Delete a data import request
    question: How do I delete a data import request I no longer need?
  - id: runDIR
    intent: Start all open chart imports in a request
    question: How do I kick off every open patient chart import under a request at once?
  phrasing_ops: 7
  slug: elation-health-data-import-request-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Definitions API from Elation Health — 2 operation(s) for definitions.
  name: Elation Health Definitions API
  phrasing_intents:
  - id: definitions_get_page_caregaps_api__quality_program__definition__get
    intent: List care gap definitions for a quality program
    question: Which care gap definitions exist for a given quality program?
  - id: definitions_post_caregaps_api__quality_program__definition__post
    intent: Create a care gap definition
    question: How do I define a new care gap measure for a quality program?
  - id: definitions_get_caregaps_api__quality_program__definition__definition_id___get
    intent: Get a care gap definition
    question: What criteria make up one specific care gap definition?
  - id: definitions_delete_caregaps_api__quality_program__definition__definition_id___delete
    intent: Delete a care gap definition
    question: Can I retire a care gap definition from a quality program?
  phrasing_ops: 4
  slug: elation-health-definitions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Delegate Permissions API from Elation Health — 4 operation(s) for delegate permissions.
  name: Elation Health Delegate Permissions API
  phrasing_intents:
  - id: get-delegate-permissions
    intent: Get a delegate permission (legacy)
    question: How do I see what a delegate is allowed to do for a physician, on the older endpoint?
  - id: update-delegate-permissions
    intent: Update a delegate permission (legacy)
    question: Can I change the permission type a delegate holds for a physician?
  - id: create-delegate-permissions
    intent: Grant a delegate permission (legacy)
    question: How do I let a staff member act on a physician's behalf through the unversioned route?
  - id: delete-a-delegate-permission
    intent: Revoke a delegate permission (legacy)
    question: How do I revoke a delegate's access using the older delete call?
  - id: find-delegate-permissions
    intent: Find delegate permissions (legacy)
    question: Who has been granted delegate access to act for physicians, per the older endpoint?
  - id: delegate_permissions_list
    intent: List delegate permissions with paging
    question: How do I page through delegate permissions in the v2.0 API?
  - id: delegate_permissions_create
    intent: Grant a delegate permission in the v2.0 API
    question: What does /api/2.0 require to give a user delegate rights for a physician?
  - id: delegate_permissions_destroy
    intent: Revoke a delegate permission in the v2.0 API
    question: How do I revoke delegate access through /api/2.0?
  phrasing_ops: 9
  slug: elation-health-delegate-permissions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Discontinued Medication API from Elation Health — 1 operation(s) for discontinued medication.
  name: Elation Health Discontinued Medication API
  phrasing_intents:
  - id: patch-discontinue-med-order
    intent: Discontinue a medication order
    question: How do I stop a patient's medication and record why?
  phrasing_ops: 1
  slug: elation-health-discontinued-medication-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Discontinued Medications API from Elation Health — 4 operation(s) for discontinued medications.
  name: Elation Health Discontinued Medications API
  phrasing_intents:
  - id: find-discontinued-medications
    intent: Search discontinued medications (legacy)
    question: Can I find which medications a patient stopped on the older unversioned endpoint?
  - id: create-discontinued-medications
    intent: Discontinue a medication order (legacy)
    question: What does the legacy call need to stop a patient's medication?
  - id: find-discontinued-medication
    intent: Look up a discontinued medication (legacy)
    question: What does the unversioned path return for one discontinued medication?
  - id: discontinued_medications_list
    intent: List discontinued medications
    question: How do I list the medications a patient has stopped taking?
  - id: discontinued_medications_create
    intent: Record a discontinued medication
    question: Can I note who documented a discontinuation in API v2.0?
  - id: discontinued_medications_destroy
    intent: Delete a discontinued medication record
    question: Can I undo a discontinuation entered by mistake?
  - id: discontinued_medications_retrieve
    intent: Get one discontinued medication
    question: What does a v2.0 discontinued medication record include?
  phrasing_ops: 7
  slug: elation-health-discontinued-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Document Tags API from Elation Health — 4 operation(s) for document tags.
  name: Elation Health Document Tags API
  phrasing_intents:
  - id: find-document-tags
    intent: List document tags (legacy endpoint)
    question: What document tags exist in my practice, per the legacy endpoint?
  - id: create-document-tag
    intent: Create a document tag (legacy endpoint)
    question: How do I add a new tag for labeling documents through the legacy endpoint?
  - id: get-document-tag
    intent: Get a document tag (legacy endpoint)
    question: How do I look up one document tag by id on the legacy path?
  - id: update-document-tag
    intent: Change a document tag's code (legacy PATCH)
    question: Can I update just a document tag's code with the legacy PATCH?
  - id: update-document-tag-1
    intent: Replace a document tag (legacy PUT)
    question: Can I overwrite a whole document tag with the legacy PUT?
  - id: document_tags_list
    intent: List document tags (v2.0)
    question: How do I search document tags by value in the 2.0 API?
  - id: document_tags_create
    intent: Create a document tag (v2.0)
    question: How do I create a document tag with a SNOMED result code in version 2.0?
  - id: document_tags_retrieve
    intent: Get a document tag (v2.0)
    question: How do I fetch a single document tag in the 2.0 API?
  phrasing_ops: 10
  slug: elation-health-document-tags-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Drug Intolerances API from Elation Health — 4 operation(s) for drug intolerances.
  name: Elation Health Drug Intolerances API
  phrasing_intents:
  - id: find-drug-intolerances
    intent: Find drug intolerances for patients
    question: What drug intolerances are recorded for a set of patients?
  - id: get-drug-intolerance
    intent: Get a drug intolerance (Get)
    question: How do I get a single drug intolerance with its reaction?
  - id: delete-drug-intolerance
    intent: Delete a drug intolerance (legacy)
    question: How do I delete a drug intolerance with the older delete call?
  - id: drug_intolerances_list
    intent: List a patient's drug intolerances
    question: Can I page through one patient's drug intolerances?
  - id: drug_intolerances_create
    intent: Record a drug intolerance
    question: How do I record that a patient can't tolerate a medication?
  - id: drug_intolerances_destroy
    intent: Delete a drug intolerance
    question: How do I delete an existing drug intolerance by id?
  - id: drug_intolerances_retrieve
    intent: Retrieve a drug intolerance
    question: Can I retrieve a drug intolerance and its status?
  - id: drug_intolerances_partial_update
    intent: Partially update a drug intolerance
    question: Can I change only the severity of an intolerance?
  phrasing_ops: 9
  slug: elation-health-drug-intolerances-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Event Subscriptions API from Elation Health — 8 operation(s) for event subscriptions.
  name: Elation Health Event Subscriptions API
  phrasing_intents:
  - id: app_published_events_list
    intent: List events published to my app
    question: Which webhook events has Elation published to my app so far?
  - id: app_published_events_retrieve
    intent: Get one event published to my app
    question: What did a single event delivered to my app contain?
  - id: app_published_events_partial_update
    intent: Patch fields on an app published event
    question: Can I change just the error content on an event sent to my app?
  - id: app_published_events_update
    intent: Replace an app published event record
    question: Can I overwrite an event published to my app, including its processed date?
  - id: app_subscriptions_list
    intent: List my app's resource subscriptions
    question: Which resources is my app currently subscribed to for updates?
  - id: app_subscriptions_create
    intent: Subscribe my app to resource updates
    question: How do I get my app notified when Elation patients or appointments change?
  - id: app_subscriptions_destroy
    intent: Delete one of my app's subscriptions
    question: How do I stop my app receiving updates for a resource?
  - id: app_subscriptions_retrieve
    intent: Get one of my app's subscriptions
    question: Can I check which resource and target one of my app subscriptions points at?
  phrasing_ops: 16
  slug: elation-health-event-subscriptions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Family Histories API from Elation Health — 4 operation(s) for family histories.
  name: Elation Health Family Histories API
  phrasing_intents:
  - id: get-family-history
    intent: Get a family history entry (Get)
    question: How do I get one family history entry for a patient?
  - id: delete-family-history
    intent: Delete a family history entry (legacy)
    question: How do I delete a family history entry with the older call?
  - id: find-family-histories
    intent: Find a patient's family history
    question: What conditions run in a patient's family?
  - id: create-family-history
    intent: Add a family history entry (legacy)
    question: How do I add a relative's condition with a SNOMED code using the older create?
  - id: family_histories_list
    intent: List family histories with paging
    question: Can I page through family histories across a practice?
  - id: family_histories_create
    intent: Create a family history entry
    question: Do I send text or an ICD-9 code when creating a family history in the v2.0 API?
  - id: family_histories_destroy
    intent: Delete a family history entry
    question: How do I delete an existing family history by id?
  - id: family_histories_retrieve
    intent: Retrieve a family history entry
    question: Can I retrieve one family history entry with its codes?
  phrasing_ops: 8
  slug: elation-health-family-histories-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Fax Lines API from Elation Health — 2 operation(s) for fax lines.
  name: Elation Health Fax Lines API
  phrasing_intents:
  - id: find-fax-lines
    intent: Find a practice's fax lines
    question: What fax numbers does my practice have in Elation?
  - id: get-fax-line
    intent: Get a fax line
    question: How do I get the details of one fax line?
  phrasing_ops: 2
  slug: elation-health-fax-lines-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Fills API from Elation Health — 4 operation(s) for fills.
  name: Elation Health Fills API
  phrasing_intents:
  - id: medication_history_download_fills_list
    intent: List fills from medication history downloads
    question: What pharmacy fills came back from a patient's medication history download?
  - id: medication_history_download_fills_retrieve
    intent: Get a fill from a medication history download
    question: How do I read one fill from a downloaded medication history?
  - id: prescription_fills_list
    intent: List prescription fills
    question: Which of a patient's prescriptions have been filled?
  - id: prescription_fills_retrieve
    intent: Get a prescription fill
    question: How do I look up one prescription fill?
  phrasing_ops: 4
  slug: elation-health-fills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Handouts API from Elation Health — 5 operation(s) for handouts.
  name: Elation Health Handouts API
  phrasing_intents:
  - id: find-hangouts
    intent: Find patient handouts (legacy)
    question: How do I search the practice's patient education handouts by name on the older endpoint?
  - id: create-hangout
    intent: Create a patient handout (legacy)
    question: How do I add a new patient education handout through the unversioned route?
  - id: get-hangouts
    intent: Get one patient handout (legacy)
    question: How do I open a single handout's content on the older unversioned route?
  - id: update-hangout-1
    intent: Patch a patient handout (legacy)
    question: Can I rename a handout without resending its content on the older PATCH route?
  - id: delete-hangout
    intent: Delete a patient handout (legacy)
    question: How do I remove an outdated handout using the older delete route?
  - id: update-hangout
    intent: Replace a patient handout (legacy)
    question: How do I overwrite a handout's whole content on the unversioned PUT route?
  - id: handouts_list
    intent: List patient handouts with paging
    question: How do I page through every handout in the v2.0 API?
  - id: handouts_create
    intent: Create a patient handout in the v2.0 API
    question: How do I publish a new education handout through /api/2.0?
  phrasing_ops: 12
  slug: elation-health-handouts-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Historical Medication Download Requests API from Elation Health — 2 operation(s) for historical medication download requests.
  name: Elation Health Historical Medication Download Requests API
  phrasing_intents:
  - id: medication_history_downloads_list
    intent: List medication history downloads
    question: What medication history downloads have been requested?
  - id: medication_history_downloads_create
    intent: Request a patient's medication history
    question: How do I pull a patient's external medication history?
  - id: medication_history_downloads_retrieve
    intent: Get a medication history download
    question: Did a medication history download succeed, and how many items came back?
  phrasing_ops: 3
  slug: elation-health-historical-medication-download-requests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Histories API from Elation Health — 4 operation(s) for histories.
  name: Elation Health Histories API
  phrasing_intents:
  - id: create-history
    intent: Add a history entry (legacy endpoint)
    question: How do I record a patient's surgical or social history through the legacy endpoint?
  - id: find-histories
    intent: Find a patient's histories (legacy endpoint)
    question: Can I see a patient's social and family history entries via the legacy lookup?
  - id: get-history
    intent: Get a history entry (legacy endpoint)
    question: Can I read one history entry on the legacy histories path?
  - id: delete-history
    intent: Delete a history entry (legacy endpoint)
    question: Is there a legacy call to remove an incorrect history entry?
  - id: histories_list
    intent: List patient histories in API 2.0
    question: How do I list patient histories for a practice in the 2.0 API?
  - id: histories_create
    intent: Create a patient history in API 2.0
    question: How do I add a family or social history entry with the 2.0 API?
  - id: histories_destroy
    intent: Delete a patient history in API 2.0
    question: How do I delete a patient history entry in the 2.0 API?
  - id: histories_retrieve
    intent: Retrieve a patient history in API 2.0
    question: How do I retrieve a single patient history by ID in API 2.0?
  phrasing_ops: 8
  slug: elation-health-histories-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Imaging Centers API from Elation Health — 4 operation(s) for imaging centers.
  name: Elation Health Imaging Centers API
  phrasing_intents:
  - id: find-imaging-centers
    intent: Search imaging centers (legacy)
    question: Can I find radiology locations by name on the older unversioned endpoint?
  - id: get-imaging-center
    intent: Look up an imaging center (legacy)
    question: What does the legacy endpoint return for one imaging center?
  - id: imaging_centers_list
    intent: List imaging centers
    question: How do I list the imaging centers I can send orders to?
  - id: imaging_centers_retrieve
    intent: Get one imaging center
    question: What address and contact details are stored for a v2.0 imaging center?
  phrasing_ops: 4
  slug: elation-health-imaging-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Imaging Order Tests API from Elation Health — 4 operation(s) for imaging order tests.
  name: Elation Health Imaging Order Tests API
  phrasing_intents:
  - id: find-imaging-order-tests
    intent: Find imaging order tests (legacy)
    question: How do I search the imaging tests a practice can order, on the older endpoint?
  - id: create-imaging-order-test
    intent: Add an imaging order test (legacy)
    question: How do I add a custom imaging test to the orderable list via the unversioned route?
  - id: get-imaging-order-test
    intent: Get an imaging order test (legacy)
    question: How do I look up one imaging test by ID on the older route?
  - id: imaging_order_tests_list
    intent: List imaging order tests with paging
    question: How do I page through imaging order tests in the v2.0 API?
  - id: imaging_order_tests_create
    intent: Create an imaging order test in v2.0
    question: What does /api/2.0 need to add an orderable imaging test?
  - id: imaging_order_tests_destroy
    intent: Delete an imaging order test in v2.0
    question: How do I delete an imaging order test through /api/2.0?
  - id: imaging_order_tests_retrieve
    intent: Retrieve an imaging order test from v2.0
    question: How do I fetch one imaging order test by ID from /api/2.0?
  phrasing_ops: 7
  slug: elation-health-imaging-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Imaging Orders API from Elation Health — 4 operation(s) for imaging orders.
  name: Elation Health Imaging Orders API
  phrasing_intents:
  - id: get-imaging-order
    intent: Get an imaging order (legacy endpoint)
    question: Can I look up one imaging order on the legacy imaging orders path?
  - id: put-imaging-order
    intent: Replace an imaging order (legacy PUT)
    question: How do I resend a whole imaging order through the legacy PUT?
  - id: patch-imaging-order
    intent: Patch an imaging order (legacy PATCH)
    question: Can I change only the ICD-10 codes on an imaging order with the legacy PATCH?
  - id: delete-imaging-order
    intent: Delete an imaging order (legacy endpoint)
    question: Is there a legacy call to delete an imaging order entered by mistake?
  - id: find-imaging-orders
    intent: Find imaging orders (legacy endpoint)
    question: Can I find all of a patient's imaging orders with the older lookup?
  - id: create-imaging-order
    intent: Place an imaging order (legacy endpoint)
    question: How do I order an X-ray or MRI for a patient through the legacy endpoint?
  - id: imaging_orders_list
    intent: List imaging orders in API 2.0
    question: How do I page through imaging orders in the 2.0 API?
  - id: imaging_orders_create
    intent: Create an imaging order in API 2.0
    question: How do I create a new imaging order with the 2.0 API?
  phrasing_ops: 12
  slug: elation-health-imaging-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Immunizations API from Elation Health — 4 operation(s) for immunizations.
  name: Elation Health Immunizations API
  phrasing_intents:
  - id: delete-immunization
    intent: Delete an immunization (legacy endpoint)
    question: Is there a legacy endpoint to remove a vaccination record?
  - id: get-immunization
    intent: Get an immunization (legacy endpoint)
    question: Can I look up one vaccination record on the legacy path?
  - id: find-immunizations
    intent: Find a patient's immunizations (legacy)
    question: What vaccines has a patient received, per the legacy endpoint?
  - id: create-immunization
    intent: Record an immunization (legacy endpoint)
    question: How do I record a vaccine given to a patient through the legacy endpoint?
  - id: immunizations_list
    intent: List immunizations (v2.0)
    question: Can I page through a patient's immunizations in the 2.0 API?
  - id: immunizations_create
    intent: Record an immunization (v2.0)
    question: How do I log a vaccine with its service location in version 2.0?
  - id: immunizations_destroy
    intent: Delete an immunization (v2.0)
    question: How do I delete a vaccination record through the 2.0 API?
  - id: immunizations_retrieve
    intent: Get an immunization (v2.0)
    question: Which 2.0 call fetches one vaccination record?
  phrasing_ops: 8
  slug: elation-health-immunizations-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Incoming Files API from Elation Health — 8 operation(s) for incoming files.
  name: Elation Health Incoming Files API
  phrasing_intents:
  - id: find-incoming-files
    intent: Find incoming faxes and files (legacy endpoint)
    question: Which faxes came in from a particular number, according to the legacy search?
  - id: get-ingoming-file
    intent: Get an incoming file (legacy endpoint)
    question: Can I open one incoming fax record on the legacy path?
  - id: create-incoming-files
    intent: Upload an incoming file group (legacy endpoint)
    question: How do I push scanned documents into a practice's inbox through the legacy endpoint?
  - id: incoming_files_list
    intent: List incoming files in API 2.0
    question: How do I list incoming faxes received on a specific practice fax line in API 2.0?
  - id: incoming_files_create
    intent: Create an incoming file group in API 2.0
    question: How do I record an inbound fax with its sender number in the 2.0 API?
  - id: incoming_files_files_retrieve
    intent: Download a file from an incoming file group
    question: How do I download one document out of an incoming fax group?
  - id: incoming_files_images_retrieve
    intent: Get a page image from an incoming file group
    question: Can I view a page image from an incoming fax at a chosen size?
  - id: incoming_files_retrieve
    intent: Retrieve an incoming file group in API 2.0
    question: How do I retrieve one incoming file group by ID in API 2.0?
  phrasing_ops: 9
  slug: elation-health-incoming-files-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Injections API from Elation Health — 2 operation(s) for injections.
  name: Elation Health Injections API
  phrasing_intents:
  - id: get-injection
    intent: Get one injection record
    question: How do I look up a single injection given to a patient?
  - id: find-injections
    intent: List injections
    question: Which injections have been recorded in Elation?
  phrasing_ops: 2
  slug: elation-health-injections-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Injections (BETA) API from Elation Health — 2 operation(s) for injections (beta).
  name: Elation Health Injections (BETA) API
  phrasing_intents:
  - id: injections_list
    intent: List injections
    question: How do I list the injections recorded in the practice?
  - id: injections_retrieve
    intent: Retrieve an injection
    question: How do I see the details of one administered injection?
  phrasing_ops: 2
  slug: elation-health-injections-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Card API from Elation Health — 1 operation(s) for insurance card.
  name: Elation Health Insurance Card API
  phrasing_intents:
  - id: patients_insurance_cards_destroy
    intent: Delete a patient's insurance card image
    question: Can I remove an outdated insurance card image from a patient?
  - id: patients_insurance_cards_list
    intent: List a patient's insurance card images
    question: How do I see the insurance card photos on file for a patient?
  - id: patients_insurance_cards_create
    intent: Upload a patient's insurance card image
    question: Can I upload a photo of the front or back of a patient's insurance card?
  phrasing_ops: 3
  slug: elation-health-insurance-card-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Companies API from Elation Health — 5 operation(s) for insurance companies.
  name: Elation Health Insurance Companies API
  phrasing_intents:
  - id: find-insurance-companies
    intent: Find insurance companies by carrier
    question: How do I find a practice's insurance company by carrier name?
  - id: create-insurance-company
    intent: Add an insurance company with payer ID
    question: Can I add a new insurance carrier with its payer ID and address?
  - id: get-insurance-company
    intent: Get an insurance company (Get endpoint)
    question: How do I get one insurance company's address and payer ID?
  - id: delete-insurance-company
    intent: Delete an insurance company (legacy)
    question: How do I remove an insurance carrier with the older delete call?
  - id: update-insurance-company-2
    intent: Patch an insurance company (legacy PATCH)
    question: Can I change just an insurer's phone number with the older PATCH call?
  - id: update-insurance-company-1
    intent: Replace an insurance company (legacy PUT)
    question: Can I overwrite an insurance company using the older PUT endpoint?
  - id: insurance_companies_list
    intent: List insurance companies with paging
    question: Can I page through every insurance company my practice has?
  - id: insurance_companies_create
    intent: Create an insurance company with eligibility ID
    question: Can I set an eligibility payer ID when creating an insurance company?
  phrasing_ops: 12
  slug: elation-health-insurance-companies-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Eligibility API from Elation Health — 2 operation(s) for insurance eligibility.
  name: Elation Health Insurance Eligibility API
  phrasing_intents:
  - id: patient_insurances_eligibility_retrieve
    intent: Get a patient insurance's eligibility
    question: Is a patient's insurance currently eligible for coverage?
  - id: patient_insurances_eligibility_create
    intent: Run an eligibility check
    question: How do I run a new eligibility check on a patient's insurance?
  - id: patient_insurances_eligibility_full_report_retrieve
    intent: Get the full eligibility report
    question: Where can I see the full eligibility report with all benefit details?
  phrasing_ops: 3
  slug: elation-health-insurance-eligibility-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Eligibility Usage API from Elation Health — 1 operation(s) for insurance eligibility usage.
  name: Elation Health Insurance Eligibility Usage API
  phrasing_intents:
  - id: practices_eligibility_usage_retrieve
    intent: Get a practice's eligibility check usage
    question: How many real-time insurance eligibility checks has my practice used?
  phrasing_ops: 1
  slug: elation-health-insurance-eligibility-usage-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Insurance Plans API from Elation Health — 5 operation(s) for insurance plans.
  name: Elation Health Insurance Plans API
  phrasing_intents:
  - id: get-insurance-plan
    intent: Get an insurance plan (legacy endpoint)
    question: How do I look up one insurance plan by id on the legacy path?
  - id: delete-insurance-plan
    intent: Delete an insurance plan (legacy endpoint)
    question: How do I remove an insurance plan using the legacy endpoint?
  - id: find-insurance-plans
    intent: Find insurance plans (legacy endpoint)
    question: What insurance plans has my practice set up, per the legacy endpoint?
  - id: create-insurance-plan
    intent: Add an insurance plan (legacy endpoint)
    question: How do I add a new insurance plan for my practice through the legacy endpoint?
  - id: update-insurance-plan
    intent: Replace an insurance plan (legacy PUT)
    question: Can I overwrite an insurance plan's name and company with the legacy PUT?
  - id: update-insurance-plan-1
    intent: Rename or reassign an insurance plan (legacy PATCH)
    question: Can I just rename an insurance plan with the legacy PATCH?
  - id: insurance_plans_list
    intent: List insurance plans (v2.0)
    question: How do I page through all insurance plans in the 2.0 API?
  - id: insurance_plans_create
    intent: Add an insurance plan (v2.0)
    question: How do I create an insurance plan in version 2.0?
  phrasing_ops: 12
  slug: elation-health-insurance-plans-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Facility Identifiers API from Elation Health — 6 operation(s) for lab facility identifiers.
  name: Elation Health Lab Facility Identifiers API
  phrasing_intents:
  - id: delete-lab-facility-identifiers
    intent: Delete a lab facility identifier (legacy)
    question: Can I remove a lab facility identifier using the older unversioned endpoint?
  - id: get-lab-facility-identifiers
    intent: Look up a lab facility identifier (legacy WIP)
    question: What does the work-in-progress legacy endpoint return for one lab facility identifier?
  - id: put-lab-facility-identifiers
    intent: Replace a lab facility identifier (legacy WIP)
    question: Which legacy WIP call overwrites a whole lab facility identifier?
  - id: patch-lab-facility-identifiers
    intent: Patch a lab facility identifier (legacy WIP)
    question: Can I deactivate a lab facility mapping with the legacy PATCH?
  - id: find-lab-facility-identifiers
    intent: List lab facility identifiers (legacy)
    question: Where do I find all lab facility identifiers on the legacy unversioned API?
  - id: create-lab-facility-identifiers
    intent: Add a lab facility identifier (legacy WIP)
    question: What does the old WIP endpoint need to register a new lab facility mapping?
  - id: lab_facility_identifiers_list
    intent: List lab vendor integrations
    question: How do I see every lab vendor integration configured for my practices?
  - id: lab_facility_identifiers_create
    intent: Set up a lab vendor integration
    question: What's required to connect a practice to a lab vendor's facility?
  phrasing_ops: 12
  slug: elation-health-lab-facility-identifiers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Order Compendiums API from Elation Health — 4 operation(s) for lab order compendiums.
  name: Elation Health Lab Order Compendiums API
  phrasing_intents:
  - id: get-lab-order-compendium
    intent: Look up a lab order compendium (legacy)
    question: How do I fetch one lab order compendium entry from the legacy endpoint?
  - id: update-lab-order-compendium
    intent: Rename a lab compendium entry (legacy PATCH)
    question: Can I change just the name of a compendium entry on the legacy endpoint?
  - id: update-lab-order-compendium-1
    intent: Replace a lab compendium entry (legacy PUT)
    question: Can I overwrite a compendium entry's vendor, code and name with the legacy PUT?
  - id: delete-lab-order-compendium
    intent: Delete a lab order compendium (legacy)
    question: How do I remove a lab order compendium entry with the legacy API?
  - id: find-lab-order-compendium
    intent: Search lab order compendiums (legacy)
    question: How can I search the legacy compendium by test code or name?
  - id: create-lab-order-compendium
    intent: Add a lab order compendium (legacy)
    question: How do I add a lab test to the compendium through the legacy API?
  - id: lab_order_compendiums_list
    intent: List lab order compendiums
    question: Which lab tests are in a vendor's order compendium in Elation?
  - id: lab_order_compendiums_create
    intent: Create a lab order compendium entry
    question: How do I add a custom lab test to a vendor's compendium in v2?
  phrasing_ops: 12
  slug: elation-health-lab-order-compendiums-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Order Sets API from Elation Health — 4 operation(s) for lab order sets.
  name: Elation Health Lab Order Sets API
  phrasing_intents:
  - id: find-lab-order-sets
    intent: Find lab order sets (legacy)
    question: How do I see the practice's saved lab order sets on the older endpoint?
  - id: create-lab-order-set
    intent: Create a lab order set (legacy)
    question: How do I save a reusable group of lab tests through the unversioned route?
  - id: get-lab-order-sets
    intent: Get one lab order set (legacy)
    question: How do I see which tests are in one saved lab set via the older route?
  - id: update-lab-order-set
    intent: Replace a lab order set (legacy)
    question: How do I overwrite a saved lab set's tests on the unversioned PUT route?
  - id: update-lab-order-set-1
    intent: Patch a lab order set (legacy)
    question: Can I rename a lab set and adjust its tests on the older PATCH route?
  - id: delete-lab-order-sets
    intent: Delete a lab order set (legacy)
    question: How do I remove a saved lab panel with the older delete call?
  - id: lab_order_sets_list
    intent: List lab order sets with paging
    question: How do I page through lab order sets in the v2.0 API?
  - id: lab_order_sets_create
    intent: Create a lab order set in the v2.0 API
    question: Can I create a v2.0 lab order set with a lab compendium code?
  phrasing_ops: 12
  slug: elation-health-lab-order-sets-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Order Tests API from Elation Health — 4 operation(s) for lab order tests.
  name: Elation Health Lab Order Tests API
  phrasing_intents:
  - id: get-lab-order-tests
    intent: Look up an orderable lab test (legacy)
    question: Can I pull one orderable lab test by id from the older unversioned endpoint?
  - id: delete-lab-order-test
    intent: Delete an orderable lab test (legacy)
    question: Can I remove a practice-created lab test with the unversioned API?
  - id: find-lab-order-tests
    intent: Search orderable lab tests (legacy)
    question: Can I look up a lab test by its code on the legacy path?
  - id: create-lab-order-test
    intent: Add an orderable lab test (legacy)
    question: What must I send to add a lab test through the legacy endpoint?
  - id: lab_order_tests_list
    intent: List orderable lab tests
    question: How do I see which lab tests a vendor offers?
  - id: lab_order_tests_create
    intent: Create an orderable lab test
    question: Is only a name required to create a lab test in API v2.0?
  - id: lab_order_tests_destroy
    intent: Delete an orderable lab test
    question: Can I delete a lab test from the catalog in API v2.0?
  - id: lab_order_tests_retrieve
    intent: Get one orderable lab test
    question: What does a single v2.0 lab test record include?
  phrasing_ops: 8
  slug: elation-health-lab-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Vendor Integrations API from Elation Health — 4 operation(s) for lab vendor integrations.
  name: Elation Health Lab Vendor Integrations API
  phrasing_intents:
  - id: get-lab-vendor-integration
    intent: Get a lab vendor integration (legacy endpoint)
    question: Can I check one lab vendor hookup through the legacy integrations path?
  - id: put-lab-vendor-integration
    intent: Replace a lab vendor integration (legacy PUT)
    question: How do I resend a whole lab vendor integration via the legacy PUT?
  - id: patch-lab-vendor-integration
    intent: Patch a lab vendor integration (legacy PATCH)
    question: Can I turn printing on or off for a lab integration with the legacy PATCH?
  - id: delete-lab-vendor-integration
    intent: Remove a lab vendor integration (legacy endpoint)
    question: Is there a legacy way to disconnect a lab vendor from my practice?
  - id: find-lab-vendor-integration
    intent: Find lab vendor integrations (legacy endpoint)
    question: Which labs is my practice connected to, according to the legacy search?
  - id: create-lab-vendor-integration
    intent: Connect a lab vendor (legacy endpoint)
    question: How do I connect my practice to a lab vendor through the legacy endpoint?
  - id: lab_vendor_integrations_list
    intent: List lab vendor integrations in API 2.0
    question: How do I list every lab vendor integration in the 2.0 API?
  - id: lab_vendor_integrations_create
    intent: Create a lab vendor integration in API 2.0
    question: How do I set up a new lab vendor integration with the 2.0 API?
  phrasing_ops: 12
  slug: elation-health-lab-vendor-integrations-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Vendor Patient Sites API from Elation Health — 4 operation(s) for lab vendor patient sites.
  name: Elation Health Lab Vendor Patient Sites API
  phrasing_intents:
  - id: get-lab-vendor-patient-site
    intent: Get a lab patient service site (Get)
    question: How do I get the address of a lab's patient service site?
  - id: patch-lab-vendor-patient-site
    intent: Patch a lab patient site (legacy)
    question: Can I patch just a lab site's phone with the older Patch call?
  - id: delete-lab-vendor-patient-site
    intent: Delete a lab patient site (legacy)
    question: How do I delete a lab draw site with the legacy call?
  - id: put-lab-vendor-patient-site
    intent: Put a lab patient site (legacy)
    question: Can I overwrite a lab patient site with the older Put call?
  - id: find-lab-vendor-patient-site
    intent: Find lab patient sites by vendor
    question: Where can patients go for a lab draw from a given lab vendor?
  - id: create-lab-vendor-patient-site
    intent: Add a lab patient site (legacy)
    question: How do I add a lab draw location for a vendor using the older create call?
  - id: lab_vendor_patient_sites_list
    intent: List lab patient sites with paging
    question: Can I page through all lab vendor patient sites?
  - id: lab_vendor_patient_sites_create
    intent: Create a lab patient site
    question: How do I create a new lab vendor patient site with just a name?
  phrasing_ops: 12
  slug: elation-health-lab-vendor-patient-sites-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Lab Vendors API from Elation Health — 4 operation(s) for lab vendors.
  name: Elation Health Lab Vendors API
  phrasing_intents:
  - id: get-lab-vendor
    intent: Get a lab vendor (legacy endpoint)
    question: How do I look up one lab vendor by id on the legacy path?
  - id: update-lab-vendor
    intent: Replace a lab vendor (legacy PUT)
    question: Can I overwrite a lab vendor's names and integration flags with the legacy PUT?
  - id: update-lab-vendor-1
    intent: Change a lab vendor's integration flags (legacy)
    question: Can I toggle results integration on a lab vendor with the legacy PATCH?
  - id: delete-lab-vendor
    intent: Delete a lab vendor (legacy endpoint)
    question: How do I remove a lab vendor using the legacy endpoint?
  - id: find-lab-vendor
    intent: Find lab vendors (legacy endpoint)
    question: How do I search lab vendors by name on the legacy endpoint?
  - id: create-lab-vendor
    intent: Add a lab vendor (legacy endpoint)
    question: How do I add a new lab vendor through the legacy endpoint?
  - id: lab_vendors_list
    intent: List lab vendors (v2.0)
    question: Which lab vendors are available to my practice in the 2.0 API?
  - id: lab_vendors_create
    intent: Add a lab vendor (v2.0)
    question: How do I create an in-house lab vendor in the 2.0 API?
  phrasing_ops: 12
  slug: elation-health-lab-vendors-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Languages API from Elation Health — 2 operation(s) for languages.
  name: Elation Health Languages API
  phrasing_intents:
  - id: find-languages
    intent: List languages (legacy)
    question: Which languages can be set on a patient via the older unversioned endpoint?
  - id: languages_list
    intent: List preferred languages
    question: How do I get the list of preferred languages for patient demographics?
  phrasing_ops: 2
  slug: elation-health-languages-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Letters API from Elation Health — 3 operation(s) for letters.
  name: Elation Health Letters API
  phrasing_intents:
  - id: find-letters
    intent: Find patient letters
    question: Which letters were sent about a patient within a date range?
  - id: get-letter
    intent: Get a letter
    question: How do I read the body of a letter I already sent?
  - id: update-letter
    intent: Replace a letter (PUT)
    question: Can I rewrite an entire letter, including its referral order, with a full update?
  - id: patch-letter
    intent: Update a letter (PATCH)
    question: Can I mark a letter as signed and sent out with a PATCH?
  - id: post-letter
    intent: Write a letter to a contact
    question: How do I send a referral letter about a patient to an outside provider?
  phrasing_ops: 5
  slug: elation-health-letters-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication History Download Fills API from Elation Health — 2 operation(s) for medication history download fills.
  name: Elation Health Medication History Download Fills API
  phrasing_intents:
  - id: get-history-download-fill
    intent: Get a downloaded medication fill
    question: How do I see one pharmacy fill from a downloaded medication history?
  - id: find-history-download-fills
    intent: Find a patient's medication fills
    question: Which prescriptions has a patient actually filled at the pharmacy?
  phrasing_ops: 2
  slug: elation-health-medication-history-download-fills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication History Downloads API from Elation Health — 2 operation(s) for medication history downloads.
  name: Elation Health Medication History Downloads API
  phrasing_intents:
  - id: get-history-object
    intent: Get a medication history download request
    question: How do I check on one historical medication download request?
  - id: create-history-object
    intent: Request a patient's medication history
    question: How do I pull a patient's outside medication history into their chart?
  - id: find-history-object
    intent: List medication history download requests
    question: Which historical medication downloads have been requested?
  phrasing_ops: 3
  slug: elation-health-medication-history-downloads-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication Order Templates API from Elation Health — 4 operation(s) for medication order templates.
  name: Elation Health Medication Order Templates API
  phrasing_intents:
  - id: find-medication-order-templates
    intent: Search prescription templates (legacy)
    question: Can I find a practice's saved prescription templates on the older unversioned endpoint?
  - id: create-medication-order-template
    intent: Save a prescription template (legacy)
    question: Which legacy call saves a reusable prescription with quantity and refills?
  - id: get-medication-order-template
    intent: Look up a prescription template (legacy)
    question: What does the legacy endpoint return for one medication order template?
  - id: update-an-existing-medication-order-template
    intent: Replace a prescription template (legacy PUT)
    question: Which legacy PUT overwrites a whole prescription template?
  - id: update-an-existing-medication-order-template-1
    intent: Patch a prescription template (legacy PATCH)
    question: Can I change only the refill count on a template with the legacy PATCH?
  - id: delete-medication-order-template
    intent: Delete a prescription template (legacy)
    question: Can I delete a saved prescription template using the older unversioned API?
  - id: medication_order_templates_list
    intent: List prescription templates
    question: How do I list the prescription templates my practice has saved?
  - id: medication_order_templates_create
    intent: Create a prescription template
    question: What's needed to create a reusable prescription in API v2.0?
  phrasing_ops: 12
  slug: elation-health-medication-order-templates-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Medication Refills API from Elation Health — 2 operation(s) for medication refills.
  name: Elation Health Medication Refills API
  phrasing_intents:
  - id: get-refill
    intent: Get a medication refill request
    question: What medication and pharmacy does a particular refill request involve?
  - id: wip-find-refills
    intent: Find medication refill requests
    question: Which refill requests came in for a patient this week?
  phrasing_ops: 2
  slug: elation-health-medication-refills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Message Threads API from Elation Health — 7 operation(s) for message threads.
  name: Elation Health Message Threads API
  phrasing_intents:
  - id: get-message-thread
    intent: Get a message thread (Get endpoint)
    question: How do I fetch a patient message thread by its id with the Get Message Thread call?
  - id: find-message-threads
    intent: Find message threads by patient or date
    question: Can I find message threads for a patient within a document date range?
  - id: create-message-thread
    intent: Start a message thread with a sender
    question: How do I start a new message thread about a patient with a named sender?
  - id: update-message-thread
    intent: Update a thread's urgency or members
    question: Can I mark an existing message thread urgent after the fact?
  - id: delete-message-thread
    intent: Delete a message thread (legacy)
    question: How do I remove a message thread using the older delete call?
  - id: create-message-thread-wip
    intent: Create a message thread (WIP endpoint)
    question: Is there a work-in-progress version of the create message thread call?
  - id: delete-message-thread-wip
    intent: Delete a message thread (WIP endpoint)
    question: Does the work-in-progress API have its own message thread delete?
  - id: message_threads_list
    intent: List message threads with paging
    question: Can I page through all message threads with limit and offset?
  phrasing_ops: 13
  slug: elation-health-message-threads-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Methods Put And Patch Not Allowed. API from Elation Health — 1 operation(s) for methods put and patch not allowed..
  name: Elation Health Methods Put And Patch Not Allowed. API
  phrasing_intents:
  - id: update-message-threadwip-methods-put-and-patch-not-allowed
    intent: Update a message thread (WIP, not allowed)
    question: Can I edit an existing message thread with PUT or PATCH?
  phrasing_ops: 1
  slug: elation-health-methods-put-and-patch-not-allowed-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Non Visit Notes API from Elation Health — 4 operation(s) for non visit notes.
  name: Elation Health Non Visit Notes API
  phrasing_intents:
  - id: get-non-visit-note
    intent: Look up a non-visit note (legacy)
    question: How do I fetch one non-visit note from the legacy endpoint?
  - id: delete-non-visit-note
    intent: Delete a non-visit note (legacy)
    question: How do I remove a non-visit note with the legacy API?
  - id: update-non-visit-note
    intent: Replace a non-visit note (legacy PUT)
    question: Can I overwrite a non-visit note's type and dates with the legacy PUT?
  - id: update-non-visit-note-1
    intent: Sign or edit a non-visit note (legacy PATCH)
    question: Can I sign a non-visit note through the legacy PATCH?
  - id: find-non-visit-notes
    intent: Find a patient's non-visit notes (legacy)
    question: How can I search a patient's non-visit notes on the legacy endpoint?
  - id: create-non-visit-note
    intent: Write a non-visit note (legacy)
    question: How do I add a non-visit note to a chart through the legacy API?
  - id: non_visit_notes_list
    intent: List non-visit notes
    question: Which non-visit notes are on a patient's chart in Elation?
  - id: non_visit_notes_create
    intent: Add a non-visit note to a chart
    question: How do I record a phone call or other non-visit note in v2?
  phrasing_ops: 12
  slug: elation-health-non-visit-notes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Notes API from Elation Health — 3 operation(s) for notes.
  name: Elation Health Notes API
  phrasing_intents:
  - id: list_notes
    intent: List visit notes
    question: How do I list a patient's notes in Elation?
  - id: create_note
    intent: Create a note
    question: How do I start a new visit note for a patient?
  - id: delete_note_by_id
    intent: Delete a draft note
    question: Can I delete a note that is still a draft?
  - id: get_note_by_id
    intent: Read a note without taking a snapshot
    question: How do I read a note's contents without starting an edit session?
  - id: update_note_by_id
    intent: Update a note's content
    question: How do I change the content of an existing note?
  - id: get_note_amendment_by_id
    intent: Get an amendment to a note
    question: How do I see an amendment added to a signed note?
  phrasing_ops: 6
  slug: elation-health-notes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Notes v1 API from Elation Health — 2 operation(s) for notes v1.
  name: Elation Health Notes v1 API
  phrasing_intents:
  - id: list_notes_v1
    intent: List visit notes metadata
    question: How do I list the notes written for a patient?
  - id: create_note_v1
    intent: Create a legacy visit note
    question: How do I write a new visit note on a patient's chart?
  - id: delete_note_by_id_v1
    intent: Delete a draft legacy note
    question: How do I throw away a draft note I no longer need?
  - id: get_note_by_id_v1
    intent: Get a legacy visit note
    question: How do I read the content of a specific note?
  - id: update_note_by_id_v1
    intent: Update a legacy visit note
    question: How do I edit the content or provider on an existing note?
  phrasing_ops: 5
  slug: elation-health-notes-v1-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Notes v2 API from Elation Health — 7 operation(s) for notes v2.
  name: Elation Health Notes v2 API
  phrasing_intents:
  - id: list_notes_v2
    intent: List visit notes
    question: How do I list the visit notes written for a patient?
  - id: create_note_v2
    intent: Start a new sections-based visit note
    question: What do I need to create a new visit note using a layout?
  - id: delete_note_by_id_v2
    intent: Delete a draft visit note
    question: Can I delete a visit note that hasn't been signed?
  - id: get_note_by_id_v2
    intent: Read a visit note
    question: Can I read the full sections of one visit note?
  - id: update_note_by_id_v2
    intent: Edit a visit note's content
    question: How do I save edits to a visit note's sections?
  - id: create_note_amendment_v2
    intent: Start an amendment to a signed note
    question: Can I amend a note after it has been signed?
  - id: delete_note_amendment_by_id_v2
    intent: Delete a draft note amendment
    question: Can I throw away an amendment I started but never signed?
  - id: get_note_amendment_by_id_v2
    intent: Read a note amendment
    question: Where can I see the contents of an amendment on a note?
  phrasing_ops: 13
  slug: elation-health-notes-v2-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Office Staff API from Elation Health — 4 operation(s) for office staff.
  name: Elation Health Office Staff API
  phrasing_intents:
  - id: get-office-staff
    intent: Get an office staff member (legacy)
    question: Can I look up one office staff member on the legacy path?
  - id: update-office-staff
    intent: Update an office staff member
    question: Can I change a staff member's email or phone?
  - id: find-office-staff
    intent: List office staff (legacy endpoint)
    question: Who is on my practice's office staff, per the legacy endpoint?
  - id: create-office-staff
    intent: Add an office staff member
    question: How do I add a new front-desk staff member to my practice?
  - id: office_staff_list
    intent: List office staff (v2.0)
    question: Is it possible to page through office staff in the 2.0 API?
  - id: office_staff_retrieve
    intent: Get an office staff member (v2.0)
    question: Can I fetch one staff member by staff id in the 2.0 API?
  phrasing_ops: 6
  slug: elation-health-office-staff-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Outstanding Balance API from Elation Health — 1 operation(s) for outstanding balance.
  name: Elation Health Outstanding Balance API
  phrasing_intents:
  - id: patients_outstanding_balance_create
    intent: Set a patient's outstanding balance
    question: What call updates what a patient owes?
  phrasing_ops: 1
  slug: elation-health-outstanding-balance-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medication (Beta) API from Elation Health — 2 operation(s) for packaged medication (beta).
  name: Elation Health Packaged Medication (Beta) API
  phrasing_intents:
  - id: packaged_medications_list
    intent: Search packaged medications by NDC or name
    question: How do I look up a packaged medication by its NDC code?
  - id: packaged_medications_retrieve
    intent: Get one packaged medication
    question: How do I get the details of one packaged medication?
  phrasing_ops: 2
  slug: elation-health-packaged-medication-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medication Labeler (Beta) API from Elation Health — 2 operation(s) for packaged medication labeler (beta).
  name: Elation Health Packaged Medication Labeler (Beta) API
  phrasing_intents:
  - id: packaged_medication_labelers_list
    intent: Search packaged medication labelers
    question: Which drug labelers match a manufacturer name?
  - id: packaged_medication_labelers_retrieve
    intent: Get a packaged medication labeler
    question: How do I look up one medication labeler by id?
  phrasing_ops: 2
  slug: elation-health-packaged-medication-labeler-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medication Labelers API from Elation Health — 2 operation(s) for packaged medication labelers.
  name: Elation Health Packaged Medication Labelers API
  phrasing_intents:
  - id: find-packaged-medication-labelers
    intent: Find packaged medication labelers
    question: How do I look up the manufacturer or labeler of a packaged drug by name?
  - id: get-packaged-medication-labeler
    intent: Get a packaged medication labeler
    question: How do I get the details of one drug labeler by ID?
  phrasing_ops: 2
  slug: elation-health-packaged-medication-labelers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Packaged Medications API from Elation Health — 2 operation(s) for packaged medications.
  name: Elation Health Packaged Medications API
  phrasing_intents:
  - id: find-packaged-medications
    intent: Search packaged medications by NDC or name
    question: Can I look up a drug package by its NDC code?
  - id: get-packaged-medication
    intent: Get one packaged medication
    question: What package size and NDC details come back for one packaged medication?
  phrasing_ops: 2
  slug: elation-health-packaged-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The patient chart import API from Elation Health — 3 operation(s) for patient chart import.
  name: Elation Health patient chart import API
  phrasing_intents:
  - id: findchartsByStatus
    intent: List chart imports by status
    question: Which patient chart imports in a data import request are still pending?
  - id: addchart
    intent: Add a patient chart to an import request
    question: How do I load a patient's chart JSON into a data import request?
  - id: getPatientChartImportById
    intent: Get one patient chart import
    question: How do I check the state of one chart import?
  - id: updatepatient-chart-import
    intent: Replace a patient chart import
    question: Can I resend the full chart JSON for an import that already exists?
  - id: updatepatient-chart-importWithForm
    intent: Change a chart import's status with form data
    question: Can I update only the status of a chart import using form data?
  - id: deletepatient-chart-import
    intent: Delete a patient chart import
    question: How do I drop a chart from a data import request?
  - id: uploadFile
    intent: Upload a document for rendering
    question: How do I upload a document to be rendered as part of a chart import?
  phrasing_ops: 7
  slug: elation-health-patient-chart-import-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Form Requests API from Elation Health — 4 operation(s) for patient form requests.
  name: Elation Health Patient Form Requests API
  phrasing_intents:
  - id: create-patient-form-request
    intent: Send a patient forms request (legacy)
    question: How do I ask a patient to complete intake forms through the unversioned route?
  - id: list-patient-form-requests
    intent: List patient form requests (legacy)
    question: How do I see which intake forms we've asked patients to fill out, via the older endpoint?
  - id: delete-patient-form-request
    intent: Cancel a patient form request (legacy)
    question: How do I withdraw a form request sent by mistake, using the older route?
  - id: get-patient-form-request
    intent: Get a patient form request (legacy)
    question: How do I check one form request's details on the older route?
  - id: update-patient-form-request
    intent: Update a patient form request (legacy)
    question: Can I change which forms a patient was asked to complete on the unversioned route?
  - id: patient_form_requests_list
    intent: List patient form requests with paging
    question: How do I page through patient form requests in the v2.0 API?
  - id: patient_form_requests_create
    intent: Send a patient forms request tied to a visit
    question: Can I send a patient pre-visit forms linked to a specific appointment?
  - id: patient_form_requests_destroy
    intent: Delete a patient form request in v2.0
    question: How do I delete a patient form request through /api/2.0?
  phrasing_ops: 11
  slug: elation-health-patient-form-requests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Form Submissions API from Elation Health — 2 operation(s) for patient form submissions.
  name: Elation Health Patient Form Submissions API
  phrasing_intents:
  - id: patient_form_submissions_list
    intent: List patient form submissions
    question: How do I see the intake forms a patient has already submitted?
  - id: patient_form_submissions_create
    intent: Record a patient's completed form
    question: How do I push a patient's completed questionnaire answers into their chart?
  - id: patient_form_submissions_retrieve
    intent: Retrieve a patient form submission
    question: How do I read the answers from one submitted patient form?
  phrasing_ops: 3
  slug: elation-health-patient-form-submissions-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Forms API from Elation Health — 4 operation(s) for patient forms.
  name: Elation Health Patient Forms API
  phrasing_intents:
  - id: find-patient-forms
    intent: Find patient forms by created date
    question: Which patient intake forms were created at my practice this month?
  - id: get-patient-form
    intent: Get a patient form (legacy Get)
    question: Is there an older call to get a patient form?
  - id: patient_forms_list
    intent: List patient forms with paging
    question: Can I page through patient forms with limit and offset?
  - id: patient_forms_retrieve
    intent: Retrieve a patient form
    question: How do I retrieve a single patient form by id?
  phrasing_ops: 4
  slug: elation-health-patient-forms-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Insurances API from Elation Health — 2 operation(s) for patient insurances.
  name: Elation Health Patient Insurances API
  phrasing_intents:
  - id: get-eligibility
    intent: Get a patient insurance's eligibility result
    question: Is this patient's insurance coverage active according to the last eligibility check?
  - id: create-eligibility
    intent: Run an insurance eligibility check
    question: How do I run a real-time eligibility check on a patient's insurance?
  - id: get-eligibility-full-report
    intent: Get the full eligibility report
    question: Where can I see the complete payer response for a patient's eligibility check?
  phrasing_ops: 3
  slug: elation-health-patient-insurances-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Letter Categories API from Elation Health — 2 operation(s) for patient letter categories.
  name: Elation Health Patient Letter Categories API
  phrasing_intents:
  - id: patient_letter_categories_list
    intent: List patient letter categories
    question: What categories can I file patient letters under?
  - id: patient_letter_categories_retrieve
    intent: Get a patient letter category
    question: How do I look up one patient letter category by id?
  phrasing_ops: 2
  slug: elation-health-patient-letter-categories-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Letters (BETA) API from Elation Health — 4 operation(s) for patient letters (beta).
  name: Elation Health Patient Letters (BETA) API
  phrasing_intents:
  - id: patient_letters_comments_list
    intent: List comments on a patient letter
    question: What comments have been left on a patient letter?
  - id: patient_letters_comments_create
    intent: Comment on a patient letter
    question: How do I add a comment to a patient letter?
  - id: patient_letters_comments_destroy
    intent: Delete a comment on a patient letter
    question: Is there a way to remove a comment from a patient letter?
  - id: patient_letters_comments_retrieve
    intent: Get one comment on a patient letter
    question: Can I read one specific comment on a patient letter?
  - id: patient_letters_list
    intent: List patient letters
    question: Which patient letters are still unread?
  - id: patient_letters_create
    intent: Write a patient letter
    question: How do I draft a letter to a patient?
  - id: patient_letters_retrieve
    intent: Get a patient letter
    question: Where can I open a single patient letter by id?
  - id: patient_letters_partial_update
    intent: Sign, send or acknowledge a patient letter
    question: How do I send a patient letter after it has been signed?
  phrasing_ops: 9
  slug: elation-health-patient-letters-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Profile Photo API from Elation Health — 2 operation(s) for patient profile photo.
  name: Elation Health Patient Profile Photo API
  phrasing_intents:
  - id: patients_get_photo_retrieve
    intent: Get a patient's photo via get_photo
    question: Is there a get_photo endpoint for downloading a patient's picture?
  - id: patients_profile_image_destroy
    intent: Delete a patient's profile image
    question: How do I remove a patient's profile picture in /api/2.0?
  - id: patients_profile_image_retrieve
    intent: Get a patient's profile image
    question: How do I show a patient's profile image in my app?
  - id: patients_profile_image_create
    intent: Upload a patient's profile image
    question: How do I upload a new headshot for a patient as base64?
  phrasing_ops: 4
  slug: elation-health-patient-profile-photo-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Provider Team Members API from Elation Health — 2 operation(s) for patient provider team members.
  name: Elation Health Patient Provider Team Members API
  phrasing_intents:
  - id: create-a-patientproviderteammember
    intent: Add a provider to a patient's care team
    question: How do I add a physician to a patient's provider team?
  - id: update-patientproviderteammember-details
    intent: Update a care team member's treatment reason
    question: Can I change the treatment reason for a provider on a care team?
  - id: delete-patientproviderteammember
    intent: Remove a provider from a patient's care team
    question: Can I take a provider off a patient's care team?
  phrasing_ops: 3
  slug: elation-health-patient-provider-team-members-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Patient Provider Teams API from Elation Health — 2 operation(s) for patient provider teams.
  name: Elation Health Patient Provider Teams API
  phrasing_intents:
  - id: get-patient-provider-teams
    intent: List patient provider teams
    question: What care teams are set up to look after patients in our practice?
  - id: list-patientproviderteammembers-of-a-given-team
    intent: List members of a provider team
    question: Who belongs to a specific patient care team?
  phrasing_ops: 2
  slug: elation-health-patient-provider-teams-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pharmacies API from Elation Health — 4 operation(s) for pharmacies.
  name: Elation Health Pharmacies API
  phrasing_intents:
  - id: get-pharmacy
    intent: Look up a pharmacy by NCPDP id (legacy)
    question: How do I look up a pharmacy by its NCPDP id on the legacy endpoint?
  - id: find-pharmacy-wip
    intent: Find pharmacies by active window (WIP)
    question: Is there a work-in-progress pharmacy search by active time on the legacy endpoint?
  - id: pharmacies_list
    intent: List pharmacies
    question: Which pharmacies can I send prescriptions to in Elation?
  - id: pharmacies_retrieve
    intent: Get one pharmacy
    question: How do I get a pharmacy's details by NCPDP id in v2?
  phrasing_ops: 4
  slug: elation-health-pharmacies-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Practice Medications API from Elation Health — 4 operation(s) for practice medications.
  name: Elation Health Practice Medications API
  phrasing_intents:
  - id: find-practice-medications
    intent: Search custom practice medications (legacy)
    question: Can I look up a practice's custom medications by name on the older unversioned path?
  - id: create-practice-medication
    intent: Add a custom practice medication (legacy)
    question: What does the legacy call need to add a medication that isn't in the drug database?
  - id: obsolete-practice-medication
    intent: Mark a custom practice medication obsolete
    question: How do I retire a custom medication so it stops showing up for prescribing?
  - id: fetch-practice-medication
    intent: Look up a custom practice medication (legacy)
    question: What does the unversioned endpoint return for one practice medication?
  - id: practice_medications_list
    intent: List custom practice medications
    question: How do I list the custom medications my practice has defined?
  - id: practice_medications_create
    intent: Create a custom practice medication
    question: Can I add a custom drug with its NDCs and RxNorm codes in API v2.0?
  - id: practice_medications_destroy
    intent: Delete a custom practice medication
    question: Can I delete a custom medication that was added by mistake?
  - id: practice_medications_retrieve
    intent: Get one custom practice medication
    question: What does a single v2.0 practice medication record contain?
  phrasing_ops: 10
  slug: elation-health-practice-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Prescription Fills API from Elation Health — 2 operation(s) for prescription fills.
  name: Elation Health Prescription Fills API
  phrasing_intents:
  - id: get-fill
    intent: Get one prescription fill
    question: How do I check a single prescription fill?
  - id: find-prescription-fills
    intent: Find prescription fills
    question: Which of a patient's prescriptions have actually been filled?
  phrasing_ops: 2
  slug: elation-health-prescription-fills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Print Headers API from Elation Health — 4 operation(s) for print headers.
  name: Elation Health Print Headers API
  phrasing_intents:
  - id: find-print-headers
    intent: Find a practice's print headers (legacy)
    question: How do I see the letterhead print headers set up for my practice on the legacy endpoint?
  - id: get-print-header
    intent: Look up a print header (legacy)
    question: Can I fetch one print header from the legacy unversioned path?
  - id: print_headers_list
    intent: List print headers
    question: Which print headers are available for printed documents in Elation?
  - id: print_headers_destroy
    intent: Delete a print header
    question: How do I delete a print header we no longer use?
  - id: print_headers_retrieve
    intent: Get one print header
    question: How do I read the details of one print header in v2?
  phrasing_ops: 5
  slug: elation-health-print-headers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Provider Team API from Elation Health — 6 operation(s) for provider team.
  name: Elation Health Provider Team API
  phrasing_intents:
  - id: patient_provider_team_members_create
    intent: Add a physician to a patient's care team
    question: How do I add a physician to a patient's provider team in Elation?
  - id: patient_provider_team_members_destroy
    intent: Remove a physician from a care team
    question: How do I take a physician off a patient's care team?
  - id: patient_provider_team_members_partial_update
    intent: Change a care team member's rank or group
    question: Can I change the rank of a physician on a patient's care team?
  - id: patient_provider_team_members_update
    intent: Replace a care team member
    question: Can I replace a care team member's whole record?
  - id: patient_provider_teams_list
    intent: List patient provider teams
    question: Which patient care teams exist across my practice?
  - id: patient_provider_teams_retrieve
    intent: Get a provider team by id
    question: How do I look up one provider team by its team id?
  - id: patient_provider_teams_team_members_retrieve
    intent: List the members of a provider team
    question: Who are the physicians on a given provider team?
  - id: patients_patient_provider_team_retrieve
    intent: Get a patient's provider team
    question: How do I find the care team for a specific patient?
  phrasing_ops: 9
  slug: elation-health-provider-team-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pulmonary Centers API from Elation Health — 4 operation(s) for pulmonary centers.
  name: Elation Health Pulmonary Centers API
  phrasing_intents:
  - id: find-pulmonary-centers
    intent: Find pulmonary centers (legacy endpoint)
    question: Which pulmonary testing centers can my practice send patients to, per the legacy lookup?
  - id: get-pulmonary-center
    intent: Get a pulmonary center (legacy endpoint)
    question: Can I look up one pulmonary center's details on the legacy path?
  - id: pulmonary_centers_list
    intent: List pulmonary centers in API 2.0
    question: How do I list pulmonary centers in the 2.0 API?
  - id: pulmonary_centers_retrieve
    intent: Retrieve a pulmonary center in API 2.0
    question: How do I retrieve a single pulmonary center by ID in API 2.0?
  phrasing_ops: 4
  slug: elation-health-pulmonary-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pulmonary Order Tests API from Elation Health — 4 operation(s) for pulmonary order tests.
  name: Elation Health Pulmonary Order Tests API
  phrasing_intents:
  - id: find-pulmonary-order-tests
    intent: Find pulmonary tests by name
    question: Which pulmonary tests, like spirometry, can my practice order?
  - id: create-pulmonary-order-test
    intent: Add a pulmonary test (legacy)
    question: How do I add an orderable pulmonary test with the older create?
  - id: get-pulmonary-order-test
    intent: Get a pulmonary test type (Get)
    question: How do I get an orderable pulmonary test by id?
  - id: pulmonary_order_tests_list
    intent: List pulmonary tests with paging
    question: Can I page through all pulmonary order tests?
  - id: pulmonary_order_tests_create
    intent: Create a pulmonary order test
    question: What's needed to create a new pulmonary order test?
  - id: pulmonary_order_tests_destroy
    intent: Delete a pulmonary order test
    question: How do I delete a pulmonary order test?
  - id: pulmonary_order_tests_retrieve
    intent: Retrieve a pulmonary order test
    question: Can I retrieve a single pulmonary order test?
  phrasing_ops: 7
  slug: elation-health-pulmonary-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Pulmonary Orders API from Elation Health — 4 operation(s) for pulmonary orders.
  name: Elation Health Pulmonary Orders API
  phrasing_intents:
  - id: get-pulmonary-order
    intent: Get a pulmonary order (Get)
    question: How do I get a patient's pulmonary function test order?
  - id: put-pulmonary-order
    intent: Overwrite a pulmonary order (legacy PUT)
    question: Can I overwrite a pulmonary order with the older PUT call?
  - id: patch-pulmonary-order
    intent: Patch a pulmonary order (legacy PATCH)
    question: Can I change a pulmonary order's ICD-10 codes with the legacy PATCH?
  - id: delete-pulmonary-order
    intent: Delete a pulmonary order (legacy)
    question: How do I cancel a pulmonary order with the older delete call?
  - id: find-pulmonary-orders
    intent: Find pulmonary orders for a patient
    question: Which pulmonary orders has a patient had, per the legacy endpoint?
  - id: create-pulmonary-order
    intent: Order pulmonary tests (legacy create)
    question: How do I order a pulmonary function test with the older create call?
  - id: pulmonary_orders_list
    intent: List pulmonary orders with paging
    question: Can I page through pulmonary orders with limit and offset?
  - id: pulmonary_orders_create
    intent: Create a pulmonary order with allergies
    question: Can I create a pulmonary order that lists the patient's allergies?
  phrasing_ops: 12
  slug: elation-health-pulmonary-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Recurring Event Groups API from Elation Health — 5 operation(s) for recurring event groups.
  name: Elation Health Recurring Event Groups API
  phrasing_intents:
  - id: get-recurring-event-group
    intent: Get a recurring event group (legacy)
    question: How do I see the details of one recurring calendar block on the older endpoint?
  - id: delete-recurring-event-group
    intent: Delete a recurring event group (legacy)
    question: How do I remove a repeating calendar block with the older delete call?
  - id: create-recurring-event-group
    intent: Create a recurring event group (legacy)
    question: Is there an older unversioned route for adding a repeating calendar block?
  - id: find-recurring-event-group
    intent: Find recurring event groups (legacy)
    question: Which recurring blocks are on a physician's calendar, per the older endpoint?
  - id: update-recurring-event-group
    intent: Update a recurring event group (legacy)
    question: Is there an older colon-path route for editing a repeating calendar block?
  - id: recurring_event_groups_list
    intent: List recurring event groups with filters
    question: How do I page through recurring calendar blocks in the v2.0 API?
  - id: recurring_event_groups_create
    intent: Create a recurring event group in v2.0
    question: How do I block off a repeating time slot on the calendar through /api/2.0?
  - id: recurring_event_groups_destroy
    intent: Delete a recurring event group in v2.0
    question: How do I delete a recurring calendar block through /api/2.0?
  phrasing_ops: 9
  slug: elation-health-recurring-event-groups-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reference Medication (Beta) API from Elation Health — 2 operation(s) for reference medication (beta).
  name: Elation Health Reference Medication (Beta) API
  phrasing_intents:
  - id: reference_medications_list
    intent: Search reference medications
    question: How do I find a drug in the reference medication list by NDC?
  - id: reference_medications_retrieve
    intent: Get a reference medication
    question: Can I read one reference medication by id?
  phrasing_ops: 2
  slug: elation-health-reference-medication-beta-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reference Medications API from Elation Health — 2 operation(s) for reference medications.
  name: Elation Health Reference Medications API
  phrasing_intents:
  - id: get-reference-medication
    intent: Get a reference medication
    question: How do I look up one drug in the medication reference by ID?
  - id: find-reference-medications
    intent: Search reference medications
    question: How do I find a medication by its NDC code?
  phrasing_ops: 2
  slug: elation-health-reference-medications-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Referral Orders API from Elation Health — 2 operation(s) for referral orders.
  name: Elation Health Referral Orders API
  phrasing_intents:
  - id: get-referral-order
    intent: Get a referral order
    question: Can I look up a referral order by id?
  - id: premium-post-referral-order
    intent: Create a referral order
    question: How do I refer a patient to a specialist?
  - id: premium-update-referral-order
    intent: Replace a referral order
    question: Can I overwrite a referral order in full, including the consultant?
  - id: premium-update-referral-order-1
    intent: Update part of a referral order
    question: Can I just add a resolution to an existing referral order?
  phrasing_ops: 4
  slug: elation-health-referral-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Referrals API from Elation Health — 4 operation(s) for referrals.
  name: Elation Health Referrals API
  phrasing_intents:
  - id: letters_list
    intent: Find letters by patient and date
    question: How do I find the letters sent about a patient in Elation?
  - id: letters_create
    intent: Send a letter about a patient
    question: How do I send a referral letter to a contact by fax or direct message?
  - id: letters_retrieve
    intent: Get one letter
    question: How do I read one letter including its fax status?
  - id: letters_partial_update
    intent: Edit part of a letter
    question: Can I change just the subject of a letter already drafted?
  - id: letters_update
    intent: Replace a letter
    question: Can I replace an entire letter record?
  - id: referral_orders_list
    intent: List referral orders
    question: Which referral orders exist across my practice?
  - id: referral_orders_create
    intent: Refer a patient to a specialist
    question: How do I create a referral order to a specialist for a patient?
  - id: referral_orders_retrieve
    intent: Get one referral order
    question: How do I see the specialty and consultant on one referral order?
  phrasing_ops: 10
  slug: elation-health-referrals-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Refills API from Elation Health — 2 operation(s) for refills.
  name: Elation Health Refills API
  phrasing_intents:
  - id: medication_refills_list
    intent: List medication refill requests
    question: How do I see the refill requests pharmacies have sent for a patient?
  - id: medication_refills_retrieve
    intent: Get one medication refill request
    question: What details come with a single refill request?
  phrasing_ops: 2
  slug: elation-health-refills-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Report Internal Notes API from Elation Health — 2 operation(s) for report internal notes.
  name: Elation Health Report Internal Notes API
  phrasing_intents:
  - id: reports_internal_notes_list
    intent: List internal notes on a report
    question: What internal notes has staff left on a lab or imaging report?
  - id: reports_internal_notes_create
    intent: Add an internal note to a report
    question: How do I add a staff-only note to a report?
  - id: reports_internal_notes_destroy
    intent: Delete an internal note from a report
    question: How do I delete an internal note left on a report?
  - id: reports_internal_notes_retrieve
    intent: Get one internal note on a report
    question: Can I read a specific internal note on a report?
  - id: reports_internal_notes_partial_update
    intent: Edit an internal note on a report
    question: Can I edit the text of an internal note on a report?
  phrasing_ops: 5
  slug: elation-health-report-internal-notes-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Report Types API from Elation Health — 4 operation(s) for report types.
  name: Elation Health Report Types API
  phrasing_intents:
  - id: find-report-types
    intent: Search report types (legacy)
    question: Which report types can I file on the older unversioned endpoint?
  - id: get-report-type
    intent: Look up a report type (legacy)
    question: What does the legacy endpoint return for one report type?
  - id: report_types_list
    intent: List report types
    question: How do I list the report types available when filing a report?
  - id: report_types_retrieve
    intent: Get one report type
    question: What does a single v2.0 report type record contain?
  phrasing_ops: 4
  slug: elation-health-report-types-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reports API from Elation Health — 9 operation(s) for reports.
  name: Elation Health Reports API
  phrasing_intents:
  - id: get-report
    intent: Look up a report (legacy endpoint)
    question: Can I pull a single lab or imaging report by id from the older unversioned reports path?
  - id: delete-report
    intent: Delete a report (legacy endpoint)
    question: Is there a way to remove a report from a chart through the old unversioned API?
  - id: sign-report
    intent: Sign off on a report (legacy endpoint)
    question: How do I mark a lab report as signed by a physician on the legacy path?
  - id: find-reports
    intent: Search reports by patient and date (legacy)
    question: Can I search the legacy reports list for one patient's results within a document date window?
  - id: create-report
    intent: File a new report to a chart (legacy)
    question: What fields must I supply to file a lab result report with the legacy create call?
  - id: retrieve-the-printable-report-view
    intent: Download a report as a printable PDF (legacy)
    question: Can I get a PDF of a lab report to print from the legacy printable link?
  - id: reports_list
    intent: List reports with date filters and paging
    question: How do I list a patient's lab and imaging reports in Elation?
  - id: reports_create
    intent: Create a report in a patient chart
    question: What's required to add a new report to a patient's chart through API v2.0?
  phrasing_ops: 17
  slug: elation-health-reports-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Reports Ext API from Elation Health — 1 operation(s) for reports ext.
  name: Elation Health Reports Ext API
  phrasing_intents:
  - id: create-external-report
    intent: Submit an external report
    question: Can an outside lab or partner push a report into a chart through the external reports endpoint?
  phrasing_ops: 1
  slug: elation-health-reports-ext-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Service Locations API from Elation Health — 4 operation(s) for service locations.
  name: Elation Health Service Locations API
  phrasing_intents:
  - id: find-service-location
    intent: List service locations (legacy endpoint)
    question: What service locations does my practice have, per the legacy endpoint?
  - id: create-service-location
    intent: Add a service location (legacy endpoint)
    question: How do I add a new office location for my practice through the legacy endpoint?
  - id: get-service-location
    intent: Get a service location (legacy endpoint)
    question: How do I look up one service location by id on the legacy path?
  - id: update-service-location
    intent: Change a service location's contact info (legacy)
    question: Can I update just the phone or fax of a location with the legacy PATCH?
  - id: update-service-location-1
    intent: Replace a service location (legacy PUT)
    question: Can I overwrite a whole service location with the legacy PUT?
  - id: delete-service-location
    intent: Delete a service location (legacy endpoint)
    question: How do I remove a closed office location using the legacy endpoint?
  - id: service_locations_list
    intent: List service locations (v2.0)
    question: How do I page through service locations in the 2.0 API?
  - id: service_locations_create
    intent: Add a service location (v2.0)
    question: How do I create a service location with a timezone in version 2.0?
  phrasing_ops: 12
  slug: elation-health-service-locations-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Sleep Centers API from Elation Health — 4 operation(s) for sleep centers.
  name: Elation Health Sleep Centers API
  phrasing_intents:
  - id: find-sleep-centers
    intent: Find sleep centers by location
    question: Which sleep centers can I refer a patient to for a sleep study?
  - id: get-sleep-center
    intent: Get a sleep center (Get)
    question: How do I get a sleep center's details by id?
  - id: sleep_centers_list
    intent: List sleep centers with paging
    question: Can I page through all sleep centers with limit and offset?
  - id: sleep_centers_retrieve
    intent: Retrieve a sleep center
    question: Where do I retrieve a single sleep center record?
  phrasing_ops: 4
  slug: elation-health-sleep-centers-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Sleep Order Tests API from Elation Health — 4 operation(s) for sleep order tests.
  name: Elation Health Sleep Order Tests API
  phrasing_intents:
  - id: find-sleep-order-tests
    intent: Find sleep study tests (legacy endpoint)
    question: Which sleep study tests can my practice order, per the legacy lookup?
  - id: create-sleep-order-test
    intent: Add a sleep study test (legacy endpoint)
    question: How do I add a custom sleep study test to my practice's list via the legacy endpoint?
  - id: get-sleep-order-test
    intent: Get a sleep study test (legacy endpoint)
    question: Can I look up one sleep order test on the legacy path?
  - id: sleep_order_tests_list
    intent: List sleep order tests in API 2.0
    question: How do I list the sleep order tests in the 2.0 API?
  - id: sleep_order_tests_create
    intent: Create a sleep order test in API 2.0
    question: How do I create a new sleep order test with the 2.0 API?
  - id: sleep_order_tests_destroy
    intent: Delete a sleep order test in API 2.0
    question: How do I delete a sleep order test in the 2.0 API?
  - id: sleep_order_tests_retrieve
    intent: Retrieve a sleep order test in API 2.0
    question: How do I retrieve a single sleep order test by ID in API 2.0?
  phrasing_ops: 7
  slug: elation-health-sleep-order-tests-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Sleep Orders API from Elation Health — 4 operation(s) for sleep orders.
  name: Elation Health Sleep Orders API
  phrasing_intents:
  - id: get-sleep-order
    intent: Look up a sleep study order (legacy)
    question: Can I pull one sleep study order by id from the older unversioned endpoint?
  - id: put-sleep-order
    intent: Replace a sleep study order (legacy PUT)
    question: Which legacy PUT overwrites an entire sleep study order?
  - id: patch-sleep-order
    intent: Patch a sleep study order (legacy PATCH)
    question: Can I change only the sleep center on an order with the legacy PATCH?
  - id: delete-sleep-order
    intent: Delete a sleep study order (legacy)
    question: Can I cancel a sleep study order by deleting it on the unversioned API?
  - id: find-sleep-orders
    intent: Search sleep study orders (legacy)
    question: Can I find a patient's sleep study orders on the legacy unversioned path?
  - id: create-sleep-order
    intent: Order a sleep study (legacy)
    question: What must I send to place a sleep study order through the legacy endpoint?
  - id: sleep_orders_list
    intent: List sleep study orders
    question: How do I list the sleep study orders for one patient?
  - id: sleep_orders_create
    intent: Place a sleep study order
    question: What's required to order a sleep study for a patient in API v2.0?
  phrasing_ops: 12
  slug: elation-health-sleep-orders-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Staff Group API from Elation Health — 1 operation(s) for staff group.
  name: Elation Health Staff Group API
  phrasing_intents:
  - id: get-staff-group
    intent: Get a staff group
    question: How do I look up a staff group by id?
  phrasing_ops: 1
  slug: elation-health-staff-group-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Staff Groups API from Elation Health — 4 operation(s) for staff groups.
  name: Elation Health Staff Groups API
  phrasing_intents:
  - id: find-staff-group
    intent: Find staff groups (legacy)
    question: How do I look up a staff group by name on the older endpoint?
  - id: create-staff-group
    intent: Create a staff group (legacy)
    question: How do I group front-desk users together through the unversioned route?
  - id: delete-a-staff-group
    intent: Delete a staff group (legacy)
    question: How do I remove a staff group with the older delete call?
  - id: update-staff-group
    intent: Update a staff group (legacy)
    question: How do I change a staff group's members on the older PUT route?
  - id: staff_groups_list
    intent: List staff groups with paging
    question: How do I page through staff groups in the v2.0 API?
  - id: staff_groups_create
    intent: Create a staff group in the v2.0 API
    question: What does /api/2.0 require to create a staff group?
  - id: staff_groups_destroy
    intent: Delete a staff group in the v2.0 API
    question: How do I delete a staff group through /api/2.0?
  - id: staff_groups_retrieve
    intent: Retrieve a staff group from the v2.0 API
    question: How do I fetch one staff group and its members from /api/2.0?
  phrasing_ops: 10
  slug: elation-health-staff-groups-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Thread Members API from Elation Health — 5 operation(s) for thread members.
  name: Elation Health Thread Members API
  phrasing_intents:
  - id: get-thread-member
    intent: Get a message thread member (legacy endpoint)
    question: Can I look up one participant of a message thread on the legacy path?
  - id: update-thread-member
    intent: Update a thread member's status (legacy PATCH)
    question: How do I mark a message thread as acknowledged for a member with the legacy PATCH?
  - id: find-thread-members
    intent: Find thread members (legacy endpoint)
    question: Which message threads is a given user a member of, per the legacy search?
  - id: create-thread-member
    intent: Add someone to a message thread (legacy endpoint)
    question: How do I add a user to an existing message thread through the legacy endpoint?
  - id: delete-thread-member
    intent: Remove a thread member (legacy endpoint)
    question: Is there a legacy call to take someone off a message thread?
  - id: thread_members_list
    intent: List thread members in API 2.0
    question: How do I list everyone on a specific message thread in the 2.0 API?
  - id: thread_members_create
    intent: Create a thread member in API 2.0
    question: How do I add a participant to a message thread with the 2.0 API?
  - id: thread_members_destroy
    intent: Delete a thread member in API 2.0
    question: How do I remove a participant from a thread in the 2.0 API?
  phrasing_ops: 11
  slug: elation-health-thread-members-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Thread Messages API from Elation Health — 5 operation(s) for thread messages.
  name: Elation Health Thread Messages API
  phrasing_intents:
  - id: get-thread-message
    intent: Get a message in a thread (Get)
    question: How do I get the body of one message in a patient thread?
  - id: delete-thread-message
    intent: Delete a thread message (legacy)
    question: How do I delete a single message from a thread with the older call?
  - id: find-thread-messages
    intent: Find thread messages (unfiltered)
    question: Can I pull every thread message without any filters?
  - id: create-thread-message
    intent: Post a message to a thread
    question: How do I add a reply to an existing message thread on the legacy endpoint?
  - id: find-thread-messages-wip
    intent: Find thread messages by thread (WIP)
    question: Is there a WIP endpoint to find messages by thread or sender?
  - id: create-thread-message-wip
    intent: Post a thread message (WIP)
    question: Does the work-in-progress API let me post a thread message?
  - id: thread_messages_list
    intent: List thread messages with paging
    question: Can I page through thread messages with limit and offset?
  - id: thread_messages_create
    intent: Create a thread message for a patient
    question: Can I create a thread message tied to a patient and practice?
  phrasing_ops: 10
  slug: elation-health-thread-messages-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Users API from Elation Health — 4 operation(s) for users.
  name: Elation Health Users API
  phrasing_intents:
  - id: post
    intent: Create a user (legacy)
    question: What does the older unversioned endpoint need to add a new user to a practice?
  - id: update-user
    intent: Update a user (legacy)
    question: Can I deactivate a user through the legacy update call?
  - id: users_list
    intent: List users
    question: How do I list everyone with a login at my practices?
  - id: users_create
    intent: Create a user
    question: Can I make a new user a practice admin or read-only in API v2.0?
  - id: users_retrieve
    intent: Get one user's details
    question: What does a single v2.0 user record show?
  - id: users_partial_update
    intent: Edit a user's settings
    question: Can I promote a user to practice admin in v2.0?
  phrasing_ops: 6
  slug: elation-health-users-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Vaccine API from Elation Health — 2 operation(s) for vaccine.
  name: Elation Health Vaccine API
  phrasing_intents:
  - id: vaccine_list
    intent: List vaccines
    question: How do I look up a vaccine by its CVX code?
  - id: vaccine_create
    intent: Add a vaccine to the practice list
    question: How do I add a custom vaccine with its NDC to our practice?
  - id: vaccine_destroy
    intent: Delete a vaccine
    question: How do I remove a vaccine entry we added by mistake?
  - id: vaccine_retrieve
    intent: Retrieve a vaccine
    question: How do I see the CVX and NDC details for one vaccine?
  phrasing_ops: 4
  slug: elation-health-vaccine-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Vaccines API from Elation Health — 1 operation(s) for vaccines.
  name: Elation Health Vaccines API
  phrasing_intents:
  - id: get-vaccine
    intent: Get a vaccine
    question: How do I look up a vaccine by id?
  - id: delete-vaccine
    intent: Delete a practice-created vaccine
    question: Can I delete a vaccine my practice added?
  phrasing_ops: 2
  slug: elation-health-vaccines-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Visit Note Templates API from Elation Health — 4 operation(s) for visit note templates.
  name: Elation Health Visit Note Templates API
  phrasing_intents:
  - id: find-visit-note-templates
    intent: Find visit note templates (legacy endpoint)
    question: What visit note templates does my practice have, via the legacy endpoint?
  - id: get-visit-note-template
    intent: Get a visit note template (legacy endpoint)
    question: Can I read a single visit note template on the legacy path?
  - id: update-visit-note-template
    intent: Update a visit note template (legacy PATCH)
    question: Can I rename a visit note template with the legacy PATCH?
  - id: delete-visit-note-template
    intent: Delete a visit note template (legacy endpoint)
    question: Is there a legacy call to delete a visit note template we no longer use?
  - id: visit_note_templates_list
    intent: List visit note templates in API 2.0
    question: How do I list visit note templates by name in the 2.0 API?
  - id: visit_note_templates_create
    intent: Create a visit note template in API 2.0
    question: How do I create a new visit note template with the 2.0 API?
  - id: visit_note_templates_destroy
    intent: Delete a visit note template in API 2.0
    question: How do I delete a visit note template in the 2.0 API?
  - id: visit_note_templates_retrieve
    intent: Retrieve a visit note template in API 2.0
    question: How do I retrieve one visit note template by ID in API 2.0?
  phrasing_ops: 10
  slug: elation-health-visit-note-templates-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Visit Note Types API from Elation Health — 5 operation(s) for visit note types.
  name: Elation Health Visit Note Types API
  phrasing_intents:
  - id: find-visit-note-types
    intent: List visit note types (legacy endpoint)
    question: What visit note types can clinicians pick from, per the legacy endpoint?
  - id: get-visit-note-types
    intent: Get a visit note type (legacy endpoint)
    question: Can I look up one visit note type on the legacy path?
  - id: delete-visit-note-type
    intent: Delete a visit note type (legacy endpoint)
    question: How do I remove a visit note type using the legacy endpoint?
  - id: update-visit-note-types
    intent: Update a visit note type (legacy PATCH)
    question: Can I rename a visit note type with the legacy PATCH?
  - id: visit_note_types_list
    intent: List visit note types (v2.0)
    question: How do I search visit note types by name in the 2.0 API?
  - id: visit_note_types_create
    intent: Create a visit note type (v2.0)
    question: How do I add a new visit note type in version 2.0?
  - id: visit_note_types_destroy
    intent: Delete a visit note type (v2.0)
    question: What's the 2.0 way to delete a visit note type?
  - id: visit_note_types_retrieve
    intent: Get a visit note type (v2.0)
    question: Which 2.0 call fetches a single visit note type?
  phrasing_ops: 10
  slug: elation-health-visit-note-types-api
- baseURL: https://api.app.elationemr.com/api/2.0
  baseurl_source: declared
  description: The Vitals API from Elation Health — 5 operation(s) for vitals.
  name: Elation Health Vitals API
  phrasing_intents:
  - id: get-vital
    intent: Look up a vitals record (legacy)
    question: Can I pull one set of recorded vitals by id from the older unversioned endpoint?
  - id: find-vitals
    intent: Search vitals by patient or note (legacy)
    question: Can I find the vitals attached to a specific visit note on the legacy path?
  - id: create-vital
    intent: Record vitals for a patient (legacy)
    question: What must I send to record a patient's blood pressure and weight through the legacy endpoint?
  - id: update-vitals-1
    intent: Patch a vitals record (legacy PATCH)
    question: Is there a legacy PATCH for correcting part of a vitals record?
  - id: update-vitals
    intent: Replace a vitals record (legacy PUT)
    question: Which legacy PUT overwrites a full set of vitals?
  - id: vitals_list
    intent: List a patient's vitals
    question: How do I list the vitals recorded for one patient?
  - id: vitals_create
    intent: Record a new set of vitals
    question: Can I record pain score and BMI percentile with vitals in API v2.0?
  - id: vitals_retrieve
    intent: Get one vitals record
    question: What does a single v2.0 vitals record include?
  phrasing_ops: 10
  slug: elation-health-vitals-api
artifact_total: 182
asyncapis:
- description: ''
  name: Elation Health Events Webhooks
  slug: elation-health-events-webhooks
collections:
- collection_type: postman
  name: API Authentication
  slug: postman-elation-api-authentication
- collection_type: postman
  name: Billing API
  slug: postman-elation-billing-api
- collection_type: postman
  name: Care Gaps API
  slug: postman-elation-care-gaps-api-1
- collection_type: postman
  name: Elation Import API
  slug: postman-elation-elation-import-api
- collection_type: postman
  name: Event Subscription API
  slug: postman-elation-event-subscription-api
- collection_type: postman
  name: Insurance API
  slug: postman-elation-insurance-api
- collection_type: postman
  name: Messaging API
  slug: postman-elation-messaging-api
- collection_type: postman
  name: Orders API
  slug: postman-elation-orders-api
- collection_type: postman
  name: Patient Document API
  slug: postman-elation-patient-document-api
- collection_type: postman
  name: Patient Profile API
  slug: postman-elation-patient-profile-api
- collection_type: postman
  name: Practice API
  slug: postman-elation-practice-api
- collection_type: postman
  name: '[Premium] Patient Insurance API'
  slug: postman-elation-premium-patient-insurance-api
- collection_type: postman
  name: Reference Data API
  slug: postman-elation-reference-data-api
- collection_type: postman
  name: Scheduling API
  slug: postman-elation-scheduling-api
- collection_type: postman
  name: User Management API
  slug: postman-elation-user-management-api
- collection_type: postman
  name: Visit Notes API
  slug: postman-elation-visit-notes-api
- collection_type: open
  name: API Authentication
  slug: open-elation-api-authentication
- collection_type: open
  name: API Settings
  slug: open-elation-api-settings
- collection_type: open
  name: Billing API
  slug: open-elation-billing-api
- collection_type: open
  name: Care Gaps API
  slug: open-elation-care-gaps-api-1
- collection_type: open
  name: Elation Import API
  slug: open-elation-elation-import-api
- collection_type: open
  name: Event Subscription API
  slug: open-elation-event-subscription-api
- collection_type: open
  name: Elation Health REST Allergies API
  slug: open-elation-health-allergies-api
- collection_type: open
  name: Elation Health REST Allergies Appointments API
  slug: open-elation-health-appointments-api
- collection_type: open
  name: Elation Health REST Allergies Authentication API
  slug: open-elation-health-authentication-api
- collection_type: open
  name: Elation Health REST Allergies Lab Orders API
  slug: open-elation-health-lab-orders-api
- collection_type: open
  name: Elation Health REST Allergies Medications API
  slug: open-elation-health-medications-api
- collection_type: open
  name: Elation Health REST Allergies Patients API
  slug: open-elation-health-patients-api
- collection_type: open
  name: Elation Health REST Allergies Physicians API
  slug: open-elation-health-physicians-api
- collection_type: open
  name: Elation Health REST Allergies Practices API
  slug: open-elation-health-practices-api
- collection_type: open
  name: Elation Health REST Allergies Problems API
  slug: open-elation-health-problems-api
- collection_type: open
  name: Insurance API
  slug: open-elation-insurance-api
- collection_type: open
  name: Messaging API
  slug: open-elation-messaging-api
- collection_type: open
  name: Orders API
  slug: open-elation-orders-api
- collection_type: open
  name: Patient Document API
  slug: open-elation-patient-document-api
- collection_type: open
  name: Patient Profile API
  slug: open-elation-patient-profile-api
- collection_type: open
  name: Practice API
  slug: open-elation-practice-api
- collection_type: open
  name: '[Premium] Patient Insurance API'
  slug: open-elation-premium-patient-insurance-api
- collection_type: open
  name: Reference Data API
  slug: open-elation-reference-data-api
- collection_type: open
  name: Scheduling API
  slug: open-elation-scheduling-api
- collection_type: open
  name: User Management API
  slug: open-elation-user-management-api
- collection_type: open
  name: Visit Notes API
  slug: open-elation-visit-notes-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/capabilities/elation-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/elation-health-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-api-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-api-authentication-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-patient-profile-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-patient-profile-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-visit-notes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-visit-notes-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-patient-document-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-patient-document-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-orders-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-orders-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-scheduling-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-scheduling-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-billing-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-billing-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-insurance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-insurance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-premium-patient-insurance-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-premium-patient-insurance-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-practice-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-practice-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-user-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-user-management-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-messaging-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-messaging-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-event-subscription-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-event-subscription-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-reference-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-reference-data-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-care-gaps-api-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-care-gaps-api-1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-elation-import-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-elation-import-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/overlays/elation-health-api-full-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elation-health-api-full-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/elation-health/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/sandbox/elation-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/elation-health-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/data-model/elation-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elation-health-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/changelog/elation-health-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elation-health-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/conventions/elation-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elation-health-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/lifecycle/elation-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elation-health-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/errors/elation-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elation-health-problem-types.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.elationhealth.com/solutions/ehr/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/conformance/elation-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elation-health-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/mcp/elation-health-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elation-health-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/mcp/elation-health-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elation-health-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/well-known/elation-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elation-health-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/packages/elation-health-packages.yml
  title: ''
  type: Packages
  url: packages/elation-health-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/llms/elation-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elation-health-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/security/elation-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elation-health-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/agentic-access/elation-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elation-health-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/scopes/elation-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/elation-health-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/authentication/elation-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elation-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elationhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.elationhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/docs/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.elationhealth.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.elationhealth.com/docs/getting-started-2
- group: auth
  title: ''
  type: Authentication
  url: https://docs.elationhealth.com/docs/oauth
- group: design
  title: ''
  type: Webhooks
  url: https://docs.elationhealth.com/docs/webhooks
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://docs.elationhealth.com/docs/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth/
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.elationhealth.com/contact-us/sandbox/
- group: operate
  title: ''
  type: Support
  url: https://www.elationhealth.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elationhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elationhealth.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/reference/api-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/resources/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/contact-us/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/elationhealth
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/plans/elation-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elation-health-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/rate-limits/elation-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elation-health-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/finops/elation-health-finops.yml
  title: ''
  type: FinOps
  url: finops/elation-health-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/a2a/elation-health-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/elation-health-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/examples/elation-health-patient-example.json
  title: ''
  type: Examples
  url: examples/elation-health-patient-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/examples/elation-health-appointment-example.json
  title: ''
  type: Examples
  url: examples/elation-health-appointment-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/vocabulary/elation-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/elation-health-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/rules/elation-health-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/elation-health-jsonschema-spectral-rules.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/json-schema/elation-health-patient-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/elation-health-patient-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/json-ld/elation-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/elation-health-context.jsonld
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/skills/elation-health-provider-published-skill.md
  title: ''
  type: AgentSkill
  url: skills/elation-health-provider-published-skill.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.elationhealth.com/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://help.elationhealth.com/articles/rest/overview/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://help.elationhealth.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.elationhealth.com/articles/rest/overview/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://help.elationhealth.com/articles/rest/overview/oauth
- group: auth
  title: ''
  type: OAuthScopes
  url: https://help.elationhealth.com/articles/rest/overview/scopes
- group: design
  title: ''
  type: Webhooks
  url: https://help.elationhealth.com/articles/rest/overview/webhooks
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://help.elationhealth.com/articles/rest/overview/mcp-server
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.elationhealth.com/articles/rest/changelog/changelog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.elationhealth.com/
- group: operate
  title: ''
  type: Support
  url: https://help.elationhealth.com/articles/rest/overview/getting-help
- group: auth
  title: ''
  type: Compliance
  url: https://help.elationhealth.com/compliance-quality
created: '2026-07-24'
description: Elation Health is a United States clinical-first electronic health record (EHR/EMR) and healthcare technology company, founded in 2010 and headquartered in San Francisco, California, serving independent primary care practices, value-based care organizations, digital health startups, and health-tech partners. Beyond its provider-facing EHR, Elation ships a broad, well-documented public REST API (v2.0) that lets partners read and write clinical and administrative data - patient profiles and demographics, allergies and problems, visit notes, clinical and lab/imaging orders, patient documents, scheduling, billing, insurance and eligibility, messaging, practice and user management, care gaps, and data import - authenticated with OAuth2. The API is documented on a ReadMe developer portal backed by machine-readable OpenAPI definitions, augmented with event subscription webhooks and a Model Context Protocol (MCP) server for agentic access. Elation also operates login-gated HL7 FHIR
  R4 and SMART-on-FHIR interoperability endpoints for ONC/CMS 21st Century Cures Act information-blocking compliance, exposed to registered applications rather than anonymously. Positioned as an independent challenger to the US EHR duopoly, Elation targets the primary-care and value-based-care segment of the largest, most commercial healthcare-API market.
examples:
- key_count: 18
  name: Elation Health Appointment Example
  slug: elation-health-appointment-example
- key_count: 25
  name: Elation Health Patient Example
  slug: elation-health-patient-example
finops:
- name: Elation Health Finops
  service_category: ''
  slug: elation-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Patient
  property_count: 43
  slug: elation-health-patient
jsonld:
- class_count: 28
  name: Elation Health Context
  property_count: 69
  slug: elation-health-context
layout: provider
mcp_servers:
- description: ''
  name: Elation Health MCP Server
  slug: elation-health-mcp-server
modified: '2026-08-14'
name: Elation Health
nav: Providers
network: true
overview: 'Elation Health publishes 126 APIs on the [APIs.io](https://apis.io/) network, including Allergies API, Appointments API, Authentication API, and 123 more. Tagged areas include Healthcare, United States, EHR, EMR, and FHIR.


  The Elation Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Elation Health''s developer surface includes sandbox, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 77 more developer resources.'
plans:
- name: Elation Health Plans Pricing
  plan_count: 3
  slug: elation-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Elation Health Rate Limits
  slug: elation-health-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Elation Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: elation-health-jsonschema-spectral-rules
scopes:
- name: Elation Health Scopes
  scope_count: 154
  slug: elation-health-scopes
  summary_line: 154 scopes · clientCredentials/password
score:
  band: exemplar
  composite: 78.0
  coverage:
    artifact_dirs: 34
    catalog_earned: 73.8
    catalog_earned_first_party: 12.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 92.1
    contract_governance: 41.7
    contract_quality: 67.6
    developer_ergonomics: 72.6
    discoverability: 76.7
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 77.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 125
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 57.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/screenshots/elation-health-2026-07-25T213054.png
security:
- kind: authentication
  name: Elation Health Authentication
  slug: elation-health-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Elation Health Domain Security
  slug: elation-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elation-health
tags:
- Healthcare
- United States
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Primary Care
- Value-Based Care
- Eligibility
- Clinical Data
- Scheduling
- e-Prescribing
- Digital Health
- A2A
website: https://www.elationhealth.com/
---
