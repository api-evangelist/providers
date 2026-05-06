---
aid: braze
url: https://raw.githubusercontent.com/api-evangelist/braze/refs/heads/main/apis.yml
name: Braze
tags:
  - Customer Engagement
  - Marketing Automation
  - Messaging
  - Push Notifications
  - Email
  - SMS
  - Mobile
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-05-04'
position: Consumer
description: Braze is a leading customer engagement platform providing REST APIs for managing user profiles, orchestrating multi-channel messaging campaigns, and exporting analytics. The platform supports email, SMS, push notifications, in-app messages, and content cards across mobile and web channels. Braze uses Bearer token authentication with region-specific REST endpoints and offers extensive webhook and Canvas automation capabilities for lifecycle marketing.
apis:
  - aid: braze:braze
    name: Braze REST API
    tags:
      - Customer Engagement
      - User Management
      - Messaging
      - Campaigns
      - Analytics
    humanURL: https://www.braze.com/docs/api/basics/
    properties:
      - url: https://www.braze.com/docs/api/basics/
        type: Documentation
      - type: OpenAPI
        url: openapi/braze-openapi.yml
    description: The Braze REST API enables server-side operations including creating and updating user profiles, triggering campaigns and Canvases, sending transactional messages, managing product catalogs, controlling subscription groups, and exporting campaign analytics and user data. Region-specific base URLs serve US, EU, AU, ID, and JP instances with Bearer token auth.
common:
  - type: Website
    url: https://www.braze.com
  - type: Documentation
    url: https://www.braze.com/docs
  - type: Partners
    url: https://www.braze.com/docs/partners/home
  - type: Support
    url: https://www.braze.com/docs/help/home
  - type: ChangeLog
    url: https://www.braze.com/docs/help/release_notes
  - type: FAQ
    url: https://www.braze.com/docs/help/faqs
  - type: RateLimits
    url: https://www.braze.com/docs/api/api_limits
  - type: UseCases
    url: https://www.braze.com/docs/api/use_cases
  - type: PrivacyPolicy
    url: https://www.braze.com/docs/user_guide/privacy_portal
  - type: Blog
    url: https://www.braze.com/resources/articles
  - type: Videos
    url: https://www.braze.com/resources/videos
  - type: CaseStudies
    url: https://www.braze.com/customers
  - type: Webinars
    url: https://www.braze.com/resources/webinars-and-events
  - type: Features
    data:
      - Custom pricing based on MAU + channels + AI usage
      - 'Mid-market: $60K-$200K/year typical'
      - 'Enterprise: $1M+/year for large deployments'
      - 'Platform Editions: Core, Pro, Enterprise'
      - 'Channels: Email, Push, In-App, Content Cards, SMS, WhatsApp, Webhooks'
      - REST API at rest.iad-XX.braze.com (region-specific)
      - '/users/track: 50,000 req/min/workspace'
      - '/messages/send: 250 req/min/workspace'
      - '/transactional/send: 250 req/sec/workspace'
      - Canvas Flow for advanced journey orchestration
      - Predictive AI for churn / conversion likelihood
      - Sage AI Copilot for marketers
      - Audience Sync to ad platforms
      - Data residency in US/EU/AU regions
      - SCIM/SSO on Enterprise
      - Webhooks for journey triggers
    sources:
      - https://www.braze.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
