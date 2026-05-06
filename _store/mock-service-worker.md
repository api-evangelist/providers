---
aid: mock-service-worker
name: Mock Service Worker
description: Mock Service Worker (MSW) is an industry-standard, open-source API mocking library for the browser and Node.js. MSW intercepts outgoing requests at the network level using Service Workers in browsers and a request interception algorithm in Node.js, allowing developers to write client-agnostic mocks for HTTP, GraphQL, WebSocket, and Server-Sent Events and reuse them across any framework, tool, or environment for development, testing, and debugging.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mock-service-worker/refs/heads/main/apis.yml
tags:
  - API Mocking
  - GraphQL
  - HTTP
  - Mock Server
  - Mocking
  - Service Worker
  - Testing
  - WebSocket
access: 3rd-Party
position: Consumer
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: mock-service-worker:msw
    name: Mock Service Worker
    description: Mock Service Worker (MSW) is an open-source library for mocking REST, GraphQL, WebSocket, and Server-Sent Events APIs at the network level. It provides setupWorker for browser environments and setupServer for Node.js, with handlers (http, graphql, ws, sse) that allow developers to declare mocked responses without modifying application code.
    image: https://mswjs.io/static/logos/msw-logo.svg
    humanURL: https://mswjs.io/
    baseURL: https://mswjs.io/
    tags:
      - API Mocking
      - GraphQL
      - HTTP
      - Mocking
      - Service Worker
      - Testing
      - WebSocket
    properties:
      - type: Documentation
        url: https://mswjs.io/docs/
      - type: GettingStarted
        url: https://mswjs.io/docs/quick-start
      - type: HTTP Handler
        url: https://mswjs.io/docs/network-behavior/rest
      - type: GraphQL Handler
        url: https://mswjs.io/docs/network-behavior/graphql
      - type: WebSocket Handler
        url: https://mswjs.io/docs/network-behavior/websocket
      - type: GitHub
        url: https://github.com/mswjs/msw
      - type: Examples
        url: https://github.com/mswjs/examples
      - type: NPM
        url: https://www.npmjs.com/package/msw
      - type: License
        url: https://github.com/mswjs/msw/blob/main/LICENSE.md
    contact:
      - FN: MSW Maintainers
        url: https://github.com/mswjs/msw
common:
  - type: Website
    url: https://mswjs.io/
  - type: Documentation
    url: https://mswjs.io/docs/
  - type: GettingStarted
    url: https://mswjs.io/docs/quick-start
  - type: GitHub
    url: https://github.com/mswjs/msw
  - type: Examples
    url: https://github.com/mswjs/examples
  - type: NPM
    url: https://www.npmjs.com/package/msw
  - type: Discord
    url: https://kettanaito.com/discord
  - type: Sponsor
    url: https://github.com/sponsors/mswjs
  - type: OpenCollective
    url: https://opencollective.com/mswjs
  - type: License
    url: https://github.com/mswjs/msw/blob/main/LICENSE.md
  - type: JSON-LD
    url: json-ld/mock-service-worker-context.jsonld
  - type: JSONSchema
    url: json-schema/mock-service-worker-handler-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
