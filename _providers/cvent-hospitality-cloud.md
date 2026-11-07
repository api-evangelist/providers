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
  - finops
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 196
  human_in_the_loop: 0
  name: Cvent Hospitality Cloud Agentic Access
  operation_count: 469
  slug: cvent-hospitality-cloud-agentic-access
  summary_line: 469 operations · 196 acting
api_count: 17
apis:
- description: Cvent's legacy SOAP 1.1 / WSDL 1.1 / WS-I Basic Profile 1.1 Web Services API, still served and still documented. 51 operations and 390 complex types under targetNamespace http://api.cvent.com/2006-11,
  name: Cvent SOAP Web Services API (V200611)
  slug: soap-v200611
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'An appointment is a meeting scheduled between two or more parties. These APIs allow you to get information about your Cvent Appointments: appointment attendees, their interests, and availabilities. * '
  name: Cvent Hospitality Cloud Appointments API
  slug: cvent-hospitality-cloud-appointments-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Attendee Activities API gives valuable insight into your customer's experience at your Cvent event. Now, you can get a fuller picture of your customer's journey, including onsite activities, offsi
  name: Cvent Hospitality Cloud Attendee Activities API
  slug: cvent-hospitality-cloud-attendee-activities-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'The Attendee Insights feature provides valuable information about your event attendees. It assists planners, marketers, and exhibitors in targeting customers effectively, thereby enhancing engagement '
  name: Cvent Hospitality Cloud Attendee Insights API
  slug: cvent-hospitality-cloud-attendee-insights-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: These APIs retrieve and manage attendee messages—communications exchanged between attendees within channels. Channels are virtual spaces created for one-on-one or group conversations, allowing attende
  name: Cvent Hospitality Cloud Attendee Messages API
  slug: cvent-hospitality-cloud-attendee-messages-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Attendee entity primarily refers to the person throughout the lifecycle of an event including registration, enrollment into sessions, and participation. Once contacts are added to events, an Atten
  name: Cvent Hospitality Cloud Attendees API
  slug: cvent-hospitality-cloud-attendees-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Audience Segments allow planners to segment their attendees into groups and better manage the attendee experience based on their defined segments. Audience Segments APIs will enable you to get, create
  name: Cvent Hospitality Cloud Audience Segments API
  slug: cvent-hospitality-cloud-audience-segments-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Endpoints for obtaining, refreshing, and validating OAuth2 access tokens.
  name: Cvent Hospitality Cloud Authentication API
  slug: cvent-hospitality-cloud-authentication-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Badge print jobs can be scheduled to a printer pool, so a printer in the printer pool can consume the job and print the badge.
  name: Cvent Hospitality Cloud Badge Print Job API
  slug: cvent-hospitality-cloud-badge-print-job-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Badge printer pools are set up from Cvent UI. You can use this API to retrieve badge printer pools.
  name: Cvent Hospitality Cloud Badge Printer Pools API
  slug: cvent-hospitality-cloud-badge-printer-pools-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Budget is an event feature used to organize spending and track [allocations](https://support.cvent.com/s/communityarticle/Setting-Up-Budget-Allocations). Use this API to view budget items, cards and c
  name: Cvent Hospitality Cloud Budget API
  slug: cvent-hospitality-cloud-budget-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'The Bulk API provides a simple interface to upload large amounts of data into Cvent. The API processes the uploaded data asynchronously making API calls on behalf of the caller. Consumers of the bulk '
  name: Cvent Hospitality Cloud Bulk API
  slug: cvent-hospitality-cloud-bulk-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Planners use eMarketing campaigns to contact an audience, such as newsletters, press releases, or product updates. Campaign emails are used as newsletters, promotions, advertisements, or marketing mes
  name: Cvent Hospitality Cloud Campaigns API
  slug: cvent-hospitality-cloud-campaigns-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '**Card Tokenization**: Tokenization is the process Cvent uses to collect sensitive card details and personally identifiable information (PII), directly from your customers in a secure manner. This gua'
  name: Cvent Hospitality Cloud Card Tokens API
  slug: cvent-hospitality-cloud-card-tokens-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: These API's provide compliance support for regulated industries. **Communication Compliance** lets you view communication activities across your account for archival or analysis. Various written forms
  name: Cvent Hospitality Cloud Compliance API
  slug: cvent-hospitality-cloud-compliance-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'A contact is a record in your account’s address book that represents an individual. The data stored within these records includes personal information, group memberships, and historical data on event '
  name: Cvent Hospitality Cloud Contacts API
  slug: cvent-hospitality-cloud-contacts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Custom Fields are created by event planners to track important information about specific objects like events, contacts, or sessions. Use these APIs to view, create, and update custom fields in your a
  name: Cvent Hospitality Cloud Custom Fields API
  slug: cvent-hospitality-cloud-custom-fields-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Discounts provide a way to reduce the cost of event registration items. Use these APIs to manage event discounts, including creating, updating, and linking discounts to agenda items.
  name: Cvent Hospitality Cloud Discounts API
  slug: cvent-hospitality-cloud-discounts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event planners use emails to invite registrants, market their events and request feedback from attendees. Use these APIs to get historical data about your emails and see relevant details like the type
  name: Cvent Hospitality Cloud Emails API
  slug: cvent-hospitality-cloud-emails-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event Credits reward attendees for participating in your events. Planners can award credits for the entire event, specific sessions, or both. You can also award credits after attendees complete survey
  name: Cvent Hospitality Cloud Event Credits API
  slug: cvent-hospitality-cloud-event-credits-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: EventFeatures related APIs
  name: Cvent Hospitality Cloud Event Features API
  slug: cvent-hospitality-cloud-event-features-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event roles are event specific permission sets for your organization's users. Use these APIs to retrieve, create, update, and delete event role assignments to your organization's users.
  name: Cvent Hospitality Cloud Event Role API
  slug: cvent-hospitality-cloud-event-role-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Event travel lets planners capture air & hotel requests from attendees and track air actuals, hotel reservations and alternate travel answers at your event. Use these endpoints to retrieve your air, h
  name: Cvent Hospitality Cloud Event Travel API
  slug: cvent-hospitality-cloud-event-travel-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Events are used to collect registrations and allow attendees to select their schedule. Use these APIs to get information about your events and use the event ID to get further details about the event, '
  name: Cvent Hospitality Cloud Events API
  slug: cvent-hospitality-cloud-events-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: An Events+ Hub persists basic information needed to assign an owner and optionally customize the public presentation.
  name: Cvent Hospitality Cloud Events+ Hub API
  slug: cvent-hospitality-cloud-events-hub-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '* **Exhibitor -** An exhibitor is an organization that is sponsoring or exhibiting at your event. This API allows you to get information about your exhibitors. * **Registration Pack -** Registration P'
  name: Cvent Hospitality Cloud Exhibitor API
  slug: cvent-hospitality-cloud-exhibitor-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Exhibitor Content operations for an exhibitor. This API allows you to upload & get exhibitor content data such as files, weblinks.
  name: Cvent Hospitality Cloud Exhibitor Content API
  slug: cvent-hospitality-cloud-exhibitor-content-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '* **Exhibitor Admin -** Exhibitor Admins are administrators that have access to the exhibitor portal. In the portal, they are able to complete pre-event tasks, manage their team, purchase LeadCapture '
  name: Cvent Hospitality Cloud Exhibitor Team API
  slug: cvent-hospitality-cloud-exhibitor-team-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Allows you to upload files and get file location using the file ID. File ID can be used with other APIs to associate the file to an entity. For example: * <a href="#operation/addSessionDoc">Add Docume'
  name: Cvent Hospitality Cloud File API
  slug: cvent-hospitality-cloud-file-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: These APIs allow you to create hooks. When triggered, a hook sends a request to your service to get updated data related to the related Cvent object. For more information on using hooks, see the [gett
  name: Cvent Hospitality Cloud Hooks API
  slug: cvent-hospitality-cloud-hooks-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'RegLink APIs allow you to exchange data with Cvent Passkey events and hotel reservation-booking engines. Generally, there are four primary categories of functionality that RegLink APIs support: * **Sy'
  name: Cvent Hospitality Cloud Housing API
  slug: cvent-hospitality-cloud-housing-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: APIs for managing hotel-related operations.
  name: Cvent Hospitality Cloud Housing Hotels API
  slug: cvent-hospitality-cloud-housing-hotels-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: '* **Leads -** Leads include leads gathered by LeadCapture, Appointments, and Inbound Leads. Use this API to get information for the lead and how it was captured. * **Lead Qualification Question -** Cu'
  name: Cvent Hospitality Cloud Leads API
  slug: cvent-hospitality-cloud-leads-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: When planning an event, meeting request forms are customizable online questionnaires to capture information about the event and facilitate the approval of events. When a meeting request form is submit
  name: Cvent Hospitality Cloud Meeting Request API
  slug: cvent-hospitality-cloud-meeting-request-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Orders represent a collection of order items purchased by an attendee. Use these APIs to get information about orders and order items.
  name: Cvent Hospitality Cloud Orders API
  slug: cvent-hospitality-cloud-orders-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Process forms automate data collection and notifications related to planning and executing events. Process form submissions are responses to a specific process form, providing data the form requests. '
  name: Cvent Hospitality Cloud Process Form API
  slug: cvent-hospitality-cloud-process-form-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Beta - All APIs are in Beta. Proposal Drafts are editable copies of proposals. This API allows you to edit proposal data privately before publishing.
  name: Cvent Hospitality Cloud Proposal Draft API
  slug: cvent-hospitality-cloud-proposal-draft-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RFP additional details APIs for managing past event references and other miscellaneous RFP operations.
  name: Cvent Hospitality Cloud RFP Additional Details API
  slug: cvent-hospitality-cloud-rfp-additional-details-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RFP (Request for Proposal) management APIs for core RFP operations including CRUD operations for base RFPs.
  name: Cvent Hospitality Cloud RFP Management API
  slug: cvent-hospitality-cloud-rfp-management-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: RFP requirements APIs for managing RFP-specific requirements including guest rooms, meeting rooms, custom questions, custom fields, and attachments (CRUD operations).
  name: Cvent Hospitality Cloud RFP Requirements API
  slug: cvent-hospitality-cloud-rfp-requirements-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Suppliers are the venues and service providers that receive and respond to RFPs. Use these APIs to manage supplier associations, view recipient history, and create award details.
  name: Cvent Hospitality Cloud RFP Suppliers API
  slug: cvent-hospitality-cloud-rfp-suppliers-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Seating lets you plan seating at your events by configuring tables and assigning seats to your attendees. The seating APIs allow you to create, update, and delete seating, tables, seats, and seating a
  name: Cvent Hospitality Cloud Seating API
  slug: cvent-hospitality-cloud-seating-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: A session is a presentation, discussion, or activity. Use these APIs to get information about your sessions and use the session ID to get further data within the event.
  name: Cvent Hospitality Cloud Sessions API
  slug: cvent-hospitality-cloud-sessions-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Retrieves Check-In & Check-Out Signatures Of Attendees
  name: Cvent Hospitality Cloud Signatures API
  slug: cvent-hospitality-cloud-signatures-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Speakers are individuals presenting at your event's session(s). Use Speaker APIs to read existing speaker data, create new speakers or update existing speakers in your events.
  name: Cvent Hospitality Cloud Speakers API
  slug: cvent-hospitality-cloud-speakers-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Surveys are lists of questions deployed to your contacts. Surveys can be standalone or can be associated to a Cvent event. Use these APIs to search for surveys and retrieve the associated questions an
  name: Cvent Hospitality Cloud Surveys API
  slug: cvent-hospitality-cloud-surveys-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: 'Transactions represent the financial exchanges that occur within your account. Use these APIs to retrieve and manage transaction data, including charges, refunds, and adjustments associated with your '
  name: Cvent Hospitality Cloud Transactions API
  slug: cvent-hospitality-cloud-transactions-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The travel account, or corporation that represents the demand-side of travel RFPs.
  name: Cvent Hospitality Cloud Travel Accounts API
  slug: cvent-hospitality-cloud-travel-accounts-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Travel RFP APIs provide access to travel programs and proposals. A travel program represents a request for proposal (RFP) that defines the specific travel needs and requirements of a travel accoun
  name: Cvent Hospitality Cloud Travel RFPs API
  slug: cvent-hospitality-cloud-travel-rfps-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The Travel Supplier APIs provide access to Cvent data related to hotels, apartments, and other travel providers. This includes information related to properties, and sleeping rooms.
  name: Cvent Hospitality Cloud Travel Suppliers API
  slug: cvent-hospitality-cloud-travel-suppliers-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Use these APIs view your REST API usage and limits metrics. For more details on limits - [Rate Limits](#section/Getting-Started/Rate-Limits)
  name: Cvent Hospitality Cloud Usage API
  slug: cvent-hospitality-cloud-usage-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: The [SCIM](https://www.simplecloud.info/) standard allows for easier cross-domain identity management. This API allows you to manage your account users and SCIM groups (representing Cvent user roles).
  name: Cvent Hospitality Cloud User SCIM API
  slug: cvent-hospitality-cloud-user-scim-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Operations for managing account users and user groups, including creation, retrieval, update, and deletion. Use these endpoints to administer user access and roles within your account.
  name: Cvent Hospitality Cloud Users API
  slug: cvent-hospitality-cloud-users-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Manage meeting rooms for a venue, including creating and updating room details, configuring capacities and amenities, and associating images.
  name: Cvent Hospitality Cloud Venue Meeting Rooms API
  slug: cvent-hospitality-cloud-venue-meeting-rooms-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Manage venue profile details including type, contact information, address, and other venue properties.
  name: Cvent Hospitality Cloud Venue Profiles API
  slug: cvent-hospitality-cloud-venue-profiles-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Videos can be added to Cvent events with renditions at various resolutions, audio files, reactions tracks, and text tracks. Attendee viewership is tracked to get insight into durations, devices used a
  name: Cvent Hospitality Cloud Video API
  slug: cvent-hospitality-cloud-video-api
- baseURL: https://api-platform.cvent.com/ea
  baseurl_source: declared
  description: Webcasts are virtual or livestreaming components of your Cvent events. Use these APIs to integrate your virtual events from outside sources into your Cvent workflows, create and delete webcasts from w
  name: Cvent Hospitality Cloud Webcasts API
  slug: cvent-hospitality-cloud-webcasts-api
artifact_total: 73
asyncapis:
- description: ''
  name: Cvent Hospitality Cloud Webhooks
  slug: cvent-hospitality-cloud-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/cvent-hospitality-cloud/finops/cvent-hospitality-cloud-finops.yml
  title: ''
  type: FinOps
  url: finops/cvent-hospitality-cloud-finops.yml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/capabilities/cvent-hospitality-cloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cvent-hospitality-cloud-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-housing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-housing-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/skills/cvent-hospitality-cloud-reglink-room-block-booking.md
  title: ''
  type: AgentSkill
  url: skills/cvent-hospitality-cloud-reglink-room-block-booking.md
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/skills/cvent-hospitality-cloud-housing-reservation-management.md
  title: ''
  type: AgentSkill
  url: skills/cvent-hospitality-cloud-housing-reservation-management.md
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-authentication-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/skills/cvent-hospitality-cloud-authentication-and-quota.md
  title: ''
  type: AgentSkill
  url: skills/cvent-hospitality-cloud-authentication-and-quota.md
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-rfp-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-rfp-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-rfp-requirements-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-rfp-requirements-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-rfp-suppliers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-rfp-suppliers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-rfp-additional-details-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-rfp-additional-details-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-proposal-drafts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-proposal-drafts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-venue-profiles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-venue-profiles-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-venue-meeting-rooms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-venue-meeting-rooms-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-meeting-requests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-meeting-requests-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-travel-rfps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-travel-rfps-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-travel-suppliers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-travel-suppliers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-travel-accounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-travel-accounts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-event-travel-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-event-travel-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/overlays/cvent-hospitality-cloud-signatures-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-hospitality-cloud-signatures-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/agentic-access/cvent-hospitality-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-hospitality-cloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cvent-hospitality-cloud/security/cvent-hospitality-cloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cvent-hospitality-cloud-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cvent-hospitality-cloud/security/cvent-hospitality-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvent-hospitality-cloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cvent-hospitality-cloud/authentication/cvent-hospitality-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cvent-hospitality-cloud-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cvent-hospitality-cloud/scopes/cvent-hospitality-cloud-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cvent-hospitality-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
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
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog/feed.xml
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/supplier-venue
- group: other
  title: ''
  type: SupplierNetwork
  url: https://www.cvent.com/venues
- group: other
  title: ''
  type: Passkey
  url: https://www.cvent.com/en/supplier-venue/passkey
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/product-terms-of-use
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://developers.cvent.com/signup
- group: start
  title: ''
  type: Login
  url: https://developers.cvent.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/en/blog/latest
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cvent.com/
- group: auth
  href: https://artifacts.apis.io/cvent-hospitality-cloud/conformance/cvent-hospitality-cloud-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cvent-hospitality-cloud-conformance.yml
- group: design
  href: https://artifacts.apis.io/cvent-hospitality-cloud/conformance/cvent-hospitality-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cvent-hospitality-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/mcp/cvent-hospitality-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cvent-hospitality-cloud-mcp.yml
- group: build
  href: https://artifacts.apis.io/cvent-hospitality-cloud/mcp/cvent-hospitality-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cvent-hospitality-cloud-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/cvent-hospitality-cloud/packages/cvent-hospitality-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/cvent-hospitality-cloud-packages.yml
- group: build
  href: https://artifacts.apis.io/cvent-hospitality-cloud/packages/cvent-hospitality-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/cvent-hospitality-cloud-packages.yml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/well-known/cvent-hospitality-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cvent-hospitality-cloud-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/llms/cvent-hospitality-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cvent-hospitality-cloud-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cvent.com/llms.txt
- group: other
  href: https://artifacts.apis.io/cvent-hospitality-cloud/wsdl/cvent-hospitality-cloud-soap-v200611.wsdl
  title: ''
  type: WSDL
  url: wsdl/cvent-hospitality-cloud-soap-v200611.wsdl
- group: design
  href: https://artifacts.apis.io/cvent-hospitality-cloud/errors/cvent-hospitality-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cvent-hospitality-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cvent-hospitality-cloud/lifecycle/cvent-hospitality-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-hospitality-cloud-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cvent-hospitality-cloud/changelog/cvent-hospitality-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cvent-hospitality-cloud-changelog.yml
- group: design
  href: https://artifacts.apis.io/cvent-hospitality-cloud/conventions/cvent-hospitality-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cvent-hospitality-cloud-conventions.yml
- group: design
  href: https://artifacts.apis.io/cvent-hospitality-cloud/data-model/cvent-hospitality-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cvent-hospitality-cloud-data-model.yml
- group: start
  href: https://artifacts.apis.io/cvent-hospitality-cloud/sandbox/cvent-hospitality-cloud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cvent-hospitality-cloud-sandbox.yml
- group: design
  href: https://artifacts.apis.io/cvent-hospitality-cloud/asyncapi/cvent-hospitality-cloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cvent-hospitality-cloud-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/cvent-hospitality-cloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/cvent-hospitality-cloud/rate-limits/cvent-hospitality-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cvent-hospitality-cloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cvent-hospitality-cloud/plans/cvent-hospitality-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cvent-hospitality-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://www.cvent.com/en/contact/support
created: '2024-01-01'
description: Cvent Hospitality Cloud is the hotel and venue product line of the Cvent Platform. It includes the Cvent Supplier Network (the marketplace connecting event planners with hotels and venues for RFPs and bookings), Passkey (hotel room block and housing management), Venue Sourcing (venue search and discovery), and Sales & Catering (booking management, catering, and contracts). Programmatic access is delivered primarily through the Passkey RegLink REST APIs (with legacy SOAP and URL-based options) and the unified Cvent Platform REST API. Authentication uses OAuth 2.0 client credentials with the token endpoint at api-platform.cvent.com/ea/oauth2/token.
finops:
- has_sources: false
  method: generated
  name: Cvent Hospitality Cloud Finops
  primary_unit: request
  service_category: API
  slug: cvent-hospitality-cloud-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-hospitality-cloud.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cvent.com over streamable HTTP requiring OAuth.
  name: Cvent MCP Server
  slug: cvent-mcp-server
modified: '2026-09-07'
name: Cvent Hospitality Cloud
nav: Providers
network: true
overview: 'Cvent Hospitality Cloud publishes 57 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointments API, Attendee Activities API, Attendee Insights API, and 54 more. Tagged areas include Catering, Group Bookings, Hospitality, Hospitality Cloud, and Hotels.


  The Cvent Hospitality Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cvent Hospitality Cloud''s developer surface includes authentication, support, engineering blog, documentation, API reference, getting-started guide, signup flow, and 56 more developer resources.'
plans:
- name: Cvent Hospitality Cloud Plans Pricing
  plan_count: 0
  slug: cvent-hospitality-cloud-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Cvent Hospitality Cloud Rate Limits
  slug: cvent-hospitality-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 118
  extends:
  - spectral:oas
  name: Cvent Hospitality Cloud API Rules
  rule_count: 77
  severity_counts:
    error: 47
    hint: 0
    info: 5
    warn: 25
  slug: cvent-hospitality-cloud-rules
scopes:
- name: Cvent Hospitality Cloud Scopes
  scope_count: 238
  slug: cvent-hospitality-cloud-scopes
  summary_line: 238 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 62.9
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/cvent-hospitality-cloud/cvent-hospitality-cloud-2026-06-20T175403.png
security:
- kind: authentication
  name: Cvent Hospitality Cloud Authentication
  slug: cvent-hospitality-cloud-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cvent Hospitality Cloud Domain Security
  slug: cvent-hospitality-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Hospitality Cloud Trust Center
  slug: cvent-hospitality-cloud-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
skill_count: 5
skills:
- name: cvent-authentication-and-quota
  slug: cvent-hospitality-cloud-authentication-and-quota
- name: cvent-housing-reservation-management
  slug: cvent-hospitality-cloud-housing-reservation-management
- name: cvent-reglink-room-block-booking
  slug: cvent-hospitality-cloud-reglink-room-block-booking
- name: cvent-rfp-intake
  slug: cvent-hospitality-cloud-rfp-intake
- name: cvent-venue-profile-maintenance
  slug: cvent-hospitality-cloud-venue-profile-maintenance
slug: cvent-hospitality-cloud
tags:
- Catering
- Group Bookings
- Hospitality
- Hospitality Cloud
- Hotels
- Housing
- OAuth
- Passkeys
- Reservations
- RFP
- Room Blocks
- Sales
- Sourcing
- Supplier Network
- Venues
- Venue Sourcing
- Authentication
website: https://www.cvent.com/en/supplier-venue
---
