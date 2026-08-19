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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 180
  human_in_the_loop: 12
  name: Daytona Io Agentic Access
  operation_count: 330
  slug: daytona-io-agentic-access
  summary_line: 330 operations · 180 acting · 12 human-in-the-loop
api_count: 28
apis:
- description: The admin API from Daytona — 15 operation(s) for admin.
  name: Daytona admin API
  slug: daytona-io-admin-api
- description: The api-keys API from Daytona — 4 operation(s) for api-keys.
  name: Daytona api-keys API
  slug: daytona-io-api-keys-api
- description: The audit API from Daytona — 1 operation(s) for audit.
  name: Daytona audit API
  slug: daytona-io-audit-api
- description: The computer-use API from Daytona — 32 operation(s) for computer-use.
  name: Daytona computer-use API
  slug: daytona-io-computer-use-api
- description: The config API from Daytona — 1 operation(s) for config.
  name: Daytona config API
  slug: daytona-io-config-api
- description: The docker-registry API from Daytona — 3 operation(s) for docker-registry.
  name: Daytona docker-registry API
  slug: daytona-io-docker-registry-api
- description: The file-system API from Daytona — 12 operation(s) for file-system.
  name: Daytona file-system API
  slug: daytona-io-file-system-api
- description: The git API from Daytona — 9 operation(s) for git.
  name: Daytona git API
  slug: daytona-io-git-api
- description: The Health API from Daytona — 2 operation(s) for health.
  name: Daytona Health API
  slug: daytona-io-health-api
- description: The info API from Daytona — 3 operation(s) for info.
  name: Daytona info API
  slug: daytona-io-info-api
- description: The interpreter API from Daytona — 3 operation(s) for interpreter.
  name: Daytona interpreter API
  slug: daytona-io-interpreter-api
- description: The jobs API from Daytona — 4 operation(s) for jobs.
  name: Daytona jobs API
  slug: daytona-io-jobs-api
- description: The lsp API from Daytona — 7 operation(s) for lsp.
  name: Daytona lsp API
  slug: daytona-io-lsp-api
- description: The object-storage API from Daytona — 1 operation(s) for object-storage.
  name: Daytona object-storage API
  slug: daytona-io-object-storage-api
- description: The organizations API from Daytona — 30 operation(s) for organizations.
  name: Daytona organizations API
  slug: daytona-io-organizations-api
- description: The port API from Daytona — 2 operation(s) for port.
  name: Daytona port API
  slug: daytona-io-port-api
- description: The preview API from Daytona — 4 operation(s) for preview.
  name: Daytona preview API
  slug: daytona-io-preview-api
- description: The process API from Daytona — 14 operation(s) for process.
  name: Daytona process API
  slug: daytona-io-process-api
- description: The regions API from Daytona — 1 operation(s) for regions.
  name: Daytona regions API
  slug: daytona-io-regions-api
- description: The runners API from Daytona — 9 operation(s) for runners.
  name: Daytona runners API
  slug: daytona-io-runners-api
- description: The sandbox API from Daytona — 37 operation(s) for sandbox.
  name: Daytona sandbox API
  slug: daytona-io-sandbox-api
- description: The server API from Daytona — 1 operation(s) for server.
  name: Daytona server API
  slug: daytona-io-server-api
- description: The snapshots API from Daytona — 6 operation(s) for snapshots.
  name: Daytona snapshots API
  slug: daytona-io-snapshots-api
- description: The toolbox API from Daytona — 61 operation(s) for toolbox.
  name: Daytona toolbox API
  slug: daytona-io-toolbox-api
- description: The users API from Daytona — 5 operation(s) for users.
  name: Daytona users API
  slug: daytona-io-users-api
- description: The volumes API from Daytona — 3 operation(s) for volumes.
  name: Daytona volumes API
  slug: daytona-io-volumes-api
- description: The webhooks API from Daytona — 3 operation(s) for webhooks.
  name: Daytona webhooks API
  slug: daytona-io-webhooks-api
- description: The workspace API from Daytona — 12 operation(s) for workspace.
  name: Daytona workspace API
  slug: daytona-io-workspace-api
arazzos:
- description: Register a snapshot from a container image, poll until it builds, and activate it if it lands inactive.
  name: Daytona Build and Activate a Snapshot
  slug: daytona-io-build-and-activate-snapshot-workflow
