---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The @yarnpkg/core programmatic JavaScript/TypeScript API that allows applications to interact with Yarn projects, workspaces, and dependency resolution. Used for building Yarn plugins and tooling inte
  name: YARN Core API
  slug: yarn-core-api
- description: The Yarn command-line interface built on @yarnpkg/cli, providing commands for package installation, workspace management, publishing, and more. Supports a plugin system for extensibility.
  name: YARN CLI
  slug: yarn-cli
artifact_total: 33
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/yarnpkg/berry/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/yarnpkg/berry/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/yarnpkg/berry/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/yarnpkg/berry/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/yarnpkg/berry/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/yarnpkg/berry/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yarn-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://yarnpkg.com/getting-started/install
- group: learn
  title: ''
  type: Tutorials
  url: https://yarnpkg.com/getting-started/usage
- group: docs
  title: ''
  type: APIReference
  url: https://yarnpkg.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yarnpkg
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yarnpkg/berry
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/yarn
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/yarnpkg/berry/blob/master/CHANGELOG.md
- group: other
  title: ''
  type: BestPractices
  url: https://yarnpkg.com/migration/guide
- group: other
  title: ''
  type: Resources
  url: https://yarnpkg.com/configuration/yarnrc
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/yarn/main/json-schema/yarn-package-schema.json
created: '2025'
description: YARN (Yet Another Resource Negotiator in the original Hadoop context; also the JavaScript package manager) refers here to the yarnpkg.com JavaScript package manager. Yarn is a fast, reliable, and secure dependency management tool for JavaScript. Originally developed by Meta as an alternative to npm, Yarn offers deterministic dependency resolution, offline caching, parallel installation, and Plug'n'Play (PnP) module resolution. The project is actively maintained under the yarnpkg/berry repository (Yarn 2+) with a modular plugin architecture. Yarn provides a programmatic JavaScript/TypeScript API via @yarnpkg/core for building tools and plugins.
features:
- description: First-class monorepo support letting projects split into sub-components managed from a single root.
  name: Workspaces
- description: Alternative installation strategy that eliminates node_modules in favor of a single resolution map for faster, stricter installs.
  name: Plug'n'Play (PnP)
- description: Modular core with 25+ default plugins and a public API for building custom workflows and integrations.
  name: Plugin Architecture
- description: Local cache of downloaded packages enabling reproducible installs without network access.
  name: Offline Caching
- description: Concurrent dependency fetching and linking for faster installs versus serial package managers.
  name: Parallel Installation
- description: Lockfile-driven dependency resolution that produces identical installs across machines and CI runs.
  name: Deterministic Resolution
- description: Stricter install mode that verifies registry metadata against the lockfile to defend against supply-chain tampering.
  name: Hardened Mode
- description: Built-in shell interpreter so package scripts behave consistently across Linux, macOS, and Windows.
  name: Cross-platform Shell
- description: Declarative rules for enforcing dependency policies and conventions across a workspace.
  name: Constraints
- description: Search and upgrade UIs that let developers explore and manage dependencies interactively.
  name: Interactive Commands
- description: TypeScript-first @yarnpkg/core surface for building plugins, tooling, and CI integrations.
  name: Programmatic API
finops:
- name: Yarn Finops
  service_category: API
  slug: yarn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yarn.png
integrations:
- description: Primary package registry for installing and publishing JavaScript packages.
  name: npm Registry
- description: Runtime that executes Yarn-managed packages and the Yarn CLI itself.
  name: Node.js
- description: Yarn ships TypeScript type definitions and is itself written primarily in TypeScript.
  name: TypeScript
- description: Node.js shim that pins and provisions the Yarn version per project.
  name: Corepack
- description: Editor SDK integration that wires Yarn PnP-managed dependencies into VS Code's TypeScript and ESLint tooling.
  name: VS Code Editor SDK
- description: Editor SDK integration for IntelliJ-family IDEs to resolve PnP dependencies in editor tooling.
  name: JetBrains Editor SDK
- description: Source repository, issue tracker, and release distribution for the yarnpkg organization.
  name: GitHub
- description: Community chat for support, contributor coordination, and announcements.
  name: Discord
json_schemas:
- name: YARN Package
  property_count: 20
  slug: yarn-package
layout: provider
modified: '2026-05-03'
name: YARN
nav: Providers
network: true
overview: 'YARN publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include JavaScript, Node.js, Package Manager, and YARN.


  The YARN catalog on APIs.io includes 1 Spectral governance ruleset.


  YARN''s developer surface includes documentation, getting-started guide, API reference, changelog, and 14 more developer resources.'
plans:
- name: Yarn Plans Pricing
  plan_count: 3
  slug: yarn-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Yarn Rate Limits
  slug: yarn-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: YARN API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: yarn-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 70.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yarn/refs/heads/main/screenshots/yarn-2026-06-20T201731.png
security:
- kind: domain-security
  name: Yarn Domain Security
  slug: yarn-domain-security
  summary_line: TLSv1.2
slug: yarn
tags:
- JavaScript
- Node.js
- Package Manager
- YARN
use_cases:
- description: Coordinate dependencies, scripts, and releases across many packages in a single repository.
  name: Monorepo Management
- description: Install, upgrade, and audit JavaScript and TypeScript dependencies for libraries and applications.
  name: Dependency Management
- description: Build and distribute plugins that extend the Yarn CLI with project-specific commands and behaviors.
  name: Plugin Development
- description: Use the lockfile, offline cache, and hardened mode to keep CI installs deterministic and tamper-resistant.
  name: Reproducible CI Builds
- description: Publish packages to npm and other registries via the npm-related CLI commands and release workflows.
  name: Package Publishing
- description: Run scripts across workspaces, share dependencies, and enforce constraints in large multi-package projects.
  name: Workspace Coordination
---
