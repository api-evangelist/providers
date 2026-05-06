---
aid: adobe-analytics
url: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/apis.yml
name: Adobe Analytics
description: Adobe Analytics provides real-time analytics and detailed segmentation capabilities across all marketing channels, enabling organizations to discover high-value audiences and power customer intelligence.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: 2024-01-01T00:00:00.000Z
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - name: Adobe Analytics API
    description: The Adobe Analytics 2.0 APIs provide programmatic access to data, reports, and administration features within Adobe Analytics. They allow you to perform almost any action available in the Analytics user interface, including reporting, segment management, calculated metrics, and component administration.
    image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
    baseUrl: https://analytics.adobe.io/api
    tags:
      - Analytics
      - Data
      - Marketing
      - Metrics
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/2.0/
      - type: APIReference
        url: https://developer.adobe.com/analytics-apis/docs/2.0/apis/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/AdobeDocs/analytics-2.0-apis/main/docs/swagger.json
      - type: OpenAPI
        url: openapi/adobe-analytics-api-openapi.yml
      - type: Authentication
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
      - type: GettingStarted
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
      - type: RateLimits
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/rate-limits/
      - type: GettingStarted
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/migration/
        title: Migration Guide
      - type: GitHubRepository
        url: https://github.com/AdobeDocs/analytics-2.0-apis
    contact:
      - type: Support
        url: https://experienceleague.adobe.com/docs/analytics.html
      - type: Support
        url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
        title: Community
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/
  - name: Adobe Analytics Bulk Data Insertion API
    description: The Bulk Data Insertion API (BDIA) lets you upload server-side call data in batches of compressed CSV files instead of using client-side libraries such as AppMeasurement. It is the recommended successor to the single-event Data Insertion API for high-volume server-side data collection.
    image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
    baseUrl: https://analytics-collection.adobe.io/aa/collect/v1
    tags:
      - Analytics
      - Batch Processing
      - Data Collection
      - Server-Side
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/bulk-data-insertion/
      - type: APIReference
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/bulk-data-insertion/endpoints/
      - type: OpenAPI
        url: openapi/adobe-analytics-bulk-data-insertion-api-openapi.yml
      - type: Authentication
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
    contact:
      - type: Support
        url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
      - type: Support
        url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
        title: Community
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/bulk-data-insertion/
  - name: Adobe Analytics Livestream API
    description: The Livestream API is a reporting feature in Adobe Analytics that allows clients to receive traffic data processed by Adobe Analytics in real time. Hits are streamed to the client on a hit-by-hit basis in the same order and rate that they are processed by Adobe servers.
    image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
    baseUrl: https://livestream.adobe.net/api/1/stream
    tags:
      - Analytics
      - Data
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/livestream/
      - type: APIReference
        url: https://developer.adobe.com/analytics-apis/docs/2.0/apis/livestream/
      - type: AsyncAPI
        url: asyncapi/adobe-analytics-livestream-asyncapi.yml
      - type: Authentication
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
      - type: ChangeLog
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/livestream/release-notes/
    contact:
      - type: Support
        url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
      - type: Support
        url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
        title: Community
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/livestream/
  - name: Adobe Analytics Data Repair API
    description: The Data Repair API allows you to permanently delete or transform data that has already been ingested in Adobe Analytics. It provides endpoints for estimating repair scope, creating repair jobs, and monitoring job status. This is a paid feature and Adobe recommends a careful, staged approach when using it.
    image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
    baseUrl: https://analytics.adobe.io/api
    tags:
      - Analytics
      - Compliance
      - Data Management
      - Privacy
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/data-repair/
      - type: APIReference
        url: https://developer.adobe.com/analytics-apis/docs/2.0/apis/data-repair/
      - type: OpenAPI
        url: openapi/adobe-analytics-data-repair-api-openapi.yml
      - type: Authentication
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
    contact:
      - type: Support
        url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
      - type: Support
        url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
        title: Community
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/data-repair/
  - name: Adobe Analytics Data Insertion API
    description: The Data Insertion API allows server-side data submission to Adobe Analytics one event at a time using HTTP GET or POST requests. Unlike the Bulk Data Insertion API which processes compressed CSV files in batches, this API handles individual hit submissions in real time and is explicitly excluded from the Analytics 1.4 API end-of-life scheduled for August 12, 2026.
    image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
    baseUrl: https://sc.omtrdc.net/b/ss
    tags:
      - Analytics
      - Data Collection
      - Real-Time
      - Server-Side
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/1.4/guides/data-insertion/
      - type: APIReference
        url: https://experienceleague.adobe.com/en/docs/analytics/import/c-data-insertion-api
    contact:
      - type: Support
        url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
      - type: Support
        url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
        title: Community
    humanURL: https://developer.adobe.com/analytics-apis/docs/1.4/guides/data-insertion/
  - name: Adobe Analytics 1.4 API
    description: The Adobe Analytics 1.4 APIs provide programmatic access to reporting, classifications, data sources, and report suite configuration. This version is deprecated and scheduled for end-of-life on August 12, 2026, after which all endpoints will cease to function. The Data Insertion API is excluded from this end-of-life.
    image: https://www.adobe.com/content/dam/cc/icons/analytics.svg
    baseUrl: https://api.omniture.com/admin/1.4
    tags:
      - Analytics
      - Deprecated
      - Legacy
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.adobe.com/analytics-apis/docs/1.4/
      - type: ReleaseNotes
        url: https://developer.adobe.com/analytics-apis/docs/1.4/guides/eol/
        title: Deprecation Notice
      - type: GettingStarted
        url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/migration/
        title: Migration Guide
      - type: GitHubRepository
        url: https://github.com/AdobeDocs/analytics-1.4-apis
    contact:
      - type: Support
        url: https://experienceleague.adobe.com/docs/analytics.html
      - type: Support
        url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
        title: Community
    humanURL: https://developer.adobe.com/analytics-apis/docs/1.4/
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
tags:
  - Adobe
  - Analytics
  - Business Intelligence
  - Customer Intelligence
  - Digital Marketing
  - Marketing
  - Web Analytics
