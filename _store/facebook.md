---
aid: facebook
name: Facebook
description: Facebook is Meta's social networking platform providing APIs for developers to integrate with Facebook's ecosystem. The Facebook Graph API is the primary way to read and write data to the Facebook social graph. Meta also provides APIs for marketing and advertising, Instagram content management, Messenger bots, Threads publishing, and WhatsApp business messaging.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advertising
  - Content Publishing
  - Messaging
  - Social Media
  - Social Networking
url: https://developers.facebook.com
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
position: Consumer
access: 3rd-Party
apis:
  - aid: facebook:facebook-graph-api
    name: Facebook Graph API
    description: The primary way to read and write data to the Facebook social graph, providing access to user profiles, posts, pages, photos, videos, comments, and social interactions. Supports nodes, edges, and fields for flexible data access.
    humanURL: https://developers.facebook.com/docs/graph-api
    baseURL: https://graph.facebook.com
    tags:
      - Comments
      - Graph
      - Pages
      - Photos
      - Posts
      - Social
      - Users
      - Videos
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/graph-api/overview
      - type: APIReference
        url: https://developers.facebook.com/docs/graph-api/reference
      - type: Authentication
        url: https://developers.facebook.com/docs/facebook-login/access-tokens
      - type: OpenAPI
        url: openapi/facebook-graph-api.yaml
  - aid: facebook:facebook-marketing-api
    name: Facebook Marketing API
    description: Programmatically manage Facebook ad campaigns, ad sets, ad creatives, Custom Audiences, and advertising reports. Access performance insights and automate campaign optimization at scale.
    humanURL: https://developers.facebook.com/docs/marketing-apis
    baseURL: https://graph.facebook.com
    tags:
      - Ad Campaigns
      - Advertising
      - Audiences
      - Insights
      - Marketing
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/marketing-api
      - type: APIReference
        url: https://developers.facebook.com/docs/marketing-api/reference
      - type: OpenAPI
        url: openapi/facebook-marketing-api.yaml
  - aid: facebook:instagram-api
    name: Instagram API
    description: Manage Instagram Business and Creator account content including publishing media, retrieving posts, managing comments, discovering mentions, and accessing account insights for analytics.
    humanURL: https://developers.facebook.com/docs/instagram-platform
    baseURL: https://graph.facebook.com
    tags:
      - Content Management
      - Instagram
      - Media
      - Social Media
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/instagram-platform
      - type: OpenAPI
        url: openapi/facebook-instagram-api.yaml
  - aid: facebook:messenger-platform-api
    name: Messenger Platform API
    description: Build messaging experiences on Facebook Messenger and Instagram Direct. Send and receive messages, create bot interactions, use templates and webviews, manage conversation routing, and integrate NLP capabilities.
    humanURL: https://developers.facebook.com/docs/messenger-platform
    baseURL: https://graph.facebook.com
    tags:
      - Bots
      - Chat
      - Messaging
      - Messenger
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/messenger-platform
      - type: OpenAPI
        url: openapi/facebook-messenger-api.yaml
  - aid: facebook:threads-api
    name: Threads API
    description: Publish and manage content on Threads, Meta's text-based social platform. Create posts and carousels, retrieve and moderate replies, access insights, and manage creator profiles at scale.
    humanURL: https://developers.facebook.com/docs/threads
    baseURL: https://graph.threads.net
    tags:
      - Content Publishing
      - Social Media
      - Threads
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/threads
      - type: OpenAPI
        url: openapi/facebook-threads-api.yaml
  - aid: facebook:whatsapp-business-api
    name: WhatsApp Business API
    description: Send and receive messages through WhatsApp Business Platform. Support text, media, templates, interactive messages, and manage business profiles for customer communication at scale.
    humanURL: https://developers.facebook.com/docs/whatsapp
    baseURL: https://graph.facebook.com
    tags:
      - Business Messaging
      - Customer Communication
      - WhatsApp
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp
      - type: OpenAPI
        url: openapi/facebook-whatsapp-api.yaml
common:
  - type: Portal
    url: https://developers.facebook.com
  - type: GettingStarted
    url: https://developers.facebook.com/docs/development/create-an-app
  - type: ChangeLog
    url: https://developers.facebook.com/docs/graph-api/changelog
  - type: StatusPage
    url: https://developers.facebook.com/status
  - type: TermsOfService
    url: https://developers.facebook.com/terms
  - type: PrivacyPolicy
    url: https://developers.facebook.com/policy
  - type: RateLimits
    url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting
  - type: GitHubOrganization
    url: https://github.com/facebook
  - type: Blog
    url: https://developers.facebook.com/blog
  - type: Support
    url: https://developers.facebook.com/support
  - type: FAQ
    url: https://developers.facebook.com/docs/development/faq
  - type: Errors
    url: https://developers.facebook.com/docs/graph-api/guides/error-handling
  - type: Features
    data:
      - name: Graph API
        description: HTTP-based API for reading and writing to the Facebook social graph with nodes, edges, and fields.
      - name: Webhooks
        description: Real-time notifications when changes occur to data your app has access to.
      - name: Batch Requests
        description: Send multiple API calls in a single HTTP request for improved performance.
      - name: Access Tokens
        description: OAuth 2.0 access tokens for user, page, app, and client authentication flows.
      - name: Facebook Login
        description: Authentication system allowing users to log into apps with their Facebook credentials.
      - name: Meta Pixel
        description: Analytics tool for measuring ad effectiveness and tracking website visitor actions.
      - name: Conversions API
        description: Server-side event tracking for ad measurement without browser dependencies.
  - type: UseCases
    data:
      - name: Social Media Management
        description: Manage pages, publish content, and engage with audiences across Facebook and Instagram.
      - name: Advertising Automation
        description: Automate ad campaign creation, optimization, and reporting at scale.
      - name: Customer Messaging
        description: Build conversational experiences on Messenger and WhatsApp for customer support and engagement.
      - name: Content Publishing
        description: Publish and schedule content across Facebook, Instagram, and Threads platforms.
      - name: Analytics and Insights
        description: Access performance data and audience insights across Meta platforms.
      - name: E-Commerce Integration
        description: Integrate product catalogs and shopping experiences with Facebook and Instagram shops.
  - type: Integrations
    data:
      - name: Shopify
        description: Connect Shopify stores with Facebook and Instagram shops for social commerce.
      - name: WordPress
        description: Facebook social plugins and login integration for WordPress sites.
      - name: Salesforce
        description: Sync Facebook lead ads and audiences with Salesforce CRM.
      - name: HubSpot
        description: Connect Facebook advertising and messaging with HubSpot marketing automation.
      - name: Zapier
        description: Automate workflows between Facebook and thousands of other apps.
  - type: SpectralRules
    url: rules/facebook-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/facebook-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/social-media-management.yaml
    title: Social Media Management
  - type: NaftikoCapability
    url: capabilities/advertising-and-marketing.yaml
    title: Advertising and Marketing
  - type: NaftikoCapability
    url: capabilities/messaging-and-communication.yaml
    title: Messaging and Communication
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
