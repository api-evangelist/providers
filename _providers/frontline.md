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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 145
  human_in_the_loop: 0
  name: Frontline Agentic Access
  operation_count: 271
  slug: frontline-agentic-access
  summary_line: 271 operations · 145 acting
api_count: 2
apis:
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Inspect the identity attached to the current API key
  name: Frontline Account API
  slug: frontline-account-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: View and manage your AI agents across your account
  name: Frontline Agent Builder API
  slug: frontline-agent-builder-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: 'Agent runtime data: conversations and transcripts'
  name: Frontline Agents API
  slug: frontline-agents-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Discover available AI models for agent configuration
  name: Frontline AI Models API
  slug: frontline-ai-models-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: View billing plan details, credits, and renewal information
  name: Frontline Billing API
  slug: frontline-billing-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage variables scoped to an agent's flow
  name: Frontline Flow Variables API
  slug: frontline-flow-variables-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: View and manage flows associated with your agents
  name: Frontline Flows API
  slug: frontline-flows-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Inbound HTTPS endpoints that external systems can post events to
  name: Frontline Incoming Webhooks API
  slug: frontline-incoming-webhooks-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage agent intents and training phrases
  name: Frontline Intents API
  slug: frontline-intents-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manual activities (notes, calls, meetings, emails) attached to object rows
  name: Frontline Object activities API
  slug: frontline-object-activities-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Per-view aggregations on objects
  name: Frontline Object aggregations API
  slug: frontline-object-aggregations-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Export object data as XLSX or CSV
  name: Frontline Object export API
  slug: frontline-object-export-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage columns on an object
  name: Frontline Object fields API
  slug: frontline-object-fields-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Files attached to object rows
  name: Frontline Object files API
  slug: frontline-object-files-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage tag/select options on object fields
  name: Frontline Object options API
  slug: frontline-object-options-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Categorize records inside an object
  name: Frontline Object record types API
  slug: frontline-object-record-types-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Link and unlink records across objects
  name: Frontline Object relations API
  slug: frontline-object-relations-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Read and write object records
  name: Frontline Object rows API
  slug: frontline-object-rows-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Tasks attached to object rows
  name: Frontline Object tasks API
  slug: frontline-object-tasks-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Saved view configurations on an object
  name: Frontline Object views API
  slug: frontline-object-views-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage CRM objects (standard and custom)
  name: Frontline Objects API
  slug: frontline-objects-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manual activities (notes, calls, meetings, emails) attached to table rows
  name: Frontline Table activities API
  slug: frontline-table-activities-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Per-view aggregations on tables
  name: Frontline Table aggregations API
  slug: frontline-table-aggregations-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Export table data as XLSX or CSV
  name: Frontline Table export API
  slug: frontline-table-export-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage columns on a table
  name: Frontline Table fields API
  slug: frontline-table-fields-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Files attached to table rows
  name: Frontline Table files API
  slug: frontline-table-files-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage tag/select options on table fields
  name: Frontline Table options API
  slug: frontline-table-options-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Read and write table rows
  name: Frontline Table rows API
  slug: frontline-table-rows-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Tasks attached to table rows
  name: Frontline Table tasks API
  slug: frontline-table-tasks-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage spreadsheet-style tables
  name: Frontline Tables API
  slug: frontline-tables-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage variables scoped to an automation workflow
  name: Frontline Workflow Variables API
  slug: frontline-workflow-variables-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: View and manage your workflows across your account
  name: Frontline Workflows API
  slug: frontline-workflows-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: View account-scoped (Studio) connected integrations, discover connectable toolkits, and configure which tools each integration exposes to agents, flows, and workflows. These are used for workflows and
  name: Frontline Account Integrations API
  slug: frontline-account-integrations-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: View connected channel integrations (WhatsApp, Instagram, Messenger) and bind numbers/accounts/pages to agents
  name: Frontline Agent Channels API
  slug: frontline-agent-channels-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage reusable instruction sets assigned to agents
  name: Frontline Agent Playbooks API
  slug: frontline-agent-playbooks-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Communication channels connected to this account (WhatsApp, Instagram, Messenger)
  name: Frontline Channels API
  slug: frontline-channels-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage custom tools — reusable HTTP/API-call integrations the account creates and assigns to agents, flows, and workflows. Distinct from built-in system tools and connected-integration (MCP) tools.
  name: Frontline Custom Tools API
  slug: frontline-custom-tools-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: 'Builder reference data sourced live from backend constants: valid icons, colors, and formats for objects/tables/fields, plus the workflow/flow node-type catalog. Use these instead of hard-coding allow'
  name: Frontline Guidance API
  slug: frontline-guidance-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Resolve resource IDs (spreadsheets, docs, drive folders, Asana projects, Salesforce SObjects, Gmail labels, Outlook folders/calendars) needed to configure event triggers. Requires a USER API key.
  name: Frontline Integration Resources API
  slug: frontline-integration-resources-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: OAuth/API connected accounts for toolkits like Google Sheets, Gmail, and Slack
  name: Frontline Integrations API
  slug: frontline-integrations-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: Manage knowledge bases, their sources (URLs, website crawls), search, and agent assignment
  name: Frontline Knowledge Bases API
  slug: frontline-knowledge-bases-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: 'User tasks — the account ''To-dos'' inbox: create, list, update, complete, and delete tasks, optionally linked to an object record. Distinct from object-row tasks (Object tasks) and from Max tasks.'
  name: Frontline User Tasks API
  slug: frontline-user-tasks-api