common:
  - type: Portal
    url: https://developer.adobe.com/analytics-apis/docs/2.0/
  - type: Documentation
    url: https://experienceleague.adobe.com/docs/analytics.html
  - type: GettingStarted
    url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
  - type: Console
    url: https://developer.adobe.com/console/
  - type: Authentication
    url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
  - type: Support
    url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
  - type: Support
    url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/adobe-analytics
  - type: GitHubOrganization
    url: https://github.com/AdobeDocs
  - type: ChangeLog
    url: https://experienceleague.adobe.com/en/docs/analytics/release-notes/latest
  - type: TermsOfService
    url: https://www.adobe.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.adobe.com/privacy/policy.html
  - type: StatusPage
    url: https://status.adobe.com/
  - type: Blog
    url: https://blog.adobe.com/en/topics/analytics
  - type: GitHubRepository
    url: https://github.com/AdobeDocs/analytics-2.0-apis
  - type: JSONSchema
    url: json-schema/adobe-analytics-report-request-schema.json
  - type: JSONLD
    url: json-ld/adobe-analytics-context.jsonld
  - type: Features
    data:
      - name: Real-Time Analytics
        description: Access and analyze data in real time as visitors interact with digital properties.
      - name: Custom Segmentation
        description: Build custom segments to isolate and analyze specific visitor groups and behaviors.
      - name: Calculated Metrics
        description: Create derived metrics combining existing metrics with mathematical formulas.
      - name: Report Suites
        description: Organize and partition data collection across multiple sites and business units.
      - name: Annotations
        description: Mark specific dates or ranges in reports with notes for contextual analysis.
      - name: Bulk Data Insertion
        description: Upload server-side event data in compressed CSV batches for high-volume collection.
      - name: Data Repair
        description: Permanently delete or transform previously ingested data for privacy compliance.
      - name: Livestream
        description: Receive real-time streaming hit data as each event is processed by Adobe servers.
      - name: Dimension And Metric Exploration
        description: Programmatically discover all available dimensions and metrics in report suites.
      - name: Component Tagging
        description: Apply tags to segments, metrics, and other components for organization and discovery.
  - type: UseCases
    data:
      - name: Marketing Campaign Analysis
        description: Measure effectiveness of marketing campaigns across channels with attribution and conversion tracking.
      - name: Customer Journey Optimization
        description: Analyze multi-touch customer journeys to identify drop-off points and optimize conversion paths.
      - name: Content Performance Tracking
        description: Evaluate which content resonates most with audiences and drives engagement.
      - name: Audience Discovery And Targeting
        description: Discover high-value audience segments for personalized marketing and advertising.
      - name: Privacy Compliance Data Management
        description: Delete or repair PII and sensitive data to comply with GDPR, CCPA, and other regulations.
      - name: Real-Time Monitoring And Alerting
        description: Monitor live traffic and KPIs with streaming data for immediate anomaly detection.
      - name: Server-Side Data Collection
        description: Collect analytics data from backend systems, IoT devices, and server-side applications.
      - name: Cross-Channel Reporting
        description: Combine web, mobile, and offline data for unified cross-channel analytics reporting.
  - type: Integrations
    data:
      - name: Adobe Experience Platform
        description: Send Analytics data to Experience Platform for unified customer profiles and journey orchestration.
      - name: Adobe Target
        description: Use Analytics segments to power personalization and A/B testing in Adobe Target.
      - name: Adobe Audience Manager
        description: Share audience segments between Analytics and Audience Manager for cross-channel activation.
      - name: Adobe Campaign
        description: Integrate campaign data with Analytics for end-to-end campaign performance measurement.
      - name: Adobe Customer Journey Analytics
        description: Extend Analytics data into CJA for cross-channel analysis with Experience Platform data.
      - name: Adobe Launch
        description: Deploy and manage Analytics tags via Adobe Experience Platform Launch tag management.
      - name: Google Ads
        description: Import Google Ads cost and click data for integrated paid search analytics.
      - name: Microsoft Power BI
        description: Connect Analytics data to Power BI dashboards for enterprise reporting and visualization.
  - type: GitHubRepository
    url: https://github.com/AdobeDocs/analytics-mcp
    title: Analytics MCP Servers Documentation
  - type: GitHubRepository
    url: https://github.com/AdobeDocs/analytics-1.4-apis
    title: Analytics 1.4 APIs Documentation
  - type: Training
    url: https://experienceleague.adobe.com/docs/analytics-learn/tutorials/overview.html
  - type: JSONLD
    url: json-ld/adobe-analytics-bulk-data-insertion-context.jsonld
  - type: JSONLD
    url: json-ld/adobe-analytics-data-repair-context.jsonld
  - type: SpectralRules
    url: rules/adobe-analytics-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/adobe-analytics-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/reporting-and-analysis.yaml
  - type: NaftikoCapability
    url: capabilities/data-collection.yaml
---
