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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: 'The Nixpacks command-line interface is the primary interface for generating build plans and producing Docker images from application source. Core commands include `nixpacks plan` (emit the JSON build '
  name: Nixpacks CLI
  slug: cli
- description: The Nixpacks build plan is the JSON representation of how a source directory will be turned into a container image. A plan declares the list of providers used, top-level `variables`, `staticAssets`, `
  name: Nixpacks Build Plan
  slug: build-plan
- description: Projects can override or extend the auto-detected build plan by committing a `nixpacks.toml` (or `nixpacks.json`) file at the root of the repository. The configuration file mirrors the build-plan stru
  name: Nixpacks Configuration File (nixpacks.toml)
  slug: configuration-file
- description: Providers are the pluggable modules that detect a language or framework in the source directory and contribute their portion of the build plan. Nixpacks ships with providers for Node (npm, pnpm, Yarn,
  name: Nixpacks Language Providers
  slug: providers
- description: The official `iloveitaly/github-action-nixpacks` GitHub Action wraps the Nixpacks CLI so that CI pipelines can build and optionally push OCI images directly from a workflow without installing Nixpacks
  name: Nixpacks GitHub Action
  slug: github-action
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nixpacks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nixpacks.com
- group: docs
  title: ''
  type: Documentation
  url: https://nixpacks.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://nixpacks.com/docs/getting-started
- group: other
  title: ''
  type: Install
  url: https://nixpacks.com/docs/install
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/railwayapp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/railwayapp/nixpacks
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/railwayapp/nixpacks
- group: commercial
  title: ''
  type: License
  url: https://github.com/railwayapp/nixpacks/blob/main/LICENSE
- group: operate
  title: ''
  type: Issues
  url: https://github.com/railwayapp/nixpacks/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/railwayapp/nixpacks/releases
- group: other
  title: ''
  type: ContainerImage
  url: https://github.com/railwayapp/nixpacks/pkgs/container/nixpacks
- group: other
  title: ''
  type: Provider
  url: https://railway.app
- group: other
  title: ''
  type: Successor
  url: https://github.com/railwayapp/railpack
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Railway
created: '2026-05-24'
description: Nixpacks is an open-source build tool that converts application source code into OCI-compliant Docker images by combining language-specific providers, Nix packages, and Buildkit. Originally created by Railway as the build system powering the Railway platform, Nixpacks inspects a project's source, selects one or more providers (Node, Python, Ruby, Go, Java, Rust, PHP, Elixir, Deno, Crystal, .NET, Swift, Scala, Dart, Haskell, Gleam, Zig, Clojure, Lunatic, Cobol, Scheme, F#, Staticfile, and more), and produces a reproducible build plan composed of setup, install, build, and start phases. The plan declares Nix packages, apt packages, environment variables, commands, and cache directories, and can be customized via a `nixpacks.toml` file, CLI flags, or environment variables. Compared with Cloud Native Buildpacks, Nixpacks uses Nix as its package layer, ships as a single Rust CLI, and outputs a plain Dockerfile/OCI image without requiring a buildpack lifecycle. The project is MIT
  licensed and currently in maintenance mode; Railway recommends Railpack as the actively developed successor.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nixpacks.png
layout: provider
modified: '2026-05-24'
name: Nixpacks
nav: Providers
network: true
overview: 'Nixpacks publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Build Tool, Buildpacks, Docker, OCI, and Nix.


  Nixpacks'' developer surface includes documentation, getting-started guide, changelog, and 12 more developer resources.'
random_paper: 45
score:
  band: emerging
  composite: 13.1
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nixpacks/refs/heads/main/screenshots/nixpacks-2026-06-20T190333.png
security:
- kind: domain-security
  name: Nixpacks Domain Security
  slug: nixpacks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nixpacks
tags:
- Build Tool
- Buildpacks
- Docker
- OCI
- Nix
- Nixpkgs
- Container Image
- Application Packaging
- Railway
- Open Source
- Rust
- DevOps
- Platform Engineering
- PaaS
website: https://nixpacks.com
---
