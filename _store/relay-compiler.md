---
aid: relay-compiler
name: Relay Compiler
description: Relay is Meta's open-source JavaScript framework and ahead-of-time GraphQL compiler for building data-driven React applications. The Relay Compiler scans JavaScript code for GraphQL fragments, aggregates and optimizes data requirements for entire apps, pre-computes queries at build time for efficient runtime performance, and generates TypeScript/Flow types for React components. It supports pagination, mutations, subscriptions, and deferred data streaming via GraphQL directives.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code Generation
  - GraphQL
  - React
  - Meta
  - Open Source
  - TypeScript
  - Build Tools
url: https://raw.githubusercontent.com/api-evangelist/relay-compiler/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: relay-compiler:relay-compiler
    name: Relay Compiler
    description: The Relay Compiler is Meta's ahead-of-time GraphQL compiler that generates optimized runtime artifacts and type-safe code for Relay applications. It processes GraphQL fragments in JavaScript/TypeScript source code, aggregates data requirements, optimizes queries, and generates TypeScript or Flow types. The compiler enforces GraphQL best practices including connection patterns, pagination fragments, and data masking.
    humanURL: https://relay.dev
    tags:
      - Compiler
      - GraphQL
      - Code Generation
      - Build Tool
      - TypeScript
      - Flow
    properties:
      - type: Documentation
        url: https://relay.dev/docs/
      - type: Getting Started
        url: https://relay.dev/docs/getting-started/
      - type: API Reference
        url: https://relay.dev/docs/api-reference/graphql-and-directives/
      - type: GitHub Repository
        url: https://github.com/facebook/relay
      - type: Releases
        url: https://github.com/facebook/relay/releases
  - aid: relay-compiler:relay-runtime
    name: Relay Runtime
    description: The Relay Runtime provides the client-side execution environment for Relay applications. It includes the normalized in-memory store, network layer, and React hooks including usePreloadedQuery, useFragment, usePaginationFragment, useRefetchableFragment, useMutation, and useSubscription for declarative data-fetching in React components.
    humanURL: https://relay.dev/docs/api-reference/
    tags:
      - Runtime
      - React Hooks
      - State Management
      - GraphQL Client
      - Data Fetching
    properties:
      - type: Documentation
        url: https://relay.dev/docs/api-reference/
      - type: GitHub Repository
        url: https://github.com/facebook/relay
common:
  - type: Website
    url: https://relay.dev
  - type: Documentation
    url: https://relay.dev/docs/
  - type: GitHub Organization
    url: https://github.com/facebook/relay
  - type: npm Package
    url: https://www.npmjs.com/package/relay-compiler
  - type: Blog
    url: https://relay.dev/blog/
  - type: Changelog
    url: https://github.com/facebook/relay/releases
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/relay-compiler/refs/heads/main/json-ld/relay-compiler-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/relay-compiler/refs/heads/main/vocabulary/relay-compiler-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
