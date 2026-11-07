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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 53
  human_in_the_loop: 10
  name: Browser Use Agentic Access
  operation_count: 103
  slug: browser-use-agentic-access
  summary_line: 103 operations · 53 acting · 10 human-in-the-loop
api_count: 4
apis:
- description: Browser Use's hosted remote Model Context Protocol server. An anonymous tools/list returns six real tools — browser_task, monitor_task, list_skills, execute_skill, get_cookies and list_browser_profile
  name: Browser Use MCP Server
  slug: browser-use-mcp
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Billing API from Browser Use — 1 operation(s) for billing.
  name: Browser Use Billing API
  phrasing_intents:
  - id: get_account_billing_billing_account_get
    intent: Check my account's credit balance
    question: How many Browser Use credits do I have left on my account?
  phrasing_ops: 1
  slug: browser-use-billing-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Browsers API from Browser Use — 3 operation(s) for browsers.
  name: Browser Use Browsers API
  phrasing_intents:
  - id: list_browser_sessions_browsers_get
    intent: List my raw browser sessions
    question: Which standalone browser sessions have I started, and what state are they in?
  - id: create_browser_session_browsers_post
    intent: Start a new cloud browser session
    question: How do I spin up a remote cloud browser I can drive myself without an AI agent?
  - id: get_browser_session_browsers__session_id__get
    intent: Get a browser session's status and URLs
    question: How can I get the live view or CDP URL for a browser session I started?
  - id: update_browser_session_browsers__session_id__patch
    intent: Stop a browser session and refund unused time
    question: How do I shut down a cloud browser session I no longer need?
  - id: list_browser_session_downloads_browsers__session_id__downloads_get
    intent: List files a browser session downloaded
    question: What files did the cloud browser download during my session?
  phrasing_ops: 5
  slug: browser-use-browsers-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Files API from Browser Use — 3 operation(s) for files.
  name: Browser Use Files API
  phrasing_intents:
  - id: agent_session_upload_file_presigned_url_files_sessions__session_id__presigned_url_post
    intent: Get an upload URL for a file in an agent session
    question: How do I give the AI agent a file to work with during its session?
  - id: browser_session_upload_file_presigned_url_files_browsers__session_id__presigned_url_post
    intent: Get an upload URL for a file in a browser session
    question: How can I upload a file into a standalone cloud browser session I'm controlling?
  - id: get_task_output_file_presigned_url_files_tasks__task_id__output_files__file_id__get
    intent: Download a file an agent task produced
    question: How do I download a file the AI agent generated while running a task?
  phrasing_ops: 3
  slug: browser-use-files-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Profiles API from Browser Use — 2 operation(s) for profiles.
  name: Browser Use Profiles API
  phrasing_intents:
  - id: list_profiles_profiles_get
    intent: List or search browser profiles
    question: Which saved browser profiles do I have in my project?
  - id: create_profile_profiles_post
    intent: Create a browser profile to keep logins
    question: How do I keep an agent logged in to a site between tasks?
  - id: get_profile_profiles__profile_id__get
    intent: Get a browser profile's details
    question: What name and user ID are attached to a particular browser profile?
  - id: update_profile_profiles__profile_id__patch
    intent: Rename a profile or change its user ID
    question: Can I rename an existing browser profile?
  - id: delete_browser_profile_profiles__profile_id__delete
    intent: Permanently delete a browser profile
    question: How do I remove a saved browser profile and its stored login state?
  phrasing_ops: 5
  slug: browser-use-profiles-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Runs API from Browser Use — 6 operation(s) for runs.
  name: Browser Use Runs API
  phrasing_intents:
  - id: create_run_runs_post
    intent: Start an agent run on a task
    question: How do I start an agent run that works through a browser task for me?
  - id: list_runs_runs_get
    intent: List agent runs
    question: What agent runs have I started recently?
  - id: list_run_attachments_runs__run_id__attachments_get
    intent: List files attached to a run
    question: Which uploaded files were attached to an agent run?
  - id: get_run_runs__run_id__get
    intent: Get a run's full summary and result
    question: How do I get the full result and task text of a finished run?
  - id: get_run_status_runs__run_id__status_get
    intent: Poll a run's status
    question: What's the lightest way to poll whether a run has finished?
  - id: cancel_run_runs__run_id__cancel_post
    intent: Cancel an in-flight run
    question: How do I cancel an agent run so it stops billing my project?
  - id: get_run_events_runs__run_id__events_get
    intent: Read a run's event stream
    question: How can I follow the step-by-step events of an agent run?
  phrasing_ops: 7
  slug: browser-use-runs-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Sessions API from Browser Use — 8 operation(s) for sessions.
  name: Browser Use Sessions API
  phrasing_intents:
  - id: list_sessions_sessions_get
    intent: List AI agent sessions
    question: Which AI agent sessions are currently active in my project?
  - id: create_session_sessions_post
    intent: Start a new AI agent session
    question: How do I open an agent session that I can send several tasks to in turn?
  - id: get_session_sessions__session_id__get
    intent: Get an agent session's status and tasks
    question: What's the live URL and current status of my agent session?
  - id: update_session_sessions__session_id__patch
    intent: Stop a session via the update action
    question: Can I stop an agent session and all its running tasks by updating the session with an action?
  - id: delete_session_sessions__session_id__delete
    intent: Delete an agent session and its tasks
    question: How do I delete an agent session together with every task in it?
  - id: purge_session_sessions__session_id__purge_post
    intent: Purge all stored data for a session
    question: How do I immediately wipe screenshots, logs and files for a session on a zero-data-retention project?
  - id: get_session_public_share_sessions__session_id__public_share_get
    intent: Get a session's public share link and stats
    question: What's the public share URL for a session I already shared?
  - id: create_session_public_share_sessions__session_id__public_share_post
    intent: Create a public share link for a session
    question: How can I share a replay of an agent session with someone who doesn't have an account?
  phrasing_ops: 15
  slug: browser-use-sessions-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Skills API from Browser Use — 8 operation(s) for skills.
  name: Browser Use Skills API
  phrasing_intents:
  - id: list_skills_skills_get
    intent: List my project's skills
    question: Which skills has my project built so far?
  - id: create_skill_skills_post
    intent: Generate a new automation skill
    question: How do I turn a repeatable browser workflow into a reusable skill?
  - id: get_skill_skills__skill_id__get
    intent: Get one of my skills
    question: What are the details and current generation state of a skill I own?
  - id: delete_skill_skills__skill_id__delete
    intent: Delete a skill I own
    question: How do I get rid of a skill my project no longer needs?
  - id: update_skill_skills__skill_id__patch
    intent: Edit a skill's title, categories or status
    question: How do I disable a skill without deleting it?
  - id: cancel_generation_skills__skill_id__cancel_post
    intent: Cancel a skill's in-progress generation
    question: How do I stop a skill that's still being generated?
  - id: rollback_skill_skills__skill_id__rollback_post
    intent: Roll a skill back to its previous version
    question: How do I revert a skill after a refinement made it worse?
  - id: execute_skill_skills__skill_id__execute_post
    intent: Run one of my own skills
    question: How do I run a skill my project created with specific inputs?
  phrasing_ops: 11
  slug: browser-use-skills-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Skills Marketplace API from Browser Use — 4 operation(s) for skills marketplace.
  name: Browser Use Skills Marketplace API
  phrasing_intents:
  - id: list_skills_marketplace_skills_get
    intent: Browse public skills in the marketplace
    question: What public skills are available in the Browser Use marketplace?
  - id: get_skill_marketplace_skills__skill_slug__get
    intent: View a public marketplace skill
    question: What does a particular public marketplace skill do?
  - id: clone_skill_marketplace_skills__skill_id__clone_post
    intent: Copy a marketplace skill into my project
    question: How do I copy a public skill into my own project so I can customize it?
  - id: execute_skill_marketplace_skills__skill_id__execute_post
    intent: Run a public marketplace skill
    question: Can I run a public marketplace skill directly without cloning it first?
  phrasing_ops: 4
  slug: browser-use-skills-marketplace-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Tasks API from Browser Use — 4 operation(s) for tasks.
  name: Browser Use Tasks API
  phrasing_intents:
  - id: list_tasks_tasks_get
    intent: List AI agent tasks
    question: Which browser agent tasks have I run, and which are still in progress?
  - id: create_task_tasks_post
    intent: Start a browser agent task
    question: How do I tell an AI agent to go do something in a browser for me?
  - id: get_task_tasks__task_id__get
    intent: Get a task's full details, steps and files
    question: How do I see every step the agent took on a task and the files it produced?
  - id: update_task_tasks__task_id__patch
    intent: Pause, resume or stop a task
    question: Can I pause an agent task partway through and resume it later?
  - id: get_task_status_tasks__task_id__status_get
    intent: Poll a task's status, output and cost
    question: What's the most efficient way to poll whether my agent task is done?
  - id: get_task_logs_tasks__task_id__logs_get
    intent: Download a task's execution logs
    question: Where can I download the detailed execution logs for a task?
  phrasing_ops: 6
  slug: browser-use-tasks-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Workspaces API from Browser Use — 5 operation(s) for workspaces.
  name: Browser Use Workspaces API
  phrasing_intents:
  - id: list_workspaces_workspaces_get
    intent: List my workspaces
    question: Which shared file workspaces exist in my project?
  - id: create_workspace_workspaces_post
    intent: Create a workspace for shared file storage
    question: How do I keep files available to the agent across multiple sessions?
  - id: get_workspace_workspaces__workspace_id__get
    intent: Get a workspace's details
    question: What are the details of a specific workspace?
  - id: update_workspace_workspaces__workspace_id__patch
    intent: Rename a workspace
    question: Can I rename a workspace after creating it?
  - id: delete_workspace_workspaces__workspace_id__delete
    intent: Delete a workspace and all its files
    question: How do I delete a whole workspace including everything stored in it?
  - id: list_workspace_files_workspaces__workspace_id__files_get
    intent: List files in a workspace
    question: What files are stored in my workspace?
  - id: delete_workspace_file_workspaces__workspace_id__files_delete
    intent: Delete one file from a workspace
    question: How do I delete a single file from a workspace without removing the workspace?
  - id: get_workspace_size_workspaces__workspace_id__size_get
    intent: Check a workspace's storage usage
    question: How much storage is a workspace using right now?
  phrasing_ops: 9
  slug: browser-use-workspaces-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The x402 API from Browser Use — 1 operation(s) for x402.
  name: Browser Use X402 API
  phrasing_intents:
  - id: x402_balance_x402_balance_post
    intent: Check a wallet project's credit balance
    question: How do I check the credit balance of a project tied to my crypto wallet?
  phrasing_ops: 1
  slug: browser-use-x402-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Extensions API from Browser Use — 2 operation(s) for extensions.
  name: Browser Use Extensions API
  slug: browser-use-extensions-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Integrations API from Browser Use — 5 operation(s) for integrations.
  name: Browser Use Integrations API
  slug: browser-use-integrations-api
