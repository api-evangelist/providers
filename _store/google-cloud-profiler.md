---
aid: google-cloud-profiler
name: Google Cloud Profiler
description: Google Cloud Profiler is a statistical, low-overhead profiling service that continuously monitors CPU usage and memory allocation in production applications. It attributes resource consumption to specific source code sections, supports Go, Java, Node.js, and Python, and provides flame graph visualizations for identifying performance bottlenecks with less than 5 percent overhead.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-profiler/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - CPU
  - Flame Graphs
  - Google Cloud
  - Memory
  - Observability
  - Performance
  - Profiling
apis:
  - name: Google Cloud Profiler API
    description: The Cloud Profiler API enables creating, listing, and managing profiling profiles for applications. It supports creating profiles for CPU, heap, wall time, contention, and thread profiling types, and provides access to collected profiling data for performance analysis.
    humanURL: https://cloud.google.com/profiler/docs
    baseURL: https://cloudprofiler.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/profiler/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/profiler/docs/about-profiler
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLDContext
        url: json-ld/json-ld.yml
common:
  - type: Portal
    url: https://cloud.google.com/profiler
  - type: Getting Started
    url: https://cloud.google.com/profiler/docs/about-profiler
  - type: Documentation
    url: https://cloud.google.com/profiler/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/profiler/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/profiler/docs/support
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
