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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 53
  human_in_the_loop: 10
  name: Browser Use Agentic Access
  operation_count: 103
  slug: browser-use-agentic-access
  summary_line: 103 operations · 53 acting · 10 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The current Browser Use Cloud REST API for long-horizon agent runs — create and monitor runs, continue conversations in sessions with a message queue, persist files in workspaces, launch and stop stea
  name: Browser Use Public API v4
  slug: browser-use-api-v4
- baseURL: https://api.browser-use.com/api/v3
  baseurl_source: declared
  description: The session-based Browser Use Cloud REST API — agent sessions with streamed messages, standalone CDP browsers, persistent workspaces and files, browser profiles, billing account balance, and an x402 m
  name: Browser Use Public API v3
  slug: browser-use-api-v3
- baseURL: https://api.browser-use.com/api/v2
  baseurl_source: declared
  description: The step-priced Browser Use Cloud REST API — tasks and task logs, sessions with public share links, presigned file upload/download URLs, browser profiles, standalone browsers, and the Skills surface t
  name: Browser Use Public API v2
  slug: browser-use-api-v2
- description: Browser Use's hosted remote Model Context Protocol server. An anonymous tools/list returns six real tools — browser_task, monitor_task, list_skills, execute_skill, get_cookies and list_browser_profile
  name: Browser Use MCP Server
  slug: browser-use-mcp
artifact_total: 14
asyncapis:
- description: ''
  name: Browser Use Webhooks
  slug: browser-use-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://browser-use.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://browser-use.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.browser-use.com
- group: docs
  title: ''
  type: APIReference
  url: https://browser-use.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.browser-use.com/cloud/quickstart
- group: operate
  title: ''
  type: Support
  url: https://link.browser-use.com/discord
- group: company
  title: ''
  type: Blog
  url: https://browser-use.com/posts
- group: company
  title: ''
  type: BlogRSS
  url: https://browser-use.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/browser-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/browser-use
- group: commercial
  title: ''
  type: Pricing
  url: https://browser-use.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.browser-use.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://browser-use.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://browser-use.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.browser-use.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/browser-use-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/browser-use-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/browser-use-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/browser-use-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/browser-use-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/browser-use-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/browser-use-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/browser-use-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/browser-use-cli.yml
- group: design
  title: ''
  type: Components
  url: components/browser-use-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/browser-use-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/browser-use-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/browser-use-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/browser-use-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/browser-use-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/browser-use-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/browser-use-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/browser-use-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/browser-use-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/browser-use-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/browser-use-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/browser-use-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/browser-use-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/browser-use-domain-security.yml
created: '2026-03-27'
description: Browser Use makes websites accessible to AI agents. It ships two commercial products on one managed browser platform — Browser Use Agents, which take a natural-language goal and return completed web work, and Browser Infrastructure, which rents stealth cloud Chromium browsers over SDK, REST, or CDP to automation you already own. The public Cloud API is versioned (v4 for long-horizon agent runs, v3 for sessions and workspaces, v2 for low-cost step-based tasks), authenticates with an X-Browser-Use-API-Key header, and is complemented by an OAuth-protected remote MCP server, signed webhooks, an A2A agent card, a published agent skill, first-party Python and TypeScript SDKs, and a CLI. The open-source browser-use Python library is a separate developer tool with its own API.
finops:
- name: Browser Use Finops
  service_category: API
  slug: browser-use-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/browser-use.png
layout: provider
mcp_servers:
- description: ''
  name: Browser Use MCP Server
  slug: browser-use-mcp-server
modified: '2026-08-29'
name: Browser Use
nav: Providers
network: true
overview: 'Browser Use publishes 3 APIs on the [APIs.io](https://apis.io/) network: Public API v4, Public API v3, and Public API v2. Tagged areas include AI Automation, Browser Automation, Web Agents, Web Scraping, and Headless Browsers.


  The Browser Use catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Browser Use''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Browser Use Plans Pricing
  plan_count: 6
  slug: browser-use-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 7
  name: Browser Use Rate Limits
  slug: browser-use-rate-limits
scopes:
- name: Browser Use Scopes
  scope_count: 0
  slug: browser-use-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.8
  coverage:
    artifact_dirs: 27
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 67.1
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 68.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/screenshots/browser-use-2026-06-20T173722.png
security:
- kind: authentication
  name: Browser Use Authentication
  slug: browser-use-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Browser Use Domain Security
  slug: browser-use-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: browser-use
tags:
- AI Automation
- Browser Automation
- Web Agents
- Web Scraping
- Headless Browsers
- Agent Infrastructure
- MCP
- Cloud Browsers
website: https://browser-use.com
---
