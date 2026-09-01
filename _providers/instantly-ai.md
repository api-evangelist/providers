---
access_model:
  confidence: high
  label: Paid plan required · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - openapi
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 112
  human_in_the_loop: 2
  name: Instantly Ai Agentic Access
  operation_count: 186
  slug: instantly-ai-agentic-access
  summary_line: 186 operations · 112 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: The Campaigns API from Instantly — 10 operation(s) for campaigns.
  name: Instantly Campaigns API
  slug: instantly-ai-campaigns-api
- description: An email account that can be used to send campaigns
  name: Instantly Account API
  slug: instantly-ai-account-api
- description: Account Campaign Mapping
  name: Instantly Account Campaign Mapping API
  slug: instantly-ai-accountcampaignmapping-api
- description: Endpoints related to analytics
  name: Instantly Analytics API
  slug: instantly-ai-analytics-api
- description: API Key
  name: Instantly API Key API
  slug: instantly-ai-apikey-api
- description: Audit log records for tracking system activities
  name: Instantly Audit Log API
  slug: instantly-ai-auditlog-api
- description: A background job that can be used to perform long-running tasks
  name: Instantly Background Job API
  slug: instantly-ai-backgroundjob-api
- description: A blocked email or domain
  name: Instantly Block List Entry API
  slug: instantly-ai-blocklistentry-api
- description: A campaign that can be sent to a list of recipients
  name: Instantly Campaign API
  slug: instantly-ai-campaign-api
- description: A subsequence entity representing a follow-up sequence
  name: Instantly Campaign Subsequence API
  slug: instantly-ai-campaignsubsequence-api
- description: CRM related actions
  name: Instantly CRM Actions API
  slug: instantly-ai-crmactions-api
- description: A custom tag for organizing and categorizing accounts and campaigns. You can use them as filters in apis that list accounts and campaigns.
  name: Instantly Custom Tag API
  slug: instantly-ai-customtag-api
