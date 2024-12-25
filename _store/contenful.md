---
aid: contenful
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/contentful.yml
apis:
  - aid: contenful:contentful-content-delivery-api
    name: Contentful Content Delivery API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cdn.contentful.com
    humanURL: >-

      https://www.contentful.com/developers/docs/references/content-delivery-api/
    overlays: []
    properties:
      - url: >-

          https://www.contentful.com/developers/docs/references/content-delivery-api/
        type: Documentation
    description: |-

      The Content Delivery API (CDA), available at cdn.contentful.com, is a
      read-only API for delivering content from Contentful to apps, websites and
      other media. Content is delivered as JSON data, and images, videos and
      other media as files.
  - aid: contenful:contentful-content-management-api
    name: Contentful Content Management API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: >-

      https://www.contentful.com/developers/docs/references/content-management-api/
    overlays: []
    properties:
      - url: >-

          https://www.contentful.com/developers/docs/references/content-management-api/
        type: Documentation
    description: |-

      Contentful's Content Management API (CMA) helps you manage content in your
      spaces. To learn more about how to model your content, read our modeling
      guide.
  - aid: contenful:contentful-preview-api
    name: Contentful Preview API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.contentful.com/developers/docs/references/content-preview-api/
    overlays: []
    properties:
      - url: >-

          https://www.contentful.com/developers/docs/references/content-preview-api/
        type: Documentation
    description: |-

      In addition to the Content Delivery API (CDA) for published content, is
      the Preview API for previewing both published and unpublished content. It
      maintains the same behaviour and parameters as the CDA, but delivers the
      latest drafts for entries and assets. The Content Preview API is used to
      display the latest version of an entry.
  - aid: contenful:contentful-images-api
    name: Contentful Images API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.contentful.com/developers/docs/references/images-api/
    overlays: []
    properties:
      - url: https://www.contentful.com/developers/docs/references/images-api/
        type: Documentation
    description: |-

      The Contentful Images API allows the retrieval and manipulation of image
      files referenced from assets.
  - aid: contenful:contentful-graphql-content-api
    name: Contentful GraphQL Content API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.contentful.com/developers/docs/references/graphql/
    overlays: []
    properties:
      - url: https://www.contentful.com/developers/docs/references/graphql/
        type: Documentation
    description: |-

      The GraphQL Content API provides a GraphQL API interface to the content
      from Contentful. Each Contentful space comes with a GraphQL schema based
      on its content model. This GraphQL schema is generated at request time and
      is always up-to-date with the current status of the space.
  - aid: contenful:contentful-user-management-api
    name: Contentful User Management API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.contentful.com/developers/docs/references/user-management-api/
    overlays: []
    properties:
      - url: >-

          https://www.contentful.com/developers/docs/references/user-management-api/
        type: Documentation
    description: |-

      Contentful's User Management API helps organizations programmatically
      manage their organizations, organization memberships, teams, space
      memberships and more.
  - aid: contenful:contentful-scim-api
    name: Contentful SCIM API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.contentful.com/developers/docs/references/scim-api/
    overlays: []
    properties:
      - url: https://www.contentful.com/developers/docs/references/scim-api/
        type: Documentation
    description: |-

      System for Cross-domain Identity Management, or SCIM, is an API
      specification created to facilitate the management of people and groups of
      people in cloud-based applications and services.
name: Contenful
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.contentful.com/developers/
    type: Portal
  - url: https://www.contentful.com/developers/docs/
    type: Documentation
  - url: https://www.contentful.com/developers/changelog/
    type: Change Log
  - url: https://www.contentful.com/blog/category/guides/
    type: Blog
  - url: https://www.contentful.com/pricing/
    type: Plans
  - url: https://www.contentful.com/sign-up/#small
    type: Sign Up
  - url: https://be.contentful.com/login
    type: Login
  - url: https://www.contentful.com/faq/webhooks/
    type: Webhooks
  - url: https://www.contentful.com/developers/changelog/
    type: Change Log
  - url: https://www.contentful.com/developers/code-of-conduct/
    type: Code of Conduct
  - url: https://www.contentful.com/support/
    type: Support
  - url: http://stackoverflow.com/questions/tagged/contentful?sort=newest
    type: Stack Overflow
  - url: https://www.contentful.com/security/
    type: Security
  - url: https://www.contentful.com/legal/privacy-at-contentful/privacy-notice/
    type: Privacy Policy
created: 2023/11/20
modified: 2023/11/20
description: |-

  Contentful is content infrastructure. Our platform lets you create, manage and
  distribute content to any platform. Unlike a CMS, we give you total freedom to
  create your own content model so you can decide which content you want to
  manage.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'

---