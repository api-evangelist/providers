---
aid: treblle
url: https://raw.githubusercontent.com/api-evangelist/treblle/refs/heads/main/apis.yml
name: Treblle
description: Treblle helps engineering and product teams build, ship and understand their REST APIs in one single place. Empowering API producers by showing actionable data in real-time where it matters. Gain a deeper understanding of your API consumers and elevate developer experience (DX). Treblle analyzes 40+ API-specific data points for every API request across the entire API landscape.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Artificial Intelligence
  - Developer Experience
  - Documentation
  - Governance
  - Insights
  - Observability
  - Platform
  - Security
  - Testing
access: 3rd-Party
created: '2025-01-08'
modified: '2026-05-03'
position: Consuming
segments:
  - Documentation
specificationVersion: '0.19'
apis:
  - aid: treblle:treblle
    name: Treblle
    tags:
      - API Intelligence
      - Monitoring
      - Observability
      - Platform
    humanURL: https://treblle.com/
    properties:
      - url: https://treblle.com/
        type: Documentation
      - url: https://docs.treblle.com/
        type: Portal
      - url: https://identity.treblle.com/register
        type: SignUp
      - url: https://identity.treblle.com/login
        type: Login
      - url: https://github.com/treblle
        type: GitHubOrg
    description: Treblle analyzes 40 API-specific data points for every API request. All data is consolidated and easily accessible in one centralized location. The only platform you need to build, ship and understand your REST APIs.
  - aid: treblle:treblle-api
    name: Treblle Platform API
    tags:
      - Analytics
      - API Intelligence
      - Governance
      - Monitoring
    humanURL: https://docs.treblle.com/
    baseURL: https://app.treblle.com/api/v1
    properties:
      - url: https://docs.treblle.com/
        type: Documentation
      - url: openapi/treblle-api-openapi.yml
        type: OpenAPI
      - url: json-schema/treblle-project-schema.json
        type: JSONSchema
      - url: json-schema/treblle-request-schema.json
        type: JSONSchema
      - url: json-schema/treblle-governance-schema.json
        type: JSONSchema
      - url: json-ld/treblle-context.jsonld
        type: JSONLD
      - url: json-structure/treblle-project-structure.json
        type: JSONStructure
      - url: examples/treblle-list-projects-example.json
        type: Example
      - url: examples/treblle-run-governance-example.json
        type: Example
      - url: rules/treblle-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/treblle-api.yaml
        type: NaftikoCapability
    description: The Treblle Platform API provides programmatic access to API project management, request logs, analytics, governance checks, endpoint discovery, and team management. Enables CI/CD integration and automation of API observability workflows.
  - aid: treblle:api-intelligence
    name: Treblle API Intelligence
    tags:
      - API Intelligence
      - Monitoring
      - Observability
    humanURL: https://treblle.com/product/api-intelligence
    properties:
      - url: https://treblle.com/product/api-intelligence
        type: ProductPage
      - url: https://docs.treblle.com/
        type: Documentation
    description: Treblle API Intelligence is a federated platform that provides 50+ API-specific data points for every request across an entire API landscape, helping teams debug and deploy fixes 15x faster through endpoint detection, custom analytics dashboards, and powerful request filtering.
  - aid: treblle:api-documentation
    name: Treblle API Documentation
    tags:
      - Developer Experience
      - Documentation
      - OpenAPI
    humanURL: https://treblle.com/product/api-documentation
    properties:
      - url: https://treblle.com/product/api-documentation
        type: ProductPage
      - url: https://docs.treblle.com/explore-treblle/platform/api-documentation
        type: Documentation
    description: Treblle API Documentation automatically generates real-time API documentation from live API traffic and SDK instrumentation, including authentication methods, endpoints, OpenAPI specs, Swagger editor integration, and an API Catalog for easy discoverability across an organization's entire API landscape.
  - aid: treblle:api-governance
    name: Treblle API Governance
    tags:
      - Compliance
      - Governance
      - Standards
    humanURL: https://treblle.com/product/api-governance
    properties:
      - url: https://treblle.com/product/api-governance
        type: ProductPage
      - url: https://docs.treblle.com/workflow-tutorials/compliance
        type: Documentation
    description: Treblle API Governance runs 30+ automated tests on APIs to assess design, performance, and security with API scoring systems. It enables shift-left and runtime security governance through automated rule enforcement, runtime security risk assessment, and compliance control for standards like GDPR, PCI, and CCPA.
  - aid: treblle:api-analytics
    name: Treblle API Analytics
    tags:
      - Analytics
      - Dashboards
      - Metrics
    humanURL: https://treblle.com/product/api-analytics
    properties:
      - url: https://treblle.com/product/api-analytics
        type: ProductPage
    description: Treblle API Analytics provides customizable dashboards for monitoring API performance and usage, enabling teams to track request metrics, location data, device information, and response times with real-time traffic detection and adoption measurement through comparative analysis.
  - aid: treblle:api-security
    name: Treblle API Security
    tags:
      - Compliance
      - Security
      - Threat Detection
    humanURL: https://treblle.com/product/api-security
    properties:
      - url: https://treblle.com/product/api-security
        type: ProductPage
      - url: https://docs.treblle.com/workflow-tutorials/security
        type: Documentation
    description: Treblle API Security provides real-time threat detection with 15+ automated security checks on every API request, analyzing payloads for SQL injection patterns, performing IP reputation checks, detecting potential DDoS attacks, and ensuring compliance with GDPR, PCI DSS, and CCPA regulations.
  - aid: treblle:api-insights
    name: Treblle API Insights
    tags:
      - Governance
      - OpenAPI
      - Scoring
    humanURL: https://treblle.com/product/api-insights
    properties:
      - url: https://treblle.com/product/api-insights
        type: ProductPage
      - url: https://docs.treblle.com/explore-treblle/api-toolkit/api-insights
        type: Documentation
    description: Treblle API Insights is a free governance tool that evaluates OpenAPI specifications, providing scores from 1-100 and letter grades from A-F across design, security, and performance categories with 30+ automated tests. Available as a web interface, native macOS application, VS Code extension, and CLI tool for CI/CD automation.
  - aid: treblle:alfred
    name: Treblle Alfred AI
    tags:
      - Artificial Intelligence
      - Assistant
      - Developer Experience
    humanURL: https://treblle.com/product/alfred
    properties:
      - url: https://treblle.com/product/alfred
        type: ProductPage
      - url: https://docs.treblle.com/explore-treblle/workspace/alfred-ai
        type: Documentation
    description: Alfred is Treblle's AI-powered integration assistant for developer portals, enabling automated code generation across multiple programming languages, endpoint discovery, and intelligent API documentation support with natural language queries, delivering 10x faster API integrations and reducing support requests by 15x.
  - aid: treblle:aspen
    name: Treblle Aspen API Testing
    tags:
      - Developer Tools
      - macOS
      - Testing
    humanURL: https://treblle.com/product/aspen
    properties:
      - url: https://treblle.com/product/aspen
        type: ProductPage
    description: Aspen is Treblle's intelligent API testing application for macOS featuring AI-powered capabilities through Alfred AI, the ability to organize API requests through Collections, automatic code generation, and team sharing. It operates entirely locally with privacy by default and no data saved to external servers.
