---
aid: thought-industries
name: Thought Industries
description: Thought Industries is a B2B learning platform (LMS/LXP) providing REST and GraphQL APIs for programmatic access to courses, users, enrollments, content management, and reporting. Their developer portal enables integration of learning experiences into enterprise workflows with webhook support and comprehensive API coverage for user lifecycle, content, and analytics.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Education
  - Learning
  - LMS
  - LXP
  - E-Learning
  - Training
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/thought-industries/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: thought-industries:rest-api
    name: Thought Industries REST API
    description: The Thought Industries REST API v1 provides programmatic access to users, enrollments, courses, groups, content, categories, bundles, reports, and learning paths. Authentication uses API key via X-API-Key header or apiKey query parameter. Base URL is tenant-scoped at https://{subdomain}.thoughtindustries.com/incoming/api/v1/.
    humanURL: https://developer.thoughtindustries.com/
    baseURL: https://{subdomain}.thoughtindustries.com/incoming/api/v1
    tags:
      - Education
      - Learning
      - LMS
      - REST
      - Users
      - Courses
      - Enrollments
    properties:
      - type: Documentation
        url: https://api.thoughtindustries.com/
      - type: GettingStarted
        url: https://developer.thoughtindustries.com/api-tutorials/
      - type: Authentication
        url: https://developer.thoughtindustries.com/api-tutorials/
      - type: OpenAPI
        url: openapi/thought-industries-openapi.yml
      - type: JSONSchema
        url: json-schema/thought-industries-user-schema.json
      - type: JSONSchema
        url: json-schema/thought-industries-enrollment-schema.json
  - aid: thought-industries:graphql-api
    name: Thought Industries GraphQL API
    description: The Thought Industries GraphQL API provides flexible querying of platform data including courses, users, content, and enrollments. Available at /incoming/api/graphql with schema introspection supported. Complements the REST API for complex queries and mutations.
    humanURL: https://developer.thoughtindustries.com/graphql/
    baseURL: https://{subdomain}.thoughtindustries.com/incoming/api
    tags:
      - GraphQL
      - Learning
      - Education
      - LMS
    properties:
      - type: Documentation
        url: https://developer.thoughtindustries.com/graphql/
      - type: GettingStarted
        url: https://developer.thoughtindustries.com/api-tutorials/
common:
  - type: Website
    url: https://www.thoughtindustries.com/
  - type: DeveloperPortal
    url: https://developer.thoughtindustries.com/
  - type: Documentation
    url: https://api.thoughtindustries.com/
  - type: GettingStarted
    url: https://developer.thoughtindustries.com/api-tutorials/
  - type: Authentication
    url: https://academy.thoughtindustries.com/courses/api-keys
  - type: GitHubOrganization
    url: https://github.com/thoughtindustries
  - type: Webhooks
    url: https://developer.thoughtindustries.com/
  - type: Support
    url: https://support.thoughtindustries.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
