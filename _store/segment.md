---
aid: segment
url: https://raw.githubusercontent.com/api-evangelist/segment/refs/heads/main/apis.yml
modified: '2026-05-04'
apis:
  - aid: segment:public-api
    name: Segment Public API
    tags:
      - Analytics
      - Customer Data
      - Destinations
      - Sources
      - Workspace Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.segmentapis.com
    humanURL: https://docs.segmentapis.com/
    properties:
      - url: https://docs.segmentapis.com/
        type: Documentation
      - url: openapi/segment-public-api-openapi.yml
        type: OpenAPI
    description: The Segment Public API allows developers to programmatically manage Segment workspaces and their resources. It supports full CRUD operations for sources, destinations, warehouses, tracking plans, and catalog entries. The API follows REST conventions with standard HTTP methods and predictable resource-oriented URLs. It is available for Team and Business tier customers and is the recommended API going forward, replacing the older Config API.
  - aid: segment:http-tracking-api
    name: Segment HTTP Tracking API
    tags:
      - Analytics
      - Customer Data
      - Events
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.segment.io
    humanURL: https://www.twilio.com/docs/segment/connections/sources/catalog/libraries/server/http-api
    properties:
      - url: https://www.twilio.com/docs/segment/connections/sources/catalog/libraries/server/http-api
        type: Documentation
      - url: openapi/segment-http-tracking-api-openapi.yml
        type: OpenAPI
      - url: asyncapi/segment-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The Segment HTTP Tracking API enables developers to record analytics data from any website or application by sending HTTP requests directly to Segment servers. It supports identify, track, page, screen, group, and alias calls, and Segment routes the collected data to configured destinations. The API accepts batch requests up to 500 KB and requires each payload to include a userId or anonymousId. It is a server-side alternative to Segment's client-side SDKs.
  - aid: segment:profile-api
    name: Segment Profile API
    tags:
      - Customer Data
      - Identity Resolution
      - Profiles
      - Unify
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://profiles.segment.com
    humanURL: https://www.twilio.com/docs/segment/unify/profile-api
    properties:
      - url: https://www.twilio.com/docs/segment/unify/profile-api
        type: Documentation
      - url: openapi/segment-profile-api-openapi.yml
        type: OpenAPI
    description: The Segment Profile API provides a single endpoint to read user-level and account-level customer data from Segment Unify. Developers can query the entire user or account object programmatically, including external IDs, traits, and events that make up a user's journey. The API uses basic authentication and typically delivers p95 response times under 200ms for the traits endpoint. It is commonly used for real-time personalization and customer data retrieval.
  - aid: segment:config-api
    name: Segment Config API
    tags:
      - Configuration
      - Destinations
      - Legacy
      - Sources
      - Workspace Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://platform.segmentapis.com
    humanURL: https://www.twilio.com/docs/segment/api/config-api
    properties:
      - url: https://www.twilio.com/docs/segment/api/config-api
        type: Documentation
      - url: openapi/segment-config-api-openapi.yml
        type: OpenAPI
    description: The Segment Config API allows programmatic management of Segment workspaces, sources, destinations, and other configuration resources. It provides endpoints to list workspace sources and destinations, create or delete destinations, and manage tracking plans. As of early 2024, Segment has stopped issuing new Config API tokens and recommends migrating to the Public API for access to the latest features. The Config API remains functional for existing users but is no longer actively developed.
  - aid: segment:pixel-tracking-api
    name: Segment Pixel Tracking API
    tags:
      - Analytics
      - Email
      - Pixel
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.segment.io
    humanURL: https://www.twilio.com/docs/segment/connections/sources/catalog/libraries/server/pixel-tracking-api
    properties:
      - url: https://www.twilio.com/docs/segment/connections/sources/catalog/libraries/server/pixel-tracking-api
        type: Documentation
      - url: openapi/segment-pixel-tracking-api-openapi.yml
        type: OpenAPI
    description: The Segment Pixel Tracking API provides a way to collect analytics data using image pixel requests, which is useful in environments where JavaScript cannot execute, such as email clients. It supports identify, track, page, screen, group, and alias calls through pixel endpoints under the api.segment.io domain. This API is particularly suited for tracking email opens, ad impressions, and other contexts where embedding a tracking pixel is the only viable data collection method.
common:
  - type: JSON-LD
    url: json-ld/segment-context.jsonld
  - type: JSONSchema
    url: json-schema/segment-event-schema.json
  - type: JSONSchema
    url: json-schema/segment-source-schema.json
  - type: JSONSchema
    url: json-schema/segment-destination-schema.json
  - type: Features
    data:
      - Free Developer plan up to ~1,000 visitors and 2 sources
      - Customer Data Pipeline custom-quoted via sales
      - Customer Data Platform (Unify + Engage) custom-quoted
      - 700+ destinations including warehouses, advertising, analytics
      - Tracking API up to 30,000 events/sec/source
      - Public API at 600 req/min/workspace
      - Functions for custom source/destination logic
      - Reverse ETL for warehouse-to-tool syncs
      - Identity resolution via Unify
      - AI-powered audiences and predictions
      - Generative audiences
      - Protocols add-on for tracking plan governance
      - OAuth 2.0 + workspace API tokens
      - HIPAA-eligible regional CDP options
      - Dedicated CSM on CDP plan
      - Connections to 90+ warehouses including BigQuery, Snowflake, Databricks
    sources:
      - https://www.twilio.com/en-us/pricing/customer-data
    updated: '2026-05-04'
description: Segment is a customer data platform that helps companies collect, clean, and route customer data to hundreds of tools used for analytics, marketing, and data warehousing.
---