- baseURL: https://prod-api.getfrontline.ai/public/v1
  baseurl_source: declared
  description: List account users to resolve IDs for relations and assignment
  name: Frontline Users API
  slug: frontline-users-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Create and manage campaign audiences
  name: Frontline Audiences API
  slug: frontline-audiences-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Create, deliver, and report on campaigns
  name: Frontline Campaigns API
  slug: frontline-campaigns-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Account-wide defaults for how email, WhatsApp, calendar, and meetings turn activity into CRM records — contact auto-creation, People linking, record assignment, and whether each is a default users may
  name: Frontline Data & Sync API
  slug: frontline-data-sync-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: 'Account-scoped email templates: reusable, versioned content that a Sequence Send Email node references by id and any other feature can send standalone'
  name: Frontline Email Templates API
  slug: frontline-email-templates-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: 'The calling user''s own connected accounts — called ''my connectors'' in the app, and `integrations` in these URLs. Read-only: list and inspect connection health and enabled tools. Connecting, disconnect'
  name: Frontline Max Connectors API
  slug: frontline-max-connectors-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Chat with Max and manage the resulting conversation threads for the calling user
  name: Frontline Max Conversations API
  slug: frontline-max-conversations-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: 'The calling user''s notetaker meetings: recordings, transcripts, AI notes, action items, folders, and note templates'
  name: Frontline Max Meetings API
  slug: frontline-max-meetings-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Reusable instruction sets that steer how the calling user's Max handles recurring work
  name: Frontline Max Playbooks API
  slug: frontline-max-playbooks-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Control whether Max reaches out unprompted, on which channel, how often, and within which hours
  name: Frontline Max Proactive API
  slug: frontline-max-proactive-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: 'Configure the calling user''s Max assistant: overview, general behaviour, scheduling, knowledge base, and per-mailbox email'
  name: Frontline Max Settings API
  slug: frontline-max-settings-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: The calling user's Max automations — scheduled (cron) and event-triggered — plus their triggers and templates
  name: Frontline Max Tasks API
  slug: frontline-max-tasks-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: Meeting volume and duration across the whole account, broken down by day, platform, source, and user. Requires an OWNER or ADMIN.
  name: Frontline Meeting Analytics API
  slug: frontline-meeting-analytics-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: 'Build and run multi-step outbound sequences: graph, nodes, edges, enrollments, recipients, and analytics'
  name: Frontline Sequences API
  slug: frontline-sequences-api
- baseURL: https://prod-api.getfrontline.ai
  baseurl_source: declared
  description: 'The account''s shared connected accounts — called ''workspace connectors'' in the app, and `integrations` in these URLs. Read-only: list them, discover connectable toolkits, and inspect which tools each '
  name: Frontline Workspace Connectors API
  slug: frontline-workspace-connectors-api
artifact_total: 123
collections:
- collection_type: open
  name: Public Account API
  slug: open-frontline-account-api
- collection_type: open
  name: Public Account Agent Builder API
  slug: open-frontline-agent-builder-api
