---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 98
  human_in_the_loop: 2
  name: Instantly Ai Agentic Access
  operation_count: 181
  slug: instantly-ai-agentic-access
  summary_line: 181 operations · 98 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: An email account that can be used to send campaigns
  name: Instantly Account API
  slug: instantly-ai-account-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: Account Campaign Mapping
  name: Instantly Account Campaign Mapping API
  slug: instantly-ai-accountcampaignmapping-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: Endpoints related to analytics
  name: Instantly Analytics API
  slug: instantly-ai-analytics-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A blocked email or domain
  name: Instantly Block List Entry API
  slug: instantly-ai-blocklistentry-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A campaign that can be sent to a list of recipients
  name: Instantly Campaign API
  slug: instantly-ai-campaign-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A subsequence entity representing a follow-up sequence
  name: Instantly Campaign Subsequence API
  slug: instantly-ai-campaignsubsequence-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: CRM related actions
  name: Instantly CRM Actions API
  slug: instantly-ai-crmactions-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A custom tag for organizing and categorizing accounts and campaigns. You can use them as filters in apis that list accounts and campaigns.
  name: Instantly Custom Tag API
  slug: instantly-ai-customtag-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: This entity represents a tag being assigned to a specific campaign or email account. When an email account is assigned a tag, a new custom tag mapping entry is created, which connects the tag (`tag_id
  name: Instantly Custom Tag Mapping API
  slug: instantly-ai-customtagmapping-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A Done-For-You email account order
  name: Instantly DFY Email Account Order API
  slug: instantly-ai-dfyemailaccountorder-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A campaign email, a reply, a manually sent email, or any other email that's visible in the Unibox
  name: Instantly Email API
  slug: instantly-ai-email-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: Analytics data for individual emails in inbox placement tests
  name: Instantly Inbox Placement Analytics API
  slug: instantly-ai-inboxplacementanalytics-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: Report data for an inbox placement test
  name: Instantly Inbox Placement Blacklist And Spam Assassin Report API
  slug: instantly-ai-inboxplacementblacklistandspamassassinreport-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: An inbox placement test
  name: Instantly Inbox Placement Test API
  slug: instantly-ai-inboxplacementtest-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A lead entity representing an individual lead
  name: Instantly Lead API
  slug: instantly-ai-lead-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A custom label for categorizing and managing leads
  name: Instantly Lead Label API
  slug: instantly-ai-leadlabel-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A list used to store leads
  name: Instantly Lead List API
  slug: instantly-ai-leadlist-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: An enrichment can take different forms, such as email enrichment or LinkedIn enrichment. Leads may be imported from SuperSearch using the dedicated endpoint, or enriched directly within a list or camp
  name: Instantly Super Search Enrichment API
  slug: instantly-ai-supersearchenrichment-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A webhook subscription for receiving event notifications
  name: Instantly Webhook API
  slug: instantly-ai-webhook-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A workspace entity representing a workspace
  name: Instantly Workspace API
  slug: instantly-ai-workspace-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: Workspace Billing
  name: Instantly Workspace Billing API
  slug: instantly-ai-workspacebilling-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A member of a workspace group. You can use the endpoints within this entity to manage the members of a workspace group.
  name: Instantly Workspace Group Member API
  slug: instantly-ai-workspacegroupmember-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A member of a workspace with associated user details
  name: Instantly Workspace Member API
  slug: instantly-ai-workspacemember-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: OAuth authentication endpoints for connecting Google and Microsoft email accounts
  name: Instantly O Auth API
  slug: instantly-ai-oauth-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: API Key
  name: Instantly API Key API
  slug: instantly-ai-api-key-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: Audit log records for tracking system activities
  name: Instantly Audit Log API
  slug: instantly-ai-audit-log-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A background job that can be used to perform long-running tasks
  name: Instantly Background Job API
  slug: instantly-ai-background-job-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A single email verification
  name: Instantly Email Verification API
  slug: instantly-ai-email-verification-api
- baseURL: https://api.instantly.ai/api/v2
  baseurl_source: declared
  description: A webhook event that was sent or attempted to be sent
  name: Instantly Webhook Event API
  slug: instantly-ai-webhook-event-api
artifact_total: 44
asyncapis:
- description: ''
  name: Instantly Ai Webhooks
  slug: instantly-ai-webhooks
collections:
- collection_type: open
  name: Instantly.ai API v2 Campaigns API
  slug: open-instantly-ai-campaigns-api
- collection_type: open
  name: Instantly.ai API v2
  slug: open-instantly-ai
common:
- group: other
  href: https://artifacts.apis.io/instantly-ai/capabilities/instantly-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/instantly-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/instantly-ai/agentic-access/instantly-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/instantly-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/instantly-ai/security/instantly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instantly-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/instantly-ai/authentication/instantly-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instantly-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://instantly.ai
- group: other
  title: ''
  type: App
  url: https://app.instantly.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.instantly.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developer.instantly.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.instantly.ai/getting-started/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.instantly.ai/getting-started/authorization
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.instantly.ai/openapi/api_v2.json
- group: commercial
  title: ''
  type: Pricing
  url: https://instantly.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://instantly.ai/blog
- group: operate
  title: ''
  type: Help
  url: https://help.instantly.ai
- group: start
  title: ''
  type: Signup
  url: https://app.instantly.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.instantly.ai/auth/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instantly.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instantly.ai/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instantlyai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Instantlydotai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@instantly-ai
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.instantly.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/instantly-ai/llms/instantly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instantly-ai-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.instantly.ai
- group: start
  title: ''
  type: Quickstart
  url: https://developer.instantly.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.instantly.ai
- group: operate
  title: ''
  type: Community
  url: https://developer.instantly.ai/getting-started/slack-channel
- group: start
  title: ''
  type: SignUp
  url: https://app.instantly.ai/auth/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Instantly-ai
- group: build
  href: https://artifacts.apis.io/instantly-ai/packages/instantly-ai-packages.yml
  title: ''
  type: Packages
  url: packages/instantly-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/instantly-ai/packages/instantly-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/instantly-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/instantly-ai/cli/instantly-ai-cli.yml
  title: ''
  type: CLI
  url: cli/instantly-ai-cli.yml
- group: agent
  href: https://artifacts.apis.io/instantly-ai/well-known/instantly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/instantly-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/instantly-ai/mcp/instantly-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/instantly-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/instantly-ai/mcp/instantly-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/instantly-ai-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/instantly-ai/a2a/instantly-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/instantly-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/instantly-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/instantly-ai/scopes/instantly-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/instantly-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/instantly-ai/conventions/instantly-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/instantly-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/instantly-ai/errors/instantly-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instantly-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/instantly-ai/conformance/instantly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instantly-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/instantly-ai/lifecycle/instantly-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/instantly-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.instantly.ai/guides/api-v1-migration
- group: design
  href: https://artifacts.apis.io/instantly-ai/asyncapi/instantly-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/instantly-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/instantly-ai/data-model/instantly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instantly-ai-data-model.yml
- group: other
  href: https://artifacts.apis.io/instantly-ai/overlays/instantly-ai-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/instantly-ai-api-v2-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/instantly-ai/plans/instantly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/instantly-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/instantly-ai/rate-limits/instantly-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/instantly-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/instantly-ai/finops/instantly-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/instantly-ai-finops.yml
created: '2026-05-23'
description: Instantly is a cold email outbound platform that combines mailbox sending infrastructure, email warmup, a B2B lead database, deliverability tools, and a unified inbox for replies. The Instantly v2 REST API at api.instantly.ai/api/v2 publishes a 173-operation OpenAPI 3.1 covering campaigns and subsequences, leads and lead lists, sending accounts and warmup, email verification, inbox placement tests, SuperSearch enrichment, blocklists, custom tags, audit logs, background jobs, webhooks, analytics, API keys, workspaces and workspace groups. Authentication is a scoped Bearer API key backed by a full OAuth 2.0 authorization server with 178 published scopes, PKCE and dynamic client registration. Instantly also runs a hosted remote MCP server, publishes an A2A agent card, an llms.txt and first-party Agent Skills.
finops:
- has_sources: true
  method: derived
  name: Instantly Ai Finops
  primary_unit: subscription
  service_category: ''
  slug: instantly-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instantly-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.instantly.ai requiring OAuth.
  name: Instantly MCP Server
  slug: instantly-ai-mcp-yml
modified: '2026-08-13'
name: Instantly
nav: Providers
network: true
overview: 'Instantly publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Campaign Mapping API, Analytics API, and 26 more. Tagged areas include Cold Email, Outbound, Sales, Deliverability, and Lead Database.


  The Instantly catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Instantly''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 42 more developer resources.'
plans:
- name: Instantly Ai Plans Pricing
  plan_count: 20
  slug: instantly-ai-plans-pricing
- name: Instantly Ai Price Estimates
  plan_count: 0
  slug: instantly-ai-price-estimates
random_paper: 21
rate_limits:
- limit_count: 7
  name: Instantly Ai Rate Limits
  slug: instantly-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Instantly API Rules
  rule_count: 65
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 16
  slug: instantly-ai-rules
scopes:
- name: Instantly Ai Scopes
  scope_count: 178
  slug: instantly-ai-scopes
  summary_line: 178 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 66.5
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 67.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 29
    mcp: first-party
    skills: first-party
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
    score: 11.1
screenshot: https://apis.io/screenshots/instantly-ai/instantly-ai-2026-06-20T183518.png
security:
- kind: authentication
  name: Instantly Ai Authentication
  slug: instantly-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Instantly Ai Domain Security
  slug: instantly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Instantly
  slug: instantly-ai-instantly-api-v2-skill
- name: instantly-gtm
  slug: instantly-ai-instantly-gtm-SKILL
slug: instantly-ai
tags:
- Cold Email
- Outbound
- Sales
- Deliverability
- Lead Database
- Email Verification
- Webhook
- A2A
website: https://instantly.ai
---
