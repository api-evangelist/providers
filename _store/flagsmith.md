---
aid: flagsmith
url: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/apis.yml
apis:
- aid: flagsmith:flags-api
  name: Flagsmith Flags API
  tags:
  - Edge
  - Feature Flags
  - Flags
  - Remote Config
  - SDKs
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://edge.api.flagsmith.com
  humanURL: https://docs.flagsmith.com/clients/rest
  properties:
  - url: https://docs.flagsmith.com/clients/rest
    type: Documentation
  - url: openapi/flagsmith-flags-api-openapi.yml
    type: OpenAPI
  description: The Flagsmith Flags API is the public-facing REST API that client-side and server-side SDKs use to retrieve feature flag values and remote configuration for environments and users. It uses a non-secret Environment Key for authentication and is designed to be fast, scalable, and publicly accessible. The Edge API endpoint at edge.api.flagsmith.com serves requests from AWS Lambda functions running in data centers near the client, providing low-latency global access to flag evaluations.
- aid: flagsmith:admin-api
  name: Flagsmith Admin API
  tags:
  - Administration
  - Environments
  - Feature Flags
  - Projects
  - Segments
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.flagsmith.com/api/v1
  humanURL: https://docs.flagsmith.com/integrating-with-flagsmith/flagsmith-api-overview/admin-api
  properties:
  - url: https://docs.flagsmith.com/integrating-with-flagsmith/flagsmith-api-overview/admin-api
    type: Documentation
  - url: openapi/flagsmith-admin-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/flagsmith-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The Flagsmith Admin API allows developers to programmatically manage all aspects of their Flagsmith projects. Anything that can be done through the Flagsmith dashboard can also be accomplished via this API, including creating, updating, and deleting projects, environments, feature flags, segments, and users. It uses a secret Organisation API Token for authentication and provides a Swagger interface at api.flagsmith.com/api/v1/docs for interactive exploration.
name: Flagsmith
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Flagsmith is an open-source feature flag and remote configuration platform that helps developers manage feature flags across web, mobile, and server-side applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

