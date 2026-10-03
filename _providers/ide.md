---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 30
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering integrated development environments (IDEs), code editors, and cloud workspaces with APIs. This topic captures the editors, IDEs, and developer workspaces that expose programmable surfaces, including local desktop IDEs (Visual Studio, JetBrains IDEs, Eclipse), modern AI-first editors (Cursor, Windsurf), agentic coding assistants (Aider, Cline, Continue, GitHub Copilot, Amazon Q Developer, Tabnine), notebook environments (Jupyter, JupyterLab, JupyterHub, Google Colab), cloud development platforms (Replit), plugin marketplaces (JetBrains Marketplace), and editor extension APIs (Visual Studio Code). IDEs and editor-as-API platforms expose extension APIs, Language Server Protocol (LSP) endpoints, workspace and project APIs, debugging APIs, plugin marketplaces, telemetry, completion and chat APIs, and remote workspace orchestration. This collection is distinct from API client tooling (HTTP request testing) and focuses on the surface where developers
  write, edit, debug, and run code.
examples:
- key_count: 14
  name: Ide Extension Example
  slug: ide-extension-example
- key_count: 10
  name: Ide Workspace Example
  slug: ide-workspace-example
features:
- description: IDEs expose extension APIs that let third-party developers add commands, views, language support, debuggers, and integrations. Examples include the VS Code Extension API, JetBrains Platform SDK, and Eclipse Platform APIs.
  name: Extension and Plugin APIs
- description: LSP is a JSON-RPC protocol that standardizes how editors communicate with language tooling (completion, hover, diagnostics, references). It is the backbone of polyglot editor support across VS Code, Neovim, JetBrains, and Eclipse Theia.
  name: Language Server Protocol (LSP)
- description: Editors expose workspace, project, and file-system APIs that extensions and remote clients use to read, write, and watch source files, including multi-root workspaces and remote workspace orchestration.
  name: Workspace and Project APIs
- description: Modern editors and assistants (GitHub Copilot, Cursor, Windsurf, Tabnine, Continue, Cline, Aider, Amazon Q Developer) expose inline completion, chat, and agentic edit APIs that integrate LLMs into the developer loop.
  name: AI Completion and Chat APIs
- description: Marketplaces like the VS Code Marketplace and JetBrains Marketplace host millions of extensions and expose APIs for publishing, searching, and managing plugin metadata, downloads, and reviews.
  name: Plugin and Extension Marketplaces
- description: Jupyter and JupyterLab expose REST APIs and a WebSocket-based messaging protocol for managing kernels, sessions, contents, and terminals, powering notebook computing in Colab, JupyterHub, and many cloud platforms.
  name: Notebook and Kernel APIs
- description: Cloud-based IDEs like Replit and remote-development backends provide APIs for provisioning ephemeral workspaces, managing containers, and streaming editor sessions to browsers.
  name: Cloud Workspaces and Remote Development
- description: Standards like the Debug Adapter Protocol (DAP) and Test Adapter Protocol let editors integrate with debuggers and test runners across many languages through a single, portable interface.
  name: Debugger and Test Adapter Protocols
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: The dominant open-source code editor with the VS Code Extension API, Language Server Protocol implementation, Debug Adapter Protocol, and a marketplace of 60,000+ extensions.
  name: Visual Studio Code
- description: A family of professional IDEs (IntelliJ IDEA, PyCharm, GoLand, WebStorm, PhpStorm, RubyMine, Rider) built on the JetBrains Platform SDK with a unified plugin model and marketplace.
  name: JetBrains IDEs
- description: AI-first code editor forked from VS Code with deep agentic editing, codebase-aware chat, and tab-driven inline completion.
  name: Cursor
- description: AI-native editor (formerly Codeium) featuring Cascade autonomous agent, multi-step planning, and enterprise APIs for completion analytics and team management.
  name: Windsurf
- description: AI pair programmer integrated into VS Code, Visual Studio, JetBrains, Neovim, and the GitHub web UI, with Copilot Chat and agent APIs.
  name: GitHub Copilot
- description: Interactive computing platform exposing REST APIs and a WebSocket messaging protocol for kernels, sessions, contents, and terminals across notebook, JupyterLab, and JupyterHub deployments.
  name: Jupyter / JupyterLab
- description: Cloud development platform offering instant containerized workspaces, multiplayer editing, an integrated terminal, and APIs for managing Repls and deployments.
  name: Replit
- description: Open-source community behind the Eclipse IDE, Eclipse Theia, Eclipse Che, and a wide ecosystem of editor and language tooling projects.
  name: Eclipse Foundation
json_schemas:
- name: Extension
  property_count: 14
  slug: ide-extension
- name: Workspace
  property_count: 10
  slug: ide-workspace
json_structures:
- name: Ide Extension Structure
  property_count: 14
  slug: ide-extension-structure
- name: Ide Workspace Structure
  property_count: 10
  slug: ide-workspace-structure
jsonld:
- class_count: 8
  name: Ide Context
  property_count: 21
  slug: ide-context
layout: provider
modified: '2026-05-19'
name: IDE
nav: Providers
network: true
overview: 'IDE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IDE, Code Editor, Cloud IDE, Developer Tools, and Workspace.


  The IDE catalog on APIs.io includes 1 JSON-LD context.


  IDE''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: ide
tags:
- IDE
- Code Editor
- Cloud IDE
- Developer Tools
- Workspace
use_cases:
- description: Developers integrate LLM-backed completion and agentic editing into IDEs through extension APIs and editor-side hooks, powering products like Copilot, Cursor, Windsurf, Continue, and Cline.
  name: Building AI Coding Assistants
- description: Engineering platform teams build internal extensions for VS Code, JetBrains, and Eclipse to embed company-specific scaffolding, deployment, and code-review tooling directly into the editor.
  name: Custom Internal Developer Tooling
- description: Data teams use Jupyter, JupyterLab, JupyterHub, and Google Colab APIs to automate notebook execution, manage shared kernels, provision multi-user environments, and integrate with data pipelines.
  name: Notebook-Driven Data Science Workflows
- description: Platforms like Replit and remote workspace backends use APIs to spin up pre-configured cloud IDEs for tutorials, interviews, and short-lived development environments without local toolchains.
  name: Cloud-Native Onboarding and Ephemeral Environments
- description: ISVs publish, version, and analyze extensions via the JetBrains Marketplace and Visual Studio Marketplace APIs, integrating release pipelines and revenue reporting into CI/CD.
  name: Plugin Distribution and Marketplace Automation
- description: Engines like Unity expose editor APIs and packages that integrate live services (multiplayer, analytics, build, asset management) directly into the editor used by game developers.
  name: Game and Real-Time Editor Tooling
- description: Tooling authors implement Language Server Protocol once and expose features (completion, navigation, diagnostics) across every LSP-capable editor, reducing per-IDE integration cost.
  name: Standardized Language Tooling Across Editors
website: https://apievangelist.com
---
