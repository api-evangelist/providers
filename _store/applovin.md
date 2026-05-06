---
aid: applovin
url: https://github.com/api-evangelist/applovin
name: AppLovin
type: Index
image: https://www.applovin.com/favicon.ico
tags:
  - Advertising
  - Mobile
  - AdTech
  - App Monetization
  - Mediation
  - User Acquisition
  - Marketing Technology
  - Conversion Tracking
description: AppLovin is a marketing platform that helps businesses reach, monetize, and grow their global audiences through mobile advertising, mediation, and analytics. The company operates platforms including AppDiscovery (Axon) for performance-based user acquisition, MAX for in-app bidding mediation, Adjust for mobile measurement, and Wurl for connected TV. AppLovin provides SDKs and REST APIs that allow app developers and advertisers to integrate ad serving, monetization, campaign management, conversion tracking, and reporting capabilities into their applications.
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: applovin-max-revenue-reporting
    name: AppLovin MAX Revenue Reporting API
    description: The MAX Revenue Reporting API returns aggregated MAX mediation revenue and user-level publisher data. Publishers query the API with a Report Key, a date range (up to a 45-day window), and a list of columns to return (day, hour, application, ad format, country, network, impressions, eCPM, revenue, etc.). The API supports filtering, sorting, and pagination, and returns results as either JSON or CSV. The endpoint is commonly integrated with mobile measurement partners (MMPs) and BI pipelines for monetization analytics.
    humanURL: https://support.axon.ai/en/max/reporting-apis/revenue-reporting-api
    baseURL: https://r.applovin.com/maxReport
    version: v1
    properties:
      - type: Documentation
        url: https://support.axon.ai/en/max/reporting-apis/revenue-reporting-api
      - type: OpenAPI
        url: openapi/applovin-max-revenue-reporting.yaml
    tags:
      - Reporting
      - Mediation
      - Monetization
      - Analytics
  - aid: applovin-max-ad-unit-management
    name: AppLovin MAX Ad Unit Management API
    description: The MAX Ad Unit Management API allows publishers to programmatically manage their MAX mediation configuration. It supports creating, listing, viewing, and editing ad units across iOS and Android apps; configuring ad network settings, frequency capping, bid floors, and segment-based waterfalls; running A/B experiments on waterfalls; and managing test devices. Authentication uses an Api-Key header containing a Management Key. Rate limit is 2,000 requests per hour.
    humanURL: https://support.axon.ai/en/max/advanced-features/ad-unit-management-api
    baseURL: https://o.applovin.com/mediation/v1
    version: v1
    properties:
      - type: Documentation
        url: https://support.axon.ai/en/max/advanced-features/ad-unit-management-api
      - type: OpenAPI
        url: openapi/applovin-max-ad-unit-management.yaml
    tags:
      - Mediation
      - Ad Units
      - Waterfalls
      - Experiments
      - Configuration
  - aid: applovin-growth-reporting
    name: AppLovin Growth (Axon / AppDiscovery) Reporting API
    description: The Growth Reporting API exposes campaign-level performance data for AppLovin's AppDiscovery / Axon advertising platform. Advertisers and publishers retrieve aggregated metrics (impressions, clicks, conversions, installs, cost, revenue) by campaign, country, day, and other dimensions, scoped by either advertiser or publisher report types. The API supports JSON and CSV output, filtering, sorting, paging, and a 45-day rolling window.
    humanURL: https://support.axon.ai/en/growth/promoting-your-apps/api/reporting-api
    baseURL: https://r.applovin.com/report
    version: v1
    properties:
      - type: Documentation
        url: https://support.axon.ai/en/growth/promoting-your-apps/api/reporting-api
      - type: OpenAPI
        url: openapi/applovin-growth-reporting.yaml
    tags:
      - Reporting
      - User Acquisition
      - Advertising
      - Analytics
  - aid: applovin-growth-asset-reporting
    name: AppLovin Growth Asset Reporting API
    description: The Growth Asset Reporting API provides creative-level performance data for AppLovin AppDiscovery campaigns. It returns metrics (impressions, clicks, CTR, cost) broken down by creative asset, creative set, and campaign, supporting both fixed time-range queries (yesterday, last_7d, last_month) and arbitrary date-range queries within a 45-day window.
    humanURL: https://support.axon.ai/en/growth/promoting-your-apps/api/asset-reporting-api
    baseURL: https://r.applovin.com/assetReport
    version: v1
    properties:
      - type: Documentation
        url: https://support.axon.ai/en/growth/promoting-your-apps/api/asset-reporting-api
      - type: OpenAPI
        url: openapi/applovin-growth-asset-reporting.yaml
    tags:
      - Reporting
      - Creatives
      - User Acquisition
      - Advertising
  - aid: applovin-axon-campaign-management
    name: AppLovin Axon Campaign Management API
    description: The Axon Campaign Management API enables advertisers to programmatically create, update, list, and manage AppLovin AppDiscovery (Axon) campaigns, creative sets, and creative assets. It supports campaign budgeting, goal optimization (CPI, CPE, CPP, ROAS variants), country/region/metro targeting, attribution tracking integration with major MMPs (Adjust, AppsFlyer, Apsalar, Branch, Kochava, Tenjin), creative set lifecycle (create, update, clone), and asset upload (HTML5 playables, images, videos). Authentication uses an Authorization header with the Campaign Management API key. Rate limit is 1,000 requests per 60 seconds.
    humanURL: https://support.axon.ai/en/app-discovery/api/axon-campaign-management-api/
    baseURL: https://api.ads.axon.ai/manage/v1
    version: v1
    properties:
      - type: Documentation
        url: https://support.axon.ai/en/app-discovery/api/axon-campaign-management-api/
      - type: OpenAPI
        url: openapi/applovin-axon-campaign-management.yaml
    tags:
      - Campaigns
      - Creatives
      - User Acquisition
      - Advertising
      - Asset Management
  - aid: applovin-conversion-api-lead-gen
    name: AppLovin Conversion API for Lead Generation
    description: The AppLovin Conversion API (CAPI) for Lead Generation lets advertisers send server-to-server conversion events (page_view, generate_lead) directly to AppLovin / Axon for attribution and optimization. Events include user identifiers (axwrt cookie, aleid, email, phone, IP, user agent) which AppLovin auto-hashes where required. Up to 100 events can be batched per request, and events are deduplicated against pixel-fired client-side events using a dedupe_id.
    humanURL: https://support.axon.ai/en/growth/promoting-your-websites/api/lead-gen-capi/
    baseURL: https://b.applovin.com
    version: v1
    properties:
      - type: Documentation
        url: https://support.axon.ai/en/growth/promoting-your-websites/api/lead-gen-capi/
      - type: OpenAPI
        url: openapi/applovin-conversion-api-lead-gen.yaml
    tags:
      - Conversion Tracking
      - Server-to-Server
      - Lead Generation
      - Attribution
