---
aid: permit-io
name: Permit.io
description: Permit.io is an authorization-as-a-service platform that helps developers build, manage, and enforce fine-grained access control in their applications. It provides a Policy Decision Point (PDP), management API, REST API, and permission query APIs for role-based, attribute-based, and relationship-based access control with support for bulk checks, data filtering, and URL-based enforcement.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Control
  - Authorization
  - Identity
  - Policy
  - Security
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/permit-io/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: permit-io:permit-io
    name: Permit.io API
    description: The Permit.io API (v2) is the management and authorization API for the Permit.io platform, covering members, API keys, organizations, projects, environments, resources, roles, role assignments, condition sets, relationships, implicit grants, and bulk operations for authorization management and enforcement.
    humanURL: https://docs.permit.io/
    baseURL: https://api.permit.io
    tags:
      - Access Control
      - Authorization
      - Policy
      - Security
    properties:
      - type: Documentation
        url: https://docs.permit.io/
      - type: API Reference
        url: https://api.permit.io/v2/redoc
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/permit-io/refs/heads/main/openapi/permit-io-openapi.json
common:
  - type: Website
    url: https://www.permit.io
  - type: Documentation
    url: https://docs.permit.io/
  - type: API Reference
    url: https://api.permit.io/v2/redoc
  - type: Sign Up
    url: https://app.permit.io/
  - type: GitHub Org
    url: https://github.com/permitio
  - type: Blog
    url: https://www.permit.io/blog
  - type: Pricing
    url: https://www.permit.io/pricing
  - type: Status
    url: https://status.permit.io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
