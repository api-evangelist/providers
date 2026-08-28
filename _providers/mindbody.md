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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 73
  human_in_the_loop: 3
  name: Mindbody Agentic Access
  operation_count: 154
  slug: mindbody-agentic-access
  summary_line: 154 operations · 73 acting · 3 human-in-the-loop
api_count: 13
apis:
- description: Appointment operations.
  name: Mindbody Appointment API
  slug: mindbody-appointment-api
- description: Class operations.
  name: Mindbody Class API
  slug: mindbody-class-api
- description: Client operations.
  name: Mindbody Client API
  slug: mindbody-client-api
- description: Cross Site operations.
  name: Mindbody Cross Site API
  slug: mindbody-cross-site-api
- description: Enrollment operations.
  name: Mindbody Enrollment API
  slug: mindbody-enrollment-api
- description: Metrics operations.
  name: Mindbody Metrics API
  slug: mindbody-metrics-api
- description: Payroll operations.
  name: Mindbody Payroll API
  slug: mindbody-payroll-api
- description: Pick A Spot operations.
  name: Mindbody Pick A Spot API
  slug: mindbody-pick-a-spot-api
- description: Sale operations.
  name: Mindbody Sale API
  slug: mindbody-sale-api
- description: Site operations.
  name: Mindbody Site API
  slug: mindbody-site-api
- description: Staff operations.
  name: Mindbody Staff API
  slug: mindbody-staff-api
- description: Subscriptions operations.
  name: Mindbody Subscriptions API
  slug: mindbody-subscriptions-api
- description: User Token operations.
  name: Mindbody User Token API
  slug: mindbody-user-token-api
arazzos:
- description: Create a new client, find an upcoming class, and book the client into it.
  name: Mindbody Add Client and Book Class
  slug: mindbody-add-client-book-class-workflow
- description: Find bookable appointment availabilities and book an appointment into an open slot.
  name: Mindbody Book Appointment
  slug: mindbody-book-appointment-workflow
- description: List sellable services, check out a cart for a client, and confirm the sale.
  name: Mindbody Browse Services and Checkout
  slug: mindbody-browse-services-checkout-workflow
- description: Check out a shopping cart for a client and confirm the resulting sale.
  name: Mindbody Checkout Cart and Confirm Sale
  slug: mindbody-checkout-cart-confirm-sale-workflow
- description: Find a client by search text and log their arrival at a location.
  name: Mindbody Client Arrival Check-In
  slug: mindbody-client-arrival-checkin-workflow
- description: Find a client and review their active memberships.
  name: Mindbody Client Membership Review
  slug: mindbody-client-membership-review-workflow
- description: Find a client and retrieve their visit history for a date range.
  name: Mindbody Client Visit History
  slug: mindbody-client-visit-history-workflow
- description: List available enrollments and add a client to a chosen enrollment.
  name: Mindbody Enroll Client in Program
  slug: mindbody-enroll-client-in-program-workflow
- description: Find a client and retrieve their purchase history.
  name: Mindbody Find Client Purchases
  slug: mindbody-find-client-purchases-workflow
- description: Issue a staff user token and use it to list clients at a site.
  name: Mindbody Issue User Token and List Clients
  slug: mindbody-issue-token-list-clients-workflow
- description: Find a client and add a contact log entry to their record.
  name: Mindbody Log Client Contact
  slug: mindbody-log-client-contact-workflow
- description: Resolve the activated sites for an API key and list the classes for one site.
  name: Mindbody Resolve Site and List Classes
  slug: mindbody-resolve-site-list-classes-workflow
- description: List a site's locations and retrieve the schedule items for one location.
  name: Mindbody Schedule Items by Location
  slug: mindbody-schedule-items-by-location-workflow
- description: Discover session types, find a bookable slot, and book an appointment.
  name: Mindbody Session Type Book Appointment
  slug: mindbody-session-type-book-appointment-workflow
- description: Resolve a staff member and retrieve their schedule items for a date range.
  name: Mindbody Staff Class Schedule
  slug: mindbody-staff-class-schedule-workflow
- description: Look up a staff member and retrieve their booked appointments for a date range.
  name: Mindbody Staff Schedule Lookup
  slug: mindbody-staff-schedule-lookup-workflow
artifact_total: 1105
collections:
- collection_type: postman
  name: Mindbody Public API v6
  slug: postman-mindbody-public-api-v6-openapi-original
- collection_type: postman
  name: Mindbody Webhooks API
  slug: postman-mindbody-webhooks-api-openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mindbody Public API v6 Appointment API
  slug: open-mindbody-appointment-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Class API
  slug: open-mindbody-class-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Client API
  slug: open-mindbody-client-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Cross Site API
  slug: open-mindbody-cross-site-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Enrollment API
  slug: open-mindbody-enrollment-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Metrics API
  slug: open-mindbody-metrics-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Payroll API
  slug: open-mindbody-payroll-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Pick A Spot API
  slug: open-mindbody-pick-a-spot-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Sale API
  slug: open-mindbody-sale-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Site API
  slug: open-mindbody-site-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Staff API
  slug: open-mindbody-staff-api
- collection_type: open
  name: Mindbody Public API v6 Appointment Subscriptions API
  slug: open-mindbody-subscriptions-api
- collection_type: open
  name: Mindbody Public API v6 Appointment User Token API
  slug: open-mindbody-user-token-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mindbody/Mindbody-API-SDKs/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mindbody-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mindbody-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindbody-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindbody-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mindbody-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mindbody/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-add-client-book-class-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-book-appointment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-browse-services-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-checkout-cart-confirm-sale-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-client-arrival-checkin-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-client-membership-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-client-visit-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-enroll-client-in-program-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-find-client-purchases-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-issue-token-list-clients-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-log-client-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-resolve-site-list-classes-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-schedule-items-by-location-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-session-type-book-appointment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-staff-class-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindbody-staff-schedule-lookup-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.mindbodyonline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mindbodyonline.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mindbodyonline.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.mindbodyonline.com/PublicDocumentation/GettingStarted
- group: start
  title: ''
  type: Signup
  url: https://developers.mindbodyonline.com/Signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mindbodyonline.com/business/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.mindbodyonline.com/s/contactapisupport
- group: operate
  title: ''
  type: FAQ
  url: https://developers.mindbodyonline.com/resources/faqs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mindbodyonline.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mindbody
- group: build
  title: Mindbody-API-SDKs
  type: GitHubRepository
  url: https://github.com/mindbody/Mindbody-API-SDKs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mindbody
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.mindbodyonline.com/Resources/ApiReleaseNotes
- group: commercial
  title: ''
  type: Plans
  url: plans/mindbody-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mindbody-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mindbody-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/mindbody-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mindbody-vocabulary.yml
created: '2026-05-11'
description: Mindbody is a business management and consumer marketplace platform for the fitness, beauty, and wellness industries, providing scheduling, point of sale, client management, marketing, and reporting tools for studios, gyms, salons, and spas. The Mindbody Public API (v6) provides REST endpoints for appointments, classes, clients, enrollments, sales, sites, staff, payroll, and cross-site identity, and is paired with a Webhooks API that pushes real-time event notifications using API key + SiteId headers, with optional OAuth 2.0 bearer tokens from the Mindbody Identity Service for staff- and client-scoped operations.
examples:
- key_count: 5
  name: Public Api V6 Add Appointment Add On Request Example
  slug: public-api-v6-add-appointment-add-on-request-example
- key_count: 2
  name: Public Api V6 Add Appointment Add On Response Example
  slug: public-api-v6-add-appointment-add-on-response-example
- key_count: 3
  name: Public Api V6 Add Appointment Outcome Example
  slug: public-api-v6-add-appointment-outcome-example
- key_count: 19
  name: Public Api V6 Add Appointment Request Example
  slug: public-api-v6-add-appointment-request-example
- key_count: 1
  name: Public Api V6 Add Appointment Response Example
  slug: public-api-v6-add-appointment-response-example
- key_count: 5
  name: Public Api V6 Add Arrival Request Example
  slug: public-api-v6-add-arrival-request-example
- key_count: 2
  name: Public Api V6 Add Arrival Response Example
  slug: public-api-v6-add-arrival-response-example
- key_count: 10
  name: Public Api V6 Add Availabilities Request Example
  slug: public-api-v6-add-availabilities-request-example
- key_count: 2
  name: Public Api V6 Add Availabilities Response Example
  slug: public-api-v6-add-availabilities-response-example
- key_count: 24
  name: Public Api V6 Add Class Enrollment Schedule Request Example
  slug: public-api-v6-add-class-enrollment-schedule-request-example
- key_count: 6
  name: Public Api V6 Add Client Direct Debit Info Request Example
  slug: public-api-v6-add-client-direct-debit-info-request-example
- key_count: 5
  name: Public Api V6 Add Client Direct Debit Info Response Example
  slug: public-api-v6-add-client-direct-debit-info-response-example
- key_count: 60
  name: Public Api V6 Add Client Request Example
  slug: public-api-v6-add-client-request-example
- key_count: 1
  name: Public Api V6 Add Client Response Example
  slug: public-api-v6-add-client-response-example
- key_count: 11
  name: Public Api V6 Add Client To Class Request Example
  slug: public-api-v6-add-client-to-class-request-example
- key_count: 1
  name: Public Api V6 Add Client To Class Response Example
  slug: public-api-v6-add-client-to-class-response-example
- key_count: 23
  name: Public Api V6 Add Client To Class Visit Example
  slug: public-api-v6-add-client-to-class-visit-example
- key_count: 8
  name: Public Api V6 Add Client To Enrollment Request Example
  slug: public-api-v6-add-client-to-enrollment-request-example
- key_count: 10
  name: Public Api V6 Add Contact Log Request Example
  slug: public-api-v6-add-contact-log-request-example
- key_count: 2
  name: Public Api V6 Add Contact Log Type Example
  slug: public-api-v6-add-contact-log-type-example
- key_count: 3
  name: Public Api V6 Add Formula Note Request Example
  slug: public-api-v6-add-formula-note-request-example
- key_count: 1
  name: Public Api V6 Add Multiple Appointments Request Example
  slug: public-api-v6-add-multiple-appointments-request-example
- key_count: 1
  name: Public Api V6 Add Multiple Appointments Response Example
  slug: public-api-v6-add-multiple-appointments-response-example
- key_count: 4
  name: Public Api V6 Add On Small Example
  slug: public-api-v6-add-on-small-example
- key_count: 4
  name: Public Api V6 Add On Small1 Example
  slug: public-api-v6-add-on-small1-example
- key_count: 11
  name: Public Api V6 Add Promo Code Request Example
  slug: public-api-v6-add-promo-code-request-example
- key_count: 1
  name: Public Api V6 Add Promo Code Response Example
  slug: public-api-v6-add-promo-code-response-example
- key_count: 9
  name: Public Api V6 Add Site Client Index Request Example
  slug: public-api-v6-add-site-client-index-request-example
- key_count: 10
  name: Public Api V6 Add Site Client Index Response Example
  slug: public-api-v6-add-site-client-index-response-example
- key_count: 11
  name: Public Api V6 Add Staff Availability Request Example
  slug: public-api-v6-add-staff-availability-request-example
- key_count: 26
  name: Public Api V6 Add Staff Request Example
  slug: public-api-v6-add-staff-request-example
- key_count: 1
  name: Public Api V6 Add Staff Response Example
  slug: public-api-v6-add-staff-response-example
- key_count: 2
  name: Public Api V6 Alternative Payment Method Example
  slug: public-api-v6-alternative-payment-method-example
- key_count: 2
  name: Public Api V6 Amenity Example
  slug: public-api-v6-amenity-example
- key_count: 2
  name: Public Api V6 Amenity1 Example
  slug: public-api-v6-amenity1-example
- key_count: 2
  name: Public Api V6 Api Error1 Example
  slug: public-api-v6-api-error1-example
- key_count: 3
  name: Public Api V6 Applicable Item Example
  slug: public-api-v6-applicable-item-example
- key_count: 5
  name: Public Api V6 Appointment Add On Example
  slug: public-api-v6-appointment-add-on-example
- key_count: 23
  name: Public Api V6 Appointment Example
  slug: public-api-v6-appointment-example
- key_count: 4
  name: Public Api V6 Appointment Option Example
  slug: public-api-v6-appointment-option-example
- key_count: 4
  name: Public Api V6 Appointment Staff Example
  slug: public-api-v6-appointment-staff-example
- key_count: 22
  name: Public Api V6 Appointment1 Example
  slug: public-api-v6-appointment1-example
- key_count: 8
  name: Public Api V6 Assign Staff Session Type Request Example
  slug: public-api-v6-assign-staff-session-type-request-example
- key_count: 8
  name: Public Api V6 Assign Staff Session Type Response Example
  slug: public-api-v6-assign-staff-session-type-response-example
- key_count: 2
  name: Public Api V6 Assigned Client Index Example
  slug: public-api-v6-assigned-client-index-example
- key_count: 3
  name: Public Api V6 Autopay Schedule Example
  slug: public-api-v6-autopay-schedule-example
- key_count: 13
  name: Public Api V6 Availability Example
  slug: public-api-v6-availability-example
- key_count: 13
  name: Public Api V6 Availability1 Example
  slug: public-api-v6-availability1-example
- key_count: 4
  name: Public Api V6 Booking Window Example
  slug: public-api-v6-booking-window-example
- key_count: 4
  name: Public Api V6 Cancel Single Class Request Example
  slug: public-api-v6-cancel-single-class-request-example
- key_count: 1
  name: Public Api V6 Cancel Single Class Response Example
  slug: public-api-v6-cancel-single-class-response-example
- key_count: 8
  name: Public Api V6 Cart Item Example
  slug: public-api-v6-cart-item-example
- key_count: 11
  name: Public Api V6 Category Example
  slug: public-api-v6-category-example
- key_count: 2
  name: Public Api V6 Checkout Alternative Payment Info Example
  slug: public-api-v6-checkout-alternative-payment-info-example
- key_count: 7
  name: Public Api V6 Checkout Appointment Booking Request Example
  slug: public-api-v6-checkout-appointment-booking-request-example
- key_count: 2
  name: Public Api V6 Checkout Item Example
  slug: public-api-v6-checkout-item-example
- key_count: 11
  name: Public Api V6 Checkout Item Wrapper Example
  slug: public-api-v6-checkout-item-wrapper-example
- key_count: 2
  name: Public Api V6 Checkout Payment Info Example
  slug: public-api-v6-checkout-payment-info-example
- key_count: 20
  name: Public Api V6 Checkout Shopping Cart Request Example
  slug: public-api-v6-checkout-shopping-cart-request-example
- key_count: 4
  name: Public Api V6 Checkout Shopping Cart Response Example
  slug: public-api-v6-checkout-shopping-cart-response-example
- key_count: 2
  name: Public Api V6 Class Client Detail Example
  slug: public-api-v6-class-client-detail-example
- key_count: 15
  name: Public Api V6 Class Description Example
  slug: public-api-v6-class-description-example
- key_count: 30
  name: Public Api V6 Class Example
  slug: public-api-v6-class-example
- key_count: 24
  name: Public Api V6 Class Schedule Example
  slug: public-api-v6-class-schedule-example
- key_count: 4
  name: Public Api V6 Client Arrival Example
  slug: public-api-v6-client-arrival-example
- key_count: 23
  name: Public Api V6 Client Contract Example
  slug: public-api-v6-client-contract-example
- key_count: 10
  name: Public Api V6 Client Credit Card Example
  slug: public-api-v6-client-credit-card-example
- key_count: 3
  name: Public Api V6 Client Document Example
  slug: public-api-v6-client-document-example
- key_count: 5
  name: Public Api V6 Client Duplicate Example
  slug: public-api-v6-client-duplicate-example
- key_count: 58
  name: Public Api V6 Client Example
  slug: public-api-v6-client-example
- key_count: 6
  name: Public Api V6 Client Index Example
  slug: public-api-v6-client-index-example
- key_count: 3
  name: Public Api V6 Client Index Value Example
  slug: public-api-v6-client-index-value-example
- key_count: 17
  name: Public Api V6 Client Membership Example
  slug: public-api-v6-client-membership-example
- key_count: 3
  name: Public Api V6 Client Memberships Example
  slug: public-api-v6-client-memberships-example
- key_count: 9
  name: Public Api V6 Client Purchase Record Example
  slug: public-api-v6-client-purchase-record-example
- key_count: 5
  name: Public Api V6 Client Relationship Example
  slug: public-api-v6-client-relationship-example
- key_count: 6
  name: Public Api V6 Client Reward Transaction Example
  slug: public-api-v6-client-reward-transaction-example
