---
aid: readme
url: https://raw.githubusercontent.com/api-evangelist/readme/refs/heads/main/apis.yml
apis:
  - aid: readme:readme-api
    name: ReadMe API
    tags:
      - Documentation
      - Developer Hub
      - Content Management
    humanURL: https://docs.readme.com/main/reference/intro-to-the-readme-api
    baseURL: https://api.readme.com/v2
    properties:
      - url: https://docs.readme.com/main/reference/intro-to-the-readme-api
        type: Documentation
      - url: https://docs.readme.com/main/reference/authentication
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/readme/refs/heads/main/openapi/readme-openapi.yml
        type: OpenAPI
    description: The ReadMe API lets you programmatically control your ReadMe developer hub. You can manage API definitions, API reference pages, guides, changelogs, custom pages, categories, branches, images, recipes, and search. Authentication uses a Bearer API key.
  - aid: readme:developer-metrics-api
    name: ReadMe Developer Metrics API
    tags:
      - Analytics
      - Metrics
      - Logging
    humanURL: https://readme.com/developer-dashboard
    baseURL: https://metrics.readme.io/v1
    properties:
      - url: https://readme.com/developer-dashboard
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/readme/refs/heads/main/openapi/readme-developer-metrics-openapi.yml
        type: OpenAPI
    description: The ReadMe Developer Metrics API provides endpoints for sending API logs and retrieving analytics data including page quality scores, page view statistics, and search analytics. It powers the Developer Dashboard where you can investigate API usage by key or email and debug requests in real time.
name: ReadMe
tags:
  - Documentation
  - Platform
  - Portals
  - Developer Hub
  - Analytics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-28'
position: Consumer
segments:
  - Documentation
description: ReadMe is a platform that helps companies create and manage their API documentation. With ReadMe, companies can easily create interactive and informative documentation that is user-friendly and visually appealing. By providing tools for developers to easily access and understand API documentation, ReadMe helps companies improve developer onboarding, increase API adoption, and drive developer satisfaction.
common:
  - url: https://readme.com
    type: Portal
  - url: https://docs.readme.com/main/docs/quickstart
    type: GettingStarted
  - url: https://docs.readme.com
    type: Documentation
  - url: https://readme.com/pricing
    type: Pricing
  - url: https://dash.readme.com/signup
    type: SignUp
  - url: https://dash.readme.com/login
    type: Login
  - url: https://readme.com/blog
    type: Blog
  - url: https://docs.readme.com/main/changelog
    type: ChangeLog
  - url: https://readme.com/about
    type: About
  - url: https://www.readmestatus.com
    type: Status
  - url: https://readme.com/tos
    type: TermsOfService
  - url: https://readme.com/privacy
    type: PrivacyPolicy
  - url: https://github.com/readmeio
    type: GitHubOrg
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
