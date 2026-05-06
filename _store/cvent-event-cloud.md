---
aid: cvent-event-cloud
name: Cvent Event Cloud
x-type: company
description: 'Cvent Event Cloud is the event management product line of the Cvent Platform. It supports the full event lifecycle: event creation, registration, marketing, agenda and session management, mobile event apps, onsite check-in, virtual and hybrid event delivery via the Attendee Hub, surveys, and analytics. The Cvent Platform REST API exposes Event Cloud resources programmatically using OAuth 2.0 client credentials, with the token endpoint at api-platform.cvent.com/ea/oauth2/token. OpenAPI specifications can be downloaded from the developer portal at developers.cvent.com.'
url: https://raw.githubusercontent.com/api-evangelist/cvent-event-cloud/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Attendee Hub
  - Attendees
  - Event Cloud
  - Event Management
  - Event Marketing
  - Events
  - Hybrid Events
  - OAuth 2.0
  - Onsite
  - Registration
  - REST
  - Sessions
  - Speakers
  - Surveys
  - Virtual Events
  - Webhooks
apis:
  - aid: cvent-event-cloud:rest-api
    name: Cvent Platform REST API (Event Cloud)
    description: RESTful API for managing events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub data. Uses OAuth 2.0 client credentials. Authorization code flow is available to planner administrators. The OpenAPI specification can be downloaded from the API reference.
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
      - type: Concepts
        url: https://developers.cvent.com/docs/rest-api
      - type: Guides
        url: https://developers.cvent.com/docs/rest-api/guides/rest-guides
      - type: RegistrationGuide
        url: https://developers.cvent.com/docs/rest-api/guides/registration-guide
      - type: MigrationGuide
        url: https://developers.cvent.com/docs/rest-api/migration-guide/benefits
      - type: OAuthTokenEndpoint
        url: https://api-platform.cvent.com/ea/oauth2/token
common:
  - type: Website
    url: https://www.cvent.com/en/event-management-software
  - type: DeveloperPortal
    url: https://developers.cvent.com/
  - type: APIReference
    url: https://developers.cvent.com/docs/rest-api/overview
  - type: AttendeeHub
    url: https://www.cvent.com/en/attendee-hub
  - type: Pricing
    url: https://www.cvent.com/en/pricing
  - type: Support
    url: https://support.cvent.com/
  - type: Status
    url: https://status.cvent.com/
  - type: TermsOfService
    url: https://www.cvent.com/en/terms-of-service
  - type: PrivacyPolicy
    url: https://www.cvent.com/en/privacy-policy
  - type: Blog
    url: https://www.cvent.com/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
