---
aid: fly-io
url: https://raw.githubusercontent.com/api-evangelist/fly-io/refs/heads/main/apis.yml
apis:
- aid: fly-io:machines-api
  name: Fly.io Machines API
  tags:
  - Deployment
  - Edge Computing
  - Infrastructure
  - Platform
  - Virtual Machines
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.machines.dev
  humanURL: https://fly.io/docs/machines/api/
  properties:
  - url: https://fly.io/docs/machines/api/
    type: Documentation
  - url: https://fly.io/docs/machines/api/working-with-machines-api/
    type: Documentation
  - url: openapi/fly-io-machines-api-openapi.yml
    type: OpenAPI
  description: The Fly.io Machines API is a low-level REST interface for provisioning and managing Fly Machines, which are fast-booting virtual machines that run on Fly.io's global edge infrastructure. It provides endpoints for creating, starting, stopping, and destroying Machines, as well as managing Fly Apps, Fly Volumes, and TLS certificates. The API is accessible publicly at https://api.machines.dev or internally within the Fly.io private WireGuard network at http://_api.internal:4280.
- aid: fly-io:graphql-api
  name: Fly.io GraphQL API
  tags:
  - Deployment
  - GraphQL
  - Infrastructure
  - Networking
  - Platform
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fly.io/graphql
  humanURL: https://api.fly.io/graphql
  properties:
  - url: https://api.fly.io/graphql
    type: Documentation
  description: The Fly.io GraphQL API provides a programmatic interface for managing Fly.io platform resources including applications, IP address allocations, organizations, and networking configuration. The endpoint is available at https://api.fly.io/graphql and includes an interactive GraphiQL explorer with schema introspection and documentation tabs accessible directly in the browser. Authentication requires an Authorization Bearer token, which can be obtained by running `flyctl auth token`.
- aid: fly-io:extensions-api
  name: Fly.io Extensions API
  tags:
  - Extensions
  - Integration
  - Partner
  - Platform
  - Provisioning
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://fly.io/docs/reference/extensions_api/
  properties:
  - url: https://fly.io/docs/reference/extensions_api/
    type: Documentation
  - url: https://fly.io/docs/about/extensions/
    type: Documentation
  - url: openapi/fly-io-extensions-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/fly-io-extensions-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The Fly.io Extensions API is a provider-facing HTTP interface that enables third-party services to integrate with the Fly.io platform as extension providers. When a Fly.io user provisions an extension via the flyctl CLI, Fly.io forwards the provisioning request to the provider's API with details about the requesting organization, and the provider responds with environment variable configuration that is attached to the target application.
name: Fly Io
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Documentation and guides from the team at Fly.io.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

