---
aid: unleash
name: Unleash
description: Unleash is the open-source feature management platform enabling progressive delivery, A/B testing, and canary releases through feature flags (feature toggles). Teams use Unleash to decouple code deployments from feature releases, control rollouts by user segment, run experiments with variants, and maintain kill switches for rapid incident response. Available as open-source (self-hosted) and as Unleash Cloud (managed).
url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
tags:
  - Feature Flags
  - Feature Management
  - Progressive Delivery
  - A/B Testing
  - Open Source
  - Developer Tools
apis:
  - aid: unleash:admin-api
    name: Unleash Admin API
    description: 'Comprehensive REST API providing full programmatic control over Unleash resources including feature flags, projects, environments, users, API tokens, strategies, segments, integrations (addons), events, change requests, and instance administration. Powers the Unleash Admin UI and enables CI/CD and GitOps automation workflows. Base URL: https://{your-unleash-instance}/api/admin'
    humanURL: https://docs.getunleash.io/api
    baseURL: https://app.unleash-instance.example.com
    tags:
      - Admin
      - Feature Flags
      - Projects
      - Environments
      - Users
      - Events
    properties:
      - type: Documentation
        url: https://docs.getunleash.io/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/openapi/unleash-admin-api-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/rules/unleash-rules.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/capabilities/feature-flag-management.yaml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/capabilities/access-management.yaml
  - aid: unleash:client-api
    name: Unleash Client API
    description: API endpoint consumed by backend Unleash SDKs to fetch complete feature flag configurations including all activation strategies. Supports server-side flag evaluation with zero additional latency after initial bootstrap. Requires a backend API token scoped to a project and environment.
    humanURL: https://docs.getunleash.io/api#client-api
    baseURL: https://app.unleash-instance.example.com
    tags:
      - Client
      - SDK
      - Feature Flags
    properties:
      - type: Documentation
        url: https://docs.getunleash.io/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/openapi/unleash-client-api-openapi.yml
  - aid: unleash:frontend-api
    name: Unleash Frontend API
    description: API endpoint consumed by frontend/client-side SDKs. Returns only the evaluated state (enabled/disabled) of feature flags for a given Unleash Context, without exposing strategy configuration. Safe for use in browser and mobile apps.
    humanURL: https://docs.getunleash.io/api#frontend-api
    baseURL: https://app.unleash-instance.example.com
    tags:
      - Frontend
      - SDK
      - Feature Flags
    properties:
      - type: Documentation
        url: https://docs.getunleash.io/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/openapi/unleash-frontend-api-openapi.yml
common:
  - type: Website
    url: https://www.getunleash.io
  - type: Documentation
    url: https://docs.getunleash.io
  - type: GitHub
    url: https://github.com/Unleash/unleash
  - type: Pricing
    url: https://www.getunleash.io/pricing
  - type: Blog
    url: https://www.getunleash.io/blog
  - type: Changelog
    url: https://github.com/Unleash/unleash/releases
  - type: SDK
    url: https://docs.getunleash.io/reference/sdks
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/vocabulary/unleash-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/json-ld/unleash-context.jsonld
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/unleash/refs/heads/main/json-schema/unleash-feature-flag-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
