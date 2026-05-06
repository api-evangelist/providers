---
aid: adobe-experience-cloud
url: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/apis.yml
apis:
  - aid: adobe-experience-cloud:analytics-api
    name: Adobe Analytics 2.0 API
    tags:
      - Analytics
      - Digital Marketing
      - Reporting
    humanURL: https://developer.adobe.com/analytics-apis/docs/2.0/
    properties:
      - url: https://developer.adobe.com/analytics-apis/docs/2.0/
        type: Documentation
      - url: openapi/adobe-analytics-api-openapi.yml
        type: OpenAPI
    description: The Adobe Analytics 2.0 API provides programmatic access to Adobe Analytics reporting, management, and configuration capabilities. It enables developers to retrieve report data, manage report suites, configure calculated metrics, segments, and dimensions, and administer users and permissions within Adobe Analytics.
  - aid: adobe-experience-cloud:experience-platform-api
    name: Adobe Experience Platform API
    tags:
      - Customer Profiles
      - Data Management
      - Platform
    humanURL: https://developer.adobe.com/experience-platform-apis/
    properties:
      - url: https://developer.adobe.com/experience-platform-apis/
        type: Documentation
      - url: openapi/adobe-experience-platform-api-openapi.yml
        type: OpenAPI
    description: The Adobe Experience Platform API provides RESTful access to core platform services including data ingestion, unified profile management, identity resolution, dataset management, schema registry, query service, and segmentation for building real-time customer profiles and orchestrating data workflows.
  - aid: adobe-experience-cloud:target-api
    name: Adobe Target API
    tags:
      - Optimization
      - Personalization
      - Testing
    humanURL: https://developer.adobe.com/target/
    properties:
      - url: https://developer.adobe.com/target/
        type: Documentation
      - url: openapi/adobe-target-api-openapi.yml
        type: OpenAPI
    description: The Adobe Target API provides programmatic access to Adobe Target for managing A/B tests, experience targeting, multivariate tests, automated personalization activities, audiences, offers, and real-time content delivery for website and application personalization.
  - aid: adobe-experience-cloud:journey-optimizer-api
    name: Adobe Journey Optimizer API
    tags:
      - Journey Orchestration
      - Messaging
      - Offer Decisioning
    humanURL: https://developer.adobe.com/journey-optimizer-apis/
    properties:
      - url: https://developer.adobe.com/journey-optimizer-apis/
        type: Documentation
      - url: openapi/adobe-journey-optimizer-api-openapi.yml
        type: OpenAPI
    description: The Adobe Journey Optimizer API enables programmatic management of customer journeys, campaigns, messages, offers, placements, and content templates across email, push, SMS, and in-app channels for orchestrating personalized multi-channel customer experiences.
  - aid: adobe-experience-cloud:campaign-api
    name: Adobe Campaign API
    tags:
      - Campaign Management
      - Email Marketing
      - Transactional Messaging
    humanURL: https://developer.adobe.com/campaign-standard-apis/
    properties:
      - url: https://developer.adobe.com/campaign-standard-apis/
        type: Documentation
      - url: openapi/adobe-campaign-api-openapi.yml
        type: OpenAPI
    description: The Adobe Campaign API provides RESTful access to Adobe Campaign for managing subscriber profiles, subscription services, marketing workflows, email deliveries, and real-time transactional messaging across email, SMS, and push notification channels.
  - aid: adobe-experience-cloud:io-events
    name: Adobe I/O Events
    tags:
      - Events
      - Integration
      - Webhooks
    humanURL: https://developer.adobe.com/events/docs/
    properties:
      - url: https://developer.adobe.com/events/docs/
        type: Documentation
      - url: asyncapi/adobe-io-events-asyncapi.yml
        type: AsyncAPI
    description: Adobe I/O Events enables developers to receive near-real-time notifications from Adobe services via webhooks and journal polling. Events are emitted when significant changes occur across Adobe Experience Cloud products for building reactive integrations and automated workflows.
