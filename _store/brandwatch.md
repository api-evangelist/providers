---
aid: brandwatch
url: https://raw.githubusercontent.com/api-evangelist/brandwatch/refs/heads/main/apis.yml
name: Brandwatch
tags:
  - Analytics
  - Social Media
  - Social Media Monitoring
  - Consumer Intelligence
  - Brand Management
  - Sentiment Analysis
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-21'
position: Consumer
description: Brandwatch is a leading consumer intelligence and social media analytics platform providing access to trillions of consumer conversations. The platform offers six distinct APIs for analysis, data upload, consumer research, social metrics, publishing, and engagement. Businesses use Brandwatch to track brand mentions, monitor competitors, analyze sentiment, and integrate social data with existing analytics and CRM systems for strategic decision-making.
apis:
  - aid: brandwatch:analysis-api
    name: Brandwatch Analysis API
    tags:
      - Analytics
      - Social Media
      - Sentiment Analysis
      - Aggregated Statistics
    humanURL: https://www.brandwatch.com/products/apis/
    properties:
      - url: https://www.brandwatch.com/products/apis/
        type: Documentation
    description: Query Brandwatch's content library or imported data to return aggregated statistics and computed analysis. Enables programmatic access to brand mention analytics, sentiment scores, volume trends, and consumer insights across social media platforms, news sites, and forums.
  - aid: brandwatch:data-upload-api
    name: Brandwatch Data Upload API
    tags:
      - Data Import
      - Custom Data
      - Analytics
    humanURL: https://www.brandwatch.com/products/apis/
    properties:
      - url: https://www.brandwatch.com/products/apis/
        type: Documentation
    description: Import unstructured data from any source for analysis alongside consumer conversation data. Enables organizations to blend proprietary data with Brandwatch's social intelligence for unified analytics.
  - aid: brandwatch:consumer-research-api
    name: Brandwatch Consumer Research API
    tags:
      - Consumer Research
      - Data Export
      - Real-time Streaming
    humanURL: https://www.brandwatch.com/products/apis/
    properties:
      - url: https://www.brandwatch.com/products/apis/
        type: Documentation
    description: Export analysis results for further research and integration with existing systems. Supports real-time data streaming alongside consumer conversation data for continuous monitoring and research workflows.
  - aid: brandwatch:measure-api
    name: Brandwatch Measure API
    tags:
      - Social Metrics
      - Owned Social
      - Reporting
    humanURL: https://www.brandwatch.com/products/apis/
    properties:
      - url: https://www.brandwatch.com/products/apis/
        type: Documentation
    description: Integrate owned social media metrics into external analytics solutions for custom reporting. Enables organizations to combine their social channel performance data with Brandwatch's audience intelligence in third-party BI and reporting platforms.
  - aid: brandwatch:publish-api
    name: Brandwatch Publish API
    tags:
      - Publishing
      - Content Management
      - Social Media
    humanURL: https://www.brandwatch.com/products/apis/
    properties:
      - url: https://www.brandwatch.com/products/apis/
        type: Documentation
    description: Export social publishing data to integrate with content management systems. Enables workflow automation between Brandwatch's publishing tools and external CMS platforms for unified content operations.
  - aid: brandwatch:engage-api
    name: Brandwatch Engage API
    tags:
      - Social Engagement
      - Customer Service
      - Inbox Management
    humanURL: https://www.brandwatch.com/products/apis/
    properties:
      - url: https://www.brandwatch.com/products/apis/
        type: Documentation
    description: Consolidate conversations from social media inboxes with customer inquiries across platforms. Enables integration of Brandwatch's engagement tools with CRM and customer service systems for unified conversation management.
common:
  - type: Website
    url: https://www.brandwatch.com
  - type: APIProducts
    url: https://www.brandwatch.com/products/apis/
  - type: Documentation
    url: https://developers.brandwatch.com
properties:
  - type: x-domain
    value: brandwatch.com
  - type: x-founded
    value: '2007'
  - type: x-headquarters
    value: Brighton, United Kingdom
  - type: x-parent-company
    value: Cision
  - type: x-industry
    value: Consumer Intelligence, Social Media Analytics
  - type: x-data-scale
    value: Trillions of consumer conversations
  - type: x-api-products
    value: Analysis API, Data Upload API, Consumer Research API, Measure API, Publish API, Engage API
  - type: x-use-cases
    value: Brand monitoring, competitor analysis, sentiment analysis, consumer research, social media reporting, content management integration, customer service consolidation, market research
  - type: x-capabilities
    value: Social listening, real-time data streaming, aggregated statistics, sentiment scoring, custom data import, owned social metrics, publishing workflow integration, cross-platform conversation management
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
