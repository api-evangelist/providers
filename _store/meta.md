---
aid: meta
url: https://raw.githubusercontent.com/api-search/social/main/_apis/meta/apis.md
specificationVersion: '0.18'
name: Meta
description: Collection of Meta (Facebook) platform APIs for social networking, messaging, advertising, content publishing, AI, and developer tools across Facebook, Instagram, WhatsApp, Threads, and Messenger.
image: https://about.meta.com/brand/resources/meta/our-logo/
tags:
  - Advertising
  - Analytics
  - Artificial Intelligence
  - Messaging
  - Social
  - Social Media
  - Virtual Reality
created: '2024-04-14T00:00:00.000Z'
modified: '2026-05-04'
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: http://apievangelist.com
  - name: Meta Platforms Inc.
    email: developer-support@meta.com
    url: https://about.meta.com
apis:
  - aid: meta:facebook-graph-api-user
    name: Facebook Graph API - User
    description: Retrieve and manage Facebook user profiles, friends lists, and account data using the Graph API User node.
    humanURL: https://developers.facebook.com/docs/graph-api/reference/user/
    tags:
      - Facebook
      - Social
      - Users
  - aid: meta:instagram-graph-api-user
    name: Instagram Graph API - User
    description: Access Instagram user profiles, media, and account information for Business and Creator accounts via the Instagram Graph API.
    humanURL: https://developers.facebook.com/docs/instagram-platform
    tags:
      - Instagram
      - Social
      - Users
  - aid: meta:facebook-graph-api-page
    name: Facebook Graph API - Page
    description: Access and manage Facebook Page settings, content, posts, and metrics using the Graph API Page node.
    humanURL: https://developers.facebook.com/docs/graph-api/reference/page/
    tags:
      - Facebook
      - Pages
      - Social
  - aid: meta:facebook-graph-api-post
    name: Facebook Graph API - Post
    description: Create, read, update, and delete posts on Facebook using the Graph API Post node.
    humanURL: https://developers.facebook.com/docs/graph-api/reference/post/
    tags:
      - Facebook
      - Posts
      - Social
  - aid: meta:facebook-graph-api-group
    name: Facebook Graph API - Group
    description: Manage Facebook Groups including members, posts, and settings using the Graph API Group node.
    humanURL: https://developers.facebook.com/docs/graph-api/reference/group/
    tags:
      - Facebook
      - Groups
      - Social
  - aid: meta:facebook-graph-api-event
    name: Facebook Graph API - Event
    description: Access and manage Facebook Events including details, attendees, and RSVPs using the Graph API Event node.
    humanURL: https://developers.facebook.com/docs/graph-api/reference/event/
    tags:
      - Events
      - Facebook
      - Social
  - aid: meta:facebook-marketing-api
    name: Facebook Marketing API
    description: Create, manage, and optimize advertising campaigns across Facebook, Instagram, and Audience Network programmatically.
    humanURL: https://developers.facebook.com/docs/marketing-api
    tags:
      - Advertising
      - Facebook
      - Marketing
    properties:
      - url: https://developers.facebook.com/docs/marketing-api/reference
        type: Reference
      - url: https://developers.facebook.com/docs/marketing-api/get-started
        type: Getting Started
  - aid: meta:conversions-api
    name: Meta Conversions API
    description: Send web, app, and offline conversion events directly from your server to Meta for improved ad measurement and optimization.
    humanURL: https://developers.facebook.com/docs/marketing-api/conversions-api
    tags:
      - Advertising
      - Analytics
      - Conversions
  - aid: meta:ad-library-api
    name: Meta Ad Library API
    description: Search and retrieve publicly visible ads across Meta platforms for transparency and research purposes via the ads_archive Graph API endpoint.
    humanURL: https://developers.facebook.com/docs/graph-api/reference/ads_archive/
    tags:
      - Advertising
      - Research
      - Transparency
  - aid: meta:whatsapp-cloud-api
    name: WhatsApp Cloud API
    description: Send and receive messages, manage phone numbers, and build messaging experiences on WhatsApp using Meta's cloud-hosted API.
    humanURL: https://developers.facebook.com/docs/whatsapp/cloud-api
    tags:
      - Cloud
      - Messaging
      - WhatsApp
    properties:
      - url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference
        type: Reference
      - url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
        type: Getting Started
  - aid: meta:whatsapp-business-management-api
    name: WhatsApp Business Management API
    description: Manage WhatsApp Business accounts, phone numbers, message templates, and business profiles programmatically.
    humanURL: https://developers.facebook.com/docs/whatsapp/business-management-api
    tags:
      - Business
      - Messaging
      - WhatsApp
  - aid: meta:messenger-platform-api
    name: Messenger Platform API
    description: Build messaging experiences on Facebook Messenger including chatbots, rich media messages, and customer service integrations.
    humanURL: https://developers.facebook.com/docs/messenger-platform
    tags:
      - Chatbots
      - Messaging
      - Social
    properties:
      - url: https://developers.facebook.com/docs/messenger-platform/reference
        type: Reference
  - aid: meta:threads-api
    name: Threads API
    description: Create and manage content, retrieve profiles, and access insights on Meta's Threads social media platform.
    humanURL: https://developers.facebook.com/docs/threads
    tags:
      - Social
      - Social Media
      - Threads
  - aid: meta:instagram-graph-api-content-publishing
    name: Instagram Graph API - Content Publishing
    description: Publish photos, videos, carousels, reels, and stories to Instagram Business and Creator accounts programmatically.
    humanURL: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-facebook-login/content-publishing
    tags:
      - Media
      - Publishing
      - Social
  - aid: meta:instagram-messaging-api
    name: Instagram Messaging API
    description: Send and receive messages on Instagram using the Messenger Platform, enabling customer service and automated messaging for Business accounts.
    humanURL: https://developers.facebook.com/docs/messenger-platform/instagram
    tags:
      - Instagram
      - Messaging
      - Social
  - aid: meta:meta-content-library-api
    name: Meta Content Library API
    description: Programmatic access to the full public content archive from Facebook, Instagram, and Threads for qualified academic and non-profit researchers.
    humanURL: https://developers.facebook.com/docs/content-library-and-api
    tags:
      - Analytics
      - Content
      - Research
  - aid: meta:llama-api
    name: Meta Llama API
    description: Access Meta's Llama large language models including Llama 4 and Llama 3 family for building AI-powered applications via a hosted API.
    humanURL: https://llama.developer.meta.com/docs/overview
    tags:
      - Artificial Intelligence
      - Large Language Models
      - Machine Learning
    properties:
      - url: https://llama.developer.meta.com/docs/quickstart
        type: Getting Started
      - url: https://llama.developer.meta.com/docs/models
        type: Reference
      - url: https://llama.developer.meta.com/docs/sdks
        type: SDKs
      - url: https://llama.developer.meta.com/docs/api-keys
        type: Authentication
