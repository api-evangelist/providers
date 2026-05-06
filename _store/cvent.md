---
aid: cvent
name: Cvent
x-type: company
description: Cvent is a leading meetings, events, and hospitality technology provider with over 4,800 employees and 22,000+ customers worldwide. The Cvent platform spans Event Cloud (event management, registration, mobile event apps, virtual and hybrid events, Attendee Hub, surveys, Diagramming, and analytics) and Hospitality Cloud (Cvent Supplier Network, Passkey, Venue Sourcing, and Sales & Catering). Programmatic access is delivered through the unified Cvent Platform REST API (api-platform.cvent.com) using OAuth 2.0 client credentials, with legacy SOAP, BadgeKit, Jifflenow, and CSN APIs documented for historical integrations. The developer portal at developers.cvent.com hosts API references, guides, OpenAPI downloads, webhooks, SSO, custom widgets, white-label, and integration documentation.
url: https://raw.githubusercontent.com/api-evangelist/cvent/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2025-11-19'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Attendee Hub
  - Attendee Management
  - Conferences
  - Diagramming
  - Event Management
  - Event Marketing
  - Events
  - Exhibitors
  - Hospitality
  - Hospitality Cloud
  - Hybrid Events
  - Meetings
  - OAuth 2.0
  - Passkey
  - Registration
  - REST API
  - SOAP API
  - SSO
  - Supplier Network
  - Surveys
  - Venue Management
  - Venue Sourcing
  - Virtual Events
  - Webhooks
  - White Label
apis:
  - aid: cvent:rest-api
    name: Cvent REST API
    description: The unified Cvent Platform REST API providing programmatic access to events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub resources. OAuth 2.0 client credentials with the token endpoint at api-platform.cvent.com/ea/oauth2/token.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/rest-api/overview
    baseURL: https://api-platform.cvent.com
    tags:
      - Attendees
      - Contacts
      - Events
      - OAuth 2.0
      - Registration
      - REST
      - Sessions
      - Surveys
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/rest-api/overview
      - type: APIReference
        url: https://developers.cvent.com/docs/rest-api/reference/reference
      - type: GettingStarted
        url: https://developers.cvent.com/docs/rest-api/tutorials/developer-quickstart
      - type: Concepts
        url: https://developers.cvent.com/docs/rest-api/explanation/concepts
      - type: ChangeLog
        url: https://developers.cvent.com/docs/rest-api/changelog
      - type: MigrationGuide
        url: https://developers.cvent.com/docs/rest-api/migration-guide/benefits
  - aid: cvent:webhooks
    name: Cvent Webhooks API
    description: Cvent Webhooks notify external applications when actions occur in Cvent and send relevant data to a specified URL, automatically pushing event, attendee, speaker, and meeting request data to subscriber endpoints for real-time integration.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/webhooks/overview
    tags:
      - Attendees
      - Events
      - Notifications
      - Sessions
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/webhooks/overview
      - type: Guide
        url: https://developers.cvent.com/docs/webhooks/understanding-webhooks
      - type: GettingStarted
        url: https://developers.cvent.com/docs/webhooks/tutorials/account-setup
      - type: TechnicalRequirements
        url: https://developers.cvent.com/docs/webhooks/technical-requirements
  - aid: cvent:csn-api
    name: Cvent Supplier Network (CSN) API
    description: The Cvent Supplier Network (CSN) API provides integration with a database of 280,000+ hotels, suppliers, and destinations worldwide. Planners search and compare venues and manage RFPs; suppliers create and update proposals via a push-pull workflow.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/legacy-api/csn/overview
    tags:
      - Hospitality
      - Proposals
      - RFP
      - Suppliers
      - Venues
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/legacy-api/csn/overview
      - type: PlannerGuide
        url: https://developers.cvent.com/docs/legacy-api/csn/planner-guide/overview
      - type: SupplierGuide
        url: https://developers.cvent.com/docs/legacy-api/csn/supplier-guide/authentication
  - aid: cvent:passkey-reglink
    name: Cvent Passkey RegLink API
    description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) connecting Cvent registration with Passkey hotel reservations. Send registrant info, fetch event and hotel availability, retrieve reservations, and create / update / cancel hotel bookings.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/passkey/REST/overview
    tags:
      - Accommodations
      - Hotels
      - Registration
      - Reservations
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/passkey/REST/overview
      - type: GettingStarted
        url: https://developers.cvent.com/docs/passkey/REST/getting-started
      - type: Callbacks
        url: https://developers.cvent.com/docs/passkey/REST/callbacks
      - type: FAQ
        url: https://developers.cvent.com/docs/passkey/REST/faq
  - aid: cvent:soap-api
    name: Cvent SOAP API (Legacy)
    description: The Cvent SOAP API is the original legacy API for pushing and pulling data between Cvent and internal systems. Supports contact and event management, custom fields, address book, and metadata. Being sunset in favor of the REST API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/legacy-api/soap-api/overview
    tags:
      - Contacts
      - Deprecated
      - Events
      - Legacy
      - Registration
      - SOAP
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/legacy-api/soap-api/overview
      - type: APIReference
        url: https://developers.cvent.com/docs/legacy-api/soap-api/call-definitions/overview
      - type: ObjectDefinitions
        url: https://developers.cvent.com/docs/legacy-api/soap-api/object-definitions/overview
      - type: MigrationGuide
        url: https://developers.cvent.com/docs/rest-api/migration-guide/benefits
  - aid: cvent:custom-widgets
    name: Cvent Custom Widgets API
    description: The Cvent Custom Widgets API allows developers to build custom interactive widgets for Cvent Event Registration pages. SDK for widget elements, configuration files, and navigation methods.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/custom-widgets/overview
    tags:
      - Customization
      - Embedding
      - Registration
      - Widgets
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/custom-widgets/overview
      - type: GitHubRepository
        url: https://github.com/cvent/custom-widgets-labs
  - aid: cvent:sso
    name: Cvent Single Sign-On (SSO) Integration
    description: Cvent SSO enables identity provider integration via SAML and OpenID Connect for planner login, access portals, event registrant and Attendee Hub, Events+, and portal applications.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/sso/overview
    tags:
      - Authentication
      - Identity
      - OpenID Connect
      - SAML
      - SSO
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/sso/overview
      - type: Concepts
        url: https://developers.cvent.com/docs/sso/explanation/concepts
  - aid: cvent:white-label
    name: Cvent White Label API
    description: The Cvent White Label API enables venues and suppliers to embed Cvent RFP functionality into their own websites with custom branding, theming, and analytics for embedded RFP forms.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/white-label/overview
    tags:
      - Branding
      - RFP
      - White Label
      - Widgets
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/white-label/overview
  - aid: cvent:salesforce-app
    name: Cvent Salesforce App
    description: The Cvent Salesforce App integrates Cvent event data with Salesforce CRM, enabling users to view events from Salesforce, invite contacts and leads, and sync attendee data bidirectionally.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/cvent-salesforce-app/overview
    tags:
      - CRM
      - Events
      - Integration
      - Salesforce
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/cvent-salesforce-app/overview
      - type: GettingStarted
        url: https://developers.cvent.com/docs/cvent-salesforce-app/app-installation
      - type: Authentication
        url: https://developers.cvent.com/docs/cvent-salesforce-app/salesforce-oauth
