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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Socket Dev Agentic Access
  operation_count: 81
  slug: socket-dev-agentic-access
  summary_line: 81 operations · 41 acting · 1 human-in-the-loop
api_count: 19
apis:
- description: The alerts API from Socket — 4 operation(s) for alerts.
  name: Socket alerts API
  slug: socket-dev-alerts-api
- description: The api-tokens API from Socket — 6 operation(s) for api-tokens.
  name: Socket api-tokens API
  slug: socket-dev-api-tokens-api
- description: The audit-log API from Socket — 1 operation(s) for audit-log.
  name: Socket audit-log API
  slug: socket-dev-audit-log-api
- description: The dependencies API from Socket — 2 operation(s) for dependencies.
  name: Socket dependencies API
  slug: socket-dev-dependencies-api
- description: The diff-scans API from Socket — 7 operation(s) for diff-scans.
  name: Socket diff-scans API
  slug: socket-dev-diff-scans-api
- description: The fixes API from Socket — 1 operation(s) for fixes.
  name: Socket fixes API
  slug: socket-dev-fixes-api
- description: The full-scans API from Socket — 13 operation(s) for full-scans.
  name: Socket full-scans API
  slug: socket-dev-full-scans-api
- description: The license-policy API from Socket — 4 operation(s) for license-policy.
  name: Socket license-policy API
  slug: socket-dev-license-policy-api
- description: The metadata API from Socket — 5 operation(s) for metadata.
  name: Socket metadata API
  slug: socket-dev-metadata-api
- description: The org-settings API from Socket — 2 operation(s) for org-settings.
  name: Socket org-settings API
  slug: socket-dev-org-settings-api
- description: The org-snapshots API from Socket — 1 operation(s) for org-snapshots.
  name: Socket org-snapshots API
  slug: socket-dev-org-snapshots-api
- description: The packages API from Socket — 2 operation(s) for packages.
  name: Socket packages API
  slug: socket-dev-packages-api
- description: The repo-labels API from Socket — 5 operation(s) for repo-labels.
  name: Socket repo-labels API
  slug: socket-dev-repo-labels-api
- description: The repos API from Socket — 2 operation(s) for repos.
  name: Socket repos API
  slug: socket-dev-repos-api
- description: The security-policy API from Socket — 1 operation(s) for security-policy.
  name: Socket security-policy API
  slug: socket-dev-security-policy-api
- description: The telemetry API from Socket — 1 operation(s) for telemetry.
  name: Socket telemetry API
  slug: socket-dev-telemetry-api
- description: The threat-feed API from Socket — 1 operation(s) for threat-feed.
  name: Socket threat-feed API
  slug: socket-dev-threat-feed-api
- description: The triage API from Socket — 2 operation(s) for triage.
  name: Socket triage API
  slug: socket-dev-triage-api
- description: The webhooks API from Socket — 2 operation(s) for webhooks.
  name: Socket webhooks API
  slug: socket-dev-webhooks-api
arazzos:
- description: Search the organization's in-use dependencies by PURL, then pull alert metadata for those same packages.
  name: Socket Audit Organization Dependencies
  slug: socket-dev-audit-dependencies-workflow
- description: Ensure a repository exists, create a full scan from manifest files, poll until it finishes, then export the alert CSV.
  name: Socket Create and Report a Full Scan
  slug: socket-dev-create-and-report-full-scan-workflow
- description: List the two most recent full scans for a repository and create a diff scan comparing them, then poll the diff until ready.
  name: Socket Diff Two Full Scans by ID
  slug: socket-dev-diff-from-scan-ids-workflow
- description: Confirm a repository, create a diff scan against its current HEAD full scan, then poll the diff until cached results are ready.
  name: Socket Diff a Repository Against Its HEAD Scan
  slug: socket-dev-diff-repo-head-workflow
- description: Confirm a repository and its HEAD scan, then fetch the available fixes for its vulnerabilities.
  name: Socket Fix Vulnerabilities in a Repository
  slug: socket-dev-fix-repo-vulnerabilities-workflow
- description: Pick the latest alert, find the full scans it appears in, then read the metadata of one of those scans.
  name: Socket Investigate Alert Across Scans
  slug: socket-dev-investigate-alert-scans-workflow
- description: Find the most recent full scan for a repository, confirm its metadata, then generate a PDF report.
  name: Socket Generate PDF Report for Latest Scan
  slug: socket-dev-latest-scan-pdf-report-workflow
- description: Look up alert metadata for a batch of packages by PURL, then fetch available fixes for the discovered vulnerabilities.
  name: Socket Package Issues and Available Fixes
  slug: socket-dev-package-issues-and-fixes-workflow
