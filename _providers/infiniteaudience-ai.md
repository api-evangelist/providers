---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 74
  human_in_the_loop: 8
  name: Infiniteaudience Ai Agentic Access
  operation_count: 131
  slug: infiniteaudience-ai-agentic-access
  summary_line: 131 operations · 74 acting · 8 human-in-the-loop
api_count: 2
apis:
- description: Remote, OAuth-protected Model Context Protocol server for exploring signals, building segments and running approved workflows from an assistant.
  name: Infinite Audience MCP Server
  slug: infinite-audience-mcp
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Agent-to-Agent task protocol
  name: Infinite Audience A2A API
  slug: infiniteaudience-ai-a2a-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Balance, top-up, and subscription management
  name: Infinite Audience Account API
  slug: infiniteaudience-ai-account-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Build, store, and manage named audience definitions
  name: Infinite Audience Audiences API
  slug: infiniteaudience-ai-audiences-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Token exchange
  name: Infinite Audience Auth API
  slug: infiniteaudience-ai-auth-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Named workspaces that group related audiences and deliveries under a single context
  name: Infinite Audience Campaigns API
  slug: infiniteaudience-ai-campaigns-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Org-wide delivery history and status
  name: Infinite Audience Deliveries API
  slug: infiniteaudience-ai-deliveries-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Audience count and lookup (exploration)
  name: Infinite Audience Discovery API
  slug: infiniteaudience-ai-discovery-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Attribute catalog, propensity models, synchronous micro-batch matching, and async file-based identity resolution
  name: Infinite Audience Enrichment API
  slug: infiniteaudience-ai-enrichment-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: The Integrations API from Infinite Audience — 3 operation(s) for integrations.
  name: Infinite Audience Integrations API
  slug: infiniteaudience-ai-integrations-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Model Context Protocol session management
  name: Infinite Audience MCP API
  slug: infiniteaudience-ai-mcp-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: OAuth 2.0 authorization server for confidential integrations and delegated REST, MCP, and A2A clients. Authenticate on behalf of one of your customers via the standard authorization-code flow with PKC
  name: Infinite Audience OAuth API
  slug: infiniteaudience-ai-oauth-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Retained activity and reusable results produced through connected partners
  name: Infinite Audience Partnerships API
  slug: infiniteaudience-ai-partnerships-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Save and manage reusable filter definitions
  name: Infinite Audience Segments API
  slug: infiniteaudience-ai-segments-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Self-service API keys and org configuration
  name: Infinite Audience Settings API
  slug: infiniteaudience-ai-settings-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Durable, per-event-filtered webhook-trigger subscriptions (e.g. one per Zap) — distinct from the single implicit URL configured under the Webhooks tag / `/v1/settings/webhook`. Delivery is retried wit
  name: Infinite Audience Triggers API
  slug: infiniteaudience-ai-triggers-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: '**Outbound webhook notifications** — the platform POSTs to your endpoint when async operations finish. **Events fired:** | Event | Trigger | |---|---| | `segment.ready` | Async segment build succeeded'
  name: Infinite Audience Webhooks API
  slug: infiniteaudience-ai-webhooks-api
- baseURL: https://api.infiniteaudience.ai
  baseurl_source: declared
  description: Monitor async audience pipeline progress (similarity and propensity subtypes). Poll GET /v1/workflows/{workflow_run_id} or respond to HITL gates via POST /v1/workflows/{workflow_run_id}/resume.
  name: Infinite Audience Workflows API
  slug: infiniteaudience-ai-workflows-api
