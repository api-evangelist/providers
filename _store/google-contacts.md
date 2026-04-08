---
aid: google-contacts
url: https://raw.githubusercontent.com/api-evangelist/google-contacts/refs/heads/main/apis.yml
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
name: Google People API
tags:
- Address Book
- Contacts
- Directory
- Google
- People
- Profiles
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google People API provides access to information about profiles and contacts. It allows you to list, create, update, delete, and search contacts, as well as manage contact groups. It replaces the legacy Google Contacts API and provides access to user profiles and directory information.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