- baseURL: https://api.browser-use.com/api/v4
  baseurl_source: declared
  description: The Wallets API from Browser Use — 2 operation(s) for wallets.
  name: Browser Use Wallets API
  slug: browser-use-wallets-api
artifact_total: 29
asyncapis:
- description: ''
  name: Browser Use Webhooks
  slug: browser-use-webhooks
common:
- group: other
  href: https://artifacts.apis.io/browser-use/capabilities/browser-use-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/browser-use-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/browser-use/overlays/browser-use-api-v4-overlay.yaml
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
  href: https://artifacts.apis.io/browser-use/changelog/browser-use-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/browser-use-changelog.yml
- group: agent
  href: https://artifacts.apis.io/browser-use/llms/browser-use-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/browser-use-llms.txt
- group: other
  href: https://artifacts.apis.io/browser-use/a2a/browser-use-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/browser-use-a2a.yml
- group: agent
  href: https://artifacts.apis.io/browser-use/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/browser-use/mcp/browser-use-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/browser-use-mcp.yml
- group: build
  href: https://artifacts.apis.io/browser-use/mcp/browser-use-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/browser-use-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/browser-use/well-known/browser-use-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/browser-use-well-known.yml
- group: build
  href: https://artifacts.apis.io/browser-use/packages/browser-use-packages.yml
  title: ''
  type: Packages
  url: packages/browser-use-packages.yml
