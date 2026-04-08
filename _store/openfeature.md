---
aid: openfeature
url: https://raw.githubusercontent.com/api-evangelist/openfeature/refs/heads/main/apis.yml
apis:
- aid: openfeature:openfeature-spec
  name: OpenFeature Evaluation API
  description: The OpenFeature specification defines a standard API for feature flag evaluation across languages. It includes the Evaluation API for resolving flag values with context, the Provider API for connecting to feature flag backends, the Hook API for intercepting evaluation lifecycle events, and the Event API for reacting to flag configuration changes. Providers can be implemented for any feature flag service.
  humanURL: https://openfeature.dev/docs/reference/intro
  properties:
  - type: Documentation
    url: https://openfeature.dev/docs/reference/intro
  tags:
  - Evaluation API
  - Feature Flags
  - Specification
name: OpenFeature
tags:
- Cloud Native
- Feature Flags
- Feature Management
- Incubating
- SDKs
- Specification
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: OpenFeature is a CNCF incubating open specification for feature flag management. It provides a vendor-agnostic API for evaluating feature flags, enabling developers to use a consistent interface regardless of the underlying feature flag provider. OpenFeature offers SDKs in multiple languages including Go, Java, JavaScript, Python, PHP, and .NET with a provider-based architecture.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

