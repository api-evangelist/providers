---
aid: albertsons
url: https://raw.githubusercontent.com/api-evangelist/albertsons/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
apis:
  - aid: albertsons:retail-media-api
    name: Albertsons Media Collective API
    tags:
      - Advertising
      - Grocery
      - Retail
      - Retail Media
      - Campaigns
      - Analytics
    baseURL: https://api.albertsons.com
    humanURL: https://portal-prod.apim.azwestus.stratus.albertsons.com/
    description: The Albertsons Media Collective API enables advertisers to integrate with Albertsons retail media network for campaign management and performance analytics. The API provides near-real-time access to campaign performance data, allowing advertisers to bring data into their own measurement models for analysis. The developer portal, built on Microsoft Azure API Management, provides API documentation, code samples, and an interactive console for testing.
    properties:
      - type: Documentation
        url: https://portal-prod.apim.azwestus.stratus.albertsons.com/
      - type: OpenAPI
        url: openapi/albertsons-retail-media-api-openapi.yml
      - type: JSONSchema
        url: json-schema/retail-media-api-campaign-schema.json
        title: Campaign Schema
      - type: JSONSchema
        url: json-schema/retail-media-api-performance-metric-schema.json
        title: Performance Metric Schema
      - type: JSONSchema
        url: json-schema/retail-media-api-audience-schema.json
        title: Audience Schema
      - type: JSONSchema
        url: json-schema/retail-media-api-report-request-schema.json
        title: Report Request Schema
      - type: JSONSchema
        url: json-schema/retail-media-api-report-response-schema.json
        title: Report Response Schema
common:
  - type: Website
    url: https://www.albertsons.com
  - type: Portal
    url: https://portal-prod.apim.azwestus.stratus.albertsons.com/
  - type: Authentication
    url: https://portal-prod.apim.azwestus.stratus.albertsons.com/
  - type: TermsOfService
    url: https://www.albertsons.com/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.albertsons.com/privacy-policy/
  - type: SpectralRules
    url: rules/albertsons-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/retail-media-advertising.yaml
    title: Retail Media Advertising Workflow
  - type: NaftikoCapability
    url: capabilities/shared/retail-media-api.yaml
    title: Retail Media API Shared Definition
  - type: Vocabulary
    url: vocabulary/albertsons-vocabulary.yaml
  - type: JSONLD
    url: json-ld/albertsons-retail-media-api-context.jsonld
  - type: Features
    data:
      - name: Near-Real-Time Campaign Performance
        description: Access advertising campaign performance data in near-real-time to bring metrics into custom dashboards and measurement models.
      - name: Audience Targeting
        description: Target campaigns using audience segments derived from Albertsons shopper purchase behavior across grocery and pharmacy banners.
      - name: Campaign Management
        description: Create, update, and manage advertising campaigns with budget controls, scheduling, and audience targeting configurations.
      - name: Custom Reporting
        description: Generate configurable performance reports with custom dimensions and metrics for export to external analytics tools.
      - name: Azure API Management Portal
        description: Interactive developer portal built on Microsoft Azure API Management with documentation, code samples, and an API testing console.
      - name: Multi-Banner Reach
        description: Access to shopper audiences across Albertsons, Safeway, Vons, Jewel-Osco, Acme, and other banner networks.
  - type: UseCases
    data:
      - name: Campaign Performance Dashboards
        description: Pull near-real-time campaign metrics into custom brand or agency dashboards for monitoring impressions, clicks, and ROAS.
      - name: Automated Budget Optimization
        description: Integrate campaign performance data into automated bidding and budget allocation systems.
      - name: Third-Party Measurement Integration
        description: Share campaign performance data with measurement partners like TransUnion for attribution and audience analysis.
      - name: Media Mix Modeling
        description: Incorporate Albertsons retail media performance data into multi-channel media mix models.
      - name: Audience Insights
        description: Analyze shopper audience segments to inform product marketing strategy and campaign targeting decisions.
  - type: Integrations
    data:
      - name: TransUnion
        description: Partnership integration for enhanced audience measurement and identity resolution using TransUnion data.
      - name: Microsoft Azure
        description: Developer portal and API gateway infrastructure built on Microsoft Azure API Management.
      - name: Analytics Platforms
        description: Export campaign data to third-party analytics dashboards and reporting tools via the Performance API.
description: Albertsons Companies is one of the largest food and drug retailers in the United States, operating supermarkets and pharmacies under banners including Albertsons, Safeway, Vons, Jewel-Osco, Acme, Shaw's, Star Market, and others. The company operates the Albertsons Media Collective, a retail media network that provides advertisers API access to near-real-time campaign performance data and audience targeting capabilities based on shopper purchase behavior across its banner network.
tags:
  - Grocery
  - Retail
  - Retail Media
  - Advertising
  - Campaigns
  - Analytics
  - Consumer Goods
  - Food
  - Pharmacy
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
