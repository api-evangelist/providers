---
aid: facebook-business-manager
name: Facebook Business Manager
description: APIs for managing Facebook Business accounts, advertising, pages, and assets across the Meta platform family. Facebook Business Manager exposes a deep catalog of Graph API surfaces for marketing, pages, conversions, business asset management, Instagram, insights, Messenger, catalogs, live video, Threads, and the WhatsApp Business Platform, all governed through a shared authentication and access model.
image: https://www.facebook.com/images/fb_icon_325x325.png
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
url: https://raw.githubusercontent.com/api-evangelist/facebook-business-manager/refs/heads/main/apis.yml
apis:
  - aid: facebook-business-manager:facebook-marketing-api
    name: Facebook Marketing API
    description: Create and manage ad campaigns, analyze performance, and automate advertising workflows.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/marketing-apis
    baseURL: https://graph.facebook.com/v18.0
    tags:
      - Ads
      - Advertising
      - Campaigns
      - Marketing
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/marketing-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/facebook-business-manager/refs/heads/main/openapi/facebook-marketing-openapi.yml
      - type: Authentication
        url: https://developers.facebook.com/docs/marketing-api/authentication
      - type: Change Log
        url: https://developers.facebook.com/docs/graph-api/changelog
      - type: Rate Limits
        url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting
      - type: Getting Started
        url: https://developers.facebook.com/docs/marketing-api/get-started
      - type: Reference
        url: https://developers.facebook.com/docs/marketing-api/reference
      - type: SDKs
        url: https://developers.facebook.com/docs/business-sdk/getting-started
  - aid: facebook-business-manager:facebook-pages-api
    name: Facebook Pages API
    description: Manage Facebook Pages, posts, comments, and engagement.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/pages
    baseURL: https://graph.facebook.com/v18.0
    tags:
      - Content
      - Pages
      - Publishing
      - Social Media
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/pages-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/facebook-business-manager/refs/heads/main/openapi/facebook-pages-openapi.yml
      - type: Getting Started
        url: https://developers.facebook.com/docs/pages/getting-started
      - type: Reference
        url: https://developers.facebook.com/docs/pages-api/overview
      - type: Authentication
        url: https://developers.facebook.com/docs/pages/access-tokens
  - name: Facebook Conversions API
    description: Send web and offline events directly to Facebook for improved tracking and attribution.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/marketing-api/conversions-api
    baseURL: https://graph.facebook.com/v18.0
    tags:
      - Attribution
      - Conversions
      - Events
      - Tracking
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/marketing-api/conversions-api
      - type: Implementation Guide
        url: https://developers.facebook.com/docs/marketing-api/conversions-api/get-started
      - type: Reference
        url: https://developers.facebook.com/docs/marketing-api/conversions-api/parameters
      - type: SDKs
        url: https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api
  - name: Facebook Business Asset API
    description: Manage business assets including pixels, catalogs, and custom audiences.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/marketing-api/business-asset-management
    baseURL: https://graph.facebook.com/v18.0
    tags:
      - Assets
      - Audiences
      - Catalogs
      - Pixels
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/marketing-api/business-asset-management
      - type: Reference
        url: https://developers.facebook.com/docs/marketing-api/business-asset-management/get-started
  - name: Facebook Instagram API
    description: Manage Instagram Business and Creator accounts through Business Manager.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/instagram-api
    baseURL: https://graph.facebook.com/v18.0
    tags:
      - Content
      - Instagram
      - Media
      - Social Media
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/instagram-api
      - type: Getting Started
        url: https://developers.facebook.com/docs/instagram-api/getting-started
      - type: Reference
        url: https://developers.facebook.com/docs/instagram-api/reference
      - type: Authentication
        url: https://developers.facebook.com/docs/instagram-api/getting-started#authentication
  - name: Facebook Insights API
    description: Access performance metrics and analytics data for Facebook Pages, ad campaigns, and content. The Insights API provides detailed reporting on engagement, reach, impressions, and audience demographics for businesses managing their Meta presence.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/platforminsights
    baseURL: https://graph.facebook.com/v25.0
    tags:
      - Analytics
      - Insights
      - Metrics
      - Reporting
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/platforminsights
      - type: Reference
        url: https://developers.facebook.com/docs/graph-api/reference/page/insights
  - name: Facebook Messenger Platform API
    description: Build conversational experiences on the Messenger platform. The Messenger Platform API enables businesses to send and receive messages, create automated bots, manage customer interactions, and integrate rich media and quick replies into chat workflows.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/messenger-platform
    baseURL: https://graph.facebook.com/v25.0
    tags:
      - Bots
      - Chat
      - Customer Service
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/messenger-platform
      - type: Getting Started
        url: https://developers.facebook.com/docs/messenger-platform/getting-started
      - type: Reference
        url: https://developers.facebook.com/docs/messenger-platform/reference
  - name: Facebook Catalog API
    description: Create and manage product catalogs for use in dynamic ads, shops, and commerce experiences across Meta platforms. The Catalog API allows businesses to upload product information, manage inventory feeds, and synchronize product data for advertising and shopping features.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/marketing-api/catalog
    baseURL: https://graph.facebook.com/v25.0
    tags:
      - Catalogs
      - Commerce
      - Products
      - Shopping
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/marketing-api/catalog
      - type: Reference
        url: https://developers.facebook.com/docs/marketing-api/catalog/reference
      - type: Getting Started
        url: https://developers.facebook.com/docs/marketing-api/catalog/get-started
  - name: Facebook Live Video API
    description: Stream live video content directly to Facebook Pages, user profiles, and groups. The Live Video API enables scheduling broadcasts, managing live streams, interacting with audiences through comments, and retrieving post-broadcast analytics.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/videos/live-video
    baseURL: https://graph.facebook.com/v25.0
    tags:
      - Broadcasting
      - Live Streaming
      - Media
      - Video
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/videos/live-video
      - type: Reference
        url: https://developers.facebook.com/docs/graph-api/reference/live-video
      - type: Getting Started
        url: https://developers.facebook.com/docs/videos/live-video/getting-started
  - name: Facebook Threads API
    description: Publish content, manage replies, and retrieve analytics on the Threads platform. The Threads API provides programmatic access for creating text posts, sharing media, managing conversations, and accessing engagement metrics for Threads profiles.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/threads
    baseURL: https://graph.threads.net/v25.0
    tags:
      - Content
      - Publishing
      - Social Media
      - Threads
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/threads
      - type: Getting Started
        url: https://developers.facebook.com/docs/threads/get-started
      - type: Reference
        url: https://developers.facebook.com/docs/threads/threads-api
  - name: Facebook WhatsApp Business Platform API
    description: Send and receive messages, manage business profiles, and automate customer communications through the WhatsApp Business Platform. The Cloud API enables businesses to integrate WhatsApp messaging into their applications for customer support, notifications, and transactional communications.
    image: https://www.facebook.com/images/fb_icon_325x325.png
    humanURL: https://developers.facebook.com/docs/whatsapp
    baseURL: https://graph.facebook.com/v25.0
    tags:
      - Customer Service
      - Messaging
      - Notifications
      - WhatsApp
    properties:
      - type: Documentation
        url: https://developers.facebook.com/docs/whatsapp/cloud-api
      - type: Getting Started
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
      - type: Reference
        url: https://developers.facebook.com/docs/whatsapp/cloud-api/reference
