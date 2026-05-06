---
aid: cvent-platform
name: Cvent Platform
x-type: company
description: 'Cvent is a leading meetings, events, and hospitality technology provider serving more than 22,000 customers worldwide. The Cvent Platform spans two product groups: Event Cloud (event management, registration, mobile event apps, virtual and hybrid events, Attendee Hub, surveys, and analytics) and Hospitality Cloud (Cvent Supplier Network, Passkey hotel room block management, Venue Sourcing, and Sales & Catering). Programmatic access is delivered through the Cvent Platform REST API protected by OAuth 2.0 client credentials, with the token endpoint at api-platform.cvent.com/ea/oauth2/token. Earlier integrations also use legacy XML SOAP / RegLink web services. The developer portal at developers.cvent.com hosts API references, guides, and OpenAPI downloads.'
url: https://raw.githubusercontent.com/api-evangelist/cvent-platform/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Attendee Hub
  - Conferences
  - Event Management
  - Event Marketing
  - Events
  - Hospitality
  - Hospitality Cloud
  - Hybrid Events
  - Meetings
  - OAuth 2.0
  - Passkey
  - Registration
  - REST API
  - Supplier Network
  - Surveys
  - Venue Management
  - Virtual Events
apis:
  - aid: cvent-platform:rest-api
    name: Cvent Platform REST API
    description: The Cvent Platform REST API is the unified RESTful interface across the Event Cloud product line, providing programmatic access to events, contacts, registrations, attendees, sessions, speakers, exhibitors, surveys, webhooks, and Attendee Hub resources. The API uses OAuth 2.0 client credentials. Authorization code flow is available to planner administrators. Developers can download the OpenAPI specification from the API reference.
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
      - type: MigrationGuide
        url: https://developers.cvent.com/docs/rest-api/migration-guide/benefits
      - type: RegistrationGuide
        url: https://developers.cvent.com/docs/rest-api/guides/registration-guide
      - type: OAuthTokenEndpoint
        url: https://api-platform.cvent.com/ea/oauth2/token
  - aid: cvent-platform:passkey-reglink
    name: Cvent Passkey RegLink API
    description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) connecting Cvent with external registration and reservation applications. Primary functions include streamlining the hotel reservation process by sending registrant information to Passkey, fetching event details and hotel room availability, retrieving reservation information, and creating, updating, and cancelling registrant hotel reservations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/passkey/REST/overview
    baseURL: https://api-platform.cvent.com
    tags:
      - Group Bookings
      - Hotel
      - Passkey
      - Reservations
      - Room Blocks
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/passkey/REST/overview
      - type: GettingStarted
        url: https://developers.cvent.com/docs/passkey/REST/getting-started
      - type: PasskeyDocs
        url: https://developers.cvent.com/doc/passkey/
common:
  - type: Website
    url: https://www.cvent.com/
  - type: DeveloperPortal
    url: https://developers.cvent.com/
  - type: APIReference
    url: https://developers.cvent.com/docs/rest-api/overview
  - type: Authentication
    url: https://developers.cvent.com/docs/rest-api
  - type: OAuthTokenEndpoint
    url: https://api-platform.cvent.com/ea/oauth2/token
  - type: SupportArticles
    url: https://support.cvent.com/
  - type: Status
    url: https://status.cvent.com/
  - type: Pricing
    url: https://www.cvent.com/en/pricing
  - type: TermsOfService
    url: https://www.cvent.com/en/terms-of-service
  - type: PrivacyPolicy
    url: https://www.cvent.com/en/privacy-policy
  - type: Blog
    url: https://www.cvent.com/blog
  - type: Twitter
    url: https://twitter.com/cvent
  - type: LinkedIn
    url: https://www.linkedin.com/company/cvent/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
