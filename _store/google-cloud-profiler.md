---
aid: google-cloud-profiler
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-profiler/refs/heads/main/apis.yml
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
name: Google Cloud Profiler
tags:
- CPU
- Flame Graphs
- Google Cloud
- Memory
- Observability
- Performance
- Profiling
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Profiler is a statistical, low-overhead profiling service that continuously monitors CPU usage and memory allocation in production applications. It attributes resource consumption to specific source code sections, supports Go, Java, Node.js, and Python, and provides flame graph visualizations for identifying performance bottlenecks with less than 5 percent overhead.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

