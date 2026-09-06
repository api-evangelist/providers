---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 81
  human_in_the_loop: 15
  name: Kernel Agentic Access
  operation_count: 135
  slug: kernel-agentic-access
  summary_line: 135 operations · 81 acting · 15 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage API keys for organization and project-scoped access.
  name: Kernel API Keys API
  slug: kernel-api-keys-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: List applications and versions.
  name: Kernel Apps API
  slug: kernel-apps-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Read audit log records for the authenticated organization.
  name: Kernel Audit Logs API
  slug: kernel-audit-logs-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Control mouse, keyboard, and screen on the browser instance.
  name: Kernel Browser Computer Controls API
  slug: kernel-browser-computer-controls-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Read, write, and manage files on the browser instance.
  name: Kernel Browser Filesystem API
  slug: kernel-browser-filesystem-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Stream logs from the browser instance.
  name: Kernel Browser Logs API
  slug: kernel-browser-logs-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Execute Playwright code against the browser instance.
  name: Kernel Browser Playwright API
  slug: kernel-browser-playwright-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage browser pools for acquiring and releasing browsers.
  name: Kernel Browser Pools API
  slug: kernel-browser-pools-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Execute and manage processes on the browser instance.
  name: Kernel Browser Processes API
  slug: kernel-browser-processes-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Record and manage browser session video replays.
  name: Kernel Browser Replays API
  slug: kernel-browser-replays-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Stream live telemetry events from a browser session.
  name: Kernel Browser Telemetry API
  slug: kernel-browser-telemetry-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage browser sessions.
  name: Kernel Browsers API
  slug: kernel-browsers-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Configure external credential providers like 1Password.
  name: Kernel Credential Providers API
  slug: kernel-credential-providers-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage credentials for authentication.
  name: Kernel Credentials API
  slug: kernel-credentials-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage app deployments and stream deployment events.
  name: Kernel Deployments API
  slug: kernel-deployments-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create, list, retrieve, and delete browser extensions.
  name: Kernel Extensions API
  slug: kernel-extensions-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Invoke actions and stream or query invocation status and events.
  name: Kernel Invocations API
  slug: kernel-invocations-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage auth connections for automated credential capture and login.
  name: Kernel Managed Auth API
  slug: kernel-managed-auth-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Read and manage organization-level limits.
  name: Kernel Organization API
  slug: kernel-organization-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create, list, retrieve, and delete browser profiles.
  name: Kernel Profiles API
  slug: kernel-profiles-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage projects for resource isolation within an organization.
  name: Kernel Projects API
  slug: kernel-projects-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Create and manage proxy configurations for routing browser traffic.
  name: Kernel Proxies API
  slug: kernel-proxies-api
arazzos:
- description: End-to-end cloud browser automation on Kernel.
  name: Kernel - create a browser, run Playwright, screenshot, tear down
  slug: kernel-browser-automate
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kernel API Keys API
  slug: open-kernel-api-keys-api
- collection_type: open
  name: Kernel API Keys Apps API
  slug: open-kernel-apps-api
- collection_type: open
  name: Kernel API Keys Audit Logs API
  slug: open-kernel-audit-logs-api
- collection_type: open
  name: Kernel API Keys Browser Computer Controls API
  slug: open-kernel-browser-computer-controls-api
- collection_type: open
  name: Kernel API Keys Browser Filesystem API
  slug: open-kernel-browser-filesystem-api
- collection_type: open
  name: Kernel API Keys Browser Logs API
  slug: open-kernel-browser-logs-api
- collection_type: open
  name: Kernel API Keys Browser Playwright API
  slug: open-kernel-browser-playwright-api
- collection_type: open
  name: Kernel API Keys Browser Pools API
  slug: open-kernel-browser-pools-api
- collection_type: open
  name: Kernel API Keys Browser Processes API
  slug: open-kernel-browser-processes-api
- collection_type: open
  name: Kernel API Keys Browser Replays API
  slug: open-kernel-browser-replays-api
