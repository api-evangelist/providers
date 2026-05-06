---
aid: netlify
name: Netlify
description: Netlify is a cloud platform for building, deploying, and scaling modern web applications with continuous deployment, serverless functions, and edge computing capabilities.
type: Contract
image: https://www.netlify.com/v3/img/components/logomark.png
access: 3rd-Party
tags:
  - CDN
  - Cloud
  - Continuous Deployment
  - Edge Computing
  - JAMstack
  - Serverless
  - Serverless Functions
  - Static Sites
  - Web Hosting
  - Websites
url: https://raw.githubusercontent.com/api-evangelist/netlify/refs/heads/main/apis.yml
created: '2023-11-14'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: netlify:netlify-api
    name: Netlify API
    description: Netlify is a hosting service for the programmable web. It understands your documents and provides an API to handle atomic deploys of websites, manage form submissions, inject JavaScript snippets, and much more. This is a REST-style API that uses JSON for serialization and OAuth 2 for authentication.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/
    baseURL: https://api.netlify.com/api/v1/
    tags:
      - Deploys
      - DNS
      - Forms
      - Hosting
      - Serverless
      - Sites
      - Webhooks
    properties:
      - type: Documentation
        url: https://open-api.netlify.com/
      - type: OpenAPI
        url: openapi/netlify-openapi-original.yml
      - type: Getting Started
        url: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/
      - type: API Guides
        url: https://docs.netlify.com/api-and-cli-guides/overview/
      - type: OpenAPI Source
        url: https://github.com/netlify/open-api
common:
  - type: Terms of Service
    url: https://www.netlify.com/legal/terms-of-use/
  - type: Blog
    url: https://netlify.com/blog/
  - type: Change Log
    url: https://netlify.com/changelog/
  - type: Change Log RSS
    url: https://www.netlify.com/changelog/feed.xml
  - type: Forum
    url: https://answers.netlify.com/
  - type: Support
    url: https://www.netlify.com/support/
  - type: Privacy Policy
    url: https://www.netlify.com/privacy/
  - type: Sign Up
    url: https://app.netlify.com/signup
  - type: Portal
    url: https://app.netlify.com/
  - type: Status
    url: https://www.netlifystatus.com/
  - type: Pricing
    url: https://www.netlify.com/pricing/
  - type: Documentation
    url: https://docs.netlify.com/
  - type: Getting Started
    url: https://docs.netlify.com/start/get-started-guide/
  - type: Authentication
    url: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/
  - type: GitHub Organization
    url: https://github.com/netlify
  - type: GitHub Repository
    url: https://github.com/netlify/open-api
  - type: CLI Repository
    url: https://github.com/netlify/cli
  - type: CLI Documentation
    url: https://cli.netlify.com/
  - type: SDK
    url: https://developers.netlify.com/sdk/
  - type: About
    url: https://www.netlify.com/about/
  - type: Contact
    url: https://www.netlify.com/contact/
  - type: Security
    url: https://www.netlify.com/security/
  - type: GDPR Policy
    url: https://www.netlify.com/gdpr-ccpa/
  - type: X (Twitter)
    url: https://x.com/netlify
  - type: Features
    data:
      - 'Free: 300 credits/mo, unlimited deploy previews, global CDN'
      - 'Personal at $9/mo: 1,000 credits, smart secret detection'
      - 'Pro at $20/mo: 3,000 credits, 3+ concurrent builds, private repos'
      - 'Enterprise custom: unlimited credits, 99.99% SLA, SSO/SCIM'
      - REST API at api.netlify.com
      - 'Open API: 500 req/min/token rate limit'
      - 'Deploy creates: 3/min/site'
      - 'Build concurrency: 1 Free/Personal, 3 Pro'
      - Edge Functions (Deno runtime)
      - Functions (Node serverless)
      - Netlify Forms
      - Netlify Identity / Auth
      - Netlify Database (Postgres)
      - Netlify Blobs (object store)
      - Image CDN with transformations
      - Webhooks for build events
    sources:
      - https://www.netlify.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - FN: Netlify
    email: support@netlify.com
    url: https://www.netlify.com
---
