---
aid: swaggerhub
name: SwaggerHub
description: SwaggerHub is SmartBear's enterprise collaborative API design and documentation platform built around the OpenAPI specification. It provides tools for designing, building, documenting, and consuming RESTful APIs with support for OpenAPI 2.0, OpenAPI 3.0, OpenAPI 3.1, and AsyncAPI specifications. The platform offers automated validation, team collaboration, lifecycle management, integrations with CI/CD pipelines, and an organizational API registry.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - API Management
  - API Registry
  - Documentation
  - OpenAPI
  - SmartBear
url: https://raw.githubusercontent.com/api-evangelist/swaggerhub/refs/heads/main/apis.yml
created: '2026-03-03'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: swaggerhub:swaggerhub-registry-api
    name: SwaggerHub Registry API
    description: The SwaggerHub Registry API allows programmatic access to all SwaggerHub resources including APIs, domains, integrations, projects, templates, and standardization rulesets. Use it to manage API versions, publish/unpublish APIs, run integrations, manage project memberships, and retrieve OpenAPI definitions in JSON or YAML format.
    humanURL: https://support.smartbear.com/swaggerhub/docs/en/swaggerhub-apis.html
    baseURL: https://api.swaggerhub.com
    tags:
      - API Management
      - API Registry
      - Documentation
      - Integrations
      - OpenAPI
      - Projects
    properties:
      - type: Documentation
        url: https://support.smartbear.com/swaggerhub/docs/en/swaggerhub-apis.html
      - type: API Reference
        url: https://api.swaggerhub.com/apis/swagger-hub/registry-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swaggerhub/refs/heads/main/openapi/swaggerhub-registry-api-openapi.yml
      - type: Postman Collection
        url: https://www.postman.com/api-evangelist/swaggerhub/documentation/1lsm5uz/swaggerhub-registry-api
  - aid: swaggerhub:swaggerhub-user-management-api
    name: SwaggerHub User Management API
    description: The SwaggerHub User Management API enables organizations to automate user provisioning, manage team memberships, and control resource access. It supports adding and removing organization members, changing user roles (Owner, Designer, Consumer), and managing resource access permissions for users and teams.
    humanURL: https://support.smartbear.com/swaggerhub/docs/en/swaggerhub-apis/user-management-api.html
    baseURL: https://api.swaggerhub.com
    tags:
      - Access Control
      - Organizations
      - Teams
      - User Management
      - Users
    properties:
      - type: Documentation
        url: https://support.smartbear.com/swaggerhub/docs/en/swaggerhub-apis/user-management-api.html
      - type: API Reference
        url: https://app.swaggerhub.com/apis-docs/swagger-hub/user-management-api/v1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swaggerhub/refs/heads/main/openapi/swaggerhub-user-management-openapi.yml
common:
  - type: Portal
    url: https://swagger.io/tools/swaggerhub/
  - type: Sign Up
    url: https://app.swaggerhub.com/signup
  - type: Login
    url: https://app.swaggerhub.com/login/
  - type: Documentation
    url: https://support.smartbear.com/swaggerhub/docs/
  - type: Getting Started
    url: https://support.smartbear.com/swaggerhub/docs/en/get-started.html
  - type: Pricing
    url: https://swagger.io/product/pricing/
  - type: Blog
    url: https://swagger.io/blog/
  - type: Status
    url: https://status.swaggerhub.com/
  - type: Support
    url: https://support.smartbear.com/swaggerhub/
  - type: Terms of Service
    url: https://app.swaggerhub.com/terms-of-service
  - type: Privacy Policy
    url: https://app.swaggerhub.com/eula
  - type: Integrations
    url: https://swagger.io/tools/swaggerhub/integrations/
  - type: CLI
    url: https://github.com/SmartBear/swaggerhub-cli
  - type: GitHub Organization
    url: https://github.com/swagger-api
  - type: OpenAPI Specification
    url: https://swagger.io/specification/
  - type: About
    url: https://swagger.io/about/
  - type: License
    url: https://swagger.io/license/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
