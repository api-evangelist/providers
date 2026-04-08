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
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Adobe Experience Cloud is an integrated suite of applications and services for digital marketing, analytics, advertising, and commerce. It provides tools for content management, personalization, customer journey orchestration, audience segmentation, real-time customer data platforms, offer decisioning, and cross-channel campaign execution, enabling organizations to deliver personalized customer experiences at scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