- collection_type: open
  name: Kernel API Keys Browser Telemetry API
  slug: open-kernel-browser-telemetry-api
- collection_type: open
  name: Kernel API Keys Browsers API
  slug: open-kernel-browsers-api
- collection_type: open
  name: Kernel API Keys Credential Providers API
  slug: open-kernel-credential-providers-api
- collection_type: open
  name: Kernel API Keys Credentials API
  slug: open-kernel-credentials-api
- collection_type: open
  name: Kernel API Keys Deployments API
  slug: open-kernel-deployments-api
- collection_type: open
  name: Kernel API Keys Extensions API
  slug: open-kernel-extensions-api
- collection_type: open
  name: Kernel API Keys Invocations API
  slug: open-kernel-invocations-api
- collection_type: open
  name: Kernel API Keys Managed Auth API
  slug: open-kernel-managed-auth-api
- collection_type: open
  name: Kernel API Keys Organization API
  slug: open-kernel-organization-api
- collection_type: open
  name: Kernel API Keys Profiles API
  slug: open-kernel-profiles-api
- collection_type: open
  name: Kernel API Keys Projects API
  slug: open-kernel-projects-api
- collection_type: open
  name: Kernel API Keys Proxies API
  slug: open-kernel-proxies-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kernel-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kernel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kernel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kernel-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/kernel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kernel-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kernel-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kernel-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kernel-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kernel-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kernel-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kernel-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kernel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kernel-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/kernel-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kernel-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kernel-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kernel-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kernel-browser-automate.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kernel.sh
- group: auth
  title: ''
  type: Compliance
  url: https://www.kernel.sh/security
- group: company
  title: ''
  type: Website
  url: https://www.kernel.sh
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kernel.sh/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://kernel.sh/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://kernel.sh/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://kernel.sh/docs/introduction/
- group: operate
  title: ''
  type: Support
  url: https://kernel.sh/docs/info/support
- group: company
  title: ''
  type: Blog
  url: https://www.kernel.sh/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kernel
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kernel.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.onkernel.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kernel.sh
created: '2026-07-17'
description: Kernel is browser infrastructure for AI agents and automations. It runs sandboxed cloud Chromium browsers that spin up in under 30ms, with Playwright execution, computer-use controls, managed authentication into third-party sites, reusable browser profiles, proxies, pre-warmed browser pools, session replays, live telemetry, and a serverless App platform for deploying and invoking agent actions. Kernel exposes a REST API (OpenAPI 3.1, 135 operations across 22 tags), first-party TypeScript, Python and Go SDKs, a CLI, and a centrally hosted MCP server so agents can drive real browsers. Backed by General Catalyst.
image: https://www.kernel.sh/favicon.ico
layout: provider
mcp_servers:
- description: Centrally hosted, authenticated remote MCP server that lets any MCP-compatible model or agent launch Chromium browsers, execute Playwright code, capture video replays, manage profiles/proxies/pools, a
  name: Kernel MCP Server
  slug: kernel-mcp-server
modified: '2026-07-19'
name: Kernel
nav: Providers
network: true
overview: 'Kernel publishes 22 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, Audit Logs API, and 19 more. Tagged areas include Company, Browser Automation, Web Agents, Browser Infrastructure, and AI Agents.


  Kernel''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, support, and 26 more developer resources.'
random_paper: 11
scopes:
- name: Kernel Scopes
  scope_count: 2
  slug: kernel-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 58.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kernel/refs/heads/main/screenshots/kernel-2026-07-25T223632.png
security:
- kind: authentication
  name: Kernel Authentication
  slug: kernel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kernel Domain Security
  slug: kernel-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Kernel Trust Center
  slug: kernel-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, PCI, GDPR
slug: kernel
tags:
- Company
- Browser Automation
- Web Agents
- Browser Infrastructure
- AI Agents
- Playwright
- Cloud Browsers
- Computer Use
- MCP
- Managed Auth
website: https://www.kernel.sh
---
