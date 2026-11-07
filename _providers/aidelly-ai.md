---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 83
  human_in_the_loop: 6
  name: Aidelly Ai Agentic Access
  operation_count: 154
  slug: aidelly-ai-agentic-access
  summary_line: 154 operations · 83 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Accounts API from Aidelly AI — 3 operation(s) for accounts.
  name: Aidelly AI Accounts API
  slug: aidelly-ai-accounts-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Workspace activity audit trail (#2005). Read-only access to historical events. Requires `activity:read` scope.
  name: Aidelly AI Activity API
  slug: aidelly-ai-activity-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Analytics API from Aidelly AI — 3 operation(s) for analytics.
  name: Aidelly AI Analytics API
  slug: aidelly-ai-analytics-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Approvals API from Aidelly AI — 4 operation(s) for approvals.
  name: Aidelly AI Approvals API
  slug: aidelly-ai-approvals-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Workspace approval gate settings — the "require member approval" toggle that drives the Team Approvals queue. Public API preview.
  name: Aidelly AI Approval Settings API
  slug: aidelly-ai-approvalsettings-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Automations API from Aidelly AI — 3 operation(s) for automations.
  name: Aidelly AI Automations API
  slug: aidelly-ai-automations-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Bio API from Aidelly AI — 1 operation(s) for bio.
  name: Aidelly AI Bio API
  slug: aidelly-ai-bio-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Brand API from Aidelly AI — 11 operation(s) for brand.
  name: Aidelly AI Brand API
  slug: aidelly-ai-brand-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Brand Interview question track generator (#812). Public API preview.
  name: Aidelly AI Brand Interview API
  slug: aidelly-ai-brandinterview-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Calendar API from Aidelly AI — 5 operation(s) for calendar.
  name: Aidelly AI Calendar API
  slug: aidelly-ai-calendar-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Content campaigns (#1351) — the grouping/reporting dimension posts are tagged with. Deleting a campaign that publish history references soft-deletes it so the history keeps its grouping (#2590).
  name: Aidelly AI Campaigns API
  slug: aidelly-ai-campaigns-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Client review portal links (#1347). Allow clients to review and provide feedback on posts before publication, without requiring an Aidelly account.
  name: Aidelly AI Client Review Links API
  slug: aidelly-ai-clientreviewlinks-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Competitors API from Aidelly AI — 1 operation(s) for competitors.
  name: Aidelly AI Competitors API
  slug: aidelly-ai-competitors-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Connections API from Aidelly AI — 1 operation(s) for connections.
  name: Aidelly AI Connections API
  slug: aidelly-ai-connections-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The ConnectLinks API from Aidelly AI — 3 operation(s) for connectlinks.
  name: Aidelly AI Connect Links API
  slug: aidelly-ai-connectlinks-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Creators API from Aidelly AI — 1 operation(s) for creators.
  name: Aidelly AI Creators API
  slug: aidelly-ai-creators-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Multi-channel posting presets (#1351). Fan one post out to multiple accounts/platforms with per-channel customization.
  name: Aidelly AI Destination Presets API
  slug: aidelly-ai-destinationpresets-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: 'Post drafts — work-in-progress content saved for later composition. Drafts are never published; they exist solely for planning and editing. Use the `draft_planned_for` field to position drafts on the '
  name: Aidelly AI Drafts API
  slug: aidelly-ai-drafts-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: E-commerce store connections (Shopify, WooCommerce, Etsy, Wix) and product browsing. Public API preview — route handlers ship in a follow-up release; in-app behavior already lives at /api/ecommerce/*.
  name: Aidelly AI Ecommerce API
  slug: aidelly-ai-ecommerce-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Ideas API from Aidelly AI — 1 operation(s) for ideas.
  name: Aidelly AI Ideas API
  slug: aidelly-ai-ideas-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The ImageEditor API from Aidelly AI — 1 operation(s) for imageeditor.
  name: Aidelly AI Image Editor API
  slug: aidelly-ai-imageeditor-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Inbox API from Aidelly AI — 7 operation(s) for inbox.
  name: Aidelly AI Inbox API
  slug: aidelly-ai-inbox-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Links API from Aidelly AI — 2 operation(s) for links.
  name: Aidelly AI Links API
  slug: aidelly-ai-links-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Media API from Aidelly AI — 2 operation(s) for media.
  name: Aidelly AI Media API
  slug: aidelly-ai-media-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Photos API from Aidelly AI — 1 operation(s) for photos.
  name: Aidelly AI Photos API
  slug: aidelly-ai-photos-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Team Approvals queue and audit events (#788). List pending posts, approve or reject them, and read the audit trail. Requires `approvals:read` / `approvals:write`.
  name: Aidelly AI Post Approvals API
  slug: aidelly-ai-postapprovals-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Post creation, scheduling, and management. Includes comments (discussions) for threaded collaboration on post drafts. Requires `posts:read` or `posts:write`; comments additionally require `comments:re
  name: Aidelly AI Posts API
  slug: aidelly-ai-posts-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Prompt library execution for AI-generated content (#2005). Run prompts with custom inputs and receive generated output. Listing requires `prompts:read`; running requires `prompts:write`.
  name: Aidelly AI Prompts API
  slug: aidelly-ai-prompts-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Recurring content scheduling queues (#1351). Define weekly time slots where posts are automatically published.
  name: Aidelly AI Queues API
  slug: aidelly-ai-queues-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The ReportLinks API from Aidelly AI — 2 operation(s) for reportlinks.
  name: Aidelly AI Report Links API
  slug: aidelly-ai-reportlinks-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Analytics report share links and distribution (#1354).
  name: Aidelly AI Reports API
  slug: aidelly-ai-reports-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Repurpose API from Aidelly AI — 2 operation(s) for repurpose.
  name: Aidelly AI Repurpose API
  slug: aidelly-ai-repurpose-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Scheduled posts API, including compose-time auto-recycle (#847) and the self-healing publish audit trail (#852). Public API preview.
  name: Aidelly AI Scheduled Posts API
  slug: aidelly-ai-scheduledposts-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Tasks API from Aidelly AI — 2 operation(s) for tasks.
  name: Aidelly AI Tasks API
  slug: aidelly-ai-tasks-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Usage API from Aidelly AI — 2 operation(s) for usage.
  name: Aidelly AI Usage API
  slug: aidelly-ai-usage-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The ViralTrends API from Aidelly AI — 1 operation(s) for viraltrends.
  name: Aidelly AI Viral Trends API
  slug: aidelly-ai-viraltrends-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Webhooks API from Aidelly AI — 3 operation(s) for webhooks.
  name: Aidelly AI Webhooks API
  slug: aidelly-ai-webhooks-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: Agency white-label branding configuration (#1644). Manage logos, colors, emails, and visibility toggles for white-label agency tenants.
  name: Aidelly AI White Label API
  slug: aidelly-ai-white-label-api
- baseURL: https://app.aidelly.ai/api/public/v1
  baseurl_source: declared
  description: The Workspaces API from Aidelly AI — 5 operation(s) for workspaces.
  name: Aidelly AI Workspaces API
  slug: aidelly-ai-workspaces-api
artifact_total: 61
asyncapis:
- description: ''
  name: Aidelly Ai Webhooks
  slug: aidelly-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/aidelly-ai/agentic-access/aidelly-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aidelly-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aidelly-ai/plans/aidelly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidelly-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/rules/aidelly-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aidelly-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/json-ld/aidelly-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aidelly-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aidelly-ai/vocabulary/aidelly-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aidelly-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aidelly-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/asyncapi/aidelly-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aidelly-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/data-model/aidelly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aidelly-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/aidelly-ai/cli/aidelly-ai-cli.yml
  title: ''
  type: CLI
  url: cli/aidelly-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/conventions/aidelly-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aidelly-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/conventions/aidelly-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aidelly-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aidelly.ai/trust
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/authentication/aidelly-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aidelly-ai-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.aidelly.ai/developers/api/deprecation
- group: design
  href: https://artifacts.apis.io/aidelly-ai/lifecycle/aidelly-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aidelly-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/errors/aidelly-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aidelly-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aidelly-ai/conformance/aidelly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aidelly-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aidelly-ai/llms/aidelly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidelly-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/aidelly-ai/mcp/aidelly-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aidelly-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/well-known/aidelly-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aidelly-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/well-known/aidelly-ai-aidelly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aidelly-ai-aidelly-security.txt
- group: agent
  href: https://artifacts.apis.io/aidelly-ai/well-known/aidelly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aidelly-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aidelly-ai/hosts/aidelly-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidelly-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aidelly-ai/vendors/aidelly-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aidelly-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aidelly.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.aidelly.ai/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.aidelly.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aidelly.ai/docs/getting-started/overview
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/scopes/aidelly-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aidelly-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/security/aidelly-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aidelly-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/security/aidelly-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aidelly-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aidelly-ai/security/aidelly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidelly-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidelly.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aidelly.ai/developers/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://www.aidelly.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.aidelly.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aidelly.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.aidelly.ai/start-trial
- group: start
  title: ''
  type: Login
  url: https://app.aidelly.ai/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aidelly.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aidelly.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.aidelly.ai/trust
created: '2026-11-01'
description: Aidelly AI provides an AI‑powered social media management platform for agencies, offering white‑label agents that can draft, publish, reply, and report on client accounts. The service supports unlimited client accounts, integrates with tools like Claude, ChatGPT, and Zapier, and includes features such as brand‑specific tone settings, multi‑platform posting (Facebook, Instagram, LinkedIn, TikTok, etc.), and detailed analytics. It aims to streamline agency workflows with AI agents that can be customized to each client’s voice and compliance needs.
image: https://www.aidelly.ai/opengraph-image?ffa205946bf99bd8
json_schemas:
- name: CreatePhotoRequest
  property_count: 7
  slug: aidelly-ai-create-photo-request
- name: CreatePostRequest
  property_count: 8
  slug: aidelly-ai-create-post-request
- name: CreateRepurposeJobRequest
  property_count: 6
  slug: aidelly-ai-create-repurpose-job-request
- name: CreateScheduledPostRequest
  property_count: 7
  slug: aidelly-ai-create-scheduled-post-request
- name: ReportSchedule
  property_count: 12
  slug: aidelly-ai-report-schedule
- name: Report
  property_count: 12
  slug: aidelly-ai-report
jsonld:
- class_count: 60
  name: Aidelly Ai Context
  property_count: 228
  slug: aidelly-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.aidelly.ai.
  name: Aidelly AI MCP Server
  slug: aidelly-ai-mcp-yml
modified: '2026-11-01'
name: Aidelly AI
nav: Providers
network: true
overview: 'Aidelly AI publishes 39 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Activity API, Analytics API, and 36 more. Tagged areas include Artificial Intelligence, Social Media, Agency, White Label, and Automation.


  The Aidelly AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Aidelly AI''s developer surface includes CLI, authentication, changelog, getting-started guide, documentation, engineering blog, pricing, and 35 more developer resources.'
plans:
- name: Aidelly Ai Plans Pricing
  plan_count: 4
  slug: aidelly-ai-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Aidelly AI API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 3
  slug: aidelly-ai-rules
scopes:
- name: Aidelly Ai Scopes
  scope_count: 57
  slug: aidelly-ai-scopes
  summary_line: 57 scopes · authorizationCode
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.6
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 67.5
    developer_ergonomics: 37.5
    discoverability: 65.8
    operational_transparency: 25.0
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aidelly Ai Authentication
  slug: aidelly-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aidelly Ai Domain Security
  slug: aidelly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aidelly Ai Vulnerability Disclosure
  slug: aidelly-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aidelly Ai Trust Center
  slug: aidelly-ai-trust-center
  summary_line: GDPR
skill_count: 5
skills:
- name: aidelly-ai-analytics-refresh-insights
  slug: aidelly-ai-analytics-refresh-insights
- name: aidelly-ai-brand-profile-update
  slug: aidelly-ai-brand-profile-update
- name: aidelly-ai-create-and-fetch-report
  slug: aidelly-ai-create-and-fetch-report
- name: aidelly-ai-ecommerce-sync-and-list
  slug: aidelly-ai-ecommerce-sync-and-list
- name: aidelly-ai-manage-webhooks
  slug: aidelly-ai-manage-webhooks
slug: aidelly-ai
tags:
- Artificial Intelligence
- Social Media
- Agency
- White Label
- Automation
website: https://aidelly.ai/
---
