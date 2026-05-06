---
aid: clevertap
name: CleverTap
url: https://raw.githubusercontent.com/api-evangelist/clevertap/refs/heads/main/apis.yml
created: '2024-11-14'
modified: '2026-04-26'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - Audiences
  - Customer Engagement
  - Customer Retention
  - Marketing Automation
  - Mobile Engagement
  - Push Notifications
  - User Behavior
description: CleverTap is a customer engagement and retention platform that helps businesses understand user behavior, segment audiences, and deliver personalized experiences across mobile push, email, SMS, in-app, web push, and WhatsApp channels. CleverTap exposes a comprehensive REST API surface covering profiles, events, campaigns, real-time analytics, catalogs, feature flags, and more, authenticated via account ID and passcode headers.
apis:
  - aid: clevertap:profile-api
    name: CleverTap Profile API
    tags:
      - Profiles
      - User Data
    humanURL: https://developer.clevertap.com/docs/profile-api
    properties:
      - url: https://developer.clevertap.com/docs/profile-api
        type: Documentation
    description: Upload, retrieve, update, and delete user profiles in CleverTap with identity, demographic, and custom property data.
  - aid: clevertap:event-api
    name: CleverTap Event API
    tags:
      - Events
      - Tracking
    humanURL: https://developer.clevertap.com/docs/event-api
    properties:
      - url: https://developer.clevertap.com/docs/event-api
        type: Documentation
    description: Record user events with arbitrary properties for behavioral segmentation, funnels, and triggered messaging.
  - aid: clevertap:campaign-api
    name: CleverTap Campaign API
    tags:
      - Campaigns
      - Messaging
    humanURL: https://developer.clevertap.com/docs/create-a-campaign-api
    properties:
      - url: https://developer.clevertap.com/docs/create-a-campaign-api
        type: Documentation
    description: Programmatically create and manage push, email, SMS, web, and in-app campaigns and retrieve message status reports.
  - aid: clevertap:bulletins-api
    name: CleverTap Bulletins API
    tags:
      - Bulletins
      - Triggers
    humanURL: https://developer.clevertap.com/docs/bulletins-api
    properties:
      - url: https://developer.clevertap.com/docs/bulletins-api
        type: Documentation
    description: Raise a Bulletin in CleverTap when a business event is triggered, used to drive real-time campaign delivery from external systems.
  - aid: clevertap:catalog-api
    name: CleverTap Catalog API
    tags:
      - Catalog
      - Product Data
    humanURL: https://developer.clevertap.com/docs/catalog-api
    properties:
      - url: https://developer.clevertap.com/docs/catalog-api
        type: Documentation
    description: Manage product catalog data feeding personalization, recommendations, and product-aware messaging.
  - aid: clevertap:custom-list-api
    name: CleverTap Custom List API
    tags:
      - Audiences
      - Lists
    humanURL: https://developer.clevertap.com/docs/custom-list-api
    properties:
      - url: https://developer.clevertap.com/docs/custom-list-api
        type: Documentation
    description: Create and update custom lists used as audience segments in campaigns and journeys.
  - aid: clevertap:remote-config-api
    name: CleverTap Remote Config API
    tags:
      - Feature Flags
      - Remote Config
    humanURL: https://developer.clevertap.com/docs/remote-config-api
    properties:
      - url: https://developer.clevertap.com/docs/remote-config-api
        type: Documentation
    description: Manage feature flags and remote configuration variables delivered to mobile apps and websites.
  - aid: clevertap:counts-api
    name: CleverTap Real-Time Counts API
    tags:
      - Analytics
      - Counts
    humanURL: https://developer.clevertap.com/docs/real-time-counts-api
    properties:
      - url: https://developer.clevertap.com/docs/real-time-counts-api
        type: Documentation
    description: Query real-time counts and trends of events, profiles, and segments.
common:
  - type: Website
    url: https://clevertap.com/
  - type: Developer Portal
    url: https://developer.clevertap.com/
  - type: Documentation
    url: https://developer.clevertap.com/docs
  - type: Authentication
    url: https://developer.clevertap.com/docs/api-authentication
  - type: Status
    url: https://status.clevertap.com/
  - type: Pricing
    url: https://clevertap.com/pricing/
  - type: Privacy Policy
    url: https://clevertap.com/privacy-policy/
  - type: Terms of Service
    url: https://clevertap.com/terms-of-service/
  - type: JSON-LD
    url: json-ld/clevertap-context.jsonld
  - type: Spectral
    url: rules/clevertap-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/clevertap-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
