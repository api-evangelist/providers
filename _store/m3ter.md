---
aid: m3ter
name: M3ter
description: 'm3ter is a usage-based billing and metering engine providing real-time usage data ingestion, pricing logic, and billing automation for API and SaaS products. The m3ter platform exposes two HTTP-based REST APIs returning JSON responses: an Ingest API for submitting raw usage measurements and a Config API for configuration and billing management. Authentication uses OAuth 2.0 Client Credentials with a Service User Access Key id and Api Secret exchanged for a Bearer Token at https://api.m3ter.com/oauth/token.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FinOps
  - Usage-Based Billing
  - Metering
  - Billing
  - Pricing
  - SaaS
url: https://raw.githubusercontent.com/api-evangelist/m3ter/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: m3ter:m3ter
    name: M3ter API
    description: The m3ter REST API provides programmatic access to the m3ter usage-based billing and metering platform. It is split into the Ingest API for submitting raw measurement data and the Config API for managing Accounts, Plans, Products, Aggregations, Counters, Meters, Pricing, Bills, Commitments, Contracts, Balances, BillJobs, Charges, Notifications, Events, Integrations, and Data Exports. Authentication uses OAuth 2.0 Client Credentials. The base URL is https://api.m3ter.com.
    humanURL: https://www.m3ter.com/
    baseURL: https://api.m3ter.com
    tags:
      - FinOps
      - Usage-Based Billing
      - Metering
      - Billing
      - Pricing
    properties:
      - type: Documentation
        url: https://docs.m3ter.com/
      - type: APIReference
        url: https://docs.m3ter.com/api
      - type: Authentication
        url: https://docs.m3ter.com/api/authentication
      - type: GettingStarted
        url: https://www.m3ter.com/docs/guides/m3ter-apis/getting-started-with-api-calls
      - type: OpenAPI
        url: openapi/m3ter-openapi.yml
      - type: SDK
        url: https://github.com/m3ter-com/m3ter-sdk-python
      - type: SDK
        url: https://github.com/m3ter-com/m3ter-sdk-node
      - type: SDK
        url: https://github.com/m3ter-com/m3ter-sdk-java
      - type: SDK
        url: https://github.com/m3ter-com/m3ter-sdk-go
      - type: SDK
        url: https://github.com/m3ter-com/m3ter-sdk-typescript
      - type: TerraformProvider
        url: https://github.com/m3ter-com/terraform-provider-m3ter
common:
  - type: Website
    url: https://www.m3ter.com/
  - type: Documentation
    url: https://docs.m3ter.com/
  - type: APIReference
    url: https://docs.m3ter.com/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