- group: build
  href: https://artifacts.apis.io/browser-use/packages/browser-use-packages.yml
  title: ''
  type: SDKs
  url: packages/browser-use-packages.yml
- group: build
  href: https://artifacts.apis.io/browser-use/cli/browser-use-cli.yml
  title: ''
  type: CLI
  url: cli/browser-use-cli.yml
- group: design
  href: https://artifacts.apis.io/browser-use/components/browser-use-components.yml
  title: ''
  type: Components
  url: components/browser-use-components.yml
- group: auth
  href: https://artifacts.apis.io/browser-use/authentication/browser-use-authentication.yml
  title: ''
  type: Authentication
  url: authentication/browser-use-authentication.yml
- group: auth
  href: https://artifacts.apis.io/browser-use/scopes/browser-use-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/browser-use-scopes.yml
- group: design
  href: https://artifacts.apis.io/browser-use/conventions/browser-use-conventions.yml
  title: ''
  type: Conventions
  url: conventions/browser-use-conventions.yml
- group: design
  href: https://artifacts.apis.io/browser-use/errors/browser-use-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/browser-use-problem-types.yml
- group: design
  href: https://artifacts.apis.io/browser-use/lifecycle/browser-use-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/browser-use-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/browser-use/conformance/browser-use-conformance.yml
  title: ''
  type: Conformance
  url: conformance/browser-use-conformance.yml
