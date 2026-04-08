---
aid: google-people
url: https://raw.githubusercontent.com/api-evangelist/google-people/refs/heads/main/apis.yml
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
name: Google People
tags:
- Address Book
- Contacts
- Google
- People
- Profiles
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google People API provides access to information about profiles and contacts. It enables reading and managing the authenticated user's contacts, contact groups, and profile information across Google services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

