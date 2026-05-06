---
aid: readme-metrics
name: ReadMe Metrics
description: ReadMe is an API documentation and developer hub platform that helps companies build interactive API documentation, track API usage analytics, and improve developer experience. ReadMe Metrics captures and analyzes API request logs to provide insights into how developers are using your APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Analytics
  - API Documentation
  - API Logs
  - API Metrics
  - API Usage
  - Developer Experience
  - Developer Hubs
url: https://raw.githubusercontent.com/api-evangelist/readme-metrics/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: readme-metrics:readme-api
    name: ReadMe API
    description: The ReadMe API allows you to programmatically manage your ReadMe developer hub, including API definitions, documentation pages, changelogs, custom pages, categories, and API usage metrics. It provides endpoints for managing projects, uploading API specifications, and retrieving analytics data.
    humanURL: https://docs.readme.com/main/reference/intro-to-the-readme-api
    tags:
      - API Analytics
      - API Documentation
      - API Management
      - Developer Hubs
    properties:
      - type: Documentation
        url: https://docs.readme.com/main/reference/intro-to-the-readme-api
      - type: OpenAPI
        url: https://spec.readme.com/openapi/6733983cabaf62002c7b16d9
      - type: GettingStarted
        url: https://docs.readme.com/main/docs/getting-started
      - type: Authentication
        url: https://docs.readme.com/main/reference/intro-to-the-readme-api#authentication
  - aid: readme-metrics:readme-metrics
    name: ReadMe Metrics
    description: ReadMe Metrics captures and analyzes API request and response data to provide usage analytics, error tracking, and developer activity insights. It helps API providers understand how their APIs are being consumed and identify issues in real time.
    humanURL: https://readme.com/metrics
    tags:
      - API Analytics
      - API Logs
      - API Metrics
      - API Usage
    properties:
      - type: Documentation
        url: https://docs.readme.com/main/docs/api-metrics-in-readme
      - type: GettingStarted
        url: https://docs.readme.com/main/docs/getting-started-with-metrics
common:
  - type: Website
    url: https://readme.com
  - type: Documentation
    url: https://docs.readme.com
  - type: Blog
    url: https://readme.com/blog
  - type: Pricing
    url: https://readme.com/pricing
  - type: Login
    url: https://dash.readme.com/login
  - type: Signup
    url: https://dash.readme.com/signup
  - type: Support
    url: https://docs.readme.com/main/docs/support
  - type: GitHub
    url: https://github.com/readmeio
  - type: Twitter
    url: https://twitter.com/readme
  - type: Changelog
    url: https://docs.readme.com/main/changelog
  - type: SDKs
    url: https://docs.readme.com/main/docs/metrics-sdks
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
