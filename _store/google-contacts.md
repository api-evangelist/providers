---
aid: google-contacts
name: Google People API
description: The Google People API provides access to information about profiles and contacts. It allows you to list, create, update, delete, and search contacts, as well as manage contact groups. It replaces the legacy Google Contacts API and provides access to user profiles and directory information.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-contacts/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Address Book
  - Contacts
  - Directory
  - Google
  - People
  - Profiles
apis:
  - name: Google People API v1
    description: The Google People API provides programmatic access to contacts and profile information. Manage contacts, contact groups, and access directory data for Google Workspace users.
    humanURL: https://developers.google.com/people
    baseURL: https://people.googleapis.com/v1
    properties:
      - type: Documentation
        url: https://developers.google.com/people/api/rest
      - type: OpenAPI
        url: openapi/contacts.yml
      - type: Authentication
        url: https://developers.google.com/people/v1/how-tos/authorizing
      - type: Getting Started
        url: https://developers.google.com/people/v1/getting-started
      - type: JSONSchema
        url: json-schema/contacts.json
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
    url: json-ld/contacts.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
