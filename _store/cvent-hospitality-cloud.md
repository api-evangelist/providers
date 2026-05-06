---
aid: cvent-hospitality-cloud
name: Cvent Hospitality Cloud
x-type: company
description: Cvent Hospitality Cloud is the hotel and venue product line of the Cvent Platform. It includes the Cvent Supplier Network (the marketplace connecting event planners with hotels and venues for RFPs and bookings), Passkey (hotel room block and housing management), Venue Sourcing (venue search and discovery), and Sales & Catering (booking management, catering, and contracts). Programmatic access is delivered primarily through the Passkey RegLink REST APIs (with legacy SOAP and URL-based options) and the unified Cvent Platform REST API. Authentication uses OAuth 2.0 client credentials with the token endpoint at api-platform.cvent.com/ea/oauth2/token.
url: https://raw.githubusercontent.com/api-evangelist/cvent-hospitality-cloud/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Catering
  - Group Bookings
  - Hospitality
  - Hospitality Cloud
  - Hotels
  - Housing
  - OAuth 2.0
  - Passkey
  - Reservations
  - RFP
  - Room Blocks
  - Sales
  - Sourcing
  - Supplier Network
  - Venues
apis:
  - aid: cvent-hospitality-cloud:passkey-reglink
    name: Cvent Passkey RegLink API
    description: Passkey RegLink APIs are RESTful JSON APIs (with legacy URL-based and SOAP options) that connect Cvent registration with Passkey hotel reservations. Primary functions include sending registrant information to Passkey to streamline hotel reservations, fetching Passkey event and hotel availability, retrieving reservation information, and creating, updating, and cancelling registrant reservations.
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
      - type: Product
        url: https://www.cvent.com/en/hospitality-cloud/passkey
  - aid: cvent-hospitality-cloud:rest-api
    name: Cvent Platform REST API (Hospitality)
    description: The unified Cvent Platform REST API also covers hospitality use cases including event-driven integrations, contact and attendee data exchange, and webhook-based notifications that can be wired into hotel and venue workflows. OAuth 2.0 client credentials.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.cvent.com/docs/rest-api/overview
    baseURL: https://api-platform.cvent.com
    tags:
      - Events
      - OAuth 2.0
      - REST
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.cvent.com/docs/rest-api/overview
      - type: Concepts
        url: https://developers.cvent.com/docs/rest-api
      - type: OAuthTokenEndpoint
        url: https://api-platform.cvent.com/ea/oauth2/token
common:
  - type: Website
    url: https://www.cvent.com/en/hospitality-cloud
  - type: SupplierNetwork
    url: https://www.cvent.com/en/hospitality-cloud/event-management/cvent-supplier-network
  - type: Passkey
    url: https://www.cvent.com/en/hospitality-cloud/passkey
  - type: DeveloperPortal
    url: https://developers.cvent.com/
  - type: Support
    url: https://support.cvent.com/
  - type: Status
    url: https://status.cvent.com/
  - type: TermsOfService
    url: https://www.cvent.com/en/terms-of-service
  - type: PrivacyPolicy
    url: https://www.cvent.com/en/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
