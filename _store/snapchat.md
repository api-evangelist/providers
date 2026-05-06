---
aid: snapchat
url: https://raw.githubusercontent.com/api-evangelist/snapchat/refs/heads/main/apis.yml
name: Snapchat
description: Snap Inc. operates Snapchat, a visual messaging app and camera platform with developer tools including the Marketing API for programmatic advertising, Conversions API for server-side conversion tracking, Login Kit for OAuth-based user authentication, Creative Kit for content sharing to Snapchat, Camera Kit for embedding Snap AR technology into third-party apps, and Lens Studio for building augmented reality experiences.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advertising
  - AR
  - Augmented Reality
  - Marketing
  - Messaging
  - Social Media
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: snapchat:snapchat-ads-api
    name: Snapchat Ads API
    description: The Snapchat Ads API (Marketing API) allows developers to programmatically create, manage, and optimize advertising campaigns on the Snapchat platform. It provides endpoints for managing organizations, ad accounts, campaigns, ad squads, ads, creatives, media, funding sources, audience segments, and measurement reporting. The API supports the full advertising lifecycle from campaign setup through reporting and optimization.
    humanURL: https://developers.snap.com/api/marketing-api/Ads-API/introduction
    tags:
      - Advertising
      - Campaigns
      - Marketing
    properties:
      - type: Documentation
        url: https://developers.snap.com/api/marketing-api/Ads-API/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snapchat/refs/heads/main/openapi/snapchat-ads-api-openapi.yml
  - aid: snapchat:snapchat-conversions-api
    name: Snapchat Conversions API
    description: The Snapchat Conversions API (CAPI) is a structured, privacy-centric server-to-server interface allowing advertisers to pass web, app, and offline conversion events directly to Snap. It helps optimize ad campaigns, improve targeting, and measure conversions while supporting first-party custom audience population in real-time. Current version is v3.
    humanURL: https://developers.snap.com/api/marketing-api/Conversions-API/Introduction
    tags:
      - Advertising
      - Analytics
      - Conversions
      - Privacy
    properties:
      - type: Documentation
        url: https://developers.snap.com/api/marketing-api/Conversions-API/Introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snapchat/refs/heads/main/openapi/snapchat-conversions-api-openapi.yml
  - aid: snapchat:snapchat-login-kit
    name: Snapchat Login Kit API
    description: Snapchat Login Kit enables developers to let users sign up and log in to their apps using their Snapchat account credentials. Built on the OAuth 2.0 standard, it provides endpoints for authorization, token exchange, token refresh, and retrieving user profile information including display name and Bitmoji avatar. Available for iOS, Android, and Web platforms.
    humanURL: https://developers.snap.com/snap-kit/login-kit/overview
    tags:
      - Authentication
      - Identity
      - OAuth
    properties:
      - type: Documentation
        url: https://developers.snap.com/snap-kit/login-kit/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snapchat/refs/heads/main/openapi/snapchat-login-kit-openapi.yml
  - aid: snapchat:snapchat-creative-kit
    name: Snapchat Creative Kit
    description: Creative Kit allows developers to let users share content including Lenses, AR experiences, filters, GIFs, videos, links, and captions from a website or app directly to Snapchat's camera or preview screen. Supports Dynamic Lenses, Stickers, and Spotlight Posting. Available as a code-only integration (SDK deprecated October 2024).
    humanURL: https://developers.snap.com/snap-kit/creative-kit/overview
    tags:
      - AR
      - Content Sharing
      - Integration
      - Social Media
    properties:
      - type: Documentation
        url: https://developers.snap.com/snap-kit/creative-kit/overview
      - type: GitHubRepository
        url: https://github.com/Snapchat/creative-kit
  - aid: snapchat:snapchat-camera-kit
    name: Snapchat Camera Kit
    description: Camera Kit enables developers to integrate Snap's AR camera technology directly into iOS, Android, and web applications, giving users access to Snap's lens library and AR experiences without leaving the host app.
    humanURL: https://developers.snap.com/camera-kit/home
    tags:
      - AR
      - Augmented Reality
      - Camera
      - SDK
    properties:
      - type: Documentation
        url: https://developers.snap.com/camera-kit/home
  - aid: snapchat:snapchat-lens-studio
    name: Lens Studio
    description: Lens Studio is Snap's desktop application for building augmented reality lenses for Snapchat and Spectacles. Provides an API for scripting lens behaviors, integrating dynamic data, and publishing to the Snap Lens Network.
    humanURL: https://developers.snap.com/lens-studio/home
    tags:
      - AR
      - Augmented Reality
      - Creative Tools
      - Lens
    properties:
      - type: Documentation
        url: https://developers.snap.com/lens-studio/home
common:
  - type: Website
    url: https://snap.com
  - type: DeveloperPortal
    url: https://developers.snap.com
  - type: Documentation
    url: https://developers.snap.com/api/marketing-api/Ads-API/introduction
  - type: GitHubOrganization
    url: https://github.com/Snapchat
  - type: TermsOfService
    url: https://snap.com/en-US/terms
  - type: PrivacyPolicy
    url: https://snap.com/en-US/privacy/privacy-policy
  - type: Blog
    url: https://eng.snap.com
  - type: Support
    url: https://businesshelp.snapchat.com
  - type: Login
    url: https://kit.snapchat.com/manage/
  - type: Pricing
    url: https://ads.snapchat.com
  - type: SignUp
    url: https://kit.snapchat.com/manage/
segments:
  - Social Media
  - Advertising
  - AR/VR
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
