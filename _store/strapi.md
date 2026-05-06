---
aid: strapi
name: Strapi
description: Strapi is an open-source, headless CMS built with Node.js that gives developers full control over their content API. It provides a customizable admin panel for content management, automatically generates REST and GraphQL APIs for every content-type, and supports flexible database options including SQLite, PostgreSQL, MySQL, and MongoDB. Strapi v5 introduces a Document Service API with flattened response format, improved TypeScript support, and an enhanced content delivery API for building fast, decoupled frontends.
url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/apis.yml
image: https://strapi.io/assets/strapi-logo-dark.svg
tags:
  - CMS
  - Content Management
  - Headless CMS
  - Node.js
  - Open Source
type: Index
access: 3rd-Party
position: Consumer
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: strapi:strapi-rest-api
    name: Strapi REST API
    description: The Strapi REST API provides automatically generated endpoints for accessing and managing content-types created within the Strapi headless CMS. Supports full CRUD operations with filtering, sorting, pagination, population of relational fields, and internationalization. Content-types are private by default and require authenticated requests or configured public permissions. The API also includes a media library Upload plugin for file management.
    humanURL: https://docs.strapi.io/cms/api/rest
    baseURL: https://{host}
    tags:
      - CMS
      - Content Management
      - REST API
      - Headless CMS
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-rest-api-openapi.yml
      - type: Documentation
        url: https://docs.strapi.io/cms/api/rest
      - type: Documentation
        url: https://docs.strapi.io/cms/api/rest/parameters
  - aid: strapi:strapi-admin-panel-api
    name: Strapi Admin Panel API
    description: The Strapi Admin Panel API powers the back-office interface for managing content-types, content entries, media assets, and administrator accounts. Provides endpoints for the Content-Type Builder, Content Manager, Media Library, and role-based access control configuration. Supports three default roles (Super Admin, Editor, Author) and includes management of API tokens, transfer tokens, and webhooks.
    humanURL: https://docs.strapi.io/cms/features/admin-panel
    baseURL: https://{host}
    tags:
      - Admin
      - CMS
      - Content Management
      - RBAC
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-admin-panel-api-openapi.yml
      - type: Documentation
        url: https://docs.strapi.io/cms/features/admin-panel
      - type: Documentation
        url: https://docs.strapi.io/cms/features/rbac
  - aid: strapi:strapi-users-permissions-api
    name: Strapi Users and Permissions API
    description: The Strapi Users and Permissions API provides a full JWT-based authentication system for protecting API endpoints, along with an access-control list strategy for managing permissions between user groups. Supports user registration, login, password reset, email confirmation, and social provider authentication via OAuth. The API enables configuration of roles and permissions to control endpoint accessibility.
    humanURL: https://docs.strapi.io/cms/features/users-permissions
    baseURL: https://{host}
    tags:
      - Authentication
      - CMS
      - Permissions
      - User Management
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-users-and-permissions-api-openapi.yml
      - type: Documentation
        url: https://docs.strapi.io/cms/features/users-permissions
  - aid: strapi:strapi-webhooks
    name: Strapi Webhooks
    description: Strapi includes a built-in webhook system that notifies external services whenever content entries or media assets are created, updated, deleted, published, or unpublished. Webhooks are configured through the admin panel and include a custom X-Strapi-Event header identifying the event type.
    humanURL: https://docs.strapi.io/cms/backend-customization/webhooks
    tags:
      - CMS
      - Events
      - Webhooks
    properties:
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/asyncapi/strapi-webhooks-asyncapi.yml
      - type: Documentation
        url: https://docs.strapi.io/cms/backend-customization/webhooks
common:
  - type: Website
    url: https://strapi.io
  - type: Documentation
    url: https://docs.strapi.io
  - type: GitHub
    url: https://github.com/strapi/strapi
  - type: Blog
    url: https://strapi.io/blog
  - type: Forum
    url: https://forum.strapi.io
  - type: Discord
    url: https://discord.strapi.io
  - type: Roadmap
    url: https://feedback.strapi.io
  - type: Changelog
    url: https://github.com/strapi/strapi/releases
  - type: Pricing
    url: https://strapi.io/pricing-cloud
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-rest-api-openapi.yml
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-admin-panel-api-openapi.yml
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-users-and-permissions-api-openapi.yml
  - type: AsyncAPI
    url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/asyncapi/strapi-webhooks-asyncapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/json-schema/strapi-content-entry-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/json-ld/strapi-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
