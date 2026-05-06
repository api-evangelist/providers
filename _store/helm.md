---
aid: helm
name: Helm
description: Package manager for Kubernetes that helps you define, install, and upgrade complex Kubernetes applications using charts. Helm uses a packaging format called charts, which are collections of files that describe a related set of Kubernetes resources. A chart repository is an HTTP server that houses an index.yaml file and packaged chart archives.
url: https://helm.sh
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Charts
  - Cloud Native
  - Container Orchestration
  - DevOps
  - Kubernetes
  - Package Manager
created: '2025'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: helm:chart-repository-api
    name: Helm Chart Repository API
    description: The Helm Chart Repository API defines the HTTP endpoints used by Helm clients to discover and download charts from a repository server. This includes the index.yaml endpoint for chart discovery and chart package download endpoints. ChartMuseum extends this with a JSON-based management API for listing, uploading, and deleting charts.
    humanURL: https://helm.sh/docs/topics/chart_repository/
    properties:
      - type: OpenAPI
        url: openapi/helm-chart-repository-openapi.yml
      - type: Documentation
        url: https://helm.sh/docs/topics/chart_repository/
      - type: JSONSchema
        url: json-schema/helm-repository-index-schema.json
    tags:
      - Charts
      - Package Registry
      - Repository
  - aid: helm:chart-yaml-schema
    name: Helm Chart.yaml Schema
    description: JSON Schema defining the structure and validation rules for Chart.yaml, the metadata file required in every Helm chart. Describes chart name, version, dependencies, maintainers, and other metadata fields.
    humanURL: https://helm.sh/docs/topics/charts/#the-chartyaml-file
    properties:
      - type: JSONSchema
        url: json-schema/helm-chart-yaml-schema.json
      - type: Documentation
        url: https://helm.sh/docs/topics/charts/#the-chartyaml-file
    tags:
      - Chart Metadata
      - Schema
      - Validation
  - aid: helm:values-yaml-schema
    name: Helm Values YAML Schema
    description: JSON Schema describing common conventional patterns for values.yaml files in Helm charts. Values.yaml provides default configuration values including container image settings, service configuration, ingress rules, resource limits, and scheduling constraints.
    humanURL: https://helm.sh/docs/chart_template_guide/values_files/
    properties:
      - type: JSONSchema
        url: json-schema/helm-values-yaml-schema.json
      - type: Documentation
        url: https://helm.sh/docs/chart_template_guide/values_files/
    tags:
      - Configuration
      - Schema
      - Values
  - aid: helm:repository-index-schema
    name: Helm Repository Index Schema
    description: JSON Schema for the index.yaml file served by Helm chart repositories. The index is the primary discovery mechanism listing all available charts and versions with download URLs and integrity digests.
    humanURL: https://helm.sh/docs/topics/chart_repository/#the-index-file
    properties:
      - type: JSONSchema
        url: json-schema/helm-repository-index-schema.json
      - type: Documentation
        url: https://helm.sh/docs/topics/chart_repository/#the-index-file
    tags:
      - Discovery
      - Repository Index
      - Schema
  - aid: helm:json-ld-context
    name: Helm JSON-LD Context
    description: JSON-LD context document mapping Helm concepts to linked data vocabularies including Schema.org, Dublin Core, SPDX, FOAF, and W3C PROV. Enables semantic interoperability of Helm chart metadata.
    humanURL: https://helm.sh/docs/
    properties:
      - type: JSON-LD
        url: json-ld/helm-context.jsonld
    tags:
      - JSON-LD
      - Linked Data
      - Semantics
  - aid: helm:go-sdk
    name: Helm Go SDK
    description: The Helm Go SDK provides Go packages for programmatically performing Helm actions such as install, upgrade, list, and rollback without using the CLI. The SDK is published as helm.sh/helm/v3 and provides a stable API surface for tooling that embeds Helm functionality.
    humanURL: https://helm.sh/docs/v3/sdk/gosdk/
    tags:
      - Go
      - Kubernetes
      - Package Manager
      - SDK
    properties:
      - type: Documentation
        url: https://helm.sh/docs/v3/sdk/gosdk/
      - type: Reference
        url: https://pkg.go.dev/helm.sh/helm/v3
      - type: GitHubRepository
        url: https://github.com/helm/helm
  - aid: helm:plugins
    name: Helm Plugins
    description: The Helm Plugins API defines the interface for extending the Helm CLI with additional subcommands. Plugins live in a single directory with a plugin.yaml descriptor and can be implemented as shell scripts, binaries, or WebAssembly modules introduced in Helm 4.
    humanURL: https://helm.sh/docs/topics/plugins/
    tags:
      - CLI
      - Extensions
      - Kubernetes
      - Plugins
    properties:
      - type: Documentation
        url: https://helm.sh/docs/topics/plugins/
      - type: Reference
        url: https://helm.sh/docs/plugins/developer/
      - type: JSONSchema
        url: json-schema/helm-plugin-schema.json
  - aid: helm:chart-template-api
    name: Helm Chart Template API
    description: The Helm Chart Template API defines the Go template language extensions, built-in objects, and Sprig function library available for authoring Helm chart templates. Templates render Kubernetes manifests from parameterized values and support flow control, named templates, and over 60 template functions.
    humanURL: https://helm.sh/docs/chart_template_guide/
    tags:
      - Charts
      - Go Templates
      - Kubernetes
      - Templates
    properties:
      - type: Documentation
        url: https://helm.sh/docs/chart_template_guide/
      - type: Reference
        url: https://helm.sh/docs/chart_template_guide/function_list/
common:
  - type: JSON-LD
    url: json-ld/helm-context.jsonld
  - type: JSONSchema
    url: json-schema/helm-plugin-schema.json
  - type: Website
    name: Helm Website
    description: Official Helm website.
    url: https://helm.sh/
  - type: Documentation
    name: Helm Documentation
    description: Official Helm documentation covering installation, chart development, and best practices.
    url: https://helm.sh/docs/
  - type: Getting Started
    name: Helm Quickstart Guide
    description: Step-by-step guide to installing Helm and deploying your first chart.
    url: https://helm.sh/docs/intro/quickstart/
  - type: GitHub Organization
    name: Helm GitHub Organization
    description: Source code repositories for Helm and related projects.
    url: https://github.com/helm
  - type: GitHubRepository
    name: Helm GitHub Repository
    description: Main Helm source code repository.
    url: https://github.com/helm/helm
  - type: Blog
    name: Helm Blog
    description: Official blog with announcements, releases, and community updates.
    url: https://helm.sh/blog/
  - type: Change Log
    name: Helm Changelog
    description: Full changelog and release history for Helm.
    url: https://helm.sh/docs/changelog/
  - type: Community
    name: Helm Community
    description: Community resources including developer calls and contribution guides.
    url: https://helm.sh/community/
  - type: Slack
    name: Helm Slack
    description: Kubernetes Slack workspace with Helm channels for community support.
    url: https://kubernetes.slack.com/messages/helm-users
  - type: Security
    name: Helm Security Policy
    description: Security process and policy for reporting vulnerabilities in Helm.
    url: https://helm.sh/community/SECURITY
  - type: ArtifactHub
    name: Artifact Hub
    description: Public chart repository search engine for discovering Helm charts.
    url: https://artifacthub.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
