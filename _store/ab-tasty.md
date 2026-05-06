---
aid: ab-tasty
url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/apis.yml
apis:
  - aid: ab-tasty:ab-tasty-decision-api
    name: AB Tasty Decision API
    humanURL: https://docs.abtasty.com/server-side/decision-api/decision-api
    properties:
      - url: https://docs.abtasty.com/server-side/decision-api/decision-api
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/openapi/decision-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-campaign-request-schema.json
        type: JSONSchema
        title: Campaign Request
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-campaign-schema.json
        type: JSONSchema
        title: Campaign
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-flag-schema.json
        type: JSONSchema
        title: Flag
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-flags-response-schema.json
        type: JSONSchema
        title: Flags Response
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-activation-request-schema.json
        type: JSONSchema
        title: Activation Request
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-flag-metadata-schema.json
        type: JSONSchema
        title: Flag Metadata
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-campaign-response-normal-schema.json
        type: JSONSchema
        title: Campaign Response Normal
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-campaign-response-simple-schema.json
        type: JSONSchema
        title: Campaign Response Simple
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-campaign-response-full-schema.json
        type: JSONSchema
        title: Campaign Response Full
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-batch-activation-request-schema.json
        type: JSONSchema
        title: Batch Activation Request
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-batch-activation-item-schema.json
        type: JSONSchema
        title: Batch Activation Item
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-campaign-variation-schema.json
        type: JSONSchema
        title: Campaign Variation
      - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-schema/decision-api-single-campaign-request-schema.json
        type: JSONSchema
        title: Single Campaign Request
      - url: https://github.com/flagship-io/flagship-ts-sdk
        type: SDK
        title: TypeScript SDK
      - url: https://github.com/flagship-io/flagship-react-sdk
        type: SDK
        title: React SDK
      - url: https://github.com/flagship-io/flagship-react-native-sdk
        type: SDK
        title: React Native SDK
      - url: https://github.com/flagship-io/flagship-flutter-sdk
        type: SDK
        title: Flutter SDK
      - url: https://github.com/flagship-io/flagship-php-sdk
        type: SDK
        title: PHP SDK
      - url: https://github.com/flagship-io/flagship-dotnet-sdk
        type: SDK
        title: .NET SDK
      - url: https://github.com/flagship-io/flagship-android
        type: SDK
        title: Android SDK
      - url: https://github.com/flagship-io/flagship-ios
        type: SDK
        title: iOS SDK
      - url: https://github.com/flagship-io/flagship-python-sdk
        type: SDK
        title: Python SDK
      - url: https://github.com/flagship-io/flagship-java
        type: SDK
        title: Java SDK
      - url: https://github.com/flagship-io/flagship-go-sdk
        type: SDK
        title: Go SDK
      - url: https://github.com/flagship-io/code-samples
        type: CodeExamples
        title: Code Samples
    tags:
      - Decision
      - Experimentation
      - Feature Flags
      - Server Side
    description: 'The AB Tasty Decision API is a server-side service that evaluates a visitors context against your active experiments, personalizations, and feature flags, then returns a deterministic decision: which campaigns the user qualifies for, the selected variation, and any variables or content to render.'
  - aid: ab-tasty:ab-tasty-remote-control-api
    name: AB Tasty Remote Control API
    humanURL: https://docs.abtasty.com/server-side/remote-control-api
    properties:
      - url: https://docs.abtasty.com/server-side/remote-control-api
        type: Documentation
    tags:
      - Remote Control
      - Campaigns
      - Experimentation
    description: AB Tastys Remote Control API is a developer and QA tool that lets you programmatically drive the AB Tasty SDK from outside your app or page, so you can precisely control and observe experiments without changing production targeting. With it, you can preview or force specific campaigns and variations for a visitor, toggle or pause experiences, set visitor/context attributes, trigger goals and custom events, refresh decisions, and clear caches to reproduce clean states.
  - aid: ab-tasty:ab-tasty-public-api
    name: AB Tasty Public API
    humanURL: https://docs.abtasty.com/integrations/custom-integrations/ab-tasty-public-api
    properties:
      - url: https://docs.abtasty.com/integrations/custom-integrations/ab-tasty-public-api
        type: Documentation
    tags:
      - Campaigns
      - Integrations
      - Management
    description: The AB Tasty Public API provides programmatic access to manage campaigns, monitor and control experiments, manage account users, and integrate AB Tasty with third-party tools. It uses OAuth-style credentials (ClientID and ClientSecret) to generate access tokens for authentication.
