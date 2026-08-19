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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The pnpm command-line interface for managing JavaScript/Node.js packages. Provides commands for installing, updating, and removing dependencies; running package scripts; executing one-off packages via
  name: pnpm CLI
  slug: pnpm-cli
- description: Native monorepo support driven by a `pnpm-workspace.yaml` file at the repository root. Supports the `workspace:` protocol for explicit local package references, a shared workspace lockfile, package fi
  name: pnpm Workspaces
  slug: pnpm-workspaces
- description: A content-addressable store that holds every version of every package exactly once on disk and hard-links (or reflinks) files into project `node_modules`. This produces a strict, non-flat dependency l
  name: pnpm Content-Addressable Store
  slug: pnpm-store
- description: Programmatic extension points for customizing dependency resolution and installation behavior. `.pnpmfile.cjs` exposes lifecycle hooks (`readPackage`, `afterAllResolved`) that let projects rewrite pac
  name: pnpm Hooks
  slug: pnpm-hooks
- description: Configuration surface for pnpm spanning `.npmrc`, environment variables, and `pnpm`-prefixed fields in `package.json`. Controls registry selection, authentication tokens, store location, hoisting beha
  name: pnpm Configuration
  slug: pnpm-config
artifact_total: 38
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pnpm-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://pnpm.io
- group: start
  title: ''
  type: GettingStarted
  url: https://pnpm.io/installation
- group: docs
  title: ''
  type: Documentation
  url: https://pnpm.io/motivation
- group: docs
  title: ''
  type: Documentation
  url: https://pnpm.io/pnpm-cli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/pnpm/pnpm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pnpm
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/pnpm/pnpm/releases
- group: commercial
  title: ''
  type: Legal
  url: https://github.com/pnpm/pnpm/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/pnpm/pnpm/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/pnpm/pnpm/issues
- group: operate
  title: ''
  type: Support
  url: https://github.com/pnpm/pnpm/discussions
- group: operate
  title: ''
  type: Contact
  url: https://chat.pnpm.io/
- group: other
  title: ''
  type: X
  url: https://x.com/pnpmjs
- group: operate
  title: ''
  type: Contact
  url: https://bsky.app/profile/pnpm.io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@pnpmjs
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/pnpm
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/pnpm
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@pnpm/exe
- group: commercial
  title: ''
  type: Pricing
  url: https://opencollective.com/pnpm
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/sponsors/pnpm
- group: company
  title: ''
  type: Blog
  url: https://pnpm.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://pnpm.io/feature-comparison
- group: docs
  title: ''
  type: Documentation
  url: https://pnpm.io/benchmarks
- group: operate
  title: ''
  type: FAQ
  url: https://pnpm.io/faq
- group: other
  title: ''
  type: Showcase
  url: https://pnpm.io/uses
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pnpm/rfcs
created: '2026-05-25'
description: pnpm is a fast, disk space efficient package manager for JavaScript and Node.js projects. It uses a content-addressable store and a strict, symlinked node_modules layout so every version of every package is stored exactly once on disk and projects can only access dependencies they explicitly declare. pnpm provides first-class monorepo support via pnpm-workspace.yaml, the workspace protocol, Catalogs, package filtering, and a shared lockfile, and ships supply-chain safety features such as minimumReleaseAge, opt-in lifecycle scripts, dependency overrides, and a built-in patch workflow. Developed in the open under the MIT license on GitHub with an Open Collective sponsorship model, pnpm is used by major JavaScript projects including Next.js, Vue, Vite, Nuxt, Material UI, Prisma, Astro, and SvelteKit.
features:
- description: Each package version is stored once on disk and hard-linked into projects, saving substantial disk space across all projects on the machine.
  name: Content-addressable store
- description: A symlinked node_modules layout means packages can only access dependencies they explicitly declare, catching phantom-dependency bugs at install time.
  name: Strict, non-flat node_modules
- description: Optimized installation pipeline that is consistently faster than npm and Yarn on cold and warm installs, especially for large monorepos.
  name: Up to 2x faster installs
- description: First-class workspaces driven by pnpm-workspace.yaml with the workspace protocol, recursive commands, package filtering, and Catalogs for shared version pinning.
  name: Native workspace and monorepo support
- description: Centralized dependency-version management across a monorepo so every package shares a single pinned version of common dependencies.
  name: Catalogs
- description: pnpm-lock.yaml captures the exact resolved dependency graph, peer relationships, and patches for reproducible installs.
  name: Deterministic lockfile
