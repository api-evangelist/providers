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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 10
apis:
- description: 'The Yarn command-line interface — `yarn` — provides install, add, remove, up, run, exec, dlx, info, why, pack, rebuild, dedupe, node, bin, search, upgrade-interactive, and stage commands for managing '
  name: Yarn CLI
  slug: yarn-cli
- description: Yarn was the first package manager built specifically around workspaces. `yarn workspace`, `yarn workspaces foreach`, `yarn workspaces focus`, and `yarn workspaces list` provide first-class monorepo c
  name: Yarn Workspaces
  slug: yarn-workspaces
- description: Plug'n'Play (PnP) is Yarn's alternative to the traditional node_modules folder. Yarn generates a single `.pnp.cjs` file containing the exact dependency tree which Node.js consults at runtime via a req
  name: Yarn Plug'n'Play
  slug: yarn-plug-n-play
- description: Zero-Installs commit Yarn's package cache (`.yarn/cache`) into the repository alongside the `.pnp.cjs` file. Clones of the repository can start working immediately without running `yarn install`, enab
  name: Yarn Zero-Installs
  slug: yarn-zero-installs
- description: Yarn Constraints let you declare cross-workspace rules — required fields in `package.json`, forbidden dependencies, version pinning, and consistency requirements — using a JavaScript or Prolog DSL. `y
  name: Yarn Constraints
  slug: yarn-constraints
- description: Yarn supports a rich set of dependency protocols beyond `npm:` semver — `git:`, `github:`, `file:`, `link:`, `portal:`, `patch:`, `exec:`, `workspace:`, and `http(s):`. Protocols are pluggable so cust
  name: Yarn Protocols
  slug: yarn-protocols
- description: Yarn ships with a full plugin API exposed by `@yarnpkg/core`. Plugins can register commands, resolvers, fetchers, linkers, and lifecycle hooks. Plugins are installed with `yarn plugin import` and list
  name: Yarn Plugin API
  slug: yarn-plugin-api
- description: Yarn provides a release-workflow primitive for monorepos. Contributors declare per-workspace version bumps as deferred decisions (`yarn version check --interactive`) and the project applies them all a
  name: Yarn Version (Release Workflow)
  slug: yarn-version
- description: First-class dependency patching — `yarn patch <package>` extracts a temporary editable copy of a dependency and `yarn patch-commit` saves the resulting diff as a `patch:` protocol entry in the lockfil
  name: Yarn Patch
  slug: yarn-patch
- description: The yarn dlx command runs a package in an isolated temporary environment without permanently installing it. Yarn's equivalent of npx, used for one-shot tools, code generators, and bootstrap scripts. A
  name: Yarn DLX
  slug: yarn-dlx
artifact_total: 35
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yarn-pkg-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://yarnpkg.com
- group: start
  title: ''
  type: GettingStarted
  url: https://yarnpkg.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/getting-started/install
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/cli
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/migration/guide
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/workspaces
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/pnp
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/zero-installs
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/constraints
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/protocols
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/plugins
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/features/editor-sdks
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/configuration/yarnrc
- group: docs
  title: ''
  type: Documentation
  url: https://yarnpkg.com/configuration/manifest
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/yarnpkg/berry
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yarnpkg/berry
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yarnpkg
- group: commercial
  title: ''
  type: License
  url: https://github.com/yarnpkg/berry/blob/master/LICENSE.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/yarnpkg/berry/blob/master/GOVERNANCE.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/yarnpkg/berry/blob/master/CONTRIBUTING.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/yarnpkg/berry/blob/master/CODE_OF_CONDUCT.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/yarnpkg/berry/releases
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/yarnpkg/rfcs
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/yarnpkg
- group: other
  title: ''
  type: Funding
  url: https://opencollective.com/yarnpkg
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/yarnpkg/setup-action
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/yarn
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@yarnpkg/core
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@yarnpkg/cli
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@yarnpkg/pnp
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@yarnpkg/fslib
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@yarnpkg/shell
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@yarnpkg/sdks
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/yarnpkg/berry/tree/master/packages
created: '2026-05-25T00:00:00.000Z'
description: Yarn is an open-source JavaScript package manager and project manager originally created at Facebook in 2016 and now developed as a fully independent community project (Yarn Berry, currently v4) on github.com/yarnpkg/berry. Yarn was the first package manager designed around workspaces and introduced Plug'n'Play (a node_modules-free module resolution strategy), Zero-Installs (committable caches for instant clones), Constraints (a cross-workspace policy DSL), and a rich protocol system covering npm, git, github, file, link, portal, patch, exec, and workspace dependencies. It is distributed via Corepack and licensed under BSD-2-Clause.
features:
- Yarn 4 (Berry) — TypeScript rewrite of the Yarn package manager, fully independent open-source project
- Workspaces — first-class monorepo support with `yarn workspace`, `yarn workspaces foreach`, and `yarn workspaces focus`
- Plug'n'Play (PnP) — node_modules-free dependency resolution via a single `.pnp.cjs` manifest plus a Rust implementation (pnp-rs)
- Zero-Installs — commit the cache so clones bootstrap with no `yarn install` step
- Constraints — JavaScript and Prolog DSL for cross-workspace policy enforcement
- Protocols — npm, git, github, file, link, portal, patch, exec, workspace, and http(s) dependency sources
- Plugin system — extensible commands, resolvers, fetchers, and linkers via `@yarnpkg/core`
- 20+ bundled plugins including plugin-npm, plugin-pnp, plugin-workspace-tools, plugin-constraints, plugin-typescript, and plugin-interactive-tools
- First-class dependency patching with yarn patch and yarn patch-commit, no extra tooling required
- Yarn dlx — safe ephemeral package execution as a drop-in replacement for npx
- Yarn up — project-wide dependency upgrades across all workspaces
- Yarn dedupe — collapse overlapping semver ranges into the fewest possible resolutions
- Yarn version — release workflow with deferred per-workspace version decisions
- Yarn npm publish and yarn npm login for npm registry publishing
- Yarn npm audit for vulnerability scanning
- Corepack integration — projects pin their Yarn version via the packageManager field in package.json
- Yarn set version stable upgrades the per-project Yarn binary
- Configuration via .yarnrc.yml with checked-in defaults
- Editor SDKs (@yarnpkg/sdks) for VS Code, Vim, and other editors to integrate with PnP
- Portable @yarnpkg/shell interpreter so scripts in package.json work identically on every OS
- BSD-2-Clause license, governed by a community contributor model independent of any single company
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yarn-pkg.png
json_schemas:
- name: Yarn Workspace package.json
  property_count: 23
  slug: yarn-pkg-workspace
jsonld:
- class_count: 29
  name: Yarn Pkg Context
  property_count: 10
  slug: yarn-pkg-context
layout: provider
modified: '2026-05-25'
name: Yarn
nav: Providers
network: true
overview: 'Yarn publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Package Manager, JavaScript, Node.js, Monorepo, and Workspaces.


  The Yarn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yarn''s developer surface includes developer portal, getting-started guide, documentation, changelog, and 32 more developer resources.'
random_paper: 11
rules:
- effective_rule_count: 5
  extends: []
  name: Yarn API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: yarn-pkg-jsonschema-spectral-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 22.7
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 21.1
  previous_composite: 26.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yarn-pkg/refs/heads/main/screenshots/yarn-pkg-2026-06-20T201737.png
security:
- kind: domain-security
  name: Yarn Pkg Domain Security
  slug: yarn-pkg-domain-security
  summary_line: TLSv1.2
slug: yarn-pkg
tags:
- Package Manager
- JavaScript
- Node.js
- Monorepo
- Workspaces
- Plug'n'Play
- Open-Source
- Berry
- Yarn 4
website: https://yarnpkg.com
---
