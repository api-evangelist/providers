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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 189
  human_in_the_loop: 0
  name: Cvent Event Cloud Agentic Access
  operation_count: 383
  slug: cvent-event-cloud-agentic-access
  summary_line: 383 operations · 189 acting
api_count: 42
apis:
- description: RESTful API for managing events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub data. Uses OAuth 2.0 client credentials. Authorization code flo
  name: Cvent Platform REST API (Event Cloud)
  slug: rest-api
- description: Event registrations and attendees
  name: Cvent Event Cloud Attendees API
  slug: cvent-event-cloud-attendees-api
- description: Contact/address book
  name: Cvent Event Cloud Contacts API
  slug: cvent-event-cloud-contacts-api
- description: Event lifecycle and configuration
  name: Cvent Event Cloud Events API
  slug: cvent-event-cloud-events-api
- description: Agenda sessions
  name: Cvent Event Cloud Sessions API
  slug: cvent-event-cloud-sessions-api
- description: 'An appointment is a meeting scheduled between two or more parties. These APIs allow you to get information about your Cvent Appointments: appointment attendees, their interests, and availabilities. * '
  name: Cvent Event Cloud Appointments API
  slug: cvent-event-cloud-appointments-api
- description: The Attendee Activities API gives valuable insight into your customer's experience at your Cvent event. Now, you can get a fuller picture of your customer's journey, including onsite activities, offsi
  name: Cvent Event Cloud Attendee Activities API
  slug: cvent-event-cloud-attendee-activities-api
- description: 'The Attendee Insights feature provides valuable information about your event attendees. It assists planners, marketers, and exhibitors in targeting customers effectively, thereby enhancing engagement '
  name: Cvent Event Cloud Attendee Insights API
  slug: cvent-event-cloud-attendee-insights-api
- description: These APIs retrieve and manage attendee messages—communications exchanged between attendees within channels. Channels are virtual spaces created for one-on-one or group conversations, allowing attende
  name: Cvent Event Cloud Attendee Messages API
  slug: cvent-event-cloud-attendee-messages-api
- description: Audience Segments allow planners to segment their attendees into groups and better manage the attendee experience based on their defined segments. Audience Segments APIs will enable you to get, create
  name: Cvent Event Cloud Audience Segments API
  slug: cvent-event-cloud-audience-segments-api
- description: Endpoints for obtaining, refreshing, and validating OAuth2 access tokens.
  name: Cvent Event Cloud Authentication API
  slug: cvent-event-cloud-authentication-api
- description: Badge print jobs can be scheduled to a printer pool, so a printer in the printer pool can consume the job and print the badge.
  name: Cvent Event Cloud Badge Print Job API
  slug: cvent-event-cloud-badge-print-job-api
- description: Badge printer pools are set up from Cvent UI. You can use this API to retrieve badge printer pools.
  name: Cvent Event Cloud Badge Printer Pools API
  slug: cvent-event-cloud-badge-printer-pools-api