- description: Snapshot a live sandbox into a reusable image and wait for the sandbox to return to running.
  name: Daytona Capture a Sandbox as a Snapshot
  slug: daytona-io-capture-sandbox-snapshot-workflow
- description: Fork an existing sandbox into a new independent copy and wait until the fork is running.
  name: Daytona Fork a Sandbox
  slug: daytona-io-fork-sandbox-workflow
- description: Build a snapshot from an image, wait for it to build, then launch and run a sandbox from it.
  name: Daytona From Container Image to Running Sandbox
  slug: daytona-io-image-to-running-sandbox-workflow
- description: Create a sandbox from a snapshot, poll until it reaches the started state, then read its details.
  name: Daytona Provision a Sandbox
  slug: daytona-io-provision-sandbox-workflow
- description: Create a persistent volume, wait until it is ready, then launch a sandbox with the volume mounted.
  name: Daytona Provision a Volume and Attach It to a New Sandbox
  slug: daytona-io-provision-volume-and-sandbox-workflow
- description: Start an archived or stopped sandbox and wait until it is running again.
  name: Daytona Restore an Archived Sandbox
  slug: daytona-io-restore-archived-sandbox-workflow
- description: Stop a running sandbox, wait until it is fully stopped, then archive it to cold storage.
  name: Daytona Stop and Archive a Sandbox
  slug: daytona-io-stop-and-archive-sandbox-workflow
artifact_total: 152
collections:
- collection_type: postman
  name: Daytona Admin API
  slug: postman-daytona-admin-api
- collection_type: postman
  name: Daytona Api Keys API
  slug: postman-daytona-api-keys-api
- collection_type: postman
  name: Daytona Health API
  slug: postman-daytona-health-api
- collection_type: postman
  name: Daytona Organizations API
  slug: postman-daytona-organizations-api
- collection_type: postman
  name: Daytona Preview API
  slug: postman-daytona-preview-api
- collection_type: postman
  name: Daytona Sandbox API
  slug: postman-daytona-sandbox-api
- collection_type: postman
  name: Daytona Sandbox Toolbox API
  slug: postman-daytona-sandbox-toolbox-api
- collection_type: postman
  name: Daytona Snapshots API
  slug: postman-daytona-snapshots-api
- collection_type: postman
  name: Daytona Toolbox API
  slug: postman-daytona-toolbox-api
- collection_type: postman
  name: Daytona Users API
  slug: postman-daytona-users-api
- collection_type: postman
  name: Daytona Volumes API
  slug: postman-daytona-volumes-api
- collection_type: postman
  name: Daytona Webhooks API
  slug: postman-daytona-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Daytona Admin API
  slug: open-daytona-admin-api
- collection_type: open
  name: Daytona Api Keys API
  slug: open-daytona-api-keys-api
- collection_type: open
  name: Daytona Health API
  slug: open-daytona-health-api
- collection_type: open
  name: Daytona admin API
  slug: open-daytona-io-admin-api
- collection_type: open
  name: Daytona admin api-keys API
  slug: open-daytona-io-api-keys-api
- collection_type: open
  name: Daytona admin audit API
  slug: open-daytona-io-audit-api
- collection_type: open
  name: Daytona admin computer-use API
  slug: open-daytona-io-computer-use-api
- collection_type: open
  name: Daytona admin config API
  slug: open-daytona-io-config-api
- collection_type: open
  name: Daytona admin docker-registry API
  slug: open-daytona-io-docker-registry-api
- collection_type: open
  name: Daytona admin file-system API
  slug: open-daytona-io-file-system-api
- collection_type: open
  name: Daytona admin git API
  slug: open-daytona-io-git-api
- collection_type: open
  name: Daytona admin Health API
  slug: open-daytona-io-health-api
- collection_type: open
  name: Daytona admin info API
  slug: open-daytona-io-info-api
- collection_type: open
  name: Daytona admin interpreter API
  slug: open-daytona-io-interpreter-api
- collection_type: open
  name: Daytona admin jobs API
  slug: open-daytona-io-jobs-api
- collection_type: open
  name: Daytona admin lsp API
  slug: open-daytona-io-lsp-api
- collection_type: open
  name: Daytona admin object-storage API
  slug: open-daytona-io-object-storage-api
- collection_type: open
  name: Daytona admin organizations API
  slug: open-daytona-io-organizations-api
- collection_type: open
  name: Daytona admin port API
  slug: open-daytona-io-port-api
