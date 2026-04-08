---
aid: google-cloud-cdn
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-cdn/refs/heads/main/apis.yml
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
name: Google Cloud CDN
tags:
- Caching
- CDN
- Content Delivery
- Google Cloud
- Networking
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud CDN (Content Delivery Network) uses Google's globally distributed edge points of presence to cache HTTP(S) load-balanced content close to users. It accelerates content delivery, reduces serving costs, and improves availability by leveraging Google's global network infrastructure for fast, reliable content distribution.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

