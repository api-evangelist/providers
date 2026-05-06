---
aid: twitter
name: X (Twitter)
description: X (formerly Twitter) is a social media platform providing APIs for accessing and integrating with posts, users, spaces, direct messages, lists, media, trends, and real-time streaming data. The X API enables developers to build applications that read and write X data, manage advertising campaigns, and subscribe to real-time activity events. Available through pay-per-use credit-based pricing with enterprise options for high-volume access.
type: Index
image: https://abs.twimg.com/favicons/twitter.ico
url: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/apis.yml
created: '2025-07-29'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Social Media
  - Microblogging
  - Real-Time Data
  - Streaming
  - Advertising
  - Content
apis:
  - aid: twitter:x-api
    name: X API
    description: The core X API providing programmatic access to posts, users, spaces, lists, direct messages, bookmarks, likes, reposts, follows, blocks, mutes, trends, communities, and compliance data. Supports post creation, search (recent and full-archive), timelines, filtered streams, sampled streams, and real-time data access. Uses OAuth 2.0 with PKCE or OAuth 1.0a authentication with credit-based pay-per-use pricing.
    image: https://abs.twimg.com/favicons/twitter.ico
    humanURL: https://docs.x.com/x-api
    baseURL: https://api.x.com/2
    properties:
      - type: Documentation
        url: https://docs.x.com/x-api
      - type: GettingStarted
        url: https://docs.x.com/x-api/getting-started/make-your-first-request
      - type: APIReference
        url: https://docs.x.com/x-api
      - type: Authentication
        url: https://docs.x.com/resources/fundamentals/authentication
      - type: RateLimits
        url: https://docs.x.com/x-api/fundamentals/rate-limits
      - type: SDK
        url: https://docs.x.com/sdks-and-tools/python-xdk
        title: Python XDK
      - type: SDK
        url: https://docs.x.com/sdks-and-tools/typescript-xdk
        title: TypeScript XDK
      - type: OpenAPI
        url: openapi/x-api-openapi.json
    tags:
      - Posts
      - Users
      - Spaces
      - Lists
      - Direct Messages
      - Streaming
      - Search
      - Timelines
  - aid: twitter:x-ads-api
    name: X Ads API
    description: The X Ads API enables programmatic management of advertising campaigns on the X platform including campaign creation and scheduling, custom audience building, creative management (draft posts, cards, media), and analytics retrieval for campaign performance metrics. Supports both synchronous and asynchronous analytics endpoints for reporting.
    image: https://abs.twimg.com/favicons/twitter.ico
    humanURL: https://docs.x.com/x-ads-api
    baseURL: https://ads-api.x.com
    properties:
      - type: Documentation
        url: https://docs.x.com/x-ads-api
      - type: GettingStarted
        url: https://docs.x.com/x-ads-api/getting-started/create-a-campaign
      - type: RateLimits
        url: https://docs.x.com/x-ads-api/fundamentals/rate-limiting
      - type: PostmanCollection
        url: postman/x-ads-api-postman-collection.json
    tags:
      - Advertising
      - Campaigns
      - Analytics
      - Audiences
      - Creatives
  - aid: twitter:x-activity-api
    name: X Activity API
    description: The X Activity API provides real-time activity event subscriptions with sub-second delivery via streaming or webhooks. Subscribe to profile updates, follows, likes, reposts, and other user activity events. Recently exited beta and is now generally available.
    image: https://abs.twimg.com/favicons/twitter.ico
    humanURL: https://docs.x.com/x-activity-api
    baseURL: https://api.x.com
    properties:
      - type: Documentation
        url: https://docs.x.com/x-activity-api
    tags:
      - Activity
      - Events
      - Real-Time
      - Streaming
      - Webhooks
