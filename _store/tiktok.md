---
aid: tiktok
name: TikTok
description: TikTok is a short-form social video platform offering developers REST APIs for advertising, e-commerce, content discovery, and platform integrations. Key products include the TikTok API for Business (advertising and campaign management), TikTok Shop API (seller product and order management), and the Data Portability API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advertising
  - Commerce
  - Content
  - E-Commerce
  - Social Media
  - Video
created: '2025-08-14'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tiktok/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tiktok:tiktok-business-api
    name: TikTok API for Business
    description: TikTok's advertising API enabling developers to create and manage ad campaigns, ad groups, creatives, audiences, and reporting for global advertisers on TikTok.
    humanURL: https://business-api.tiktok.com/portal/docs
    baseURL: https://business-api.tiktok.com
    tags:
      - Advertising
      - Campaigns
      - Marketing
      - Social Media
    properties:
      - type: Documentation
        url: https://business-api.tiktok.com/portal/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok/refs/heads/main/openapi/tiktok-business-openapi.yml
  - aid: tiktok:tiktok-shop-api
    name: TikTok Shop API
    description: TikTok Shop Partner API enabling sellers and partners to manage product catalogs, process orders, handle logistics, and integrate with TikTok's commerce ecosystem.
    humanURL: https://partner.tiktokshop.com/docv2/page/tts-api-concepts-overview
    baseURL: https://open-api.tiktokglobalshop.com
    tags:
      - Commerce
      - E-Commerce
      - Products
      - Orders
    properties:
      - type: Documentation
        url: https://partner.tiktokshop.com/doc/page/63fd743c715d622a338c4e54
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok/refs/heads/main/openapi/tiktok-shop-openapi.yml
  - aid: tiktok:tiktok-data-portability-api
    name: TikTok Data Portability API
    description: Allows users to export their TikTok data including activity, videos, and profile information to third-party services.
    humanURL: https://developers.tiktok.com/doc/data-portability-api-get-started
    baseURL: https://open.tiktokapis.com
    tags:
      - Data Portability
      - Privacy
      - User Data
    properties:
      - type: Documentation
        url: https://developers.tiktok.com/doc/data-portability-api-get-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok/refs/heads/main/openapi/tiktok-data-portability-openapi.yml
common:
  - type: Website
    url: https://www.tiktok.com/
  - type: Portal
    url: https://developers.tiktok.com/
  - type: Documentation
    url: https://developers.tiktok.com/doc/overview
  - type: Getting Started
    url: https://developers.tiktok.com/doc/overview
  - type: Business API Portal
    url: https://business-api.tiktok.com/portal
  - type: Shop Partner Portal
    url: https://partner.tiktokshop.com/
  - type: Authentication
    url: https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens
  - type: GitHub Organization
    url: https://github.com/tiktok
  - type: SDK
    url: https://github.com/tiktok/tiktok-business-api-sdk
  - type: Change Log
    url: https://developers.tiktok.com/doc/changelog
  - type: Blog
    url: https://developers.tiktok.com/blog
  - type: Forum
    url: https://developers.tiktok.com/community
  - type: Status
    url: https://status.tiktok.com/
  - type: Terms of Service
    url: https://developers.tiktok.com/doc/tiktok-api-terms-of-service
  - type: Privacy Policy
    url: https://developers.tiktok.com/doc/tiktok-api-data-privacy
  - type: Sign Up
    url: https://developers.tiktok.com/
  - type: Login
    url: https://developers.tiktok.com/login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