common:
  - type: Website
    url: https://www.cvent.com/
  - type: DeveloperPortal
    url: https://developers.cvent.com/
  - type: APIReference
    url: https://developers.cvent.com/docs/rest-api/reference/reference
  - type: Authentication
    url: https://developers.cvent.com/docs/rest-api/explanation/authentication
  - type: OAuthTokenEndpoint
    url: https://api-platform.cvent.com/ea/oauth2/token
  - type: SignUp
    url: https://developers.cvent.com/register
  - type: Standards
    url: https://developers.cvent.com/docs/rest-api/reference/api-standards
  - type: ChangeLog
    url: https://developers.cvent.com/docs/rest-api/changelog
  - type: Status
    url: https://status.cvent.com
  - type: Support
    url: https://support.cvent.com/
  - type: Pricing
    url: https://www.cvent.com/en/event-management-software/cvent-pricing
  - type: TermsOfService
    url: https://www.cvent.com/en/terms-of-use
  - type: PrivacyPolicy
    url: https://www.cvent.com/en/privacy-policy
  - type: Security
    url: https://www.cvent.com/en/security
  - type: Training
    url: https://www.cvent.com/en/academy
  - type: Community
    url: https://community.cvent.com/home
  - type: Blog
    url: https://www.cvent.com/en/blog
  - type: GitHub
    url: https://github.com/cvent
  - type: Twitter
    url: https://twitter.com/cvent
  - type: LinkedIn
    url: https://www.linkedin.com/company/cvent
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - FN: Cvent Developer Relations
    email: developersupport@cvent.com
    url: https://developers.cvent.com
---
