---
aid: hubspot
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/hubspot.yml
apis:
  - aid: hubspot:hubspot-domains-api
    name: HubSpot Domains API
    tags:
      - Domains
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/overview
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/domains-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/domains
        type: Documentation
      - url: properties/hubspot-domains-api-openapi.yml
        type: OpenAPI
    description: |-

      These endpoints allow you to return information about the domains
      connected to a particular HubSpot CMS site. You can return data for a list
      of domains or specify a domain by ID.
  - aid: hubspot:hubspot-source-code-api
    name: HubSpot Source Code API
    tags:
      - Sources
      - Code
      - Environments
      - Content
      - Path
      - Validate
      - Extract
      - Async
      - Task
      - Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/source-code
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/public/api/spec/v1/specs/cms/v3/source-code-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/source-code
        type: Documentation
      - url: properties/hubspot-source-code-api-openapi.yml
        type: OpenAPI
    description: |-

      Endpoints for interacting with files in the CMS Developer File System.
      These files include HTML templates, CSS, JS, modules, and other assets
      which are used to create CMS content.
  - aid: hubspot:hubspot-posts-api
    name: HubSpot Posts API
    tags:
      - Blogs
      - Posts
      - Schedules
      - Batch
      - Read
      - Multi
      - Language
      - Blog  Posts
      - Objects
      - Draft
      - Revisions
      - Restore
      - Variations
      - Clone
      - Detach
      - Groups
      - Live
      - Archive
      - Reset
      - Attach
      - Set
      - Primary
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/blog-post
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/blogs/blog-posts-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/blog-post
        type: Documentation
      - url: properties/hubspot-posts-api-openapi.yml
        type: OpenAPI
    description: |-

      Use these endpoints for interacting with Blog Posts, Blog Authors, and
      Blog Tags.
  - aid: hubspot:hubspot-authors-api
    name: HubSpot Authors API
    tags:
      - Blogs
      - Authors
      - Objects
      - Batch
      - Multi
      - Language
      - Detach
      - Groups
      - Set
      - Primary
      - Archive
      - Read
      - Attach
      - Variations
      - Languages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/blog-authors
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/blogs/authors-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/blog-authors
        type: Documentation
      - url: properties/hubspot-authors-api-openapi.yml
        type: OpenAPI
    description: |-

      Use the blog authors API to manage author information for your blog
      posts. 
  - aid: hubspot:hubspot-url-redirects-api
    name: HubSpot URL Redirects API
    tags:
      - Redirects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/url-redirects
    overlays:
      - url: >-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/url-redirects-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/url-redirects
        type: Documentation
      - url: properties/hubspot-url-redirects-api-openapi.yml
        type: OpenAPI
    description: |-

      URL redirects allow you to redirect traffic from a HubSpot-hosted page or
      blog post to any URL. You can also update URL redirects in bulk and use a
      flexible pattern redirect to dynamically update the structure of URLs.
name: HubSpot
tags:
  - CRM
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://api.hubspot.com/api-catalog-public/v1/apis
    type: Index
  - url: https://developers.hubspot.com/
    type: Portal
  - url: https://developers.hubspot.com/docs/api/overview
    type: Documentation
  - url: https://developers.hubspot.com/changelog
    type: Change Log
  - url: https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers
    type: Forums
  - url: https://developers.hubspot.com/slack
    type: Slack
  - url: https://developers.hubspot.com/blog
    type: Blog
  - url: https://offers.hubspot.com/developer-newsletter-signup
    type: Newsletter
  - url: https://www.hubspot.com/developer-community-events
    type: Events
  - url: https://ecosystem.hubspot.com/marketplace/apps
    type: Marketplace
  - url: https://legal.hubspot.com/privacy-policy
    type: Privacy Policy
  - url: https://legal.hubspot.com/terms-of-service
    type: Terms of Service
created: 2023/11/14
modified: '2024-12-30'
position: Consuming
description: |-

  HubSpot is a leading CRM platform that provides software and support to help
  businesses grow better. Our platform includes marketing, sales, service, and
  website management products that start free and scale to meet our customers'
  needs at any stage of growth. Today, thousands of customers around the world
  use our powerful and easy-to-use tools and integrations to attract, engage,
  and delight customers.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'

---