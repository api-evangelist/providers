---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sweep-dev-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sweep-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sweep.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sweep.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://sweep.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.sweep.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sweep.dev/changelog
- group: other
  title: ''
  type: JetBrainsMarketplace
  url: https://plugins.jetbrains.com/plugin/24701-sweep-ai
- group: build
  title: ''
  type: VSCodeMarketplace
  url: https://marketplace.visualstudio.com/items?itemName=sweepai.sweep
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sweepai
- group: build
  title: ''
  type: LegacyGitHubAgent
  url: https://github.com/sweepai/sweep
- group: other
  title: ''
  type: YCombinatorLaunch
  url: https://www.ycombinator.com/launches/JAE-sweep-ai-powered-junior-developer
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sweep__ai
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sweep
- group: operate
  title: ''
  type: Contact
  url: mailto:team@sweep.dev
created: '2026-05-25'
description: Sweep is a San Francisco-based, Y Combinator-backed company (originally launched as "Sweep — AI-powered junior developer") that has pivoted from being a GitHub App which turned issues into pull requests into an AI coding assistant delivered primarily as a JetBrains IDE plugin, with autocomplete-only support for VS Code and Zed. The current Sweep product pairs a proprietary "Tab model" next-edit autocomplete with an in-IDE Agent for chat, inline editing, AI commit messages, and AI code review across IntelliJ IDEA, PyCharm, WebStorm, GoLand, PhpStorm, Rider, Android Studio, RustRover, RubyMine, CLion, and Aqua. The plugin indexes the local codebase for context, supports Remote MCP Servers with OAuth, web search and fetch tools, and ships under a commercial credit-based pricing model (Free Trial, Basic $10/mo, Pro $20/mo, Ultra $60/mo) with enterprise SOC 2 and zero-data-retention options via contact sales. Sweep has no public developer REST API, no SDK, and no documented webhooks;
  the company's primary distribution surfaces are the JetBrains Marketplace, the VS Code Marketplace, and the Zed extension registry, and its open-source footprint on GitHub has narrowed to research forks (SWE-bench, SGLang), tokenizer/diff utilities (bpe-qwen, difflib-rs), and the now-legacy sweepai/sweep repository that documented the original GitHub PR agent. Sweep is profiled here as an AI developer-experience vendor rather than as an API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sweep-dev.png
layout: provider
modified: '2026-05-25'
name: Sweep
nav: Providers
network: true
overview: 'Sweep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Coding Assistant, AI Developer Tools, AI Agent, Code Autocomplete, and Next Edit Suggestions.


  Sweep''s developer surface includes documentation, pricing, engineering blog, changelog, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sweep-dev/refs/heads/main/screenshots/sweep-dev-2026-06-20T194800.png
security:
- kind: domain-security
  name: Sweep Dev Domain Security
  slug: sweep-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sweep Dev Trust Center
  slug: sweep-dev-trust-center
  summary_line: SOC 2
slug: sweep-dev
tags:
- AI Coding Assistant
- AI Developer Tools
- AI Agent
- Code Autocomplete
- Next Edit Suggestions
- JetBrains Plugin
- IntelliJ Platform
- VS Code Extension
- Zed Editor
- Code Review
- AI Commit Messages
- Inline Editing
- MCP
- Developer Productivity
- GitHub Issues
- Pull Request Automation
- Y Combinator
website: https://sweep.dev
---
