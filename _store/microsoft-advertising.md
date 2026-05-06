---
aid: microsoft-advertising
name: Microsoft Advertising
description: Microsoft Advertising provides APIs for managing ad campaigns, reporting on performance, and bulk operations across the Microsoft Advertising network including Bing, MSN, and partner sites. The platform offers programmatic access to campaign management, reporting, and bulk operations services for advertisers and developers.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-advertising/refs/heads/main/apis.yml
tags:
  - Advertising
  - Analytics
  - Bing Ads
  - Bulk Operations
  - Campaigns
  - Microsoft
  - Reporting
apis:
  - aid: microsoft-advertising:campaign-management-api
    name: Microsoft Advertising Campaign Management API
    tags:
      - Advertising
      - Bing Ads
      - Campaigns
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://campaign.api.bingads.microsoft.com/Api/Advertiser/CampaignManagement/v13/
    humanURL: https://learn.microsoft.com/en-us/advertising/campaign-management-service/campaign-management-service-reference
    properties:
      - url: https://learn.microsoft.com/en-us/advertising/campaign-management-service/campaign-management-service-reference
        type: Documentation
    description: The Microsoft Advertising Campaign Management API enables programmatic management of advertising campaigns, ad groups, ads, keywords, and targeting. Developers can create and modify campaign structures, set bids and budgets, manage audiences, and configure ad extensions across the Microsoft Advertising network.
  - aid: microsoft-advertising:reporting-api
    name: Microsoft Advertising Reporting API
    tags:
      - Advertising
      - Analytics
      - Reporting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://reporting.api.bingads.microsoft.com/Api/Advertiser/Reporting/v13/
    humanURL: https://learn.microsoft.com/en-us/advertising/reporting-service/reporting-service-reference
    properties:
      - url: https://learn.microsoft.com/en-us/advertising/reporting-service/reporting-service-reference
        type: Documentation
    description: The Microsoft Advertising Reporting API provides access to performance reports for campaigns, ad groups, ads, and keywords. Developers can request reports on impressions, clicks, conversions, spend, and other metrics with customizable date ranges, filters, and aggregation levels.
  - aid: microsoft-advertising:bulk-api
    name: Microsoft Advertising Bulk API
    tags:
      - Advertising
      - Batch Processing
      - Bulk Operations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://bulk.api.bingads.microsoft.com/Api/Advertiser/CampaignManagement/v13/
    humanURL: https://learn.microsoft.com/en-us/advertising/bulk-service/bulk-service-reference
    properties:
      - url: https://learn.microsoft.com/en-us/advertising/bulk-service/bulk-service-reference
        type: Documentation
    description: The Microsoft Advertising Bulk API enables efficient management of large-scale advertising campaigns through batch upload and download operations. It supports CSV-based bulk operations for creating, updating, and deleting campaigns, ad groups, ads, and keywords in a single request.
common:
  - type: Portal
    url: https://ads.microsoft.com/
  - type: Developer Portal
    url: https://learn.microsoft.com/en-us/advertising/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/advertising/guides/client-libraries
  - type: Authentication
    url: https://learn.microsoft.com/en-us/advertising/guides/authentication-oauth
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