- description: Create a full scan and poll its metadata until the scan_state leaves the processing states.
  name: Socket Poll Full Scan to Completion
  slug: socket-dev-poll-full-scan-completion-workflow
- description: Create an organization webhook for selected events, then read it back to confirm it was registered.
  name: Socket Provision and Verify a Webhook
  slug: socket-dev-provision-webhook-workflow
- description: Rescan an existing full scan to apply the latest policies, poll the new scan to completion, then export its alert CSV.
  name: Socket Rescan and Report a Full Scan
  slug: socket-dev-rescan-and-report-workflow
- description: Read the organization's current security policy, then write back an updated default level and rule set.
  name: Socket Review and Update Org Security Policy
  slug: socket-dev-review-update-security-policy-workflow
- description: Start an on-demand historical data snapshot job, then poll the snapshot list until the job's request id appears.
  name: Socket Start and Poll Historical Snapshot
  slug: socket-dev-snapshot-and-list-workflow
- description: List the latest organization alerts and, when any are present, apply a triage state to one of them.
  name: Socket Triage Latest Alerts
  slug: socket-dev-triage-latest-alerts-workflow
artifact_total: 123
collections:
- collection_type: postman
  name: Socket Alerts API
  slug: postman-socket-alerts-api
- collection_type: postman
  name: Socket Api Tokens API
  slug: postman-socket-api-tokens-api
- collection_type: postman
  name: Socket Audit Log API
  slug: postman-socket-audit-log-api
- collection_type: postman
  name: Socket Dependencies API
  slug: postman-socket-dependencies-api
- collection_type: postman
  name: Socket Diff Scans API
  slug: postman-socket-diff-scans-api
- collection_type: postman
  name: Socket Fixes API
  slug: postman-socket-fixes-api
- collection_type: postman
  name: Socket Full Scans API
  slug: postman-socket-full-scans-api
- collection_type: postman
  name: Socket Metadata API
  slug: postman-socket-metadata-api
- collection_type: postman
  name: Socket Org Settings API
  slug: postman-socket-org-settings-api
- collection_type: postman
  name: Socket Org Snapshots API
  slug: postman-socket-org-snapshots-api
- collection_type: postman
  name: Socket Packages API
  slug: postman-socket-packages-api
- collection_type: postman
  name: Socket Repos API
  slug: postman-socket-repos-api
- collection_type: postman
  name: Socket Threat Feed API
  slug: postman-socket-threat-feed-api
- collection_type: postman
  name: Socket Triage API
  slug: postman-socket-triage-api
- collection_type: postman
  name: Socket Webhooks API
  slug: postman-socket-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Socket Alerts API
  slug: open-socket-alerts-api
- collection_type: open
  name: Socket Api Tokens API
  slug: open-socket-api-tokens-api
- collection_type: open
  name: Socket Audit Log API
  slug: open-socket-audit-log-api
- collection_type: open
  name: Socket Dependencies API
  slug: open-socket-dependencies-api
- collection_type: open
  name: Socket alerts API
  slug: open-socket-dev-alerts-api
- collection_type: open
  name: Socket alerts api-tokens API
  slug: open-socket-dev-api-tokens-api
- collection_type: open
  name: Socket alerts audit-log API
  slug: open-socket-dev-audit-log-api
- collection_type: open
  name: Socket alerts dependencies API
  slug: open-socket-dev-dependencies-api
- collection_type: open
  name: Socket alerts diff-scans API
  slug: open-socket-dev-diff-scans-api
- collection_type: open
  name: Socket alerts fixes API
  slug: open-socket-dev-fixes-api
- collection_type: open
  name: Socket alerts full-scans API
  slug: open-socket-dev-full-scans-api
- collection_type: open
  name: Socket alerts license-policy API
  slug: open-socket-dev-license-policy-api
- collection_type: open
  name: Socket alerts metadata API
  slug: open-socket-dev-metadata-api
- collection_type: open
  name: Socket alerts org-settings API
  slug: open-socket-dev-org-settings-api
- collection_type: open
  name: Socket alerts org-snapshots API
  slug: open-socket-dev-org-snapshots-api
- collection_type: open
  name: Socket alerts packages API
  slug: open-socket-dev-packages-api
- collection_type: open
  name: Socket alerts repo-labels API
  slug: open-socket-dev-repo-labels-api
- collection_type: open
  name: Socket alerts repos API
  slug: open-socket-dev-repos-api
- collection_type: open
  name: Socket alerts security-policy API
  slug: open-socket-dev-security-policy-api
