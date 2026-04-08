---
aid: launchdarkly
url: https://raw.githubusercontent.com/api-evangelist/launchdarkly/refs/heads/main/apis.yml
apis:
- aid: launchdarkly:rest-api
  name: LaunchDarkly REST API
  tags:
  - Environments
  - Experimentation
  - Feature Flags
  - Feature Management
  - Segments
  - Toggles
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://app.launchdarkly.com/api/v2
  humanURL: https://apidocs.launchdarkly.com/
  properties:
  - url: https://apidocs.launchdarkly.com/
    type: Documentation
  - type: OpenAPI
    url: openapi/launchdarkly-rest-api-openapi.yml
  description: The LaunchDarkly REST API provides programmatic access to the full LaunchDarkly feature management platform. Developers can create, update, and manage feature flags, targeting rules, user segments, projects, environments, and team members. The API also supports scheduled flag changes, release pipelines, experimentation, approval workflows, and webhook integrations.
- aid: launchdarkly:webhooks-api
  name: LaunchDarkly Webhooks API
  tags:
  - Events
  - Integrations
  - Notifications
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://app.launchdarkly.com/api/v2
  humanURL: https://launchdarkly.com/docs/api/webhooks
  properties:
  - url: https://launchdarkly.com/docs/api/webhooks
    type: Documentation
  - type: AsyncAPI
    url: asyncapi/launchdarkly-webhooks-asyncapi.yml
  description: The LaunchDarkly Webhooks API allows developers to build custom integrations that subscribe to activity events within LaunchDarkly. When actions occur such as flag changes, project creation, or environment modifications, LaunchDarkly sends HTTP POST payloads to configured webhook URLs. This enables use cases like updating external issue trackers, notifying support systems of feature rollouts, and triggering downstream automation workflows based on feature flag lifecycle events.
- aid: launchdarkly:relay-proxy
  name: LaunchDarkly Relay Proxy
  tags:
  - Edge
  - Infrastructure
  - Performance
  - Proxy
  - Streaming
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://launchdarkly.com/docs/sdk/relay-proxy
  properties:
  - url: https://launchdarkly.com/docs/sdk/relay-proxy
    type: Documentation
  - type: OpenAPI
    url: openapi/launchdarkly-relay-proxy-openapi.yml
  description: The LaunchDarkly Relay Proxy is a small Go application that connects to the LaunchDarkly streaming API and proxies that connection to SDK clients within an organization's network. Instead of each server making outbound connections to LaunchDarkly's streaming service, multiple servers connect to the local Relay Proxy which maintains a single connection upstream.
name: Launchdarkly
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: LaunchDarkly is a feature management platform that enables development teams to deliver and control software through feature flags, allowing them to test in production and roll out features safely.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