- group: auth
  href: https://artifacts.apis.io/browser-use/conformance/browser-use-conformance.yml
  title: ''
  type: Compliance
  url: conformance/browser-use-conformance.yml
- group: design
  href: https://artifacts.apis.io/browser-use/asyncapi/browser-use-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/browser-use-webhooks.yml
- group: design
  href: https://artifacts.apis.io/browser-use/data-model/browser-use-data-model.yml
  title: ''
  type: DataModel
  url: data-model/browser-use-data-model.yml
- group: operate
  href: https://artifacts.apis.io/browser-use/rate-limits/browser-use-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/browser-use-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/browser-use/plans/browser-use-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/browser-use-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/browser-use/finops/browser-use-finops.yml
  title: ''
  type: FinOps
  url: finops/browser-use-finops.yml
- group: agent
  href: https://artifacts.apis.io/browser-use/agentic-access/browser-use-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/browser-use-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/browser-use/security/browser-use-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/browser-use-domain-security.yml
created: '2026-03-27'
description: Browser Use makes websites accessible to AI agents. It ships two commercial products on one managed browser platform — Browser Use Agents, which take a natural-language goal and return completed web work, and Browser Infrastructure, which rents stealth cloud Chromium browsers over SDK, REST, or CDP to automation you already own. The public Cloud API is versioned (v4 for long-horizon agent runs, v3 for sessions and workspaces, v2 for low-cost step-based tasks), authenticates with an X-Browser-Use-API-Key header, and is complemented by an OAuth-protected remote MCP server, signed webhooks, an A2A agent card, a published agent skill, first-party Python and TypeScript SDKs, and a CLI. The open-source browser-use Python library is a separate developer tool with its own API.
finops:
- has_sources: true
  method: derived
  name: Browser Use Finops
  primary_unit: gb
  service_category: ''
  slug: browser-use-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/browser-use.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.browser-use.com requiring OAuth; 6 tools listed.
  name: Browser Use MCP Server
  slug: browser-use-mcp-yml
modified: '2026-08-29'
name: Browser Use
nav: Providers
network: true
overview: 'Browser Use publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Browsers API, Files API, and 12 more. Tagged areas include AI Automation, Browser Automation, Web Agents, Web Scraping, and Agent Infrastructure.


  The Browser Use catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Browser Use''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Browser Use Plans Pricing
  plan_count: 8
  slug: browser-use-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 7
  name: Browser Use Rate Limits
  slug: browser-use-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Browser Use API Rules
  rule_count: 56
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 10
  slug: browser-use-rules
scopes:
- name: Browser Use Scopes
  scope_count: 1
  slug: browser-use-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 72.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 60.9
    developer_ergonomics: 77.9
    discoverability: 80.0
    operational_transparency: 65.8
  previous_composite: 72.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/browser-use/browser-use-2026-06-20T173722.png
security:
- kind: authentication
  name: Browser Use Authentication
  slug: browser-use-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Browser Use Domain Security
  slug: browser-use-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Browser
  slug: browser-use-browser
- name: browser-use-continue-a-conversation
  slug: browser-use-continue-a-conversation
- name: browser-use-rent-a-cloud-browser
  slug: browser-use-rent-a-cloud-browser
- name: browser-use-run-a-web-task
  slug: browser-use-run-a-web-task
slug: browser-use
tags:
- AI Automation
- Browser Automation
- Web Agents
- Web Scraping
- Agent Infrastructure
- MCP
- Cloud Browser
- A2A
website: https://browser-use.com
---
