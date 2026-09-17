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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 222
  human_in_the_loop: 0
  name: Cvent Registration Agentic Access
  operation_count: 489
  slug: cvent-registration-agentic-access
  summary_line: 489 operations · 222 acting
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
  slug: cvent-registration-attendees-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Contact/address book
  name: Cvent Registration Contacts API
  slug: cvent-registration-contacts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event lifecycle and configuration
  name: Cvent Registration Events API
  slug: cvent-registration-events-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor management
  name: Cvent Registration Exhibitors API
  slug: cvent-registration-exhibitors-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Agenda sessions
  name: Cvent Registration Sessions API
  slug: cvent-registration-sessions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webhook subscriptions
  name: Cvent Registration Webhooks API
  slug: cvent-registration-webhooks-api
- description: The legacy Cvent SOAP API, still served and still publishing its WSDL at api.cvent.com/soap/V200611.ASMX?WSDL (HTTP 200, 330,911 bytes, targetNamespace http://api.cvent.com/2006-11). Cvent maintains a
  name: Cvent SOAP API (legacy V200611)
  slug: soap-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Account-level orders and transactions for event registration commerce. Added to the Cvent contract in the 2026-08-20 release. Read-only.
  name: Cvent Registration Orders and Transactions API
  slug: cvent-registration-orders-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Post-event and in-event surveys attached to the registration record.
  name: Cvent Registration Surveys API
  slug: cvent-registration-surveys-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Speaker records, speaker documents and speaker-to-session assignment.
  name: Cvent Registration Speakers API
  slug: cvent-registration-speakers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Table assignment, seating, badge print jobs and badge printer pools for on-site check-in.
  name: Cvent Registration Seating and Badging API
  slug: cvent-registration-seating-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Discount codes and their association to order items.
  name: Cvent Registration Discounts API
  slug: cvent-registration-discounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Custom field definitions and answers on contacts, events and sessions.
  name: Cvent Registration Custom Fields API
  slug: cvent-registration-custom-fields-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Registration travel — air, ground and arrival/departure data attached to an attendee.
  name: Cvent Registration Event Travel API
  slug: cvent-registration-event-travel-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Attendee activities, attendee insights (engagement scores) and attendee messages.
  name: Cvent Registration Attendee Activities API
  slug: cvent-registration-attendee-activities-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Read the account's REST usage tier (Free / Standard / Premium) and current quota consumption before planning a batch.
  name: Cvent Registration Usage and Quota API
  slug: cvent-registration-usage-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'An appointment is a meeting scheduled between two or more parties. These APIs allow you to get information about your Cvent Appointments: appointment attendees, their interests, and availabilities. * '
  name: Cvent Registration Appointments API
  slug: cvent-registration-appointments-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'The Attendee Insights feature provides valuable information about your event attendees. It assists planners, marketers, and exhibitors in targeting customers effectively, thereby enhancing engagement '
  name: Cvent Registration Attendee Insights API
  slug: cvent-registration-attendee-insights-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These APIs retrieve and manage attendee messages—communications exchanged between attendees within channels. Channels are virtual spaces created for one-on-one or group conversations, allowing attende
  name: Cvent Registration Attendee Messages API
  slug: cvent-registration-attendee-messages-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Audience Segments allow planners to segment their attendees into groups and better manage the attendee experience based on their defined segments. Audience Segments APIs will enable you to get, create
  name: Cvent Registration Audience Segments API
  slug: cvent-registration-audience-segments-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Endpoints for obtaining, refreshing, and validating OAuth2 access tokens.
  name: Cvent Registration Authentication API
  slug: cvent-registration-authentication-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Badge print jobs can be scheduled to a printer pool, so a printer in the printer pool can consume the job and print the badge.
  name: Cvent Registration Badge Print Job API
  slug: cvent-registration-badge-print-job-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Badge printer pools are set up from Cvent UI. You can use this API to retrieve badge printer pools.
  name: Cvent Registration Badge Printer Pools API
  slug: cvent-registration-badge-printer-pools-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Budget is an event feature used to organize spending and track [allocations](https://support.cvent.com/s/communityarticle/Setting-Up-Budget-Allocations). Use this API to view budget items, cards and c
  name: Cvent Registration Budget API
  slug: cvent-registration-budget-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'The Bulk API provides a simple interface to upload large amounts of data into Cvent. The API processes the uploaded data asynchronously making API calls on behalf of the caller. Consumers of the bulk '
  name: Cvent Registration Bulk API
  slug: cvent-registration-bulk-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Planners use eMarketing campaigns to contact an audience, such as newsletters, press releases, or product updates. Campaign emails are used as newsletters, promotions, advertisements, or marketing mes
  name: Cvent Registration Campaigns API
  slug: cvent-registration-campaigns-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '**Card Tokenization**: Tokenization is the process Cvent uses to collect sensitive card details and personally identifiable information (PII), directly from your customers in a secure manner. This gua'
  name: Cvent Registration Card Tokens API
  slug: cvent-registration-card-tokens-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These API's provide compliance support for regulated industries. **Communication Compliance** lets you view communication activities across your account for archival or analysis. Various written forms
  name: Cvent Registration Compliance API
  slug: cvent-registration-compliance-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event planners use emails to invite registrants, market their events and request feedback from attendees. Use these APIs to get historical data about your emails and see relevant details like the type
  name: Cvent Registration Emails API
  slug: cvent-registration-emails-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event Credits reward attendees for participating in your events. Planners can award credits for the entire event, specific sessions, or both. You can also award credits after attendees complete survey
  name: Cvent Registration Event Credits API
  slug: cvent-registration-event-credits-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: EventFeatures related APIs
  name: Cvent Registration Event Features API
  slug: cvent-registration-event-features-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Event roles are event specific permission sets for your organization's users. Use these APIs to retrieve, create, update, and delete event role assignments to your organization's users.
  name: Cvent Registration Event Role API
  slug: cvent-registration-event-role-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: An Events+ Hub persists basic information needed to assign an owner and optionally customize the public presentation.
  name: Cvent Registration Events+ Hub API
  slug: cvent-registration-events-hub-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Exhibitor -** An exhibitor is an organization that is sponsoring or exhibiting at your event. This API allows you to get information about your exhibitors. * **Registration Pack -** Registration P'
  name: Cvent Registration Exhibitor API
  slug: cvent-registration-exhibitor-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Exhibitor Content operations for an exhibitor. This API allows you to upload & get exhibitor content data such as files, weblinks.
  name: Cvent Registration Exhibitor Content API
  slug: cvent-registration-exhibitor-content-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Exhibitor Admin -** Exhibitor Admins are administrators that have access to the exhibitor portal. In the portal, they are able to complete pre-event tasks, manage their team, purchase LeadCapture '
  name: Cvent Registration Exhibitor Team API
  slug: cvent-registration-exhibitor-team-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Allows you to upload files and get file location using the file ID. File ID can be used with other APIs to associate the file to an entity. For example: * <a href="#operation/addSessionDoc">Add Docume'
  name: Cvent Registration File API
  slug: cvent-registration-file-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: These APIs allow you to create hooks. When triggered, a hook sends a request to your service to get updated data related to the related Cvent object. For more information on using hooks, see the [gett
  name: Cvent Registration Hooks API
  slug: cvent-registration-hooks-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'RegLink APIs allow you to exchange data with Cvent Passkey events and hotel reservation-booking engines. Generally, there are four primary categories of functionality that RegLink APIs support: * **Sy'
  name: Cvent Registration Housing API
  slug: cvent-registration-housing-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: APIs for managing hotel-related operations.
  name: Cvent Registration Housing Hotels API
  slug: cvent-registration-housing-hotels-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: '* **Leads -** Leads include leads gathered by LeadCapture, Appointments, and Inbound Leads. Use this API to get information for the lead and how it was captured. * **Lead Qualification Question -** Cu'
  name: Cvent Registration Leads API
  slug: cvent-registration-leads-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: When planning an event, meeting request forms are customizable online questionnaires to capture information about the event and facilitate the approval of events. When a meeting request form is submit
  name: Cvent Registration Meeting Request API
  slug: cvent-registration-meeting-request-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Process forms automate data collection and notifications related to planning and executing events. Process form submissions are responses to a specific process form, providing data the form requests. '
  name: Cvent Registration Process Form API
  slug: cvent-registration-process-form-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Beta - All APIs are in Beta. Proposal Drafts are editable copies of proposals. This API allows you to edit proposal data privately before publishing.
  name: Cvent Registration Proposal Draft API
  slug: cvent-registration-proposal-draft-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP additional details APIs for managing past event references and other miscellaneous RFP operations.
  name: Cvent Registration RFP Additional Details API
  slug: cvent-registration-rfp-additional-details-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP (Request for Proposal) management APIs for core RFP operations including CRUD operations for base RFPs.
  name: Cvent Registration RFP Management API
  slug: cvent-registration-rfp-management-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: RFP requirements APIs for managing RFP-specific requirements including guest rooms, meeting rooms, custom questions, custom fields, and attachments (CRUD operations).
  name: Cvent Registration RFP Requirements API
  slug: cvent-registration-rfp-requirements-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Suppliers are the venues and service providers that receive and respond to RFPs. Use these APIs to manage supplier associations, view recipient history, and create award details.
  name: Cvent Registration RFP Suppliers API
  slug: cvent-registration-rfp-suppliers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Retrieves Check-In & Check-Out Signatures Of Attendees
  name: Cvent Registration Signatures API
  slug: cvent-registration-signatures-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: 'Transactions represent the financial exchanges that occur within your account. Use these APIs to retrieve and manage transaction data, including charges, refunds, and adjustments associated with your '
  name: Cvent Registration Transactions API
  slug: cvent-registration-transactions-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The travel account, or corporation that represents the demand-side of travel RFPs.
  name: Cvent Registration Travel Accounts API
  slug: cvent-registration-travel-accounts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Travel RFP APIs provide access to travel programs and proposals. A travel program represents a request for proposal (RFP) that defines the specific travel needs and requirements of a travel accoun
  name: Cvent Registration Travel RFPs API
  slug: cvent-registration-travel-rfps-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The Travel Supplier APIs provide access to Cvent data related to hotels, apartments, and other travel providers. This includes information related to properties, and sleeping rooms.
  name: Cvent Registration Travel Suppliers API
  slug: cvent-registration-travel-suppliers-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: The [SCIM](https://www.simplecloud.info/) standard allows for easier cross-domain identity management. This API allows you to manage your account users and SCIM groups (representing Cvent user roles).
  name: Cvent Registration User SCIM API
  slug: cvent-registration-user-scim-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Operations for managing account users and user groups, including creation, retrieval, update, and deletion. Use these endpoints to administer user access and roles within your account.
  name: Cvent Registration Users API
  slug: cvent-registration-users-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Manage meeting rooms for a venue, including creating and updating room details, configuring capacities and amenities, and associating images.
  name: Cvent Registration Venue Meeting Rooms API
  slug: cvent-registration-venue-meeting-rooms-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Manage venue profile details including type, contact information, address, and other venue properties.
  name: Cvent Registration Venue Profiles API
  slug: cvent-registration-venue-profiles-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Videos can be added to Cvent events with renditions at various resolutions, audio files, reactions tracks, and text tracks. Attendee viewership is tracked to get insight into durations, devices used a
  name: Cvent Registration Video API
  slug: cvent-registration-video-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: Webcasts are virtual or livestreaming components of your Cvent events. Use these APIs to integrate your virtual events from outside sources into your Cvent workflows, create and delete webcasts from w
  name: Cvent Registration Webcasts API
  slug: cvent-registration-webcasts-api
- baseURL: https://api-platform.cvent.com
  baseurl_source: declared
  description: OAuth 2.0 token issuance
  name: Cvent Registration O Auth API
  slug: cvent-registration-oauth-api
artifact_total: 81
asyncapis:
- description: ''
  name: Cvent Registration Webhooks
  slug: cvent-registration-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/agentic-access/cvent-registration-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-registration-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/security/cvent-registration-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cvent-registration-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/security/cvent-registration-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvent-registration-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/authentication/cvent-registration-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cvent-registration-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/scopes/cvent-registration-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/overlays/_index.yml
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/overlays/cvent-registration-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cvent-registration-public-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/wsdl/cvent-registration-soap-v200611.wsdl
  title: ''
  type: WSDL
  url: wsdl/cvent-registration-soap-v200611.wsdl
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/llms/cvent-registration-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cvent-registration-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/packages/cvent-registration-packages.yml
  title: ''
  type: Packages
  url: packages/cvent-registration-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/packages/cvent-registration-packages.yml
  title: ''
  type: SDKs
  url: packages/cvent-registration-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/conformance/cvent-registration-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cvent-registration-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/conformance/cvent-registration-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cvent-registration-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/errors/cvent-registration-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cvent-registration-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/lifecycle/cvent-registration-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-registration-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/lifecycle/cvent-registration-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cvent-registration-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/conventions/cvent-registration-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cvent-registration-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/changelog/cvent-registration-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cvent-registration-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/components/cvent-registration-components.yml
  title: ''
  type: Components
  url: components/cvent-registration-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/data-model/cvent-registration-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cvent-registration-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/asyncapi/cvent-registration-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cvent-registration-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/mcp/cvent-registration-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cvent-registration-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/security/cvent-registration-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cvent-registration-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/security/cvent-registration-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cvent-registration-vulnerability-disclosure.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/plans/cvent-registration-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cvent-registration-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/rate-limits/cvent-registration-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cvent-registration-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/finops/cvent-registration-finops.yml
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
- name: Cvent Registration Finops
  service_category: API
  slug: cvent-registration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-registration.png
layout: provider
modified: '2026-09-07'
name: Cvent Registration
nav: Providers
network: true
overview: 'Cvent Registration publishes 59 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 56 more. Tagged areas include Attendee Management, Attendees, Conferences, Event Management, and Event.


  The Cvent Registration catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cvent Registration''s developer surface includes authentication, API reference, support, pricing, engineering blog, changelog, documentation, and 41 more developer resources.'
plans:
- name: Cvent Registration Plans Pricing
  plan_count: 5
  slug: cvent-registration-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Cvent Registration Rate Limits
  slug: cvent-registration-rate-limits
scopes:
- name: Cvent Registration Scopes
  scope_count: 238
  slug: cvent-registration-scopes
  summary_line: 238 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 79.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.0
    catalog_earned_first_party: 24.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 71.4
    developer_ergonomics: 66.1
    discoverability: 51.9
    operational_transparency: 92.1
  previous_composite: 82.0
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/screenshots/cvent-registration-2026-06-20T175407.png
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
slug: cvent-registration
tags:
- Attendee Management
- Attendees
- Conferences
- Event Management
- Event
- Authentication
- On-Site Check-In
- Payments
- Registration
- REST API
- SCIM
- SDK
- SOAP
- Ticketing
- Webhook
website: https://www.cvent.com/en/event-management-software/online-registration-software
---
