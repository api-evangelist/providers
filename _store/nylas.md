---
aid: nylas
name: Nylas
description: Nylas connects your application to every email inbox and calendar in the world. The Nylas v3 platform provides REST APIs for email, calendar, contacts, scheduling, authentication, and administration with official SDKs for Node.js, Python, Ruby, and Kotlin/Java.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Calendar
  - Communication
  - Contacts
  - Email
  - Messaging
  - Scheduling
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/nylas/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: nylas:nylas-api
    name: Nylas API
    description: The Nylas v3 REST API provides programmatic access to email, calendar, contacts, scheduling, authentication, and administration features across every major email and calendar provider.
    humanURL: https://developer.nylas.com/
    baseURL: https://api.us.nylas.com
    tags:
      - Calendar
      - Communication
      - Contacts
      - Email
      - Messaging
      - Scheduling
    properties:
      - type: Documentation
        url: https://developer.nylas.com/docs/
      - type: APIReference
        url: https://developer.nylas.com/docs/reference/api/
      - type: GettingStarted
        url: https://developer.nylas.com/docs/v3/getting-started/
      - type: Authentication
        url: https://developer.nylas.com/docs/v3/auth/
      - type: RateLimits
        url: https://developer.nylas.com/docs/dev-guide/platform/rate-limits/
      - type: Errors
        url: https://developer.nylas.com/docs/api/errors/
      - type: Pricing
        url: https://www.nylas.com/pricing/
      - type: SignUp
        url: https://dashboard-v3.nylas.com/register
      - type: StatusPage
        url: https://status.nylas.com/
      - type: SDK
        name: Node.js SDK
        url: https://github.com/nylas/nylas-nodejs
      - type: SDK
        name: Python SDK
        url: https://github.com/nylas/nylas-python
      - type: SDK
        name: Ruby SDK
        url: https://github.com/nylas/nylas-ruby
      - type: SDK
        name: Java/Kotlin SDK
        url: https://github.com/nylas/nylas-java
common:
  - type: Website
    url: https://www.nylas.com/
  - type: Documentation
    url: https://developer.nylas.com/
  - type: Blog
    url: https://www.nylas.com/blog/
  - type: GitHubOrg
    url: https://github.com/nylas
  - type: TermsOfService
    url: https://www.nylas.com/legal/terms/
  - type: PrivacyPolicy
    url: https://www.nylas.com/legal/privacy-policy/
  - type: StatusPage
    url: https://status.nylas.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
