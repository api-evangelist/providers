---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: true
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
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 125
  human_in_the_loop: 7
  name: Duvo Ai Agentic Access
  operation_count: 217
  slug: duvo-ai-agentic-access
  summary_line: 217 operations · 125 acting · 7 human-in-the-loop
api_count: 28
apis:
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Organize agents into folders
  name: Duvo Ai Agent Folders API
  slug: duvo-ai-agent-folders-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Read an agent's memory files (the Memory feature in the Duvo UI)
  name: Duvo Ai Agent Memory API
  slug: duvo-ai-agent-memory-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create and manage agents for automation workloads
  name: Duvo Ai Agents API
  slug: duvo-ai-agents-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Configure case triggers that automatically dispatch agent runs (Runs in the Duvo UI) for cases added to a queue
  name: Duvo Ai Case Triggers API
  slug: duvo-ai-case-triggers-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create, list, and manage cases and their labels within queues
  name: Duvo Ai Cases API
  slug: duvo-ai-cases-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Clarity API from Duvo Ai — 17 operation(s) for clarity.
  name: Duvo Ai Clarity API
  slug: duvo-ai-clarity-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage Clarity v2 process snapshots, transformation proposals, and the extra-capture-request follow-up loop
  name: Duvo Ai ClarityV2 API
  slug: duvo-ai-clarityv2-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage your connected integrations
  name: Duvo Ai Connections API
  slug: duvo-ai-connections-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage logins (domain + username + password + TOTP) used by agents to sign in to websites and desktop applications, and attach them to assignment revisions
  name: Duvo Ai Credentials API
  slug: duvo-ai-credentials-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create, list, iterate on, and delete Duvo Pulse dashboards — live, agent-generated visualizations of your Duvo data
  name: Duvo Ai Duvo Pulse API
  slug: duvo-ai-duvo-pulse-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage team files.
  name: Duvo Ai Files API
  slug: duvo-ai-files-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Browse the team's catalog of available integration types
  name: Duvo Ai Integrations API
  slug: duvo-ai-integrations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: MCP JSON-RPC endpoint exposing public API routes as LLM-callable tools
  name: Duvo Ai MCP API
  slug: duvo-ai-mcp-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Inspect organizations you belong to and the teams within them
  name: Duvo Ai Organizations API
  slug: duvo-ai-organizations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Discover plugins that can be referenced from a revision.
  name: Duvo Ai Plugins API
  slug: duvo-ai-plugins-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage queues and their agent bindings
  name: Duvo Ai Queues API
  slug: duvo-ai-queues-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Attach integrations to assignment revisions, pin specific connections, and link queues
  name: Duvo Ai Revision Integrations API
  slug: duvo-ai-revision-integrations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create and manage agent revisions — the underlying Setup for an Agent
  name: Duvo Ai Revisions API
  slug: duvo-ai-revisions-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Start, monitor, and manage agent runs (Runs in the Duvo UI)
  name: Duvo Ai Runs API
  slug: duvo-ai-runs-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Create sandboxes and upload files for agent runs
  name: Duvo Ai Sandboxes API
  slug: duvo-ai-sandboxes-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List schedules configured for an agent
  name: Duvo Ai Schedules API
  slug: duvo-ai-schedules-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage env-var secrets injected into runs, and attach them to assignment revisions. Only metadata is exposed; values are never returned
  name: Duvo Ai Secrets API
  slug: duvo-ai-secrets-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Manage team and system skills (reusable knowledge packs).
  name: Duvo Ai Skills API
  slug: duvo-ai-skills-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List, apply, and dismiss an Agent's improvement suggestions (the suggestions inbox in the Duvo UI)
  name: Duvo Ai Suggestions API
  slug: duvo-ai-suggestions-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Inspect the team and members associated with the API key
  name: Duvo Ai Team API
  slug: duvo-ai-team-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Configure event triggers that start a Run automatically when an external event fires (e.g. an email arrives, a Linear issue is created, or a file changes in Google Drive)
  name: Duvo Ai Triggers API
  slug: duvo-ai-triggers-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List and manage automations — the workspace container that groups the agents and queues making up one end-to-end process
  name: Duvo Ai Automations API
  slug: duvo-ai-automations-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Upload, list, download, and remove the files attached to a case
  name: Duvo Ai Case Attachments API
  slug: duvo-ai-case-attachments-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Cases UI API from Duvo Ai — 1 operation(s) for cases ui.
  name: Duvo Ai Cases UI API
  slug: duvo-ai-cases-ui-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Clarity Export API from Duvo Ai — 3 operation(s) for clarity export.
  name: Duvo Ai Clarity Export API
  slug: duvo-ai-clarity-export-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Clarity Guest Interviews API from Duvo Ai — 1 operation(s) for clarity guest interviews.
  name: Duvo Ai Clarity Guest Interviews API
  slug: duvo-ai-clarity-guest-interviews-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The Clarity Process Invite Links API from Duvo Ai — 3 operation(s) for clarity process invite links.
  name: Duvo Ai Clarity Process Invite Links API
  slug: duvo-ai-clarity-process-invite-links-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: The ClarityInterview API from Duvo Ai — 12 operation(s) for clarityinterview.
  name: Duvo Ai Clarity Interview API
  slug: duvo-ai-clarityinterview-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: Invite people to a team — one at a time or in bulk, scoped to a Clarity process or the whole team — and manage the team's shareable invite link
  name: Duvo Ai Invites API
  slug: duvo-ai-invites-api