- collection_type: open
  name: Daytona admin process API
  slug: open-daytona-io-process-api
- collection_type: open
  name: Daytona admin regions API
  slug: open-daytona-io-regions-api
- collection_type: open
  name: Daytona admin runners API
  slug: open-daytona-io-runners-api
- collection_type: open
  name: Daytona admin sandbox API
  slug: open-daytona-io-sandbox-api
- collection_type: open
  name: Daytona admin server API
  slug: open-daytona-io-server-api
- collection_type: open
  name: Daytona admin snapshots API
  slug: open-daytona-io-snapshots-api
- collection_type: open
  name: Daytona admin toolbox API
  slug: open-daytona-io-toolbox-api
- collection_type: open
  name: Daytona admin users API
  slug: open-daytona-io-users-api
- collection_type: open
  name: Daytona admin volumes API
  slug: open-daytona-io-volumes-api
- collection_type: open
  name: Daytona admin webhooks API
  slug: open-daytona-io-webhooks-api
- collection_type: open
  name: Daytona admin workspace API
  slug: open-daytona-io-workspace-api
- collection_type: open
  name: Daytona Organizations API
  slug: open-daytona-organizations-api
- collection_type: open
  name: Daytona Sandbox API
  slug: open-daytona-sandbox-api
- collection_type: open
  name: Daytona Sandbox Toolbox API
  slug: open-daytona-sandbox-toolbox-api
- collection_type: open
  name: Daytona Snapshots API
  slug: open-daytona-snapshots-api
- collection_type: open
  name: Daytona Toolbox API
  slug: open-daytona-toolbox-api
- collection_type: open
  name: Daytona Users API
  slug: open-daytona-users-api
- collection_type: open
  name: Daytona Volumes API
  slug: open-daytona-volumes-api
- collection_type: open
  name: Daytona Webhooks API
  slug: open-daytona-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/daytona-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/daytona-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daytona-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/daytona-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/daytona/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-build-and-activate-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-capture-sandbox-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-fork-sandbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-image-to-running-sandbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-provision-sandbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-provision-volume-and-sandbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-restore-archived-sandbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/daytona-io-stop-and-archive-sandbox-workflow.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.daytona.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.daytona.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.daytona.io/docs/en/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://www.daytona.io/docs/en
- group: docs
  title: ''
  type: APIReference
  url: https://www.daytona.io/docs/en/tools/api/
- group: start
  title: ''
  type: Console
  url: https://app.daytona.io/
- group: start
  title: ''
  type: Signup
  url: https://app.daytona.io/
- group: start
  title: ''
  type: Login
  url: https://app.daytona.io/
- group: auth
  title: ''
  type: Authentication
  url: https://www.daytona.io/docs/en/account-management/api-keys
- group: operate
  title: ''
  type: RateLimits
  url: https://www.daytona.io/docs/en/account-management/limits
- group: other
  title: ''
  type: Regions
  url: https://www.daytona.io/docs/en/sandbox/regions
- group: company
  title: ''
  type: Blog
  url: https://www.daytona.io/dotfiles
- group: company
  title: ''
  type: Newsletter
  url: https://www.daytona.io/dotfiles
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@daytonaio
- group: operate
  title: ''
  type: Support
  url: https://go.daytona.io/slack
- group: operate
  title: ''
  type: Contact
  url: https://www.daytona.io/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.app.daytona.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.daytona.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daytona.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daytona.io/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.daytona.io/docs/en/security/security-exhibit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daytonaio
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/daytonaio/daytona
- group: other
  title: ''
  type: X
  url: https://twitter.com/daytonaio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/daytonaio/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/daytona/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@daytonaio/sdk
- group: build
  title: ''
  type: SDKs
  url: https://rubygems.org/gems/daytona
- group: build
  title: ''
  type: SDKs
  url: https://pkg.go.dev/github.com/daytonaio/daytona
- group: build
  title: ''
  type: SDKs
  url: https://central.sonatype.com/artifact/io.daytona/daytona-sdk
- group: build
  title: ''
  type: CLI
  url: https://www.daytona.io/docs/en/tools/cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/daytonaio/homebrew-cli
- group: other
  title: ''
  type: Resources
  url: https://github.com/daytonaio/helm-charts
- group: other
  title: ''
  type: Resources
  url: https://github.com/daytonaio/terraform-modules
