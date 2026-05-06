---
aid: google-analytics
name: Google Analytics
description: Google Analytics provides data and insights about website and app usage, enabling businesses to understand their audience and optimize their digital properties through customer-centric measurement, machine learning insights, and cross-platform attribution.
type: Index
image: https://www.google.com/analytics/images/google-analytics-logo.png
url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-17'
specificationVersion: '0.19'
tags:
  - Analytics
  - Data
  - Google
  - Metrics
  - Reporting
  - Web Analytics
  - Machine Learning
  - Attribution
apis:
  - aid: google-analytics:google-analytics-data-api
    name: Google Analytics Data API (GA4)
    description: The Google Analytics Data API provides programmatic access to Google Analytics 4 (GA4) report data including standard reports, pivot reports, real-time reports, funnel reports, and audience exports.
    image: https://www.google.com/analytics/images/google-analytics-logo.png
    humanURL: https://developers.google.com/analytics/devguides/reporting/data/v1
    baseURL: https://analyticsdata.googleapis.com
    properties:
      - type: Documentation
        url: https://developers.google.com/analytics/devguides/reporting/data/v1
      - type: OpenAPI
        url: openapi/google-analytics-data-api.yaml
      - type: APIReference
        url: https://developers.google.com/analytics/devguides/reporting/data/v1/rest
      - type: Quickstart
        url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart
      - type: Authentication
        url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
      - type: RateLimits
        url: https://developers.google.com/analytics/devguides/reporting/data/v1/quotas
      - type: SDK
        url: https://pypi.org/project/google-analytics-data/
        title: Python SDK
      - type: SDK
        url: https://www.npmjs.com/package/@google-analytics/data
        title: Node.js SDK
      - type: SDK
        url: https://central.sonatype.com/artifact/com.google.analytics/google-analytics-data
        title: Java SDK
      - type: SDK
        url: https://www.nuget.org/packages/Google.Analytics.Data.V1Beta
        title: .NET SDK
      - type: SDK
        url: https://packagist.org/packages/google/analytics-data
        title: PHP SDK
      - type: CodeExamples
        url: https://github.com/googleanalytics/python-docs-samples
        title: Python Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/java-docs-samples
        title: Java Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/nodejs-docs-samples
        title: Node.js Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/dotnet-docs-samples
        title: .NET Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/php-docs-samples
        title: PHP Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/analytics-data-curl-examples
        title: Curl Examples
      - type: CodeExamples
        url: https://github.com/googleanalytics/analytics-data-javascript-examples
        title: JavaScript Examples
    tags:
      - Analytics
      - Data API
      - GA4
      - Reporting
      - Real-Time
      - Funnels
  - aid: google-analytics:google-analytics-admin-api
    name: Google Analytics Admin API
    description: The Analytics Admin API allows programmatic access to configuration data for Google Analytics 4 properties including account management, data streams, custom dimensions, key events, user permissions, and integration linking.
    image: https://www.google.com/analytics/images/google-analytics-logo.png
    humanURL: https://developers.google.com/analytics/devguides/config/admin/v1
    baseURL: https://analyticsadmin.googleapis.com
    properties:
      - type: Documentation
        url: https://developers.google.com/analytics/devguides/config/admin/v1
      - type: OpenAPI
        url: openapi/google-analytics-admin-api.yaml
      - type: APIReference
        url: https://developers.google.com/analytics/devguides/config/admin/v1/rest
      - type: Quickstart
        url: https://developers.google.com/analytics/devguides/config/admin/v1/quickstart
      - type: SDK
        url: https://developers.google.com/analytics/devguides/config/admin/v1/client-libraries
      - type: SDK
        url: https://pypi.org/project/google-analytics-admin/
        title: Python SDK
      - type: SDK
        url: https://www.npmjs.com/package/@google-analytics/admin
        title: Node.js SDK
      - type: SDK
        url: https://central.sonatype.com/artifact/com.google.analytics/google-analytics-admin
        title: Java SDK
      - type: SDK
        url: https://www.nuget.org/packages/Google.Analytics.Admin.V1Beta
        title: .NET SDK
      - type: SDK
        url: https://packagist.org/packages/google/analytics-admin
        title: PHP SDK
      - type: CodeExamples
        url: https://github.com/googleanalytics/python-docs-samples
        title: Python Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/java-docs-samples
        title: Java Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/nodejs-docs-samples
        title: Node.js Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/dotnet-docs-samples
        title: .NET Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/php-docs-samples
        title: PHP Samples
      - type: CodeExamples
        url: https://github.com/googleanalytics/analytics-samples-config
        title: Configuration Samples
    tags:
      - Admin
      - Configuration
      - GA4
      - Management
      - Permissions
  - aid: google-analytics:google-analytics-measurement-protocol
    name: Google Analytics Measurement Protocol (GA4)
    description: The Measurement Protocol lets you send events directly to Google Analytics servers via HTTP requests to augment existing GA4 data with server-to-server and offline interactions.
    image: https://www.google.com/analytics/images/google-analytics-logo.png
    humanURL: https://developers.google.com/analytics/devguides/collection/protocol/ga4
    baseURL: https://www.google-analytics.com
    properties:
      - type: Documentation
        url: https://developers.google.com/analytics/devguides/collection/protocol/ga4
      - type: APIReference
        url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference
      - type: Quickstart
        url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/sending-events
      - type: OpenAPI
        url: openapi/google-analytics-measurement-protocol.yaml
      - type: Troubleshooting
        url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/troubleshooting
    tags:
      - Events
      - Measurement
      - Server-Side
      - Tracking
  - aid: google-analytics:google-analytics-user-deletion-api
    name: Google Analytics User Deletion API
    description: The User Deletion API enables removal of data linked to specific user identifiers in Google Analytics, supporting compliance with data protection and privacy requirements.
    image: https://www.google.com/analytics/images/google-analytics-logo.png
    humanURL: https://developers.google.com/analytics/devguides/config/userdeletion/v3
    baseURL: https://www.googleapis.com/analytics/v3
    properties:
      - type: Documentation
        url: https://developers.google.com/analytics/devguides/config/userdeletion/v3
      - type: APIReference
        url: https://developers.google.com/analytics/devguides/config/userdeletion/v3/reference
      - type: OpenAPI
        url: openapi/google-analytics-user-deletion-api.yaml
      - type: Authentication
        url: https://developers.google.com/analytics/devguides/config/userdeletion/v3/authorization
    tags:
      - Compliance
      - Data Privacy
      - GDPR
      - User Deletion
  - aid: google-analytics:google-analytics-reporting-api-v4
    name: Google Analytics Reporting API v4 (Universal Analytics)
    description: The Analytics Reporting API v4 provides programmatic access to Universal Analytics report data. Universal Analytics was sunset on July 1, 2023 and users should migrate to GA4.
    image: https://www.google.com/analytics/images/google-analytics-logo.png
    humanURL: https://developers.google.com/analytics/devguides/reporting/core/v4
    baseURL: https://analyticsreporting.googleapis.com
    properties:
      - type: Documentation
        url: https://developers.google.com/analytics/devguides/reporting/core/v4
      - type: OpenAPI
        url: openapi/google-analytics-reporting-api-v4.yaml
      - type: GettingStarted
        url: https://developers.google.com/analytics/devguides/migration/api/reporting-ua-to-ga4
    tags:
      - Analytics
      - Deprecated
      - Legacy
      - Reporting
      - Universal Analytics
  - aid: google-analytics:google-analytics-management-api-v3
    name: Google Analytics Management API v3
    description: The Analytics Management API allows access to configuration data for Universal Analytics accounts, properties, and views. Deprecated with Universal Analytics sunset.
    image: https://www.google.com/analytics/images/google-analytics-logo.png
    humanURL: https://developers.google.com/analytics/devguides/config/mgmt/v3
    baseURL: https://www.googleapis.com/analytics/v3
    properties:
      - type: Documentation
        url: https://developers.google.com/analytics/devguides/config/mgmt/v3
      - type: OpenAPI
        url: openapi/google-analytics-management-api-v3.yaml
      - type: APIReference
        url: https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference
    tags:
      - Configuration
      - Deprecated
      - Legacy
      - Management
      - Universal Analytics
