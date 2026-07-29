---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Wakatime Agentic Access
  operation_count: 51
  slug: wakatime-agentic-access
  summary_line: 51 operations · 11 acting
api_count: 20
apis:
- description: Per-project commits enriched with coding time.
  name: WakaTime Commits API
  slug: wakatime-commits-api
- description: User and organization custom-rule definitions for time attribution.
  name: WakaTime Custom Rules API
  slug: wakatime-custom-rules-api
- description: Full data exports.
  name: WakaTime Data Dumps API
  slug: wakatime-data-dumps-api
- description: Continuous time-on-task spans derived from heartbeats.
  name: WakaTime Durations API
  slug: wakatime-durations-api
- description: Available editor plugins and versions.
  name: WakaTime Editors API
  slug: wakatime-editors-api
- description: Non-IDE activity durations created via the API.
  name: WakaTime External Durations API
  slug: wakatime-external-durations-api
- description: User coding goals and their progress.
  name: WakaTime Goals API
  slug: wakatime-goals-api
- description: Coding-activity pings sent by editor plugins.
  name: WakaTime Heartbeats API
  slug: wakatime-heartbeats-api
- description: Curated analytics views (weekdays, days, projects, languages, editors, machines, operating systems, AI days, best day, daily average).
  name: WakaTime Insights API
  slug: wakatime-insights-api
- description: Programming languages.
  name: WakaTime Languages API
  slug: wakatime-languages-api
- description: Public and private leaderboard rankings.
  name: WakaTime Leaderboards API
  slug: wakatime-leaderboards-api
- description: Devices that have sent heartbeats.
  name: WakaTime Machines API
  slug: wakatime-machines-api
- description: WakaTime infrastructure metadata.
  name: WakaTime Meta API
  slug: wakatime-meta-api
- description: Team/organization dashboards and member analytics.
  name: WakaTime Organizations API
  slug: wakatime-organizations-api
- description: Projects the authenticated user has logged time against.
  name: WakaTime Projects API
  slug: wakatime-projects-api
- description: User-wide statistics over preset and custom ranges.
  name: WakaTime Stats API
  slug: wakatime-stats-api
- description: Cached today-only stats for status-bar displays.
  name: WakaTime Status Bar API
  slug: wakatime-status-bar-api
- description: Daily aggregations of coding activity by project, language, editor, OS, machine, branch, and category.
  name: WakaTime Summaries API
  slug: wakatime-summaries-api
- description: Editor + OS user-agent inventory.
  name: WakaTime User Agents API
  slug: wakatime-user-agents-api
- description: Authenticated user profile and public user lookups.
  name: WakaTime Users API
  slug: wakatime-users-api
arazzos:
- description: Pull the status-bar today snapshot, then the day's raw heartbeats and computed durations.
  name: WakaTime Daily Activity Audit
  slug: wakatime-daily-activity-audit-workflow
- description: Check for existing data exports, create a new dump when none exist, then re-list to confirm.
  name: WakaTime Data Dump Export
  slug: wakatime-data-dump-export-workflow
- description: List the user's coding goals, then load the detailed progress for the first goal.
  name: WakaTime Goals Review
  slug: wakatime-goals-review-workflow
- description: Read the public leaderboard, resolve the top leader's public profile, and their all-time totals.
  name: WakaTime Leaderboard To User
  slug: wakatime-leaderboard-to-user-workflow
- description: List the user's private leaderboards, load one board's rankings, then resolve the top member.
  name: WakaTime Private Leaderboard Rankings
  slug: wakatime-private-leaderboard-rankings-workflow
- description: Resolve the current user, load a project's details, list its commits, then fetch one commit.
  name: WakaTime Project Deep Dive
  slug: wakatime-project-deep-dive-workflow
- description: Send a single editor heartbeat, then list the day's heartbeats to confirm it landed.
  name: WakaTime Send Heartbeat And Verify
  slug: wakatime-send-heartbeat-and-verify-workflow
- description: Compare a preset named-range stat set against a custom-range stat set and the global aggregate.
  name: WakaTime Stats Range Comparison
  slug: wakatime-stats-range-comparison-workflow
- description: Pull daily summaries over a date range, then drill into a single day's activity durations.
  name: WakaTime Summaries To Durations Drilldown
  slug: wakatime-summaries-to-durations-workflow
- description: Assemble a snapshot of the authenticated user's profile, all-time totals, recent stats, and projects.
  name: WakaTime User Profile Overview
  slug: wakatime-user-profile-overview-workflow
artifact_total: 52
collections:
- collection_type: postman
  name: WakaTime API
  slug: postman-wakatime-api-v1