- group: design
  title: ''
  type: SpectralRules
  url: rules/daytona-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/daytona-io-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/daytona-io-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/daytona-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/daytona-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/daytona-io-finops.yml
created: '2026-05-25'
description: Daytona is open-source, secure, and elastic infrastructure for running AI-generated code. Daytona sandboxes spin up in under 90 milliseconds and provide isolated Linux, Windows, and macOS environments where autonomous agents and developer workflows can execute untrusted code, perform file system and Git operations, run language servers, drive virtual desktops, and persist state via snapshots and volumes. The platform exposes a control-plane REST API (sandboxes, snapshots, volumes, organizations, runners, webhooks) and an in-sandbox Toolbox API (file system, Git, LSP, process execution, PTY, computer use, interpreter), with official SDKs for TypeScript, Python, Ruby, Go, and Java, plus a Go CLI and Homebrew/Windows installers.
examples:
- key_count: 8
  name: Daytona Sandbox Create Example
  slug: daytona-sandbox-create-example
- key_count: 13
  name: Daytona Sandbox Response Example
  slug: daytona-sandbox-response-example
- key_count: 3
  name: Daytona Snapshot Create Example
  slug: daytona-snapshot-create-example
- key_count: 3
  name: Daytona Toolbox Filesystem Write Example
  slug: daytona-toolbox-filesystem-write-example
- key_count: 3
  name: Daytona Toolbox Process Execute Example
  slug: daytona-toolbox-process-execute-example
- key_count: 3
  name: Daytona Volume Create Example
  slug: daytona-volume-create-example
- key_count: 2
  name: Daytona Webhook Create Example
  slug: daytona-webhook-create-example
features:
- description: Sandboxes boot in under 90 milliseconds, enabling per-request isolation for agents at scale.
  name: Sub-90ms cold start
- description: Spin up thousands of concurrent sandboxes for parallel agent runs, evaluation harnesses, and batch code execution.
  name: Massive parallelism
- description: Persist file system, process, and environment state via snapshots, and share data across sandboxes via volumes.
  name: Snapshots and volumes
- description: Programmatically drive Linux, Windows, and macOS GUI desktops via a built-in computer-use API for agent control.
  name: Computer Use desktops
- description: Native support for Python, TypeScript, Ruby, Go, and Java with built-in package management.
  name: Multi-language runtimes
- description: Language Server Protocol bridging and Git operations are first-class agent tools, not bolted-on shell calls.
  name: Built-in LSP and Git
- description: The Daytona platform is AGPL-3.0 open source and self-hostable on Kubernetes via official Helm charts.
  name: Open-source core
- description: Run the Daytona control plane against your own compute pools for data-residency and cost control.
  name: Customer-managed compute
- description: Humans can drop into any sandbox via SSH, web terminal, VNC, or VS Code Browser for debugging.
  name: SSH and VS Code Browser
- description: Subscribe to sandbox lifecycle events and emit OpenTelemetry traces for observability.
  name: Webhooks and OpenTelemetry
finops:
- name: Daytona Io Finops
  service_category: ''
  slug: daytona-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/daytona-io.png
integrations:
- description: Daytona is integrated as a code execution tool in the LangChain ecosystem.
  name: LangChain
- description: Daytona is supported as a sandbox host for Anthropic Claude Managed Agents.
  name: Anthropic Claude Managed Agents
- description: Daytona plugin for Google's Agent Development Kit enables ADK agents to run code in Daytona sandboxes.
  name: Google ADK
- description: Coding agent reference powered by Daytona using Inngest AgentKit.
  name: Inngest AgentKit
- description: Run Codex, Gemini CLI, and Claude Code in Daytona sandboxes via VibeKit.
  name: VibeKit
- description: Daytona sandboxes are available through Stripe Projects.
  name: Stripe Projects
- description: OpenHands open-source agent runtime uses Daytona for sandboxed code execution.
  name: OpenHands
- description: Sandboxed code execution backend for SWE-agent powered in part by Daytona.
  name: SWE-ReX
- description: Self-host the Daytona control plane on Kubernetes via official Helm charts.
  name: Kubernetes
- description: Provision Daytona infrastructure using official Terraform modules.
  name: Terraform
- description: Daytona exposes an MCP server so MCP-compatible agents and IDEs can invoke sandbox tools natively.
  name: MCP
- description: Connect to a running sandbox from VS Code via the VS Code Browser, SSH, or official extension.
  name: VS Code
