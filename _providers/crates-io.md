---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Crates Io Agentic Access
  operation_count: 15
  slug: crates-io-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 5
apis:
- description: Registry configuration document
  name: crates.io Config API
  slug: crates-io-config-api
- description: Search and manage Rust crates
  name: crates.io Crates API
  slug: crates-io-crates-api
- description: Per-crate index metadata files served over HTTP
  name: crates.io Index API
  slug: crates-io-index-api
- description: List, add, and remove crate owners
  name: crates.io Owners API
  slug: crates-io-owners-api
- description: Yank and unyank crate versions
  name: crates.io Versions API
  slug: crates-io-versions-api
artifact_total: 35
collections:
- collection_type: open
  name: crates.io Sparse Index API
  slug: open-crates-io-sparse-index
- collection_type: open
  name: crates.io Web API
  slug: open-crates-io-web-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crates-io-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crates-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crates-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crates-io-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://crates.io
- group: docs
  title: ''
  type: Documentation
  url: https://doc.rust-lang.org/cargo/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.rust-lang.org/cargo/reference/registry-web-api.html
- group: docs
  title: ''
  type: Documentation
  url: https://doc.rust-lang.org/cargo/reference/registry-index.html
- group: docs
  title: ''
  type: Documentation
  url: https://doc.rust-lang.org/cargo/reference/registries.html
- group: docs
  title: ''
  type: Documentation
  url: https://doc.rust-lang.org/cargo/reference/registry-authentication.html
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.rust-lang.org/cargo/reference/publishing.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rust-lang/crates.io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rust-lang/crates.io-index
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rust-lang/crates.io-index-archive
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rust-lang/cargo
- group: build
  title: ''
  type: Tools
  url: https://github.com/rust-lang/crates-io-auth-action
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rust-lang/crates-io-cargo-teams
- group: build
  title: ''
  type: Tools
  url: https://github.com/rust-lang/crates-io-ops-bot
- group: build
  title: ''
  type: Tools
  url: https://github.com/rust-lang/crates_io_og_image
- group: build
  title: ''
  type: Tools
  url: https://github.com/rust-lang/crates-io-heroku-metrics
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crates.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.rust-lang.org/inside-rust/
- group: operate
  title: ''
  type: ChangeLog
  url: https://blog.rust-lang.org/2023/03/09/Rust-1.68.0.html
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/rust-lang/crates.io/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/rust-lang/crates.io/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/rust-lang/crates.io/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/rust-lang/crates.io/blob/main/LICENSE-APACHE
- group: commercial
  title: ''
  type: License
  url: https://github.com/rust-lang/crates.io/blob/main/LICENSE-MIT
- group: operate
  title: ''
  type: Support
  url: mailto:help@crates.io
- group: operate
  title: ''
  type: Forums
  url: https://rust-lang.zulipchat.com/#narrow/stream/318791-t-crates-io
- group: operate
  title: ''
  type: Forums
  url: https://github.com/rust-lang/crates.io/discussions
- group: docs
  title: ''
  type: Documentation
  url: https://crates.io/policies
- group: docs
  title: ''
  type: Documentation
  url: https://crates.io/data-access
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rs
- group: other
  title: ''
  type: Sponsor
  url: https://foundation.rust-lang.org/
- group: other
  title: ''
  type: Sponsor
  url: https://aws.amazon.com/
- group: other
  title: ''
  type: Sponsor
  url: https://www.fastly.com/
created: '2026-05-25T00:00:00.000Z'
description: crates.io is the official package registry for the Rust programming language, operated by the crates.io team under the Rust Foundation with infrastructure support from Amazon Web Services and Fastly. It exposes a Web API at /api/v1 used by Cargo and the website for search, publishing, yanking, and owner management, plus a sparse HTTP index at index.crates.io that has been Cargo's default registry protocol since Rust 1.70 (June 2023). The legacy git index is still mirrored. Every published version is checksummed with SHA-256 and companion documentation is auto-built on docs.rs. The crates.io source code is dual-licensed under Apache-2.0 and MIT and runs on Rust (axum, diesel) with a SvelteKit frontend.
examples:
- key_count: 2
  name: Crates Io Config Example
  slug: crates-io-config-example
- key_count: 2
  name: Crates Io Get Crate Example
  slug: crates-io-get-crate-example
- key_count: 2
  name: Crates Io Search Example
  slug: crates-io-search-example
- key_count: 2
  name: Crates Io Sparse Index Example
  slug: crates-io-sparse-index-example
features:
- Centralized package registry for the Rust programming language operated by the crates.io team under the Rust Foundation
- Web API at https://crates.io/api/v1 for search, crate detail, version detail, download redirect, publish, yank, unyank, and owner management
- Sparse HTTP index at https://index.crates.io (default for Cargo since Rust 1.70) — replaces the legacy git index for the vast majority of fetches
- Legacy git index at https://github.com/rust-lang/crates.io-index still mirrored for source replacement and offline scenarios
- SHA-256 checksums published per version for tamper-evident downloads
- Index format v2 with features2 map for namespaced and weak-dep features
- Per-crate keywords, categories, and reverse-dependency listings on the website
- Authentication via per-user API tokens scoped to publish, yank, and owner-management permissions
- Trusted Publishing flow via crates-io-auth-action exchanging GitHub Actions OIDC tokens for short-lived publish tokens
- Open source under Apache-2.0 and MIT — backend in Rust (axum + diesel), frontend in SvelteKit/TypeScript
- Infrastructure sponsored by Amazon Web Services (file hosting) and Fastly (CDN)
- Status page at status.crates.io reporting crates.io and docs.rs uptime
- Companion documentation host docs.rs auto-builds and serves docs for every published crate version
- No paid plans — operated as a public good of the Rust ecosystem
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crates-io.png
json_schemas:
- name: crates.io Crate
  property_count: 4
  slug: crates-io-crate
- name: crates.io Sparse Index Entry
  property_count: 10
  slug: crates-io-index-entry
json_structures:
- name: Crates Io Crate Structure
  property_count: 0
  slug: crates-io-crate-structure
jsonld:
- class_count: 0
  name: Crates Io Context
  property_count: 8
  slug: crates-io-context
layout: provider
modified: '2026-05-25'
name: crates.io
nav: Providers
network: true
overview: 'crates.io publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Config API, Crates API, Index API, and 2 more. Tagged areas include Rust, Package Registry, Crates, Cargo, and Open Source.


  The crates.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  crates.io''s developer surface includes authentication, developer portal, documentation, getting-started guide, tooling, engineering blog, changelog, and 30 more developer resources.'
random_paper: 1
rules:
- name: crates.io API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: crates-io-jsonschema-spectral-rules
- name: crates.io API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 2
    info: 1
    warn: 3
  slug: crates-io-rules
score:
  band: developing
  composite: 45.8
  delta: -3.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 68.0
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crates-io/refs/heads/main/screenshots/crates-io-2026-06-20T175213.png
security:
- kind: authentication
  name: Crates Io Authentication
  slug: crates-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crates Io Domain Security
  slug: crates-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Crates Io Vulnerability Disclosure
  slug: crates-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crates-io
tags:
- Rust
- Package Registry
- Crates
- Cargo
- Open Source
- Developer Tools
- Rust Foundation
website: https://crates.io
---
