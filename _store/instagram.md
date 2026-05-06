---
aid: instagram
name: Instagram
description: Instagram is a photo and video sharing social networking platform owned by Meta. The Instagram APIs allow developers to build integrations with Instagram Business and Creator accounts for content publishing, media management, comment moderation, hashtag discovery, insights and analytics, messaging, and embedding. Available through the Meta Developer Platform with Facebook Login or Instagram Login authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Instagram
  - Meta
  - Photos
  - Social Media
  - Videos
  - Content Publishing
apis:
  - aid: instagram:instagram-api-with-instagram-login
    name: Instagram API with Instagram Login
    description: The Instagram API with Instagram Login enables access to Instagram Business and Creator accounts using Instagram native login flow. Supports media management, content publishing, comment handling, mention identification, messaging, insights, and webhooks.
    humanURL: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login
    baseURL: https://graph.instagram.com
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login
      - type: GettingStarted
        url: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/getting-started
      - type: APIReference
        url: https://developers.facebook.com/docs/instagram-api/reference
      - type: Authentication
        url: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/business-login
      - type: OpenAPI
        url: openapi/instagram-graph-api.yaml
    tags:
      - Content Publishing
      - Instagram Login
      - Media
      - Messaging
      - Social Media
  - aid: instagram:instagram-api-with-facebook-login
    name: Instagram API with Facebook Login
    description: The Instagram API with Facebook Login accesses Instagram Business and Creator accounts linked to Facebook Pages. Enables media retrieval and publishing, comment management, mention identification, hashtag-based media discovery, insights, and business metadata.
    humanURL: https://developers.facebook.com/docs/instagram-api
    baseURL: https://graph.facebook.com
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/instagram-api/
      - type: GettingStarted
        url: https://developers.facebook.com/docs/instagram-api/getting-started
      - type: APIReference
        url: https://developers.facebook.com/docs/instagram-api/reference
      - type: Authentication
        url: https://developers.facebook.com/docs/instagram-api/overview#authentication
      - type: ChangeLog
        url: https://developers.facebook.com/docs/instagram-api/changelog
      - type: OpenAPI
        url: openapi/instagram-graph-api.yaml
    tags:
      - Content Publishing
      - Facebook Login
      - Hashtags
      - Media
      - Social Media
  - aid: instagram:instagram-messaging-api
    name: Instagram Messaging API
    description: The Messenger API support for Instagram consolidates Instagram and Facebook Page messaging into a unified platform. Enables businesses and creators to manage conversations, send and receive messages, and handle messaging automation across Instagram Direct.
    humanURL: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api
    baseURL: https://graph.instagram.com
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api
    tags:
      - Direct Messages
      - Messaging
      - Social Media
  - aid: instagram:instagram-oembed-api
    name: Instagram oEmbed API
    description: The Instagram oEmbed endpoint returns HTML and metadata for embedding Instagram photos, videos, reels, and carousels on third-party websites using the standard oEmbed protocol.
    humanURL: https://developers.facebook.com/docs/instagram-platform/oembed
    baseURL: https://graph.facebook.com
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/instagram-platform/oembed
    tags:
      - Embedding
      - oEmbed
      - Social Media
common:
  - type: Portal
    url: https://developers.facebook.com/docs/instagram-platform
  - type: GettingStarted
    url: https://developers.facebook.com/docs/instagram-api/getting-started
  - type: Authentication
    url: https://developers.facebook.com/docs/instagram-api/overview#authentication
  - type: TermsOfService
    url: https://developers.facebook.com/terms
  - type: PrivacyPolicy
    url: https://www.facebook.com/privacy/explanation
  - type: StatusPage
    url: https://developers.facebook.com/status/
  - type: ChangeLog
    url: https://developers.facebook.com/docs/instagram-api/changelog
  - type: Support
    url: https://developers.facebook.com/support
  - type: Blog
    url: https://developers.facebook.com/blog/
  - type: GitHubOrganization
    url: https://github.com/fbsamples
  - type: Features
    data:
      - name: Content Publishing
        description: Publish photos, videos, reels, carousels, and stories to Instagram Business and Creator accounts programmatically.
      - name: Media Management
        description: Retrieve, manage, and organize published media including photos, videos, stories, and albums.
      - name: Comment Moderation
        description: Read, reply to, hide, and delete comments on Instagram media for brand safety and engagement.
      - name: Hashtag Discovery
        description: Search for hashtags and discover top and recent media associated with specific hashtags.
      - name: Mention Tracking
        description: Identify and retrieve media where your account has been mentioned by other Instagram users.
      - name: Insights and Analytics
        description: Access account-level and media-level metrics for reach, impressions, engagement, and audience demographics.
      - name: Instagram Direct Messaging
        description: Send and receive messages through Instagram Direct for customer service and business communication.
      - name: Stories Publishing
        description: Publish ephemeral story content including photos and videos that disappear after 24 hours.
      - name: Reels Publishing
        description: Create and publish short-form video content as Instagram Reels.
      - name: oEmbed
        description: Embed Instagram posts, reels, and videos on third-party websites using the standard oEmbed protocol.
      - name: Webhooks
        description: Receive real-time notifications for comments, mentions, messages, and story insights via webhooks.
      - name: Private Replies
        description: Send private direct messages in response to public comments on your Instagram media.
  - type: UseCases
    data:
      - name: Social Media Management
        description: Automate content publishing, scheduling, and media management across Instagram accounts.
      - name: Brand Monitoring
        description: Track mentions, comments, and hashtags to monitor brand sentiment and engagement.
      - name: Customer Service
        description: Manage Instagram Direct conversations for customer support and business inquiries.
      - name: Analytics and Reporting
        description: Retrieve insights and metrics for measuring content performance and audience growth.
      - name: Content Curation
        description: Discover and curate content through hashtag search and mention tracking.
      - name: E-commerce Integration
        description: Connect product catalogs and shopping features with Instagram content for social commerce.
      - name: Influencer Marketing
        description: Track creator account metrics, media performance, and audience insights for influencer campaigns.
      - name: Website Embedding
        description: Embed Instagram posts, reels, and galleries on websites and blogs using oEmbed.
  - type: Integrations
    data:
      - name: Facebook
        description: Unified management of Instagram and Facebook content, messaging, and advertising through the Meta platform.
      - name: Meta Business Suite
        description: Centralized dashboard for managing Instagram and Facebook business accounts, content, and insights.
      - name: WhatsApp
        description: Cross-platform messaging through Meta unified messaging infrastructure.
      - name: Webhooks
        description: Real-time event notifications for comments, mentions, messages, and story insights.
  - type: Solutions
    data:
      - name: Instagram API with Instagram Login
        description: Native Instagram authentication for Business and Creator accounts with full API access.
      - name: Instagram API with Facebook Login
        description: Facebook Page-linked authentication for Instagram Business accounts with hashtag discovery.
      - name: Instagram Messaging
        description: Unified messaging across Instagram Direct and Facebook Messenger for business communication.
      - name: Instagram Embedding
        description: oEmbed and embed tools for displaying Instagram content on third-party websites.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