common:
  - type: Portal
    url: https://developer.x.com/en/portal/dashboard
  - type: GettingStarted
    url: https://docs.x.com/x-api/getting-started/make-your-first-request
  - type: Console
    url: https://developer.x.com/en/portal/dashboard
  - type: SignUp
    url: https://developer.x.com/en/portal/petition/essential/basic-info
  - type: Authentication
    url: https://docs.x.com/resources/fundamentals/authentication
  - type: SDK
    url: https://docs.x.com/sdks-and-tools/python-xdk
    title: Python XDK
  - type: SDK
    url: https://docs.x.com/sdks-and-tools/typescript-xdk
    title: TypeScript XDK
  - type: CLI
    url: https://docs.x.com/sdks-and-tools/xurl
    title: xurl
  - type: Pricing
    url: https://developer.x.com/en/portal/petition/essential/basic-info
  - type: TermsOfService
    url: https://developer.x.com/en/developer-terms/agreement-and-policy
  - type: PrivacyPolicy
    url: https://x.com/en/privacy
  - type: StatusPage
    url: https://api.twitterstat.us/
  - type: Support
    url: https://devcommunity.x.com/
  - type: Blog
    url: https://blog.x.com/developer
  - type: ReleaseNotes
    url: https://docs.x.com/changelog
  - type: GitHubOrganization
    url: https://github.com/xdevplatform
  - type: GitHubRepository
    url: https://github.com/xdevplatform/xdk-python
    description: Auto-generated Python SDK for the X API.
  - type: GitHubRepository
    url: https://github.com/xdevplatform/xdk-typescript
    description: Auto-generated TypeScript SDK for the X API.
  - type: GitHubRepository
    url: https://github.com/xdevplatform/xurl
    description: Official CLI for the X API with built-in authentication.
  - type: GitHubRepository
    url: https://github.com/xdevplatform/xdk
    description: SDK generator for the X APIs producing auto-generated client libraries.
  - type: GitHubRepository
    url: https://github.com/xdevplatform/twitter-api-java-sdk
    description: Official Java SDK for the Twitter/X API.
  - type: GitHubRepository
    url: https://github.com/xdevplatform/twitter-ruby-ads-sdk
    description: Official Ruby SDK for the Twitter/X Ads API.
  - type: Tools
    url: https://github.com/xdevplatform/xmcp
    description: MCP server for the X API enabling AI agent integration.
  - type: Sandbox
    url: https://github.com/xdevplatform/playground
    description: Standalone local HTTP server simulating the X API v2 for testing and development with interactive web UI.
  - type: CodeExamples
    url: https://github.com/xdevplatform/samples
    description: Official sample code for X API v2 endpoints.
  - type: CodeExamples
    url: https://github.com/xdevplatform/xchat-bot-python
    description: Example DM reply bot in Python for X encrypted chat system.
  - type: PostmanWorkspace
    url: https://docs.x.com/sdks-and-tools/postman
  - type: PostmanCollection
    url: postman/x-api-v2-postman-collection.json
  - type: X
    url: https://x.com/XDevelopers
  - type: Features
    data:
      - name: Post Management
        description: Create, delete, edit, repost, quote, like, and bookmark posts programmatically.
      - name: Real-Time Streaming
        description: Access filtered streams, sampled streams, firehose, and language-specific streams for real-time post data.
      - name: Full-Archive Search
        description: Search the complete archive of public posts with advanced query operators and date filtering.
      - name: User Lookup and Management
        description: Look up users by ID or username, manage follows, blocks, mutes, and retrieve user metrics.
      - name: Spaces
        description: Discover and look up live audio Spaces with host, speaker, and listener data.
      - name: Direct Messages
        description: Send and receive direct messages, create conversations, and manage participants.
      - name: Lists
        description: Create, manage, and query lists including membership, followers, and pinned lists.
      - name: Trends
        description: Access personalized and geographic trending topics.
      - name: Media Upload
        description: Upload images, videos, and large files using chunked upload with metadata and subtitle support.
      - name: Compliance
        description: Access compliance streams and batch jobs for data deletion and user protection events.
      - name: Communities and Community Notes
        description: Access community data and community notes for collaborative fact-checking.
      - name: Ad Campaign Management
        description: Programmatically create, schedule, and manage advertising campaigns with targeting and budget controls.
  - type: UseCases
    data:
      - name: Social Listening
        description: Monitor brand mentions, sentiment, and conversations in real-time using filtered streams and search endpoints.
      - name: Content Publishing
        description: Automate post creation, scheduling, and thread publishing for social media management platforms.
      - name: Analytics and Reporting
        description: Retrieve post metrics, user engagement data, and campaign performance for business intelligence.
      - name: Bot Development
        description: Build automated accounts that respond to mentions, post updates, or provide customer service.
      - name: Research and Academic Analysis
        description: Access full-archive search and streaming data for social media research and trend analysis.
      - name: Advertising Automation
        description: Programmatically manage ad campaigns, audiences, creatives, and bidding strategies at scale.
      - name: Real-Time Event Monitoring
        description: Track live events, breaking news, and trending topics with streaming APIs and trend endpoints.
      - name: Community Management
        description: Manage followers, lists, and direct messages for community engagement and moderation.
  - type: Integrations
    data:
      - name: Postman
        description: Official Postman collections for exploring and testing X API endpoints interactively.
      - name: MCP Servers
        description: Integration with AI tools and agents through Model Context Protocol servers.
      - name: Webhook Delivery
        description: Real-time event delivery via webhooks for the Activity API.
  - type: Solutions
    data:
      - name: X API Pay-Per-Use
        description: Credit-based pricing with no commitments. Pay only for what you use with access to core X API endpoints.
      - name: X API Enterprise
        description: High-volume access with custom rate limits, dedicated account management, full firehose, and premium support.
      - name: X Ads API
        description: Advertising platform API for campaign management, audience targeting, creative management, and analytics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