common:
  - type: Website
    url: https://www.applovin.com
  - type: Documentation
    url: https://support.axon.ai
  - type: DeveloperPortal
    url: https://developers.applovin.com
  - type: Support
    url: https://support.axon.ai
  - type: Blog
    url: https://www.applovin.com/blog/
  - type: TermsOfService
    url: https://www.applovin.com/legal/
  - type: PrivacyPolicy
    url: https://www.applovin.com/privacy/
  - type: GitHubOrganization
    url: https://github.com/AppLovin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-SDK-Android
    title: MAX Android SDK
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-SDK-iOS
    title: MAX iOS SDK
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Swift-Package
    title: MAX Swift Package
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Unity-Plugin
    title: MAX Unity Plugin
  - type: SDK
    url: https://www.npmjs.com/package/react-native-applovin-max
    title: MAX React Native Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Flutter
    title: MAX Flutter Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Cordova
    title: MAX Cordova Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Unreal
    title: MAX Unreal Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Defold
    title: MAX Defold Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Godot
    title: MAX Godot Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-AIR
    title: MAX Adobe AIR Plugin
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Ad-Review-SDK-Android
    title: MAX Ad Review Android SDK
  - type: SDK
    url: https://github.com/AppLovin/AppLovin-MAX-Ad-Review-SDK-iOS
    title: MAX Ad Review iOS SDK
  - type: CodeExamples
    url: https://github.com/AppLovin/AppLovin-MAX-Unity-Plugin
    title: MAX Unity Demo App
  - type: Tools
    url: https://github.com/AppLovin/CocoaPods-Specs
    title: AppLovin CocoaPods Specs Repository
  - type: Tools
    url: https://github.com/AppLovin/homebrew-Mobile-Tools
    title: Homebrew Mobile Tools Tap
  - type: SpectralRules
    url: rules/applovin-rules.yml
    title: AppLovin Spectral Ruleset
  - type: NaftikoCapability
    url: capabilities/publisher-monetization.yaml
    title: Publisher Monetization Workflow
  - type: NaftikoCapability
    url: capabilities/advertiser-growth.yaml
    title: Advertiser Growth Workflow
  - type: JSONLD
    url: json-ld/applovin-context.jsonld
    title: AppLovin JSON-LD Context
  - type: Vocabulary
    url: vocabulary/applovin-vocabulary.yml
    title: AppLovin Domain Vocabulary
  - type: JSONSchema
    url: json-schema/applovin-campaign-schema.json
    title: AppLovin Campaign Schema
  - type: JSONSchema
    url: json-schema/applovin-creative-set-schema.json
    title: AppLovin Creative Set Schema
  - type: JSONSchema
    url: json-schema/applovin-ad-unit-schema.json
    title: AppLovin Ad Unit Schema
  - type: JSONSchema
    url: json-schema/applovin-conversion-event-schema.json
    title: AppLovin Conversion Event Schema
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
