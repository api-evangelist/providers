---
aid: plausible
name: Plausible
description: Plausible is an open source, privacy-friendly web analytics platform designed as a lightweight alternative to Google Analytics. It provides essential website traffic metrics without using cookies or collecting personal data, making it compliant with GDPR, CCPA, and other privacy regulations out of the box. It can be self-hosted or used as a cloud service.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Cookie-Free
  - GDPR
  - Open Source
  - Privacy
  - Web Analytics
url: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: plausible:stats-api
    name: Plausible Stats API
    description: The Plausible Stats API provides programmatic access to website analytics data including aggregate metrics, time-series data, and breakdowns by various dimensions such as pages, sources, countries, devices, and browsers. It enables developers to retrieve visitor counts, pageviews, bounce rates, visit durations, and custom event data for building external dashboards and integrating analytics into other applications.
    humanURL: https://plausible.io/docs/stats-api
    baseURL: https://plausible.io/api/v2
    tags:
      - Analytics
      - Metrics
      - Reporting
      - Statistics
    properties:
      - type: Documentation
        url: https://plausible.io/docs/stats-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/openapi/plausible-stats-openapi.yml
  - aid: plausible:events-api
    name: Plausible Events API
    description: The Plausible Events API allows developers to send pageview and custom events to Plausible from server-side applications, mobile apps, or any environment where the standard JavaScript snippet cannot be used. It supports recording pageviews, custom events with properties, and revenue tracking data while maintaining Plausible's privacy-first approach.
    humanURL: https://plausible.io/docs/events-api
    baseURL: https://plausible.io/api
    tags:
      - Analytics
      - Events
      - Pageviews
      - Tracking
    properties:
      - type: Documentation
        url: https://plausible.io/docs/events-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/openapi/plausible-events-openapi.yml
  - aid: plausible:sites-api
    name: Plausible Sites API
    description: The Plausible Sites API enables developers to programmatically manage sites within their Plausible account. It supports creating new sites, deleting existing sites, retrieving site information, and managing shared links and goals. This API is useful for agencies and platforms that need to automate site provisioning and configuration.
    humanURL: https://plausible.io/docs/sites-api
    baseURL: https://plausible.io/api/v1/sites
    tags:
      - Analytics
      - Management
      - Provisioning
      - Sites
    properties:
      - type: Documentation
        url: https://plausible.io/docs/sites-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/openapi/plausible-sites-openapi.yml
common:
  - type: Website
    url: https://plausible.io
  - type: Documentation
    url: https://plausible.io/docs
  - type: APIDocumentation
    url: https://plausible.io/docs/stats-api
  - type: GettingStarted
    url: https://plausible.io/docs/add-website
  - type: Blog
    url: https://plausible.io/blog
  - type: Pricing
    url: https://plausible.io/pricing
  - type: GitHub
    url: https://github.com/plausible/analytics
  - type: Login
    url: https://plausible.io/login
  - type: Signup
    url: https://plausible.io/register
  - type: Support
    url: https://plausible.io/contact
  - type: SelfHosted
    url: https://plausible.io/self-hosted-web-analytics
  - type: Changelog
    url: https://github.com/plausible/analytics/releases
  - type: TermsOfService
    url: https://plausible.io/terms
  - type: PrivacyPolicy
    url: https://plausible.io/privacy
  - type: DataPolicy
    url: https://plausible.io/data-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
