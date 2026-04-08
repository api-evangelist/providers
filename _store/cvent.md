---
aid: cvent
url: https://raw.githubusercontent.com/api-evangelist/cvent/refs/heads/main/apis.yml
apis:
- aid: cvent:cvent
  name: Cvent
  tags:
  - Conferences
  - Events
  - Exhibitors
  - Meetings
  - Sessions
  humanURL: https://developers.cvent.com/
  properties:
  - url: https://developers.cvent.com/
    type: Documentation
  - url: properties/cvent-openapi.yml
    type: OpenAPI
  - url: https://developers.cvent.com/docs/rest-api/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/rest-api/reference/reference
    type: APIReference
  - url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
    type: GettingStarted
  - url: https://developers.cvent.com/docs/rest-api/explanation/concepts
    type: Concepts
  - url: https://developers.cvent.com/docs/rest-api/explanation/using-the-reference
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/guides/registration-guide
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/guides/managing-events-guide
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/guides/event-travel-guide
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/guides/user-management
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/guides/vevent-integration
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/migration-guide/benefits
    type: MigrationGuide
  - url: https://developers.cvent.com/docs/rest-api/changelog
    type: ChangeLog
  - url: https://developers.cvent.com/documentation#section/Getting-Started/Authentication
    type: Authentication
  - url: https://developers.cvent.com/docs/rest-api/guides/bulk-api-user-guide
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/guides/compliance-guide
    type: Guide
  description: Cvent is an event management and hospitality platform that helps organizations plan, promote, execute, and analyze in-person, virtual, and hybrid events. It provides tools for tasks such as attendee registration, website creation, email marketing, venue sourcing, budgeting, and on-site check-in, streamlining the entire event lifecycle.
- aid: cvent:webhooks
  name: Cvent Webhooks API
  tags:
  - Attendees
  - Events
  - Notifications
  - Sessions
  - Webhooks
  humanURL: https://developers.cvent.com/docs/webhooks/overview
  properties:
  - url: https://developers.cvent.com/docs/webhooks/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/webhooks/understanding-webhooks
    type: Guide
  - url: https://developers.cvent.com/docs/webhooks/tutorials/account-setup
    type: GettingStarted
  - url: https://developers.cvent.com/docs/webhooks/guides/event-setup
    type: Guide
  - url: https://developers.cvent.com/docs/webhooks/guides/manual-sync
    type: Guide
  - url: https://developers.cvent.com/docs/webhooks/technical-requirements
    type: TechnicalRequirements
  description: Cvent Webhooks notify external applications when actions occur in Cvent and send relevant data to a specified URL. Webhooks automatically push event, attendee, speaker, and meeting request data to your endpoints, enabling real-time integration with minimal development effort compared to polling REST APIs.
- aid: cvent:http-post
  name: Cvent HTTP POST Integration
  tags:
  - Authentication
  - Events
  - Identity
  - Registration
  humanURL: https://developers.cvent.com/docs/http-post/overview
  properties:
  - url: https://developers.cvent.com/docs/http-post/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/http-post/reference/endpoints
    type: APIReference
  - url: https://developers.cvent.com/docs/http-post/explanation/concepts
    type: Concepts
  description: The Cvent HTTP POST Integration provides a way to identify users at time of registration or authenticate account access using HTTP POST requests. It enables external systems to exchange data with Cvent during the registration workflow.
- aid: cvent:csn-api
  name: Cvent Supplier Network (CSN) API
  tags:
  - Hospitality
  - Proposals
  - RFP
  - Suppliers
  - Venues
  humanURL: https://developers.cvent.com/docs/legacy-api/csn/overview
  properties:
  - url: https://developers.cvent.com/docs/legacy-api/csn/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/legacy-api/csn/planner-guide/overview
    type: Guide
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/authentication
    type: Authentication
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/scopes
    type: Scopes
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/creating-proposal
    type: Guide
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/push-notification-system
    type: Guide
  - url: https://developers.cvent.com/docs/legacy-api/csn/planner-guide/authentication
    type: Authentication
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/rfp-response
    type: Guide
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/submitting-responses
    type: Guide
  - url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/updating-proposal
    type: Guide
  description: The Cvent Supplier Network (CSN) API provides integration with a database of 280,000+ hotels, suppliers, and destinations worldwide. It enables planners to search and compare venues, manage RFPs, and allows suppliers to create and update proposals programmatically using a push-pull workflow.