- collection_type: open
  name: WakaTime API
  slug: open-wakatime-api-v1
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wakatime-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wakatime-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wakatime-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wakatime-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wakatime-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wakatime-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wakatime/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-daily-activity-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-data-dump-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-goals-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-leaderboard-to-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-private-leaderboard-rankings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-project-deep-dive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-send-heartbeat-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-stats-range-comparison-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-summaries-to-durations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wakatime-user-profile-overview-workflow.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wakatime-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wakatime-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wakatime-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wakatime-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/wakatime-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/wakatime-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/
- group: company
  title: ''
  type: Website
  url: https://wakatime.com
- group: docs
  title: ''
  type: Documentation
  url: https://wakatime.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://wakatime.com/developers
- group: start
  title: ''
  type: Signup
  url: https://wakatime.com/signup
- group: start
  title: ''
  type: Login
  url: https://wakatime.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://wakatime.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://wakatime.com/blog
- group: company
  title: ''
  type: BlogContent
  url: https://github.com/wakatime/wakatime-blog
- group: operate
  title: ''
  type: Status
  url: https://wakatime.com/status
- group: operate
  title: ''
  type: StatusRepo
  url: https://github.com/wakatime/statuspage
- group: operate
  title: ''
  type: ChangeLog
  url: https://wakatime.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://wakatime.com/help
- group: operate
  title: ''
  type: ContactSupport
  url: https://wakatime.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wakatime.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wakatime.com/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://github.com/wakatime/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wakatime
- group: company
  title: ''
  type: TwitterAccount
  url: https://twitter.com/wakatime
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: other
  title: ''
  type: Leaderboards
  url: https://wakatime.com/leaders
- group: other
  title: ''
  type: Embeddable
  url: https://wakatime.com/share
- group: company
  title: ''
  type: PartnerProgram
  url: https://wakatime.com/partners
- group: other
  title: ''
  type: Affiliates
  url: https://wakatime.com/affiliates
- group: build
  title: wakatime-cli (Go, shared by all editor plugins)
  type: CLI
  url: https://github.com/wakatime/wakatime-cli
- group: build
  title: wakatime (Python wrapper for wakatime-cli)
  type: CLI
  url: https://pypi.org/project/wakatime/
- group: build
  title: WakaTime CLI Homebrew Tap
  type: Tools
  url: https://github.com/wakatime/homebrew-tap
- group: build
  title: wakadump (CLI data dump converter)
  type: Tools
  url: https://github.com/wakatime/wakadump
- group: build
  title: WakaQ (Python background job queue used internally by WakaTime)
  type: Tools
  url: https://github.com/wakatime/wakaq
- group: build
  title: WakaQ TypeScript (TypeScript port of WakaQ)
  type: Tools
  url: https://github.com/wakatime/wakaq-ts
- group: build
  title: Crackboard.dev (daily productivity leaderboard built on WakaTime)
  type: Tools
  url: https://github.com/wakatime/crackboard.dev
- group: build
  title: wakatime.io documentation site
  type: Tools
  url: https://github.com/wakatime/wakatime.io
- group: build
  title: Visual Studio Code Plugin
  type: Plugin
  url: https://github.com/wakatime/vscode-wakatime
- group: build
  title: JetBrains IDEs Plugin (IntelliJ, PyCharm, RubyMine, PhpStorm, GoLand, Rider, WebStorm, AppCode, AndroidStudio)
  type: Plugin
  url: https://github.com/wakatime/jetbrains-wakatime
- group: build
  title: Vim Plugin
  type: Plugin
  url: https://github.com/wakatime/vim-wakatime
- group: build
  title: Neovim/Vim Plugin (vim-wakatime)
  type: Plugin
  url: https://github.com/wakatime/vim-wakatime
- group: build
  title: Emacs Plugin (wakatime-mode)
  type: Plugin
  url: https://github.com/wakatime/wakatime-mode
- group: build
  title: Sublime Text Plugin
  type: Plugin
  url: https://github.com/wakatime/sublime-wakatime
- group: build
  title: Atom Plugin
  type: Plugin
  url: https://github.com/wakatime/atom-wakatime
- group: build
  title: Xcode Plugin
  type: Plugin
  url: https://github.com/wakatime/xcode-wakatime
- group: build
  title: Visual Studio Plugin
  type: Plugin
  url: https://github.com/wakatime/visualstudio-wakatime
- group: build
  title: Eclipse Plugin
  type: Plugin
  url: https://github.com/wakatime/eclipse-wakatime
- group: build
  title: NetBeans Plugin
  type: Plugin
  url: https://github.com/wakatime/netbeans-wakatime
- group: build
  title: Zed Plugin
  type: Plugin
  url: https://github.com/wakatime/zed-wakatime
- group: build
  title: Notepad++ Plugin
  type: Plugin
  url: https://github.com/wakatime/notepadpp-wakatime
- group: build
  title: Brackets Plugin
  type: Plugin
  url: https://github.com/wakatime/brackets-wakatime