- collection_type: open
  name: Public Account Agents API
  slug: open-frontline-agents-api
- collection_type: open
  name: Public Account AI Models API
  slug: open-frontline-ai-models-api
- collection_type: open
  name: Public Account Billing API
  slug: open-frontline-billing-api
- collection_type: open
  name: Public Account Flow Variables API
  slug: open-frontline-flow-variables-api
- collection_type: open
  name: Public Account Flows API
  slug: open-frontline-flows-api
- collection_type: open
  name: Public Account Incoming Webhooks API
  slug: open-frontline-incoming-webhooks-api
- collection_type: open
  name: Public Account Intents API
  slug: open-frontline-intents-api
- collection_type: open
  name: Public Account Object activities API
  slug: open-frontline-object-activities-api
- collection_type: open
  name: Public Account Object aggregations API
  slug: open-frontline-object-aggregations-api
- collection_type: open
  name: Public Account Object export API
  slug: open-frontline-object-export-api
- collection_type: open
  name: Public Account Object fields API
  slug: open-frontline-object-fields-api
- collection_type: open
  name: Public Account Object files API
  slug: open-frontline-object-files-api
- collection_type: open
  name: Public Account Object options API
  slug: open-frontline-object-options-api
- collection_type: open
  name: Public Account Object record types API
  slug: open-frontline-object-record-types-api
- collection_type: open
  name: Public Account Object relations API
  slug: open-frontline-object-relations-api
- collection_type: open
  name: Public Account Object rows API
  slug: open-frontline-object-rows-api
- collection_type: open
  name: Public Account Object tasks API
  slug: open-frontline-object-tasks-api
- collection_type: open
  name: Public Account Object views API
  slug: open-frontline-object-views-api
- collection_type: open
  name: Public Account Objects API
  slug: open-frontline-objects-api
- collection_type: open
  name: Public Account Table activities API
  slug: open-frontline-table-activities-api
- collection_type: open
  name: Public Account Table aggregations API
  slug: open-frontline-table-aggregations-api
- collection_type: open
  name: Public Account Table export API
  slug: open-frontline-table-export-api
- collection_type: open
  name: Public Account Table fields API
  slug: open-frontline-table-fields-api
- collection_type: open
  name: Public Account Table files API
  slug: open-frontline-table-files-api
- collection_type: open
  name: Public Account Table options API
  slug: open-frontline-table-options-api
- collection_type: open
  name: Public Account Table rows API
  slug: open-frontline-table-rows-api
- collection_type: open
  name: Public Account Table tasks API
  slug: open-frontline-table-tasks-api
- collection_type: open
  name: Public Account Tables API
  slug: open-frontline-tables-api
- collection_type: open
  name: Public Account Tools API
  slug: open-frontline-tools-api
- collection_type: open
  name: Public Account Workflow Variables API
  slug: open-frontline-workflow-variables-api
- collection_type: open
  name: Public Account Workflows API
  slug: open-frontline-workflows-api
common:
- group: other
  href: https://artifacts.apis.io/frontline/capabilities/frontline-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/frontline-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/frontline/authentication/frontline-authentication.yml
  title: ''
  type: Authentication
  url: authentication/frontline-authentication.yml
- group: design
  href: https://artifacts.apis.io/frontline/conventions/frontline-conventions.yml
  title: ''
  type: Conventions
  url: conventions/frontline-conventions.yml
- group: design
  href: https://artifacts.apis.io/frontline/errors/frontline-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/frontline-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/frontline/rate-limits/frontline-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/frontline-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/frontline/lifecycle/frontline-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/frontline-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/frontline/conformance/frontline-conformance.yml
  title: ''
  type: Conformance
  url: conformance/frontline-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.getfrontline.ai/
- group: auth
  href: https://artifacts.apis.io/frontline/security/frontline-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/frontline-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/frontline/security/frontline-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frontline-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/frontline/agentic-access/frontline-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/frontline-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/frontline/mcp/frontline-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/frontline-mcp.yml
- group: agent
  href: https://artifacts.apis.io/frontline/llms/frontline-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/frontline-llms.txt
- group: design
  href: https://artifacts.apis.io/frontline/data-model/frontline-data-model.yml
  title: ''
  type: DataModel
  url: data-model/frontline-data-model.yml
