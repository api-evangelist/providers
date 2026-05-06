---
aid: cvent-registration
name: Cvent Registration
x-type: company
description: Cvent Registration is the event registration product within the Cvent Event Cloud, providing online registration websites, attendee data capture, payment processing, registration travel, group registration, custom field collection, and badge / on-site check-in workflows. Registration data is exposed programmatically through the unified Cvent Platform REST API at api-platform.cvent.com (OAuth 2.0 client credentials), with a dedicated Registration Guide on the Cvent developer portal. Real-time registration changes are also delivered through Cvent Webhooks. Earlier integrations relied on the legacy Cvent SOAP API.
url: https://raw.githubusercontent.com/api-evangelist/cvent-registration/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Attendee Management
  - Attendees
  - Conferences
  - Event Management
  - Events
  - OAuth 2.0
  - On-Site Check-In
  - Payments
  - Registration
  - REST API
  - Ticketing
  - Webhooks
apis:
  - aid: cvent-registration:rest-api
    name: Cvent Registration REST API
    description: The Cvent Registration REST API is the registration surface of the unified Cvent Platform REST API. It allows integrations to create and manage events, registration types, fees, sessions, contacts, attendees, registrations, payments, and travel data. Authentication uses OAuth 2.0 client credentials with the token endpoint at api-platform.cvent.com/ea/oauth2/token. Detailed registration workflows are documented in the Registration Guide.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/rest-api/guides/registration-guide
    baseURL: https://api-platform.cvent.com
    tags:
      - Attendees
      - Contacts
      - Events
      - OAuth 2.0
      - Payments
      - Registration
      - REST
      - Sessions
      - Ticketing
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/rest-api/overview
      - type: RegistrationGuide
        url: https://developers.cvent.com/docs/rest-api/guides/registration-guide
      - type: APIReference
        url: https://developers.cvent.com/docs/rest-api/reference/reference
      - type: Authentication
        url: https://developers.cvent.com/docs/rest-api/explanation/authentication
      - type: OAuthTokenEndpoint
        url: https://api-platform.cvent.com/ea/oauth2/token
      - type: ChangeLog
        url: https://developers.cvent.com/docs/rest-api/changelog
  - aid: cvent-registration:webhooks
    name: Cvent Registration Webhooks
    description: Cvent Webhooks deliver real-time push notifications when registration, attendee, session, and meeting request events occur in Cvent. Webhook subscribers receive event payloads at a configured URL, enabling reactive integration with CRM, marketing automation, data warehouses, and analytics without polling the REST API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/webhooks/overview
    tags:
      - Attendees
      - Events
      - Notifications
      - Real-Time
      - Registration
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/webhooks/overview
      - type: GettingStarted
        url: https://developers.cvent.com/docs/webhooks/tutorials/account-setup
      - type: Guide
        url: https://developers.cvent.com/docs/webhooks/understanding-webhooks
      - type: TechnicalRequirements
        url: https://developers.cvent.com/docs/webhooks/technical-requirements
common:
  - type: Website
    url: https://www.cvent.com/en/event-management-software/online-registration-software
  - type: DeveloperPortal
    url: https://developers.cvent.com/
  - type: APIReference
    url: https://developers.cvent.com/docs/rest-api/reference/reference
  - type: Authentication
    url: https://developers.cvent.com/docs/rest-api/explanation/authentication
  - type: OAuthTokenEndpoint
    url: https://api-platform.cvent.com/ea/oauth2/token
  - type: Status
    url: https://status.cvent.com/
  - type: Support
    url: https://support.cvent.com/
  - type: Pricing
    url: https://www.cvent.com/en/pricing
  - type: TermsOfService
    url: https://www.cvent.com/en/terms-of-service
  - type: PrivacyPolicy
    url: https://www.cvent.com/en/privacy-policy
  - type: Twitter
    url: https://twitter.com/cvent
  - type: LinkedIn
    url: https://www.linkedin.com/company/cvent/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