- group: build
  title: TextMate Plugin
  type: Plugin
  url: https://github.com/wakatime/textmate-wakatime
- group: build
  title: Komodo Plugin
  type: Plugin
  url: https://github.com/wakatime/komodo-wakatime
- group: build
  title: Geany Plugin
  type: Plugin
  url: https://github.com/wakatime/geany-wakatime
- group: build
  title: Gedit Plugin
  type: Plugin
  url: https://github.com/wakatime/gedit-wakatime
- group: build
  title: Kate Plugin
  type: Plugin
  url: https://github.com/wakatime/kate-wakatime
- group: build
  title: Nova Plugin
  type: Plugin
  url: https://github.com/wakatime/WakaTime.novaextension
- group: build
  title: Micro Plugin
  type: Plugin
  url: https://github.com/wakatime/micro-wakatime
- group: build
  title: Kakoune Plugin
  type: Plugin
  url: https://github.com/wakatime/kakoune-wakatime
- group: build
  title: SQL Server Management Studio (SSMS) Plugin
  type: Plugin
  url: https://github.com/wakatime/ssms-wakatime
- group: build
  title: Office Add-ins Plugin
  type: Plugin
  url: https://github.com/wakatime/office-wakatime
- group: build
  title: Delphi Plugin
  type: Plugin
  url: https://github.com/wakatime/delphi-wakatime
- group: build
  title: Coda Plugin
  type: Plugin
  url: https://github.com/wakatime/coda-wakatime
- group: build
  title: Cloud9 Plugin
  type: Plugin
  url: https://github.com/wakatime/c9-wakatime
- group: build
  title: Wing IDE Plugin
  type: Plugin
  url: https://github.com/wakatime/wing-wakatime
- group: build
  title: SlickEdit Plugin
  type: Plugin
  url: https://github.com/wakatime/se_wakatime
- group: build
  title: IDA Pro Plugin
  type: Plugin
  url: https://github.com/wakatime/ida-wakatime-py
- group: build
  title: Eric IDE Plugin
  type: Plugin
  url: https://github.com/wakatime/eric6-wakatime
- group: build
  title: macOS System Tray (tracks Xcode, Figma, Postman, etc.)
  type: Plugin
  url: https://github.com/wakatime/macos-wakatime
- group: build
  title: Windows & Linux Desktop System Tray
  type: Plugin
  url: https://github.com/wakatime/desktop-wakatime
- group: build
  title: Chrome / browser extension
  type: Plugin
  url: https://github.com/wakatime/browser-wakatime
- group: build
  title: Figma Plugin
  type: Plugin
  url: https://github.com/wakatime/figma-wakatime
- group: build
  title: Sketch Plugin
  type: Plugin
  url: https://github.com/wakatime/sketch-wakatime
- group: build
  title: Adobe XD Plugin
  type: Plugin
  url: https://github.com/wakatime/adobe-xd-wakatime
- group: build
  title: Blender Plugin
  type: Plugin
  url: https://github.com/wakatime/blender-wakatime
- group: build
  title: Godot Plugin
  type: Plugin
  url: https://github.com/wakatime/godot-wakatime
- group: build
  title: Unity Plugin
  type: Plugin
  url: https://github.com/wakatime/wakatime-unity
- group: build
  title: Roblox Studio Plugin
  type: Plugin
  url: https://github.com/wakatime/roblox-studio-wakatime
- group: build
  title: Obsidian Plugin
  type: Plugin
  url: https://github.com/wakatime/obsidian-wakatime
- group: build
  title: JupyterLab Plugin
  type: Plugin
  url: https://github.com/wakatime/jupyterlab-wakatime
- group: build
  title: Zotero Plugin
  type: Plugin
  url: https://github.com/wakatime/zotero-wakatime
- group: build
  title: Discord BetterDiscord Plugin
  type: Plugin
  url: https://github.com/wakatime/discord-wakatime
- group: build
  title: Discord Vencord Plugin
  type: Plugin
  url: https://github.com/wakatime/vencord-wakatime
- group: build
  title: Python REPL Plugin (repl-python-wakatime)
  type: Plugin
  url: https://github.com/wakatime/repl-python-wakatime
- group: build
  title: Processing 3 Plugin
  type: Plugin
  url: https://github.com/wakatime/processing-wakatime
- group: build
  title: TeXstudio Plugin
  type: Plugin
  url: https://github.com/wakatime/texstudio-wakatime
- group: build
  title: ReclassEx Plugin
  type: Plugin
  url: https://github.com/wakatime/reclassex-wakatime
- group: build
  title: Codex Plugin
  type: Plugin
  url: https://github.com/wakatime/codex-wakatime
- group: build
  title: Claude Code Plugin (track Claude Code AI coding time)
  type: Plugin
  url: https://github.com/wakatime/claude-code-wakatime
