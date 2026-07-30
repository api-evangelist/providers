---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bazel Build Agentic Access
  operation_count: 5
  slug: bazel-build-agentic-access
  summary_line: 5 operations
api_count: 6
apis:
- description: The `bazel` command line tool is the primary user-facing surface of Bazel. It exposes commands such as `build`, `test`, `run`, `query`, `cquery`, `aquery`, `mod`, `fetch`, `info`, `coverage`, and `cle
  name: Bazel Command Line Interface
  slug: bazel-cli
- description: Bazel's build rules, macros, and module extensions are written in Starlark — a deterministic Python dialect. The Starlark Build API exposes the rule(), repository_rule(), module_extension(), aspect(),
  name: Bazel Starlark Build API
  slug: bazel-starlark-api
- description: Bazel speaks the open Remote Execution API (REAPI), a gRPC protocol for content-addressable storage and distributed action execution. REAPI lets Bazel offload compile, test, and link actions to a remo
  name: Bazel Remote Execution API
  slug: bazel-remote-execution-api
- description: The Build Event Protocol (BEP) is Bazel's structured stream of build events — target configured, progress, test results, action executed, build finished — emitted during every invocation. BEP can be w
  name: Bazel Build Event Protocol
  slug: bazel-build-event-protocol
- description: Per-module metadata and version manifests
  name: Bazel Modules API
  slug: bazel-build-modules-api
- description: Registry-wide metadata
  name: Bazel Registry API
  slug: bazel-build-registry-api
artifact_total: 29
collections:
- collection_type: open
  name: Bazel Central Registry API
  slug: open-bazel-central-registry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bazel-build-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bazel-build-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://bazel.build/
- group: docs
  title: ''
  type: Documentation
  url: https://bazel.build/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://bazel.build/start
- group: docs
  title: ''
  type: APIReference
  url: https://bazel.build/reference
- group: company
  title: ''
  type: Blog
  url: https://blog.bazel.build/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bazelbuild
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/bazel
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/bazel-central-registry
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/bazelisk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/buildtools
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/bazel-gazelle
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/bazel-skylib
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bazelbuild/remote-apis
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/bazelbuild/bazel/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/bazelbuild/bazel/issues
- group: operate
  title: ''
  type: RoadMap
  url: https://bazel.build/about/roadmap
- group: other
  title: ''
  type: Governance
  url: https://bazel.build/contribute/contribution-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/bazelbuild/bazel/blob/master/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://bazel.build/about/security
- group: operate
  title: ''
  type: Forums
  url: https://slack.bazel.build/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/bazel
- group: build
  title: ''
  type: Tools
  url: https://github.com/bazelbuild/bazelisk
- group: build
  title: ''
  type: Tools
  url: https://github.com/bazelbuild/buildtools
- group: build
  title: ''
  type: Tools
  url: https://github.com/bazelbuild/bazel-gazelle
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_cc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_apple
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_kotlin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_scala
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_docker
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_oci
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_proto
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/rules_pkg
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bazelbuild/bazel-skylib
- group: build
  title: ''
  type: Plugins
  url: https://github.com/bazelbuild/intellij
- group: build
  title: ''
  type: Plugins
  url: https://github.com/bazelbuild/vscode-bazel
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/bazelbuild/examples
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bazel-build-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bazel-build-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/bazel-build-rules.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/bazelbuild/bazel/blob/master/LICENSE
created: '2026-05-25'
description: Bazel is a fast, scalable, multi-language and extensible build tool open-sourced by Google. It supports software projects of any size across Java, C++, Go, Python, Rust, Swift, Kotlin, Scala, Android, iOS, and many other languages and platforms. Bazel uses a hermetic, sandboxed execution model with content-addressable caching, parallel builds, and remote execution. The project ships the `bazel` CLI, the Starlark extension language for build rules, the MODULE.bazel external-dependency system (Bzlmod), and the Bazel Central Registry — a public HTTP index registry that hosts community-maintained Bazel modules.
examples:
- key_count: 5
  name: Bcr Rules Python Metadata Example
  slug: bcr-rules-python-metadata-example
- key_count: 6
  name: Bcr Source Archive Example
  slug: bcr-source-archive-example
features:
- description: One build tool spans Java, C++, Go, Python, Rust, Swift, Kotlin, Scala, Android, iOS, Objective-C, and dozens of community-maintained language rules.
  name: Multi-Language Support
- description: Sandboxed action execution and explicit dependency declarations make Bazel builds reproducible across machines and CI runners.
  name: Hermetic, Reproducible Builds
- description: Fine-grained action graph and Merkle-tree based caching mean only what changed gets rebuilt, even in monorepos with millions of targets.
  name: Incremental Builds
- description: Bazel speaks the open Remote Execution API (REAPI) so teams can share a Content-Addressable Store and offload actions to a remote build farm.
  name: Remote Caching and Execution
- description: MODULE.bazel + the Bazel Central Registry replace the legacy WORKSPACE system with versioned, transitive, registry-resolved modules.
  name: Bzlmod External Dependencies
- description: A deterministic Python-like DSL for writing custom rules, repository rules, module extensions, and aspects without touching Bazel internals.
  name: Starlark Extension Language
- description: Every invocation emits a structured BEP/BES stream consumable by CI dashboards, observability tools, and flake detectors.
  name: Build Event Protocol
- description: bazel query, cquery (configured), and aquery (action graph) let you inspect dependency graphs, configuration transitions, and the actual actions Bazel will run.
  name: Query Languages
- description: Platform-aware toolchain selection lets one BUILD graph target Linux, macOS, Windows, Android, iOS, and embedded targets from the same source tree.
  name: Toolchain Resolution
- description: Long-lived worker processes (javac, scalac, etc.) amortize JVM and compiler startup across many actions for faster incremental builds.
  name: Persistent Workers
- description: Default public index of Bazel modules at bcr.bazel.build with searchable UI at registry.bazel.build.
  name: Bazel Central Registry
- description: Pins the exact Bazel version per project via .bazelversion so every contributor and CI runner uses the same build tool.
  name: Bazelisk Version Launcher
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bazel-build.png
json_schemas:
- name: Bazel Registry Metadata
  property_count: 2
  slug: bcr-bazel-registry
- name: BCR Module Metadata
  property_count: 5
  slug: bcr-metadata
- name: BCR Module Source
  property_count: 1
  slug: bcr-source
jsonld:
- class_count: 33
  name: Bazel Build Context
  property_count: 2
  slug: bazel-build-context
layout: provider
modified: '2026-05-25'
name: Bazel
nav: Providers
network: true
overview: 'Bazel publishes 2 APIs on the [APIs.io](https://apis.io/) network: Modules API and Registry API. Tagged areas include Build Systems, Build Tool, Bzlmod, CI/CD, and Developer Tools.


  The Bazel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bazel''s developer surface includes developer portal, documentation, getting-started guide, API reference, engineering blog, changelog, Stack Overflow tag, and 41 more developer resources.'
random_paper: 33
rules:
- name: Bazel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bazel-build-jsonschema-spectral-rules
- name: Bazel API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: bazel-build-rules
score:
  band: developing
  composite: 49.9
  delta: -4.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 71.2
    developer_ergonomics: 52.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bazel-build/refs/heads/main/screenshots/bazel-build-2026-06-20T173055.png
security:
- kind: domain-security
  name: Bazel Build Domain Security
  slug: bazel-build-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bazel-build
tags:
- Build Systems
- Build Tool
- Bzlmod
- CI/CD
- Developer Tools
- Hermetic Builds
- Monorepo
- Open Source
- Remote Execution
- Starlark
website: https://bazel.build/
---
