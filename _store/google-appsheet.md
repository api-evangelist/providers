---
aid: google-appsheet
url: https://raw.githubusercontent.com/api-evangelist/google-appsheet/refs/heads/main/apis.yml
apis:
- aid: google-appsheet:google-appsheet
  name: Google AppSheet API
  description: Provides REST API access to AppSheet applications for performing CRUD operations on table data and invoking custom actions programmatically.
  humanURL: https://support.google.com/appsheet/answer/10105398
  baseURL: https://api.appsheet.com/api/v2
  properties:
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: JSONSchema
    url: json-schema/ActionRequest.json
  tags:
  - Actions
  - AppSheet
  - No-Code
  - Tables
name: Google AppSheet
tags:
- Applications
- Data
- Google
- Low-Code
- No-Code
- Tables
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google AppSheet API enables programmatic access to AppSheet applications, allowing developers to add, update, delete, and find records in AppSheet tables, as well as invoke predefined AppSheet actions via a REST interface.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

