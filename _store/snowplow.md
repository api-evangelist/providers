---
aid: snowplow
name: Snowplow
description: Snowplow is a behavioral data platform that enables organizations to collect, process, and model granular event-level data from web, mobile, and server-side sources, providing a data pipeline for analytics and AI use cases. The platform uses a schema-first approach with self-describing JSON events validated against the Iglu schema registry. The Snowplow Console API provides programmatic governance of data structures (schemas), data products (tracking plans), and event specifications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics Platform
  - Behavioral Data
  - Data Collection
  - Data Engineering
  - Data Pipeline
  - Event Tracking
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/snowplow/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: snowplow:snowplow-console-api
    name: Snowplow Console API
    description: The Snowplow Console API provides programmatic management of the Snowplow behavioral data platform. Covers data structures (JSON schemas for event validation), data products (tracking plans), event specifications, and credentials. All endpoints are scoped to an organization and require JWT bearer authentication. Accessible via Swagger UI at https://console.snowplowanalytics.com/api/msc/v1/docs/.
    humanURL: https://docs.snowplow.io/docs/event-studio/programmatic-management/
    tags:
      - Analytics Platform
      - Data Governance
      - Data Structures
      - Schema Management
    properties:
      - type: Documentation
        url: https://docs.snowplow.io/docs/event-studio/programmatic-management/
      - type: SwaggerUI
        url: https://console.snowplowanalytics.com/api/msc/v1/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/snowplow/refs/heads/main/openapi/snowplow-console-api-openapi.yml
  - aid: snowplow:snowplow-trackers
    name: Snowplow Tracker SDKs
    description: Snowplow provides tracker SDKs for all major platforms including JavaScript (web), iOS, Android, Python, Java, Go, Ruby, .NET, PHP, and Rust. Trackers generate self-describing events and send them to the Snowplow Collector. All trackers support self-describing events, contexts, page views, structured events, and session tracking.
    humanURL: https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications
    tags:
      - Analytics
      - Event Tracking
      - SDK
    properties:
      - type: Documentation
        url: https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications
      - type: GitHubOrg
        url: https://github.com/snowplow
common:
  - type: Website
    url: https://snowplow.io
  - type: Documentation
    url: https://docs.snowplow.io
  - type: Blog
    url: https://snowplow.io/blog
  - type: Pricing
    url: https://snowplow.io/pricing
  - type: GitHub
    url: https://github.com/snowplow
  - type: Login
    url: https://console.snowplowanalytics.com
  - type: Signup
    url: https://snowplow.io/get-started
  - type: Support
    url: https://snowplow.io/support
  - type: GettingStarted
    url: https://docs.snowplow.io/docs/getting-started-on-snowplow-open-source
  - type: Community
    url: https://discourse.snowplow.io
  - type: DataStructuresAPI
    url: https://docs.snowplow.io/docs/data-product-studio/data-structures/manage/api/
  - type: TrackingPlansAPI
    url: https://docs.snowplow.io/docs/data-product-studio/data-products/api/
  - type: CredentialsAPI
    url: https://docs.snowplow.io/docs/account-management/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
