---
aid: openfeature
name: OpenFeature
description: OpenFeature is a CNCF incubating open specification for feature flag management. It provides a vendor-agnostic API for evaluating feature flags, enabling developers to use a consistent interface regardless of the underlying feature flag provider. OpenFeature offers SDKs in multiple languages including Go, Java, JavaScript, Python, PHP, and .NET with a provider-based architecture.
url: https://openfeature.dev
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Feature Flags
  - Feature Management
  - Incubating
  - SDKs
  - Specification
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: openfeature:openfeature-spec
    name: OpenFeature Evaluation API
    description: The OpenFeature specification defines a standard API for feature flag evaluation across languages. It includes the Evaluation API for resolving flag values with context, the Provider API for connecting to feature flag backends, the Hook API for intercepting evaluation lifecycle events, and the Event API for reacting to flag configuration changes. Providers can be implemented for any feature flag service.
    humanURL: https://openfeature.dev/docs/reference/intro
    properties:
      - type: Documentation
        url: https://openfeature.dev/docs/reference/intro
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openfeature/refs/heads/main/openapi/openfeature-openapi.yaml
    tags:
      - Evaluation API
      - Feature Flags
      - Specification
common:
  - type: Documentation
    name: OpenFeature Documentation
    description: Official OpenFeature documentation.
    url: https://openfeature.dev/docs/
  - type: GitHubOrg
    name: OpenFeature GitHub
    description: Source code and SDKs.
    url: https://github.com/open-feature
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
