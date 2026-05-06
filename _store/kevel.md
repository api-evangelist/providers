---
aid: kevel
name: Kevel
description: Kevel is an API-first ad serving platform that lets brands and publishers build unified, fully customized ad systems supporting any ad format, any creative, and multiple demand sources. Kevel exposes a Decision API for ad requests, a Management API for campaign and creative operations, a Reporting API for performance analytics, and a UserDB API for first-party audience and user data.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Ad Serving
  - Advertising
  - API-First
  - Audience
  - Monetization
  - Reporting
url: https://raw.githubusercontent.com/api-evangelist/kevel/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kevel:decision-api
    name: Kevel Decision API
    description: The Decision API enables ad requests without using ad code. By posting to a RESTful endpoint, Kevel's ad engine returns decision data and creative contents for serving ads in your application across web, mobile, native, audio, video, and CTV surfaces.
    humanURL: https://dev.kevel.com/reference/request
    tags:
      - Ad Serving
      - Decision
      - Native Ads
    properties:
      - type: Documentation
        url: https://dev.kevel.com/docs/native-ads-api-quickstart
      - type: Reference
        url: https://dev.kevel.com/reference/request
  - aid: kevel:management-api
    name: Kevel Management API
    description: The Management API provides programmatic access to manage advertisers, campaigns, flights, ads, creatives, channels, sites, zones, and other platform resources. It is the system-of-record API used to provision and operate the Kevel ad server.
    humanURL: https://dev.kevel.com/docs/management-api-tutorial
    tags:
      - Campaigns
      - Creatives
      - Management
    properties:
      - type: Documentation
        url: https://dev.kevel.com/docs/management-api-tutorial
      - type: Reference
        url: https://dev.kevel.com/reference/getting-started-with-the-management-api
  - aid: kevel:reporting-api
    name: Kevel Reporting API
    description: The Reporting API exposes ad serving performance data, allowing customers to pull impressions, clicks, conversions, revenue, and other metrics by advertiser, campaign, flight, ad, creative, site, zone, and date range for analytics and finance workflows.
    humanURL: https://dev.kevel.com/reference/reporting-overview
    tags:
      - Analytics
      - Reporting
    properties:
      - type: Documentation
        url: https://dev.kevel.com/reference/reporting-overview
  - aid: kevel:userdb-api
    name: Kevel UserDB API
    description: The UserDB API provides first-party audience and user data management, enabling customers to read and write user keys, custom properties, interests, and audience segment membership for targeting in the Decision API.
    humanURL: https://dev.kevel.com/reference/userdb-overview
    tags:
      - Audience
      - Targeting
      - UserDB
    properties:
      - type: Documentation
        url: https://dev.kevel.com/reference/userdb-overview
common:
  - type: Website
    url: https://www.kevel.com
    name: Kevel Website
  - type: Portal
    url: https://dev.kevel.com/
    name: Kevel Developer Portal
  - type: Documentation
    url: https://dev.kevel.com/docs/understanding-kevel
    name: Kevel Documentation
  - type: GettingStarted
    url: https://dev.kevel.com/reference/getting-started-with-kevel
    name: Getting Started with Kevel
  - type: Reference
    url: https://dev.kevel.com/reference
    name: Kevel API Reference
  - type: SDKs
    url: https://dev.kevel.com/docs/sdks
    name: Kevel SDKs
  - type: Blog
    url: https://www.kevel.com/blog
    name: Kevel Blog
  - type: Pricing
    url: https://www.kevel.com/pricing
    name: Kevel Pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