- description: Connect to a running sandbox from JetBrains IDEs via the official JetBrains plugin.
  name: JetBrains
json_schemas:
- name: ApiKeyResponse
  property_count: 5
  slug: daytona-api-key
- name: Organization
  property_count: 25
  slug: daytona-organization
- name: Sandbox
  property_count: 33
  slug: daytona-sandbox
- name: SnapshotDto
  property_count: 20
  slug: daytona-snapshot
- name: User
  property_count: 5
  slug: daytona-user
- name: VolumeDto
  property_count: 8
  slug: daytona-volume
- name: WebhookEvent
  property_count: 0
  slug: daytona-webhook
json_structures:
- name: Daytona Api Key Structure
  property_count: 5
  slug: daytona-api-key-structure
- name: Daytona Organization Structure
  property_count: 25
  slug: daytona-organization-structure
- name: Daytona Sandbox Structure
  property_count: 33
  slug: daytona-sandbox-structure
- name: Daytona Snapshot Structure
  property_count: 20
  slug: daytona-snapshot-structure
- name: Daytona User Structure
  property_count: 5
  slug: daytona-user-structure
- name: Daytona Volume Structure
  property_count: 8
  slug: daytona-volume-structure
- name: Daytona Webhook Structure
  property_count: 0
  slug: daytona-webhook-structure
jsonld:
- class_count: 30
  name: Daytona Io Context
  property_count: 10
  slug: daytona-io-context
layout: provider
modified: '2026-05-25'
name: Daytona
nav: Providers
network: true
overview: 'Daytona publishes 28 APIs on the [APIs.io](https://apis.io/) network, including admin API, api-keys API, audit API, and 25 more. Tagged areas include AI, Agents, Artificial Intelligence, Cloud, and Code Execution.


  The Daytona catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Daytona''s developer surface includes authentication, documentation, getting-started guide, API reference, developer console, signup flow, engineering blog, and 46 more developer resources.'
plans:
- name: Daytona Io Plans Pricing
  plan_count: 4
  slug: daytona-io-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 0
  name: Daytona Io Rate Limits
  slug: daytona-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Daytona API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: daytona-io-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Daytona API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: daytona-rules
score:
  band: strong
  composite: 65.2
  delta: -4.4
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 25.0
    contract_quality: 65.2
    developer_ergonomics: 92.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 31.6
  previous_composite: 69.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daytona-io/refs/heads/main/screenshots/daytona-io-2026-06-20T175734.png
security:
- kind: authentication
  name: Daytona Io Authentication
  slug: daytona-io-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Daytona Io Domain Security
  slug: daytona-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Daytona Io Trust Center
  slug: daytona-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: daytona-io
solutions:
- description: Fully managed sandbox infrastructure at app.daytona.io with pay-as-you-go pricing and $200 free credit.
  name: Daytona Cloud
- description: Run Daytona's managed control plane against your own VPC/Kubernetes compute for residency and cost control.
  name: Customer-Managed Compute
- description: Deploy the full Daytona platform on your own Kubernetes via Helm for fully air-gapped deployments.
  name: Self-Hosted Open Source
- description: Up to $50k in free Daytona compute credits for qualifying startups building agent infrastructure.
  name: Startups Program
tags:
- AI
- Agents
- Artificial Intelligence
- Cloud
- Code Execution
- Computer Use
- Developer Tools
- Infrastructure
- Open Source
- Sandbox
- Secure Execution
use_cases:
- description: Give every agent its own isolated computer to run, test, and iterate on generated code safely.
  name: AI coding agents
- description: Back chatbot code-execution features (Python interpreter, data analysis, plotting) with disposable sandboxes.
  name: Code interpreter for LLM apps
- description: Drive headless and headed Linux/Windows/macOS desktops for browser automation and GUI-driven workflows.
  name: Computer-use agents
- description: Run SWE-bench-style benchmarks and agent evaluations in massively parallel sandboxes with reproducible state.
  name: Evaluation harnesses
- description: Execute untrusted PRs from autonomous agents in isolated environments without risking host infrastructure.
  name: CI for AI-generated code
- description: Provide cloud dev environments for engineers with persistent volumes, snapshots, and SSH/VS Code access.
  name: Hosted developer environments
- description: Run user-uploaded notebooks and scripts safely with built-in Python and TypeScript interpreters.
  name: Sandboxed data analysis
website: https://www.daytona.io/
---