name: Adobe Experience Cloud
tags:
  - Analytics
  - Customer Experience
  - Digital Marketing
  - Personalization
  - Campaign Management
  - Journey Orchestration
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://developer.adobe.com/
    type: Portal
  - url: https://developer.adobe.com/developer-console/docs/guides/
    type: Documentation
  - url: https://developer.adobe.com/apis/
    type: Documentation
  - url: https://blog.developer.adobe.com/
    type: Blog
  - url: https://experienceleague.adobe.com/
    type: Support
  - type: TermsOfService
    url: https://www.adobe.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.adobe.com/privacy.html
  - type: StatusPage
    url: https://status.adobe.com/
  - type: Console
    url: https://developer.adobe.com/console/
  - type: SignUp
    url: https://developer.adobe.com/
  - type: GettingStarted
    url: https://developer.adobe.com/developer-console/docs/guides/getting-started/
  - type: GitHubOrganization
    url: https://github.com/adobe
  - type: YouTube
    url: https://www.youtube.com/user/AdobeDeveloperTV
  - type: ChangeLog
    url: https://developer.adobe.com/events/docs/whats_new/
  - type: Features
    data:
      - name: Real-Time Customer Profiles
        description: Build and query unified customer profiles from multiple data sources using the Experience Platform APIs.
      - name: Analytics Reporting
        description: Retrieve dimensional reports, calculated metrics, and segment data from Adobe Analytics via REST API.
      - name: A/B and Multivariate Testing
        description: Create, manage, and retrieve results for A/B tests and automated personalization activities via Adobe Target API.
      - name: Multi-Channel Campaign Execution
        description: Orchestrate email, SMS, push, and in-app campaigns programmatically using Adobe Campaign and Journey Optimizer APIs.
      - name: Webhook Event Streaming
        description: Subscribe to near-real-time events from all Adobe Experience Cloud products via Adobe I/O Events.
      - name: Offer Decisioning
        description: Manage offers, placements, and decisioning rules for personalized content delivery using Journey Optimizer APIs.
      - name: Data Ingestion and Schema Registry
        description: Ingest batch and streaming data and register schemas using Experience Platform APIs.
      - name: Identity Resolution
        description: Resolve customer identities across devices and channels using Experience Platform Identity Service API.
      - name: Audience Segmentation
        description: Create and evaluate audience segments using Experience Platform Segmentation Service API.
      - name: OAuth 2.0 and JWT Authentication
        description: Secure all APIs using OAuth 2.0 server-to-server credentials via Adobe Developer Console.
  - type: UseCases
    data:
      - name: Customer Data Platform
        description: Ingest data from multiple sources, resolve identities, and activate unified customer profiles for personalization.
      - name: Marketing Automation
        description: Automate campaign creation, scheduling, and execution across email, SMS, and push channels using Campaign and Journey Optimizer APIs.
      - name: Digital Analytics Reporting
        description: Extract Adobe Analytics data into custom dashboards, BI tools, and data warehouses via the Analytics 2.0 API.
      - name: Real-Time Personalization
        description: Deliver personalized content and offers in real time using Adobe Target and Journey Optimizer APIs.
      - name: Event-Driven Workflows
        description: Build reactive integrations that respond to Experience Cloud events such as profile updates, campaign completions, and audience changes.
      - name: Audience Activation
        description: Create and activate audiences across paid media, email, and on-site channels using Experience Platform Segmentation API.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync customer data and campaign results between Adobe Experience Cloud and Salesforce CRM.
      - name: Microsoft Azure
        description: Ingest data from Azure Data Lake and Blob Storage into Adobe Experience Platform.
      - name: Google BigQuery
        description: Connect Google BigQuery datasets to Adobe Experience Platform for data ingestion and activation.
      - name: Workfront
        description: Integrate Workfront project management with Adobe Experience Cloud for content workflow automation.
      - name: Marketo Engage
        description: Sync lead data and campaign activities between Marketo Engage and Adobe Experience Cloud.
      - name: ServiceNow
        description: Connect ServiceNow customer data with Adobe Experience Cloud for unified customer service experiences.
      - name: Snowflake
        description: Connect Snowflake data warehouse to Experience Platform for federated audience composition.
  - type: SpectralRules
    url: rules/adobe-experience-cloud-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/customer-data-platform.yaml
  - type: NaftikoCapability
    url: capabilities/digital-marketing.yaml
  - type: Vocabulary
    url: vocabulary/adobe-experience-cloud-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-analytics-api-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-campaign-api-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-experience-platform-api-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-io-events-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-journey-optimizer-api-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-experience-cloud-target-api-context.jsonld
created: '2025-01-01'
modified: '2026-04-19'
description: Adobe Experience Cloud is an integrated suite of applications and services for digital marketing, analytics, advertising, and commerce. It provides tools for content management, personalization, customer journey orchestration, audience segmentation, real-time customer data platforms, offer decisioning, and cross-channel campaign execution, enabling organizations to deliver personalized customer experiences at scale.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
