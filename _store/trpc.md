---
aid: trpc
name: tRPC
description: tRPC is a TypeScript framework for building end-to-end typesafe APIs without code generation or schemas. It leverages TypeScript's type inference to provide full static typesafety and autocompletion between client and server, with zero runtime dependencies. tRPC v11 supports queries, mutations, and subscriptions via HTTP GET/POST and WebSocket adapters for Express, Fastify, Next.js, AWS Lambda, and edge runtimes.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Composition
  - API Framework
  - BFF
  - End-to-End Type Safety
  - RPC
  - TypeScript
url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trpc:http-api
    name: tRPC HTTP Protocol
    description: The tRPC HTTP API protocol surface. tRPC servers expose procedures via HTTP GET (queries) and HTTP POST (mutations). Clients use httpBatchLink to batch concurrent calls into single requests. Input is passed via JSON-encoded query parameters (GET) or request bodies (POST). Authentication uses Bearer tokens for protected procedures.
    humanURL: https://trpc.io/docs/
    baseURL: https://your-server.example.com/api/trpc
    tags:
      - API Framework
      - HTTP
      - RPC
      - TypeScript
    properties:
      - type: Documentation
        url: https://trpc.io/docs
      - type: Getting Started
        url: https://trpc.io/docs/quickstart
      - type: GitHubRepository
        url: https://github.com/trpc/trpc
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/openapi/trpc-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/rules/trpc-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/capabilities/typesafe-api-integration.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/json-schema/trpc-procedure-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/json-schema/trpc-error-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/json-ld/trpc-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/vocabulary/trpc-vocabulary.yml
common:
  - type: Website
    url: https://trpc.io/
  - type: Documentation
    url: https://trpc.io/docs
  - type: GitHub Organization
    url: https://github.com/trpc
  - type: GitHubRepository
    url: https://github.com/trpc/trpc
  - type: NPM
    url: https://www.npmjs.com/package/@trpc/server
  - type: Discord
    url: https://trpc.io/discord
  - type: Twitter
    url: https://twitter.com/alexdotjs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