- description: minimumReleaseAge to delay adoption of brand-new package versions, ignoredBuiltDependencies and onlyBuiltDependencies to opt into lifecycle scripts, and removal of postinstall scripts by default.
  name: Supply-chain safety controls
- description: Built-in workflow to patch installed dependencies and persist the patch in pnpm.patchedDependencies without forking the package.
  name: pnpm patch
- description: Repository-level dependency rewriting and peer-dependency repair without forking upstream packages.
  name: pnpm overrides and packageExtensions
- description: readPackage and afterAllResolved hooks let you programmatically rewrite manifests during resolution and installation.
  name: .pnpmfile.cjs hooks
- description: Run packages without installing them globally, with caching in the store.
  name: pnx (dlx) and pnpm exec
- description: pnpm env install lets you manage Node.js (and other JavaScript runtime) versions directly through pnpm.
  name: Built-in runtime management
- description: Distributed as @pnpm/exe, a single self-contained executable that does not require an existing Node.js installation.
  name: Cross-platform standalone binary
- description: First-class support for Node.js Corepack so projects can pin a specific pnpm version via packageManager in package.json.
  name: Corepack-compatible
- description: Permissively licensed and developed in the open on GitHub with an Open Collective sponsorship model.
  name: MIT-licensed open source
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pnpm.png
integrations:
- description: pnpm is one of the package managers managed by Corepack, enabling version pinning via packageManager in package.json.
  name: Node.js Corepack
- description: Official pnpm/action-setup and pnpm/setup actions for installing pnpm and a JavaScript runtime in a single step.
  name: GitHub Actions
- description: Recommended workflow tool for versioning and publishing packages in pnpm monorepos.
  name: Changesets
- description: Rush uses pnpm under the hood for large monorepos at Microsoft and elsewhere.
  name: Microsoft Rush
- description: Nx integrates with pnpm workspaces for monorepo task orchestration and caching.
  name: Nx
- description: First-class pnpm workspace support for incremental builds and remote caching.
  name: Turbo (Turborepo)
- description: Official guidance for using pnpm in Docker images, including the standalone binary and lockfile-aware multi-stage builds.
  name: Docker
- description: Works with any npm-compatible registry including Verdaccio, JFrog Artifactory, GitHub Packages, and AWS CodeArtifact.
  name: Verdaccio and private registries
- description: Bit Cloud (a Platinum sponsor) uses pnpm as a foundation for component-based development.
  name: Bit
- description: First-class support for pnpm in major JavaScript deployment platforms with workspace-aware installs.
  name: Vercel, Netlify, Cloudflare Pages
layout: provider
modified: '2026-05-25'
name: pnpm
nav: Providers
network: true
overview: 'pnpm publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Node.js, Package Manager, Monorepo, JavaScript, and Open Source.


  pnpm''s developer surface includes developer portal, getting-started guide, documentation, release notes, legal docs, changelog, support, and 20 more developer resources.'
random_paper: 145
score:
  band: emerging
  composite: 20.4
  delta: 0.8
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 19.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pnpm/refs/heads/main/screenshots/pnpm-2026-06-20T191821.png
security:
- kind: domain-security
  name: Pnpm Domain Security
  slug: pnpm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pnpm
tags:
- Node.js
- Package Manager
- Monorepo
- JavaScript
- Open Source
- Developer Tools
- Dependency Management
- CLI
use_cases:
- description: Manage hundreds of interdependent packages with a single shared lockfile, the workspace protocol, Catalogs, and recursive commands.
  name: Large JavaScript monorepos
- description: Cut install time substantially in CI by leveraging the content-addressable store and the official pnpm/action-setup GitHub Action.
  name: CI/CD pipeline acceleration
- description: Share a single copy of each package version across every project on a machine, dramatically reducing disk usage compared to npm or Yarn.
  name: Disk-constrained developer machines
- description: Use minimumReleaseAge, ignoredBuiltDependencies, and strict lifecycle script policy to reduce exposure to malicious or compromised npm packages.
  name: Supply-chain hardening
- description: The strict non-flat node_modules layout surfaces undeclared dependencies during local development rather than in production.
  name: Phantom dependency detection
- description: pnpm-lock.yaml plus pnpm.overrides and pnpm.patchedDependencies make installations byte-reproducible across machines.
  name: Reproducible builds
- description: Use the pnpm/setup action and pnpm env to standardize Node.js, Bun, or Deno versions across teams.
  name: Multi-runtime JavaScript projects
website: https://pnpm.io
---
