---
aid: google-admin-sdk
name: Google Admin SDK
description: The Google Admin SDK provides a collection of RESTful APIs for managing Google Workspace organizations at scale. It includes the Directory API for managing users, groups, devices, and organizational units; the Reports API for auditing activity and usage; and the Data Transfer API for migrating data between users. These APIs enable programmatic integration with enterprise IT infrastructure.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-admin-sdk/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Administration
  - Devices
  - Directory
  - Enterprise
  - Google
  - Google Workspace
  - Groups
  - Users
apis:
  - aid: google-admin-sdk:google-admin-sdk-directory-api
    name: Google Admin SDK Directory API
    description: The Admin SDK Directory API enables management of users, groups, devices, organizational units, roles, domains, and other directory resources in a Google Workspace domain.
    humanURL: https://developers.google.com/workspace/admin/directory/reference/rest
    baseURL: https://admin.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.jsonld
    tags:
      - Administration
      - Devices
      - Directory
      - Groups
      - Users
common:
  - type: Getting Started
    url: https://developers.google.com/workspace/admin/overview
  - type: Pricing
    url: https://workspace.google.com/pricing
  - type: JSONLD
    url: json-ld/json-ld.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
