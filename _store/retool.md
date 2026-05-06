---
aid: retool
name: Retool
description: Retool is a low-code platform for building internal tools, dashboards, and admin panels quickly using pre-built UI components that connect to any database or API. Retool provides a management REST API for programmatically administering users, groups, apps, resources, permissions, and source control integrations. It supports enterprise features including SSO, SCIM 2.0 provisioning, self-hosting, and AI-powered app generation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Admin Panel
  - Dashboard
  - Internal Tools
  - Low Code
  - No Code
url: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: retool:retool-management-api
    name: Retool Management API
    description: The Retool Management API enables administrators to programmatically manage users, groups, permissions, apps, resources, workflows, folders, spaces, and source control integrations. Authenticated via Bearer token. Supports both the native v1 API and SCIM 2.0 for enterprise identity provider integration.
    humanURL: https://docs.retool.com/reference/api/v2
    tags:
      - Administration
      - Apps
      - Groups
      - Permissions
      - Users
    properties:
      - type: Documentation
        url: https://docs.retool.com/reference/api/v2
      - type: Authentication
        url: https://docs.retool.com/org-users/concepts/retool-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/openapi/retool-management-api-openapi.yml
  - aid: retool:retool-scim-api
    name: Retool SCIM 2.0 API
    description: Retool implements a subset of the SCIM 2.0 API for automated user provisioning and group mapping through identity providers like Okta and Azure Active Directory (Entra ID). Available on Enterprise plan.
    humanURL: https://docs.retool.com/org-users/concepts/scim
    tags:
      - Enterprise
      - Identity
      - Okta
      - Provisioning
      - SCIM
      - SSO
    properties:
      - type: Documentation
        url: https://docs.retool.com/org-users/concepts/scim
  - aid: retool:retool-platform
    name: Retool Platform
    description: Retool's low-code platform provides a visual development environment with 100+ pre-built components, native connectors to 70+ data sources, AI-powered app generation (AppGen), workflow automation, built-in database, and mobile app support. Supports self-hosted and cloud deployment options with ISO 27001 and SOC 2 compliance.
    humanURL: https://retool.com/
    tags:
      - AI
      - Dashboard
      - Internal Tools
      - Low Code
      - Mobile
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.retool.com/
      - type: GettingStarted
        url: https://docs.retool.com/quickstarts
      - type: Pricing
        url: https://retool.com/pricing
common:
  - type: Website
    url: https://retool.com/
  - type: Documentation
    url: https://docs.retool.com/
  - type: APIReference
    url: https://docs.retool.com/reference/api/v2
  - type: Blog
    url: https://retool.com/blog
  - type: Changelog
    url: https://retool.com/changelog
  - type: Status
    url: https://status.retool.com
  - type: Support
    url: https://support.retool.com
  - type: Community
    url: https://community.retool.com
  - type: GitHub
    url: https://github.com/tryretool
  - type: Pricing
    url: https://retool.com/pricing
  - type: Login
    url: https://login.retool.com
  - type: Twitter
    url: https://twitter.com/retool
  - type: LinkedIn
    url: https://www.linkedin.com/company/tryretool
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/openapi/retool-management-api-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/vocabulary/retool-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