common:
  - url: https://developers.facebook.com/?no_redirect=1
    name: Social technologies | Meta for Developers
    type: Portal
  - url: https://developers.facebook.com/docs/
    name: Meta Developer Documentation | Meta APIs, SDKs & Guides
    type: Documentation
  - url: https://developers.facebook.com/docs/graph-api/overview
    name: Graph API Overview
    type: Overview
  - url: https://developers.facebook.com/docs/graph-api/get-started
    name: Get Started
    type: Getting Started
  - url: https://developers.facebook.com/docs/facebook-login
    type: Authentication
  - url: https://developers.facebook.com/docs/access-tokens
    name: Access Tokens
    type: Authentication
  - url: https://developers.facebook.com/docs/graph-api/changelog
    name: Graph API Changelog
    type: Change Log
  - url: https://developers.facebook.com/docs/graph-api/reference
    name: Graph API Reference
    type: Reference
  - url: https://developers.facebook.com/blog/
    name: News for Developers | Facebook Developers
    type: Blog
  - url: https://metastatus.com/
    name: Status
    type: Status
  - url: https://developers.facebook.com/apps/
    name: Applications
    type: Console
  - url: https://developers.facebook.com/
    name: Sign Up - Meta for Developers
    type: Sign Up
  - url: https://developers.facebook.com/terms/
    name: Platform Terms - Meta for Developers
    type: Terms of Service
  - url: https://www.facebook.com/privacy/explanation
    type: Privacy Policy
  - url: https://developers.facebook.com/support/
    name: Developer Support - Meta for Developers
    type: Support
  - url: https://developers.facebook.com/support/bugs/
    name: Platform Bug Reports - Meta for Developers
    type: Bugs
  - url: https://developers.facebook.com/community/
    name: Developer Community Forum - Meta for Developers
    type: Forums
  - url: https://developers.facebook.com/support/faq/
    name: Developer FAQ - Meta for Developers
    type: FAQ
  - url: https://developers.facebook.com/tools/explorer/
    name: Graph API Explorer
    type: Explorer
  - url: https://developers.facebook.com/tools/
    name: Developer Tools - Meta for Developers
    type: Tools
  - url: https://developers.facebook.com/apps/
    name: All Apps - Meta for Developers
    type: Applications
  - url: https://developers.facebook.com/incident/report/
    name: Report an Incident - Meta for Developers
    type: Incident Report
  - url: https://developers.facebook.com/m/signup/
    name: Meta for Developers Newsletter | Meta for Developers
    type: Newsletter
  - url: https://developers.facebook.com/videos/
    name: Videos for Developers
    type: Videos
  - url: https://developers.facebook.com/docs/graph-api/webhooks
    name: Webhooks - Graph API
    type: Webhooks
  - url: https://developers.facebook.com/docs/facebook-login/security
    name: Facebook Login Security
    type: Security
  - url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting/
    name: Rate Limits - Graph API
    type: Rate Limits
  - url: https://developers.facebook.com/docs/graph-api/guides/versioning
    name: Versioning - Graph API
    type: Versioning
  - url: https://developers.facebook.com/docs/graph-api/results
    name: Paginated Results
    type: Pagination
    mediaType: text/html
  - url: https://github.com/facebook
    name: Meta Open Source on GitHub
    type: GitHub Organization
  - url: https://opensource.fb.com/
    name: Meta Open Source
    type: Open Source
  - url: https://stackoverflow.com/questions/tagged/facebook-graph-api
    name: Stack Overflow - Facebook Graph API
    type: Stack Overflow
  - url: https://github.com/facebook/facebook-python-business-sdk
    name: Python SDK
    type: SDKs
  - url: https://github.com/facebook/facebook-nodejs-business-sdk
    name: Node.js SDK
    type: SDKs
  - url: https://github.com/facebook/facebook-php-business-sdk
    name: PHP SDK
    type: SDKs
  - url: https://github.com/facebook/facebook-java-business-sdk
    name: Java SDK
    type: SDKs
  - url: https://github.com/facebook/facebook-ruby-business-sdk
    name: Ruby SDK
    type: SDKs
  - url: https://github.com/facebook/facebook-ios-sdk
    name: iOS SDK
    type: SDKs
  - url: https://github.com/facebook/facebook-android-sdk
    name: Android SDK
    type: SDKs
  - url: json-schema/user.json
    name: User Schema
    type: JSONSchema
    mediaType: application/schema+json
    description: JSON Schema for the Meta Graph API User node covering identity, demographics, profile details, and engagement fields.
  - url: json-schema/page.json
    name: Page Schema
    type: JSONSchema
    mediaType: application/schema+json
    description: JSON Schema for the Meta Graph API Page node covering identity, category, contact information, location, and engagement metrics.
  - url: json-schema/post.json
    name: Post Schema
    type: JSONSchema
    mediaType: application/schema+json
    description: JSON Schema for the Meta Graph API Post node covering content, authorship, privacy, engagement metrics, and attached media.
  - url: json-schema/ad-campaign.json
    name: Ad Campaign Schema
    type: JSONSchema
    mediaType: application/schema+json
    description: JSON Schema for the Meta Marketing API Campaign object covering budget, objective, status, bidding, and scheduling fields.
  - url: json-schema/message.json
    name: Message Schema
    type: JSONSchema
    mediaType: application/schema+json
    description: JSON Schema for Meta messaging across WhatsApp Cloud API, Messenger Platform, and Instagram Messaging covering text, media, template, and interactive message types.
  - url: json-schema/media.json
    name: Media Schema
    type: JSONSchema
    mediaType: application/schema+json
    description: JSON Schema for Meta media objects across Facebook photos/videos and Instagram media including images, videos, carousels, reels, and stories.
  - url: json-ld/meta-context.jsonld
    name: JSON-LD Context
    type: JSON-LD
    mediaType: application/ld+json
    description: JSON-LD context mapping Meta Graph API entities (User, Page, Post, AdCampaign, Message, Media) to schema.org vocabulary for linked data interoperability.
  - data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Free tier.
        description: Facebook only has a single plan.
    name: Plans
    type: Plans
  - url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting/
    data:
      - name: Platform Rate Limits
        type: Platform
        limit: 200
        paths:
          - /v23.0/me
        metric: request
        domains:
          - graph.facebook.com
        timeframe: hours
        operations:
          - getUser
        description: Graph API requests made with an application access token are counted against that apps rate limit. An apps call count is the number of calls it can make during a rolling one hour window and is calculated as Calls within one hour = 200 * Number of Users. The Number of Users is based on the number of unique daily active users an app has. In cases where there are slow periods of daily usage, such as if your app has high activity on weekends but low activity over weekdays, the weekly and monthly active Users are used to calculate the number of Users for your app. Apps with high daily engagement will have higher rate limits than apps with low daily engagement, regardless of the actual number of app installs. Note that this is not a per User limit but a limit on calls made by your app. Any individual User can make more than 200 calls per hour using your app, as long as the total calls from your app does not exceed the app maximum. For example, if your app has 100 Users, your app can make 20,000 calls per hour. However, your top ten most engaged Users could make 19,000 of those calls.
        userMultiplied: true
    name: Rate Limits - Graph API
    type: Rate Limits
    description: Working to build as machine-readable schema.
  - url: https://developers.facebook.com/docs/graph-api/guides/versioning
    data:
      type: Semantic
      parameter: path
    name: Versioning - Graph API
    type: Versioning
    description: Working to build as machine-readable schema.
  - data:
      $id: https://example.com/offset-pagination.schema.json
      type: object
      title: Offset-based Pagination Response
      $schema: https://json-schema.org/draft/2020-12/schema
      examples:
        - data:
            - id: '123'
              name: Item 26
            - id: '456'
              name: Item 27
            - id: '789'
              name: Item 28
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=50
            previous: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=0
        - data:
            - id: '111'
              name: First item
            - id: '222'
              name: Second item
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=25
        - data:
            - id: '999'
              name: Last item
          paging:
            previous: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=75
        - data: []
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=50
      required:
        - data
        - paging
      properties:
        data:
          type: array
          items:
            description: Individual data item (schema depends on specific endpoint)
          description: Array containing the endpoint data items for the current offset range
        paging:
          type: object
          properties:
            next:
              type: string
              format: uri
              description: Graph API endpoint URL for the next page of data with updated 'offset' parameter. Absence indicates last page.
            previous:
              type: string
              format: uri
              description: Graph API endpoint URL for the previous page of data with updated 'offset' parameter. Absence indicates first page.
          description: Pagination metadata and navigation links with offset-based parameters
          minProperties: 1
          additionalProperties: false
      description: JSON schema for offset-based pagination responses using numeric offsets in Graph API
      additionalProperties: false
    name: Offset-based Pagination
    type: Pagination
    mediaType: application/schema+json
    description: Still need to figure out how to reference in OpenAPI.
  - data:
      $id: https://example.com/time-pagination.schema.json
      type: object
      title: Facebook Time-based Pagination Response
      $schema: https://json-schema.org/draft/2020-12/schema
      examples:
        - data:
            - id: '123'
              message: Example post
              created_time: 2013-04-02T07:42:34+0000
            - id: '456'
              message: Another post
              created_time: 2013-03-30T15:29:34+0000
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774
            previous: https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754
        - data:
            - id: '789'
              message: First page example
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774
        - data:
            - id: '999'
              message: Last page example
          paging:
            previous: https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754
      required:
        - data
        - paging
      properties:
        data:
          type: array
          items:
            description: Individual data item (schema depends on specific endpoint)
          description: Array containing the endpoint data items for the current time range
        paging:
          type: object
          properties:
            next:
              type: string
              format: uri
              description: Graph API endpoint URL for the next page of data with 'until' timestamp parameter
            previous:
              type: string
              format: uri
              description: Graph API endpoint URL for the previous page of data with 'since' timestamp parameter
          description: Pagination metadata and navigation links with time-based parameters
          minProperties: 1
          additionalProperties: false
      description: JSON schema for time-based pagination responses using Unix timestamps in Graph API
      additionalProperties: false
    name: Time-based Pagination
    type: Pagination
    mediaType: application/schema+json
    description: Still need to figure out how to reference in OpenAPI.
  - data:
      $id: https://example.com/cursor-pagination.schema.json
      type: object
      title: Facebook Cursor-based Pagination Response
      $schema: https://json-schema.org/draft/2020-12/schema
      examples:
        - data:
            - id: '123'
              name: Example Item 1
            - id: '456'
              name: Example Item 2
          paging:
            next: https://graph.facebook.com/{your-user-id}/albums?limit=25&after=MTAxNTExOTQ1MjAwNzI5NDE=
            cursors:
              after: MTAxNTExOTQ1MjAwNzI5NDE=
              before: NDMyNzQyODI3OTQw
            previous: https://graph.facebook.com/{your-user-id}/albums?limit=25&before=NDMyNzQyODI3OTQw
      required:
        - data
        - paging
      properties:
        data:
          type: array
          items:
            description: Individual data item (schema depends on specific endpoint)
          description: Array containing the endpoint data items for the current page
        paging:
          type: object
          required:
            - cursors
          properties:
            next:
              type: string
              format: uri
              description: Graph API endpoint URL for the next page of data. Absence indicates last page.
            cursors:
              type: object
              required:
                - after
                - before
              properties:
                after:
                  type: string
                  pattern: ^[A-Za-z0-9+/=]+$
                  description: Cursor pointing to the end of the current page of data
                before:
                  type: string
                  pattern: ^[A-Za-z0-9+/=]+$
                  description: Cursor pointing to the start of the current page of data
              description: Cursor strings marking the boundaries of the current page
              additionalProperties: false
            previous:
              type: string
              format: uri
              description: Graph API endpoint URL for the previous page of data. Absence indicates first page.
          description: Pagination metadata and navigation links
          additionalProperties: false
      description: JSON schema for cursor-based pagination responses used in Graph API
      additionalProperties: false
    name: Cursor-based Pagination
    type: Pagination
    mediaType: application/schema+json
    description: Still need to figure out how to reference in OpenAPI.
  - type: Features
    data:
      - 'Meta (Facebook + Instagram + WhatsApp + Threads): hundreds of services across Social + Messaging + Ads'
      - 'Detailed pricing: see https://developers.facebook.com/docs/marketing-api'
      - 'Service: Facebook Graph API'
      - 'Service: Marketing API'
      - 'Service: Instagram Graph API'
      - 'Service: Instagram Basic Display API'
      - 'Service: WhatsApp Business Platform / Cloud API'
      - 'Service: Threads API'
      - 'Service: Messenger Platform'
      - 'Service: Workplace by Meta API (sunset)'
      - 'Service: Meta Conversion API (server-side events)'
    sources:
      - https://developers.facebook.com/docs/marketing-api
      - https://focus.finops.org/
    updated: '2026-05-04'
---
