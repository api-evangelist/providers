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
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 80
  human_in_the_loop: 14
  name: Kernel Agentic Access
  operation_count: 135
  slug: kernel-agentic-access
  summary_line: 135 operations · 80 acting · 14 human-in-the-loop
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
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Inspect the identity and authorization context for the current request.
  name: Kernel Authentication API
  slug: kernel-authentication-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Execute JavaScript in the browser instance's persistent Browser REPL.
  name: Kernel Browser REPL API
  slug: kernel-browser-repl-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Discover and invoke native page tools across the browser instance.
  name: Kernel Browser WebMCP API
  slug: kernel-browser-webmcp-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Resolve browser and proxy recommendations for bot-protected sites.
  name: Kernel Config Registry API
  slug: kernel-config-registry-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: Search the web and retrieve content for selected results.
  name: Kernel Search API
  slug: kernel-search-api
- baseURL: https://api.onkernel.com
  baseurl_source: declared
  description: The Vaults API from Kernel — 9 operation(s) for vaults.
  name: Kernel Vaults API
  slug: kernel-vaults-api
arazzos:
- description: End-to-end cloud browser automation on Kernel.
  name: Kernel - create a browser, run Playwright, screenshot, tear down
  slug: kernel-browser-automate
artifact_total: 64
collections:
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
- group: commercial
  href: https://artifacts.apis.io/kernel/plans/kernel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kernel-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/kernel/capabilities/kernel-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kernel-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/kernel/overlays/kernel-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kernel-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/kernel/agentic-access/kernel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kernel-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kernel/security/kernel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kernel-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kernel/authentication/kernel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kernel-authentication.yml
- group: build
  href: https://artifacts.apis.io/kernel/packages/kernel-packages.yml
  title: ''
  type: Packages
  url: packages/kernel-packages.yml
- group: build
  href: https://artifacts.apis.io/kernel/packages/kernel-packages.yml
  title: ''
  type: SDKs
  url: packages/kernel-packages.yml
- group: build
  href: https://artifacts.apis.io/kernel/cli/kernel-cli.yml
  title: ''
  type: CLI
  url: cli/kernel-cli.yml
- group: agent
  href: https://artifacts.apis.io/kernel/mcp/kernel-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kernel-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kernel/well-known/kernel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kernel-well-known.yml
- group: auth
  href: https://artifacts.apis.io/kernel/scopes/kernel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/kernel-scopes.yml
- group: design
  href: https://artifacts.apis.io/kernel/conventions/kernel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kernel-conventions.yml
- group: design
  href: https://artifacts.apis.io/kernel/conformance/kernel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kernel-conformance.yml
- group: design
  href: https://artifacts.apis.io/kernel/errors/kernel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kernel-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kernel/lifecycle/kernel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kernel-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/kernel/lifecycle/kernel-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/kernel-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kernel/data-model/kernel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kernel-data-model.yml
- group: operate
  href: https://artifacts.apis.io/kernel/changelog/kernel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kernel-changelog.yml
- group: agent
  href: https://artifacts.apis.io/kernel/llms/kernel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kernel-llms.txt
- group: agent
  href: https://artifacts.apis.io/kernel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kernel/arazzo/kernel-browser-automate.yml
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
finops:
- has_sources: true
  method: derived
  name: Kernel Finops
  primary_unit: subscription
  service_category: ''
  slug: kernel-finops
  template: false
image: https://www.kernel.sh/favicon.ico
layout: provider
mcp_servers:
- description: Centrally hosted, authenticated remote MCP server that lets any MCP-compatible model or agent launch Chromium browsers, execute Playwright code, capture video replays, manage profiles/proxies/pools, a
  name: Kernel MCP Server
  slug: kernel
modified: '2026-07-19'
name: Kernel
nav: Providers
network: true
overview: 'Kernel publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, Audit Logs API, and 25 more. Tagged areas include Company, Browser Automation, Web Agents, Browser Infrastructure, and AI Agents.


  Kernel''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Kernel Plans Pricing
  plan_count: 4
  slug: kernel-plans-pricing
- name: Kernel Price Estimates
  plan_count: 0
  slug: kernel-price-estimates
random_paper: 17
scopes:
- name: Kernel Scopes
  scope_count: 2
  slug: kernel-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 51.1
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kernel/kernel-2026-07-25T223632.png
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
skill_count: 4
skills:
- name: Acquire and release browsers from a pre-warmed pool
  slug: kernel-browser-pool
- name: Create a cloud browser and automate it with Playwright
  slug: kernel-create-browser-and-automate
- name: Deploy a Kernel app and invoke an action
  slug: kernel-deploy-and-invoke-app
- name: Log a browser into a site with Managed Auth
  slug: kernel-managed-auth-login
slug: kernel
tags:
- Company
- Browser Automation
- Web Agents
- Browser Infrastructure
- AI Agents
- Playwright
- Cloud Browser
- Computer Use
- MCP
- Managed Auth
website: https://www.kernel.sh
---