- description: This entity represents a tag being assigned to a specific campaign or email account. When an email account is assigned a tag, a new custom tag mapping entry is created, which connects the tag (`tag_id
  name: Instantly Custom Tag Mapping API
  slug: instantly-ai-customtagmapping-api
- description: A Done-For-You email account order
  name: Instantly DFY Email Account Order API
  slug: instantly-ai-dfyemailaccountorder-api
- description: A campaign email, a reply, a manually sent email, or any other email that's visible in the Unibox
  name: Instantly Email API
  slug: instantly-ai-email-api
- description: A single email verification
  name: Instantly Email Verification API
  slug: instantly-ai-emailverification-api
- description: Analytics data for individual emails in inbox placement tests
  name: Instantly Inbox Placement Analytics API
  slug: instantly-ai-inboxplacementanalytics-api
- description: Report data for an inbox placement test
  name: Instantly Inbox Placement Blacklist And Spam Assassin Report API
  slug: instantly-ai-inboxplacementblacklistandspamassassinreport-api
- description: An inbox placement test
  name: Instantly Inbox Placement Test API
  slug: instantly-ai-inboxplacementtest-api
- description: A lead entity representing an individual lead
  name: Instantly Lead API
  slug: instantly-ai-lead-api
- description: A custom label for categorizing and managing leads
  name: Instantly Lead Label API
  slug: instantly-ai-leadlabel-api
- description: A list used to store leads
  name: Instantly Lead List API
  slug: instantly-ai-leadlist-api
- description: OAuth authentication endpoints for connecting Google and Microsoft email accounts
  name: Instantly O Auth API
  slug: instantly-ai-oauth-api
- description: An enrichment can take different forms, such as email enrichment or LinkedIn enrichment. Leads may be imported from SuperSearch using the dedicated endpoint, or enriched directly within a list or camp
  name: Instantly Super Search Enrichment API
  slug: instantly-ai-supersearchenrichment-api
- description: A webhook subscription for receiving event notifications
  name: Instantly Webhook API
  slug: instantly-ai-webhook-api
- description: A webhook event that was sent or attempted to be sent
  name: Instantly Webhook Event API
  slug: instantly-ai-webhookevent-api
- description: A workspace entity representing a workspace
  name: Instantly Workspace API
  slug: instantly-ai-workspace-api
- description: Workspace Billing
  name: Instantly Workspace Billing API
  slug: instantly-ai-workspacebilling-api
- description: A member of a workspace group. You can use the endpoints within this entity to manage the members of a workspace group.
  name: Instantly Workspace Group Member API
  slug: instantly-ai-workspacegroupmember-api
- description: A member of a workspace with associated user details
  name: Instantly Workspace Member API
  slug: instantly-ai-workspacemember-api
artifact_total: 43
asyncapis:
- description: ''
  name: Instantly Ai Webhooks
  slug: instantly-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instantly.ai API v2 Campaigns API
  slug: open-instantly-ai-campaigns-api
- collection_type: open
  name: Instantly.ai API v2
  slug: open-instantly-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instantly-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instantly-ai-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/instantly-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/instantly-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/instantly-ai-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/instantly-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instantly-ai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/instantly-ai-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/instantly-ai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/instantly-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instantly-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instantly-ai-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instantly-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instantly-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.instantly.ai/guides/api-v1-migration
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instantly-ai-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instantly-ai-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/instantly-ai-api-v2-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/instantly-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instantly-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/instantly-ai-finops.yml
created: '2026-05-23'
description: Instantly is a cold email outbound platform that combines mailbox sending infrastructure, email warmup, a B2B lead database, deliverability tools, and a unified inbox for replies. The Instantly v2 REST API at api.instantly.ai/api/v2 publishes a 173-operation OpenAPI 3.1 covering campaigns and subsequences, leads and lead lists, sending accounts and warmup, email verification, inbox placement tests, SuperSearch enrichment, blocklists, custom tags, audit logs, background jobs, webhooks, analytics, API keys, workspaces and workspace groups. Authentication is a scoped Bearer API key backed by a full OAuth 2.0 authorization server with 178 published scopes, PKCE and dynamic client registration. Instantly also runs a hosted remote MCP server, publishes an A2A agent card, an llms.txt and first-party Agent Skills.
finops:
- name: Instantly Ai Finops
  service_category: API
  slug: instantly-ai-finops
graphqls:
- description: '> **Not a provider surface — modelled, not published.** Instantly ships no GraphQL API. On'
  name: Instantly GraphQL Schema
  slug: instantly-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instantly-ai.png
layout: provider
mcp_servers:
- description: ''
  name: Instantly MCP Server
  slug: instantly-mcp-server
modified: '2026-08-13'
name: Instantly
nav: Providers
network: true
overview: 'Instantly publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Account API, Account Campaign Mapping API, and 27 more. Tagged areas include Cold Email, Outbound, Sales, Deliverability, and Lead Database.


  The Instantly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Instantly''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 41 more developer resources.'
plans:
- name: Instantly Ai Plans Pricing
  plan_count: 13
  slug: instantly-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 7
  name: Instantly Ai Rate Limits
  slug: instantly-ai-rate-limits
scopes:
- name: Instantly Ai Scopes
  scope_count: 178
  slug: instantly-ai-scopes
  summary_line: 178 scopes · authorizationCode
score:
  band: strong
  composite: 65.5
  coverage:
    artifact_dirs: 26
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 70.9
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instantly-ai/refs/heads/main/screenshots/instantly-ai-2026-06-20T183518.png
security:
- kind: authentication
  name: Instantly Ai Authentication
  slug: instantly-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Instantly Ai Domain Security
  slug: instantly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instantly-ai
tags:
- Cold Email
- Outbound
- Sales
- Deliverability
- Lead Database
- Email Verification
- Webhook
website: https://instantly.ai
---