common:
  - name: Pricing - Treblle
    description: 'null'
    url: https://treblle.com/pricing
    type: Pricing
  - name: Getting Started with Treblle
    description: 'null'
    url: https://docs.treblle.com/guides/getting-started/
    type: Documentation
  - name: Integrations - Treblle
    description: 'null'
    url: https://docs.treblle.com/integrations/
    type: Integrations
  - name: Getting Started with Treblle
    description: 'null'
    url: https://docs.treblle.com/guides/getting-started/
    type: GettingStarted
  - name: Customers - Treblle
    description: 'null'
    url: https://treblle.com/customers
    type: Customers
  - name: Treblle Status Page
    description: 'null'
    url: https://status.treblle.com/
    type: Status
  - name: Treblle Blog
    description: 'null'
    url: https://blog.treblle.com/
    type: Blog
  - name: Data Security - Treblle
    description: 'null'
    url: https://treblle.com/security
    type: Security
  - name: Terms of Service - Treblle
    description: 'null'
    url: https://treblle.com/terms-of-service
    type: TermsOfService
  - name: Privacy Policy - Treblle
    description: 'null'
    url: https://treblle.com/privacy-policy
    type: PrivacyPolicy
  - name: About Us - Treblle
    description: 'null'
    url: https://treblle.com/about-us
    type: About
  - name: Treblle Enterprise Platform
    description: 'null'
    url: https://treblle.com/enterprise
    type: Enterprise
  - name: Treblle GitHub Organization
    description: 'null'
    url: https://github.com/treblle
    type: GitHubOrg
  - name: Treblle on LinkedIn
    description: 'null'
    url: https://www.linkedin.com/company/treblle
    type: LinkedIn
  - name: Treblle on Twitter
    description: 'null'
    url: https://twitter.com/treblleapi
    type: Twitter
  - name: Treblle Sign Up
    description: 'null'
    url: https://identity.treblle.com/register
    type: SignUp
  - name: Treblle Login
    description: 'null'
    url: https://identity.treblle.com/login
    type: Login
  - name: Treblle API Observability Capability
    url: capabilities/api-observability.yaml
    type: NaftikoCapability
  - name: Treblle Vocabulary
    url: vocabulary/treblle-vocabulary.yml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
