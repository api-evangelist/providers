---
aid: lunar-dev
url: https://raw.githubusercontent.com/api-evangelist/lunar-dev/refs/heads/main/apis.yml
apis:
  - aid: lunar-dev:gateway-admin
    name: Lunar.dev Gateway Admin API
    tags:
      - AI Gateway
      - Consumption Gateway
      - Control
      - Discovery
      - Flows
      - Health
      - Integrations
      - MCP Gateway
      - Performance
      - Platform
      - Policies
      - Visibility
    humanURL: https://docs.lunar.dev/
    properties:
      - url: https://docs.lunar.dev/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/lunar-dev/refs/heads/main/openapi/lunar-dev-gateway-admin-openapi.yml
        type: OpenAPI
      - url: json-schema/health-status.json
        type: JSONSchema
      - url: json-schema/discovered-endpoint.json
        type: JSONSchema
      - url: json-schema/policy.json
        type: JSONSchema
      - url: json-schema/flow.json
        type: JSONSchema
      - url: json-schema/validation-result.json
        type: JSONSchema
      - url: json-ld/lunar-dev-context.jsonld
        type: JSONLD
    description: The Lunar.dev Gateway Admin API provides administrative endpoints for managing and monitoring the Lunar API Consumption Gateway. It enables health monitoring, endpoint discovery, flow validation, and policy management for the running gateway instance.
  - aid: lunar-dev:gateway-proxy
    name: Lunar.dev Gateway Proxy API
    tags:
      - AI Gateway
      - Consumption Gateway
      - Egress
      - Integrations
      - MCP Gateway
      - Platform
      - Proxy
      - Quota Management
      - Rate Limiting
      - Traffic Management
    humanURL: https://docs.lunar.dev/
    properties:
      - url: https://docs.lunar.dev/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/lunar-dev/refs/heads/main/openapi/lunar-dev-gateway-proxy-openapi.yml
        type: OpenAPI
    description: The Lunar.dev Gateway Proxy API handles routing of outbound egress API traffic through the Lunar Gateway. Client applications send third-party API requests through this proxy, which provides traffic management, policy enforcement, caching, rate limiting, quota management, and real-time observability.
name: Lunar.dev
tags:
  - AI Gateway
  - Automation
  - Consumption Gateway
  - Control
  - Deployment
  - Integrations
  - MCP Gateway
  - Performance
  - Platform
  - Version Control
  - Visibility
  - Workflows
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.youtube.com/channel/UCgWge-0djZcm-JWU82FbR7A
    name: Youtube
    type: Youtube
  - url: https://github.com/TheLunarCompany
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.lunar.dev/
    name: Lunar | Ground Control for 3rd Party APIs
    type: Website
    description: 'null'
  - url: https://www.lunar.dev/lunar-blog
    name: API Management Blog | Lunar
    type: Blog
    description: 'null'
  - url: https://www.lunar.dev/guides-resources
    name: 'API Consumption Management: Resources & Guides | Lunar.dev'
    type: Guide
    description: 'null'
  - url: https://www.lunar.dev/faqs
    name: Lunar | Frequently asked questions
    type: FAQ
    description: 'null'
  - url: https://www.lunar.dev/case-study
    name: Lunar Case Studies
    type: Customers
    description: 'null'
  - url: https://www.lunar.dev/case-study
    name: Lunar Case Studies
    type: Customers
    description: 'null'
  - url: https://www.lunar.dev/use-cases
    name: Use cases
    type: UseCases
    description: 'null'
  - url: https://docs.lunar.dev/
    name: Home | Lunar Docs
    type: Documentation
    description: 'null'
  - url: https://docs.lunar.dev/quick-start-guide/
    name: Quick Start Guide | Lunar Docs
    type: GettingStarted
    description: 'null'
  - url: https://docs.lunar.dev/quotas/quotas-overview
    name: Quotas Overview | Lunar Docs
    type: Quotas
    description: 'null'
  - url: https://docs.lunar.dev/additional-resources/faqs/faqIndex
    name: FAQs | Lunar Docs
    type: FAQ
    description: 'null'
  - url: https://www.lunar.dev/about-us
    name: About Us | Lunar
    type: About
    description: 'null'
  - url: https://login.lunar.dev/u/login?state=hKFo2SBYaVVrZmZpMHhLN3M3RFlmV0s1WUZCYzZjb2Nwa2FNWaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEtDRC1iM2d3Z1ltMTNSYmpKZEloOHFHUFp3aG5FMk9vo2NpZNkgQTZBOVRoUnJ6anp2eEx6cFUwRm5JZE1Id0xUUmdnSFE
    name: Sign in | Lunar.dev
    type: Login
    description: 'null'
  - url: https://login.lunar.dev/u/login?state=hKFo2SBkZkoxMlV1VVFQQmZ3ejlTQjU2QWdteFBEbG1tSWNERaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFVCVnEySHI0MHlSLTdmRU0ydzBGeTd6aFlxLTFYUlhMo2NpZNkgQTZBOVRoUnJ6anp2eEx6cFUwRm5JZE1Id0xUUmdnSFE
    name: Sign in | Lunar.dev
    type: SignUp
    description: 'null'
  - url: https://www.lunar.dev/privacy-policy
    name: Lunar | Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.lunar.dev/terms-of-use
    name: Lunar | Terms of Use
    type: TermsOfService
    description: 'null'
  - url: https://www.lunar.dev/lunar-blog
    name: API Management Blog | Lunar
    type: Blog
    description: 'null'
  - url: https://www.lunar.dev/demo
    name: See lunar.dev in action
    type: Support
    description: 'null'
  - url: https://www.lunar.dev/pricing
    name: Lunar | Pricing
    type: Pricing
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: Additional Features
      - name: Advanced Traffic Controls
      - name: Broad Sdk Support
      - name: Centralized Consumption
      - name: Configurable Policies
      - name: Consumer Tags
      - name: Egress API Proxy
      - name: Fail-Safe Mechanisms
      - name: Generic Approach
      - name: Inventory of APIs
      - name: Insights
      - name: Lunar Proxy
      - name: Lunar Interceptor
      - name: No Code Changes
      - name: Plugin System
      - name: Prioritized API Queuing
      - name: Production-Grade Ready
      - name: Quota Management
      - name: Real-Time Insights
      - name: Real-Time Controls
      - name: Real-Time Monitoring
      - name: Visibility
  - name: Use Cases
    type: UseCases
    data:
      - name: AI-Aware API Consumption
      - name: API Consumption Management
      - name: Consolidating Mcp Servers
      - name: Cost Optimization
      - name: Egress API Proxy
      - name: Managing Api-Driven Tasks
      - name: Policy Enforcement
      - name: Visibility and Alerts
created: '2025-01-08'
modified: '2026-04-28'
position: Consumer
description: Lunar.dev is an enterprise-grade gateway platform for AI governance and third-party API consumption control. It unifies an MCP Gateway, AI Gateway, and API Consumption Gateway into a single control point that gives organizations observability, access control, policy enforcement, quota management, rate limiting, and real-time monitoring over how applications and AI agents authenticate, discover tools, and consume third-party APIs.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