common:
  - type: Portal
    url: https://developers.facebook.com
  - type: Developer Console
    url: https://developers.facebook.com/apps
  - type: Business Manager
    url: https://business.facebook.com
  - type: Support
    url: https://developers.facebook.com/support
  - type: Status
    url: https://developers.facebook.com/status
  - type: Terms of Service
    url: https://developers.facebook.com/terms
  - type: Privacy Policy
    url: https://www.facebook.com/privacy/explanation
  - type: Getting Started
    url: https://developers.facebook.com/docs/development/create-an-app
  - type: Documentation
    url: https://developers.facebook.com/docs
  - type: Authentication
    url: https://developers.facebook.com/docs/facebook-login/guides/access-tokens
  - type: Rate Limits
    url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting
  - type: Change Log
    url: https://developers.facebook.com/docs/graph-api/changelog
  - type: Blog
    url: https://developers.meta.com/blog/
  - type: Website
    url: https://www.meta.com
  - type: Sign Up
    url: https://developers.facebook.com/async/registration/
  - type: SDKs
    url: https://developers.facebook.com/docs/business-sdk/getting-started
  - type: GitHub Organization
    url: https://github.com/facebook
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/facebook-graph-api
  - type: Community
    url: https://developers.facebook.com/community
  - type: Developer Tools
    url: https://developers.facebook.com/tools/explorer
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Advertising
  - Analytics
  - Business Management
  - Marketing
  - Social Media
---