- key_count: 14
  name: Public Api V6 Client Service Example
  slug: public-api-v6-client-service-example
- key_count: 16
  name: Public Api V6 Client Service With Activation Type Example
  slug: public-api-v6-client-service-with-activation-type-example
- key_count: 3
  name: Public Api V6 Client Suspension Info Example
  slug: public-api-v6-client-suspension-info-example
- key_count: 2
  name: Public Api V6 Client Type Example
  slug: public-api-v6-client-type-example
- key_count: 59
  name: Public Api V6 Client With Suspension Info Example
  slug: public-api-v6-client-with-suspension-info-example
- key_count: 2
  name: Public Api V6 Color Example
  slug: public-api-v6-color-example
- key_count: 2
  name: Public Api V6 Commission Detail Example
  slug: public-api-v6-commission-detail-example
- key_count: 7
  name: Public Api V6 Commission Payroll Purchase Event Example
  slug: public-api-v6-commission-payroll-purchase-event-example
- key_count: 3
  name: Public Api V6 Complete Checkout Shopping Cart Using Alternative Payments Request Example
  slug: public-api-v6-complete-checkout-shopping-cart-using-alternative-payments-request-example
- key_count: 4
  name: Public Api V6 Contact Log Comment Example
  slug: public-api-v6-contact-log-comment-example
- key_count: 11
  name: Public Api V6 Contact Log Example
  slug: public-api-v6-contact-log-example
- key_count: 2
  name: Public Api V6 Contact Log Sub Type Example
  slug: public-api-v6-contact-log-sub-type-example
- key_count: 3
  name: Public Api V6 Contact Log Type Example
  slug: public-api-v6-contact-log-type-example
- key_count: 38
  name: Public Api V6 Contract Example
  slug: public-api-v6-contract-example
- key_count: 7
  name: Public Api V6 Contract Item Example
  slug: public-api-v6-contract-item-example
- key_count: 6
  name: Public Api V6 Copy Credit Card Request Example
  slug: public-api-v6-copy-credit-card-request-example
- key_count: 5
  name: Public Api V6 Copy Credit Card Response Client Example
  slug: public-api-v6-copy-credit-card-response-client-example
- key_count: 2
  name: Public Api V6 Copy Credit Card Response Example
  slug: public-api-v6-copy-credit-card-response-example
- key_count: 10
  name: Public Api V6 Course Example
  slug: public-api-v6-course-example
- key_count: 2
  name: Public Api V6 Create Reservation Response Example
  slug: public-api-v6-create-reservation-response-example
- key_count: 11
  name: Public Api V6 Credit Card Info Example
  slug: public-api-v6-credit-card-info-example
- key_count: 4
  name: Public Api V6 Cross Regional Client Association Example
  slug: public-api-v6-cross-regional-client-association-example
- key_count: 3
  name: Public Api V6 Custom Client Field Example
  slug: public-api-v6-custom-client-field-example
- key_count: 4
  name: Public Api V6 Custom Client Field Value Example
  slug: public-api-v6-custom-client-field-value-example
- key_count: 2
  name: Public Api V6 Custom Payment Method Example
  slug: public-api-v6-custom-payment-method-example
- key_count: 1
  name: Public Api V6 Deactivate Promo Code Request Example
  slug: public-api-v6-deactivate-promo-code-request-example
- key_count: 4
  name: Public Api V6 Direct Debit Info Example
  slug: public-api-v6-direct-debit-info-example
- key_count: 2
  name: Public Api V6 Discount Example
  slug: public-api-v6-discount-example
- key_count: 10
  name: Public Api V6 Formula Note Response Example
  slug: public-api-v6-formula-note-response-example
- key_count: 4
  name: Public Api V6 Gender Option Example
  slug: public-api-v6-gender-option-example
- key_count: 2
  name: Public Api V6 Get Activation Code Response Example
  slug: public-api-v6-get-activation-code-response-example
- key_count: 2
  name: Public Api V6 Get Active Client Memberships Response Example
  slug: public-api-v6-get-active-client-memberships-response-example
- key_count: 2
  name: Public Api V6 Get Active Clients Memberships Response Example
  slug: public-api-v6-get-active-clients-memberships-response-example
- key_count: 2
  name: Public Api V6 Get Active Session Times Response Example
  slug: public-api-v6-get-active-session-times-response-example
- key_count: 2
  name: Public Api V6 Get Add Ons Response Example
  slug: public-api-v6-get-add-ons-response-example
- key_count: 1
  name: Public Api V6 Get Alternative Payment Methods Response Example
  slug: public-api-v6-get-alternative-payment-methods-response-example
- key_count: 1
  name: Public Api V6 Get Appointment Options Response Example
  slug: public-api-v6-get-appointment-options-response-example
- key_count: 1
  name: Public Api V6 Get Available Dates Response Example
  slug: public-api-v6-get-available-dates-response-example
- key_count: 2
  name: Public Api V6 Get Bookable Items Response Example
  slug: public-api-v6-get-bookable-items-response-example
- key_count: 2
  name: Public Api V6 Get Categories Response Example
  slug: public-api-v6-get-categories-response-example
- key_count: 2
  name: Public Api V6 Get Class Descriptions Response Example
  slug: public-api-v6-get-class-descriptions-response-example
- key_count: 2
  name: Public Api V6 Get Class Schedules Response Example
  slug: public-api-v6-get-class-schedules-response-example
- key_count: 1
  name: Public Api V6 Get Class Visits Response Example
  slug: public-api-v6-get-class-visits-response-example
- key_count: 2
  name: Public Api V6 Get Classes Response Example
  slug: public-api-v6-get-classes-response-example
- key_count: 2
  name: Public Api V6 Get Client Account Balances Response Example
  slug: public-api-v6-get-client-account-balances-response-example
- key_count: 5
  name: Public Api V6 Get Client Complete Info Response Example
  slug: public-api-v6-get-client-complete-info-response-example
- key_count: 2
  name: Public Api V6 Get Client Contracts Response Example
  slug: public-api-v6-get-client-contracts-response-example
- key_count: 2
  name: Public Api V6 Get Client Duplicates Response Example
  slug: public-api-v6-get-client-duplicates-response-example
- key_count: 2
  name: Public Api V6 Get Client Formula Notes Response Example
  slug: public-api-v6-get-client-formula-notes-response-example
- key_count: 1
  name: Public Api V6 Get Client Indexes Response Example
  slug: public-api-v6-get-client-indexes-response-example
- key_count: 2
  name: Public Api V6 Get Client Purchases Response Example
  slug: public-api-v6-get-client-purchases-response-example
- key_count: 1
  name: Public Api V6 Get Client Referral Types Response Example
  slug: public-api-v6-get-client-referral-types-response-example
- key_count: 3
  name: Public Api V6 Get Client Rewards Response Example
  slug: public-api-v6-get-client-rewards-response-example
- key_count: 2
  name: Public Api V6 Get Client Schedule Response Example
  slug: public-api-v6-get-client-schedule-response-example
- key_count: 2
  name: Public Api V6 Get Client Services Response Example
  slug: public-api-v6-get-client-services-response-example
- key_count: 2
  name: Public Api V6 Get Client Visits Response Example
  slug: public-api-v6-get-client-visits-response-example
- key_count: 2
  name: Public Api V6 Get Clients Response Example
  slug: public-api-v6-get-clients-response-example
- key_count: 2
  name: Public Api V6 Get Commissions Response Example
  slug: public-api-v6-get-commissions-response-example
- key_count: 2
  name: Public Api V6 Get Contact Log Types Response Example
  slug: public-api-v6-get-contact-log-types-response-example
- key_count: 2
  name: Public Api V6 Get Contact Logs Response Example
  slug: public-api-v6-get-contact-logs-response-example
- key_count: 2
  name: Public Api V6 Get Contracts Response Example
  slug: public-api-v6-get-contracts-response-example
- key_count: 2
  name: Public Api V6 Get Courses Reponse Example
  slug: public-api-v6-get-courses-reponse-example
- key_count: 2
  name: Public Api V6 Get Cross Regional Client Associations Response Example
  slug: public-api-v6-get-cross-regional-client-associations-response-example
- key_count: 2
  name: Public Api V6 Get Custom Client Fields Response Example
  slug: public-api-v6-get-custom-client-fields-response-example
- key_count: 2
  name: Public Api V6 Get Custom Payment Methods Response Example
  slug: public-api-v6-get-custom-payment-methods-response-example
- key_count: 2
  name: Public Api V6 Get Enrollments Response Example
  slug: public-api-v6-get-enrollments-response-example
- key_count: 1
  name: Public Api V6 Get Genders Response Example
  slug: public-api-v6-get-genders-response-example
- key_count: 2
  name: Public Api V6 Get Gift Card Balance Response Example
  slug: public-api-v6-get-gift-card-balance-response-example
- key_count: 2
  name: Public Api V6 Get Gift Card Response Example
  slug: public-api-v6-get-gift-card-response-example
- key_count: 1
  name: Public Api V6 Get Liability Waiver Response Example
  slug: public-api-v6-get-liability-waiver-response-example
- key_count: 2
  name: Public Api V6 Get Locations Response Example
  slug: public-api-v6-get-locations-response-example
- key_count: 1
  name: Public Api V6 Get Memberships Response Example
  slug: public-api-v6-get-memberships-response-example
- key_count: 1
  name: Public Api V6 Get Mobile Providers Response Example
  slug: public-api-v6-get-mobile-providers-response-example
- key_count: 2
  name: Public Api V6 Get Packages Response Example
  slug: public-api-v6-get-packages-response-example
- key_count: 1
  name: Public Api V6 Get Payment Types Response Example
  slug: public-api-v6-get-payment-types-response-example
- key_count: 3
  name: Public Api V6 Get Pick Aspot Class Response Example
  slug: public-api-v6-get-pick-aspot-class-response-example
- key_count: 2
  name: Public Api V6 Get Products Inventory Response Example
  slug: public-api-v6-get-products-inventory-response-example
- key_count: 2
  name: Public Api V6 Get Products Response Example
  slug: public-api-v6-get-products-response-example
- key_count: 2
  name: Public Api V6 Get Programs Response Example
  slug: public-api-v6-get-programs-response-example
- key_count: 2
  name: Public Api V6 Get Promo Codes Response Example
  slug: public-api-v6-get-promo-codes-response-example
- key_count: 1
  name: Public Api V6 Get Prospect Stages Response Example
  slug: public-api-v6-get-prospect-stages-response-example
- key_count: 2
  name: Public Api V6 Get Relationships Response Example
  slug: public-api-v6-get-relationships-response-example
- key_count: 1
  name: Public Api V6 Get Required Client Fields Response Example
  slug: public-api-v6-get-required-client-fields-response-example
- key_count: 3
  name: Public Api V6 Get Reservation Response Example
  slug: public-api-v6-get-reservation-response-example
- key_count: 2
  name: Public Api V6 Get Resource Availabilities Response Example
  slug: public-api-v6-get-resource-availabilities-response-example
- key_count: 2
  name: Public Api V6 Get Sales Reps Response Example
  slug: public-api-v6-get-sales-reps-response-example
- key_count: 2
  name: Public Api V6 Get Sales Response Example
  slug: public-api-v6-get-sales-response-example
- key_count: 2
  name: Public Api V6 Get Schedule Items Response Example
  slug: public-api-v6-get-schedule-items-response-example
- key_count: 2
  name: Public Api V6 Get Scheduled Service Earnings Response Example
  slug: public-api-v6-get-scheduled-service-earnings-response-example
- key_count: 2
  name: Public Api V6 Get Semesters Response Example
  slug: public-api-v6-get-semesters-response-example
- key_count: 2
  name: Public Api V6 Get Services Response Example
  slug: public-api-v6-get-services-response-example
- key_count: 2
  name: Public Api V6 Get Session Types Response Example
  slug: public-api-v6-get-session-types-response-example
- key_count: 2
  name: Public Api V6 Get Sites Response Example
  slug: public-api-v6-get-sites-response-example
- key_count: 2
  name: Public Api V6 Get Staff Appointments Response Example
  slug: public-api-v6-get-staff-appointments-response-example
- key_count: 2
  name: Public Api V6 Get Staff Image Urlresponse Example
  slug: public-api-v6-get-staff-image-urlresponse-example
- key_count: 1
  name: Public Api V6 Get Staff Permissions Response Example
  slug: public-api-v6-get-staff-permissions-response-example
- key_count: 2
  name: Public Api V6 Get Staff Response Example
  slug: public-api-v6-get-staff-response-example
- key_count: 2
  name: Public Api V6 Get Staff Session Types Response Example
  slug: public-api-v6-get-staff-session-types-response-example
- key_count: 2
  name: Public Api V6 Get Time Cards Response Example
  slug: public-api-v6-get-time-cards-response-example
- key_count: 2
  name: Public Api V6 Get Tips Response Example
  slug: public-api-v6-get-tips-response-example
- key_count: 2
  name: Public Api V6 Get Transactions Response Example
  slug: public-api-v6-get-transactions-response-example
- key_count: 2
  name: Public Api V6 Get Unavailabilities Response Example
  slug: public-api-v6-get-unavailabilities-response-example
- key_count: 2
  name: Public Api V6 Get Waitlist Entries Response Example
  slug: public-api-v6-get-waitlist-entries-response-example
- key_count: 12
  name: Public Api V6 Gift Card Example
  slug: public-api-v6-gift-card-example
- key_count: 3
  name: Public Api V6 Gift Card Layout Example
  slug: public-api-v6-gift-card-layout-example
- key_count: 1
  name: Public Api V6 Http Content Example
  slug: public-api-v6-http-content-example
- key_count: 15
  name: Public Api V6 Initiate Checkout Shopping Cart Using Alternative Payments Request Example
  slug: public-api-v6-initiate-checkout-shopping-cart-using-alternative-payments-request-example
- key_count: 10
  name: Public Api V6 Initiate Purchase Contract Request Example
  slug: public-api-v6-initiate-purchase-contract-request-example
- key_count: 2
  name: Public Api V6 Issue Request Example
  slug: public-api-v6-issue-request-example
- key_count: 4
  name: Public Api V6 Issue Response Example
  slug: public-api-v6-issue-response-example
- key_count: 5
  name: Public Api V6 Lead Channel Example
  slug: public-api-v6-lead-channel-example
- key_count: 3
  name: Public Api V6 Level Example
  slug: public-api-v6-level-example
- key_count: 3
  name: Public Api V6 Liability Example
  slug: public-api-v6-liability-example
- key_count: 25
  name: Public Api V6 Location Example
  slug: public-api-v6-location-example
- key_count: 56
  name: Public Api V6 Location1 Example
  slug: public-api-v6-location1-example
- key_count: 2
  name: Public Api V6 M0 Culture Neutral Public Key Token B77A5C561934E089 Example
  slug: public-api-v6-m0-culture-neutral-public-key-token-b77a5c561934e089-example
- key_count: 14
  name: Public Api V6 Membership Example
  slug: public-api-v6-membership-example
- key_count: 2
  name: Public Api V6 Membership Type Restriction Example
  slug: public-api-v6-membership-type-restriction-example
- key_count: 2
  name: Public Api V6 Merge Clients Request Example
  slug: public-api-v6-merge-clients-request-example
- key_count: 4
  name: Public Api V6 Mobile Provider Example
  slug: public-api-v6-mobile-provider-example
- key_count: 6
  name: Public Api V6 Package Example
  slug: public-api-v6-package-example
- key_count: 4
  name: Public Api V6 Pagination Example
  slug: public-api-v6-pagination-example
- key_count: 4
  name: Public Api V6 Pagination Response Example
  slug: public-api-v6-pagination-response-example
- key_count: 3
  name: Public Api V6 Payment Processing Failure Example
  slug: public-api-v6-payment-processing-failure-example
- key_count: 4
  name: Public Api V6 Payment Type Example
  slug: public-api-v6-payment-type-example
- key_count: 11
  name: Public Api V6 Pick Aspot Class Example
  slug: public-api-v6-pick-aspot-class-example
- key_count: 2
  name: Public Api V6 Pricing Relationships Example
  slug: public-api-v6-pricing-relationships-example
- key_count: 20
  name: Public Api V6 Product Example
  slug: public-api-v6-product-example
- key_count: 10
  name: Public Api V6 Products Inventory Example
  slug: public-api-v6-products-inventory-example
- key_count: 6
  name: Public Api V6 Program Example
  slug: public-api-v6-program-example
- key_count: 2
  name: Public Api V6 Program Membership Example
  slug: public-api-v6-program-membership-example
