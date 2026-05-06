---
aid: porter
name: Porter
description: A package manager for Kubernetes that uses Cloud Native Application Bundles (CNAB) to package and deploy applications along with their dependencies and configuration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - CNAB
  - DevOps
  - Kubernetes
  - Package Manager
url: https://raw.githubusercontent.com/api-evangelist/porter/refs/heads/main/apis.yml
created: '2025'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: porter:porter-bundle-api
    name: Porter Bundle API
    description: Core API for authoring, building, distributing, and installing Cloud Native Application Bundles (CNAB) using Porter. Bundles package application artifacts, client tools, configuration, and deployment logic into a single distributable installer that can be run with a single command.
    humanURL: https://porter.sh/docs/
    baseURL: https://porter.sh
    tags:
      - Cloud Native
      - CNAB
      - DevOps
      - Kubernetes
      - Package Manager
    properties:
      - type: Documentation
        url: https://porter.sh/docs/
      - type: Getting Started
        url: https://porter.sh/docs/learn/
      - type: OpenAPI
        url: openapi/porter-bundle-openapi.yml
      - type: JSONSchema
        url: json-schema/porter-manifest-schema.json
  - aid: porter:porter-mixins-api
    name: Porter Mixins API
    description: Extension interface for building and using mixins, which are the building blocks for authoring Porter bundles. Mixins provide pre-built integrations for interacting with tools and services such as Kubernetes, Helm, Terraform, and Docker Compose from within a bundle action.
    humanURL: https://porter.sh/mixins/
    baseURL: https://porter.sh
    tags:
      - CNAB
      - DevOps
      - Extensions
      - Mixins
      - Plugins
    properties:
      - type: Documentation
        url: https://porter.sh/mixins/
      - type: Reference
        url: https://porter.sh/docs/development/dev-a-mixin/
  - aid: porter:porter-plugins-api
    name: Porter Plugins API
    description: Plugin interface that allows extending Porter's core functionality, such as storing installation data, credential sets, and parameter sets in external systems like cloud storage instead of the local filesystem. Plugins reimplement Porter's default behavior to integrate with enterprise or cloud infrastructure.
    humanURL: https://porter.sh/docs/introduction/concepts-and-components/mixins-vs-plugins/
    baseURL: https://porter.sh
    tags:
      - Cloud Native
      - CNAB
      - DevOps
      - Extensions
      - Plugins
    properties:
      - type: Documentation
        url: https://porter.sh/docs/introduction/concepts-and-components/mixins-vs-plugins/
common:
  - type: Website
    url: https://porter.sh/
  - type: JSON-LD
    url: json-ld/porter-context.jsonld
  - type: JSONSchema
    url: json-schema/porter-manifest-schema.json
  - type: Documentation
    url: https://porter.sh/docs/
  - type: Getting Started
    url: https://porter.sh/docs/learn/
  - type: GitHub Organization
    url: https://github.com/getporter
  - type: GitHubRepository
    url: https://github.com/getporter/porter
  - type: Community
    url: https://porter.sh/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
