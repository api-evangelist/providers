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
    description: >-
      GraphQL is a query language for APIs. You can use it to request the exact
      data you need, and therefore limit the number of requests you need.
      GraphQL data is arranged in types, so your client can use client-side
      GraphQL libraries to consume the API and avoid manual parsing. There are
      no fixed endpoints and no data model, so you can add to the API without
      creating breaking changes. This enables us to have a versionless API.
  - name: ' api/v4/groups'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-groups-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-groups-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/projects'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-projects-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-projects-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/admin'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-admin-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-admin-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/applications'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-applications-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-applications-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/avatar'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-avatar-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-avatar-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/broadcast messages'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-broadcast-messages-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-broadcast-messages-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/bulk imports'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-bulk-imports-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-bulk-imports-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/application'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-application-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-application-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/metadata'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-metadata-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-metadata-openapi-original.yml
        type: OpenAPI
    description: Needs description.
  - name: ' api/v4/version'
    tags: []
    overlays:
      - url: overlays/gitlab-api-v4-version-openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/gitlab-api-v4-version-openapi-original.yml
        type: OpenAPI
    description: Needs description.
name: GitLab
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
modified: 2023/11/10
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  GitLab Inc. is an open-core company that operates GitLab, a DevOps software
  package that can develop, secure, and operate software.[9] The open source
  software project was created by Ukrainian developer Dmytro Zaporozhets and
  Dutch developer Sytse Sijbrandij.[10] In 2018, GitLab Inc. was considered to
  be the first partly-Ukrainian unicorn. Since its founding, GitLab Inc. has
  promoted remote work,[13] and is known as one of the largest all-remote
  companies in the world.[14] GitLab has an estimated 30 million registered
  users, with 1 million being active licensed users.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'

---