- key_count: 9
  name: Public Api V6 Program1 Example
  slug: public-api-v6-program1-example
- key_count: 14
  name: Public Api V6 Promo Code Example
  slug: public-api-v6-promo-code-example
- key_count: 3
  name: Public Api V6 Prospect Stage Example
  slug: public-api-v6-prospect-stage-example
- key_count: 8
  name: Public Api V6 Purchase Account Credit Request Example
  slug: public-api-v6-purchase-account-credit-request-example
- key_count: 5
  name: Public Api V6 Purchase Account Credit Response Example
  slug: public-api-v6-purchase-account-credit-response-example
- key_count: 19
  name: Public Api V6 Purchase Contract Request Example
  slug: public-api-v6-purchase-contract-request-example
- key_count: 7
  name: Public Api V6 Purchase Contract Response Example
  slug: public-api-v6-purchase-contract-response-example
- key_count: 4
  name: Public Api V6 Purchase Contract Response Totals Example
  slug: public-api-v6-purchase-contract-response-totals-example
- key_count: 17
  name: Public Api V6 Purchase Gift Card Request Example
  slug: public-api-v6-purchase-gift-card-request-example
- key_count: 11
  name: Public Api V6 Purchase Gift Card Response Example
  slug: public-api-v6-purchase-gift-card-response-example
- key_count: 25
  name: Public Api V6 Purchased Item Example
  slug: public-api-v6-purchased-item-example
- key_count: 3
  name: Public Api V6 Relationship Example
  slug: public-api-v6-relationship-example
- key_count: 7
  name: Public Api V6 Remove Client From Class Request Example
  slug: public-api-v6-remove-client-from-class-request-example
- key_count: 1
  name: Public Api V6 Remove Client From Class Response Example
  slug: public-api-v6-remove-client-from-class-response-example
- key_count: 6
  name: Public Api V6 Remove Clients From Classes Request Example
  slug: public-api-v6-remove-clients-from-classes-request-example
- key_count: 3
  name: Public Api V6 Remove Clients From Classes Response Example
  slug: public-api-v6-remove-clients-from-classes-response-example
- key_count: 9
  name: Public Api V6 Reservation Example
  slug: public-api-v6-reservation-example
- key_count: 3
  name: Public Api V6 Resource Availability Example
  slug: public-api-v6-resource-availability-example
- key_count: 5
  name: Public Api V6 Resource Availability1 Example
  slug: public-api-v6-resource-availability1-example
- key_count: 2
  name: Public Api V6 Resource Example
  slug: public-api-v6-resource-example
- key_count: 2
  name: Public Api V6 Resource Slim Example
  slug: public-api-v6-resource-slim-example
- key_count: 3
  name: Public Api V6 Response Details Example
  slug: public-api-v6-response-details-example
- key_count: 2
  name: Public Api V6 Return Sale Request Example
  slug: public-api-v6-return-sale-request-example
- key_count: 3
  name: Public Api V6 Return Sale Response Example
  slug: public-api-v6-return-sale-response-example
- key_count: 11
  name: Public Api V6 Sale Example
  slug: public-api-v6-sale-example
- key_count: 6
  name: Public Api V6 Sale Payment Example
  slug: public-api-v6-sale-payment-example
- key_count: 5
  name: Public Api V6 Sales Rep Example
  slug: public-api-v6-sales-rep-example
- key_count: 4
  name: Public Api V6 Sales Rep Response Example
  slug: public-api-v6-sales-rep-response-example
- key_count: 5
  name: Public Api V6 Scheduled Service Earnings Event Example
  slug: public-api-v6-scheduled-service-earnings-event-example
- key_count: 8
  name: Public Api V6 Semester Example
  slug: public-api-v6-semester-example
- key_count: 2
  name: Public Api V6 Send Auto Email Request Example
  slug: public-api-v6-send-auto-email-request-example
- key_count: 3
  name: Public Api V6 Send Password Reset Email Request Example
  slug: public-api-v6-send-password-reset-email-request-example
- key_count: 27
  name: Public Api V6 Service Example
  slug: public-api-v6-service-example
- key_count: 2
  name: Public Api V6 Service Tag Example
  slug: public-api-v6-service-tag-example
- key_count: 13
  name: Public Api V6 Session Type Example
  slug: public-api-v6-session-type-example
- key_count: 14
  name: Public Api V6 Session Type1 Example
  slug: public-api-v6-session-type1-example
- key_count: 8
  name: Public Api V6 Shopping Cart Example
  slug: public-api-v6-shopping-cart-example
- key_count: 23
  name: Public Api V6 Site Example
  slug: public-api-v6-site-example
- key_count: 2
  name: Public Api V6 Size Example
  slug: public-api-v6-size-example
- key_count: 3
  name: Public Api V6 Spot Example
  slug: public-api-v6-spot-example
- key_count: 38
  name: Public Api V6 Staff Example
  slug: public-api-v6-staff-example
- key_count: 4
  name: Public Api V6 Staff Permission Group Example
  slug: public-api-v6-staff-permission-group-example
- key_count: 15
  name: Public Api V6 Staff Session Type Example
  slug: public-api-v6-staff-session-type-example
- key_count: 2
  name: Public Api V6 Staff Setting Example
  slug: public-api-v6-staff-setting-example
- key_count: 45
  name: Public Api V6 Staff1 Example
  slug: public-api-v6-staff1-example
- key_count: 1
  name: Public Api V6 Stored Card Info Example
  slug: public-api-v6-stored-card-info-example
- key_count: 3
  name: Public Api V6 Sub Category Example
  slug: public-api-v6-sub-category-example
- key_count: 6
  name: Public Api V6 Substitute Class Teacher Request Example
  slug: public-api-v6-substitute-class-teacher-request-example
- key_count: 1
  name: Public Api V6 Substitute Class Teacher Response Example
  slug: public-api-v6-substitute-class-teacher-response-example
- key_count: 21
  name: Public Api V6 Substitute Teacher Class Example
  slug: public-api-v6-substitute-teacher-class-example
- key_count: 9
  name: Public Api V6 Suspend Contract Request Example
  slug: public-api-v6-suspend-contract-request-example
- key_count: 1
  name: Public Api V6 Suspend Contract Response Example
  slug: public-api-v6-suspend-contract-response-example
- key_count: 5
  name: Public Api V6 Terminate Contract Request Example
  slug: public-api-v6-terminate-contract-request-example
- key_count: 1
  name: Public Api V6 Terminate Contract Response Example
  slug: public-api-v6-terminate-contract-response-example
- key_count: 7
  name: Public Api V6 Time Card Event Example
  slug: public-api-v6-time-card-event-example
- key_count: 4
  name: Public Api V6 Tip Example
  slug: public-api-v6-tip-example
- key_count: 17
  name: Public Api V6 Transaction Example
  slug: public-api-v6-transaction-example
- key_count: 2
  name: Public Api V6 Transaction Response Example
  slug: public-api-v6-transaction-response-example
- key_count: 4
  name: Public Api V6 Unavailability Example
  slug: public-api-v6-unavailability-example
- key_count: 5
  name: Public Api V6 Unavailability Plain Example
  slug: public-api-v6-unavailability-plain-example
- key_count: 4
  name: Public Api V6 Unavailability1 Example
  slug: public-api-v6-unavailability1-example
- key_count: 7
  name: Public Api V6 Upcoming Autopay Event Example
  slug: public-api-v6-upcoming-autopay-event-example
- key_count: 14
  name: Public Api V6 Update Appointment Request Example
  slug: public-api-v6-update-appointment-request-example
- key_count: 1
  name: Public Api V6 Update Appointment Response Example
  slug: public-api-v6-update-appointment-response-example
- key_count: 9
  name: Public Api V6 Update Availability Request Example
  slug: public-api-v6-update-availability-request-example
- key_count: 2
  name: Public Api V6 Update Availability Response Example
  slug: public-api-v6-update-availability-response-example
- key_count: 24
  name: Public Api V6 Update Class Enrollment Schedule Request Example
  slug: public-api-v6-update-class-enrollment-schedule-request-example
- key_count: 1
  name: Public Api V6 Update Class Schedule Notes Request Example
  slug: public-api-v6-update-class-schedule-notes-request-example
- key_count: 7
  name: Public Api V6 Update Client Contract Autopays Request Example
  slug: public-api-v6-update-client-contract-autopays-request-example
- key_count: 5
  name: Public Api V6 Update Client Request Example
  slug: public-api-v6-update-client-request-example
- key_count: 1
  name: Public Api V6 Update Client Response Example
  slug: public-api-v6-update-client-response-example
- key_count: 6
  name: Public Api V6 Update Client Rewards Request Example
  slug: public-api-v6-update-client-rewards-request-example
- key_count: 5
  name: Public Api V6 Update Client Service Request Example
  slug: public-api-v6-update-client-service-request-example
- key_count: 1
  name: Public Api V6 Update Client Service Response Example
  slug: public-api-v6-update-client-service-response-example
- key_count: 7
  name: Public Api V6 Update Client Visit Request Example
  slug: public-api-v6-update-client-visit-request-example
- key_count: 1
  name: Public Api V6 Update Client Visit Response Example
  slug: public-api-v6-update-client-visit-response-example
- key_count: 2
  name: Public Api V6 Update Contact Log Comment Example
  slug: public-api-v6-update-contact-log-comment-example
- key_count: 10
  name: Public Api V6 Update Contact Log Request Example
  slug: public-api-v6-update-contact-log-request-example
- key_count: 2
  name: Public Api V6 Update Contact Log Type Example
  slug: public-api-v6-update-contact-log-type-example
- key_count: 3
  name: Public Api V6 Update Product Price Request Example
  slug: public-api-v6-update-product-price-request-example
- key_count: 1
  name: Public Api V6 Update Product Price Response Example
  slug: public-api-v6-update-product-price-response-example
- key_count: 2
  name: Public Api V6 Update Reservation Response Example
  slug: public-api-v6-update-reservation-response-example
- key_count: 2
  name: Public Api V6 Update Sale Date Request Example
  slug: public-api-v6-update-sale-date-request-example
- key_count: 1
  name: Public Api V6 Update Sale Date Response Example
  slug: public-api-v6-update-sale-date-response-example
- key_count: 1
  name: Public Api V6 Update Service Response Example
  slug: public-api-v6-update-service-response-example
- key_count: 10
  name: Public Api V6 Update Site Client Index Request Example
  slug: public-api-v6-update-site-client-index-request-example
- key_count: 10
  name: Public Api V6 Update Site Client Index Response Example
  slug: public-api-v6-update-site-client-index-response-example
- key_count: 2
  name: Public Api V6 Update Staff Permissions Request Example
  slug: public-api-v6-update-staff-permissions-request-example
- key_count: 1
  name: Public Api V6 Update Staff Permissions Response Example
  slug: public-api-v6-update-staff-permissions-response-example
- key_count: 28
  name: Public Api V6 Update Staff Request Example
  slug: public-api-v6-update-staff-request-example
- key_count: 1
  name: Public Api V6 Update Staff Response Example
  slug: public-api-v6-update-staff-response-example
- key_count: 2
  name: Public Api V6 Upload Client Document Request Example
  slug: public-api-v6-upload-client-document-request-example
- key_count: 2
  name: Public Api V6 Upload Client Document Response Example
  slug: public-api-v6-upload-client-document-response-example
- key_count: 2
  name: Public Api V6 Upload Client Photo Request Example
  slug: public-api-v6-upload-client-photo-request-example
- key_count: 2
  name: Public Api V6 Upload Client Photo Response Example
  slug: public-api-v6-upload-client-photo-response-example
- key_count: 4
  name: Public Api V6 User Example
  slug: public-api-v6-user-example
- key_count: 28
  name: Public Api V6 Visit Example
  slug: public-api-v6-visit-example
- key_count: 2
  name: Public Api V6 Visit Waitlist Info Example
  slug: public-api-v6-visit-waitlist-info-example
- key_count: 29
  name: Public Api V6 Visit With Waitlist Info Example
  slug: public-api-v6-visit-with-waitlist-info-example
- key_count: 9
  name: Public Api V6 Waitlist Entry Example
  slug: public-api-v6-waitlist-entry-example
- key_count: 2
  name: Public Api V6 Written Class Schedules Info Example
  slug: public-api-v6-written-class-schedules-info-example
- key_count: 4
  name: Webhooks Api Create Subscription Request Example
  slug: webhooks-api-create-subscription-request-example
- key_count: 11
  name: Webhooks Api Create Subscription Response Example
  slug: webhooks-api-create-subscription-response-example
- key_count: 4
  name: Webhooks Api Deactivate Subscription Response Example
  slug: webhooks-api-deactivate-subscription-response-example
- key_count: 1
  name: Webhooks Api Get Metrics Response Example
  slug: webhooks-api-get-metrics-response-example
- key_count: 1
  name: Webhooks Api Get Subscriptions Response Example
  slug: webhooks-api-get-subscriptions-response-example
- key_count: 8
  name: Webhooks Api Metric Example
  slug: webhooks-api-metric-example
- key_count: 5
  name: Webhooks Api Patch Subscription Request Example
  slug: webhooks-api-patch-subscription-request-example
- key_count: 3
  name: Webhooks Api Push Api Error Example
  slug: webhooks-api-push-api-error-example
- key_count: 3
  name: Webhooks Api Push Api Result Create Subscription Response Example
  slug: webhooks-api-push-api-result-create-subscription-response-example
- key_count: 3
  name: Webhooks Api Push Api Result Deactivate Subscription Response Example
  slug: webhooks-api-push-api-result-deactivate-subscription-response-example
- key_count: 3
  name: Webhooks Api Push Api Result Get Subscriptions Response Example
  slug: webhooks-api-push-api-result-get-subscriptions-response-example
- key_count: 3
  name: Webhooks Api Push Api Result Subscription Example
  slug: webhooks-api-push-api-result-subscription-example
- key_count: 10
  name: Webhooks Api Subscription Example
  slug: webhooks-api-subscription-example
features:
- description: Online booking widgets, class schedules, appointments, enrollments, and Pick-a-Spot reservations.
  name: Booking and Scheduling
- description: In-studio POS for products, services, contracts, gift cards, custom payment methods, refunds, and returns.
  name: Point of Sale
- description: Client profiles, contracts, services, contact logs, formula notes, custom fields, and red/yellow alerts.
  name: Client Management
- description: Staff schedules, permissions, availability, class pay, commissions, and time-clock reporting.
  name: Staff and Payroll
- description: HMAC-signed, near real-time delivery of site, location, appointment, class, client, sale, and staff events.
  name: Webhooks
- description: OpenID Connect via signin.mindbodyonline.com with the Mindbody.Api.Public.v6 scope for delegated calls.
  name: Identity and OAuth
- description: Discover which Mindbody businesses a client is associated with across the network.
  name: Cross-Site Lookup
- description: Mindbody consumer app marketplace exposes participating studios to nearby members.
  name: Marketplace Listing
finops:
- name: Mindbody Finops
  service_category: Business Management SaaS
  slug: mindbody-finops
graphqls:
- description: This conceptual GraphQL schema represents the Mindbody Public API v6 domain model for fitness, wellness, and beauty business management. Mindbody exposes a REST API at `https://api.mindbodyonline.com`
  name: Mindbody GraphQL Schema
  slug: mindbody-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindbody.png
integrations:
- description: OpenID Connect provider at signin.mindbodyonline.com powering OAuth 2.0 flows for the Public API.
  name: Mindbody Identity Service
- description: Consumer app surface exposing participating studios for nearby discovery and booking.
  name: Mindbody Marketplace
- description: Mindbody-vetted directory of integrations at partnerstore.mindbodyonline.com.
  name: Partner Store
- description: Aggregator marketplace integrating with Mindbody for class supply.
  name: ClassPass
- description: Integrated card processing and custom payment methods routed through the Sale endpoints.
  name: Payment Processors
json_schemas:
- name: ActionEnum
  property_count: 0
  slug: public-api-v6-action-enum
- name: Action1Enum
  property_count: 0
  slug: public-api-v6-action1-enum
- name: Action11Enum
  property_count: 0
  slug: public-api-v6-action11-enum
- name: Action8Enum
  property_count: 0
  slug: public-api-v6-action8-enum
- name: ActivationTypeEnum
  property_count: 0
  slug: public-api-v6-activation-type-enum
- name: AddAppointmentAddOnRequest
  property_count: 5
  slug: public-api-v6-add-appointment-add-on-request
- name: AddAppointmentAddOnResponse
  property_count: 2
  slug: public-api-v6-add-appointment-add-on-response
