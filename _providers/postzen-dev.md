---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Postzen Dev Agentic Access
  operation_count: 72
  slug: postzen-dev-agentic-access
  summary_line: 72 operations · 39 acting
api_count: 1
apis:
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: List and disconnect connected social accounts.
  name: postzen-dev Accounts API
  slug: postzen-dev-accounts-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Read post, engagement, follower, and posting-time analytics, and synchronize external posts.
  name: postzen-dev Analytics API
  slug: postzen-dev-analytics-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Manage PostZen API keys programmatically. Creating and deleting keys requires a read-write key with full profile access.
  name: postzen-dev API Keys API
  slug: postzen-dev-api-keys-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Instagram comment and story reply automations with private replies and delivery logs.
  name: postzen-dev Comment Automations API
  slug: postzen-dev-comment-automations-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Start and complete OAuth account connection flows.
  name: postzen-dev Connect API
  slug: postzen-dev-connect-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Profile-owned people from the API, inbox, and comment automations. Maximum 5000 contacts per user and 20 channels per contact. Message counters start when Contacts ships; historical messages are not b
  name: postzen-dev Contacts API
  slug: postzen-dev-contacts-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Read and moderate comments on Instagram, Facebook, and Threads posts. Every endpoint takes the connected account as `accountId` and identifies the post either by its PostZen post id or by the platform
  name: postzen-dev Inbox API
  slug: postzen-dev-inbox-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Create presigned upload URLs for PostZen-hosted media, or upload a small file directly.
  name: postzen-dev Media API
  slug: postzen-dev-media-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Create drafts, scheduled posts, or immediate posts, and read LinkedIn comments and reactions on published organization posts. The LinkedIn reads arrive with company-page posting, which is not availabl
  name: postzen-dev Posts API
  slug: postzen-dev-posts-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: List, create, update, and delete PostZen profiles.
  name: postzen-dev Profiles API
  slug: postzen-dev-profiles-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Manage per-profile posting queues. A queue is a named weekly schedule (`slots` of `{ dayOfWeek, time }`) evaluated in the queue's own timezone. A profile may hold several queues and exactly one is the
  name: postzen-dev Queues API
  slug: postzen-dev-queues-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Payloads PostZen sends to your webhook endpoints, grouped by event family. Every delivery is the JSON envelope `{ id, type, apiVersion, createdAt, data }`; `type` names the event and `data` has the sh
  name: postzen-dev Webhook Events API
  slug: postzen-dev-webhook-events-api
- baseURL: https://api.postzen.dev
  baseurl_source: declared
  description: Manage outbound webhook endpoints and retained delivery logs. PostZen sends an at-least-once JSON envelope `{ id, type, apiVersion, createdAt, data }` using `POST`; automatic retries and manual redeli
  name: postzen-dev Webhooks API
  slug: postzen-dev-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Postzen Dev Webhooks
  slug: postzen-dev-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/postzen-dev/agentic-access/postzen-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postzen-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/postzen-dev/rate-limits/postzen-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postzen-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/postzen-dev/plans/postzen-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postzen-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/rules/postzen-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/postzen-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/json-ld/postzen-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postzen-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/postzen-dev/vocabulary/postzen-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postzen-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/postzen-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/asyncapi/postzen-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/postzen-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/data-model/postzen-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postzen-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/postzen-dev/cli/postzen-dev-cli.yml
  title: ''
  type: CLI
  url: cli/postzen-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/conventions/postzen-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postzen-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/conventions/postzen-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postzen-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/postzen-dev/authentication/postzen-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postzen-dev-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postzen.dev
- group: design
  href: https://artifacts.apis.io/postzen-dev/lifecycle/postzen-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/postzen-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/errors/postzen-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postzen-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/postzen-dev/conformance/postzen-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postzen-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/postzen-dev/llms/postzen-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postzen-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/postzen-dev/mcp/postzen-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/postzen-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/postzen-dev/mcp/postzen-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/postzen-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/postzen-dev/well-known/postzen-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postzen-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/postzen-dev/hosts/postzen-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postzen-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/postzen-dev/vendors/postzen-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postzen-dev-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.postzen.dev/api-reference
- group: auth
  href: https://artifacts.apis.io/postzen-dev/security/postzen-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postzen-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postzen.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postzen.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.postzen.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.postzen.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.postzen.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.postzen.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.postzen.dev/privacy
created: '2026-10-31'
description: PostZen provides a unified social media API for developers and AI agents, enabling posting, scheduling, analytics, comment and direct message management across ten major platforms. Features include media uploads, managed OAuth, analytics dashboards, inbox handling, webhooks, an MCP server, CLI tools, and SDKs. Two free accounts are available with no credit card required.
image: https://www.postzen.dev/opengraph-image.png
json_schemas:
- name: CommentAutomationCreateRequest
  property_count: 24
  slug: postzen-dev-comment-automation-create-request
- name: CommentAutomationUpdateRequest
  property_count: 23
  slug: postzen-dev-comment-automation-update-request
- name: ContactChannel
  property_count: 11
  slug: postzen-dev-contact-channel
- name: ContactCreateRequest
  property_count: 12
  slug: postzen-dev-contact-create-request
- name: Contact
  property_count: 18
  slug: postzen-dev-contact
- name: ContactUpdateRequest
  property_count: 9
  slug: postzen-dev-contact-update-request
jsonld:
- class_count: 120
  name: Postzen Dev Context
  property_count: 272
  slug: postzen-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.postzen.dev.
  name: postzen-dev MCP Server
  slug: postzen-dev-mcp-yml
modified: '2026-10-31'
name: postzen-dev
nav: Providers
network: true
overview: 'postzen-dev publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, API Keys API, and 10 more. Tagged areas include social-media, api, developer-tools, ai-agents, and automation.


  The postzen-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  postzen-dev''s developer surface includes CLI, authentication, API reference, documentation, pricing, engineering blog, and 26 more developer resources.'
plans:
- name: Postzen Dev Plans Pricing
  plan_count: 4
  slug: postzen-dev-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Postzen Dev Rate Limits
  slug: postzen-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: postzen-dev API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: postzen-dev-rules
scopes:
- name: Postzen Dev Scopes
  scope_count: 0
  slug: postzen-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 70.2
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 52.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Postzen Dev Authentication
  slug: postzen-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Postzen Dev Domain Security
  slug: postzen-dev-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: create-post
  slug: postzen-dev-create-post
slug: postzen-dev
tags:
- social-media
- api
- developer-tools
- ai-agents
- automation
website: https://postzen.dev/
---
