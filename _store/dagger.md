---
aid: dagger
name: Dagger
x-type: opensource
description: Dagger is an open-source programmable CI/CD engine that runs pipelines in containers using a unified, introspectable GraphQL API. Pipelines are written as code in the developer's preferred language (Go, Python, TypeScript, PHP, Java, .NET, Elixir, or Rust) using Dagger SDKs and packaged as Dagger Modules that can be published to the Daggerverse module index. The Dagger Engine exposes Container, Directory, File, Secret, and CacheVolume as first-class GraphQL types backed by a content-addressed store, enabling deterministic builds and aggressive caching. Dagger Cloud provides the hosted control plane for pipeline traces, checks, and module observability. Dagger does not expose a public REST API; clients connect to a per-session Dagger Engine GraphQL endpoint and the optional Dagger Cloud Web UI.
url: https://raw.githubusercontent.com/api-evangelist/dagger/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Open Source
position: Consumer
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Build Automation
  - BuildKit
  - CI/CD
  - Containers
  - DAG
  - Daggerverse
  - DevOps
  - GraphQL
  - Modules
  - OCI
  - Open Source
  - Pipelines
  - Programmable Pipelines
  - SDKs
apis:
  - aid: dagger:graphql
    name: Dagger Engine GraphQL API
    description: The Dagger Engine exposes a unified, introspectable GraphQL type system at a per-session endpoint. The schema includes Container, Directory, File, Secret, CacheVolume, and other first-class types and is dynamically extended at runtime by loaded Dagger Modules. All Dagger SDKs (Go, Python, TypeScript, PHP, Java, .NET, Elixir, Rust) are generated against this schema. There is no publicly-hosted REST endpoint.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.dagger.io/api/
    tags:
      - GraphQL
      - Introspection
      - Modules
      - SDK
    properties:
      - type: Documentation
        url: https://docs.dagger.io/api/
      - type: APIReference
        url: https://docs.dagger.io/reference/
      - type: APIInternals
        url: https://docs.dagger.io/api/internals/
      - type: Blog
        url: https://dagger.io/blog/graphql
      - type: Capabilities
        url: capabilities/dagger-graphql-capabilities.yml
  - aid: dagger:sdks
    name: Dagger SDKs
    description: Native SDKs for Go, Python, TypeScript, PHP, Java, .NET, Elixir, and Rust that generate strongly typed clients against the Dagger Engine's GraphQL schema, allowing pipelines to be written as regular code in the developer's preferred language.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.dagger.io/sdk/
    tags:
      - .NET
      - Elixir
      - Go
      - Java
      - PHP
      - Python
      - Rust
      - SDKs
      - TypeScript
    properties:
      - type: Documentation
        url: https://docs.dagger.io/sdk/
      - type: GitHubRepository
        url: https://github.com/dagger/dagger
  - aid: dagger:daggerverse
    name: Daggerverse Module Index
    description: Daggerverse is the free, public index of Dagger Modules. Developers search for, browse, and consume reusable Modules contributed by the Dagger community.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://daggerverse.dev/
    tags:
      - Daggerverse
      - Modules
      - Registry
    properties:
      - type: Website
        url: https://daggerverse.dev/
      - type: Quickstart
        url: https://docs.dagger.io/ci/quickstart/simplify/
  - aid: dagger:cloud
    name: Dagger Cloud
    description: Dagger Cloud is the hosted control plane providing pipeline traces, checks, module observability, and team collaboration. It integrates with the local Dagger Engine for seamless trace uploads.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dagger.io/cloud
    tags:
      - Cloud
      - Observability
      - Telemetry
      - Traces
    properties:
      - type: Website
        url: https://dagger.io/cloud
      - type: SignUp
        url: https://dagger.cloud/signup
common:
  - type: Website
    url: https://dagger.io/
  - type: Documentation
    url: https://docs.dagger.io/
  - type: GettingStarted
    url: https://docs.dagger.io/quickstart
  - type: Reference
    url: https://docs.dagger.io/reference/
  - type: GitHubOrganization
    url: https://github.com/dagger
  - type: GitHubRepository
    url: https://github.com/dagger/dagger
  - type: Daggerverse
    url: https://daggerverse.dev/
  - type: Blog
    url: https://dagger.io/blog
  - type: Pricing
    url: https://dagger.io/pricing
  - type: SignUp
    url: https://dagger.cloud/signup
  - type: Discord
    url: https://discord.gg/dagger-io
  - type: YouTube
    url: https://www.youtube.com/@dagger-io
  - type: Twitter
    url: https://twitter.com/dagger_io
  - type: License
    url: https://github.com/dagger/dagger/blob/main/LICENSE
  - type: JSON-LD
    url: json-ld/dagger-context.jsonld
  - type: Vocabulary
    url: vocabulary/dagger-vocabulary.yml
  - type: Capabilities
    url: capabilities/dagger-graphql-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