name: AB Tasty
tags:
  - Aggregation
  - Experimentation
  - Feature Flags
  - Personalization
  - A/B Testing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.abtasty.com/
    name: Website
    type: Website
  - url: https://developers.abtasty.com/
    name: Developer Portal
    type: Portal
  - url: https://docs.abtasty.com/
    name: Documentation
    type: Documentation
  - url: https://www.abtasty.com/pricing/
    name: Pricing
    type: Pricing
  - url: https://support.abtasty.com/hc/en-us
    name: Support
    type: Support
  - url: https://www.abtasty.com/legal-notices/
    name: Legal Notices
    type: Legal
  - url: https://www.abtasty.com/privacy-policy/
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://github.com/flagship-io
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/flagship-io/abtasty-cli
    name: AB Tasty CLI
    type: CLI
  - url: https://github.com/flagship-io/mcp-server
    name: MCP Server
    type: Tools
    title: MCP Server
  - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/rules/ab-tasty-spectral-rules.yml
    name: AB Tasty Spectral Rules
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/vocabulary/ab-tasty-vocabulary.yaml
    name: AB Tasty Vocabulary
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/capabilities/feature-experimentation.yaml
    name: Feature Experimentation Capability
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/ab-tasty/refs/heads/main/json-ld/ab-tasty-decision-api-context.jsonld
    name: Decision API JSON-LD Context
    type: JSONLD
  - type: Features
    data:
      - name: A/B Testing
        description: Advanced A/B testing with conversion safety mechanisms and unlimited variations
      - name: Feature Flags
        description: Server-side feature flags with targeting and gradual rollouts
      - name: Personalization
        description: Experience customization based on emotional needs and engagement segmentation
      - name: E-Merchandising
        description: Unified search, recommendations, and product visibility control
      - name: Progressive Rollouts
        description: Progressive feature release with automatic KPI-triggered rollbacks
      - name: AI Visual Editor
        description: AI-powered prompt-based visual modifications for experiments
      - name: AdaptiveCX
        description: Real-time predictive AI for anonymous visitor personalization targeting 90% of visitors
      - name: Multivariate Testing
        description: Test multiple variables simultaneously across web and mobile
  - type: UseCases
    data:
      - name: Web Experimentation
        description: Run A/B tests and multivariate experiments on websites to optimize conversion rates
      - name: Feature Experimentation
        description: Multi-channel feature testing across devices via API or SDK implementation
      - name: Server-Side Testing
        description: Backend and edge worker experiments using the Decision API
      - name: E-commerce Optimization
        description: Merchandising, recommendations, and personalized product experiences
      - name: Progressive Deployment
        description: Gradual feature rollouts with automated rollback based on KPI monitoring
      - name: Anonymous Personalization
        description: AI-driven real-time personalization for anonymous visitors
  - type: Integrations
    data:
      - name: Google Cloud
        description: Partnership with Google Cloud for infrastructure and analytics integration
      - name: Analytics Tools
        description: Connect with analytics platforms via the integration hub for data sharing
      - name: CDPs
        description: Customer Data Platform integrations for enhanced visitor profiling
      - name: OpenFeature
        description: OpenFeature provider integration for standardized feature flag management
      - name: Vercel
        description: Edge function integration with Vercel for server-side experimentation
      - name: Cloudflare
        description: Cloudflare Worker integration for edge-based feature experimentation
      - name: AWS Lambda
        description: AWS Lambda integration for serverless feature experimentation
      - name: Fastly
        description: Fastly worker integration for CDN-level feature experimentation
      - name: Akamai
        description: Akamai worker integration for CDN-level feature experimentation
      - name: Shopify Hydrogen
        description: Shopify Hydrogen framework integration for headless commerce experimentation
created: '2025-06-05'
modified: '2026-04-19'
position: Consuming
description: At AB Tasty, we are your partner for pushing great ideas even further through optimization. We achieve this by empowering brands to build better experiences using personalization, experimentation, recommendations, merchandising, and the market's only emotions-based segmentation solution.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