- aid: cvent:passkey-reglink
  name: Cvent Passkey RegLink API
  tags:
  - Accommodations
  - Hotels
  - Registration
  - Reservations
  humanURL: https://developers.cvent.com/docs/passkey/REST/overview
  properties:
  - url: https://developers.cvent.com/docs/passkey/REST/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/passkey/REST/getting-started
    type: GettingStarted
  - url: https://developers.cvent.com/docs/passkey/REST/callbacks
    type: Callbacks
  - url: https://developers.cvent.com/docs/passkey/REST/faq
    type: FAQ
  - url: https://developers.cvent.com/docs/legacy-api/reglink/overview
    type: Documentation
  description: The Cvent Passkey RegLink API provides functional integration with external applications such as registration systems. It enables third-party systems to interact and exchange data with Passkey event and hotel reservation-booking engines, supporting different integration levels from basic URL-based to advanced RESTful JSON-based APIs.
- aid: cvent:soap-api
  name: Cvent SOAP API (Legacy)
  tags:
  - Contacts
  - Deprecated
  - Events
  - Legacy
  - Registration
  humanURL: https://developers.cvent.com/docs/legacy-api/soap-api/overview
  properties:
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/framework
    type: Guide
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/api-management
    type: APIManagement
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/call-definitions/overview
    type: APIReference
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/object-definitions/overview
    type: APIReference
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/sample-code
    type: SampleCode
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/changelog
    type: ChangeLog
  - url: https://developers.cvent.com/docs/legacy-api/soap-api/soap-certificates
    type: Guide
  - url: https://developers.cvent.com/docs/rest-api/migration-guide/benefits
    type: Migration Guide
  - url: https://developers.cvent.com/docs/rest-api/migration-guide/calls-and-methods
    type: Migration Guide
  description: The Cvent SOAP API is the original legacy API for pushing and pulling data between Cvent and internal systems. It supports contact management, event management, custom fields, address book operations, and metadata retrieval. This API is being sunset and developers are encouraged to migrate to the REST API.
- aid: cvent:custom-widgets
  name: Cvent Custom Widgets API
  tags:
  - Customization
  - Embedding
  - Registration
  - Widgets
  humanURL: https://developers.cvent.com/docs/custom-widgets/overview
  properties:
  - url: https://developers.cvent.com/docs/custom-widgets/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/custom-widgets/publishing
    type: Guide
  - url: https://developers.cvent.com/docs/custom-widgets/required-assets/custom-widget-element
    type: Guide
  - url: https://developers.cvent.com/docs/custom-widgets/required-assets/custom-widget-configuration
    type: Guide
  - url: https://developers.cvent.com/docs/custom-widgets/examples/featured-session-widget
    type: Guide
  - url: https://developers.cvent.com/docs/custom-widgets/sdk/navigation
    type: Guide
  - url: https://github.com/cvent/custom-widgets-labs
    type: GitHubRepository
  description: The Cvent Custom Widgets API allows developers to build custom interactive widgets for Cvent Event Registration pages. It provides an SDK for creating widget elements, configuration files, and navigation methods, enabling organizations to customize how attendees interact with event registration experiences.
- aid: cvent:sso
  name: Cvent Single Sign-On (SSO) Integration
  tags:
  - Authentication
  - Identity
  - SAML
  - SSO
  humanURL: https://developers.cvent.com/docs/sso/overview
  properties:
  - url: https://developers.cvent.com/docs/sso/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/sso/explanation/concepts
    type: Concepts
  - url: https://developers.cvent.com/docs/sso/guides/access-portal
    type: Guide
  - url: https://developers.cvent.com/docs/sso/guides/planner-login
    type: Guide
  - url: https://developers.cvent.com/docs/sso/guides/event-attendee-hub
    type: Guide
  - url: https://developers.cvent.com/docs/sso/guides/events-plus
    type: Guide
  - url: https://developers.cvent.com/docs/sso/guides/portals
    type: Guide
  description: Cvent Single Sign-On (SSO) enables identity provider integration for authenticating users across Cvent products. It supports both SAML and OpenID Connect protocols for planner login, access portals, event registrant and attendee hub, Events+, and portal applications.
- aid: cvent:white-label
  name: Cvent White Label API
  tags:
  - Branding
  - RFP
  - White Label
  - Widgets
  humanURL: https://developers.cvent.com/docs/white-label/overview
  properties:
  - url: https://developers.cvent.com/docs/white-label/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/white-label/widget-api-deployment
    type: Guide
  - url: https://developers.cvent.com/docs/white-label/custom-theme-branding
    type: Guide
  - url: https://developers.cvent.com/docs/white-label/analytics
    type: Guide
  description: The Cvent White Label API enables venues and suppliers to embed Cvent RFP functionality directly into their own websites with custom branding. It provides widget API deployment, custom theming and branding configuration, and analytics capabilities for tracking engagement with embedded RFP forms.
