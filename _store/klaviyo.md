---
aid: klaviyo
name: Klaviyo
url: https://raw.githubusercontent.com/api-evangelist/klaviyo/refs/heads/main/apis.yml
description: Klaviyo is a marketing automation and customer data platform built for ecommerce. Build custom integrations to bring data into Klaviyo to create personalized experiences across email, SMS, mobile push, and more. The Klaviyo API exposes profiles, events, lists, segments, campaigns, flows, catalogs, coupons, metrics, reviews, templates, webhooks, and reporting endpoints for building rich integrations and data pipelines.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Contract
position: Consuming
access: 3rd-Party
tags:
  - Marketing
  - Email
  - SMS
  - Customer Data
  - Ecommerce
  - Automation
created: '2024-11-07T00:00:00.000Z'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: klaviyo:klaviyo-api
    name: Klaviyo API
    description: The Klaviyo API provides programmatic access to profiles, events, lists, segments, campaigns, flows, templates, catalogs, coupons, metrics, reviews, forms, images, tags, webhooks, tracking settings, custom objects, conversations, web feeds, data privacy, and reporting. It is used to build personalized customer experiences across email, SMS, mobile push, and other channels for ecommerce brands.
    humanURL: https://developers.klaviyo.com/
    baseURL: https://a.klaviyo.com
    tags:
      - Profiles
      - Events
      - Lists
      - Segments
      - Campaigns
      - Flows
      - Catalogs
      - Coupons
      - Metrics
      - Reviews
      - Templates
      - Webhooks
      - Forms
      - Reporting
    properties:
      - type: Documentation
        url: https://developers.klaviyo.com/
      - type: OpenAPI
        url: openapi/klaviyo-openapi.json
      - type: Reference
        url: https://developers.klaviyo.com/en/reference/api_overview
      - type: Authentication
        url: https://developers.klaviyo.com/en/docs/authenticate_
      - type: Rate Limits
        url: https://developers.klaviyo.com/en/docs/rate_limits_and_error_handling
      - type: Versioning
        url: https://developers.klaviyo.com/en/docs/api_versioning_and_deprecation_policy
      - type: Changelog
        url: https://developers.klaviyo.com/en/docs/changelog_
      - type: SDKs
        url: https://developers.klaviyo.com/en/docs/sdk_overview
      - type: GitHub
        url: https://github.com/klaviyo/openapi
common:
  - type: Website
    url: https://www.klaviyo.com
  - type: Portal
    url: https://developers.klaviyo.com/
  - type: Documentation
    url: https://developers.klaviyo.com/en/docs
  - type: Reference
    url: https://developers.klaviyo.com/en/reference/api_overview
  - type: Authentication
    url: https://developers.klaviyo.com/en/docs/authenticate_
  - type: RateLimits
    url: https://developers.klaviyo.com/en/docs/rate_limits_and_error_handling
  - type: Changelog
    url: https://developers.klaviyo.com/en/docs/changelog_
  - type: SDKs
    url: https://developers.klaviyo.com/en/docs/sdk_overview
  - type: Status
    url: https://status.klaviyo.com/
  - type: Blog
    url: https://www.klaviyo.com/blog
  - type: Sign Up
    url: https://www.klaviyo.com/signup
  - type: Pricing
    url: https://www.klaviyo.com/pricing
  - type: Terms of Service
    url: https://www.klaviyo.com/legal/terms-of-service
  - type: Privacy Policy
    url: https://www.klaviyo.com/legal/privacy-policy
  - type: Support
    url: https://help.klaviyo.com/
  - type: GitHub
    url: https://github.com/klaviyo
  - type: Features
    data:
      - 'Free: 250 profiles, 500 emails/mo, 150 SMS credits/mo'
      - Email plan from $20/mo (500 profiles) up to $720+/mo (50K profiles)
      - Email + SMS from $35/mo (500 profiles) with 1,250 SMS credits
      - 'SMS credits: 1=domestic SMS, 3=MMS, 3-12=international'
      - Public API at api.klaviyo.com
      - Default 75 req/s burst, 700 req/min steady-state
      - OAuth 2.0 (private apps) and API keys
      - Webhooks for profile, event, and metric updates
      - Profile and event APIs (track, identify)
      - Lists, segments, campaigns, flows
      - Templates with drag-and-drop editor
      - Predictive analytics (CLV, churn risk)
      - AI segments and AI-generated content
      - Marketing Agent for campaign and flow creation
      - 350+ ecommerce/CRM integrations
      - Mobile push notifications and on-site messaging
    sources:
      - https://www.klaviyo.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