- group: other
  href: https://artifacts.apis.io/frontline/overlays/frontline-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/frontline-overlay.yaml
- group: build
  href: https://artifacts.apis.io/frontline/packages/frontline-packages.yml
  title: ''
  type: Packages
  url: packages/frontline-packages.yml
- group: build
  href: https://artifacts.apis.io/frontline/cli/frontline-cli.yml
  title: ''
  type: CLI
  url: cli/frontline-cli.yml
- group: agent
  href: https://artifacts.apis.io/frontline/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getfrontline.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://frontline-public-api.redocly.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getfrontline.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getfrontline.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getfrontline.ai
- group: operate
  title: ''
  type: Support
  url: https://help.getfrontline.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getfrontline.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getfrontline.ai/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/frontline/plans/frontline-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/frontline-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getfrontline.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.getfrontline.ai/blog
- group: company
  title: ''
  type: Website
  url: https://getfrontline.ai
created: '2026-07-17'
description: Frontline is an AI-native CRM platform that builds and maintains itself. It unifies customer context from WhatsApp, email, and meetings, ships AI agents (Max) that draft replies, proposals, follow-ups and meeting notes, and a Studio for building an AI workforce for sales and support. The Frontline Public API exposes agents, agent-builder flows, automation workflows, CRM objects and rows, tables, tools, intents, AI models, incoming webhooks, account, and billing over REST at https://prod-api.getfrontline.ai/public/v1, authenticated with GENERAL (account) and USER Bearer API keys. Backed by 500 Global.
finops:
- has_sources: true
  method: derived
  name: Frontline Finops
  primary_unit: user/month · billed annually
  service_category: ''
  slug: frontline-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/frontline.png
layout: provider
modified: '2026-08-14'
name: Frontline
nav: Providers
network: true
overview: 'Frontline publishes 57 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent Builder API, Agents API, and 54 more. Tagged areas include Company, CRM, AI Agents, Sales Automation, and Customer Service.


  The Frontline catalog on APIs.io includes 1 Spectral governance ruleset.


  Frontline''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Frontline Plans Pricing
  plan_count: 10
  slug: frontline-plans-pricing
- name: Frontline Price Estimates
  plan_count: 0
  slug: frontline-price-estimates
random_paper: 17
rate_limits:
- limit_count: 1
  name: Frontline Rate Limits
  slug: frontline-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Frontline API Rules
  rule_count: 65
  severity_counts:
    error: 46
    hint: 0
    info: 6
    warn: 13
  slug: frontline-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 51.8
    developer_ergonomics: 71.4
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 102
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/frontline/frontline-2026-07-25T215237.png
security:
- kind: authentication
  name: Frontline Authentication
  slug: frontline-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Frontline Domain Security
  slug: frontline-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Frontline Trust Center
  slug: frontline-trust-center
  summary_line: SOC 2 Type 1
skill_count: 41
skills:
- name: agent-builder
  slug: agent-builder
- name: agent-channels
  slug: agent-channels
- name: agent-playbooks
  slug: agent-playbooks
- name: agents-chat
  slug: agents-chat
- name: aggregations
  slug: aggregations
- name: ai-models
  slug: ai-models
- name: auth-and-profiles
  slug: auth-and-profiles
- name: crm-objects
  slug: crm-objects
- name: crm-setup
  slug: crm-setup
- name: crud-operations
  slug: crud-operations
- name: custom-tools
  slug: custom-tools
- name: export-and-delete
  slug: export-and-delete
- name: files
  slug: files
- name: filter-and-query
  slug: filter-and-query
- name: flow-builder
  slug: flow-builder
- name: formulas
  slug: formulas
- name: frontline-agents
  slug: frontline-agents
- name: frontline-api
  slug: frontline-api
- name: frontline-billing
  slug: frontline-billing
- name: frontline-docs
  slug: frontline-docs
- name: frontline-internals
  slug: frontline-internals
- name: frontline-workflows
  slug: frontline-workflows
- name: incoming-webhooks
  slug: incoming-webhooks
- name: integrations
  slug: integrations
slug: frontline
tags:
- Company
- CRM
- AI Agents
- Sales Automation
- Customer Service
- Workflows
- Conversational AI
website: https://getfrontline.ai
---
