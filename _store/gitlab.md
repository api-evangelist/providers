---
aid: gitlab
url: https://raw.githubusercontent.com/api-search/code/main/_apis/gitlab/apis.md
apis:
  - aid: gitlab:gitlab-graphql-api
    name: GitLab GraphQL API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.gitlab.com/ee/api/graphql/
    overlays: []
    properties:
      - url: https://docs.gitlab.com/ee/api/graphql/
        type: Documentation
      - url: >-
          https://docs.gitlab.com/ee/api/graphql/#deprecation-and-removal-process
        type: Deprecation
      - url: >-
          https://docs.gitlab.com/ee/api/graphql/#deprecation-and-removal-process
        type: Breaking Changes
      - url: https://docs.gitlab.com/ee/api/graphql/#limits
        type: Rate Limits
    description: |-
      GraphQL is a query language for APIs. You can use it to request the exact
      data you need, and therefore limit the number of requests you need.
      GraphQL data is arranged in types, so your client can use client-side
      GraphQL libraries to consume the API and avoid manual parsing. There are
      no fixed endpoints and no data model, so you can add to the API without
      creating breaking changes. This enables us to have a versionless API.
  - aid: gitlab:apiv4groups
    name: GitLab Groups API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-groups-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-groups-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4projects
    name: GitLab Projects API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-projects-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4admin
    name: GitLab Admin API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-admin-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-admin-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4applications
    name: GitLab Applications API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-applications-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-applications-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4avatar
    name: GitLab Avatar API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-avatar-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-avatar-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4broadcast-messages
    name: GitLab Broadcast Messages API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-broadcast-messages-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-broadcast-messages-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4bulk-imports
    name: GitLab Bulk Imports API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-bulk-imports-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-bulk-imports-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4application
    name: GitLab Applications API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-application-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-application-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4metadata
    name: GitLab Metadata API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-metadata-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-metadata-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - aid: gitlab:apiv4version
    name: GitLab Version API
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-version-openapi-search.yml
        type: OpenAPI
    properties:
      - url: openapi/gitlab-api-v4-version-openapi-original.yml
        type: OpenAPI
    description: Needs description.
name: GitLab
tags:
  - Code
  - Software Development
  - Source Control
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://about.gitlab.com/terms/
    type: Terms of Service
  - url: https://about.gitlab.com/privacy/
    type: Privacy Policy
  - url: https://about.gitlab.com/company/contact/
    type: Contact
  - url: https://docs.gitlab.com/ee/editor_extensions/
    type: IDE
  - url: https://about.gitlab.com/releases/categories/releases/
    type: Whats New
created: 2023/11/10
modified: '2024-12-30'
position: Consuming
description: >-
  GitLab Inc. is an open-core company that develops GitLab, a DevOps software
  platform for building, securing, and managing applications. Created by
  Ukrainian developer Dmytro Zaporozhets and Dutch developer Sytse Sijbrandij,
  GitLab became the first partly-Ukrainian unicorn in 2018. Known for promoting
  remote work, it is one of the largest all-remote companies globally. GitLab
  has approximately 30 million registered users, including 1 million active
  licensed users.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---