- name: AddAppointmentOutcome
  property_count: 3
  slug: public-api-v6-add-appointment-outcome
- name: AddAppointmentRequest
  property_count: 19
  slug: public-api-v6-add-appointment-request
- name: AddAppointmentResponse
  property_count: 1
  slug: public-api-v6-add-appointment-response
- name: AddArrivalRequest
  property_count: 5
  slug: public-api-v6-add-arrival-request
- name: AddArrivalResponse
  property_count: 2
  slug: public-api-v6-add-arrival-response
- name: AddAvailabilitiesRequest
  property_count: 10
  slug: public-api-v6-add-availabilities-request
- name: AddAvailabilitiesResponse
  property_count: 2
  slug: public-api-v6-add-availabilities-response
- name: AddClassEnrollmentScheduleRequest
  property_count: 24
  slug: public-api-v6-add-class-enrollment-schedule-request
- name: AddClientDirectDebitInfoRequest
  property_count: 6
  slug: public-api-v6-add-client-direct-debit-info-request
- name: AddClientDirectDebitInfoResponse
  property_count: 5
  slug: public-api-v6-add-client-direct-debit-info-response
- name: AddClientRequest
  property_count: 60
  slug: public-api-v6-add-client-request
- name: AddClientResponse
  property_count: 1
  slug: public-api-v6-add-client-response
- name: AddClientToClassRequest
  property_count: 11
  slug: public-api-v6-add-client-to-class-request
- name: AddClientToClassResponse
  property_count: 1
  slug: public-api-v6-add-client-to-class-response
- name: AddClientToClassVisit
  property_count: 23
  slug: public-api-v6-add-client-to-class-visit
- name: AddClientToEnrollmentRequest
  property_count: 8
  slug: public-api-v6-add-client-to-enrollment-request
- name: AddContactLogRequest
  property_count: 10
  slug: public-api-v6-add-contact-log-request
- name: AddContactLogType
  property_count: 2
  slug: public-api-v6-add-contact-log-type
- name: AddFormulaNoteRequest
  property_count: 3
  slug: public-api-v6-add-formula-note-request
- name: AddMultipleAppointmentsRequest
  property_count: 1
  slug: public-api-v6-add-multiple-appointments-request
- name: AddMultipleAppointmentsResponse
  property_count: 1
  slug: public-api-v6-add-multiple-appointments-response
- name: AddOnSmall
  property_count: 4
  slug: public-api-v6-add-on-small
- name: AddOnSmall1
  property_count: 4
  slug: public-api-v6-add-on-small1
- name: AddPromoCodeRequest
  property_count: 11
  slug: public-api-v6-add-promo-code-request
- name: AddPromoCodeResponse
  property_count: 1
  slug: public-api-v6-add-promo-code-response
- name: AddSiteClientIndexRequest
  property_count: 9
  slug: public-api-v6-add-site-client-index-request
- name: AddSiteClientIndexResponse
  property_count: 10
  slug: public-api-v6-add-site-client-index-response
- name: AddStaffAvailabilityRequest
  property_count: 11
  slug: public-api-v6-add-staff-availability-request
- name: AddStaffRequest
  property_count: 26
  slug: public-api-v6-add-staff-request
- name: AddStaffResponse
  property_count: 1
  slug: public-api-v6-add-staff-response
- name: AllowedPermissionEnum
  property_count: 0
  slug: public-api-v6-allowed-permission-enum
- name: AlternativePaymentMethod
  property_count: 2
  slug: public-api-v6-alternative-payment-method
- name: Amenity
  property_count: 2
  slug: public-api-v6-amenity
- name: Amenity1
  property_count: 2
  slug: public-api-v6-amenity1
- name: ApiError1
  property_count: 2
  slug: public-api-v6-api-error1
- name: ApplicableItem
  property_count: 3
  slug: public-api-v6-applicable-item
- name: AppointmentAddOn
  property_count: 5
  slug: public-api-v6-appointment-add-on
- name: AppointmentGenderPreferenceEnum
  property_count: 0
  slug: public-api-v6-appointment-gender-preference-enum
- name: AppointmentGenderPreference1Enum
  property_count: 0
  slug: public-api-v6-appointment-gender-preference1-enum
- name: AppointmentOption
  property_count: 4
  slug: public-api-v6-appointment-option
- name: Appointment
  property_count: 23
  slug: public-api-v6-appointment
- name: AppointmentStaff
  property_count: 4
  slug: public-api-v6-appointment-staff
- name: AppointmentStatusEnum
  property_count: 0
  slug: public-api-v6-appointment-status-enum
- name: Appointment1
  property_count: 22
  slug: public-api-v6-appointment1
- name: AssignStaffSessionTypeRequest
  property_count: 8
  slug: public-api-v6-assign-staff-session-type-request
- name: AssignStaffSessionTypeResponse
  property_count: 8
  slug: public-api-v6-assign-staff-session-type-response
- name: AssignedClientIndex
  property_count: 2
  slug: public-api-v6-assigned-client-index
- name: AutopaySchedule
  property_count: 3
  slug: public-api-v6-autopay-schedule
- name: AutopayStatusEnum
  property_count: 0
  slug: public-api-v6-autopay-status-enum
- name: Availability
  property_count: 13
  slug: public-api-v6-availability
- name: Availability1
  property_count: 13
  slug: public-api-v6-availability1
- name: BookingStatusEnum
  property_count: 0
  slug: public-api-v6-booking-status-enum
- name: BookingWindow
  property_count: 4
  slug: public-api-v6-booking-window
- name: CancelSingleClassRequest
  property_count: 4
  slug: public-api-v6-cancel-single-class-request
- name: CancelSingleClassResponse
  property_count: 1
  slug: public-api-v6-cancel-single-class-response
- name: CartItem
  property_count: 8
  slug: public-api-v6-cart-item
- name: Category
  property_count: 11
  slug: public-api-v6-category
- name: CheckoutAlternativePaymentInfo
  property_count: 2
  slug: public-api-v6-checkout-alternative-payment-info
- name: CheckoutAppointmentBookingRequest
  property_count: 7
  slug: public-api-v6-checkout-appointment-booking-request
- name: CheckoutItem
  property_count: 2
  slug: public-api-v6-checkout-item
- name: CheckoutItemWrapper
  property_count: 11
  slug: public-api-v6-checkout-item-wrapper
- name: CheckoutPaymentInfo
  property_count: 2
  slug: public-api-v6-checkout-payment-info
- name: CheckoutShoppingCartRequest
  property_count: 20
  slug: public-api-v6-checkout-shopping-cart-request
- name: CheckoutShoppingCartResponse
  property_count: 4
  slug: public-api-v6-checkout-shopping-cart-response
- name: ClassClientDetail
  property_count: 2
  slug: public-api-v6-class-client-detail
- name: ClassDescription
  property_count: 15
  slug: public-api-v6-class-description
- name: ClassSchedule
  property_count: 24
  slug: public-api-v6-class-schedule
- name: Class
  property_count: 30
  slug: public-api-v6-class
- name: ClientArrival
  property_count: 4
  slug: public-api-v6-client-arrival
- name: ClientContract
  property_count: 23
  slug: public-api-v6-client-contract
- name: ClientCreditCard
  property_count: 10
  slug: public-api-v6-client-credit-card
- name: ClientDocument
  property_count: 3
  slug: public-api-v6-client-document
- name: ClientDuplicate
  property_count: 5
  slug: public-api-v6-client-duplicate
- name: ClientIndex
  property_count: 6
  slug: public-api-v6-client-index
- name: ClientIndexValue
  property_count: 3
  slug: public-api-v6-client-index-value
- name: ClientMembership
  property_count: 17
  slug: public-api-v6-client-membership
- name: ClientMemberships
  property_count: 3
  slug: public-api-v6-client-memberships
- name: ClientPurchaseRecord
  property_count: 9
  slug: public-api-v6-client-purchase-record
- name: ClientRelationship
  property_count: 5
  slug: public-api-v6-client-relationship
- name: ClientRewardTransaction
  property_count: 6
  slug: public-api-v6-client-reward-transaction
- name: Client
  property_count: 58
  slug: public-api-v6-client
- name: ClientService
  property_count: 14
  slug: public-api-v6-client-service
- name: ClientServiceWithActivationType
  property_count: 16
  slug: public-api-v6-client-service-with-activation-type
- name: ClientSuspensionInfo
  property_count: 3
  slug: public-api-v6-client-suspension-info
- name: ClientType
  property_count: 2
  slug: public-api-v6-client-type
- name: ClientWithSuspensionInfo
  property_count: 59
  slug: public-api-v6-client-with-suspension-info
- name: Color
  property_count: 2
  slug: public-api-v6-color
- name: CommissionDetail
  property_count: 2
  slug: public-api-v6-commission-detail
- name: CommissionPayrollPurchaseEvent
  property_count: 7
  slug: public-api-v6-commission-payroll-purchase-event
- name: CompleteCheckoutShoppingCartUsingAlternativePaymentsRequest
  property_count: 3
  slug: public-api-v6-complete-checkout-shopping-cart-using-alternative-payments-request
- name: ContactLogComment
  property_count: 4
  slug: public-api-v6-contact-log-comment
- name: ContactLog
  property_count: 11
  slug: public-api-v6-contact-log
- name: ContactLogSubType
  property_count: 2
  slug: public-api-v6-contact-log-sub-type
- name: ContactLogType
  property_count: 3
  slug: public-api-v6-contact-log-type
- name: ContentFormatEnum
  property_count: 0
  slug: public-api-v6-content-format-enum
- name: ContractItem
  property_count: 7
  slug: public-api-v6-contract-item
- name: Contract
  property_count: 38
  slug: public-api-v6-contract
- name: CopyCreditCardRequest
  property_count: 6
  slug: public-api-v6-copy-credit-card-request
- name: CopyCreditCardResponseClient
  property_count: 5
  slug: public-api-v6-copy-credit-card-response-client
- name: CopyCreditCardResponse
  property_count: 2
  slug: public-api-v6-copy-credit-card-response
- name: Course
  property_count: 10
  slug: public-api-v6-course
- name: CreateReservationResponse
  property_count: 2
  slug: public-api-v6-create-reservation-response
- name: CreditCardInfo
  property_count: 11
  slug: public-api-v6-credit-card-info
- name: CrossRegionalClientAssociation
  property_count: 4
  slug: public-api-v6-cross-regional-client-association
- name: CustomClientField
  property_count: 3
  slug: public-api-v6-custom-client-field
- name: CustomClientFieldValue
  property_count: 4
  slug: public-api-v6-custom-client-field-value
- name: CustomPaymentMethod
  property_count: 2
  slug: public-api-v6-custom-payment-method
- name: DaysOfWeekEnum
  property_count: 0
  slug: public-api-v6-days-of-week-enum
- name: DaysValidEnum
  property_count: 0
  slug: public-api-v6-days-valid-enum
- name: DeactivatePromoCodeRequest
  property_count: 1
  slug: public-api-v6-deactivate-promo-code-request
- name: DeniedPermissionEnum
  property_count: 0
  slug: public-api-v6-denied-permission-enum
- name: DirectDebitInfo
  property_count: 4
  slug: public-api-v6-direct-debit-info
- name: Discount
  property_count: 2
  slug: public-api-v6-discount
- name: FormulaNoteResponse
  property_count: 10
  slug: public-api-v6-formula-note-response
- name: FrequencyTypeEnum
  property_count: 0
  slug: public-api-v6-frequency-type-enum
- name: GenderOption
  property_count: 4
  slug: public-api-v6-gender-option
- name: GenderPreferenceEnum
  property_count: 0
  slug: public-api-v6-gender-preference-enum
- name: GetActivationCodeResponse
  property_count: 2
  slug: public-api-v6-get-activation-code-response
- name: GetActiveClientMembershipsResponse
  property_count: 2
  slug: public-api-v6-get-active-client-memberships-response
- name: GetActiveClientsMembershipsResponse
  property_count: 2
  slug: public-api-v6-get-active-clients-memberships-response
- name: GetActiveSessionTimesResponse
  property_count: 2
  slug: public-api-v6-get-active-session-times-response
- name: GetAddOnsResponse
  property_count: 2
  slug: public-api-v6-get-add-ons-response
- name: GetAlternativePaymentMethodsResponse
  property_count: 1
  slug: public-api-v6-get-alternative-payment-methods-response
- name: GetAppointmentOptionsResponse
  property_count: 1
  slug: public-api-v6-get-appointment-options-response
- name: GetAvailableDatesResponse
  property_count: 1
  slug: public-api-v6-get-available-dates-response
- name: GetBookableItemsResponse
  property_count: 2
  slug: public-api-v6-get-bookable-items-response
- name: GetCategoriesResponse
  property_count: 2
  slug: public-api-v6-get-categories-response
- name: GetClassDescriptionsResponse
  property_count: 2
  slug: public-api-v6-get-class-descriptions-response
- name: GetClassSchedulesResponse
  property_count: 2
  slug: public-api-v6-get-class-schedules-response
- name: GetClassVisitsResponse
  property_count: 1
  slug: public-api-v6-get-class-visits-response
- name: GetClassesResponse
  property_count: 2
  slug: public-api-v6-get-classes-response
- name: GetClientAccountBalancesResponse
  property_count: 2
  slug: public-api-v6-get-client-account-balances-response
- name: GetClientCompleteInfoResponse
  property_count: 5
  slug: public-api-v6-get-client-complete-info-response
- name: GetClientContractsResponse
  property_count: 2
  slug: public-api-v6-get-client-contracts-response
- name: GetClientDuplicatesResponse
  property_count: 2
  slug: public-api-v6-get-client-duplicates-response
- name: GetClientFormulaNotesResponse
  property_count: 2
  slug: public-api-v6-get-client-formula-notes-response
- name: GetClientIndexesResponse
  property_count: 1
  slug: public-api-v6-get-client-indexes-response
- name: GetClientPurchasesResponse
  property_count: 2
  slug: public-api-v6-get-client-purchases-response
- name: GetClientReferralTypesResponse
  property_count: 1
  slug: public-api-v6-get-client-referral-types-response
- name: GetClientRewardsResponse
  property_count: 3
  slug: public-api-v6-get-client-rewards-response
- name: GetClientScheduleResponse
  property_count: 2
  slug: public-api-v6-get-client-schedule-response
- name: GetClientServicesResponse
  property_count: 2
  slug: public-api-v6-get-client-services-response
- name: GetClientVisitsResponse
  property_count: 2
  slug: public-api-v6-get-client-visits-response
- name: GetClientsResponse
  property_count: 2
  slug: public-api-v6-get-clients-response
- name: GetCommissionsResponse
  property_count: 2
  slug: public-api-v6-get-commissions-response
- name: GetContactLogTypesResponse
  property_count: 2
  slug: public-api-v6-get-contact-log-types-response
- name: GetContactLogsResponse
  property_count: 2
  slug: public-api-v6-get-contact-logs-response
- name: GetContractsResponse
  property_count: 2
  slug: public-api-v6-get-contracts-response
- name: GetCoursesReponse
  property_count: 2
  slug: public-api-v6-get-courses-reponse
- name: GetCrossRegionalClientAssociationsResponse
  property_count: 2
  slug: public-api-v6-get-cross-regional-client-associations-response
- name: GetCustomClientFieldsResponse
  property_count: 2
  slug: public-api-v6-get-custom-client-fields-response
- name: GetCustomPaymentMethodsResponse
  property_count: 2
  slug: public-api-v6-get-custom-payment-methods-response
- name: GetEnrollmentsResponse
  property_count: 2
  slug: public-api-v6-get-enrollments-response
- name: GetGendersResponse
  property_count: 1
  slug: public-api-v6-get-genders-response
- name: GetGiftCardBalanceResponse
  property_count: 2
  slug: public-api-v6-get-gift-card-balance-response
- name: GetGiftCardResponse
  property_count: 2
  slug: public-api-v6-get-gift-card-response
- name: GetLiabilityWaiverResponse
  property_count: 1
  slug: public-api-v6-get-liability-waiver-response
- name: GetLocationsResponse
  property_count: 2
  slug: public-api-v6-get-locations-response
- name: GetMembershipsResponse
  property_count: 1
  slug: public-api-v6-get-memberships-response
- name: GetMobileProvidersResponse
  property_count: 1
  slug: public-api-v6-get-mobile-providers-response
- name: GetPackagesResponse
  property_count: 2
  slug: public-api-v6-get-packages-response
- name: GetPaymentTypesResponse
  property_count: 1
  slug: public-api-v6-get-payment-types-response
- name: GetPickASpotClassResponse
  property_count: 3
  slug: public-api-v6-get-pick-aspot-class-response
