---
aid: sitefinity-cms
url: https://raw.githubusercontent.com/api-evangelist/sitefinity-cms/refs/heads/main/apis.yml
name: Sitefinity CMS
description: Sitefinity CMS is a .NET-based content management system developed by Progress Software that provides REST APIs for managing content items, pages, users, roles, taxonomies, media, and e-commerce resources. Developers use the Sitefinity REST API to build headless front-ends, integrate third-party systems, automate content operations, and extend the platform with custom modules.
tags:
  - Content Management
  - Headless CMS
  - .NET
  - REST
created: '2025-01-08'
modified: '2026-05-02'
apis:
  - aid: sitefinity-cms:content-api
    name: Sitefinity CMS Content API
    description: The Sitefinity CMS Content API provides RESTful access to all content types defined in a Sitefinity instance. Developers use it to create, read, update, and delete content items, manage content translations, publish and unpublish items, and query content with filtering, sorting, and pagination. The API is organized around content type endpoints generated dynamically from the Sitefinity content model, enabling custom content types to be accessed via consistent patterns.
    humanURL: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api
    baseURL: https://your-site.sitefinity.com/api/default
    tags:
      - Content Management
      - Content Types
      - REST
    properties:
      - url: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api
        type: Documentation
      - type: OpenAPI
        url: openapi/sitefinity-cms-content-api-openapi.yml
  - aid: sitefinity-cms:pages-api
    name: Sitefinity CMS Pages API
    description: The Sitefinity CMS Pages API provides REST endpoints for managing the page hierarchy, page properties, page templates, and page nodes. Developers use it to automate page creation, update navigation structures, manage URL routing, and integrate page management into CI/CD workflows. The Pages API is part of the broader Sitefinity REST infrastructure and supports standard CRUD operations.
    humanURL: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api-pages
    baseURL: https://your-site.sitefinity.com/api/default
    tags:
      - Pages
      - Content Management
      - REST
    properties:
      - url: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api-pages
        type: Documentation
  - aid: sitefinity-cms:users-roles-api
    name: Sitefinity CMS Users and Roles API
    description: The Sitefinity CMS Users and Roles API provides REST endpoints for managing user accounts, roles, and permissions. Developers use this API to automate user provisioning, manage role assignments, and integrate Sitefinity identity management with external identity providers. The Roles API exposes operations for listing, creating, and updating roles and their associated permissions.
    humanURL: https://www.progress.com/documentation/sitefinity-cms/for-developers-roles-api
    baseURL: https://your-site.sitefinity.com/api/default
    tags:
      - Users
      - Roles
      - Identity
      - REST
    properties:
      - url: https://www.progress.com/documentation/sitefinity-cms/for-developers-roles-api
        type: Documentation
  - aid: sitefinity-cms:media-api
    name: Sitefinity CMS Media API
    description: The Sitefinity CMS Media API provides REST endpoints for managing images, videos, documents, and other media items stored in Sitefinity libraries. Developers use it to upload, retrieve, update, and delete media assets programmatically, supporting headless media workflows and integrations with digital asset management pipelines.
    humanURL: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api-media
    baseURL: https://your-site.sitefinity.com/api/default
    tags:
      - Media
      - Digital Assets
      - Libraries
      - REST
    properties:
      - url: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api-media
        type: Documentation
  - aid: sitefinity-cms:taxonomies-api
    name: Sitefinity CMS Taxonomies API
    description: The Sitefinity CMS Taxonomies API provides REST endpoints for managing taxonomies, categories, and tags used to classify and organize content. Developers use it to create classification structures, assign taxonomy items to content, and query content by taxonomy dimension for filtering and navigation.
    humanURL: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api
    baseURL: https://your-site.sitefinity.com/api/default
    tags:
      - Taxonomies
      - Classification
      - Content Management
      - REST
    properties:
      - url: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api
        type: Documentation
common:
  - type: Website
    url: https://www.progress.com/sitefinity-cms
  - type: Documentation
    url: https://www.progress.com/documentation/sitefinity-cms
  - type: Portal
    url: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api
  - type: Blog
    url: https://www.progress.com/blogs/sitefinity
  - type: Support
    url: https://www.progress.com/support
  - type: JSON-LD
    url: json-ld/sitefinity-cms-context.jsonld
  - type: SpectralRules
    url: rules/sitefinity-cms-rules.yml
  - type: Vocabulary
    url: vocabulary/sitefinity-cms-vocabulary.yml
  - type: Capabilities
    url: capabilities/content-management.yaml
---
