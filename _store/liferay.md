---
aid: liferay
name: Liferay
description: Liferay DXP is an open-source digital experience platform offering headless REST APIs for managing users, roles, permissions, content, and site configuration. The Roles API lets you list, retrieve, and associate or dissociate regular, site, and organization roles for users.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Open Source
  - Digital Experience
  - DXP
  - Roles
  - Users
  - Permissions
  - Headless
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/liferay/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: liferay:liferay
    name: Liferay Roles API
    description: 'Liferay''s headless admin user Roles API. Create and manage roles via REST: list and retrieve roles, and associate or dissociate users to regular, site, and organization roles.'
    humanURL: https://learn.liferay.com/w/dxp/integration/headless-apis/user-management-apis/roles-api-basics
    baseURL: http://localhost:8080/o/headless-admin-user/v1.0
    tags:
      - Roles
      - Users
      - Permissions
    properties:
      - type: Documentation
        url: https://learn.liferay.com/w/dxp/integration/headless-apis/user-management-apis/roles-api-basics
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/liferay/refs/heads/main/openapi/liferay-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