- name: GetProductsInventoryResponse
  property_count: 2
  slug: public-api-v6-get-products-inventory-response
- name: GetProductsResponse
  property_count: 2
  slug: public-api-v6-get-products-response
- name: GetProgramsResponse
  property_count: 2
  slug: public-api-v6-get-programs-response
- name: GetPromoCodesResponse
  property_count: 2
  slug: public-api-v6-get-promo-codes-response
- name: GetProspectStagesResponse
  property_count: 1
  slug: public-api-v6-get-prospect-stages-response
- name: GetRelationshipsResponse
  property_count: 2
  slug: public-api-v6-get-relationships-response
- name: GetRequiredClientFieldsResponse
  property_count: 1
  slug: public-api-v6-get-required-client-fields-response
- name: GetReservationResponse
  property_count: 3
  slug: public-api-v6-get-reservation-response
- name: GetResourceAvailabilitiesResponse
  property_count: 2
  slug: public-api-v6-get-resource-availabilities-response
- name: GetSalesRepsResponse
  property_count: 2
  slug: public-api-v6-get-sales-reps-response
- name: GetSalesResponse
  property_count: 2
  slug: public-api-v6-get-sales-response
- name: GetScheduleItemsResponse
  property_count: 2
  slug: public-api-v6-get-schedule-items-response
- name: GetScheduledServiceEarningsResponse
  property_count: 2
  slug: public-api-v6-get-scheduled-service-earnings-response
- name: GetSemestersResponse
  property_count: 2
  slug: public-api-v6-get-semesters-response
- name: GetServicesResponse
  property_count: 2
  slug: public-api-v6-get-services-response
- name: GetSessionTypesResponse
  property_count: 2
  slug: public-api-v6-get-session-types-response
- name: GetSitesResponse
  property_count: 2
  slug: public-api-v6-get-sites-response
- name: GetStaffAppointmentsResponse
  property_count: 2
  slug: public-api-v6-get-staff-appointments-response
- name: GetStaffImageURLResponse
  property_count: 2
  slug: public-api-v6-get-staff-image-urlresponse
- name: GetStaffPermissionsResponse
  property_count: 1
  slug: public-api-v6-get-staff-permissions-response
- name: GetStaffResponse
  property_count: 2
  slug: public-api-v6-get-staff-response
- name: GetStaffSessionTypesResponse
  property_count: 2
  slug: public-api-v6-get-staff-session-types-response
- name: GetTimeCardsResponse
  property_count: 2
  slug: public-api-v6-get-time-cards-response
- name: GetTipsResponse
  property_count: 2
  slug: public-api-v6-get-tips-response
- name: GetTransactionsResponse
  property_count: 2
  slug: public-api-v6-get-transactions-response
- name: GetUnavailabilitiesResponse
  property_count: 2
  slug: public-api-v6-get-unavailabilities-response
- name: GetWaitlistEntriesResponse
  property_count: 2
  slug: public-api-v6-get-waitlist-entries-response
- name: GiftCardLayout
  property_count: 3
  slug: public-api-v6-gift-card-layout
- name: GiftCard
  property_count: 12
  slug: public-api-v6-gift-card
- name: HttpContent
  property_count: 1
  slug: public-api-v6-http-content
- name: InitiateCheckoutShoppingCartUsingAlternativePaymentsRequest
  property_count: 15
  slug: public-api-v6-initiate-checkout-shopping-cart-using-alternative-payments-request
- name: InitiatePurchaseContractRequest
  property_count: 10
  slug: public-api-v6-initiate-purchase-contract-request
- name: IssueRequest
  property_count: 2
  slug: public-api-v6-issue-request
- name: IssueResponse
  property_count: 4
  slug: public-api-v6-issue-response
- name: LeadChannel
  property_count: 5
  slug: public-api-v6-lead-channel
- name: Level
  property_count: 3
  slug: public-api-v6-level
- name: Liability
  property_count: 3
  slug: public-api-v6-liability
- name: Location
  property_count: 25
  slug: public-api-v6-location
- name: Location1
  property_count: 56
  slug: public-api-v6-location1
- name: M0CultureNeutralPublicKeyTokenB77a5c561934e089
  property_count: 2
  slug: public-api-v6-m0-culture-neutral-public-key-token-b77a5c561934e089
- name: Membership
  property_count: 14
  slug: public-api-v6-membership
- name: MembershipTypeRestriction
  property_count: 2
  slug: public-api-v6-membership-type-restriction
- name: MergeClientsRequest
  property_count: 2
  slug: public-api-v6-merge-clients-request
- name: MinimumCommitmentUnitEnum
  property_count: 0
  slug: public-api-v6-minimum-commitment-unit-enum
- name: MobileProvider
  property_count: 4
  slug: public-api-v6-mobile-provider
- name: Package
  property_count: 6
  slug: public-api-v6-package
- name: PaginationResponse
  property_count: 4
  slug: public-api-v6-pagination-response
- name: Pagination
  property_count: 4
  slug: public-api-v6-pagination
- name: PaymentMethodEnum
  property_count: 0
  slug: public-api-v6-payment-method-enum
- name: PaymentProcessingFailure
  property_count: 3
  slug: public-api-v6-payment-processing-failure
- name: PaymentType
  property_count: 4
  slug: public-api-v6-payment-type
- name: PickASpotClass
  property_count: 11
  slug: public-api-v6-pick-aspot-class
- name: PricingRelationships
  property_count: 2
  slug: public-api-v6-pricing-relationships
- name: Product
  property_count: 20
  slug: public-api-v6-product
- name: ProductsInventory
  property_count: 10
  slug: public-api-v6-products-inventory
- name: ProgramMembership
  property_count: 2
  slug: public-api-v6-program-membership
- name: Program
  property_count: 6
  slug: public-api-v6-program
- name: Program1
  property_count: 9
  slug: public-api-v6-program1
- name: PromoCode
  property_count: 14
  slug: public-api-v6-promo-code
- name: ProspectStage
  property_count: 3
  slug: public-api-v6-prospect-stage
- name: PublicDisplayEnum
  property_count: 0
  slug: public-api-v6-public-display-enum
- name: PublicDisplay1Enum
  property_count: 0
  slug: public-api-v6-public-display1-enum
- name: PurchaseAccountCreditRequest
  property_count: 8
  slug: public-api-v6-purchase-account-credit-request
- name: PurchaseAccountCreditResponse
  property_count: 5
  slug: public-api-v6-purchase-account-credit-response
- name: PurchaseContractRequest
  property_count: 19
  slug: public-api-v6-purchase-contract-request
- name: PurchaseContractResponse
  property_count: 7
  slug: public-api-v6-purchase-contract-response
- name: PurchaseContractResponseTotals
  property_count: 4
  slug: public-api-v6-purchase-contract-response-totals
- name: PurchaseGiftCardRequest
  property_count: 17
  slug: public-api-v6-purchase-gift-card-request
- name: PurchaseGiftCardResponse
  property_count: 11
  slug: public-api-v6-purchase-gift-card-response
- name: PurchasedItem
  property_count: 25
  slug: public-api-v6-purchased-item
- name: Relationship
  property_count: 3
  slug: public-api-v6-relationship
- name: RemoveClientFromClassRequest
  property_count: 7
  slug: public-api-v6-remove-client-from-class-request
- name: RemoveClientFromClassResponse
  property_count: 1
  slug: public-api-v6-remove-client-from-class-response
- name: RemoveClientsFromClassesRequest
  property_count: 6
  slug: public-api-v6-remove-clients-from-classes-request
- name: RemoveClientsFromClassesResponse
  property_count: 3
  slug: public-api-v6-remove-clients-from-classes-response
- name: Reservation
  property_count: 9
  slug: public-api-v6-reservation
- name: ResourceAvailability
  property_count: 3
  slug: public-api-v6-resource-availability
- name: ResourceAvailability1
  property_count: 5
  slug: public-api-v6-resource-availability1
- name: Resource
  property_count: 2
  slug: public-api-v6-resource
- name: ResourceSlim
  property_count: 2
  slug: public-api-v6-resource-slim
- name: ResponseDetails
  property_count: 3
  slug: public-api-v6-response-details
- name: ReturnSaleRequest
  property_count: 2
  slug: public-api-v6-return-sale-request
- name: ReturnSaleResponse
  property_count: 3
  slug: public-api-v6-return-sale-response
- name: SalePayment
  property_count: 6
  slug: public-api-v6-sale-payment
- name: Sale
  property_count: 11
  slug: public-api-v6-sale
- name: SalesRepResponse
  property_count: 4
  slug: public-api-v6-sales-rep-response
- name: SalesRep
  property_count: 5
  slug: public-api-v6-sales-rep
- name: ScheduleTypeEnum
  property_count: 0
  slug: public-api-v6-schedule-type-enum
- name: ScheduleType2Enum
  property_count: 0
  slug: public-api-v6-schedule-type2-enum
- name: ScheduledServiceEarningsEvent
  property_count: 5
  slug: public-api-v6-scheduled-service-earnings-event
- name: ScheduledServiceTypeEnum
  property_count: 0
  slug: public-api-v6-scheduled-service-type-enum
- name: Semester
  property_count: 8
  slug: public-api-v6-semester
- name: SendAutoEmailRequest
  property_count: 2
  slug: public-api-v6-send-auto-email-request
- name: SendPasswordResetEmailRequest
  property_count: 3
  slug: public-api-v6-send-password-reset-email-request
- name: Service
  property_count: 27
  slug: public-api-v6-service
- name: ServiceTag
  property_count: 2
  slug: public-api-v6-service-tag
- name: SessionType
  property_count: 13
  slug: public-api-v6-session-type
- name: SessionType1
  property_count: 14
  slug: public-api-v6-session-type1
- name: ShoppingCart
  property_count: 8
  slug: public-api-v6-shopping-cart
- name: Site
  property_count: 23
  slug: public-api-v6-site
- name: Size
  property_count: 2
  slug: public-api-v6-size
- name: Spot
  property_count: 3
  slug: public-api-v6-spot
- name: StaffPermissionGroup
  property_count: 4
  slug: public-api-v6-staff-permission-group
- name: Staff
  property_count: 38
  slug: public-api-v6-staff
- name: StaffSessionType
  property_count: 15
  slug: public-api-v6-staff-session-type
- name: StaffSetting
  property_count: 2
  slug: public-api-v6-staff-setting
- name: Staff1
  property_count: 45
  slug: public-api-v6-staff1
- name: StatusEnum
  property_count: 0
  slug: public-api-v6-status-enum
- name: Status1Enum
  property_count: 0
  slug: public-api-v6-status1-enum
- name: StoredCardInfo
  property_count: 1
  slug: public-api-v6-stored-card-info
- name: SubCategory
  property_count: 3
  slug: public-api-v6-sub-category
- name: SubstituteClassTeacherRequest
  property_count: 6
  slug: public-api-v6-substitute-class-teacher-request
- name: SubstituteClassTeacherResponse
  property_count: 1
  slug: public-api-v6-substitute-class-teacher-response
- name: SubstituteTeacherClass
  property_count: 21
  slug: public-api-v6-substitute-teacher-class
- name: SuspendContractRequest
  property_count: 9
  slug: public-api-v6-suspend-contract-request
- name: SuspendContractResponse
  property_count: 1
  slug: public-api-v6-suspend-contract-response
- name: TerminateContractRequest
  property_count: 5
  slug: public-api-v6-terminate-contract-request
- name: TerminateContractResponse
  property_count: 1
  slug: public-api-v6-terminate-contract-response
- name: TimeCardEvent
  property_count: 7
  slug: public-api-v6-time-card-event
- name: Tip
  property_count: 4
  slug: public-api-v6-tip
- name: TransactionResponse
  property_count: 2
  slug: public-api-v6-transaction-response
- name: Transaction
  property_count: 17
  slug: public-api-v6-transaction
- name: TypeEnum
  property_count: 0
  slug: public-api-v6-type-enum
- name: Type1Enum
  property_count: 0
  slug: public-api-v6-type1-enum
- name: Type2Enum
  property_count: 0
  slug: public-api-v6-type2-enum
- name: UnavailabilityPlain
  property_count: 5
  slug: public-api-v6-unavailability-plain
- name: Unavailability
  property_count: 4
  slug: public-api-v6-unavailability
- name: Unavailability1
  property_count: 4
  slug: public-api-v6-unavailability1
- name: UpcomingAutopayEvent
  property_count: 7
  slug: public-api-v6-upcoming-autopay-event
- name: UpdateAppointmentRequest
  property_count: 14
  slug: public-api-v6-update-appointment-request
- name: UpdateAppointmentResponse
  property_count: 1
  slug: public-api-v6-update-appointment-response
- name: UpdateAvailabilityRequest
  property_count: 9
  slug: public-api-v6-update-availability-request
- name: UpdateAvailabilityResponse
  property_count: 2
  slug: public-api-v6-update-availability-response
- name: UpdateClassEnrollmentScheduleRequest
  property_count: 24
  slug: public-api-v6-update-class-enrollment-schedule-request
- name: UpdateClassScheduleNotesRequest
  property_count: 1
  slug: public-api-v6-update-class-schedule-notes-request
- name: UpdateClientContractAutopaysRequest
  property_count: 7
  slug: public-api-v6-update-client-contract-autopays-request
- name: UpdateClientRequest
  property_count: 5
  slug: public-api-v6-update-client-request
- name: UpdateClientResponse
  property_count: 1
  slug: public-api-v6-update-client-response
- name: UpdateClientRewardsRequest
  property_count: 6
  slug: public-api-v6-update-client-rewards-request
- name: UpdateClientServiceRequest
  property_count: 5
  slug: public-api-v6-update-client-service-request
- name: UpdateClientServiceResponse
  property_count: 1
  slug: public-api-v6-update-client-service-response
- name: UpdateClientVisitRequest
  property_count: 7
  slug: public-api-v6-update-client-visit-request
- name: UpdateClientVisitResponse
  property_count: 1
  slug: public-api-v6-update-client-visit-response
- name: UpdateContactLogComment
  property_count: 2
  slug: public-api-v6-update-contact-log-comment
- name: UpdateContactLogRequest
  property_count: 10
  slug: public-api-v6-update-contact-log-request
- name: UpdateContactLogType
  property_count: 2
  slug: public-api-v6-update-contact-log-type
- name: UpdateProductPriceRequest
  property_count: 3
  slug: public-api-v6-update-product-price-request
- name: UpdateProductPriceResponse
  property_count: 1
  slug: public-api-v6-update-product-price-response
- name: UpdateReservationResponse
  property_count: 2
  slug: public-api-v6-update-reservation-response
- name: UpdateSaleDateRequest
  property_count: 2
  slug: public-api-v6-update-sale-date-request
- name: UpdateSaleDateResponse
  property_count: 1
  slug: public-api-v6-update-sale-date-response
- name: UpdateServiceResponse
  property_count: 1
  slug: public-api-v6-update-service-response
- name: UpdateSiteClientIndexRequest
  property_count: 10
  slug: public-api-v6-update-site-client-index-request
- name: UpdateSiteClientIndexResponse
  property_count: 10
  slug: public-api-v6-update-site-client-index-response
- name: UpdateStaffPermissionsRequest
  property_count: 2
  slug: public-api-v6-update-staff-permissions-request
- name: UpdateStaffPermissionsResponse
  property_count: 1
  slug: public-api-v6-update-staff-permissions-response
- name: UpdateStaffRequest
  property_count: 28
  slug: public-api-v6-update-staff-request
- name: UpdateStaffResponse
  property_count: 1
  slug: public-api-v6-update-staff-response
- name: UploadClientDocumentRequest
  property_count: 2
  slug: public-api-v6-upload-client-document-request
- name: UploadClientDocumentResponse
  property_count: 2
  slug: public-api-v6-upload-client-document-response
- name: UploadClientPhotoRequest
  property_count: 2
  slug: public-api-v6-upload-client-photo-request
- name: UploadClientPhotoResponse
  property_count: 2
  slug: public-api-v6-upload-client-photo-response
- name: User
  property_count: 4
  slug: public-api-v6-user
- name: Visit
  property_count: 28
  slug: public-api-v6-visit
- name: VisitWaitlistInfo
  property_count: 2
  slug: public-api-v6-visit-waitlist-info
- name: VisitWithWaitlistInfo
  property_count: 29
  slug: public-api-v6-visit-with-waitlist-info
- name: WaitlistEntry
  property_count: 9
  slug: public-api-v6-waitlist-entry
- name: WrittenClassSchedulesInfo
  property_count: 2
  slug: public-api-v6-written-class-schedules-info