artifact_total: 33
asyncapis:
- description: ''
  name: Infiniteaudience Ai Webhooks
  slug: infiniteaudience-ai-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/plans/infiniteaudience-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infiniteaudience-ai-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/agentic-access/infiniteaudience-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infiniteaudience-ai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/rules/infiniteaudience-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/infiniteaudience-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/json-ld/infiniteaudience-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/infiniteaudience-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/vocabulary/infiniteaudience-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/infiniteaudience-ai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/asyncapi/infiniteaudience-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/infiniteaudience-ai-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/data-model/infiniteaudience-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infiniteaudience-ai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/conventions/infiniteaudience-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/infiniteaudience-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/conventions/infiniteaudience-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infiniteaudience-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/errors/infiniteaudience-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infiniteaudience-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/conformance/infiniteaudience-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infiniteaudience-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/llms/infiniteaudience-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infiniteaudience-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/a2a/infiniteaudience-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/infiniteaudience-ai-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/mcp/infiniteaudience-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/infiniteaudience-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/mcp/infiniteaudience-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/infiniteaudience-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/well-known/infiniteaudience-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infiniteaudience-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/hosts/infiniteaudience-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infiniteaudience-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/vendors/infiniteaudience-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infiniteaudience-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/packages/infiniteaudience-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/infiniteaudience-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/packages/infiniteaudience-ai-packages.yml
  title: ''
  type: Packages
  url: packages/infiniteaudience-ai-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.infiniteaudience.ai/surfaces/activation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/authentication/infiniteaudience-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/infiniteaudience-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/security/infiniteaudience-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infiniteaudience-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infiniteaudience.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infiniteaudience.ai/agents/a2a/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.infiniteaudience.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infiniteaudience.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/no-fait
- group: company
  title: ''
  type: Newsroom
  url: https://infiniteaudience.ai/news
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infiniteaudience.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.infiniteaudience.ai/api/
created: '2026-10-09'
description: Infinite Audience, built by NO FAIT, is a customer-intelligence platform for identity resolution, consumer data enrichment, audience building and activation. Its REST API (api.infiniteaudience.ai) covers discovery counts, segments, audiences, campaigns, deliveries, file and micro-batch matching, webhooks and billing, and it also exposes a remote OAuth-protected MCP server and an A2A agent.
image: https://infiniteaudience.ai/assets/infinite-audience-logo.png
json_schemas:
- name: AudienceObject
  property_count: 26
  slug: infiniteaudience-ai-audience-object
- name: AudienceRefreshResult
  property_count: 14
  slug: infiniteaudience-ai-audience-refresh-result
- name: Campaign
  property_count: 7
  slug: infiniteaudience-ai-campaign
- name: DeliveryObject
  property_count: 24
  slug: infiniteaudience-ai-delivery-object
- name: FileMatchJob
  property_count: 21
  slug: infiniteaudience-ai-file-match-job
- name: SegmentObject
  property_count: 36
  slug: infiniteaudience-ai-segment-object
jsonld:
- class_count: 83
  name: Infiniteaudience Ai Context
  property_count: 384
  slug: infiniteaudience-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.infiniteaudience.ai requiring OAuth; 54 tools listed.
  name: Infinite Audience MCP Server
  slug: infinite-audience-mcp-server
modified: '2026-10-09'
name: Infinite Audience
nav: Providers
network: true
overview: 'Infinite Audience publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, Account API, Audiences API, and 15 more. Tagged areas include Company, Identity Resolution, Data Enrichment, Audiences, and Marketing.


  The Infinite Audience catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Infinite Audience''s developer surface includes getting-started guide, authentication, documentation, API reference, and 28 more developer resources.'
plans:
- name: Infiniteaudience Ai Plans Pricing
  plan_count: 1
  slug: infiniteaudience-ai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Infiniteaudience Ai Rate Limits
  slug: infiniteaudience-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Infinite Audience API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: infiniteaudience-ai-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 71.2
    developer_ergonomics: 58.9
    discoverability: 76.7
    operational_transparency: 28.9
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/infiniteaudience-ai/refs/heads/main/screenshots/infiniteaudience-ai-2026-10-11T105924.png
security:
- kind: authentication
  name: Infiniteaudience Ai Authentication
  slug: infiniteaudience-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Infiniteaudience Ai Domain Security
  slug: infiniteaudience-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infiniteaudience-ai
tags:
- Company
- Identity Resolution
- Data Enrichment
- Audiences
- Marketing
- MCP
- A2A
website: https://infiniteaudience.ai
---
