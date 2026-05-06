---
aid: yarn
name: YARN
description: YARN (Yet Another Resource Negotiator in the original Hadoop context; also the JavaScript package manager) refers here to the yarnpkg.com JavaScript package manager. Yarn is a fast, reliable, and secure dependency management tool for JavaScript. Originally developed by Meta as an alternative to npm, Yarn offers deterministic dependency resolution, offline caching, parallel installation, and Plug'n'Play (PnP) module resolution. The project is actively maintained under the yarnpkg/berry repository (Yarn 2+) with a modular plugin architecture. Yarn provides a programmatic JavaScript/TypeScript API via @yarnpkg/core for building tools and plugins.
type: Index
url: https://github.com/yarnpkg/berry
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - JavaScript
  - Node.js
  - Package Manager
  - YARN
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: yarn:yarn-core-api
    name: YARN Core API
    description: The @yarnpkg/core programmatic JavaScript/TypeScript API that allows applications to interact with Yarn projects, workspaces, and dependency resolution. Used for building Yarn plugins and tooling integrations.
    humanURL: https://yarnpkg.com/api
    baseURL: https://yarnpkg.com
    tags:
      - API
      - JavaScript
      - Package Manager
      - Plugin
      - TypeScript
    properties:
      - type: Documentation
        url: https://yarnpkg.com/api
      - type: APIReference
        url: https://yarnpkg.com/api
      - type: GitHubRepository
        url: https://github.com/yarnpkg/berry
      - type: GettingStarted
        url: https://yarnpkg.com/advanced/plugin-tutorial
      - type: Tutorials
        url: https://yarnpkg.com/advanced/plugin-tutorial
  - aid: yarn:yarn-cli
    name: YARN CLI
    description: The Yarn command-line interface built on @yarnpkg/cli, providing commands for package installation, workspace management, publishing, and more. Supports a plugin system for extensibility.
    humanURL: https://yarnpkg.com/cli
    baseURL: https://yarnpkg.com
    tags:
      - CLI
      - JavaScript
      - Package Manager
    properties:
      - type: Documentation
        url: https://yarnpkg.com/cli
      - type: APIReference
        url: https://yarnpkg.com/cli
      - type: CLI
        url: https://yarnpkg.com/cli
      - type: GettingStarted
        url: https://yarnpkg.com/getting-started/install
common:
  - type: Documentation
    url: https://yarnpkg.com/getting-started
  - type: GettingStarted
    url: https://yarnpkg.com/getting-started/install
  - type: Tutorials
    url: https://yarnpkg.com/getting-started/usage
  - type: APIReference
    url: https://yarnpkg.com/api
  - type: GitHubOrganization
    url: https://github.com/yarnpkg
  - type: GitHubRepository
    url: https://github.com/yarnpkg/berry
  - type: SDK
    url: https://www.npmjs.com/package/yarn
  - type: ChangeLog
    url: https://github.com/yarnpkg/berry/blob/master/CHANGELOG.md
  - type: BestPractices
    url: https://yarnpkg.com/migration/guide
  - type: Resources
    url: https://yarnpkg.com/configuration/yarnrc
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/yarn/main/json-schema/yarn-package-schema.json
  - type: Features
    data:
      - name: Workspaces
        description: First-class monorepo support letting projects split into sub-components managed from a single root.
      - name: Plug'n'Play (PnP)
        description: Alternative installation strategy that eliminates node_modules in favor of a single resolution map for faster, stricter installs.
      - name: Plugin Architecture
        description: Modular core with 25+ default plugins and a public API for building custom workflows and integrations.
      - name: Offline Caching
        description: Local cache of downloaded packages enabling reproducible installs without network access.
      - name: Parallel Installation
        description: Concurrent dependency fetching and linking for faster installs versus serial package managers.
      - name: Deterministic Resolution
        description: Lockfile-driven dependency resolution that produces identical installs across machines and CI runs.
      - name: Hardened Mode
        description: Stricter install mode that verifies registry metadata against the lockfile to defend against supply-chain tampering.
      - name: Cross-platform Shell
        description: Built-in shell interpreter so package scripts behave consistently across Linux, macOS, and Windows.
      - name: Constraints
        description: Declarative rules for enforcing dependency policies and conventions across a workspace.
      - name: Interactive Commands
        description: Search and upgrade UIs that let developers explore and manage dependencies interactively.
      - name: Programmatic API
        description: TypeScript-first @yarnpkg/core surface for building plugins, tooling, and CI integrations.
  - type: UseCases
    data:
      - name: Monorepo Management
        description: Coordinate dependencies, scripts, and releases across many packages in a single repository.
      - name: Dependency Management
        description: Install, upgrade, and audit JavaScript and TypeScript dependencies for libraries and applications.
      - name: Plugin Development
        description: Build and distribute plugins that extend the Yarn CLI with project-specific commands and behaviors.
      - name: Reproducible CI Builds
        description: Use the lockfile, offline cache, and hardened mode to keep CI installs deterministic and tamper-resistant.
      - name: Package Publishing
        description: Publish packages to npm and other registries via the npm-related CLI commands and release workflows.
      - name: Workspace Coordination
        description: Run scripts across workspaces, share dependencies, and enforce constraints in large multi-package projects.
  - type: Integrations
    data:
      - name: npm Registry
        description: Primary package registry for installing and publishing JavaScript packages.
      - name: Node.js
        description: Runtime that executes Yarn-managed packages and the Yarn CLI itself.
      - name: TypeScript
        description: Yarn ships TypeScript type definitions and is itself written primarily in TypeScript.
      - name: Corepack
        description: Node.js shim that pins and provisions the Yarn version per project.
      - name: VS Code Editor SDK
        description: Editor SDK integration that wires Yarn PnP-managed dependencies into VS Code's TypeScript and ESLint tooling.
      - name: JetBrains Editor SDK
        description: Editor SDK integration for IntelliJ-family IDEs to resolve PnP dependencies in editor tooling.
      - name: GitHub
        description: Source repository, issue tracker, and release distribution for the yarnpkg organization.
      - name: Discord
        description: Community chat for support, contributor coordination, and announcements.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
