---
aid: plausible
url: https://raw.githubusercontent.com/api-evangelist/plausible/refs/heads/main/apis.yml
apis:
- aid: plausible:stats-api
  name: Plausible Stats API
  description: The Plausible Stats API provides programmatic access to website analytics data including aggregate metrics, time-series data, and breakdowns by various dimensions such as pages, sources, countries, devices, and browsers. It enables developers to retrieve visitor counts, pageviews, bounce rates, visit durations, and custom event data for building external dashboards and integrating analytics into other applications.
  humanURL: https://plausible.io/docs/stats-api
  tags:
  - Analytics
  - Metrics
  - Reporting
  - Statistics
  properties:
  - type: Documentation
    url: https://plausible.io/docs/stats-api
- aid: plausible:events-api
  name: Plausible Events API
  description: The Plausible Events API allows developers to send pageview and custom events to Plausible from server-side applications, mobile apps, or any environment where the standard JavaScript snippet cannot be used. It supports recording pageviews, custom events with properties, and revenue tracking data while maintaining Plausible's privacy-first approach.
  humanURL: https://plausible.io/docs/events-api
  tags:
  - Analytics
  - Events
  - Pageviews
  - Tracking
  properties:
  - type: Documentation
    url: https://plausible.io/docs/events-api
- aid: plausible:sites-api
  name: Plausible Sites API
  description: The Plausible Sites API enables developers to programmatically manage sites within their Plausible account. It supports creating new sites, deleting existing sites, retrieving site information, and managing shared links and goals. This API is useful for agencies and platforms that need to automate site provisioning and configuration.
  humanURL: https://plausible.io/docs/sites-api
  tags:
  - Analytics
  - Management
  - Provisioning
  - Sites
  properties:
  - type: Documentation
    url: https://plausible.io/docs/sites-api
name: Plausible
tags:
- Analytics
- Cookie-Free
- GDPR
- Open Source
- Privacy
- Web Analytics
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Plausible is an open source, privacy-friendly web analytics platform designed as a lightweight alternative to Google Analytics. It provides essential website traffic metrics without using cookies or collecting personal data, making it compliant with GDPR, CCPA, and other privacy regulations out of the box. It can be self-hosted or used as a cloud service.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

