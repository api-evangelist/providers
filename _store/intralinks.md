---
aid: intralinks
url: https://raw.githubusercontent.com/api-evangelist/intralinks/refs/heads/main/apis.yml
apis:
  - aid: intralinks:api
    name: Intralinks API
    tags:
      - Document Management
      - Secure File Sharing
      - Virtual Data Room
    humanURL: https://developers.intralinks.com
    properties:
      - url: https://developers.intralinks.com/swagger/
        type: Documentation
      - url: openapi/intralinks-api-openapi.yml
        type: OpenAPI
      - url: json-schema/workspace.json
        type: JSONSchema
      - url: json-schema/document.json
        type: JSONSchema
      - url: json-schema/folder.json
        type: JSONSchema
      - url: json-schema/group.json
        type: JSONSchema
      - url: json-schema/user.json
        type: JSONSchema
      - url: json-schema/permission.json
        type: JSONSchema
      - url: json-schema/splash.json
        type: JSONSchema
      - url: json-schema/custom-field.json
        type: JSONSchema
      - url: json-ld/intralinks-context.jsonld
        type: JSONLD
    description: The Intralinks API provides RESTful access to the Intralinks virtual data room platform, enabling programmatic management of workspaces (exchanges), documents, folders, groups, users, permissions, splash screens, and custom fields. Authentication uses OAuth 2.0 with authorization code and client credentials flows. The API supports secure document sharing, M&A due diligence workflows, and confidential business collaboration.
name: Intralinks
tags:
  - Document Management
  - Secure File Sharing
  - Virtual Data Room
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://developers.intralinks.com
    name: Intralinks Developer Portal
    type: Portal
    description: 'null'
  - url: https://developers.intralinks.com/swagger/
    name: Intralinks API Documentation
    type: Documentation
    description: 'null'
  - url: https://support.intralinks.com/hc/en-us/sections/17037626903707-Intralinks-APIs
    name: Intralinks API Support
    type: Support
    description: 'null'
  - url: https://www.intralinks.com/why-intralinks/apis-deployment
    name: Intralinks APIs and Platform Accelerators
    type: GettingStarted
    description: 'null'
created: '2025-01-01'
modified: '2026-04-28'
position: Consumer
description: Intralinks is a cloud-based virtual data room and secure file sharing platform used for M&A transactions, due diligence, and confidential business collaboration. The platform provides APIs for programmatic access to workspaces, documents, folders, groups, users, and permissions, enabling integration with enterprise document management and deal workflow systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