- group: build
  title: Camunda Modeler Plugin
  type: Plugin
  url: https://github.com/wakatime/camunda-modeler-wakatime-plugin
- group: build
  title: WakaTime Mobile (dashboard viewer)
  type: Tools
  url: https://github.com/wakatime/wakatime-mobile
- group: other
  title: Wakapi (self-hosted WakaTime-compatible backend)
  type: SimilarAPIs
  url: https://github.com/muety/wakapi
- group: other
  title: Code::Stats
  type: SimilarAPIs
  url: https://codestats.net/
- group: other
  title: Toggl Track
  type: SimilarAPIs
  url: https://toggl.com/track/
- group: build
  title: MCP Server (geeknees, Node.js, third-party)
  type: Tools
  url: https://github.com/geeknees/wakatime-mcp
- group: build
  title: MCP Server (geeknees Ruby implementation, third-party)
  type: Tools
  url: https://github.com/geeknees/wakatime-mcp-rb
- group: build
  title: MCP Server (dpshde, third-party)
  type: Tools
  url: https://github.com/dpshde/wakatime-mcp
- group: build
  title: MCP Server (pipeworx-io, third-party)
  type: Tools
  url: https://github.com/pipeworx-io/mcp-wakatime
created: '2026-05-28'
description: WakaTime is an automated time-tracking and productivity analytics service for software developers. IDE plugins (VS Code, JetBrains, Vim, Emacs, Sublime, Xcode, Visual Studio, Eclipse, and many more) send heartbeats describing the file, project, language, branch, and editor a developer is working in, and the WakaTime API v1 aggregates that data into dashboards, summaries, stats, goals, leaderboards, and team/organization dashboards. WakaTime also offers private leaderboards, code-time-on-commit enrichment for GitHub/GitLab/Bitbucket, embeddable charts, and a full data export.
examples:
- key_count: 2
  name: Wakatime Create Heartbeat Example
  slug: wakatime-create-heartbeat-example
- key_count: 2
  name: Wakatime Get Stats Last 7 Days Example
  slug: wakatime-get-stats-last-7-days-example
- key_count: 2
  name: Wakatime List Leaders Example
  slug: wakatime-list-leaders-example
- key_count: 2
  name: Wakatime List Summaries Example
  slug: wakatime-list-summaries-example
finops:
- name: Wakatime Finops
  service_category: Developer Tools
  slug: wakatime-finops
image: https://wakatime.com/static/img/wakatime.svg
json_schemas:
- name: Heartbeat
  property_count: 21
  slug: wakatime-heartbeat
- name: SummaryDay
  property_count: 11
  slug: wakatime-summary
- name: User
  property_count: 27
  slug: wakatime-user
json_structures:
- name: Wakatime Heartbeat Structure
  property_count: 21
  slug: wakatime-heartbeat-structure
jsonld:
- class_count: 0
  name: Wakatime Context
  property_count: 69
  slug: wakatime-context
layout: provider
modified: '2026-05-30'
name: WakaTime
nav: Providers
network: true
overview: 'WakaTime publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Commits API, Custom Rules API, Data Dumps API, and 17 more. Tagged areas include Developer Productivity, Developer Tools, Time Tracking, Coding Analytics, and Leaderboards.


  The WakaTime catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WakaTime''s developer surface includes authentication, code examples, documentation, API reference, signup flow, pricing, engineering blog, and 109 more developer resources.'
plans:
- name: Wakatime Plans Pricing
  plan_count: 5
  slug: wakatime-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Wakatime Rate Limits
  slug: wakatime-rate-limits
rules:
- name: WakaTime API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wakatime-jsonschema-spectral-rules
- name: WakaTime API Rules
  rule_count: 51
  severity_counts:
    error: 18
    hint: 0
    info: 7
    warn: 26
  slug: wakatime-rules
scopes:
- name: Wakatime Scopes
  scope_count: 8
  slug: wakatime-scopes
  summary_line: 8 scopes · authorizationCode/implicit
score:
  band: strong
  composite: 64.4
  delta: -7.5
  facets:
    commercial_clarity: 92.1
    contract_quality: 61.4
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 71.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 20
      marker_coverage: 100.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wakatime/refs/heads/main/screenshots/wakatime-2026-06-20T201207.png
security:
- kind: authentication
  name: Wakatime Authentication
  slug: wakatime-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Wakatime Domain Security
  slug: wakatime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wakatime Vulnerability Disclosure
  slug: wakatime-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Wakatime Trust Center
  slug: wakatime-trust-center
  summary_line: SOC 2, ISO 27001
slug: wakatime
tags:
- Developer Productivity
- Developer Tools
- Time Tracking
- Coding Analytics
- Leaderboards
- IDE Plugins
- Open Source
- Public APIs
website: https://wakatime.com
---
