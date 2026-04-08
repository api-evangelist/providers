---
aid: zesty
url: https://raw.githubusercontent.com/api-evangelist/zesty/refs/heads/main/apis.yml
apis:
- aid: zesty:auth-api
  name: Zesty Auth API
  tags:
  - Authentication
  - Sessions
  - Tokens
  humanURL: https://docs.zesty.io/docs/auth-api
  properties:
  - url: https://docs.zesty.io/docs/auth-api
    type: Documentation
  - url: openapi/zesty-auth-api-openapi.yml
    type: OpenAPI
  description: The Zesty.io Auth API is used to authenticate users with the platform. It returns a session token that grants access to the Instances API, Accounts API, and Media API. User authentication is done by providing an email and password combination, which issues a short-lived 30-minute session token.
- aid: zesty:accounts-api
  name: Zesty Accounts API
  tags:
  - Accounts
  - Instances
  - Roles
  - Teams
  - Users
  humanURL: https://docs.zesty.io/docs/accounts
  properties:
  - url: https://docs.zesty.io/docs/accounts
    type: Documentation
  - url: openapi/zesty-accounts-api-openapi.yml
    type: OpenAPI
  - url: json-schema/instance.json
    type: JSONSchema
  - url: json-schema/user.json
    type: JSONSchema
  - url: json-schema/role.json
    type: JSONSchema
  - url: json-schema/team.json
    type: JSONSchema
  - url: json-schema/token.json
    type: JSONSchema
  description: The Zesty.io Accounts API is used to manage users, roles, instances, teams, tokens, ecosystems, webhooks, and apps. It provides administrative control over the organizational structure of a Zesty.io account.
- aid: zesty:instances-api
  name: Zesty Instances API
  tags:
  - CMS
  - Content Items
  - Content Models
  - Publishing
  - Views
  humanURL: https://docs.zesty.io/docs/instances-api
  properties:
  - url: https://docs.zesty.io/docs/instances-api
    type: Documentation
  - url: openapi/zesty-instances-api-openapi.yml
    type: OpenAPI
  - url: json-schema/content-model.json
    type: JSONSchema
  - url: json-schema/content-item.json
    type: JSONSchema
  - url: json-schema/field.json
    type: JSONSchema
  description: The Zesty.io Instances API is a REST API that allows CRUD operations on Zesty.io instances. It provides access to content models, content items, fields, views, stylesheets, scripts, settings, head tags, navigation, audits, and publishing operations. Each instance is identified by a unique ZUID.
- aid: zesty:media-api
  name: Zesty Media API
  tags:
  - CDN
  - Files
  - Images
  - Media
  - Storage
  humanURL: https://docs.zesty.io/docs/media
  properties:
  - url: https://docs.zesty.io/docs/media
    type: Documentation
  - url: openapi/zesty-media-api-openapi.yml
    type: OpenAPI
  - url: json-schema/media-bin.json
    type: JSONSchema
  - url: json-schema/media-group.json
    type: JSONSchema
  - url: json-schema/media-file.json
    type: JSONSchema
  - url: json-ld/zesty-context.jsonld
    type: JSONLD
  description: 'The Zesty.io Media API is a collection of services for managing media files. It consists of four services: Media Manager, Media Storage, Media Modify, and Media Resolver. It handles bins, groups (folders), file uploads, and CDN URL resolution.'
name: Zesty
tags:
- CMS
- Composable
- Content Management
- Headless CMS
- Media
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-07'
position: Consumer
description: Zesty.io is a composable, data-driven, headless CMS platform that provides REST APIs for authentication, account management, instance content management, and media file management. All resources are identified by ZUIDs (Zesty Universal Identifiers).
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

