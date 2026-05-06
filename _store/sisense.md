---
aid: sisense
name: Sisense
description: Sisense is a business intelligence and analytics platform that enables organizations to build and embed analytics into applications and workflows. It provides REST APIs for managing dashboards, data models (Elasticubes and live models), users, groups, data security rules, and builds. The platform supports both extract-based and live data model architectures with comprehensive programmatic administration capabilities.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Dashboards
  - Data Models
  - Embedded Analytics
created: '2025-01-08'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sisense/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sisense:rest-api-v1
    name: Sisense REST API v1
    description: The Sisense REST API v1 provides programmatic access to dashboards, users, groups, Elasticubes, data security rules, and builds. It supports both extract-based Elasticube models and live data models. Authentication uses Bearer tokens obtained via the login endpoint or from User Profiles settings.
    humanURL: https://developer.sisense.com/guides/restApi/v1/
    baseURL: https://your-sisense-host/api/v1
    tags:
      - Dashboards
      - Users
      - Groups
      - Elasticubes
      - Data Models
      - Analytics
    properties:
      - type: Documentation
        url: https://developer.sisense.com/guides/restApi/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sisense/refs/heads/main/openapi/sisense-rest-api-openapi.yml
  - aid: sisense:rest-api-v2
    name: Sisense REST API v2
    description: The Sisense REST API v2 provides access to Datamodels (the v2 replacement for Elasticubes), builds, and advanced data model management capabilities including schema management, field configuration, and live data model operations.
    humanURL: https://developer.sisense.com/guides/restApi/v2/
    baseURL: https://your-sisense-host/api/v2
    tags:
      - Data Models
      - Builds
      - Analytics
    properties:
      - type: Documentation
        url: https://developer.sisense.com/guides/restApi/v2/
  - aid: sisense:user-role-management-api
    name: Sisense User and Role Management API
    description: The Sisense User and Role Management API (RBAC) enables administrators to manage users, roles, and permissions programmatically. Available on select plans through contact with Customer Success Manager.
    humanURL: https://dtdocs.sisense.com/article/user-and-role-management-api-rbac
    baseURL: https://your-sisense-host/api/v1
    tags:
      - Users
      - Roles
      - RBAC
      - Identity
    properties:
      - type: Documentation
        url: https://dtdocs.sisense.com/article/user-and-role-management-api-rbac
common:
  - type: Website
    url: https://www.sisense.com/
  - type: DeveloperPortal
    url: https://developer.sisense.com/
  - type: Documentation
    url: https://docs.sisense.com/
  - type: Pricing
    url: https://www.sisense.com/pricing/
  - type: Blog
    url: https://www.sisense.com/blog/
  - type: GitHubOrg
    url: https://github.com/sisense
  - type: Community
    url: https://community.sisense.com/
  - type: TermsOfService
    url: https://www.sisense.com/legal/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.sisense.com/legal/privacy-policy/
  - type: Support
    url: https://support.sisense.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