- description: Budget is an event feature used to organize spending and track [allocations](https://support.cvent.com/s/communityarticle/Setting-Up-Budget-Allocations). Use this API to view budget items, cards and c
  name: Cvent Event Cloud Budget API
  slug: cvent-event-cloud-budget-api
- description: 'The Bulk API provides a simple interface to upload large amounts of data into Cvent. The API processes the uploaded data asynchronously making API calls on behalf of the caller. Consumers of the bulk '
  name: Cvent Event Cloud Bulk API
  slug: cvent-event-cloud-bulk-api
- description: Planners use eMarketing campaigns to contact an audience, such as newsletters, press releases, or product updates. Campaign emails are used as newsletters, promotions, advertisements, or marketing mes
  name: Cvent Event Cloud Campaigns API
  slug: cvent-event-cloud-campaigns-api
- description: '**Card Tokenization**: Tokenization is the process Cvent uses to collect sensitive card details and personally identifiable information (PII), directly from your customers in a secure manner. This gua'
  name: Cvent Event Cloud Card Tokens API
  slug: cvent-event-cloud-card-tokens-api
- description: These API's provide compliance support for regulated industries. **Communication Compliance** lets you view communication activities across your account. Various written forms of communication are cap
  name: Cvent Event Cloud Compliance API
  slug: cvent-event-cloud-compliance-api
- description: Custom Fields are created by event planners to track important information about specific objects like events, contacts, or sessions. Use these APIs to view, create, and update custom fields in your a
  name: Cvent Event Cloud Custom Fields API
  slug: cvent-event-cloud-custom-fields-api
- description: Discounts provide a way to reduce the cost of event registration items. Use these APIs to manage event discounts, including creating, updating, and linking discounts to agenda items.
  name: Cvent Event Cloud Discounts API
  slug: cvent-event-cloud-discounts-api
- description: Event planners use emails to invite registrants, market their events and request feedback from attendees. Use these APIs to get historical data about your emails and see relevant details like the type
  name: Cvent Event Cloud Emails API
  slug: cvent-event-cloud-emails-api
- description: Event Credits reward attendees for participating in your events. Planners can award credits for the entire event, specific sessions, or both. You can also award credits after attendees complete survey
  name: Cvent Event Cloud Event Credits API
  slug: cvent-event-cloud-event-credits-api
- description: EventFeatures related APIs
  name: Cvent Event Cloud Event Features API
  slug: cvent-event-cloud-event-features-api
- description: Event roles are event specific permission sets for your organization's users. Use these APIs to retrieve, create, update, and delete event role assignments to your organization's users.
  name: Cvent Event Cloud Event Role API
  slug: cvent-event-cloud-event-role-api
- description: Event travel lets planners capture air & hotel requests from attendees and track air actuals, hotel reservations and alternate travel answers at your event. Use these endpoints to retrieve your air, h
  name: Cvent Event Cloud Event Travel API
  slug: cvent-event-cloud-event-travel-api
- description: An Events+ Hub persists basic information needed to assign an owner and optionally customize the public presentation.
  name: Cvent Event Cloud Events+ Hub API
  slug: cvent-event-cloud-events-hub-api
- description: '* **Exhibitor -** An exhibitor is an organization that is sponsoring or exhibiting at your event. This API allows you to get information about your exhibitors. * **Registration Pack -** Registration P'
  name: Cvent Event Cloud Exhibitor API
  slug: cvent-event-cloud-exhibitor-api
- description: Exhibitor Content operations for an exhibitor. This API allows you to upload & get exhibitor content data such as files, weblinks.
  name: Cvent Event Cloud Exhibitor Content API
  slug: cvent-event-cloud-exhibitor-content-api
- description: '* **Exhibitor Admin -** Exhibitor Admins are administrators that have access to the exhibitor portal. In the portal, they are able to complete pre-event tasks, manage their team, purchase LeadCapture '
  name: Cvent Event Cloud Exhibitor Team API
  slug: cvent-event-cloud-exhibitor-team-api
- description: 'Allows you to upload files and get file location using the file ID. File ID can be used with other APIs to associate the file to an entity. For example: * <a href="#operation/addSessionDoc">Add Docume'
  name: Cvent Event Cloud File API
  slug: cvent-event-cloud-file-api
- description: These APIs allow you to create hooks. When triggered, a hook sends a request to your service to get updated data related to the related Cvent object. For more information on using hooks, see the [gett
  name: Cvent Event Cloud Hooks API
  slug: cvent-event-cloud-hooks-api
- description: '* **Leads -** Leads include leads gathered by LeadCapture, Appointments, and Inbound Leads. Use this API to get information for the lead and how it was captured. * **Lead Qualification Question -** Cu'
  name: Cvent Event Cloud Leads API
  slug: cvent-event-cloud-leads-api
- description: 'Process forms automate data collection and notifications related to planning and executing events. Process form submissions are responses to a specific process form, providing data the form requests. '
  name: Cvent Event Cloud Process Form API
  slug: cvent-event-cloud-process-form-api
- description: Seating lets you plan seating at your events by configuring tables and assigning seats to your attendees. The seating APIs allow you to create, update, and delete seating, tables, seats, and seating a
  name: Cvent Event Cloud Seating API
  slug: cvent-event-cloud-seating-api
- description: Retrieves Check-In & Check-Out Signatures Of Attendees
  name: Cvent Event Cloud Signatures API
  slug: cvent-event-cloud-signatures-api
- description: Speakers are individuals presenting at your event's session(s). Use Speaker APIs to read existing speaker data, create new speakers or update existing speakers in your events.
  name: Cvent Event Cloud Speakers API
  slug: cvent-event-cloud-speakers-api
- description: Surveys are lists of questions deployed to your contacts. Surveys can be standalone or can be associated to a Cvent event. Use these APIs to search for surveys and retrieve the associated questions an
  name: Cvent Event Cloud Surveys API
  slug: cvent-event-cloud-surveys-api
- description: Use these APIs view your REST API usage and limits metrics. For more details on limits - [Rate Limits](#section/Getting-Started/Rate-Limits)
  name: Cvent Event Cloud Usage API
  slug: cvent-event-cloud-usage-api
- description: The [SCIM](https://www.simplecloud.info/) standard allows for easier cross-domain identity management. This API allows you to manage your account users and SCIM groups (representing Cvent user roles).
  name: Cvent Event Cloud User SCIM API
  slug: cvent-event-cloud-user-scim-api
- description: Operations for managing account users and user groups, including creation, retrieval, update, and deletion. Use these endpoints to administer user access and roles within your account.
  name: Cvent Event Cloud Users API
  slug: cvent-event-cloud-users-api
- description: Videos can be added to Cvent events with renditions at various resolutions, audio files, reactions tracks, and text tracks. Attendee viewership is tracked to get insight into durations, devices used a
  name: Cvent Event Cloud Video API
  slug: cvent-event-cloud-video-api
- description: Webcasts are virtual or livestreaming components of your Cvent events. Use these APIs to integrate your virtual events from outside sources into your Cvent workflows, create and delete webcasts from w
  name: Cvent Event Cloud Webcasts API
  slug: cvent-event-cloud-webcasts-api
arazzos:
- description: Created from /Users/mkothari/git-cvent-public/rest-sdks/.speakeasy/temp/overlay_RizoNFXzgC.yaml
  name: Test Suite
  slug: cvent-event-cloud-sdk-tests.arazzo
artifact_total: 95
asyncapis:
- description: ''
  name: Cvent Event Cloud Webhooks
  slug: cvent-event-cloud-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cvent REST APIs — Event Cloud Appointments API
  slug: open-cvent-event-cloud-appointments-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendee Activities API
  slug: open-cvent-event-cloud-attendee-activities-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendee Insights API
  slug: open-cvent-event-cloud-attendee-insights-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendee Messages API
  slug: open-cvent-event-cloud-attendee-messages-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Attendees API
  slug: open-cvent-event-cloud-attendees-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Audience Segments API
  slug: open-cvent-event-cloud-audience-segments-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Authentication API
  slug: open-cvent-event-cloud-authentication-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Badge Print Job API
  slug: open-cvent-event-cloud-badge-print-job-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Badge Printer Pools API
  slug: open-cvent-event-cloud-badge-printer-pools-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Budget API
  slug: open-cvent-event-cloud-budget-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Bulk API
  slug: open-cvent-event-cloud-bulk-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Campaigns API
  slug: open-cvent-event-cloud-campaigns-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Card Tokens API
  slug: open-cvent-event-cloud-card-tokens-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Compliance API
  slug: open-cvent-event-cloud-compliance-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Contacts API
  slug: open-cvent-event-cloud-contacts-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Custom Fields API
  slug: open-cvent-event-cloud-custom-fields-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Discounts API
  slug: open-cvent-event-cloud-discounts-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Emails API
  slug: open-cvent-event-cloud-emails-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Credits API
  slug: open-cvent-event-cloud-event-credits-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Features API
  slug: open-cvent-event-cloud-event-features-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Role API
  slug: open-cvent-event-cloud-event-role-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Event Travel API
  slug: open-cvent-event-cloud-event-travel-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Events API
  slug: open-cvent-event-cloud-events-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Events+ Hub API
  slug: open-cvent-event-cloud-events-hub-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Exhibitor API
  slug: open-cvent-event-cloud-exhibitor-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Exhibitor Content API
  slug: open-cvent-event-cloud-exhibitor-content-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Exhibitor Team API
  slug: open-cvent-event-cloud-exhibitor-team-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud File API
  slug: open-cvent-event-cloud-file-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Hooks API
  slug: open-cvent-event-cloud-hooks-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Leads API
  slug: open-cvent-event-cloud-leads-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Process Form API
  slug: open-cvent-event-cloud-process-form-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Seating API
  slug: open-cvent-event-cloud-seating-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Sessions API
  slug: open-cvent-event-cloud-sessions-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Signatures API
  slug: open-cvent-event-cloud-signatures-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Speakers API
  slug: open-cvent-event-cloud-speakers-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Surveys API
  slug: open-cvent-event-cloud-surveys-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Usage API
  slug: open-cvent-event-cloud-usage-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud User SCIM API
  slug: open-cvent-event-cloud-user-scim-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Users API
  slug: open-cvent-event-cloud-users-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Video API
  slug: open-cvent-event-cloud-video-api
- collection_type: open
  name: Cvent REST APIs — Event Cloud Webcasts API
  slug: open-cvent-event-cloud-webcasts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-event-cloud-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cvent-event-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-event-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-event-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-event-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cvent
- group: company
  title: ''
  type: Website
  url: https://www.cvent.com/en/event-management-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/rest-api/overview
- group: other
  title: ''
  type: AttendeeHub
  url: https://www.cvent.com/en/attendee-hub
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/event-management-software/cvent-pricing
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
  type: TermsOfService
  url: https://www.cvent.com/en/cvent-general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.cvent.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cvent.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cvent-event-cloud-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
- group: docs
  title: ''
  type: Guides
  url: https://developers.cvent.com/docs/rest-api/guides/rest-guides
- group: start
  title: ''
  type: SignUp
  url: https://developers.cvent.com/applications
- group: auth
  title: ''
  type: TrustCenterURL
  url: https://trust.cvent.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cvent/rest-sdks
- group: build
  title: ''
  type: Packages
  url: packages/cvent-event-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cvent-event-cloud-packages.yml
- group: docs
  title: ''
  type: SDKDocumentation
  url: https://developers.cvent.com/docs/rest-api/sdks
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cvent-event-cloud-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cvent-event-cloud-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cvent-event-cloud-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cvent-event-cloud-overlays.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cvent-event-cloud-sdk-tests.arazzo.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cvent-event-cloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cvent-event-cloud-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cvent-event-cloud-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cvent-event-cloud-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cvent-event-cloud-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cvent-event-cloud-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cvent-event-cloud-changelog.yml
- group: operate
  title: ''
  type: ChangeLogURL
  url: https://developers.cvent.com/docs/rest-api/changelog
- group: design
  title: ''
  type: Components
  url: components/cvent-event-cloud-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cvent-event-cloud-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cvent-event-cloud-webhooks.yml
- group: docs
  title: ''
  type: WebhooksDocumentation
  url: https://developers.cvent.com/docs/webhooks/overview
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cvent-event-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cvent-event-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cvent-event-cloud-finops.yml
created: '2024-01-01'
description: 'Cvent Event Cloud is the event management product line of the Cvent Platform. It supports the full event lifecycle: event creation, registration, marketing, agenda and session management, mobile event apps, onsite check-in, virtual and hybrid event delivery via the Attendee Hub, surveys, and analytics. Cvent publishes its own OpenAPI specification in public git at github.com/cvent/rest-sdks (cvent-public-spec/openapi.yaml) — 346 paths, 458 operations, 1,302 schemas — and generates its first-party TypeScript, .NET and Java SDKs from it with Speakeasy, applying five published OpenAPI Overlay 1.0.0 documents in the process. Access is OAuth 2.0, client credentials for server-to-server and authorization code for planner administrators, with the token endpoint at api-platform.cvent.com/ea/oauth2/token and 235 declared scopes. Regional bases split North America (api-platform.cvent.com/ea) from Europe (api-platform-eur.cvent.com/ea) with no cross-region read. Cvent also runs a live
  remote MCP server at mcp.cvent.com/mcp secured with OAuth 2.1 and PKCE, publishes a dated biweekly changelog, a 40-message webhook catalogue, SCIM 2.0 user provisioning, and a Custom Widgets browser SDK for embedding components in Cvent-hosted event pages.'
finops:
- name: Cvent Event Cloud Finops
  service_category: API
  slug: cvent-event-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-event-cloud.png
layout: provider
mcp_servers:
- description: ''
  name: cvent-event-cloud-mcp.yml
  slug: cvent-event-cloud-mcpyml
modified: '2026-08-13'
name: Cvent Event Cloud
nav: Providers
network: true
overview: 'Cvent Event Cloud publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Contacts API, Events API, and 38 more. Tagged areas include Attendee Hub, Attendees, Bulk, Contacts, and Event Cloud.


  The Cvent Event Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cvent Event Cloud''s developer surface includes authentication, API reference, pricing, support, engineering blog, documentation, getting-started guide, and 41 more developer resources.'
plans:
- name: Cvent Event Cloud Plans Pricing
  plan_count: 3
  slug: cvent-event-cloud-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Cvent Event Cloud Rate Limits
  slug: cvent-event-cloud-rate-limits
scopes:
- name: Cvent Event Cloud Scopes
  scope_count: 235
  slug: cvent-event-cloud-scopes
  summary_line: 235 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 71.9
  delta: 6.3
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 16.7
    contract_quality: 74.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 81.6
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/screenshots/cvent-event-cloud-2026-06-20T175402.png
security:
- kind: authentication
  name: Cvent Event Cloud Authentication
  slug: cvent-event-cloud-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cvent Event Cloud Domain Security
  slug: cvent-event-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cvent Event Cloud Trust Center
  slug: cvent-event-cloud-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: cvent-event-cloud
tags:
- Attendee Hub
- Attendees
- Bulk
- Contacts
- Event Cloud
- Event Management
- Event Marketing
- Events
- Exhibitors
- Hybrid Events
- MCP
- OAuth 2.0
- Onsite
- OpenAPI
- Overlay
- Registration
- REST
- SCIM
- SDKs
- Sessions
- Speakers
- Surveys
- Virtual Events
- Webcasts
- Webhooks
website: https://www.cvent.com/en/event-management-software
---