- aid: cvent:dfi
  name: Cvent Dynamic Field Integration (DFI)
  tags:
  - CRM
  - Data Sync
  - Fields
  - Integration
  humanURL: https://developers.cvent.com/docs/dfi/overview
  properties:
  - url: https://developers.cvent.com/docs/dfi/overview
    type: Documentation
  description: Cvent Dynamic Field Integration (DFI) enables organizations to integrate their CRM with Cvent data by configuring field mappings between systems. It supports SFTP-based data exchange, PGP encryption, and dynamic field sets for populating meeting request forms with external data.
- aid: cvent:salesforce-app
  name: Cvent Salesforce App
  tags:
  - CRM
  - Events
  - Integration
  - Salesforce
  humanURL: https://developers.cvent.com/docs/cvent-salesforce-app/overview
  properties:
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/app-installation
    type: GettingStarted
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/salesforce-oauth
    type: Authentication
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/connect-to-cvent
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/cvent-side-setup
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/general-data-structure
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/salesforce-as-an-external-data-source
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/attendee-activities
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/customizing-page-layouts
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/retrieve-cvent-custom-fields
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/reporting
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/event-visibility
    type: Guide
  - url: https://developers.cvent.com/docs/cvent-salesforce-app/release-notes
    type: Change Log
  description: The Cvent Salesforce App integrates Cvent event data with Salesforce CRM, enabling users to view Cvent events from Salesforce, invite and register contacts and leads, and sync attendee data bidirectionally between the two platforms. It supports OAuth-based authentication, custom field mapping, reporting, and automation workflows.
- aid: cvent:badgekit-api
  name: Cvent BadgeKit API (Legacy)
  tags:
  - Badges
  - Events
  - Lead Capture
  - Legacy
  - Scanning
  humanURL: https://developers.cvent.com/docs/legacy-api/badgekit/overview
  properties:
  - url: https://developers.cvent.com/docs/legacy-api/badgekit/overview
    type: Documentation
  - url: https://developers.cvent.com/docs/legacy-api/badgekit/Authentication
    type: Authentication
  - url: https://developers.cvent.com/docs/legacy-api/badgekit/Setting_Up_Your_Scanning_Software
    type: GettingStarted
  - url: https://developers.cvent.com/docs/legacy-api/badgekit/Attendees_Object
    type: APIReference
  description: The Cvent BadgeKit API allows exhibitors to integrate their own custom lead scanning software at events. It provides access to standard and custom attendee fields shared by event planners, enabling exhibitors to capture and manage lead data from badge scans during in-person events.
- aid: cvent:jifflenow-api
  name: Cvent Jifflenow API (Legacy)
  tags:
  - Events
  - Legacy
  - Meetings
  - Scheduling
  - Users
  humanURL: https://developers.cvent.com/docs/legacy-api/jifflenow-api/introduction
  properties:
  - url: https://developers.cvent.com/docs/legacy-api/jifflenow-api/introduction
    type: Documentation
  - url: https://developers.cvent.com/docs/legacy-api/jifflenow-api/getting-started
    type: GettingStarted
  - url: https://developers.cvent.com/docs/legacy-api/jifflenow-api/user/users-list
    type: APIReference
  description: The Cvent Jifflenow API provides programmatic access to Jifflenow meeting management functionality, including user management, event creation and updates, meeting scheduling, session management, and calendar blocking. It supports integration with external systems for coordinating one-on-one meetings at events and conferences.
name: Cvent
tags:
- Attendee Management
- Conferences
- Event Management
- Events
- Hospitality
- Meetings
- Registration
- Venue Management
type: Index
image: https://www.cvent.com/themes/custom/cvent_theme/cvent-logo.svg
access: 3rd-Party
common:
- url: https://developers.cvent.com/documentation
  name: API Reference
  type: Documentation
  description: 'null'
- url: https://developers.cvent.com/docs/rest-api/tutorials/inviting-your-developers
  name: Developer Documentation
  type: Tutorials
  description: 'null'
- url: https://developers.cvent.com/docs/rest-api/guides/rest-guides
  name: Developer Documentation
  type: Guide
  description: 'null'
- url: https://developers.cvent.com/docs/rest-api/reference/api-standards
  name: Developer Documentation
  type: Standards
  description: 'null'
- url: https://developers.cvent.com/docs/rest-api/changelog
  name: Developer Documentation
  type: ChangeLog
  description: 'null'
- url: https://developers.cvent.com/docs/custom-widgets/overview
  name: Developer Documentation
  type: Widgets
  description: 'null'
- url: https://developers.cvent.com/docs/white-label/overview
  name: Developer Documentation
  type: WhiteLabel
  description: 'null'
- url: https://developers.cvent.com/docs/sso/overview
  name: Developer Documentation
  type: SSO
  description: 'null'