- name: CreateSubscriptionRequest
  property_count: 4
  slug: webhooks-api-create-subscription-request
- name: CreateSubscriptionResponse
  property_count: 11
  slug: webhooks-api-create-subscription-response
- name: DeactivateSubscriptionResponse
  property_count: 4
  slug: webhooks-api-deactivate-subscription-response
- name: GetMetricsResponse
  property_count: 1
  slug: webhooks-api-get-metrics-response
- name: GetSubscriptionsResponse
  property_count: 1
  slug: webhooks-api-get-subscriptions-response
- name: Metric
  property_count: 8
  slug: webhooks-api-metric
- name: PatchSubscriptionRequest
  property_count: 5
  slug: webhooks-api-patch-subscription-request
- name: PushApiError
  property_count: 3
  slug: webhooks-api-push-api-error
- name: PushApiResultCreateSubscriptionResponse
  property_count: 3
  slug: webhooks-api-push-api-result-create-subscription-response
- name: PushApiResultDeactivateSubscriptionResponse
  property_count: 3
  slug: webhooks-api-push-api-result-deactivate-subscription-response
- name: PushApiResultGetSubscriptionsResponse
  property_count: 3
  slug: webhooks-api-push-api-result-get-subscriptions-response
- name: PushApiResultSubscription
  property_count: 3
  slug: webhooks-api-push-api-result-subscription
- name: Subscription
  property_count: 10
  slug: webhooks-api-subscription
json_structures:
- name: Public Api V6 Action Enum Structure
  property_count: 0
  slug: public-api-v6-action-enum-structure
- name: Public Api V6 Action1 Enum Structure
  property_count: 0
  slug: public-api-v6-action1-enum-structure
- name: Public Api V6 Action11 Enum Structure
  property_count: 0
  slug: public-api-v6-action11-enum-structure
- name: Public Api V6 Action8 Enum Structure
  property_count: 0
  slug: public-api-v6-action8-enum-structure
- name: Public Api V6 Activation Type Enum Structure
  property_count: 0
  slug: public-api-v6-activation-type-enum-structure
- name: Public Api V6 Add Appointment Add On Request Structure
  property_count: 5
  slug: public-api-v6-add-appointment-add-on-request-structure
- name: Public Api V6 Add Appointment Add On Response Structure
  property_count: 2
  slug: public-api-v6-add-appointment-add-on-response-structure
- name: Public Api V6 Add Appointment Outcome Structure
  property_count: 3
  slug: public-api-v6-add-appointment-outcome-structure
- name: Public Api V6 Add Appointment Request Structure
  property_count: 19
  slug: public-api-v6-add-appointment-request-structure
- name: Public Api V6 Add Appointment Response Structure
  property_count: 1
  slug: public-api-v6-add-appointment-response-structure
- name: Public Api V6 Add Arrival Request Structure
  property_count: 5
  slug: public-api-v6-add-arrival-request-structure
- name: Public Api V6 Add Arrival Response Structure
  property_count: 2
  slug: public-api-v6-add-arrival-response-structure
- name: Public Api V6 Add Availabilities Request Structure
  property_count: 10
  slug: public-api-v6-add-availabilities-request-structure
- name: Public Api V6 Add Availabilities Response Structure
  property_count: 2
  slug: public-api-v6-add-availabilities-response-structure
- name: Public Api V6 Add Class Enrollment Schedule Request Structure
  property_count: 24
  slug: public-api-v6-add-class-enrollment-schedule-request-structure
- name: Public Api V6 Add Client Direct Debit Info Request Structure
  property_count: 6
  slug: public-api-v6-add-client-direct-debit-info-request-structure
- name: Public Api V6 Add Client Direct Debit Info Response Structure
  property_count: 5
  slug: public-api-v6-add-client-direct-debit-info-response-structure
- name: Public Api V6 Add Client Request Structure
  property_count: 60
  slug: public-api-v6-add-client-request-structure
- name: Public Api V6 Add Client Response Structure
  property_count: 1
  slug: public-api-v6-add-client-response-structure
- name: Public Api V6 Add Client To Class Request Structure
  property_count: 11
  slug: public-api-v6-add-client-to-class-request-structure
- name: Public Api V6 Add Client To Class Response Structure
  property_count: 1
  slug: public-api-v6-add-client-to-class-response-structure
- name: Public Api V6 Add Client To Class Visit Structure
  property_count: 23
  slug: public-api-v6-add-client-to-class-visit-structure
- name: Public Api V6 Add Client To Enrollment Request Structure
  property_count: 8
  slug: public-api-v6-add-client-to-enrollment-request-structure
- name: Public Api V6 Add Contact Log Request Structure
  property_count: 10
  slug: public-api-v6-add-contact-log-request-structure
- name: Public Api V6 Add Contact Log Type Structure
  property_count: 2
  slug: public-api-v6-add-contact-log-type-structure
- name: Public Api V6 Add Formula Note Request Structure
  property_count: 3
  slug: public-api-v6-add-formula-note-request-structure
- name: Public Api V6 Add Multiple Appointments Request Structure
  property_count: 1
  slug: public-api-v6-add-multiple-appointments-request-structure
- name: Public Api V6 Add Multiple Appointments Response Structure
  property_count: 1
  slug: public-api-v6-add-multiple-appointments-response-structure
- name: Public Api V6 Add On Small Structure
  property_count: 4
  slug: public-api-v6-add-on-small-structure
- name: Public Api V6 Add On Small1 Structure
  property_count: 4
  slug: public-api-v6-add-on-small1-structure
- name: Public Api V6 Add Promo Code Request Structure
  property_count: 11
  slug: public-api-v6-add-promo-code-request-structure
- name: Public Api V6 Add Promo Code Response Structure
  property_count: 1
  slug: public-api-v6-add-promo-code-response-structure
- name: Public Api V6 Add Site Client Index Request Structure
  property_count: 9
  slug: public-api-v6-add-site-client-index-request-structure
- name: Public Api V6 Add Site Client Index Response Structure
  property_count: 10
  slug: public-api-v6-add-site-client-index-response-structure
- name: Public Api V6 Add Staff Availability Request Structure
  property_count: 11
  slug: public-api-v6-add-staff-availability-request-structure
- name: Public Api V6 Add Staff Request Structure
  property_count: 26
  slug: public-api-v6-add-staff-request-structure
- name: Public Api V6 Add Staff Response Structure
  property_count: 1
  slug: public-api-v6-add-staff-response-structure
- name: Public Api V6 Allowed Permission Enum Structure
  property_count: 0
  slug: public-api-v6-allowed-permission-enum-structure
- name: Public Api V6 Alternative Payment Method Structure
  property_count: 2
  slug: public-api-v6-alternative-payment-method-structure
- name: Public Api V6 Amenity Structure
  property_count: 2
  slug: public-api-v6-amenity-structure
- name: Public Api V6 Amenity1 Structure
  property_count: 2
  slug: public-api-v6-amenity1-structure
- name: Public Api V6 Api Error1 Structure
  property_count: 2
  slug: public-api-v6-api-error1-structure
- name: Public Api V6 Applicable Item Structure
  property_count: 3
  slug: public-api-v6-applicable-item-structure
- name: Public Api V6 Appointment Add On Structure
  property_count: 5
  slug: public-api-v6-appointment-add-on-structure
- name: Public Api V6 Appointment Gender Preference Enum Structure
  property_count: 0
  slug: public-api-v6-appointment-gender-preference-enum-structure
- name: Public Api V6 Appointment Gender Preference1 Enum Structure
  property_count: 0
  slug: public-api-v6-appointment-gender-preference1-enum-structure
- name: Public Api V6 Appointment Option Structure
  property_count: 4
  slug: public-api-v6-appointment-option-structure
- name: Public Api V6 Appointment Staff Structure
  property_count: 4
  slug: public-api-v6-appointment-staff-structure
- name: Public Api V6 Appointment Status Enum Structure
  property_count: 0
  slug: public-api-v6-appointment-status-enum-structure
- name: Public Api V6 Appointment Structure
  property_count: 23
  slug: public-api-v6-appointment-structure
- name: Public Api V6 Appointment1 Structure
  property_count: 22
  slug: public-api-v6-appointment1-structure
- name: Public Api V6 Assign Staff Session Type Request Structure
  property_count: 8
  slug: public-api-v6-assign-staff-session-type-request-structure
- name: Public Api V6 Assign Staff Session Type Response Structure
  property_count: 8
  slug: public-api-v6-assign-staff-session-type-response-structure
- name: Public Api V6 Assigned Client Index Structure
  property_count: 2
  slug: public-api-v6-assigned-client-index-structure
- name: Public Api V6 Autopay Schedule Structure
  property_count: 3
  slug: public-api-v6-autopay-schedule-structure
- name: Public Api V6 Autopay Status Enum Structure
  property_count: 0
  slug: public-api-v6-autopay-status-enum-structure
- name: Public Api V6 Availability Structure
  property_count: 13
  slug: public-api-v6-availability-structure
- name: Public Api V6 Availability1 Structure
  property_count: 13
  slug: public-api-v6-availability1-structure
- name: Public Api V6 Booking Status Enum Structure
  property_count: 0
  slug: public-api-v6-booking-status-enum-structure
- name: Public Api V6 Booking Window Structure
  property_count: 4
  slug: public-api-v6-booking-window-structure
- name: Public Api V6 Cancel Single Class Request Structure
  property_count: 4
  slug: public-api-v6-cancel-single-class-request-structure
- name: Public Api V6 Cancel Single Class Response Structure
  property_count: 1
  slug: public-api-v6-cancel-single-class-response-structure
- name: Public Api V6 Cart Item Structure
  property_count: 8
  slug: public-api-v6-cart-item-structure
- name: Public Api V6 Category Structure
  property_count: 11
  slug: public-api-v6-category-structure
- name: Public Api V6 Checkout Alternative Payment Info Structure
  property_count: 2
  slug: public-api-v6-checkout-alternative-payment-info-structure
- name: Public Api V6 Checkout Appointment Booking Request Structure
  property_count: 7
  slug: public-api-v6-checkout-appointment-booking-request-structure
- name: Public Api V6 Checkout Item Structure
  property_count: 2
  slug: public-api-v6-checkout-item-structure
- name: Public Api V6 Checkout Item Wrapper Structure
  property_count: 11
  slug: public-api-v6-checkout-item-wrapper-structure
- name: Public Api V6 Checkout Payment Info Structure
  property_count: 2
  slug: public-api-v6-checkout-payment-info-structure
- name: Public Api V6 Checkout Shopping Cart Request Structure
  property_count: 20
  slug: public-api-v6-checkout-shopping-cart-request-structure
- name: Public Api V6 Checkout Shopping Cart Response Structure
  property_count: 4
  slug: public-api-v6-checkout-shopping-cart-response-structure
- name: Public Api V6 Class Client Detail Structure
  property_count: 2
  slug: public-api-v6-class-client-detail-structure
- name: Public Api V6 Class Description Structure
  property_count: 15
  slug: public-api-v6-class-description-structure
- name: Public Api V6 Class Schedule Structure
  property_count: 24
  slug: public-api-v6-class-schedule-structure
- name: Public Api V6 Class Structure
  property_count: 30
  slug: public-api-v6-class-structure
- name: Public Api V6 Client Arrival Structure
  property_count: 4
  slug: public-api-v6-client-arrival-structure
- name: Public Api V6 Client Contract Structure
  property_count: 23
  slug: public-api-v6-client-contract-structure
- name: Public Api V6 Client Credit Card Structure
  property_count: 10
  slug: public-api-v6-client-credit-card-structure
- name: Public Api V6 Client Document Structure
  property_count: 3
  slug: public-api-v6-client-document-structure
- name: Public Api V6 Client Duplicate Structure
  property_count: 5
  slug: public-api-v6-client-duplicate-structure
- name: Public Api V6 Client Index Structure
  property_count: 6
  slug: public-api-v6-client-index-structure
- name: Public Api V6 Client Index Value Structure
  property_count: 3
  slug: public-api-v6-client-index-value-structure
- name: Public Api V6 Client Membership Structure
  property_count: 17
  slug: public-api-v6-client-membership-structure
- name: Public Api V6 Client Memberships Structure
  property_count: 3
  slug: public-api-v6-client-memberships-structure
- name: Public Api V6 Client Purchase Record Structure
  property_count: 9
  slug: public-api-v6-client-purchase-record-structure
- name: Public Api V6 Client Relationship Structure
  property_count: 5
  slug: public-api-v6-client-relationship-structure
- name: Public Api V6 Client Reward Transaction Structure
  property_count: 6
  slug: public-api-v6-client-reward-transaction-structure
- name: Public Api V6 Client Service Structure
  property_count: 14
  slug: public-api-v6-client-service-structure
- name: Public Api V6 Client Service With Activation Type Structure
  property_count: 16
  slug: public-api-v6-client-service-with-activation-type-structure
- name: Public Api V6 Client Structure
  property_count: 58
  slug: public-api-v6-client-structure
- name: Public Api V6 Client Suspension Info Structure
  property_count: 3
  slug: public-api-v6-client-suspension-info-structure
- name: Public Api V6 Client Type Structure
  property_count: 2
  slug: public-api-v6-client-type-structure
- name: Public Api V6 Client With Suspension Info Structure
  property_count: 59
  slug: public-api-v6-client-with-suspension-info-structure
- name: Public Api V6 Color Structure
  property_count: 2
  slug: public-api-v6-color-structure
- name: Public Api V6 Commission Detail Structure
  property_count: 2
  slug: public-api-v6-commission-detail-structure
- name: Public Api V6 Commission Payroll Purchase Event Structure
  property_count: 7
  slug: public-api-v6-commission-payroll-purchase-event-structure
- name: Public Api V6 Complete Checkout Shopping Cart Using Alternative Payments Request Structure
  property_count: 3
  slug: public-api-v6-complete-checkout-shopping-cart-using-alternative-payments-request-structure
- name: Public Api V6 Contact Log Comment Structure
  property_count: 4
  slug: public-api-v6-contact-log-comment-structure
- name: Public Api V6 Contact Log Structure
  property_count: 11
  slug: public-api-v6-contact-log-structure
- name: Public Api V6 Contact Log Sub Type Structure
  property_count: 2
  slug: public-api-v6-contact-log-sub-type-structure
- name: Public Api V6 Contact Log Type Structure
  property_count: 3
  slug: public-api-v6-contact-log-type-structure
- name: Public Api V6 Content Format Enum Structure
  property_count: 0
  slug: public-api-v6-content-format-enum-structure
- name: Public Api V6 Contract Item Structure
  property_count: 7
  slug: public-api-v6-contract-item-structure
- name: Public Api V6 Contract Structure
  property_count: 38
  slug: public-api-v6-contract-structure
- name: Public Api V6 Copy Credit Card Request Structure
  property_count: 6
  slug: public-api-v6-copy-credit-card-request-structure
- name: Public Api V6 Copy Credit Card Response Client Structure
  property_count: 5
  slug: public-api-v6-copy-credit-card-response-client-structure
- name: Public Api V6 Copy Credit Card Response Structure
  property_count: 2
  slug: public-api-v6-copy-credit-card-response-structure
- name: Public Api V6 Course Structure
  property_count: 10
  slug: public-api-v6-course-structure
- name: Public Api V6 Create Reservation Response Structure
  property_count: 2
  slug: public-api-v6-create-reservation-response-structure
- name: Public Api V6 Credit Card Info Structure
  property_count: 11
  slug: public-api-v6-credit-card-info-structure
- name: Public Api V6 Cross Regional Client Association Structure
  property_count: 4
  slug: public-api-v6-cross-regional-client-association-structure
- name: Public Api V6 Custom Client Field Structure
  property_count: 3
  slug: public-api-v6-custom-client-field-structure
- name: Public Api V6 Custom Client Field Value Structure
  property_count: 4
  slug: public-api-v6-custom-client-field-value-structure
- name: Public Api V6 Custom Payment Method Structure
  property_count: 2
  slug: public-api-v6-custom-payment-method-structure
- name: Public Api V6 Days Of Week Enum Structure
  property_count: 0
  slug: public-api-v6-days-of-week-enum-structure
- name: Public Api V6 Days Valid Enum Structure
  property_count: 0
  slug: public-api-v6-days-valid-enum-structure
- name: Public Api V6 Deactivate Promo Code Request Structure
  property_count: 1
  slug: public-api-v6-deactivate-promo-code-request-structure
- name: Public Api V6 Denied Permission Enum Structure
  property_count: 0
  slug: public-api-v6-denied-permission-enum-structure
