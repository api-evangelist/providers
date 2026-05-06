---
aid: sentry
name: Sentry
description: Sentry is a developer-first application monitoring platform that helps software teams discover, triage, and prioritize errors and performance issues in production. Sentry provides real-time error monitoring, performance tracing, session replay, profiling, and release tracking for web, mobile, and backend applications across 22+ platforms and languages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Error Monitoring
  - Debugging
  - Observability
  - Application Performance Management
  - Developer Tools
url: https://raw.githubusercontent.com/api-evangelist/sentry/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: sentry:sentry-error-monitoring-api
    name: Sentry Error Monitoring API
    description: Sentry provides error monitoring and performance tracking REST APIs for software applications. APIs enable issue management, event retrieval, release tracking, alert configuration, and project administration. All endpoints are scoped to an organization. Current API version is v0.
    humanURL: https://docs.sentry.io/api/
    baseURL: https://sentry.io/api/0
    tags:
      - Error Monitoring
      - Debugging
      - Observability
      - Application Performance Management
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/
      - type: Reference
        url: https://docs.sentry.io/api/
      - type: Authentication
        url: https://docs.sentry.io/api/auth/
      - type: RateLimits
        url: https://docs.sentry.io/api/ratelimits/
      - type: GettingStarted
        url: https://docs.sentry.io/api/guides/create-auth-token/
      - type: OpenAPI
        url: openapi/sentry-api-openapi.yml
    contact:
      - FN: Sentry Support
        url: https://sentry.io/support/
        email: support@sentry.io
  - aid: sentry:sentry-sdk-api
    name: Sentry SDK API
    description: Sentry provides official SDKs for 22+ platforms including JavaScript, Python, PHP, .NET, Java, Go, Ruby, Rust, Android, Apple, React Native, Unity, and Unreal Engine. Each SDK provides error capture, performance monitoring, session replay, and profiling capabilities.
    humanURL: https://docs.sentry.io/platforms/
    tags:
      - Error Monitoring
      - Debugging
      - Observability
      - Application Performance Management
      - SDK
    properties:
      - type: Documentation
        url: https://docs.sentry.io/platforms/
      - type: Reference
        url: https://develop.sentry.dev/sdk/overview/
  - aid: sentry:sentry-integration-platform-api
    name: Sentry Integration Platform API
    description: The Sentry Integration Platform API enables building public and internal integrations with Sentry. Supports OAuth2 with PKCE, device authorization flow for CLI/CI environments, webhook notifications, and custom alert actions for third-party applications.
    humanURL: https://docs.sentry.io/api/integration/
    tags:
      - Error Monitoring
      - Integrations
      - Webhooks
      - OAuth
    properties:
      - type: Documentation
        url: https://docs.sentry.io/api/integration/
      - type: Authentication
        url: https://docs.sentry.io/api/auth/
      - type: AsyncAPI
        url: asyncapi/sentry-webhooks-asyncapi.yml
common:
  - type: Website
    url: https://sentry.io/
  - type: Portal
    url: https://docs.sentry.io/api/
  - type: Documentation
    url: https://docs.sentry.io/api/
  - type: Authentication
    url: https://docs.sentry.io/api/auth/
  - type: RateLimits
    url: https://docs.sentry.io/api/ratelimits/
  - type: GettingStarted
    url: https://docs.sentry.io/api/guides/create-auth-token/
  - type: ChangeLog
    url: https://sentry.io/changelog/
  - type: Status
    url: https://status.sentry.io/
  - type: TermsOfService
    url: https://sentry.io/terms/
  - type: PrivacyPolicy
    url: https://sentry.io/legal/privacy/
  - type: Blog
    url: https://sentry.io/blog/
  - type: SDKs
    url: https://docs.sentry.io/platforms/
  - type: GitHubOrganization
    url: https://github.com/getsentry
  - type: DeveloperTools
    url: https://sandbox.sentry.io/
  - type: Pricing
    url: https://sentry.io/pricing/
  - type: SignUp
    url: https://sentry.io/signup/
  - type: Login
    url: https://sentry.io/auth/login/
  - type: JSONSchema
    url: json-schema/sentry-issue-schema.json
  - type: JSONLDContext
    url: json-ld/sentry-context.jsonld
  - type: JSONStructure
    url: json-structure/sentry-issue-structure.json
  - type: Vocabulary
    url: vocabulary/sentry-vocabulary.yml
  - type: SpectralRules
    url: rules/sentry-rules.yml
  - type: Capabilities
    url: capabilities/error-monitoring.yaml
  - type: Features
    data:
      - 'Developer: free with 5K errors, 5M spans, 50 replays'
      - 'Team at $26/mo annual: 50K errors, 5M spans, unlimited users'
      - 'Business at $80/mo: insights, anomaly detection, SAML/SCIM'
      - 'Enterprise: custom retention, residency, TAM'
      - Pay-as-you-go for additional volume on Team+
      - 'Web API: 40 req/sec read and write per auth token'
      - SDK ingest per-DSN with configurable spike protection
      - OAuth 2.0 (Sentry Apps) and auth tokens
      - Webhooks for issues, alerts, deployments
      - 100+ language/framework SDKs
      - Tracing with distributed context
      - Profiling for CPU and memory
      - Session Replay (web and mobile)
      - Uptime and Cron monitoring
      - Performance/Insights dashboards (Business+)
      - AI debugging agent (Team+ add-on)
    sources:
      - https://sentry.io/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