- collection_type: open
  name: Socket alerts telemetry API
  slug: open-socket-dev-telemetry-api
- collection_type: open
  name: Socket alerts threat-feed API
  slug: open-socket-dev-threat-feed-api
- collection_type: open
  name: Socket alerts triage API
  slug: open-socket-dev-triage-api
- collection_type: open
  name: Socket alerts webhooks API
  slug: open-socket-dev-webhooks-api
- collection_type: open
  name: Socket Diff Scans API
  slug: open-socket-diff-scans-api
- collection_type: open
  name: Socket Fixes API
  slug: open-socket-fixes-api
- collection_type: open
  name: Socket Full Scans API
  slug: open-socket-full-scans-api
- collection_type: open
  name: Socket Metadata API
  slug: open-socket-metadata-api
- collection_type: open
  name: Socket Org Settings API
  slug: open-socket-org-settings-api
- collection_type: open
  name: Socket Org Snapshots API
  slug: open-socket-org-snapshots-api
- collection_type: open
  name: Socket Packages API
  slug: open-socket-packages-api
- collection_type: open
  name: Socket Repos API
  slug: open-socket-repos-api
- collection_type: open
  name: Socket Threat Feed API
  slug: open-socket-threat-feed-api
- collection_type: open
  name: Socket Triage API
  slug: open-socket-triage-api
- collection_type: open
  name: Socket Webhooks API
  slug: open-socket-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/socket-dev-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/socket-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socket-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/socket-dev-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/socket/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-audit-dependencies-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-create-and-report-full-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-diff-from-scan-ids-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-diff-repo-head-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-fix-repo-vulnerabilities-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-investigate-alert-scans-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-latest-scan-pdf-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-package-issues-and-fixes-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-poll-full-scan-completion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-provision-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-rescan-and-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-review-update-security-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-snapshot-and-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/socket-dev-triage-latest-alerts-workflow.yml
- group: build
  title: ''
  type: Packages
  url: packages/socket-dev-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/socket-dev-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socket-dev-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/socket-dev-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/socket-dev-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/socket-dev-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/socket-dev-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/socket-dev-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/socket-dev-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/socket-dev-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/socket-dev-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/socket-dev-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/socket-dev-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/socket-dev-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-alerts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-api-tokens-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-audit-log-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-dependencies-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-diff-scans-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-fixes-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-full-scans-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-metadata-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-org-settings-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-org-snapshots-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-packages-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-repos-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-threat-feed-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-triage-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/socket-dev-socket-webhooks-api-overlay.yaml
- group: start
  title: ''
  type: Portal
  url: https://socket.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socket.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socket.dev/reference/introduction-to-socket-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socket.dev/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.socket.dev/reference/authentication-types
- group: start
  title: ''
  type: Signup
  url: https://socket.dev/login
- group: company
  title: ''
  type: Blog
  url: https://socket.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://socket.dev/blog/categories/product-updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socket.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://socket.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socket.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socket.dev/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://socket.dev/legal/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SocketDev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/socket-security
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SocketSecurity
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SocketDev/socket-sdk-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SocketDev/socket-sdk-python
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-python-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/sfw-free
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-vscode
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/action
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-basics
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-patch
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-siem-connector
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/bun-security-scanner
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-registry
- group: build
  title: ''
  type: Tools
  url: https://github.com/SocketDev/socket-config-js
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.socket.dev/v0/openapi
- group: commercial
  title: ''
  type: Plans
  url: plans/socket-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/socket-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/socket-dev-finops.yml
created: '2026-05-25'
description: Socket is a developer-first supply-chain security platform that protects applications from malicious dependencies, vulnerable packages, license risk, and software-supply-chain attacks across npm, PyPI, Go, Maven, Cargo, NuGet, RubyGems, and other open-source ecosystems. Socket ships a hosted API, CLI, MCP server, Firewall package-installer proxy (sfw), GitHub App, IDE extensions, SDKs, and reusable integrations for Jira, Slack, GitHub, GitLab, Bitbucket, Azure DevOps, and Microsoft Teams. The Socket API exposes 70+ alert categories — malware, typo- squats, install scripts, telemetry, native code, crypto wallets, suspicious network activity, license issues — plus full-scan reports with SBOM export (CycloneDX, SPDX, OpenVEX), diff scans for pull requests, a triage workflow, webhooks, and a real-time threat feed of newly discovered malicious packages.
examples:
- key_count: 2
  name: Socket Create Full Scan Example
  slug: socket-create-full-scan-example
