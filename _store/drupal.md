---
aid: drupal
url: https://raw.githubusercontent.com/api-evangelist/drupal/refs/heads/main/apis.yml
apis:
  - aid: drupal:rest-api
    name: Drupal REST API
    tags:
      - CMS
      - Content Management
      - REST
      - Web Services
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com
    humanURL: https://www.drupal.org/docs/core-modules-and-themes/core-modules/restful-web-services-module
    properties:
      - url: https://www.drupal.org/docs/core-modules-and-themes/core-modules/restful-web-services-module
        type: Documentation
      - url: openapi/drupal-rest-api-openapi.yml
        type: OpenAPI
    description: The Drupal RESTful Web Services API is a core module that exposes Drupal entities and data as REST resources over HTTP. It supports multiple serialization formats and HTTP methods including GET, POST, PATCH, and DELETE, and is highly configurable in terms of which resources, formats, and authentication methods are enabled. Unlike the JSON:API module, it allows developers to define custom REST endpoints for non-entity data and complex business logic operations.
  - aid: drupal:jsonapi
    name: Drupal JSON:API
    tags:
      - CMS
      - Content Management
      - Headless
      - JSON:API
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com/jsonapi
    humanURL: https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/api-overview
    properties:
      - url: https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/api-overview
        type: Documentation
      - url: openapi/drupal-jsonapi-openapi.yml
        type: OpenAPI
      - url: json-schema/drupal-jsonapi-resource-schema.json
        type: JSONSchema
    description: The Drupal JSON:API module is a core component that exposes all Drupal entity types and bundles as a standards-compliant JSON:API interface, requiring no configuration to enable. Each entity bundle receives a unique URL path following the pattern /jsonapi/{entity_type}/{bundle}, and the module supports GET, POST, PATCH, and DELETE operations for full CRUD access.
  - aid: drupal:graphql
    name: Drupal GraphQL API
    tags:
      - CMS
      - Content Management
      - GraphQL
      - Headless
      - Query Language
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://example.com/graphql
    humanURL: https://www.drupal.org/docs/contributed-modules/graphql
    properties:
      - url: https://www.drupal.org/docs/contributed-modules/graphql
        type: Documentation
      - url: https://drupal-graphql.gitbook.io/graphql/
        type: Documentation
    description: The Drupal GraphQL module is a contributed module that enables developers to craft and expose a GraphQL schema for Drupal 10 and 11, allowing client applications to query Drupal content and entities using GraphQL syntax. It supports both queries and mutations for reading and writing data, and includes a built-in GraphiQL Explorer interface at /graphql/explorer for interactive schema browsing and query development.
common:
  - url: json-ld/drupal-context.jsonld
    type: JSON-LD
  - url: json-schema/drupal-node-schema.json
    type: JSONSchema
modified: '2026-04-28'
description: Drupal is an open-source content management system written in PHP and used to build websites, applications, and digital experiences for individuals, organizations, and enterprises worldwide.
---