- name: Public Api V6 Direct Debit Info Structure
  property_count: 4
  slug: public-api-v6-direct-debit-info-structure
- name: Public Api V6 Discount Structure
  property_count: 2
  slug: public-api-v6-discount-structure
- name: Public Api V6 Formula Note Response Structure
  property_count: 10
  slug: public-api-v6-formula-note-response-structure
- name: Public Api V6 Frequency Type Enum Structure
  property_count: 0
  slug: public-api-v6-frequency-type-enum-structure
- name: Public Api V6 Gender Option Structure
  property_count: 4
  slug: public-api-v6-gender-option-structure
- name: Public Api V6 Gender Preference Enum Structure
  property_count: 0
  slug: public-api-v6-gender-preference-enum-structure
- name: Public Api V6 Get Activation Code Response Structure
  property_count: 2
  slug: public-api-v6-get-activation-code-response-structure
- name: Public Api V6 Get Active Client Memberships Response Structure
  property_count: 2
  slug: public-api-v6-get-active-client-memberships-response-structure
- name: Public Api V6 Get Active Clients Memberships Response Structure
  property_count: 2
  slug: public-api-v6-get-active-clients-memberships-response-structure
- name: Public Api V6 Get Active Session Times Response Structure
  property_count: 2
  slug: public-api-v6-get-active-session-times-response-structure
- name: Public Api V6 Get Add Ons Response Structure
  property_count: 2
  slug: public-api-v6-get-add-ons-response-structure
- name: Public Api V6 Get Alternative Payment Methods Response Structure
  property_count: 1
  slug: public-api-v6-get-alternative-payment-methods-response-structure
- name: Public Api V6 Get Appointment Options Response Structure
  property_count: 1
  slug: public-api-v6-get-appointment-options-response-structure
- name: Public Api V6 Get Available Dates Response Structure
  property_count: 1
  slug: public-api-v6-get-available-dates-response-structure
- name: Public Api V6 Get Bookable Items Response Structure
  property_count: 2
  slug: public-api-v6-get-bookable-items-response-structure
- name: Public Api V6 Get Categories Response Structure
  property_count: 2
  slug: public-api-v6-get-categories-response-structure
- name: Public Api V6 Get Class Descriptions Response Structure
  property_count: 2
  slug: public-api-v6-get-class-descriptions-response-structure
- name: Public Api V6 Get Class Schedules Response Structure
  property_count: 2
  slug: public-api-v6-get-class-schedules-response-structure
- name: Public Api V6 Get Class Visits Response Structure
  property_count: 1
  slug: public-api-v6-get-class-visits-response-structure
- name: Public Api V6 Get Classes Response Structure
  property_count: 2
  slug: public-api-v6-get-classes-response-structure
- name: Public Api V6 Get Client Account Balances Response Structure
  property_count: 2
  slug: public-api-v6-get-client-account-balances-response-structure
- name: Public Api V6 Get Client Complete Info Response Structure
  property_count: 5
  slug: public-api-v6-get-client-complete-info-response-structure
- name: Public Api V6 Get Client Contracts Response Structure
  property_count: 2
  slug: public-api-v6-get-client-contracts-response-structure
- name: Public Api V6 Get Client Duplicates Response Structure
  property_count: 2
  slug: public-api-v6-get-client-duplicates-response-structure
- name: Public Api V6 Get Client Formula Notes Response Structure
  property_count: 2
  slug: public-api-v6-get-client-formula-notes-response-structure
- name: Public Api V6 Get Client Indexes Response Structure
  property_count: 1
  slug: public-api-v6-get-client-indexes-response-structure
- name: Public Api V6 Get Client Purchases Response Structure
  property_count: 2
  slug: public-api-v6-get-client-purchases-response-structure
- name: Public Api V6 Get Client Referral Types Response Structure
  property_count: 1
  slug: public-api-v6-get-client-referral-types-response-structure
- name: Public Api V6 Get Client Rewards Response Structure
  property_count: 3
  slug: public-api-v6-get-client-rewards-response-structure
- name: Public Api V6 Get Client Schedule Response Structure
  property_count: 2
  slug: public-api-v6-get-client-schedule-response-structure
- name: Public Api V6 Get Client Services Response Structure
  property_count: 2
  slug: public-api-v6-get-client-services-response-structure
- name: Public Api V6 Get Client Visits Response Structure
  property_count: 2
  slug: public-api-v6-get-client-visits-response-structure
- name: Public Api V6 Get Clients Response Structure
  property_count: 2
  slug: public-api-v6-get-clients-response-structure
- name: Public Api V6 Get Commissions Response Structure
  property_count: 2
  slug: public-api-v6-get-commissions-response-structure
- name: Public Api V6 Get Contact Log Types Response Structure
  property_count: 2
  slug: public-api-v6-get-contact-log-types-response-structure
- name: Public Api V6 Get Contact Logs Response Structure
  property_count: 2
  slug: public-api-v6-get-contact-logs-response-structure
- name: Public Api V6 Get Contracts Response Structure
  property_count: 2
  slug: public-api-v6-get-contracts-response-structure
- name: Public Api V6 Get Courses Reponse Structure
  property_count: 2
  slug: public-api-v6-get-courses-reponse-structure
- name: Public Api V6 Get Cross Regional Client Associations Response Structure
  property_count: 2
  slug: public-api-v6-get-cross-regional-client-associations-response-structure
- name: Public Api V6 Get Custom Client Fields Response Structure
  property_count: 2
  slug: public-api-v6-get-custom-client-fields-response-structure
- name: Public Api V6 Get Custom Payment Methods Response Structure
  property_count: 2
  slug: public-api-v6-get-custom-payment-methods-response-structure
- name: Public Api V6 Get Enrollments Response Structure
  property_count: 2
  slug: public-api-v6-get-enrollments-response-structure
- name: Public Api V6 Get Genders Response Structure
  property_count: 1
  slug: public-api-v6-get-genders-response-structure
- name: Public Api V6 Get Gift Card Balance Response Structure
  property_count: 2
  slug: public-api-v6-get-gift-card-balance-response-structure
- name: Public Api V6 Get Gift Card Response Structure
  property_count: 2
  slug: public-api-v6-get-gift-card-response-structure
- name: Public Api V6 Get Liability Waiver Response Structure
  property_count: 1
  slug: public-api-v6-get-liability-waiver-response-structure
- name: Public Api V6 Get Locations Response Structure
  property_count: 2
  slug: public-api-v6-get-locations-response-structure
- name: Public Api V6 Get Memberships Response Structure
  property_count: 1
  slug: public-api-v6-get-memberships-response-structure
- name: Public Api V6 Get Mobile Providers Response Structure
  property_count: 1
  slug: public-api-v6-get-mobile-providers-response-structure
- name: Public Api V6 Get Packages Response Structure
  property_count: 2
  slug: public-api-v6-get-packages-response-structure
- name: Public Api V6 Get Payment Types Response Structure
  property_count: 1
  slug: public-api-v6-get-payment-types-response-structure
- name: Public Api V6 Get Pick Aspot Class Response Structure
  property_count: 3
  slug: public-api-v6-get-pick-aspot-class-response-structure
- name: Public Api V6 Get Products Inventory Response Structure
  property_count: 2
  slug: public-api-v6-get-products-inventory-response-structure
- name: Public Api V6 Get Products Response Structure
  property_count: 2
  slug: public-api-v6-get-products-response-structure
- name: Public Api V6 Get Programs Response Structure
  property_count: 2
  slug: public-api-v6-get-programs-response-structure
- name: Public Api V6 Get Promo Codes Response Structure
  property_count: 2
  slug: public-api-v6-get-promo-codes-response-structure
- name: Public Api V6 Get Prospect Stages Response Structure
  property_count: 1
  slug: public-api-v6-get-prospect-stages-response-structure
- name: Public Api V6 Get Relationships Response Structure
  property_count: 2
  slug: public-api-v6-get-relationships-response-structure
- name: Public Api V6 Get Required Client Fields Response Structure
  property_count: 1
  slug: public-api-v6-get-required-client-fields-response-structure
- name: Public Api V6 Get Reservation Response Structure
  property_count: 3
  slug: public-api-v6-get-reservation-response-structure
- name: Public Api V6 Get Resource Availabilities Response Structure
  property_count: 2
  slug: public-api-v6-get-resource-availabilities-response-structure
- name: Public Api V6 Get Sales Reps Response Structure
  property_count: 2
  slug: public-api-v6-get-sales-reps-response-structure
- name: Public Api V6 Get Sales Response Structure
  property_count: 2
  slug: public-api-v6-get-sales-response-structure
- name: Public Api V6 Get Schedule Items Response Structure
  property_count: 2
  slug: public-api-v6-get-schedule-items-response-structure
- name: Public Api V6 Get Scheduled Service Earnings Response Structure
  property_count: 2
  slug: public-api-v6-get-scheduled-service-earnings-response-structure
- name: Public Api V6 Get Semesters Response Structure
  property_count: 2
  slug: public-api-v6-get-semesters-response-structure
- name: Public Api V6 Get Services Response Structure
  property_count: 2
  slug: public-api-v6-get-services-response-structure
- name: Public Api V6 Get Session Types Response Structure
  property_count: 2
  slug: public-api-v6-get-session-types-response-structure
- name: Public Api V6 Get Sites Response Structure
  property_count: 2
  slug: public-api-v6-get-sites-response-structure
- name: Public Api V6 Get Staff Appointments Response Structure
  property_count: 2
  slug: public-api-v6-get-staff-appointments-response-structure
- name: Public Api V6 Get Staff Image Urlresponse Structure
  property_count: 2
  slug: public-api-v6-get-staff-image-urlresponse-structure
- name: Public Api V6 Get Staff Permissions Response Structure
  property_count: 1
  slug: public-api-v6-get-staff-permissions-response-structure
- name: Public Api V6 Get Staff Response Structure
  property_count: 2
  slug: public-api-v6-get-staff-response-structure
- name: Public Api V6 Get Staff Session Types Response Structure
  property_count: 2
  slug: public-api-v6-get-staff-session-types-response-structure
- name: Public Api V6 Get Time Cards Response Structure
  property_count: 2
  slug: public-api-v6-get-time-cards-response-structure
- name: Public Api V6 Get Tips Response Structure
  property_count: 2
  slug: public-api-v6-get-tips-response-structure
- name: Public Api V6 Get Transactions Response Structure
  property_count: 2
  slug: public-api-v6-get-transactions-response-structure
- name: Public Api V6 Get Unavailabilities Response Structure
  property_count: 2
  slug: public-api-v6-get-unavailabilities-response-structure
- name: Public Api V6 Get Waitlist Entries Response Structure
  property_count: 2
  slug: public-api-v6-get-waitlist-entries-response-structure
- name: Public Api V6 Gift Card Layout Structure
  property_count: 3
  slug: public-api-v6-gift-card-layout-structure
- name: Public Api V6 Gift Card Structure
  property_count: 12
  slug: public-api-v6-gift-card-structure
- name: Public Api V6 Http Content Structure
  property_count: 1
  slug: public-api-v6-http-content-structure
- name: Public Api V6 Initiate Checkout Shopping Cart Using Alternative Payments Request Structure
  property_count: 15
  slug: public-api-v6-initiate-checkout-shopping-cart-using-alternative-payments-request-structure
- name: Public Api V6 Initiate Purchase Contract Request Structure
  property_count: 10
  slug: public-api-v6-initiate-purchase-contract-request-structure
- name: Public Api V6 Issue Request Structure
  property_count: 2
  slug: public-api-v6-issue-request-structure
- name: Public Api V6 Issue Response Structure
  property_count: 4
  slug: public-api-v6-issue-response-structure
- name: Public Api V6 Lead Channel Structure
  property_count: 5
  slug: public-api-v6-lead-channel-structure
- name: Public Api V6 Level Structure
  property_count: 3
  slug: public-api-v6-level-structure
- name: Public Api V6 Liability Structure
  property_count: 3
  slug: public-api-v6-liability-structure
- name: Public Api V6 Location Structure
  property_count: 25
  slug: public-api-v6-location-structure
- name: Public Api V6 Location1 Structure
  property_count: 56
  slug: public-api-v6-location1-structure
- name: Public Api V6 M0 Culture Neutral Public Key Token B77A5C561934E089 Structure
  property_count: 2
  slug: public-api-v6-m0-culture-neutral-public-key-token-b77a5c561934e089-structure
- name: Public Api V6 Membership Structure
  property_count: 14
  slug: public-api-v6-membership-structure
- name: Public Api V6 Membership Type Restriction Structure
  property_count: 2
  slug: public-api-v6-membership-type-restriction-structure
- name: Public Api V6 Merge Clients Request Structure
  property_count: 2
  slug: public-api-v6-merge-clients-request-structure
- name: Public Api V6 Minimum Commitment Unit Enum Structure
  property_count: 0
  slug: public-api-v6-minimum-commitment-unit-enum-structure
- name: Public Api V6 Mobile Provider Structure
  property_count: 4
  slug: public-api-v6-mobile-provider-structure
- name: Public Api V6 Package Structure
  property_count: 6
  slug: public-api-v6-package-structure
- name: Public Api V6 Pagination Response Structure
  property_count: 4
  slug: public-api-v6-pagination-response-structure
- name: Public Api V6 Pagination Structure
  property_count: 4
  slug: public-api-v6-pagination-structure
- name: Public Api V6 Payment Method Enum Structure
  property_count: 0
  slug: public-api-v6-payment-method-enum-structure
- name: Public Api V6 Payment Processing Failure Structure
  property_count: 3
  slug: public-api-v6-payment-processing-failure-structure
- name: Public Api V6 Payment Type Structure
  property_count: 4
  slug: public-api-v6-payment-type-structure
- name: Public Api V6 Pick Aspot Class Structure
  property_count: 11
  slug: public-api-v6-pick-aspot-class-structure
- name: Public Api V6 Pricing Relationships Structure
  property_count: 2
  slug: public-api-v6-pricing-relationships-structure
- name: Public Api V6 Product Structure
  property_count: 20
  slug: public-api-v6-product-structure
- name: Public Api V6 Products Inventory Structure
  property_count: 10
  slug: public-api-v6-products-inventory-structure
- name: Public Api V6 Program Membership Structure
  property_count: 2
  slug: public-api-v6-program-membership-structure
- name: Public Api V6 Program Structure
  property_count: 6
  slug: public-api-v6-program-structure
- name: Public Api V6 Program1 Structure
  property_count: 9
  slug: public-api-v6-program1-structure
- name: Public Api V6 Promo Code Structure
  property_count: 14
  slug: public-api-v6-promo-code-structure
- name: Public Api V6 Prospect Stage Structure
  property_count: 3
  slug: public-api-v6-prospect-stage-structure
- name: Public Api V6 Public Display Enum Structure
  property_count: 0
  slug: public-api-v6-public-display-enum-structure
- name: Public Api V6 Public Display1 Enum Structure
  property_count: 0
  slug: public-api-v6-public-display1-enum-structure
- name: Public Api V6 Purchase Account Credit Request Structure
  property_count: 8
  slug: public-api-v6-purchase-account-credit-request-structure
- name: Public Api V6 Purchase Account Credit Response Structure
  property_count: 5
  slug: public-api-v6-purchase-account-credit-response-structure
- name: Public Api V6 Purchase Contract Request Structure
  property_count: 19
  slug: public-api-v6-purchase-contract-request-structure
- name: Public Api V6 Purchase Contract Response Structure
  property_count: 7
  slug: public-api-v6-purchase-contract-response-structure
- name: Public Api V6 Purchase Contract Response Totals Structure
  property_count: 4
  slug: public-api-v6-purchase-contract-response-totals-structure
- name: Public Api V6 Purchase Gift Card Request Structure
  property_count: 17
  slug: public-api-v6-purchase-gift-card-request-structure
- name: Public Api V6 Purchase Gift Card Response Structure
  property_count: 11
  slug: public-api-v6-purchase-gift-card-response-structure
- name: Public Api V6 Purchased Item Structure
  property_count: 25
  slug: public-api-v6-purchased-item-structure
- name: Public Api V6 Relationship Structure
  property_count: 3
  slug: public-api-v6-relationship-structure
- name: Public Api V6 Remove Client From Class Request Structure
  property_count: 7
  slug: public-api-v6-remove-client-from-class-request-structure
- name: Public Api V6 Remove Client From Class Response Structure
  property_count: 1
  slug: public-api-v6-remove-client-from-class-response-structure
- name: Public Api V6 Remove Clients From Classes Request Structure
  property_count: 6
  slug: public-api-v6-remove-clients-from-classes-request-structure
