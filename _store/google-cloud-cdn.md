---
aid: google-cloud-cdn
name: Google Cloud CDN
description: Google Cloud CDN (Content Delivery Network) uses Google's globally distributed edge points of presence to cache HTTP(S) load-balanced content close to users. It accelerates content delivery, reduces serving costs, and improves availability by leveraging Google's global network infrastructure for fast, reliable content distribution.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/google-cloud-cdn/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Caching
  - CDN
  - Content Delivery
  - Google Cloud
  - Networking
apis:
  - name: Google Cloud CDN API
    description: The Cloud CDN API enables programmatic management of CDN-enabled backend services, URL maps, cache invalidation, and edge caching policies through the Compute Engine API, providing control over content distribution and caching behavior.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/cdn/docs
    baseURL: https://compute.googleapis.com
    tags:
      - Backend Services
      - Cache Invalidation
      - Edge Caching
      - Load Balancing
      - URL Maps
    properties:
      - type: Documentation
        url: https://cloud.google.com/cdn/docs/reference/rest
      - type: OpenAPI
        url: openapi/cdn-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/cdn/docs/quickstart
      - type: JSONSchema
        url: json-schema/cdn-backendservice.json
common:
  - type: Portal
    url: https://cloud.google.com/cdn
  - type: Getting Started
    url: https://cloud.google.com/cdn/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/cdn/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/cdn/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/cdn/docs/support
  - type: JSON-LD
    url: json-ld/cdn-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
