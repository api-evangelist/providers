---
aid: google-appsheet
name: Google AppSheet
description: The Google AppSheet API enables programmatic access to AppSheet applications, allowing developers to add, update, delete, and find records in AppSheet tables, as well as invoke predefined AppSheet actions via a REST interface.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-appsheet/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Applications
  - Data
  - Google
  - Low-Code
  - No-Code
  - Tables
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
common:
  - type: Getting Started
    url: https://support.google.com/appsheet/answer/10105398
  - type: Pricing
    url: https://workspace.google.com/products/appsheet/pricing/
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
