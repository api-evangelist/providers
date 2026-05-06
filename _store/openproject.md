---
aid: openproject
name: OpenProject
description: OpenProject is an open source project management platform offering work package tracking, Gantt charts, agile boards, time tracking, BIM, and enterprise project portfolio management. The OpenProject APIv3 is a hypermedia (HAL+JSON) REST API that exposes work packages, projects, users, attachments, custom fields, and many other resources.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agile
  - Gantt
  - Open Source
  - Project Management
  - Time Tracking
  - Work Packages
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openproject/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openproject:openproject-api
    name: OpenProject API v3
    description: The OpenProject API v3 is a hypermedia REST API (HATEOAS, HAL+JSON) for managing work packages, projects, users, time entries, attachments, custom fields, and other OpenProject resources. It supports session, basic, bearer (API token), and OAuth 2.0 authentication.
    humanURL: https://www.openproject.org/docs/api/
    baseURL: https://community.openproject.org/api/v3
    properties:
      - type: Documentation
        url: https://www.openproject.org/docs/api/
      - type: Introduction
        url: https://www.openproject.org/docs/api/introduction/
      - type: Endpoints
        url: https://www.openproject.org/docs/api/endpoints/
      - type: GitHub
        url: https://github.com/opf/openproject
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openproject/refs/heads/main/openapi/openproject-openapi.yml
    tags:
      - Project Management
      - Work Packages
      - HAL+JSON
common:
  - type: Website
    url: https://www.openproject.org
  - type: Documentation
    url: https://www.openproject.org/docs/
  - type: API
    url: https://www.openproject.org/docs/api/
  - type: GitHub
    url: https://github.com/opf/openproject
  - type: Pricing
    url: https://www.openproject.org/pricing/
  - type: SelfHosting
    url: https://www.openproject.org/docs/installation-and-operations/
  - type: Login
    url: https://community.openproject.org/login
  - type: Support
    url: https://www.openproject.org/docs/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