- key_count: 2
  name: Socket Purl Batch Example
  slug: socket-purl-batch-example
- key_count: 2
  name: Socket Threat Feed Example
  slug: socket-threat-feed-example
- key_count: 2
  name: Socket Triage Update Example
  slug: socket-triage-update-example
features:
- Socket API — supply-chain risk data via Package URL (purl) across npm, PyPI, Go, Maven, Cargo, NuGet, RubyGems, and others
- Full Scans — repository-wide dependency graph and alert reports with SBOM export (CycloneDX, SPDX, OpenVEX, CSV, PDF)
- Diff Scans — pull-request-aware comparison between two full scans, output as JSON or GFM markdown comment
- Triage workflow — list and update disposition (ignore, acknowledge, escalate, allow) for alerts at scale
- Historical alerts, dependencies, and snapshots — long-window trend analytics for posture reporting
- Threat Feed — real-time discovery of malicious and suspicious packages across ecosystems
- Fixes — version bumps, patches, and overrides for vulnerable dependencies, including auto-PR generation
- 70+ alert categories — malware, typosquats, install scripts, telemetry, native code, crypto wallets, supply-chain risks
- Security and license policies per organization with per-repo label overrides
- Webhooks for scan completion, alert generation, triage events, and threat-feed matches
- Socket Firewall — registry proxy and `sfw` runtime that prevents installation of malicious packages
- Socket CLI (JavaScript + Python) for scanning, fixing, and config validation
- Socket MCP Server — Model Context Protocol server exposing Socket data to AI agents
- Socket Optimize — drop-in package overrides for npm/pnpm/yarn that replace vulnerable transitive dependencies
- Socket Basics — bundled SAST + Secrets + Container scanning for organizations standardizing on a single tool
- Socket VS Code extension and Socket GitHub Action for in-editor and in-CI security gates
- GitHub, GitLab, Bitbucket, Azure DevOps, Jira, Slack, and Microsoft Teams integrations
- SDKs for JavaScript / TypeScript (`@socketsecurity/sdk`) and Python
- Append-only audit log of every administrative action for compliance evidence
- Live OpenAPI spec served from https://api.socket.dev/v0/openapi
finops:
- name: Socket Dev Finops
  service_category: Security
  slug: socket-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/socket-dev.png
json_schemas:
- name: SocketAlert
  property_count: 15
  slug: socket-alert
- name: SocketFullScanArtifact
  property_count: 0
  slug: socket-full-scan
- name: SocketPURL
  property_count: 6
  slug: socket-package
jsonld:
- class_count: 0
  name: Socket Context
  property_count: 10
  slug: socket-context
layout: provider
mcp_servers:
- description: ''
  name: socket-dev-mcp.yml
  slug: socket-dev-mcpyml
modified: '2026-06-20'
name: Socket
nav: Providers
network: true
overview: 'Socket publishes 19 APIs on the [APIs.io](https://apis.io/) network, including alerts API, api-tokens API, audit-log API, and 16 more. Tagged areas include Supply Chain Security, Open Source Security, Software Composition Analysis, SCA, and Malware Detection.


  The Socket catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Socket''s developer surface includes authentication, changelog, CLI, developer portal, documentation, getting-started guide, signup flow, and 75 more developer resources.'
plans:
- name: Socket Dev Plans Pricing
  plan_count: 3
  slug: socket-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Socket Dev Rate Limits
  slug: socket-dev-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Socket API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: socket-dev-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Socket API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 3
    info: 0
    warn: 7
  slug: socket-dev-rules
scopes:
- name: Socket Dev Scopes
  scope_count: 97
  slug: socket-dev-scopes
  summary_line: 97 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.5
  delta: -18.3
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 26.5
    contract_quality: 67.6
    developer_ergonomics: 47.6
    discoverability: 77.8
    governance: 26.5
    operational_transparency: 50.0
  previous_composite: 74.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/socket-dev/refs/heads/main/screenshots/socket-dev-2026-06-20T194122.png
security:
- kind: authentication
  name: Socket Dev Authentication
  slug: socket-dev-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Socket Dev Domain Security
  slug: socket-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Socket Dev Vulnerability Disclosure
  slug: socket-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Socket Dev Trust Center
  slug: socket-dev-trust-center
  summary_line: SOC 2 Type I
slug: socket-dev
tags:
- Supply Chain Security
- Open Source Security
- Software Composition Analysis
- SCA
- Malware Detection
- Dependency Scanning
- SBOM
- npm
- PyPI
- Go
- Maven
- Cargo
- NuGet
- RubyGems
- Developer Security
website: https://socket.dev/
---
