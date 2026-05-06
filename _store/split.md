---
aid: split
name: Split
description: Split, now part of Harness Feature Management and Experimentation, is a feature flag and experimentation platform that enables teams to safely release features with controlled rollouts and measure their impact. Their developer platform provides REST APIs for managing feature flags, environments, segments, and workspaces, along with SDKs for evaluating feature flags across multiple languages and platforms.
url: https://raw.githubusercontent.com/api-evangelist/split/refs/heads/main/apis.yml
created: '2026-03-20'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
tags:
  - Experimentation
  - Feature Flags
  - Feature Management
  - Rollouts
  - SDKs
apis:
  - aid: split:split-admin-api
    name: Split Admin API
    description: The Split Admin API is a REST API that enables programmatic management of workspaces (projects), environments, traffic types, attributes, users, groups, API keys, and change requests within the Split platform (now Harness Feature Management and Experimentation). The API uses resource-oriented URLs, returns JSON responses, and requires Admin API keys for authentication. All endpoints are prefixed with /internal/api/v2 on the api.split.io host.
    humanURL: https://docs.split.io/reference/introduction
    tags:
      - Administration
      - Experimentation
      - Feature Flags
      - Feature Management
    properties:
      - type: Documentation
        url: https://docs.split.io/reference/introduction
      - type: OpenAPI
        url: openapi/split-admin-api-openapi.yml
      - type: JSONStructure
        url: json-structure/split-feature-flag-structure.json
  - aid: split:split-feature-flag-api
    name: Split Feature Flag API
    description: The Split Feature Flag API provides endpoints for creating, editing, and deleting feature flags (splits) and their definitions within specific environments. Developers can use this API to define treatments, configure targeting rules, set percentage-based rollouts, and manage feature flag lifecycles programmatically.
    humanURL: https://docs.split.io/reference/feature-flag-overview
    tags:
      - Feature Flags
      - Rollouts
      - Targeting
      - Treatments
    properties:
      - type: Documentation
        url: https://docs.split.io/reference/feature-flag-overview
      - type: OpenAPI
        url: openapi/split-feature-flag-api-openapi.yml
      - type: JSONStructure
        url: json-structure/split-feature-flag-definition-structure.json
  - aid: split:split-evaluator-api
    name: Split Evaluator API
    description: The Split Evaluator is an HTTP service that wraps Split SDKs to provide feature flag evaluation via a REST API. It enables applications that cannot directly embed an SDK to request treatment evaluations over HTTP, making it suitable for architectures where a centralized evaluation service is preferred.
    humanURL: https://help.split.io/hc/en-us/articles/360020037072-Split-Evaluator
    tags:
      - Evaluation
      - Feature Flags
      - Microservices
      - Treatments
    properties:
      - type: Documentation
        url: https://help.split.io/hc/en-us/articles/360020037072-Split-Evaluator
      - type: OpenAPI
        url: openapi/split-evaluator-api-openapi.yml
  - aid: split:split-javascript-sdk
    name: Split JavaScript SDK
    description: The Split JavaScript SDK provides client-side integration for feature flag evaluation in browser-based applications. It handles real-time feature flag synchronization, treatment evaluation, event tracking, and impression management.
    humanURL: https://help.split.io/hc/en-us/articles/360020448791-JavaScript-SDK
    tags:
      - Browser
      - Feature Flags
      - JavaScript
      - SDK
    properties:
      - type: Documentation
        url: https://help.split.io/hc/en-us/articles/360020448791-JavaScript-SDK
  - aid: split:split-nodejs-sdk
    name: Split Node.js SDK
    description: The Split Node.js SDK enables server-side feature flag evaluation for Node.js applications with local evaluation, automatic synchronization, event tracking, and impression logging.
    humanURL: https://help.split.io/hc/en-us/articles/360020564931-Node-js-SDK
    tags:
      - Feature Flags
      - Node.js
      - SDK
      - Server Side
    properties:
      - type: Documentation
        url: https://help.split.io/hc/en-us/articles/360020564931-Node-js-SDK
  - aid: split:split-java-sdk
    name: Split Java SDK
    description: The Split Java SDK provides server-side feature flag evaluation for Java and JVM-based applications with local treatment evaluation and streaming updates.
    humanURL: https://help.split.io/hc/en-us/articles/360020405151-Java-SDK
    tags:
      - Feature Flags
      - Java
      - SDK
      - Server Side
    properties:
      - type: Documentation
        url: https://help.split.io/hc/en-us/articles/360020405151-Java-SDK
  - aid: split:split-python-sdk
    name: Split Python SDK
    description: The Split Python SDK enables server-side feature flag evaluation for Python applications, suitable for Django, Flask, and other frameworks.
    humanURL: https://help.split.io/hc/en-us/articles/360020359652-Python-SDK
    tags:
      - Feature Flags
      - Python
      - SDK
      - Server Side
    properties:
      - type: Documentation
        url: https://help.split.io/hc/en-us/articles/360020359652-Python-SDK
  - aid: split:split-react-sdk
    name: Split React SDK
    description: The Split React SDK provides React-specific components and hooks for integrating feature flags including a SplitProvider context, useTreatments hooks, and conditional rendering components.
    humanURL: https://help.split.io/hc/en-us/articles/360038825091-React-SDK
    tags:
      - Feature Flags
      - Frontend
      - JavaScript
      - React
      - SDK
    properties:
      - type: Documentation
        url: https://help.split.io/hc/en-us/articles/360038825091-React-SDK
common:
  - type: Portal
    url: https://docs.split.io/reference/introduction
  - type: Documentation
    url: https://help.split.io/hc/en-us
  - type: Website
    url: https://www.split.io/
  - type: PrivacyPolicy
    url: https://www.harness.io/legal/privacy
  - type: TermsOfService
    url: https://www.harness.io/legal/terms-of-use
  - type: Blog
    url: https://www.split.io/blog/
  - type: Login
    url: https://app.split.io/login
  - type: JSONSchema
    url: json-schema/split-feature-flag-schema.json
  - type: JSONSchema
    url: json-schema/split-feature-flag-definition-schema.json
  - type: JSONSchema
    url: json-schema/split-segment-schema.json
  - type: JSONStructure
    url: json-structure/split-feature-flag-structure.json
  - type: JSONStructure
    url: json-structure/split-feature-flag-definition-structure.json
  - type: JSON-LD
    url: json-ld/split-context.jsonld
  - type: SpectralRules
    url: rules/split-rules.yml
  - type: Capabilities
    url: capabilities/feature-flag-management.yaml
  - type: Vocabulary
    url: vocabulary/split-vocabulary.yml
  - type: Features
    data:
      - Individual free for solo devs, up to 10 MAU
      - 'Team: per-MAU pricing (custom)'
      - 'Enterprise: Statistical Engine, Causal Impact, SCIM/SSO'
      - Now Harness Feature Management & Experimentation (FME)
      - Server-side and client-side SDKs
      - Targeting rules with attributes
      - Experimentation with frequentist and Bayesian inference
      - 'Admin API: 80 req/min/org'
      - Datafile-based SDK distribution (CDN-backed)
      - 'Events API: 100 events per request'
      - OAuth 2.0 + API keys
      - Webhooks for split changes and rollouts
      - Audit logs (Enterprise)
      - Streaming changes (server-sent events)
      - Causal Impact analysis for treatment effect
      - Integration with Datadog, NewRelic, Segment for guardrails
    sources:
      - https://www.harness.io/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
