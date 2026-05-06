---
aid: google-cloud-app-engine
name: Google Cloud App Engine
description: Google Cloud App Engine is a fully managed, serverless platform for developing and hosting web applications at scale. It supports popular programming languages and provides built-in services and APIs such as NoSQL datastores, memcache, and a user authentication API, allowing developers to focus on writing code without managing the underlying infrastructure.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/google-cloud-app-engine/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - App Engine
  - Compute
  - Google Cloud
  - PaaS
  - Serverless
  - Web Applications
apis:
  - name: Google Cloud App Engine Admin API
    description: The App Engine Admin API enables developers to provision and manage their App Engine applications programmatically, including deploying new versions, managing traffic splitting, configuring services, and monitoring application health.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/appengine/docs/admin-api
    baseURL: https://appengine.googleapis.com
    tags:
      - Applications
      - Deployments
      - Instances
      - Versions
    properties:
      - type: Documentation
        url: https://cloud.google.com/appengine/docs/admin-api/reference/rest
      - type: OpenAPI
        url: openapi/appengine-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/appengine/docs/admin-api/access-control
      - type: Getting Started
        url: https://cloud.google.com/appengine/docs/getting-started
      - type: JSONSchema
        url: json-schema/appengine-application.json
common:
  - type: Portal
    url: https://cloud.google.com/appengine
  - type: Getting Started
    url: https://cloud.google.com/appengine/docs/getting-started
  - type: Documentation
    url: https://cloud.google.com/appengine/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/appengine/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/appengine/docs/support
  - type: JSON-LD
    url: json-ld/appengine-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
