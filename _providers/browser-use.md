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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.0
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 53
  human_in_the_loop: 10
  name: Browser Use Agentic Access
  operation_count: 103
  slug: browser-use-agentic-access
  summary_line: 103 operations · 53 acting · 10 human-in-the-loop
api_count: 6
apis:
- description: Browser Use's hosted remote Model Context Protocol server. An anonymous tools/list returns six real tools — browser_task, monitor_task, list_skills, execute_skill, get_cookies and list_browser_profile
  name: Browser Use MCP Server
  slug: browser-use-mcp
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Billing API from Browser Use — 1 operation(s) for billing.
  name: Browser Use Billing API
  slug: browser-use-billing-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Browsers API from Browser Use — 3 operation(s) for browsers.
  name: Browser Use Browsers API
  slug: browser-use-browsers-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Files API from Browser Use — 3 operation(s) for files.
  name: Browser Use Files API
  slug: browser-use-files-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Profiles API from Browser Use — 2 operation(s) for profiles.
  name: Browser Use Profiles API
  slug: browser-use-profiles-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Runs API from Browser Use — 6 operation(s) for runs.
  name: Browser Use Runs API
  slug: browser-use-runs-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Sessions API from Browser Use — 8 operation(s) for sessions.
  name: Browser Use Sessions API
  slug: browser-use-sessions-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Skills API from Browser Use — 8 operation(s) for skills.
  name: Browser Use Skills API
  slug: browser-use-skills-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Skills Marketplace API from Browser Use — 4 operation(s) for skills marketplace.
  name: Browser Use Skills Marketplace API
  slug: browser-use-skills-marketplace-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Tasks API from Browser Use — 4 operation(s) for tasks.
  name: Browser Use Tasks API
  slug: browser-use-tasks-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Workspaces API from Browser Use — 5 operation(s) for workspaces.
  name: Browser Use Workspaces API
  slug: browser-use-workspaces-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The x402 API from Browser Use — 1 operation(s) for x402.
  name: Browser Use X402 API
  slug: browser-use-x402-api
artifact_total: 22
asyncapis:
- description: ''
  name: Browser Use Webhooks
  slug: browser-use-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/overlays/browser-use-api-v4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/browser-use-api-v4-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/changelog/browser-use-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/browser-use-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/llms/browser-use-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/browser-use-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/a2a/browser-use-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/browser-use-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/mcp/browser-use-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/browser-use-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/mcp/browser-use-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/browser-use-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/well-known/browser-use-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/browser-use-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/packages/browser-use-packages.yml
  title: ''
  type: Packages
  url: packages/browser-use-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/packages/browser-use-packages.yml
  title: ''
  type: SDKs
  url: packages/browser-use-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/cli/browser-use-cli.yml
  title: ''
  type: CLI
  url: cli/browser-use-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/components/browser-use-components.yml
  title: ''
  type: Components
  url: components/browser-use-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/authentication/browser-use-authentication.yml
  title: ''
  type: Authentication
  url: authentication/browser-use-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/scopes/browser-use-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/browser-use-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/conventions/browser-use-conventions.yml
  title: ''
  type: Conventions
  url: conventions/browser-use-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/errors/browser-use-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/browser-use-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/lifecycle/browser-use-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/browser-use-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/conformance/browser-use-conformance.yml
  title: ''
  type: Conformance
  url: conformance/browser-use-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/conformance/browser-use-conformance.yml
  title: ''
  type: Compliance
  url: conformance/browser-use-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/asyncapi/browser-use-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/browser-use-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/data-model/browser-use-data-model.yml
  title: ''
  type: DataModel
  url: data-model/browser-use-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/rate-limits/browser-use-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/browser-use-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/plans/browser-use-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/browser-use-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/finops/browser-use-finops.yml
  title: ''
  type: FinOps
  url: finops/browser-use-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/agentic-access/browser-use-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/browser-use-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/browser-use/refs/heads/main/security/browser-use-domain-security.yml
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
overview: 'Browser Use publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Browsers API, Files API, and 8 more. Tagged areas include AI Automation, Browser Automation, Web Agents, Web Scraping, and Headless Browser.


  The Browser Use catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Browser Use''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Browser Use Plans Pricing
  plan_count: 6
  slug: browser-use-plans-pricing
random_paper: 6
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
  composite: 68.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 66.4
    developer_ergonomics: 78.6
    discoverability: 81.5
    operational_transparency: 65.8
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Headless Browser
- Agent Infrastructure
- MCP
- Cloud Browsers
website: https://browser-use.com
---
