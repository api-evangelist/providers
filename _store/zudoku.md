---
aid: zudoku
url: https://raw.githubusercontent.com/api-evangelist/zudoku/refs/heads/main/apis.yml
apis:
- aid: zudoku:configuration-api
  name: Zudoku Configuration API
  tags:
  - Configuration
  - Developer Tools
  - Documentation
  humanURL: https://zudoku.dev/docs/configuration/overview
  properties:
  - url: https://zudoku.dev/docs/configuration/overview
    type: Documentation
  - url: openapi/zudoku-configuration-api-openapi.yml
    type: OpenAPI
  - url: json-schema/zudoku-config.json
    type: JSONSchema
  - url: json-schema/api-reference.json
    type: JSONSchema
  - url: json-schema/authentication.json
    type: JSONSchema
  - url: json-schema/theme.json
    type: JSONSchema
  - url: json-schema/plugin.json
    type: JSONSchema
  - url: json-ld/zudoku-context.jsonld
    type: JSONLD
  description: Zudoku is an open-source, developer-first API documentation framework built by Zuplo. It uses a file-based configuration model (zudoku.config.ts) to generate interactive API documentation from OpenAPI v2/v3 schemas. The configuration API defines how API references, navigation, authentication (OAuth2, OpenID Connect), theming, plugins, and MDX documentation pages are structured and managed.
name: Zudoku
tags:
- Developer Tools
- Documentation
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-05'
modified: '2026-04-07'
position: Consuming
description: Zudoku is an open-source, developer-first platform for creating clean, consistent API documentation built on a modern stack including React, TypeScript, and Vite. The tool enables developers to auto-generate documentation from OpenAPI v2/v3 schemas (supporting both single and multi-API setups) and provides built-in authentication and authorization support for OAuth2, JWT, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
common:
- name: Quickstart | Zudoku
  description: 'null'
  url: https://zudoku.dev/docs/quickstart
  type: Documentation
- name: Overview | Zudoku
  description: 'null'
  url: https://zudoku.dev/docs/configuration/authentication
  type: Authentication
- name: Sentry | Zudoku
  description: 'null'
  url: https://zudoku.dev/docs/configuration/sentry
  type: Integrations
- name: Static Files | Zudoku
  description: 'null'
  url: https://zudoku.dev/docs/guides/static-files
  type: Guide
---

