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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Limrun Agentic Access
  operation_count: 26
  slug: limrun-agentic-access
  summary_line: 26 operations · 11 acting
api_count: 7
apis:
- description: The Analytics API from Limrun — 3 operation(s) for analytics.
  name: Limrun Analytics API
  slug: limrun-analytics-api
- description: The Android Instances API from Limrun — 2 operation(s) for android instances.
  name: Limrun Android Instances API
  slug: limrun-android-instances-api
- description: The Assets API from Limrun — 2 operation(s) for assets.
  name: Limrun Assets API
  slug: limrun-assets-api
- description: The Downloads API from Limrun — 1 operation(s) for downloads.
  name: Limrun Downloads API
  slug: limrun-downloads-api
- description: The Gradle Instances API from Limrun — 2 operation(s) for gradle instances.
  name: Limrun Gradle Instances API
  slug: limrun-gradle-instances-api
- description: The Ios Instances API from Limrun — 2 operation(s) for ios instances.
  name: Limrun Ios Instances API
  slug: limrun-ios-instances-api
- description: The Xcode Instances API from Limrun — 4 operation(s) for xcode instances.
  name: Limrun Xcode Instances API
  slug: limrun-xcode-instances-api
artifact_total: 13
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/limrun-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://lim.run
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.limrun.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.limrun.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.limrun.com/docs/reference/sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.limrun.com/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.limrun.com
- group: start
  title: ''
  type: Console
  url: https://console.limrun.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/limrun-inc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.limrun.com
- group: operate
  title: ''
  type: Support
  url: mailto:contact@limrun.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/limrun-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/limrun-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/limrun-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/limrun-cli.yml
- group: design
  title: ''
  type: Components
  url: components/limrun-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/limrun-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/limrun-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/limrun-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/limrun-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/limrun-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/limrun-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/limrun-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/limrun-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/limrun-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/limrun-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/limrun-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/limrun-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/limrun-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/limrun-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/limrun-inc/typescript-sdk/blob/main/SECURITY.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/limrun-agentic-access.yml
created: '2026-07-17'
description: 'Limrun (Limrun, Inc.) is a Y Combinator-backed cloud infrastructure company for mobile development, built so cloud coding agents and Linux CI runners can build, run, and test iOS and Android apps without a Mac. Limrun exposes three composable cloud services behind one REST control plane at api.limrun.com: iOS simulators running on real Macs (streamable in a browser and drivable programmatically through taps, screenshots, accessibility element trees, video recording, and app lifecycle), remote Xcode and Bazel build sandboxes that accept synced sources and run xcodebuild or remote build execution, and accelerated Android emulators reachable over an ADB tunnel by Android Studio, Appium, or scrcpy. Gradle build sandboxes and a managed Asset Storage service for .apk and .app build artifacts round out the platform. Every instance is created through the control plane with an org API key and returns its own per-instance token, data-plane URLs, a signed browser stream URL, and its own
  Model Context Protocol server, which makes Limrun one of the few providers shipping a per-instance MCP endpoint alongside first-party Agent Skills for coding agents.'
image: https://lim.run/logo-inner-filled-no-border.svg
layout: provider
mcp_servers:
- description: ''
  name: limrun-mcp.yml
  slug: limrun-mcpyml
modified: '2026-07-19'
name: Limrun
nav: Providers
network: true
overview: 'Limrun publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Android Instances API, Assets API, and 4 more. Tagged areas include Company, Mobile, iOS, Android, and Simulators.


  Limrun''s developer surface includes documentation, API reference, getting-started guide, signup flow, developer console, support, CLI, and 26 more developer resources.'
random_paper: 83
scopes:
- name: Limrun Scopes
  scope_count: 1
  slug: limrun-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.5
  delta: -0.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 40.2
    developer_ergonomics: 84.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/limrun/refs/heads/main/screenshots/limrun-2026-07-25T225212.png
security:
- kind: authentication
  name: Limrun Authentication
  slug: limrun-authentication
  summary_line: http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Limrun Domain Security
  slug: limrun-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Limrun Vulnerability Disclosure
  slug: limrun-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: limrun
tags:
- Company
- Mobile
- iOS
- Android
- Simulators
- Emulators
- Cloud Infrastructure
- Continuous Integration
- Developer Tools
- Testing
- Agents
- Model Context Protocol
- Sandboxes
- Xcode
website: https://lim.run
---
