---
aid: umami
name: Umami
description: Umami is an open source, privacy-first web analytics platform that provides website traffic insights without cookies or personal data collection, serving as a simple and fast alternative to Google Analytics. The Umami API provides full programmatic access to analytics data, website management, session tracking, event data, and team collaboration features for both self-hosted and cloud instances.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cookieless Tracking
  - Open Source
  - Privacy
  - Web Analytics
  - Website Analytics
url: https://raw.githubusercontent.com/api-evangelist/umami/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: umami:umami-api
    name: Umami API
    description: The Umami API provides programmatic access to website analytics data including pageviews, sessions, events, and metrics, allowing developers to collect tracking data and retrieve analytics reports. Self-hosted instances use JWT bearer tokens; Umami Cloud uses API key authentication.
    humanURL: https://umami.is
    baseURL: https://api.umami.is
    tags:
      - Open Source
      - Privacy
      - Tracking API
      - Web Analytics
    properties:
      - type: Documentation
        url: https://umami.is/docs
      - type: GettingStarted
        url: https://umami.is/docs/getting-started
      - type: APIDocumentation
        url: https://umami.is/docs/api
      - type: GitHubOrg
        url: https://github.com/umami-software/umami
      - type: OpenAPI
        url: openapi/umami-openapi.yml
      - type: JSONSchema
        url: json-schema/umami-website-schema.json
      - type: JSONSchema
        url: json-schema/umami-website-list-schema.json
      - type: JSONSchema
        url: json-schema/umami-website-request-schema.json
      - type: JSONSchema
        url: json-schema/umami-website-stats-schema.json
      - type: JSONSchema
        url: json-schema/umami-pageview-data-schema.json
      - type: JSONSchema
        url: json-schema/umami-metric-schema.json
      - type: JSONSchema
        url: json-schema/umami-active-visitors-schema.json
      - type: JSONSchema
        url: json-schema/umami-session-schema.json
      - type: JSONSchema
        url: json-schema/umami-session-list-schema.json
      - type: JSONSchema
        url: json-schema/umami-session-stats-schema.json
      - type: JSONSchema
        url: json-schema/umami-user-schema.json
      - type: JSONSchema
        url: json-schema/umami-user-request-schema.json
      - type: JSONSchema
        url: json-schema/umami-team-schema.json
      - type: JSONSchema
        url: json-schema/umami-team-list-schema.json
      - type: JSONSchema
        url: json-schema/umami-team-member-schema.json
      - type: JSONSchema
        url: json-schema/umami-team-request-schema.json
      - type: JSONSchema
        url: json-schema/umami-login-request-schema.json
      - type: JSONSchema
        url: json-schema/umami-login-response-schema.json
      - type: JSONSchema
        url: json-schema/umami-ok-response-schema.json
      - type: JSONStructure
        url: json-structure/umami-website-structure.json
      - type: JSONStructure
        url: json-structure/umami-website-list-structure.json
      - type: JSONStructure
        url: json-structure/umami-website-stats-structure.json
      - type: JSONStructure
        url: json-structure/umami-session-structure.json
      - type: JSONStructure
        url: json-structure/umami-session-list-structure.json
      - type: JSONStructure
        url: json-structure/umami-metric-structure.json
      - type: JSONStructure
        url: json-structure/umami-user-structure.json
      - type: JSONStructure
        url: json-structure/umami-team-structure.json
      - type: JSONStructure
        url: json-structure/umami-team-member-structure.json
      - type: JSONLDContext
        url: json-ld/umami-context.jsonld
      - type: Example
        url: examples/umami-website-example.json
      - type: Example
        url: examples/umami-website-stats-example.json
      - type: Example
        url: examples/umami-pageview-data-example.json
      - type: Example
        url: examples/umami-metric-example.json
      - type: Example
        url: examples/umami-session-example.json
      - type: Example
        url: examples/umami-session-stats-example.json
      - type: Example
        url: examples/umami-user-example.json
      - type: Example
        url: examples/umami-team-example.json
      - type: Example
        url: examples/umami-active-visitors-example.json
common:
  - type: Website
    url: https://umami.is
  - type: Documentation
    url: https://umami.is/docs
  - type: Blog
    url: https://umami.is/blog
  - type: Pricing
    url: https://umami.is/pricing
  - type: GitHub
    url: https://github.com/umami-software/umami
  - type: Login
    url: https://cloud.umami.is
  - type: Signup
    url: https://cloud.umami.is
  - type: SelfHosting
    url: https://umami.is/docs/install
  - type: Support
    url: https://umami.is/docs/support
  - type: SpectralRules
    url: rules/umami-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/web-analytics.yaml
    title: Web Analytics
  - type: Vocabulary
    url: vocabulary/umami-vocabulary.yaml
  - type: Features
    data:
      - name: Privacy-First Analytics
        description: Tracks website traffic without cookies or personal data, fully GDPR compliant without consent banners.
      - name: Real-Time Data
        description: Live visitor counts and real-time pageview tracking for immediate traffic insights.
      - name: Custom Events
        description: Track custom user interactions and conversions with a simple JavaScript API.
      - name: Team Collaboration
        description: Share analytics access across teams with role-based access control.
      - name: Self-Hosting Support
        description: Deploy on your own infrastructure for complete data ownership and control.
      - name: Open Source
        description: MIT-licensed open source software with active community development and full transparency.
      - name: Multi-Site Support
        description: Manage and analyze multiple websites from a single Umami instance.
      - name: API Access
        description: Full REST API for programmatic access to all analytics data and management functions.
  - type: UseCases
    data:
      - name: Website Performance Monitoring
        description: Track pageviews, unique visitors, bounce rates, and session duration for website optimization.
      - name: Privacy-Compliant Analytics
        description: Replace Google Analytics with a cookieless solution that requires no consent banners under GDPR.
      - name: Marketing Analytics
        description: Analyze traffic sources, referrers, and UTM campaign data to measure marketing effectiveness.
      - name: Custom Event Tracking
        description: Track button clicks, form submissions, and custom conversions using the Umami event API.
      - name: Developer Dashboards
        description: Build custom analytics dashboards using the REST API to display site metrics in your own apps.
      - name: Multi-Tenant Analytics
        description: Provide analytics access to multiple clients or teams with shared infrastructure and access controls.
  - type: Integrations
    data:
      - name: Next.js
        description: First-class integration with Next.js via the @umami/nextjs package for page view tracking.
      - name: WordPress
        description: Track WordPress sites by adding the Umami tracking script via plugin or manual installation.
      - name: Vercel
        description: Deploy Umami on Vercel with a one-click deployment for managed self-hosting.
      - name: Docker
        description: Run Umami in any environment using the official Docker container image.
      - name: Cloudflare
        description: Deploy tracking scripts behind Cloudflare for performance and abuse prevention.
  - type: Solutions
    data:
      - name: Umami Cloud
        description: Hosted Umami instance at cloud.umami.is with managed infrastructure and API key authentication.
      - name: Umami Self-Hosted
        description: Run your own Umami instance on any infrastructure with full data ownership and JWT authentication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