common:
  - type: GettingStarted
    url: https://developers.google.com/analytics/get-started
  - type: Portal
    url: https://developers.google.com/analytics
  - type: Console
    url: https://console.cloud.google.com/apis/library/analytics.googleapis.com
  - type: SignUp
    url: https://analytics.google.com/analytics/
  - type: Authentication
    url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
  - type: SDK
    url: https://developers.google.com/analytics/devguides/config/admin/v1/client-libraries
  - type: Tools
    url: https://github.com/googleanalytics/google-analytics-mcp
    title: MCP Server
  - type: Tools
    url: https://ga-dev-tools.google/ga4/
    title: GA Dev Tools
  - type: Tools
    url: https://github.com/googleanalytics/ecommerce-migration-helper
    title: E-commerce Migration Helper
  - type: Tutorials
    url: https://github.com/googleanalytics/ga4-tutorials
    title: GA4 Tutorials
  - type: CodeExamples
    url: https://github.com/googleanalytics/gtm-consent-mode-examples
    title: Consent Mode Examples
  - type: Pricing
    url: https://marketingplatform.google.com/about/analytics/
  - type: TermsOfService
    url: https://developers.google.com/analytics/terms
  - type: PrivacyPolicy
    url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/policy
  - type: Blog
    url: https://analytics.googleblog.com/
  - type: StatusPage
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/analytics/support
  - type: FAQ
    url: https://support.google.com/analytics
  - type: ReleaseNotes
    url: https://support.google.com/analytics/answer/9164320
  - type: ChangeLog
    url: https://groups.google.com/forum/#!forum/google-analytics-api-notify
  - type: Skills
    data:
      - name: Run Report
        url: skills/run-report/SKILL.md
      - name: Run Realtime Report
        url: skills/run-realtime-report/SKILL.md
      - name: Run Pivot Report
        url: skills/run-pivot-report/SKILL.md
      - name: Batch Run Reports
        url: skills/batch-run-reports/SKILL.md
      - name: Batch Run Pivot Reports
        url: skills/batch-run-pivot-reports/SKILL.md
      - name: Check Compatibility
        url: skills/check-compatibility/SKILL.md
      - name: Create Audience Export
        url: skills/create-audience-export/SKILL.md
      - name: Get Audience Export
        url: skills/get-audience-export/SKILL.md
      - name: List Audience Exports
        url: skills/list-audience-exports/SKILL.md
      - name: Query Audience Export
        url: skills/query-audience-export/SKILL.md
      - name: List Account Summaries
        url: skills/list-account-summaries/SKILL.md
      - name: List Accounts
        url: skills/list-accounts/SKILL.md
      - name: Provision Account Ticket
        url: skills/provision-account-ticket/SKILL.md
      - name: List Properties
        url: skills/list-properties/SKILL.md
      - name: Create Property
        url: skills/create-property/SKILL.md
      - name: Search Change History Events
        url: skills/search-change-history-events/SKILL.md
      - name: Run Access Report
        url: skills/run-access-report/SKILL.md
      - name: Delete Google Ads Link
        url: skills/delete-google-ads-link/SKILL.md
      - name: Get Measurement Protocol Secret
        url: skills/get-measurement-protocol-secret/SKILL.md
      - name: Update Google Ads Link
        url: skills/update-google-ads-link/SKILL.md
      - name: Archive Custom Metric
        url: skills/archive-custom-metric/SKILL.md
      - name: List Conversion Events
        url: skills/list-conversion-events/SKILL.md
      - name: Create Conversion Event
        url: skills/create-conversion-event/SKILL.md
      - name: List Custom Dimensions
        url: skills/list-custom-dimensions/SKILL.md
      - name: Create Custom Dimension
        url: skills/create-custom-dimension/SKILL.md
      - name: List Custom Metrics
        url: skills/list-custom-metrics/SKILL.md
      - name: Create Custom Metric
        url: skills/create-custom-metric/SKILL.md
      - name: List Data Streams
        url: skills/list-data-streams/SKILL.md
      - name: Create Data Stream
        url: skills/create-data-stream/SKILL.md
      - name: List Firebase Links
        url: skills/list-firebase-links/SKILL.md
      - name: Create Firebase Link
        url: skills/create-firebase-link/SKILL.md
      - name: List Google Ads Links
        url: skills/list-google-ads-links/SKILL.md
      - name: Create Google Ads Link
        url: skills/create-google-ads-link/SKILL.md
      - name: List Measurement Protocol Secrets
        url: skills/list-measurement-protocol-secrets/SKILL.md
      - name: Create Measurement Protocol Secret
        url: skills/create-measurement-protocol-secret/SKILL.md
      - name: Acknowledge User Data Collection
        url: skills/acknowledge-user-data-collection/SKILL.md
      - name: Send Events
        url: skills/send-events/SKILL.md
      - name: Validate Events
        url: skills/validate-events/SKILL.md
      - name: Upsert User Deletion Request
        url: skills/upsert-user-deletion-request/SKILL.md
  - type: GitHubOrganization
    url: https://github.com/googleanalytics/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/google-analytics
  - type: YouTube
    url: https://www.youtube.com/user/googleanalytics
  - type: Training
    url: https://goo.gle/ga-courses
  - type: Academy
    url: https://marketingplatformacademy.withgoogle.com/google-analytics-360
  - type: Features
    data:
      - name: Predictive Capabilities
        description: Machine learning models that predict future actions users may take, like purchasing or churning.
      - name: Proactive Insights
        description: Automatically detects and surfaces actionable insights from your data.
      - name: Real-Time Reporting
        description: Monitor user activity on your site or app as it happens.
      - name: Data-Driven Attribution
        description: Machine learning to understand how each touchpoint contributes to conversions.
      - name: Free-Form Exploration
        description: Drag-and-drop analysis with instant visualizations for custom reporting.
      - name: Funnel Exploration
        description: Visualize user steps through conversion funnels and identify optimization opportunities.
      - name: Path Exploration
        description: Visualize user navigation paths to understand how users reach conversions.
      - name: Cohort Exploration
        description: Analyze behavior of users grouped by common attributes over time.
      - name: BigQuery Export
        description: Export raw event data to BigQuery for advanced analysis and data warehousing.
      - name: Cross-Platform Measurement
        description: Customer-centric measurement across websites and apps throughout the entire customer lifecycle.
      - name: Privacy-Safe Modeling
        description: Machine learning models that provide a complete picture of the customer journey while respecting privacy.
      - name: Custom Dimensions and Metrics
        description: Define custom dimensions and metrics to capture data specific to your business needs.
  - type: UseCases
    data:
      - name: Website Traffic Analysis
        description: Understand where visitors come from, what pages they view, and how they interact with your website.
      - name: Conversion Optimization
        description: Track conversion events, analyze funnels, and identify drop-off points to improve conversion rates.
      - name: Audience Segmentation
        description: Segment users by demographics, behavior, technology, and custom attributes for targeted analysis.
      - name: Marketing Campaign Measurement
        description: Measure the effectiveness of advertising campaigns across channels with attribution modeling.
      - name: E-commerce Analytics
        description: Track purchase activity, revenue, product performance, and shopping behavior.
      - name: App Analytics
        description: Measure user engagement, retention, and in-app actions for mobile and web applications.
      - name: Server-Side Event Tracking
        description: Send events from your server using the Measurement Protocol for offline and backend interactions.
      - name: Compliance and Data Privacy
        description: Manage user data deletion requests and privacy compliance using the User Deletion API.
      - name: Custom Reporting and Dashboards
        description: Build custom reports and dashboards programmatically using the Data API.
      - name: Real-Time Monitoring
        description: Monitor live user activity for time-sensitive campaigns, launches, and events.
  - type: Integrations
    data:
      - name: Google Ads
        description: Link Google Ads accounts to analyze campaign performance and optimize ad spend with Analytics data.
      - name: Google BigQuery
        description: Export raw Analytics data to BigQuery for advanced SQL-based analysis and data warehousing.
      - name: Google Search Console
        description: Connect Search Console to see organic search queries, impressions, and click data alongside Analytics.
      - name: Firebase
        description: Integrate with Firebase for comprehensive mobile and web app analytics and event tracking.
      - name: Display & Video 360
        description: Link DV360 for programmatic advertising measurement and attribution.
      - name: Search Ads 360
        description: Connect SA360 for unified search advertising measurement across engines.
      - name: Google Tag Manager
        description: Use Tag Manager to deploy and manage Analytics tags without modifying website code.
      - name: Google Ad Manager
        description: Integrate publisher ad serving data with Analytics for holistic content and ad performance analysis.
      - name: Google Cloud
        description: Leverage Google Cloud services for advanced data processing, ML models, and storage with Analytics data.
      - name: Salesforce Marketing Cloud
        description: Connect Salesforce Marketing Cloud for cross-platform marketing measurement and audience activation.
  - type: Solutions
    data:
      - name: Google Analytics Free
        description: Full-featured web and app analytics solution available at no charge for businesses of all sizes.
      - name: Analytics 360
        description: Enterprise-grade analytics with advanced features including intraday data, sub-properties, roll-up reporting, and higher limits.
      - name: Google Marketing Platform
        description: Integrated advertising and analytics platform combining Analytics 360 with advertising products for enterprise marketing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