- baseURL: https://api.duvo.ai
  baseurl_source: declared
  description: List, read, dismiss, and clear the authenticated user's team notifications (the Notification Center in the Duvo UI)
  name: Duvo Ai Notifications API
  slug: duvo-ai-notifications-api
artifact_total: 74
asyncapis:
- description: ''
  name: Duvo Ai Webhooks
  slug: duvo-ai-webhooks
collections:
- collection_type: open
  name: Duvo Public Agent Folders API
  slug: open-duvo-ai-agent-folders-api
- collection_type: open
  name: Duvo Public Agent Folders Agent Memory API
  slug: open-duvo-ai-agent-memory-api
- collection_type: open
  name: Duvo Public Agent Folders Agents API
  slug: open-duvo-ai-agents-api
- collection_type: open
  name: Duvo Public Agent Folders Case Triggers API
  slug: open-duvo-ai-case-triggers-api
- collection_type: open
  name: Duvo Public Agent Folders Cases API
  slug: open-duvo-ai-cases-api
- collection_type: open
  name: Duvo Public Agent Folders Clarity API
  slug: open-duvo-ai-clarity-api
- collection_type: open
  name: Duvo Public Agent Folders ClarityV2 API
  slug: open-duvo-ai-clarityv2-api
- collection_type: open
  name: Duvo Public Agent Folders Connections API
  slug: open-duvo-ai-connections-api
- collection_type: open
  name: Duvo Public Agent Folders Credentials API
  slug: open-duvo-ai-credentials-api
- collection_type: open
  name: Duvo Public Agent Folders Duvo Pulse API
  slug: open-duvo-ai-duvo-pulse-api
- collection_type: open
  name: Duvo Public Agent Folders Files API
  slug: open-duvo-ai-files-api
- collection_type: open
  name: Duvo Public Agent Folders Integrations API
  slug: open-duvo-ai-integrations-api
- collection_type: open
  name: Duvo Public Agent Folders MCP API
  slug: open-duvo-ai-mcp-api
- collection_type: open
  name: Duvo Public Agent Folders Organizations API
  slug: open-duvo-ai-organizations-api
- collection_type: open
  name: Duvo Public Agent Folders Plugins API
  slug: open-duvo-ai-plugins-api
- collection_type: open
  name: Duvo Public Agent Folders Queues API
  slug: open-duvo-ai-queues-api
- collection_type: open
  name: Duvo Public Agent Folders Revision Integrations API
  slug: open-duvo-ai-revision-integrations-api
- collection_type: open
  name: Duvo Public Agent Folders Revisions API
  slug: open-duvo-ai-revisions-api
- collection_type: open
  name: Duvo Public Agent Folders Runs API
  slug: open-duvo-ai-runs-api
- collection_type: open
  name: Duvo Public Agent Folders Sandboxes API
  slug: open-duvo-ai-sandboxes-api
- collection_type: open
  name: Duvo Public Agent Folders Schedules API
  slug: open-duvo-ai-schedules-api
- collection_type: open
  name: Duvo Public Agent Folders Secrets API
  slug: open-duvo-ai-secrets-api
- collection_type: open
  name: Duvo Public Agent Folders Skills API
  slug: open-duvo-ai-skills-api
- collection_type: open
  name: Duvo Public Agent Folders Suggestions API
  slug: open-duvo-ai-suggestions-api
- collection_type: open
  name: Duvo Public Agent Folders Team API
  slug: open-duvo-ai-team-api
- collection_type: open
  name: Duvo Public Agent Folders Triggers API
  slug: open-duvo-ai-triggers-api
common:
- group: commercial
  href: https://artifacts.apis.io/duvo-ai/plans/duvo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duvo-ai-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.duvo.ai/blog/feed.xml
