---
aid: stigg
name: Stigg
description: Stigg is a pricing and packaging platform providing feature management, entitlements, and usage-based billing for SaaS and API products. It enables engineering teams to integrate once and allows product managers to iterate on pricing without additional engineering effort. Stigg provides advanced metering, entitlement checks, and subscription management via GraphQL and REST APIs with SDKs in multiple languages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FinOps
  - Pricing
  - Billing
  - Entitlements
  - Usage-Based Billing
  - SaaS
url: https://raw.githubusercontent.com/api-evangelist/stigg/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stigg:stigg-graphql
    name: Stigg GraphQL API
    description: The Stigg GraphQL API provides full access to customer provisioning, subscription management, entitlement checking, usage reporting, and pricing plan management. Authentication uses the X-API-KEY header with a Full access key from the Stigg dashboard.
    humanURL: https://docs.stigg.io/api-and-sdks/integration/backend/graphql
    tags:
      - GraphQL
      - Entitlements
      - Subscriptions
      - Billing
    properties:
      - type: Documentation
        url: https://docs.stigg.io/api-and-sdks/integration/backend/graphql
      - type: GraphQL
        url: https://api.stigg.io/graphql
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stigg/refs/heads/main/openapi/stigg-openapi.yml
  - aid: stigg:stigg-rest
    name: Stigg REST API
    description: The Stigg REST API (Beta) provides language-agnostic HTTP access to customer management, subscription operations, entitlement checks, and usage reporting. Supports TypeScript, Python, Go, Ruby, C#, and Java SDKs.
    humanURL: https://docs.stigg.io/api-and-sdks/integration/overview
    tags:
      - REST
      - Entitlements
      - Subscriptions
      - Billing
    properties:
      - type: Documentation
        url: https://docs.stigg.io/api-and-sdks/integration/overview
  - aid: stigg:stigg-node-sdk
    name: Stigg Node.js SDK
    description: Official Node.js / TypeScript SDK for integrating Stigg entitlements, feature flags, and usage-based billing into backend services.
    humanURL: https://docs.stigg.io/api-and-sdks/integration/backend/nodejs
    tags:
      - Node.js
      - TypeScript
      - SDK
    properties:
      - type: Documentation
        url: https://docs.stigg.io/api-and-sdks/integration/backend/nodejs
  - aid: stigg:stigg-python-sdk
    name: Stigg Python SDK
    description: Official Python SDK for integrating Stigg entitlements and usage-based billing into Python backend services.
    humanURL: https://docs.stigg.io/api-and-sdks/integration/backend/python
    tags:
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://docs.stigg.io/api-and-sdks/integration/backend/python
  - aid: stigg:stigg-go-sdk
    name: Stigg Go SDK
    description: Official Go SDK for integrating Stigg entitlements and usage-based billing into Go backend services.
    humanURL: https://docs.stigg.io/api-and-sdks/integration/backend/go
    tags:
      - Go
      - SDK
    properties:
      - type: Documentation
        url: https://docs.stigg.io/api-and-sdks/integration/backend/go
  - aid: stigg:stigg-react-sdk
    name: Stigg React SDK
    description: Official React frontend SDK for rendering pricing tables, entitlement gates, and usage meters in React applications.
    humanURL: https://docs.stigg.io/api-and-sdks/integration/frontend/react
    tags:
      - React
      - Frontend
      - SDK
    properties:
      - type: Documentation
        url: https://docs.stigg.io/api-and-sdks/integration/frontend/react
common:
  - type: Website
    url: https://www.stigg.io/
  - type: Documentation
    url: https://docs.stigg.io/
  - type: Getting Started
    url: https://docs.stigg.io/getting-started
  - type: GitHub Organization
    url: https://github.com/stiggio
  - type: Sign Up
    url: https://app.stigg.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
