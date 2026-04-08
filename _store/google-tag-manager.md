---
aid: google-tag-manager
url: https://raw.githubusercontent.com/api-evangelist/google-tag-manager/refs/heads/main/apis.yml
apis:
- name: Google Tag Manager API
  description: The Tag Manager API allows clients to access and modify container and tag configuration.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_tag_manager.svg
  humanURL: https://developers.google.com/tag-platform/tag-manager/api/v2
  baseURL: https://tagmanager.googleapis.com
  tags:
  - Analytics
  - Containers
  - Permissions
  - Tag Management
  - Triggers
  - Variables
  - Versions
  - Workspaces
  properties:
  - type: OpenAPI
    url: openapi/google-tag-manager-api-v2-openapi.yml
  - type: x-openapi-original
    url: https://tagmanager.googleapis.com/$discovery/rest?version=v2
  - type: JSONSchema
    url: json-schema/google-tag-manager-container-schema.json
  - type: JSONLD
    url: json-ld/google-tag-manager-context.jsonld
  - type: Documentation
    url: https://developers.google.com/tag-platform/tag-manager/api/v2
  - type: x-api-reference
    url: https://developers.google.com/tag-platform/tag-manager/api/reference/rest
  - type: Authentication
    url: https://developers.google.com/tag-platform/tag-manager/api/v2/authorization
  - type: x-getting-started
    url: https://developers.google.com/tag-platform/tag-manager/api/v2/devguide
  - type: x-sdk
    url: https://developers.google.com/tag-platform/tag-manager/api/v2/libraries
  - type: x-rate-limits
    url: https://developers.google.com/tag-platform/tag-manager/api/v2/limits-quotas
  - type: x-change-log
    url: https://support.google.com/tagmanager/answer/4620708
  contact:
  - FN: Google Support
    url: https://support.google.com/tagmanager
    email: ''
- name: Google Tag Manager Server-side Tagging API
  description: The Server-side Tagging API provides APIs for building custom tags, clients, and variables that run in a server-side container, enabling server-to-server data collection and processing.
  image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_tag_manager.svg
  humanURL: https://developers.google.com/tag-platform/tag-manager/server-side
  baseURL: https://tagmanager.googleapis.com
  tags:
  - Analytics
  - Data Collection
  - Privacy
  - Server-Side Tagging
  - Tag Management
  properties:
  - type: Documentation
    url: https://developers.google.com/tag-platform/tag-manager/server-side
  - type: x-api-reference
    url: https://developers.google.com/tag-platform/tag-manager/server-side/api
  - type: x-getting-started
    url: https://developers.google.com/tag-platform/tag-manager/server-side/intro
  - type: x-change-log
    url: https://developers.google.com/tag-platform/tag-manager/server-side/release-notes
  contact:
  - FN: Google Support
    url: https://support.google.com/tagmanager
    email: ''
name: Google Tag Manager
tags:
- Analytics
- Conversion Tracking
- Marketing
- Tag Management
- Tracking
type: Contract
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_tag_manager.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Tag Manager is a tag management system that allows you to quickly and easily update measurement codes and related code fragments collectively known as tags on your website or mobile app.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