- name: Public Api V6 Remove Clients From Classes Response Structure
  property_count: 3
  slug: public-api-v6-remove-clients-from-classes-response-structure
- name: Public Api V6 Reservation Structure
  property_count: 9
  slug: public-api-v6-reservation-structure
- name: Public Api V6 Resource Availability Structure
  property_count: 3
  slug: public-api-v6-resource-availability-structure
- name: Public Api V6 Resource Availability1 Structure
  property_count: 5
  slug: public-api-v6-resource-availability1-structure
- name: Public Api V6 Resource Slim Structure
  property_count: 2
  slug: public-api-v6-resource-slim-structure
- name: Public Api V6 Resource Structure
  property_count: 2
  slug: public-api-v6-resource-structure
- name: Public Api V6 Response Details Structure
  property_count: 3
  slug: public-api-v6-response-details-structure
- name: Public Api V6 Return Sale Request Structure
  property_count: 2
  slug: public-api-v6-return-sale-request-structure
- name: Public Api V6 Return Sale Response Structure
  property_count: 3
  slug: public-api-v6-return-sale-response-structure
- name: Public Api V6 Sale Payment Structure
  property_count: 6
  slug: public-api-v6-sale-payment-structure
- name: Public Api V6 Sale Structure
  property_count: 11
  slug: public-api-v6-sale-structure
- name: Public Api V6 Sales Rep Response Structure
  property_count: 4
  slug: public-api-v6-sales-rep-response-structure
- name: Public Api V6 Sales Rep Structure
  property_count: 5
  slug: public-api-v6-sales-rep-structure
- name: Public Api V6 Schedule Type Enum Structure
  property_count: 0
  slug: public-api-v6-schedule-type-enum-structure
- name: Public Api V6 Schedule Type2 Enum Structure
  property_count: 0
  slug: public-api-v6-schedule-type2-enum-structure
- name: Public Api V6 Scheduled Service Earnings Event Structure
  property_count: 5
  slug: public-api-v6-scheduled-service-earnings-event-structure
- name: Public Api V6 Scheduled Service Type Enum Structure
  property_count: 0
  slug: public-api-v6-scheduled-service-type-enum-structure
- name: Public Api V6 Semester Structure
  property_count: 8
  slug: public-api-v6-semester-structure
- name: Public Api V6 Send Auto Email Request Structure
  property_count: 2
  slug: public-api-v6-send-auto-email-request-structure
- name: Public Api V6 Send Password Reset Email Request Structure
  property_count: 3
  slug: public-api-v6-send-password-reset-email-request-structure
- name: Public Api V6 Service Structure
  property_count: 27
  slug: public-api-v6-service-structure
- name: Public Api V6 Service Tag Structure
  property_count: 2
  slug: public-api-v6-service-tag-structure
- name: Public Api V6 Session Type Structure
  property_count: 13
  slug: public-api-v6-session-type-structure
- name: Public Api V6 Session Type1 Structure
  property_count: 14
  slug: public-api-v6-session-type1-structure
- name: Public Api V6 Shopping Cart Structure
  property_count: 8
  slug: public-api-v6-shopping-cart-structure
- name: Public Api V6 Site Structure
  property_count: 23
  slug: public-api-v6-site-structure
- name: Public Api V6 Size Structure
  property_count: 2
  slug: public-api-v6-size-structure
- name: Public Api V6 Spot Structure
  property_count: 3
  slug: public-api-v6-spot-structure
- name: Public Api V6 Staff Permission Group Structure
  property_count: 4
  slug: public-api-v6-staff-permission-group-structure
- name: Public Api V6 Staff Session Type Structure
  property_count: 15
  slug: public-api-v6-staff-session-type-structure
- name: Public Api V6 Staff Setting Structure
  property_count: 2
  slug: public-api-v6-staff-setting-structure
- name: Public Api V6 Staff Structure
  property_count: 38
  slug: public-api-v6-staff-structure
- name: Public Api V6 Staff1 Structure
  property_count: 45
  slug: public-api-v6-staff1-structure
- name: Public Api V6 Status Enum Structure
  property_count: 0
  slug: public-api-v6-status-enum-structure
- name: Public Api V6 Status1 Enum Structure
  property_count: 0
  slug: public-api-v6-status1-enum-structure
- name: Public Api V6 Stored Card Info Structure
  property_count: 1
  slug: public-api-v6-stored-card-info-structure
- name: Public Api V6 Sub Category Structure
  property_count: 3
  slug: public-api-v6-sub-category-structure
- name: Public Api V6 Substitute Class Teacher Request Structure
  property_count: 6
  slug: public-api-v6-substitute-class-teacher-request-structure
- name: Public Api V6 Substitute Class Teacher Response Structure
  property_count: 1
  slug: public-api-v6-substitute-class-teacher-response-structure
- name: Public Api V6 Substitute Teacher Class Structure
  property_count: 21
  slug: public-api-v6-substitute-teacher-class-structure
- name: Public Api V6 Suspend Contract Request Structure
  property_count: 9
  slug: public-api-v6-suspend-contract-request-structure
- name: Public Api V6 Suspend Contract Response Structure
  property_count: 1
  slug: public-api-v6-suspend-contract-response-structure
- name: Public Api V6 Terminate Contract Request Structure
  property_count: 5
  slug: public-api-v6-terminate-contract-request-structure
- name: Public Api V6 Terminate Contract Response Structure
  property_count: 1
  slug: public-api-v6-terminate-contract-response-structure
- name: Public Api V6 Time Card Event Structure
  property_count: 7
  slug: public-api-v6-time-card-event-structure
- name: Public Api V6 Tip Structure
  property_count: 4
  slug: public-api-v6-tip-structure
- name: Public Api V6 Transaction Response Structure
  property_count: 2
  slug: public-api-v6-transaction-response-structure
- name: Public Api V6 Transaction Structure
  property_count: 17
  slug: public-api-v6-transaction-structure
- name: Public Api V6 Type Enum Structure
  property_count: 0
  slug: public-api-v6-type-enum-structure
- name: Public Api V6 Type1 Enum Structure
  property_count: 0
  slug: public-api-v6-type1-enum-structure
- name: Public Api V6 Type2 Enum Structure
  property_count: 0
  slug: public-api-v6-type2-enum-structure
- name: Public Api V6 Unavailability Plain Structure
  property_count: 5
  slug: public-api-v6-unavailability-plain-structure
- name: Public Api V6 Unavailability Structure
  property_count: 4
  slug: public-api-v6-unavailability-structure
- name: Public Api V6 Unavailability1 Structure
  property_count: 4
  slug: public-api-v6-unavailability1-structure
- name: Public Api V6 Upcoming Autopay Event Structure
  property_count: 7
  slug: public-api-v6-upcoming-autopay-event-structure
- name: Public Api V6 Update Appointment Request Structure
  property_count: 14
  slug: public-api-v6-update-appointment-request-structure
- name: Public Api V6 Update Appointment Response Structure
  property_count: 1
  slug: public-api-v6-update-appointment-response-structure
- name: Public Api V6 Update Availability Request Structure
  property_count: 9
  slug: public-api-v6-update-availability-request-structure
- name: Public Api V6 Update Availability Response Structure
  property_count: 2
  slug: public-api-v6-update-availability-response-structure
- name: Public Api V6 Update Class Enrollment Schedule Request Structure
  property_count: 24
  slug: public-api-v6-update-class-enrollment-schedule-request-structure
- name: Public Api V6 Update Class Schedule Notes Request Structure
  property_count: 1
  slug: public-api-v6-update-class-schedule-notes-request-structure
- name: Public Api V6 Update Client Contract Autopays Request Structure
  property_count: 7
  slug: public-api-v6-update-client-contract-autopays-request-structure
- name: Public Api V6 Update Client Request Structure
  property_count: 5
  slug: public-api-v6-update-client-request-structure
- name: Public Api V6 Update Client Response Structure
  property_count: 1
  slug: public-api-v6-update-client-response-structure
- name: Public Api V6 Update Client Rewards Request Structure
  property_count: 6
  slug: public-api-v6-update-client-rewards-request-structure
- name: Public Api V6 Update Client Service Request Structure
  property_count: 5
  slug: public-api-v6-update-client-service-request-structure
- name: Public Api V6 Update Client Service Response Structure
  property_count: 1
  slug: public-api-v6-update-client-service-response-structure
- name: Public Api V6 Update Client Visit Request Structure
  property_count: 7
  slug: public-api-v6-update-client-visit-request-structure
- name: Public Api V6 Update Client Visit Response Structure
  property_count: 1
  slug: public-api-v6-update-client-visit-response-structure
- name: Public Api V6 Update Contact Log Comment Structure
  property_count: 2
  slug: public-api-v6-update-contact-log-comment-structure
- name: Public Api V6 Update Contact Log Request Structure
  property_count: 10
  slug: public-api-v6-update-contact-log-request-structure
- name: Public Api V6 Update Contact Log Type Structure
  property_count: 2
  slug: public-api-v6-update-contact-log-type-structure
- name: Public Api V6 Update Product Price Request Structure
  property_count: 3
  slug: public-api-v6-update-product-price-request-structure
- name: Public Api V6 Update Product Price Response Structure
  property_count: 1
  slug: public-api-v6-update-product-price-response-structure
- name: Public Api V6 Update Reservation Response Structure
  property_count: 2
  slug: public-api-v6-update-reservation-response-structure
- name: Public Api V6 Update Sale Date Request Structure
  property_count: 2
  slug: public-api-v6-update-sale-date-request-structure
- name: Public Api V6 Update Sale Date Response Structure
  property_count: 1
  slug: public-api-v6-update-sale-date-response-structure
- name: Public Api V6 Update Service Response Structure
  property_count: 1
  slug: public-api-v6-update-service-response-structure
- name: Public Api V6 Update Site Client Index Request Structure
  property_count: 10
  slug: public-api-v6-update-site-client-index-request-structure
- name: Public Api V6 Update Site Client Index Response Structure
  property_count: 10
  slug: public-api-v6-update-site-client-index-response-structure
- name: Public Api V6 Update Staff Permissions Request Structure
  property_count: 2
  slug: public-api-v6-update-staff-permissions-request-structure
- name: Public Api V6 Update Staff Permissions Response Structure
  property_count: 1
  slug: public-api-v6-update-staff-permissions-response-structure
- name: Public Api V6 Update Staff Request Structure
  property_count: 28
  slug: public-api-v6-update-staff-request-structure
- name: Public Api V6 Update Staff Response Structure
  property_count: 1
  slug: public-api-v6-update-staff-response-structure
- name: Public Api V6 Upload Client Document Request Structure
  property_count: 2
  slug: public-api-v6-upload-client-document-request-structure
- name: Public Api V6 Upload Client Document Response Structure
  property_count: 2
  slug: public-api-v6-upload-client-document-response-structure
- name: Public Api V6 Upload Client Photo Request Structure
  property_count: 2
  slug: public-api-v6-upload-client-photo-request-structure
- name: Public Api V6 Upload Client Photo Response Structure
  property_count: 2
  slug: public-api-v6-upload-client-photo-response-structure
- name: Public Api V6 User Structure
  property_count: 4
  slug: public-api-v6-user-structure
- name: Public Api V6 Visit Structure
  property_count: 28
  slug: public-api-v6-visit-structure
- name: Public Api V6 Visit Waitlist Info Structure
  property_count: 2
  slug: public-api-v6-visit-waitlist-info-structure
- name: Public Api V6 Visit With Waitlist Info Structure
  property_count: 29
  slug: public-api-v6-visit-with-waitlist-info-structure
- name: Public Api V6 Waitlist Entry Structure
  property_count: 9
  slug: public-api-v6-waitlist-entry-structure
- name: Public Api V6 Written Class Schedules Info Structure
  property_count: 2
  slug: public-api-v6-written-class-schedules-info-structure
- name: Webhooks Api Create Subscription Request Structure
  property_count: 4
  slug: webhooks-api-create-subscription-request-structure
- name: Webhooks Api Create Subscription Response Structure
  property_count: 11
  slug: webhooks-api-create-subscription-response-structure
- name: Webhooks Api Deactivate Subscription Response Structure
  property_count: 4
  slug: webhooks-api-deactivate-subscription-response-structure
- name: Webhooks Api Get Metrics Response Structure
  property_count: 1
  slug: webhooks-api-get-metrics-response-structure
- name: Webhooks Api Get Subscriptions Response Structure
  property_count: 1
  slug: webhooks-api-get-subscriptions-response-structure
- name: Webhooks Api Metric Structure
  property_count: 8
  slug: webhooks-api-metric-structure
- name: Webhooks Api Patch Subscription Request Structure
  property_count: 5
  slug: webhooks-api-patch-subscription-request-structure
- name: Webhooks Api Push Api Error Structure
  property_count: 3
  slug: webhooks-api-push-api-error-structure
- name: Webhooks Api Push Api Result Create Subscription Response Structure
  property_count: 3
  slug: webhooks-api-push-api-result-create-subscription-response-structure
- name: Webhooks Api Push Api Result Deactivate Subscription Response Structure
  property_count: 3
  slug: webhooks-api-push-api-result-deactivate-subscription-response-structure
- name: Webhooks Api Push Api Result Get Subscriptions Response Structure
  property_count: 3
  slug: webhooks-api-push-api-result-get-subscriptions-response-structure
- name: Webhooks Api Push Api Result Subscription Structure
  property_count: 3
  slug: webhooks-api-push-api-result-subscription-structure
- name: Webhooks Api Subscription Structure
  property_count: 10
  slug: webhooks-api-subscription-structure
jsonld:
- class_count: 309
  name: Mindbody Public Api V6 Context
  property_count: 797
  slug: mindbody-public-api-v6-context
- class_count: 13
  name: Mindbody Webhooks Api Context
  property_count: 25
  slug: mindbody-webhooks-api-context
layout: provider
modified: '2026-05-28'
name: Mindbody
nav: Providers
network: true
overview: 'Mindbody publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Appointment API, Class API, Client API, and 10 more. Tagged areas include Fitness, Wellness, Beauty, Scheduling, and Booking.


  The Mindbody catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Mindbody''s developer surface includes authentication, documentation, getting-started guide, signup flow, pricing, support, FAQ, and 34 more developer resources.'
plans:
- name: Mindbody Plans Pricing
  plan_count: 4
  slug: mindbody-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Mindbody Rate Limits
  slug: mindbody-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Mindbody API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mindbody-jsonschema-spectral-rules
- effective_rule_count: 94
  extends:
  - spectral:oas
  name: Mindbody API Rules
  rule_count: 53
  severity_counts:
    error: 16
    hint: 0
    info: 5
    warn: 32
  slug: mindbody-spectral-rules
scopes:
- name: Mindbody Scopes
  scope_count: 5
  slug: mindbody-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 66.2
  delta: 5.4
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 28.8
    contract_quality: 71.4
    developer_ergonomics: 76.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 65.8
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/mindbody/refs/heads/main/screenshots/mindbody-2026-06-20T185555.png
security:
- kind: authentication
  name: Mindbody Authentication
  slug: mindbody-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Mindbody Domain Security
  slug: mindbody-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mindbody Trust Center
  slug: mindbody-trust-center
  summary_line: PCI DSS
slug: mindbody
solutions:
- description: Yoga, pilates, barre, indoor cycling, HIIT, and martial-arts studios.
  name: Boutique Fitness
- description: Hair, nail, and beauty salons using appointment scheduling and POS.
  name: Beauty and Salon
- description: Day spas, medspas, and integrative wellness centers.
  name: Spa and Wellness
- description: Multi-location gyms and health clubs with classes, personal training, and recurring memberships.
  name: Health Clubs and Gyms
tags:
- Fitness
- Wellness
- Beauty
- Scheduling
- Booking
- Point-of-Sale
- Studios
- Salons
- Spas
- Webhook
use_cases:
- description: Build branded mobile or web booking experiences for yoga, pilates, barre, and fitness studios.
  name: Studio Booking Apps
- description: Sync clients and sales events into CRMs (HubSpot, Salesforce) and trigger marketing journeys.
  name: CRM and Marketing Automation
- description: Power class/appointment discovery and booking in third-party wellness apps and ClassPass-style platforms.
  name: Wellness Aggregator Integrations
- description: Pipe payroll, sales, and class fill data into BI tooling for chain operators.
  name: Studio Operations Analytics
- description: Drive loyalty points and rewards from visit/sale events delivered via the Webhooks API.
  name: Customer Loyalty Programs
- description: Use Cross-Site to recognize repeat clients across affiliated Mindbody businesses.
  name: Network Identity
website: https://www.mindbodyonline.com/
---
