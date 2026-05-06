---
aid: google-people
name: Google People
description: The Google People API provides access to information about profiles and contacts. It enables reading and managing the authenticated user's contacts, contact groups, and profile information across Google services.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-people/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Address Book
  - Contacts
  - Google
  - People
  - Profiles
apis:
  - name: Google People API
    description: Provides access to Google Contacts data including creating, reading, updating, and deleting contacts and contact groups, searching contacts, and accessing profile information.
    humanURL: https://developers.google.com/people
    baseURL: https://people.googleapis.com/v1
    tags:
      - Contacts
      - People
      - Profiles
    properties:
      - type: Documentation
        url: https://developers.google.com/people/api/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/people/v1/how-tos/authorizing
      - type: Getting Started
        url: https://developers.google.com/people/v1/getting-started
      - type: JSONSchema
        url: json-schema/Person.json
common:
  - type: Portal
    url: https://developers.google.com/people
  - type: Getting Started
    url: https://developers.google.com/people/v1/getting-started
  - type: Documentation
    url: https://developers.google.com/people
  - type: Authentication
    url: https://developers.google.com/people/v1/how-tos/authorizing
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/people/v1/support
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
