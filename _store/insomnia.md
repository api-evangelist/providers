---
aid: insomnia
url: https://raw.githubusercontent.com/api-evangelist/insomnia/refs/heads/main/apis.yml
apis:
- aid: insomnia:insomnia
  name: Insomnia
  tags:
  - API Clients
  - API Design
  - Debugging
  - Mocking
  - Testing
  humanURL: https://insomnia.rest/
  properties:
  - url: https://docs.insomnia.rest/
    type: Documentation
  - url: https://insomnia.rest/plugins
    type: Plugins
  - url: https://docs.insomnia.rest/inso-cli/introduction/
    type: CLI
  - url: https://docs.insomnia.rest/inso-cli/cli-command-reference
    type: CLIReference
  - url: https://docs.insomnia.rest/insomnia/api-mocking/
    type: MockServer
  description: Insomnia is an open-source, cross-platform API development platform by Kong for designing, debugging, and testing HTTP, REST, GraphQL, gRPC, SOAP, WebSockets, SSE, and Socket.IO APIs. It includes an Inso CLI for CI/CD integration, cloud-hosted and self-hosted mock servers, OpenAPI spec design tools, and collaborative features with cloud sync, local vault, and Git storage options.
- aid: insomnia:mock-server-api
  name: Insomnia Mock Server API
  tags:
  - API Design
  - Mocking
  - Testing
  humanURL: https://docs.insomnia.rest/insomnia/api-mocking/
  properties:
  - url: https://docs.insomnia.rest/insomnia/api-mocking/
    type: Documentation
  - url: openapi/insomnia-mock-server-openapi.yml
    type: OpenAPI
  - url: json-schema/workspace.json
    type: JSONSchema
  - url: json-schema/request.json
    type: JSONSchema
  - url: json-schema/environment.json
    type: JSONSchema
  - url: json-ld/insomnia-context.jsonld
    type: JSONLD
  description: The Insomnia Mock Server API allows developers to create, manage, and interact with mock servers powered by Insomnia (Kong). Mock servers simulate API endpoints by returning predefined responses based on OpenAPI specifications or custom route configurations, enabling teams to develop and test against realistic API behavior before the actual implementation is complete.
name: Insomnia
tags:
- API Design
- CLI
- Clients
- Mocking
- Platform
- Testing
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Insomnia is an open-source, cross-platform API development platform by Kong for designing, debugging, and testing HTTP, REST, GraphQL, gRPC, SOAP, WebSockets, SSE, and Socket.IO APIs. It includes an Inso CLI for CI/CD integration, cloud-hosted and self-hosted mock servers, OpenAPI spec design tools, and collaborative features with cloud sync, local vault, and Git storage options.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