- url: https://developers.cvent.com/docs/webhooks/overview
  name: Developer Documentation
  type: Webhooks
  description: 'null'
- url: https://support.cvent.com/s/communityarticle/What-can-Cvent-s-API-do
  name: What can Cvents API do?
  type: Support
  description: 'null'
- url: https://www.cvent.com/
  name: Cvent | Event Platform for In-person, Virtual, and Hybrid Events & Webinars
  type: Website
  description: 'null'
- url: https://www.cvent.com/en/event-management-software/cvent-integrations
  name: Meeting & Events Tools Integration With Cvent
  type: Integrations
  description: 'null'
- url: https://www.cvent.com/en/blog
  name: Meetings, Hospitality, and Events Industry Tips | Cvent Blog
  type: Blog
  description: 'null'
- url: https://www.cvent.com/
  name: Cvent | Event Platform for In-person, Virtual, and Hybrid Events & Webinars
  type: Website
  description: 'null'
- url: https://www.cvent.com/en/event-management-software/cvent-pricing
  name: Cvent Pricing | Request a Quote
  type: Pricing
  description: 'null'
- url: https://careers.cvent.com/
  name: Cvent Careers
  type: Careers
  description: 'null'
- url: https://www.cvent.com/en/become-partner
  name: Partner Program - Join the Cvent Partner Program | Cvent
  type: Partners
  description: 'null'
- url: https://www.cvent.com/en/blog
  name: Meetings, Hospitality, and Events Industry Tips | Cvent Blog
  type: Blog
  description: 'null'
- url: https://www.cvent.com/en/case-studies
  name: Cvent Customer Success Stories & Reviews
  type: CaseStudies
  description: 'null'
- url: https://web.cvent.com/eventsplus/0a191bdc-46ea-47bb-921a-69d252ad21e3/eventcalendars/2402d010-8588-4fba-a3fc-e684ce562ab7
  name: Upcoming Events
  type: Events
  description: 'null'
- url: https://web.cvent.com/eventsplus/0a191bdc-46ea-47bb-921a-69d252ad21e3/eventcalendars/2402d010-8588-4fba-a3fc-e684ce562ab7?field_event_type_target_id%5B46%5D=46&cvt_cal_filters=%5B%7B%22type%22%3A%22checkbox%22%2C%22field%22%3A%22f92543ff-cabd-454e-b582-65df803329ac%22%2C%22values%22%3A%5B%22Webinar%22%5D%2C%22cventFieldType%22%3A%2241%22%7D%5D
  name: Upcoming Events
  type: Webinars
  description: 'null'
- url: https://community.cvent.com/home
  name: Cvent Community Home - Cvent Community
  type: Community
  description: 'null'
- url: https://developers.cvent.com/
  name: Overview
  type: Portal
  description: 'null'
- url: https://developers.cvent.com/documentation
  name: API Reference
  type: Documentation
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started
  name: API Reference
  type: GettingStarted
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started/Authentication
  name: API Reference
  type: Authentication
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started/Rate-Limits
  name: API Reference
  type: RateLimits
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started/Pagination
  name: API Reference
  type: Pagination
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started/Filtering
  name: API Reference
  type: Filtering
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started/Versioning
  name: API Reference
  type: ChangeLog
  description: 'null'
- url: https://developers.cvent.com/documentation#section/Getting-Started/Standards
  name: API Reference
  type: Standards
  description: 'null'
- url: https://developers.cvent.com/docs/webhooks/overview
  name: Developer Documentation
  type: Webhooks
  description: 'null'
- url: https://developers.cvent.com/docs/webhooks/overview#guides
  name: Developer Documentation
  type: Guide
  description: 'null'
- url: https://developers.cvent.com/docs/sso/overview
  name: Developer Documentation
  type: SSO
  description: 'null'
- url: https://developers.cvent.com/docs/white-label/overview
  name: Developer Documentation
  type: WhiteLabel
  description: 'null'
- url: https://www.cvent.com/en/security
  name: Event Data Security for Customers | Cvent
  type: Security
  description: 'null'
- url: https://www.cvent.com/en/academy
  name: Cvent Academy | Cvent
  type: Training
  description: 'null'
- url: https://app.cvent.com/subscribers/Login.aspx?ReturnUrl=%2fsubscribers%2fdefault.aspx
  name: Log In
  type: Login
  description: 'null'
- url: https://www.cvent.com/en/request-demo
  name: Cvent Demo | Cvent
  type: RequestDemo
  description: 'null'
created: '2025-11-19'
modified: '2026-04-07'
position: Consumer
description: Cvent is a leading meetings, events, and hospitality technology provider with over 4,800 employees and 21,000+ customers worldwide. The platform offers event management software, venue sourcing, attendee engagement tools, and event marketing solutions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

