---
aid: dotcms
url: https://raw.githubusercontent.com/api-evangelist/dotcms/refs/heads/main/apis.yml
apis:
  - aid: dotcms:rest
    name: dotCMS REST API
    tags:
      - CMS
      - Content
      - Content Management
    humanURL: https://dev.dotcms.com/docs/getting-started-rest-apis
    baseURL: https://demo.dotcms.com/api
    properties:
      - url: https://dev.dotcms.com/docs/getting-started-rest-apis
        type: Documentation
      - url: https://dev.dotcms.com/docs
        type: Developer
    description: The dotCMS REST API exposes the platform's content management capabilities through HTTP endpoints, allowing developers to create, read, update, and delete content, manage workflows, navigate site hierarchy, perform search queries, and administer users, roles, and permissions. The API is organized into resource groups including Content, Workflow, Search, Navigation, Sites, and User management, and supports authentication via JWT tokens, basic auth, and API keys.
  - aid: dotcms:graphql
    name: dotCMS GraphQL API
    tags:
      - CMS
      - Content
      - Content Management
      - GraphQL
    humanURL: https://dev.dotcms.com/docs/graphql
    baseURL: https://demo.dotcms.com/api/v1/graphql
    properties:
      - url: https://dev.dotcms.com/docs/graphql
        type: Documentation
    description: The dotCMS GraphQL API provides a single endpoint for querying content across all content types using a self-documenting schema. It supports Lucene-style query strings, pagination, sorting, and content-type collections, and exposes base types for File, Form, Key/Value, Page, Persona, Vanity URL, and Widget content. The API accepts the same authentication methods as the dotCMS REST API and includes a built-in GraphQL Playground for exploring the schema.
name: dotCMS
tags:
  - CMS
  - Content
  - Content Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-28'
position: Consumer
description: dotCMS is a content management system that provides organizations with a powerful platform to create, manage, and deliver digital content. It offers a wide range of features, including content authoring tools, workflow management, personalization capabilities, and content analytics. With dotCMS, users can easily create and update websites, intranet portals, and mobile applications. The platform is designed to be flexible and scalable, making it suitable for businesses of all sizes.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
