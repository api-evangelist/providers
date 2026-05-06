---
aid: google-cloud-run
name: Google Cloud Run
description: Google Cloud Run is a fully managed serverless platform that enables you to run stateless containers that are invocable via HTTP requests. It abstracts away infrastructure management so you can focus on building applications.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-run/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Cloud Run
  - Containers
  - Google Cloud
  - Serverless
apis:
  - name: Google Cloud Run Admin API
    description: The Cloud Run Admin API deploys and manages user-provided container images as serverless services. It allows you to create, update, and delete services and revisions, manage traffic routing between revisions, and configure domain mappings and IAM policies.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/run/docs
    baseURL: https://run.googleapis.com
    tags:
      - Containers
      - Serverless
    properties:
      - type: Documentation
        url: https://cloud.google.com/run/docs/reference/rest
      - type: OpenAPI
        url: openapi/google-cloud-run-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/run/docs/quickstarts
      - type: JSONSchema
        url: json-schema/google-cloud-run-service-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/run
  - type: Getting Started
    url: https://cloud.google.com/run/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/run/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/run/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/run/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-run-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