- group: other
  href: https://artifacts.apis.io/duvo-ai/capabilities/duvo-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/duvo-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/duvo-ai/overlays/duvo-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/duvo-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/duvo-ai/agentic-access/duvo-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/duvo-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/duvo-ai/security/duvo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duvo-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/duvo-ai/authentication/duvo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duvo-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/duvo-ai/scopes/duvo-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/duvo-ai-scopes.yml
- group: build
  href: https://artifacts.apis.io/duvo-ai/packages/duvo-ai-packages.yml
  title: ''
  type: Packages
  url: packages/duvo-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/duvo-ai/packages/duvo-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/duvo-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/duvo-ai/cli/duvo-ai-cli.yml
  title: ''
  type: CLI
  url: cli/duvo-ai-cli.yml
- group: agent
  href: https://artifacts.apis.io/duvo-ai/mcp/duvo-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/duvo-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/duvo-ai/well-known/duvo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duvo-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/duvo-ai/llms/duvo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duvo-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/duvo-ai/conventions/duvo-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/duvo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/duvo-ai/conventions/duvo-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/duvo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/duvo-ai/errors/duvo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/duvo-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/duvo-ai/lifecycle/duvo-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/duvo-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/duvo-ai/conformance/duvo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duvo-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/duvo-ai/data-model/duvo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duvo-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/duvo-ai/asyncapi/duvo-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/duvo-ai-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/duvo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.duvo.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.duvo.ai
- group: docs
  title: ''
  type: APIReference
  url: https://www.duvo.ai/api-reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.duvo.ai/getting-started.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duvoai
- group: company
  title: ''
  type: Blog
  url: https://www.duvo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.duvo.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.duvo.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.duvo.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.duvo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.duvo.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://www.duvo.ai
created: '2026-07-17'
description: Duvo (taskcrew Inc.) is a process intelligence and automation platform that captures how work really happens, reveals improvement and transformation opportunities, and delivers reliable governed automation across existing enterprise systems. It builds evidence-backed process catalogues, role-specific training, improvement plans, transformation roadmaps, and SAP migration fact bases, then runs cross-system operational workflows — purchase orders, invoice matching, inventory exceptions, supplier onboarding, master data — through agents, queues, human approvals, files, webhooks, and browser automation. Duvo exposes a 213-operation workspace-scoped public API (api.duvo.ai), a hosted MCP server, an official CLI, agent skills, and a full agent-native discovery surface (.well-known agent + MCP cards, llms.txt). Backed by Northzone.
finops:
- has_sources: true
  method: derived
  name: Duvo Ai Finops
  primary_unit: subscription
  service_category: ''
  slug: duvo-ai-finops
  template: false
image: https://www.duvo.ai/logo/duvo-logo-icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.duvo.ai over streamable HTTP; 4 tools listed.
  name: Duvo MCP
  slug: duvo-mcp
modified: '2026-10-06'
name: Duvo Ai
nav: Providers
network: true
overview: 'Duvo Ai publishes 35 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Folders API, Agent Memory API, Agents API, and 32 more. Tagged areas include Company, Enterprise AI, Process Intelligence, Automation, and Agents.


  The Duvo Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Duvo Ai''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, support, and 27 more developer resources.'
plans:
- name: Duvo Ai Plans Pricing
  plan_count: 6
  slug: duvo-ai-plans-pricing
- name: Duvo Ai Price Estimates
  plan_count: 0
  slug: duvo-ai-price-estimates
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Duvo Ai API Rules
  rule_count: 53
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 12
  slug: duvo-ai-rules
scopes:
- name: Duvo Ai Scopes
  scope_count: 8
  slug: duvo-ai-scopes
  summary_line: 8 scopes
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 60.0
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - czech-republic
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 87
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 72.2
screenshot: https://apis.io/screenshots/duvo-ai/duvo-ai-2026-07-25T212653.png
security:
- kind: authentication
  name: Duvo Ai Authentication
  slug: duvo-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Duvo Ai Domain Security
  slug: duvo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Explore and snapshot a Duvo Clarity process
  slug: duvo-ai-clarity-process
- name: Create and work a Duvo queue of cases
  slug: duvo-ai-queue-cases
- name: Start and monitor a Duvo run
  slug: duvo-ai-start-and-monitor-run
slug: duvo-ai
tags:
- Company
- Enterprise AI
- Process Intelligence
- Automation
- Agents
- SAP Migration
- ERP
- Transformation
- Approvals
- Audit
- MCP
website: https://www.duvo.ai
---
