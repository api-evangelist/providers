---
aid: tiktok-for-developers
name: TikTok for Developers
description: TikTok for Developers provides a suite of REST APIs enabling third-party platforms to integrate with TikTok's social video ecosystem. Products include Login Kit, Display API, Content Posting API, Research API, and the TikTok API for Business, supporting use cases from user authentication and video publishing to advertising campaign management and academic research.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advertising
  - Analytics
  - Authentication
  - Content
  - Social Media
  - Video
created: '2025-07-29'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tiktok-for-developers/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tiktok-for-developers:tiktok-display-api
    name: TikTok Display API
    description: Enables developers to access TikTok user profile information and video metadata. Supports retrieving user info, listing recent videos, and querying videos by ID.
    humanURL: https://developers.tiktok.com/doc/display-api-overview
    baseURL: https://open.tiktokapis.com
    tags:
      - Content
      - Social Media
      - Video
    properties:
      - type: Documentation
        url: https://developers.tiktok.com/doc/display-api-overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok-for-developers/refs/heads/main/openapi/tiktok-display-openapi.yml
  - aid: tiktok-for-developers:tiktok-content-posting-api
    name: TikTok Content Posting API
    description: Allows third-party platforms to publish videos directly to a user's TikTok account. Supports direct post and upload-then-publish flows including initiating uploads, uploading video chunks, and checking publish status.
    humanURL: https://developers.tiktok.com/doc/content-posting-api-reference-direct-post
    baseURL: https://open.tiktokapis.com
    tags:
      - Content
      - Publishing
      - Social Media
      - Video
    properties:
      - type: Documentation
        url: https://developers.tiktok.com/doc/content-posting-api-get-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok-for-developers/refs/heads/main/openapi/tiktok-content-posting-openapi.yml
  - aid: tiktok-for-developers:tiktok-research-api
    name: TikTok Research API
    description: Provides academic and institutional researchers with access to TikTok public data including video queries, user information, comments, followers, and liked videos.
    humanURL: https://developers.tiktok.com/doc/research-api-get-started
    baseURL: https://open.tiktokapis.com
    tags:
      - Analytics
      - Research
      - Social Media
      - Video
    properties:
      - type: Documentation
        url: https://developers.tiktok.com/doc/research-api-get-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok-for-developers/refs/heads/main/openapi/tiktok-research-openapi.yml
  - aid: tiktok-for-developers:tiktok-login-kit
    name: TikTok Login Kit
    description: Allows users to securely log in to third-party apps and websites using their TikTok credentials via OAuth 2.0. Supports authorization code flow and token management.
    humanURL: https://developers.tiktok.com/doc/login-kit-web
    baseURL: https://open.tiktokapis.com
    tags:
      - Authentication
      - OAuth
      - Social Login
    properties:
      - type: Documentation
        url: https://developers.tiktok.com/doc/login-kit-web
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tiktok-for-developers/refs/heads/main/openapi/tiktok-login-kit-openapi.yml
common:
  - type: Website
    url: https://www.tiktok.com/
  - type: Portal
    url: https://developers.tiktok.com/
  - type: Documentation
    url: https://developers.tiktok.com/doc/overview
  - type: Getting Started
    url: https://developers.tiktok.com/doc/overview
  - type: Authentication
    url: https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens
  - type: GitHub Organization
    url: https://github.com/tiktok
  - type: SDK
    url: https://github.com/tiktok/tiktok-opensdk-ios
  - type: SDK
    url: https://github.com/tiktok/tiktok-opensdk-android
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
  - type: Use Cases
    url: https://developers.tiktok.com/
  - type: Sign Up
    url: https://developers.tiktok.com/
  - type: Login
    url: https://developers.tiktok.com/login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
